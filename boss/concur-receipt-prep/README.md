# Concur receipt-prep (for Dad)

Turn a folder of raw receipt photos into clean, **Concur-ready** files plus a
review summary, so you can forward them to `receipts@concur.com` from your
**verified Concur email address**.

It does **not** send anything. It preps and flags for your review — the forward
has to come from the email Concur knows.

## What it does, per file

1. **Convert HEIC → JPG.** Concur accepts PNG/JPG/PDF/TIFF, **not HEIC** — and
   iPhone shoots HEIC by default, so this is the #1 gotcha. Uses macOS `sips`.
2. **Auto-rotate** (bakes in EXIF orientation) + optional `--crop` to receipt bounds.
3. **OCR** vendor / date / total via macOS **Vision** (`vision_ocr.swift`), falling
   back to `pytesseract`.
4. **Rename** → `YYYY-MM-DD_Vendor_$Amount.jpg`, falling back to
   `YYYY-MM-DD_receipt_N.jpg` when OCR can't find enough.

## Output

```
~/expenses/dad/outbox/<month>/
  2026-05-12_Starbucks_$9.76.jpg
  2026-05-14_WholeFoodsMarket_$84.20.jpg
  ...
  summary.csv         # date, vendor, amount, filename, ocr_ok, notes
  draft_email.txt     # ready-to-paste body for the forward
```

`<month>` defaults to the **previous** calendar month (the job runs on the 1st to
prep the month that just closed). Override with `--month 2026-05`.

## Install the monthly job (macOS)

```bash
cd boss/concur-receipt-prep
./install.sh            # substitutes paths + loads a launchd agent
```

Runs the **1st of each month at 09:00**, processing whatever is in the inbox, and
sends an [ntfy](https://ntfy.sh) push when done:
*"X receipts prepped for dad's Concur — review outbox."*

To get the push, set a topic (pick something unguessable — anyone who knows it can
read your notifications):

```bash
# edit CONCUR_NTFY_TOPIC in ~/Library/LaunchAgents/com.user.concur-receipt-prep.plist
# subscribe on your phone via the ntfy app to the same topic, then reload:
launchctl unload ~/Library/LaunchAgents/com.user.concur-receipt-prep.plist
launchctl load   ~/Library/LaunchAgents/com.user.concur-receipt-prep.plist
launchctl start  com.user.concur-receipt-prep     # test it once now
```

Uninstall: `./install.sh --uninstall`.

## Run it by hand

```bash
./run.sh                  # prep previous month's receipts from the inbox
./run.sh --dry-run        # show what would happen, write nothing
./run.sh --month 2026-05  # specific month label
./run.sh --crop           # also try to crop to receipt bounds (needs OpenCV)
```

## Configuration

Set via env vars (the launchd plist and `install.sh` wire these up):

| Var | Default | Meaning |
|-----|---------|---------|
| `CONCUR_INBOX`       | `~/expenses/dad/inbox`  | where raw photos land (export from the shared Photos album) |
| `CONCUR_OUTBOX`      | `~/expenses/dad/outbox` | where cleaned files + summary go |
| `CONCUR_NTFY_TOPIC`  | *(empty)* | ntfy topic for the done push; empty = no push |
| `CONCUR_NTFY_SERVER` | `https://ntfy.sh` | self-host if you prefer |
| `CONCUR_TO`          | `receipts@concur.com` | address shown in the draft |

## Dependencies

**On macOS, none are required** — it uses built-in `sips`, `mdls`, `curl`, and the
Vision framework (`vision_ocr.swift` needs the Xcode Command Line Tools:
`xcode-select --install`).

Optional fallbacks (for non-Mac hosts or extras) are in `requirements.txt`:
`pillow` + `pillow-heif` (conversion), `pytesseract` (OCR), `opencv-python` (`--crop`).

## Workflow

1. Dad adds receipt photos to the shared Photos album all month.
2. You export the album into `~/expenses/dad/inbox/` (or point `CONCUR_INBOX` at it).
3. On the 1st, the job preps everything and pushes you a notification.
4. Open `outbox/<month>/`, skim `summary.csv`, fix any `ocr_ok=no` names.
5. Forward the files to `receipts@concur.com` **from your verified Concur address**,
   using `draft_email.txt` as the body.

## Tests

```bash
python3 test_prep_receipts.py
```

Covers the OCR-parsing and naming core (date/vendor/amount extraction, filename
construction, fallbacks) — no macOS tools needed.
