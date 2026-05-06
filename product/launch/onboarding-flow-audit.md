# Customer onboarding flow audit — pre-launch buyer-experience pass

**Date**: 2026-05-06
**Method**: read each onboarding surface in the order a real buyer encounters them, simulating the 0-to-7-day post-purchase experience. NO EDITS to source files; observation-only audit.

**Audit lens** (per Tom's brief):
1. **Logical flow** — does each step assume the previous one happened?
2. **Hand-offs** — does email → PDF → Notion read as one coherent product?
3. **Voice consistency** — lowercase `hey,` opener everywhere; sentence case body; ChatGPT/Notion/Gumroad casing
4. **Action clarity** — at each step, does the buyer know the immediate next action?
5. **Emotional pacing** — does the energy match someone who just spent $39 (warm, not cheerleader; direct, not cold)?

**Severity scale**:
- 🔴 **refund-risk** — gap could trigger refund or trust loss
- 🟠 **quality-improvement** — gap reduces perceived value but won't cause refunds
- 🟡 **nice-to-have** — polish; buyer won't notice if missing

**Verdict summary**: 5 onboarding steps audited; **8 gaps identified** (1 refund-risk, 4 quality-improvement, 3 nice-to-have). The flow is fundamentally sound — voice and action clarity are consistently strong. The 1 refund-risk is a hand-off mismatch between Option B delivery (ConvertKit) and the email body's reference to Gumroad's "download button at the bottom of this email."

---

## Step 1 — Receipt email body (`DELIVERY_EMAIL.md`)

**Buyer experience**: 30 seconds after paying $39 (or $29 with `LAUNCH`), the email lands. Subject is `Your Job Hunter's AI Bundle is here` (or A/B/C variant). Buyer opens, scans for download.

**What works** ✅
- Opens "hey," — matches the lowercase brand voice signal.
- "It's here." in the first sentence — confirms arrival before anything else, which is what the buyer is looking for.
- "What you just bought" recap with 6 bullets — buyer instantly sees what they paid for. Justifies the $39 in <10 seconds.
- Three imperative tips ("Start with", "Don't run", "Open the worksheet") — tells the buyer what to do, no aspirational language.
- "The prompts are sharp; you have to feed them" — sets expectation that the buyer's effort matters. This single sentence prevents refund regret from buyers who expected one-click hiring.
- Reply CTA is soft and one-shot — "tell me what role and level you're hunting for" — invites engagement without pressuring.
- P.S. handles the "do I have to re-buy for updates?" objection without dedicating a paragraph to it.
- Brand names cased correctly throughout: ChatGPT, LinkedIn, Notion, Gumroad, BATNA, Module, Flynn.

**Gaps**

### 1a — 🔴 refund-risk: download-button reference assumes Option A (Gumroad receipt), breaks under Option B (ConvertKit)
The email body says: *"the download button at the bottom of this email takes you straight to it"*. This is true for Option A (Gumroad's auto-attached download button below the receipt). It is **false** for Option B (ConvertKit Sequence triggered by buyer tag — ConvertKit doesn't auto-attach a Gumroad download button).

If the owner picks Option B (recommended in `DELIVERY_EMAIL.md` for deliverability), the buyer reads "the download button at the bottom of this email" and there's no button. They scroll to the bottom; nothing. They reply "where's the download?" — and the support template fires (`support-templates.md` Template 2). Refund risk is real for buyers who don't bother replying and just refund instead.

**Recommended fix**: branch the body language conditionally. If Option A, keep "the download button at the bottom of this email." If Option B, change to "your download is in your Gumroad library — link below: [Gumroad library URL]" + add an explicit link to gumroad.com/library or directly to the file. The Option B setup notes already mention this concern at line 200: *"include a download link to the bundle PDF in the body itself, since ConvertKit doesn't attach the Gumroad download button."* But the email body itself still references "the download button at the bottom of this email" — which is a contradiction the owner has to remember to fix when pasting into ConvertKit.

**Severity**: 🔴 refund-risk. Surfaces if owner ships Option B without rewriting the body's download-button line.

### 1b — 🟠 quality-improvement: Notion duplication URL is buried mid-bullet
The Notion link sits inside the 6th "what you just bought" bullet, mid-paragraph: *"Bonus: a Notion workspace mirroring the whole bundle, with one-click copy on every prompt — duplicate it to your own workspace here: https://learned-guilty-545.notion.site/..."*

A buyer scanning the bullet list quickly may skim past the URL, then later wonder where the Notion link is. Template 2 (Notion-link-missing) exists in support-templates because this is anticipated.

**Recommended fix**: pull the Notion URL onto its own paragraph below the bullet list, with a label like "Open the Notion workspace" or "Duplicate the Notion workspace". Visual separation. Same content, more discoverable.

**Severity**: 🟠 quality-improvement. Doesn't cause refunds (Template 2 catches it) but reduces friction.

### 1c — 🟡 nice-to-have: no explicit "expected delivery time" reassurance
Some buyers expect a confirmation before the receipt arrives ("your purchase is being processed, check your email in 2 minutes"). The receipt itself is the only signal, and if it lands in spam (Option A's `noreply@customers.gumroad.com`), the buyer waits, refunds, and then finds the email later.

**Recommended fix**: add 1 sentence to the Gumroad listing page or the success page (post-checkout) saying "Check your email — receipt usually lands within 60 seconds. If you don't see it, check Promotions / spam." Out of scope for this file (would touch GUMROAD_LISTING.md), but worth flagging as a gap in the broader onboarding.

**Severity**: 🟡 nice-to-have.

---

## Step 2 — Welcome message body (`GUMROAD_LISTING.md` Field 12)

**Buyer experience**: same email as Step 1 — Field 12 of GUMROAD_LISTING.md was rewritten in the editorial pass (commit `ec3b90a`) to point at DELIVERY_EMAIL.md as source of truth. There is no separate welcome message; the receipt IS the welcome.

**Gaps**

### 2a — 🟠 quality-improvement: no separate post-purchase welcome flow exists
Many infoproduct buyers receive 2 emails: (1) the receipt confirming the order, then (2) a personalized welcome email a few hours or 24 hours later. Currently the bundle has only #1.

**Why this matters**: buyers in Promotions/spam who miss the receipt have no second-touch to recover them. The first time the bundle reaches their attention may be the v1.1 broadcast weeks later — by which time the refund window is half-gone and they've forgotten they bought.

**Recommended fix**: build a 2-email post-purchase ConvertKit sequence triggered by `bundle-buyer-2026-may` tag:
- Email 1 (immediate, via Option B in DELIVERY_EMAIL.md) — receipt + welcome (current state)
- Email 2 (Day 2, ~24-36 hours after purchase) — short check-in: "did you find the bundle? hit reply if anything's missing" + reinforces the BATNA-worksheet-first tip

This is in v1.1 backlog territory (NTH-tier, similar to SF1 comp triangulator concept) but worth flagging as a structural gap, not just polish.

**Severity**: 🟠 quality-improvement. v1.1 candidate.

### 2b — ✅ clean: voice consistency
Field 12's pointer text matches the broader file's editorial voice (sentence case, no overclaiming). No drift from Step 1.

---

## Step 3 — PDF first 5 pages (`product/build/output/job-hunters-bundle.pdf`)

**Buyer experience**: clicks the Gumroad download button (or scrolls Gumroad library), the 119-page PDF opens. First impression is the title page; flips to TOC; lands on Module 1.

**Pages walked**:
- **Page 1** — Title page: "The Job Hunter's Bundle / 44 Prompts · 8 Negotiation Scripts · 3 Worksheets / Flynn Sinclair"
- **Pages 2-3** — TOC across 2 pages, with hyperlinked entries
- **Page 4** — Module 1 — Resume opens. Header line: "8 prompts · ATS optimization checklist · 3 before/after examples All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o)." Then "How to use this module" (4 sentences) and Prompt 1 begins.
- **Page 5** — continues into Prompt 1's body and into Prompt 2.

**What works** ✅
- Hyperlinked TOC (verified in PDF QA report) — buyer can click directly to any section.
- "How to use this module" appears at the start of Module 1 with the 4-sentence rules: (1) prompts are copy-paste blocks, (2) replace bracketed placeholders, (3) paste the whole prompt + your inputs as one message, (4) give ChatGPT your raw material first ("Prompts run on blank slate produce generic output. That's the #1 reason AI resumes get flagged.").
- The "raw material first" rule reinforces the receipt email's Tip #2 ("don't run on a blank slate").
- Brand names cased correctly: ChatGPT, GPT-4o-mini, GPT-4o.

**Gaps**

### 3a — 🟠 quality-improvement: no welcome page bridges the receipt email and Module 1
The receipt email ends with three imperative tips. The PDF opens straight into Module 1 with its own "How to use this module" rules. There's no continuity between the email's tips and the PDF's first content. A buyer who opens the PDF a week after the email has forgotten the email's tips.

**What's missing**: a 1-page welcome at PDF page 2 (between title and TOC) that:
- Restates the 3 tips from the receipt email so they live in the bundle itself
- Explains the bundle's structure (5 modules + scripts + worksheets) at a glance
- Anchors the version + date ("v1.0 — May 2026")
- Reinforces the "free updates" promise inside the PDF where buyers will re-find it

**Recommended fix**: write 1-page welcome → already in v1.1 backlog as SF3 (with 2 sources: notion/05-changelog.md v1.1 list + PDF_QA_REPORT.md S3). Coordinate with v1.1 PDF re-render cycle.

**Severity**: 🟠 quality-improvement. Already tracked in v1.1 backlog.

### 3b — 🟠 quality-improvement: bundle ends abruptly (paired with start gap)
Symmetric to 3a — the bundle's last page is Module 5 Worksheet 3's end-marker. No closing handoff, no "what next" page, no version mark, no "thank you" beat. Reader hits a wall.

**Recommended fix**: write 1-page closing → already in v1.1 backlog as SF4. Bundle with v1.1 PDF re-render.

**Severity**: 🟠 quality-improvement. Already tracked.

### 3c — 🟡 nice-to-have: title page is sparse / brand-light
Title page has only "The Job Hunter's Bundle / 44 Prompts · 8 Negotiation Scripts · 3 Worksheets / Flynn Sinclair." No `snipprompts.com`, no tagline, no version. A buyer screenshotting the title page (e.g., to share on social, to add to a desktop icon) has nothing to attribute back to the brand.

**Recommended fix**: add `date: "May 2026 · v1.0"` + a tagline + `snipprompts.com` to the title block via `defaults.yaml` metadata → already in v1.1 backlog as NTH3 + NTH4.

**Severity**: 🟡 nice-to-have. Already tracked.

---

## Step 4 — Notion "Start here" page (`notion/00-START_HERE.md`)

**Buyer experience**: clicks the Notion duplication URL from the receipt email (Step 1), lands on the published Notion workspace, sees the "Start here" page as the parent.

**What works** ✅
- Voice exactly matches the receipt email: lowercase "hey," opener, sentence case body, "Good luck out there. — Flynn" signoff.
- Workspace map ("What's in here") gives a 5-bullet overview that mirrors the PDF's TOC structure but adds Notion-specific surfaces (Job tracker, Progress checklist).
- "15-minute quick-win path" is the same Module 5 → BATNA → Counter-offer flow as the receipt email's Tip 1 — reinforces the message at the highest-leverage moment.
- "Three rules that make the prompts work" restates the receipt email's three tips (don't run blank, BATNA before negotiation, prompts are sharp). Reinforcement, not redundancy — the buyer reads them once in email, possibly forgets, then re-encounters them when they actually open the bundle.
- Updates wording: "Free updates pushed to your Gumroad library — no re-download needed." Matches the softened wording across the rest of the launch surfaces.

**Gaps**

### 4a — 🔴-adjacent: live Notion workspace currently shows "12 months of free updates" (NOT this softened wording)
Per `v1.1-quick-actions.md`: source-file edits to `notion/00-START_HERE.md` and `notion/05-changelog.md` (commits `ffcbfd6` + `33efbc4`) don't auto-propagate to the published Notion duplication template. Until the owner hand-edits the live Notion pages, buyers who duplicate the workspace see the OLDER "12 months of free updates" wording — which contradicts the softened version in the receipt email and on the Gumroad listing FAQ.

**Buyer impact**: contradiction between the receipt email's update promise ("Free updates pushed to your Gumroad library, no re-download needed") and the Notion workspace's update promise ("12 months of free updates"). Buyer asks support: "is it 12 months or forever?" Either answer creates friction.

**Severity classification**: this is a 🔴 if not fixed before launch (the contradiction is real). Once owner re-syncs the live Notion (5 min per `v1.1-quick-actions.md` O1), this resolves. Already tracked as O1 in `v1.1-backlog.md`.

**Recommended fix**: owner re-syncs the 2 Notion pages before May 17 (already a soft-blocker in v1.1 backlog).

**Severity**: 🔴 if unfixed by May 17; ✅ if O1 lands.

### 4b — 🟡 nice-to-have: workspace map describes 5 surfaces but doesn't link to them
"What's in here" lists Prompt library / Templates / Job tracker / Progress checklist / Changelog as sub-pages. In the markdown source, those aren't actual links. After Notion import they should appear as nested pages in the sidebar (per IMPORT_GUIDE.md), but the prose itself doesn't link directly.

**Recommended fix**: after Notion import, the owner could go back to the START_HERE page and turn each bold name into a Notion @mention link to the sub-page. Manual ~5 min step. Easy to overlook. Worth flagging in the IMPORT_GUIDE as Step 7.

**Severity**: 🟡 nice-to-have. Notion's automatic sidebar handles navigation; explicit links are a polish.

---

## Step 5 — Notion `IMPORT_GUIDE.md` (sophisticated buyer)

**Critical clarification on Tom's brief**: `IMPORT_GUIDE.md` is **owner-facing, not buyer-facing**. It's the documentation Flynn reads to import the markdown sources into Notion and set up the duplication URL. Per its own Step 2 instructions, only files `00-START_HERE.md` through `05-changelog.md` are imported into the published workspace; `IMPORT_GUIDE.md` itself is excluded.

A buyer who duplicates the workspace will not see IMPORT_GUIDE.md as a Notion page. They access it only if:
- They click into the GitHub repo via some path (no link in the bundle gives them this path)
- They search for "snipprompts notion import" online (unlikely)

**Realistic answer**: 0% of buyers will encounter IMPORT_GUIDE.md. Step 5 of Tom's audit list doesn't apply to the buyer journey.

**Audit-completeness note**: the file is well-structured for its actual audience (the owner). Voice differs from buyer-facing copy (more directive: "Drag and drop or select all six files"). That's appropriate; owner docs don't need the brand voice signal.

**Gaps for owner**: covered separately in `v1.1-backlog.md` NTH13 (URL example mismatch in IMPORT_GUIDE.md line 127). Not a buyer-experience issue.

**Severity**: not applicable to buyer journey.

---

## Cross-step audit findings

### Voice consistency across all 4 buyer-facing steps

| Step | "hey," opener | Sentence case body | Brand names cased | Signoff |
|---|---|---|---|---|
| 1 (receipt email) | ✅ | ✅ | ✅ | "— Flynn" + snipprompts.com |
| 2 (welcome — same as 1) | ✅ | ✅ | ✅ | (inherits) |
| 3 (PDF early pages) | n/a (no opener convention) | ✅ | ✅ | n/a |
| 4 (Notion Start here) | ✅ | ✅ | ✅ | "— Flynn" + snipprompts.com |

**Verdict**: voice consistency is the strongest part of the onboarding. A buyer reads receipt → PDF → Notion as one writer. ✅ clean across all 4 steps.

### Hand-off continuity (does each step assume the previous?)

| Hand-off | Score | Notes |
|---|---|---|
| Receipt email → PDF | ⚠️ partial | Email tips don't appear in PDF. SF3 welcome page would close this. |
| Receipt email → Notion | ✅ clean | "Three rules" in Start here page mirror email's three tips. Reinforcement. |
| PDF → Notion | ⚠️ partial | PDF doesn't reference Notion as a companion explicitly (only the receipt email does). A buyer who comes back to the PDF a week later, having forgotten the email, may not realize the Notion workspace exists. |
| Notion → PDF | ✅ clean | Notion Start here explicitly says "The PDF is the long-form reference." |

**Recommended fix**: in the SF3 welcome page (v1.1), add 1 line: "There's also a Notion workspace mirroring this bundle (link is in your receipt email)." Closes the PDF → Notion hand-off.

### Action clarity at each step

| Step | Clear immediate next action? |
|---|---|
| 1 (receipt) | ✅ "Click the download button" + "duplicate the Notion workspace" + "open Module 5 if you have an offer" |
| 3 (PDF) | ✅ Module 1 opens with "How to use this module" (4 sentences of clear rules) |
| 4 (Notion Start here) | ✅ "15-minute quick-win path" gives 3 specific actions |

**Verdict**: action clarity is strong. ✅ clean.

### Emotional pacing

The receipt email is warm but not cheerleader. "It's here. The PDF is in your Gumroad library." — clean, professional. The "Good luck out there" signoff is one of the warmest beats; it acknowledges the buyer is in the trenches. PDF's "How to use this module" is functional and direct (matches the bundle's anti-fluff voice). Notion's Start here mirrors the receipt email's warmth.

**Verdict**: emotional pacing matches the buyer's expected energy at $39 spend — warm but not fawning, direct but not cold. ✅ clean.

---

## Summary table — all gaps by severity

| ID | Step | Severity | Gap | Fix path | Status |
|---|---|---|---|---|---|
| 1a | Receipt email | 🔴 refund-risk | "Download button at bottom" assumes Option A; breaks under Option B | Branch body language conditionally for Option A vs B, OR pick one option for v1 launch and align body | **Not in v1.1 backlog** — surface for owner pre-launch |
| 4a | Notion Start here | 🔴 (until O1 lands) | Live Notion shows "12 months" wording — contradicts receipt email | Owner runs O1 (re-sync 2 Notion pages, ~5 min) | Tracked as O1 pre-launch owner action |
| 1b | Receipt email | 🟠 quality-improvement | Notion URL buried mid-bullet | Pull URL onto its own paragraph with a label | Not yet tracked — propose adding to v1.1 backlog as NTH17 |
| 1c | Receipt email | 🟡 nice-to-have | No "check your email" reassurance on success page | 1 sentence on Gumroad listing post-checkout success page | Not tracked — minor |
| 2a | Welcome flow | 🟠 quality-improvement | No 2-email post-purchase nurture | Build Day-2 check-in via ConvertKit Sequence | Adjacent to v1.1 SF1 nurture work; propose adding as SF12 |
| 3a | PDF first pages | 🟠 quality-improvement | No welcome page; PDF jumps to Module 1 | Write 1-page welcome | Tracked as SF3 in v1.1 backlog |
| 3b | PDF last page | 🟠 quality-improvement | Bundle ends abruptly | Write 1-page closing | Tracked as SF4 in v1.1 backlog |
| 3c | PDF title page | 🟡 nice-to-have | Sparse / brand-light | Add date + tagline + snipprompts.com | Tracked as NTH3 + NTH4 in v1.1 backlog |
| 4b | Notion Start here | 🟡 nice-to-have | Workspace-map bullets aren't Notion @mention links | Manual link conversion after Notion import | Not tracked — flag as IMPORT_GUIDE Step 7 |

---

## Recommended actions

### Pre-launch (must, ~10 min total)
1. **Resolve 1a (download-button reference)**: owner picks Option A or Option B, then verifies the receipt email body matches. If Option B (recommended for deliverability), edit the body's "the download button at the bottom of this email" to reference the Gumroad library URL or an embedded link. ~5 min.
2. **Resolve 4a (Notion re-sync)**: already tracked as v1.1-backlog O1. Owner does the 5-min Notion hand-edit before launch.

### v1.1 (next bundle update cycle)
3. Add 1b to v1.1 backlog (label as NTH17 — Notion URL buried mid-bullet).
4. Add 2a to v1.1 backlog (label as SF12 — Day-2 post-purchase check-in email).
5. SF3 + SF4 + NTH3 + NTH4 already tracked. The welcome page (SF3) should explicitly reference the Notion workspace as a companion (per the Hand-off section finding above).

### Don't action
6. Step 5 (IMPORT_GUIDE.md) — owner-facing, not buyer-facing. The audit mismatch was Tom's brief listing it; reality is buyers don't see it. No buyer-experience work needed.

---

## Limits of this audit

- **No real buyer was tested**. This is a structural read of the artifacts, not a real $39 buyer's lived experience. A real buyer might surface issues that aren't visible from artifact-reading alone (e.g., emotional reactions to specific phrasings, confusion at specific transition points). The May 14 walkthrough (per `sprint-plan-may-4-17.md`) — owner does a $0 test purchase — partially addresses this, but a real buyer's eye is still missing.
- **The PDF audit only covered the first 5 pages**. Tom's brief specified that, but the buyer's full PDF experience is 119 pages. Mid-bundle and end-of-bundle gaps are not captured here (some are flagged in `v1.1-backlog.md` from earlier passes).
- **Notion sub-pages 01–05 not individually audited**. Step 4 only covered `00-START_HERE.md`. The prompt library, templates, job tracker, progress checklist, and changelog could each have their own onboarding-flow gaps. Out of scope for this audit; recommend a follow-up pass if owner wants full Notion coverage.
