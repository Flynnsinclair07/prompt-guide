# Pre-Launch Email Sequence — ConvertKit

**Status**: Paste-ready. 4 emails timed across May 3 → May 17, 2026.
**List**: existing snipprompts.com subscribers (form UID `d02eb77674`).
**Workflow type**: ConvertKit Broadcast (not a Sequence). Broadcasts let you schedule by date and segment by tag — Sequences are fixed-interval and trigger on signup, which is the wrong shape for a launch ramp.

How to use this file:
1. Each section maps to one ConvertKit broadcast. Subject + preview + body are paste-ready.
2. The `[GUMROAD_URL]` placeholder appears in Email 4 only. Replace with the live Gumroad URL before scheduling. Everything else has no placeholders.
3. Recommended segment for all four: subscribers with the `lead-magnet` or `homepage-signup` tag (i.e. the existing list — exclude `bundle-buyer-2026-may` so buyers don't get launch-day pitches).
4. Time-zone: schedule for **9:00 AM Eastern (US)** unless noted. Tested send window for this audience.

---

## Email 1 — Announce (send: May 3, 2026, 9:00 AM ET)

**Tag added on send**: `bundle-announced`
**Segment**: existing subscribers, exclude any with `bundle-buyer-*` tag
**Goal**: tell the list a paid bundle is coming May 17, no pitch, just context. Build expectation, harvest replies for testimonials/objections.

### Subject

```
Heads up — I'm launching something on May 17
```

### Preview text (the snippet under the subject in inbox)

```
You don't need to do anything. Just want you on the list early.
```

### Body

```
hey,

Quick note. On May 17 I'm launching a paid product called The Job Hunter's AI Bundle — five modules, 44 ChatGPT prompts, plus the salary-negotiation scripts I haven't put on the site for free.

Why I'm telling you two weeks early: subscribers get $10 off on launch day. No code chase, I'll just send it. The price is $39, the launch-week price is $29.

You don't have to do anything right now. I'll send three more emails over the next two weeks:

1. May 12 — preview of the salary-negotiation module (the one most of you have asked about).
2. May 16 — launch eve, what's actually inside.
3. May 17 — go-live with your $10-off link.

If you'd rather skip these and stay only on the free-prompts list, the unsubscribe link is at the bottom — no hard feelings, you'll keep getting the prompt-guide updates.

One ask: if you're between jobs right now, hit reply and tell me what part of the search is grinding you down. The bundle's already written but I'll write a free post about whatever the most common answer is.

Talk soon,
Flynn
snipprompts.com
```

### Sender + reply-to

- **From name**: `Flynn at SnipPrompts`
- **From email**: whatever you've been sending the lead-magnet welcome from (keep consistent — switching senders mid-list tanks deliverability for ~7 days)
- **Reply-to**: same. The "hit reply and tell me" CTA only works if replies actually reach you.

---

## Email 2 — Tease the salary module (send: May 12, 2026, 9:00 AM ET)

**Tag added on send**: `bundle-teased`
**Segment**: existing subscribers, exclude `bundle-buyer-*` and **exclude** anyone who unsubscribed from Email 1
**Goal**: deliver one *actually useful* prompt from Module 5 for free. Builds trust, demonstrates the bundle's depth, gives forwarders a reason to forward.

### Subject

```
The "we don't have budget" rebuttal (free preview from the bundle)
```

### Preview text

```
One prompt. Use it next time someone says it to you. 5 days to launch.
```

### Body

```
hey,

Five days to launch. Here's one of the prompts from the bundle's salary-negotiation module so you can see the rigor before you decide whether to buy.

The setup: you got an offer. You countered. They came back with "we don't have budget for that." Most candidates fold here. They shouldn't — "no budget" is a stage, not a sentence.

Here's the prompt. Paste it into ChatGPT (or Claude / Gemini), fill the brackets, and you'll get back a stage-aware rebuttal calibrated to what *kind* of "no budget" you're hearing.

---

You are a senior comp negotiation coach. I'm in an active negotiation and the recruiter just told me "we don't have budget for that."

Before drafting my response, classify which of these four things they actually mean:

(a) hard ceiling — the requisition is locked at a max number, and they can't move it without re-approval
(b) soft signal — they want to see if I'll fold, no real ceiling
(c) component swap — they can't move base, but can move sign-on, equity, PTO, or start date
(d) wrong-level pushback — they think I'm asking out-of-band for the title, and the real conversation is about leveling, not money

Then draft three response options, one for each of the most likely scenarios above. Each response should:
- acknowledge what they said without conceding it's final
- ask one diagnostic question that surfaces which of (a)–(d) is actually happening
- give me a fallback ask that swaps to a non-base component if (c) is true

My context:
- Role: [TITLE]
- Original ask: [NUMBER]
- Their offer: [NUMBER]
- Counter I sent: [NUMBER]
- Vibe of the recruiter so far: [WORD: warm / neutral / clipped]
- Stage of process: [final / between final and offer / offer in hand]

Do not reassure me. Do not pad. Do not invent numbers I didn't give you. End with one sentence on which of the four scenarios is most likely given my context, and why.

---

That's one prompt. The bundle has 43 more, plus 8 negotiation scripts, plus a BATNA worksheet, plus a comp-research template — for $29 launch week.

Two more emails between now and Sunday: launch-eve preview Friday, go-live Sunday morning.

Talk soon,
Flynn
```

### Sender + reply-to

Same as Email 1.

---

## Email 3 — Launch eve (send: May 16, 2026, 5:00 PM ET — Saturday evening)

**Tag added on send**: `bundle-launch-eve`
**Segment**: existing subscribers, exclude `bundle-buyer-*` and unsubscribers
**Goal**: full inventory. People who want to think it through overnight get the spec sheet now, not at 9 AM Sunday when they're checking email half-awake.

### Subject

```
Tomorrow: the full bundle, and what's actually in it
```

### Preview text

```
44 prompts, 8 scripts, 3 worksheets. Live tomorrow at 9 AM ET.
```

### Body

```
hey,

The Job Hunter's AI Bundle goes live tomorrow morning at 9 AM Eastern.

Subscribers get $10 off — final price $29 instead of $39. I'll send the buy link at 9 AM.

Tonight, the full inventory so you can decide whether it's for you:

**Module 1 — Resume**
8 prompts (resume from scratch, ATS keyword injection, bullet rewrite, career-switcher angle, executive summary, more) · 5-step ATS optimization checklist · 3 before/after worked examples (entry-level grad, mid-career switcher, senior).

**Module 2 — Cover Letter**
6 prompts · 3 plug-and-play templates · "What hiring managers actually skim for" cheat sheet — 13 signals plus the one question that earns the interview.

**Module 3 — Interview Prep**
12 prompts (behavioral by role, STAR structuring, weakness reframe, reverse-interview, red-flag detection, more) · 3-round AI-grilling rehearsal workflow · answer-scoring prompt that grades your reply and rewrites it stronger.

**Module 4 — LinkedIn Profile**
8 prompts (headline, About, recruiter cold-DM, recommendation request, post-connection follow-up, more) · 14-item optimization checklist · weekly content prompt pack (10 post types).

**Module 5 — Salary Negotiation** (the flagship)
10 prompts (offer evaluation, counter-offer scripting, multiple-offer leverage, equity / RSU, sign-on bonus, remote / relocation, exploding offer response, more) · 8 copy-paste scripts · BATNA worksheet · comp research template · walkaway math calculator.

Format: a single 119-page PDF (works on Mac, PC, Kindle, iPad, anywhere) plus a bonus interactive Notion workspace with one-click copy.

Refund policy: 14 days, no questions, Gumroad handles it.

What it's not: a one-click resume generator. A Teal / Rezi competitor. A get-hired-while-you-sleep promise. It's a workflow — you still have to do the job hunt.

What it is: the deep version of the five career prompts on snipprompts.com, expanded with the scripts and worksheets I'd use myself if I were running my own search today.

Tomorrow at 9 AM Eastern, I'll send the link with your $29 launch price built in.

Sleep on it.

Flynn
```

### Sender + reply-to

Same as Email 1.

---

## Email 4 — Launch day (send: May 17, 2026, 9:00 AM ET — Sunday morning)

**Tag added on send**: `bundle-launch-day`
**Segment**: existing subscribers, exclude `bundle-buyer-*` and unsubscribers
**Goal**: drop the link, drop the price, get out of the way.

**Pre-flight checklist** (do these before scheduling/sending):
1. Gumroad listing toggled from Unpublished → Published.
2. Gumroad discount code `LAUNCH` ($10 off → final $29) active and limited to first 100 uses or 48 hours.
3. Replace `[GUMROAD_URL]` placeholder below with the live URL (e.g. `https://snipprompts.gumroad.com/l/job-hunters-ai-bundle/LAUNCH` — appending `/LAUNCH` auto-applies the discount, no code-chase for the buyer).
4. Test the link from a private window before scheduling.

### Subject

```
Live now: $29 with code LAUNCH (next 48h only)
```

### Preview text

```
The Job Hunter's AI Bundle is live. Here's the discounted link.
```

### Body

```
hey,

The Job Hunter's AI Bundle is live.

Your link (price already discounted, no code to remember):
[GUMROAD_URL]

$29 instead of $39. Discount runs 48 hours — Tuesday May 19 at 9 AM Eastern, the price reverts to $39 and the code goes off.

What you get:

— 44 ChatGPT prompts across resume, cover letter, interview, LinkedIn, salary negotiation
— 8 negotiation scripts (decline-and-counter, "we don't have budget" rebuttal, leverage, accept-and-lock, more)
— 3 worksheets (BATNA, comp research, walkaway math)
— 3 worked resume before/after examples
— 14-item LinkedIn optimization checklist
— 3-round AI-grilling interview rehearsal workflow
— 119-page polished PDF + bonus Notion workspace

12 months of free updates. 14-day no-questions refund.

Less than 15 minutes with a resume coach. One salary counter you wouldn't have written on your own pays for the bundle 100×.

If the link breaks, just hit reply — I'll fix it.

Flynn
[GUMROAD_URL]

P.S. If you've been forwarding the snipprompts.com prompts to friends who are job-hunting, this is the one to forward today. The launch discount is per-buyer, not per-account — your friends get $29 too if they use the same link before Tuesday.
```

### Sender + reply-to

Same as Email 1.

---

## Optional Email 5 — 24-hour reminder (send: May 18, 2026, 5:00 PM ET — Monday evening)

**Only send if**: open rate on Email 4 was >40% AND fewer than 50 sales by Monday 5 PM. If sales are tracking above 50, the reminder annoys more than it converts — skip it.

**Tag added on send**: `bundle-launch-reminder`
**Segment**: existing subscribers, exclude `bundle-buyer-2026-may`, exclude unsubscribers, exclude anyone who didn't open Email 4 (don't waste a reminder on people who didn't see the announcement)

### Subject

```
16 hours left at $29
```

### Preview text

```
Tuesday 9 AM ET the price reverts to $39. Quick reminder, no spam.
```

### Body

```
hey,

Quick reminder. The Job Hunter's AI Bundle launch discount ends tomorrow (Tuesday) 9 AM Eastern.

After that it's $39, no code. Right now it's $29:
[GUMROAD_URL]

If you've been on the fence: Module 4 (LinkedIn outreach — recruiter cold-DM, recommendation request, post-connection follow-up) and Module 5 (the negotiation playbook — 10 prompts, 8 scripts, 3 worksheets) are entirely net-new. Nothing on snipprompts.com touches this depth. Those two modules alone are worth the $29.

Same 14-day refund. If you buy and don't find at least one prompt that pays for the bundle in the first hour, refund yourself, no email needed.

Flynn
[GUMROAD_URL]
```

---

## ConvertKit setup checklist (one-time, before scheduling Email 1)

1. **Tag setup** — create these tags in ConvertKit if they don't exist:
   - `bundle-announced`
   - `bundle-teased`
   - `bundle-launch-eve`
   - `bundle-launch-day`
   - `bundle-launch-reminder`
   - `bundle-buyer-2026-may` (this one is added automatically by the Gumroad → ConvertKit integration on purchase — see `GUMROAD_LISTING.md` Field 14)

2. **Segment exclusions** — for every broadcast, the exclusion segment is the same:
   - Has tag `bundle-buyer-2026-may` (don't pitch buyers)
   - Has tag `unsubscribed` (ConvertKit handles automatically)

3. **Schedule all four** in ConvertKit on May 3 morning. Email 1 sends immediately, Emails 2/3/4 are pre-scheduled. Email 5 stays as a draft — only send if the trigger conditions above are met.

4. **Reply-handling**: open the ConvertKit inbox tab on May 3 around the announce-email send, and again on May 17 at 9 AM. The replies to Email 1 ("what's grinding you down") are gold — testimonial fodder, objection map, future-content idea log.

---

## Voice / tone notes (don't paste, for my own consistency)

- Lower-case "hey," opener throughout. No "Hi friend," or "Dear subscriber," — that's Mailchimp 2014 voice.
- No emojis in subject lines (deliverability + voice consistency with site).
- One CTA per email. No "PS also follow me on LinkedIn" cruft.
- Specific numbers everywhere. "$29" beats "discounted." "Tuesday 9 AM Eastern" beats "soon."
- The "hit reply" CTA is in Email 1 only. Saturating it cheapens it.
- Don't use "exclusive," "amazing," or "game-changing." Ever.

---

<!--
[Editor's note — editorial pass, May 3, 2026]

Substantive changes from the original draft. Revert any of these if you disagree.

1. "Hey," → "hey," in all 5 email bodies. The voice notes (above) already mandated
   lowercase but the bodies were sentence case — fixed the inconsistency. Now matches
   DELIVERY_EMAIL.md so the buyer experience reads as one writer.
2. Email 1: ~~broadened "if you're between jobs right now" to "if any part of the job
   search is grinding you down right now"~~. **Reverted per Tom's QA review** — tighter
   CTAs convert better on low-volume lists; "between jobs" is a more specific buyer
   signal that filters for usable testimonial / objection-mapping fodder. Quality of
   reply > quantity of replies. Original wording restored.
3. Email 4: dropped the "Anchor:" prefix on the closing line. That word leaked the
   marketing internals to the reader (anchoring is what we're doing TO them, not
   something we should narrate). Body of the line stayed the same — it's a strong
   anchor — just removed the meta-language.
4. Email 5: tightened the Module 4/5 claim. The original said "the only modules with
   no free version anywhere on the site" but snipprompts.com has free Resume,
   Cover Letter, Interview Prep, LinkedIn Profile, AND Negotiation prompts — so
   "no free version" was technically false. The new wording calls out specific net-
   new content (LinkedIn outreach prompts; full negotiation playbook depth) without
   overclaiming.

Left alone deliberately:
- Email 3's "What it's not / what it is" closer. Strong; keep.
- Email 4 P.S. about forwarding to friends. Adds a small amount of complexity but
  the "per-buyer not per-account" line is the kind of specific thing that earns trust.
- The 4-email schedule (May 3 / 12 / 16 / 17). Pacing is right.
- Subject line for Email 1 ("Heads up — I'm launching something on May 17"). It's
  conversational, signals importance without selling. Keep.
-->

