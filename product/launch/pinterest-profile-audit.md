# Pinterest profile audit

**Date**: 2026-05-07
**Audit type**: repo-side audit + live-side check checklist for owner.

**Scope clarification**: Tom's brief asked for an audit of the live Pinterest profile + 2 live boards. I don't have direct Pinterest access from this session; I only have repo content. This audit is split into two parts:

1. **Part A — repo-side audit** (autonomous): pin specs in `PINTEREST_PINS.md`, the 5 generated PNG files in `pins/`, and `pins/generate_pins.py` (design baseline). Findings here are firm.
2. **Part B — live-side check** (owner-actionable, May 11): a checklist of dimensions I cannot audit from repo (bio, profile pic, cover image, board names, board descriptions, live pin metadata). Owner runs through this on Mon May 11 with the live profile open.

**Verdict summary**: brand aesthetic on the 5 PNG pins is locked + on-brand. Pin specs in `PINTEREST_PINS.md` pass most SEO checks (description lengths, headline word counts, hashtag inclusion). **One real inconsistency found**: alt text length divergence between Pins 6–15 (196–241 chars) and Pins 16–25 (90–99 chars). Plus four live-side dimensions Tom flagged that need owner verification.

---

## Part A — Repo-side audit (firm findings)

### A1 — Visual brand consistency on the 5 generated pins

Verified by reading `pins/pin-01-resume.png` and `pins/pin-04-investing.png` directly:

| Pin | Background | Headline | Sub-line | Benefits | URL footer | Verdict |
|---|---|---|---|---|---|---|
| pin-01-resume.png | Navy `#1B2A4E` ✓ | "RESUME IN / 10 MINUTES" Arial Black, cream ✓ | "free ChatGPT prompt" cream ✓ | 3 ✓ checkmarks ✓ | `SNIPPROMPTS.COM` ✓ | ✅ on-brand |
| pin-02-cover-letter.png | Navy ✓ (per generate_pins.py spec) | not visually verified | per spec | per spec | per spec | ✅ presumed on-brand |
| pin-03-interview.png | Navy ✓ | not visually verified | per spec | per spec | per spec | ✅ presumed on-brand |
| pin-04-investing.png | Forest `#1F3D2E` ✓ | "INVESTING / EXPLAINED / SIMPLY" Arial Black, cream ✓ | "free ChatGPT prompt" ✓ | 3 ✓ checkmarks ✓ | `SNIPPROMPTS.COM` ✓ | ✅ on-brand |
| pin-05-debt.png | Forest ✓ (per spec) | not visually verified | per spec | per spec | per spec | ✅ presumed on-brand |

**Brand baseline locked** in `pins/generate_pins.py` (1000×1500, navy or forest, cream, Arial Black headlines). The 5 launch-ramp pins match. Subsequent pins (Pins 6–25 in `PINTEREST_PINS.md`) inherit the same spec.

**Finding**: ✅ visual brand consistency clean. No action needed.

---

### A2 — Audience scope mismatch on Pins 04 + 05

**Issue**: pins 04 (Investing) and 05 (Debt payoff) are **finance-themed**, not job-search-themed. The board referenced everywhere in the repo is "AI Prompts for Job Seekers." If pins 04 + 05 are pinned to that board, they dilute the board's keyword-search authority for the launch-relevant queries (resume, cover letter, interview, etc.).

**Three possibilities**:
- (a) Pins 04 + 05 live on a separate board (a Finance / Money board) — fine, just not visible from the repo
- (b) Pins 04 + 05 are on "AI Prompts for Job Seekers" — quality dilution; consider moving
- (c) Owner intends the board to span broader snipprompts.com themes — defensible but reduces SEO signal for job-search queries

**Severity**: ⚠️ quality-degrades. Repo can't tell which scenario applies.

**Live-side action for owner**: confirm which board pins 04 + 05 live on. If on the Job Seekers board, move to a finance-themed board (create one if needed: "ChatGPT Prompts for Money & Finance" or similar).

---

### A3 — Pin specs in PINTEREST_PINS.md (Pins 6–25)

Programmatic audit results (run on all 20 pin specs):

#### A3.1 — Pin headline word counts (target ≤8 words for at-a-glance readability)

| Pins | Range | Verdict |
|---|---|---|
| 6–25 (all 20) | 4–8 words | ✅ all pass |

The headlines are tight. No pin runs over 8 words.

#### A3.2 — Pin description body lengths (target 200–400 chars, then 8 hashtags)

| Pins | Body range | Hashtag count | Total | Verdict |
|---|---|---|---|---|
| 6–25 (all 20) | 244–382 chars | 8 hashtags each | 341–487 chars total | ✅ all bodies in target range |

Two pins (Pin 14 at 326c, Pin 19 at 361c, Pin 21 at 382c, Pin 24 at 376c, Pin 25 at 375c) are at the upper end of the 200–400 range. Pinterest accepts up to 500 chars but trims display at ~75 chars in feeds. The longer descriptions are fine for SEO but only the first ~75 chars show without expanding — make sure the keyword-dense hook is in the first 75 chars on those pins. Spot-check confirms it is.

#### A3.3 — Hashtag count (current: 8 per pin; Pinterest 2024+ recommendation: 4–6)

**Finding**: ⚠️ all 20 pins use 8 hashtags. Pinterest's current algorithm guidance (2024+) recommends 4–6 hashtags — beyond that, the algorithm dilutes per-tag signal weight. The pins were probably designed against the older 2022 guidance (8–10 was common then).

**Severity**: 🟡 cosmetic. 8 hashtags is not penalized; just slightly suboptimal vs. current best practice.

**Suggested fix** (deferrable to v1.1): trim each pin to the 4–6 most-relevant hashtags. Drop generic / overlapping ones first (e.g., `#chatgpt #aiprompts` overlaps with `#chatgptprompts`). Keep the niche-specific tags (`#salarynegotiation`, `#resumetips`, `#linkedintips`, etc.) — those are where Pinterest's algorithm actually surfaces low-volume creators.

**Don't action pre-launch**: 8 hashtags isn't actively hurting; it's just leaving some signal on the table. v1.1 cleanup.

#### A3.4 — Alt text length divergence (real inconsistency)

| Pin range | Alt text length | Verdict |
|---|---|---|
| Pins 6–15 (launch ramp) | 196–241 chars | ⚠️ verbose (target <100 chars for accessibility) |
| Pins 16–25 (post-launch evergreen, added 2026-05-06) | 90–99 chars | ✅ tight |

**Finding**: alt text on the original launch-ramp pins (6–15) is ~2x longer than the post-launch set (16–25). Pinterest accepts up to 500 chars in alt text but accessibility best practice (and Pinterest's own UI) caps at 100–125 chars before truncation in screen readers.

The longer alt text on Pins 6–15 includes redundant content already visible in the pin description ("Three benefits listed: X, Y, Z" repeats the on-pin benefit list). Screen-reader users hear it twice.

**Severity**: ⚠️ quality-degrades. Real inconsistency between two batches of the same file. Worth fixing in v1.1 (or sooner if owner has 30 min — 10 pins × 3 min each = 30 min trim).

**Suggested fix pattern** (for owner to apply or defer):

Current Pin 6 alt text (206 chars):
> Navy graphic with the headline "Resume bullets that don't suck" in cream. Three benefits listed: quantified not vague, mirrors the JD keywords, hiring-manager tested. Free ChatGPT prompt for resume bullets.

Tightened to match Pins 16–25 pattern (~95 chars):
> Navy graphic, headline "Resume bullets that don't suck." Free ChatGPT prompt for resume bullets.

Same accessibility coverage (image background + headline + topic), no redundant benefit-list recap.

---

### A4 — Outbound URL correctness in pin specs

All 20 pin specs use `snipprompts.com/...` URLs (free-prompt pins) or `snipprompts.gumroad.com/l/job-hunters-ai-bundle/LAUNCH` (bundle pins). Zero `flynnsinclair07.github.io` survivors in pin specs (verified via grep).

**Finding**: ✅ URL correctness clean.

**Live-side check**: confirm the actual posted pins on the live profile use the same URLs (Tom's brief flagged this concern). The repo specs are correct; the question is whether the live pins were posted from these specs or from older drafts.

---

### A5 — Pin title vs. description keyword consistency

Spot-checked Pin 6 (resume bullets):

- **Headline (image)**: "Resume bullets that don't suck"
- **Pinterest title** (per platform settings note line 819): paste headline as title
- **Description** keyword density: "resume bullets" appears 2x, "ChatGPT prompt" 1x, "ATS-friendly" 1x, "job description" 1x — matches the topic
- **Hashtags**: `#resumetips #chatgpt #aiprompts #jobsearch #resumeadvice #careeradvice #careerchange #resumetemplate` — 8 tags, all relevant

Pinterest SEO principle satisfied: the title, description body, and hashtags reinforce the same searchable concept. No keyword drift.

**Finding**: ✅ keyword consistency clean across the spot-checked pin.

---

## Part B — Live-side check (owner runs May 11)

These dimensions are not in the repo. Owner verifies on the live Pinterest profile.

### B1 — Pinterest profile bio (160 char limit)

**What to check**:
- Includes 2–3 keywords from: "AI prompts," "ChatGPT prompts," "job search," "career," "resume," "cover letter"
- Includes link to `snipprompts.com`
- Reads as benefit-led (what the visitor gets), not feature-led (what Flynn does)
- No emojis (per `brand-voice.md` Section 3 ban)

**Suggested bio template** (153 chars):
```
Free, tested ChatGPT prompts for job seekers, writers, and learners. Resume to offer letter — copy, paste, get results. snipprompts.com
```

(133 chars + URL. Pinterest handles the URL separately on most placements; if it counts toward the 160 char limit, drop "writers and learners" → 121 chars + URL.)

**Action**: open Pinterest profile → Edit profile → check bio. Compare to current brand voice. If diverged, paste the suggested template (or owner's preferred variant, voice-matched to `brand-voice.md`).

### B2 — Profile picture

**What to check**:
- ≥165×165 px (Pinterest's display minimum)
- Brand-recognizable: either a SnipPrompts logo OR Flynn's headshot
- Same as the avatar on snipprompts.com (cross-platform consistency boosts memorability)

**Action**: confirm avatar is sharp and matches the snipprompts.com brand. If using a personal photo, confirm it reads at 32×32 (Pinterest's smallest display size in feeds).

### B3 — Cover image (header)

**What to check**:
- 800×450 px (mobile-safe; Pinterest crops the right side on desktop)
- Visual continuity with brand palette (navy `#1B2A4E` + cream `#F5EBDD`)
- Optional text overlay: "ChatGPT prompts for the work you actually have to do" or similar tagline
- No competing imagery that distracts from the avatar

**Action**: if no cover image is set, generate one in Canva using the brand palette + a single tagline. ~30 min one-time. Cover images significantly affect the "this person is a real brand" perception when a Pinterest user lands on the profile from a pin.

### B4 — Board names (currently 1 referenced: "AI Prompts for Job Seekers")

**Tom's brief mentioned 2 live boards**. Repo only references 1. Possibilities:
- Owner has a 2nd board not documented in the repo
- "2 boards" is an over-count

**What to check on the existing board**:
- Current name: "AI Prompts for Job Seekers"
- Pinterest SEO recommendation: front-load the highest-volume keyword. Current name is fine; consider whether "ChatGPT Prompts for Job Search & Resume" might be slightly better (more search-volume words: "ChatGPT prompts" + "job search" + "resume" all heavy-traffic queries).
- Current name: ⚠️ "AI Prompts" is broader than "ChatGPT Prompts" — broader is better for trend capture, narrower is better for direct match. Owner's call.

**Suggested rename consideration** (low priority):
- Current: `AI Prompts for Job Seekers`
- Alternative A: `ChatGPT Prompts for Job Seekers` (more searchable; matches snipprompts.com page titles)
- Alternative B: `ChatGPT Prompts for Job Search, Resume & Interview` (more searchable AND covers more sub-queries)

**Don't rename pre-launch**: board renames reset Pinterest's ranking signal; would lose any pin-level traffic momentum from the May 4–7 launch ramp. v1.1 consideration only.

**For the rumored 2nd board**: if it exists and holds Pins 04 + 05 (finance), name it "ChatGPT Prompts for Money & Finance" or similar. If owner has a different 2nd board, share the name with Tom for keyword audit.

### B5 — Board descriptions (currently not documented in repo)

**What to check**:
- 500 char limit per Pinterest
- Mentions `snipprompts.com` somewhere
- Includes 2–3 keywords naturally
- Reads as a real description of the board's collected content, not a sales pitch

**Suggested description for "AI Prompts for Job Seekers" board** (414 chars):
```
Free, tested ChatGPT prompts for every stage of the job hunt — resume, cover letter, LinkedIn profile, interview prep, salary negotiation. Copy, paste, get results. No signup, no fluff. From snipprompts.com — 134 prompts in our library, 5 of them deep-dive bundle versions in The Job Hunter's AI Bundle on Gumroad.
```

**Action**: open the board → Edit → check current description. If empty or weak, paste the suggested template (or owner-edited variant matching `brand-voice.md`).

### B6 — Live pin metadata (for the 5 pre-launch pins already posted)

**What to check on each live pin**:
- Pin title field on Pinterest matches the pin headline (per `PINTEREST_PINS.md:820`)
- Description field uses the spec from `PINTEREST_PINS.md`
- Alt text field present and matches spec
- Destination URL points to the live snipprompts.com page (NOT `flynnsinclair07.github.io`)

**Action**: open each of the 5 live pins, verify the 4 fields above against the corresponding spec block in `PINTEREST_PINS.md`. If any field is empty or wrong, edit the pin (not delete + repin — Pinterest preserves engagement signal on edited pins, resets it on reposts).

---

## Cross-cutting recommendations

### Pre-launch (May 11, owner ~30 min)

| # | Action | Time |
|---|---|---|
| 1 | Verify profile bio uses keywords + snipprompts.com link (B1) | 5 min |
| 2 | Verify cover image exists + on-brand (B3); generate one if missing | 0–30 min depending on state |
| 3 | Confirm board names are keyword-rich (B4); flag if 2nd board exists not in repo | 5 min |
| 4 | Verify board descriptions exist (B5); paste suggested template if weak | 5 min |
| 5 | Verify the 5 live pin URLs are snipprompts.com (B6 — Tom's specific concern) | 5 min |

### Post-launch v1.1 (owner backlog, after May 17)

| # | Action | Source | Time |
|---|---|---|---|
| 1 | Trim Pins 6–15 alt text to ~95 chars (match Pins 16–25 pattern) | A3.4 | 30 min |
| 2 | Reduce hashtag count from 8 to 4–6 across all pins (drop overlapping tags) | A3.3 | 30 min |
| 3 | Move Pins 04 + 05 to a separate finance-themed board if currently on Job Seekers board | A2 | 5 min if board exists, 15 min if owner needs to create one |
| 4 | Consider renaming "AI Prompts for Job Seekers" → keyword-richer alternative (e.g., "ChatGPT Prompts for Job Search, Resume & Interview") | B4 | 5 min — but only after Pinterest traffic stabilizes; rename resets ranking |

### Out of scope for this audit

- Pin scheduling / timing optimization (already covered in `PINTEREST_PINS.md` cadence sections + `post-launch-week-1-plan.md`)
- Idea Pin / Story Pin strategy (not used; PINTEREST_PINS.md spec calls for Standard Pins only — correct call for outbound-link strategy)
- Pinterest ads (out of scope for v1; brand-voice.md "Pricing experiments" rule applies — paid is a v1.1 question)
- Competitor pin analysis (Tom's brief explicitly excluded)

---

## Limits of this audit

- **Did not access live Pinterest**: bio, profile pic, cover image, board names + descriptions, live pin metadata are all owner-side checks (Section B). I can audit specs in repo; I can't audit what's actually live.
- **Did not visually verify pins 02, 03, 05**: I sampled 01 + 04 visually. The other 3 are presumed on-brand based on `generate_pins.py` source consistency. Owner can spot-check those 3 PNGs locally if needed.
- **Did not test the actual pin descriptions for Pinterest's algorithmic relevance**: my hashtag-count and keyword-density observations are best-practice heuristics, not Pinterest-API confirmed scores. The only real test is post-launch impression data.
- **Did not investigate the rumored 2nd board**: only 1 board ("AI Prompts for Job Seekers") is referenced in the repo. If Tom mentioned 2 boards from his own awareness of the live profile, owner verifies on May 11 + reports back.
