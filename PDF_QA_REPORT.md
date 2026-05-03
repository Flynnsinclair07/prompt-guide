# PDF Visual QA Report — job-hunters-bundle.pdf

**Build under review**: `product/build/output/job-hunters-bundle.pdf` (rebuilt at end of QA)
**Specs**: 119 pages · 514 KB · A4 · LuaTeX 1.24 · Eisvogel template · Pandoc 3.9.0.2
**Method**: rendered to 150 DPI PNGs via `pdftoppm`; sampled the first 10 pages, every 5th body page, the last 5 pages, and all section-boundary pages; cross-referenced suspect renderings against source markdown via `pdftotext`; ran text-extract grep scans for markdown artifacts and dev-process leakage.

---

## Verdict

**Ship-Ready (after this QA pass).**

Two structural blockers were found and fixed in-session — both rooted in build-process metadata leaking into the published bundle. After those fixes the document reads as one coherent product. Three should-fix items remain (cosmetic / nice-to-have); none warrant pushing the May 17 launch.

The PDF is now safe to upload to Gumroad as the launch deliverable.

---

## What was fixed in this QA pass

These are committed on `launch-prep`. Each was inside the user's "obvious and trivial" criterion (build-process artifact in source markdown that mis-rendered as part of the published TOC).

### Fix 1 — Module 5 structural cleanup *(was Blocker)*

**Symptom**: Module 5's source markdown had Scripts and Prompts interleaved. The published TOC showed:

```
Module 5 — Salary Negotiation
  Prompt 1 … Prompt 5
Scripts                                           ← H1 break
  Script 1 … Script 3
  Prompt 6 … Prompt 10                            ← prompts nested under "Scripts"
Scripts (Batch 2) — Scripts 4–8                   ← build-process artifact title
  Script 4 … Script 8
Worksheets
```

Cause: Module 5 was built in two batches (per `product/build-log.md` Apr 23 entries). Batch 1 shipped Prompts 1–5 + Scripts 1–3, then Batch 2 appended Prompts 6–10 + Scripts 4–8. The append order leaked structure into the published file.

**Fix applied** ([product/module-05-salary-negotiation.md](product/module-05-salary-negotiation.md)): pure block reorder, no content edited:
- Moved Prompts 6–10 (lines 937–1769) to immediately after Prompt 5
- Removed the `# Scripts (Batch 2) — Scripts 4–8` heading (lines 1771–1773) so Scripts 1–8 sit under one `# Scripts` H1

**Verification**: `pdftotext` of the rebuilt TOC shows the correct order — Module 5 → Prompts 1–10 → Scripts → Scripts 1–8 → Worksheets → Worksheets 1–3. `grep 'Batch [12]'` returns no matches. PDF identical size (514 KB) and page count (119), confirming content-neutrality of the move.

### Fix 2 — Module 5 dev-process metadata in body *(was Should-Fix, escalated to Blocker)*

**Symptom**: Module 5's prelude (page 67 of the bundle) opened with three lines that read like internal dev notes, not buyer-facing copy:

```
**FLAGSHIP MODULE**

**Target on completion**: 10 prompts · 8 scripts · 3 worksheets …
**This commit — Batch 1**: 5 prompts + 3 scripts (for boss QA before Batch 2)
All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o).
```

The "FLAGSHIP MODULE" / "Target on completion" / "This commit — Batch 1 (for boss QA)" lines did not match the convention every other module (1–4) uses. A buyer landing on page 67 would read those lines and think the document was a draft or pirated.

**Fix applied** ([product/module-05-salary-negotiation.md:1-4](product/module-05-salary-negotiation.md)): rewrote the prelude to match the M1–M4 convention:

```
# Module 5 — Salary Negotiation

**10 prompts · 8 scripts · 3 worksheets (BATNA · Comp research · Walkaway math)**
All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o).
```

**Verification**: `grep -E 'FLAGSHIP|Target on completion|boss QA'` on the rebuilt PDF returns no matches.

---

## Remaining issues — Should-Fix

These don't block launch but would polish the product if you have a free hour pre–May 17.

### S1 — Soft-wrap continuation arrows (↪) in many code blocks

**Where**: most prompts that contain long lines wrap with the fvextra `↪` arrow at the start of the wrap line. Examples on pages 4 (Prompt 1: "every bullet starts with a strong action ↪ verb"), 9, 25, 80, 83.

**Why it's not a blocker**: the convention is documented in fvextra; readers familiar with technical docs recognize it. The prompt is still copy-pasteable verbatim — ChatGPT ignores the arrow if you somehow include it (and you can't, since selecting the line in a PDF reader copies it without the arrow).

**Why it's still ugly**: visual noise mid-prose. A reader unfamiliar with the convention can briefly mis-parse it as a different glyph.

**Fix paths** (pick one):
1. Cheap: tighten source lines so they fit in column without wrap. Mostly affects prompts with long inline phrases. ~30 min hand-edit.
2. Medium: switch fvextra config to `breaksymbolleft={}, breaksymbolright={}` in `product/build/defaults.yaml` to suppress the arrow entirely. Risk: makes wrapped lines look continuous (arguably worse than the arrow — the reader doesn't know the line wrapped).
3. Best: increase the column width (pandoc default ~80 chars) by reducing left+right margins from 2.2cm to 1.8cm in `defaults.yaml`. Reflows everything, page count may drop slightly. Pandoc rebuild + full re-QA needed if you do this.

**Recommended**: leave as-is for v1. If buyers complain, do option 3 in v1.1.

### S2 — Title page is sparse / brand-light

**Where**: page 1.

**What it shows**: thin horizontal rule top-left, then "The Job Hunter's Bundle / 44 Prompts · 8 Negotiation Scripts · 3 Worksheets / Flynn Sinclair" — and a lot of empty black space below.

**Why it's not a blocker**: it's a clean, bookish title page. Not embarrassing, just minimal.

**Why it's still worth a fix**: there's no `snipprompts.com` reference, no tagline, no version/date. A buyer exporting a printed copy or sharing the title page screenshot has nothing to attribute back to your brand.

**Fix path**: add a one-line tagline + URL under the author name in the eisvogel `title` block. Edit the metadata in `product/build/defaults.yaml`:

```yaml
metadata:
  title: "The Job Hunter's Bundle"
  subtitle: "44 Prompts · 8 Negotiation Scripts · 3 Worksheets"
  author: "Flynn Sinclair"
  date: "May 2026 · v1.0"        # add
```

Eisvogel renders `date` on the title page. Add `snipprompts.com` either by appending to author line ("Flynn Sinclair · snipprompts.com") or in a footer-rule template variable. ~5 min + rebuild.

### S3 — No closing/handoff content at end of bundle

**Where**: page 119 (last page). The bundle ends with "End of Module 5: 10 prompts · 8 scripts · 3 worksheets. Flagship module complete."

**Why it's not a blocker**: Module 5 is the flagship and a logical-feeling end. The buyer doesn't drop off a cliff — they hit a clear "done" signal.

**Why it's still worth a fix**: the outline (`product/job-hunter-bundle-outline.md` §3) called for a "quick reference card (1-page index)" as net-new content. It was never written. The bundle would feel more finished with one of:
- A 1-page quick-reference index (every prompt + the page it lives on)
- A closing "Next steps" page (use the prompts in this order; reply with feedback)
- A 1-page "What's coming in v1.1" pre-commitment

**Recommended**: write the quick-reference index. ~45 min. Adds 1 page (would push to 120). Buyer perceived value goes up disproportionately.

---

## Remaining issues — Nice-to-have

Items I noticed but wouldn't action even with unlimited time. Logged so they don't surprise you later.

### N1 — A4 paper size vs. US Letter
Already flagged in [LAUNCH_PUNCHLIST.md](LAUNCH_PUNCHLIST.md) Q3. The current build is A4 (LuaTeX default). For a digital-first product, A4 is fine — most buyers read on screen. Switching to Letter is a one-line change in `defaults.yaml` (`papersize: letter`) and a full rebuild + re-QA. Defer to v1.1.

### N2 — `oneside` + report class causes mid-page section starts
Modules 2–5 each begin mid-page (after the previous module's trailing content). This is the deliberate trade-off documented in `product/build/defaults.yaml:18-23` to avoid 25 blank verso pages with the `book` class. Reads slightly less ceremonial than a "module starts on a new page" book — but the alternative is a much longer, gappier document. Keep as-is.

### N3 — Title-page horizontal rule extends to right margin
The thin rule above the title is set by Eisvogel to span `\textwidth`, which is the column width (not page width), so it appears to "end" at the right text margin rather than the page edge. Looks slightly unbalanced against the otherwise centered title block. Cosmetic only. Eisvogel template edit if you ever care.

### N4 — No version/changelog page
Outline §3 mentioned an "Updates log" as part of the bundle's promise (12 months of updates). Nowhere in the published PDF is there a "v1.0 — May 2026" mark or a place where future updates will appear. Add when you ship v1.1; not needed at launch.

### N5 — No license / TOU page
The bundle has no language about whether buyers can share it, print it, or quote it. Standard infoproduct convention is one paragraph: "single user, do not redistribute, all rights reserved." Add if you care; many creators don't bother for v1.

---

## Page-by-page issue table

Every issue I logged, by page number. Severity: **B**locker (fixed in this pass), **S**hould-fix, **N**ice-to-have. Source-markdown file/line cited where the fix lands.

| Page | Severity | Issue | Source |
|---:|:---:|---|---|
| 1 | S2 | Title page sparse; no tagline / URL / version | `product/build/defaults.yaml:76-82` (metadata block) |
| 1 | N3 | Title rule appears short of right page edge | Eisvogel template internal |
| 2–3 | B (fixed) | TOC showed "Scripts" containing 5 prompts + "Scripts (Batch 2) — Scripts 4–8" | `product/module-05-salary-negotiation.md:733, 1771` (both removed/restructured) |
| 4, 9, 25, 60, 80, 83, 100 | S1 | Code blocks soft-wrap with `↪` continuation arrows mid-prose | `product/build/defaults.yaml:60-62` (fvextra config) or all module markdown (line tightening) |
| 18 | — | (no issue) bold rendering verified inside body prose; pdftotext confirms no literal `**` leakage | — |
| 67 | B (fixed) | Module 5 prelude had FLAGSHIP / Target on completion / boss QA dev metadata | `product/module-05-salary-negotiation.md:1-7` (rewritten to match M1–M4 convention) |
| 81–101 | B (fixed) | Module 5 prompts 6–10 nested under "Scripts" H1; "Scripts (Batch 2)" header at p.102 | `product/module-05-salary-negotiation.md:937-1773` (block reordered) |
| 119 | S3 | Bundle ends abruptly with Module 5 end-marker; no quick-reference card / closing handoff | new content needed (referenced in `product/job-hunter-bundle-outline.md:78`) |
| — | N1 | A4 instead of US Letter | `product/build/defaults.yaml` (add `papersize: letter` under variables) |
| — | N2 | Module sections begin mid-page (deliberate) | `product/build/defaults.yaml:18-23` (architectural choice, not a bug) |
| — | N4 | No "v1.0 / May 2026" version marker anywhere | `product/build/defaults.yaml` metadata or new welcome page |
| — | N5 | No license / terms-of-use language | new page or Gumroad listing description |

---

## What I checked that came back clean

These are the dimensions the brief asked me to inspect; logging the negatives so you know they were verified, not skipped.

- **Page count**: 119, matches `pdfinfo`. No blank pages (smallest non-title page = 162 KB; all body pages between 161–414 KB, consistent with content density).
- **Duplicate pages**: none. PNG byte-size distribution has no near-duplicates.
- **Page numbering**: footer numbers run consistently 1–118 (title page is unnumbered, "1" starts on TOC page 1). TOC entries match rendered page numbers throughout (verified Module 1: p.3, Module 2: p.18, Module 3: p.30, Module 4: p.50, Module 5: p.67, Scripts: p.98, Worksheets: p.112 — all correct after the restructure).
- **Markdown bold (`**foo**`) in body prose**: renders correctly as bold typography. The pdftotext extraction shows no literal asterisks in body text. (Asterisks DO appear inside code-block prompts — that's intentional; those `**foo**` markers are part of the prompt syntax that ChatGPT will render as bold in its response.)
- **Headers**: H1/H2 hierarchy is consistent. No orphaned headings on sampled pages (heading-at-bottom-with-content-on-next-page).
- **Em/en dashes**: render correctly. The previous QA fix (commit `ccf3282`) for en-dash corruption near digits ("2–3") is holding — verified at multiple sample points.
- **Emoji glyphs (🟢🟡🟠🔴)**: render via Apple Color Emoji fallback (commit `a3e1406`). Verified visually on a Module 3 P12 sample page.
- **Code-block right-margin overflow**: held; no overflows seen in samples (commit `86c8731`).
- **External URLs**: every URL I sampled (snipprompts.com mentions, levels.fyi, glassdoor, reddit references in source) renders as plain text — pandoc didn't auto-link them, which is fine for a print-style PDF and avoids the "broken link in 6 months" failure mode.
- **Internal cross-references**: bundle has minimal internal cross-refs (the outline noted "no cross-links to snipprompts.com from inside prompts"). The few "see Module X" mentions in the body are plain text, not links — appropriate.
- **Worksheets layout**: pages 112–119 render the BATNA / comp research / walkaway-math worksheets with checkbox-style `[  ]` placeholders intact. No table corruption.
- **Author metadata**: `Flynn Sinclair` set correctly in PDF metadata (`pdfinfo` confirms).

---

## Build commands used (reproducibility)

```bash
# Render
cd /private/tmp/prompt-guide/.claude/worktrees/affectionate-elgamal-b8c3fa/product/build
./build.sh full

# Convert to PNGs at 150 DPI
mkdir -p /tmp/pdf-qa-pages
cd /tmp/pdf-qa-pages
pdftoppm -r 150 -png \
  /private/tmp/prompt-guide/.claude/worktrees/affectionate-elgamal-b8c3fa/product/build/output/job-hunters-bundle.pdf \
  page

# Verify clean of dev artifacts
PDF=…/job-hunters-bundle.pdf
pdftotext "$PDF" - | grep -nE 'Batch [12]|FLAGSHIP|Target on completion|boss QA'   # should return nothing
```

If you ever need to re-run the QA, the page-by-page PNGs in `/tmp/pdf-qa-pages-v3/` (the post-fix render) are still around.

---

## Pre-launch reminders that touch this file

- The output PDF is what gets uploaded to Gumroad as the deliverable (per [GUMROAD_LISTING.md](GUMROAD_LISTING.md) Field 8). The committed source markdown changes mean **the next time you run `./build.sh full` you'll get the cleaned-up file** — but the PDF in `product/build/output/` is gitignored, so the version that ships is whichever was built last on your machine. Rebuild once before uploading to Gumroad on May 5–6.
- The bundle text says "119-page PDF" in [GUMROAD_LISTING.md](GUMROAD_LISTING.md) and [EMAIL_SEQUENCE.md](EMAIL_SEQUENCE.md). Page count is unchanged at 119 after the fixes. No copy update needed.
- The [DELIVERY_EMAIL.md](DELIVERY_EMAIL.md) "what you just bought" recap accurately reflects the new structure. No copy update needed.
