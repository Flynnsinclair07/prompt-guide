# Week 1 QA Sample — Boss Review

**For**: Boss Tom
**From**: Worker
**Pulled**: 2026-04-23 (Day 2 actual-calendar, all Week-1 content landed in one push on 2026-04-22)
**Scope**: 6 prompts + 1 workflow (the Answer-Scoring prompt) = 7 artifacts total

## Composition

| # | Module | Prompt | Selection reason |
|---|---|---|---|
| 1 | M1 | P1 · Resume from scratch | Strongest because it's the only M1 prompt with a persona seed + has the "do not invent" anti-BS clause — closest thing in M1 to the signature pattern |
| 2 | M2 | P2 · Mirror-the-JD | Strongest because it's M2's only persona-seeded prompt + has a delivery quality gate ("list the 6+ keywords and where") |
| 3 | M2 | P6 · Follow-up (5-scenario switch) | Strongest because the scenario-switching mechanic is the single most differentiated move in M2 after P5 (which you already reviewed) |
| 4 | M3 | P6 · Why this company | Included per boss flag — batched 2–6 without individual review, spot-check for signature drift |
| 5 | M3 | P8 · Salary screen | Strongest because the pre-output research-gate is the signature quality-gate move at its sharpest (refuses to write scripts until the user has done research) |
| 6 | M3 | P12 · Red-flag detection | Strongest because the traffic-light rating + pattern analysis turns a diffuse "vibe check" into structured output |
| 7 | Workflow | Answer-Scoring prompt | Picked over Rehearsal Round 2 because it's fully standalone — boss sees it complete, not mid-sequence |

## Known signature drift (flagged in polish pass, slotted for Week 3 must-ship fix)

- **M1 persona-seed backfill** on P3–P8 (6 prompts) — 6 of 8 M1 prompts lack persona seed
- **M2 persona-seed backfill** on P1, P3–P6 (5 prompts) — 5 of 6 M2 prompts lack persona seed
- **M1 + M2 pre-output quality-gate backfill** — M3 has a gate on every prompt; M1 and M2 mostly don't
- **M3 P10 / M2 P6 thank-you overlap** — consolidate or hard cross-ref decision pending
- Budget: ~2 hours on May 7 (Week 3 polish day)

Boss-originated backlog also logged (post-launch v2): research-signal terminology simplification, rehearsal Round 1 end-marker, M3 P8/P9 commentary tightening.

---

# 1. Module 1 · Prompt 1 — Resume from scratch (tailored to one role)

*Strongest M1 because it's the only M1 prompt with a persona seed + anti-BS "do not invent" clause.*

```
You are an executive resume writer with 15 years of experience placing candidates in [INDUSTRY].

I'm applying for a [JOB TITLE] role at [COMPANY]. Here's the job description:

[PASTE THE FULL JOB DESCRIPTION]

Here's my raw experience, in bullet form:

[PASTE 8–15 BULLETS COVERING YOUR WORK HISTORY, EDUCATION, AND SKILLS — MESSY IS FINE]

Write a complete one-page resume optimized for this specific role. Use this structure:
1. Contact line: name, email, phone, city + state, LinkedIn URL placeholder
2. Professional summary: 2–3 sentences, tailored to the JD, keyword-dense
3. Experience: 3 roles max, 4–5 bullets each, every bullet starts with a strong action verb, quantified where possible
4. Education: school, degree, year
5. Skills: 8–12 skills pulled directly from the JD's keywords

Constraints:
- ATS-readable format only: plain text, no tables, no graphics, no columns
- Keyword density must mirror the JD (use the same phrasing when possible)
- Every experience bullet must have at least one number, percentage, or dollar amount if the role allows
- Output as plain text ready to paste into a Google Doc

Do not invent achievements, companies, or metrics not in my input.
```

**Why this prompt works:** Three things most generic resume prompts miss: (1) it forces ATS-readable output (no tables / graphics — the #1 reason resumes fail the first filter), (2) it anchors keyword density to the actual JD rather than hoping ChatGPT guesses, and (3) the "do not invent" line blocks the hallucinated-achievement failure mode that gets candidates caught in interviews.

---

# 2. Module 2 · Prompt 2 — Mirror-the-JD (the keyword-aligned body)

*Strongest M2 pick because it's the only M2 prompt with a persona seed + has a keyword-trace delivery gate.*

```
You are a cover letter writer who specializes in ATS and human readability
simultaneously.

Job description:
[PASTE THE FULL JD]

My resume (plain text):
[PASTE YOUR RESUME]

My opening paragraph (already written):
[PASTE THE OPENER YOU'LL USE — IF YOU DON'T HAVE ONE, SAY "GENERATE ONE"]

Write the body of the cover letter (2–3 paragraphs, 180–260 words total)
that does all of the following:

1. Identify the 4 most important responsibilities in the JD and map each one
   to a specific bullet or project from my resume — don't just restate the
   bullet; tell the hiring manager what that experience means for THIS role
2. Use at least 6 keywords from the JD, woven naturally (no stuffing, no
   keyword soup) — at least 3 of them in the first paragraph of the body
3. Include one concrete, quantified accomplishment that maps to the biggest
   stated priority in the JD
4. Do not repeat the opener's research hook — the body is about me-to-them fit,
   not company flattery
5. End the body (before the closing paragraph) with one sentence that signals
   I understand what a hard week in this role looks like

Constraints:
- No corporate jargon: no "synergize", "leverage", "drive value", "results-
  oriented", "passionate", "dynamic", "proven track record"
- One paragraph per topic — no paragraphs longer than 5 sentences
- Every claim must be grounded in my resume. If you want to make a claim I
  can't back up from my inputs, flag it at the end instead of inventing it

After the body, list:
- The 6+ keywords you wove in and where
- Any claim you flagged instead of writing (if any)
```

**Why this prompt works:** The "map 4 JD responsibilities to resume bullets" structure is what hiring managers actually want to see — it's the proof-of-fit a cover letter is supposed to deliver, and it's the exact thing ChatGPT skips by default. The banned-jargon list kills the corporate-voice tell. The "signal I understand what a hard week looks like" sentence is the thing that separates a generic letter from one written by someone who's done the job before.

---

# 3. Module 2 · Prompt 6 — Follow-up (after applying · after the interview)

*Strongest M2 pick after P5 because the 5-scenario switch mechanic is unique in the module — scenario-specific length, timing, and off-ramp rules.*

```
I need to write a follow-up message. Help me choose which scenario this is
and draft the right one.

Scenario (choose):
[ ] A — Applied 5–10 business days ago, no response, want to nudge without
      annoying anyone
[ ] B — Just finished a phone screen or first round interview with
      [INTERVIEWER NAME / ROLE], thank-you note due within 24 hours
[ ] C — Finished a final/panel round, want to reinforce fit before they
      decide
[ ] D — It's been 7–14 days since the interview and I've heard nothing; I
      want to check in without sounding anxious
[ ] E — They ghosted after a strong interview (3+ weeks); I want to send
      one final, dignified message

Fill these in so the message is specific, not generic:
- Company: [COMPANY]
- Role: [JOB TITLE]
- If B or C: specific moment from the conversation I want to build on: [ONE
  SENTENCE — e.g., "we talked about the dashboard rewrite and you mentioned
  X was the hardest part"]
- If B or C: one thing I didn't get to fully explain or wish I'd said better:
  [ONE SENTENCE, OR "NONE"]
- If A, D, or E: the last touchpoint date and what happened: [ONE SENTENCE]

Write the message (email format, no cover-letter formality) following these
rules for the chosen scenario:

Length targets:
- Scenario A (post-application nudge): 60–90 words
- Scenario B (24-hour thank-you): 90–130 words
- Scenario C (post-final reinforcement): 120–180 words
- Scenario D (polite check-in): 50–80 words
- Scenario E (final dignified close): 60–90 words

Universal rules:
- Subject line should be one clean line, no "RE:" gaming, no clickbait
- Do not thank them more than once
- Do not apologize for following up (never say "sorry to bother you")
- Do not re-pitch the full job — reference the specific conversation
- For B and C: reference ONE specific thing discussed to prove I was
  actually present in the conversation, not just performing
- For D and E: make it easy for them to say "we went another direction" —
  give a polite off-ramp
- For E: close the door gracefully. Never send two "final" messages.

At the bottom, give me:
- The subject line
- The ideal send time (day of week + time) for this scenario
- One sentence on what NOT to do in the next 48 hours after sending
```

**Why this prompt works:** Follow-ups are a different craft than cover letters — shorter, calibrated to a specific scenario, with send-timing that matters. Most prompts treat "follow-up" as one thing. Splitting it into 5 scenarios with distinct length targets and rules gives the right structure for each. The "off-ramp for D and E" rule is the move that separates polite candidates from desperate ones — it's the whole difference between getting a response and getting blacklisted.

---

# 4. Module 3 · Prompt 6 — "Why this company?" research

*Included per boss flag — batched 2–6 without individual review, spot-check for signature drift.*

```
You are a research analyst who helps candidates build specific, evidence-
backed answers to "Why do you want to work here?" — the question most
candidates wing and most interviewers silently grade.

Inputs:
- Company: [COMPANY NAME]
- Role: [JOB TITLE]
- Stage / size / industry if you know it: [e.g., "Series C fintech, 400
  people, B2B"]
- What I already know about the company (dump anything — product, news,
  Glassdoor, friends who work there, a post the CEO wrote): [PASTE]
- The 2–3 things the JD emphasized most: [LIST]
- What genuinely draws me to this company (honest version — can be partial,
  shaky, or "not sure yet"): [PASTE]

Do the following:

1. Generate 5 specific reasons I could genuinely give for wanting to work
   at THIS company — not at "a company like this." Each reason must be:
   - Tied to a concrete signal (a product decision, a publicly stated bet,
     a recent launch, a hiring pattern, a founder's public writing, an
     industry shift the company is responding to)
   - Something I could back up if the interviewer asked "can you say more
     about that?"
   - Distinct from the other 4 reasons (don't give me 5 versions of
     "innovative product")

   For each reason, cite where the signal came from (my inputs, a public
   source I'm inferring from, or "this is a reasonable guess based on
   industry patterns — verify before using"). Do not fabricate quotes or
   decisions.

2. Rank the 5 reasons by how well each would land with this specific
   interviewer profile: [CHOOSE — founder/CEO · hiring manager · peer panel
   · recruiter · skip-level]. Explain the ranking in one line each.

3. For the top 2 reasons, write a 45–70 second spoken answer (90–140 words)
   that combines reason + personal connection + forward-looking statement
   (what I'd want to do there). First person, no hedging, no "I'm excited
   about" filler opener.

4. Flag the 2–3 things I should specifically NOT say:
   - Any reason that would apply equally to 10 other companies ("I want a
     fast-paced environment")
   - Any reason that could sound transactional ("I want to work in [CITY]")
   - Any reason that reveals I haven't actually used the product or done
     homework

Constraints:
- Do not lean on the company's About page or tagline. That's what every
  candidate does. Push for one level deeper — a product decision, a
  changelog post, a leadership hire, a customer case study.
- Do not invent specifics. If my inputs don't give you enough to build a
  strong answer, tell me what to go find (e.g., "read the CEO's latest
  podcast appearance", "check the last 3 blog posts") rather than bluffing.
- If my "honest version" input is weak — I don't actually have strong
  evidence I want this company specifically — flag that directly. A generic
  "why this company" answer is worse than a short-but-specific one.
```

**Why this prompt works:** "Why do you want to work here?" is the most-asked, least-prepared-for interview question. Generic answers get silently graded down. This prompt forces every reason to be tied to a concrete signal with a citation, which is the thing most candidates skip. The "rank by interviewer profile" step makes the prompt work across a full interview loop — the reason that lands with the CEO isn't the reason that lands with the peer panel. The "if your honest input is weak, flag it" clause is the anti-bluff move: better to walk in with a short, specific answer than a long, generic one that signals you haven't done the work.

---

# 5. Module 3 · Prompt 8 — Salary screen (the recruiter's first money question)

*Strongest M3 pick because the pre-output reality check refuses to write scripts until research is done — signature quality-gate at its sharpest.*

```
You are a recruiter coach who has trained 100+ candidates to handle the
salary screen without lowballing themselves or pricing themselves out of
the process. You know when to give a number, when to deflect, and when
deflecting is making the candidate look evasive.

Inputs:
- Role: [JOB TITLE]
- Location and work arrangement: [CITY, REMOTE / HYBRID / ONSITE]
- Company stage: [Series B · public · government · nonprofit · etc.]
- My current comp (base · bonus · equity): [PASTE — OR "UNEMPLOYED" / "NOT
  SHARING"]
- My target comp (base · bonus · equity): [PASTE]
- What I've researched about this role's market rate: [LEVELS.FYI NUMBER,
  GLASSDOOR RANGE, FRIEND-AT-COMPANY INTEL — OR "HAVEN'T RESEARCHED YET"]
- The exact question the recruiter asked (or is likely to ask): [PASTE —
  OR "WHAT ARE YOUR SALARY EXPECTATIONS?"]
- Where I am in the process: [first call · after phone screen · post-
  onsite · they've verbally indicated interest]

Do the following:

BEFORE writing any scripts, do this check:
- Is my target comp realistic for this role/market/stage? Compare against
  my research inputs. If my target is >25% above stated market rate
  WITHOUT a specific justification (competing offer, rare skill, unusually
  senior level), flag it and tell me to adjust or provide justification
  before the call.
- If I said "HAVEN'T RESEARCHED YET" — stop. Tell me what to look up in
  the next 30 minutes and in what order (Levels.fyi, Glassdoor, LinkedIn
  Salary, 1 reference conversation). Do not write scripts until I have a
  defensible range.

Once the check passes, write 3 responses, calibrated to three scenarios:

1. **Recruiter-first-call version** (the safest move): deflect specifically,
   not genericly. 40–70 words spoken. Buy time to learn the role while
   signaling I'm not going to waste anyone's time.

2. **Mid-process version** (after phone screen, before onsite): land a
   defensible range, not a single number. 50–80 words. Include the
   research-backed anchor and a soft ceiling I'd go to.

3. **Post-onsite version** (when they've verbally indicated interest or
   asked for a target): give a specific number or tight range. 40–60
   words. Confident. No hedging qualifiers.

For each version, tell me:
- The exact thing to say (first person, spoken cadence)
- The follow-up question the recruiter will likely ask
- What NOT to say in the same breath

Constraints:
- Do not tell me to say "I'm flexible" without a number. That reads as "I
  don't know my worth" and anchors me low.
- Do not tell me to demand above-market compensation without specific
  justification. That gets me screened out before the team hears my name.
- Do not volunteer my CURRENT salary unless I'm legally in a state where
  the employer asked and I have a strategic reason to share. In most
  states, the current-salary ask is illegal and I should decline politely.
- If my situation is "UNEMPLOYED," adjust the scripts to avoid anchoring
  to zero — market rate is the anchor, not my current state.
```

**Why this prompt works:** The salary screen is the single highest-leverage 5 minutes in the entire process — a wrong number here locks the ceiling for the whole offer. The pre-output reality check ("is your target realistic? is your research done?") refuses to write scripts until the user has what they need to defend their range. The three-scenario split is the thing most prompts miss: the right answer changes depending on where you are in the loop. The "don't volunteer current salary" clause is a legal-and-strategic safeguard that even coaches sometimes forget to flag.

---

# 6. Module 3 · Prompt 12 — Red-flag detection (decode the warning signs)

*Strongest M3 pick because the traffic-light rating + pattern analysis turns a diffuse "vibe check" into a structured output — hardest-to-match move in the bundle.*

```
You are a hiring manager who left 2 companies after missing red flags in
interviews you should have caught. You now help candidates decode the
specific phrasings, hesitations, and tells that reveal problems the
company doesn't want to say out loud.

Inputs:
- Company: [COMPANY NAME]
- Role: [JOB TITLE]
- What the interviewer actually said — direct quotes or close
  paraphrases — on any of these topics: workload, team dynamics, manager
  quality, turnover, priorities, company direction, work-life balance,
  compensation: [PASTE EVERYTHING I CAN REMEMBER — messy is fine]
- Any non-verbal or pattern signals I noticed: [e.g., "hiring manager
  rolled their eyes when I asked about on-call", "recruiter dodged the
  layoff question twice", "three different people gave me three different
  answers about who owns the product" — OR "NOTHING NOTABLE"]
- How many total people I've talked to at this company: [NUMBER]

Do the following:

1. For each quote or signal I gave you, rate it on this scale:
   - 🟢 Green: normal, healthy, no concern
   - 🟡 Yellow: worth a follow-up question; not disqualifying alone but
     pattern-watch
   - 🟠 Orange: specific concern; would need clear explanation to overcome
   - 🔴 Red: likely indicator of a structural problem; don't join without
     a much better answer

2. For every yellow/orange/red signal, write:
   - What the signal probably means (the thing they're not saying)
   - One specific follow-up question I could ask to stress-test it
   - What a reassuring answer would actually sound like vs. a deflecting
     one

3. Identify any PATTERNS across multiple signals. A single yellow is
   noise; three yellows on the same theme (e.g., "workload was mentioned
   by every single person unprompted") is a pattern, and patterns matter
   more than individual signals.

4. Give me a bottom-line read: take-the-offer / negotiate-hard / walk-
   away. Explain the call in 2–3 sentences. If my inputs are too thin for
   a read, say so and tell me what specific questions to get answered in
   the next round.

Constraints:
- Do not flag things as red just to seem thorough. Most interviews have
  1–2 yellows; a real red-flag moment is rarer than prep guides pretend.
- Do not over-interpret friendly ambiguity. "We're growing fast" is not
  a red flag. "We're growing so fast that the previous person in this
  role burned out" is.
- Do not be the only voice telling me to walk. If I'm getting 3 yellows
  and a salary under market, the call might be "negotiate hard," not
  "walk." Calibrate to severity, not volume.
- If my pattern input is "NOTHING NOTABLE" and I've only talked to one
  person, tell me that's not enough data — push me to surface patterns
  from the next round before making a call.
```

**Why this prompt works:** Red-flag detection is the single most underprep'd part of the interview process — most candidates process what was said literally and miss the subtext. The traffic-light rating turns a diffuse "vibe check" into a pattern-recognizable output. The "what a reassuring vs. deflecting answer sounds like" section gives the candidate a stress-test for every next conversation. The "patterns matter more than individual signals" clause is the part people skip when they're falling in love with an offer — and the exact move that prevents joining a company you'll regret in 90 days.

---

# 7. Workflow · Answer-Scoring prompt

*Picked over Rehearsal Round 2 because it reads clean as a standalone artifact — boss sees it complete, not mid-sequence. 5-dimension grade, no-inflation constraint, salvageable-or-scrap fork.*

```
You are an interview coach who grades answers on a 10-point scale across
5 dimensions. You do not pad, you do not soften, and you tell the
candidate when the answer is unsalvageable and they need to pick a
different story.

Inputs:
- The interview question: [PASTE THE EXACT QUESTION]
- My answer (word-for-word if possible — okay if it's how you'd say it
  out loud, not how you'd write it): [PASTE]
- Role I'm interviewing for: [JOB TITLE]
- Round type: [recruiter screen · hiring manager · peer panel · final
  round · founder/CEO]

Step 1 — score the answer on 5 dimensions (1–10 each):
- **Structure**: does it follow a recognizable shape (STAR or similar)?
  Does the listener know where they are in the story at any point?
- **Specificity**: numbers, names, concrete moments vs. abstractions.
- **Ownership**: does the answer show what *I* did (vs. what the team
  did)? Are the verbs first-person and decisive?
- **Relevance**: does the story actually answer the question asked, or
  does it answer a nearby question the candidate preferred?
- **Landability**: would a tired interviewer in round 4 catch the point
  on first listen?

For each dimension, give the score and one sentence of why.

Step 2 — top-line diagnosis:
- Total score: X / 50
- The single biggest problem with this answer (one sentence).
- Is this answer salvageable with a rewrite, or should I pick a different
  story entirely? If different story: what KIND of story would fit better
  (e.g., "you need a conflict-with-peer story, not a cross-functional
  coordination story").

Step 3 — IF salvageable, rewrite it:
- Use the STAR structure (S: ≤30 words, T: ≤20 words, A: 60–100 words,
  R: ≤40 words)
- First-person, decisive verbs
- Add a "load-bearing sentence" flag at the bottom — the one sentence I
  must land if the interviewer cuts me off

IF NOT salvageable, skip the rewrite and tell me which of my other stories
(if I've shared any) would fit better, or ask me for a different brain-
dump targeting the right kind of story.

Constraints:
- Do not invent details, numbers, or outcomes I didn't give you. If the
  answer needs a number and I didn't provide one, flag it as "need to
  fill in: ___" rather than making one up.
- Do not score an answer above 7 overall unless it genuinely hits across
  all five dimensions. Grade inflation is how candidates walk into
  interviews thinking they're prepped when they aren't.
- Do not rewrite past the word targets. Longer is not stronger.
- If the answer is under 60 words or over 280, flag the length problem
  before anything else — length discipline is its own signal.
```

**Why this prompt works:** Most self-review is too kind. This prompt forces a 5-dimension grade with a no-inflation constraint, which catches the specific weakness instead of vaguely calling the answer "good." The "salvageable or pick a different story" fork is the part candidates need most — sometimes the right move is scrapping the story, not polishing it, and most coaches don't say that out loud. The "load-bearing sentence" tag carries the answer through a rushed interview when the interviewer cuts you off at 45 seconds.

---

**End of sample.** 6 prompts + 1 workflow. Ready for Thursday Apr 24 boss review.
