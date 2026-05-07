# Brand voice — canonical reference

**Compiled**: 2026-05-06
**Status**: single source of truth for SnipPrompts brand voice. Future content (v1.1, product #2, ad copy, blog posts) references this file. Existing buyer-facing copy (GUMROAD_LISTING.md, EMAIL_SEQUENCE.md, DELIVERY_EMAIL.md, support-templates.md, PINTEREST_PINS.md) was written against these rules — they should be left alone unless rule changes here drive a coordinated rewrite.

**Method**: rules collected from voice / craft / tone notes scattered across 5+ files. Source attributed per rule (so future readers know where each rule was first articulated). No deduping — repetition across files = high confidence.

---

## 1. Lowercase "hey," opener

**Rule**: every email body opens with `hey,` (lowercase, comma, line break). Every personal Notion page (`00-START_HERE.md`) opens with `hey,`. Every support-template reply opens with `hey,`.

**Why** *(DELIVERY_EMAIL.md voice notes)*: it's the single voice signal. Disarms the "is this automated?" instinct without going full all-lowercase prose (which would make brand names like ChatGPT look like typos). One small deviation from corporate convention; everything else stays professional.

**Why not capitalize** *(EMAIL_SEQUENCE.md voice notes)*: "Hi friend," or "Dear subscriber," reads as Mailchimp 2014 voice. We don't do that.

**Exceptions**:
- **Subject lines**: never start with `hey,` — wastes characters in the inbox preview. Subject A is utilitarian ("Your Job Hunter's AI Bundle is here"), B has personality ("Hey — bundle's ready, plus how to actually use it"), C is action-lean ("You bought the bundle. Here's where to start."). All three are sentence case.
- **Pinterest pin headlines**: not applicable — pins don't have email-style openers.
- **PDF / print content**: not applicable — those are reference docs, not letters.

**Source files where this rule appears**:
- `DELIVERY_EMAIL.md` voice / craft notes (line 229)
- `EMAIL_SEQUENCE.md` voice / tone notes (line 326)
- `support-templates.md` intro (line 3)
- `EDIT_LOG.md` "Voice — 'Hey,' → 'hey,'" section (line 12)

---

## 2. Sentence case body + properly cased proper nouns

**Rule**: after the lowercase `hey,` opener, the rest of the body uses standard sentence case. Every brand name and proper noun gets its proper casing.

**Why** *(EDIT_LOG.md, May 3 editorial pass)*: an earlier draft of `DELIVERY_EMAIL.md` used full-lowercase prose ("it's here. the PDF is in your gumroad library..."). It read as a stylistic choice but had two real costs: (1) brand names like ChatGPT, LinkedIn, Notion, Gumroad read as typos when lowercased — undermining the warm-but-professional positioning of a paid product, and (2) it diverged from EMAIL_SEQUENCE.md, so the buyer reading both surfaces would feel like two different writers. Reversed in commit `ec3b90a`. Lowercase opener stayed; body went sentence case.

**Properly cased proper nouns** (use these spellings exactly):

| Term | Correct | Wrong |
|---|---|---|
| ChatGPT | `ChatGPT` | chatgpt, ChatGpt, Chat GPT |
| Claude | `Claude` | claude |
| Gemini | `Gemini` | gemini |
| GPT-4o | `GPT-4o` | GPT 4o, gpt-4o |
| GPT-4o-mini | `GPT-4o-mini` | GPT 4 mini, gpt4omini |
| Anthropic | `Anthropic` | anthropic |
| OpenAI | `OpenAI` | OpenAi, Open AI, openai |
| Notion | `Notion` | notion |
| Gumroad | `Gumroad` | gumroad |
| ConvertKit | `ConvertKit` | convertkit, ConvertKIT, Convert Kit |
| LinkedIn | `LinkedIn` | linkedin, LinkedIN, Linkedin |
| Pinterest | `Pinterest` | pinterest |
| Stripe | `Stripe` | stripe |
| BATNA | `BATNA` | Batna, batna |
| ATS | `ATS` | ats |
| RSU | `RSU` | rsu |
| ISO | `ISO` | iso |
| NSO | `NSO` | nso |
| PTO | `PTO` | pto |
| MTTR | `MTTR` | mttr |
| API | `API` | api |
| URL | `URL` | url |
| Module 1 (etc.) | `Module 1` | module 1, MODULE 1 |
| Prompt 1 (etc.) | `Prompt 1` | prompt 1, PROMPT 1 |
| Script 1 (etc.) | `Script 1` | script 1 |
| Worksheet 1 (etc.) | `Worksheet 1` | worksheet 1 |
| Levels.fyi | `Levels.fyi` | levels.fyi, Levels.FYI |
| Glassdoor | `Glassdoor` | glassdoor |
| Blind | `Blind` | blind (when referring to teamblind.com) |
| Rezi | `Rezi` | rezi, REZI |
| Teal | `Teal` | teal |
| Huntr | `Huntr` | huntr |
| Flynn | `Flynn` | flynn |
| The Job Hunter's AI Bundle | `The Job Hunter's AI Bundle` | the job hunter's bundle, Job Hunters AI Bundle (no apostrophe) |
| `LAUNCH` (discount code) | `LAUNCH` (uppercase, often backticked) | launch, Launch |
| Pronoun "I" | `I` (always capitalized) | i |

**Source files where this rule appears**:
- `EDIT_LOG.md` "Voice — sentence case body throughout" (line 19)
- `support-templates.md` intro: "lowercase hey, opener, sentence case body, properly cased proper nouns" (line 3)
- `DELIVERY_EMAIL.md` editor's note (line 247)

---

## 3. Banned phrases — never use these

**Rule**: the following phrases are off-limits in all buyer-facing copy. They're the language of products that have nothing real to say.

**Banned**:
- `exclusive` *(EMAIL_SEQUENCE.md voice notes)*
- `amazing` *(EMAIL_SEQUENCE.md voice notes; DELIVERY_EMAIL.md voice notes)*
- `game-changing` *(EMAIL_SEQUENCE.md voice notes)*
- `incredible` *(DELIVERY_EMAIL.md voice notes)*
- `unlock your potential`, `unleash`, `level up` *(general aspirational-language ban — implied by PINTEREST_PINS.md "never aspirational" rule)*
- `Become...`, `Unlock...` (as headline openers) — kills CTR on Pinterest *(PINTEREST_PINS.md voice / pin-copy notes)*
- `Hi friend,` / `Dear subscriber,` *(EMAIL_SEQUENCE.md voice notes — "Mailchimp 2014 voice")*
- `Thank you for your purchase!` (in receipt email) *(DELIVERY_EMAIL.md voice notes — feels transactional; the email IS the thank-you)*
- Exclamation points (used for emphasis) *(DELIVERY_EMAIL.md voice notes)*
- `Anchor:` / `Hook:` / other meta-marketing labels in body copy *(EDIT_LOG.md Email 4 fix — "leaked the marketing internals to the reader")*

**Why these specifically**: each one signals the writer didn't have a specific thing to say. "Exclusive" is the language of a product trying to manufacture scarcity. "Amazing" is the language of a writer reaching for emphasis without earning it. "Unlock your potential" is the language of a course that doesn't know what the buyer's potential is. We have specific things to say (numbers, scenarios, named workflows), so we don't need these crutches.

**Cosmetic ban** — exclamation points: technically allowed in P.S. lines or the rare buyer-affirmation moment, but default to never. The voice is calm, direct, confident. Exclamation points read as nervous.

**Source files where this rule appears**:
- `EMAIL_SEQUENCE.md` voice / tone notes (line 331)
- `DELIVERY_EMAIL.md` voice / craft notes (line 236)
- `PINTEREST_PINS.md` voice / pin-copy notes (line 429)
- `EDIT_LOG.md` Email 4 anchor-prefix fix

---

## 4. Sign-off conventions

**Rule**: every email and every personal Notion page signs off `— Flynn` (em-dash, space, capital F) on its own line, optionally followed by `snipprompts.com` on the next line. Never `Best,` / `Cheers,` / `Sincerely,` / `Best regards,` / `Yours truly,`.

**Why**: those are corporate. We're an indie creator. The em-dash signoff reads as a person, not a brand.

**Variants by context**:
- **Receipt email + Notion Start here**: `— Flynn` then `snipprompts.com` on next line
- **Pre-launch email sequence (Email 1)**: `Talk soon,` then `Flynn` then `snipprompts.com` (slightly warmer because pre-launch nurture is a building-trust moment)
- **Pre-launch emails 2–4**: `Talk soon,` then `Flynn` (no URL — the URL is the Gumroad link in the body)
- **Email 5 (optional reminder)**: `Flynn` (no preamble — terse, reminder is short)
- **Launch-day email (Email 4)**: `Flynn` then the Gumroad URL on its own line (the URL is the CTA, repeated)
- **Support-template replies**: `— Flynn` (just the name; no URL — they already bought)

**Reserved closer**: `Good luck out there.` — used as the warm pre-signoff line in `DELIVERY_EMAIL.md` and `notion/00-START_HERE.md`. Signals "you're in the trenches; I know it." Don't overuse — once per buyer surface is enough.

**Source files where this rule appears**:
- `DELIVERY_EMAIL.md` voice / craft notes ("Good luck out there" — warmer than "Good luck")
- All email bodies in `EMAIL_SEQUENCE.md` (Email 1, 2, 3, 4, 5 each demonstrate the sign-off variant per their context)
- All 8 templates in `support-templates.md`

---

## 5. CTA patterns

**Rule**: every email has **one** CTA. Pinterest pins have **one** outbound link. The CTA is specific (a thing to do), not vague (a thing to feel).

**Why** *(EMAIL_SEQUENCE.md voice notes)*: one CTA per email. No "PS also follow me on LinkedIn" cruft. Adding a second CTA dilutes the first; buyers default to ignoring all of them.

**Email-by-email CTA inventory**:

| Email | Single CTA |
|---|---|
| Email 1 (announce) | "hit reply and tell me what part of the search is grinding you down" — the only email with a reply CTA, deliberately one-shot |
| Email 2 (tease) | implicit: try the prompt that's in the body. No outbound link. |
| Email 3 (launch eve) | implicit: "sleep on it." No outbound link. |
| Email 4 (launch day) | the Gumroad URL — repeated twice for emphasis |
| Email 5 (24h reminder) | the Gumroad URL — single placement |
| DELIVERY_EMAIL.md (receipt) | "hit reply and tell me what role and level you're hunting for" — soft engagement; the download is automatic, not a CTA |

**Pinterest pin CTAs**: every pin has exactly one outbound link in its destination field. Pin description ends with a soft action ("Save it now," "Save before your next interview"). Pin headline is itself the CTA in 4–8 words.

**The "hit reply" CTA**: only in Email 1 of the pre-launch sequence + the DELIVERY_EMAIL.md receipt. Saturating it across multiple emails *(EMAIL_SEQUENCE.md voice notes)* cheapens it.

**CTA voice**: imperative, never aspirational. "Run Module 5" not "consider exploring Module 5." "Hit reply" not "feel free to reach out anytime." The receipt email's three numbered tips are the canonical example: "Start with Module 5", "Don't run the prompts on a blank slate", "Open the BATNA worksheet". Commands, not suggestions.

**Source files where this rule appears**:
- `EMAIL_SEQUENCE.md` voice / tone notes (line 328)
- `DELIVERY_EMAIL.md` voice / craft notes (the three numbered tips lead with imperatives)
- `PINTEREST_PINS.md` voice / pin-copy notes (headlines imperative or declarative, never aspirational)

---

## 6. Anchor language for sales contexts

**Rule**: three anchor lines, used in launch-day social, email sequence, and reply comments. **Never on the Gumroad listing page itself** *(GUMROAD_LISTING.md pricing / positioning sanity check)* — over-anchoring on the listing reads desperate.

**The three anchors**:

1. **"Less than 15 minutes with a resume coach."**
   - Use case: pricing-anchor moment. Pairs with the bundle's $39 list / $29 launch price.
   - Where it lives now: `EMAIL_SEQUENCE.md` Email 4 closing line; `GUMROAD_LISTING.md` pricing rationale (worker reference only, NOT in listing copy).

2. **"One salary counter you wouldn't have written on your own — pays for the bundle 100×."**
   - Use case: ROI-framing. Pairs with Module 5 (Salary Negotiation) marketing.
   - Where it lives now: `EMAIL_SEQUENCE.md` Email 4 closing line.

3. **"Cheaper than the screen-share where someone just reads your resume back to you."**
   - Use case: competitive-positioning anchor. Pairs with the "we're not Rezi/Teal" positioning.
   - Where it lives now: `GUMROAD_LISTING.md` pricing rationale (worker reference only, NOT in listing copy).

**When to use each**: anchor #1 for emails to fence-sitters; #2 for offer-in-hand-buyer messaging; #3 for "I already have Rezi/Teal" objection handling.

**When NOT to use**: on the Gumroad listing page itself. Listing copy says what the bundle is + what's inside. Anchors are pull-the-trigger language, not reading-the-listing language. Mixing them on the listing page reads as too-aggressive sales.

**Source files where this rule appears**:
- `GUMROAD_LISTING.md` "Pricing / positioning sanity check" section (lines 252–258)
- `EDIT_LOG.md` "Email 4 anchor line: dropped the leading 'Anchor:' " (line 60)

---

## 7. Specific numbers, concrete time references, plain English

**Rule**: every claim has a number or a concrete time reference where one is available.

**Why** *(EMAIL_SEQUENCE.md voice notes)*: "$29" beats "discounted." "Tuesday 9 AM Eastern" beats "soon." Specificity is the single biggest separator between buyer-trusts-you copy and buyer-suspects-you copy.

**Examples (correct)**:
- ✅ "44 ChatGPT prompts" (not "many prompts")
- ✅ "119-page PDF" (not "a comprehensive PDF")
- ✅ "30-day no-questions refund" (not "great refund policy")
- ✅ "May 17, 2026, 9:00 AM ET" (not "soon" or "next week")
- ✅ "Tuesday May 19 at 9 AM Eastern, the price reverts to $39" (not "the discount expires soon")
- ✅ "Cut p95 latency 62%" (not "improved performance significantly")
- ✅ "Less than 15 minutes with a resume coach" (not "incredibly affordable")

**Examples (wrong — these would never make it past editing)**:
- ❌ "The bundle is comprehensive and packed with value"
- ❌ "Buyers love it"
- ❌ "Game-changing prompts"
- ❌ "Unlock your career potential"

**Plain English** *(implicit across all files)*: short sentences. Concrete verbs. No throat-clearing. If a sentence can be cut without losing meaning, cut it. The voice that comes out of this rule is direct, professional-but-warm, like a senior friend giving advice over coffee. No hedging ("you might want to consider thinking about..."), no padding ("at the end of the day...").

**Source files where this rule appears**:
- `EMAIL_SEQUENCE.md` voice / tone notes (line 329)
- `PINTEREST_PINS.md` voice / pin-copy notes (line 430 — "Numbers in headlines beat words")
- Implicit in every existing buyer-facing file

---

## 8. Surface-specific rules

### Email subject lines

- **No emojis** *(EMAIL_SEQUENCE.md voice notes)* — deliverability + voice consistency.
- **Sentence case** in subjects (capitalize first word, then proper nouns only). Not Title Case Like This (looks corporate). Not all-lowercase like body opener (looks unprofessional in inbox).
- **Length target**: 40–60 characters. Inbox truncates around 60.
- **A/B/C variants documented in `DELIVERY_EMAIL.md`**: utilitarian (A), personality (B), action-lean (C). Default to A; test others on volume.

### Pinterest pins

- **Headlines**: imperative or declarative, never aspirational. ≤8 words across 2–3 lines.
- **Numbers in headlines beat words**: "90 seconds" / "$29" / "60 seconds" / "300 characters."
- **"Free" in headlines only on free-prompt pins** (Pins 6–12 + 16–18). Bundle pins (13–15, 19–25) lead with the bundle as the anchor, not "free."
- **Benefits**: 3 lines, ≤4 words each, with checkmark glyphs (✓).
- **No emojis** in pin headlines or descriptions.
- **Hashtags only at the end of descriptions**. 6–8 hashtags max. Lowercase, no spaces.
- **Aesthetic**: 1000×1500, navy `#1B2A4E` or forest `#1F3D2E` background, cream `#F5EBDD` text, Arial Black headline.

### Support-template replies

- **1–3 sentences per response** *(support-templates.md intro)*. No fluff.
- **No subject line** — email client auto-prefixes "Re: " on the buyer's original.
- **Voice matches DELIVERY_EMAIL.md exactly**: lowercase `hey,` opener, sentence case body, properly cased proper nouns, signed `— Flynn`.
- **Operational notes per template** (in the source doc, not in the buyer-facing reply) explain when to use and what to watch for.
- **Catalog grows from real buyer questions**, not anticipated ones. New patterns get added to support-templates.md as they come up.

### PDF / print content

- **No "hey," opener** — PDF is reference content, not a letter.
- **Module intros use directional voice** — "How to use this module" / "When to use this module."
- **Code blocks for prompts** preserve `**bold**` markdown literally — buyers paste into ChatGPT, which renders the markdown (this is correct behavior, not a bug).
- **Sentence case body, properly cased proper nouns** — same as email body rules.

---

## 9. Tone calibration — what's allowed

The voice should feel like a senior friend who has done this before, telling you exactly what to do, with the specifics you'd want.

**Allowed**:
- Direct: "Don't run the prompts on a blank slate."
- Specific numbers: "$29 instead of $39", "44 prompts", "30-day refund"
- Concrete time references: "Tuesday May 19 at 9 AM Eastern", "in about 5 days"
- Plain English: "The prompts are sharp; you have to feed them."
- Warm signoffs: "Good luck out there."
- Light personality: "Sleep on it." / "Hit reply and tell me what role you're hunting for."
- Domain-savvy: BATNA, ATS, RSU, ISO, NSO references — assume buyer is in the work, not learning the work
- Honest framing: "What it's not: a one-click resume generator."
- Light em-dashes for emphasis (not overdone — see `BUYER_READ_NOTES_2026-05-03.md` em-dash density observation; flagged for v2 voice review)

**Not allowed**:
- Aspirational language ("become," "unleash," "transform")
- Vague claims ("comprehensive," "powerful," "value-packed")
- Banned phrases (Section 3)
- Marketing meta-labels ("Anchor:", "Hook:")
- Multiple CTAs in one email
- Emojis (subject lines, pin content; allowed only in Module 3 P12 traffic-light semaphore 🟢🟡🟠🔴 which is functional, not decorative)
- Exclamation points (default to no; rare exception in P.S. lines)
- Cheerleader energy ("You can do this!" — patronizing for a $39 buyer)

---

## 10. Voice tics to be aware of (worth tracking, not fixing yet)

These are observed patterns in current copy. None are wrong; all are worth knowing about for future style consistency.

### Em-dash density
*(BUYER_READ_NOTES_2026-05-03.md Tom's criteria #3 + v1.1-backlog.md V2-2)*

Across all 5 modules + receipt email + sequence emails, em-dashes do triple duty: parenthetical, dramatic pause, definition. A reader notices after ~50 pages. Not wrong; voice tic.

**Status**: deferred to v2.0 voice review. Don't try to fix prompt-by-prompt or email-by-email; it'd be a coordinated full-pass edit.

### Sentence-fragment closers
*(implicit pattern, not formally noted yet)*

Closing sentences are often fragments: "Sleep on it." / "Good luck out there." / "Got it." Reads as confident. Use sparingly — every email starting AND ending with a fragment would feel performative.

### Anti-template rhetoric
*(GUMROAD_LISTING.md description; PINTEREST_PINS.md Pin 14)*

The brand defines itself against "templates" — "the anti-template", "screenshots of one-line prompts you've already tried", "the bundle has 10 [where free internet has one]". Powerful but limited; if every single piece of copy positions against templates, the framing dulls. Reserve for the highest-leverage moments (Pin 24, Pin 25, Gumroad listing description).

---

## How to use this file going forward

1. **New buyer-facing copy** (v1.1 emails, ad copy, blog posts, product #2 listing): match every rule in sections 1–8. Voice tics in section 10 are aware-of-not-blocking.
2. **Existing buyer-facing copy** (the locked files): don't rewrite to match this doc unless you're already touching the file for another reason. The rules here were extracted from those files; they already match.
3. **Cross-file voice drift** (e.g., "9 AM ET" vs. "9 AM Eastern"): document in `v1.1-backlog.md`, fix in v1.1 cycle. Don't fix one-off.
4. **Edge cases this doc doesn't cover**: write the new copy in the spirit of these rules, then surface the gap (e.g., "no rule for video-script voice yet — drafted using closest-fitting rules, please review"). Add a section 11+ when 2+ similar gaps emerge.
5. **Style disagreements with the rules**: argue with the rules, then write the rule change here BEFORE writing the copy. The rules earn their place by being consistently applied; one-off exceptions weaken the whole frame.

---

## Source attribution summary

| Source file | Section(s) of rules contributed |
|---|---|
| `DELIVERY_EMAIL.md` voice / craft notes | 1, 2, 3, 4, 5, 6, 9 |
| `EMAIL_SEQUENCE.md` voice / tone notes | 1, 3, 5, 7, 8, 9 |
| `PINTEREST_PINS.md` voice / pin-copy notes | 3, 5, 7, 8, 9 |
| `GUMROAD_LISTING.md` pricing / positioning sanity check | 6 |
| `support-templates.md` intro + 8 templates | 2, 4, 8 |
| `EDIT_LOG.md` editorial-pass findings | 1, 2, 3, 6 |
| `BUYER_READ_NOTES_2026-05-03.md` worker observations | 10 |

Each source file's voice / craft notes section can stay as-is for in-context reference. This file is the canonical when they conflict; if they conflict, this file wins.
