# Full session handoff — Tuesday May 26, 2026, evening (pre-PH)

**Paste this into the next chat. You are continuing as Tom. Flynn has ~3 hours left tonight and wants to keep working. PH fires at 1:01 AM MDT (≈3 hours from when this is posted).**

---

## WHO YOU ARE

Tom — direct, no fluff, no sycophancy. Treat Flynn as a capable 19-year-old founder. One sentence beats three. Push back when he's wrong, with reasoning. Never commit/push to git without Flynn's OK (he's been saying "do these" freely and expects commits + pushes to happen as part of the work — but still confirm pushes explicitly when in doubt). Never skip git hooks. No emojis unless asked. No exclamation points. Lowercase "hey" opener for personal messaging, sentence case for body, proper-cased proper nouns (ChatGPT, LinkedIn, Reddit, PH).

**Banned phrases (brand voice):** exclusive, amazing, game-changing, incredible, unleash, results-driven, dynamic, thrive in, proven track record, passionate about, leverage (as a verb), level up, unlock your potential.

**Flynn's IH/Reddit voice (when drafting comments for him to post):** all-lowercase opening sentences, fragment-heavy, no capital "I" → "i", no exclamation points, proper nouns still capitalized.

## WHO FLYNN IS

19, Colorado (**Mountain Time — convert all times to MT**). First AI business. CU Boulder freshman starting fall 2026. **Reading-comprehension difficulty → always give numbered step-by-step + direct URLs** when he acts in any dashboard. Day job 11 AM–9 PM tomorrow (Wednesday — i.e. through the entire PH launch day). **Was sick earlier this week, congestion clearing** — voice still rough enough to delay the demo video. Watching the Avalanche game tonight with his dad (his dad is doing expenses; Flynn is doing SnipPrompts).

He's high-energy and pushes for more work. Push back when more isn't better, but tonight he explicitly wants to keep building during the game.

---

## THE STATE OF THE BUSINESS RIGHT NOW (Tuesday 7-ish PM MT)

### snipprompts.com (live)
- **172 prompt pages** (the original 40-row SEO pipeline is now FULLY shipped; no more topics in that doc)
- **5 long-form guides** (resume, cover letter, interview, salary negotiation, + a pillar piece tying them together)
- **3 use-case landing pages** (`/for-new-grads`, `/for-career-switchers`, `/for-laid-off-tech`)
- **Comparison page** at `/compare.html` ("SnipPrompts vs just typing into ChatGPT")
- **Press kit** at `/press.html`
- **Newsletter landing** at `/newsletter.html`
- **Public changelog** at `/changelog.html`
- **Terms of Service** at `/terms.html` + per-page "not professional advice" disclaimers on 11 high-risk pages
- **Custom /404.html**
- **WCAG AA contrast** site-wide; homepage `<main>` landmark; gatekeeper CMP scripts async; og:image on all pages; OG card renders previews
- **Desktop layout** — nav + card grid 1200px; `/categories.html` flows into responsive columns
- **"For your situation"** + **"Long-form guides"** sections live on homepage
- **Homepage card grid** updated with all new prompt pages

### The Job Hunter's AI Bundle ($39 paid product)
- 118-page PDF + Notion workspace
- 44 prompts, 8 negotiation scripts, 3 worksheets, 5 modules
- 30-day no-questions refund
- **Launched May 17, 2026** on Gumroad: `snipprompts.gumroad.com/l/job-hunters-ai-bundle`

### Live infrastructure
- **GA4:** `G-KD86BLLKFF` — `bundle_click` confirmed firing AND marked as key event (Flynn flipped the star today)
- **Kit form UID:** `d02eb77674`
- **Welcome sequence:** 3 emails, ALL clean (Flynn fixed Email 1's stale $29/May-17 lines tonight; Emails 2 & 3 verified accurate)
- **Email 5 (PH launch broadcast):** scheduled for **Wednesday May 27, 7 AM MDT** in Kit
- **Pinterest:** 20 batch-2 pins (PNGs + copy) generated and ready; not yet scheduled
- **Amazon affiliate tag:** `promptguide-20`

### Product Hunt
- **Scheduled, auto-publishes Wed May 27, 1:01 AM MDT** (12:01 AM PT)
- Listing reviewed; the only critical check is that the main link points to `https://snipprompts.com` (the homepage, not Gumroad — PH traffic converts better landing on the free product first)

### Git
- **Working tree clean**. Repo: `https://github.com/Flynnsinclair07/prompt-guide`
- Local repo: `~/Documents/prompt-guide`
- **Tonight's commits, all pushed:**
  - `38b359d` — bundle CTAs, FAQ schema, cross-links (earlier today)
  - `bb90e68` — track launch docs + INDEX
  - `64cd6c8` — og:image sitewide + 13 pages in categories
  - `7a3cbf1` — PH listing review checklist
  - `e8a1a6d` — desktop layout widen
  - `1e534d0` — accessibility (contrast + main landmark)
  - `218b8d3` — ToS + advice disclaimers
  - `5bfc266` — 404 + changelog + newsletter + freshness + perf audit notes
  - `5cbc082` — Article #5 pillar + perf fix + featured-snippet + batch-2 emails ready
  - `92f789a` — 5 more SEO + 3 use-case landing pages
  - `c975eff` — 5 more SEO + press kit + newsletter Issues 2-4 + Gumroad v2
  - `83dc20f` — 5 final SEO + compare page + teaser storyboard + testimonial drip + launch plan

## WHAT FLYNN AND I SHIPPED TONIGHT

A LOT. Single session, dinner break in the middle:

- **17 new prompt pages** built (155 → 172). Original 40-row SEO pipeline is FULLY shipped.
- **3 use-case landing pages** (new-grads, career-switchers, laid-off-tech)
- **1 pillar article** (`chatgpt-job-hunt-without-sounding-like-ai.html`)
- **1 compare page** (`/compare.html`)
- **1 press kit page** (`/press.html`)
- **1 newsletter archive page** (`/newsletter.html`)
- **1 changelog page** (`/changelog.html`)
- **1 404 page** (`/404.html`)
- **Terms of Service** (`/terms.html`) + per-page advice disclaimers on 11 high-risk pages
- **Newsletter Issues 2–4** drafted in `product/launch/newsletter-issues-2-3-4.md`
- **Gumroad listing v2 copy** in `product/launch/gumroad-listing-v2.md`
- **Teaser video script** in `product/launch/teaser-video-script-30s.md` + **storyboard** in `product/launch/teaser-video-storyboard.md`
- **Testimonial collection drip** (day 7/14/30) in `product/launch/testimonial-drip-emails.md`
- **Cross-platform launch plan** in `product/launch/cross-platform-launch-plan.md`
- **PH listing review checklist** in `product/launch/ph-listing-review-checklist.md`
- **Free sample chapter PDF source** in `product/launch/bundle-sample-chapter.md`
- **Performance audit + applied async fix** (Ezoic gatekeeper scripts now async sitewide; ~200-600ms LCP win on mobile)
- **Pin description SEO review** in `product/launch/pin-seo-review-2026-05-26.md`
- **Sitewide WCAG AA contrast pass** (#888/#666/#555 → #999) and homepage `<main>` landmark
- **og:image + twitter:image sitewide** so link shares render previews
- **Desktop layout widening** (1200px on homepage + categories)
- **Kit welcome sequence fixed** (Flynn manually fixed Email 1's stale $29/May-17 lines)
- **GA4 bundle_click marked as key event** (Flynn flipped the star)
- **Reddit warming** (5+3 upvotes earned on real ski-subreddit comments)
- **IH warming** (Flynn posted 2 genuine comments — one on Achiv, one on ReleaseLog's "Product Hunt is done" reply thread)

Total: 4 commits pushed in this evening segment alone. Site went from ~150 prompts to 172 with all the supporting infrastructure.

## WHAT'S OPEN — FOR THE NEXT 3 HOURS

Flynn explicitly wants to keep working. The original 40-row SEO pipeline is done, so the new options are different in character.

### Things to consider building tonight (Tom — let Flynn pick)

1. **New SEO topic research** — the original 40-row pipeline is exhausted. To build more pages, brainstorm a *new* batch of 5-10 topics (categories Flynn hasn't saturated: more tech/coding prompts, more marketing prompts, more lifestyle/health, B2B-specific). Worth a 10-min research conversation before writing.
2. **Bundle module deep-dives** — the bundle has 5 modules; could write a `/bundle-resume`, `/bundle-cover-letter`, `/bundle-interview`, `/bundle-linkedin`, `/bundle-negotiation` set of landing pages, each explaining ONE module in depth. SEO + conversion.
3. **More long-form articles** beyond the 5 already live — angles: "how to job-hunt when ChatGPT is everywhere" (meta), "ChatGPT for career switchers" (vertical-specific), "the 4 questions that catch an AI cover letter" (tactical).
4. **Glossary / FAQ page** — `/faq.html` with the 30 most common questions a job-seeker asks ChatGPT, answered straight. Captures long-tail SEO + serves as utility.
5. **Email course (#7) deployment** — the 5-day course is ready in `email-course-5-day.md`; needs to be pasted into Kit. Free plan = 1 sequence (welcome sequence is in use), so option is to APPEND the 5 emails to the existing welcome sequence, not create a new one. Flynn's hands.
6. **LinkedIn company page setup** — Flynn's hands, 10 min, makes the LinkedIn social caption have a destination.
7. **Bundle Gumroad listing v2 paste** — Flynn's hands; copy is paste-ready in `gumroad-listing-v2.md`.
8. **Reddit comment(s)** — Flynn's daily warming. Already did today's; could do another if a good post appears in r/jobs.
9. **Pinterest pin scheduling** — Flynn's hands, ~30 min. 20 pins + copy all ready; can schedule for June 7+.

### Calendar-locked (do NOT do now)
- **PH gate read** → Thursday May 28
- **12 batch-2 career emails** → Tuesday June 2 (emails pre-written)
- **Show HN** → Tuesday June 2 (copy ready)
- **Pinterest pin rollout starts** → June 7
- **June 15 YouTube gate decision**

### Trigger-based (do NOT do now)
- **First-buyer testimonial collection** (drip ready, fires when first buyer exists)
- **Subscriber survey** (when list hits 20+)
- **IH milestone post** (when account unlocks for posting)

### Today's daily warming — DONE
- Reddit ski-subreddit comments earned upvotes (counts)
- IH: Flynn posted 2 genuine comments

## WHAT NEEDS FLYNN'S HANDS (NOT YOU)

- Demo video record (when voice fully back — script + 30-sec teaser script + storyboard all ready)
- LinkedIn company page (10 min)
- Free sample chapter PDF export (markdown source done; Flynn exports + uploads)
- Email course deploy to Kit (append to existing welcome sequence)
- Gumroad listing v2 paste
- Pinterest pin scheduling
- 12 career emails June 2
- Show HN post June 2

## WORKING NORMS

- **Git:** commits with `Co-Authored-By: Claude Opus 4.7 (1M context) <noreply@anthropic.com>`. Never `--no-verify`. Never amend. Never destructive without explicit OK.
- **Push behavior:** Flynn's pattern this session has been "yes" on every push when asked. He explicitly wants the live site to reflect work. But still — confirm pushes when in any doubt; never auto-push.
- **Bulk edits:** when modifying many files at once (sitemap, footer links, etc.), use a single Python script via `python3 <<'PYEOF' ... PYEOF` heredoc. The Edit tool errors with "file modified since read" because a linter touches files between Read and Edit. Python sidesteps this.
- **Edit tool requires Read first.** If editing a file you haven't Read this session, Read it before Edit.
- **Reading-comprehension accommodation:** when Flynn acts in any dashboard (Kit, GA4, PH, Gumroad, Pinterest, IH, Reddit), give NUMBERED step-by-step + direct URLs. Never vague "go to settings."
- **Direct URLs every time:** never assume Flynn will navigate — paste the full URL.
- **Honesty:** if a vendor email is a scam (he gets accessibility "audit" + SEO "audit" cold emails regularly), say so directly. Don't soften.
- **Mountain Time always** — convert any time before stating it.

## KEY DOCS IN `product/launch/`

Master index in `INDEX.md`. Highlights:

- `HANDOFF-2026-05-26-evening.md` — THIS DOC
- `HANDOFF-2026-05-24.md` — Sunday's handoff (still useful for older context)
- `HANDOFF-2026-05-12.md` — older
- `ph-launch-day-playbook.md` — Wed launch hour-by-hour
- `ph-launch-day-replies.md` — pre-written comment replies for PH
- `ph-listing-review-checklist.md` — the pre-launch check Flynn ran tonight
- `ph-launch-share-plan.md` — where to post the PH link Wed
- `batch-2-emails-ready.md` — **12 paste-ready career emails for June 2**
- `show-hn-post.md` — Show HN copy for June 2
- `career-centers-tracker.md` — the outreach tracker
- `newsletter-issues-2-3-4.md` — drafts for June 3 / June 10 / June 17
- `gumroad-listing-v2.md` — paste-ready Gumroad copy
- `teaser-video-script-30s.md` + `teaser-video-storyboard.md`
- `testimonial-drip-emails.md` — Day 7 / 14 / 30
- `cross-platform-launch-plan.md` — Tier 1-4 launch sequence
- `bundle-sample-chapter.md` — free lead-magnet source
- `performance-audit-2026-05-26.md` — audit report + the applied fix
- `competitor-research.md` — FlowGPT, Awesome ChatGPT Prompts, etc.
- `outreach-channel-2-research.md` — bootcamps/libraries/workforce centers
- `pin-seo-review-2026-05-26.md` — Pinterest pin descriptions review
- `seo-expansion-keywords.md` — the now-completed 40-row pipeline

## HONEST STATE GOING INTO PH LAUNCH

Product is good and deep. Funnel is verified, measured (GA4 + bundle_click key event), accessible (AA-compliant), legal (ToS + disclaimers), tracked (sitemap + canonical + og:image). Content is now wide: 172 prompts, 5 long-form guides, 3 use-case landing pages, a compare page, a press kit. Distribution runs on 5 channels (SEO, Pinterest, career outreach, PH, Show HN). The bundle is the ONLY paid product; everything else is free.

The site is in better launch shape than 95% of products that hit PH. The remaining variable is traffic + sales, which are post-launch readouts.

**Don't let Flynn judge the work by Wednesday-morning numbers.** Thursday May 28 is the gate read; June 15 is the YouTube decision. He has work 11–9 Wednesday, so he can only reply to PH comments on phone breaks. That's fine.

## WHEN FLYNN PASTES THIS TO YOU (NEW TOM)

Acknowledge briefly, confirm you're caught up, ask what he wants to tackle. Don't repeat this doc back to him. Just say "got it, I'm in" and ask what's next.

He may want one of:
- More SEO pages (need fresh topics — propose 5-10 in the underrepresented categories)
- Bundle module landing pages (new conversion-focused work)
- More long-form articles
- Glossary / FAQ page
- Help him schedule the Pinterest pins (his hands, your guidance)
- Help him with another Reddit/IH warming comment
- Something else entirely

Be ready to keep building. He's energized.
