# Buyer-Perspective Read — Worker Notes

**Date**: 2026-05-03 (late night, post-PDF cleanup)
**Read by**: Worker (with caveat: brings 3-week production fatigue, not a real $39 buyer's eye — but applied Tom's specific criteria systematically)
**Source**: `product/module-01-resume.md` through `product/module-05-salary-negotiation.md`
**Status**: observations only. **No edits made tonight.** All decisions deferred to fresh-eyes review tomorrow.

---

## Tom's criteria, observations against each

### 1. Setup overpromises / gate underdelivers

**M1 P1**: persona is generic ("executive resume writer with 15 years"), no pre-output gate, no failure-mode checks. Promises "complete one-page resume optimized for this specific role" but no length validation in constraints — output could run 1.5+ pages depending on input volume. **The 3 unupgraded prompts (M1 P1, M1 P2, M2 P2) read noticeably shallower than the rest.** Already in v2 backlog (week3-polish noted this) but more visible to a buyer than originally scoped.

**M1 P3**: line 91 says "in the output flag which of the 3 versions would be strongest with a number I could supply later." Circular logic — generates 3 versions then asks user to retroactively flag which would be stronger if numbers were provided. Should gate on numbers FIRST (refuse to generate without metrics) OR drop the post-hoc flagging. As written it's both.

**M3 P12 (red-flag detection)**: 4-color rating (🟢🟡🟠🔴) is the visible polish but the gate doesn't anchor what makes something yellow vs orange beyond "specific concern." Two runs of the same input could produce different ratings.

**M5 P1**: Persona promises "compensation strategist for 200+ candidates" then constraint says "Do not cite sources you can't verify... use them as direction-setting benchmarks, always paired with 'verify at current data.'" The persona implies authoritative comp data; the constraint correctly hedges. Buyer might feel the disclaimer undercuts the persona promise.

### 2. Adjacent prompts that feel redundant

**M1 P2 + P3 + P4**: all "edit my existing resume" workflows. P2 = full rewrite. P3 = single bullet. P4 = ATS keywords. Buyer might run all 3 sequentially and get whiplashy iteration. Sequencing isn't called out anywhere.

**M2 P4 + P5**: referral version vs cold application. Mutually exclusive scenarios — a "pick your path" decision tree at module top would help. Right now buyer has to read 6 prompt headers to figure out which applies.

**M3 P11 + P12**: P11 (reverse-interview, screen the company) + P12 (red-flag detection, decode what they said). Complementary but the relationship isn't called out. Buyer could run both for the same interview without realizing they overlap.

**M5 P1 + M3 P8**: M5 P1 is market-rate research (set the number); M3 P8 is salary screen (the recruiter's first money question). Adjacent topics, no cross-ref between modules. Most candidates hit M3 P8 BEFORE they've done M5 P1 — a forward pointer in M3 P8 to "do M5 P1 first if you haven't" would close the loop.

### 3. Voice drift between modules

**Persona-seed depth gap (already known)**: M1 P1, M1 P2, M2 P2 use generic personas without volume markers. Every other prompt across all 5 modules has "X has done [N hundred/thousand specific units]" framing. The 3 stragglers visibly break the pattern when reading top-to-bottom.

**Gate format inconsistency in M3**: P1/P2/P3 use "Do the following:" header. P4/P5 use "CHECK 1 / CHECK 2" labels. Other M3 prompts use "BEFORE [doing X], do these checks." Three different gate formats within one module. Subtle but a careful buyer notices.

**M5 vs other modules — feature richness**: M5 has explicit "Post-output — what to do AFTER the conversation" sections on most prompts. M1-M4 don't have post-output sections at this depth. M5 is clearly the most mature module; the others feel less complete by comparison. A buyer reading M5 first would set an expectation that earlier modules don't meet.

**Em-dash density**: across all 5 modules, em-dashes do triple duty — parenthetical, dramatic pause, definition. A reader notices this after ~50 pages. Not wrong, just a voice tic worth being aware of.

### 4. "Wait, what?" moments

**M1 before/after examples (BIGGEST FLAG)**: All 3 examples (Maya Chen, Derek Olusanya, Priya Raghavan) show input bullets with NO metrics, then output with rich quantified outcomes:
- Maya: "helped with email campaigns" → "28% open rate vs 18% baseline, 47 MQLs"
- Derek: "Built a flashcard app" → "1,200 weekly-active users across 9 schools, 38% week-4 retention"
- Priya: "scaled team 15 to 35" → "62% latency cut, $12M ARR enterprise tier, MTTR 4h → 38min"

**Where did the numbers come from?** The "what changed" commentary describes the transformation but doesn't explain that the candidate had to provide these numbers when the prompt asked clarifying questions. A buyer reading these examples might think (a) the prompts magically generate metrics, OR (b) it's OK to put numbers like that without having them, OR (c) the prompts violate their own "do not invent" constraints.

**Fix**: add a clarifying note before each AFTER showing 1-2 example clarifying questions the prompt asked and the candidate's actual answers. Or add a single note at the top of "Before/after examples" section explaining "The polished AFTER reflects answers the candidate provided when the prompt asked specific clarifying questions about metrics. The numbers are real, sourced from the candidate's memory of the work — not invented by the model."

This is a real "wait what" that affects buyer trust in the bundle's "do not invent" promise.

**M3 rehearsal workflow continuity**: 3-round structure where Round 2 prompt says "Same interview continues, but now you probe." If the user pastes Round 2 into a NEW ChatGPT chat (which the workflow doesn't explicitly forbid), the model has no context from Round 1 and the "continues" framing is a lie. Workflow needs explicit instruction: "**Paste all 3 round prompts into the SAME ChatGPT chat session.** Do not start a new chat between rounds."

**M2 P6**: Cross-reference at top tells user to use M3 P10 for Scenarios B and C. But the prompt body still has length targets and rules for B and C scenarios. Either the prompt fully drops B and C OR keeps them — currently does both: warns away then handles them anyway. Tom's earlier verdict was Path C (cross-ref only, no scenario collapse), which is the source of this — but worth flagging as a known v2 cleanup.

**M5 P12 / scripts referenced in TOC**: TOC lists Scripts 4-8 as "Scripts (Batch 2)" — a development-process artifact the buyer doesn't need to see. (Already noted in EDIT_LOG / PDF_QA_REPORT but worth re-flagging in the buyer perspective.)

### 5. Formatting fine but content meh

**M1 ATS workflow checklist**: Solid but generic. File type, formatting, section order — reads as conventional resume advice rather than the bundle's signature failure-mode-naming depth. Doesn't have the same persona-rigor as the prompts.

**M1 ATS workflow Step 5**: Recommends jobscan.co as the scan-test tool. External dependency that could change pricing or disappear. Either drop the reference OR soften to "any free ATS scanner like jobscan.co or similar."

**M2 cheat sheet ("What hiring managers actually skim for")**: Solid content but reads as more conventional than the prompts. Feels like a different writer — less of the bundle's anti-template philosophy, more of standard cover-letter-tips territory.

**M4 weekly content pack** (10 post types): Good structure but each type description is generic. Doesn't reference Prompt 5 with enough specificity for the buyer to know "if I want to do post type 3 (framework), here's how to use Prompt 5 to write it." Currently says "references Prompt 5 in this module" but doesn't show the wiring.

---

## Cross-cutting observations (not in Tom's criteria but worth noting)

### Decision-tree gaps

Every module has multiple prompts. Buyer overwhelm risk:
- M3 has 12 prompts. A buyer with an interview tomorrow needs to know: "these 3 in this order."
- M5 has 10 prompts + 8 scripts + 3 worksheets = 21 artifacts. Buyer with an offer in hand needs to know: "P1 → P2 → P3 → Script 1, in that order."

Each module intro tries to bucket the prompts (M3 does "predict / answer / show research / close") but doesn't give a time-bounded sequencing recipe. A "Quick Start: 30-minute prep for a phone screen tomorrow" or "60-minute prep for a final round" would close this.

### Time-to-complete guidance

None of the prompts indicate how long they take to run (including ChatGPT response time + clarifying-question rounds). A buyer triaging 21 M5 artifacts has no way to estimate time investment. Adding "~10 min" or "~25 min including 2 rounds of follow-up questions" headers would help.

### M5 is the flagship — the rest could feel thinner by comparison

M5 has full vertical depth: persona-seed + pre-output gate + main output + post-output behavior + scripts + worksheets. M1-M4 mostly have persona-seed + pre-output gate + main output, no post-output, no scripts/worksheets. A buyer who reads M5 first might wonder why M1-M4 don't get the same treatment. (Reasonable answer: they don't need it. But the asymmetry is real.)

---

## What I deliberately did NOT do

- **Did not edit any prompt content.** Per Tom: "Don't edit anything tonight. Edits at midnight after 16 hrs of work will be wrong half the time."
- **Did not commit changes to product/module-*.md files.** This notes file is the only artifact.
- **Did not propose specific rewrites.** Observations only; rewrites need fresh-eyes review.
- **Did not re-render the PDF.** Source is the source of truth for content review.

---

## Recommended fresh-eyes review order tomorrow morning

If owner has ~60 minutes:
1. **The before/after examples issue (M1)** — 15 min. Decide whether to add the clarifying note about where the numbers came from. Highest buyer-trust risk.
2. **Persona-seed backfill on M1 P1, M1 P2, M2 P2** — 30 min. The 3 stragglers. Mechanical fix using the M4 gate template the rest of the bundle follows.
3. **Rehearsal workflow continuity note (M3)** — 5 min. Single line: "Paste all 3 round prompts into the SAME ChatGPT chat session."
4. **Decision-tree per module** — 10 min. One-paragraph "if you're in situation X, run these prompts in this order" at top of each module. Optional but high-leverage.

If owner has 90 minutes: above + M5/M3 cross-reference (M5 P1 ↔ M3 P8).

Everything else is v1.5 or v2 backlog. Don't try to fix in the May 4-17 window unless they surface in the buyer walkthroughs.

---

## What I'm NOT recommending

- **Title page redesign**: already on Tom's v1 launch action list (Canva), don't double-flag.
- **Cover image upgrade**: same.
- **Em-dash density**: voice tic, not a defect. Leave for v2 voice review.
- **External dependencies (jobscan.co)**: minor, don't fix in launch window.
- **Cheat sheet voice (M2)**: not bad, just different — preserves variety, may actually be a feature.

---

End of notes. Worker standing down. Owner reads with fresh eyes May 4 morning, decides what (if anything) goes into the launch window vs v2.
