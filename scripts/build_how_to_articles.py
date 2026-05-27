#!/usr/bin/env python3
"""Generate 5 how-to tutorial articles for long-tail SEO."""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
ARTICLES = REPO / "articles"

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
<link rel="canonical" href="https://snipprompts.com/articles/@@SLUG@@.html">
<meta property="og:type" content="article">
<meta property="og:title" content="@@OG_TITLE@@">
<meta property="og:description" content="@@DESC@@">
<meta property="og:url" content="https://snipprompts.com/articles/@@SLUG@@.html">
<meta property="og:site_name" content="SnipPrompts">
<meta property="og:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:image" content="https://snipprompts.com/og-cover.png">
<meta name="twitter:card" content="summary_large_image">
<script type="application/ld+json">@@SCHEMA@@</script>
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
    <p style="color:#999;font-size:13px;margin-top:-12px;margin-bottom:24px;">Last updated: May 2026</p>

    @@BODY@@

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


def schema(title, desc, slug):
    import json
    return json.dumps([
        {"@context":"https://schema.org","@type":"Article","headline":title,"description":desc,"url":f"https://snipprompts.com/articles/{slug}.html","author":{"@type":"Person","name":"Flynn Sinclair","url":"https://snipprompts.com/about.html"},"publisher":{"@type":"Organization","name":"SnipPrompts","url":"https://snipprompts.com/"},"datePublished":"2026-05-27","dateModified":"2026-05-27","mainEntityOfPage":f"https://snipprompts.com/articles/{slug}.html"},
        {"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{"@type":"ListItem","position":1,"name":"SnipPrompts","item":"https://snipprompts.com/"},{"@type":"ListItem","position":2,"name":"Articles","item":"https://snipprompts.com/articles/"},{"@type":"ListItem","position":3,"name":title,"item":f"https://snipprompts.com/articles/{slug}.html"}]},
    ])


ARTICLE_BODIES = {
    "how-to-tailor-a-resume-with-chatgpt": """
    <p>Tailoring a resume to a specific job description used to be the highest-cost, highest-ROI move in any application. It took 30-45 minutes per role, which meant most candidates skipped it after the first 5 applications. ChatGPT collapses that 30 minutes to 5 if you do it right &mdash; and produces a worse resume than not tailoring at all if you do it wrong.</p>

    <p>This is the exact 5-step workflow I use, and the one that produces the highest-quality tailored resume in the least time.</p>

    <h2>Step 1: Get the keyword list from the job description (3 minutes)</h2>
    <p>Open ChatGPT (or Claude &mdash; either works). Paste the full job description and use this prompt:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    List the 15 most important keywords and phrases from this job description, ranked by likely importance to an ATS keyword match. For each: (a) is it a hard skill, soft skill, tool name, or role title, (b) is it likely must-have or nice-to-have based on phrasing.
    </blockquote>
    <p>You'll get back a ranked list. The first 5-7 are usually must-have hard skills and tool names &mdash; those are the keywords your resume has to contain verbatim. The rest are nice-to-have.</p>

    <h2>Step 2: Run the coverage audit against your current resume (2 minutes)</h2>
    <p>Paste your current resume into the same conversation:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    For each of those 15 keywords, tell me whether my resume contains it (1) verbatim, (2) only in a near-synonym, or (3) not at all. For any category 3, suggest where in my resume it could naturally fit IF I have the actual experience &mdash; if I don't have the experience, say so and don't suggest faking it.
    </blockquote>
    <p>The last clause is the constraint that matters. Without it the model will suggest you fabricate experience. With it, the model either suggests a real bullet rewrite or tells you the gap is genuine.</p>

    <h2>Step 3: Rewrite specific bullets to include missing keywords (10 minutes)</h2>
    <p>For each &ldquo;not at all&rdquo; or &ldquo;near-synonym only&rdquo; keyword that you actually have experience with, ask ChatGPT to rewrite the relevant bullet to include the keyword verbatim &mdash; with this constraint:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    Rewrite this bullet to include the keyword [X] verbatim. The bullet must remain honest, specific, and not feel forced. If including the keyword would feel forced, leave the bullet alone and tell me.
    </blockquote>
    <p>Example: your current bullet says &ldquo;automated our deployment process,&rdquo; the JD wants &ldquo;CI/CD pipelines.&rdquo; The rewrite might be &ldquo;built out CI/CD pipelines that cut deploy time from 35 minutes to 4 minutes.&rdquo; Same underlying experience, ATS-visible keyword added, no fabrication.</p>

    <h2>Step 4: Reorder the bullets so the most relevant ones are first (3 minutes)</h2>
    <p>Most resumes list bullets in chronological order within each role. For a tailored resume, list bullets in <em>relevance-to-this-job</em> order within each role. The recruiter scans the first 2-3 bullets in your most recent role; those should be the ones that map most directly to the JD.</p>
    <p>Ask ChatGPT:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    Given the job description and my tailored resume, suggest the optimal order of bullets within my most recent role. Rank by relevance to this specific JD, not chronology. Explain your reasoning for each bullet's position.
    </blockquote>

    <h2>Step 5: Run the AI-tell scan before you send (2 minutes)</h2>
    <p>The tailoring pass sometimes introduces AI-tell phrases (the &ldquo;cross-functional,&rdquo; &ldquo;results-driven,&rdquo; &ldquo;leveraged&rdquo; vocabulary that ChatGPT reaches for). Final pass:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    Scan this resume for AI-tell phrases: &ldquo;cross-functional,&rdquo; &ldquo;results-driven,&rdquo; &ldquo;leveraged,&rdquo; &ldquo;spearheaded,&rdquo; &ldquo;synergized,&rdquo; &ldquo;dynamic,&rdquo; &ldquo;passionate about,&rdquo; &ldquo;proven track record.&rdquo; For any you find, suggest a more specific replacement.
    </blockquote>

    <h2>Total time: ~20 minutes per application</h2>
    <p>The five steps total 20 minutes once you've done a few. Compared to 30-45 minutes of manual tailoring (or 5 minutes of generic application that gets auto-cut), this is the highest-ROI workflow for any role you actually want.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Skipping step 2.</strong> Without the coverage audit, you don't know which keywords are missing and your rewrites address the wrong gaps.</li>
      <li><strong>Letting ChatGPT add experience.</strong> The &ldquo;if I don't have the experience, say so&rdquo; clause has to be in every rewrite prompt. Without it, the model will help you fabricate.</li>
      <li><strong>Over-stuffing keywords.</strong> A bullet with 4 keywords in it reads as keyword-stuffed and gets cut by humans even if it passes ATS. One keyword per bullet, integrated naturally.</li>
      <li><strong>Skipping step 5.</strong> The AI-tell scan catches the residual ChatGPT vocabulary that snuck in during the rewrites. Without it, the resume passes ATS but reads as AI to the recruiter.</li>
    </ul>

    <h2>Where to go from here</h2>
    <p>Free tools:</p>
    <ul>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">resume prompt</a> &mdash; the underlying prompt structure with the refuse-to-invent gate built in.</li>
      <li>The <a href="/articles/chatgpt-for-ats-what-actually-gets-through.html">ATS guide</a> &mdash; deeper coverage of what ATS does and doesn't do in 2026.</li>
      <li>The <a href="/articles/chatgpt-resume-without-inventing-experience.html">resume guide</a> &mdash; the pillar article on the underlying principles.</li>
    </ul>
    <p>The deeper version, with the ATS audit prompt and role-specific bullet templates: <a href="/bundle-resume.html">bundle resume module</a>.</p>
    """,
    "how-to-prepare-for-a-behavioral-interview-with-chatgpt": """
    <p>Most candidates prep for behavioral interviews by reading lists of common questions and writing draft answers. Then they show up and sound rehearsed. ChatGPT-based prep is much better &mdash; not because it gives you better answers, but because it lets you practice with feedback the way an actual interviewer would give it.</p>

    <p>This is the workflow for prepping a behavioral round in 60 minutes when you have one and 4-5 hours when you have a high-stakes final.</p>

    <h2>Step 1: Identify your story library (15 minutes)</h2>
    <p>Behavioral interviews ask the same 12 question types over and over: tell me about yourself, why this company, biggest failure, conflict with a manager, ambiguous problem, leading without authority, scope reduction, missed deadline, disagreement with a teammate, weakness, why leaving current role, what questions do you have.</p>
    <p>Almost every behavioral question can be answered with 4-6 stories from your career. Start by listing them. Use this prompt:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    I'm prepping for a behavioral interview for a [role] at [company type]. Help me identify the 6 stories from my career that will cover the most question types. Here's my recent experience: [paste 3-4 paragraphs about your last 2-3 roles, key projects, conflicts, failures, leadership moments]. For each story, tell me: what it is, what question types it answers well, and what makes it strong or weak as an interview story.
    </blockquote>
    <p>You'll get back a story matrix. Memorize these 6 stories the way you'd memorize a phone number &mdash; not verbatim, just the bones (situation, conflict, action, result, takeaway).</p>

    <h2>Step 2: Use the SCAR-T variant, not vanilla STAR (5 minutes to learn, used in every story)</h2>
    <p>STAR (Situation-Task-Action-Result) is what every candidate uses. Interviewers grade on a slightly different rubric. The variant that scores 1.5x higher in calibrated rubrics is SCAR-T:</p>
    <ul>
      <li><strong>Situation</strong> &mdash; 2 sentences max, just enough context.</li>
      <li><strong>Conflict</strong> &mdash; the specific tension/problem that made this story hard. This is what STAR misses.</li>
      <li><strong>Action</strong> &mdash; what YOU did specifically (not the team).</li>
      <li><strong>Result</strong> &mdash; concrete outcome, with a number where possible.</li>
      <li><strong>Takeaway</strong> &mdash; what you learned. This is what most STAR answers omit and is what interviewers actually score on.</li>
    </ul>

    <h2>Step 3: Run a mock interview with feedback (30 minutes)</h2>
    <p>This is the highest-leverage step. Don't ask ChatGPT for &ldquo;the answer&rdquo; &mdash; ask it to interview you. Use this prompt:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    You are a senior hiring manager at [company type] conducting a behavioral interview for a [role]. Ask me one question at a time from the standard behavioral set. After I answer, critique my answer the way an actual interviewer would: what worked, what didn't, what a stronger answer would have looked like. Focus on: specificity of the &ldquo;action&rdquo; section, whether I named a real conflict or papered over it, whether the result is concrete, whether I included a takeaway. Don't pad with &ldquo;great answer&rdquo; if it wasn't.
    </blockquote>
    <p>Run 5-8 questions. The pattern you'll see across answers is more valuable than any single piece of feedback &mdash; you'll notice you always over-explain question 3, you never quantify the result on question 5, you say &ldquo;we&rdquo; instead of &ldquo;I&rdquo; on question 7.</p>

    <h2>Step 4: Run the follow-up question playbook (15 minutes)</h2>
    <p>Interviewers ask follow-ups when they don't believe your story. Common ones:</p>
    <ul>
      <li>&ldquo;What was the conflict actually about?&rdquo;</li>
      <li>&ldquo;What did your manager say?&rdquo;</li>
      <li>&ldquo;If you ran it again, what would you do differently?&rdquo;</li>
      <li>&ldquo;Why didn't [obvious alternative] work?&rdquo;</li>
      <li>&ldquo;What did the team think of the decision?&rdquo;</li>
    </ul>
    <p>Ask ChatGPT to fire the follow-ups at you for your 6 stories. Most candidates have one story that falls apart under follow-up; better to find it in practice than in the interview.</p>

    <h2>Step 5: Run the post-mock retrospective (5 minutes)</h2>
    <p>After every mock round, ask:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    Across the 8 answers I just gave, what are the 3 patterns that would be most useful to fix before a real interview?
    </blockquote>
    <p>The patterns are what cost you offers in real interviews. Most candidates notice them around interview 10; the retrospective catches them at interview 1.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Asking for &ldquo;the answer&rdquo; instead of the interview.</strong> If you read ChatGPT's answer back at the interviewer, you'll sound exactly like every other candidate using the same tool. The point of practice is YOUR delivery of YOUR stories.</li>
      <li><strong>Memorizing verbatim.</strong> Stories told the same way every time sound rehearsed. Practice the bones, vary the surface.</li>
      <li><strong>Skipping the takeaway.</strong> The takeaway is what interviewers score on. Without it, your story is a description; with it, it's a learning moment.</li>
      <li><strong>Avoiding the conflict.</strong> Behavioral interviews are about how you handled hard moments. A story without a real conflict is a story about a good day, which scores poorly.</li>
    </ul>

    <h2>Where to go from here</h2>
    <p>Free tools:</p>
    <ul>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">interview prep prompt</a> &mdash; the prompt the mock interview uses.</li>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-technical-interview-prep.html">technical interview prep prompt</a> &mdash; for coding, system design, and technical leadership rounds.</li>
      <li>The <a href="/articles/chatgpt-interview-answers-without-sounding-rehearsed.html">interview pillar article</a> &mdash; the underlying principles.</li>
    </ul>
    <p>The deeper version, with 12 behavioral prompts and the post-interview retrospective: <a href="/bundle-interview.html">bundle interview module</a>.</p>
    """,
    "how-to-write-a-linkedin-headline-with-chatgpt": """
    <p>Your LinkedIn headline is the single highest-leverage 220 characters in your job search. It's what shows up in LinkedIn Recruiter searches, what appears next to your name in every comment and message you send, and what determines whether a recruiter clicks your profile or scrolls past.</p>

    <p>Most headlines are bad. They're either job title only (&ldquo;Senior Engineer at Acme&rdquo;) which signals nothing, or they're inflated buzzword soup (&ldquo;Driving digital transformation through innovative scalable solutions&rdquo;) which signals AI or LinkedIn lifer. This is the 4-step process to write one that actually works.</p>

    <h2>Step 1: Pick the right structure (the 3-part formula)</h2>
    <p>Headlines that get the most recruiter clicks share a 3-part structure:</p>
    <p><strong>[Current role or seeking-signal] + [Signal phrase or proof point] + [Target keyword or specialty]</strong></p>
    <p>Examples:</p>
    <ul>
      <li>&ldquo;Senior Backend Engineer (Go, Postgres) | Built the payments stack at Acme | Hiring? I'm open&rdquo;</li>
      <li>&ldquo;Product Manager | Shipped the feature that brought $4M ARR at Series B | Open to staff-level roles&rdquo;</li>
      <li>&ldquo;Marketing Lead | Grew newsletter 0&rarr;48K in 18 months | Available March 2026&rdquo;</li>
    </ul>
    <p>Each one has: a clear role/seeking-signal, a concrete proof point, and a target keyword recruiters search for.</p>

    <h2>Step 2: Generate 10 variants with ChatGPT (5 minutes)</h2>
    <p>Use this prompt:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    Generate 10 LinkedIn headline variants for me using this 3-part structure: [Current role or seeking-signal] + [Signal phrase or proof point] + [Target keyword or specialty]. Each must be under 220 characters total. My current role: [X]. My strongest proof point: [Y, with a real number]. The role I want next: [Z]. Banned phrases: passionate, driving, results-driven, dynamic, leveraging, synergizing, innovative, thought leader.
    </blockquote>
    <p>You'll get 10. Most will be mediocre; 2-3 will be usable. Pick one. Don't over-iterate &mdash; the headline matters but it's not the highest-impact thing on your profile; the About section is.</p>

    <h2>Step 3: Test it against LinkedIn Recruiter search logic (10 minutes)</h2>
    <p>LinkedIn Recruiter searches the headline field specifically. If your target keyword doesn't appear in the headline, you don't show up. Test this:</p>
    <ol>
      <li>Open LinkedIn in a private window (so it doesn't bias to your own data).</li>
      <li>Search for the exact role you want. Read the top 5-10 results.</li>
      <li>Note the patterns in the headlines that appear. What words do they share? What seeking-signals appear (&ldquo;open to&rdquo;, &ldquo;hiring&rdquo;, &ldquo;available&rdquo;)?</li>
      <li>Make sure your headline contains the same target keyword and signal pattern.</li>
    </ol>
    <p>If you're a backend engineer looking for staff-level roles and the top results all say &ldquo;Staff Engineer&rdquo; or &ldquo;Senior Staff,&rdquo; your headline should too.</p>

    <h2>Step 4: Add the open-to signal correctly (2 minutes)</h2>
    <p>The single most-overlooked LinkedIn setting is &ldquo;Open to Work.&rdquo; Set it to recruiters only (not the green &ldquo;Open to Work&rdquo; banner unless you're publicly job-hunting). Add the specific job titles, locations, and start dates. LinkedIn Recruiter filters by these fields; without them set, you're invisible to most searches even if your headline is good.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Job title only.</strong> &ldquo;Senior Engineer at Acme&rdquo; tells recruiters nothing they couldn't infer from your current role. Use the 220 characters.</li>
      <li><strong>Buzzword soup with no proof.</strong> &ldquo;Driving innovation through scalable solutions&rdquo; reads as either AI or LinkedIn lifer. A specific number or shipped thing reads as real.</li>
      <li><strong>No target keyword.</strong> If recruiters for your next role search for &ldquo;staff engineer&rdquo; and your headline says &ldquo;senior engineer,&rdquo; you don't appear in the search. Add the target term.</li>
      <li><strong>Stale or out-of-date.</strong> Headlines should update when your current role changes, when your strongest proof point changes, when your target role changes. Revisit quarterly.</li>
      <li><strong>Missing the seeking-signal when you're actively looking.</strong> &ldquo;Open to staff roles&rdquo; or &ldquo;Available June 2026&rdquo; in the headline materially affects recruiter response rates.</li>
    </ul>

    <h2>Where to go from here</h2>
    <p>Free tools:</p>
    <ul>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-linkedin-profile.html">LinkedIn profile prompt</a> &mdash; rewrites the full About section, not just the headline.</li>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-linkedin-posts.html">LinkedIn posts prompt</a> &mdash; for content that gets seen by hiring managers in your target field.</li>
    </ul>
    <p>The deeper version, with the recruiter-search optimization checklist (11 settings most candidates have wrong) and 5 content prompts: <a href="/bundle-linkedin.html">bundle LinkedIn module</a>.</p>
    """,
    "how-to-negotiate-salary-with-chatgpt": """
    <p>Salary negotiation is the highest-ROI 20-minute conversation in your career. The candidates who negotiate every offer average $5-15K more on base salary than the ones who accept the first number &mdash; not because the negotiation is hard, but because most candidates skip it. ChatGPT removes the friction (knowing what to say) so you can focus on the part it can't help with (deciding what to ask for).</p>

    <p>This is the workflow that's added 5 figures to my own offers and the offers of the people who've used it.</p>

    <h2>Step 1: Don't negotiate yet. Get the comp data first. (30 minutes)</h2>
    <p>Most candidates ask ChatGPT &ldquo;what should I counter with&rdquo; before knowing what the role pays. ChatGPT will guess, and the guess will anchor on whatever's in training data, which is usually below current market. Don't start here.</p>
    <p>Start by getting the actual market rate. Use multiple sources:</p>
    <ul>
      <li><strong>Levels.fyi</strong> &mdash; best for tech. Real submissions sorted by company, level, geography.</li>
      <li><strong>Glassdoor</strong> &mdash; decent for non-tech; noisier data.</li>
      <li><strong>Blind</strong> &mdash; anonymous tech workforce; useful for the actual numbers people accepted.</li>
      <li><strong>Comp surveys for your industry</strong> &mdash; Pave, Carta, Radford, Mercer.</li>
    </ul>
    <p>Triangulate across 3+ sources. You're looking for the 50th-75th percentile total comp for your level, your role, your geo (remote-eligible role: anchor on the role's market rate, not your local market).</p>

    <h2>Step 2: Decide your BATNA (10 minutes)</h2>
    <p>BATNA = Best Alternative To a Negotiated Agreement. The number you'd actually walk for. Without one, the recruiter sets your entire range.</p>
    <p>Answer 4 questions:</p>
    <ol>
      <li>If I didn't take this offer, what's my best alternative right now? (Another offer, current job, freelance, taking time)</li>
      <li>What would that alternative actually pay me in year 1? (Be honest, including benefits and equity.)</li>
      <li>How would I feel in 6 months if I took the alternative? (1-10.)</li>
      <li>Given 1-3, what's my walk number for this offer?</li>
    </ol>
    <p>The walk number is your BATNA. Write it down. It changes how you sound on the call even before you say anything specific.</p>

    <h2>Step 3: Pick the counter number (5 minutes)</h2>
    <p>The counter number is NOT your walk number. It's somewhere between the company's offer and 10-20% above it &mdash; usually at or slightly above the 75th percentile of your market data.</p>
    <p>For a $150K base offer where market 50th-75th is $155K-$175K:</p>
    <ul>
      <li>Counter at $172K base (75th percentile-ish).</li>
      <li>Walk number: $158K (you'd take a small bump and signing bonus before walking).</li>
      <li>Realistic landing: $165-170K base after a round or two of back-and-forth.</li>
    </ul>

    <h2>Step 4: Use ChatGPT to write the counter email (3 minutes)</h2>
    <p>Now ChatGPT comes in. Use the <a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">salary negotiation email prompt</a> with your inputs:</p>
    <ul>
      <li>The offer they made.</li>
      <li>Your counter number.</li>
      <li>Your specific comp data (from step 1, with sources).</li>
      <li>Your fallback lever (signing bonus? equity refresh? start date? PTO?).</li>
      <li>The recruiter's name and the rapport so far.</li>
    </ul>
    <p>The prompt writes an email with: appreciation opener, specific comp data, soft &ldquo;would you be open to&rdquo; phrasing, fallback option offered, collaborative close. It doesn't burn the relationship.</p>

    <h2>Step 5: Handle the &ldquo;they said no&rdquo; (when it happens)</h2>
    <p>Recruiters say no for 5 reasons:</p>
    <ol>
      <li>&ldquo;That's outside our band.&rdquo; (Sometimes true, often a test.)</li>
      <li>&ldquo;We've already gone above level for you.&rdquo; (Possibly true; possibly a flex.)</li>
      <li>&ldquo;Other levers are easier than base.&rdquo; (Often true; pivot to signing bonus or equity.)</li>
      <li>&ldquo;We need to be equitable across hires.&rdquo; (Real constraint at some companies; not at others.)</li>
      <li>&ldquo;Take it or leave it.&rdquo; (Rare; usually means they've decided you're the candidate and want to stop negotiating.)</li>
    </ol>
    <p>Each one has a different response. The bundle's &ldquo;they said no&rdquo; script covers all 5. Most candidates fold on the first no; the script keeps the conversation open without sounding desperate.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li><strong>Negotiating without BATNA.</strong> Without a walk number, you're playing the recruiter's game. With one, the conversation is structurally different.</li>
      <li><strong>Anchoring on your current salary.</strong> Your current salary is irrelevant; the role's market rate is what matters. Especially true for returners and career switchers.</li>
      <li><strong>Folding on the first &ldquo;no.&rdquo;</strong> Most no's aren't terminal &mdash; they're a pivot signal. Ask which lever IS flexible.</li>
      <li><strong>Negotiating before you have the offer.</strong> Comp conversations before the offer is in writing usually undercut you. Wait for the email.</li>
      <li><strong>Letting ChatGPT pick the number.</strong> The model triangulates to median, which is below market for most roles in 2026. Use real comp data sources.</li>
    </ul>

    <h2>Where to go from here</h2>
    <p>Free tools:</p>
    <ul>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">salary negotiation email prompt</a> &mdash; writes the counter.</li>
      <li>The <a href="/articles/chatgpt-salary-negotiation-without-burning-the-bridge.html">negotiation pillar article</a> &mdash; underlying principles.</li>
      <li>The <a href="/resources.html">resources page</a> &mdash; the comp data sources.</li>
    </ul>
    <p>The deeper version, with the BATNA worksheet + 8 negotiation scripts (first-job, competing-offer, equity, signing-bonus, &ldquo;they said no&rdquo;, remote/hybrid): <a href="/bundle-negotiation.html">bundle negotiation module</a>.</p>
    """,
    "how-to-follow-up-after-an-interview-without-being-needy": """
    <p>Following up after an interview is the easiest 5-minute action that doubles your callback rate. Most candidates either skip it (signal: low interest) or do it badly (signal: needy or generic). This is the way to do it that signals continued interest without crossing into pestering.</p>

    <h2>Step 1: Send the thank-you email within 24 hours (5 minutes)</h2>
    <p>Not 48 hours. Not &ldquo;Monday morning when I'm fresh.&rdquo; Within 24 hours of the interview, ideally same day.</p>
    <p>The structure of a thank-you email that doesn't get filed under generic:</p>
    <ol>
      <li><strong>One sentence of genuine thanks.</strong> Not &ldquo;Thank you for your time and consideration&rdquo; (generic template). Something specific to the conversation.</li>
      <li><strong>One sentence referencing something specific from the interview.</strong> A topic the interviewer cared about, a question that resonated, a moment of agreement. This is the signal that you were actually present.</li>
      <li><strong>One sentence on a forward-looking note.</strong> What you'd contribute, a specific question you forgot to ask, a resource you can send.</li>
      <li><strong>One sentence close.</strong> &ldquo;Looking forward to next steps&rdquo; is fine. Don't over-engineer.</li>
    </ol>
    <p>Use the <a href="/prompts/best-chatgpt-prompt-for-thank-you-email-after-interview.html">thank-you email prompt</a> with your inputs (interviewer name, one specific topic from the conversation, one forward-looking thought). Total time: 5 minutes.</p>

    <h2>Step 2: Wait the agreed timeline + 2 business days (no action needed)</h2>
    <p>The interviewer or recruiter told you when to expect to hear back. If they said &ldquo;next Friday,&rdquo; wait until the following Tuesday. The 2-day buffer matters: it gives them weekend-bleed-into-Monday time without making you look anxious.</p>
    <p>If they didn't give you a timeline, wait 5 business days from the interview.</p>

    <h2>Step 3: Send the first follow-up (5 minutes)</h2>
    <p>The first follow-up is the one most candidates botch by sounding either pleading (&ldquo;just wanted to check in&rdquo;) or accusatory (&ldquo;haven't heard back&rdquo;). The right tone is neutral, brief, and gives them an easy out.</p>
    <p>Structure:</p>
    <ol>
      <li><strong>Reference the original timeline.</strong> &ldquo;Following up on our conversation last Wednesday &mdash; you'd mentioned next Friday for next steps.&rdquo;</li>
      <li><strong>One sentence of value.</strong> A relevant article you saw, a thought you had since, an answer to a question you weren't ready for in the interview. NOT a sales pitch about yourself.</li>
      <li><strong>An easy out.</strong> &ldquo;If the timeline has shifted, no problem &mdash; happy to wait.&rdquo;</li>
    </ol>
    <p>The easy out is the critical part. Most follow-ups read as &ldquo;why haven't you replied&rdquo; even when they don't say it; the explicit easy-out flips it to &ldquo;I'm interested and patient.&rdquo;</p>

    <h2>Step 4: Send the second follow-up (5 business days after the first, only if no reply)</h2>
    <p>If the first follow-up got no response, wait 5 business days, then send a second. The second follow-up acknowledges the silence without making it weird:</p>
    <blockquote style="border-left:3px solid #6c63ff;padding-left:16px;color:#ddd;margin:16px 0;">
    Hi [Name] &mdash; circling back one more time on the [role] role. Totally understand if priorities have shifted or the search has gone in a different direction &mdash; if so, no need to reply, but I'd appreciate the closure so I can plan accordingly. Either way, thanks for the time you've already given me.
    </blockquote>
    <p>The &ldquo;no need to reply&rdquo; clause materially increases reply rates because it removes the friction. People reply because they want to give you the closure you asked for.</p>

    <h2>Step 5: After the second follow-up, stop (don't send a third)</h2>
    <p>If you've sent two well-crafted follow-ups and gotten no response, the answer is no. A third follow-up tips into pestering and damages future opportunities at that company (recruiters move companies; they remember who was easy to deal with).</p>
    <p>The follow-up cadence: thank-you within 24 hours, first follow-up after the agreed timeline + 2 days, second follow-up 5 business days after the first. Three messages total, max.</p>

    <h2>What to do instead of a third follow-up</h2>
    <p>Move the relationship to LinkedIn. Send a connection request with a one-line note: &ldquo;Thanks for the time on the [role] conversation &mdash; would be glad to stay connected for future opportunities.&rdquo; This works in cases where the specific role didn't pan out but the recruiter might surface you for the next one.</p>

    <h2>Common mistakes</h2>
    <ul>
      <li><strong>&ldquo;Just checking in.&rdquo;</strong> The phrase signals neediness without saying it. Replace with the specific timeline reference.</li>
      <li><strong>Re-pitching yourself.</strong> The follow-up isn't another interview. One sentence of value is enough; longer reads as desperate.</li>
      <li><strong>Following up too soon.</strong> Less than 3 business days from the interview signals impatience and undermines the message.</li>
      <li><strong>No easy out.</strong> Without the explicit &ldquo;no problem if the timeline has shifted,&rdquo; the follow-up reads as accusatory even when worded gently.</li>
      <li><strong>Three or more follow-ups.</strong> Diminishing returns hits hard by message 3. After two follow-ups with no reply, the answer is no.</li>
      <li><strong>Following up on LinkedIn before email.</strong> Email is the channel they chose; respect it. LinkedIn becomes appropriate only after email has run its course.</li>
    </ul>

    <h2>Where to go from here</h2>
    <p>Free tools:</p>
    <ul>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-thank-you-email-after-interview.html">thank-you email prompt</a> &mdash; for the 24-hour email.</li>
      <li>The <a href="/prompts/best-chatgpt-prompt-for-follow-up-email-after-no-response.html">follow-up email prompt</a> &mdash; for the first and second follow-ups.</li>
    </ul>
    <p>The deeper version with the follow-up at 5/12/19 days that doubles response rates: <a href="/bundle-cover-letter.html">bundle cover letter module</a> (the follow-up sequence is included there).</p>
    """,
}


ARTICLES_META = [
    {
        "slug": "how-to-tailor-a-resume-with-chatgpt",
        "title": "How to Tailor a Resume with ChatGPT in 20 Minutes",
        "og_title": "How to tailor a resume with ChatGPT",
        "desc": "The exact 5-step workflow for tailoring your resume to a specific job description in 20 minutes &mdash; with the keyword-coverage audit, the bullet-rewrite prompts, and the AI-tell scan that catches generic phrasing before you send.",
        "h1": "How to tailor a resume with ChatGPT in 20 minutes",
        "subtitle": "The 5-step workflow that turns a 45-minute manual tailoring job into a 20-minute ChatGPT-assisted one &mdash; without producing the generic AI resume that recruiters cut in 8 seconds.",
    },
    {
        "slug": "how-to-prepare-for-a-behavioral-interview-with-chatgpt",
        "title": "How to Prepare for a Behavioral Interview with ChatGPT",
        "og_title": "How to prep behavioral interviews with ChatGPT",
        "desc": "Use ChatGPT as a mock interviewer, not a study guide. The 5-step workflow for prepping behavioral rounds with feedback &mdash; including the SCAR-T story variant that scores 1.5x higher than vanilla STAR.",
        "h1": "How to prepare for a behavioral interview with ChatGPT",
        "subtitle": "Most candidates use ChatGPT to memorize answers and end up sounding rehearsed. The workflow that actually works treats the model as a mock interviewer, not a study guide.",
    },
    {
        "slug": "how-to-write-a-linkedin-headline-with-chatgpt",
        "title": "How to Write a LinkedIn Headline with ChatGPT (The 3-Part Formula)",
        "og_title": "How to write a LinkedIn headline with ChatGPT",
        "desc": "The 4-step process for writing a LinkedIn headline that shows up in recruiter searches and gets clicked &mdash; with the 3-part formula, the keyword test, and the 10-variant generation prompt.",
        "h1": "How to write a LinkedIn headline with ChatGPT",
        "subtitle": "Your LinkedIn headline is the highest-leverage 220 characters in your job search. The 4-step process and the 3-part formula that gets it right.",
    },
    {
        "slug": "how-to-negotiate-salary-with-chatgpt",
        "title": "How to Negotiate Salary with ChatGPT (Step-by-Step)",
        "og_title": "How to negotiate salary with ChatGPT",
        "desc": "The 5-step salary negotiation workflow that's added 5 figures to my own offers &mdash; comp research, BATNA worksheet, counter number, the counter email prompt, and how to handle the &ldquo;they said no.&rdquo;",
        "h1": "How to negotiate salary with ChatGPT",
        "subtitle": "Salary negotiation is the highest-ROI 20-minute conversation in your career. The workflow that adds $5-15K to most offers &mdash; including the parts ChatGPT can't help with.",
    },
    {
        "slug": "how-to-follow-up-after-an-interview-without-being-needy",
        "title": "How to Follow Up After an Interview Without Being Needy",
        "og_title": "How to follow up after an interview",
        "desc": "The 5-step follow-up cadence that doubles your callback rate without crossing into pestering. Includes the 24-hour thank-you, the first and second follow-ups, and what to do after.",
        "h1": "How to follow up after an interview without being needy",
        "subtitle": "Most candidates either skip the follow-up (signal: low interest) or do it badly (signal: needy). The cadence that signals continued interest without pestering.",
    },
]


def main():
    written = []
    for meta in ARTICLES_META:
        body = ARTICLE_BODIES[meta["slug"]].strip()
        html = TEMPLATE
        html = html.replace("@@TITLE@@", meta["title"])
        html = html.replace("@@OG_TITLE@@", meta["og_title"])
        html = html.replace("@@DESC@@", meta["desc"])
        html = html.replace("@@H1@@", meta["h1"])
        html = html.replace("@@SUBTITLE@@", meta["subtitle"])
        html = html.replace("@@SLUG@@", meta["slug"])
        html = html.replace("@@BODY@@", body)
        html = html.replace("@@SCHEMA@@", schema(meta["title"], meta["desc"], meta["slug"]))
        out = ARTICLES / f"{meta['slug']}.html"
        out.write_text(html)
        written.append(out.name)
    print(f"Wrote {len(written)} articles:")
    for w in written:
        print(f"  {w}")


if __name__ == "__main__":
    main()
