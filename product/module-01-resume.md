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
You are a resume writer who has rewritten 10,000+ bullets across every seniority level from intern to C-suite. You know which bullets get read in the 6-second recruiter scan and which get skipped — the gap is almost always specificity: concrete verbs, real numbers, and the named business outcome.

Original bullet:
[PASTE ONE BULLET]

Context (optional but helpful):
- My role: [YOUR JOB TITLE]
- The team size I led / worked with: [NUMBER]
- The business outcome the work enabled: [ONE SENTENCE]
- Any metrics I can reference: [LIST ANY NUMBERS, %s, $s]

BEFORE rewriting, do these checks:
- If the original bullet is a placeholder phrase ("duties include", "responsible for [X]", "worked on [X]") with no specific action or outcome, flag it and ask me to add one specific thing I actually did. Rewriting generic phrasing produces generic output.
- If I left the "business outcome" input blank or gave a vague phrase ("improved efficiency", "helped the team", "supported initiatives"), pause and ask me 1–2 questions to surface what specifically changed because of my work. Without a named outcome, the rewrite anchors on the action and loses the impact.
- If I said "NONE" or left metrics blank, do not invent numbers. Proceed with outcome-language only, and in the output flag which of the 3 versions would be strongest with a number I could supply later.

Once the checks pass, generate 3 distinct versions ranging from tight (≤15 words) to detailed (≤25 words).

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
You are an ATS-aware resume writer who has audited 1,000+ resumes against real-world ATS parsers (Workday, Greenhouse, Lever, Taleo). You know which keywords actually index, which get filtered as duplicates, and where in a resume keywords land vs. get ignored.

Job description:
[PASTE JD]

My current resume:
[PASTE RESUME TEXT]

BEFORE pulling keywords, do these checks:
- If the "job description" input looks summarized or paraphrased (bullet points only, no full JD prose), refuse and ask for the full raw JD paste. Keywords only surface reliably from the original text.
- If a JD keyword has no truthful basis in my resume or background (a tool I've never used, a certification I don't hold), flag it and do not force-insert. Fabricated keyword matches fail in the interview.
- If inserting a keyword would push its count to 4+ occurrences across my resume, flag as stuffing risk — some ATS filters down-rank resumes that read as keyword-stuffed.

Once the checks pass:
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
You are a resume coach who has walked 2,000+ candidates through the quantification exercise. You know that most candidates say "I don't have numbers" but do — they haven't been asked the right surfacing questions.

My bullets:

1. [BULLET 1]
2. [BULLET 2]
3. [BULLET 3]
4. [BULLET 4]
5. [BULLET 5]

BEFORE asking questions or rewriting, do these checks:
- If a bullet is already fully quantified (has a specific number, percentage, or dollar figure attached to an outcome), do not force a second number — tell me it's already quantified and skip it.
- If I say "no numbers exist for this" before I've answered any surfacing questions, do not accept that. Ask 2–3 specific, answerable questions first (team size, baseline, frequency, duration, scale). Premature "no" is the single most common way candidates leave numbers on the table.
- If a bullet is genuinely unquantifiable (certain soft / relationship / one-off work), name that explicitly and rewrite with outcome-language only, rather than forcing a fake number.

Once the checks pass, for each remaining bullet: ask me 2–3 clarifying questions that would help me attach a number, percentage, dollar amount, or time savings. Questions should be specific and answerable — things I likely know or can estimate. Examples of good questions: "How many people were on the team?" "What was the before-state baseline?" "How often did the process run?" Bad questions: "What was the impact?" (too vague).

After I answer, rewrite each bullet using my numbers.
```

**Why this prompt works:** Flips the interaction — ChatGPT interviews you instead of guessing. Most people have the numbers but don't know which ones matter for a resume. The question-first structure surfaces the numbers you already know but hadn't thought to include.

---

## Prompt 6 — Career-switcher angle (emphasize transferable skills)

```
You are a career-transition coach who has guided 500+ candidates through cross-field pivots (tech → product, teaching → PM, finance → startup, corporate → nonprofit). You know transferable skills aren't claimed — they're demonstrated through outcome language the target field already uses.

I'm switching from [CURRENT FIELD] to [TARGET FIELD]. My current resume reads like a [CURRENT FIELD] resume, which makes me look unqualified for [TARGET FIELD] roles.

Job description for the target role:
[PASTE JD]

My resume (current):
[PASTE RESUME TEXT]

BEFORE rewriting, do these checks:
- If "[TARGET FIELD]" is vague ("something more creative", "a change", "tech"), refuse to proceed until I name a specific role or function. A pivot from marketing to "tech" produces a generic rewrite; a pivot from marketing to "B2B SaaS product management" produces a targeted one.
- If the JD is missing or was paraphrased, refuse — without the full target JD, transferable-skill mapping is imagined, not grounded in what the hiring manager is actually screening for.
- Do not assume I have no relevant side work. Before the repositioning step, ask me 2–3 questions about volunteer roles, freelance, certifications, portfolio projects, or adjacent experience that could anchor the pivot. Candidates chronically underreport transferable work.

Once the checks pass, rewrite my resume to emphasize the transferable skills and outcomes that matter for [TARGET FIELD], while being fully honest about my background. Specifically:

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
You are an executive resume writer who has written the top 3 lines for 800+ resumes across senior IC through C-level. You know the summary is the 5-second decision point: keep reading or skip.

Role:
[JOB TITLE AT COMPANY]

Job description:
[PASTE JD]

Key inputs about me:
- Years of experience in [FIELD]: [NUMBER]
- 2–3 most relevant accomplishments: [BULLET LIST]
- What I'm known for / my differentiator: [ONE SENTENCE]
- What I'm targeting: [SENIORITY LEVEL / DOMAIN / COMPANY TYPE]

BEFORE writing summaries, do these checks:
- If my years of experience / targeted seniority suggest IC or junior level (under ~6 years, or targeting non-leadership roles), push back on the "executive summary" framing. Offer to write a "professional summary" instead (same 5-variant structure, different register). "Executive summary" on a junior resume reads as overreach.
- If "what I'm known for / my differentiator" is vague ("hard worker", "team player", "passionate"), surface a real differentiator first — ask 2–3 questions to find an unusual skill combination, named accomplishment, or specific domain depth. Without it, all 5 variants read generic.
- If the "accomplishments" input has no quantified wins, flag that the results-first variant (#1) will be the weakest of the 5 — it needs a number to lead with — and either ask for one or note upfront that the variant will under-deliver.

Once the checks pass, write 5 different executive summary options for the top of my resume. Each should be 2–3 sentences, ATS-friendly, keyword-dense, and tailored to this specific role.

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
You are a resume writer who has done 500+ LinkedIn-to-resume conversions. You know LinkedIn rewards voice and narrative, resumes reward compression and keywords — and that pasting LinkedIn into a resume template without running the transform is the #1 reason experienced candidates get screened out.

My LinkedIn profile (copy-paste everything: headline, about, experience, education, skills):
[PASTE LINKEDIN PROFILE TEXT]

Job description:
[PASTE JD]

BEFORE converting, do these checks:
- If the pasted LinkedIn is just the default "[role] at [company]" with empty or near-empty About / experience detail, refuse and ask me to paste the full content: headline, full About section, each role's detail bullets, education, skills. An empty LinkedIn produces an empty resume.
- If the LinkedIn About section is a long first-person narrative, flag that compression to 2–3 sentences will lose voice — confirm with me whether to compress aggressively (best for ATS) or preserve more narrative (best for hiring-manager-facing formats) before proceeding.
- If the JD is missing, skip step 3 (keyword weaving) and tell me explicitly. Without a JD, there's nothing to anchor the keyword pass to.

Once the checks pass, convert my LinkedIn profile into a one-page ATS-readable resume tailored to the attached job description. Transform as follows:

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

Three worked examples — entry-level, mid-career switcher, and senior. Each shows the original draft, the exact prompt run, and the polished output. Use these to calibrate what "good" looks like before you run the prompts on your own material.

**One thing to know before reading the examples**: the metrics in each AFTER (open rates, retention numbers, ARR figures, latency cuts, MQL counts) are the candidate's real numbers. They came out when the prompt asked clarifying questions about scale, baseline, and outcomes — not from the model. The bundle's prompts surface what you already know; they refuse to invent. When you run these prompts on your own material, the AFTER you produce will be quantified to the same level only if you can answer the same kinds of questions. That's the work.

---

### Example 1 — Entry-level (recent grad → Marketing Coordinator)

**Candidate**: Maya Chen, BA Marketing (2025), one internship + two campus jobs. Applying to Marketing Coordinator at a B2B SaaS company.

**Job description (excerpt)**:
> Marketing Coordinator — support demand-gen team on email campaigns, landing pages, and HubSpot workflows. Track campaign performance in GA4. Collaborate with content and sales ops. Skills: HubSpot, GA4, Figma, A/B testing, copy editing.

**BEFORE** (original draft — weak):

```
MAYA CHEN
maya.chen@email.com · (555) 123-4567

OBJECTIVE
Recent graduate looking for a marketing role at a growing company where I can
apply my skills and learn from experienced professionals.

EDUCATION
University of State, BA Marketing, 2025

EXPERIENCE

Marketing Intern, LocalCo — Summer 2024
- Responsible for social media posts
- Helped with email campaigns
- Assisted the marketing team with various projects
- Worked on graphic design tasks

Campus Tour Guide, University of State — 2023–2025
- Gave tours to prospective students
- Represented the university at events
- Worked with a team

Barista, Campus Coffee — 2022–2024
- Served customers
- Handled cash register
- Cleaned the store

SKILLS
Microsoft Office, social media, teamwork, communication
```

**Prompt run** — Prompt 2 (rewrite) + Prompt 4 (keyword injection), back to back.

**AFTER** (polished output):

```
MAYA CHEN
maya.chen@email.com · (555) 123-4567 · Austin, TX · linkedin.com/in/mayachen

SUMMARY
Marketing graduate with hands-on experience running email campaigns, HubSpot
workflows, and GA4 reporting during a B2B SaaS internship. Combines demand-gen
fundamentals with copy editing and Figma design. Seeking Marketing Coordinator
role to own campaign execution end-to-end.

EXPERIENCE

Marketing Intern — LocalCo (B2B SaaS, 40 employees)                Summer 2024
- Built and shipped 6 email campaigns in HubSpot, averaging 28% open rate (vs.
  18% team baseline) and driving 47 MQLs over the internship
- Designed 4 landing pages in Figma and HubSpot; A/B tested headline variants,
  lifting conversion from 3.1% to 4.8% on the top-performing page
- Tracked campaign performance in GA4 and built a weekly dashboard the demand-
  gen team adopted as their standing report
- Edited and shipped 22 blog posts, cutting average review-to-publish time from
  6 days to 2 by tightening the copy-edit checklist

Campus Tour Guide — University of State                            2023–2025
- Led 3–5 group tours per week for prospective students and families (~200
  total), consistently rated 4.8/5 on post-tour surveys
- Trained 4 incoming guides on the 90-minute tour script and Q&A protocols

Barista — Campus Coffee                                            2022–2024
- Processed ~120 transactions per shift during peak hours while maintaining
  accurate cash drawer with zero shortages over 18 months

EDUCATION
University of State — BA Marketing, 2025 (GPA 3.7)
Relevant coursework: Digital Marketing, Consumer Behavior, Marketing Analytics

SKILLS
HubSpot · GA4 · Figma · A/B testing · Email marketing · Landing page copy ·
Campaign reporting · Excel · Copy editing
```

**What changed (the big four)**:

1. **Objective → Summary**: Objective sections date the resume and focus on what the candidate wants. Summary focuses on what the employer gets — and packs keywords from the JD.
2. **Quantified the intern role**: The original said "helped with email campaigns." The prompt asked Maya for the numbers she already knew (open rate, MQL count) and used them. This is the single biggest upgrade.
3. **Cut the filler verbs**: "Responsible for", "helped with", "assisted", "worked on" — all replaced with "Built", "Designed", "Tracked", "Led", "Trained".
4. **Skills section aligned to the JD**: The JD asked for HubSpot, GA4, Figma, A/B testing, copy editing — all now present in both the experience bullets *and* the skills list. The original had none of them.

---

### Example 2 — Mid-career switcher (teacher → Product Manager)

**Candidate**: Derek Olusanya, 8 years high-school math teacher + AP Computer Science, also runs an EdTech side project. Applying for Associate Product Manager at a consumer EdTech company.

**Job description (excerpt)**:
> Associate Product Manager, EdTech — partner with eng + design to ship features for K–12 learning product. Write specs, run user interviews, prioritize roadmap. We love candidates with classroom experience. Skills: user research, roadmap prioritization, data literacy, cross-functional communication.

**BEFORE** (original draft — reads like a teacher, not a PM):

```
DEREK OLUSANYA
derek.o@email.com · (555) 987-6543

EDUCATION
M.Ed, Curriculum & Instruction, State University, 2018
BS, Mathematics, State University, 2015
Teaching Credential, Single Subject Math, 2016

TEACHING EXPERIENCE

Math Teacher — Roosevelt High School                              2017–Present
- Teach Algebra I, Algebra II, and AP Computer Science
- Responsible for curriculum planning and lesson preparation
- Manage a classroom of 35 students
- Grade assignments and provide feedback
- Communicate with parents and administration
- Participated in department curriculum committee
- Ran after-school coding club

Math Teacher — Jefferson Middle School                            2016–2017
- Taught 7th and 8th grade math
- Developed lesson plans aligned with state standards

Student Teacher — Lincoln High                                    Spring 2016
- Assisted lead teacher in Algebra I classroom

SIDE PROJECT
Built a flashcard app called MathFlash for my students

HOBBIES
Chess, running, woodworking
```

**Prompt run** — Prompt 6 (career-switcher angle), then Prompt 7 (executive summary) to generate 5 summary options.

**AFTER** (polished output):

```
DEREK OLUSANYA
derek.o@email.com · (555) 987-6543 · Oakland, CA · linkedin.com/in/derekolusanya
github.com/derek-o/mathflash

SUMMARY
Former high-school math and CS teacher moving into product, with 8 years of
daily user research with the exact audience EdTech products serve: 14–18 year
old learners and their teachers. Shipped a self-built study app (MathFlash,
1,200 active users) from idea to production. Built cross-functional fluency
between pedagogy, data, and engineering — the core job of an EdTech APM.

PRODUCT & CROSS-FUNCTIONAL EXPERIENCE

MathFlash — Founder / Solo Product Manager                        2022–Present
- Conceived, spec'd, and shipped a flashcard study app for Algebra I students
  after identifying a gap in retention tooling in my own classroom
- Ran 40+ user interviews with students and 12 with other math teachers to
  prioritize the v1 feature set; killed 3 planned features based on feedback
- Grew to 1,200 weekly-active users across 9 schools in the Bay Area without
  paid acquisition; retention at week 4 is 38%
- Wrote product specs, coordinated with a contract React Native developer, and
  ran weekly sprint reviews for 14 months
- Pulled funnel data from Mixpanel weekly to prioritize the backlog; shipped
  15 features in year 1 based on usage data, not gut calls

Math & CS Teacher — Roosevelt High School                         2017–Present
- Deliver curriculum to ~150 students per year across Algebra I, Algebra II,
  and AP Computer Science; consistently rated top-3 teacher in student surveys
- Redesigned the AP CS curriculum in year 3, lifting AP exam pass rate from
  54% to 81% over two cohorts — effectively a roadmap prioritization exercise
  with measurable outcomes
- Ran classroom-scale A/B tests on two teaching methods (2018 and 2020); wrote
  both up for the department curriculum committee
- Founded and ran after-school coding club (25 students/semester), a direct
  feedback loop for what EdTech features teens actually use

EARLIER
Math Teacher, Jefferson Middle School (2016–2017) · Student Teacher, Lincoln
High (Spring 2016)

EDUCATION
M.Ed, Curriculum & Instruction — State University, 2018
BS Mathematics — State University, 2015

SKILLS
User research · Roadmap prioritization · Product specs · Mixpanel · SQL (basic)
· Figma · A/B testing · Cross-functional communication · K–12 curriculum design

GAPS I'M CLOSING (next 8 weeks)
- Completing Reforge's Product Strategy course (June cohort)
- Shipping v2 of MathFlash with in-app experimentation framework
```

**What changed (the big four)**:

1. **Reframed the job title mental model**: Original led with "Math Teacher." The polished version re-centers around "cross-functional experience" and surfaces the side project first — because *that* is the PM evidence. The teaching role is still there but framed in PM language ("roadmap prioritization exercise with measurable outcomes").
2. **MathFlash promoted from "hobby" to flagship experience**: It's the strongest PM evidence in his whole background. Burying it at the bottom was malpractice. Now it opens the experience section.
3. **Teaching bullets re-worded in PM vocabulary**: "Managed a classroom" became "deliver curriculum to ~150 students/year" and the AP CS redesign became a "roadmap prioritization exercise with measurable outcomes." Same work, different frame.
4. **Gaps closing section at the bottom**: The career-switcher prompt generated concrete 8-week actions. Including this turns a potential objection ("but he's a teacher") into a signal of self-awareness and drive.

---

### Example 3 — Senior / Executive (bloated 2-page → sharp 1-page VP Eng)

**Candidate**: Priya Raghavan, 16 years in software, currently Director of Engineering at a 400-person company. Applying for VP of Engineering at a Series B SaaS company.

**Job description (excerpt)**:
> VP Engineering — own the engineering org (currently 35, scaling to 60). Partner with CEO and CPO on product-engineering strategy. Scale infra and hiring. Report to CEO. Looking for operators who've scaled orgs through Series B → C. Skills: engineering leadership, org design, hiring, infra scaling, executive communication.

**BEFORE** (original draft — bloated, two pages, dated framing):

```
PRIYA RAGHAVAN
priya.r@email.com · (555) 222-3333

OBJECTIVE
Seasoned engineering leader with 16 years of experience seeking a VP of
Engineering role at a high-growth technology company where I can leverage
my skills in leadership, software architecture, and team building.

PROFESSIONAL EXPERIENCE

Director of Engineering — BigCo Inc.                               2020–Present
- Responsible for leading a large engineering organization
- Manage multiple engineering teams across the product
- Work with product management to define technical strategy
- Hire and mentor engineers
- Drive architectural decisions
- Participate in executive leadership meetings
- Have led initiatives to modernize our technology stack
- Was involved in scaling the team from 15 to 35 engineers over 4 years
- Have implemented various process improvements to increase velocity
- Handled on-call rotation and incident response processes

Senior Engineering Manager — MidCo                                 2016–2020
- Managed two engineering teams of 6–8 engineers each
- Delivered major product initiatives including platform rewrite
- Hired and grew engineers
- Worked on architecture and code reviews
- Participated in company-wide engineering initiatives

Engineering Manager — StartupCo                                    2013–2016
- Managed a team of engineers
- Was promoted from Senior Engineer role
- Led technical design and implementation of core product features
- Mentored team members and contributed to the hiring process

Senior Software Engineer — StartupCo                               2011–2013
- Was a senior engineer working on the platform team
- Worked on backend systems in Python and Go
- Participated in on-call rotation

Software Engineer — FirstCo                                        2008–2011
- Started career as a software engineer working on web applications
- Contributed to the codebase using Java and JavaScript

EDUCATION
MS Computer Science, Stanford University, 2008
BS Computer Science, University of California, Berkeley, 2006

SKILLS AND TECHNOLOGIES
Leadership, Management, Team Building, Mentoring, Agile, Scrum, Java, Python,
Go, JavaScript, React, Node.js, AWS, Kubernetes, Docker, PostgreSQL, MongoDB,
Redis, Microservices, REST APIs, GraphQL, CI/CD, Git

CERTIFICATIONS
AWS Certified Solutions Architect

PUBLICATIONS
Blog post on engineering leadership on Medium, 2022
```

**Prompt run** — Prompt 7 (5 summary options, chose "Results-first"), then Prompt 2 (full rewrite), then a final pass with Prompt 3 on the two weakest bullets.

**AFTER** (polished output — 1 page):

```
PRIYA RAGHAVAN
priya.r@email.com · (555) 222-3333 · San Francisco, CA · linkedin.com/in/priyar

Engineering leader who has scaled two orgs through Series B → C. Took BigCo's
engineering org from 15 to 35, cut p95 latency 62%, and shipped the platform
migration that unlocked a $12M ARR enterprise tier. Known for partnering tightly
with CEO/CPO to align eng capacity with product strategy.

LEADERSHIP EXPERIENCE

Director of Engineering — BigCo Inc. ($80M ARR SaaS)               2020–Present
- Scaled engineering from 15 to 35 across 5 teams (platform, product, data,
  infra, security); reshaped org design twice to match product bets
- Led platform migration to Kubernetes + multi-region AWS in 9 months; cut p95
  API latency 62% and enabled the $12M ARR enterprise tier that launched 2023
- Hired 24 engineers including 4 EMs and 2 staff+; retention at 94% over the
  last 24 months in a market where peer companies averaged 78%
- Partner weekly with CEO and CPO to set the 6-month engineering roadmap;
  own quarterly board updates on engineering health and hiring
- Rebuilt the on-call + incident-response program: reduced Sev-1s from 11/year
  to 2, mean time to resolve from 4h to 38 minutes

Senior Engineering Manager — MidCo                                 2016–2020
- Managed two teams (6 + 8 engineers) through the 18-month platform rewrite
  that replaced a monolith consuming 40% of eng bandwidth on maintenance
- Grew and promoted 5 engineers to senior, 2 to staff; ran hiring loops that
  closed 18 hires over 3 years at a 71% offer-accept rate

Engineering Manager, then Senior Software Engineer — StartupCo    2011–2016
- Promoted from IC to EM at 18 months; built the 7-person platform team that
  owned billing, auth, and the public API through Series A → B
- Prior IC work: backend platform in Python + Go, on-call lead for payments

EARLIER
Software Engineer, FirstCo (2008–2011) — Java/JavaScript, web platform

EDUCATION
MS Computer Science — Stanford, 2008 · BS CS — UC Berkeley, 2006

SELECTED SKILLS
Org design · Scaling through Series B → C · Executive communication · Hiring
(ICs through staff+) · Infra scaling (AWS, Kubernetes) · Incident response
```

**What changed (the big four)**:

1. **Cut from 2 pages to 1**: Senior resumes over 1 page are rarely read top-to-bottom. The polished version drops the SKILLS-AND-TECHNOLOGIES wall (15 items reduced to 6 that actually matter for a VP role), merges two stints at StartupCo into one line, and drops the Medium post + AWS cert (not load-bearing at VP level).
2. **Summary leads with numbers**: Original opened with "Seasoned engineering leader with 16 years of experience." Polished opens with two specific outcomes ("15 → 35 headcount, 62% latency cut") and one strategic outcome ("$12M ARR enterprise tier"). At the VP level, the summary is the resume — recruiters and CEOs decide in 10 seconds.
3. **Every bullet now has an outcome, not an activity**: "Responsible for leading a large engineering organization" → "Scaled engineering from 15 to 35 across 5 teams; reshaped org design twice to match product bets." The action is still there — plus the outcome and the context.
4. **Tuned to the JD's exact language**: JD asked for "scaled orgs through Series B → C" → that exact phrase is now in the summary. JD asked for "executive communication" → it's in the skills line. JD asked for "partner with CEO and CPO" → it's a bullet under Director role. ATS keyword alignment and human-readable alignment are the same move at this level.

---

**How to use these examples**: Pick the one closest to your stage, read the BEFORE and AFTER side-by-side, then scroll back to the prompt it used and run it on your own material. The point isn't to copy the finished output — it's to calibrate what the gap between a draft and a shipped resume looks like before you run the prompts blind.
