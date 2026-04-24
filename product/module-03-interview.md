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

## Prompt 7 — Closing questions to ask (the last 5 minutes of the interview)

```
You are a senior hiring manager who has run 400+ interview loops. You
silently grade candidates on the questions they ask at the end — that's
where you see how they actually think, whether they've done the work, and
whether they'll be a pain to manage. Candidates who ask generic questions
("What's the culture like?") lose ground they can't recover.

Inputs:
- Role I'm interviewing for: [JOB TITLE]
- Seniority: [IC · senior IC · staff · manager · director · VP]
- Who I'm interviewing with RIGHT NOW: [CHOOSE — recruiter · hiring
  manager · peer · cross-functional partner · skip-level · founder/CEO]
- Company: [COMPANY NAME]
- Company stage: [e.g., "Series B, 120 people" or "public, 5000+"]
- Job description: [PASTE]
- Things the interviewer mentioned during the conversation that I want to
  dig deeper on: [LIST — OR "NONE STOOD OUT"]

Do the following:

1. Generate 12 closing questions I could ask THIS specific interviewer type.
   Each question must be:
   - Specific enough that it couldn't be asked of 10 other companies
   - Calibrated to the interviewer's role (I should ask a peer about day-to-
     day reality; I should ask a hiring manager about the 6-month bar; I
     should ask a skip-level about strategy)
   - Phrased as a real question, not a job-interview-question-dressed-as-a-
     question ("What are the biggest challenges facing this role?" is the
     latter — don't write those)

2. Tag each question with:
   - What it signals about me (e.g., "shows I've thought about scale",
     "shows I'm already doing the job in my head", "shows I care about
     team health not just prestige")
   - A risk level: ✓ safe · ⚠ only-if-it's-landing · ✗ skip unless it's
     clearly the right interviewer

3. Pick the top 3 for THIS interviewer specifically and explain why each
   lands for this role/stage in one sentence.

4. Pull 2 questions from my earlier-in-the-conversation list (the things
   the interviewer mentioned) that would show I was actually listening.
   Reference the specific thing they said. If I wrote "none stood out,"
   skip this step — and tell me that's a problem worth fixing next round.

Constraints:
- Do not include any of these: "What's the culture like?", "What's the
  biggest challenge?", "What does success look like in this role?", "Can
  you tell me about the team?" — these signal I didn't prep.
- Do not invent things the interviewer "probably cares about" — use what's
  in my inputs or infer carefully from the JD and cite it.
- Do not ask about salary or benefits here. Those are a separate
  conversation with the recruiter, not the hiring manager.
```

**Why this prompt works:** Closing questions are where the interview's grade gets locked in, and most candidates walk in with the same four dead questions. The per-interviewer-role calibration is the move — a peer wants different questions than a VP, and generic prep ignores that. The "safe / only-if-landing / skip" risk tag catches the specific failure mode of asking a great question to the wrong person. The banned-question list kills the exact phrasings that telegraph a candidate didn't prepare.

---

## Prompt 8 — Salary screen (the recruiter's first money question)

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
- Do not volunteer my CURRENT salary. The current-salary question is
  illegal in many states and cities (check your state's salary history
  ban status). Regardless of legality, volunteering your current salary
  almost always anchors you low — decline politely and pivot to your
  target range.
- If my situation is "UNEMPLOYED," adjust the scripts to avoid anchoring
  to zero — market rate is the anchor, not my current state.
```

**Why this prompt works:** The salary screen is the single highest-leverage 5 minutes in the entire process — a wrong number here locks the ceiling for the whole offer. The pre-output reality check ("is your target realistic? is your research done?") refuses to write scripts until the user has what they need to defend their range. The three-scenario split is the thing most prompts miss: the right answer changes depending on where you are in the loop. The "don't volunteer current salary" clause is a legal-and-strategic safeguard that even coaches sometimes forget to flag.

---

## Prompt 9 — Panel / multi-interviewer prep (one loop, 4–6 different heads)

```
You are an interview-loop coach who has run hundreds of full-day panel
rounds at companies with rigorous hiring bars. You know each interviewer
is grading a different signal, and a candidate who plays them all the same
loses ground with every round. You help candidates map the signals, prep
once for the whole loop, and walk in knowing what each hour is really
about.

Inputs:
- Company: [COMPANY NAME]
- Role: [JOB TITLE]
- Seniority: [IC · senior · staff · manager · director · VP]
- Job description: [PASTE]
- The panel schedule I received (titles/roles, not names if I don't have
  them): [PASTE THE FULL SCHEDULE — EACH BLOCK + WHO]
- Total duration of the loop: [e.g., "4 hours, 5 rounds"]
- My resume: [PASTE]

Do the following:

1. For each interviewer block in my schedule, generate a signal map:
   - What this interviewer is almost certainly grading (the 1–2 signals
     that matter most for their role — e.g., hiring manager grades job-
     readiness and managerial fit; peer grades day-to-day collaboration
     and technical judgment; skip-level grades strategic thinking and
     growth potential; cross-functional partner grades clarity and mutual
     dependency awareness)
   - The 3 most likely question types for this round
   - The trap specific to this round (e.g., "peer rounds often go too
     informal and candidates reveal opinions that haven't been stress-
     tested", "hiring manager rounds tempt over-explaining the resume")
   - Which of my resume's accomplishments is the strongest fit for THIS
     round's signal — name it specifically

2. Identify the 2–3 signals the loop as a whole is testing that no single
   round covers — cross-round patterns the calibration meeting will use
   to compare me to other candidates. For each, tell me which rounds I
   should plant evidence in and how.

3. Flag the single highest-risk round in my loop and why. If multiple
   rounds look equally risky, say so.

4. Give me a 5-minute between-round reset routine: what to write down from
   the previous round, what to look up for the next round, how to mentally
   transition from one interviewer's register to the next.

Constraints:
- Do not treat every interviewer as interchangeable. A peer and a VP are
  grading fundamentally different things; the same story should be told
  differently to each.
- Do not invent company-specific panel patterns. Base the map on the
  schedule I gave you and reasonable inferences from the JD.
- If my schedule is missing information (e.g., no titles listed), tell me
  the 2–3 questions I should email the recruiter to fill the gaps BEFORE
  the loop — don't just work around the missing data.
```

**Why this prompt works:** A panel loop is a coordinated grading exercise, not a series of independent interviews, and most prep ignores that. The signal map per interviewer is the core move — it tells the candidate what each round is really for, which reshapes which stories they tell where. The "cross-round signals" step is the thing that separates someone who passes a hiring committee from someone who dazzles one interviewer and falls flat with another. The between-round reset routine is operational prep nobody else includes and every candidate needs by hour three of a long loop.

---

## Prompt 10 — Post-interview thank-you (not the email Prompt 6 in Module 2 — this is the one-hour-after version)

```
You are an interview coach who has read thousands of thank-you notes. You
know which ones get forwarded to the hiring manager with "I really liked
this candidate" on top, and which ones get archived unread. The difference
is in the first three lines and whether the candidate actually listened.

This is different from a generic follow-up. This is the 24-hour thank-you
after a conversation that mattered.

Inputs:
- Interviewer's name and role: [FULL NAME · ROLE · COMPANY]
- Round type: [recruiter screen · phone screen · hiring manager · peer
  panel · final · skip-level · founder/CEO]
- The single moment of the conversation I want to build on — a specific
  thing they said, a decision they described, a question that stuck with
  me, a shared reference: [PASTE — be specific, not "they were nice"]
- One thing I didn't get to fully explain or wish I'd said better: [ONE
  SENTENCE — OR "NOTHING — WENT WELL"]
- How they're likely to decide (gut feel · structured rubric · vote with
  panel): [PICK ONE — OR "I DON'T KNOW"]

Do the following:

1. Write the note (email format, no subject-line games). Length by round:
   - Recruiter screen: 60–80 words
   - Hiring manager: 100–140 words
   - Peer: 80–120 words
   - Skip-level or founder: 120–160 words
   - Panel or cross-functional: 90–130 words

2. Structure (required in this order):
   - First line: reference the SPECIFIC moment from the conversation. Not
     "thanks for your time today" — name the thing. One sentence.
   - Second chunk (2–4 sentences): what that moment made me think, or how
     it connected to something I've done. Forward-looking, not
     sycophantic.
   - Third chunk (1–2 sentences): the one thing I want to reinforce about
     my fit for the role — ideally the one thing I didn't land as well as
     I wanted to in the interview itself.
   - Close: one concrete forward-looking sentence, not "thank you for
     your consideration."

3. Subject line: one clean line, 4–8 words. Do not use "Thank you" alone —
   that's what every other candidate writes. Reference the topic.

4. At the bottom, flag any sentence in my note that could read as
   sycophantic or over-eager, and give me a tighter version.

Constraints:
- Do not write "It was great meeting you" — reflexive filler every
  candidate writes.
- Do not apologize for things that went okay. ("Sorry I rambled a bit
  on…") — unless something genuinely bombed, don't call attention to it.
- Do not reuse lines from my cover letter or introduce. This is new
  writing from the conversation we just had.
- Do not send the same template to two interviewers on the same panel.
  Each note should be reference-specific to that conversation.
```

**Why this prompt works:** Generic thank-you notes are spam. This prompt refuses to write one without a specific conversation-moment input, which forces the candidate to actually remember what happened. The length-by-round tuning matches the norm (a 200-word note to a peer reads as try-hard; a 40-word note to a founder reads as careless). The "sycophancy flag" at the end is the self-edit most candidates skip — and the exact thing that gets notes archived unread.

---

## Prompt 11 — Reverse-interview (screen the company before you accept)

```
You are an experienced operator who has worked at 6 companies across the
stage spectrum and joined 2 that you should have screened harder before
saying yes. You help candidates turn the interview into a two-way
evaluation instead of a one-way pitch.

Inputs:
- Company: [COMPANY NAME]
- Role: [JOB TITLE]
- Stage/size: [e.g., "Series C, 400 people" or "public, 5000+"]
- What I've noticed about them so far — good AND concerning: [PASTE
  HONEST LIST]
- My deal-breakers (things I will not accept regardless of comp): [LIST —
  e.g., "no 24/7 on-call", "must be hybrid not full RTO", "manager I can
  actually respect"]
- What I'm most worried about (the specific failure scenario): [ONE
  SENTENCE — e.g., "that I'll be isolated", "that the company runs out of
  money in 12 months", "that the manager is a dick"]
- Who I'll be meeting this round: [CHOOSE — recruiter · hiring manager ·
  peer · skip-level · founder/CEO]

Do the following:

1. Generate 15 reverse-interview questions calibrated to what I'm actually
   worried about and who I'm talking to. Each question should:
   - Target a specific thing a company can be vague about (runway, on-
     call load, manager turnover, promotion rhythm, layoff history, scope
     creep, who the role exists for)
   - Be answerable in 2–4 sentences — not open-ended "tell me about…"
   - Surface real information, not comfort-answers

2. Organize the 15 into 4 buckets and name each:
   - Business health / longevity
   - Role reality (day-to-day, workload, expectations)
   - Manager and team quality
   - Growth / exit / advancement path

3. Rank the 15 by signal strength — which questions produce the most
   useful information regardless of how the person answers. The gold
   questions are the ones where HOW they answer (hesitation, specificity,
   who they blame) tells me more than the content.

4. For the 5 highest-signal questions, tell me what a GOOD answer sounds
   like, what a WARNING answer sounds like, and what a DISQUALIFYING
   answer sounds like. Be specific.

Constraints:
- Do not include generic softball questions ("What's the team culture
  like?") — those invite rehearsed answers and waste my one chance to
  probe.
- Do not assume the company is a good actor by default. Some of the best
  information comes from questions designed to catch evasion.
- If my "most worried about" input is vague, say so — a vague worry
  produces vague questions. Push me to name the specific scenario before
  you write questions.
- Do not write questions that would read as adversarial if overheard.
  These need to land as "I'm doing due diligence," not "I'm grilling you."
```

**Why this prompt works:** Most candidates treat the interview as one-way — they get asked, they don't ask back. That's how people end up at jobs they should have avoided. The differentiator here is the "good answer / warning answer / disqualifying answer" rubric on the top 5 — it teaches the candidate to read the room, not just collect data. The "gold questions are the ones where HOW they answer tells you more than WHAT they say" framing is the move that turns reverse-interviewing from a checklist exercise into a real evaluation.

---

## Prompt 12 — Red-flag detection (decode the warning signs in what they actually said)

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

## AI-grilling rehearsal workflow

Three-round structure for practicing behavioral and role-specific answers out loud with ChatGPT acting as the interviewer. Run this 1–2 days before the real interview. Use it on the answers you built with Prompt 4 (STAR structuring).

### Round 1 — Warm-up (confidence and pacing)

Prompt to paste into ChatGPT:

```
You are interviewing me for a [JOB TITLE] role at [COMPANY]. You're a
hiring manager, neutral tone, no follow-up probes yet. Ask me one
behavioral question. After I answer, give me ONLY:
- Did I hit the 90–140 second mark? (actual estimate in seconds)
- Did the answer have a clear "so what"? Yes / No / Partial
- One sentence on what the answer was missing, if anything

Do not yet pressure-test me. This is warm-up. Ask a standard question from
this list and wait for my answer: [PASTE 5 STANDARD QUESTIONS YOU EXPECT —
PULL FROM PROMPT 1 OUTPUT].

When you ask, use one line only. Do not preamble.
```

**Goal of Round 1**: get comfortable answering out loud, calibrate length, check for a clear "so what." Run 3–5 questions. Re-prompt the same question if your first answer rambled.

### Round 2 — Pressure (follow-up probes and clarifying challenges)

Prompt to paste:

```
Same interview continues, but now you probe. After I answer each question,
ask ONE follow-up that challenges a weak point in my answer. Examples of
good follow-ups:
- "That sounds like the team's win — what did YOU specifically do?"
- "What would you have done differently?"
- "You said [X]. How did you actually measure that?"
- "Walk me through the moment you realized [Y] wasn't working."

Do not soften. Do not give feedback yet. Just probe. After 3 rounds of
question + follow-up, pause and give me the single weakest moment across
all my answers and what specifically was weak about it.

Start with one question, wait for my answer, then probe.
```

**Goal of Round 2**: find the seams. Most answers fall apart on the second follow-up ("can you say more about how YOU specifically drove that?"). This round exposes those seams before a real interviewer does.

### Round 3 — Curveballs (questions I didn't prep for)

Prompt to paste:

```
Same interview. Ask me 5 questions I likely haven't prepared for —
unusual behavioral questions, edge cases from the JD, hypotheticals, or
deliberate attempts to catch me off-script. Examples:
- "Tell me about a time you were wrong about something important."
- "What's something your last manager would say you could do better?"
- "Hypothetical: [scenario specific to THIS JD]. Walk me through your
  first 30 days."
- Any question that targets an INFERRED gap in my resume — surface the
  question the interviewer might silently have.

For each, after I answer, give me:
- A 1–10 score on structure, specificity, and confidence
- The one thing that would have made the answer stronger
- Whether the answer would land with this specific role

At the end of the 5, tell me the single biggest pattern across my curveball
answers — the gap I need to close before the real interview.

Role: [JOB TITLE]
Company: [COMPANY]
JD: [PASTE]
Resume: [PASTE]
```

**Goal of Round 3**: catch the unscripted-you failures. If you can survive a curveball round and hold your structure, you're ready.

### How to run the whole workflow

- Total time: 60–90 minutes, out loud, in a room alone or on a walk
- Record yourself on your phone for Round 2 and Round 3 — listening back is uncomfortable and the most efficient prep there is
- Do this 24–48 hours before the real interview, not the morning of
- After each round, paste any answers that scored <7 back into the Answer-Scoring Prompt below for a rewrite

---

## Answer-scoring prompt (grade and rewrite one answer at a time)

Use this after the rehearsal workflow, or on any answer you want to upgrade. This is the repair prompt — it takes one answer and returns a stronger one.

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
