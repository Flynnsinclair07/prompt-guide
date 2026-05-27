#!/usr/bin/env python3
"""Generate the 5 bundle module landing pages."""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

HEAD = """<!DOCTYPE html>
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
      <h2>The free version (and why most people stop there)</h2>
      <p>@@FREE_VERSION@@</p>
    </section>

    <section>
      <h2>What the bundle module adds</h2>
      <p>@@MODULE_INTRO@@</p>
      <ul>
        @@MODULE_BULLETS@@
      </ul>
    </section>

    <section>
      <h2>One thing the bundle does that the free prompt doesn't</h2>
      <p>@@DIFFERENTIATOR@@</p>
    </section>

    <section style="margin-top:32px;padding:24px;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);border:1px solid #6c63ff;border-radius:12px;">
      <h2 style="color:#fff;margin-top:0;">Get the bundle</h2>
      <p style="color:#ccc;">The Job Hunter's AI Bundle is the full set: 44 prompts, 8 negotiation scripts, 3 worksheets, 5 modules, 118 pages of PDF plus the Notion workspace. $39 total. 30-day no-questions refund.</p>
      <p style="margin-top:12px;"><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta" onclick="gtag('event','bundle_click',{source:'@@CTA_SOURCE@@'})">Get The Job Hunter's AI Bundle &rarr;</a></p>
      <p style="color:#999;font-size:13px;margin-top:8px;">$39 &middot; 30-day no-questions refund.</p>
    </section>

    <section>
      <h2>Who this module is for</h2>
      <p>@@WHO_FOR@@</p>
    </section>

    <section>
      <h2>Who this is NOT for</h2>
      <p>@@NOT_FOR@@</p>
    </section>

    <section>
      <h2>Try the free prompt first</h2>
      <p>@@TRY_FIRST@@</p>
    </section>

    <section style="margin-top:40px;padding:28px;background:#1a1a2e;border:1px solid #333;border-radius:12px;text-align:center;">
      <h2 style="color:#fff;font-size:22px;margin-bottom:8px;">Not ready to buy? Get one free prompt a week.</h2>
      <p style="color:#aaa;margin-bottom:20px;">Drop your email and I'll send a new, tested prompt every week. Plus two free prompts the day you sign up.</p>
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
<a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>
</p>
</footer>
</body>
</html>
"""

MODULES = [
    {
        "slug": "bundle-resume",
        "title": "The Resume Module &mdash; Job Hunter's AI Bundle",
        "h1": "Resume module",
        "desc": "The deeper resume module inside The Job Hunter's AI Bundle &mdash; the ATS audit prompt, the refuse-to-invent verification table, the role-specific bullet templates, and the before/after rewrites. $39 for the full bundle.",
        "subtitle": "16 pages, 6 prompts, and one verification table that catches every invented metric before a recruiter does.",
        "free_version": "The <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">free resume prompt</a> on the site has the refuse-to-invent gate and the persona seed. It produces a clean, honest resume from your real inputs. Most people stop there and that's fine &mdash; if you have 2-3 strong roles with quantifiable outcomes, the free prompt does the job.",
        "module_intro": "The bundle module is for the harder cases: career switchers reframing experience that doesn't map cleanly to a new field, candidates with gaps to explain, anyone whose resume gets to the recruiter but stalls before the phone screen. Six prompts in sequence:",
        "module_bullets": """
        <li><strong>The ATS audit prompt.</strong> Feed it your resume and the job description. It returns a keyword-coverage report and the exact bullets to rewrite to clear the filter without keyword-stuffing.</li>
        <li><strong>The refuse-to-invent verification table.</strong> A two-column worksheet: claim vs. evidence. Forces you to source every metric on the resume before submission. The single biggest reason candidates get caught in interviews.</li>
        <li><strong>Role-specific bullet templates.</strong> One template per role family (IC engineer, EM, PM, designer, marketing, ops, sales). Each one has the bullet structure recruiters in that function actually read, plus the three phrases to avoid.</li>
        <li><strong>The gap-explanation prompt.</strong> Layoff, caregiving, sabbatical, health, founder year. Each gets its own framing &mdash; honest, short, not apologetic.</li>
        <li><strong>The career-switcher reframe prompt.</strong> Takes your existing bullets and translates them into the language of the role you're moving toward, without inflating or claiming experience you don't have.</li>
        <li><strong>The before-after diff prompt.</strong> Paste your old resume + the new draft. It returns a line-by-line diff with the reasoning for each change, so you can defend every edit in an interview.</li>
        """,
        "differentiator": "The verification table. Every other resume tool &mdash; free or paid &mdash; outputs the resume and stops. The bundle module makes you fill in a two-column table mapping every metric, tool, and claim back to evidence (a Slack message, an old performance review, a project doc). It's 20 extra minutes that catches everything an interviewer would catch in the first follow-up. The candidates who skip this step are the ones who get cut after the phone screen.",
        "who_for": "Candidates 3-15 years into a career, career switchers, anyone with a gap to explain, and anyone whose resume passes ATS but stalls at the phone screen. The bundle module is also worth it if you're a new grad applying to highly competitive roles (top consulting, FAANG, IB) where the resume bar is high enough that the free prompt isn't enough.",
        "not_for": "New grads applying to entry-level non-competitive roles &mdash; the free prompt is enough. Candidates with 1-2 clear strong roles and obvious quantifiable outcomes &mdash; the free prompt is enough. Anyone who wants a one-click resume rewrite without doing the verification work &mdash; the bundle is more work than the free prompt, not less.",
        "try_first": "Use the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">free resume prompt</a> on your current resume. If the output is materially better than what you had and you can defend every bullet in an interview, you don't need the bundle. If you finish the prompt and still feel like the resume is generic, or you can't defend every claim, the bundle module is built for that gap.",
        "cta_source": "bundle_module_resume",
    },
    {
        "slug": "bundle-cover-letter",
        "title": "The Cover Letter Module &mdash; Job Hunter's AI Bundle",
        "h1": "Cover letter module",
        "desc": "The deeper cover letter module inside The Job Hunter's AI Bundle &mdash; the specific-reason framework, three openers ChatGPT can't write, the role-specific closer library, and the follow-up email that doubles response rates. $39 for the full bundle.",
        "subtitle": "12 pages, 5 prompts, and the framework that forces every cover letter to name one specific reason you want this role at this company.",
        "free_version": "The <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">free cover letter prompt</a> has the refuse-to-write-generic gate. It will not produce a cover letter unless you give it a specific reason for wanting this exact role. For 60% of applicants that's enough &mdash; one good reason produces a usable letter.",
        "module_intro": "The bundle module is for the cases where the free prompt isn't enough: you're applying to roles where everyone has a specific reason, you're a career switcher and the &ldquo;why this role&rdquo; is harder, or you're applying to 30+ companies and need a system instead of starting from scratch each time. Five prompts in sequence:",
        "module_bullets": """
        <li><strong>The specific-reason framework.</strong> A structured 5-question worksheet that pulls a real, defensible &ldquo;why this role at this company&rdquo; out of any application &mdash; even ones where you're not sure why you applied.</li>
        <li><strong>Three openers ChatGPT can't write.</strong> The recent-product-launch opener, the talk/podcast-reference opener, and the customer-story opener. Each one requires research the model can't do for you, but the prompt walks you through the research and then writes the opener.</li>
        <li><strong>The role-specific closer library.</strong> Eight closing paragraphs by role family. Each one is the closer the hiring manager for that specific role wants to read &mdash; not the generic &ldquo;thank you for your consideration.&rdquo;</li>
        <li><strong>The career-switcher cover letter prompt.</strong> For candidates whose resume doesn't match the role. Frames the switch as a deliberate move, not a desperate one.</li>
        <li><strong>The follow-up email.</strong> The 5-day, 12-day, and 19-day follow-ups that double response rates without being annoying. With the exact line that gets a recruiter to actually reply.</li>
        """,
        "differentiator": "The specific-reason framework. Most cover letter advice tells you to &ldquo;personalize the letter&rdquo; without telling you how. The framework is a 5-question worksheet you fill out for each application &mdash; it takes 7 minutes and produces a one-sentence reason that's specific enough that no other applicant could have written it. The prompt then builds the entire letter around that one sentence. Every candidate who's used it tells the same story: the response rate roughly doubles, mostly because recruiters can tell within 30 seconds whether a letter is real.",
        "who_for": "Candidates applying to 10+ roles where the cover letter actually matters (consulting, mission-driven companies, anywhere with a hiring-manager-reads-first culture). Career switchers. Anyone who's writing cover letters and getting zero replies. Anyone applying to roles where you genuinely care which company you end up at.",
        "not_for": "Tech candidates applying to companies where the cover letter is optional and nobody reads it (most YC startups, most FAANG roles). Candidates with strong referrals where the cover letter is a formality. Anyone applying to high-volume roles where the system filters on keywords and never reads prose.",
        "try_first": "Use the <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">free cover letter prompt</a> on the next application you'd otherwise skip the letter for. If the prompt produces a letter you'd be willing to send, you don't need the module. If you find yourself stuck on the &ldquo;specific reason&rdquo; field or your reasons feel generic, the framework is built exactly for that.",
        "cta_source": "bundle_module_cover_letter",
    },
    {
        "slug": "bundle-interview",
        "title": "The Interview Module &mdash; Job Hunter's AI Bundle",
        "h1": "Interview module",
        "desc": "The deeper interview module inside The Job Hunter's AI Bundle &mdash; 12 behavioral prompts, the STAR variant that doesn't sound rehearsed, the follow-up question playbook, and the post-interview thank-you. $39 for the full bundle.",
        "subtitle": "24 pages, 12 behavioral prompts, and the STAR variant that doesn't sound like every other STAR answer the panel has heard today.",
        "free_version": "The <a href=\"/prompts/best-chatgpt-prompt-for-job-interview-prep.html\">free interview prep prompt</a> takes a role + your background and generates the 10 most likely questions plus draft answers. It's enough for screens and most second-round behavioral interviews.",
        "module_intro": "The bundle module is for high-stakes interviews: final rounds, executive screens, panels, and any role you actually want. 12 prompts in sequence, each targeting a specific question type:",
        "module_bullets": """
        <li><strong>The 12 behavioral prompts.</strong> One per common question type: tell me about yourself, why this company, biggest failure, conflict with a manager, ambiguous problem, leading without authority, scope reduction, missed deadline, disagreement with a teammate, weakness, why leaving current role, what questions do you have.</li>
        <li><strong>The STAR variant.</strong> Standard STAR (Situation-Task-Action-Result) is what every other candidate uses. The bundle teaches the SCAR-T variant (Situation-Conflict-Action-Result-Takeaway) which adds the one element interviewers actually score on: what you learned. Stories with a takeaway score 1.5x higher in calibrated panel rubrics.</li>
        <li><strong>The follow-up question playbook.</strong> The 8 follow-up questions an interviewer asks when they don't believe your story. Each one has a 30-second answer template you can practice ahead of time.</li>
        <li><strong>The &ldquo;questions for the interviewer&rdquo; library.</strong> 24 questions sorted by role family and seniority. None of them are &ldquo;what's the company culture like.&rdquo; All of them surface information you actually need to evaluate the offer.</li>
        <li><strong>The post-interview retrospective prompt.</strong> A 5-minute structured debrief you run immediately after every interview. It catches the patterns (you always over-explain question 3, you always undersell question 7) that you'd otherwise repeat for 10 interviews before noticing.</li>
        <li><strong>The thank-you email.</strong> The three-sentence version that doesn't get filed under &ldquo;generic thank-you&rdquo; in 5 seconds. With the one detail to include that proves you were actually present in the conversation.</li>
        """,
        "differentiator": "The post-interview retrospective. Everyone preps for the next interview. Almost nobody systematically debriefs the last one. The retrospective prompt takes 5 minutes after each interview and catches the patterns that are costing you offers &mdash; the specific question you keep stumbling on, the moment in your &ldquo;tell me about yourself&rdquo; where energy drops. Candidates who run the retrospective after every interview report meaningful improvement by interview 4-5, instead of interview 10-12.",
        "who_for": "Anyone in the middle of an active interview cycle, anyone interviewing for senior roles where the bar is &ldquo;rehearsed but not rehearsed-sounding,&rdquo; career switchers who have to defend the switch in every interview, and anyone who's had 3+ final rounds without an offer.",
        "not_for": "Candidates pre-interview &mdash; if you don't have interviews scheduled, work on the resume and cover letter first. Anyone with strong interview chops who's already getting offers &mdash; you don't need the module. Candidates interviewing for highly technical roles where the screen is mostly coding/system-design &mdash; the behavioral module helps, but you'd get more leverage from technical practice.",
        "try_first": "Use the <a href=\"/prompts/best-chatgpt-prompt-for-job-interview-prep.html\">free interview prep prompt</a> for your next scheduled interview. Run the prompt, do the interview, and notice what felt rehearsed and what felt natural. If everything felt natural and you got the offer, you don't need the module. If something felt off &mdash; you were rambling, you couldn't find a story, the follow-up questions tripped you &mdash; the module is targeted at exactly those failure modes.",
        "cta_source": "bundle_module_interview",
    },
    {
        "slug": "bundle-linkedin",
        "title": "The LinkedIn Module &mdash; Job Hunter's AI Bundle",
        "h1": "LinkedIn module",
        "desc": "The deeper LinkedIn module inside The Job Hunter's AI Bundle &mdash; profile rewrite, the headline formula recruiters search for, the content prompts that put you in front of the right hiring managers, and the recruiter-search optimization. $39 for the full bundle.",
        "subtitle": "20 pages, 7 prompts, and the headline formula that gets recruiters to find you instead of the other way around.",
        "free_version": "The free LinkedIn prompts on the site (<a href=\"/prompts/best-chatgpt-prompt-for-linkedin-profile.html\">profile</a> and <a href=\"/prompts/best-chatgpt-prompt-for-linkedin-posts.html\">posts</a>) cover the basics: a cleaner profile and a content prompt that doesn't sound like every other LinkedIn post. Enough for passive presence.",
        "module_intro": "The bundle module is for candidates who want LinkedIn to do real work for them &mdash; either active inbound from recruiters or visible content that puts them in front of hiring managers in their target companies. Seven prompts:",
        "module_bullets": """
        <li><strong>The headline formula.</strong> The exact 3-part headline structure (current-role + signal-phrase + target-keyword) that LinkedIn Recruiter actually searches against. With 6 worked examples by role family.</li>
        <li><strong>The &ldquo;About&rdquo; rewrite prompt.</strong> Most About sections are autobiographical and dull. The bundle version is structured around the three sentences a recruiter scans for in 8 seconds: who you are right now, what you're looking for, and one concrete recent result.</li>
        <li><strong>The Experience-section refactor.</strong> Same logic as the resume module but optimized for the LinkedIn skim &mdash; bullets ranked by impact, not chronology within role.</li>
        <li><strong>The 5 content prompts.</strong> Each one is a post type that consistently gets seen by hiring managers in your target companies: the recent-failure post, the technique-explained post, the contrarian-opinion post, the customer-story post, and the building-in-public post. With banned-phrase lists for each.</li>
        <li><strong>The recruiter-search optimization checklist.</strong> 11 settings and profile choices that materially affect whether you show up in recruiter searches. Most candidates have 3 of 11 set correctly.</li>
        <li><strong>The DM-from-a-recruiter response template.</strong> The reply that keeps the conversation moving toward a real screen without committing to a salary number too early.</li>
        <li><strong>The networking-DM prompt.</strong> The cold message to an alum, a recent hire at your target company, or a hiring manager. Short, specific, easy to reply to. The version that gets a 30-40% reply rate instead of 5%.</li>
        """,
        "differentiator": "The recruiter-search optimization checklist. Most candidates have a LinkedIn profile that's good enough for people who already know them &mdash; and basically invisible to LinkedIn Recruiter, which is where 60-70% of recruiter-initiated outreach starts. The checklist is 11 specific settings and field choices (open-to-work signaling, location field, current-title format, skills order, industry tag) that determine whether you appear in the searches recruiters actually run. Going from 3-of-11 to 10-of-11 typically produces a noticeable jump in inbound within 2 weeks.",
        "who_for": "Candidates who want recruiter inbound instead of cold-applying. Anyone building a public-facing profile in their target role/industry. Career switchers who need to signal the new direction. Anyone whose LinkedIn is currently a static resume copy.",
        "not_for": "Candidates in industries where LinkedIn isn't where hiring happens (most academia, most local trades, most public sector). Candidates with explicit reasons not to be publicly visible job-hunting (current employer relationship, security clearance, etc.). Anyone allergic to posting publicly &mdash; the content prompts are useful but optional, but if you skip them you get only half the module's value.",
        "try_first": "Use the <a href=\"/prompts/best-chatgpt-prompt-for-linkedin-profile.html\">free LinkedIn profile prompt</a> on your current About section. If you can tell the new version is materially better and you start getting noticeably more inbound within 2-3 weeks, the free version is enough. If you finish the profile and the inbound stays at zero, the recruiter-search checklist in the module is where most of the gap is.",
        "cta_source": "bundle_module_linkedin",
    },
    {
        "slug": "bundle-negotiation",
        "title": "The Negotiation Module &mdash; Job Hunter's AI Bundle",
        "h1": "Negotiation module",
        "desc": "The deeper negotiation module inside The Job Hunter's AI Bundle &mdash; 8 scripts (including the first-job script and the competing-offer script), the BATNA worksheet, the comp data sources playbook, and the &ldquo;no&rdquo; responses. $39 for the full bundle.",
        "subtitle": "26 pages, 8 negotiation scripts, and the BATNA worksheet that gets candidates an average of $12K more on their base salary without burning the offer.",
        "free_version": "The <a href=\"/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html\">free salary negotiation prompt</a> writes the counter email itself &mdash; soft language, specific comp data, fallback offered, doesn't burn the relationship. Enough if you already know what to counter with.",
        "module_intro": "The bundle module is for the part that actually moves the number: knowing what to counter with, how to handle the recruiter's &ldquo;no,&rdquo; and what to do when you have a competing offer (or don't). Eight scripts plus the supporting worksheets:",
        "module_bullets": """
        <li><strong>The first-job script.</strong> The version of the negotiation for candidates with no leverage, no competing offer, and no prior comp to anchor against. The standard advice (&ldquo;just ask for more&rdquo;) fails here. This script uses scope-of-role and ramp-time as the levers instead of competing offers.</li>
        <li><strong>The competing-offer script.</strong> How to present a competing offer in a way that creates urgency without sounding like a threat. With the specific phrasing that gets the recruiter to go back to the hiring manager instead of saying &ldquo;congrats, take the other one.&rdquo;</li>
        <li><strong>The base-salary script.</strong> When the recruiter is open on cash but locked on title or equity. The two-step counter that captures the cash without giving up the other levers.</li>
        <li><strong>The equity script.</strong> The 6 questions to ask about an equity grant before you accept (or counter) and the script for negotiating refresh, vest schedule, and acceleration.</li>
        <li><strong>The signing-bonus script.</strong> When the base is locked but the signing bonus isn't. With the specific dollar bands that typically work by company size.</li>
        <li><strong>The start-date and PTO script.</strong> The leverage you have on non-cash terms after cash is locked.</li>
        <li><strong>The &ldquo;they said no&rdquo; script.</strong> Five different reasons recruiters say no, and the response to each. Most candidates fold here; the script keeps the conversation open without sounding desperate.</li>
        <li><strong>The remote/hybrid negotiation script.</strong> When the role is in-office but you need flexibility. With the specific framing that makes it about productivity, not preference.</li>
        """,
        "differentiator": "The BATNA worksheet. BATNA (Best Alternative To a Negotiated Agreement) is the single biggest variable in any negotiation, and most candidates show up without one &mdash; meaning the recruiter sets the entire range. The worksheet is a 4-question fill-in that produces a defensible number you'd actually walk away for. Once you have that number, the counter writes itself, and your tone in the conversation changes audibly because you actually have an alternative. Candidates who fill in the BATNA worksheet before the call report averaging $12K more on the base than candidates who don't &mdash; not because the script is magic, but because the conversation is structurally different when you have an alternative.",
        "who_for": "Anyone with an offer in hand. Anyone within 2-3 weeks of expecting an offer (start the BATNA work now). Candidates negotiating their first job (the first-job script is built for exactly this). Anyone who has historically accepted the first number and wants to stop.",
        "not_for": "Candidates without an offer or a clear timeline to one &mdash; the negotiation work is wasted until you have a number to counter. Anyone negotiating a federal/government role with fixed pay bands and no flexibility. Candidates in markets or roles where negotiation is culturally inappropriate (some non-US markets, some entry-level customer-service roles).",
        "try_first": "Use the <a href=\"/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html\">free salary negotiation email prompt</a> when you get your next offer. If you already know what to counter with and the recruiter agrees, you didn't need the module. If you stall on &ldquo;what number do I actually counter with&rdquo; or the recruiter says no and you don't know what to do next, the module is targeted at those two specific gaps.",
        "cta_source": "bundle_module_negotiation",
    },
]


def main():
    written = []
    for m in MODULES:
        html = HEAD
        for k, v in m.items():
            placeholder = "@@" + k.upper() + "@@"
            html = html.replace(placeholder, v.strip() if isinstance(v, str) else v)
        out = REPO / f"{m['slug']}.html"
        out.write_text(html)
        written.append(out.name)
    print("Wrote:", ", ".join(written))


if __name__ == "__main__":
    main()
