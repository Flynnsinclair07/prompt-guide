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

## Prompt 4 — Referral version *(draft scheduled for day 3)*

---

## Prompt 5 — Cold application (no referral, no recruiter) *(draft scheduled for day 3)*

---

## Prompt 6 — Follow-up (after submitting, after the interview) *(draft scheduled for day 3)*

---

## 3 templates *(scheduled for day 3)*
- 1-page classic
- Story-driven
- Brief-and-punchy (under 200 words)

## "What hiring managers actually skim for" cheat sheet *(scheduled for day 3)*
