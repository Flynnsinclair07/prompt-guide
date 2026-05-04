# Editorial Pass — Change Log

**Date**: May 3, 2026
**Branch**: `launch-prep`
**Files**: GUMROAD_LISTING.md, EMAIL_SEQUENCE.md, PINTEREST_PINS.md, DELIVERY_EMAIL.md
**Tone**: ruthless. Every change has a reason; revert any that don't sit right.

Each file also has an inline `<!-- [Editor's note] -->` block at the bottom recapping its file-specific changes for context when reading the file in isolation.

---

## Cross-file consistency fixes

### Voice — "Hey," → "hey,"
Both EMAIL_SEQUENCE.md and DELIVERY_EMAIL.md had voice notes mandating a lowercase `hey,` opener, but the actual emails in EMAIL_SEQUENCE.md used capitalized `Hey,`. Unified on lowercase `hey,` opener across all five email bodies in EMAIL_SEQUENCE.md plus the GUMROAD_LISTING.md receipt email (now superseded — see below). DELIVERY_EMAIL.md was already lowercase.

### Voice — sentence case body throughout
DELIVERY_EMAIL.md previously used full-lowercase prose body ("it's here. the PDF is in your gumroad library..."). This was a deliberate voice choice in the prior session, but it had two costs: (1) brand names like ChatGPT, LinkedIn, Notion, and Gumroad read as typos when lowercased, and (2) it diverged from EMAIL_SEQUENCE.md's sentence case body. Standardized on **lowercase `hey,` opener + sentence case body + properly cased proper nouns** across both files. The "hey," signal is preserved; the rest of the prose now reads as a paid-product email, not a typo.

### Receipt email duplication eliminated
GUMROAD_LISTING.md Field 12 had an embedded receipt-email body that was a stale copy of the post-purchase email — superseded when DELIVERY_EMAIL.md was shipped as the dedicated source of truth. Replaced Field 12's embedded body with a pointer to DELIVERY_EMAIL.md, eliminating the drift surface. Both files now agree on one canonical source.

### Page count: "~141 pages" → "119-page"
Verified via `pdfinfo` on the rebuilt bundle. Updated GUMROAD_LISTING.md (was the only file claiming 141). EMAIL_SEQUENCE.md and PINTEREST_PINS.md already said 119; DELIVERY_EMAIL.md doesn't quote a page count. All four files now consistent.

### Paper size: "letter size" → claim dropped
GUMROAD_LISTING.md said "print-ready letter size". The actual build is A4 (lualatex default per `defaults.yaml`). Dropped the paper-size claim entirely rather than swap to A4 — buyers are reading on screen and don't care, but stating a paper size that isn't true is the kind of thing that earns a refund email. Logged as a v1.1 nice-to-have in PDF_QA_REPORT.md.

### Site traffic claims: pre-traffic reality
README.md says "Traffic-waiting-phase rules (until 100+ monthly organic visitors)" and "Phase 2 content paused until Search Console shows which pages actually get impressions." Two files made claims that contradicted this:
- GUMROAD_LISTING.md description: "Built around the prompts that already get used thousands of times a month at snipprompts.com" → rewrote to "Built from the five career prompts on snipprompts.com" (claim-free, true).
- GUMROAD_LISTING.md About: "the deep version of the five career prompts that get the most traffic" → rewrote to "the five career prompts on the site, plus everything that didn't fit on a free page" (claim-free, true).
- EMAIL_SEQUENCE.md Email 3: "the deep version of the five career prompts that get the most traffic on snipprompts.com" → rewrote to "the deep version of the five career prompts on snipprompts.com, expanded with the scripts and worksheets I'd use myself if I were running my own search today" (drops the false traffic claim, adds personal-stake framing).

---

## Per-file changes

### GUMROAD_LISTING.md

Top edits (rationale at bottom of the file in `<!-- editor's note -->`):

- **Field 5 hook** — dropped "thousands of times a month" false claim; replaced with truthful "built from the five career prompts on snipprompts.com" framing.
- **Field 5 Format section** — "~141 pages" → "119-page"; dropped "print-ready letter size" (PDF is A4, not letter).
- **Field 5 About** — rewrote to drop the unverifiable "most traffic" claim; new wording is claim-free and accurate.
- **Field 12 receipt body** — replaced the embedded duplicate with a one-paragraph pointer to DELIVERY_EMAIL.md as source of truth.
- **Listing-day step #2** — clarified the "warm but un-indexed" advice (an unpublished listing doesn't have a URL to keep warm; the actual reason is to protect the discount window for subscribers).

Left alone deliberately:
- The `## What's inside / ## Format / ## Who this is for / ## Who this isn't for / ## FAQ / ## About the author` section structure. Could be tightened but the current sub-heads earn their place — each answers a buyer's tab-switching question.
- The "Less than 15 minutes with a resume coach" anchor and the "/Cheaper than the screen-share where someone just reads your resume back to you" anchor — both keep, both work.
- Module 5 prompt order in the Field 5 list. PDF orders them market-rate research → offer evaluation, but the listing leads with offer evaluation as a marketing choice (most relatable starting point for a buyer with an offer in hand). Marketing copy doesn't need to mirror the PDF.

### EMAIL_SEQUENCE.md

Top edits:

- **All five email bodies**: `Hey,` → `hey,` to match the file's own voice spec (line 326) and DELIVERY_EMAIL.md.
- **Email 1 reply CTA**: broadened "if you're between jobs right now" to "if any part of the job search is grinding you down right now". The original gated the reply CTA on a subset of subscribers (between jobs); the bigger pool — passive subscribers thinking about moving — is also valid testimonial / objection-mapping fodder.
- **Email 3** ("What it is" closer): dropped the "most traffic" claim per pre-traffic reality.
- **Email 4 anchor line**: dropped the leading "Anchor:" — that word leaked the marketing internals to the reader (anchoring is something we do TO them, not narrate). The line itself stays; just removed the meta-language.
- **Email 5** module-overlap claim: tightened "the only modules with no free version anywhere on the site are Modules 4 and 5" to specifically call out the net-new content (LinkedIn outreach prompts; full negotiation playbook depth). Original was technically false — snipprompts.com has free LinkedIn Profile and Negotiation prompts, just not at this depth.

Left alone deliberately:
- The 4-email schedule (May 3 / 12 / 16 / 17). Pacing is right.
- Subject line for Email 1 ("Heads up — I'm launching something on May 17"). Conversational, signals importance without selling.
- Email 3's "What it's not / what it is" closer.
- Email 4 P.S. about forwarding to friends and the per-buyer/not-per-account discount detail.
- The Optional Email 5 send conditions ("only if Email 4 open rate >40% AND fewer than 50 sales by Monday 5 PM"). Smart trigger.

### PINTEREST_PINS.md

Top edits:

- **Pin 6 benefit**: "Past senior engineer tested" → "Hiring-manager tested" (typo fix; "Hiring-manager" is universally relatable across roles, not engineering-specific, and matches the Pinterest description's "tested by senior engineers and hiring managers" claim).
- **Pin 12 benefit**: "Works on InMail too" → "No InMail needed" (the original implied the prompt also works on the paid InMail feature, but the actual selling point is the opposite — fits in a 300-char free-LinkedIn connection-request note, no InMail required). Matches the Pinterest description.
- **Pin 6 + Pin 12 alt text**: updated to match the new benefit lines.

Left alone deliberately:
- The 10-pin drip schedule (May 4 → 17). Cadence is right; the May 10 skip (Mother's Day) is a smart call.
- Pin 13 "Subscribers get $29" framing — the launch discount IS list-only pre-May 17 (the Gumroad listing isn't published until launch morning), so the framing is accurate AND the friction it creates ("must subscribe to get the deal") is the intended funnel mechanism. Don't soften.
- Pin 14's "The free internet has one negotiation prompt" hook. Bold but accurate (snipprompts.com has exactly one negotiation prompt; the bundle has 10 + 8 scripts + 3 worksheets).
- Existing pin aesthetic spec (1000×1500, navy/forest, cream text). Brand-locked.
- The voice rules at bottom (no aspirational headlines, numbers in headlines, "free" only on free-prompt pins). All correct.

### DELIVERY_EMAIL.md

Top edits:

- **Body**: rewrote from full-lowercase prose to lowercase `hey,` opener + sentence case body + properly cased proper nouns (ChatGPT, LinkedIn, Notion, Gumroad, BATNA, Module, Flynn, "I"). The lowercase voice signal is preserved in the opener; the rest now reads professionally and matches EMAIL_SEQUENCE.md.
- **Plain-text fallback**: same conversion applied.
- **Voice / craft notes**: rewrote to sentence case to match. Content unchanged — same craft principles (lowercase opener, no "thank you for your purchase", imperative tips, "prompts are sharp; you have to feed them", concrete 5-day promise, P.S. for updates).
- **Notes on the body**: updated the Notion-link cross-reference now that GUMROAD_LISTING.md Field 12 points back to this file.

Left alone deliberately:
- The 3 subject lines (A/B/C) and the A/B/C decision rationale (33/33/34 split, pick winner on reply rate not opens).
- The body content. Every paragraph does a specific job (download mechanic → what-you-bought recap → 3 imperative tips → 5-day comp-prompt promise → reply ask → P.S. for update objection). No filler to cut.
- The "the prompts are sharp; you have to feed them" line — most important sentence in the email. Sets expectations that prevent refund regret.
- The 5-day comp-prompt follow-up promise. Concrete, falsifiable, builds trust.
- The Gumroad-vs-ConvertKit setup paths (Option A simpler, Option B better deliverability).

---

## What I checked but didn't change

- **Module 5 prompt list orderings** in GUMROAD_LISTING.md and EMAIL_SEQUENCE.md don't match the PDF's (which goes market-rate research → offer evaluation → … → justify your ask). Marketing copy isn't a PDF table of contents; the listing's order leads with the most relatable hook for a buyer with an offer in hand. No change.
- **The 13 cheat-sheet signals claim** in GUMROAD_LISTING.md ("13 signals + the one question that earns the interview"). Verified against the source: Module 2's cheat sheet has exactly 13 numbered signals. Accurate.
- **The 134 free prompts claim** in GUMROAD_LISTING.md About section. Verified: `prompts/*.html` has 134 files. Accurate.
- **Site-Career-tagged prompts**: 9 prompts on the site are tagged Career (Cover Letter, Resume, LinkedIn Profile, Interview Prep, Resignation Letter, Performance Review, Resume Bullets, Networking Email, Professional Bio). The bundle expands 5 of these into modules. The "5 starter prompts on these topics" framing in GUMROAD_LISTING.md is accurate (one free prompt per bundle topic).
- **Pricing claims**: $39 list / $29 launch consistent across all four files. No change.
- **Launch date**: May 17, 2026 consistent across all four files. No change.
- **Discount code `LAUNCH`** consistent across all four files. No change.
- **`bundle-buyer-2026-may` tag** consistent across all four files. No change.
- **ConvertKit form UID `d02eb77674`** consistent across all four files. No change.
- **Gumroad URL pattern** still uses `snipprompts.gumroad.com` placeholder. Open question logged in LAUNCH_PUNCHLIST.md Q1 — Flynn needs to confirm the actual storefront subdomain on listing day.

---

## Verification commands run

```bash
# Page count: 119 (verified, all four files now consistent)
pdfinfo product/build/output/job-hunters-bundle.pdf | grep Pages

# 'Hey,' capitalized scan: 0 instances in email bodies (good)
grep -nE '^Hey,$' GUMROAD_LISTING.md EMAIL_SEQUENCE.md DELIVERY_EMAIL.md

# 'thousands of times' scan: 0 instances in copy (only in editor's notes referencing the original)
grep -niE 'thousands' GUMROAD_LISTING.md EMAIL_SEQUENCE.md PINTEREST_PINS.md DELIVERY_EMAIL.md

# Pin 6 typo scan: 0 instances of "Past senior engineer tested" remain
grep -nE 'Past senior' PINTEREST_PINS.md

# Site career prompts count
grep -c 'category-tag">Career<' index.html  # 9 confirmed
```

All scans return clean results.
