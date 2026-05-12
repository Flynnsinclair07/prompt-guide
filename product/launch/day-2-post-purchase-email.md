# Day 2 post-purchase email

**Status**: Draft. Ships post-launch as a Kit Sequence triggered by `bundle-buyer-2026-may` tag.

**Send timing**: 24-36 hours after the tag is applied (i.e., 24-36 hours after manual buyer tagging on Mon May 18).

**Purpose**: Recover buyers who missed the receipt (Promotions/spam), reinforce the highest-leverage starting prompt, and harvest one specific question per buyer for testimonial/objection mapping.

**Sender**: `flynn@snipprompts.com`, "Flynn Sinclair"

---

## Subject

```
How's the bundle treating you?
```

## Preview text

```
24 hours in — quick check. Plus the highest-leverage prompt to run first.
```

## Body

```
hey,

24 hours in — quick check.

Did the PDF and the Notion workspace both land in your Gumroad library? If anything's missing or the Notion duplication link didn't work, hit reply and I'll fix it the same day.

Two starting points depending on where you are:

If you have an offer in hand right now, go straight to page 111 — the BATNA worksheet in Module 5. That's the single highest-leverage artifact in the bundle. Fill it out before you do anything else with the offer. Most candidates who counter without a BATNA leave $5K-30K on the table.

If you're earlier in the search, run the resume bullet rewrite from Module 1 first. It's the prompt that breaks the most "AI slop" patterns — refuses to invent metrics, kills banned phrases like "leveraged" and "synergistic," forces you to surface your real numbers.

One ask: what part of the job search are you actively working on right now? Be specific — "senior PM, switching out of healthcare" beats "looking around." I read every reply and what you tell me shapes what I write next.

Talk soon,
Flynn
```

---

## Voice checks

- ✅ Lowercase "hey," opener
- ✅ No banned phrases (exclusive, amazing, game-changing, incredible, unleash)
- ✅ No emojis, no exclamation points
- ✅ Proper-noun casing: BATNA, Notion, Gumroad, Module 1/5, PDF
- ✅ Specific number (page 111) instead of vague reference
- ✅ Specific dollar range ($5K-30K) instead of "a lot of money"
- ✅ "Hit reply" CTA preserved (one ask per email)
- ✅ Sign-off: "Talk soon, Flynn" (nurture voice, not "— Flynn" receipt voice)

## Build notes

When wiring in Kit (post-launch, Mon May 18 onwards once first buyers exist):

1. **Kit → Automate → Sequences → New Sequence**
2. Name: `Buyer — Day 2 check-in`
3. Trigger: subscriber tagged `bundle-buyer-2026-may`
4. Email 1 of sequence:
   - Delay: 1 day (24 hours from tag apply)
   - Subject + body per above
   - Sender: `flynn@snipprompts.com`
5. Publish sequence

## Future v1.1 considerations (do not action pre-launch)

- Day 5 follow-up: "Did you run any of the prompts? Which one?" — collects efficacy data for the 30-day Typeform survey
- Day 14: "Halfway through your refund window — anything not working?" — surfaces refund-likely buyers BEFORE they hit refund, giving owner a chance to fix or proactively offer help
- These would extend the same Kit Sequence with additional emails on a longer delay
