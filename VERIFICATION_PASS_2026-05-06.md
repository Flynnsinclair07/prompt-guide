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

---

## Post-Batch-3 Self-QA Pass

**Date appended**: 2026-05-06 (later same day, after Batch 3 commits land)
**Scope**: re-audit of all 9 deliverables shipped across the 3 dispatch batches, against `brand-voice.md` (the new canonical voice authority created in Task 8) and the factual claims established in the May 6 verification pass above.

**Method**: per-file grep checks for factual accuracy (page count, refund window, launch date, discount code casing, prices), banned-phrase scans against the brand-voice.md banned list, cross-reference resolution checks, completeness checks against Tom's per-task spec.

**Verdict summary**: 9 deliverables shipped; **all 9 pass factual / voice / completeness checks**. Three minor cross-file issues found (none refund-risk; none would block launch). The most material item is the onboarding-flow-audit's NEW finding 1a (download-button refund-risk under Option B delivery) which is documented in the audit but not yet folded into v1.1-backlog.md — surfaced for owner triage.

---

### ✅ Files that passed all checks

| # | File | Lines | Commit | Pass notes |
|---|---|---:|---|---|
| 1 | `product/launch/day-1-launch-checklist.md` | 270 | `04414c2` | 29 numbered action items across 7 windows. Tom's 4-part spec met (what / where / success / fail-recovery). All cross-references resolve. |
| 2 | `PINTEREST_PINS.md` (Pins 16–25 only) | +399 | `6df2999` | 10 new pins added; existing Pins 6–15 untouched (verified). All spec constraints met (headlines ≤8 words, alt text <100 chars, descriptions 200–400 chars). Voice consistent with Pins 6–15. |
| 3 | `VERIFICATION_PASS_2026-05-06.md` (original sections) | 221 | `8b68172` | 8 categories scanned; 5 ✅ / 5 ⚠️ / 0 🔴. The doc you're reading. |
| 4 | `product/launch/post-launch-week-1-plan.md` | 374 | `18b243e` | All 7 days (May 18–24) covered with morning/afternoon/evening blocks. Time budgets, success criteria, gate-check matrix all present. |
| 5 | `product/launch/v1.1-backlog.md` | 368 | `78adca0` | Tom's 4 priority levels (🔴/🟠/🟡/⚪) + Pre-launch owner actions + Resolved-before-v1.0 table. 30+ items consolidated. |
| 6 | `product/launch/onboarding-flow-audit.md` | 265 | `d436579` | All 5 buyer-journey steps documented + cross-step audit findings + summary table. |
| 7 | `product/launch/test-purchase-debugging.md` | 208 | `b9796ac` | All 8 failure modes covered with symptom / cause / fix / severity. Pre-walkthrough checklist included. |
| 8 | `product/launch/brand-voice.md` | 332 | `bbff7fc` | Tom's 7 spec sections + 3 bonus (specific-numbers rule, surface-specific rules, voice-tics-to-track). 35+ proper-noun lookup table. Source attribution per rule. |
| 9 | `.gitignore` (Task 9 update) | +21 | `125f7b6` | macOS noise patterns added; verified `git check-ignore` matches all 3 .DS_Store files + `product/build/output/`. No `git rm --cached` needed (none were tracked). |

### Factual accuracy checks (all green)

| Fact | Canonical | Status across 9 deliverables |
|---|---|---|
| Page count | 119 | ✅ all "119" or "119-page". "141" only appears in historical/debugging context (resolved-items table, "what NOT to see if file is wrong version") |
| Refund window | 30-day | ✅ all "30-day" / "30 days". "14-day" only in resolved-items table |
| Launch date | May 17 (year implied or explicit) | ✅ consistent across 41 references |
| Discount code | `LAUNCH` (uppercase, often backticked) | ✅ no lowercase usage as code reference |
| Prices | $29 launch / $39 list | ✅ only these two prices appear; other $-figures are domain-specific (e.g., "$120K offers", "$15–30/mo Rezi") |
| Bundle name | "The Job Hunter's AI Bundle" | ✅ exact casing + apostrophe consistent |

### Voice rule compliance (against brand-voice.md banned-phrase list)

Banned phrases (`exclusive`, `amazing`, `game-changing`, `incredible`, `unleash`, `unlock your potential`, `Hi friend,`, `Dear subscriber,`, `Thank you for your purchase!`) appear in `brand-voice.md` itself — but only as documentation of the rules (the file lists them as banned). Zero occurrences in the other 8 deliverables.

Other voice checks: lowercase `hey,` opener appears only where it should (the operational docs are reference material, not personal letters). Properly cased proper nouns (ChatGPT, LinkedIn, Notion, Gumroad, BATNA, etc.) — verified consistent across all 9 deliverables. Sign-off conventions (`— Flynn`) — applied where appropriate (this is an operational batch, not a buyer-facing batch, so sign-offs are minimal).

---

### ⚠️ Minor issues found

#### W1 — 3 referenced files don't exist on disk
The operational docs reference files that don't currently exist:

| Referenced file | Referenced from | Status | Action |
|---|---|---|---|
| `tracking/daily-metrics-template.csv` | day-1-launch-checklist + post-launch-week-1-plan + test-purchase-debugging | In the 130+ deleted-files set from prior session damage | **Resolves automatically** when owner runs `git restore .` to recover the working tree |
| `product/launch/refund-log-2026-05.md` | post-launch-week-1-plan + test-purchase-debugging | Designed to auto-create on first refund (not a missing file — a future file) | **Not a bug** — both referencing docs explicitly say "create on first refund" |
| `product/post-launch-roadmap.md` | post-launch-week-1-plan May 24 gate-check section (only as alternative location) | Optional / contingent — only created if YouTube gate fires | **Not a bug** — explicitly conditional |

**Severity**: 🟡 cosmetic. The first item resolves on owner's `git restore .`; the other two are intentionally future/contingent files.

#### W2 — Onboarding-flow-audit's NEW findings not folded into v1.1-backlog
`product/launch/onboarding-flow-audit.md` (commit `d436579`) surfaced 3 items that the audit explicitly recommended adding to v1.1-backlog.md:
- **Finding 1a (🔴 refund-risk)**: download-button reference assumes Option A, breaks under Option B — most material new gap from the entire batch
- **NTH17 proposal**: Notion duplication URL buried mid-bullet in receipt email
- **SF12 proposal**: no Day-2 post-purchase check-in email (no nurture sequence beyond receipt)

`v1.1-backlog.md` was committed in `78adca0` BEFORE the audit found these. The audit explicitly chose "audit only, owner triages" (no edits to source files), which is correct behavior — but means owner needs to manually triage these 3 items into the backlog when reviewing.

**Severity**: ⚠️ quality-improvement. Surfaced clearly here so owner doesn't miss it in triage.

#### W3 — VERIFICATION_PASS_2026-05-06.md M2 finding still active (Notion URL example mismatch in IMPORT_GUIDE.md)
The May-6 morning verification pass flagged that `notion/IMPORT_GUIDE.md` line 127 has an example URL pattern that differs from the actual live URL. Tracked as v1.1-backlog NTH13. Not actioned in Batch 3 (out of scope per Tom's locked-files rule on `IMPORT_GUIDE.md`-adjacent edits).

**Severity**: 🟡 nice-to-have. Owner-facing only (buyers don't see IMPORT_GUIDE.md). Tracked.

---

### 🔴 Major issues found

**None**. No factual contradictions across the 9 deliverables. No banned-phrase violations. No refund-risk gaps in the operational docs themselves (refund-risk in onboarding-flow-audit's finding 1a is documented + flagged in W2 above).

---

### 🔧 Cross-file issues

#### X1 — Audit-to-backlog handoff requires owner triage (W2 above, restated as cross-file)
The onboarding-flow-audit and v1.1-backlog were written in the same batch but in sequence — backlog first, then audit. Audit recommendations propose 3 backlog additions but don't apply them. Owner needs to:
1. Read onboarding-flow-audit's "Recommended actions" → "v1.1" section
2. Manually add NTH17 + SF12 entries to v1.1-backlog.md
3. Decide pre-launch on finding 1a (Option A vs. B receipt-email decision)

Without this triage step, the 3 items risk falling through the cracks.

#### X2 — Pre-launch owner action O1 (Notion re-sync) is the only true blocker
Of all the items flagged across the 9 deliverables, only **O1 — Live Notion workspace re-sync** is a true pre-launch blocker (5 min owner action). Everything else is either ship-ready, post-launch, or v1.1.

Source: `v1.1-backlog.md` Pre-launch owner actions section + `onboarding-flow-audit.md` finding 4a + `v1.1-quick-actions.md`.

**Recommendation**: owner does O1 before May 17. ~5 min. If it slips, the 12-month-vs-no-time-commitment contradiction between the receipt email and the live Notion workspace is real and visible to early buyers.

#### X3 — Option A vs Option B receipt-email decision is unforced but consequential
`DELIVERY_EMAIL.md` documents both Option A (Gumroad receipt) and Option B (ConvertKit Sequence). Owner hasn't picked. The onboarding-flow-audit's finding 1a (download-button reference) makes this decision a soft pre-launch deadline:

- If owner picks Option A: receipt email body is correct as-written. ~0 min remediation.
- If owner picks Option B: receipt email body's "the download button at the bottom of this email" sentence becomes false, requires editing to reference the Gumroad library URL. ~5 min remediation.

`test-purchase-debugging.md` failure mode 2 also touches on this (Option B silent failure scenario).

**Recommendation**: owner picks A or B before the May 9 walkthrough so the test purchase exercises the actual delivery path. Email-body edit (if B) takes 5 min once decided.

---

### Outstanding owner actions (consolidated, in priority order)

These are the actions blocking or improving v1.0 launch. Pre-launch (May 17) blockers are 🔴; post-launch v1.1 work is 🟠/🟡.

| Priority | Action | Source | Time |
|---|---|---|---|
| 🔴 pre-launch | `git restore .` to recover the 130+ unstaged deletions in working tree | VERIFICATION_PASS Out-of-scope flag | 30 sec |
| 🔴 pre-launch | Pick Option A vs Option B for receipt-email delivery; if B, edit body's download-button sentence | onboarding-flow-audit finding 1a + test-purchase-debugging FM2 | 5 min |
| 🔴 pre-launch | Live Notion workspace re-sync (hand-edit `00-START_HERE.md` + `05-changelog.md` in published Notion OR re-import) | v1.1-backlog O1 + v1.1-quick-actions.md | 5 min |
| 🔴 pre-launch | Verify Stripe Connect status: Active (not Pending) | test-purchase-debugging FM1 | 30 sec verify |
| 🟠 pre-launch | Verify Gumroad storefront subdomain matches the placeholder used in copy (`snipprompts.gumroad.com`) | v1.1-backlog O2 | 30 sec |
| 🟠 pre-launch | Verify ConvertKit form endpoint accepts the homepage form POST (test signup) | v1.1-backlog O3 | 30 sec |
| 🟠 pre-launch | Manually add NTH17 + SF12 to v1.1-backlog.md per onboarding audit's recommendations | onboarding-flow-audit Recommended actions | 5 min |
| 🟡 post-launch | Push the 10 unpushed commits when ready | All 3 batches | 10 sec |
| 🟡 post-launch | Triage v1.1-backlog priorities; pick which items ship in v1.1 cycle | v1.1-backlog Suggested sequencing | 30 min review |

**Total pre-launch owner-time**: ~15 minutes of focused account-credentialed work, plus the May 9 + May 14 walkthroughs already scheduled.

---

### Concerns / things I'd flag if I were the QA reviewer signing off

1. **Repo working-tree damage is still unresolved**. 130+ files missing from disk; recoverable via `git restore .`; not run autonomously per global rules. This has persisted across 3 dispatch batches. If owner doesn't run `git restore .` before launch day, several launch-day operations will fail (e.g., `./build.sh full` to rebuild PDF won't work — `product/build/build.sh` is in the deleted set). **Owner MUST run `git restore .` on review.**

2. **The Option A vs B decision is the riskiest unforced error in the launch**. If owner doesn't decide and just defaults to Option A by inertia, fine. If owner sets up Option B without remembering to edit the receipt body, buyers hit the broken download-button reference and refund risk surfaces. The fix is 5 minutes; the risk if missed is real.

3. **No real buyer has tested any of this**. Every QA pass to date — this one included — is structural-read-of-artifacts, not a real $39 buyer's lived experience. The May 9 + May 14 walkthroughs are the closest we have. The onboarding-flow-audit explicitly documents this limit.

4. **Batch 3 went smoothly because the editorial discipline established in earlier batches held**. Voice consistency, factual accuracy, cross-file references — all clean across 10 commits and ~3,000 lines of new operational docs. The brand-voice.md doc that landed today crystallizes that discipline for v1.1+ work.

5. **The 9 deliverables are useful in isolation AND as a system**. day-1-launch-checklist references support-templates; post-launch-week-1-plan references v1.1-backlog; test-purchase-debugging references day-1-checklist + post-launch-plan; brand-voice references all 5 source files. The cross-references resolve correctly. Owner can read any one file and find what they need; can also follow the chain to context.

**Overall recommendation**: ship the 10 commits to remote. Run `git restore .` to recover working tree. Decide Option A vs B. Do the 5-minute Notion re-sync. Then walkthroughs May 9 + May 14 should run clean against this complete operational framework.

---

End of Post-Batch-3 Self-QA Pass.
