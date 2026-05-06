# Cross-reference verification pass — May 6, 2026

**Trigger**: pre-walkthrough audit, ~11 days before launch.
**Method**: recursive grep across all `.md` files in repo root, `product/launch/`, `notion/`. No edits — observation-only report. Owner triages and decides.

**Files scanned** (19):
- Repo root: BUYER_READ_NOTES_2026-05-03.md, DELIVERY_EMAIL.md, EDIT_LOG.md, EMAIL_SEQUENCE.md, GUMROAD_LISTING.md, LAUNCH_PUNCHLIST.md, PDF_QA_REPORT.md, PINTEREST_PINS.md, v1.1-quick-actions.md
- `product/launch/`: day-1-launch-checklist.md, sprint-plan-may-4-17.md, support-templates.md
- `notion/`: 00-START_HERE.md, 01-prompt-library.md, 02-templates.md, 03-job-tracker.md, 04-progress-checklist.md, 05-changelog.md, IMPORT_GUIDE.md

---

## Summary

- ✅ **5 categories pass clean** (no inconsistencies): page count, refund window, discount code casing, discount amounts, bundle name + apostrophe.
- ⚠️ **5 categories have minor inconsistencies** (none buyer-blocking): launch date format, Notion URL example, updates-language wording variants, email send-time format, one stale editor's note.
- 🔴 **0 major issues**. No buyer-facing falsehoods, no contradictions that would confuse a buyer.
- ⚠️ **1 meta-issue** outside Tom's scan scope but discovered during this session: working tree has 130+ files missing relative to `main`. Repo recovery needed (separate from this verification report). See "Out-of-scope flag" at the bottom.

---

## ✅ Categories that passed (no inconsistencies)

### Page count — "119"
All buyer-facing references say "119-page" or "119 pages":
- `GUMROAD_LISTING.md` Field 5: "a 119-page PDF"
- `EMAIL_SEQUENCE.md` Email 3: "a single 119-page PDF" + Email 4 "119-page polished PDF"
- `PINTEREST_PINS.md` Pin 15 + Pin 25: "119-page PDF + Notion"
- `notion/05-changelog.md`: "119-page PDF (hyperlinked TOC, code-styled prompt callouts)"

"141" only survives in historical editor's-note documentation (`EDIT_LOG.md` lines 23–24, `GUMROAD_LISTING.md` line 285) — describing the original-then-corrected claim. Not buyer-facing.

### Refund window — "30-day"
All buyer-facing copy uses "30-day" or "30 days":
- `GUMROAD_LISTING.md` Field 13 + FAQ Q8: "30 days, no questions"
- `EMAIL_SEQUENCE.md` Email 3 + Email 4 + Email 5: "30-day no-questions refund" / "Same 30-day refund" / "Refund policy: 30 days, no questions, Gumroad handles it"
- `PINTEREST_PINS.md` Pins 15, 19, 20, 21, 22, 23, 24, 25: all "30-day refund"
- `notion/05-changelog.md`: "30-day no-questions refund window via Gumroad"

"14 days" only appears in:
- `LAUNCH_PUNCHLIST.md` line 74, 130: "next 14 days" (calendar window between merge and launch — different domain, not refund)
- Historical editor's notes in `GUMROAD_LISTING.md` line 319 + 325 documenting the 14→30 change
- `notion/01-prompt-library.md` lines 577, 594: "7–14 days" interview-follow-up timing — completely different domain

### Discount code — `LAUNCH` casing
Always uppercase as a code, always backticked when referencing the code itself. Lowercase "launch" only appears in:
- File path prefixes (`product/launch/...`)
- The word "launch" in narrative prose (e.g., "launch day", "launch eve", "launch-prep")
- Pinterest pin headlines like "Launch teaser:" (capital L is start-of-phrase)

No instances of `launch` (lowercase) being used to reference the discount code.

### Discount amounts — $29 / $39 / $10 off
- `$29` appears 31× across files; always paired with launch context
- `$39` appears 35× across files; always paired with regular-price context
- `$10 off` appears 6× across `EMAIL_SEQUENCE.md` + `GUMROAD_LISTING.md` + `day-1-launch-checklist.md`; always describes the discount mechanic
- Other prices ($59, $89) appear only in `GUMROAD_LISTING.md`'s Tier 2/3 upsell architecture section — Q3 future products, not v1 launch claims. Expected.

`DELIVERY_EMAIL.md` mentions `$29`/`$39` only inside a voice-note paragraph that explains why the body deliberately doesn't mention price. Not a regression — meta-commentary on the convention itself.

### Bundle name + apostrophe — "The Job Hunter's AI Bundle"
Appears exactly as canonical across 23+ instances in 6 files. No variations found:
- No "The Job Hunters AI Bundle" (no apostrophe)
- No "the Job Hunter's AI bundle" (lowercase 'B' / 't')
- No "JobHunter" / "Job-Hunter" formatted differently
- The deliverable filename `job-hunters-bundle.pdf` and URL slug `job-hunters-ai-bundle` correctly use the apostrophe-less plural-possessive form for filesystem/URL safety; product name uses the apostrophe form. Both are valid registers of the same name; not an inconsistency.

### Bonus check — ConvertKit form UID + buyer tag
- ConvertKit form UID `d02eb77674` consistent across all references (4 files)
- `bundle-buyer-2026-may` tag consistent across 13 references in 5 files

---

## ⚠️ Categories with minor inconsistencies

None buyer-blocking. Each has a suggested fix; none are required before launch.

### M1 — Launch date format mix: "May 17" vs. "May 17, 2026"

**Pattern**: roughly 35× "May 17" (informal, year implied by surrounding date language); roughly 4× "May 17, 2026" (formal, year explicit).

**Examples**:
- Formal: `LAUNCH_PUNCHLIST.md` line 1 ("Launch Punchlist — Job Hunter's AI Bundle (May 17, 2026)"), `EDIT_LOG.md` line 111
- Informal: dozens of "May 17 launch" / "live tomorrow at 9 AM ET" / "May 17 9 AM ET" references across `EMAIL_SEQUENCE.md`, `PINTEREST_PINS.md`, `GUMROAD_LISTING.md`

**Buyer impact**: zero. The launch is in 11 days; year is unambiguous from context.

**Suggested fix** (if owner wants strict consistency): use "May 17, 2026" only in document headers / titles / file metadata where the date stands alone; use "May 17" in narrative prose where surrounding "tomorrow" / "Sunday" / "this week" makes year obvious. Current usage roughly matches this convention already; one-pass tightening optional.

### M2 — Notion URL example in IMPORT_GUIDE.md doesn't match the actual URL

**Location**: `notion/IMPORT_GUIDE.md` line 127 has an example URL:
```
https://flynnsinclair.notion.site/The-Job-Hunters-AI-Bundle-XXXXXXXX
```

**Actual live URL** (in `DELIVERY_EMAIL.md` body + `support-templates.md` Template 2):
```
https://learned-guilty-545.notion.site/The-Job-Hunter-s-AI-Bundle-35634cf5abb9800babe5c22b28888ccf
```

**Mismatches**:
1. Subdomain: `flynnsinclair` vs. `learned-guilty-545`
2. Path slug: `Hunters` (no apostrophe) vs. `Hunter-s` (apostrophe encoded)
3. ID: `XXXXXXXX` placeholder vs. real 32-char ID

**Buyer impact**: zero — IMPORT_GUIDE.md is owner-facing, not buyer-facing. But a future-owner re-reading this guide post-launch might think the actual URL pattern is the example pattern, and fail to find the live workspace.

**Suggested fix**: replace the example URL block in IMPORT_GUIDE.md with the actual live URL (and a sentence clarifying that future workspaces would generate their own subdomain/ID). One-line edit.

### M3 — Updates-language wording variants

**Pattern**: same idea ("free updates pushed to your Gumroad library, no re-download") expressed in 4 different phrasings:

| File | Phrasing |
|---|---|
| `DELIVERY_EMAIL.md` line 165 | "Free updates pushed to your Gumroad library — no re-download needed." |
| `EMAIL_SEQUENCE.md` line 247 | "Free updates pushed to your Gumroad library — no re-download needed. 30-day no-questions refund." |
| `GUMROAD_LISTING.md` line 132 (FAQ Q6) | "Any updates I publish appear automatically in your Gumroad library. No re-download needed. The Notion workspace updates live." |
| `PINTEREST_PINS.md` Pin 15 + Pin 25 | "Free updates, no re-download" / "free updates with no re-download" |
| `notion/05-changelog.md` lines 3 + 17 | "Free updates pushed to your Gumroad library — no re-download needed" |

**Buyer impact**: minimal. All variants communicate the same value claim; a buyer reading multiple surfaces won't perceive a contradiction.

**Suggested fix** (if owner wants tighter): pick one canonical sentence and propagate. Recommend the GUMROAD_LISTING.md FAQ Q6 version as canonical (most complete, includes the Notion update mechanic). Pinterest pin character constraints justify the shortened "Free updates, no re-download" — keep as-is, don't try to cram the full sentence into a 4-word benefit line.

### M4 — Email send-time format: "9 AM ET" vs. "9 AM Eastern"

**Pattern**: most references say "9 AM ET" (compact, professional). Two body references in `EMAIL_SEQUENCE.md` use "9 AM Eastern" (long form):
- Email 3 body line 188: "Tomorrow at 9 AM Eastern, I'll send the link with your $29 launch price built in."
- Email 4 body line 235: "Tuesday May 19 at 9 AM Eastern, the price reverts to $39 and the code goes off."

Plus one Email 3 body reference at line 159: "goes live tomorrow morning at 9 AM Eastern."

**Buyer impact**: zero. Both formats unambiguous.

**Suggested fix** (if owner wants strictness): unify to "9 AM ET" everywhere, or accept the deliberate variation (long-form "Eastern" reads warmer in flowing prose; compact "ET" reads tight in tables/checklists). Current usage looks like a deliberate stylistic split, not a bug.

### M5 — Stale editor's note in GUMROAD_LISTING.md line 332

**Location**: `GUMROAD_LISTING.md` line 332, inside the `<!-- Tom-QA pass —- May 3, 2026 -->` editor's note HTML comment block.

**Issue**: the note says:
> ...the parallel "12 months of free updates" claim still appears in DELIVERY_EMAIL.md P.S., EMAIL_SEQUENCE.md Email 4, PINTEREST_PINS.md Pin 15 — same falsifiability concern, surfacing those for Tom's call when each file comes up in QA.

But those parallel claims have since been softened (commit `ffcbfd6` on May 3 + `33efbc4` on May 4). The "still appears in" sentence is now historically inaccurate — they no longer appear.

**Buyer impact**: zero. HTML comments don't render on the Gumroad listing.

**Suggested fix**: rewrite the sentence to past tense ("originally appeared in [files] — subsequently softened in commit ffcbfd6") OR drop the sentence entirely. Either way, no buyer-facing change. Low priority; could batch with any future GUMROAD_LISTING.md touch.

This was already flagged in my May 4 verification pass and acknowledged by Tom as deferred. Re-flagging for completeness.

---

## 🔴 Major issues — none

No falsehoods. No contradictions. No buyer-facing claims that would generate refund requests or trust loss.

---

## Out-of-scope flag — repo working-tree damage

**Not part of Tom's scan request, but discovered during this session and material**:

When `.git/HEAD` was restored at session start, `git status` revealed 130+ files showing as `deleted` relative to `main`:
- All 134 `prompts/*.html` files
- All 8 `scripts/*.py` files
- All 5 `pins/*.png` + `pins/generate_pins.py`
- `research/`, `templates/`, `tracking/` directory contents
- Top-level `README.md`, `CNAME`, `llms.txt`, `package.json`, `robots.txt`
- `product/build-log.md`, `product/job-hunter-bundle-outline.md`, `product/module-02-cover-letter.md`, `product/module-04-linkedin.md`, `product/week3-polish.md`, `product/build/build.sh`, `product/build/.gitignore`

The files exist in `main` (commit `e631ecc`, fully pushed to origin), so they're recoverable via `git restore .` — but per global rules I cannot run destructive git commands without explicit owner permission. The unstaged deletions did NOT enter the 3 commits I made today (used targeted `git add <path>` for each file).

**Recovery on owner's review**: `git restore .` from repo root will pull the missing files back from `HEAD`. Working tree will then match `main` again. Untracked `.DS_Store` files and `product/build/output/` (gitignored build artifact dir) are not affected.

**Today's 3 commits are clean** (no deletions staged). They can be pushed independently of the recovery; recovery and push are independent operations.

---

## Verification commands run (reproducibility)

```bash
cd /private/tmp/prompt-guide

# Page count
grep -rnE '\b119[ -]?page' --include='*.md' .
grep -rnE '\b141\b' --include='*.md' .

# Refund window
grep -rnE '\b30[- ]days?( refund| no-questions| window)' --include='*.md' .
grep -rnE '\b14[- ]days?( refund| no-questions| window)' --include='*.md' .

# Discount code
grep -rnE '\bLAUNCH\b' --include='*.md' .

# Prices
grep -rnE '\$10[ -]off' --include='*.md' .
grep -cE '\$29\b' *.md product/launch/*.md notion/*.md
grep -cE '\$39\b' *.md product/launch/*.md notion/*.md

# Launch date
grep -rnE 'May 17(, 2026)?' --include='*.md' .

# Notion URL
grep -rnE 'NOTION_DUPLICATION_URL|learned-guilty-545|notion\.site|notion\.so' --include='*.md' .

# Bundle name
grep -rcE "The Job Hunter's AI Bundle" --include='*.md' .
grep -rnE "Job Hunter[s]" --include='*.md' . | grep -vE "Hunter's"

# Updates language
grep -rnE 'free updates|12 months' --include='*.md' .

# Bonus
grep -rnE 'd02eb77674|bundle-buyer-' --include='*.md' .
grep -rnE '9 ?(AM|am) ?(ET|Eastern)' --include='*.md' .
```

All output reviewed manually; categorized findings above.
