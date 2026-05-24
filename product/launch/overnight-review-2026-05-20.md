# Overnight review — Wed May 20, 2026 → Thu May 21 AM

**TL;DR:** All 3 tasks done. 1 critical issue in affiliate-research.md (Skillshare blocked). 6 high-fit prompt pages missing bundle CTAs — copy drafted below for each. Article HTML draft ready for review at `product/launch/article-1-resume-without-inventing-experience.html`. Banned-phrase scan: clean across all 6 dispatch files + new HTML (all hits are meta-references in quotes as examples).

---

## Task 1: Dispatch file audit (5 files)

### ✓ show-hn-post.md — ship as-is

- Voice clean
- Title char count flagged correctly (81 vs 80 limit) with cleaner 73-char variant ready
- Pre-staged answers for the 3 predictable first comments are sharp
- Banned-phrase mentions are meta-references in quotes (line 26, 51) — fine

**Action:** none. Post Tue/Wed/Thu 8-10 AM ET as scheduled.

---

### ⚠️ affiliate-research.md — CRITICAL: Skillshare blocked

- **Skillshare's affiliate program is invite-only as of 2026-05-20** (you confirmed tonight). The file's entire "apply Skillshare now" recommendation is dead.
- Coursera path remains valid but gated by 1k uniques/mo — apply post-PH.
- Other 3 (Udemy / LinkedIn Learning / MasterClass) skip-tier reasoning still correct.

**Action options:**

- **A) Add a banner note** at the top of the file:
  ```
  > **Update 2026-05-20:** Skillshare is currently invite-only. The "apply now" recommendation below is blocked. Re-check the signup page periodically; apply when reopened. Coursera path (post-PH) is unchanged.
  ```
- **B) Wait** — leave the file as-is, set a calendar reminder for June 5 to re-check Skillshare. If reopened, ignore the banner. If still closed, add it.

Memory file saved: `~/.claude/.../memory/project_skillshare_blocked.md`. So next session won't re-recommend it cold.

**My pick: A.** Future-you reading this file might miss the memory ping. Banner is 30 seconds of work.

---

### ✓ article-1-draft.md — ship as-is, HTML built

- Voice clean across 1,750 words
- Keyword rationale in the frontmatter is solid (saturation analysis is honest)
- 4 internal links all point to live pages on snipprompts.com
- Soft Gumroad CTA at the end is internally consistent with the article (refuse-to-invent framing matches the bundle's actual structure)
- One judgment call I made in the HTML port: dropped the "$39, 119 pages, 44 prompts, 30-day refund" specifics from the closing CTA body and moved them to a smaller line below the button. Reduces the "ad" feel at the end of an article. See `article-1-resume-without-inventing-experience.html` lines 142-144 — change back if you prefer the original.

**Action:** review the HTML (see Task 2), decide deploy URL.

---

### ✓ career-center-outreach.md — ship as-is

- Voice clean, lowercase "hey," opener, sentence-case body
- One link in signature, no bundle mention anywhere (correct — career centers won't link to commercial)
- "AI is already happening, here's the safer version" hook is the right angle for conflicted directors
- Operational notes (personalization, send time, batch size) all accurate

**Action:** none for the file itself. When you start sending, the 20-per-batch + manual personalization line is the rule. Don't bulk-send.

---

### ✓ reddit-prep.md — ship as-is (already actioned)

- 8 archetypes cover the recurring posts well
- Workflow + account-hygiene notes at the bottom were correct (you hit them tonight — your Ok_Penalty1888 account is borderline for r/jobs/r/resumes per the file's rules)
- Tonight's reality check: account warming worked in r/skiing, AutoMod ate r/gym attempts → consistent with the file's "lighter-mod subs first" guidance

**Action:** none. File becomes load-bearing next week (~May 27+) when account has aged enough to post the archetypes in target subs.

---

### ✓ indie-hackers-post.md — ship after Line A fix

- Already reviewed tonight, factual issue flagged (test-purchase refund line, line 22)
- Recommended fix: delete the parenthetical entirely. Simpler.
- Tonight's reality check: posted 1 warming comment on ReleaseLog's post. Need 1-2 more before the milestone post lands.

**Action:** apply Line A fix tomorrow before posting.

---

## Task 2: HTML article build

**File:** `product/launch/article-1-resume-without-inventing-experience.html`

**Status:** draft, uncommitted, not in the live site directory. Visible in your Launch preview panel.

**Decisions I made (review before deploy):**

1. **Canonical URL:** I used `https://snipprompts.com/articles/chatgpt-resume-without-inventing-experience.html` — implies a new `/articles/` directory. No such directory exists yet. Options:
   - **A)** Create `/articles/` and move the file there before deploy. Cleanest URL pattern for longform content vs. prompt pages.
   - **B)** Deploy under `/prompts/` with the same URL slug. Mismatch (it's not a prompt page) but avoids creating new directory structure.
   - **C)** Use `/guides/` instead of `/articles/`. Functionally identical.

   **My pick: A.** Longform articles deserve their own URL pattern — easier to mark separately in the sitemap, easier to add more later, the breadcrumb schema already uses "Articles" as the parent.

2. **Schema:** used `Article` schema instead of `HowTo` (matches longform content type). Added breadcrumb schema. Did NOT add FAQ schema since the article has no Q&A blocks.

3. **Author/publisher:** filled in with your name + SnipPrompts. Schema requires both for Article type.

4. **Bundle CTA at the end:** softer than the prompt-page CTAs ("Want the full job-search workflow?" framing). The article isn't a sales page, so a hard CTA breaks the read. Price + refund moved to a sub-line under the button.

5. **Related Prompts:** linked to all 4 internal references from the article body. Plus same Kit email-capture block from the prompt pages.

**Before deploy you need to:**

- Decide A vs B vs C on URL pattern (see above)
- Move/copy file to chosen directory
- Update `sitemap.xml` with the new URL + today's lastmod
- Update `categories.html` or homepage if you want a "Recent Articles" or "Guides" surface
- Commit + push when satisfied

---

## Task 3: Bundle CTA audit

**Method:** grepped all 134 prompt pages for `job-hunters-ai-bundle` link. 4 pages have it (the optimized career 4: writing-a-resume, writing-a-cover-letter, job-interview-prep, resignation-letter). 130 don't.

**High-fit pages currently missing the CTA** — these should get one because the bundle directly covers their topic:

| Page | Why it fits the bundle | Priority |
|---|---|---|
| `best-chatgpt-prompt-for-resume-bullets.html` | Bundle has 8 resume prompts incl. bullet rewrites with ATS keyword injection | **HIGH** |
| `best-chatgpt-prompt-for-linkedin-profile.html` | Bundle covers LinkedIn profile + headline + About | **HIGH** |
| `best-chatgpt-prompt-for-negotiation.html` | Bundle has 8 negotiation scripts. Direct overlap. | **HIGH** |
| `best-chatgpt-prompt-for-linkedin-posts.html` | LinkedIn-adjacent; bundle has post + comment prompts | MEDIUM |
| `best-chatgpt-prompt-for-networking-email.html` | Job-search workflow includes outreach emails | MEDIUM |
| `best-chatgpt-prompt-for-performance-review.html` | Career-adjacent; bundle has perf-review angle | LOW |

**Skip:** salary/compensation pages that don't exist; everything else on the 134 list (creative writing, lifestyle, coding, etc.) is too far from the bundle's job-search focus. Don't over-CTAize.

### Proposed CTA copy for each (drop in before the `Related Prompts` section, matching the writing-a-resume.html pattern at line 121)

**1. resume-bullets:**
```html
<section><h2>Want the full resume workflow?</h2><p>This prompt rewrites your bullets. <strong>The Job Hunter's AI Bundle</strong> has 8 resume prompts — bullet rewrites, ATS keyword injection, a career-switcher angle, a 5-step optimization checklist, and 3 before/after examples — inside the complete resume-to-offer-letter workflow: 44 prompts, 8 negotiation scripts, 3 worksheets.</p><p><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta">Get The Job Hunter's AI Bundle →</a></p></section>
```

**2. linkedin-profile:**
```html
<section><h2>Want the full LinkedIn workflow?</h2><p>This prompt writes your profile. <strong>The Job Hunter's AI Bundle</strong> covers the full LinkedIn arc — profile + About + headline variants, post and comment prompts, recruiter-outreach reply templates — alongside resume, cover letter, interview prep, and salary negotiation: 44 prompts, 8 negotiation scripts, 3 worksheets, all with refuse-to-invent guardrails.</p><p><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta">Get The Job Hunter's AI Bundle →</a></p></section>
```

**3. negotiation:**
```html
<section><h2>Want every negotiation script?</h2><p>This prompt builds one counter. <strong>The Job Hunter's AI Bundle</strong> has 8 negotiation scripts covering base salary, equity, signing bonus, relocation, remote work, title bump, start date, and competing-offer leverage — plus the full job-search workflow that gets you to the offer in the first place: 44 prompts, 3 worksheets.</p><p><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta">Get The Job Hunter's AI Bundle →</a></p></section>
```

**4. linkedin-posts:**
```html
<section><h2>Want the full LinkedIn workflow?</h2><p>This prompt writes your posts. <strong>The Job Hunter's AI Bundle</strong> wraps the LinkedIn workflow — profile, About, headline, posts, comments, recruiter replies — inside the full job-search toolkit: 44 prompts, 8 negotiation scripts, 3 worksheets, all engineered to not sound like AI.</p><p><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta">Get The Job Hunter's AI Bundle →</a></p></section>
```

**5. networking-email:**
```html
<section><h2>Want the full job-search toolkit?</h2><p>This prompt handles outreach. <strong>The Job Hunter's AI Bundle</strong> covers the full arc — resume, cover letter, LinkedIn, recruiter outreach, interview prep, salary negotiation — as a 119-page workbook with 44 prompts, 8 negotiation scripts, and 3 worksheets. Same refuse-to-invent discipline applied end-to-end.</p><p><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta">Get The Job Hunter's AI Bundle →</a></p></section>
```

**6. performance-review:**
```html
<section><h2>Want the full career toolkit?</h2><p>This prompt structures your self-review. <strong>The Job Hunter's AI Bundle</strong> goes further — when the review goes well (or doesn't), the bundle has the resume, LinkedIn, interview, and salary-negotiation prompts to use the result: 44 prompts, 8 negotiation scripts, 3 worksheets.</p><p><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta">Get The Job Hunter's AI Bundle →</a></p></section>
```

### Where to insert

In each page, insert the section right before this block:
```html
<section>
  <h2>Related Prompts</h2>
  <div class="related">
    ...
```

That matches the pattern on writing-a-resume.html line 121, which sits between the "Tips" / "Tools" sections and the "Related Prompts" section.

### Suggested order

If you want to ship these incrementally rather than all at once:

1. **resume-bullets** + **linkedin-profile** + **negotiation** (the 3 HIGH-priority ones) — these are the cleanest topical fits and most likely to convert. Do these tomorrow morning between IH comments and demo video.
2. **linkedin-posts** + **networking-email** — when you have 15 more minutes. Less urgent.
3. **performance-review** — only if you want full coverage. Bundle fit is weakest here.

### Sitemap

After CTA additions, bump `<lastmod>` on each modified page in `sitemap.xml`. The 4 already-optimized pages already had a bump 5/18; these 6 are net-new.

---

## Banned-phrase scan results (passed)

Scanned all 6 dispatch files + new article HTML for: exclusive, amazing, game-changing, incredible, unleash, results-driven, dynamic, thrive in, proven track record, passionate about, level up, unlock your potential.

**All hits are meta-references** — phrases appearing in quotes as examples of what to avoid:

- `show-hn-post.md:26` — describes the banned-phrase list as a feature of the prompts
- `show-hn-post.md:51` — "what to avoid in the post itself" instructions
- `article-1-resume-without-inventing-experience.html:56` — quoting the cliché "passionate about driving cross-functional collaboration" as an example of bad output
- `article-1-resume-without-inventing-experience.html:83` — listing failure-mode 3 (generic clichés) with examples in quotes
- `article-1-resume-without-inventing-experience.html:116` — example prompt body showing the banned list
- `reddit-prep.md:77, 79` — same meta-pattern in archetype 3 cover-letter reply

**No actual voice violations.** All files clean.

---

## Tomorrow morning's queue (revised based on tonight's work)

1. **Apply affiliate-research.md banner** (Skillshare blocked) — 1 min
2. **Apply Line A fix** to indie-hackers-post.md, then comment on 1 more IH thread for warming, then post the milestone story — 30 min
3. **Demo video** — script ready, ~60 sec — 30 min
4. **Add 3 HIGH-priority bundle CTAs** (resume-bullets, linkedin-profile, negotiation) using the copy in Task 3 above — 15 min, plus sitemap lastmod bump
5. **Decide article URL pattern** (A/B/C in Task 2), move HTML file, update sitemap, commit + push — 20 min
6. **College career centers outreach** — first batch of 20 personalized emails — 60-90 min

Stretch tasks (if energy remains after the demo video):
- Show HN post (or wait until next Tue/Wed morning per the file's recommendation)
- Bundle CTAs #4-6 (MEDIUM/LOW priority)

---

## Files produced overnight

1. `product/launch/article-1-resume-without-inventing-experience.html` — draft HTML, uncommitted, not yet in live site directory
2. `product/launch/overnight-review-2026-05-20.md` — this file
3. `~/.claude/projects/-Users-flynnsinclair07-claude/memory/project_skillshare_blocked.md` — memory note for next session

No commits made. No live site files modified.

— end of overnight review —
