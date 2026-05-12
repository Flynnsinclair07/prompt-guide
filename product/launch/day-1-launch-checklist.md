# Day-1 launch checklist — May 17, 2026 (Sun)

Operational timeline for launch day. Time-stamped, paste-into-tabs ready, no buyer-facing copy.

Every item has four parts: **what** to do, **where** to do it (URL or app), **success** (how you know it worked), **fail-recovery** (what to do if it didn't).

All times are **ET** unless noted. Owner is in MDT (UTC−6); add 2 hours for ET.

**Buyer-tagging is manual, not automated.** Kit free tier blocks Gumroad app integration. On Monday May 18 ~3 PM MT, export Gumroad sales CSV and bulk-add `bundle-buyer-2026-may` tag in Kit before publishing Email 5.

> Print this page or pin it as a Notion page in your workspace. Don't try to navigate it on a phone during the launch window.

---

## Pre-launch — Saturday May 16 evening (8–10pm ET / 6–8pm MDT)

### 1. Final pre-flight check on Gumroad listing
- **What**: open the draft Gumroad listing, verify each field against current state — title `The Job Hunter's AI Bundle`, price $39, refund 30-day no questions, files (`job-hunters-bundle.pdf` 119 pages + `job-hunters-bundle-notion-link.txt`), discount code `LAUNCH` configured but toggled OFF, Notion duplication URL `https://learned-guilty-545.notion.site/The-Job-Hunter-s-AI-Bundle-35634cf5abb9800babe5c22b28888ccf` resolves.
- **Where**: gumroad.com → Products → Job Hunter's AI Bundle (draft) → Edit
- **Success**: every field matches; no `[NOTION_DUPLICATION_URL]` or other placeholder text survives anywhere.
- **Fail-recovery**: any placeholder still present → fix it now, not at 8:55am tomorrow.

### 1.5. Verify Vladyslav deliverables are uploaded to Gumroad
- **What**: horizontal 1280×720 bundle cover image uploaded, square 600×600 thumbnail uploaded, 60-second demo video uploaded as preview image (if recorded), 3 PDF page screenshot previews still present. Verify all 20 Pinterest pins from his batch are uploaded to the AI Prompts for Job Seekers board with proper descriptions and destination URLs from `PINTEREST_PINS.md`.
- **Where**: Gumroad → Products → Job Hunter's AI Bundle → Edit (cover/thumbnail/preview); Pinterest → AI Prompts for Job Seekers board.
- **Success**: all assets present on Gumroad; all 20 pins live on Pinterest with correct descriptions + URLs.
- **Fail-recovery**: missing asset → upload now from Vladyslav's delivery folder. Pin description wrong → edit inline on Pinterest.

### 2. Verify the discount code is created (but OFF)
- **What**: confirm `LAUNCH` discount code exists, $10 off, 100 use cap OR May 19 9 AM ET (= May 19 6 AM PDT in Gumroad's timezone) expiration, currently **toggled OFF**.
- **Where**: Gumroad → Discounts → LAUNCH
- **Success**: code shows in list, status = inactive/disabled.
- **Fail-recovery**: doesn't exist → create it now ($10 off, 100 use cap or May 19 9 AM ET expiration). Already active → toggle OFF (you don't want early discount leaks before public launch).

### 3. Verify ConvertKit Email 4 is queued with real Gumroad URL
- **What**: open the Email 4 broadcast, confirm body has the live Gumroad URL with `/LAUNCH` appended (auto-applies discount). No `[GUMROAD_URL]` placeholder remaining.
- **Where**: ConvertKit → Broadcasts → Email 4 (May 17, 9am ET) → Preview
- **Success**: live URL present, looks clickable, segment correctly excludes `bundle-buyer-2026-may`.
- **Fail-recovery**: placeholder still present → replace with `https://snipprompts.gumroad.com/l/job-hunters-ai-bundle/LAUNCH` (or your actual storefront subdomain — verify in Gumroad if unsure). Test the URL in incognito.

### 4. Verify Notion duplication URL still works
- **What**: open the live Notion duplication URL in an incognito window. Confirm the workspace renders, "Duplicate" button is visible top-right, all 7 pages load.
- **Where**: incognito browser → paste URL from `DELIVERY_EMAIL.md` line 58
- **Success**: workspace loads, Duplicate button works (test by clicking → cancel before duplicating to prevent your account creating extra copies).
- **Fail-recovery**: 404 → re-create the duplication share link in Notion (Share → Publish → "Allow duplicate as template" → copy URL). Update `DELIVERY_EMAIL.md` and `support-templates.md` line 30. Stale link is the worst possible buyer-experience bug.

### 5. Sleep
- **What**: bed by 10pm ET (8pm MDT). 7+ hours.
- **Where**: literally bed.
- **Success**: you wake up before 8am ET (6am MDT) refreshed.
- **Fail-recovery**: if you can't sleep, don't start fixing things. Sleep deprivation tomorrow is more expensive than any unfixed item tonight. Anything broken is also broken at 8am — fix then.

---

## Launch morning — 6am–9am ET (4am–7am MDT)

### 6. Wake-up + caffeine (6am ET / 4am MDT)
- **What**: wake up, coffee/tea, eat something. Open laptop on desk (not couch).
- **Where**: kitchen → desk.
- **Success**: you're awake, hydrated, sitting at your desk with two screens (or one + phone) by 6:30am ET.
- **Fail-recovery**: overslept past 7am ET → no panic, you have 2 hours. Skip workout/walk, prioritize the checklist.

### 7. Re-verify all 4 pre-flight items from last night (6:30–7am ET)
- **What**: same checks as Pre-launch items 1–4, fresh-eye pass.
- **Where**: same URLs/apps.
- **Success**: nothing changed overnight, all 4 items still green.
- **Fail-recovery**: anything changed (Gumroad pushed an update, ConvertKit broadcast got unscheduled, Notion link broke) → fix immediately.

### 8. Open all the tabs you'll need at 9am (7–7:30am ET)
Pre-load tabs in a dedicated browser window so you're not searching for URLs at 9:00:00.
- **Tabs**:
  - Gumroad → Products → Job Hunter's AI Bundle (draft, ready to publish)
  - Gumroad → Discounts → LAUNCH (ready to toggle on)
  - Gumroad → Sales (will populate after launch)
  - ConvertKit → Broadcasts → Email 4 (verify scheduled)
  - ConvertKit → Subscribers (watch for buyer-tag fires)
  - Pinterest → AI Prompts for Job Seekers board (ready to upload launch-day pin)
  - Pinterest → Analytics → Overview
  - Inbox tab (Gmail/whatever) on `bundle-buyer-2026-may` filter, plus general inbox
  - `product/launch/support-templates.md` open in your editor
  - `product/launch/sprint-plan-may-4-17.md` if you want context on prior days

### 9. Test purchase flow with $0 discount (7:30–8am ET)
- **What**: use a Gumroad 100% test discount code on yourself (you may have created one for May 14 walkthrough — if so, re-use; otherwise create a fresh `TEST100` code, 100% off, 1 use). Buy the bundle. Verify receipt email lands, both files (PDF + Notion link) download cleanly. NOTE: ConvertKit buyer-tag automation is not wired (Kit free tier blocks the integration) — manual tagging happens Monday May 18 via Gumroad CSV export, see new section 26.
- **Where**: Gumroad listing URL (still draft — accessible to you logged in even if not published) → checkout with test code.
- **Success**: receipt email lands in your inbox, both files download cleanly.
- **Fail-recovery**: receipt email doesn't arrive → check Gumroad → Workflows → Receipt email is enabled. Files don't download → check Field 8 file uploads.
- **Then**: refund the test purchase via Gumroad → Sales → Refund. Disable the `TEST100` code so it can't be reused.

### 10. Post launch-day pin to Pinterest (8–8:30am ET) — schedule ahead, don't post live
- **What**: schedule (NOT publish-now) the launch-day pin from Vladyslav's batch — the navy pin titled 'LIVE NOW / $29 LAUNCH WEEK ONLY' (Pin 10 in his delivery, was Pin 15 in old PINTEREST_PINS.md numbering) — to post at 9:01am ET. Pinterest's scheduler is reliable; scheduling avoids the risk of a 9:00am-sharp scramble.
- **Where**: Pinterest → AI Prompts for Job Seekers board → "Create Pin" → Schedule.
- **Success**: pin shows in scheduled-pins queue, scheduled time = 9:01am ET, link points to live Gumroad URL with `/LAUNCH`.
- **Fail-recovery**: scheduling broken → set a phone alarm for 9:01am, post manually then.

### 11. Brief inbox + Twitter/LinkedIn check (8:30–8:55am ET)
- **What**: 5-min scan of inbox, mute any non-launch threads, set Slack/Discord/Teams to DND.
- **Where**: inbox + comm apps.
- **Success**: no surprises, nothing competing for your attention 9:00–10:00.
- **Fail-recovery**: critical email (boss/family) → handle quickly, then back to launch.

### 12. T-minus-5 — final breath (8:55am ET)
- **What**: stand up, stretch, drink water. Sit back down at 8:58.
- **Where**: desk.
- **Success**: heart rate normal, hands not shaking.
- **Fail-recovery**: nervous? → deep breaths. The plan is fine. The discount is real. The bundle works. You've walked every step twice.

---

## 9:00am ET — PUBLISH

The actual launch moment. Execute in this exact order. **~3 minutes total.**

### 13. 9:00:00 — Toggle Gumroad listing → Published
- **What**: click Publish on the Gumroad listing.
- **Where**: Gumroad → Products → Job Hunter's AI Bundle → Publish button.
- **Success**: listing status changes to "Published", public URL becomes live.
- **Fail-recovery**: button errors → refresh, retry. Persistent error → contact Gumroad support (they're slow on Sundays — escalate via Twitter @gumroad if needed).

### 14. 9:00:30 — Toggle LAUNCH discount → Active
- **What**: enable the LAUNCH discount code.
- **Where**: Gumroad → Discounts → LAUNCH → toggle to active.
- **Success**: discount code shows as active. Test in incognito: visit `[live-url]/LAUNCH` — price shows $29.
- **Fail-recovery**: discount won't activate → re-create it from scratch (Gumroad sometimes silently breaks discount codes; faster to re-create than debug). Update Email 4 + launch-day pin if URL changed.

### 15. 9:01:00 — Verify Email 4 sent + launch-day pin published
- **What**: check ConvertKit broadcast status (should show "sent" within 60 seconds of 9:00). Check Pinterest scheduled pins (launch-day pin should have moved from scheduled to live).
- **Where**: ConvertKit → Broadcasts → Email 4 (status). Pinterest → AI Prompts for Job Seekers board (launch-day pin visible).
- **Success**: both showing "sent/live".
- **Fail-recovery**: Email 4 didn't send → trigger manually via "Send now". Launch-day pin didn't post → upload manually now.

### 16. 9:02:00 — Tag Gumroad listing for SEO/discovery
- **What**: add tags + category to the listing. Tags: `chatgpt, ai prompts, job search, resume, cover letter, interview prep, linkedin, salary negotiation, career, career change`. Primary category: Self Improvement → Career.
- **Where**: Gumroad → Products → Job Hunter's AI Bundle → Edit → Tags + Category.
- **Success**: listing shows up under those Gumroad category browse pages within ~10 minutes.
- **Fail-recovery**: tag limit hit → drop low-priority ones (`career change`, `linkedin` are first to cut; keep `chatgpt`, `salary negotiation`, `resume`, `ai prompts`, `career`).

---

## 9:00–10:00am ET — opening hour

### 17. Watch for the first sale (9:00–9:30am ET)
- **What**: keep Gumroad → Sales tab open. The first sale typically lands within 15 minutes of Email 4 hitting inboxes.
- **Where**: Gumroad → Sales (auto-refreshes).
- **Success**: first sale visible in Gumroad.
- **Fail-recovery**: no sale by 9:30 → not necessarily a problem. Sunday-morning audiences read at different times. Worry threshold: nothing by 11am.

### 18. Reply triage (rolling, every 10 min)
- **What**: open the inbox. Reply to anything that comes in using `product/launch/support-templates.md`. Don't write fresh replies — the templates exist for exactly this moment.
- **Where**: inbox + `support-templates.md`.
- **Success**: every reply goes out within 30 minutes of receipt during the launch window.
- **Fail-recovery**: high volume → batch in 15-min cycles, not real-time. Quality over speed.

### 19. Check Pinterest impressions on launch-day pin (9:30am ET)
- **What**: scan the launch-day pin stats — early impressions / saves / outbound clicks.
- **Where**: Pinterest → Analytics → launch-day pin.
- **Success**: at least some impressions registering by 9:30 (the launch board has a small audience but it'll show some movement).
- **Fail-recovery**: zero impressions after 30 min → re-share the pin or post a duplicate. Pinterest sometimes shadowbans new pins for the first 24h on small boards.

---

## 10:00am–12:00pm ET — monitoring

### 20. Sales dashboard check-in (every 30 min)
- **What**: count sales, count refunds, count outliers (price-mismatch errors, etc.).
- **Where**: Gumroad → Sales.
- **Success**: sales accumulating at a non-zero rate. Refund count = 0 (refunds happen mostly day 2–14, not hour 1).
- **Fail-recovery**: sales rate stalls → don't change anything live, but note the time of stall for end-of-day debrief. Check if Email 4 has unusual bounce rate (ConvertKit → Email 4 → stats).

### 21. ConvertKit click-rate check (10:30am ET)
- **What**: open Email 4 stats — open rate, click-through rate, unsubscribe rate.
- **Where**: ConvertKit → Broadcasts → Email 4 → Stats.
- **Success**: open rate >35% (your list opens at high rates because it's an opt-in list). Click rate >8%. Unsubscribes <2%.
- **Fail-recovery**: open rate <25% → likely deliverability hit (subject spam-flagged, or sent during low-engagement window). Note and adjust Email 5 (May 18 reminder) timing if it goes out.

### 22. Inbox monitoring (rolling)
- Same as item 18. Reply with templates.

---

## 12:00pm ET check-in

### 23. Lunch + sales tally
- **What**: take a real lunch break (30 min). Then snapshot: sales count, refund count, ConvertKit open/click rates, Pinterest impressions. Note in a single message to yourself.
- **Where**: real food, then desk.
- **Success**: you ate. Tally captured.
- **Fail-recovery**: skipping lunch is the failure-recovery for "nothing else", not the default. Eat.

### 24. Check the LAUNCH discount cap
- **What**: Gumroad → Discounts → LAUNCH → uses count. The discount caps at 100 uses; if you're approaching cap, decide whether to (a) let it expire on cap or (b) extend cap to 150/200/etc.
- **Where**: Gumroad → Discounts → LAUNCH.
- **Success**: under cap. Plenty of headroom for afternoon + Monday.
- **Fail-recovery**: at or near cap by noon → that's a great problem. Don't extend impulsively; the scarcity drives Email 5 conversion. Let it cap naturally; future launches benefit from the precedent.

---

## 6:00pm ET check-in

### 25. End-of-day-ish tally
- **What**: snapshot sales, refunds, opens, clicks, Pinterest impressions, support emails handled. Note any surprising patterns (specific time of sale clusters, specific question repeated).
- **Where**: each platform's analytics.
- **Success**: numbers captured for the May 17 row of your tracking spreadsheet (`tracking/daily-metrics-template.csv`).
- **Fail-recovery**: tracking spreadsheet missing or broken → just note in any text file. Don't lose the data point because the tool isn't perfect.

### 26a. Manual buyer tagging (Monday May 18, ~3 PM MT, before Email 5 decision)
- **What**: Export sales from Gumroad → Sales → Filter by The Job Hunter's AI Bundle → Export CSV. Open the CSV, copy the email column. In Kit → Subscribers → Bulk add subscribers (or import CSV with tag column). Apply tag `bundle-buyer-2026-may` to every buyer email. This must happen BEFORE Email 5 publishes — Email 5's `pre-launch-subscribers` segment relies on this tag to exclude buyers manually (Kit can't auto-exclude tags at broadcast level). Time: 5-15 min depending on sale count.
- **Where**: Gumroad → Sales → Export CSV; Kit → Subscribers → Bulk add / Import.
- **Success**: every buyer email shows `bundle-buyer-2026-may` tag in Kit before Email 5 sends.
- **Fail-recovery**: CSV export fails → pull buyer emails manually from Gumroad Sales view. Kit bulk-add errors → import via CSV with a tag column instead.

### 26. Decide on Email 5 (24h reminder, May 18 5pm ET)
- **What**: per `EMAIL_SEQUENCE.md` Email 5 conditions: only send if open rate on Email 4 >40% AND fewer than 50 sales by Monday 5pm ET. As of 6pm Sunday, eyeball whether you're tracking toward those conditions. If clearly above 50 sales already, plan to skip Email 5 (the reminder hurts more than it helps when the launch is going well).
- **Where**: ConvertKit → Broadcasts → Email 5 (currently draft).
- **Success**: decision made. Email 5 either queued for May 18 5pm or marked to-skip.
- **Fail-recovery**: undecided → wait until Monday morning, decide then.

---

## 12:00am ET / midnight check-in

### 27. Rest-of-launch-window verify
- **What**: quick scan that everything's still healthy. Listing live, discount active, no buyer crisis emails, no Pinterest pin pulled by spam-detect.
- **Where**: bed (yes, on phone — but only if you wake naturally). If you're already asleep, skip.
- **Success**: nothing on fire.
- **Fail-recovery**: anything actively broken → fix the one thing, then back to bed. Don't open the laptop.

---

## End-of-day metrics capture (Monday morning, before any new launch work)

### 28. Capture the May 17 numbers
- **What**: write down exactly:
  - Total sales count (Gumroad → Sales)
  - Total refund count (Gumroad → Refunds — usually 0 on day 1)
  - Email 4 open rate (ConvertKit → stats)
  - Email 4 click-through rate (ConvertKit → stats)
  - Email 4 unsubscribe count (ConvertKit → stats)
  - Pinterest impressions on launch-day pin (Pinterest → Analytics)
  - Pinterest outbound clicks on launch-day pin (Pinterest → Analytics)
  - Notion workspace duplications (Notion → Share → analytics, if available)
  - Support emails received + replied (rough count)
- **Where**: a single text file or row in `tracking/daily-metrics-template.csv`.
- **Success**: file exists, numbers in it, dated 2026-05-17.
- **Fail-recovery**: any platform's analytics not loading → note the partial data and the gap. You can re-pull next week if needed; what matters is the launch-day snapshot.

### 29. Capture the qualitative
- **What**: 3 sentences max. Best-thing, worst-thing, surprise. Add to the day's metrics file.
- **Where**: same file.
- **Success**: short paragraph captured. Future you in 6 months will reread this when planning the next launch.
- **Fail-recovery**: too tired to write 3 sentences → 1 sentence is fine. Don't skip entirely.

---

## What this checklist deliberately does NOT include

- **Social media engagement on the launch tweet/post**. Out of scope — there's no committed launch tweet/LinkedIn post. If you decide to post, slot for 9:05am ET after Pin 15 goes live.
- **Manually emailing specific contacts**. The bundle is opt-in via the email list. Don't DM people.
- **Pricing experiments mid-launch**. $39/$29 is locked.
- **Live Twitter/LinkedIn AMA or replies to Pinterest comments mid-launch**. Replying to Pinterest comments is fine but should be batched, not real-time.
- **Recording a launch retrospective video**. Worth doing for v1.1 launch; not for v1.

---

## If something major goes wrong

Three categories of major failure and the playbook for each:

### A. Gumroad listing won't publish
- Possible causes: payout setup not finished (Stripe), file upload limit hit, account in review.
- Recovery: contact Gumroad support, post on their Discord, escalate via Twitter. While that runs, post a "launching shortly, technical hiccup, link coming" update on the Pinterest pin description and reply to early support emails with the same.

### B. Email 4 fails to send
- Possible causes: ConvertKit deliverability issue, segment empty, payment hold.
- Recovery: send manually via "Send now". If still failing, send a short manual broadcast to the same segment with just the URL.

### C. Notion link broken
- Possible causes: workspace accidentally unpublished, share-link expired, Notion outage.
- Recovery: this is the most common day-1 failure mode and `support-templates.md` Template 2 covers it. If the link is genuinely broken (vs. just un-discoverable), re-publish the workspace, update the link in the receipt email going forward, and reply to anyone who already bought with the new link directly.

---

## After Day 1

This file is single-use. Don't try to re-purpose it for v1.1 launch — write a new one then, informed by what you learned today. Archive this file to `product/launch/archive/` after May 18 so it doesn't clutter the active launch directory.
