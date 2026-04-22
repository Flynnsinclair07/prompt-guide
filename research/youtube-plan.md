# Faceless YouTube — Research Report

Research only. No channel creation. Q2 execution per Path X.

Research date: 2026-04-21
Source notes: public pricing pages + direct YouTube search (`ChatGPT prompt for resume`) via Chrome.

---

## 1. ElevenLabs free tier

**Verdict: Free tier is a non-starter for commercial YouTube. Must upgrade.**

| Item | Free tier | Notes |
|---|---|---|
| Character limit | 10,000 credits/month (≈10,000 chars) | 1 char ≈ 1 credit on most models |
| Voice cloning | ❌ not included | Instant clone starts at Starter ($6/mo) |
| Commercial license | ❌ not included | First available on Starter ($6/mo) |
| Attribution requirement | Not spelled out on free tier, but commercial use is explicitly gated — monetized YouTube counts as commercial |
| Export restrictions | None specified |

**Implication:**
- 10k chars/month ≈ ~7 scripts @ 1,500 chars each — too thin for 2–3 uploads/week.
- **Commercial use requires Starter tier at $6/mo minimum.** Non-negotiable if channel is monetized or has affiliate links.
- Recommendation: launch on **Starter ($6/mo)** from day 1. Upgrade to **Creator ($22/mo)** if monthly cap (~100k credits) is hit.

---

## 2. Video tool comparison — 60–90 sec AI-voiced shorts

Scoped to the specific use case: "paste a script → get a 60–90 sec video with AI voice + auto b-roll → export."

| Tool | Free tier | Watermark on free | Fits use case? | Paid entry | Notes |
|---|---|---|---|---|---|
| **Creatify** | 2 videos/mo (10 credits) | ✅ yes, free has watermark | ✅ yes — script-to-video w/ AI voice + stock | $33/mo (20 videos) | Built for ad-style shorts. Free tier too small to test meaningfully. |
| **Opus Clip** | 60 min/mo processing | — | ❌ no — **repurposes existing long videos into clips.** Does NOT generate from script + voice. | Paid plans credit-based | Wrong tool for this use case. Skip. |
| **Pictory** | 14-day trial, 3 projects | Trial only | ✅ yes — script-to-video, licensed stock, AI voiceover built-in | $25/mo (Starter, 200 video min) | Closest match to use case. Licensed stock + voice bundled = no extra cost. Used heavily by faceless YouTubers. |
| **CapCut AI video** | Yes (free tier exists) | Details unclear from docs | ✅ yes — text-to-video w/ AI voice + avatars + stock | Free for starter use | Has 100+ avatars, 30+ templates. Commercial terms need ToS review. |

**Recommendation**: **Pictory ($25/mo)** as the primary for v1.
- Script-to-video pipeline matches the use case exactly
- Licensed stock + voice built in → no separate ElevenLabs needed for first 3 months (reassess later if voice quality feels off)
- Proven in the faceless YouTube niche
- Under the $30 monthly-tool ceiling

**Fallback**: **CapCut** free tier if we want to de-risk spend in month 1. Trade-off: more assembly work, less pipelined.

**Not Opus Clip**: wrong category — it's for repurposing podcasts and long videos. Hold in reserve for a future phase where we're clipping long-form content.

---

## 3. YouTube niche competition

Query: `ChatGPT prompt for resume` — organic top 5 (sponsored skipped).

| # | Video | Channel | Views | Age | Thumbnail style |
|---|---|---|---|---|---|
| 1 | Tailor Your Resume in Under 3 Minutes Using ChatGPT (Step-by-Step) | Ogaga Johnson (Project Management Coach) | 43K | 9 months | Face + big colored text overlay |
| 2 | Fix an AI-Sounding Resume With These ChatGPT Prompts | Resume Genius (verified brand) | 2.7K | 2 months | Face + branded graphics + comparison badges |
| 3 | Land a Job using ChatGPT: The Definitive Guide! | Jeff Su (verified) | 890K | 2 years | Face + ChatGPT logo + resume graphic |
| 4 | Master the Perfect ChatGPT Prompt Formula (in just 8 minutes)! | Jeff Su (verified) | 3.5M | 2 years | Face + formula chalkboard overlay |
| 5 | How Recruiters Can Tell Your Resume Came From ChatGPT | Melanie Woods | 15K | 2 years | Text-dominant + small face |

**Key observations:**

- **Top views skew to evergreen (2-year-old) videos** — the niche is long-tail, ranks once and earns views for years. Good news for SEO-style faceless content.
- **Jeff Su dominates** — 4.4M+ combined views from 2 videos. Heavy moat but also validates the niche.
- **Smaller/newer channels can rank** — Ogaga (43K, 9mo) and Resume Genius (2.7K, 2mo) both make top 5. Newer entrants aren't locked out.
- **Upload frequency for top 5**: not shown in search, but multi-year-old videos still at the top = the niche rewards one-good-video-per-month cadence over daily churn. Pace for Path X should be **1–2 uploads/week**, not daily.
- **No faceless channel in the top 5.** That's both a warning and an opening — see §4.

---

## 4. Thumbnail style in this niche

**Dominant pattern**: face + bold high-contrast text overlay. 4 of 5 top results use a visible creator face. Text is:
- ALL CAPS or Title Case
- 30–60pt visual-equivalent (huge relative to thumbnail)
- 2–3 color palette max, strong contrast
- ChatGPT-green often present as an accent

**Counter-pattern (1 of 5)**: Melanie Woods — text-dominant with a small face in the corner. Yellow/black palette, 3-line stacked headline ("HOW CAN I TELL / ChatGPT / CREATED YOUR RESUME"). 15K views at 2 years — respectable but not top-tier.

**Strategic call for a faceless channel:**

Going faceless in a face-dominated niche is bucking convention. Two viable ways to compensate:

- **A. Screen-recording thumbnails**: show the ChatGPT interface mid-task ("Watch this prompt build a resume in real time"). Replaces the face with a visual proof-of-value.
- **B. Typography-only + a clear visual hook**: stacked high-contrast text with one piece of iconography (a resume mock-up, a ChatGPT logo, a simple diagram). Melanie Woods is a data point this can work.

**Recommendation**: hybrid — Option A for thumbnails (real screen capture + minimal text), Option B for the first 3 video title cards. Test both, let CTR data pick the winner by video #10.

---

## 5. Cost + cadence plan (v1)

| Line item | Monthly cost | Notes |
|---|---|---|
| ElevenLabs Starter | $6 | Commercial license, ~40k chars, ~25 scripts |
| Pictory Starter | $25 | 200 video min, script-to-video, licensed stock |
| **Total** | **$31/mo** | Under the $40 ceiling |

**Cadence target (Q2 launch)**: 1–2 uploads/week.
- 1 upload/week = 4/mo → ~6k chars consumed on ElevenLabs, well under cap
- Pictory 200 video minutes = ~133 uploads at 90 sec each; zero risk of cap
- Total production time target: 2–3 hrs/week (script + assemble + thumbnail + publish)

---

## 6. Open risks + decisions for Boss

- **Voice choice**: Pictory has built-in AI voices (likely generic). ElevenLabs delivers distinctly better voices but adds a pipeline step. Start with Pictory's built-in for v1; upgrade to ElevenLabs for scripts where voice quality matters (ask: is the listener a job seeker who'll notice robotic voice? Probably yes — consider ElevenLabs from day 1 despite the pipeline cost).
- **Faceless vs low-face hybrid**: confirmed faceless is harder in this niche. Willing to reconsider or 100% committed to no face?
- **Short-form vs long-form**: 60–90 sec shorts are the spec, but top 5 organic results are all 4–8 min. Shorts may earn fewer views per upload but are also faster to produce. Recommend **test both formats in the first 10 uploads** — half shorts, half 4-min explainers — and let watch-time data pick the winner by month 2.
- **Channel niche scoping**: "ChatGPT prompt for X" is broad. Narrow the first 20 uploads to **Job Hunter's Bundle topics only** (resume, cover letter, interview, LinkedIn, salary negotiation). Each video drives to bundle via pinned comment + description link. Tight topical focus = better algo signal + direct product funnel.

---

## 7. What's NOT in this report

- No channel creation, no branding, no production
- No test uploads
- No thumbnail A/B test setup
- No script library planning (lives in Task 2's bundle outline work)

Q2 execution gate: complete Job Hunter's Bundle launch first. YouTube starts after bundle is live and has its first 5 sales.
