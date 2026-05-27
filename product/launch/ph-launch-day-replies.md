# PH Launch Day — Comment Reply Bank

**How to use:** these are pre-written, ready-to-adapt replies for the comments you'll most likely get on launch day (Wed May 27). Match the archetype, swap in any specific detail from their actual comment, paste. Brand voice throughout — lowercase opener, no exclamation points, no banned phrases.

**Golden rules on launch day:**
- Reply to every real comment within ~30 min of it landing.
- Acknowledge the specific thing they said — never a generic "thanks!"
- Engage genuine critique, ignore trolls.
- Mention the bundle at most once per thread, only if asked.

---

## 1. "How is this different from awesome-chatgpt-prompts / other free prompt lists?"

```
fair question — most prompt repos are one-line "act as a [role]" snippets. each page here is a structured prompt with input slots, a refuse-to-invent gate (it asks for real numbers instead of fabricating them), a banned-phrase list, and post-output rules. closer to a function with arguments than a one-liner. the whole thing is built around the specific ways ChatGPT fails at a task, not just "here's a prompt."
```

## 2. "Can you show me a strong example?"

```
yeah — the interview-prep and salary-negotiation ones are the higher-craft examples:
https://snipprompts.com/prompts/best-chatgpt-prompt-for-job-interview-prep.html
the resume one looks the most generic on the surface but the guardrails are the point — it refuses to invent metrics you didn't give it. curious what you think of the structure.
```

## 3. "How do you stop the model from just ignoring the guardrails?"

```
honest answer: sometimes it does ignore them, especially smaller models. the post-output validation step catches maybe 70% of those — it re-reads its own output and flags banned phrases or unverified numbers. the rest you catch on the first read. the gates reduce the failure rate a lot, they don't eliminate it. that's also why every page says "review the output," not "paste and ship."
```

## 4. "Is this just a funnel for the paid bundle?"

```
the 134+ prompts on the site are genuinely free, no signup, no wall — that's the real front door and it'll stay that way. there's a paid bundle for job hunters who want the deep version (more prompts, scripts, worksheets), but the free pages aren't crippled to push it. you can use the whole site forever and never hit a paywall.
```

## 5. "Why should I trust prompts built by a [student / first-timer]?"

```
fair to be skeptical. the prompts either work or they don't — every one was tested on ChatGPT free tier plus Claude and Gemini, rewritten until the output was something a recruiter actually reads. i'm 19 and this is my first thing, so i'd rather you judge it on the output than on my résumé. if a prompt falls over for you, tell me which one and i'll fix it.
```

## 6. "Prompts are dead / just talk to the model normally."

```
partly agree — for casual stuff you don't need a prompt, you just chat. these are for the high-stakes, repeatable tasks where the default output gets you in trouble: a resume that invents a metric you can't defend in the interview, a cover letter that reads like every other one. for those, a structured prompt with guardrails beats winging it. for "what's a good dinner recipe," yeah, just ask.
```

## 7. "Does it work with Claude / Gemini?"

```
yep — written around ChatGPT's phrasing but they run the same on Claude, Gemini, or any modern model. the failure modes i designed around (invented numbers, clichés, generic output) are common to all of them.
```

## 8. Generic positive ("nice / congrats / cool idea")

```
thanks — appreciate you taking a look. if you end up using one, i'd genuinely like to hear what worked or didn't.
```

## 9. Someone shares a bad-AI-output story (the maker comment asks for this)

```
that's exactly the kind of thing the prompts are built around — [reference their specific example]. the [resume/cover letter/whichever] one has a gate for precisely that failure. thanks for sharing it, this is the feedback i actually want.
```

## 10. Feature request / "you should add [X]"

```
good call — [X] isn't on the site yet. adding it to the list. if you want, i'll reply here when it's up.
```

(Then actually build it — you've got a 40-topic pipeline; a real "you asked, here it is" follow-up is gold.)

## 11. "What's the refund policy?" / "I'd buy it but I'm worried it won't work for me"

```
30 days, no questions, just email me at flynn@snipprompts.com or hit the refund button in your Gumroad library. i won't ask why. if the bundle doesn't help you in 30 days it doesn't help you and i'd rather you have the money back. the site has free versions of every prompt — start there, see if the structure works for you, then decide if you want the deeper paid version.
```

## 12. "Cool but I'd pay $19 not $39" / pricing pushback

```
fair. honest answer on $39 — it's priced low enough that anyone who actually job-hunts can pay for it, and high enough that i can spend the time keeping it updated when ChatGPT changes (which is most weeks). $19 would mean i can't, and the bundle would rot. that said: the site has all five career prompts free. start there. if the free pages do the job, you don't need the paid version and that's the point. if you want the deeper version after using the free ones, $39 is the deal.
```

## 13. "Why should I pay when [free competitor] exists?" (gentler version of refund/pricing)

```
honest answer: don't, if [free competitor] is working for you. the bundle is for people who tried the free side and want the deeper version — the verification tables, the negotiation scripts, the worksheets that aren't on the open internet. if you haven't tried the free pages on snipprompts.com yet, start there. that's the right entry point.
```

---

## The maker's first comment (already in the PH listing, here for reference)

It auto-posts at launch. Ends with the question "what's the worst AI-generated output you've gotten?" — when people answer, use reply #9.
