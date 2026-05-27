#!/usr/bin/env python3
"""Generate 3 competitor comparison pages: SnipPrompts vs FlowGPT / awesome-chatgpt-prompts / AIPRM."""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

TEMPLATE = """<!DOCTYPE html>
<html lang="en">
<head>
<script async data-cfasync="false" src="https://cmp.gatekeeperconsent.com/min.js"></script>
<script async data-cfasync="false" src="https://the.gatekeeperconsent.com/cmp.min.js"></script>
<script async src="//www.ezojs.com/ezoic/sa.min.js"></script>
<script>
window.ezstandalone = window.ezstandalone || {};
ezstandalone.cmd = ezstandalone.cmd || [];
</script>
<script src="//ezoicanalytics.com/analytics.js"></script>

<meta name="google-site-verification" content="UsbuShh_rEGpXp2XLU7L0fjjSZpzPejHGhc8Z9uCh-0">
<script async src="https://www.googletagmanager.com/gtag/js?id=G-KD86BLLKFF"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){dataLayer.push(arguments);}
gtag('js', new Date());
gtag('config', 'G-KD86BLLKFF');
</script>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>@@TITLE@@ | SnipPrompts</title>
<meta name="description" content="@@DESC@@">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/style.css">
<link rel="canonical" href="https://snipprompts.com/@@SLUG@@.html">
<meta property="og:type" content="article">
<meta property="og:title" content="@@TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://snipprompts.com/@@SLUG@@.html">
<meta property="og:site_name" content="SnipPrompts">
<meta property="og:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
</head>
<body>
<nav>
  <a href="/" class="logo">SnipPrompts</a>
  <a href="/categories.html">All Prompts</a>
</nav>
<main>
  <article>
    <h1>@@H1@@</h1>
    <p class="subtitle">@@SUBTITLE@@</p>

    <section>
      <h2>The short answer</h2>
      <p>@@SHORT_ANSWER@@</p>
    </section>

    <section>
      <h2>What @@COMPETITOR@@ is</h2>
      <p>@@COMPETITOR_DESC@@</p>
    </section>

    <section>
      <h2>What SnipPrompts is</h2>
      <p>@@SELF_DESC@@</p>
    </section>

    <section>
      <h2>Side by side</h2>
      <div style="overflow-x:auto;margin-top:16px;">
      <table style="width:100%;border-collapse:collapse;color:#ddd;font-size:14px;">
        <thead>
          <tr style="background:#1a1a2e;">
            <th style="text-align:left;padding:12px;border-bottom:2px solid #6c63ff;">&nbsp;</th>
            <th style="text-align:left;padding:12px;border-bottom:2px solid #6c63ff;">@@COMPETITOR@@</th>
            <th style="text-align:left;padding:12px;border-bottom:2px solid #6c63ff;">SnipPrompts</th>
          </tr>
        </thead>
        <tbody>
          @@COMPARISON_ROWS@@
        </tbody>
      </table>
      </div>
    </section>

    <section>
      <h2>When you'd actually want @@COMPETITOR@@ instead</h2>
      <p>@@WHEN_COMPETITOR@@</p>
    </section>

    <section>
      <h2>When SnipPrompts is the better fit</h2>
      <p>@@WHEN_SELF@@</p>
    </section>

    <section>
      <h2>One honest critique of SnipPrompts</h2>
      <p>@@HONEST_CRITIQUE@@</p>
    </section>

    <section>
      <h2>Where to start</h2>
      <p>If you've been using @@COMPETITOR@@ and the outputs feel generic or AI-tell heavy, try one of these head-to-head with your usual approach:</p>
      <ul>
        <li>The <a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">resume prompt</a> on a bullet that's currently vague.</li>
        <li>The <a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">cover letter prompt</a> on the next role you're applying to.</li>
        <li>The <a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">salary negotiation prompt</a> if you have an offer in hand.</li>
      </ul>
      <p>If you can tell the difference in 5 minutes, you don't need to read further. If you can't, neither one cost you anything.</p>
    </section>
  </article>
</main>
<footer>
<p>&copy; 2026 SnipPrompts. AI prompts for every use case.</p>
<p style="margin-top:8px;">
<a href="/about.html" style="color:#999;margin-right:16px;">About</a>
<a href="/privacy.html" style="color:#999;margin-right:16px;">Privacy</a>
<a href="/terms.html" style="color:#999;margin-right:16px;">Terms</a>
<a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>
</p>
</footer>
</body>
</html>
"""


def row(label, them, us):
    return f"""<tr style="border-bottom:1px solid #333;">
            <td style="padding:12px;font-weight:600;color:#fff;">{label}</td>
            <td style="padding:12px;">{them}</td>
            <td style="padding:12px;color:#ccc;">{us}</td>
          </tr>"""


PAGES = [
    {
        "slug": "snipprompts-vs-flowgpt",
        "competitor": "FlowGPT",
        "title": "SnipPrompts vs FlowGPT &mdash; honest comparison",
        "desc": "Honest side-by-side: what FlowGPT is good for, what it's not, and how SnipPrompts compares for job-hunt and career prompts. No trash-talk.",
        "h1": "SnipPrompts vs FlowGPT",
        "subtitle": "Two different ideas of what a prompt library is for. Here's the honest comparison and when each one wins.",
        "short_answer": "FlowGPT is a community marketplace &mdash; tens of thousands of prompts contributed by users across every topic, including roleplay, NSFW, jailbreaks, productivity, and yes, career stuff. SnipPrompts is a focused, curated library &mdash; 172 prompts that pass an editorial bar, with five long-form guides and a paid bundle for job-hunt depth. If you want quantity and discovery, FlowGPT. If you want a smaller library where every prompt has been written and tested for one use case (career), SnipPrompts.",
        "competitor_desc": "FlowGPT (flowgpt.com) is a community-driven prompt marketplace launched in 2022. Anyone can publish, anyone can fork, and the platform leans into the long tail &mdash; the front page surfaces trending prompts across every category from coding to character roleplay. The model is closer to Reddit + Hugging Face than to a curated library. You'll find brilliant prompts and you'll find a lot of low-quality ones; the discovery is the product.",
        "self_desc": "SnipPrompts is a curated library focused on practical work prompts (career being the deepest vertical) and a paid bundle that goes deeper on job-hunting specifically. Every prompt has been written or rewritten by the maintainer, tested against ChatGPT/Claude/Gemini, and structured around three rules: a narrow persona, a refuse-to-invent gate, and a banned-phrase list. 172 prompts, 5 long-form guides, 1 paid bundle.",
        "comparison_rows": "\n          ".join([
            row("Library size", "100K+ prompts", "172 curated prompts"),
            row("Curation model", "Community-contributed, upvote-ranked", "Editorial &mdash; every prompt reviewed and tested"),
            row("Topic breadth", "Everything from coding to roleplay to therapy to NSFW", "Career, communication, creative, business, productivity"),
            row("Job-hunt depth", "Hundreds of resume/interview prompts of varying quality", "5 long-form guides + paid bundle (44 prompts, 8 negotiation scripts, 3 worksheets)"),
            row("Account required", "Yes to save or contribute", "No &mdash; everything is public, no signup"),
            row("Pricing", "Free with paid pro tier ($10/mo)", "Free site + optional $39 one-time bundle"),
            row("Best for discovery", "Yes &mdash; browse, fork, remix", "No &mdash; the library is intentionally small"),
            row("Best for &ldquo;just give me the right prompt&rdquo;", "Slower &mdash; you'll evaluate several before finding one that holds up", "Faster &mdash; one prompt per use case, already tested"),
        ]),
        "when_competitor": "Use FlowGPT when you want to explore prompt patterns across many domains, when you want to see how dozens of writers approach the same problem, or when you're working on a niche use case (a specific game, a specific roleplay, a specific creative format) where curated libraries won't go. FlowGPT is also the right place if you want to publish your own prompts and grow an audience &mdash; SnipPrompts doesn't have that feature and won't.",
        "when_self": "Use SnipPrompts when you want one tested prompt per use case without having to evaluate ten variants. Specifically for job-hunt work: the editorial pass means every resume/cover-letter/interview/negotiation prompt has been written with the same three rules (narrow persona, refuse-to-invent, banned-phrase list) that catch the most common ChatGPT failure modes. If you're job-hunting, the depth here is substantially greater than FlowGPT's career section even though the total prompt count is 100x smaller.",
        "honest_critique": "If you're not job-hunting and not writing communications or business prose, SnipPrompts is a smaller and less useful library than FlowGPT. The career focus is real &mdash; 1/3 of the prompts on the site are job-related, and the paid bundle is entirely career. For a developer looking for code-gen prompts or a writer looking for fiction prompts, FlowGPT's long tail will serve you better. The honest pitch for SnipPrompts is &ldquo;narrow and deep,&rdquo; not &ldquo;everything.&rdquo;",
    },
    {
        "slug": "snipprompts-vs-awesome-chatgpt-prompts",
        "competitor": "awesome-chatgpt-prompts",
        "title": "SnipPrompts vs awesome-chatgpt-prompts &mdash; honest comparison",
        "desc": "Honest side-by-side: what awesome-chatgpt-prompts (the famous GitHub repo) is good for, what it's not, and how SnipPrompts compares for practical career work. No trash-talk.",
        "h1": "SnipPrompts vs awesome-chatgpt-prompts",
        "subtitle": "The most-starred prompt repo on GitHub vs a curated career-focused library. Different tools, different jobs.",
        "short_answer": "awesome-chatgpt-prompts is the canonical GitHub repo (100K+ stars) that popularized the &ldquo;act as a [role]&rdquo; pattern. It's a community-curated reference list of ~200 short persona prompts you can copy and adapt. SnipPrompts is a website with 172 longer, structured prompts focused on practical career and communication work, plus a paid bundle. Use the GitHub repo as a reference for persona patterns; use SnipPrompts when you want a ready-to-run prompt for a specific use case.",
        "competitor_desc": "awesome-chatgpt-prompts (github.com/f/awesome-chatgpt-prompts) is the most-starred prompt repository on GitHub, started in December 2022 by Fatih Kadir Ak&inodot;n. It's a markdown table of ~200 prompts in the format &ldquo;Act as a [role]. I want you to [do task]&rdquo; covering everything from Linux terminal to philosopher to interviewer. It's a reference work &mdash; designed to be copied, adapted, and built on. It's responsible for the &ldquo;act as a [X]&rdquo; convention being everywhere.",
        "self_desc": "SnipPrompts is a curated website (not a GitHub repo) with 172 prompts, each on its own page with worked examples and tested variants. Every prompt is structured around three rules: a narrow persona seed, a refuse-to-invent gate, and a banned-phrase list. Career is the deepest vertical, with 5 long-form guides and a paid bundle. The prompts are typically 5-15x longer than the repo's, because the structure adds verification, examples, and edge-case handling.",
        "comparison_rows": "\n          ".join([
            row("Format", "GitHub markdown table", "Web pages, one prompt per page"),
            row("Prompt count", "~200 short prompts", "172 longer structured prompts"),
            row("Avg prompt length", "1-3 sentences", "10-40 lines, with worked examples"),
            row("Browse experience", "Scroll the README", "Categories, search, dedicated landing pages"),
            row("Reference vs ready-to-use", "Reference patterns to adapt", "Ready-to-run for a specific use case"),
            row("Career-specific depth", "A handful of generic interview/recruiter prompts", "5 guides + 44 paid prompts + 8 negotiation scripts"),
            row("Refuse-to-invent gate", "No &mdash; persona only", "Yes &mdash; standard in every prompt where invention is a risk"),
            row("Updates", "Community PRs", "Editorial updates by maintainer"),
            row("Pricing", "Free (open source, MIT)", "Free site + optional $39 bundle"),
        ]),
        "when_competitor": "Use awesome-chatgpt-prompts when you want to study persona-prompt patterns, when you're building your own prompt library and want a reference of how the canonical &ldquo;act as&rdquo; pattern is structured, or when you have an unusual use case (a specific historical figure, a specific niche profession) and you want a short seed you'll customize. It's also the right resource if you want to contribute &mdash; the repo accepts PRs, SnipPrompts doesn't.",
        "when_self": "Use SnipPrompts when you want a prompt that's already done the customization for you. The awesome-chatgpt-prompts version of &ldquo;act as a recruiter&rdquo; is one sentence; the SnipPrompts version is the same persona + a refuse-to-invent gate + verification questions + a banned-phrase list + worked examples. For practical career work, the second one produces materially better output without requiring you to know what to add. The trade-off is breadth: 172 prompts isn't going to cover every niche the GitHub repo does.",
        "honest_critique": "awesome-chatgpt-prompts has done more to teach the world prompt engineering than any other single resource. SnipPrompts builds on patterns it popularized. If you only need a persona seed and you're confident customizing the rest yourself, the GitHub repo is leaner and free, and you don't need SnipPrompts. The case for SnipPrompts is: most people don't customize, they copy and ship &mdash; and the difference between a seed prompt and a full structured prompt shows up in the output.",
    },
    {
        "slug": "snipprompts-vs-aiprm",
        "competitor": "AIPRM",
        "title": "SnipPrompts vs AIPRM &mdash; honest comparison",
        "desc": "Honest side-by-side: what AIPRM (the Chrome extension prompt library) is good for, what it's not, and how SnipPrompts compares for job-hunt and career prompts. No trash-talk.",
        "h1": "SnipPrompts vs AIPRM",
        "subtitle": "A Chrome-extension prompt library aimed at SEO and marketing pros vs a curated career-focused library. Different audiences, mostly non-overlapping use cases.",
        "short_answer": "AIPRM is a Chrome extension that injects a prompt library into the ChatGPT interface, primarily aimed at SEO and digital-marketing professionals. SnipPrompts is a website you visit, primarily focused on practical career and communication work. If your main job is content marketing or SEO, AIPRM is purpose-built for you. If your main job is anything else (and especially if you're job-hunting), SnipPrompts will fit better.",
        "competitor_desc": "AIPRM (aiprm.com) is a Chrome extension launched in early 2023 that overlays a prompt library directly inside the ChatGPT web interface. The library has thousands of prompts contributed by community members, ranked by usage, and heavily weighted toward SEO, content marketing, e-commerce listings, and ads. Free tier with limits; Pro tiers from $20-$80/month for advanced features (private prompts, team management, prompt analytics).",
        "self_desc": "SnipPrompts is a website (no extension, no overlay) with 172 curated prompts focused on practical work prompts &mdash; career being the deepest vertical, with 5 long-form guides and a paid bundle for job-hunt depth. Every prompt is structured around three rules: a narrow persona seed, a refuse-to-invent gate, and a banned-phrase list. Free site + optional $39 one-time bundle.",
        "comparison_rows": "\n          ".join([
            row("Format", "Chrome extension overlay on ChatGPT", "Standalone website &mdash; copy/paste prompts"),
            row("Library size", "Thousands of community prompts", "172 curated prompts"),
            row("Audience focus", "SEO, content marketing, e-commerce", "Job-hunting, communication, business writing"),
            row("Best vertical", "Content marketing &amp; SEO prompts", "Career &amp; job-hunting prompts"),
            row("Curation", "Community + voting", "Editorial &mdash; every prompt reviewed and tested"),
            row("Browser dependency", "Chrome/Edge required", "Any browser, any device"),
            row("Pricing", "Free tier + $20-$80/mo Pro", "Free site + $39 one-time bundle"),
            row("Privacy", "Extension reads ChatGPT page DOM", "No extension, no tracking beyond standard analytics"),
            row("Best for &ldquo;quick prompt during a ChatGPT session&rdquo;", "Yes &mdash; the overlay is the whole point", "No &mdash; switch tabs to copy a prompt"),
        ]),
        "when_competitor": "Use AIPRM when content marketing or SEO is the core of your work and you want the prompt library inside the ChatGPT interface so you don't break flow. The overlay UX is genuinely better than copy/paste if you're running 50+ prompts a week in ChatGPT. If you're a freelancer doing client SEO/content work, the SEO-specific prompts there are deeper than anything on SnipPrompts &mdash; that's not the vertical SnipPrompts is built for.",
        "when_self": "Use SnipPrompts when your work isn't primarily content marketing. For job-hunting specifically, the depth gap is large &mdash; AIPRM has a handful of generic resume/interview prompts; SnipPrompts has 5 long-form guides, 3 use-case landing pages (new grads, career switchers, laid-off tech), and a paid bundle with 44 prompts and 8 negotiation scripts. Also use SnipPrompts if you don't want a browser extension reading your ChatGPT pages, or if you're on a browser AIPRM doesn't support.",
        "honest_critique": "If you're an SEO or content-marketing professional, AIPRM's library and workflow integration is substantially better than what SnipPrompts offers in those verticals. SnipPrompts has marketing prompts but they're a side category, not the main investment. The honest pitch for SnipPrompts vs AIPRM is: SnipPrompts wins for career work and for users who don't want a browser extension; AIPRM wins for high-volume SEO and content workflows where the overlay UX matters more than the prompt structure.",
    },
]


def main():
    written = []
    for p in PAGES:
        html = TEMPLATE
        for k, v in p.items():
            html = html.replace("@@" + k.upper() + "@@", v.strip() if isinstance(v, str) else v)
        out = REPO / f"{p['slug']}.html"
        out.write_text(html)
        written.append(out.name)
    print("Wrote:", ", ".join(written))


if __name__ == "__main__":
    main()
