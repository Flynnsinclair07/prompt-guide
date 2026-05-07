# Pre-launch welcome sequence — ConvertKit

**Status**: Paste-ready. 3-email sequence triggered on signup at the snipprompts.com homepage form (UID `d02eb77674`). Designed for the May 7 → May 17 pre-launch window; cadence-collapse rule + post-launch handling documented at the bottom.

**Purpose**: new subscribers signing up between today and launch get a value-driven nurture instead of going cold. Each email is value first, soft bundle reference second. After Welcome 3, subscribers join the main launch flow (`EMAIL_SEQUENCE.md`).

**Workflow type**: ConvertKit Sequence (not Broadcast). Sequences fire on a per-subscriber timer relative to signup — exactly the shape Tom called for.

How to use this file:
1. Each email block has subject + preview + body, paste-ready.
2. No placeholders to replace — the URLs are stable snipprompts.com prompt pages.
3. Sequence trigger: form UID `d02eb77674` signup → enter sequence at Welcome 1.
4. Exit conditions: cap Welcome 2 + 3 at May 14 cutoff; subscribers signing up later than that get Welcome 1 only, then go straight into the main launch flow.

---

## Welcome 1 — Immediate (sends 0 hours after signup)

**Tag added on send**: `welcome-active`
**Segment**: all subscribers from form UID `d02eb77674`
**Goal**: acknowledge the signup, deliver immediate value (2 free prompts), set the May 17 expectation, harvest reply signal.

### Subject

```
Welcome — your first 2 free prompts
```

### Preview text

```
Resume + cover letter prompts to start. Heads up about May 17.
```

### Body

```
hey,

Thanks for signing up. snipprompts.com has 134 free, tested ChatGPT prompts — copy, paste, run. No signup walls inside, no upsells in the prompt body, just the prompts.

Two to start with, depending on where you are in the search:

1. Writing a Resume — https://snipprompts.com/prompts/best-chatgpt-prompt-for-writing-a-resume.html
   The full ATS-readable rewrite. Takes about 5 minutes once you paste your raw experience.

2. Writing a Cover Letter — https://snipprompts.com/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html
   Hook-first opener, sounds human, mirrors the JD without copying it.

Both work on free ChatGPT, Claude, or Gemini. The prompts are written around ChatGPT's phrasing but they run the same on any modern model.

Heads up: I'm shipping a paid bundle on May 17 — the deep versions of these five career prompts (resume, cover letter, interview, LinkedIn, salary negotiation), plus 8 negotiation scripts and 3 worksheets you can't find on the free side. Subscribers get $10 off launch week. More on that closer to the date.

One ask: hit reply and tell me what part of the search you're working on right now. Doesn't need to be long — "senior PM, switching out of healthcare" is plenty. I read every reply, and what you tell me changes what I write next.

Talk soon,
Flynn
snipprompts.com
```

### Sender + reply-to

- **From name**: `Flynn at SnipPrompts`
- **From email**: same as the existing lead-magnet welcome (consistency keeps deliverability stable)
- **Reply-to**: same. The "hit reply" CTA only works if replies land somewhere you'll see them.

### Notes

- This is the only email in the welcome sequence with the explicit "hit reply" CTA. Per `brand-voice.md` Section 5, saturating reply CTAs cheapens them — Welcome 2 and Welcome 3 use implicit/soft actions only.
- Subscribers who reply get tagged `replied-welcome-1` (high-engagement signal — informs future broadcasts).

---

## Welcome 2 — Value drop (sends 3 days after signup)

**Tag added on send**: `welcome-2-sent`
**Segment**: subscribers with tag `welcome-active`, exclude `bundle-buyer-2026-may`
**Goal**: deliver one tactical insight that immediately improves whatever AI prompts they're already running. Soft bundle reference at the end.

### Subject

```
The one line that fixes 80% of AI resume prompts
```

### Preview text

```
Most prompts let ChatGPT fabricate metrics. This is the fix.
```

### Body

```
hey,

Quick tactical thing.

Most AI resume prompts you'll find online have a hidden failure mode: they let ChatGPT confidently invent metrics. Numbers, percentages, project outcomes, headcounts. ChatGPT generates plausible-sounding ones because it doesn't know which ones are real, and the prompt doesn't tell it to refuse.

You paste the resume in an interview. The recruiter asks a follow-up about the 28% conversion lift — and you have nothing to say.

The fix is one line. Add this to any AI resume prompt you're running:

"Do not invent achievements, companies, percentages, or metrics not present in my input. If the input doesn't have a number, leave it qualitative."

That's it. Drops the hallucination rate to near-zero on any modern model. Forces the AI to ask you for clarifying numbers when it wants them — which is what you wanted in the first place.

That's one rule. The Job Hunter's AI Bundle (May 17) bakes this kind of rule into all 44 prompts as pre-output gates and banned-phrase lists — the prompts refuse to proceed on weak inputs instead of fabricating to fill gaps. Five career modules, one workflow, resume to offer letter.

More on the bundle next week. For now: try the line above on whatever AI prompt you used last.

Talk soon,
Flynn
```

### Sender + reply-to

Same as Welcome 1.

### Notes

- The tactical insight (the "do not invent" line) is genuine value — it's a real upgrade to any resume prompt the subscriber is currently using. Don't water it down.
- The bundle reference is one paragraph, not the focus. Welcome 2's job is to demonstrate brand-aligned thinking, not sell.

---

## Welcome 3 — Launch pre-tease (sends 7 days after signup, OR May 14, whichever is sooner)

**Tag added on send**: `welcome-3-sent`. Tag `welcome-active` is removed on this send (subscriber is now in the main launch flow segment).
**Segment**: subscribers with tag `welcome-active` AND signup date ≤ May 14, exclude `bundle-buyer-2026-may`
**Goal**: preview a specific framework from the bundle (BATNA), build anticipation for May 17, name the $29 subscriber discount.

### Subject

```
BATNA — the negotiation move most candidates skip
```

### Preview text

```
The framework that decides whether you can walk. May 17 is close.
```

### Body

```
hey,

If you're going to negotiate an offer in the next 6 months, the single most important thing to figure out before the call is your BATNA.

BATNA = Best Alternative To Negotiated Agreement. Plain English: what you'd actually do if this offer falls through. Not your hope, not your aspiration — the specific, real, available option you'd take.

It matters because a negotiation without a real BATNA is just an acceptance. You can't walk, so you can't push. Most candidates over-negotiate from a weak BATNA and get the offer pulled, OR under-negotiate from a strong BATNA and leave $5K–$30K on the table.

The 4-question version, run before any salary call:

1. If this offer goes away today, what do I actually do? (stay in current role / take a specific other live offer / wait on a near-offer / search from unemployment with N months of runway)
2. What's the comp value of that path?
3. How does it compare to this offer (higher / similar / lower / much lower)?
4. Am I confident I'd take it, or am I bluffing myself?

The answers determine how aggressively you can counter. BATNA higher than the offer = walk-away leverage. BATNA much lower = counter from market data and outcomes, not from leverage. The mistake most candidates make is acting like they have leverage when they don't, or hiding leverage they actually have.

If you've got an offer in hand right now — or one you're imagining for the next role — run those 4 questions on your own situation before Sunday. The bundle's BATNA worksheet expands these into a 12-question version with comp triangulation and walkaway math, but the 4 above are 80% of the value.

The Job Hunter's AI Bundle ships May 17 — 5 modules, 44 prompts, 8 negotiation scripts, 3 worksheets including BATNA. Subscribers get launch-week pricing: $29 instead of the $39 list. I'll send the buy link Sunday May 17 at 9 AM ET. No code chase.

Talk soon,
Flynn
```

### Sender + reply-to

Same as Welcome 1.

### Notes

- BATNA preview was chosen specifically because (a) it's a Module 5 (flagship) framework, (b) it doesn't duplicate `EMAIL_SEQUENCE.md` Email 2's "we don't have budget" rebuttal preview — subscribers who get both see different value, and (c) BATNA is novel terminology to most candidates, so it lands as new information.
- The launch-week price reference here is the only place in the welcome sequence where money gets named. Don't move it earlier — value first, price later.

---

## Hand-off to main launch flow

After Welcome 3 fires (or after the May 14 cutoff for late signups), the subscriber's `welcome-active` tag is removed. They become eligible for the main launch broadcasts in `EMAIL_SEQUENCE.md`.

**Per-signup-date timeline** (assuming signup happens between today and launch):

| Signup date | Welcome 1 | Welcome 2 | Welcome 3 | Joins main launch at |
|---|---|---|---|---|
| May 7 | May 7 | May 10 | May 14 | Email 3 (Launch eve, May 16) |
| May 8 | May 8 | May 11 | May 14 (capped) | Email 3 (May 16) |
| May 9 | May 9 | May 12 | May 14 (capped) | Email 3 (May 16) |
| May 10 | May 10 | May 13 | May 14 (capped) | Email 3 (May 16) |
| May 11 | May 11 | May 14 (capped) | skipped | Email 3 (May 16) |
| May 12 | May 12 | May 14 (capped) | skipped | Email 3 (May 16) |
| May 13 | May 13 | May 14 (capped) | skipped | Email 3 (May 16) |
| May 14 | May 14 | skipped | skipped | Email 3 (May 16) |
| May 15 | May 15 | skipped | skipped | Email 3 (May 16) |
| May 16 | May 16 (morning) | skipped | skipped | Email 4 (Launch day, May 17) |
| May 17+ | (post-launch — see below) | | | |

**Cadence-collapse rule**: Welcome 2 and Welcome 3 cap at May 14 (3 days before launch). Subscribers in the active welcome flow on May 14 receive whichever welcome is next-due that day, then exit the welcome flow. Subscribers signing up after May 14 get Welcome 1 only, then go directly into the launch sequence.

**Why cap at May 14**: avoids Welcome 3 colliding with Email 3 (Launch eve, May 16) or sending after the launch broadcast — both of which would feel out of sequence to the subscriber.

**Exclude welcome subscribers from the main launch broadcasts while welcome-active**: every broadcast in `EMAIL_SEQUENCE.md` (Emails 1–5) should add `exclude: tag = welcome-active` to its segment. This prevents subscribers from getting Welcome 2 the same day as Email 2 (May 12 collision risk).

---

## Post-launch handling (May 17+)

The welcome sequence as written assumes the bundle launches May 17 with the $29 subscriber discount. After launch, two things break:

1. **Welcome 3's "$29 launch-week pricing" line is outdated.** The discount expires May 19; signups after that should hear "$39 standard, 30-day no-questions refund" instead.
2. **The launch-day urgency framing ("Sunday May 17 at 9 AM ET") becomes nonsense.** The launch already happened.

**Recommended owner action May 18 (after launch)**:
- Pause this sequence in ConvertKit (don't delete — it's the right shape, just needs Welcome 3 rewritten).
- Build an evergreen Welcome 3 that links to the live Gumroad URL + mentions the standard $39 price + 30-day refund. ~30 min rewrite.
- Re-publish the sequence so new subscribers from May 18 onward get the evergreen version.

This is logged in `v1.1-backlog.md` as **SF13 — Post-launch evergreen Welcome 3 rewrite** (propose adding to the backlog when this commit lands; not yet present).

---

## Setup notes — ConvertKit visual editor flow

ConvertKit's UI rearranges itself every quarter or so, so this is conceptual, not click-by-click. Adapt to whatever ConvertKit looks like the day you build it.

### Step 1 — Create the sequence

ConvertKit → Sequences → New sequence. Name: `Welcome — pre-launch May 2026`.

Add 3 emails to the sequence. For each:
- Send delay (relative to sequence entry, NOT relative to subscribe date — ConvertKit treats these the same when the sequence trigger is "subscribed to form")
  - Welcome 1: 0 hours
  - Welcome 2: 3 days
  - Welcome 3: 7 days
- Subject + preview + body: paste from this file verbatim.
- Send window: 9:00 AM subscriber's local time (ConvertKit's default is good; don't override unless you're seeing weird send times).

### Step 2 — Set the trigger

Sequence settings → "When subscribers should be added":
- Trigger: subscribed to form `Snipprompts homepage signup` (the form with UID `d02eb77674`)
- Add tag on entry: `welcome-active`

### Step 3 — Set exit conditions

Sequence settings → "When subscribers should be removed":
- Remove from sequence when tag `bundle-buyer-2026-may` is added (covers the rare case where a welcome subscriber buys before Welcome 3 fires — they shouldn't get the launch tease after they've bought)
- Remove from sequence when sequence completes (default; ConvertKit handles)

### Step 4 — Cap Welcome 2 + 3 at May 14

This is the cadence-collapse rule and ConvertKit's UI doesn't support date-based send caps natively. Two options:

**Option A — Manual pause** (simpler):
On May 14 evening, owner edits the sequence and toggles Welcome 2 + Welcome 3 to "draft" (i.e., they don't send to anyone still in the sequence). Subscribers added after May 14 get Welcome 1 only, then exit.

**Option B — Visual automation builder** (better, more setup):
Use ConvertKit's Automations (separate from Sequences) — the visual flow builder supports conditional branches with date checks. Build a flow that fires Welcome 1 immediately, then checks "is it before May 14?" before firing Welcome 2 and Welcome 3.

**Recommended for v1**: Option A. It's brittle but works for a 10-day pre-launch window. Set a calendar reminder for May 14 evening to toggle the sequence.

### Step 5 — Tag-based exclusions on main launch broadcasts

Open `EMAIL_SEQUENCE.md` Email 1 / 2 / 3 / 4 / 5 broadcast segments in ConvertKit. Add `welcome-active` to the exclusion tag list for each. This prevents welcome-flow subscribers from getting main launch broadcasts before they finish welcome.

If you skip this step, late-pre-launch signups will get duplicate touches the same day (Welcome 2 + Email 2 on May 12, for example). Annoying, not catastrophic — but easy to fix once.

### Step 6 — Test before activating

Add yourself as a test subscriber via the actual snipprompts.com homepage form (use a personal email you control). Confirm:
- Welcome 1 lands within 5 minutes
- `welcome-active` tag is applied
- Welcome 2 schedules for +3 days (verify the schedule, don't wait)
- Welcome 3 schedules for +7 days
- Exit on `bundle-buyer-2026-may` tag works (manually add the tag; sequence should exit)

Once green, activate the sequence.

---

## Voice / craft notes (for your reference, don't paste)

- Lowercase `hey,` opener on all 3 emails, per `brand-voice.md` Section 1.
- Sentence case body throughout. Properly cased proper nouns: ChatGPT, Claude, Gemini, BATNA, Module 5 (only in Welcome 3 body), per `brand-voice.md` Section 2's lookup table.
- `Talk soon,` / `Flynn` sign-off matches `EMAIL_SEQUENCE.md` Email 1 + Email 2 register (pre-launch nurture). Welcome 1 includes `snipprompts.com` after the name to anchor the brand on first contact; Welcome 2 + 3 drop it (subscriber already knows where the email came from).
- One CTA per email, per `brand-voice.md` Section 5: Welcome 1 has the explicit reply CTA; Welcome 2's CTA is implicit ("try the line above"); Welcome 3's is implicit ("run those 4 questions").
- Specific numbers everywhere: 134 free prompts / 5 minutes / 28% / 4 questions / $5K–$30K / $29 / $39 / 12-question / 9 AM ET / 7 days / 6 months. Per `brand-voice.md` Section 7.
- No banned phrases. No emojis. No exclamation points (P.S. lines were considered but cut for brevity).
- The "do not invent" line in Welcome 2 is the single sentence that ties the welcome sequence to the bundle's positioning. It's the same anti-hallucination rule that runs through every prompt in the bundle, given as a free demo. If a subscriber adds that line to their existing AI prompts and it works for them, the bundle's value proposition just got proved with zero spend.

---

## Suggested addition to v1.1 backlog

After this sequence ships, propose adding to `product/launch/v1.1-backlog.md`:

```
### SF13 — Post-launch evergreen Welcome 3 rewrite
- **Sources**: `welcome-sequence.md` post-launch handling section
- **Description**: Welcome 3's $29 launch-week pricing line goes stale May 19 (discount expires). Sequence needs an evergreen rewrite for new subscribers signing up post-launch.
- **Buyer impact**: minor — subscribers signing up post-launch read a stale launch-day reference. Trust hit, not refund risk.
- **Fix**: rewrite Welcome 3's last 2 paragraphs to reference standard pricing + live Gumroad URL + 30-day refund.
- **Time**: ~30 min.
- **Owner**: worker drafts; owner reviews.
- **When**: v1.1 — first item to ship after May 17 launch (May 18 morning).
```
