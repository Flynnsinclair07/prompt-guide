#!/usr/bin/env python3
"""
Monthly Concur receipt-prep tool.

Takes a folder of raw receipt photos (HEIC/JPG/PNG/PDF/screenshots) and produces
clean, Concur-ready files plus a review summary, so they can be forwarded to
receipts@concur.com from a verified Concur email address.

Pipeline, per file:
  1. Convert HEIC -> JPG   (Concur accepts PNG/JPG/PDF/TIFF, NOT HEIC -- the main gotcha,
     because iPhone shoots HEIC by default).
  2. Auto-rotate via EXIF orientation; optional crop to receipt bounds.
  3. OCR vendor / date / total  (macOS Vision via a Swift helper, or pytesseract fallback).
  4. Rename  YYYY-MM-DD_Vendor_$Amount.jpg, falling back to YYYY-MM-DD_receipt_N.jpg
     when OCR can't find enough.

Outputs (under outbox/<month>/):
  - one cleaned receipt per input file
  - summary.csv          (date, vendor, amount, filename)
  - draft_email.txt      (ready-to-paste body for the forward to receipts@concur.com)

It deliberately does NOT send anything. The forward has to come from your verified
Concur email address -- this tool just preps and flags for review.

Designed to run on macOS (uses `sips`, `mdls`, and the Vision framework when present),
but degrades gracefully: anything macOS-specific is optional and falls back.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import os
import re
import shutil
import subprocess
import sys
from dataclasses import dataclass, field
from pathlib import Path

# ----------------------------------------------------------------------------
# Configuration -- override via env vars or CLI flags.
# ----------------------------------------------------------------------------
DEFAULT_INBOX = Path(os.environ.get("CONCUR_INBOX", "~/expenses/dad/inbox")).expanduser()
DEFAULT_OUTBOX = Path(os.environ.get("CONCUR_OUTBOX", "~/expenses/dad/outbox")).expanduser()
CONCUR_TO = os.environ.get("CONCUR_TO", "receipts@concur.com")

# Input formats we know how to handle.
HEIC_EXTS = {".heic", ".heif"}
RASTER_EXTS = {".jpg", ".jpeg", ".png", ".tiff", ".tif"}
PDF_EXTS = {".pdf"}
SUPPORTED_EXTS = HEIC_EXTS | RASTER_EXTS | PDF_EXTS

HERE = Path(__file__).resolve().parent
VISION_HELPER = HERE / "vision_ocr.swift"


# ----------------------------------------------------------------------------
# Result record
# ----------------------------------------------------------------------------
@dataclass
class Receipt:
    source: Path
    out_name: str = ""
    out_path: Path | None = None
    date: str = ""            # YYYY-MM-DD
    vendor: str = ""
    amount: str = ""          # e.g. "42.50" (no currency symbol)
    ocr_ok: bool = False
    notes: list[str] = field(default_factory=list)

    @property
    def amount_display(self) -> str:
        return f"${self.amount}" if self.amount else ""


# ----------------------------------------------------------------------------
# Small shell helpers
# ----------------------------------------------------------------------------
def _have(cmd: str) -> bool:
    return shutil.which(cmd) is not None


def _run(cmd: list[str], **kw) -> subprocess.CompletedProcess:
    return subprocess.run(cmd, capture_output=True, text=True, **kw)


# ----------------------------------------------------------------------------
# Step 1+2: convert + normalize an input into a single Concur-ready file.
# Returns the path of the produced file inside `dest_dir` (without final rename yet).
# ----------------------------------------------------------------------------
def normalize_file(src: Path, dest_dir: Path, *, do_crop: bool, rec: Receipt) -> Path | None:
    ext = src.suffix.lower()
    dest_dir.mkdir(parents=True, exist_ok=True)

    # PDFs are already Concur-accepted; copy through untouched.
    if ext in PDF_EXTS:
        out = dest_dir / (src.stem + ".pdf")
        shutil.copy2(src, out)
        return out

    out = dest_dir / (src.stem + ".jpg")

    if ext in HEIC_EXTS:
        if _have("sips"):
            r = _run(["sips", "-s", "format", "jpeg", str(src), "--out", str(out)])
            if r.returncode != 0 or not out.exists():
                rec.notes.append("HEIC convert via sips failed")
                if not _convert_with_pillow(src, out, rec):
                    return None
        elif not _convert_with_pillow(src, out, rec):
            rec.notes.append("no HEIC converter available (need macOS sips or pillow-heif)")
            return None
    elif ext in RASTER_EXTS:
        # Re-encode to JPG for a uniform output (PNG/TIFF -> JPG). sips keeps it lossless-ish.
        if _have("sips"):
            r = _run(["sips", "-s", "format", "jpeg", str(src), "--out", str(out)])
            if r.returncode != 0 or not out.exists():
                shutil.copy2(src, dest_dir / src.name)
                out = dest_dir / src.name
        else:
            shutil.copy2(src, dest_dir / src.name)
            out = dest_dir / src.name
    else:
        return None

    _auto_rotate(out)
    if do_crop:
        _crop_to_receipt(out, rec)
    return out


def _convert_with_pillow(src: Path, out: Path, rec: Receipt) -> bool:
    """Fallback HEIC/image conversion using Pillow (+ pillow-heif if installed)."""
    try:
        try:
            import pillow_heif  # type: ignore
            pillow_heif.register_heif_opener()
        except Exception:
            pass
        from PIL import Image, ImageOps  # type: ignore
        img = Image.open(src)
        img = ImageOps.exif_transpose(img)  # bake in rotation
        img.convert("RGB").save(out, "JPEG", quality=90)
        return True
    except Exception as e:  # pragma: no cover - depends on optional deps
        rec.notes.append(f"pillow convert failed: {e}")
        return False


def _auto_rotate(path: Path) -> None:
    """Bake EXIF orientation into pixels so Concur shows it upright."""
    if _have("sips"):
        # sips applies the rotation implied by EXIF when it rewrites the file.
        _run(["sips", "-s", "formatOptions", "high", str(path), "--out", str(path)])
        return
    try:
        from PIL import Image, ImageOps  # type: ignore
        img = ImageOps.exif_transpose(Image.open(path))
        img.save(path)
    except Exception:
        pass


def _crop_to_receipt(path: Path, rec: Receipt) -> None:
    """Optional crop to the receipt's bounding box (best-effort; needs OpenCV)."""
    try:
        import cv2  # type: ignore
        import numpy as np  # type: ignore
        img = cv2.imread(str(path))
        if img is None:
            return
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (5, 5), 0)
        edges = cv2.Canny(gray, 50, 150)
        edges = cv2.dilate(edges, None, iterations=2)
        cnts, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        if not cnts:
            return
        c = max(cnts, key=cv2.contourArea)
        if cv2.contourArea(c) < 0.25 * img.shape[0] * img.shape[1]:
            return  # don't crop if we didn't find a confident large region
        x, y, w, h = cv2.boundingRect(c)
        pad = 10
        x0, y0 = max(0, x - pad), max(0, y - pad)
        x1, y1 = min(img.shape[1], x + w + pad), min(img.shape[0], y + h + pad)
        cv2.imwrite(str(path), img[y0:y1, x0:x1])
    except Exception:
        rec.notes.append("crop skipped (OpenCV not available)")


# ----------------------------------------------------------------------------
# Step 3: OCR
# ----------------------------------------------------------------------------
def ocr_text(path: Path) -> str:
    """Return recognized text. Prefers macOS Vision; falls back to pytesseract."""
    # macOS Vision via the bundled Swift helper.
    if _have("swift") and VISION_HELPER.exists() and path.suffix.lower() != ".pdf":
        r = _run(["swift", str(VISION_HELPER), str(path)])
        if r.returncode == 0 and r.stdout.strip():
            return r.stdout
    # pytesseract fallback.
    try:
        import pytesseract  # type: ignore
        from PIL import Image  # type: ignore
        return pytesseract.image_to_string(Image.open(path))
    except Exception:
        return ""


# ----------------------------------------------------------------------------
# Parsing OCR text -> (date, vendor, amount). Pure functions; unit-testable.
# ----------------------------------------------------------------------------
_MONTHS = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "sept": 9, "oct": 10, "nov": 11, "dec": 12,
}
_AMOUNT_RE = re.compile(r"\$?\s*(\d{1,3}(?:,\d{3})*(?:\.\d{2})|\d+\.\d{2})")
_TOTAL_HINTS = ("grand total", "total due", "amount due", "balance due", "total", "amount", "balance")
_TOTAL_NEGATIVE = ("subtotal", "sub total", "tax", "tip", "change", "cash", "tender")

# Lines that look like a street address, city/state/ZIP, or phone number are NOT the
# vendor -- used to skip past them when a receipt's name line starts with a number
# (e.g. "7 ELEVEN" sits above "310 W UINTAH ST" / "COLORADO SPRINGS CO 80905").
_STREET_SUFFIX = (r"st|street|ave|avenue|blvd|rd|road|dr|drive|ln|lane|way|hwy|highway|"
                  r"ct|court|pkwy|pky|pl|plz|plaza|sq|ste|suite|unit|fl|floor")
_ADDR_RE = re.compile(rf"^\s*\d{{1,6}}\s+\w+.*\b(?:{_STREET_SUFFIX})\b\.?", re.I)
_CITYZIP_RE = re.compile(r"\b[A-Za-z]{2}\s+\d{5}(?:-?\d{4})?\b")   # "NE 68508", "CO 80905..."
_PHONE_RE = re.compile(r"\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}")


def parse_date(text: str) -> str:
    """Find the most plausible receipt date, return YYYY-MM-DD or ''."""
    # ISO first.
    m = re.search(r"\b(20\d{2})[-/.](\d{1,2})[-/.](\d{1,2})\b", text)
    if m:
        y, mo, d = map(int, m.groups())
        return _safe_date(y, mo, d)
    # US / EU numeric: MM/DD/YYYY or DD/MM/YYYY (assume US for receipts).
    m = re.search(r"\b(\d{1,2})[-/.](\d{1,2})[-/.](20\d{2}|\d{2})\b", text)
    if m:
        a, b, y = m.groups()
        y = int(y)
        if y < 100:
            y += 2000
        mo, d = int(a), int(b)
        if mo > 12 and d <= 12:  # clearly DD/MM
            mo, d = d, mo
        return _safe_date(y, mo, d)
    # "Jan 5, 2026" / "5 Jan 2026"
    m = re.search(r"\b([A-Za-z]{3,9})\.?\s+(\d{1,2}),?\s+(20\d{2})\b", text)
    if m and m.group(1)[:3].lower() in _MONTHS:
        mo = _MONTHS[m.group(1)[:3].lower()]
        return _safe_date(int(m.group(3)), mo, int(m.group(2)))
    m = re.search(r"\b(\d{1,2})\s+([A-Za-z]{3,9})\.?\s+(20\d{2})\b", text)
    if m and m.group(2)[:3].lower() in _MONTHS:
        mo = _MONTHS[m.group(2)[:3].lower()]
        return _safe_date(int(m.group(3)), mo, int(m.group(1)))
    return ""


def _safe_date(y: int, mo: int, d: int) -> str:
    try:
        return dt.date(y, mo, d).isoformat()
    except ValueError:
        return ""


def parse_amount(text: str) -> str:
    """Find the receipt total. Prefer a 'total' line; else the largest currency value."""
    lines = [ln.strip() for ln in text.splitlines() if ln.strip()]
    best = None
    for ln in lines:
        low = ln.lower()
        if any(neg in low for neg in _TOTAL_NEGATIVE) and "total" not in low.replace("subtotal", ""):
            continue
        if any(h in low for h in _TOTAL_HINTS):
            vals = [_to_float(x) for x in _AMOUNT_RE.findall(ln)]
            vals = [v for v in vals if v is not None]
            if vals:
                cand = max(vals)
                if best is None or cand >= best:
                    best = cand
    if best is None:
        all_vals = [_to_float(x) for x in _AMOUNT_RE.findall(text)]
        all_vals = [v for v in all_vals if v is not None]
        if all_vals:
            best = max(all_vals)
    return f"{best:.2f}" if best is not None else ""


def _to_float(s: str) -> float | None:
    try:
        return float(s.replace(",", "").replace("$", "").strip())
    except ValueError:
        return None


def parse_vendor(text: str) -> str:
    """Guess the vendor from the top of the receipt."""
    for ln in text.splitlines():
        s = ln.strip()
        if not s:
            continue
        letters = sum(c.isalpha() for c in s)
        digits = sum(c.isdigit() for c in s)
        if letters < 3:
            continue
        if digits > letters:        # phone numbers / amounts / mostly-numeric lines
            continue
        # Skip address / city-ZIP / phone lines. A brand may legitimately start with a
        # number ("7 ELEVEN", "5 Guys"), so we test what the line *is* rather than just
        # its first character.
        if _ADDR_RE.match(s) or _CITYZIP_RE.search(s) or _PHONE_RE.search(s):
            continue
        if any(h in s.lower() for h in ("receipt", "invoice", "order #", "www.", "http", ".com", "@")):
            continue
        return s
    return ""


def sanitize_vendor(vendor: str) -> str:
    """Make a vendor string safe + tidy for a filename."""
    v = re.sub(r"[^A-Za-z0-9 ]", "", vendor).strip()
    v = re.sub(r"\s+", " ", v)
    # Drop long numeric tokens (store/register/order numbers like 6003 or 53313) but keep
    # short ones that are part of a brand name (the "7" in 7 Eleven, the "5" in 5 Guys).
    words = [w for w in v.split() if not (w.isdigit() and len(w) >= 3)][:3]
    out = "".join(_cap_word(w) for w in words)
    return out or ""


def _cap_word(w: str) -> str:
    # Normalize SHOUTY ("STARBUCKS"->"Starbucks") but preserve intentional mixed case
    # ("UCHealth", "McDonald").
    if w.isupper() or w.islower():
        return w.capitalize()
    return w


def build_filename(rec: Receipt, fallback_index: int) -> str:
    ext = (rec.out_path.suffix if rec.out_path else ".jpg")
    if rec.date and rec.vendor and rec.amount:
        return f"{rec.date}_{sanitize_vendor(rec.vendor)}_${rec.amount}{ext}"
    date = rec.date or "0000-00-00"
    return f"{date}_receipt_{fallback_index}{ext}"


# ----------------------------------------------------------------------------
# Date fallbacks from file metadata (when OCR finds no date).
# ----------------------------------------------------------------------------
def file_date(path: Path) -> str:
    if _have("mdls"):
        r = _run(["mdls", "-raw", "-name", "kMDItemContentCreationDate", str(path)])
        out = r.stdout.strip()
        if out and out != "(null)":
            m = re.match(r"(\d{4})-(\d{2})-(\d{2})", out)
            if m:
                return "-".join(m.groups())
    try:
        ts = path.stat().st_mtime
        return dt.date.fromtimestamp(ts).isoformat()
    except Exception:
        return ""


# ----------------------------------------------------------------------------
# Outputs
# ----------------------------------------------------------------------------
def write_summary(receipts: list[Receipt], out_dir: Path) -> Path:
    path = out_dir / "summary.csv"
    with path.open("w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["date", "vendor", "amount", "filename", "ocr_ok", "notes"])
        for r in sorted(receipts, key=lambda x: (x.date or "", x.out_name)):
            w.writerow([
                r.date, r.vendor, r.amount_display, r.out_name,
                "yes" if r.ocr_ok else "no", "; ".join(r.notes),
            ])
    return path


def write_email_draft(receipts: list[Receipt], out_dir: Path, month_label: str) -> Path:
    path = out_dir / "draft_email.txt"
    prepped = [r for r in receipts if r.out_name]   # only files that actually made it out
    failed = [r for r in receipts if not r.out_name]
    total = 0.0
    for r in prepped:
        try:
            total += float(r.amount)
        except (TypeError, ValueError):
            pass
    lines = [
        f"To: {CONCUR_TO}",
        f"Subject: Receipts — {month_label}",
        "",
        f"Hi,",
        "",
        f"Attaching {len(prepped)} receipt(s) for {month_label}.",
        "",
    ]
    for r in sorted(prepped, key=lambda x: (x.date or "", x.out_name)):
        amt = r.amount_display or "(amount?)"
        vendor = r.vendor or "(vendor?)"
        date = r.date or "(date?)"
        lines.append(f"  • {date}  {vendor:<24}  {amt:>10}   {r.out_name}")
    lines += [
        "",
        f"Total: ${total:,.2f}" if total else "Total: (review amounts in summary.csv)",
        "",
        "Thanks",
        "",
    ]
    if failed:
        lines += [
            f"⚠ {len(failed)} file(s) could not be prepped and were left in the inbox — "
            "see summary.csv:",
            *[f"    - {r.source.name}: {'; '.join(r.notes)}" for r in failed],
            "",
        ]
    lines += [
        "-- ",
        "NOTE: Do NOT send from this draft directly. Concur only accepts receipts",
        "emailed from your verified Concur address. Attach the files in this folder",
        "and forward from that account.",
    ]
    path.write_text("\n".join(lines) + "\n")
    return path


def notify(count: int) -> None:
    """Post a native macOS notification to Notification Center (no third-party service)."""
    msg = f"{count} receipts prepped for dad's Concur — review outbox."
    if _have("osascript"):
        # Escape double-quotes for the AppleScript string literal.
        body = msg.replace('"', '\\"')
        script = f'display notification "{body}" with title "Concur receipt prep" sound name "Glass"'
        r = _run(["osascript", "-e", script])
        if r.returncode != 0:
            print(f"[notify] osascript failed: {r.stderr.strip()}")
    else:
        # Not on macOS — just log it (e.g. when run from a Linux host).
        print(f"[notify] {msg}")


# ----------------------------------------------------------------------------
# Driver
# ----------------------------------------------------------------------------
def discover(inbox: Path) -> list[Path]:
    files = [p for p in sorted(inbox.iterdir())
             if p.is_file() and p.suffix.lower() in SUPPORTED_EXTS]
    return files


def process(inbox: Path, outbox: Path, month_label: str, *, do_crop: bool,
            dry_run: bool) -> list[Receipt]:
    out_dir = outbox / month_label
    files = discover(inbox)
    if not files:
        print(f"[prep] nothing to process in {inbox}")
        return []

    print(f"[prep] {len(files)} file(s) -> {out_dir}")
    receipts: list[Receipt] = []
    fallback_index = 0
    used_names: set[str] = set()

    for src in files:
        rec = Receipt(source=src)
        fallback_index += 1
        if dry_run:
            rec.notes.append("dry-run: not written")
            receipts.append(rec)
            print(f"  - {src.name} (dry-run)")
            continue

        produced = normalize_file(src, out_dir, do_crop=do_crop, rec=rec)
        if produced is None:
            rec.notes.append("could not convert/normalize — left in inbox")
            receipts.append(rec)
            print(f"  ! {src.name}: skipped ({'; '.join(rec.notes)})")
            continue
        rec.out_path = produced

        text = ocr_text(produced)
        rec.date = parse_date(text)
        rec.vendor = parse_vendor(text)
        rec.amount = parse_amount(text)
        rec.ocr_ok = bool(rec.date and rec.vendor and rec.amount)
        if not rec.date:
            rec.date = file_date(src)
            if rec.date:
                rec.notes.append("date from file metadata")

        name = build_filename(rec, fallback_index)
        # Avoid collisions.
        stem, ext = os.path.splitext(name)
        n = 2
        while name in used_names or (out_dir / name).exists() and (out_dir / name) != produced:
            name = f"{stem}_{n}{ext}"
            n += 1
        used_names.add(name)

        final = out_dir / name
        if produced != final:
            produced.rename(final)
        rec.out_path = final
        rec.out_name = name
        receipts.append(rec)
        flag = "ok" if rec.ocr_ok else "fallback"
        print(f"  - {src.name} -> {name}  [{flag}]")

    if not dry_run and receipts:
        out_dir.mkdir(parents=True, exist_ok=True)
        s = write_summary(receipts, out_dir)
        e = write_email_draft(receipts, out_dir, month_label)
        print(f"[prep] wrote {s.name} and {e.name}")
    return receipts


def default_month_label(today: dt.date | None = None) -> str:
    """The month being prepped. Run on the 1st preps the month that just ended."""
    today = today or dt.date.today()
    first = today.replace(day=1)
    prev = first - dt.timedelta(days=1)
    return prev.strftime("%Y-%m")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inbox", type=Path, default=DEFAULT_INBOX)
    ap.add_argument("--outbox", type=Path, default=DEFAULT_OUTBOX)
    ap.add_argument("--month", default=None,
                    help="Output subfolder label, e.g. 2026-05 (default: previous month).")
    ap.add_argument("--crop", action="store_true", help="Attempt crop to receipt bounds (needs OpenCV).")
    ap.add_argument("--no-notify", action="store_true", help="Skip the macOS notification.")
    ap.add_argument("--dry-run", action="store_true", help="List what would happen; write nothing.")
    args = ap.parse_args(argv)

    inbox = args.inbox.expanduser()
    outbox = args.outbox.expanduser()
    month_label = args.month or default_month_label()

    if not inbox.exists():
        print(f"[prep] inbox not found: {inbox}", file=sys.stderr)
        return 1

    receipts = process(inbox, outbox, month_label, do_crop=args.crop, dry_run=args.dry_run)
    if not args.dry_run and receipts and not args.no_notify:
        notify(len([r for r in receipts if r.out_name]))
    print(f"[prep] done: {len([r for r in receipts if r.out_name])} prepped, "
          f"{len([r for r in receipts if not r.out_name])} need attention.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
