# Email broadcast pre-flight QA — May 7, 2026

**Scope**: Email 2 (May 12 tease), Email 3 (May 16 launch eve), Email 4 (May 17 launch day), Email 5 (May 18 optional reminder) in `EMAIL_SEQUENCE.md`. Email 1 is deprecated (commit `2192921`); not in QA scope.

**Method**: per-broadcast read-through against the 10 QA dimensions Tom called out, plus mechanical greps for stale references / banned phrases / URL correctness.

**Verdict**: **1 launch-blocking finding (Email 3 discount framing). 4 quality-degrades. 2 cosmetic.** All other dimensions across all 4 broadcasts pass clean.

---

## 🔴 Launch-blocking — fix before owner schedules

### LB1 — Email 3 line 163: "$10 off" framing not unified to the "$29 instead of $39 list" pattern

**Where**: `EMAIL_SEQUENCE.md:163`
```
Subscribers get $10 off — final price $29 instead of $39. I'll send the buy link at 9 AM.
```

**Why blocking**: Tom explicitly unified the discount framing across `welcome-sequence.md` Welcome 1 in commit `7d701ce` — the rule was "dollar amounts you'll pay are more concrete than discounts off an unspecified anchor." The fix in Welcome 1 went from `Subscribers get $10 off launch week` to `Subscribers get launch-week pricing: $29 instead of the $39 list`. Email 3 still leads with "$10 off" — the exact framing Tom flagged as inconsistent.

Email 3 ships May 16 at 5 PM ET to the entire pre-launch subscriber list. Subscribers who got Welcome 1 see "$29 instead of the $39 list" first, then read Email 3's "$10 off — final price $29 instead of $39" and notice the framing shift mid-sequence.

**Severity**: 🔴 launch-blocking. Same framing inconsistency Tom called out in Welcome 1; same fix.

**Suggested fix** (paste-ready replacement for line 163):
```
Subscribers get launch-week pricing: $29 instead of the $39 list. I'll send the buy link at 9 AM.
```

Drops "$10 off — final price". Otherwise unchanged.

---

## ⚠️ Quality-degrades — owner triages before or after scheduling

### Q1 — Email 2 line 124: "for $29 launch week" is a third framing variant

**Where**: `EMAIL_SEQUENCE.md:124`
```
That's one prompt. The bundle has 43 more, plus 8 negotiation scripts, plus a BATNA worksheet, plus a comp-research template — for $29 launch week.
```

**Issue**: this isn't literal "$10 off" (the framing Tom replaced) but it's also not the unified "$29 instead of the $39 list" pattern. It's a fragment ("for $29 launch week") that names the price but skips the comparison anchor ($39).

Less material than LB1 because: (a) the framing is closer to the unified pattern than Email 3's, (b) Email 2 sends 5 days before launch when subscribers haven't yet been primed by Welcome 1's exact wording. But still a third variant in a 5-broadcast sequence.

**Suggested fix** (one-line replacement, optional):
```
That's one prompt. The bundle has 43 more, plus 8 negotiation scripts, plus a BATNA worksheet, plus a comp-research template — $29 instead of the $39 list, launch week only.
```

**Severity**: ⚠️ quality-degrades. Fix if owner wants single-framing consistency across the entire pre-launch arc; skip if owner wants Email 2 to read more conversational than Welcome 1's listing-style framing.

### Q2 — Email 3 sign-off uses "Flynn" alone, drifts from `brand-voice.md` Section 4

**Where**: `EMAIL_SEQUENCE.md:194` — Email 3 closes with just `Flynn` (no preamble).

**Issue**: `brand-voice.md` Section 4 documents the pre-launch sign-off variants:
- Pre-launch emails 2–4: `Talk soon,` then `Flynn`
- Email 5 (optional reminder): `Flynn` (no preamble)
- Launch-day email (Email 4): `Flynn` then Gumroad URL

So per the doc, Email 3 should be `Talk soon, / Flynn`. Reality skips the preamble.

Reading the actual Email 3 closer ("Sleep on it. / Flynn"): the terse "Sleep on it." closer reads better without "Talk soon," — adding the preamble would soften a beat that's deliberately punchy.

**Two interpretations**:
- (a) Email 3 is fine as-is; `brand-voice.md` Section 4 over-specified "2–4 use Talk soon" when reality has Email 3 deliberately terse.
- (b) Email 3 should be edited to add `Talk soon,` for doc consistency.

**Suggested fix**: update `brand-voice.md` Section 4 (NOT Email 3 itself) to acknowledge Email 3 uses just `Flynn` for tone reasons. Specifically:

Current `brand-voice.md` line 12:
> - **Pre-launch emails 2–4**: `Talk soon,` then `Flynn` (no URL — the URL is the Gumroad link in the body)

Replace with:
> - **Pre-launch Email 2**: `Talk soon,` then `Flynn` (matches Email 1's warmer pre-launch nurture register)
> - **Pre-launch Email 3 (launch eve)**: `Flynn` alone — paired with the terse "Sleep on it." closer; the preamble would soften the punch

**Severity**: ⚠️ quality-degrades (doc drift, not reality drift). Reality is fine; doc needs reconciliation.

### Q3 — Email 5 sign-off pattern not in `brand-voice.md` Section 4

**Where**: `EMAIL_SEQUENCE.md:300-301` — Email 5 closes with `Flynn` then `[GUMROAD_URL]` on the next line.

**Issue**: `brand-voice.md` Section 4 says Email 5 = `Flynn` (no preamble — terse, reminder is short). It doesn't mention the URL repeat. Reality matches Email 4's `Flynn + URL` pattern (URL repeated as the CTA).

**Why reality is right**: Email 5 is a reminder broadcast to subscribers who haven't bought; the URL needs to be the last thing they see. Same logic as Email 4. Removing the URL would weaken the CTA.

**Suggested fix**: update `brand-voice.md` Section 4 (NOT Email 5 itself) to say:

> - **Email 5 (optional reminder)**: `Flynn` then the Gumroad URL on its own line (same pattern as Email 4 — the reminder's job is to repeat the URL)

**Severity**: ⚠️ quality-degrades (doc drift). Same kind of issue as Q2 — `brand-voice.md` Section 4 was written from the email-headers and missed the URL-after-name pattern in the actual bodies.

### Q4 — Email 4 pre-flight checklist line 211: "$10 off" framing in operational note

**Where**: `EMAIL_SEQUENCE.md:211` — pre-flight checklist for Email 4:
```
2. Gumroad discount code `LAUNCH` ($10 off → final $29) active and limited to first 100 uses or 48 hours.
```

**Issue**: "$10 off → final $29" is internal operational note (instructing owner how to set up the Gumroad discount). Not buyer-facing — buyers never see the pre-flight checklist. But the framing Tom unified away from still appears here.

**Severity**: ⚠️ quality-degrades (internal-doc only, not buyer-facing). Owner can fix when they touch the file next; no rush.

**Suggested fix** (low priority):
```
2. Gumroad discount code `LAUNCH` (set $10 off so final price = $29) active and limited to first 100 uses or 48 hours.
```

Same operational meaning; clarifies that "$10 off" is the Gumroad config setting, not the buyer-facing framing.

---

## 🟡 Cosmetic — flag for awareness, no action needed

### C1 — Email 4 subject says "with code LAUNCH" but body says "no code to remember"

**Where**: 
- `EMAIL_SEQUENCE.md:218` (subject): `Live now: $29 with code LAUNCH (next 48h only)`
- `EMAIL_SEQUENCE.md:234` (body): `Your link (price already discounted, no code to remember):`

**Tension**: subject implies buyer types `LAUNCH` at checkout; body says they don't (because the `/LAUNCH` URL auto-applies the discount).

**Why this is fine**: subjects need recognizable shorthand for inbox scanning; "with code LAUNCH" is a clear value-prop signal even if the actual mechanic is URL-auto-apply. Buyers don't read subjects as literal instructions.

**Severity**: 🟡 cosmetic. No action.

### C2 — "9 AM ET" vs "9 AM Eastern" deliberate split

**Where**: 
- Preview texts use "9 AM ET" form (Email 3 line 153, Email 5 line 283)
- Body texts use "9 AM Eastern" form (Email 3 lines 161 + 190, Email 5 line 291)

**Why this is the deliberate pattern**: per `brand-voice.md` voice notes, long form "Eastern" reads warmer in flowing prose; short form "ET" works better in tight inbox previews. Already noted in `v1.1-backlog.md` NTH15 — owner deferred unification as "deliberate split."

**Severity**: 🟡 cosmetic. No action; tracked.

---

## ✅ Pass per dimension across all 4 broadcasts

| Dimension | Email 2 | Email 3 | Email 4 | Email 5 |
|---|---|---|---|---|
| Lowercase `hey,` opener | ✅ | ✅ | ✅ | ✅ |
| Sentence case body | ✅ | ✅ | ✅ | ✅ |
| Properly cased proper nouns (ChatGPT/Claude/Gemini/BATNA/LinkedIn/Notion/Gumroad/Module N) | ✅ | ✅ | ✅ | ✅ |
| Discount framing | ⚠️ Q1 | 🔴 LB1 | ✅ | ✅ |
| Page count "119" (where mentioned) | n/a | ✅ | ✅ | n/a |
| Refund "30-day" / "30 days" (where mentioned) | n/a | ✅ | ✅ | ✅ |
| Launch date "May 17" / "Tuesday May 19" | ✅ | ✅ | ✅ | ✅ |
| Subject sentence-case, no marketing-speak, no emojis | ✅ | ✅ | ✅ | ✅ |
| One CTA per email | ✅ | ✅ | ✅ | ✅ |
| Sign-off per `brand-voice.md` Section 4 | ✅ | ⚠️ Q2 | ✅ | ⚠️ Q3 |
| URL correctness (snipprompts.com, no flynnsinclair07.github.io) | ✅ | ✅ | ✅ | ✅ |
| No banned phrases | ✅ | ✅ | ✅ | ✅ |
| No "12 months" / "14-day refund" / "141 page" survivors | ✅ | ✅ | ✅ | ✅ |

---

## Mechanical greps run

```bash
# URL correctness — zero hits expected
grep -nE 'flynnsinclair07\.github\.io|github\.io/prompt-guide' EMAIL_SEQUENCE.md
# Result: zero hits ✅

# stale claims — zero hits expected
grep -nE '12 month|14[ -]day|141[ -]page' EMAIL_SEQUENCE.md
# Result: zero hits ✅

# banned phrases — zero hits in email bodies expected
grep -niE 'exclusive|amazing|game[ -]changing|incredible|unleash' EMAIL_SEQUENCE.md
# Result: 1 hit at line 333 (voice notes documenting the rule); zero in email bodies ✅

# $10 off references
grep -nE '\$10 off' EMAIL_SEQUENCE.md
# Result: 3 hits — line 42 (deprecated Email 1, not sending), line 163 (Email 3 body — LB1), line 211 (Email 4 pre-flight, internal — Q4)
```

---

## Recommended owner action sequence

Before scheduling Email 2/3/4/5 in Kit:

1. **Fix LB1** — Email 3 line 163 — replace "$10 off — final price $29 instead of $39" with "launch-week pricing: $29 instead of the $39 list". 1-min edit.

2. **Decide on Q1** — Email 2 framing variant. Owner's call: tighten to match unified pattern, or leave as conversational fragment. 1-min edit if fixing.

3. **Schedule the broadcasts in Kit** with the LB1 fix applied. Email 2/3/4 get scheduled now; Email 5 stays as draft pending May 18 5pm metric check.

4. **Optionally fix Q4** (Email 4 pre-flight checklist "$10 off" wording) — operational only, no schedule impact.

5. **Defer Q2 + Q3** — these are `brand-voice.md` doc drifts, not email body issues. Update `brand-voice.md` Section 4 in the next pass that touches it (or fold into v1.1-backlog if owner wants to defer).

**Total fix time before scheduling**: ~5 min for LB1 + Q1.

---

## What I deliberately did NOT touch

Per Tom's read-only verification rule: zero edits to `EMAIL_SEQUENCE.md`. All findings above are observations + suggested fixes for owner triage. Owner applies fixes manually before/during Kit scheduling.

`brand-voice.md` Section 4 doc-drift items (Q2 + Q3) noted but not edited — that file was identified as the canonical voice authority in the May 6 batch and shouldn't be edited mid-pre-flight.
