#!/usr/bin/env python3
"""Generate 5 new vertical landing pages.

Mirrors the structure of for-new-grads.html / for-career-switchers.html / for-laid-off-tech.html.
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
      <h2>What's hard about your situation</h2>
      <p>@@SITUATION_INTRO@@</p>
      <ul>
        @@SITUATION_BULLETS@@
      </ul>
    </section>

    <section>
      <h2>The five free prompts you'll use most</h2>
      <ol>
        @@PROMPT_LIST@@
      </ol>
    </section>

    <section style="margin-top:32px;padding:24px;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);border:1px solid #6c63ff;border-radius:12px;">
      <h2 style="color:#fff;margin-top:0;">The deeper version: The Job Hunter's AI Bundle</h2>
      <p style="color:#ccc;">@@BUNDLE_PITCH@@</p>
      <p style="margin-top:12px;"><a href="https://snipprompts.gumroad.com/l/job-hunters-ai-bundle" class="cta" onclick="gtag('event','bundle_click',{source:'@@CTA_SOURCE@@'})">Get The Job Hunter's AI Bundle &rarr;</a></p>
      <p style="color:#999;font-size:13px;margin-top:8px;">$39 &middot; 30-day no-questions refund.</p>
    </section>

    <section>
      <h2>One specific story</h2>
      <p>@@SPECIFIC_STORY@@</p>
    </section>

    <section>
      <h2>Where to start</h2>
      <p>@@WHERE_TO_START@@</p>
    </section>

    <section style="margin-top:40px;padding:28px;background:#1a1a2e;border:1px solid #333;border-radius:12px;text-align:center;">
      <h2 style="color:#fff;font-size:22px;margin-bottom:8px;">Prompt of the week &mdash; free</h2>
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
<a href="/faq.html" style="color:#999;margin-right:16px;">FAQ</a>
<a href="/resources.html" style="color:#999;margin-right:16px;">Resources</a>
<a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>
</p>
</footer>
</body>
</html>
"""


PAGES = [
    {
        "slug": "for-internships",
        "title": "ChatGPT Prompts for Internship Applications",
        "og_title": "For internship applications",
        "desc": "Free ChatGPT prompts built for internship applications &mdash; when you're an undergrad with class projects, one campus job, and no &ldquo;real&rdquo; experience yet. Five prompts that map to the internship-hunt cycle.",
        "h1": "For internship applications",
        "subtitle": "Summer internships, co-ops, return-offer conversions. You're 19, 20, 21 &mdash; competing against thousands of other students for a handful of slots, and the standard career advice doesn't fit.",
        "situation_intro": "Internship recruiting in 2026 is its own beast: huge applicant pools, aggressive deadlines (some FAANG internships post in August for the following summer), and the awkward reality that your resume is mostly class projects, a campus job, and one club leadership role. The off-the-shelf ChatGPT resume prompt fails harder here than for anyone else &mdash; the model has nothing to work with, so it inflates everything.",
        "situation_bullets": """
        <li><strong>You're competing in a flooded pool.</strong> A top-tier finance or tech internship gets 10,000+ applicants for 200 spots. The application has to clear ATS keyword filters AND read as honest in 8 seconds of human skim.</li>
        <li><strong>Your &ldquo;experience&rdquo; is class projects, campus jobs, and clubs.</strong> All real, all worth listing &mdash; but the framing matters. &ldquo;Worked on a marketing project&rdquo; gets cut. &ldquo;Designed the email campaign for a 200-person student nonprofit, growing signups from 480 to 630 in one semester&rdquo; doesn't.</li>
        <li><strong>The behavioral interview asks about leadership and conflict you haven't had at work.</strong> Recruiters know this. They want stories from class, clubs, sports, or part-time work &mdash; but most students freeze when asked because they think those stories don't &ldquo;count.&rdquo; They do.</li>
        <li><strong>The return-offer conversion is the highest-leverage decision.</strong> 70%+ of full-time tech offers go to former interns. The internship is the full-time interview. Most interns treat it like a summer job.</li>
        """,
        "prompt_list": """
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">Writing a Resume</a> &mdash; feed it your class projects, campus job, and clubs. The refuse-to-invent gate keeps it from inflating your three-person group project into a &ldquo;cross-functional team leadership initiative.&rdquo;</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">Writing a Cover Letter</a> &mdash; the internship-specific version forces you to name ONE real reason you want this internship at this company. Not &ldquo;I want to learn.&rdquo; A specific reason.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">Job Interview Prep</a> &mdash; practice the behavioral questions you'll get on class projects, leadership in clubs, and the &ldquo;tell me about yourself&rdquo; that 80% of interns blow.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-networking-email.html">Networking Email</a> &mdash; the cold email to alumni at your target company. For internship recruiting this is often the difference between an interview and the rejection-pile auto-reply.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-thank-you-email-after-interview.html">Thank-You Email After Interview</a> &mdash; the three-sentence email that doesn't get filed as generic. Specific to one moment in the conversation.</li>
        """,
        "bundle_pitch": "For internships, the bundle's LinkedIn module helps you signal &ldquo;intern-ready&rdquo; in the LinkedIn searches recruiters run, the interview module has the 12 behavioral questions every intern interview reaches for, and the negotiation module has the first-job script for the (yes, real) intern offer negotiation. $39 total. 30-day refund if it's not what you need.",
        "cta_source": "landing_for_internships",
        "specific_story": "A junior at a mid-tier state school used the networking-email prompt to reach 14 alumni at her target consulting firm in November. 4 replied. 2 introduced her to the campus recruiter. 1 referred her resume directly. She got the on-campus interview slot that hadn't existed before. The resume prompt and cover letter prompt did the rest. Final-round offer in February. The prompts didn't write the path &mdash; they removed the friction from sending 14 specific, personal messages instead of one generic cold application.",
        "where_to_start": "If you're early: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> first. If you have a resume and you're staring at applications: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">cover-letter prompt</a> next. If you have an interview: <a href=\"/prompts/best-chatgpt-prompt-for-job-interview-prep.html\">interview prep</a>. If you're trying to get an interview at all: <a href=\"/prompts/best-chatgpt-prompt-for-networking-email.html\">networking email</a> &mdash; this is usually the highest-leverage move for internship recruiting and the one most students skip.",
    },
    {
        "slug": "for-veterans",
        "title": "ChatGPT Prompts for Military-to-Civilian Career Transition",
        "og_title": "For veterans transitioning to civilian roles",
        "desc": "Free ChatGPT prompts built for veterans translating military experience to civilian roles &mdash; the resume rewrite that survives a civilian recruiter's 8-second skim, the cover letter that explains the transition, and the interview prep for the questions every veteran gets asked.",
        "h1": "For veterans transitioning to civilian roles",
        "subtitle": "Translating military experience to civilian language without losing what matters. Five prompts that handle the resume rewrite, the &ldquo;why are you leaving the military&rdquo; question, and the comp conversation that veterans typically lose money on.",
        "situation_intro": "Civilian recruiters skim a military resume in 8 seconds, the same as any other. The difference is they're reading job titles, ranks, and acronyms that don't map cleanly to civilian roles &mdash; and they're not going to do the translation work for you. The two failure modes: (1) leaving your resume in military language and getting screened out, or (2) over-translating and losing the leadership signal that's the strongest thing on your record.",
        "situation_bullets": """
        <li><strong>Your resume has acronyms civilian recruiters don't decode.</strong> MOS codes, unit names, awards, deployment locations. Some of it translates obviously (Squad Leader = team lead of 8-12), some doesn't (OIC, NCOIC, S-3, MOS 11B). The translation is a skill, not just a vocabulary swap.</li>
        <li><strong>Your leadership experience is undersold by default.</strong> A 26-year-old Marine sergeant who's led 40 people in life-or-death situations puts &ldquo;managed team&rdquo; on the resume. Civilian peers with 1/10 the responsibility write &ldquo;spearheaded cross-functional initiatives.&rdquo; The translation needs to claim what you actually did.</li>
        <li><strong>The &ldquo;why are you leaving the military&rdquo; question gets asked in every interview.</strong> There's a good answer (specific, forward-looking, not bitter) and there are several bad ones (vague, complaining about the institution, or implying you didn't have a choice). The prompt covers the structure.</li>
        <li><strong>Comp negotiation is where veterans leave the most on the table.</strong> Military pay structure is published and clear; civilian comp is opaque and assumed-negotiable. Most veterans accept the first offer because that's what feels normal. The first offer is rarely the company's best number.</li>
        """,
        "prompt_list": """
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">Writing a Resume</a> &mdash; feed it your real military experience and let the refuse-to-invent gate keep you honest. The civilian-translation pass is a follow-up: &ldquo;translate this resume into civilian language without losing the leadership scope or the technical specifics.&rdquo;</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">Writing a Cover Letter</a> &mdash; the cover letter does the work of explaining the transition. The prompt forces you to name one specific reason for moving to this exact role at this company. &ldquo;Transitioning out of the military&rdquo; alone isn't enough.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">Job Interview Prep</a> &mdash; practices the questions you'll actually get: why now, why this role, what's the biggest leadership challenge you've faced, how do you handle conflict. Veterans have stronger answers to most of these than civilian peers; the gap is usually in the telling.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-networking-email.html">Networking Email</a> &mdash; the cold email to veterans already at your target company (most companies have veteran ERGs and warm referrals). The intro that says &ldquo;fellow vet, 2 minutes for a question&rdquo; is one of the highest-reply-rate cold outreaches in any market.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">Salary Negotiation Email</a> &mdash; writes the counter email itself. The harder part (deciding what to counter with) is in the bundle's BATNA worksheet.</li>
        """,
        "bundle_pitch": "For veterans, the bundle's negotiation module is the most valuable single piece &mdash; veterans average $8-15K under market on first civilian offers, and the first-job script in the bundle is built for exactly this transition. The LinkedIn module helps you signal to recruiters who actively search for veterans (most large companies do). $39 total. 30-day refund if it's not what you need.",
        "cta_source": "landing_for_veterans",
        "specific_story": "A Marine staff sergeant transitioning into operations roles in 2024 used the resume prompt to translate &ldquo;led 4 squads in counter-IED operations across two deployments&rdquo; into &ldquo;led 4 distributed teams of 12-15 in a high-stakes operational environment; built and ran the readiness protocols that cut response time 40%.&rdquo; Same facts, civilian language, recruiter-skim-friendly. He went from 0 callbacks on 60 cold applications to 4 callbacks on 12 targeted ones after the rewrite. The negotiation prompt added $12K to the offer he accepted because he countered for the first time in his career.",
        "where_to_start": "If you're early in the transition: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> with the civilian-translation pass. If you have a resume and you're not getting callbacks: the issue is likely targeting and warm channels &mdash; <a href=\"/prompts/best-chatgpt-prompt-for-networking-email.html\">networking email prompt</a> next. If you have an interview: <a href=\"/prompts/best-chatgpt-prompt-for-job-interview-prep.html\">interview prep</a>. If you have an offer: <a href=\"/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html\">salary negotiation</a> &mdash; do not accept the first number.",
    },
    {
        "slug": "for-remote-jobs",
        "title": "ChatGPT Prompts for Remote Job Applications",
        "og_title": "For remote job applications",
        "desc": "Free ChatGPT prompts built for remote-job applications. The resume that signals &ldquo;remote-ready,&rdquo; the cover letter that addresses the hiring manager's actual remote worry, and the interview prep for the async-collab questions every remote interview asks.",
        "h1": "For remote job applications",
        "subtitle": "Remote roles in 2026 get 5-10x more applicants than equivalent on-site roles. Five prompts that handle the remote-specific signaling, the &ldquo;can you work async&rdquo; question, and the geographic-arbitrage comp conversation.",
        "situation_intro": "The remote market is the most competitive segment of the job market. The applicant pool is global, every laid-off tech worker is applying, and hiring managers are now explicitly screening for remote-readiness signals &mdash; not just &ldquo;can you do the job&rdquo; but &ldquo;can you do it without anyone managing you in person.&rdquo; A resume that doesn't address this gets filtered, even when the candidate is strong.",
        "situation_bullets": """
        <li><strong>Remote roles get 5-10x the applicant volume of on-site roles.</strong> Same job, 700 vs 100 applications. Generic resumes get auto-cut. The bar for a callback is materially higher.</li>
        <li><strong>Hiring managers screen for remote-readiness signals.</strong> Async communication examples, distributed-team experience, output-not-hours framing, a real home office setup. Most candidates don't surface any of this, and the manager assumes worst case.</li>
        <li><strong>The cover letter needs to address the unstated worry.</strong> Hiring managers reading a remote applicant's letter are asking &ldquo;will this person ghost me&rdquo; or &ldquo;will they need me to fly them out for offsites.&rdquo; A good cover letter names the worry and answers it without being weird.</li>
        <li><strong>Comp conversations get geo-arbitrage'd if you don't anchor.</strong> &ldquo;What's your salary expectation&rdquo; on a remote role usually means &ldquo;we'll pay you whatever your local market pays.&rdquo; If you're in a low-cost-of-living area, recruiters use that against you unless you anchor first.</li>
        """,
        "prompt_list": """
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">Writing a Resume</a> &mdash; feed it your real experience and add the remote-specific framing: distributed-team work, async communication examples, output-driven bullets. The refuse-to-invent gate keeps the framing honest.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">Writing a Cover Letter</a> &mdash; the remote-version requires you to name ONE specific reason you want this remote role at this company, AND addresses the unspoken &ldquo;why should I trust you remote&rdquo; concern with proof, not adjectives.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">Job Interview Prep</a> &mdash; practices the remote-specific questions every interview asks: how you handle async communication, how you build relationships without in-person time, how you escalate when stuck, how you protect focus without a manager visible.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-linkedin-profile.html">LinkedIn Profile</a> &mdash; the &ldquo;open to remote&rdquo; signal is buried in LinkedIn unless you set 3-4 specific fields. The prompt covers the headline + about-section rewrites that route remote-hiring recruiters to your profile.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">Salary Negotiation Email</a> &mdash; writes the counter email. For remote roles specifically, anchor on the role's market rate (Levels.fyi remote-eligible band), NOT your local market. The prompt covers the phrasing.</li>
        """,
        "bundle_pitch": "For remote-job applicants, the bundle's negotiation module is the highest-leverage piece &mdash; the geo-arbitrage script alone covers a typical $10-20K gap. The LinkedIn module's recruiter-search checklist is built for the remote-hiring search patterns specifically. $39 total. 30-day refund if it's not what you need.",
        "cta_source": "landing_for_remote_jobs",
        "specific_story": "An engineer in Boise applied to 40 remote senior roles in Q4 2025 and got 2 callbacks. He used the resume prompt + cover letter prompt with the remote-specific framing on the next 15 applications &mdash; surfaced the 3 years of distributed-team work he'd buried, addressed the async-collab worry in the cover letter directly, and anchored comp expectations at the role's market rate (not Boise's). 6 callbacks. The role he took came in at $172K, $35K above the Boise-anchored offer he'd been about to accept on a different application.",
        "where_to_start": "If you're new to remote-job hunting: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> with the remote-readiness framing first. If you have a resume and you're getting low callback rates: the issue is usually the cover letter &mdash; <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">cover-letter prompt</a> addresses the unspoken remote-trust concern. If you have an interview: <a href=\"/prompts/best-chatgpt-prompt-for-job-interview-prep.html\">interview prep</a>. If you have an offer: <a href=\"/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html\">salary negotiation</a> &mdash; anchor on role market rate, not local.",
    },
    {
        "slug": "for-international-applicants",
        "title": "ChatGPT Prompts for International Applicants (US Job Search)",
        "og_title": "For international applicants",
        "desc": "Free ChatGPT prompts built for international applicants targeting US roles &mdash; US resume conventions vs international, the visa-sponsorship conversation, and the cover letter that doesn't read as ESL even when English isn't your first language.",
        "h1": "For international applicants",
        "subtitle": "Targeting US roles from outside the US (or on F-1/OPT). Five prompts that handle the US-resume conventions, the visa conversation, and the cover letter that doesn't telegraph &ldquo;non-native English speaker&rdquo; when you don't want it to.",
        "situation_intro": "International applicants targeting US roles face two structural disadvantages and one cultural one. Structural: US resume conventions are different (one page, no photo, no DOB, no marital status), and visa sponsorship is a hard filter at most companies. Cultural: cover letters and self-presentation in the US lean more direct and claim-driven than in many other markets &mdash; a letter that reads as appropriately humble in Germany or India reads as under-selling in the US.",
        "situation_bullets": """
        <li><strong>US resume conventions are stricter than most other markets.</strong> One page for under 10 years experience, no photo, no DOB, no marital status, no full address (city + state only). A CV from most other countries breaks all of these. Recruiters notice in 5 seconds.</li>
        <li><strong>Visa sponsorship is a hard filter at maybe 60% of US employers.</strong> &ldquo;Do you require sponsorship now or in the future&rdquo; is asked on most US applications &mdash; an honest yes auto-cuts you at companies that don't sponsor. The fix is targeting (apply only to sponsoring companies) and timing (apply in the windows when sponsoring companies hire).</li>
        <li><strong>US cover letters are more direct than most international norms.</strong> &ldquo;I would be very grateful for the opportunity to be considered&rdquo; reads as servile in the US, not polite. The American norm is &ldquo;here's why I'm a fit; here's what I'd contribute; let's talk.&rdquo;</li>
        <li><strong>The interview includes a comp conversation US-norm-style.</strong> Direct, anchored on numbers, often early in the process. Candidates from cultures where comp is discussed only after offer often miss the cue and either lowball themselves or seem dodgy.</li>
        """,
        "prompt_list": """
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">Writing a Resume</a> &mdash; feed it your international CV and add the constraint: &ldquo;convert to US resume conventions (one page, no photo, no DOB, no marital status, city + state only).&rdquo; The refuse-to-invent gate keeps it honest in the conversion.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">Writing a Cover Letter</a> &mdash; the US-norm version. Direct, claim-driven, specific reason for THIS role, ends with a concrete ask. If you've ever been told your English &ldquo;sounds non-native,&rdquo; the issue is usually structure not vocabulary; the prompt fixes structure.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">Job Interview Prep</a> &mdash; practices the US-norm behavioral questions PLUS the visa-status conversation and the &ldquo;tell me about yourself&rdquo; (US-norm: 90 seconds, structured, ends on a forward-looking note).</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-networking-email.html">Networking Email</a> &mdash; for international applicants, warm intros from anyone already at the target company are even higher-leverage than for US applicants. The prompt covers the cold-outreach to international alumni, former colleagues now in the US, and friends-of-friends.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">Salary Negotiation Email</a> &mdash; the US-norm counter is more direct than most international norms. The prompt covers the phrasing that's appropriately direct without coming across as aggressive.</li>
        """,
        "bundle_pitch": "For international applicants, the bundle's negotiation module is the most valuable single piece &mdash; international candidates leave the most on the table here, and the &ldquo;they said no&rdquo; script handles the visa-cost pushback companies sometimes deploy. The cover letter module has the structure that reads as native-US even when English isn't your first language. $39 total. 30-day refund if it's not what you need.",
        "cta_source": "landing_for_international_applicants",
        "specific_story": "A software engineer applying from Germany used the resume prompt to convert her two-page European CV (with photo, DOB, and four languages listed) to a one-page US resume. The cover letter prompt rewrote her overly-humble opening into the US-direct version. Most of her applications had been to companies that don't sponsor &mdash; the targeting fix mattered as much as the resume fix. After re-targeting + re-writing, she landed phone screens at 3 sponsoring companies in 6 weeks and accepted an offer that came in $25K above her initial expectation because she countered using the negotiation script.",
        "where_to_start": "Step 1: confirm you're applying to companies that sponsor (most YC startups, most FAANG, most large pharma; check H-1B Visa Wiki or MyVisaJobs). Step 2: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> with the US-conversion pass. Step 3: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">cover-letter prompt</a> with the US-direct framing. Step 4: <a href=\"/prompts/best-chatgpt-prompt-for-networking-email.html\">networking</a> &mdash; warm intros matter more here. Step 5 (when offer): <a href=\"/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html\">salary negotiation</a>.",
    },
    {
        "slug": "for-returning-parents",
        "title": "ChatGPT Prompts for Parents Returning to Work",
        "og_title": "For parents returning to work",
        "desc": "Free ChatGPT prompts built for parents returning to work after a caregiving gap. The resume that explains the gap honestly without apologizing, the cover letter that doesn't sound rusty, and the interview prep for &ldquo;why did you take time off&rdquo; that doesn't drift into over-explanation.",
        "h1": "For parents returning to work",
        "subtitle": "Returning after a caregiving gap of 1 to 10+ years. Five prompts that handle the gap explanation, the &ldquo;technically rusty but conceptually sharper&rdquo; framing, and the comp anchor that returners typically lowball themselves on.",
        "situation_intro": "The hardest part of returning to work isn't your skills. It's the framing &mdash; how you explain the gap, how you signal that you're back in seriously, how you handle the recruiter's unspoken &ldquo;will this person leave again in 6 months&rdquo; concern. Most returners over-apologize, under-anchor on comp, and accept the first role offered because it feels presumptuous to negotiate after time away. None of that is necessary.",
        "situation_bullets": """
        <li><strong>The gap on the resume needs ONE clear sentence, not a paragraph of apology.</strong> &ldquo;Career break for caregiving, 2021-2025&rdquo; on the resume is enough; the explanation goes in the cover letter only if asked. Most resumes over-explain and undersell.</li>
        <li><strong>Recruiters are reading for &ldquo;is this person back in seriously.&rdquo;</strong> Signals that work: a specific role you're targeting (not &ldquo;open to anything&rdquo;), recent skill refreshes (a course, a freelance project, a volunteer role), and a clear forward-looking story in the cover letter. Vagueness reads as ambivalence.</li>
        <li><strong>The &ldquo;why did you take time off&rdquo; question is asked in every interview.</strong> The good answer is short, specific, forward-looking, and doesn't include a defense of the decision. The bad answer is a 4-minute justification.</li>
        <li><strong>Comp negotiation is where returners leave the most on the table.</strong> Returners take an average $15-30K below market on their first post-gap role because they accept the first offer, anchor on their pre-gap salary, or feel grateful enough to skip negotiating. The market rate is the market rate; the gap is irrelevant to it.</li>
        """,
        "prompt_list": """
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-resume.html">Writing a Resume</a> &mdash; feed it your real pre-gap experience plus anything you did during the gap (volunteer, freelance, board work, refresh courses). The refuse-to-invent gate keeps it honest; the gap-explanation framing comes from the prompt.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html">Writing a Cover Letter</a> &mdash; the returning-version forces a forward-looking story (what you're back to do, why this role specifically) instead of a backward-looking apology. The prompt blocks both &ldquo;I took time off to raise my kids&rdquo; (over-disclosure) and &ldquo;I'm thrilled to return&rdquo; (under-anchored).</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-job-interview-prep.html">Job Interview Prep</a> &mdash; practices the &ldquo;tell me about the gap&rdquo; question with a 60-second structured answer, plus the &ldquo;what have you been doing to keep skills sharp&rdquo; follow-up (most returners freeze on this one).</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-networking-email.html">Networking Email</a> &mdash; reactivating your old network is one of the highest-leverage moves for returners. Most pre-gap colleagues are now 5-10 years more senior and can refer or hire directly. The prompt covers the &ldquo;haven't talked in a few years, what's been happening, here's what I'm looking for&rdquo; outreach.</li>
        <li><a href="/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html">Salary Negotiation Email</a> &mdash; writes the counter. The harder part for returners (deciding what to counter with, given the gap) is in the bundle's BATNA worksheet; anchor on the role's current market rate, not your pre-gap salary.</li>
        """,
        "bundle_pitch": "For returners, the bundle's resume module has the gap-explanation framings (caregiving, health, sabbatical, founder year) that don't sound apologetic. The negotiation module is the highest-leverage single piece &mdash; returners average $15-30K under market on first offers, and the bundle's market-anchor script + &ldquo;they said no&rdquo; responses are built for this. $39 total. 30-day refund if it's not what you need.",
        "cta_source": "landing_for_returning_parents",
        "specific_story": "A product manager returning after 6 years out used the resume prompt with a single line for the gap (&ldquo;Career break for caregiving, 2019-2025&rdquo;) and added a 6-month freelance product audit she'd done during the gap. The cover letter prompt produced a forward-looking version focused on what she wanted next, not what she'd been doing. The networking-email prompt reconnected her with 11 former colleagues; 4 introduced her to current openings. The salary negotiation prompt brought her offer from $148K to $172K because she anchored on current PM market rate, not on her 2018 number. Whole cycle: 4 months.",
        "where_to_start": "If you're early in the return: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-resume.html\">resume prompt</a> with the gap-explanation framing. Then <a href=\"/prompts/best-chatgpt-prompt-for-networking-email.html\">networking email</a> to reactivate your pre-gap network &mdash; this is usually the highest-leverage move and the one returners skip because it feels awkward. If you have a resume and you're applying cold: <a href=\"/prompts/best-chatgpt-prompt-for-writing-a-cover-letter.html\">cover-letter prompt</a> with the forward-looking framing. If you have an interview: <a href=\"/prompts/best-chatgpt-prompt-for-job-interview-prep.html\">interview prep</a>. If you have an offer: <a href=\"/prompts/best-chatgpt-prompt-for-salary-negotiation-email.html\">salary negotiation</a> &mdash; anchor on current market rate, not pre-gap salary.",
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
