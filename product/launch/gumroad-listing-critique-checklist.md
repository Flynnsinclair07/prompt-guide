# Gumroad listing — pre-PH critique checklist

You can't see your live listing the way a $39 buyer sees it. This is the ~10-min pass you do tonight so it's clean when PH traffic hits.

**Open in a private window (so Gumroad's analytics don't track you):**
https://snipprompts.gumroad.com/l/job-hunters-ai-bundle

Read it as someone who clicked from PH at 1:30 AM, knows nothing about you, is on mobile, and has $39 in their account.

---

## The 3 things that will lose you the sale

### 1. The first 10 seconds (the hero)
- [ ] Does the **product name + first sentence** answer "what is this and who is it for?" in 5 seconds? "The Job Hunter's AI Bundle — 44 ChatGPT prompts for the resume-to-offer arc" is fine. "Premium AI workflow accelerator" is not.
- [ ] Is the **price visible above the fold**? Buyers who scroll looking for the price assume it's hidden because it's high.
- [ ] Is the **first gallery image** strong enough that someone who only looks at it can decide? Stock-style "AI brain" graphics are the kiss of death. A screenshot of an actual prompt page is better.

### 2. The middle (the description)
- [ ] Does the description **start with the problem** (AI invents experience, cover letters all sound the same), not the product?
- [ ] Are the **modules listed concretely** — "8 negotiation scripts" not "negotiation guidance"?
- [ ] Is the **30-day refund** mentioned in the body (not just hidden in Gumroad's policy)?
- [ ] **Stale text check:** any "$29 launch pricing" left? Any "119-page" (it's 118)? Any "launches May 17" framing (it's launched)?

### 3. The buy button
- [ ] Default Gumroad buy-button text is "I want this!" — replace with "Get the bundle" or "Get The Job Hunter's AI Bundle." (Exclamation point is a banned brand-voice tell.)
- [ ] Does the **refund** language appear directly under or next to the buy button? Risk-reduction language at the moment of conversion is the single highest-impact lift.

---

## The 5 things that might be worth changing tonight

If you have ~15 min after the dry-run, knock these out:

1. **First paragraph of the description** — if it currently starts with "The Job Hunter's AI Bundle is..." rewrite to lead with the problem. The v2 paste-ready copy in `gumroad-listing-v2.md` opens with "Every ChatGPT job-search prompt on the open internet has the same failure mode" — copy that opener verbatim.

2. **Module list formatting** — convert any wall-of-text into a tight bulleted list with module names + one-line value. Example:
   - **Module 1 — Resume:** 8 prompts including the verification-table version.
   - **Module 5 — Salary Negotiation (flagship):** 10 prompts + 8 scripts + 3 worksheets.
   
   The full version is in `gumroad-listing-v2.md`.

3. **FAQ block** — Gumroad has a built-in FAQ section. Paste in the 8 FAQs from `gumroad-listing-v2.md` (refunds, ChatGPT free tier compatibility, format, "is this a course," "what if I'm not in tech," updates, sales/discounts, sharing).

4. **Gallery images** — confirm the 3-4 currently in there. If any have stale text or look like stock photography, replace with a clean screenshot of a real bundle page (Module 5 BATNA worksheet, or Module 1 resume prompt). Even a low-res screenshot beats a generic graphic.

5. **Suggested price** — Gumroad has a "name your price" toggle. Make sure that's OFF (you want a fixed $39). Make sure the minimum isn't accidentally $0. Make sure there's no leftover discount code from earlier this month.

---

## What NOT to do tonight

- ❌ **Don't change the price.** You set $39; stick to it. Mid-launch price changes confuse and signal panic.
- ❌ **Don't add a discount code "for PH launch."** The hero offer is the 30-day refund, not a discount. Coupons attract bargain-hunters who refund at higher rates.
- ❌ **Don't rewrite the entire listing tonight.** Pre-launch is for confidence-checking, not redesigning. The v2 paste-ready copy can wait until post-launch reflection (use the rest of this week for that).
- ❌ **Don't enable Gumroad's "rated 5 stars by X" widget** if it's based on <5 ratings. Statistically meaningless social proof reads as fake.

---

## After the dry-run: 2-min checklist

- [ ] Click "Buy" yourself (use a different email than your iCloud one) and walk through to the Gumroad checkout. Note any friction.
- [ ] Cancel before completing the purchase. (Don't actually charge your own card.)
- [ ] Check the post-purchase email Gumroad sends — is the file delivery link working? Is the Notion workspace link valid?
- [ ] If anything's broken in the buyer flow, fix BEFORE the PH listing goes live. A broken checkout at minute 5 of a PH launch is the single worst possible outcome.

---

## One more thing — analytics

Gumroad shows you traffic + sales but not "where the traffic came from." Add UTM parameters to your PH link and any social posts:

- PH → `https://snipprompts.gumroad.com/l/job-hunters-ai-bundle?utm_source=producthunt&utm_medium=launch&utm_campaign=may27_launch`
- Show HN (June 2) → `?utm_source=hn&utm_medium=showhn`
- X / LinkedIn → `?utm_source=x&utm_medium=organic`

This way Thursday's gate read tells you not just "X sales" but "X sales from PH, Y from referrals, Z from organic search." That data shapes your June outreach decisions.

You can't UTM-tag the PH "Main link" itself (PH strips it), but you can put the UTM-tagged link in your maker's first comment + Email 5 + the X thread.
