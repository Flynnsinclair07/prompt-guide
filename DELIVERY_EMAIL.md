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

it's here. the PDF is in your gumroad library — the download
button at the bottom of this email takes you straight to it,
or open gumroad.com/library if you ever lose the email.

what you just bought:

- 44 copy-paste chatgpt prompts across resume, cover letter,
  interview, linkedin, and salary negotiation
- 8 negotiation scripts (the "we don't have budget" rebuttal,
  the "i have another offer" leverage script, the accept-and-
  lock-terms close, more)
- 3 worksheets — BATNA, comp research template, walkaway math
- 3 before/after worked resumes (entry-level grad, mid-career
  switcher, senior IC)
- 14-item linkedin optimization checklist + weekly content pack
- bonus: a notion workspace mirroring the whole bundle, with
  one-click copy on every prompt — duplicate it to your own
  workspace here: NOTION_DUPLICATION_URL

three things before you dive in.

1. start with module 5 if you have an offer in hand right now.
   salary negotiation is the fastest dollar-per-hour any prompt
   in here will save you. one counter you wouldn't have written
   on your own pays back what you spent a hundred times. the
   rest of the bundle will still be here next week.

2. don't run the prompts on a blank slate.
   every prompt assumes you'll paste your actual resume, the
   actual JD, your actual offer numbers. without that context
   you get generic chatgpt output. the prompts are sharp; you
   have to feed them.

3. open the BATNA worksheet (module 5) before you run any of
   the negotiation prompts. prompts 6-10 in module 5 assume you
   already know your walkaway number. the worksheet takes 15
   minutes and is the difference between countering with
   confidence and bluffing yourself into a pulled offer.

what's coming next:

in about 5 days i'll email you one extra prompt that didn't
make the final cut for length reasons — the "is this offer
below market?" comp triangulator. still useful, you get it
free for buying.

after that, only when there's something worth saying. probably
one email a month at most. you can unsubscribe any time and
still keep the bundle.

one ask: hit reply and tell me what role and level you're
hunting for. doesn't have to be long — "senior PM, switching
out of healthcare" is plenty. i read every reply, and what
people tell me changes what i write next.

good luck out there.

— flynn
snipprompts.com

p.s. the bundle gets free updates for 12 months. when chatgpt
changes (it will), the prompts get rewritten and the same
download link picks up the new version. no re-purchase, no
new email.
```

**Notes on the body**:

- **Notion link**: replace `NOTION_DUPLICATION_URL` (literal placeholder, also referenced in `GUMROAD_LISTING.md` Field 12). One find/replace before scheduling — same string in both files.
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

it's here. the PDF is in your gumroad library. the download button at
the bottom of this email takes you straight to it, or open
gumroad.com/library if you ever lose the email.

what you just bought: 44 copy-paste chatgpt prompts across resume,
cover letter, interview, linkedin, and salary negotiation. 8 negotiation
scripts (the "we don't have budget" rebuttal, the "i have another
offer" leverage script, the accept-and-lock-terms close, and more). 3
worksheets — BATNA, comp research template, walkaway math. 3 before /
after worked resumes (entry-level grad, mid-career switcher, senior
IC). a 14-item linkedin optimization checklist plus a weekly content
pack. and a bonus notion workspace mirroring the whole bundle with
one-click copy on every prompt: NOTION_DUPLICATION_URL

three things before you dive in.

first, start with module 5 if you have an offer in hand right now.
salary negotiation is the fastest dollar-per-hour any prompt in here
will save you. one counter you wouldn't have written on your own pays
back what you spent a hundred times. the rest of the bundle will still
be here next week.

second, don't run the prompts on a blank slate. every prompt assumes
you'll paste your actual resume, the actual JD, your actual offer
numbers. without that context you get generic chatgpt output. the
prompts are sharp; you have to feed them.

third, open the BATNA worksheet (module 5) before you run any of the
negotiation prompts. prompts 6 through 10 in module 5 assume you
already know your walkaway number. the worksheet takes 15 minutes and
is the difference between countering with confidence and bluffing
yourself into a pulled offer.

what's coming next: in about 5 days i'll email you one extra prompt
that didn't make the final cut for length reasons — the "is this offer
below market?" comp triangulator. still useful, you get it free for
buying. after that, only when there's something worth saying. probably
one email a month at most. you can unsubscribe any time and still keep
the bundle.

one ask: hit reply and tell me what role and level you're hunting for.
doesn't have to be long — "senior PM, switching out of healthcare" is
plenty. i read every reply, and what people tell me changes what i
write next.

good luck out there.

— flynn
snipprompts.com

p.s. the bundle gets free updates for 12 months. when chatgpt changes
(it will), the prompts get rewritten and the same download link picks
up the new version. no re-purchase, no new email.
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

- "hey," lowercase. matches the rest of the site voice and disarms the "is this an automated email?" instinct.
- no "thank you for your purchase". feels transactional. the value of the bundle is the thank-you.
- the three numbered tips lead with imperatives ("start with", "don't run", "open the worksheet"). not aspirational, not "consider trying". commands.
- "the prompts are sharp; you have to feed them" — most important sentence in the email. sets the right relationship between buyer and product. the prompts aren't magic; the buyer's effort is still the bottleneck. setting that expectation upfront prevents refund requests from buyers who expected one-click hiring.
- the comp-prompt promise is concrete and small. "i'll email you one extra prompt in 5 days" is a specific, falsifiable promise. it builds trust. "i'll send you helpful content" is a vague promise nobody believes.
- "good luck out there" — warmer than "good luck". signals you know they're in the trenches.
- the PS does load-bearing work: it neutralizes the "do i have to buy this again next year?" objection without making the email about updates.
- no emojis. no exclamation points. no "amazing" / "incredible" / "exclusive". the buyer just spent money — they don't need to be sold again.
