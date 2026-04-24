# Module 2 — Cover Letter

**6 prompts · 3 templates · "what hiring managers actually skim for" cheat sheet**
All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o).

---

## When to use this module

Cover letters are dead in some industries (most software engineering roles), alive in others (comms, marketing, ops, anything with a writing sample component), and mandatory in a few (academia, nonprofits, government, some exec roles). When they're required, a good one is a disproportionate unlock — most applicants submit a template with "I am writing to express my interest" at the top. Yours doesn't have to.

**Rule of thumb**: if the posting asks for one, write one. If it's optional, write one for any role you'd be upset to lose. If it's not mentioned, skip it unless you're switching industries, coming back from a gap, or know the hiring manager's name.

---

## Prompt 1 — Hook-first opener (the anti-template)

```
Write the first paragraph of a cover letter for a [JOB TITLE] role at [COMPANY].

The opener must NOT:
- Start with "I am writing to express my interest"
- Start with "As a [job title] with X years of experience"
- Start with "I am excited to apply for"
- Recite my resume
- Mention the job posting or where I saw it

The opener MUST:
- Be 2–4 sentences, 45–75 words
- Open with a concrete moment, number, or observation about [COMPANY] or its market
- Show I've done 10+ minutes of research (reference a product decision, recent
  launch, public metric, podcast appearance, changelog post, or public writing)
- Land on a single sentence that connects a specific thing I've done to a
  specific thing [COMPANY] is working on right now

Inputs:
- Company: [COMPANY NAME]
- What they do / their bet: [1–2 SENTENCES]
- Something specific they did recently that I noticed: [URL OR DESCRIPTION]
- One thing I've done that's directly relevant: [ONE SENTENCE]

Generate 3 distinct opener options — each different in angle and tone. For
each, write one line below it naming which hiring manager personality it
would land best with (e.g., "numbers-driven VP", "craft-obsessed founder",
"pragmatic ops lead").
```

**Why this prompt works:** The banned-phrase list is the whole point. ChatGPT's default cover letter opener is a template nobody reads. Forcing it away from the defaults — and onto a concrete moment or research signal — makes the first 5 seconds worth reading. The "3 options tuned to different reader personas" step saves you from the wrong-register problem (e.g., a witty opener sent to a numbers-driven VP).

---

## Prompt 2 — Mirror-the-JD (the keyword-aligned body)

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

## Prompt 3 — Industry-switcher version (addressing the elephant directly)

```
I'm applying for a [TARGET JOB TITLE] role at [COMPANY], switching from
[CURRENT INDUSTRY / ROLE] to [TARGET INDUSTRY]. My resume shows the switch
isn't a natural fit on paper, so the cover letter has to do the positioning
work.

Write a full one-page cover letter (300–380 words) that does the following:

1. Opening (45–75 words): lead with ONE specific observation about [COMPANY]
   or [TARGET INDUSTRY] that reveals I've done real homework — not a generic
   "I've always been fascinated by" line. No apology for the switch.

2. Body paragraph 1 (80–120 words): the "why I'm credible for this" pivot.
   Name the 2–3 transferable skills from my background that map to this role.
   For each, give one concrete example with a number or outcome. Frame my
   unusual background as a specific advantage for [TARGET INDUSTRY], not a
   gap to overlook.

3. Body paragraph 2 (80–120 words): evidence that I'm already operating in
   [TARGET INDUSTRY] mentally and practically — list any side project,
   course, certification, writing, community involvement, or freelance work
   that's pointed this direction. If I don't have much yet, name what I'm
   doing in the next 60 days to close the gap.

4. Closing (40–60 words): specific and forward-looking. What I'd want to dig
   into in the first conversation. No "thank you for your consideration"
   autopilot.

Inputs:
- Current field: [e.g., classroom teaching, clinical nursing, investment
  banking, restaurant management]
- Target field: [e.g., product management, UX research, data analytics]
- Target role JD: [PASTE]
- My resume: [PASTE]
- Any side projects, self-study, or community involvement pointing toward
  the new field: [LIST — OR WRITE "NONE YET" IF HONEST]
- The single strongest transferable outcome from my current work: [ONE
  SENTENCE WITH A NUMBER IF POSSIBLE]

Constraints:
- Do not apologize, hedge, or use the word "transition" (overused)
- Do not invent experience or credentials I didn't provide
- If my "current field → target field" pivot has a common failure mode that
  the hiring manager is likely worried about, address it directly in one
  sentence rather than avoiding it

After the letter, list the 2–3 objections you anticipated from the hiring
manager and the specific sentence in the letter that answered each.
```

**Why this prompt works:** Most industry-switcher cover letters try to hide the switch, which reads as evasive. This prompt does the opposite — it names the pivot in the first sentence of the user's input and positions it as an advantage. The "list the objections you anticipated and what sentence answered each" footer forces the letter to actually do the defensive work rather than hoping the hiring manager won't notice. The ban on the word "transition" kills the single most overused word in switcher cover letters.

---

## Prompt 4 — Referral version (someone warm-introduced you)

```
Someone I know is referring me internally for a [JOB TITLE] role at [COMPANY].
Write a cover letter that uses the referral without burning the referrer's
goodwill or making me sound like I'm trading on their name instead of my own
qualifications.

Inputs:
- Referrer's name: [FULL NAME]
- My relationship to the referrer: [e.g., "former manager at X", "college
  classmate", "met at Y conference", "they're a current employee I DM'd"]
- How strongly they can vouch for me: [CHOOSE ONE: "worked with me closely
  and would go to bat" · "knows my work second-hand" · "barely knows me but
  agreed to forward my resume"]
- Did the referrer actually say something specific about why I'd fit? If yes,
  paste it here: [THEIR WORDS, OR "THEY DIDN'T SAY ANYTHING SPECIFIC"]
- Job description: [PASTE]
- My resume: [PASTE]

Write a full one-page cover letter (280–350 words) structured as:

1. Opener (40–60 words): name the referrer in the FIRST sentence with the
   right degree of warmth. Do not oversell the relationship. If they barely
   know me, say "X mentioned the team was hiring" — not "X and I have worked
   together extensively."

2. Body paragraph 1 (100–130 words): pivot quickly off the referral and onto
   my own evidence. Identify the top 2 things this role needs based on the
   JD, and map each to a specific thing I've done (with a number where
   possible). The referral got me in the door; this paragraph has to carry
   me from there.

3. Body paragraph 2 (80–110 words): one concrete story, 3–5 sentences, about
   a problem I solved that's structurally similar to what this role will
   face. Name the situation, what I did, and what changed.

4. Closing (40–60 words): specific and forward-looking. Mention the
   referrer once more, lightly (e.g., "If it's useful, [REFERRER] can speak
   to [SPECIFIC TRAIT]"). End with a concrete next step, not a thank-you.

Hard rules:
- Name the referrer in sentence 1, once in the middle if natural, and at most
  once in the closing — total mentions capped at 3
- Do not claim the referrer "highly recommended" or "thinks I'd be perfect"
  unless they said that exact thing in the inputs above
- Do not write a letter that would embarrass the referrer if they read it
- If my relationship to the referrer is weak (option 3 above), the cover
  letter must carry 90% of its own weight — write as if the referral got me
  opened but the letter has to earn the interview alone
```

**Why this prompt works:** Referrals are the highest-leverage cover letter type and the one people most often blow. Two common failure modes: overselling the relationship (which the referrer hates, because it lands back on them) and leaning on the name so hard that the letter itself has no substance. The "cap at 3 mentions" rule and the "weak/strong relationship" input force the prompt to calibrate tone to the actual relationship, not the candidate's wishful thinking.

---

## Prompt 5 — Cold application (no referral, no recruiter, no insider)

```
I'm applying cold to a [JOB TITLE] role at [COMPANY] — no referral, no prior
relationship, no recruiter reaching out. My cover letter has to do 100% of
the positioning work.

Inputs:
- Job description: [PASTE FULL JD]
- My resume: [PASTE]
- Why I specifically want THIS company (not "any good company"): [2–4
  sentences — if I can't answer this, the prompt will fail]
- One specific thing about the company I noticed in research that goes
  beyond the homepage: [a product decision, a recent launch, a podcast
  appearance from a founder, a Glassdoor pattern, a changelog post, a hiring
  spike in a specific area, etc.]
- The single most relevant thing from my background for this role: [ONE
  SENTENCE WITH A NUMBER OR OUTCOME]

Write a cold cover letter (300–380 words, one page) structured as:

1. Opener (50–75 words): start with the specific research signal, not a
   generic "I'm excited to apply" line. Show you understand what the company
   is actually building — not just what it says on its careers page.

2. Body paragraph 1 (100–130 words): the fit case. Identify the 3 most
   important requirements in the JD and map each to a specific thing I've
   done. Quantified where possible. This paragraph is the reason I get an
   interview.

3. Body paragraph 2 (70–100 words): one short story or moment that shows
   I've already been operating in the problem space the company cares about.
   This can be a side project, a post I wrote, a talk I gave, a customer I
   helped — anything that's evidence I care about this beyond wanting a job.

4. Closing (40–60 words): name one specific thing I'd want to dig into in a
   first conversation. Avoid generic sign-offs.

Constraints:
- Do not write "I came across this role on [job board]" — nobody cares
- Do not use phrases: "I am writing to express my interest", "I believe I
  would be a great fit", "my skills align perfectly", "results-driven",
  "proven track record", "passionate about"
- Every paragraph must give the reader a reason to keep reading. If a
  paragraph only restates my resume, cut it or replace it.
- If, based on my inputs, I don't actually have strong evidence for this
  company specifically, flag that — don't paper over it with flattery

Before the letter, in 2 sentences, tell me the single best argument this
letter makes for me. If you can't name one, rewrite before delivering.
```

**Why this prompt works:** Cold applications are where generic cover letters go to die. Two moves matter most: a research signal that proves 10+ minutes of work, and a single best argument the whole letter is making. The "tell me the single best argument before delivering" step forces the prompt to have a *thesis* — which is the thing cold letters almost always lack. If ChatGPT can't name the argument, the letter isn't ready.

---

## Prompt 6 — Follow-up (after applying · after the interview)

> **Note on Scenarios B and C**: if you're writing a thank-you after an interview that actually mattered, use **Module 3 Prompt 10** instead — it calibrates by round type (recruiter screen through founder/CEO) and includes a sycophancy self-edit this prompt doesn't. Use Scenarios A, D, E here for application nudges, check-ins, and ghosted closes — those have no Module 3 equivalent.

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

## 3 cover letter templates

Three templates, each ~1 page, covering the main stylistic registers. Use these as starting scaffolding when you want structure before you run the prompts, or as reference for how the finished output should be shaped. Fill in the bracketed inputs yourself — the prompts above will produce output that fits into any of these three shapes.

---

### Template A — The 1-page classic (the safe default)

Use when: the company is corporate, the JD is formal, the hiring manager is likely a VP or above, or you have no signal on company culture.

```
[YOUR NAME]
[EMAIL] · [PHONE] · [CITY, STATE]

[DATE]

Hiring Manager
[COMPANY NAME]
[CITY, STATE]

Dear Hiring Manager,

[OPENER — 2–4 sentences, 45–75 words. Start with a concrete research signal
about the company or a clear statement of why THIS role at THIS company.
Avoid "I am writing to express my interest."]

[BODY PARAGRAPH 1 — 80–120 words. The fit case. Identify the top 2–3
responsibilities from the JD and map each to a specific accomplishment from
your resume. At least one quantified outcome. Use 3–4 keywords from the JD
naturally.]

[BODY PARAGRAPH 2 — 70–100 words. One concrete story or example that shows
you've solved a similar problem before. Situation, what you did, outcome.
Keep it tight — this is not the place for a novel.]

[CLOSING — 40–60 words. Forward-looking. Mention one specific thing you'd
want to dig into in a first conversation. Sign off without "thank you for
your consideration" — try "Happy to walk through any of this in more
detail" or "Glad to send samples of [X] if useful."]

Best,
[YOUR NAME]
```

---

### Template B — Story-driven (the memorable one)

Use when: the company culture is informal or founder-led, the role is creative, brand, or mission-aligned, or you have a genuinely strong story that fits the work.

```
[YOUR NAME] · [EMAIL] · [LINKEDIN OR PORTFOLIO URL]

Dear [HIRING MANAGER'S NAME IF YOU HAVE IT, OTHERWISE: team],

[OPENER — 3–5 sentences. Open with a specific moment, not a summary. "Last
spring I spent three weeks watching teachers ignore our dashboard…" is a
legitimate opener. Land on why that moment is relevant to what COMPANY is
building.]

[BODY — 180–260 words across 1–2 paragraphs. This is a single story, not a
list of accomplishments. Tell it in order: setup → complication → what you
did → what changed. The story should naturally surface 2–3 of your most
relevant strengths without listing them. Keyword references should be woven
in, not stacked.]

[BRIDGE — 30–50 words. One short paragraph that connects the story's lesson
to what you'd do at COMPANY. Concrete, not abstract.]

[CLOSING — 30–50 words. Short. Confident. Invite a specific next step —
e.g., "Would love 20 minutes to hear how you're thinking about [X]" — and
sign off.]

[YOUR NAME]
```

---

### Template C — Brief-and-punchy (under 200 words total)

Use when: the company is startup/engineering-heavy, the hiring manager is likely reading on their phone, the JD is short and scrappy, or you've been told by someone inside that "we read the first 100 words and skim the rest."

```
[YOUR NAME] · [EMAIL] · [LINKEDIN]

Hi [NAME OR TEAM],

[OPENER — 1–2 sentences, 20–35 words. One sharp research signal or one
sharp reason. No wind-up.]

[FIT — 3–5 bullet points, each 1 line, each 10–18 words. Each bullet
pairs one JD requirement with one specific thing you've done. Quantify where
possible. Lead bullets with action verbs or nouns, not "I".]

[CLOSING — 1–2 sentences, 20–30 words. Direct. One forward-looking
sentence. No "thank you for considering my application."]

[YOUR NAME]
```

**Rule for Template C**: if the letter is over 200 words, cut. The whole point is that it reads in 30 seconds. If the reader wants more, your resume is attached.

---

## "What hiring managers actually skim for" — 1-page cheat sheet

Most cover letters are read the way you read a LinkedIn profile: 7 seconds, eyes bouncing. Here's what the average hiring manager is actually hunting for in those 7 seconds. Build your letter so these answers are findable *without* reading the full text.

### The 4 things scanned in the first 5 seconds

1. **Is this letter written for THIS job, or recycled?** Signals: company name in the first 1–2 sentences; at least one phrase from the JD in the opener; a research signal that couldn't come from the job posting alone.
2. **Do they have the top 2–3 things the JD asks for?** Signals: those 2–3 requirements appear in the first body paragraph, each paired with a specific experience. If the hiring manager has to go find the evidence, you've lost.
3. **Is there a number?** At least one quantified outcome in the body — ideally in bold, or at least near the top of a paragraph. This is the single easiest thing to add and the most often missing.
4. **Is this one page?** For the classic and story-driven templates, one page. For brief-and-punchy, under 200 words. Anything longer gets skimmed harder and trusted less.

### The 5 things scanned in the next 15 seconds

5. **Does the candidate understand the business?** A sentence that shows you know what the company sells, who to, and what's hard about it right now.
6. **Is there a moment of specificity?** One concrete detail (a project, a client, a number, a tool, a decision) that proves you've actually done the work, not just read about it.
7. **Does this person write like a human?** No "synergize", no "leverage", no "passionate about", no "proven track record". Varied sentence length. A voice.
8. **Is the fit naturally obvious, or are they arguing?** Good letters don't say "I'd be a great fit" — they put the evidence in place so the reader draws the conclusion.
9. **Is the close confident or apologetic?** A forward-looking closing ("Glad to walk through any of this…") outperforms a deferential one ("Thank you for your consideration…") ~every time.

### The 4 automatic rejection signals

10. **Typos, especially in the company name.** Instant no.
11. **Wrong company name or wrong role.** Lethal. Double-check before sending.
12. **Any sentence that reads like a generic template** ("I am writing to express my interest in the [ROLE] position at [COMPANY]"). Templates aren't bad; template *voice* is.
13. **A cover letter longer than a page on a hiring manager's phone screen.** If it takes more than two swipes to finish, you're asking for time nobody gave you.

### The one thing that earns the interview

A cover letter that answers the one question the resume can't: **"Why you, specifically, for this role, right now?"** Everything above is in service of making that answer visible inside 20 seconds of reading.

If your letter doesn't answer that question, rewrite it before sending. If you can't answer it at all, this might not be the right role to apply for — and that's also a useful signal.
