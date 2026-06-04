# Show HN — Pre-drafted comment replies (for Fri June 5 launch)

> **⚠ DECIDE BEFORE POSTING (Tom flagged Wed Jun 3 night):**
> 1. **Friday vs. weekday.** `show-hn-post.md` advises *avoid Fridays — front-page decay before the weekend*. You're launching Friday because it's your only no-work window. Accept the decay risk, or move to Thu Jun 4 (you work 11-4, so you'd post ~7 AM MT and lose the mid-day monitoring window). Your call.
> 2. **Post time.** This file says submit **7:00 AM MT (= 9 AM ET, mid-window)**; the handoff says **8:00 AM MT (= 10 AM ET, tail edge)**. 7 AM MT is the stronger slot. Pick one and set the alarm to match.


Have these in a separate browser tab when you post. The first 2 hours are where Show HN posts live or die — speed of reply matters as much as quality.

**Tone rules:** lowercase opener, no exclamation points, fragments OK, generous and direct. HN respects honest specificity over polish. Don't oversell. Don't pad with thanks.

---

## Reply (a) — "how is this different from awesome-chatgpt-prompts?"

This is the #1 most-likely question. Have this ready.

```
fair comparison. awesome-chatgpt-prompts is the canonical reference repo — short "act as a [role]" personas in a markdown table. it taught the convention, snipprompts builds on it.

three structural differences:

1. each prompt is its own page with input slots (`[YOUR ROLE]`, `[THE METRIC]`) instead of a one-line persona. avg length is 10-40 lines.

2. every prompt has a refuse-to-invent gate: if you don't provide a required input, the prompt instructs the model to ASK you rather than make something up. catches most "chatgpt fabricated my experience" failures.

3. every prompt has a banned-phrase list specific to the domain. e.g. cover letters ban "i am writing to express," "proven track record," "results-driven." resumes ban "spearheaded," "cross-functional," "leverage."

the github repo is broader (any topic). snipprompts is narrower (career, communication, business) and deeper per prompt. if you want the persona seed, the repo is leaner. if you want a ready-to-run structured prompt for a specific use case, snipprompts is the bet.

honest critique of snipprompts: i'm one person, the library is 182 prompts not 200k. small library is the bet — every prompt has been written + tested, but it's narrower than a community marketplace.
```

---

## Reply (b) — "show me an example prompt"

Link to a high-craft one. NOT the resume prompt (most generic-looking). Best picks: interview prep, salary negotiation, or one of the new ones (regex, api-documentation, technical-interview-prep).

```
sure — three with different shapes:

interview prep (mock-with-feedback structure):
https://snipprompts.com/prompts/best-chatgpt-prompt-for-job-interview-prep.html

salary negotiation email (refuse-to-invent gate + verification table):
https://snipprompts.com/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html

regex (technical, shows the "specify the flavor + give me 3 should-match AND 3 should-not-match examples" structure):
https://snipprompts.com/prompts/best-chatgpt-prompt-for-regex.html

each one has the prompt itself in a copy box at the top, a worked example below, and tips. all free, no signup.

happy to swap notes on what fails — i've found the refuse-to-invent gate works ~70% on smaller models (3.5, 4o-mini) and ~90% on claude opus and gpt-4. the validator step catches more of the misses.
```

---

## Reply (c) — "how do you handle the model just ignoring the gate?"

Honest answer. HN crowd respects "here's what doesn't work."

```
honest answer: sometimes it does ignore the gate, especially smaller models.

what i've found:

- on gpt-4 / claude opus, the gate fires ~85-90% of the time. the model genuinely asks for missing inputs before writing.

- on gpt-4o-mini, gpt-3.5, gemini flash, it fires more like 60-70%. small models lose constraints in long prompts.

- the post-output validator step (third guardrail) catches ~50-60% of the remaining misses. the model is better at critiquing its own output than at preventing the failure in the first place.

- the rest you catch on the first read.

mitigations that actually work:
1. put the gate at the END of the prompt as well as the beginning. recency bias in attention helps.
2. add a final line: "before you write, repeat back the constraints in one sentence." this forces the model to acknowledge them.
3. for smaller models, split the workflow into two prompts: one for the verification questions, one for the output.

the paid bundle handles this more rigorously with worksheets that force you to fill the inputs before the prompt runs. the free pages are deliberately compact, so they accept some failure rate as the cost of being copy-paste runnable in one shot.
```

---

## Bonus prepared answers (less likely but worth having)

### "what's the business model?"

```
free site is free, no signup, no ads on prompt pages (ezoic ads only on resource and category pages where they don't disrupt the copy flow). paid bundle is $39 one-time for job-hunt depth: 44 prompts, 8 negotiation scripts, 5 modules, 118-page pdf + notion. 30-day refund. that's it. no subscription, no upsell ladder.

bundle is at snipprompts.gumroad.com/l/job-hunters-ai-bundle if you want to see it.
```

(Mention the bundle ONCE per thread. Don't re-link in subsequent comments.)

### "why career as the deepest vertical?"

```
because cost-of-failure is highest there. a bad ChatGPT recipe wastes 5 min of cooking time. a bad ChatGPT resume costs you the role, and you don't find out for weeks. high-stakes prompts are where guardrails matter most.

the rest of the library (business writing, finance, marketing) uses the same three rules but those verticals are wider and shallower. career is where i went deep first because the failure mode is the worst.
```

### "this looks like an SEO play"

```
fair — the page-per-prompt structure is unambiguously SEO-friendly. but the trade is the same trade the github repo makes: one canonical page per use case so you don't scroll a wall.

what i'd say in defense: every prompt has been written and tested, not auto-generated. the long-form guides (8 of them) are explicit about failure modes including ones that make the product look bad ("here's what the resume prompt invents when you give it thin input"). harder to read as pure SEO when the content actively warns you about the product's limits.

honest critique: yes, the page count helps SEO. that's not a bug, but it's a real factor in how the library is structured.
```

---

---

## More anticipated questions (added Tom, Jun 3)

### "do these work on Claude / Gemini or just ChatGPT?"

```
all three. the prompts are written around chatgpt's phrasing but the structure — input slots, refuse-to-invent gate, banned-phrase list, self-validation step — is model-agnostic. tested most on gpt-4/4o and claude opus, lighter on gemini. the refuse-to-invent gate is actually most reliable on claude in my experience.
```

### "why copy-paste prompts instead of a custom GPT?"

```
fair — a custom gpt would be smoother for a chatgpt-plus user. two reasons i went copy-paste:

1. works for everyone, including free-tier and non-chatgpt users. a custom gpt locks you into plus.
2. you can see and edit the whole prompt. the guardrails are visible, so you can tune the banned-phrase list to your own field. a custom gpt hides the machinery.

the tradeoff is friction — you paste instead of click. for a high-stakes one-off like a resume, i think the transparency is worth the paste.
```

### "what does 'tested' actually mean?"

```
honest scope: tested = i ran each prompt with real and deliberately-thin inputs across gpt-4/4o and claude opus, and checked that (a) the refuse-to-invent gate fired on missing inputs, (b) the output didn't emit banned phrases, (c) the self-validation step caught its own misses.

it is NOT a/b tested at scale or benchmarked with metrics. it's one person's structured manual testing. i'd call it "hand-verified," not "empirically validated." if someone wants to help build a real eval harness, i'm interested.
```

### "isn't a banned-phrase list brittle as models change?"

```
yes, somewhat. the specific cliches shift as models retrain — "delve," "tapestry," "boasts" came and went. but the failure MODE (defaulting to high-frequency filler) is stable, so the approach holds even as the list needs updating. i treat the list as living and revise it when a new tell shows up. it's maintenance, not a one-time fix. the refuse-to-invent gate is the more durable of the two guardrails.
```

---

## Posting workflow Fri June 5

1. 6:50 AM MT — open https://news.ycombinator.com/submit
2. Title: `Show HN: SnipPrompts – 182 ChatGPT prompts engineered to not sound like AI`
3. URL: `https://snipprompts.com`
4. Body: paste from `show-hn-post.md`
5. Submit at 7:00 AM MT (= 9:00 AM ET — top of peak HN window)
6. IMMEDIATELY refresh your post page and have these replies in a side tab
7. Reply to the first 3 substantive comments within 5 min each
8. Stay in thread for first 2 hours (until ~9 AM MT / 11 AM ET)
9. After 2 hours, check back every hour for the rest of the day

## What NOT to do in the thread

- Don't reply to obvious trolls or "this is just SEO" drive-bys with defensive paragraphs. 1-line acknowledgments only, or skip.
- Don't link the bundle more than once. HN downvotes second-pitch.
- Don't reply "good question!" — start every reply with substance.
- Don't paste this whole file. Use the relevant reply only.
