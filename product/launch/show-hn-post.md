# Show HN post

**Title (80 char max for HN, current is 81 — see note):**

> Show HN: SnipPrompts – 134 free, tested ChatGPT prompts that don't sound like AI

**Title char count:** 81. HN truncates around 80. Variant if you want to be safe:

> Show HN: SnipPrompts – 134 ChatGPT prompts engineered to not sound like AI

(73 chars — same hook, fits cleanly.)

**Recommended posting window:** Tue, Wed, or Thu, 8:00–10:00 AM Eastern. Avoid Mondays (high noise) and Fridays (front-page decay before weekend traffic peaks). Submit, then sit on the comments for the first 2 hours — the second hour is where Show HN posts live or die.

**URL field:** `https://snipprompts.com`

**Body (172 words):**

---

I've been building SnipPrompts for the last few months — a free library of 134 ChatGPT prompts across resumes, cover letters, interviews, business writing, personal finance, and a few lifestyle categories. Site is static HTML/CSS, no signup, no paywall on the prompts.

The thing I actually want feedback on is the engineering inside each prompt, not the volume. Every prompt has three guardrails:

1. A refuse-to-invent gate. If the input is missing a field the prompt needs (a metric, a date, a real anecdote), the prompt instructs the model to ask for it rather than fabricate. Closes off most of the "ChatGPT invented experience I don't have" failure mode.
2. A banned-phrase list. Each prompt carries the corpus-specific list of clichés it must not emit — "results-driven," "passionate about," "leverage" as a verb, "level up," and so on.
3. A post-output validation step. The prompt asks the model to re-read its own output and flag any banned phrase, vague claim, or unverified number before returning it.

It's the difference between a one-line prompt and a small program. Built in plain markdown, paste-ready.

Free to copy, no account. Feedback on the prompt structure especially welcome — happy to swap notes on what works and what falls over.

snipprompts.com

---

**Word count:** 198 (in the 150–250 target).

**Notes for the comments thread (don't paste in the body):**

- Be in the thread from minute 0. HN expects the author to engage.
- The first three comments will be one of: (a) "how is this different from awesome-chatgpt-prompts," (b) "show me an example prompt," (c) "how do you handle the model just ignoring the gate." Have all three answers ready.
  - (a) Most prompt repos are one-line "act as a X." Each SnipPrompts page is a structured prompt with input slots, guardrails, and an output validator. Closer to a function signature than a recipe.
  - (b) Link directly to one of the higher-craft ones — interview prep or salary negotiation work well. Don't link the resume one, it's the most generic-looking on the surface.
  - (c) Honest answer — sometimes the model does ignore the gate, especially smaller models. The validator step catches ~70% of those; the rest you catch on the first read. The bundle (paid product) handles this more rigorously but the free pages are deliberately compact.
- If someone asks about the bundle, mention it once, link it once, then drop it. HN audience will downvote a second pitch in the same thread.
- Don't reply to obvious troll comments. Reply to substantive critique, especially anyone who actually opens a prompt and tells you what's wrong with it.

**What to avoid in the post itself:**

- No "exclusive," "amazing," "incredible," "game-changing," "unlock," "unleash," "level up." (All banned.)
- No exclamation points.
- No "I'm a solo founder" sob story. HN doesn't reward that on Show HN.
- No screenshots. Plain text body. Site loads in 1 frame.
- No mention of Pinterest, no mention of the bundle in the body. The bundle goes in a reply if asked, not in the OP.
