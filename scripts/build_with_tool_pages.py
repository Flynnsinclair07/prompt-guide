#!/usr/bin/env python3
"""Generate 5 'with [tool]' landing pages.

Captures tool-branded search: 'how to use Claude for resumes', 'Gemini cover letter prompt', etc.
Same prompts work; framing is tool-specific (where each tool wins vs the others).
"""
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
<meta property="og:type" content="article">
<meta property="og:title" content="@@OG_TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://snipprompts.com/@@SLUG@@.html">
<meta property="og:site_name" content="SnipPrompts">
<meta property="og:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="canonical" href="https://snipprompts.com/@@SLUG@@.html">
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
      <h2>Where @@TOOL_NAME@@ wins</h2>
      <p>@@WHERE_WINS@@</p>
      <ul>
        @@WINS_BULLETS@@
      </ul>
    </section>

    <section>
      <h2>Where @@TOOL_NAME@@ loses to other tools</h2>
      <p>@@WHERE_LOSES@@</p>
    </section>

    <section>
      <h2>The 5 prompts that work best with @@TOOL_NAME@@</h2>
      <p>Every prompt on SnipPrompts is structured around three rules &mdash; a narrow persona seed, a refuse-to-invent gate, and a banned-phrase list. All three travel across tools. The 5 prompts below are the ones that produce the best output specifically with @@TOOL_NAME@@:</p>
      <ol>
        @@PROMPT_LIST@@
      </ol>
    </section>

    <section>
      <h2>One tool-specific tip</h2>
      <p>@@TOOL_TIP@@</p>
    </section>

    <section style="margin-top:32px;padding:24px;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);border:1px solid #6c63ff;border-radius:12px;">
      <h2 style="color:#fff;margin-top:0;">If job hunting is the use case</h2>
      <p style="color:#ccc;">The Job Hunter's AI Bundle is the deeper version of the job-hunt prompts &mdash; 44 prompts, 8 negotiation scripts, 5 modules, 118-page PDF + Notion workspace. All of it works with @@TOOL_NAME@@. $39, 30-day no-questions refund.</p>
      <p style="margin-top:12px;"><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta" onclick="gtag('event','bundle_click',{source:'@@CTA_SOURCE@@'})">Get The Job Hunter's AI Bundle &rarr;</a></p>
    </section>

    <section>
      <h2>Where to start</h2>
      <p>@@WHERE_TO_START@@</p>
    </section>

    <section style="margin-top:40px;padding:28px;background:#1a1a2e;border:1px solid #333;border-radius:12px;text-align:center;">
      <h2 style="color:#fff;font-size:22px;margin-bottom:8px;">One free, tested prompt every week.</h2>
      <p style="color:#aaa;margin-bottom:20px;">Drop your email and I'll send a new prompt every week. Plus two free prompts the day you sign up.</p>
      <script async data-uid="d02eb77674" src="https://promptguide.kit.com/d02eb77674/index.js"></script>
      <p style="color:#999;font-size:12px;margin-top:12px;">No spam. Unsubscribe anytime.</p>
    </section>
  </article>
</main>
<footer>
<p>&copy; 2026 SnipPrompts. AI prompts for every use case.</p>
<p style="margin-top:8px;">
<a href="/about.html" style="color:#999;margin-right:16px;">About</a>
<a href="/privacy.html" style="color:#999;margin-right:16px;">Privacy</a>
<a href="/terms.html" style="color:#999;margin-right:16px;">Terms</a>
<a href="/faq.html" style="color:#999;margin-right:16px;">FAQ</a>
<a href="/resources.html" style="color:#999;margin-right:16px;">Resources</a>
<a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>
</p>
</footer>
</body>
</html>
"""

PROMPT_LIST_DEFAULT = """
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">Writing a Resume</a> &mdash; refuse-to-invent gate keeps the output honest.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">Writing a Cover Letter</a> &mdash; refuse-to-generic gate forces a specific reason.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">Job Interview Prep</a> &mdash; treats the model as mock interviewer, not study guide.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">Salary Negotiation Email</a> &mdash; soft language, specific comp data, fallback offered.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-linkedin-profile.html">LinkedIn Profile</a> &mdash; the 3 sentences a recruiter scans for in 8 seconds.</li>
"""

PAGES = [
    {
        "slug": "with-claude",
        "tool_name": "Claude",
        "title": "How to Use Claude for Job Hunting (Resume, Cover Letter, Interview)",
        "og_title": "How to use Claude for your job hunt",
        "desc": "Free, tested Claude prompts for the job hunt. Where Claude beats ChatGPT for resumes and cover letters, the 5 prompts that work best with Claude specifically, and one Claude-only tip that materially improves output.",
        "h1": "How to use Claude for your job hunt",
        "subtitle": "Claude is the model I personally use for writing-heavy job-hunt work. Here's where it beats ChatGPT, where it doesn't, and the 5 prompts that produce the best output with Claude specifically.",
        "short_answer": "Claude (Anthropic's model) is generally the strongest writing model in 2026 for structured, long-context tasks &mdash; which describes most of the job hunt. It's better than ChatGPT free at refusing to invent, better at following long structured prompts without drifting, and better at long-context tasks (turning a 5-page job description into specific resume bullets). Where it loses: image generation, web browsing on the free tier, and any task where you want the model to be more creative/aggressive than careful.",
        "where_wins": "Claude wins on the parts of the job hunt that matter most:",
        "wins_bullets": """
        <li><strong>Refusing to invent.</strong> Claude's default is more conservative than ChatGPT's, which matters enormously for resume bullets. When you tell Claude &ldquo;don't add metrics I haven't given you,&rdquo; it actually doesn't.</li>
        <li><strong>Following long structured prompts.</strong> The 30-line prompts on SnipPrompts (with persona, constraints, banned phrases, and example outputs) work better in Claude than in ChatGPT free &mdash; ChatGPT free will sometimes ignore the back half.</li>
        <li><strong>Long context.</strong> Pasting a 5-page job description plus your full 3-page resume plus your LinkedIn About section in one prompt works in Claude Pro (200K context) better than ChatGPT free (32K).</li>
        <li><strong>Honest critique.</strong> Asking Claude to critique your cover letter draft produces sharper, more useful criticism than ChatGPT, which tends toward encouraging language.</li>
        <li><strong>Refusing to write generic content when constraint is in the prompt.</strong> Claude respects the &ldquo;refuse to write the cover letter unless I give you one specific real reason&rdquo; constraint; ChatGPT will sometimes produce a generic letter anyway with a disclaimer.</li>
        """,
        "where_loses": "Claude loses to other tools in a few spots. ChatGPT is better for image generation (DALL-E integration, no equivalent in Claude). ChatGPT Plus is better if you need web browsing on the free tier (Claude requires Pro for web search). Gemini is better integrated into Gmail and Docs if you're already in Google Workspace. Perplexity is purpose-built for live information lookup and is better at &ldquo;what's the median salary for [role] in [city]&rdquo;-style queries with cited sources. None of these matter for the resume/cover-letter/interview workflow &mdash; Claude wins there &mdash; but they matter for adjacent tasks.",
        "prompt_list": PROMPT_LIST_DEFAULT,
        "tool_tip": "Claude-specific tip: when you paste a structured prompt into Claude, end the prompt with the literal phrase <em>&ldquo;before you write, confirm you understand the constraints by repeating them back in one sentence.&rdquo;</em> Claude does this; ChatGPT often skips it. The confirmation step catches misread instructions before you waste a 2,000-word response on the wrong output. Single highest-ROI Claude-specific habit.",
        "cta_source": "landing_with_claude",
        "where_to_start": "Open Claude (claude.ai &mdash; free tier is enough for most job-hunt prompts). Start with the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> on a real bullet that's currently vague. Note how the refuse-to-invent gate actually fires in Claude (it asks you for verification before writing). Then run the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">cover letter prompt</a> on your next application with one specific real reason as input. If you can tell the difference vs the ChatGPT output you've been getting, the model fit is real.",
    },
    {
        "slug": "with-gemini",
        "tool_name": "Gemini",
        "title": "How to Use Gemini for Job Hunting (Resume, Cover Letter, Interview)",
        "og_title": "How to use Gemini for your job hunt",
        "desc": "Free, tested Gemini prompts for the job hunt. Where Gemini wins (Gmail / Docs integration) and where it loses, the 5 prompts that work best with Gemini, and one Gemini-only tip for outreach emails.",
        "h1": "How to use Gemini for your job hunt",
        "subtitle": "Gemini (Google's model) is the right choice if you're already living in Google Workspace. Here's where it wins, where it loses to ChatGPT and Claude, and the 5 prompts that produce the best output with Gemini specifically.",
        "short_answer": "Gemini is best when your workflow is already in Gmail and Google Docs &mdash; it integrates with both natively, which is genuinely useful for outreach drafts and resume editing inside Docs. The model itself (Gemini 2.0) is competitive with ChatGPT for most tasks and slightly behind Claude on long structured prompts. If you don't use Google Workspace heavily, the integration advantage doesn't matter and Claude/ChatGPT are easier.",
        "where_wins": "Gemini wins on the integration, not the model itself:",
        "wins_bullets": """
        <li><strong>Gmail integration.</strong> Drafting cold outreach, networking emails, and follow-ups inside Gmail's compose window with Gemini is materially faster than copy-pasting between ChatGPT and Gmail. For job-hunt outreach specifically, this is the killer feature.</li>
        <li><strong>Google Docs integration.</strong> Editing your resume in Docs with Gemini's side-panel suggestions is faster than the ChatGPT-then-copy-back workflow. The refuse-to-invent prompt structure still works.</li>
        <li><strong>Free tier is generous.</strong> Gemini's free tier handles most job-hunt prompts without hitting limits, including longer documents.</li>
        <li><strong>Image-aware resume review.</strong> Gemini can look at a screenshot of your formatted resume (not just the text) and flag layout issues that text-only models can't see.</li>
        <li><strong>Calendar integration for interview prep.</strong> When you ask Gemini to prep you for an interview, it can see your upcoming calendar events. Niche but useful.</li>
        """,
        "where_loses": "Gemini loses to Claude on long structured prompts &mdash; the 30-line prompts on SnipPrompts (with persona, constraints, banned phrases) work but Gemini occasionally drops the banned-phrase constraint in long outputs. ChatGPT Plus is generally more reliable for cover letters where the &ldquo;refuse to write generic&rdquo; constraint is doing the work; Gemini sometimes writes a generic version anyway. If you're not in Google Workspace, the integration advantage disappears and the model alone isn't compelling.",
        "prompt_list": PROMPT_LIST_DEFAULT,
        "tool_tip": "Gemini-specific tip: for cold outreach emails (networking, recruiter follow-ups), open Gmail compose first, then trigger Gemini from inside compose. The drafts come out shorter and more in-Gmail-tone than if you ask Gemini in the chat interface and paste back. Material difference in reply rate when the email reads as written-in-Gmail vs. obviously-pasted-from-AI.",
        "cta_source": "landing_with_gemini",
        "where_to_start": "Open Gemini (gemini.google.com &mdash; free tier is enough). Start with the <a href=\"/prompts/best-chatgpt-prompt-for-networking-email.html\">networking email prompt</a> &mdash; Gemini's Gmail integration is where it most clearly beats ChatGPT, and outreach is high-leverage. Then try the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> inside Google Docs with Gemini's side-panel. If the Workspace integration feels useful, you're in the right tool; if it doesn't, Claude is the better pick.",
    },
    {
        "slug": "with-gpt-4o",
        "tool_name": "GPT-4o (ChatGPT)",
        "title": "How to Use GPT-4o (ChatGPT) for Job Hunting",
        "og_title": "How to use GPT-4o for your job hunt",
        "desc": "Free, tested GPT-4o (ChatGPT) prompts for the job hunt. Where GPT-4o wins (versatility, image gen, browsing), where it loses to Claude, and the 5 prompts that produce the best output with GPT-4o specifically.",
        "h1": "How to use GPT-4o (ChatGPT) for your job hunt",
        "subtitle": "GPT-4o is the default for most job-hunters &mdash; it's free, fast, and broadly capable. Here's where it wins, where Claude or Gemini beats it, and the 5 prompts that produce the best output with GPT-4o specifically.",
        "short_answer": "GPT-4o (OpenAI's flagship, free on chatgpt.com) is the strongest all-around tool for job hunting if you're using only one. It's fast, has the largest plugin/integration ecosystem, handles images and audio natively, and works well with the structured prompts on SnipPrompts. Where it loses: it'll occasionally drop refuse-to-invent constraints (Claude is stricter), and the free tier has tighter context limits than Claude free.",
        "where_wins": "GPT-4o wins on versatility and ecosystem:",
        "wins_bullets": """
        <li><strong>Default familiarity.</strong> Every job-hunt prompt on SnipPrompts was written for and tested in ChatGPT. They work in other tools too but they were tuned here first.</li>
        <li><strong>Native image and audio.</strong> Upload a screenshot of your resume and ask &ldquo;what would a recruiter notice first?&rdquo; Read an interview practice answer out loud and have ChatGPT critique your delivery. Neither works in Claude free.</li>
        <li><strong>DALL-E integration.</strong> If you need a LinkedIn banner, headshot replacement, or any branded image for your job-hunt presence, ChatGPT generates them inline. No equivalent in Claude.</li>
        <li><strong>Browsing on Plus tier.</strong> &ldquo;Look up the most recent press releases from [company]&rdquo; works on ChatGPT Plus; useful for cover letter research.</li>
        <li><strong>Custom GPTs.</strong> Plus subscribers can save a configured GPT (e.g., &ldquo;Resume Coach with the refuse-to-invent gate built in&rdquo;) and reuse it without re-pasting the prompt every time.</li>
        """,
        "where_loses": "GPT-4o loses to Claude on refuse-to-invent strictness &mdash; ChatGPT will occasionally add a metric or detail you didn't provide, even with the gate in the prompt. For high-stakes resume work this matters; for lower-stakes work it doesn't. Gemini wins on Gmail integration for outreach. Free-tier context limits are tighter than Claude free, so pasting a 5-page job description + full resume in one prompt sometimes hits limits.",
        "prompt_list": PROMPT_LIST_DEFAULT,
        "tool_tip": "GPT-4o-specific tip: for high-stakes resume work where you can't afford the model to invent a number, add this line to the prompt: <em>&ldquo;after writing each bullet, list any metric, tool name, role title, or outcome that came from your knowledge rather than my input. If any did, rewrite the bullet without it.&rdquo;</em> This adds 10 seconds to the response and catches the rare ChatGPT fabrication that the standard gate misses.",
        "cta_source": "landing_with_gpt_4o",
        "where_to_start": "Open ChatGPT (chat.openai.com &mdash; free tier works). If you have ChatGPT Plus, save the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> as a Custom GPT so you can reuse it. Run it on your current resume. Then the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">cover letter prompt</a> on your next application. ChatGPT is the tool the prompts were tuned in, so the output match is closest here.",
    },
    {
        "slug": "with-perplexity",
        "tool_name": "Perplexity",
        "title": "How to Use Perplexity for Job Hunting (Comp Research, Company Research)",
        "og_title": "How to use Perplexity for your job hunt",
        "desc": "Perplexity isn't the right tool for writing your resume &mdash; but it's the best tool for the research that goes into the resume. Comp data with citations, company research, interview prep on real recent news. Here's where Perplexity wins in the job hunt.",
        "h1": "How to use Perplexity for your job hunt",
        "subtitle": "Perplexity isn't the right tool for writing your resume. It's the right tool for the research that goes into it &mdash; comp data, company news, interview prep on actual recent events. Use it alongside ChatGPT or Claude, not instead of them.",
        "short_answer": "Perplexity is a search-first AI: it answers questions with cited sources rather than free-form writing. That makes it the wrong tool for drafting a resume or cover letter, and the right tool for the research that goes into them &mdash; comp data, company news, hiring manager backgrounds, recent product launches you can reference in a cover letter. The fastest workflow: Perplexity for research, ChatGPT or Claude for writing.",
        "where_wins": "Perplexity wins on the research layer of the job hunt:",
        "wins_bullets": """
        <li><strong>Comp research with citations.</strong> &ldquo;What's the 50th percentile total comp for a senior backend engineer at a Series B startup in Boulder?&rdquo; returns numbers + Levels.fyi / Glassdoor / Blind sources you can click through. Faster than checking each site individually.</li>
        <li><strong>Company research for cover letters.</strong> &ldquo;What has [company] shipped in the last 90 days that's been publicly discussed?&rdquo; gives you the specific recent thing to reference in your cover letter &mdash; the exact thing the refuse-to-generic prompt requires.</li>
        <li><strong>Hiring manager research.</strong> &ldquo;What has [hiring manager name] published or spoken about recently?&rdquo; surfaces talks, podcasts, and posts you can reference in outreach without it being weird.</li>
        <li><strong>Interview prep on current events.</strong> &ldquo;What's happening in [industry] this quarter that an interviewer might ask about?&rdquo; works much better in Perplexity than in models without web access.</li>
        <li><strong>Cited answers reduce fabrication risk.</strong> Because Perplexity shows sources, you can verify any number before quoting it in a salary negotiation or cover letter. Lower risk than asking ChatGPT to estimate.</li>
        """,
        "where_loses": "Perplexity loses on writing. Don't use it to draft a resume, cover letter, or interview answer &mdash; the output reads as written-by-a-search-engine because that's what it is. Don't use it as your only AI tool; use it for the research and switch to Claude or ChatGPT for the writing.",
        "prompt_list": """
        <li>Use Perplexity for: comp research before negotiation, company research before a cover letter, hiring manager research before outreach.</li>
        <li>Then switch to Claude or ChatGPT for: <a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">writing the resume</a>, <a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">writing the cover letter</a>, <a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">running the mock interview</a>, <a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">writing the negotiation email</a>, and <a href="/prompts/best-chatgpt-prompt-for-networking-email.html">drafting outreach</a> &mdash; using the research Perplexity surfaced as input.</li>
        """,
        "tool_tip": "Perplexity-specific tip: when researching comp, run the same query 3 different ways (&ldquo;senior backend engineer Boulder comp,&rdquo; &ldquo;Series B startup engineer comp Colorado,&rdquo; &ldquo;remote-eligible senior engineer total compensation 2026&rdquo;) and triangulate across all three. Single-query Perplexity answers can anchor on outdated or unrepresentative sources; three queries usually surface the convergent number plus the outliers.",
        "cta_source": "landing_with_perplexity",
        "where_to_start": "Open Perplexity (perplexity.ai &mdash; free tier is enough). Run one query: &ldquo;What is the 50th-75th percentile total comp for [your target role] at [target company size] in [your location]?&rdquo; Then open Claude or ChatGPT in another tab with the <a href=\"/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html\">salary negotiation prompt</a> and feed it the comp data you just verified. This two-tool workflow is the highest-ROI use of Perplexity in the job hunt.",
    },
    {
        "slug": "with-copilot",
        "tool_name": "Microsoft Copilot",
        "title": "How to Use Microsoft Copilot for Job Hunting",
        "og_title": "How to use Copilot for your job hunt",
        "desc": "Microsoft Copilot for the job hunt &mdash; where it wins (Word integration, free in Edge, Office 365 sync), where it loses to ChatGPT and Claude, and the 5 prompts that work best with Copilot specifically.",
        "h1": "How to use Microsoft Copilot for your job hunt",
        "subtitle": "Copilot (Microsoft's GPT-4 wrapper, free on copilot.microsoft.com) is the right pick if you're editing your resume in Word or living in Office 365. Here's where it wins, where it loses, and the 5 prompts that work best with Copilot.",
        "short_answer": "Microsoft Copilot is GPT-4 with Microsoft's UX wrapper plus deep Office 365 integration. As a model it's very close to ChatGPT (it IS GPT-4 under the hood for most surfaces). The reason to choose Copilot specifically: you're editing your resume in Word, your cover letter in Outlook, and you want the AI to live where the document lives. If you're not in Office 365, ChatGPT directly is simpler.",
        "where_wins": "Copilot wins on Microsoft Office integration:",
        "wins_bullets": """
        <li><strong>Word integration for resume editing.</strong> Selecting a bullet in Word and asking Copilot to rewrite it (with the refuse-to-invent constraint in the prompt) is faster than copy-pasting between Word and ChatGPT.</li>
        <li><strong>Outlook integration for outreach.</strong> Drafting cold outreach emails or follow-ups directly in Outlook with Copilot pulled in is fast, and the tone comes out as &ldquo;written in Outlook&rdquo; rather than &ldquo;pasted from a chatbot.&rdquo;</li>
        <li><strong>Edge browser integration.</strong> Reading a job description in Edge and triggering Copilot to summarize key keywords, required skills, and red flags works inline. No tab-switching.</li>
        <li><strong>Free GPT-4 access.</strong> Microsoft Copilot uses GPT-4 (or a variant) on the free tier, where ChatGPT free uses GPT-3.5 or 4o-mini for most prompts. Worth noting if you're not paying for ChatGPT Plus.</li>
        <li><strong>Enterprise privacy if you're using a work account.</strong> Copilot for Business (Microsoft 365 Copilot) doesn't train on your inputs by default. Useful if you're job-hunting on the side and want to use AI for your resume without it ending up in a training corpus.</li>
        """,
        "where_loses": "Copilot loses to Claude on refuse-to-invent strictness for the same reasons ChatGPT does. Loses to ChatGPT directly on familiar UX and Custom GPTs (Copilot doesn't have an equivalent of saved custom configurations). Loses to Gemini if you're in Google Workspace instead of Office 365. Loses to Perplexity for research with citations.",
        "prompt_list": PROMPT_LIST_DEFAULT,
        "tool_tip": "Copilot-specific tip: when you're editing your resume in Word, don't paste the entire prompt into a chat window. Instead, select the specific bullet you want rewritten and trigger Copilot from the right-click menu. The prompt context is shorter, the rewrite is more focused, and Copilot keeps the formatting (font, spacing, bullet style) that pasting back from a chat window strips.",
        "cta_source": "landing_with_copilot",
        "where_to_start": "Open your resume in Word, install/enable Copilot if you haven't (free on Microsoft 365 personal, paid on enterprise). Select a weak bullet, ask Copilot to rewrite using the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> structure. Then open Outlook and use the <a href=\"/prompts/best-chatgpt-prompt-for-networking-email.html\">networking email prompt</a> in compose. If the Office integration meaningfully speeds up your workflow, you're in the right tool; if you're not editing in Word, ChatGPT directly is simpler.",
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
    print(f"Wrote {len(written)} pages:")
    for w in written:
        print(f"  {w}")


if __name__ == "__main__":
    main()
