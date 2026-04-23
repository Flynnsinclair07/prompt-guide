# Module 3 — Interview Prep

**12 prompts · AI-grilling rehearsal workflow · answer-scoring prompt**
All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o).

---

## When to use this module

Interview prep is the highest-leverage phase of the job hunt. A good resume gets you in the room; a good interview lands the offer. The prompts below split into four jobs the interview-prep workflow needs to do:

1. **Predict what they'll actually ask** (Prompts 1–3)
2. **Build answers that hold up under pressure** (Prompts 4–6)
3. **Show you've done the work on their side of the table** (Prompts 7–9)
4. **Close the loop — and screen THEM** (Prompts 10–12)

Run them in order the first time, then cherry-pick for each interview round. Always feed the AI your resume and the JD before you run the prompt — a prompt on a blank slate produces generic prep, which is the exact thing your competition is walking in with.

---

## Prompt 1 — Behavioral questions by role (predict what they'll actually ask)

```
You are an interviewer who has run 500+ behavioral interviews for [ROLE] roles
at [INDUSTRY] companies. You know which questions get asked, which ones
actually matter, and how candidates usually flub them.

Inputs:
- Role I'm interviewing for: [JOB TITLE]
- Seniority level: [e.g., IC, senior IC, staff, manager, director, VP]
- Company: [COMPANY NAME]
- Stage of the interview: [e.g., recruiter screen, hiring manager, peer
  panel, final round with CEO]
- Job description: [PASTE FULL JD]
- My resume: [PASTE]

Do the following:

1. Generate the 15 most likely behavioral questions I will face in THIS round
   at THIS company for THIS role. Be specific — not a generic list. If the JD
   emphasizes collaboration, weight toward collaboration questions. If it
   emphasizes independent judgment, weight toward autonomy questions.

2. For each question, give me:
   - The question itself, worded the way a real interviewer would say it
     (not the academic textbook version)
   - A one-line tag: what they're actually testing (e.g., "conflict
     resolution under ambiguity", "ownership vs. blame-shifting", "ability
     to escalate appropriately")
   - A likelihood score out of 10 for this specific round at this specific
     company — be honest. If a question is standard-everywhere, say so. If
     a question is unusually likely given signals in the JD, flag why.

3. Then group the 15 questions into 3 clusters by theme (e.g., "collaboration
   under pressure", "judgment calls", "self-awareness"). Name each cluster.

4. For the 5 highest-likelihood questions, flag the common failure mode —
   the specific way candidates typically answer badly. Examples of failure
   modes: "answers with a team achievement instead of a personal one",
   "spends 90% of the answer on setup and 10% on outcome", "picks a weakness
   that's actually a strength in disguise and sounds insincere".

Constraints:
- Do not pad the list with generic filler. 15 real questions > 20 mediocre
  ones. If the role doesn't warrant 15 distinct questions, say so and give
  me a tighter list.
- Do not invent questions based on company values that aren't in my inputs.
  If you reference a company value, cite where in my inputs you saw it.
- Do not lecture me on the STAR method here — that's a separate prompt.
```

**Why this prompt works:** Three moves that separate this from every "top 20 behavioral interview questions" list online. First, it's tailored to the exact round at the exact company — a recruiter screen and a peer panel at the same company get different questions, and most prep ignores that. Second, the likelihood score forces the model to rank rather than just list, which tells you where to spend your prep time. Third, the "common failure mode" tag on the top 5 is the part most candidates skip: knowing the question is half the prep; knowing how people usually blow the answer is the other half.

---

## Prompt 2 — Technical questions by industry (predict the exact technicals)

```
You are a hiring manager who has run 300+ technical interviews for [ROLE]
positions in [INDUSTRY]. You know what gets asked in a 45-minute technical
screen vs. a deep-dive panel, and you know which questions are signal vs.
noise at [COMPANY]'s stage.

Inputs:
- Role: [JOB TITLE]
- Seniority: [IC · senior · staff · manager · etc.]
- Company and stage: [COMPANY NAME · approx. size or stage, e.g., "Series
  B, 120 people" or "Fortune 500 enterprise"]
- Technical format I'm about to face: [CHOOSE — phone screen · take-home ·
  live coding · whiteboard system design · SQL / data exercise · case
  study · portfolio review · other]
- Length of the round: [45 min · 60 min · 90 min · multi-hour]
- Job description: [PASTE FULL JD]
- My resume: [PASTE]
- Skills or tools I'm strongest on: [LIST]
- Skills or tools I'm weakest on that are in the JD: [LIST — be honest]

Do the following:

1. Generate the 12 most likely technical questions or scenarios I'll face in
   THIS format at THIS company. Not a generic list — weighted to the JD's
   specific responsibilities and the company's stage. A 120-person Series B
   doesn't interview the same way as a Fortune 500 or a 4-person seed co.

2. For each question, give me:
   - The question or scenario, phrased the way a real interviewer would open
     it (not a textbook prompt)
   - What they're actually testing (the skill behind the question, not the
     surface topic — e.g., "trade-off reasoning under ambiguity" not just
     "design a URL shortener")
   - Difficulty tier: easy · moderate · hard · stretch — calibrated to my
     stated seniority. Mark any that are stretch questions likely thrown in
     to see how I think when I don't know the answer.
   - A likelihood score out of 10 for this round at this company

3. Flag the 3 questions that are most likely to be make-or-break for this
   specific role. Explain why in one sentence each.

4. Identify the 2–3 areas where my weakest-skills list intersects with the
   likely questions. Tell me specifically what to brush up on in the next
   48 hours — not "learn SQL" but "revisit window functions, specifically
   LAG and LEAD, and practice writing a 3-table join with a CTE."

Constraints:
- Do not pad with generic leetcode-style questions for roles that aren't
  leetcode-heavy. If this is a system design round, give system design.
  If it's a SQL round, give SQL. Respect the stated format.
- Do not invent company-specific signals. If you cite something "XCo is
  known for asking X," cite where in my inputs you saw that — or don't
  make the claim.
- Do not give me the answers here. This prompt is for predicting and
  prioritizing. Answers are a separate pass.
- If my weak-skills list and the JD's required skills have a gap so large
  that 48 hours of prep can't close it, say so directly.
```

**Why this prompt works:** Generic technical prep lists get you ready for every job and no specific job. The format input (take-home vs. live coding vs. system design) changes everything — most prompt libraries ignore that. The "intersection of my weak skills × likely questions" step turns prediction into a prioritized action list for the next 48 hours. The "if the gap is too large, say so" clause is the anti-bluff move: better to walk in knowing you'll get mauled on one question than to pretend the prep was enough.

---

## Prompt 3 — Case interview (consulting, strategy, PM case rounds)

```
You are a former [CONSULTING FIRM / PRODUCT LEADER] partner / principal who
has run 200+ case interviews. You grade candidates on structure, business
judgment, quantitative comfort, and how they handle new information mid-case
— not on whether they arrive at "the" answer.

Inputs:
- Role I'm interviewing for: [JOB TITLE]
- Type of case expected: [CHOOSE — management consulting (market sizing,
  profitability, market entry, M&A) · product sense (should [COMPANY] build
  X?) · strategy case · operations case · data / analytics case · other]
- Company: [COMPANY NAME]
- Industry focus if known: [INDUSTRY — or "unknown, give me generalist
  prep"]
- My background: [PASTE RESUME OR SUMMARY]
- Specific case topic the recruiter flagged (if any): [PASTE OR "NONE
  FLAGGED"]

Do the following:

1. Generate 5 realistic case prompts I should expect at this type of round,
   each 3–5 sentences long, worded the way an interviewer would actually
   open them. Make them varied — don't give me 5 profitability cases.

2. For each case, write out:
   - The first 60 seconds of my answer (the structuring move — the framework
     I'd lay out, adapted to THIS case, not the MBA-textbook version).
     Write this in first person as if I'm speaking.
   - The 3–5 clarifying questions I should ask before diving in. Order them
     by which matters most if the interviewer will only let me ask 2.
   - The 2 most common failure modes on this case (e.g., "diving into
     numbers before structuring", "framework-dumping without connecting to
     the specific client", "missing the second-order effect")

3. Then pick the hardest of the 5 and walk me through it end-to-end, in
   this format:
   - Structure (the top 3–4 buckets I'd analyze, named and justified in one
     line each)
   - Key numbers I'd need to make reasonable estimates about (with a
     defensible back-of-envelope assumption for each)
   - The 1–2 insights the case is really testing for
   - How I'd land the recommendation in 2–3 sentences

4. Flag any bucket that most candidates overlook and explain why it matters.

Constraints:
- Do not default to generic MBA framework-speak ("Porter's Five Forces",
  "SWOT") unless the framework genuinely fits the case. Frameworks are
  scaffolding, not the answer. If you use one, adapt it to THIS case.
- Do not pretend to know proprietary [COMPANY] cases. Estimate based on
  public signals or say "I don't have specific data on [COMPANY]'s cases,
  here's a representative one for the industry."
- Do not invent numbers and present them as facts. For estimates, label
  them "reasonable estimate" and show the back-of-envelope math.
- Before you deliver the walk-through in step 3, state in one sentence
  what the case is really testing. If you can't name it, restructure your
  answer before delivering.
```

**Why this prompt works:** Case prep libraries are everywhere — and most produce the same MBA-framework mush that interviewers have been trained to see through. Three differentiators here: first, the "first 60 seconds in first person" forces the AI to script the actual structuring move, not describe it; second, the "what is this case really testing" quality gate before the walk-through makes the AI commit to a thesis; third, the "label estimates and show the math" clause trains you to flag your own assumptions the way a real case interviewer wants to hear.

---

## Prompt 4 — STAR answer structuring (turn a rough story into a tight answer)

```
You are an interview coach who has rewritten thousands of STAR answers.
You cut, you don't pad. You tell candidates when their story is the wrong
story for the question.

Inputs:
- The behavioral question I'm answering: [PASTE THE EXACT QUESTION]
- My rough story (brain-dump, 3–10 sentences, messy is fine): [PASTE]
- Role I'm interviewing for: [JOB TITLE]
- The trait or skill this question is testing (if I know): [e.g., "conflict
  resolution", "ownership" — or "not sure"]

Before you write the STAR answer, do these two checks:

CHECK 1 — Is this the right story for this question?
State in one sentence what this question is actually testing. Then say
whether my story is strong, okay, or weak evidence for that trait. If it's
weak, tell me to pick a different story rather than rewriting this one.

CHECK 2 — What's the single "so what" of this story?
In one sentence, name the outcome or insight the story builds toward. If
you can't name a clear "so what", my story probably doesn't have one — tell
me what's missing rather than papering over it.

If both checks pass, write the STAR answer:

- **Situation** (1–2 sentences, max 30 words): the context the listener
  needs. No background dump. No "so basically what happened was…"
- **Task** (1 sentence, max 20 words): what I specifically was responsible
  for. Not what the team was doing — what I owned.
- **Action** (2–4 sentences, 60–100 words): the specific things I did, in
  first person, with verbs that show decision-making (decided, pushed back,
  escalated, cut, pivoted, built). Not "we".
- **Result** (1–2 sentences, max 40 words): what changed, with a number or
  concrete outcome where honestly possible. If there's no number, give a
  specific qualitative outcome that can be verified.

Length target: 90–140 seconds spoken (roughly 180–260 words written).

After the answer, give me:
- One follow-up question the interviewer is likely to ask based on this
  answer
- The one sentence in my story that's the "load-bearing" sentence — the one
  that carries the signal. If the interviewer cuts me off after 45 seconds,
  this sentence is the one I have to land.

Constraints:
- Do not invent details, numbers, or dialogue I didn't provide. If the
  story needs a number to be strong and I didn't give you one, tell me
  what to find rather than making one up.
- Do not write "We" when you mean "I". This question is about me. If the
  story is genuinely a team story, flag it as a risk and suggest where I
  can legitimately say "I" without overclaiming.
- Do not use "I was able to…". Use "I did". Cut hedges.
```

**Why this prompt works:** Most STAR prompts just reformat bad stories into STAR shape. This one refuses to start until two checks pass — is this the right story, and does it have a clear "so what." The "load-bearing sentence" at the end is the secret weapon: if the interviewer interrupts at 45 seconds, you already know the one sentence you have to land. The "we vs. I" ban kills the single most common team-story failure mode that makes candidates sound like passengers.

---

## Prompt 5 — Weakness reframe (answer the trap question without lying)

```
You are a hiring manager who has heard every version of the "biggest
weakness" answer. You immediately catch humble-brags ("I work too hard"),
non-answers ("I'm too detail-oriented"), and disclosure landmines (genuine
red flags a candidate shouldn't share). You help candidates land an answer
that's honest, specific, and safe.

Inputs:
- Role I'm interviewing for: [JOB TITLE]
- The 1–3 weaknesses I've been considering talking about: [PASTE — if I
  haven't picked one yet, write "help me find one"]
- The top 2 qualifications the JD is looking for: [LIST]
- Anything specifically NOT to mention (e.g., a past firing, an unrelated
  mental health issue, a visa complication): [LIST — or "nothing to flag"]

Do the following:

CHECK FIRST — is each weakness I listed interview-safe?
For each weakness I proposed, tag it:
- ✓ Safe and usable — honest, specific, not core to the JD's top qualifications
- ⚠ Risky — it's a humble-brag or non-answer; interviewer will see through it
- ✗ Disclosure landmine — this reveals something that will hurt me in this
  role; do not use

Explain each tag in one sentence.

If I said "help me find one," skip the check step and propose 3 weaknesses
that are genuinely mine-to-claim based on my resume and the JD — specific,
honest, and not disqualifying for this role.

Once we've landed on one safe weakness, write the answer (75–110 seconds
spoken, roughly 150–220 words written), structured as:

1. The weakness, named specifically. Not "I struggle with" — say what the
   actual failure mode looks like in practice. One concrete behavior or
   pattern.

2. A real example of when it showed up (2–3 sentences). Use first person,
   be specific, include the situation and the consequence. Do not sanitize
   it so much that the weakness disappears.

3. What I'm doing about it (3–4 sentences). This is the load-bearing part.
   Name the specific tactic, tool, habit, feedback mechanism, or process
   change I've put in place. Show evidence of improvement with a concrete
   example or outcome — not "I've been working on it."

4. One honest sentence that acknowledges it's still a work in progress,
   because claiming a weakness is fully fixed reads as either dishonest or
   not a real weakness.

Constraints:
- Do not use the phrases "I work too hard", "I'm a perfectionist", "I care
  too much", "I overprepare". These are interview clichés; they signal
  I'm performing rather than answering.
- Do not pick a weakness that's actually a core requirement of the role.
  If I'm applying for a sales role, "I'm not great at talking to strangers"
  is not the weakness I want on the record.
- If the safest weakness I listed is too mild to sound like a real
  weakness, tell me directly — an interviewer hearing a non-weakness
  counts it as evasion, not humility.
```

**Why this prompt works:** Weakness questions are a trap for two reasons — candidates give humble-brags (interviewers hate these) or they accidentally disclose something that gets them cut. This prompt refuses to write an answer until each proposed weakness is tagged safe/risky/landmine, which catches both failure modes before they get spoken in the room. The banned-phrase list ("I'm a perfectionist", "I care too much") kills the exact clichés that signal to a seasoned interviewer that the candidate is performing. The final "still a work in progress" line is what separates an honest answer from a rehearsed one.

---

## Prompt 6 — "Why this company?" research (answer the most-skipped question well)

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

## Prompts 7–12 *(scheduled for Day 5: closing questions · salary screen · panel prep · thank-you · reverse-interview · red-flag detection)*

## AI-grilling rehearsal workflow *(scheduled for Day 5)*

## Answer-scoring prompt *(scheduled for Day 5)*
