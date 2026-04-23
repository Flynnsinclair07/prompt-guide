# Week 3 Polish Pass — Pre-loaded edits for May 7

**Execute**: 2026-05-07 (Week 3 polish day)
**Budget**: ~3 hours
**Scope lock**: NO polish work before May 7. This file is staging only — do not execute items below during Module 4 or Module 5 build.

---

## Must-ship items (v1 launch)

### 1. M3 P8 — Salary law fix

**Location**: `product/module-03-interview.md`, Prompt 8 Constraints section, bullet about volunteering current salary.

**Find and replace this text**:

```
- Do not volunteer my CURRENT salary unless I'm legally in a state where
  the employer asked and I have a strategic reason to share. In most
  states, the current-salary ask is illegal and I should decline politely.
```

**With this text (boss Option B)**:

```
- Do not volunteer my CURRENT salary. The current-salary question is
  illegal in many states and cities (check your state's salary history
  ban status). Regardless of legality, volunteering your current salary
  almost always anchors you low — decline politely and pivot to your
  target range.
```

**Why**: Original text overstated the illegality ("in most states") and put the legal burden on the reader. Option B is accurate (many not most), delegates verification to the reader, and reinforces the strategic point independent of legality.

---

### 2. M3 P12 — Emoji PDF render test

**Location**: `product/module-03-interview.md`, Prompt 12, rating scale bullets.

**Action**: Export a test PDF of M3 P12 and verify 🟢🟡🟠🔴 emojis render correctly. If broken (box characters, missing glyphs, rendering as blank):

**Fallback**: replace emoji with text tags in this exact format:

- 🟢 → `[GREEN]`
- 🟡 → `[YELLOW]`
- 🟠 → `[ORANGE]`
- 🔴 → `[RED]`

Apply consistently across the rating scale and any downstream references in the rest of the prompt.

---

### 3. Persona-seed backfill — Module 1 (6 prompts)

Backfill persona-seed openers on M1 prompts that lack them. Match the voice and structure of M1 P1 and M1 P2 (which already have persona seeds).

**Prompts needing persona seed**:
- M1 P3 (Bullet rewrite) — candidate persona: "senior recruiter who has read 10,000+ resume bullets"
- M1 P4 (ATS keyword injection) — candidate persona: "ATS consultant who has reverse-engineered parser behavior"
- M1 P5 (Quantify achievements) — candidate persona: "resume coach specializing in quantification"
- M1 P6 (Career-switcher angle) — candidate persona: "career-transition coach"
- M1 P7 (Executive summary) — candidate persona: "executive resume writer"
- M1 P8 (LinkedIn → resume converter) — candidate persona: "resume writer who has done 500+ LinkedIn-to-resume conversions"

**Rule**: persona seeds are additive only. Do not rewrite prompt body text. Prepend a 1–2 sentence persona opener that matches the signature pattern.

---

### 4. Persona-seed backfill — Module 2 (5 prompts)

Same approach as #3. Prompts needing persona seed:
- M2 P1 (Hook-first opener)
- M2 P3 (Industry-switcher version)
- M2 P4 (Referral version)
- M2 P5 (Cold application)
- M2 P6 (Follow-up)

**Note**: M2 P5 is already boss-reviewed/greenlit — adding persona seed is a polish enhancement, not a rewrite.

---

### 5. Pre-output quality-gate backfill — Modules 1 + 2

Audit every M1 and M2 prompt for missing pre-output quality gates. M3 has a gate on every prompt; M1 and M2 mostly don't.

**Template update (boss, 2026-04-23)**: use **Module 4** gate style as the template, not M3. M4 gates are more surgical — they ask specific clarifying questions and refuse to proceed until inputs pass, rather than running generic "have you thought about this?" checks. Example of M4 gate style: M4 P1's "if I listed soft skills, flag them and ask me to replace with searchable hard skills. Do not generate a headline using non-searchable terms."

**Approach**: for each prompt, identify the single biggest "bad input → bad output" failure mode, and insert a pre-generation check that refuses to proceed until the user fixes the input.

**Examples of gates to add**:
- M1 P1 (Resume from scratch): gate — if user's raw experience bullets don't include any numbers, pause and ask for 3 quantifiable achievements before writing.
- M2 P2 (Mirror-the-JD): gate — if the opener input is "GENERATE ONE" and the research-signal input is blank, pause and ask user to name one concrete signal.
- M1 P4 (ATS keyword injection): gate — if user's resume is under 200 words, pause; prompt assumes a full resume and will produce weak output on a stub.

**Rule**: gates are additive only. Do not restructure the existing prompt body.

---

### 6. M2 P6 / M3 P10 thank-you redundancy decision

**Issue**: M2 P6 Scenario B (24-hour thank-you) overlaps with M3 P10 (post-interview thank-you dedicated prompt). A buyer who opens both will notice the overlap.

**Decision required on May 7**: pick one of three paths:

**Path A — Consolidate into M3 P10**: remove Scenario B from M2 P6 (leaving 4 scenarios: A, C, D, E). Add a cross-reference: "For 24-hour post-interview thank-yous, see Module 3 Prompt 10."

**Path B — Consolidate into M2 P6**: remove M3 P10 entirely. Expand Scenario B in M2 P6 to include the depth currently in M3 P10. Keep M3 at 11 prompts (not 12), update module header count.

**Path C — Hard cross-reference**: keep both. Add an explicit note at the top of each: "See also: [other prompt] for [specific use case]. The two are intentionally different — M2 P6 gives 5-scenario quick scripts; M3 P10 is a deeper standalone thank-you."

**Recommendation for boss review**: Path C preserves most content without losing depth, and buyers who notice the overlap will see it's intentional rather than redundant.

**Execution rule (boss, 2026-04-23)**: do NOT apply Path C (or A or B) until boss greenlights the specific execution. On May 7, paste the full text of M2 P6 and M3 P10 side-by-side in this file along with the proposed cross-reference wording. Wait for boss approval before modifying either prompt.

---

## Post-launch v2 backlog (NOT for May 7)

These items were flagged but reclassified to post-launch:

- M2 P5: "research signal" terminology → "specific thing you noticed" for less-technical buyers
- Rehearsal Round 1: add explicit end-marker ("end Round 1 and prompt me to move to Round 2")
- M3 P8, P9: commentary tightening (4 sentences → 3)
- **M5 P2 strike/409A imprecision** (boss flagged 2026-04-23): current text in Hidden Traps reads "a low-strike grant at a company with low recent 409A valuation is worth much less than a high-strike grant at a company trending up" — imprecise, could mislead. Replace with boss's suggested rewrite:
  > "Equity value depends on the gap between your strike price and the company's expected future FMV. A grant with a huge notional value can be worth little if the company isn't growing; a smaller grant at a rapidly-appreciating company can be worth far more. Ask for the company's last 409A valuation and think about growth trajectory before pricing equity in your head."

---

---

## Signature pattern reference (for backfill voice consistency)

### Primary signature (all modules should hit this)
1. **Persona seed** — "You are a [role] who has [specific credential]"
2. **Pre-output quality gate** — refuses to generate until inputs pass (M4 style)
3. **"Do not" bans** — specific banned phrases, openers, and failure modes
4. **Anti-BS clause** — flag missing data, refuse to invent

### Secondary signature pattern (emerged across M3 + M4, boss-identified 2026-04-23)

**Structure: Pre-output gate → Output → Post-output behavior rules**

The post-output section does real work. Examples:
- M3 P8 salary screen: "what NOT to say in the same breath"
- M4 P6 recruiter cold-DM: "what NOT to do in the next 48 hours after sending"
- M4 P7 recommendation request: "what to do if they don't reply within 10 days"
- M4 P8 post-connection follow-up: "what to do if they don't reply within 2 weeks"

**Rule**: use this pattern in any prompt where a "what happens after the output is sent" dimension exists. Module 5 (negotiation) is especially high-leverage for this — counter-offer, exploding offer response, PTO ask all have major post-output reality.

---

**Do not execute any item in this file before 2026-05-07.** Scope lock in effect through end of Module 4 + Module 5 build.
