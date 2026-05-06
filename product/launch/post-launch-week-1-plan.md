# Post-launch week 1 ops plan — May 18–24, 2026

Daily ops cadence for the seven days after launch. Lighter than launch day, but not zero — week 1 is when buyer trust is forged or broken.

**State entering week 1** (per `day-1-launch-checklist.md`):
- Bundle published on Gumroad (May 17 9am ET)
- `LAUNCH` discount expires May 19 9am ET (or first 100 uses, whichever)
- Email 4 sent May 17 9am ET; Email 5 (24h reminder) is conditional on May 18 5pm
- Pin 15 posted May 17 morning; Pins 16–25 drip per `PINTEREST_PINS.md`
- May 17 metrics captured in `tracking/daily-metrics-template.csv`

**Week-1 themes**:
1. Convert remaining list interest before discount expires (May 18–19)
2. Land the first batch of refunds without panicking — most happen day 2–7
3. Maintain Pinterest momentum without burst-uploading
4. Decide whether to escalate to YouTube planning or hold (May 24 gate check)

---

## Daily monitoring rhythm — 3 check-ins per day

Same shape every day; the contents change by phase of the week.

### Morning check (15–20 min, ~9am ET / 7am MDT)
- **What**: scan inbox for support emails received overnight; scan Gumroad → Sales for overnight sales count + any refund flags.
- **Where**: inbox + Gumroad → Sales.
- **Time**: 15 min normal, 20 min if 3+ support emails queued.

### Afternoon check (10 min, ~1pm ET / 11am MDT)
- **What**: reply to any support email older than 4 hours; quick glance at Pinterest analytics on yesterday's pin (impressions + saves).
- **Where**: inbox + Pinterest → Analytics.
- **Time**: 10 min normal.

### Evening check (15 min, ~6pm ET / 4pm MDT)
- **What**: snapshot daily metrics into `tracking/daily-metrics-template.csv` — sales count, refund count, Email open/click for any sent broadcast, Pinterest pin impressions/clicks. Reply to remaining support emails so nothing crosses the next morning.
- **Where**: each platform's analytics + tracking spreadsheet.
- **Time**: 15 min normal.

**Total daily ops time**: ~40–45 min on quiet days, ~70 min on heavy days.

---

## Support email triage rules

Use templates from `product/launch/support-templates.md` first. Don't write fresh replies unless the question doesn't fit any template.

| Email type | Template | Response time target |
|---|---|---|
| Refund request | Template 1 | **24 hours max** (process refund first, then reply) |
| Notion link missing | Template 2 | 24 hours max (recovery path = high friction = high refund risk) |
| PDF won't open | Template 3 | 24 hours max (same logic) |
| Model compatibility (Claude/Gemini) | Template 4 | 48 hours |
| Sharing / gifting | Template 5 | 48 hours |
| Day-5 prompt question | Template 6 | 48 hours |
| v2 question | Template 7 | 48 hours |
| Discount expired | Template 8 | 48 hours |
| Doesn't fit any template | (write fresh) | 48 hours, log for v1.1 |

**Workflow**:
1. Open email → match against template list
2. If match: copy template → paste → personalize bracketed bits → send
3. If no match: write fresh reply in same voice (lowercase `hey,`, sentence case, `— Flynn` sign-off), then add the new template to `support-templates.md` per its catalog-grows footer

**Never**:
- Apologize for the bundle's existence ("sorry it didn't work for you" — say "refund processed" instead)
- Promise features that aren't shipped ("I'll add that in v1.1!" — say "logging for v1.1 consideration")
- Reply faster than 1 hour (don't be available; sets unsustainable expectation)

---

## Refund handling

**Refund without question** (Template 1, process within 24h):
- Buyer says "this isn't what I expected" / "doesn't work for my situation" / "I changed my mind" / any soft refund-trigger
- Process refund in Gumroad → Sales → find buyer → Refund button
- Reply with Template 1 text
- Log refund reason in a single text file `product/launch/refund-log-2026-05.md` (create on first refund). Format: `YYYY-MM-DD | order ID | reason in buyer's own words`

**Ask one follow-up before refunding** (rare — only when refund would set bad precedent):
- Buyer says "the prompts didn't work" without specifics — one-line follow-up: "Quick question to make this useful for v1.1: which prompt and what was the output?" Then refund regardless of answer.
- Buyer says "I bought the wrong thing" — one-line: "Got it — refunding now. Quick question to help me improve the listing: what did you think you were buying?"

**Don't ever**:
- Refuse a refund within the 30-day window
- Argue the buyer's reasoning
- Take longer than 24 hours to process

**For v1.1 learnings**: at end of week 1 (May 24), read `refund-log-2026-05.md`. Look for patterns. If 3+ refunds cite the same issue, that's a v1.1 must-fix in `product/launch/v1.1-backlog.md`.

---

## Pinterest cadence

**Existing schedule** (per `PINTEREST_PINS.md` Pins 16–25 cadence table):
- May 18 → Pin 16 (Salary screen)
- May 20 → Pin 17 (Weakness question)
- May 22 → Pin 19 (100 applications)
- May 24 → Pin 20 (Recruiter ghost)

That's 4 new pins in week 1.

**To hit Tom's 5–10 pins/week target**, supplement with **repins of older pins** (Pins 6–12 from launch ramp). Pinterest treats a repin to the same board as a fresh impression — the algorithm doesn't penalize. Pick the 2–3 highest-performing pins from the May 4–17 ramp (check Pinterest → Analytics → top pins by impression) and repin them on otherwise-empty days.

**Daily Pinterest workflow** (~10 min on post-days, ~3 min on no-post days):

| Day | New pin to post | Repin candidate (optional, owner's call) |
|---|---|---|
| May 18 | Pin 16 (Salary screen) | — |
| May 19 | — (rest from launch week) | optional repin: highest-performing pin May 4–17 |
| May 20 | Pin 17 (Weakness question) | — |
| May 21 | — | optional repin |
| May 22 | Pin 19 (100 applications) | — |
| May 23 | — | optional repin |
| May 24 | Pin 20 (Recruiter ghost) | — |

**Rule**: don't post 2 fresh pins same day. Pinterest's algorithm flags burst-uploading on small boards — costs you reach for ~24h after.

**Production process per pin** (~10 min):
1. Open `pins/pin-01-resume.png` in Canva → "Use as template"
2. Swap headline, sub-line, benefits per the spec block in `PINTEREST_PINS.md`
3. Export PNG, 1000×1500, "Best" quality
4. Upload directly to Pinterest (don't use Canva's share-to-Pinterest)
5. Paste description + alt text from spec block
6. Set destination link
7. Schedule for next morning at 7am ET (Pinterest reach peaks 7–9am ET on weekdays)

---

## ConvertKit follow-up

**Email 5 (24-hour reminder)** — May 18 5pm ET decision:
- **Send if**: Email 4 open rate >40% AND fewer than 50 sales by Monday 5pm ET
- **Skip if**: sales tracking above 50 (reminder annoys more than converts)
- Body already drafted in `EMAIL_SEQUENCE.md` Email 5 — has `[GUMROAD_URL]` placeholder, replace with live URL before send

**Next broadcast after Email 5 (or skip-of-5)** — earliest May 24 evening:
- Don't send anything May 19–23. Buyer fatigue is real after a 4-email launch sequence; subscribers need a week of silence to recalibrate.
- May 24 evening or May 25 morning is the earliest acceptable next-broadcast window.

**Three options for the May 24+ broadcast** (decide based on week 1 metrics):
1. **First-week thanks + soft proof** (if 10+ sales, no surprises): "Hey — thanks to the X of you who picked up the bundle. Here's what people are using it for first..." — Light, warm, no re-pitch. Builds list trust.
2. **Value email — one new prompt** (if sales <10 or feedback is sparse): one fresh prompt in the body, no Gumroad link, just value. Re-engages list without selling. Pulls from the comp-triangulator concept that's in v1.1 backlog (only if it's been written by then).
3. **Skip until June** (if list is fatigued — unsubscribe rate on Email 4 was >2%, or open rate <25%): cool-off period, next email June 1+ when there's something genuinely new to say.

**Default recommendation**: option 1 if launch hit 10+ sales, option 2 if 1–9 sales, option 3 if 0 sales. Make the call Sunday May 24 evening.

---

## Sales monitoring metrics

Capture in `tracking/daily-metrics-template.csv`, one row per day. Required columns:

| Column | Where | Notes |
|---|---|---|
| `date` | — | YYYY-MM-DD |
| `sales_count` | Gumroad → Sales | total since launch (cumulative) |
| `sales_today` | Gumroad → Sales | new today only |
| `refund_count` | Gumroad → Refunds | total since launch (cumulative) |
| `refund_rate` | calculated | refund_count / sales_count, rounded to 1 decimal |
| `discount_uses` | Gumroad → Discounts → LAUNCH | only relevant May 17–19 |
| `email_opens` | ConvertKit → broadcasts | for any broadcast sent that day |
| `email_clicks` | ConvertKit → broadcasts | for any broadcast sent that day |
| `pinterest_impressions` | Pinterest → Analytics → Overview | last-24h (cumulative monthly is also useful) |
| `pinterest_outbound_clicks` | Pinterest → Analytics → Overview | last-24h |
| `gumroad_traffic_source` | Gumroad → Sales (per-sale referrer if available) | "ConvertKit / Pinterest / direct / other" |
| `support_emails_in` | inbox | count |
| `support_emails_replied` | inbox | count |

**Why daily, not weekly**: trends only show in dailies. Refund clusters on day 3 vs. day 6 mean very different things; weekly aggregates hide that.

---

## Day-by-day plan

### Mon May 18 — first full ops day

**Time budget**: ~70 min (heavier than typical because of Email 5 decision + first metrics capture).

**Morning (~9am ET, 20 min)**:
- [ ] Scan inbox for overnight support emails, reply with templates (most likely: PDF-won't-open, Notion-link-missing). Target: clear inbox by 10am.
- [ ] Gumroad → Sales: capture overnight sales count.
- [ ] Open `tracking/daily-metrics-template.csv`, add May 18 row.

**Afternoon (~1pm ET, 10 min)**:
- [ ] Production: build Pin 16 (Salary screen) in Canva per spec. Upload directly to Pinterest, schedule for tomorrow 7am ET.
- [ ] Glance at Pin 15 analytics (24h post-launch) — impressions, saves, outbound clicks.

**5pm ET — Email 5 decision (15 min)**:
- [ ] Pull Email 4 stats from ConvertKit: open rate, click rate, unsubscribe count.
- [ ] Pull Gumroad sales count.
- [ ] Decide: send Email 5 or skip per the rules above.
  - If sending: replace `[GUMROAD_URL]` in body with `https://snipprompts.gumroad.com/l/job-hunters-ai-bundle/LAUNCH`, schedule for 5:30pm ET (next 30 min).
  - If skipping: mark Email 5 in ConvertKit as "do not send".
- [ ] Note decision + reasoning in tracking spreadsheet's notes column.

**Evening (~6pm ET, 15 min)**:
- [ ] Refresh metrics row in spreadsheet.
- [ ] Reply to any support emails received during the day.
- [ ] Verify Pin 16 is scheduled for tomorrow morning.

**Success criteria**: zero support emails older than 24h. Email 5 decision made + executed. Day 1 metrics row complete.

---

### Tue May 19 — discount expiration day

**Time budget**: ~50 min.

**Morning (~9am ET, 20 min)**:
- [ ] **At 9am ET sharp**: verify the LAUNCH discount has expired automatically (per the Field 11 cap of May 19 23:59 UTC, which is May 19 7:59pm ET — wait, that's later in the day. Earlier expiration would be the 100-use cap if hit). Check Gumroad → Discounts → LAUNCH to see if it's still active or capped.
- [ ] If still active and 100-use cap not reached: leave it; lets the cap or the Tuesday-end timer fire naturally.
- [ ] Pin 16 (Salary screen) goes live — verify it's posted, glance at first 90 minutes of impressions.
- [ ] Process overnight support emails.
- [ ] Capture overnight sales count.

**Afternoon (~1pm ET, 10 min)**:
- [ ] Build Pin 17 (Weakness question) in Canva. Upload + schedule for May 20 7am ET.
- [ ] Reply to support emails.

**Evening (~6pm ET, 20 min — LAUNCH discount post-mortem)**:
- [ ] If LAUNCH discount expired today (cap hit OR Tuesday timer): note final use count + total $29 sales attributable to discount. Compare to Email 4 click count. The conversion math here informs v1.1 launch discount strategy.
- [ ] Verify product listing now shows $39 (not $29) for new visitors. Test in incognito.
- [ ] Capture day's metrics. Note any unusual patterns.

**Success criteria**: LAUNCH discount cleanly off (or capped). Listing shows $39. Pin 17 scheduled.

---

### Wed May 20 — first quiet day

**Time budget**: ~40 min.

**Morning (~9am ET, 15 min)**:
- [ ] Pin 17 goes live — verify posted.
- [ ] Process support emails.
- [ ] Capture sales (cumulative day 3).

**Afternoon (~1pm ET, 10 min)**:
- [ ] Optional repin: pick best-performing pin from May 4–17 ramp, repin to AI Prompts for Job Seekers board.
- [ ] Reply to support emails.

**Evening (~6pm ET, 15 min)**:
- [ ] Capture metrics.
- [ ] First refund-rate check: if refund rate >5% by day 3, that's an early warning. Read the refund log; look for repeated language.

**Success criteria**: refund rate <5%. Two pins live this week (Pin 16 + 17).

---

### Thu May 21 — production day

**Time budget**: ~40 min.

**Morning (~9am ET, 15 min)**:
- [ ] Process support emails.
- [ ] Capture sales (day 4).

**Afternoon (~1pm ET, 15 min)**:
- [ ] Build Pin 19 (100 applications, forest color) in Canva. Upload + schedule for May 22 7am ET.
- [ ] Reply to support emails.

**Evening (~6pm ET, 10 min)**:
- [ ] Capture metrics.
- [ ] Optional: if total sales <5 by EOD May 21, flag for Sunday's YouTube gate decision (ahead of full May 24 check).

**Success criteria**: Pin 19 scheduled. Inbox clear.

---

### Fri May 22 — Pin 19 live + halfway-week metric check

**Time budget**: ~45 min.

**Morning (~9am ET, 15 min)**:
- [ ] Pin 19 goes live — verify posted.
- [ ] Process support emails.
- [ ] Capture sales (day 5).

**Afternoon (~1pm ET, 10 min)**:
- [ ] Optional repin from May 4–17 ramp.
- [ ] Reply to support emails.

**Evening (~6pm ET, 20 min — halfway-week tally)**:
- [ ] 5-day post-launch tally. Capture in tracking spreadsheet AND in a 1-paragraph summary note: total sales, total refunds, refund rate, total Pinterest impressions, total support emails handled.
- [ ] Compare to gate-check thresholds (5 sales / 1K Pinterest impressions). If ahead of pace, low-stress weekend ahead. If behind, the weekend's Pinterest cadence becomes more important.

**Success criteria**: 5-day summary captured. Halfway-pace assessment noted.

---

### Sat May 23 — production day + light ops

**Time budget**: ~30 min (weekend cadence; less rigorous).

**Morning (~10am ET, 10 min — weekend slack)**:
- [ ] Process any support emails.
- [ ] Capture overnight sales.

**Afternoon (~2pm ET, 15 min)**:
- [ ] Build Pin 20 (Recruiter ghost) in Canva. Upload + schedule for May 24 7am ET.

**Evening (~6pm ET, 5 min)**:
- [ ] Quick metrics capture. Don't overthink it on a Saturday.

**Success criteria**: Pin 20 scheduled.

---

### Sun May 24 — gate check + next-broadcast decision

**Time budget**: ~75 min (the heaviest day of the week — week-1 wrap-up).

**Morning (~10am ET, 15 min)**:
- [ ] Pin 20 goes live — verify posted.
- [ ] Process support emails.
- [ ] Capture overnight sales.

**Midday (~1pm ET, 30 min — gate check + week 1 retrospective)**:

The two gate-check thresholds Tom set:
1. **5+ sales since launch?** Track Gumroad → Sales count.
2. **1,000+ Pinterest impressions?** Track Pinterest → Analytics → Overview, all time post-May-17.

Decision matrix:

| Sales | Pinterest impressions | Decision |
|---|---|---|
| ≥5 | ≥1,000 | **Start YouTube planning Q2 now**. The bundle has product-market signal AND traffic signal. Use the next 6 weeks to outline + script + record the first 3 videos before the June 15 forced trigger. |
| ≥5 | <1,000 | **Wait for June 15 trigger**. Bundle has buyer signal but Pinterest reach hasn't compounded yet. Give it 3 more weeks; if Pinterest crosses 1K by then, go. |
| <5 | ≥1,000 | **Wait for June 15 trigger + investigate funnel**. Pinterest is driving traffic but the listing isn't converting. Pre-June-15 work: read the refund log, audit the listing, talk to anyone who almost-bought. |
| <5 | <1,000 | **Wait for June 15 trigger; reduce expectations for v1**. The bundle may be a slow-burn. YouTube planning anyway makes sense as a lead-gen channel, but starts later (post-June-15) with adjusted ambition. |

- [ ] Pull both numbers, run the matrix, note the decision in the tracking spreadsheet's notes column.
- [ ] If decision is "start YouTube planning Q2 now": create a 3-line note in `product/launch/v1.1-backlog.md` (or a new `product/post-launch-roadmap.md`) capturing the trigger condition that fired and the 6-week plan window.

**Afternoon (~3pm ET, 15 min — refund-log read)**:
- [ ] Read every entry in `product/launch/refund-log-2026-05.md`. Cluster by reason. Note any pattern (3+ same complaint = v1.1 must-fix flag).
- [ ] Add findings to `product/launch/v1.1-backlog.md` if the file exists, or create it from the v1.1 backlog template.

**Evening (~6pm ET, 15 min — next-broadcast decision)**:
- [ ] Run the ConvertKit option-1/2/3 logic above.
- [ ] If sending an email this week, draft now (or queue for May 25 morning).
- [ ] Capture final week 1 metrics summary in tracking spreadsheet AND in a 1-paragraph note in the day's row.

**Success criteria**: gate check decided. Refund log read + clustered. Next-broadcast decision made.

---

## What week 1 deliberately does NOT include

- **Active Pinterest community engagement** (commenting on others' pins, repinning others' content). Optional flywheel work; scope creep for week 1.
- **YouTube content production**. Even if the gate fires "start now", May 18–24 is monitoring + planning prep. No filming.
- **Soliciting testimonials**. Buyers are 0–7 days into the bundle; testimonials need 14+ days of usage to be honest. Wait until week 3.
- **Pricing experiments**. $39 fixed for the foreseeable future.
- **Paid Pinterest ads**. v1 is organic only. Paid is a v1.1 question.

---

## End-of-week-1 deliverables (May 25 morning, before any week-2 work)

A clean week-1 report consists of:

1. **`tracking/daily-metrics-template.csv`** — all 7 days populated (May 18–24)
2. **`product/launch/refund-log-2026-05.md`** — every refund logged with reason
3. **A 1-paragraph week-1 summary** in `product/launch/post-launch-week-1-plan.md` (this file) at the bottom — total sales, refund rate, Pinterest impressions, key qualitative notes, gate-check decision
4. **`product/launch/v1.1-backlog.md`** — updated with any week-1 findings (refund patterns, support-email patterns, gaps in DELIVERY_EMAIL.md or onboarding flow that buyers hit)

If any of those four are missing or stale on May 25 morning, week 2 work waits until they're complete. The data captured in week 1 is the input that makes weeks 2+ smarter.

---

## Append below — Week 1 summary (fill in May 24 evening)

> **TBD — fill in May 24 evening after the gate check. Format**: 1 paragraph, ~5 sentences. Total sales, refund rate, Pinterest impressions, gate-check decision, single most surprising thing that happened week 1.
