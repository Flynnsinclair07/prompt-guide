# Faceless YouTube — Research Report

Research only. No channel creation. Q2 execution per Path X.

Research date: 2026-04-21
Boss review: 2026-04-21 (amendments applied — see §2 tool decision, §5 budget, §6 content mix, §7 launch gate, §8 Shorts strategy)
Source notes: public pricing pages + direct YouTube search (`ChatGPT prompt for resume`) via Chrome.

---

## 1. ElevenLabs free tier

**Verdict: Free tier is a non-starter for commercial YouTube. Starter at $6/mo approved — pending OpenAI TTS price/quality comparison (§6).**

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
- Boss amendment: validate against **OpenAI TTS** (comparable quality at lower per-char cost in some tiers) before locking the ElevenLabs subscription. OpenAI TTS can also produce multiple voices without separate cloning fees.

---

## 2. Video tool decision — FREE TOOLS ONLY for first 3 videos

**Boss amendment (overrides earlier Pictory recommendation):** Pictory $25/mo **NOT APPROVED**. Use free tools for v1. Revisit paid only if output quality is unacceptable after 3 videos. Q2 tool budget capped at **$6–7/mo** (ElevenLabs only).

Scope: script-to-video pipeline for 60–90 sec shorts AND 4–7 min long-form.

| Tool | Free tier | Fits use case? | Notes |
|---|---|---|---|
| **CapCut (desktop + web)** | Yes, robust free tier | ✅ Yes — AI video generator + avatars + stock library + script-to-video | **Primary recommendation.** Full free-tier suite. Commercial-use terms need ToS read before monetization. |
| **Canva Video** | Yes — generous free plan | ✅ Yes — template-driven, text-to-video, built-in stock | Strongest for branded 4–7 min explainers. Templates match our navy/cream palette out of the box. |
| **Veed** | Free tier w/ 25-min export cap | ✅ Yes — AI voice + auto-captions + stock + screen recording | **Best for screen-recording thumbnails** (matches thumbnail strategy in §4). Free tier adds watermark; ~5 min export cap on free. |
| **DaVinci Resolve** | Fully free (not a trial) | ✅ Yes — pro-grade editor | Steeper learning curve but no cap, no watermark, no subscription. Best for polished long-form. |

**Recommended stack (v1, 3-video test)**:
- **Script + voice**: ElevenLabs Starter ($6/mo) → generate narration MP3
- **Assembly**: CapCut free for Shorts (fast turnaround), Canva Video free for long-form explainers (branded template consistency)
- **Screen recording**: macOS built-in (Cmd+Shift+5) or Veed's free recorder → feed into CapCut/Canva as the core b-roll
- **Thumbnails**: reuse Python/PIL generator from Pinterest pins — no new tool

**~~Pictory~~**: removed per Boss.
**~~Opus Clip~~**: wrong category (repurposes existing long videos, doesn't generate from script). Keep in reserve for a future phase if we accumulate long-form content worth clipping.

**Decision gate on free-tool stack**: after 3 videos, evaluate output quality against top-5 niche videos. If quality feels >1 tier below, reconsider paid (Canva Pro at $15/mo is the cheapest upgrade path).

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
- **All top 5 are long-form (4:37, 4:47, 4-8 min)** — none are Shorts. Long-form dominates search discovery. This is why Boss amended the content mix to 70% long-form.

---

## 4. Thumbnail style in this niche

**Dominant pattern**: face + bold high-contrast text overlay. 4 of 5 top results use a visible creator face. Text is:
- ALL CAPS or Title Case
- 30–60pt visual-equivalent (huge relative to thumbnail)
- 2–3 color palette max, strong contrast
- ChatGPT-green often present as an accent

**Counter-pattern (1 of 5)**: Melanie Woods — text-dominant with a small face in the corner. Yellow/black palette, 3-line stacked headline. 15K views at 2 years — respectable but not top-tier.

**Strategic call for a faceless channel (Boss-approved):**

Use **screen-recording thumbnails** as the primary strategy. A real screenshot of ChatGPT mid-task — prompt pasted, output streaming — replaces the missing face with a visual proof-of-value. Works for both Shorts and long-form.

Template spec for the Python/PIL generator:
- 1280×720 (YouTube)
- ChatGPT UI screenshot dominates left 60%
- Navy `#1B2A4E` sidebar on right 40% with cream headline (2–3 words, Arial Black)
- Arrow or circle annotation on the output to draw the eye

Fallback pattern for topical / non-screen-rec videos: Melanie Woods-style typography-only thumbnail with a single icon (resume silhouette, briefcase, dollar sign).

---

## 5. Cost + cadence plan (v1, Boss-amended)

| Line item | Monthly cost |
|---|---|
| ElevenLabs Starter | **$6** |
| CapCut (free) | $0 |
| Canva Video (free) | $0 |
| Veed (free tier) | $0 |
| DaVinci Resolve | $0 |
| Thumbnail generator (Python/PIL, reused) | $0 |
| **Total** | **$6/mo** (under $6–7 cap) |

**Cadence target (Q2 launch)**: **1–2 uploads/week** (Boss-approved).
- 1 upload/week = 4/mo → ~6k chars consumed on ElevenLabs, well under cap
- Total production time target: 2–3 hrs/week (script + assemble + thumbnail + publish)

---

## 6. Content mix — 70% long-form / 30% Shorts (Boss-locked)

Boss amendment: not just Shorts. Dominant format is long-form explainers (**4–7 min**), with Shorts as a discovery layer.

- **Long-form (70%)**: one 4–7 min video every ~10 days. SEO-style, ranks for `ChatGPT prompt for [X]` searches. Drives watch-time and subscribers.
- **Shorts (30%)**: one 60–90 sec Short every ~2 weeks. Discovery channel, surfaces to non-subscribers via the Shorts shelf. See §8 for Shorts strategy.

Rough Q2 plan (first 60 days): **6 long-form + 3 Shorts** = 9 total uploads.

**First 20-upload scope**: lock topical focus to **Job Hunter's Bundle modules only** — resume, cover letter, interview, LinkedIn, salary negotiation. Each video drives to the bundle via pinned comment + description link. Tight topical focus = better algo signal + direct product funnel.

**Other open decisions (still pending Boss):**

- **Voice choice**: CapCut/Canva have built-in voices (passable but generic). ElevenLabs delivers distinctly better voices. Given we're already paying ElevenLabs Starter, default to ElevenLabs for all scripts; use built-ins only as emergency fallback.
- **OpenAI TTS comparison**: before committing ElevenLabs subscription, test one script against OpenAI's `tts-1-hd` model. Decision criteria: voice quality at comparable naturalness → lower $/char wins.

---

## 7. Launch gate (Boss-amended)

YouTube channel creation and first upload happen when **any one** of these triggers fires:

1. **5 Job Hunter's Bundle sales** on Gumroad, OR
2. **1,000 Pinterest impressions** (cumulative across boards), OR
3. **June 15, 2026** — hard deadline regardless of the other two

First-hit trigger wins. No earlier start — channel creation is time-expensive and we need the bundle + pin momentum to feed the YouTube description links.

---

## 8. YouTube Shorts as a discovery channel

Shorts are the **top-of-funnel** for this channel. They won't drive direct product sales on their own — they drive subscribers and push viewers into the long-form explainers where the conversion happens.

### Why Shorts matter in this niche

- YouTube's Shorts shelf surfaces content to non-subscribers at much higher rates than regular videos
- The 60-sec "watch ChatGPT do X in real time" format maps perfectly to prompt content — prompt in, output out, done
- Shorts view counts are 5–10× regular videos on average, even on small channels
- Zero face required — the ChatGPT UI is the visual

### Format spec for a 60–90 sec faceless Short

| Second | Content |
|---|---|
| 0–3 | Hook: big text overlay ("Write your resume in 60 seconds with this prompt") + fast cut to ChatGPT interface |
| 3–10 | Problem reframe ("most resume prompts are generic — this one isn't") |
| 10–40 | **Prompt reveal + live execution** — screen record the prompt being pasted into ChatGPT, output streaming. This is the payoff. |
| 40–55 | Output highlight — callout boxes on 2–3 lines of the generated output |
| 55–60 | CTA: "Full prompt library at snipprompts.com — link in description / pinned comment" |

### Production stack (all free)

- **Screen record**: macOS Cmd+Shift+5 (native) or Veed free recorder
- **Vertical 1080×1920 canvas**: CapCut free
- **Voice**: ElevenLabs Starter (one short script ≈ 200–300 chars, trivial usage)
- **Captions**: auto-generate in CapCut or Veed, force on (most Shorts are watched muted)
- **Thumbnail**: not needed for Shorts (YouTube auto-picks; optimize by making sure second 0–1 of the video is visually strong)

### Top 5 Shorts in the niche — DATA GAP

Could not fetch live Shorts search results in this research pass (YouTube search is JS-walled; WebFetch returns footer only). **This specific data point requires a manual capture from YouTube.**

**Action item for Boss or a follow-up research sprint**:
- Navigate to `youtube.com/results?search_query=chatgpt+prompt+resume&sp=EgIYAQ%253D%253D` (Shorts filter)
- Capture top 5: title, channel, views, likes, faceless vs face, hook style
- Feed results back into this doc as §8.1

Pattern-level expectation (not verified): faceless Shorts in this niche almost certainly exist and perform well — the format is too natural for the content not to have been tried. Confirming this would validate the strategy; if it turns out faceless Shorts here are rare, we'd have a positioning advantage rather than a problem.

### First 3 Shorts — topic slate (aligned with bundle modules)

1. "The ChatGPT resume prompt that actually quantifies your impact" — Module 1
2. "How to ask ChatGPT for interview questions that screen the *company* for red flags" — Module 3 (differentiated content)
3. "The salary negotiation prompt worth $10,000" — Module 5 (flagship, highest hook)

Each drops the full prompt in the description so viewers can copy-paste immediately without friction.

---

## 9. What's NOT in this report

- No channel creation, no branding, no production
- No test uploads
- No thumbnail A/B test setup
- No script library planning (lives in Task 2's bundle outline work)
- No verified top-5 Shorts data (§8 data gap — flagged for follow-up)

Q2 execution gate amended: launch triggers on first hit of (5 sales / 1,000 Pinterest impressions / June 15 hard deadline).
