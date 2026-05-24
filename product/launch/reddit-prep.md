# Reddit reply prep

**Status / honesty note:** Reddit (`reddit.com` and `old.reddit.com`) is blocked from this environment's web fetcher, and `site:reddit.com` returns no indexed results through web search. I could not pull 5–10 live URLs from the last 7 days. Rather than fabricate post links, I built a **pattern library**: the 8 post archetypes that recur weekly in r/jobs, r/resumes, r/cscareerquestions, and r/jobsearchhacks, each paired with a draft reply you can paste with light customization once you find the matching live thread.

**Workflow:** open each sub's `/new` feed sorted by past week, scan for a post matching one of the archetypes below, paste the draft, swap in 1–2 sentence-level details from the OP's actual post so it reads as a human reply, not a template. Goal is 1 paste per sub per day, max. Reddit kills accounts that paste identical replies across subs.

**Rules of engagement:**
- One link per reply. Always to the free snipprompts.com page, never the bundle.
- 3–6 sentences. Helpful first, link second.
- No "check out my site." Frame the link as "here's the prompt I'd use" or "this is the one I'd paste."
- Skip posts older than 3 days — the karma's gone and the OP has moved on.
- Skip posts with 200+ comments — your reply gets buried.
- Sweet spot: 1–6 hours old, 5–30 comments.

**Verified snipprompts.com pages used below** (URL pattern: `https://snipprompts.com/prompts/best-chatgpt-prompt-for-{slug}.html`):

| Topic | Slug |
|---|---|
| Resume (full) | `writing-a-resume` |
| Resume bullets | `resume-bullets` |
| Cover letter | `writing-a-cover-letter` |
| Job interview prep | `job-interview-prep` |
| LinkedIn profile | `linkedin-profile` |
| LinkedIn posts | `linkedin-posts` |
| Salary negotiation | `negotiation` |
| Performance review | `performance-review` |
| Resignation letter | `resignation-letter` |

---

## Archetype 1 — "I've sent 200 applications and nothing"

**Where it lives:** r/jobs, r/jobsearchhacks, occasionally r/resumes. Multiple times per week.

**The signal:** OP shares a volume number (50, 100, 200, 400 apps) + zero or near-zero callbacks. Usually 2–5 paragraphs of frustration. Resume sometimes pasted, sometimes not.

**Why your free pages fit:** the volume-with-no-response problem is almost always a resume problem (generic bullets, no metrics, wrong keywords for the ATS) and sometimes a cover letter problem (one template recycled with the company name swapped). Both are solvable with prompts.

**Draft reply:**

> 200 with zero callbacks is almost never a quantity problem — it's a signal the resume is getting filtered before a human sees it. Two things worth checking before you send another one out: are your bullets written as outcomes ("cut p95 latency 62%") or as duties ("responsible for backend services"), and does your resume use the exact keywords from the job posting, in roughly the same casing.
>
> If your bullets are duty-shaped, here's the prompt I'd use to rewrite them: https://snipprompts.com/prompts/best-chatgpt-prompt-for-resume-bullets.html — it's free and it has guardrails so ChatGPT can't invent metrics you don't actually have.
>
> Try it on three bullets, see if the rewrites feel like you, then expand. Don't paste the whole resume in one go — the model loses the thread.

---

## Archetype 2 — "My resume keeps getting auto-rejected, I think it's the ATS"

**Where it lives:** r/resumes, r/jobs, r/jobsearchhacks.

**The signal:** OP mentions "ATS," "applicant tracking system," "keyword match," or rejection emails within 24 hours of applying.

**Why your free pages fit:** the resume bullets prompt and the full resume prompt both bake in "use the exact terminology from the job description" as a step. Worth pointing OP at the prompt instead of just saying "use keywords."

**Draft reply:**

> The 24-hour rejection email almost always means the ATS or a human-with-30-seconds filtered you out on a keyword match check. Two things tend to fix it: (1) for every job you apply to, copy the JD into a doc and highlight the 8–12 concrete skills/tools/methodologies it lists, then make sure those exact phrasings appear in your resume; (2) write your bullets as outcomes with numbers, not as job duties.
>
> If you want a starting point, this is the resume prompt I'd run with your existing resume + the JD pasted in: https://snipprompts.com/prompts/best-chatgpt-prompt-for-writing-a-resume.html — it tells the model not to invent anything that wasn't in your input, which is the part most ChatGPT resume advice skips over.
>
> Worth doing for the next 5 applications, not all of them. Tailoring 5 carefully beats spraying 50.

---

## Archetype 3 — "Cover letters are the worst, I never know what to write"

**Where it lives:** r/jobs (most common), r/resumes, r/jobsearchhacks.

**The signal:** OP is paralyzed on cover letters, often asks "do I even need one anymore" or "what do I put in here." Sometimes drops a draft asking for feedback.

**Why your free pages fit:** cover letter prompt page is one of the highest-fit recommendations because the problem is almost always "I don't know what to say" — which is a prompt problem, not a writing problem.

**Draft reply:**

> Most cover letters fail the same way: they restate the resume in paragraph form. The thing recruiters are actually scanning for is one specific reason you'd be useful for this exact role at this exact company — not "I'm passionate about your mission."
>
> If you're stuck on the blank page, here's the prompt I'd use: https://snipprompts.com/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html — it asks for the JD, the company, and one specific accomplishment you want to lead with, then writes around that. Banned-phrase list inside so it doesn't come back with "results-driven" or "passionate about."
>
> Three sentences in the body is plenty. The hiring manager isn't reading paragraph four.

---

## Archetype 4 — "I have a behavioral interview Friday, what do I do"

**Where it lives:** r/cscareerquestions, r/jobs.

**The signal:** OP has a specific interview date, often a specific company, asks for prep advice. Usually nervous about behavioral / "tell me about a time" questions.

**Why your free pages fit:** the interview prep prompt walks through STAR-format answers for the role they're interviewing for. Pairs well with "do mock answers out loud, don't just read them."

**Draft reply:**

> The two things that move the needle on behavioral: (1) have 6–8 stories from your last 2 jobs that you can adapt to almost any question — leadership conflict, ambiguous project, tight deadline, mistake you owned, cross-functional disagreement, that kind of thing — and (2) say them out loud, not just in your head. Reading them silently is how you end up rambling on the day.
>
> For drafting the stories, this is the prompt I'd use: https://snipprompts.com/prompts/best-chatgpt-prompt-for-job-interview-prep.html — paste the role, the JD, and your real situations, and it'll structure them in STAR with the metrics in the right places.
>
> Then run them with a friend or your phone voice memo. The first time you say a story out loud is always the worst version.

---

## Archetype 5 — "My LinkedIn is dead / I need to update it / hiring manager said it's weak"

**Where it lives:** r/jobs, r/resumes, occasionally r/cscareerquestions.

**The signal:** OP wants headline / about / experience help, sometimes flags that they got passed over for a role and suspect LinkedIn was the reason.

**Why your free pages fit:** LinkedIn profile prompt is built around the headline+about combo that recruiters actually filter on. LinkedIn posts prompt is the second hit if they're trying to build visibility, but lead with the profile one.

**Draft reply:**

> The two highest-leverage pieces on LinkedIn are the headline (because it's what shows in every search result and connection request) and the first two lines of your About (because that's all that renders before the "see more"). Job title alone in the headline is a waste — it limits you to one search keyword.
>
> If you want a structured way to redo both, this is the prompt I'd run: https://snipprompts.com/prompts/best-chatgpt-prompt-for-linkedin-profile.html — it takes your role, target role, and one concrete achievement and gives you headline + About copy in the recruiter-search-friendly format.
>
> Update on a weekend if you can, so it doesn't ping your network with "started a new position" type notifications.

---

## Archetype 6 — "I'm getting a lowball offer, how do I counter"

**Where it lives:** r/cscareerquestions (often), r/jobs, r/jobsearchhacks.

**The signal:** OP has a real offer on the table, mentions the number, asks how to push back. Sometimes mentions Levels.fyi or Glassdoor comp data.

**Why your free pages fit:** the negotiation prompt is the strongest single-prompt recommendation in the whole library — clear, specific, drops a counter script into the model.

**Draft reply:**

> Counter, always. The worst case is they say no and the offer stands; the actual probability of them rescinding is near zero. You're looking for somewhere between "the number you actually want" and "the number you think is achievable based on comparable data."
>
> For the script itself, this is the prompt I'd run: https://snipprompts.com/prompts/best-chatgpt-prompt-for-negotiation.html — it takes the role, the offer, and what you think you're worth based on Levels.fyi / Glassdoor / similar, and writes a counter that doesn't sound like a confrontation.
>
> Send it in writing, not on a call. Keeps you off-script and gives them time to actually escalate it internally.

---

## Archetype 7 — "I'm quitting, how do I write the resignation letter / talk to my manager"

**Where it lives:** r/jobs (most common), occasionally r/cscareerquestions.

**The signal:** OP has accepted another offer or is about to quit, wants help with the letter, sometimes nervous about the conversation. Often asks how much notice to give.

**Why your free pages fit:** resignation letter prompt is a clean fit — gives a 2-paragraph professional letter without the awkward emotional padding.

**Draft reply:**

> Resignation letter is short on purpose. Two paragraphs: (1) stating you're resigning and your last day, (2) brief thanks + offer to help with the handoff. That's it. Don't explain why you're leaving, don't list grievances, don't put anything in writing you wouldn't want a future reference call to surface.
>
> For the wording, this is the prompt I'd use: https://snipprompts.com/prompts/best-chatgpt-prompt-for-resignation-letter.html — it gives a standard 2-week-notice version and a longer version if you're giving more runway.
>
> The verbal conversation matters more than the letter. Tell your manager first, hand them the letter at the end, not the other way around.

---

## Archetype 8 — "Performance review is next week and I have no idea what to write about myself"

**Where it lives:** r/cscareerquestions, r/jobs.

**The signal:** OP has a self-review deadline, doesn't know how to structure it, often worried about "sounding arrogant" or "sounding modest." Sometimes specifically asks about promo packets.

**Why your free pages fit:** performance review prompt structures the year into impact-level / project-level / skill-level so OP isn't staring at a blank doc.

**Draft reply:**

> Self-reviews are weirdly hard because you're trying to remember 12 months of work under deadline pressure. The trick is to dump everything first — every project, every win, every cross-team thing you touched — and then structure it after. Don't structure-then-fill; you'll forget half of it.
>
> For the structuring pass, this is the prompt I'd use: https://snipprompts.com/prompts/best-chatgpt-prompt-for-performance-review.html — you paste the brain-dump and your role, and it groups things into impact / projects / growth in the format most companies expect.
>
> One thing that helps: pull your last review's goals first, so you can explicitly map this year's work back to them. Reviewers love the "you set X, you did X" structure.

---

## Notes for posting

- **Account hygiene:** if you don't have a 6-month+ Reddit account with some karma already, the spam filter will eat your replies in r/resumes and r/jobs. Use whatever your oldest account is.
- **Rate:** 2–3 replies per day across the four subs is the safe upper bound. Five in one afternoon looks like a bot.
- **Edit before pasting:** rewrite the first sentence of each reply to reference one thing from the OP's actual post. "200 with zero callbacks" → "150 in 8 weeks with two phone screens" if that's what they actually said. The rest can stay.
- **Soft self-promo flag:** every subreddit has different rules. r/resumes is strictest on links to your own site. Watch for mod removal in the first hour; if removed, don't repost, just move to the next sub.
- **Link tracking:** if you want to know which replies converted, append `?ref=reddit-{sub}` to the URL — the site won't care, you get an attribution trail in analytics.
