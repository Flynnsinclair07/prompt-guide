# HANDOFF — Wednesday June 3, 2026 (evening)

Paste this at the start of the next session. Picks up where tonight left off.

## WHO YOU ARE

Tom — direct, no fluff, no sycophancy. Treat Flynn as a capable 19-year-old founder. One sentence beats three. Push back when he's wrong, with reasoning. Never commit/push to git without Flynn's OK (his pattern is "yes" to every push but always confirm). Never skip git hooks. No emojis unless asked. No exclamation points. Lowercase "hey" opener for personal messaging.

Banned phrases: exclusive, amazing, game-changing, incredible, unleash, results-driven, dynamic, thrive in, proven track record, passionate about, leverage (as a verb), level up, unlock your potential.

Flynn's IH/Reddit voice: all-lowercase opening sentences, fragment-heavy, no capital "i" → "i", no exclamation points, proper nouns still capitalized.

## WHO FLYNN IS

19, Colorado (Mountain Time — convert all times to MT). First AI business. CU Boulder freshman starting fall 2026. Reading-comprehension difficulty → always give numbered step-by-step + direct URLs when he acts in any dashboard. Work schedule: Wed + Thu 11 AM-4 PM, Sun 4-9 PM. ADHD meds affect sleep — sometimes works late.

Side context: he was sick the week before launch; voice has recovered. Hanging out with friends some weeknights. Doesn't wake before 9 AM most days unless there's a specific reason.

## THE BIG MOMENT THIS WEEK

**Friday June 5, 8 AM MT — Show HN.**

That's the one launch we have left this week. All prep is done:
- `product/launch/show-hn-post.md` — title + body + URL field, ready to copy-paste into https://news.ycombinator.com/submit
- `product/launch/show-hn-replies-pre-drafted.md` — 3 pre-drafted replies for the most likely first comments + bonus replies for less likely ones

Flynn must be IN the comment thread for the first 2 hours after posting. Friday morning is his only window without work conflict.

## SITE STATE — what's live now

- **snipprompts.com** — 230 pages
  - 182 prompt pages (`prompts/`)
  - 8 long-form articles (`articles/`)
  - 8 vertical landing pages (`/for-*.html`)
  - 5 with-tool landing pages (`/with-*.html`)
  - 5 bundle module landing pages (`/bundle-*.html`)
  - 3 competitor comparison pages (`/snipprompts-vs-*.html`)
  - FAQ, Resources, About, Press, Privacy, Terms, Affiliate Disclosure, Changelog, 404, Newsletter
  - Homepage routing tiles (added 2026-05-27)
- **Bundle live on Gumroad** — `snipprompts.gumroad.com/l/job-hunters-ai-bundle`, $39, 30-day refund
- **Domain** — Porkbun, auto-renew on, expires 2027-04-20

## TRAFFIC + REVENUE STATE (as of June 3 evening)

- **GA4:** 81 active users in last 7 days (May 25-31), up 1,520% vs prior week. Spike on May 27 (PH launch day) hit ~45 users. 1 key event = 1 bundle_click recorded. Decay to baseline (~10/day) by May 30-31.
- **Gumroad sales:** 0
- **Kit subscribers:** unconfirmed (Kit welcome sequence not verified yet — TODO)
- **Search Console:** 134 pages "Discovered - currently not indexed," 1 page indexed. 6 URLs manually requested for indexing on 2026-06-02 + 4 more URLs requested 2026-06-03. Sitemap resubmitted 2026-06-02 (was last read Apr 20).

## ACTIVE CAMPAIGNS

### Career-center outreach — 54 emails sent across 3 batches
- **Batch 1 (21 schools):** sent 2026-05-21. 3 auto-replies confirmed.
- **Batch 2 Group A (7 schools):** sent 2026-05-23. AI-overlap heavy hooks.
- **Batch 2 Group B (11 schools):** sent 2026-05-28. **1 real reply: Sarah Heath at UVM.** She said "I'll check it out" + liked Flynn's follow-up. Door open, no commitment yet.
- **Batch 3 (15 schools):** sent 2026-06-02. Zero bounces so far. Reply window: 3-14 days from send.
- **Deferred:** Drake (no director), UNI (no current director), UNC-Greeley (needs phone-verify).
- **Tracker file:** `product/launch/career-centers-tracker.md`
- **Bounce-fallbacks:** `product/launch/career-centers-bounce-fallbacks.md`

### Pinterest — Batch 2 scheduling COMPLETE
- Scheduled tonight (2026-06-03): 13 of 14 pins for June 7-July 1, all 9 PM MT.
- Pin 14 (tax-prep, July 3) needs to be scheduled June 5-6 when window rolls.
- Pins 35-40 (mid-batch-2 remainder) need to be scheduled mid-June.
- Pins 41-60 (batch 3) start publishing July 17 — need to be scheduled mid-July.
- **Files:** `pins/PINS-BATCH-2.md`, `pins/PINS-BATCH-3.md`, PNGs in `pins/`

### Show HN — Friday June 5, 8 AM MT
- Updated copy in `product/launch/show-hn-post.md` (182 prompts, 74-char title, expanded categories, 8 guides)
- 3 pre-drafted comment replies in `show-hn-replies-pre-drafted.md`
- Flynn must be in thread 8-10 AM MT minimum

### YouTube — channel setup pending
- Plan: `product/launch/youtube-plan-2026-06.md` (voice-only screen recording + faceless slideshow, no on-camera face)
- First script ready: `product/launch/youtube-script-01-resume-screen-recording.md` (10 min, "ChatGPT for resumes without inventing experience")
- Target first upload: Sunday June 14, 7 PM MT
- Voice has recovered — recording is unblocked
- Channel + first video unrecorded as of 2026-06-03

### Indie Hackers — 1 post live
- URL: https://www.indiehackers.com/post/launched-on-product-hunt-yesterday-2-upvotes-0-sales-what-the-data-actually-said-259e99ca68
- Thread settled — 1 substantive commenter (Aryan, who turned out to be pitching beryxa.com domain). Flynn replied twice, polite decline. Beryxa.com confirmed on Atom.com at $4,399 — Aryan was the seller.
- No new comments since.

### Twitter/X — NOT SET UP
- 10 threads pre-drafted in `product/launch/twitter-threads-10-launch-week.md`
- Screen Time on Flynn's phone blocks the X app — try Safari private window or Chrome on Mac

### Amazon Associates — NEW account active as of 2026-06-03
- Store ID: **`promptguide0a-20`** (Amazon assigned, `promptguide-20` was taken by a different account)
- Mass-replaced 258 instances of `promptguide-20` → `promptguide0a-20` across HTML + Python files
- W-9 validated (US citizen, 0% withholding)
- Payment method: Gift card ($10 threshold, faster payout than $100 check minimum)
- 180-day rule active: needs 3 qualifying sales by ~late November or account closes

### Newsletter (Kit) — welcome sequence NOT verified
- Welcome sequence: 3 emails, supposed to fire on signup
- Flynn never tested by subscribing himself with a different email
- TODO: subscribe `snipprompts.team@gmail.com` to the Kit list, confirm welcome arrives

## WHAT GOT DONE TONIGHT (Wed June 3 evening)

1. Pinterest batch 2 scheduling — 13 pins scheduled (June 7 → July 1)
2. Amazon Associates signup complete (W-9, gift card payout, tag promptguide0a-20)
3. 258 affiliate links updated across site, committed + pushed
4. 4 more Search Console URL indexing requests (interview prep, salary, resume article, resources)
5. Domain auto-renew confirmed (Porkbun, 2027-04-20)
6. Gumroad profile bio updated, logo uploaded
7. Business Gmail created: `snipprompts.team@gmail.com`
8. 5 dashboards bookmarked (GA4, Kit, Gumroad, Search Console, IH, PH)
9. Gumroad affiliate program — stayed in (other Gumroad creators can promote bundle for 10% commission)

## TOMORROW (Thursday June 4)

- Work 11-4 (no SnipPrompts requirements during)
- Optional evening: Verify Kit welcome sequence + LinkedIn company page setup + 1-2 Reddit comments
- Watch inbox for career-center replies (batch 3 reply window opens around now)
- Show HN prep — re-read replies file before bed

## FRIDAY (June 5) — SHOW HN DAY

1. Wake 7 AM MT (alarm)
2. Coffee + open `show-hn-post.md` and `show-hn-replies-pre-drafted.md`
3. 8:00 AM MT — submit at https://news.ycombinator.com/submit
   - Title: `Show HN: SnipPrompts – 182 ChatGPT prompts engineered to not sound like AI`
   - URL: `https://snipprompts.com`
   - Body: paste from show-hn-post.md
4. 8:00-12:00 MT — sit on thread, reply to comments within 5 min each
5. PM — schedule pin-37-tax-prep.png for July 3 (Pinterest window has rolled forward)
6. Late afternoon — assess Show HN outcome

## NEXT 7 DAYS — daily routine

Per `product/launch/daily-distribution-routine.md`:
- 15 min inbox triage (career-center replies, bounces)
- 20 min community presence (Reddit or IH or HN, ONE channel)
- 20 min original content (2-3 days/week — IH post, LinkedIn, Twitter thread, newsletter)
- 5 min buffer (Pinterest scheduling as window rolls, notes)

## KEY DOCS IN `product/launch/`

- **`master-todo-2026-06-03.md`** — 6-month roadmap, all channels, time-based plan
- **`daily-distribution-routine.md`** — 60-min/day framework for next 90 days
- **`HANDOFF-2026-06-03-evening.md`** — THIS DOC
- `show-hn-post.md`, `show-hn-replies-pre-drafted.md` — Friday's launch
- `career-centers-tracker.md`, `career-centers-bounce-fallbacks.md` — outreach campaign
- `career-centers-batch-3-emails-2026-06-02.md` — most recent send
- `youtube-plan-2026-06.md`, `youtube-script-01-resume-screen-recording.md` — YouTube prep
- `twitter-threads-10-launch-week.md` — Twitter threads waiting for account
- `pinterest-variants-to-test-2026-07-19.md` — future pin variants test
- `daily-distribution-routine.md` — daily 60-min framework
- `pins/PINS-BATCH-2.md`, `pins/PINS-BATCH-3.md` — Pinterest copy
- `email-course-5-day.md` — 5-email course to deploy to Kit
- `newsletter-issues-2-3-4.md` — drafts for next 3 newsletters
- `email-sequences-cart-and-reengagement.md` — abandoned cart + Kit re-engagement
- `testimonial-drip-emails.md` — fires when first buyer exists (Day 7/14/30)
- `june-15-youtube-gate.md` — June 15 decision framework
- `indie-hackers-post.md` — original IH post template (now stale)
- `ih-post-2026-05-28-postmortem.md` — what's currently live on IH

## REVENUE TIMELINE — honest base case

- **First $1** (affiliate trickle from Resources page Amazon links): late June - early July
- **First bundle sale** ($35 net): August likely, July if anything pops
- **First $100/month**: October-November
- **First $500/month**: January-March 2027

## STILL ON DECK (no specific date)

- 🟢 Verify Kit welcome sequence (5 min — should be tonight or tomorrow)
- 🟢 LinkedIn company page setup (10 min)
- 🟢 Twitter/X account setup (need to bypass Screen Time)
- 🟢 ElevenLabs voice clone setup (TikTok semi-automation prep)
- 🟢 YouTube channel setup + first video record
- 🟢 Reddit — 3-5 substantive comments in r/cscareerquestions (deferred from May 28)
- 🟢 IH milestone post when first sale lands
- 🔧 API setups for morning briefing: Search Console → Gumroad → Kit → GA4 → iCloud IMAP

## CALENDAR / TIME-LOCKED ITEMS

| Date | Item |
|---|---|
| Fri Jun 5 | Show HN at 8 AM MT |
| Fri Jun 5 PM | Schedule remaining Pinterest pin |
| Fri Jun 5 PM | Weekly review per daily routine |
| Jun 7 | Pinterest batch 2 starts publishing (pin 21, 9 PM MT) |
| Jun 14 | YouTube video 1 target upload (Sun 7 PM MT) |
| Jun 15 | YouTube gate decision |
| Mid-Jun | Schedule remaining batch 2 pins (35-40) |
| Mid-Jul | Schedule batch 3 pins (41-60) |
| Jul 17 | Pinterest batch 3 starts |
| Jul 19 | Pinterest variants test session |
| Aug 1 | 60-day metrics review |
| Sep 14 | YouTube 90-day evaluation |

## WORKING NORMS

- **Git:** commits with `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`. Never `--no-verify`. Never amend. Never destructive without explicit OK. Confirm pushes when in doubt.
- **Bulk edits:** use Python heredoc via `python3 <<'PYEOF' ... PYEOF`. Edit tool errors with "file modified since read" because a linter touches files between Read and Edit. Python sidesteps this.
- **Reading-comprehension accommodation:** when Flynn acts in any dashboard, give NUMBERED step-by-step + direct URLs. Never vague "go to settings."
- **Mountain Time always** — Flynn is in Colorado.
- **Honesty:** if a vendor email is a scam (Talon, ReleaseLog, Viberank, Beryxa rebrand pitch), say so directly. Don't soften.
- **Brand integrity:** SnipPrompts is anti-AI-tell. Don't suggest AI voice or AI avatars for the channel. Voice cloning of Flynn's own voice for TikTok is the line we agreed on.

## RECENT MISTAKES TO AVOID

- The May 28 batch-2 "Tuesday June 2" send was almost a disaster — those emails were already sent Thursday May 28. Always check the tracker before sending.
- Old `promptguide-20` Amazon tag was going to someone else's account for weeks. Always verify external account setup is complete before relying on tracking.
- Pinterest scheduler window is ~28 days, not 30. Schedule what fits, queue the rest.

## OPEN BLOCKERS

- **Twitter/X:** Screen Time blocks the app. Workaround needed (Safari private window or Chrome on Mac).
- **TikTok:** decided semi-automated path (voice clone + CapCut + scheduler) but not built.
- **Morning briefing:** schedule skill broken on Anthropic's side. Manual trigger ("run morning briefing") works as fallback.
- **API setups for briefing:** none done yet. Lowest priority — fine to delay.

## ONE-LINE STATE SUMMARY

54 outreach emails out, 1 real reply (UVM open door), 0 sales, 81 users / week, 13 Pinterest pins scheduled, Show HN in 36 hours, Amazon Associates active, voice recovered, YouTube ready to record, everything pushed to GitHub.
