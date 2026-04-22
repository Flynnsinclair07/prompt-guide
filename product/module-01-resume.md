# Module 1 — Resume

**8 prompts · ATS optimization checklist · 3 before/after examples**
All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o).

---

## How to use this module

Every prompt below is a copy-paste block. Replace the bracketed placeholders `[LIKE THIS]` with your actual inputs. Paste the entire prompt (including your inputs) into ChatGPT as one message.

**Always give ChatGPT your raw material first** — job description, your experience bullets, your draft. Prompts run on blank slate produce generic output. That's the #1 reason AI resumes get flagged.

---

## Prompt 1 — Resume from scratch (tailored to one role)

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

## Prompt 2 — Resume rewrite (fix an existing draft)

```
You are a senior resume coach. Rewrite my resume below to be stronger, more concise, and better optimized for this job description.

Job description:
[PASTE THE JOB DESCRIPTION]

My current resume (full text):
[PASTE YOUR CURRENT RESUME AS PLAIN TEXT]

Apply these edits:
1. Replace every weak verb ("responsible for", "worked on", "helped with", "assisted") with a specific action verb
2. Quantify every bullet where possible — add a number, percentage, dollar amount, or scale indicator
3. Add 3–5 keywords from the JD that are missing from my resume, woven naturally into existing bullets (do not fabricate new experience)
4. Tighten the summary section to 2–3 sentences, leading with the most relevant thing for this JD
5. Flag any bullet that is too vague to save; suggest what I should provide to make it stronger

Output the rewritten resume in plain text, then at the bottom list every change you made with a one-line reason.
```

**Why this prompt works:** The "list every change with a reason" footer creates a review trail — you see exactly what ChatGPT did and can reject anything that feels off. The "flag bullets too vague to save" instruction stops ChatGPT from fabricating filler to paper over genuine gaps.

---

## Prompt 3 — Bullet rewrite (single bullet at a time)

```
Rewrite the following resume bullet to be more specific, quantified, and action-oriented. Give me 3 distinct versions ranging from tight (≤15 words) to detailed (≤25 words).

Original bullet:
[PASTE ONE BULLET]

Context (optional but helpful):
- My role: [YOUR JOB TITLE]
- The team size I led / worked with: [NUMBER]
- The business outcome the work enabled: [ONE SENTENCE]
- Any metrics I can reference: [LIST ANY NUMBERS, %s, $s]

Constraints:
- Every version starts with a strong action verb
- Every version includes at least one number if the context allows
- Do not invent metrics I didn't provide
- No corporate jargon: no "synergized", "leveraged", "spearheaded", "drove value"
```

**Why this prompt works:** Three versions at different lengths lets you A/B against your real resume's line-budget. The banned-jargon list kills the exact clichés that signal "AI-written" to experienced recruiters (most prompts produce these by default).

---

## Prompt 4 — ATS keyword injection

```
I need to insert missing keywords from this job description into my resume without sounding forced or fake.

Job description:
[PASTE JD]

My current resume:
[PASTE RESUME TEXT]

Do the following:
1. Pull the 15 most important keywords and phrases from the JD (hard skills, tools, methodologies, certifications, industry terms). Ignore filler ("team player", "self-starter").
2. Show me which of those 15 already appear in my resume (exact match or close variant).
3. For the missing keywords, suggest where in my resume to add each one — which bullet or section — and give me the rewritten version of that line with the keyword woven in. If a keyword can't be truthfully added based on my experience, flag it and do not force it.

Output format:
- Keyword list (15 total) with ✓ / ✗ / ? marks (present / missing / partial)
- For each ✗, the exact before/after of the bullet or section I should edit
- For each flagged ? or skipped keyword, a short note explaining why
```

**Why this prompt works:** Structured output (✓/✗/?) makes this a checklist, not a wall of text. Most ATS-keyword advice is generic ("add keywords!"). This prompt extracts the specific ones from this specific JD and tells you exactly which line to edit.

---

## Prompt 5 — Quantify achievements (when you don't know the numbers)

```
I'm stuck quantifying my resume bullets. For each bullet below, ask me 2–3 clarifying questions that would help me attach a number, percentage, dollar amount, or time savings.

Questions should be specific and answerable — things I likely know or can estimate. Examples of good questions: "How many people were on the team?" "What was the before-state baseline?" "How often did the process run?" Bad questions: "What was the impact?" (too vague).

After I answer, rewrite each bullet using my numbers.

My bullets:

1. [BULLET 1]
2. [BULLET 2]
3. [BULLET 3]
4. [BULLET 4]
5. [BULLET 5]
```

**Why this prompt works:** Flips the interaction — ChatGPT interviews you instead of guessing. Most people have the numbers but don't know which ones matter for a resume. The question-first structure surfaces the numbers you already know but hadn't thought to include.

---

## Prompt 6 — Career-switcher angle (emphasize transferable skills)

```
I'm switching from [CURRENT FIELD] to [TARGET FIELD]. My current resume reads like a [CURRENT FIELD] resume, which makes me look unqualified for [TARGET FIELD] roles.

Job description for the target role:
[PASTE JD]

My resume (current):
[PASTE RESUME TEXT]

Rewrite my resume to emphasize the transferable skills and outcomes that matter for [TARGET FIELD], while being fully honest about my background. Specifically:

1. Rewrite the professional summary to position me as a [TARGET FIELD] candidate with unusual background in [CURRENT FIELD] as a strength (not a gap)
2. For each experience bullet, reframe the outcome in language that a [TARGET FIELD] hiring manager would recognize (use the JD's vocabulary)
3. Surface any project, side work, certification, or volunteer experience that's more relevant to [TARGET FIELD] than my main job — even if it's small
4. Identify the 2–3 biggest gaps between my background and the JD, and suggest concrete, low-cost ways to close them in the next 4–8 weeks (certification, side project, portfolio piece)

Do not invent experience. Reframing only.
```

**Why this prompt works:** Career-switchers need positioning, not just rewriting. The "unusual background as a strength" instruction stops ChatGPT from hiding your past (which reads as evasive) and instead leans into the switch as a story. The gap-closing suggestions at the end turn this from a resume prompt into a career-planning one.

---

## Prompt 7 — Executive summary (the top 3 lines that matter most)

```
Write 5 different executive summary options for the top of my resume. Each should be 2–3 sentences, ATS-friendly, keyword-dense, and tailored to this specific role.

Role:
[JOB TITLE AT COMPANY]

Job description:
[PASTE JD]

Key inputs about me:
- Years of experience in [FIELD]: [NUMBER]
- 2–3 most relevant accomplishments: [BULLET LIST]
- What I'm known for / my differentiator: [ONE SENTENCE]
- What I'm targeting: [SENIORITY LEVEL / DOMAIN / COMPANY TYPE]

Make the 5 options distinct in tone:
1. Results-first (lead with a big quantified win)
2. Skills-first (lead with hard-skill alignment to the JD)
3. Story-first (one-sentence narrative about my path)
4. Industry-expert (lead with domain depth and reputation)
5. Hybrid (balanced — any of the above)

For each, explain in one sentence which type of role/hiring manager it fits best.
```

**Why this prompt works:** Most resumes die in the first 3 lines. Giving you 5 styles to choose from (instead of one "best" version) means you can match the summary to the company culture — a results-first summary for a sales role, a story-first summary for a storytelling-oriented brand. The "which role it fits best" note turns this into a positioning exercise.

---

## Prompt 8 — LinkedIn → resume converter

```
Convert my LinkedIn profile below into a one-page ATS-readable resume tailored to the attached job description.

My LinkedIn profile (copy-paste everything: headline, about, experience, education, skills):
[PASTE LINKEDIN PROFILE TEXT]

Job description:
[PASTE JD]

Transform as follows:
1. Drop LinkedIn-specific fluff: the first-person "about" narrative, endorsement counts, featured media descriptions, recommendation quotes
2. Compress experience bullets — LinkedIn allows long paragraphs; resumes need 1 line per bullet, 4–5 bullets per role, action-verb leads, quantified outcomes
3. Pull keywords from the JD and weave them into the resume where my LinkedIn experience supports them
4. Rewrite the About section into a 2–3 sentence professional summary
5. Format as plain text: no emoji, no bullet symbols other than hyphens, no section dividers other than blank lines

Output the finished resume, then list the 5 biggest changes you made (LinkedIn → resume) and why.
```

**Why this prompt works:** LinkedIn and resumes are fundamentally different formats — LinkedIn rewards voice and narrative; resumes reward compression and keywords. Most people paste their LinkedIn into a resume template and wonder why it doesn't work. This prompt runs the transform deliberately and shows you what was cut.

---

## ATS optimization workflow — 5-step checklist

Run through this for every resume before you submit.

**1. Keyword density**
- Pull the top 15 keywords from the JD (hard skills, tools, certifications, methodologies, industry terms)
- Your resume should hit ≥10 of them with exact or near-exact match
- Paste resume + JD into ChatGPT with Prompt 4 to verify

**2. Section order**
- Top-to-bottom: Name/contact → Summary → Experience → Education → Skills
- No "Objective" section (dated, wastes space)
- Skills at the bottom or top depending on role seniority; mid-career and later go bottom

**3. Formatting**
- One column, left-aligned
- No tables, text boxes, icons, graphics, headshots
- Consistent bullet symbol (hyphen or standard bullet), no emojis
- Standard fonts only: Arial, Calibri, Georgia, Times New Roman, Helvetica

**4. File type**
- **Submit as .docx** unless the posting explicitly requires PDF
- Parsers handle .docx better than PDF for keyword extraction
- Exception: Greenhouse, Lever, and Workday ATS systems handle both fine — default to .docx anyway

**5. Scan test**
- Copy your resume text from the .docx into a plain-text editor (TextEdit, Notepad, or https://jobscan.co free tier)
- If you see broken formatting, weird characters, or the section order scrambles — that's what the ATS sees, and you need to fix it

---

## Before/after examples

*(Scheduled for day 2 of build — 3 examples: entry-level · mid-career switcher · senior)*
