#!/usr/bin/env python3
"""Generate 10 new SEO prompt pages in underrepresented categories.

Categories filled:
  - Tech/coding (4): regex, git-commit-message, api-documentation, technical-interview-prep
  - Marketing/ads (2): google-ads-copy, facebook-ad-copy
  - B2B sales (3): cold-dm-linkedin, discovery-call-questions, lost-deal-postmortem
  - Health (1): doctor-appointment-prep
"""
import json
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
PROMPTS_DIR = REPO / "prompts"

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
<title>@@PAGE_TITLE@@ | SnipPrompts</title>
<meta name="description" content="@@DESC@@">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<link rel="icon" type="image/png" sizes="16x16" href="/favicon-16x16.png">
<link rel="apple-touch-icon" sizes="180x180" href="/apple-touch-icon.png">
<link rel="stylesheet" href="/style.css">
<meta property="og:type" content="article">
<meta property="og:title" content="@@PAGE_TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://snipprompts.com/prompts/@@SLUG@@.html">
<meta property="og:site_name" content="SnipPrompts">
<meta property="og:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="@@PAGE_TITLE@@">
<meta name="twitter:description" content="@@DESC@@">
<link rel="canonical" href="https://snipprompts.com/prompts/@@SLUG@@.html">
<script type="application/ld+json">@@SCHEMA@@</script>
</head>
<body>
<nav>
  <a href="/" class="logo">SnipPrompts</a>
  <a href="/categories.html">All Prompts</a>
</nav>
<main>
  <article>
    <h1>@@PAGE_TITLE@@</h1>
    <p class="subtitle">@@SUBTITLE@@</p>

    <div class="prompt-box">
      <div class="prompt-header">
        <span>The Prompt</span>
        <button onclick="copyPrompt(this)">Copy</button>
      </div>
      <pre class="prompt-text">@@PROMPT@@</pre>
    </div>

    <section>
      <h2>How to Use This Prompt</h2>
      <ol>
        @@HOW_TO_STEPS@@
      </ol>
      <p>@@HOW_TO_NOTE@@</p>
    </section>

    <section>
      <h2>Example Output</h2>
      <div class="example-box">
        <p><strong>Task:</strong> @@EXAMPLE_TASK@@</p>
        <p><strong>Response:</strong></p>
        <pre style="color:#ccc;font-size:13px;">@@EXAMPLE_OUTPUT@@</pre>
      </div>
    </section>

    <section>
      <h2>Tips to Get Better Results</h2>
      <ul>
        @@TIPS@@
      </ul>
    </section>

    <section class="tools-section">
      <h2>Best AI Tools for This</h2>
      <a href="https://chat.openai.com" target="_blank" rel="noopener">ChatGPT</a>
      <a href="https://www.amazon.com/gp/search?ie=UTF8&tag=promptguide0a-20&linkCode=ur2&camp=1789&creative=9325&index=books&keywords=AI+productivity+tools" target="_blank" rel="noopener">AI Books on Amazon</a>
      <a href="https://claude.ai" target="_blank" rel="noopener">Claude</a>
    </section>

    <section>
      <h2>Related Prompts</h2>
      <div class="related">
        <a href="/prompts/@@RELATED_1@@.html">@@RELATED_1_NAME@@</a>
        <a href="/prompts/@@RELATED_2@@.html">@@RELATED_2_NAME@@</a>
      </div>
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
<script>
function copyPrompt(btn) {
  const text = btn.parentElement.nextElementSibling.textContent;
  navigator.clipboard.writeText(text).then(() => {
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = 'Copy', 2000);
  });
}
</script>
</body>
</html>
"""


def build_schema(title, desc, slug):
    return json.dumps([
        {
            "@context": "https://schema.org",
            "@type": "HowTo",
            "name": title,
            "description": desc,
            "url": f"https://snipprompts.com/prompts/{slug}.html",
            "totalTime": "PT2M",
            "supply": [{"@type": "HowToSupply", "name": "ChatGPT or Claude account"}],
            "tool": [{"@type": "HowToTool", "name": "AI chatbot"}],
            "step": [
                {"@type": "HowToStep", "position": 1, "name": "Copy the prompt", "text": "Click the copy button to grab the full prompt template."},
                {"@type": "HowToStep", "position": 2, "name": "Fill in your details", "text": "Replace everything in [BRACKETS] with your specific information."},
                {"@type": "HowToStep", "position": 3, "name": "Paste into your AI", "text": "Paste the filled-in prompt into ChatGPT or Claude and hit enter."},
                {"@type": "HowToStep", "position": 4, "name": "Iterate the result", "text": "Review the output and ask follow-up questions to refine it."},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "FAQPage",
            "mainEntity": [
                {"@type": "Question", "name": "Is this prompt free to use?", "acceptedAnswer": {"@type": "Answer", "text": "Yes — every prompt on SnipPrompts is free to copy and use with ChatGPT, Claude, or any AI assistant. No account required."}},
                {"@type": "Question", "name": "Does this work with ChatGPT and Claude?", "acceptedAnswer": {"@type": "Answer", "text": "Yes, this prompt works with ChatGPT (free and paid plans), Claude, Gemini, and most other AI chatbots. Just paste it in and fill in your details."}},
                {"@type": "Question", "name": "How do I get better results from this prompt?", "acceptedAnswer": {"@type": "Answer", "text": "Be specific when filling in the brackets. Generic input produces generic output. Include real details, numbers, and context. Follow up with 'make it shorter' or 'try a different angle' to iterate."}},
            ],
        },
        {
            "@context": "https://schema.org",
            "@type": "BreadcrumbList",
            "itemListElement": [
                {"@type": "ListItem", "position": 1, "name": "SnipPrompts", "item": "https://snipprompts.com/"},
                {"@type": "ListItem", "position": 2, "name": "Prompts", "item": "https://snipprompts.com/categories.html"},
                {"@type": "ListItem", "position": 3, "name": title, "item": f"https://snipprompts.com/prompts/{slug}.html"},
            ],
        },
    ])


PROMPTS = [
    {
        "slug": "best-chatgpt-prompt-for-regex",
        "page_title": "Best ChatGPT Prompt for Regex",
        "desc": "The best AI prompt for writing and explaining regular expressions. Works for Python, JavaScript, grep, sed, and any flavor of regex.",
        "subtitle": "Write the regex you need, understand the one you have, and stop guessing at character classes.",
        "prompt": """You are a senior engineer who has written regular expressions in production for 15 years across Python, JavaScript, Go, grep, and sed. Help me with a regex task.

Regex flavor: [PCRE / JavaScript / Python re / Go / POSIX / grep / etc.]
What I'm trying to match: [DESCRIBE IN PLAIN ENGLISH — be specific about what counts and what doesn't]
Sample inputs that SHOULD match:
[PASTE 3-5 EXAMPLES]
Sample inputs that should NOT match:
[PASTE 3-5 EXAMPLES — the edge cases that trip up bad regex]

Requirements:
- Give me the regex pattern, in the exact flavor I specified
- Walk through it character-by-character so I understand what each piece does
- Show me the gotchas (greedy vs lazy, anchoring, escaping in this flavor)
- If a non-regex approach (string methods, parser) would be safer, say so first
- If my requirement is ambiguous, ASK before guessing — don't write a regex that almost works""",
        "how_to_steps": [
            "Copy the prompt and specify your regex flavor",
            "Always paste 3-5 should-match AND 3-5 should-NOT-match examples — without negatives the regex will overmatch",
            "Describe the rule in plain English first (&ldquo;US phone numbers with optional country code&rdquo;), not regex shorthand",
            "Paste into ChatGPT or Claude",
            "Test the regex against ALL your examples before shipping &mdash; regex bugs hide in the cases you didn't think of",
        ],
        "how_to_note": "The single biggest mistake people make is giving only positive examples. The model will write a regex that matches those but also matches a lot you didn't intend. Always include the things that should NOT match.",
        "example_task": "Match US phone numbers with optional country code and parentheses",
        "example_output": """Pattern (PCRE / Python re):
^(?:\\+?1[-. ]?)?\\(?([0-9]{3})\\)?[-. ]?([0-9]{3})[-. ]?([0-9]{4})$

Walkthrough:
  ^                   Anchor: start of string
  (?:\\+?1[-. ]?)?     Optional country code: +1, 1, +1-, 1., etc.
  \\(?                 Optional opening paren
  ([0-9]{3})          Capture group 1: area code
  \\)?                 Optional closing paren
  [-. ]?              Optional separator: -, ., space
  ([0-9]{3})          Capture group 2: prefix
  [-. ]?              Optional separator
  ([0-9]{4})          Capture group 3: line number
  $                   Anchor: end of string

Gotcha: if your input is multiline and you want to match per-line, use re.MULTILINE
and ^ / $ will anchor to line boundaries.""",
        "tips": [
            "<strong>Test against the negatives first.</strong> Run the regex on your should-NOT-match examples. If any match, the regex is wrong &mdash; even if all the should-match cases pass.",
            "<strong>Specify the flavor.</strong> JavaScript regex doesn't support lookbehinds the same way Python does. Python's re is different from PCRE. Tell the model which one.",
            "<strong>Ask for a non-regex alternative.</strong> For HTML, JSON, and CSV, regex is the wrong tool &mdash; use a parser. A good prompt response will say so.",
            "<strong>Iterate with new edge cases.</strong> After it gives you a pattern, throw a weird input at it (&ldquo;what about an extension like x1234?&rdquo;) and ask it to handle.",
        ],
        "related_1": "best-chatgpt-prompt-for-coding",
        "related_1_name": "Best Prompt for Coding",
        "related_2": "best-chatgpt-prompt-for-python-code",
        "related_2_name": "Best Prompt for Python Code",
    },
    {
        "slug": "best-chatgpt-prompt-for-git-commit-message",
        "page_title": "Best ChatGPT Prompt for Git Commit Messages",
        "desc": "Write clear, conventional Git commit messages from your diff. Stops you shipping &ldquo;fix stuff&rdquo; commits.",
        "subtitle": "Paste the diff, get a commit message in the convention your team actually uses.",
        "prompt": """You are a senior engineer who has reviewed thousands of pull requests. Write a Git commit message for this change.

Convention to follow: [Conventional Commits / Angular / team-custom / just plain English]
Repo context (one sentence): [WHAT THE PROJECT IS, e.g. &ldquo;a Next.js marketing site&rdquo;]
The diff:
```
[PASTE git diff OR PATCH HERE]
```
What I was actually trying to do (in my own words): [ONE OR TWO SENTENCES]
Related ticket / issue (if any): [ID or URL]

Requirements:
- Subject line: imperative mood, under 72 characters, no trailing period
- If using Conventional Commits, pick the right type (feat / fix / refactor / docs / chore / test / perf / build / ci / style)
- Body (if needed): explain WHY, not WHAT &mdash; the diff already shows what changed
- If the change is split across concerns (e.g. a refactor + a bug fix), call that out and suggest splitting the commit
- If the diff and my description disagree, ASK before writing &mdash; don't paper over a mismatch""",
        "how_to_steps": [
            "Run <code>git diff --staged</code> (or <code>git diff HEAD~1</code>) and paste the output",
            "Tell the model the convention &mdash; Conventional Commits is the most common but say what your team uses",
            "Describe what you were trying to do in plain English &mdash; the diff alone doesn't tell the model the why",
            "Paste into ChatGPT or Claude",
            "Review the message before committing &mdash; the model can mis-read intent if the diff is large",
        ],
        "how_to_note": "If the diff is over ~300 lines, the commit probably should be split. A good prompt response will tell you that instead of writing one giant message.",
        "example_task": "Commit message for a fix that adds null-check to a user lookup",
        "example_output": """fix(auth): handle null user in session lookup

The session lookup was crashing when a user was deleted mid-session
because we assumed `users.findById` always returned an object. It can
return null when the row is gone. Caller now handles the null case
and clears the session instead.

Refs #4821""",
        "tips": [
            "<strong>Stage first, then diff.</strong> <code>git diff --staged</code> gives the model exactly what's going into the commit. <code>git diff</code> shows unstaged work too.",
            "<strong>Don't paste 1,000-line diffs.</strong> If the diff is huge, the commit should be split. Ask the model &ldquo;should this be one commit or multiple?&rdquo;",
            "<strong>The WHY is the whole point.</strong> &ldquo;Updated user.ts&rdquo; is useless. &ldquo;Handle null user in session lookup because deleted users were crashing the session middleware&rdquo; tells the next reader (or future you) what they need.",
            "<strong>Iterate on tone.</strong> If your team writes terse commits, say &ldquo;keep it to one line, no body.&rdquo; If your team writes essays, say so.",
        ],
        "related_1": "best-chatgpt-prompt-for-coding",
        "related_1_name": "Best Prompt for Coding",
        "related_2": "best-chatgpt-prompt-for-standup-update",
        "related_2_name": "Best Prompt for Standup Updates",
    },
    {
        "slug": "best-chatgpt-prompt-for-api-documentation",
        "page_title": "Best ChatGPT Prompt for API Documentation",
        "desc": "Generate clean, accurate API documentation from your code. Covers endpoints, request/response shapes, errors, and examples.",
        "subtitle": "Turn your route handlers into docs developers actually read.",
        "prompt": """You are a senior technical writer who has documented APIs at scale (think Stripe, Twilio quality). Generate documentation for this endpoint.

Documentation style: [OpenAPI / Stripe-style narrative / README-style / Postman / team-custom]
Language / framework: [Python+FastAPI / Node+Express / Go / Ruby+Rails / etc.]
The endpoint code:
```
[PASTE THE HANDLER + ROUTE DEFINITION + ANY MIDDLEWARE THAT MATTERS]
```
The data model (if relevant):
```
[PASTE THE SCHEMA / DATACLASS / STRUCT]
```
Who's reading this doc: [internal devs / external developers / partner integrators]
Auth model: [API key / OAuth / JWT / cookie / none]

Requirements:
- Document: HTTP method, path, auth required, request params/body, response shape, status codes
- For EVERY error status (4xx, 5xx) the endpoint can return, explain when it fires and what the developer should do
- Include at least one working example: curl request + sample response
- If you can infer rate limits or idempotency behavior from the code, note them
- If a piece of the behavior isn't clear from the code (silent fallbacks, edge cases), FLAG it instead of guessing&mdash;ask me to confirm""",
        "how_to_steps": [
            "Paste the route handler AND the schema/model it uses &mdash; without the schema the docs will be vague",
            "Specify the doc style &mdash; OpenAPI is structured, Stripe-style is narrative; the output is very different",
            "Tell the model who the reader is &mdash; internal developer docs and external partner docs have different tone",
            "Paste into ChatGPT or Claude",
            "Read the &ldquo;FLAG&rdquo; section carefully &mdash; those are the questions you need to answer before the docs ship",
        ],
        "how_to_note": "The model will sometimes hallucinate error codes the endpoint doesn't actually return. After generation, grep your handler for every <code>raise</code> / <code>throw</code> / <code>return Response(status=</code> and verify the doc lists exactly those.",
        "example_task": "Document a POST /users/:id/refund endpoint that triggers an async refund",
        "example_output": """POST /users/:id/refund
Refund a charge for a specific user.

Auth: API key (Bearer token)

Path params:
  id (string, required) &mdash; the user's UUID

Request body (application/json):
  {
    "charge_id": "ch_xxx",   // required
    "amount":    1500,        // optional, defaults to full charge; in cents
    "reason":    "duplicate"  // optional: duplicate | fraudulent | requested_by_customer
  }

Responses:
  202 Accepted &mdash; refund queued; returns { "refund_id": "rf_xxx", "status": "pending" }
  400 Bad Request &mdash; charge_id missing, or amount > charge total
  402 Payment Required &mdash; original payment method no longer available
  404 Not Found &mdash; user or charge not found, or charge doesn't belong to user
  409 Conflict &mdash; charge already fully refunded
  429 Too Many Requests &mdash; more than 30 refund requests per minute per API key

Example:
  curl -X POST https://api.example.com/users/usr_123/refund \\
    -H "Authorization: Bearer sk_live_xxx" \\
    -d '{"charge_id": "ch_abc", "amount": 500, "reason": "duplicate"}'""",
        "tips": [
            "<strong>Document errors developers can actually fix.</strong> &ldquo;500 internal error&rdquo; tells the integrator nothing. &ldquo;500 if the upstream payment processor times out &mdash; retry with exponential backoff&rdquo; tells them what to do.",
            "<strong>Include a working example.</strong> Not pseudocode &mdash; a real curl command they can copy and run. Tested examples are the highest-trust signal docs can give.",
            "<strong>Cover the unhappy path.</strong> Most API docs document the happy path well and the error responses poorly. The error path is where integrators get stuck and write support tickets.",
            "<strong>Verify after generation.</strong> The model will occasionally invent status codes. Grep your handler for actual return statements and reconcile.",
        ],
        "related_1": "best-chatgpt-prompt-for-coding",
        "related_1_name": "Best Prompt for Coding",
        "related_2": "best-chatgpt-prompt-for-white-paper",
        "related_2_name": "Best Prompt for White Papers",
    },
    {
        "slug": "best-chatgpt-prompt-for-technical-interview-prep",
        "page_title": "Best ChatGPT Prompt for Technical Interview Prep",
        "desc": "Prep for technical interviews (coding, system design, behavioral) with a senior engineer who's actually conducted them. Practice with feedback, not just answers.",
        "subtitle": "For coding rounds, system design, and the behavioral round most engineers underprepare for.",
        "prompt": """You are a senior engineer who has conducted 300+ technical interviews at FAANG-tier and Series-B companies. Help me prep for an upcoming interview.

Company: [COMPANY NAME or type — e.g. &ldquo;mid-stage B2B SaaS&rdquo;]
Role: [Senior backend engineer / Staff infra / EM / etc.]
Round type: [coding / system design / behavioral / take-home / live debugging / leadership]
My background (one paragraph): [LANGUAGES, YEARS, RECENT PROJECTS]
What I'm worried about: [SPECIFIC WEAKNESS &mdash; dynamic programming, distributed systems, leading without authority, etc.]
Time I have to prep: [DAYS / HOURS]

Requirements:
- Treat this as an actual interview, not a lecture
- For coding: give me a problem at the right difficulty, wait for my solution, then critique it the way an interviewer would (not just &ldquo;here's the answer&rdquo;)
- For system design: ask the clarifying questions a strong candidate would ask, then push back on my answer the way a strong interviewer would
- For behavioral: ask the actual question, let me answer, then tell me what would have scored higher and why
- Focus on the SPECIFIC weakness I named &mdash; don't drift into general advice
- If my answer is good, say so plainly; don't pad with &ldquo;great answer!&rdquo; if it wasn't""",
        "how_to_steps": [
            "Pick the round type you're worried about &mdash; don't try to prep all four in one session",
            "Be specific about your background &mdash; the model will calibrate the difficulty",
            "Name the specific weakness &mdash; &ldquo;I always over-explain in system design&rdquo; gets better feedback than &ldquo;system design&rdquo;",
            "Paste into ChatGPT or Claude &mdash; treat it as a live interview, not a Q&amp;A",
            "Run 3-5 rounds in a session, not 1 &mdash; the second and third rounds are where the patterns show up",
        ],
        "how_to_note": "The biggest gain from practice interviews is noticing your own patterns &mdash; you always over-explain, you never ask about scale, you skip the test cases. After 5 mock rounds you'll see the pattern; after 1 you won't.",
        "example_task": "System design mock for a senior backend role",
        "example_output": """Question: Design a URL shortener. Assume 100M URLs created per day, 10B reads per day, global latency target p99 under 100ms.

Before I let you start &mdash; what clarifying questions would you ask me?

[after candidate answers]

Good catch on the read/write ratio. You didn't ask about:
  - Custom aliases vs auto-generated
  - Expiration / retention
  - Analytics (do we track click counts?)

These materially change the data model. A strong candidate asks 4-6 clarifiers before drawing anything. You asked 2.

Now &mdash; sketch the high-level architecture. I'll push back on each piece.

[after sketch]

Your write path uses base62 encoding of an auto-incrementing ID. Two pushbacks:
  1. The auto-increment is a bottleneck at 100M writes/day across regions. How do you avoid coordinated ID generation?
  2. Base62 of a sequential ID leaks volume to anyone scraping. Is that OK?

What's your answer?""",
        "tips": [
            "<strong>Don't ask for the answer.</strong> Ask the model to interview you. The difference between practice and study is huge.",
            "<strong>Specify the weakness.</strong> &ldquo;I freeze on hash-table problems&rdquo; gets you 10 hash-table problems with feedback. &ldquo;Coding&rdquo; gets you generic advice.",
            "<strong>Stay in the role.</strong> If you blank, don't ask for the answer &mdash; ask &ldquo;what would a hint look like?&rdquo; That's what real interviewers offer.",
            "<strong>Run a debrief.</strong> After each mock, ask &ldquo;what patterns showed up across these 3 rounds?&rdquo; The patterns are what cost real offers.",
        ],
        "related_1": "best-chatgpt-prompt-for-job-interview-prep",
        "related_1_name": "Best Prompt for Job Interview Prep",
        "related_2": "best-chatgpt-prompt-for-coding",
        "related_2_name": "Best Prompt for Coding",
    },
    {
        "slug": "best-chatgpt-prompt-for-cold-dm-linkedin",
        "page_title": "Best ChatGPT Prompt for Cold LinkedIn DMs",
        "desc": "Write cold LinkedIn outreach that gets replies instead of being ignored. For sales, business development, and partnership outreach.",
        "subtitle": "Short, specific, easy to reply to &mdash; without sounding like every other &ldquo;quick question&rdquo; DM in their inbox.",
        "prompt": """You are a senior B2B sales leader who has personally sent 10,000+ cold LinkedIn DMs and tracked the reply rates. Write a cold message.

Who I am: [YOUR ROLE + ONE-LINE CREDIBILITY ANCHOR &mdash; e.g. &ldquo;head of partnerships at a 50-person logistics startup&rdquo;]
Who I'm reaching: [THEIR ROLE + COMPANY + WHY THEM SPECIFICALLY &mdash; e.g. &ldquo;VP of Ops at Acme; saw the LinkedIn post about their new warehouse&rdquo;]
What I want from them (be honest): [intro to someone / 20-min call / feedback on a product / partnership convo / referral]
ONE specific real reason I'm reaching them (not them as a role, them specifically): [A POST, A TALK, A PROJECT, A SHARED CONNECTION]
What's in it for them: [BE HONEST &mdash; if it's mostly for me, say so]

Requirements:
- Under 100 words
- First line is NOT &ldquo;Hi [Name], hope you're doing well&rdquo; or anything they've read a thousand times
- The specific reason must appear in the first two sentences &mdash; before the ask
- The ask is concrete and easy to say yes to (15 minutes, one yes/no question, a specific resource)
- No emojis, no &ldquo;quick question,&rdquo; no &ldquo;I'll keep this brief&rdquo; (they all do, none are)
- If my specific reason isn't actually specific (&ldquo;love your work&rdquo;), FLAG it &mdash; don't paper over with corporate filler""",
        "how_to_steps": [
            "Identify ONE specific real reason you're reaching this person &mdash; a post they wrote, a project at their company, a shared connection. &ldquo;Saw your profile&rdquo; doesn't count.",
            "Be honest about what you want &mdash; the model will write a much better DM if it knows whether you want a 20-min call, an intro, or just a reply",
            "State the credibility anchor &mdash; one line about who you are so they know it's not a random",
            "Paste into ChatGPT or Claude",
            "Send it. If you get no replies in 7 days, the issue is almost always the specific-reason field, not the wording",
        ],
        "how_to_note": "Reply rates on cold LinkedIn DMs are typically 3-10% with a specific reason and 0-2% without. The whole craft is the specific reason &mdash; the rest is just not screwing it up.",
        "example_task": "Cold DM to a VP of Engineering about a developer tooling product",
        "example_output": """Hi Maya &mdash;

Read your QCon talk on the migration off the in-house build system. The bit about rollback as a default-on, not opt-in feature is the same principle we built our deploy tool around &mdash; been trying to articulate it for a year and couldn't.

I lead product at Boulder, a deploy tool for the &ldquo;3-engineer team that needs prod-grade infra&rdquo; segment. Curious whether you're seeing demand for that from your customer base now that the toolchain is consolidated.

Worth 15 minutes? Happy with a no &mdash; just thought the overlap was worth asking about.

&mdash; Sam""",
        "tips": [
            "<strong>The specific reason is the whole thing.</strong> &ldquo;Saw your talk at QCon last month&rdquo; &gt;&gt; &ldquo;impressed by your work.&rdquo; If you can't name something specific, you're not ready to send the DM.",
            "<strong>Make the ask easy to refuse.</strong> &ldquo;Happy with a no&rdquo; reduces friction; recipients reply more often to messages that explicitly accept rejection.",
            "<strong>Don't open with &lsquo;hope you're doing well.&rsquo;</strong> Every cold DM does. Lead with the specific reason &mdash; that's the differentiator.",
            "<strong>Send to inboxes, not connection requests.</strong> A 100-word DM with no connection request often gets read; a connection-request-then-DM gets filtered.",
        ],
        "related_1": "best-chatgpt-prompt-for-networking-email",
        "related_1_name": "Best Prompt for Networking Emails",
        "related_2": "best-chatgpt-prompt-for-sales-cold-call",
        "related_2_name": "Best Prompt for Sales Cold Calls",
    },
    {
        "slug": "best-chatgpt-prompt-for-google-ads-copy",
        "page_title": "Best ChatGPT Prompt for Google Ads Copy",
        "desc": "Write Google Ads headlines, descriptions, and extensions that match search intent and stay under character limits. For Search and Performance Max.",
        "subtitle": "Headlines under 30 chars, descriptions under 90 &mdash; that match what the searcher actually typed.",
        "prompt": """You are a senior paid-search specialist who has managed multi-million-dollar Google Ads accounts across SaaS, e-commerce, and lead gen. Write ad copy for a Google Ads campaign.

Campaign type: [Search / Performance Max / Display]
Product or service: [ONE SENTENCE &mdash; what you're selling]
Landing page URL: [PASTE URL]
Target keywords (the actual queries we're bidding on): [LIST 5-15]
Searcher intent: [research / comparison / ready-to-buy / branded]
One thing that makes us different: [PROOF, NOT ADJECTIVES &mdash; &ldquo;30-day free trial, no credit card&rdquo; not &ldquo;leading provider&rdquo;]
Banned phrases (corporate filler we never use): leading, best-in-class, results-driven, world-class, innovative

Requirements:
- Generate 15 headlines (max 30 characters each, counted exactly)
- Generate 4 descriptions (max 90 characters each, counted exactly)
- Match the searcher's literal query language in at least 5 headlines (if they searched &ldquo;crm for solo founders&rdquo;, one headline says &ldquo;CRM for Solo Founders&rdquo;)
- Each description must include ONE concrete proof point (a number, a guarantee, a specific feature)
- Include at least 3 sitelink suggestions and 2 callout extensions
- If a headline exceeds 30 chars, count it again and shorten &mdash; do not submit anything over the limit""",
        "how_to_steps": [
            "Pull your actual top keywords from Google Ads (Search Terms report) &mdash; the model writes much better copy when it sees real queries",
            "Paste the landing page URL OR the headline + key value props if the page isn't live yet",
            "Specify the searcher intent &mdash; research-intent ads (&ldquo;what is X&rdquo;) and buy-intent ads (&ldquo;buy X&rdquo;) need totally different copy",
            "Paste into ChatGPT or Claude",
            "Count characters before publishing &mdash; the model will sometimes go over. Reject anything that doesn't fit.",
        ],
        "how_to_note": "Google's Responsive Search Ads rotate up to 15 headlines and 4 descriptions. Generating extras and letting Google's machine learning pick the winners is the modern playbook &mdash; not picking 3 favorites yourself.",
        "example_task": "Search ad for &ldquo;crm for solo founders&rdquo; targeting a free-trial signup",
        "example_output": """Headlines (max 30 chars):
  CRM for Solo Founders
  Built for One-Person Cos
  Free 30 Days, No Card
  CRM Without the Bloat
  10-Min Setup, Real CRM
  Track Deals, Not Tabs
  CRM Made for Solo Devs
  Pipeline + Notes in One
  Solo Founder? Try Free
  CRM That Doesn't Slow You
  No-Code Pipeline Tool
  CRM Under $20/Month
  Cancel in 1 Click
  Solo Founders Love It
  Built by a Solo Founder

Descriptions (max 90 chars):
  CRM made for one-person teams. 30-day free trial. No card. Set up in under 10 mins.
  Track deals, notes, and tasks without a 6-figure sales stack. Free trial, no credit card.
  The lightweight CRM solo founders actually finish setting up. Free 30-day trial.
  Solo founders, not sales orgs. 100+ founders signed up last month. Try free, cancel in 1 click.

Sitelinks:
  Pricing  |  See Features  |  Compare to HubSpot
Callouts:
  No credit card  |  Cancel anytime""",
        "tips": [
            "<strong>Mirror the query.</strong> If the searcher typed &ldquo;crm for solo founders,&rdquo; at least one headline must contain &ldquo;CRM for Solo Founders.&rdquo; This is how you win Quality Score.",
            "<strong>Proof beats adjectives.</strong> &ldquo;100+ founders signed up last month&rdquo; outperforms &ldquo;leading CRM&rdquo; every time.",
            "<strong>Use the character counter.</strong> Google rejects anything over the limit. The model gets this wrong about 1 in 8 headlines; verify before saving.",
            "<strong>Let Google test, don't pre-pick.</strong> Submit 15 headlines, not the 3 you like. Google's machine learning will surface the winners faster than your gut.",
        ],
        "related_1": "best-chatgpt-prompt-for-copywriting",
        "related_1_name": "Best Prompt for Copywriting",
        "related_2": "best-chatgpt-prompt-for-landing-page-audit",
        "related_2_name": "Best Prompt for Landing Page Audits",
    },
    {
        "slug": "best-chatgpt-prompt-for-facebook-ad-copy",
        "page_title": "Best ChatGPT Prompt for Facebook Ad Copy",
        "desc": "Write Facebook (Meta) ad copy that stops the scroll and matches the format &mdash; primary text, headline, description, and CTA.",
        "subtitle": "Primary text, headline, description, CTA &mdash; written for the actual platform, not generic ad-speak.",
        "prompt": """You are a senior paid-social specialist who has run 7-figure Meta ad budgets across DTC, B2B, and apps. Write Facebook ad copy.

Campaign objective: [Sales / Leads / Traffic / Awareness / App Installs]
Product or service: [ONE SENTENCE &mdash; what you're selling, and the price if relevant]
Audience: [BE SPECIFIC &mdash; &ldquo;US new moms 28-38, kids under 2&rdquo; not &ldquo;moms&rdquo;]
What problem this solves for them: [THEIR WORDS, NOT YOURS]
Visual we're pairing with: [STATIC IMAGE / 9:16 VIDEO / CAROUSEL / UGC TESTIMONIAL]
Landing page promise: [WHAT THEY'LL SEE WHEN THEY CLICK]
Hook angle (pick one): [problem-aware / category-aware / contrarian / founder-story / customer-result]

Requirements:
- Primary text (up to 125 chars before truncation): hook in line 1 must stop the scroll
- Headline (up to 40 chars): clear value prop, not clever wordplay
- Description (up to 30 chars): secondary detail or proof
- CTA button: pick from Meta's allowed list (Shop Now / Learn More / Sign Up / Get Offer / Download / Subscribe / Get Quote / etc.)
- Match the visual: if the visual is UGC testimonial, the copy should read like a friend recommending; if it's a product photo, the copy should be punchy claims
- Provide 3 variants of the primary text for testing
- No clichés, no &ldquo;tired of [X]?&rdquo;, no &ldquo;swipe up&rdquo; (wrong platform)""",
        "how_to_steps": [
            "Define your audience SPECIFICALLY &mdash; demographic + psychographic + behavior. &ldquo;Moms&rdquo; produces generic copy; &ldquo;US new moms 28-38 with kids under 2 who buy DTC&rdquo; produces good copy.",
            "Pair the copy to the visual &mdash; UGC and product shots want very different tones",
            "Pick ONE hook angle per ad &mdash; testing 4 variants on different angles is better than one ad trying all four",
            "Paste into ChatGPT or Claude",
            "Test 3 variants of the primary text; the headline can stay constant",
        ],
        "how_to_note": "Meta ads succeed or fail in the first 3 seconds for video, the first line of primary text for static. The hook is the entire ad. Spend disproportionate time on line 1.",
        "example_task": "DTC ad for a $34 sleep supplement, audience = stressed working parents",
        "example_output": """Primary text (variant 1, problem-aware hook):
The reason you keep waking up at 3am isn't your kids. It's your cortisol crashing. Magnesium glycinate fixes it &mdash; 89% of our buyers report sleeping through within 2 weeks. $34, free returns.

Primary text (variant 2, founder-story hook):
I started taking magnesium glycinate because I was waking up at 3am every night and couldn't function the next day. 11 days later I slept through. Now we make our own version. $34 with free returns.

Primary text (variant 3, customer-result hook):
&ldquo;I haven't woken up at 3am in 6 weeks.&rdquo; &mdash; Jenna, 34, two kids under 5. The supplement she's talking about: magnesium glycinate, $34, free returns.

Headline (40 chars max):
Sleep Through the Night Again

Description (30 chars max):
Free returns, 89% success rate

CTA: Shop Now""",
        "tips": [
            "<strong>Line 1 of primary text is the whole ad.</strong> Meta truncates at 125 chars on mobile. If line 1 doesn't stop the scroll, lines 2-5 don't matter.",
            "<strong>Specific audience &gt; generic audience.</strong> The copy for &ldquo;moms&rdquo; is bad. The copy for &ldquo;US new moms 28-38 with kids under 2&rdquo; is good. The targeting is the same; the copy is the difference.",
            "<strong>Test angles, not adjectives.</strong> Three variants on three different hook angles (problem / story / result) will outperform three variants of the same hook with different words.",
            "<strong>Match the visual.</strong> A UGC video needs copy that sounds like a real person. A studio product shot can have punchier claim copy. Mismatched ads underperform.",
        ],
        "related_1": "best-chatgpt-prompt-for-copywriting",
        "related_1_name": "Best Prompt for Copywriting",
        "related_2": "best-chatgpt-prompt-for-instagram-bio",
        "related_2_name": "Best Prompt for Instagram Bios",
    },
    {
        "slug": "best-chatgpt-prompt-for-doctor-appointment-prep",
        "page_title": "Best ChatGPT Prompt for Doctor Appointment Prep",
        "desc": "Prep for a doctor's appointment so you don't leave with unanswered questions. Symptom summary, questions to ask, and what to push back on.",
        "subtitle": "Walk in organized: symptom timeline, focused questions, and what to ask if you're not satisfied with the answer.",
        "prompt": """You are a primary-care doctor who is honest about how rushed appointments are and how to make the most of 15 minutes. Help me prep for an upcoming appointment.

What kind of appointment: [primary care / specialist (which kind) / urgent care / follow-up]
What's bringing me in (in my own words, no jargon): [DESCRIBE]
How long this has been going on: [DAYS / WEEKS / MONTHS]
Symptoms (be specific, including what makes them better/worse):
  - [SYMPTOM 1 + when, severity 1-10, triggers]
  - [SYMPTOM 2]
What I've already tried (medications, home remedies, lifestyle changes): [LIST]
My relevant history (medications, conditions, family history if relevant): [BRIEF]
What I'm hoping to leave the appointment with: [diagnosis / test / referral / med / reassurance / plan]

Requirements:
- Give me a SHORT (under 2 minute) opening summary I can read aloud to the doctor &mdash; not a medical essay
- List 5-8 specific questions to ask, in order of importance
- For each question, tell me what a satisfactory answer looks like AND what to ask if the answer is vague
- Flag any symptoms in my list that warrant earlier care (ER, urgent care today)
- Do NOT diagnose me. Do NOT recommend specific medications. This is appointment prep, not medical advice.
- If something I described could be serious, say so plainly and tell me to call my doctor or 911 NOW &mdash; not wait for the appointment""",
        "how_to_steps": [
            "Write down your symptoms BEFORE you talk to the model &mdash; specific symptoms, timeline, severity 1-10",
            "Include what you've already tried &mdash; this saves 5 minutes in the appointment and shows the doctor you're prepared",
            "Be honest about what you want to leave with &mdash; if you want a referral, say so; the questions look different",
            "Paste into ChatGPT or Claude",
            "Read the &ldquo;flag earlier care&rdquo; section first &mdash; if anything in your symptoms warrants urgent care, don't wait for the appointment",
        ],
        "how_to_note": "This is appointment prep, not medical advice. ChatGPT does not have your chart, your vitals, or the ability to examine you. The point of this prompt is to walk in organized &mdash; not to skip the doctor.",
        "example_task": "Prep for a primary-care appointment about persistent fatigue",
        "example_output": """Opening summary (read aloud, ~90 seconds):
&ldquo;I've been more tired than usual for about 3 months. It's not exhaustion after a busy day &mdash; it's tired even after a full night of sleep. I've tried going to bed earlier, cutting back on coffee after noon, and a multivitamin, no change. I'm sleeping 7-8 hours and tracked it with my watch. I'm a 32-year-old woman, periods are regular but heavier than 2 years ago. No new medications. My mom was hypothyroid &mdash; diagnosed at 35. I'd like to figure out what to test for.&rdquo;

Questions to ask (in order):
  1. Given the symptoms and family history, what blood panels would you order today?
     [Satisfactory answer names specifics: CBC, ferritin, TSH, free T4, vitamin D, B12.
      If vague: ask &ldquo;Can we run a full iron panel and a thyroid panel today?&rdquo;]
  2. If everything comes back normal, what's the next step?
     [Satisfactory answer names a timeline and a referral path.]
  3. Could the heavier periods be related to the fatigue?
     [Satisfactory answer addresses ferritin specifically.]
  ... (5 more)

When to call earlier:
  If you develop shortness of breath at rest, chest pain, or fainting,
  go to the ER &mdash; don't wait for the appointment.""",
        "tips": [
            "<strong>Specifics beat severity words.</strong> &ldquo;Tired even after 8 hours of sleep, started 3 months ago&rdquo; gets a useful response. &ldquo;Really tired&rdquo; does not.",
            "<strong>Bring the summary, on paper.</strong> Hand the doctor a printed half-page. Most will appreciate it; it's faster than them reconstructing your story.",
            "<strong>Ask what tests, not what diagnosis.</strong> Doctors will run the tests; getting them to commit to a diagnosis in 15 minutes is unreasonable.",
            "<strong>If the answer is vague, ask one follow-up.</strong> &ldquo;What specifically would we be testing for?&rdquo; is a fair question. Two follow-ups is also fair. After that, you're past appointment length.",
            "<strong>This is appointment prep, not medical advice.</strong> ChatGPT can't see you. Anything that feels urgent today &mdash; chest pain, breathing trouble, severe pain &mdash; is a 911 call or urgent care, not a chatbot.",
        ],
        "related_1": "best-chatgpt-prompt-for-sleep-better",
        "related_1_name": "Best Prompt for Sleeping Better",
        "related_2": "best-chatgpt-prompt-for-fitness-plan",
        "related_2_name": "Best Prompt for Fitness Plans",
    },
    {
        "slug": "best-chatgpt-prompt-for-discovery-call-questions",
        "page_title": "Best ChatGPT Prompt for Discovery Call Questions",
        "desc": "Generate the discovery call questions that actually qualify a deal &mdash; pain, budget, authority, timeline &mdash; without sounding like a script.",
        "subtitle": "Pain, authority, budget, timeline &mdash; in a conversation that doesn't sound like a script.",
        "prompt": """You are a senior B2B sales leader who has run thousands of discovery calls and trained AEs to do the same. Generate discovery questions for an upcoming call.

What we sell: [ONE SENTENCE]
Who the call is with (role + company + size): [SPECIFIC]
Where they came from (inbound / outbound / referral / event): [SPECIFIC]
What I already know about their situation: [WHATEVER YOU HAVE]
Average sales cycle and deal size: [E.G. &ldquo;45 days, $25K ACV&rdquo;]
What disqualifies a deal for us: [BE SPECIFIC &mdash; company size, tech stack, geography, etc.]

Requirements:
- 12-15 questions organized into: Context, Pain, Impact, Decision Process, Budget, Timeline
- Open-ended (no yes/no questions), specific (not &ldquo;tell me about your challenges&rdquo;)
- For EACH question, give me: the question itself, what a strong answer sounds like, what a red-flag answer sounds like, and the follow-up to ask if the answer is weak
- Include 2-3 questions designed to uncover competing solutions they're evaluating
- Include 1 question that will surface internal political risk (champions, blockers, executive sponsor)
- Do NOT include &ldquo;what keeps you up at night&rdquo; or &ldquo;if you could wave a magic wand&rdquo; or any other sales cliché""",
        "how_to_steps": [
            "Specify their role &mdash; you ask a VP very different questions than an IC champion",
            "Be honest about your disqualifiers &mdash; the questions should screen them in or out, not just qualify in",
            "Note where they came from &mdash; inbound vs outbound calls run differently in the first 5 minutes",
            "Paste into ChatGPT or Claude",
            "Pick 8-10 from the list for the actual call; don't try to ask all 15",
        ],
        "how_to_note": "Discovery calls fail when reps ask too many questions and never listen. A good call asks 8-12 questions and spends 60% of the time letting the prospect talk. The list is for prep; don't read from it.",
        "example_task": "Discovery questions for a 30-min call with a VP of Engineering at a 200-person SaaS company about an observability product",
        "example_output": """CONTEXT (5 min):
1. What does your current observability stack look like?
   Strong answer: names 3-5 specific tools, knows costs, owns budget.
   Red flag: &ldquo;we have a few things, the team handles it.&rdquo;
   Weak-answer follow-up: &ldquo;Who on your team would know off the top of their head?&rdquo;

2. Walk me through the last on-call incident your team handled. What happened?
   Strong answer: specific incident, named root cause, named time-to-resolution.
   Red flag: vague, can't recall a specific one.
   Weak-answer follow-up: &ldquo;What's the most recent one that lost someone sleep?&rdquo;

PAIN (8 min):
3. When something breaks in production, what's the first place your team looks?
   ... (continues for all 12-15 questions)

DECISION + POLITICAL:
12. Who else, besides you, would need to weigh in on a decision like this?
    Strong answer: names 2-3 people by name and role.
    Red flag: &ldquo;just me&rdquo; (rarely true at 200-person company &mdash; signals low engagement
    or hidden blockers).""",
        "tips": [
            "<strong>Ask, then shut up.</strong> The pause after a hard question is where you learn things. Sales reps lose deals by filling the silence with the next question.",
            "<strong>Get to budget by call 1 or 2.</strong> If you finish the discovery without knowing whether they can buy what you sell, you've wasted both sides' time.",
            "<strong>Surface competition.</strong> &ldquo;Who else are you looking at?&rdquo; is a fair question by minute 20. Reps who don't ask end up surprised in the demo.",
            "<strong>Screen out, too.</strong> Discovery is also disqualification. If the call surfaces a hard disqualifier (no budget, wrong size, wrong tech stack), end it gracefully instead of forcing it forward.",
        ],
        "related_1": "best-chatgpt-prompt-for-sales-pitch",
        "related_1_name": "Best Prompt for Sales Pitches",
        "related_2": "best-chatgpt-prompt-for-sales-cold-call",
        "related_2_name": "Best Prompt for Sales Cold Calls",
    },
    {
        "slug": "best-chatgpt-prompt-for-lost-deal-postmortem",
        "page_title": "Best ChatGPT Prompt for Lost-Deal Postmortems",
        "desc": "Run an honest postmortem on a lost B2B deal &mdash; what actually killed it, what could have changed the outcome, and what to fix in the next deal.",
        "subtitle": "Cut through &ldquo;they went with a competitor&rdquo; to the real reason &mdash; and the pattern across your lost deals.",
        "prompt": """You are a senior sales leader who has run thousands of lost-deal reviews and is honest about the unflattering reasons deals die. Help me run a postmortem on this lost deal.

The deal (one paragraph): [COMPANY, ACV, CYCLE LENGTH, WHO YOU WERE TALKING TO, WHEN AND HOW IT DIED]
The official reason they gave for not buying: [WHAT THEY SAID]
What competitors (if any) they evaluated: [LIST]
The decision-makers + champions + blockers: [WHO WAS WHO]
Key moments in the cycle: [DEMO, EVAL, PROCUREMENT &mdash; what went well, what didn't]
My honest gut about why we lost (not what we say in pipeline review): [BE HONEST]

Requirements:
- Tell me the most likely REAL reason we lost &mdash; not the official reason
- Score these factors 1-5 for how much they contributed: product fit, price, champion strength, executive alignment, our salescraft, competitor strength, timing, internal political risk
- Identify the single decision in this cycle that, if made differently, would have most changed the outcome
- Identify what's likely a pattern across our lost deals (if you can infer from this one) and what to ask the rest of the team
- Honest, no padding &mdash; if my salescraft was the issue, say so
- If the official reason and the real reason are different, explain why customers usually give the softer reason""",
        "how_to_steps": [
            "Be honest about what happened &mdash; the prompt is useless if you give the same story you told in pipeline review",
            "Include who was who &mdash; champion strength is one of the top reasons deals die and most reps don't track it",
            "Note the key moments &mdash; demo, eval, procurement &mdash; each one has different failure modes",
            "Paste into ChatGPT or Claude",
            "Take the &ldquo;single decision&rdquo; output and decide whether it's a one-off or a pattern across deals",
        ],
        "how_to_note": "The official reason customers give for not buying is almost always softer than the real one. &ldquo;Bad timing&rdquo; usually means &ldquo;you didn't make the case strongly enough.&rdquo; &ldquo;Budget&rdquo; usually means &ldquo;not worth this much to us.&rdquo; The point of the postmortem is to get past the soft answer.",
        "example_task": "Postmortem on a $40K ACV deal that died after final exec presentation",
        "example_output": """Most likely real reason we lost:
The CFO never had a clear answer to &ldquo;why now, why this, why us?&rdquo; on the same page.
Our champion sold us internally as &ldquo;a better version of [incumbent]&rdquo; rather than as a
business-impact case &mdash; which made it easy for the CFO to defer.

Factor scoring (1-5):
  Product fit:           4 (strong)
  Price:                 3 (not the issue, but the CFO's anchor)
  Champion strength:     2 (engaged but couldn't carry the exec sell)
  Executive alignment:   1 (we never met the CFO; saw slides only)
  Our salescraft:        2 (we trusted the champion too much)
  Competitor strength:   3 (incumbent had inertia)
  Timing:                3 (Q3 budget review &mdash; soft window)
  Internal political:    4 (CFO and VP Eng didn't align on priority)

Single decision that would have most changed the outcome:
Push for a 20-minute meeting with the CFO before final presentation, prepared with
a one-page business-impact slide. Probable counterfactual: even a 50% chance of a
yes is worth it because everything downstream depends on exec alignment.

Likely pattern (worth checking with the team):
We trust champions to sell internally. We should ask in EVERY deal:
&ldquo;Who else needs to be in the room before final, and how do we get there?&rdquo;""",
        "tips": [
            "<strong>Get the real reason from the customer.</strong> Schedule a 15-min &ldquo;learning&rdquo; call after the loss. The honest reason often comes out then because the sales pressure is off.",
            "<strong>Score every deal on the same factors.</strong> Doing 10 of these creates a pattern: you'll see &ldquo;champion strength&rdquo; or &ldquo;exec alignment&rdquo; show up over and over.",
            "<strong>The single-decision question is the most valuable.</strong> &ldquo;If you ran this deal again, what's the one thing you'd do differently?&rdquo; surfaces the action item that actually changes future deals.",
            "<strong>Share the postmortems.</strong> Lost-deal reviews are most valuable when the whole team sees the patterns. Quarterly review of all losses &gt; one-off rep retrospectives.",
        ],
        "related_1": "best-chatgpt-prompt-for-sales-pitch",
        "related_1_name": "Best Prompt for Sales Pitches",
        "related_2": "best-chatgpt-prompt-for-performance-review",
        "related_2_name": "Best Prompt for Performance Reviews",
    },
]


def main():
    written = []
    for p in PROMPTS:
        schema = build_schema(p["page_title"], p["desc"], p["slug"])
        steps = "\n        ".join(f"<li>{s}</li>" for s in p["how_to_steps"])
        tips = "\n        ".join(f"<li>{t}</li>" for t in p["tips"])

        html = TEMPLATE
        html = html.replace("@@PAGE_TITLE@@", p["page_title"])
        html = html.replace("@@DESC@@", p["desc"])
        html = html.replace("@@SLUG@@", p["slug"])
        html = html.replace("@@SUBTITLE@@", p["subtitle"])
        html = html.replace("@@PROMPT@@", p["prompt"])
        html = html.replace("@@HOW_TO_STEPS@@", steps)
        html = html.replace("@@HOW_TO_NOTE@@", p["how_to_note"])
        html = html.replace("@@EXAMPLE_TASK@@", p["example_task"])
        html = html.replace("@@EXAMPLE_OUTPUT@@", p["example_output"])
        html = html.replace("@@TIPS@@", tips)
        html = html.replace("@@RELATED_1@@", p["related_1"])
        html = html.replace("@@RELATED_1_NAME@@", p["related_1_name"])
        html = html.replace("@@RELATED_2@@", p["related_2"])
        html = html.replace("@@RELATED_2_NAME@@", p["related_2_name"])
        html = html.replace("@@SCHEMA@@", schema)

        out = PROMPTS_DIR / f"{p['slug']}.html"
        out.write_text(html)
        written.append(out.name)
    print(f"Wrote {len(written)} pages:")
    for w in written:
        print(f"  {w}")


if __name__ == "__main__":
    main()
