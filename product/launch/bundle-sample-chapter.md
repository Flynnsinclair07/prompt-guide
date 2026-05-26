# The Job Hunter's AI Bundle — Free Sample

*This is a representative sample of what's inside the full bundle. It uses one prompt from the Resume module — fully built out the way the paid version does — so you can decide if the deeper version is worth $39 to you. Read it, run it on your own resume, see what it does.*

*Flynn — May 2026*

---

## What's different about the bundle's prompts

The free prompts on snipprompts.com are good. They get you a usable draft. The bundle's versions are *structured* differently — they refuse to run on weak input, they have explicit banned-phrase lists, and they include a post-output validation step that catches the AI tells most candidates miss. The difference is the difference between a one-line "act as a resume writer" prompt and a small, opinionated program.

Three patterns appear in every bundle prompt:

**1. The persona seed.** Not "you are an expert" — a specific, narrow role with constraints. "You are a senior recruiter at a Series-B SaaS company who reads 200 resumes a week. You hate jargon. You read past clichés." The narrower the persona, the better the output.

**2. The refuse-to-invent gate.** A hard rule the model can't talk its way around: "If a metric, percentage, role, or outcome is not in my input, do not include it in the output. If you are unsure, ask before writing." This single line stops 80% of hallucinations.

**3. The post-output validation step.** After the model writes the draft, it must re-read its own output against a checklist: banned phrases, vague claims, unverified numbers, format mismatch. The model surfaces what it caught. You fix what it missed.

The bundle has 44 prompts built around these patterns, in a specific order — resume → cover letter → LinkedIn → interview → salary negotiation. One workflow, not a pile.

---

## Module 1, Prompt 1 — The Resume Rewrite

**What it does:** rewrites your existing resume against a specific target role, without inventing anything you didn't give it. Returns the resume plus a list of every claim it couldn't verify from your input — so you know what to add or remove.

**When to use it:** you have a resume (any version, even a rough one) and a specific job description you want to tailor to. Not for writing a resume from scratch — that's Prompt 2.

**Input slots:**

```
You are a senior recruiter at the target company below. You have read
200 resumes for this role this month. You skim each one for 7 seconds
before deciding whether to read past line 4. You hate clichés and
ignore claims with no specific evidence.

TARGET ROLE: [PASTE THE FULL JOB DESCRIPTION, OR LINK + SUMMARY]

MY CURRENT RESUME: [PASTE THE FULL CURRENT TEXT — DON'T SUMMARIZE]

THINGS I ACTUALLY DID THAT AREN'T IN THE RESUME YET (raw, messy is fine):
[BULLET DUMP — projects, tools, metrics, soft wins, hand-offs, anything]

NUMBERS I'M NOT SURE ABOUT (true range, not made up):
[e.g. "increased something by maybe 15–25%" or "team grew from 3 to 6
to 9 over 18 months"]

HARD RULES — DO NOT VIOLATE:
1. Do not invent any metric, tool, role, project, or outcome that is
   not in my input. If the input doesn't have a number, leave it
   qualitative. Don't add a number.
2. If a bullet has no measurable outcome, write it without one.
3. Banned phrases — do not emit: results-driven, proven track record,
   passionate about, leverage [as a verb], thrive in, dynamic, level up,
   strong communicator, cross-functional collaboration, spearheaded.
4. If you are unsure whether something is in my input, ASK ME before
   writing it. Do not guess.
5. Match the keyword set of the target role where it is honest to do
   so. If the target asks for a skill I don't have, do NOT add it.

OUTPUT IN THIS ORDER:
A. The rewritten resume in plain text (single page, ATS-friendly).
B. Verification table — for each bullet you wrote, the source line in
   my input you pulled from.
C. Gap list — anything in the target JD I do NOT match, with one short
   suggestion per gap (skill to learn, project to start, or "apply
   anyway, here's how to frame it").
D. The 5 strongest bullet candidates from my input that did NOT make
   the page, in case I want to swap.
```

**How to run it:** paste this whole block into ChatGPT (or Claude, or Gemini) and replace the [BRACKETED] sections with your actual content. The fuller you make the third section ("things I actually did that aren't in the resume yet"), the more material the model has to work with — and the less it needs to invent.

**Common mistake:** people paste a 4-line "summary of my background" instead of the actual resume text plus the brain-dump. The model can only work with what you give it. Specific, dense input → specific, dense output. Vague input → cliché soup.

---

## Example: a partial output (lightly edited from a real run)

**Input:** mid-career analytics manager applying for a senior data PM role at a logistics SaaS.

**A. Verification table excerpt:**

| Output bullet | Source line in your input |
|---|---|
| "Migrated reporting pipeline from Looker to a custom warehouse layer; cut weekly refresh from 14h to 90 min." | "We replaced Looker with our own warehouse. Old weekly run took ~14 hours, after the migration ~1.5 hours." |
| "Hired and onboarded 2 senior data analysts; built the team's first runbook for incident response." | "Hired Maria and Lev. Wrote the runbook nobody had bothered with before." |
| (No bullet about ML, despite target JD asking) | NOT IN INPUT — see Gap List item 3. |

**C. Gap list excerpt:**

> 3. Target JD asks for "ML model deployment experience." I did not include this — you did not list it. If you have any ML adjacent work (even shipping a model someone else built, or evaluating one), tell me and I'll add. If not, apply anyway and address in the cover letter: "I have not deployed an ML model in production. I have deployed [thing X], and the closest analog is [Y]."

That's the bundle's version. The free version is shorter, has the same refuse-to-invent gate, and skips the verification table. The verification table is the thing buyers tell me made the biggest difference — it stops the model from sneaking inventions into your final.

---

## What's in the full bundle

| Module | Prompts | Highlights |
|---|---|---|
| 1. Resume | 8 | This prompt + ATS-readability checklist + 3 before/after examples |
| 2. Cover Letter | 6 | Banned-phrase prompt + 3 opener templates + "skim for" cheat sheet |
| 3. Interview | 12 | Story-mining workflow + 3-round AI grilling drill + answer-scoring prompt |
| 4. LinkedIn | 8 | Headline prompt + 14-item profile checklist + 10-post-type weekly content pack |
| 5. Salary Negotiation | 10 prompts + 8 scripts + 3 worksheets | BATNA worksheet, comp triangulator, walkaway-math calculator, scripts for every common pushback |

Plus a Notion workspace so the whole workflow has a home, not 44 files in a folder.

118 pages total. $39 on Gumroad. 30-day refund if it isn't useful — no questions, just reply to your receipt.

[Get The Job Hunter's AI Bundle →](https://snipprompts.gumroad.com/l/job-hunters-ai-bundle)

---

*Built by Flynn Sinclair in Colorado. snipprompts.com.*
*If a prompt in this sample doesn't work for you, email flynn@snipprompts.com — I read every reply.*
