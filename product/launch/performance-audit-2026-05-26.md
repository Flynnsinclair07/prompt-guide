# Performance audit — 2026-05-26

Code-level review of likely LCP/INP issues on snipprompts.com. **I can't run Lighthouse from here**, so this is what's findable from the source. Pair this with a real Lighthouse run on `snipprompts.com` and `snipprompts.com/prompts/best-chatgpt-prompt-for-writing-a-resume.html` once you can.

## What looks fine
- **Static HTML on GitHub Pages.** No server-side render cost, edge caching is good, no runtime DB. Baseline is solid.
- **No client-side framework, no bundler, no JS hydration step.** Total JS on a prompt page is ~10 lines (the copy-button handler). LCP and INP cost from your own code is essentially zero.
- **CSS is one ~300-line file (`/style.css`)**, no `@import`, no preloaded fonts, no FOUC risk.
- **`og-cover.png` is 60KB, 1280×720.** Fine for social — and it's only loaded by social crawlers, not visitors.
- **Favicons sized correctly** (16×16, 32×32, 180×180 apple-touch).
- **No render-blocking custom fonts** — `body` uses `-apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif`, the system stack. Fastest possible font load.

## What probably hurts performance (in priority order)
1. **Ezoic + Google Analytics scripts in `<head>`, loaded ahead of content.** Every page loads ezojs CMP + ezoic analytics + gtag.js. Even with `async`, the **CMP scripts (`cmp.gatekeeperconsent.com`, `the.gatekeeperconsent.com`) are NOT async** in the markup — they're plain `<script src=...>` tags. That blocks parser progress until they fetch. On a cold-cache mobile connection this is the single biggest INP/LCP drag. **Fix:** add `async` (or `defer`) to both gatekeeper script tags. Five-character change per page, big real-world win.
2. **Total third-party JS is heavy.** Ezoic CMP + Ezoic SA + Ezoic analytics + gtag = ~4 third-party domains contacted on every page load. Each is a connection cost. **Fix:** can't remove Ezoic (revenue), but make all 4 truly async/defer. Long-term: consider whether Ezoic is netting more than it costs at current traffic — at 127 impressions/week the revenue is tiny, the perf cost is the same as at scale.
3. **Prompt-page JSON-LD blocks are 2–4 KB each.** Not huge, but they're inline in the HTML and they're served on every prompt page (`HowTo` + `FAQPage` + `BreadcrumbList`). Worth it for SEO; nothing to fix.
4. **Card-grid on homepage renders 147+ DOM nodes** (one per card). Inexpensive on desktop, can be noticeable on a low-end Android. **Fix (future):** lazy-render below-the-fold cards via `IntersectionObserver`, or paginate. Not urgent.
5. **`launch-banner` uses a CSS gradient + transition.** Cheap. No fix.

## Specific changes I'd recommend (in order of payoff)
1. **Make the 2 gatekeeper scripts async.** Edit `<script data-cfasync="false" src="https://cmp.gatekeeperconsent.com/min.js"></script>` → add `async`. Same for `the.gatekeeperconsent.com/cmp.min.js`. Apply to every HTML file (sed/perl, one pass). Estimated LCP improvement on mobile: 200–600ms.
2. **Add `loading="lazy"` to any future inline images on the homepage** (currently no `<img>` tags in the card grid, but if you ever add thumbnails, this is the discipline).
3. **Add a `<link rel="preconnect" href="https://www.googletagmanager.com">`** in `<head>` to warm the GA connection during parsing. Marginal but free.

## What NOT to chase
- Don't minify CSS. Your CSS is 300 lines; minification saves bytes that gzip already eats. Negligible win, real complexity cost.
- Don't move to a static-site generator. Plain HTML + GitHub Pages is already the fastest option short of edge functions.
- Don't bother with Service Worker / PWA at current traffic. The complexity outweighs any caching benefit.

## Action item
The single highest-payoff change is **making the two gatekeeper consent scripts async**. Want me to do that as a separate commit?
