# Post-Purchase Delivery Email — Job Hunter's AI Bundle

**Status**: Paste-ready. Goes out the moment a buyer purchases on Gumroad.
**Why this email matters more than any other**: it arrives 30 seconds after they pay. They're checking their inbox to make sure the thing actually came through. This is the first sentence of the product experience — not marketing, not nurture, the product.

This file replaces the placeholder draft in `product/job-hunter-bundle-outline.md` Section 7. Voice matches `EMAIL_SEQUENCE.md` and `GUMROAD_LISTING.md`.

---

## Subject lines — primary + 2 A/B alternates

**A (primary, ship this if not testing)**
```
Your Job Hunter's AI Bundle is here
```
Why: utilitarian. The buyer is looking for "did the thing arrive?" — this answers it in five words. No clickbait, no curiosity gap, no padding.

**B (personality lean)**
```
Hey — bundle's ready, plus how to actually use it
```
Why: signals the email isn't just a download link, it's setup advice. Higher intent-to-open from a buyer who wants the *workflow*, not just the file. Slight risk of looking less official, which can hurt deliverability into Primary tab on Gmail.

**C (action lean)**
```
You bought the bundle. Here's where to start.
```
Why: assumes the buyer is action-oriented (most are — they just chose to spend money on a workflow product). Performs well in copy tests for buyer-mindset audiences.

**A/B/C plan**: 33/33/34 split for first ~100 buyers. Pick the winner on **reply rate**, not open rate — replies signal engagement, opens just signal "I checked." Once a winner is locked in, ship that subject for the rest of the launch.

**All three subjects**: no emojis. Doesn't say "DELIVERED" or "ORDER #1234". Doesn't say "Thank you for your purchase!". Reads like a person sent it, which is the point.

---

## Email body — paste-ready (markdown / HTML-safe)

```
hey,

It's here. The PDF is in your Gumroad library — the download
button at the bottom of this email takes you straight to it,
or open gumroad.com/library if you ever lose this email.

What you just bought:

- 44 copy-paste ChatGPT prompts across resume, cover letter,
  interview, LinkedIn, and salary negotiation
- 8 negotiation scripts (the "we don't have budget" rebuttal,
  the "I have another offer" leverage script, the accept-and-
  lock-terms close, more)
- 3 worksheets — BATNA, comp research template, walkaway math
- 3 before/after worked resumes (entry-level grad, mid-career
  switcher, senior IC)
- 14-item LinkedIn optimization checklist + weekly content pack
- Bonus: a Notion workspace mirroring the whole bundle, with
  one-click copy on every prompt — duplicate it to your own
  workspace here: NOTION_DUPLICATION_URL

Three things before you dive in.

1. Start with Module 5 if you have an offer in hand right now.
   Salary negotiation is the fastest dollar-per-hour any prompt
   in here will save you. One counter you wouldn't have written
   on your own pays back what you spent a hundred times. The
   rest of the bundle will still be here next week.

2. Don't run the prompts on a blank slate.
   Every prompt assumes you'll paste your actual resume, the
   actual JD, your actual offer numbers. Without that context
   you get generic ChatGPT output. The prompts are sharp; you
   have to feed them.

3. Open the BATNA worksheet (Module 5) before you run any of
   the negotiation prompts. Prompts 6–10 in Module 5 assume you
   already know your walkaway number. The worksheet takes 15
   minutes and is the difference between countering with
   confidence and bluffing yourself into a pulled offer.

What's coming next:

In about 5 days I'll email you one extra prompt that didn't
make the final cut for length reasons — the "is this offer
below market?" comp triangulator. Still useful, you get it
free for buying.

After that, only when there's something worth saying. Probably
one email a month at most. You can unsubscribe any time and
still keep the bundle.

One ask: hit reply and tell me what role and level you're
hunting for. Doesn't have to be long — "senior PM, switching
out of healthcare" is plenty. I read every reply, and what
people tell me changes what I write next.

Good luck out there.

— Flynn
snipprompts.com

P.S. The bundle gets free updates for 12 months. When ChatGPT
changes (it will), the prompts get rewritten and the same
download link picks up the new version. No re-purchase, no
new email.
```

**Notes on the body**:

- **Notion link**: replace `NOTION_DUPLICATION_URL` (literal placeholder appears twice in this file — HTML body and plain-text fallback). One find/replace before scheduling. `GUMROAD_LISTING.md` Field 12 now points back to this file as the source of truth, so the placeholder lives in one place only.
- **Price not mentioned**: deliberate. They just paid. Saying "$39" or "$29" reminds them what they spent, which can trigger buyer's remorse. Saying "what you spent" abstracts it.
- **No "thank you for your purchase"**: feels corporate. The whole email *is* the thank-you.
- **One CTA, soft**: the reply ask. Download is automatic via Gumroad's button. Notion is bonus. Reply is the only thing being asked for, and it's the thing that builds the list-of-real-humans flywheel.
- **Lowercase opener**: matches the rest of the snipprompts.com voice. Don't capitalize it.
- **No call to "follow on socials"**: takes attention away from the product. Mention socials in email 3 of the post-purchase nurture, not here.
- **The PS does work**: handles the "what about updates?" objection without dedicating a full paragraph to it.

---

## Plain-text fallback (for multipart email, or systems that strip HTML)

Functionally identical content, no markdown bullets, line-flow prose. Use this as the `text/plain` part of a multipart email, or paste this version if your delivery tool only accepts plain text.

```
hey,

It's here. The PDF is in your Gumroad library. The download button at
the bottom of this email takes you straight to it, or open
gumroad.com/library if you ever lose this email.

What you just bought: 44 copy-paste ChatGPT prompts across resume,
cover letter, interview, LinkedIn, and salary negotiation. 8 negotiation
scripts (the "we don't have budget" rebuttal, the "I have another
offer" leverage script, the accept-and-lock-terms close, and more). 3
worksheets — BATNA, comp research template, walkaway math. 3 before/
after worked resumes (entry-level grad, mid-career switcher, senior
IC). A 14-item LinkedIn optimization checklist plus a weekly content
pack. And a bonus Notion workspace mirroring the whole bundle with
one-click copy on every prompt: NOTION_DUPLICATION_URL

Three things before you dive in.

First, start with Module 5 if you have an offer in hand right now.
Salary negotiation is the fastest dollar-per-hour any prompt in here
will save you. One counter you wouldn't have written on your own pays
back what you spent a hundred times. The rest of the bundle will still
be here next week.

Second, don't run the prompts on a blank slate. Every prompt assumes
you'll paste your actual resume, the actual JD, your actual offer
numbers. Without that context you get generic ChatGPT output. The
prompts are sharp; you have to feed them.

Third, open the BATNA worksheet (Module 5) before you run any of the
negotiation prompts. Prompts 6 through 10 in Module 5 assume you
already know your walkaway number. The worksheet takes 15 minutes and
is the difference between countering with confidence and bluffing
yourself into a pulled offer.

What's coming next: in about 5 days I'll email you one extra prompt
that didn't make the final cut for length reasons — the "is this offer
below market?" comp triangulator. Still useful, you get it free for
buying. After that, only when there's something worth saying. Probably
one email a month at most. You can unsubscribe any time and still keep
the bundle.

One ask: hit reply and tell me what role and level you're hunting for.
Doesn't have to be long — "senior PM, switching out of healthcare" is
plenty. I read every reply, and what people tell me changes what I
write next.

Good luck out there.

— Flynn
snipprompts.com

P.S. The bundle gets free updates for 12 months. When ChatGPT changes
(it will), the prompts get rewritten and the same download link picks
up the new version. No re-purchase, no new email.
```

---

## [Setup notes — where to paste this and how to wire it up]

Two ways to deliver this email. **Option A is simpler. Option B is better.** Pick one — don't run both, buyers will get duplicates.

### Option A — Gumroad's built-in receipt customization (10 min, ship-it-today path)

Gumroad sends the receipt automatically the moment a sale completes. You can customize the body, and Gumroad attaches the download button below your text.

1. Gumroad → Products → **Job Hunter's AI Bundle** → **Workflows** tab → **Receipt email**.
2. Subject field: paste **Subject A** above (or whichever variant you're testing).
3. Body field: paste the **email body** block above. Replace `NOTION_DUPLICATION_URL` with the live duplicate-this-template URL from Notion (Share → Publish → "Allow duplicate as template" → copy URL).
4. Save. Send a $0 test purchase to yourself with a 100% discount code to confirm formatting renders correctly.

**Tradeoffs**:
- ✓ Zero extra tooling. Email goes out on purchase, no integration to break.
- ✗ Sends from `noreply@customers.gumroad.com`. Gmail often files this in **Promotions**, not Primary. Lower open rate than a domain email.
- ✗ A/B testing subject lines requires manually toggling the receipt template. Not a real test.

### Option B — ConvertKit sequence triggered by purchase tag (30 min, recommended)

Gumroad's ConvertKit integration tags every buyer with `bundle-buyer-2026-may` on purchase (per `GUMROAD_LISTING.md` Field 14). A ConvertKit Sequence triggered by that tag fires the moment the tag is applied — practically simultaneous with Gumroad's receipt.

1. **Disable** Gumroad's receipt body (leave the auto-receipt for the download link, but blank out the custom message — buyers shouldn't get this email twice).
2. ConvertKit → **Sequences** → New sequence: name it `Bundle Buyer — Day 0 Welcome`.
3. Email 1 of the sequence:
   - Send delay: **immediately** (0 minutes after tag applied).
   - Subject: paste Subject A (or A/B/C if testing — ConvertKit supports per-email subject A/B in the Pro plan).
   - Body: paste the body block above. Replace `NOTION_DUPLICATION_URL`.
   - **Important**: include a download link to the bundle PDF in the body itself, since ConvertKit doesn't attach the Gumroad download button. Either link to `https://snipprompts.gumroad.com/library` (their general library) or upload `job-hunters-bundle.pdf` to a private S3/Drive URL and link directly. The S3 path is cleaner; the library path means buyers always see the latest version.
4. Sequence trigger: **Subscriber tag matches `bundle-buyer-2026-may`**.
5. Sequence → **Publish**.
6. Test: in ConvertKit, manually add the tag to a test subscriber (your own email) and confirm the email fires within 60 seconds.

**Tradeoffs**:
- ✓ Sends from your verified domain. Lands in Primary tab. ~30–40% better open rate than Gumroad's noreply.
- ✓ Real A/B testing on subject lines (ConvertKit's built-in split test).
- ✓ Sets up a multi-email post-purchase nurture sequence — Email 2 (Day 5) is the comp-prompt promised in the body; Email 3 (Day 14) is "how's the hunt going?" check-in; Email 4 (Day 30) is "any new modules to suggest?" feedback ask.
- ✗ Requires the Gumroad → ConvertKit integration to be live and tested. If the integration silently fails, buyers get no welcome — monitor the first 5 sales manually.

### Whichever option you choose

**Replace these placeholders before going live**:

| Placeholder | Replace with | Lives in |
|---|---|---|
| `NOTION_DUPLICATION_URL` | Notion → Share → Publish → "Allow duplicate as template" → copy URL | This file (2 places: HTML body + plain-text body) |

**Don't include the `bundle-buyer-2026-may` segment in the launch-prep broadcast list** — buyers shouldn't get the launch-day pitch. This is already configured in `EMAIL_SEQUENCE.md` (every broadcast excludes the `bundle-buyer-*` tag). Sanity-check before scheduling.

**The Day 5 follow-up email (the "comp triangulator" promise)** isn't drafted yet. The body of this email commits you to writing it within 5 days of launch. If you're not going to ship the comp prompt, edit the body to remove that paragraph before launch — don't ship a promise you won't keep.

### Form UID reference

ConvertKit form UID for the snipprompts.com lead-magnet (the existing list, not buyers): `d02eb77674`. **Do not** trigger the welcome sequence off this form UID — it's the free-prompt list, not the buyer list. Buyer list uses tag `bundle-buyer-2026-may` (set up via Gumroad's CK integration on purchase).

---

## Voice / craft notes (for your reference, don't paste)

- Lowercase "hey," opener. The single voice signal — disarms the "is this automated?" instinct without going full all-lowercase prose (which would just make brand names like ChatGPT look like typos). Matches the EMAIL_SEQUENCE.md pre-launch emails so the buyer's experience reads as one writer.
- No "thank you for your purchase". Feels transactional. The whole email IS the thank-you.
- The three numbered tips lead with imperatives ("Start with", "Don't run", "Open the worksheet"). Not aspirational, not "consider trying" — commands.
- "The prompts are sharp; you have to feed them" — most important sentence in the email. Sets the right relationship between buyer and product. The prompts aren't magic; the buyer's effort is still the bottleneck. Setting that expectation upfront prevents refund requests from buyers who expected one-click hiring.
- The comp-prompt promise is concrete and small. "I'll email you one extra prompt in 5 days" is a specific, falsifiable promise. It builds trust. "I'll send you helpful content" is a vague promise nobody believes.
- "Good luck out there" — warmer than "Good luck". Signals you know they're in the trenches.
- The P.S. does load-bearing work: it neutralizes the "do I have to buy this again next year?" objection without making the email about updates.
- No emojis. No exclamation points. No "amazing" / "incredible" / "exclusive". The buyer just spent money — they don't need to be sold again.

---

<!--
[Editor's note — editorial pass, May 3, 2026]

Substantive change: the original draft used full-lowercase prose throughout the body
("it's here. the PDF is in your gumroad library...") as a deliberate voice signal.
Changed to lowercase "hey," opener + sentence case body for two reasons:

1. Brand-name correctness. ChatGPT, Notion, LinkedIn, Gumroad, Flynn, BATNA, "I" all
   need proper casing. With them lowercase, they read like typos, not voice — which
   undermines the warm-but-professional positioning of a paid product.
2. Consistency with EMAIL_SEQUENCE.md. The pre-launch emails use sentence case body
   with a lowercase "hey," opener. After purchase, the buyer is reading the same
   writer's voice — drift between the two would feel weird. The "hey," signal is
   preserved; the rest of the prose now matches.

The voice / craft notes were also updated to reflect the new style — content is
unchanged, just sentence case.

Left alone deliberately:
- The body content. Every line is doing a specific job (download mechanic →
  what-you-bought recap → 3 imperative tips → 5-day comp-prompt promise → reply ask
  → P.S. for update objection). No filler to cut.
- The 3 subject lines (A/B/C) and the A/B/C decision rationale.
- The Gumroad-vs-ConvertKit setup paths (Option A simpler, Option B better).
- The "the prompts are sharp; you have to feed them" line — keep it, it sets
  expectations that prevent refund regret.
- The comp-prompt promise (5 days). Still concrete, still falsifiable, still good.
-->

