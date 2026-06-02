# Master TODO — SnipPrompts roadmap

**Created:** 2026-06-03 (the night before Show HN)
**Horizon:** next 6 months
**Status:** baseline state captured + everything we've discussed

## Legend

- 🟢 **Flynn's hands** — only you can do this (your accounts, your face/voice, your judgment)
- 🔵 **My hands** — I can build/draft/research without you (file work, web search, agents)
- 🟡 **Together** — you provide input or decision, I produce the artifact
- 🔧 **Setup work** — one-time setup that unlocks ongoing automation
- 📅 **Time-locked** — has a specific date
- ⏳ **Trigger-based** — fires when something else happens (first sale, list hits 20, etc.)

---

# THIS WEEK (June 3-7)

## 📅 Wed June 3 — Show HN day
- 🟢 9:00 AM MT — wake up
- 🟡 9:00-9:15 AM — run morning briefing (manual trigger by saying "morning briefing")
- 🟢 9:15-9:30 AM — coffee + skim briefing
- 🟢 9:30 AM MT — post Show HN at https://news.ycombinator.com/submit
- 🟢 9:30-11:30 AM — sit on HN thread, reply to comments within 5 min each (use `show-hn-replies-pre-drafted.md`)
- 🟢 Throughout day — check HN comments every hour after the 2-hour active window
- 🔵 End of day — I update tracker with HN outcome (upvotes, comments, traffic spike)

## 📅 Thu June 4 — Reddit start
- 🟢 9-10 AM MT — Reddit session in r/cscareerquestions (60-90 min)
  - Find 3-5 active threads about resumes/cover letters/interviews
  - Write substantive replies (link snipprompts URL only when it directly answers)
  - I draft replies if you paste the threads here
- 🟢 Inbox check — career-center bounces? replies? Log in tracker
- 🟢 Show HN gate-read — see Wed numbers, decide next steps

## 📅 Fri June 5 — Weekly review + Pinterest scheduling
- 🟢 9-10 AM MT — friday review (per `daily-distribution-routine.md`)
  - Visitors this week (GA4)
  - New subscribers (Kit)
  - Career-center replies (inbox)
  - HN/IH/Reddit engagement counts
  - One surprise + one change for next week
- 🟢 30 min — Pinterest scheduling — log into Pinterest, schedule pins 21-40 starting June 7 (1 every 2 days for the next 40 days, until July 17)
  - Files ready: `pins/PINS-BATCH-2.md` for copy
  - Pinterest's free scheduler caps at 30 days ahead — schedule what fits, queue the rest as the window rolls forward

## 📅 Sat-Sun June 6-7 — REST
- No site work. No inbox. No GA4. Recovery time.
- Exception: same-day reply if a career-center director or HN comment lands that needs response

---

# NEXT WEEK (June 8-14)

## 📅 Mon June 8 — Voice recovery check
- 🟢 Test your voice on a 60-sec recording. If clean → green light for YouTube video 1 + TikTok setup. If still rough → push another week.

## 🔧 LinkedIn company page setup (~10 min)
- 🟢 Create SnipPrompts company page (not personal account) at https://www.linkedin.com/company/setup/new/
- Bio: same brand voice + URL
- Logo: `pins/snipprompts-logo.png`
- Set yourself as Admin

## 🔧 Twitter/X account setup (~30 min)
- 🟢 Get past Screen Time block — either:
  - Disable Screen Time temporarily, OR
  - Use desktop browser instead of mobile (https://x.com/signup on Mac), OR
  - Use a friend's phone to do signup
- Handle: `@snipprompts` or `@snipprompts_com`
- Bio: from `youtube-plan-2026-06.md` template
- 🟢 Post Thread 1 (launch announcement) from `product/launch/twitter-threads-10-launch-week.md`
- Set posting cadence: 1 thread per week (Wednesdays)

## 🔧 ElevenLabs voice clone setup (~30 min — IF doing TikTok)
- 🟢 Sign up at https://elevenlabs.io (free trial)
- 🟢 Record 5-10 min of voice samples (read any of your articles aloud)
- 🟢 Train voice clone
- 🟢 Test by generating audio from a Twitter thread script
- 💰 If happy → subscribe to Starter ($5/mo)

## YouTube — record video 1
- 🟢 Channel setup (~30 min) per `youtube-plan-2026-06.md`
- 🟢 Record video 1 using `youtube-script-01-resume-screen-recording.md` (~60-90 min including redos)
- 🟢 Edit in iMovie (~30-60 min)
- 🟢 Upload, schedule for Sunday June 14, 7 PM MT

## TikTok — first 3 videos (IF doing semi-automated)
- 🔵 I draft 5 short scripts (30-60 sec each)
- 🟢 You paste each into ElevenLabs → generate audio
- 🟢 Drop into CapCut → auto-caption + B-roll → export
- 🟢 Schedule via TikTok native scheduler

## Career-center work
- 🟢 Daily 15-min inbox check (replies, bounces, auto-replies)
- 🟢 Reply to anyone who actually responds with substance — same day

## Morning briefing
- 🟡 Retry `/schedule` skill if Anthropic's service is back up
- If still broken — keep manual trigger by saying "morning briefing"
- 🔵 I refine the briefing prompt over the week based on what's actually useful

---

# WEEK OF JUNE 15

## 📅 June 14 (Sun) — YouTube video 1 goes live
- 🟢 Schedule upload by Sat eve so it publishes Sunday 7 PM MT
- 🟢 Reply to first comments within 24 hours

## 📅 June 15 — YouTube gate decision
- 🟡 Open `product/launch/june-15-youtube-gate.md` and review the gate criteria
- 🟢 Decision: continue weekly YouTube, OR pause, OR adjust format
- Default: continue if first video has any engagement (5+ views, 1+ comment)

## 📅 June 16-20 — Record YouTube video 2
- 🔵 I draft script (cover letter prompt walkthrough)
- 🟢 You record + edit + schedule for June 21 upload

## 🔧 API setups (when you have an hour)
Priority order (most useful first):

### 1. Google Search Console API — verify indexing growth
- 🟢 Go to https://search.google.com/search-console
- Settings → Users and permissions → confirm API access
- 🔵 I write a Python script that pulls indexed page count weekly into briefing
- Time: 30 min total

### 2. Gumroad API — sales count for briefing
- 🟢 https://gumroad.com/settings/advanced → generate API token
- 🟢 Paste token securely (we'll set up env var)
- 🔵 I write briefing integration
- Time: 20 min total

### 3. Kit (ConvertKit) API — subscriber count
- 🟢 https://app.kit.com/account_settings/advanced_settings → API key
- 🟢 Paste securely
- 🔵 I write briefing integration
- Time: 20 min total

### 4. GA4 API — traffic numbers
- 🟢 Google Cloud Console → enable Google Analytics Data API
- 🟢 Create service account, download JSON key
- 🟢 Add service account email as viewer in GA4
- 🔵 I write briefing integration
- Time: 60-90 min total — most complex setup. Worth doing once your traffic is interesting.

### 5. iCloud IMAP — email auto-scan for replies
- 🟢 Apple ID → Sign in & Security → App-Specific Passwords → generate one for "Briefing agent"
- 🔵 I write IMAP integration to scan unread career-center inbox replies
- Time: 30-45 min — also annoying but useful

### 6. TikTok API — scheduled posting (OPTIONAL)
- TikTok's official API is very restricted; most people use third-party schedulers
- Skip unless you really want it
- Alternative: TikTok's native scheduler (free, 10 days ahead) — no API needed

---

# REST OF JUNE (after June 20)

## Recurring weekly (every week, in priority order)
1. 🟢 Mon-Fri: 60-min daily distribution routine (`daily-distribution-routine.md`)
2. 🟢 Wed: post Twitter thread #2 (from `twitter-threads-10-launch-week.md`)
3. 🟢 Sat morning: schedule next Pinterest pins as the 30-day window rolls forward
4. 🟢 Sun 7 PM MT: YouTube video uploads
5. 🟢 Fri afternoon: weekly review (15 min)

## Once during late June (~2 hours total)
- 🟢 LinkedIn company page post #1 — a story about the launch + what didn't work
- 🟢 IH post #2 — a 30-day post-mortem update from the May 28 post
- 🔵 I draft both

## ⏳ Trigger-based (fires when X happens)
- **First bundle sale** → run testimonial collection (Day 7/14/30 drip) using `testimonial-drip-emails.md`
- **Email list hits 20 subscribers** → send subscriber survey ("what would you pay for next?")
- **IH account unlocks "Milestones" group** → post first-sale story when it happens
- **Career-center director replies asking for more info** → send the one-pager from `career-center-onepager.md`
- **Any bounce comes in** → use `career-centers-bounce-fallbacks.md` to retry

---

# JULY

## 📅 July 1 — 30-day metrics review
- 🟢 GA4 monthly comparison: May → June
- 🟢 Kit subscriber growth
- 🟢 Gumroad sales count (first dollar by now?)
- 🟢 Search Console indexed page count (should be 50-150 by now)
- 🟢 Career-center reply rate

## 📅 July 7 — Pinterest batch 2 publishing kicks in
- Pins 21-40 publish 1 every 2 days through July 17
- No action needed — they're scheduled

## 📅 July 17 — Pinterest batch 3 starts publishing
- Pins 41-60 publish 1 every 2 days through August 27
- No action needed — they're scheduled

## 📅 July 19 — Pin variants test session
- 🟢 Per `pinterest-variants-to-test-2026-07-19.md`
- Pull batch 2 analytics, identify winning patterns, build 5 variants for batch 4
- 🔵 I help with the build step

## Ongoing through July
- 🟢 Weekly YouTube uploads (videos 4-7)
- 🟢 Weekly Twitter threads (#5-8)
- 🟢 Daily 60-min routine
- 🟢 Reddit comments (1-2/week in r/cscareerquestions)
- 🟢 Career-center inbox monitoring
- 🟢 IH post #3 — mid-month, share whatever's working

## Career-center batch 4 (mid-July, ~90 min)
- 🔵 I research 15 new schools (different regions than batches 1-3)
- 🟢 You send the emails
- Goal: 70 total career-center outreaches by end of July

---

# AUGUST

## 📅 Aug 1 — 60-day metrics review
- 🟢 First bundle sale should have landed by now (per earlier honest timeline). If not — diagnose.
- 🟢 Pinterest pins should be producing first traffic — visible in GA4
- 🟢 Search Console: indexed page count should be 150-250 by now
- 🟢 Career-center: first link inclusions might be visible in Google search

## Ongoing through August
- 🟢 Weekly YouTube uploads (videos 8-11)
- 🟢 Weekly Twitter threads (#9-10, then start cycling)
- 🟢 Reddit + IH presence
- 🟢 Career-center batch 5 if patterns suggest it's worth continuing

## Possible new builds (IF traffic justifies)
- 🔵 5 more vertical landing pages (different audiences)
- 🔵 5 more with-tool pages (new AI tools as they launch)
- 🔵 New article topics based on what's actually ranking in Search Console

## ⏳ Trigger-based — could happen this month
- First bundle sale → testimonial drip starts
- First career-center link goes live → publicize in IH post
- First 100-visitor day → celebrate, screenshot, post on socials

---

# SEPT - NOV

## 📅 Sept 14 — YouTube 90-day evaluation
- 🟢 Did YouTube produce meaningful subscribers? Watch time? Traffic to snipprompts.com?
- Decision: scale (record 2/week), maintain (1/week), or pause
- Default: maintain at 1/week unless clearly working OR clearly failing

## 📅 Sept 30 — Full quarterly review
- 🟢 Q3 results across all channels
- 🟢 Decide which channels to double down on Q4 vs which to drop
- 🔵 I write the analysis if you paste the numbers

## Possible bigger builds (IF you're at meaningful traffic)
- New paid product? (Bundle v2? Different niche?)
- Affiliate program?
- Free email course as a lead magnet?
- Sponsorships if YouTube grows?

## ⏳ Trigger-based
- $100/month MRR → consider hiring 1 freelancer (writer, video editor)
- 1000 email subscribers → consider running a webinar
- 5000 YouTube subs → consider sponsorship outreach

---

# BACKGROUND TASKS (no specific date, do when applicable)

## Site / SEO infrastructure
- 🔵 Monitor Search Console weekly for indexing growth + errors
- 🔵 If a page gets traffic, look at what query → tune the page
- 🔵 Add new prompts when actual user need emerges (don't speculatively build)
- 🟢 Domain renewal check — should be 2027 or later, verify in registrar

## Email infrastructure
- 🟢 Deploy 5-day email course to Kit (append to welcome sequence) — `email-course-5-day.md`
- 🟢 Verify Kit welcome sequence fires (subscribe yourself with different email)
- 🟢 Cart abandonment sequence — set up in Gumroad when traffic justifies
- 🟢 Newsletter cadence: send Issues 2-4 in `newsletter-issues-2-3-4.md` weekly starting whenever you want

## Brand / housekeeping
- 🟢 Update Gumroad profile bio if empty
- 🟢 Add domain auto-renew if not already set
- 🟢 OG images — current single image is fine for now. Custom per-category later if traffic justifies.
- 🟢 LinkedIn personal post once you're more comfortable (or never — your call)

## Engagement / community building
- 🟢 Reddit: 5+ substantive comments per week in r/cscareerquestions, building reputation
- 🟢 IH: 2-3 comments per week on OTHER posts, building profile recognition
- 🟢 HN: 1-2 substantive comments per week on relevant top threads
- 🟢 Twitter: engage with replies to your threads, RT 1-2 relevant things per week

---

# CHANNEL SUMMARY (where each one is)

| Channel | Status | Cadence | What's Next |
|---|---|---|---|
| **SEO (snipprompts.com)** | 230 pages live, 1 indexed | Passive | Wait for indexing; let it compound |
| **Email (Kit)** | Welcome sequence live | Weekly newsletter | Verify welcome fires, deploy 5-day course |
| **Bundle (Gumroad)** | Live, $39 | Passive | Wait for first sale (~August) |
| **Career-center outreach** | 54 emails sent, 1 reply | Batches of 15 every 30 days | Batch 4 mid-July |
| **Pinterest** | 60 pins generated, 0 scheduled | 1 pin every 2 days starting June 7 | Schedule batch 2 this Fri |
| **Show HN** | Pre-drafted, posting Wed | One-shot | Tomorrow 9:30 AM MT |
| **Indie Hackers** | 1 post live, 1 reply ongoing | Bi-weekly comments + monthly post | Comment on others this week |
| **Reddit (r/cscareerquestions)** | 0 comments yet | 1-2/week | Start Thursday |
| **LinkedIn (company)** | Not set up | Weekly post | Set up next week |
| **Twitter/X** | Not set up (Screen Time blocked) | Weekly thread | Set up next week |
| **YouTube** | Plan + first script ready | Weekly video | Record after voice recovery |
| **TikTok** | Not set up | 5-7 short videos per week | ElevenLabs + CapCut next week |
| **API integrations** | None | Set up over June-July | Search Console first |

---

# REALITY CHECK

## The 11-channel framework

Most successful solo content businesses run 2-3 channels deep, not 11 shallow. You're attempting more because:
- You're 19 and have summer time
- Some channels are passive (SEO, Pinterest, email)
- AI tools let you batch content efficiently

But — if any channel feels like grinding without signal, **drop it.** Don't keep all 11 running out of guilt.

## What I'd cut first if you're overwhelmed

In order of "easiest to drop without losing much":
1. **TikTok** — high effort/ambiguous payoff for SnipPrompts brand
2. **LinkedIn personal** — you don't want it tied to your friends/family anyway
3. **Twitter/X** — useful but compounds slowly; skip if it feels forced

Keep these no matter what:
1. **SEO** — you've already built it; just needs time
2. **Email** — owned audience compounds forever
3. **Career-center outreach** — your strongest reply rate, real signal
4. **Show HN tomorrow** — one-shot, do it

---

# IF YOU READ ONE THING

Your single highest-leverage activity for the next 90 days: **post 1 YouTube video per week consistently**. That's it. Everything else is supporting work.

YouTube content compounds for years. A video that gets 10 views in week 1 can get 10,000 views in year 2 if it ranks. None of the other channels (Pinterest, email, social) compound like that.

The YouTube video doesn't have to be perfect. It has to exist. Done > polished.

That's the game.
