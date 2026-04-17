"""Batch 4: 50 more pages. Shorter format to stay efficient."""
import sys
sys.path.insert(0, 'scripts')
from page_template import make_page

# Shorter format — each page still has all required sections but briefer
def short_page(slug, title, subtitle, prompt, example_out, amazon_kw, amazon_txt, related):
    how_to_use = [
        "Copy the prompt and replace the bracketed sections with your specific details",
        "Be as specific as possible — vague input produces vague output",
        "Paste into ChatGPT or Claude and review the result",
        "Iterate with follow-ups like 'make it shorter' or 'try a different angle'",
    ]
    tips = [
        "<strong>Give context.</strong> The more background you provide, the better the AI response.",
        "<strong>Ask for options.</strong> Request 3 versions and pick the strongest one.",
        "<strong>Iterate, don't accept.</strong> The first response is rarely the best.",
        "<strong>Edit in your voice.</strong> AI output should be a starting point, not the final.",
    ]
    return {
        "slug": slug, "title": title, "subtitle": subtitle, "prompt": prompt,
        "how_to_use": how_to_use, "example_output": example_out,
        "tips": tips, "amazon_keywords": amazon_kw, "amazon_text": amazon_txt,
        "related": related,
    }

PAGES = [
    short_page(
        "best-chatgpt-prompt-for-grant-writing",
        "Best ChatGPT Prompt for Grant Writing",
        "Write compelling grant proposals that win funding — for nonprofits, researchers, and artists.",
        """You are a professional grant writer who has secured $50M+ in funding. Write a grant proposal for me.

Organization: [NAME AND MISSION]
Grant opportunity: [FUNDER + AMOUNT + DEADLINE]
Project: [WHAT YOU'LL DO WITH THE FUNDING]
Problem you're solving: [THE NEED]
Target beneficiaries: [WHO BENEFITS AND HOW MANY]
Outcomes: [MEASURABLE RESULTS YOU'LL DELIVER]
Budget total: $[AMOUNT]

Write:
1. Executive summary (1 paragraph)
2. Statement of need (with data)
3. Project description
4. Goals and measurable outcomes
5. Budget narrative
6. Evaluation plan
7. Organizational capacity

Requirements: Match funder's priorities. Use active voice. Include specific numbers. No jargon.""",
        "<p><strong>Executive summary:</strong> Project Bloom addresses adolescent mental health gaps in rural Colorado through a peer-support program that will serve 400 teens annually...</p>",
        "grant+writing+nonprofit+book", "Grant Writing Books",
        [("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan"), ("best-chatgpt-prompt-for-copywriting", "Copywriting")]
    ),
    short_page(
        "best-chatgpt-prompt-for-personal-statement",
        "Best ChatGPT Prompt for Personal Statement",
        "Write a college or grad school personal statement that stands out — authentic, specific, and memorable.",
        """You are a college admissions consultant who has helped 500+ students get into top programs. Help me write my personal statement.

Applying to: [UNDERGRAD / GRAD SCHOOL / MBA / LAW / MED / OTHER]
Target schools: [LIST]
Intended major/program: [FIELD]
Word limit: [NUMBER]
A defining moment in my life: [STORY]
Why I want this field: [YOUR WHY]
What makes me unique: [DISTINCTIVE QUALITY OR EXPERIENCE]

Write:
1. An opening hook that drops the reader into a specific moment
2. The story that reveals who I am
3. How that connects to my field/goals
4. Why this specific school
5. A closing that looks forward

Requirements: Show, don't tell. Specific details beat abstract claims. No cliches ('I've always wanted to help people'). One clear theme throughout.""",
        "<p><strong>Opening:</strong> My grandmother couldn't read the pill bottle. She handed it to me, embarrassed, and asked what the small print said...</p>",
        "college+admissions+essay+book", "Admissions Books",
        [("best-chatgpt-prompt-for-essay-writing", "Essay Writing"), ("best-chatgpt-prompt-for-writing-a-cover-letter", "Writing a Cover Letter")]
    ),
    short_page(
        "best-chatgpt-prompt-for-scholarship-essay",
        "Best ChatGPT Prompt for Scholarship Essay",
        "Write a scholarship essay that wins — with a clear story, specific details, and a strong case for why you deserve the funding.",
        """You are a scholarship committee veteran who has reviewed 10,000+ applications. Help me write my scholarship essay.

Scholarship name: [NAME]
Amount: $[AMOUNT]
Essay prompt: [EXACT PROMPT]
Word limit: [NUMBER]
My background: [KEY DETAILS]
Financial need (if relevant): [BRIEF CONTEXT]
Academic interests: [FIELD]
Community involvement or leadership: [EXAMPLES]

Write a response that:
- Directly answers the prompt
- Opens with a specific moment, not a thesis statement
- Shows impact through concrete examples
- Connects my story to the scholarship's mission
- Closes with forward momentum

Requirements: Every sentence earns its place. No padding. Match the essay to the funder's values.""",
        "<p><strong>Hook:</strong> The first time I translated an insurance form for my mother at the kitchen table, I was nine years old...</p>",
        "scholarship+college+funding+book", "Scholarship Books",
        [("best-chatgpt-prompt-for-personal-statement", "Personal Statement"), ("best-chatgpt-prompt-for-essay-writing", "Essay Writing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-eulogy",
        "Best ChatGPT Prompt for Eulogy",
        "Write a heartfelt, honest eulogy that honors someone's real life — with specific memories, not platitudes.",
        """You are a writer who specializes in helping people give eulogies at funerals. Help me write one.

The person's name: [NAME]
Relationship to me: [WHO THEY WERE TO YOU]
Age at passing: [AGE]
3 specific memories I want to share: [LIST]
Their defining qualities: [2-3 TRAITS]
Their life's work or passion: [WHAT THEY LOVED]
A line that captures who they were: [QUOTE OR PHRASE]
Audience: [FAMILY / MIXED / RELIGIOUS / SECULAR]
Length: [MINUTES]

Write:
1. An opening that draws the room in
2. 2-3 specific stories that reveal who they really were
3. What we learned from them
4. A closing that lets everyone breathe

Requirements: No empty phrases ('taken too soon,' 'in a better place'). Specific details. Room for humor if appropriate. Earn any emotion.""",
        "<p><strong>Opening:</strong> Anyone who rode in my dad's pickup truck knew two things: the passenger seat tilted, and you were going to hear the same three Merle Haggard songs...</p>",
        "eulogy+memorial+speech+book", "Memorial Speech Books",
        [("best-chatgpt-prompt-for-wedding-speech", "Wedding Speech"), ("best-chatgpt-prompt-for-birthday-message", "Birthday Messages")]
    ),
    short_page(
        "best-chatgpt-prompt-for-stock-analysis",
        "Best ChatGPT Prompt for Stock Analysis",
        "Analyze a stock's fundamentals, competitive position, and risks — as a framework for your own research (not investment advice).",
        """You are a financial analyst with CFA training. Help me analyze a stock.

Ticker/Company: [TICKER]
Industry: [SECTOR]
My research stage: [INITIAL DD / DEEPER DIVE]
Investment horizon: [SHORT / LONG-TERM]

Analyze:
1. Business model — how they make money
2. Key financials (latest revenue, earnings, margins, debt)
3. Competitive moat — what protects them
4. Main competitors and market share
5. Top 3 risks
6. Valuation metrics vs peers (P/E, P/S, EV/EBITDA)
7. Recent catalysts or developments
8. What would make this a bad investment

Requirements: Stick to publicly available information. Flag what you're uncertain about. This is education, not investment advice. I should verify everything with current filings.""",
        "<p><strong>Business model:</strong> Company X generates 78% of revenue from recurring SaaS subscriptions with 95%+ net revenue retention...</p>",
        "investing+stocks+book+analysis", "Investing Books",
        [("best-chatgpt-prompt-for-investing-beginners", "Investing for Beginners"), ("best-chatgpt-prompt-for-data-analysis", "Data Analysis")]
    ),
    short_page(
        "best-chatgpt-prompt-for-retirement-planning",
        "Best ChatGPT Prompt for Retirement Planning",
        "Build a retirement roadmap — savings targets, account strategy, and projections based on your income and timeline.",
        """You are a Certified Financial Planner. Help me plan for retirement.

My age: [AGE]
Target retirement age: [AGE]
Current income: $[AMOUNT]
Current retirement savings: $[AMOUNT]
Retirement account types I have: [401k / IRA / Roth / HSA / Taxable]
Monthly savings rate: $[AMOUNT]
Target lifestyle in retirement: [MONTHLY SPEND]

Build:
1. Rough retirement number I need based on the 4% rule
2. Whether I'm on track or behind
3. Account priority order (match → IRA → etc.)
4. Asset allocation appropriate for my age
5. Catch-up strategies if behind
6. Social Security timing considerations
7. 3 biggest risks to my plan

Requirements: Conservative assumptions. Flag uncertainty. Recommend seeing a fee-only fiduciary for complex situations.""",
        "<p><strong>Retirement number:</strong> Based on $60K/yr target spending, you need ~$1.5M (25x rule)...</p>",
        "retirement+planning+book+financial", "Retirement Books",
        [("best-chatgpt-prompt-for-investing-beginners", "Investing for Beginners"), ("best-chatgpt-prompt-for-budgeting", "Budgeting")]
    ),
    short_page(
        "best-chatgpt-prompt-for-credit-score",
        "Best ChatGPT Prompt for Improving Credit Score",
        "Get a specific plan to raise your credit score — based on what's actually dragging it down.",
        """You are a credit expert. Help me improve my credit score.

Current score: [NUMBER]
Score range goal: [NUMBER]
Timeline: [MONTHS]
My accounts:
- Credit cards: [NUMBER] with $[TOTAL BALANCES] on $[TOTAL LIMITS]
- Loans: [LIST]
- Length of credit history: [YEARS]
- Recent hard inquiries: [NUMBER in last 2 years]
Known issues: [e.g. late payment 6 months ago, collection, none]

Give me:
1. The 3 highest-impact moves for my situation
2. Utilization ratio strategy (keep under 30%, ideally under 10%)
3. Whether to pay off vs. keep old accounts open
4. How to handle any negative items
5. Timeline estimate per move
6. What NOT to do (closing old cards, applying for new credit)

Requirements: Specific percentages and numbers. Realistic timelines (credit takes months, not weeks).""",
        "<p><strong>Top move:</strong> Drop utilization from 45% to under 10% by paying down Card A. Expected impact: 30-50 points in one reporting cycle.</p>",
        "credit+score+personal+finance+book", "Credit Books",
        [("best-chatgpt-prompt-for-debt-payoff", "Debt Payoff Plan"), ("best-chatgpt-prompt-for-budgeting", "Budgeting")]
    ),
    short_page(
        "best-chatgpt-prompt-for-medical-school-admission",
        "Best ChatGPT Prompt for Medical School Application",
        "Nail your medical school application — AMCAS personal statement, secondaries, interview prep, and strategy.",
        """You are a pre-med advisor who has helped 200+ students get into MD programs. Help with my application.

What I need: [personal statement / secondary essays / activities descriptions / interview prep / school list strategy]
My stats: MCAT [SCORE], GPA [NUMBER]
Schools I'm targeting: [LIST]
My story / 'why medicine': [2-3 SENTENCES]
Clinical experience: [HOURS + TYPE]
Research: [HOURS + PUBLICATIONS IF ANY]
Shadowing: [HOURS + SPECIALTIES]
Unique factors: [WHAT MAKES YOU DIFFERENT]

For personal statement:
- Start with a scene, not a summary
- Show why medicine through experience, not claims
- Connect your path to medicine specifically (not just 'helping people')
- Stay under 5,300 characters

Requirements: No saviorism. Specific patients/moments. Real reflection, not platitudes.""",
        "<p><strong>Opening:</strong> The monitor showed numbers I didn't understand, but Mrs. Garcia's face was clear enough...</p>",
        "medical+school+admission+book", "Med School Books",
        [("best-chatgpt-prompt-for-personal-statement", "Personal Statement"), ("best-chatgpt-prompt-for-job-interview-prep", "Interview Prep")]
    ),
    short_page(
        "best-chatgpt-prompt-for-law-school-admission",
        "Best ChatGPT Prompt for Law School Application",
        "Craft a law school application that gets you into top programs — personal statement, diversity statement, and addenda.",
        """You are a law school admissions consultant. Help with my application.

What I need: [personal statement / diversity statement / GPA or LSAT addendum / school-specific essays]
My LSAT: [SCORE]
My GPA: [NUMBER]
Undergrad school and major: [INFO]
Why law: [REAL REASON]
My background or life experience: [RELEVANT CONTEXT]
Schools I'm applying to: [LIST including reaches and targets]

For personal statement:
- 2-page limit (double-spaced)
- Show character through a specific story
- Don't explain why you want to be a lawyer by describing what lawyers do
- Connect your past to your future without cliches

Requirements: No 'I want to make a difference' openings. Specific incidents. Clear voice. Avoid political/religious topics unless central to your story.""",
        "<p><strong>Personal statement opening:</strong> The lease my landlord handed me was eight pages of small print. I signed it because I had to. Two years later, I understood why I shouldn't have...</p>",
        "law+school+admission+LSAT+book", "Law School Books",
        [("best-chatgpt-prompt-for-personal-statement", "Personal Statement"), ("best-chatgpt-prompt-for-essay-writing", "Essay Writing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-mba-application",
        "Best ChatGPT Prompt for MBA Application",
        "Write MBA application essays that win — goals essays, 'why us' essays, and leadership stories for top programs.",
        """You are an MBA admissions consultant who has placed candidates at M7 programs. Help with my application.

School: [PROGRAM]
Essay prompt: [EXACT PROMPT]
Word limit: [NUMBER]
My career so far: [BRIEF]
Years of experience: [NUMBER]
Short-term post-MBA goal: [ROLE, INDUSTRY, COMPANY TYPES]
Long-term goal: [VISION]
Why this school specifically: [2-3 REASONS BEYOND RANKING]
A leadership story I could tell: [BRIEF]

Write:
- Clear career narrative (past → MBA → future)
- Specific 'why now, why MBA, why this school'
- Leadership story with struggle, action, and outcome
- Personal voice, not consultancy-speak

Requirements: Avoid 'passion' and 'journey.' No Hail Mary career pivots without bridge experience.""",
        "<p><strong>Goals:</strong> Short-term: product management at an enterprise fintech. Long-term: found a company that brings financial tooling to gig workers...</p>",
        "MBA+admission+business+school+book", "MBA Books",
        [("best-chatgpt-prompt-for-personal-statement", "Personal Statement"), ("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan")]
    ),
    short_page(
        "best-chatgpt-prompt-for-online-course-outline",
        "Best ChatGPT Prompt for Online Course Outline",
        "Structure an online course that students actually finish — with clear modules, outcomes, and engagement hooks.",
        """You are an online course creator who has built courses for 100K+ students. Design a course outline for me.

Course topic: [SUBJECT]
Target student: [WHO IS TAKING THIS AND THEIR LEVEL]
Main transformation: [WHAT THEY CAN DO AFTER]
Format: [video / written / mixed]
Length: [HOURS or LESSONS]
Price point: $[AMOUNT]
Platform: [Teachable / Kajabi / Udemy / Own site]

Build:
1. Course promise in one sentence
2. 5-7 module outline with clear outcomes per module
3. Lessons per module (3-5 each)
4. One 'aha' moment per module
5. Built-in accountability (exercises, assessments, community)
6. Completion rate boosters (wins in first 20%)
7. Recommended support: email sequence, cohort vs self-paced

Requirements: Every module should solve a smaller problem. No fluff modules. Students need quick wins early.""",
        "<p><strong>Module 1: Foundations (Quick Win Week)</strong> — Students publish their first project by end of week 1...</p>",
        "online+course+creation+book+teaching", "Course Creation Books",
        [("best-chatgpt-prompt-for-lesson-plans", "Lesson Plans"), ("best-chatgpt-prompt-for-content-ideas", "Content Ideas")]
    ),
    short_page(
        "best-chatgpt-prompt-for-webinar-script",
        "Best ChatGPT Prompt for Webinar Script",
        "Write a webinar script that keeps people watching AND buys your offer at the end — with hooks, teaching, and a natural pitch.",
        """You are a webinar expert who has sold $10M+ through live and evergreen webinars. Write my script.

Webinar topic: [WHAT YOU'RE TEACHING]
Length: [MINUTES]
Offer at the end: [PRODUCT + PRICE]
Target audience: [WHO + PAIN POINT]
Promise: [WHAT THEY'LL LEAVE WITH]

Structure:
1. Hook (0-5 min): Why to stay. Earned curiosity.
2. Credibility (5-10 min): Why listen to you specifically.
3. Big idea (10-20 min): Reframe their thinking.
4. Teach 3 steps (20-45 min): Real value — not bait-and-switch.
5. Transition to offer (45-55 min): Name the gap between what they just learned and full transformation.
6. Offer (55-75 min): Stack value, scarcity, guarantee.
7. Q&A (75-90 min): Objection handling.

Requirements: Teach real content. No 'I'll tell you in a minute.' Offer must be genuinely valuable. Refund policy included.""",
        "<p><strong>Hook:</strong> In the next 60 minutes I'm going to show you why the 3 most common productivity tactics are making you slower, not faster...</p>",
        "webinar+marketing+book+launch", "Webinar Books",
        [("best-chatgpt-prompt-for-sales-pitch", "Sales Pitch"), ("best-chatgpt-prompt-for-copywriting", "Copywriting")]
    ),
    short_page(
        "best-chatgpt-prompt-for-youtube-thumbnails",
        "Best ChatGPT Prompt for YouTube Thumbnail Ideas",
        "Generate YouTube thumbnail concepts with text, visuals, and emotion that actually get clicks.",
        """You are a YouTube strategist who has designed thumbnails for channels with 10M+ subscribers. Give me thumbnail concepts.

Video title: [TITLE]
Video topic: [WHAT IT'S ABOUT]
Channel style: [CLEAN / BUSY / FACE-FORWARD / MINIMAL]
Audience: [WHO WATCHES]
Main emotion I want to trigger: [CURIOSITY / SHOCK / RELIEF / TRUST]

Give me:
1. 5 thumbnail concepts — each with different angle
2. Text to overlay (max 3-5 words, high contrast)
3. Facial expression or visual for each
4. Color palette
5. Which concept to A/B test first
6. Common thumbnail mistakes to avoid

Requirements: Text must read at 120x67px. Avoid clickbait that disappoints (destroys retention). Match energy to title.""",
        "<p><strong>Concept 1:</strong> Shocked face left side, red slash through $500, green arrow pointing to $47. Text: 'I WAS SO WRONG'</p>",
        "YouTube+thumbnail+design+book", "YouTube Design Books",
        [("best-chatgpt-prompt-for-youtube-scripts", "YouTube Scripts"), ("best-chatgpt-prompt-for-midjourney", "Midjourney Prompts")]
    ),
    short_page(
        "best-chatgpt-prompt-for-etsy-listing",
        "Best ChatGPT Prompt for Etsy Listing",
        "Write Etsy listings that rank in search AND convert browsers into buyers — titles, tags, and descriptions optimized for Etsy's algorithm.",
        """You are an Etsy SEO expert who has helped shops hit $1M+ in sales. Write an Etsy listing for me.

Product: [WHAT IT IS]
Category: [HANDMADE / VINTAGE / SUPPLY]
Price: $[AMOUNT]
Materials: [LIST]
Target buyer: [WHO BUYS THIS]
Unique angle: [WHAT MAKES IT DIFFERENT]
Keywords I'm targeting: [MAIN + LONG-TAIL]

Write:
1. Title (140 char max, front-loaded with main keyword)
2. 13 tags (20 char each, mix broad + specific)
3. Opening 2 lines that get the buyer hooked
4. Full description with benefits, specs, shipping info
5. Strong CTA
6. Attributes to fill in (color, style, occasion, etc.)

Requirements: First 40 chars of title are priority. Tags shouldn't repeat words. Description under 1000 chars but detailed.""",
        "<p><strong>Title:</strong> Personalized Wooden Cutting Board — Custom Name Engraving, Housewarming Gift, Maple Charcuterie Board</p>",
        "Etsy+selling+handmade+business+book", "Etsy Business Books",
        [("best-chatgpt-prompt-for-product-descriptions", "Product Descriptions"), ("best-chatgpt-prompt-for-seo", "SEO")]
    ),
    short_page(
        "best-chatgpt-prompt-for-shopify-store",
        "Best ChatGPT Prompt for Shopify Store Setup",
        "Plan and launch a Shopify store — from niche to product pages to marketing — with a clear 30-day roadmap.",
        """You are an ecommerce consultant who has launched 50+ successful Shopify stores. Plan my store.

What I'm selling: [PRODUCT OR NICHE]
Business model: [DROPSHIP / OWN INVENTORY / PRINT ON DEMAND / HANDMADE]
Starting budget: $[AMOUNT]
Target customer: [WHO]
Price range: $[LOW-HIGH]

Build:
1. Store name ideas (5 options)
2. Homepage structure (hero, social proof, product, story)
3. 3-5 product page essentials (what to include for conversion)
4. Collection/category strategy
5. Shipping and returns policy (reasonable defaults)
6. 30-day launch roadmap (week by week)
7. First $1K in sales plan — traffic sources and conversion tactics
8. Top 3 Shopify apps worth installing, 3 to skip

Requirements: Focus on profitability, not just revenue. Include realistic ad spend and margins.""",
        "<p><strong>Week 1:</strong> Niche validation + 5 supplier samples. Launch Shopify trial. Write brand story and brand colors.</p>",
        "Shopify+ecommerce+dropshipping+book", "Ecommerce Books",
        [("best-chatgpt-prompt-for-product-descriptions", "Product Descriptions"), ("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan")]
    ),
    short_page(
        "best-chatgpt-prompt-for-print-on-demand",
        "Best ChatGPT Prompt for Print on Demand",
        "Find winning print-on-demand niches, design ideas, and launch plans for Merch by Amazon, Redbubble, or Printful.",
        """You are a POD seller who has moved 100K+ units. Help me plan my print-on-demand business.

Platform: [Merch by Amazon / Redbubble / Etsy + Printful / Teespring]
Niche area I'm considering: [INTEREST OR AUDIENCE]
Starting budget: $[AMOUNT]
Time per week: [HOURS]

Give me:
1. 10 niche sub-topics within my interest with search demand signals
2. 5 design concept directions per niche (text-based, illustration, vintage, minimalist, combo)
3. Winning vs losing niches (oversaturated to avoid)
4. Pricing strategy
5. Launch plan: 10 designs → test → scale
6. Traffic sources beyond platform search (Pinterest, TikTok, email)
7. When to reinvest profits

Requirements: Realistic timelines. Most new designs flop. Factor in royalty splits. No trademark infringement ever.""",
        "<p><strong>Niche:</strong> 'Dog mom' within pet lovers — 3 sub-angles: specific breeds, sarcastic quotes, minimalist line art</p>",
        "print+on+demand+business+t-shirt+book", "POD Books",
        [("best-chatgpt-prompt-for-amazon-fba", "Amazon FBA"), ("best-chatgpt-prompt-for-etsy-listing", "Etsy Listing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-freelance-proposal",
        "Best ChatGPT Prompt for Freelance Proposal",
        "Write Upwork, Fiverr, or email freelance proposals that actually get responses — even as a new freelancer.",
        """You are a senior freelancer who earns $250K+/year. Write a freelance proposal for me.

Platform: [Upwork / Fiverr / Cold email / Other]
Job description (paste): [WHAT THEY POSTED]
My skills: [RELEVANT SKILLS]
My experience level: [NEW / MID / SENIOR]
Rate I want to charge: $[HOURLY OR PROJECT]
Unique angle: [WHAT SETS ME APART]

Write:
1. Opening line that references specifically what they need (not 'Hi, I saw your post')
2. Proof I can deliver (1 specific past result OR sample approach)
3. 3 questions that show I understand the problem
4. Scope + timeline + rate
5. Clear next step

Requirements: Under 200 words. No template language. No sob story about being new. Confidence without arrogance.""",
        "<p><strong>Opening:</strong> I noticed you need landing pages for a SaaS onboarding flow — specifically focused on activation. That's the exact problem I worked on for [X] last year and lifted trial-to-paid from 9% to 14%.</p>",
        "freelance+business+Upwork+book", "Freelance Books",
        [("best-chatgpt-prompt-for-sales-pitch", "Sales Pitch"), ("best-chatgpt-prompt-for-writing-a-cover-letter", "Writing a Cover Letter")]
    ),
    short_page(
        "best-chatgpt-prompt-for-consulting-proposal",
        "Best ChatGPT Prompt for Consulting Proposal",
        "Write consulting proposals that close $10K-$100K engagements — with clear scope, pricing, and credibility.",
        """You are a consulting firm partner who has sold $50M+ in engagements. Write a proposal for me.

Client: [COMPANY + INDUSTRY]
Their problem: [WHAT THEY NEED SOLVED]
Scope of work: [WHAT YOU'LL DO]
Duration: [WEEKS OR MONTHS]
Total fee: $[AMOUNT] or rate + estimate
Team: [YOU OR YOU + OTHERS]

Write:
1. Executive summary (2 sentences)
2. Our understanding of your situation (shows you listened)
3. Proposed approach with phases
4. Deliverables per phase
5. Timeline with milestones
6. Team and relevant experience
7. Investment + payment terms
8. Next steps

Requirements: Match their sophistication. Results > activities in scope. Clear decision deadline.""",
        "<p><strong>Approach:</strong> Phase 1 (2 weeks): Current state audit. Phase 2 (3 weeks): Strategy design. Phase 3 (4 weeks): Pilot implementation.</p>",
        "consulting+business+book+sales", "Consulting Books",
        [("best-chatgpt-prompt-for-sales-pitch", "Sales Pitch"), ("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan")]
    ),
    short_page(
        "best-chatgpt-prompt-for-brand-voice",
        "Best ChatGPT Prompt for Brand Voice",
        "Define your brand voice with clear guidelines, do/don't examples, and tone variations that keep your copy consistent.",
        """You are a brand strategist. Define a brand voice for me.

Brand: [NAME + WHAT YOU DO]
Target customer: [DETAILED PERSONA]
Competitors' voices: [2-3 EXAMPLES]
Brand personality: [3 ADJECTIVES]
Personality NOT: [WHAT TO AVOID]
Channels: [WEB / EMAIL / SOCIAL / ADS]

Create:
1. Brand voice in 3 clear attributes (e.g. 'Confident but warm, direct but not harsh')
2. Do/Don't word lists (specific vocabulary)
3. Example sentences for the same message in: marketing, support, social, legal
4. Tone variations by situation (launch, crisis, everyday)
5. Grammar rules (Oxford comma, contractions, sentence length)
6. Taglines in the voice (5 options)
7. One-page voice guideline summary

Requirements: Specific enough that a new writer could match it. Show before/after of weak vs. on-brand copy.""",
        "<p><strong>Voice:</strong> Direct, curious, human. Not: corporate, salesy, ironic. Always: contractions, short sentences, specific nouns over adjectives.</p>",
        "branding+book+voice+marketing", "Branding Books",
        [("best-chatgpt-prompt-for-copywriting", "Copywriting"), ("best-chatgpt-prompt-for-naming-a-business", "Naming a Business")]
    ),
    short_page(
        "best-chatgpt-prompt-for-case-study",
        "Best ChatGPT Prompt for Case Study",
        "Write customer case studies that close deals — with story structure, real numbers, and quotes that feel authentic.",
        """You are a B2B marketer who writes case studies for 6-figure deals. Write one for me.

Client: [COMPANY NAME + INDUSTRY]
What they bought: [PRODUCT/SERVICE]
Their problem before: [SPECIFIC PAIN + COST]
Why they chose us: [DECISION FACTOR]
How we solved it: [SOLUTION + TIMELINE]
Results: [METRICS WITH NUMBERS]
Direct quote from client (if available): [QUOTE]

Structure:
1. Headline with outcome + numbers
2. Client intro (who they are, why readers should care)
3. The challenge (specific, costly)
4. The search for a solution
5. Implementation story
6. Results (hero metric + supporting)
7. Client quote at emotional peak
8. What's next for the client

Requirements: Tell the story of a person (champion at the client), not a logo. Include setbacks and honest reflection.""",
        "<p><strong>Headline:</strong> How Acme Cut Onboarding Time 65% and Saved $400K in Year One</p>",
        "case+study+B2B+marketing+book", "B2B Marketing Books",
        [("best-chatgpt-prompt-for-copywriting", "Copywriting"), ("best-chatgpt-prompt-for-content-ideas", "Content Ideas")]
    ),
    short_page(
        "best-chatgpt-prompt-for-white-paper",
        "Best ChatGPT Prompt for White Paper",
        "Write B2B white papers that establish authority and generate leads — with research, narrative, and clear CTAs.",
        """You are a B2B content strategist who has written white papers that generated $10M+ in pipeline. Write one for me.

Topic: [SUBJECT]
Target reader: [TITLE + INDUSTRY]
Length: [PAGES]
Purpose: [lead gen / thought leadership / sales enablement]
Our expertise angle: [WHY YOU]
Desired action after reading: [CTA]

Structure:
1. Executive summary (1 page)
2. Problem landscape (with research/data)
3. Why existing approaches fall short
4. New framework or model
5. Applied example or case
6. Recommendations + checklist
7. Author bio + CTA

Requirements: Cite real studies (I'll verify). Visuals in every 2 pages. No gated facts behind the CTA — give real value.""",
        "<p><strong>Framework:</strong> The Three Layer Model for enterprise data governance — strategy layer, process layer, tool layer...</p>",
        "B2B+content+marketing+book", "B2B Content Books",
        [("best-chatgpt-prompt-for-case-study", "Case Study"), ("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post")]
    ),
    short_page(
        "best-chatgpt-prompt-for-customer-survey",
        "Best ChatGPT Prompt for Customer Survey Questions",
        "Write customer survey questions that produce actionable insights — no vague 'on a scale of 1-10' filler.",
        """You are a customer research expert. Design a survey for me.

Goal: [WHAT YOU WANT TO LEARN]
Audience: [WHO TAKES IT]
Distribution: [EMAIL / IN-APP / POST-PURCHASE]
Incentive (if any): [WHAT YOU'RE OFFERING]
Target length: [MINUTES OR QUESTIONS]

Build:
1. Opening (why they should take 2 minutes)
2. 8-12 questions that reveal real insight, not vanity metrics
3. Mix of: multiple choice, open-ended, ranking
4. Skip logic if relevant
5. Demographics only if needed (keep short)
6. Closing thank-you + what happens next

Requirements: Avoid leading questions. Every Q must tie to a decision. NPS alone is useless without a follow-up 'why.'""",
        "<p><strong>Q1:</strong> In one sentence, what problem were you trying to solve when you first tried our product?</p>",
        "customer+research+product+book", "Product Books",
        [("best-chatgpt-prompt-for-data-analysis", "Data Analysis"), ("best-chatgpt-prompt-for-email-marketing", "Email Marketing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-pricing-strategy",
        "Best ChatGPT Prompt for Pricing Strategy",
        "Set the right price for your product or service — without leaving money on the table or pricing yourself out of the market.",
        """You are a pricing strategist who has worked with Fortune 500s and startups. Help me set pricing.

Product/service: [WHAT YOU SELL]
Target customer: [WHO BUYS]
Current price (if any): $[AMOUNT]
Costs per unit: $[AMOUNT]
Competitors' pricing: [2-3 DATA POINTS]
Value delivered: [QUANTIFIABLE VALUE TO CUSTOMER]
Business model: [ONE-TIME / SUBSCRIPTION / USAGE]

Analyze:
1. Cost-plus floor
2. Competitive positioning range
3. Value-based ceiling (often much higher)
4. Recommended price + confidence level
5. 3 pricing tiers if applicable
6. Anchor pricing strategy
7. Whether to raise, lower, or hold current price
8. How to test price changes safely

Requirements: Value > cost in recommendation logic. Flag if I'm underpricing (most founders do).""",
        "<p><strong>Tiers:</strong> Starter $29, Growth $99, Scale $299. Anchor with 'Enterprise: Contact us.'</p>",
        "pricing+strategy+book+business", "Pricing Books",
        [("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan"), ("best-chatgpt-prompt-for-negotiation", "Negotiation")]
    ),
    short_page(
        "best-chatgpt-prompt-for-customer-service-reply",
        "Best ChatGPT Prompt for Customer Service Reply",
        "Write customer service replies that solve the problem, calm the customer, and protect your business.",
        """You are a customer experience leader. Help me respond to a customer.

Customer's message (paste): [COMPLAINT OR QUESTION]
Situation: [WHAT ACTUALLY HAPPENED FROM YOUR SIDE]
Policy/facts: [WHAT YOU CAN/CANNOT DO]
Channel: [EMAIL / CHAT / REVIEW RESPONSE]
Desired outcome: [RESOLUTION YOU CAN OFFER]
Customer tier (if relevant): [NEW / REPEAT / VIP]

Write:
1. Opening that acknowledges their frustration (don't start with 'I understand')
2. Specific explanation (not 'due to high volume')
3. What you're doing about it
4. What they should expect next + when
5. A small gesture of goodwill if warranted
6. A close that invites further dialogue

Requirements: Never defensive. Apologize only for real problems. Don't promise what you can't deliver. No copy-paste tone.""",
        "<p><strong>Opening:</strong> Alex, I'm sorry the order didn't arrive. I can see on my end that FedEx marked it delivered on Tuesday — but it clearly isn't where it should be.</p>",
        "customer+service+book+communication", "Customer Service Books",
        [("best-chatgpt-prompt-for-writing-emails", "Writing Emails"), ("best-chatgpt-prompt-for-apology-letter", "Apology Letter")]
    ),
    short_page(
        "best-chatgpt-prompt-for-resume-bullets",
        "Best ChatGPT Prompt for Resume Bullets",
        "Turn boring job duties into resume bullets with numbers, action verbs, and real impact — the kind recruiters actually read.",
        """You are a resume writer who has rewritten 5,000+ resumes for top companies. Improve my resume bullets.

My role: [JOB TITLE at COMPANY]
Target role I'm applying for: [JOB TITLE]
Current bullets (paste): [YOUR BULLETS]
Context I want to add: [NUMBERS, SCOPE, OUTCOMES]

Rewrite each bullet to:
1. Start with a strong action verb (not 'Responsible for')
2. Include a specific number where possible
3. Show the outcome, not just the task
4. Use language from the target job description
5. Demonstrate scope (team size, budget, users)
6. Keep under 2 lines each
7. Vary the opening verbs across bullets

Requirements: No buzzwords ('synergized,' 'rockstar'). If you don't have exact numbers, estimate with '~' and keep it reasonable.""",
        "<p><strong>Before:</strong> Responsible for managing social media<br><strong>After:</strong> Grew Instagram following from 3K to 47K in 12 months by launching a weekly educational series, driving 18% of site traffic.</p>",
        "resume+writing+career+book", "Resume Books",
        [("best-chatgpt-prompt-for-writing-a-resume", "Writing a Resume"), ("best-chatgpt-prompt-for-linkedin-profile", "LinkedIn Profile")]
    ),
    short_page(
        "best-chatgpt-prompt-for-networking-email",
        "Best ChatGPT Prompt for Networking Email",
        "Write cold networking emails that get responses — to informational interviews, mentors, and people you admire.",
        """You are a networking expert. Write a networking email for me.

Who I'm emailing: [NAME + TITLE + COMPANY]
How I found them: [LINKEDIN / MUTUAL / TALK / ARTICLE]
What I want: [INFORMATIONAL INTERVIEW / ADVICE / SPECIFIC Q]
Why me: [2 SENTENCES ABOUT YOUR SITUATION]
What I respect about them: [SPECIFIC — mention a talk, article, or accomplishment]

Write:
- Subject line (under 50 chars, curiosity or specificity)
- Opening that references them specifically
- Why you're reaching out (honest)
- Specific, small ask (15 min call, one question, or quick reply)
- Make it easy to say no
- No pressure close

Requirements: Under 150 words. No 'I hope this finds you well.' Respect their time. Don't ask for a job.""",
        "<p><strong>Subject:</strong> Your talk on pricing — one question<br><br>Hi Maya, I watched your SaaStr session on value-based pricing twice — the part about 'pricing the outcome' changed how I think about it...</p>",
        "networking+career+book+professional", "Networking Books",
        [("best-chatgpt-prompt-for-writing-emails", "Writing Emails"), ("best-chatgpt-prompt-for-linkedin-profile", "LinkedIn Profile")]
    ),
    short_page(
        "best-chatgpt-prompt-for-event-planning",
        "Best ChatGPT Prompt for Event Planning",
        "Plan a birthday, baby shower, or corporate event — with timeline, checklist, budget, and vendor questions.",
        """You are an event planner. Help me plan an event.

Event type: [BIRTHDAY / BABY SHOWER / CORPORATE / RETREAT / OTHER]
Guest count: [NUMBER]
Date: [WHEN]
Budget: $[TOTAL]
Venue type: [HOME / RENTAL / RESTAURANT / OUTDOOR]
Theme or vibe: [STYLE]
Must-haves: [ANY]
Must-avoid: [ANY]

Build:
1. Planning timeline backward from event date (8 weeks → day of)
2. Budget breakdown by category
3. Vendor list needed + key questions to ask each
4. Invitation strategy and timeline
5. Day-of run sheet (hour by hour)
6. Gift/favor idea if applicable
7. Common mistakes at this type of event
8. Rainy day / backup plan

Requirements: Realistic timeline. Buffer in budget. Honest about what needs booking weeks out.""",
        "<p><strong>6 weeks out:</strong> Venue contract signed, save-the-dates sent, catering confirmed, photographer booked.</p>",
        "event+planning+book+organizer", "Event Planning Books",
        [("best-chatgpt-prompt-for-wedding-planning", "Wedding Planning"), ("best-chatgpt-prompt-for-birthday-message", "Birthday Messages")]
    ),
    short_page(
        "best-chatgpt-prompt-for-hiking-route",
        "Best ChatGPT Prompt for Hiking Route Planning",
        "Plan a hiking trip — route recommendations, gear list, water logistics, and bailout options — matched to your skill level.",
        """You are an experienced backpacker. Plan a hiking trip for me.

Location: [REGION OR PARK]
Days/nights: [DURATION]
My experience: [DAYHIKER / WEEKEND BACKPACKER / EXPERIENCED]
Fitness: [AVERAGE / ABOVE / BELOW]
Group size: [NUMBER]
Time of year: [SEASON]
What I want: [SOLITUDE / VIEWS / LAKES / SUMMITS / EASY]
Avoid: [e.g. exposure, altitude, bugs, crowds]

Give me:
1. Route recommendation with daily mileage and elevation
2. Permit/reservation requirements
3. Gear list (without padding — essentials only)
4. Water sources per day
5. Campsite options with pros/cons
6. Weather considerations for that season
7. Bailout points if something goes wrong
8. What to do if injury, weather, or wildlife issues

Requirements: Be honest about difficulty. Tell me if route doesn't match my skill level. Include safety for my group size.""",
        "<p><strong>Day 1:</strong> TH at 7am, 6.2 mi with 2,400ft gain to Sapphire Lake. Water at mile 3. Camp at large stand of trees on north side.</p>",
        "backpacking+hiking+guide+book", "Hiking Books",
        [("best-chatgpt-prompt-for-travel-planning", "Travel Planning"), ("best-chatgpt-prompt-for-road-trip-planning", "Road Trip Planning")]
    ),
    short_page(
        "best-chatgpt-prompt-for-camping-trip",
        "Best ChatGPT Prompt for Camping Trip Planning",
        "Plan a camping trip your group will actually enjoy — gear list, meals, activities, and site selection.",
        """You are a camping expert. Plan a camping trip.

Destination: [CAMPGROUND OR AREA]
Dates: [WHEN]
Group: [NUMBER + AGES if kids involved]
Camping type: [CAR / TENT / RV / BACKCOUNTRY]
Experience level: [FIRST-TIMERS / OCCASIONAL / VETERAN]
Budget: $[TOTAL]

Plan:
1. Campsite selection tips (what to book, what to avoid)
2. Gear checklist by category (shelter, sleep, cook, clothing)
3. Meal plan (breakfast, lunch, dinner, snacks for each day)
4. Fire/cooking setup
5. Activities suited to your group and area
6. Kid-friendly tips if relevant
7. Weather contingencies
8. Packout/pack down day timing

Requirements: Realistic for skill level. Budget-aware. Don't forget small things first-timers miss (trash bags, headlamps).""",
        "<p><strong>Day 1 dinner:</strong> Foil-pack chicken fajitas on the fire — prep vegetables at home, foil sealed in cooler.</p>",
        "camping+outdoor+guide+book", "Camping Books",
        [("best-chatgpt-prompt-for-hiking-route", "Hiking Route"), ("best-chatgpt-prompt-for-travel-planning", "Travel Planning")]
    ),
    short_page(
        "best-chatgpt-prompt-for-meal-prep-sunday",
        "Best ChatGPT Prompt for Sunday Meal Prep",
        "Plan a 2-3 hour Sunday meal prep session that makes your entire work week easier — with shopping list and timing.",
        """You are a meal prep coach. Plan my Sunday prep.

People to feed: [NUMBER]
Days to cover: [e.g. Mon-Fri lunches]
Time I have: [HOURS]
Dietary needs: [ANY]
Budget: $[TOTAL]
Skill level: [BEGINNER / INTERMEDIATE]
What I already have: [PROTEINS, GRAINS, PANTRY STAPLES]
What I hate eating leftover: [LIST]

Give me:
1. Menu for the week (breakfast / lunch / dinner that rotates well)
2. Shopping list organized by grocery section
3. Prep timeline (what to cook first for maximum parallelization)
4. Storage guide (which meals freeze, which hold 5 days in fridge)
5. Reheat instructions that keep food good
6. Flavor variations so you don't get bored
7. Total active prep time

Requirements: Under 3 hrs total. Variety in textures and flavors. Include one 'back-up' meal for when you can't face leftovers.""",
        "<p><strong>Prep order:</strong> Preheat oven → start grains on stove → chop vegetables → roast proteins → assemble containers while rice cooks.</p>",
        "meal+prep+cooking+book", "Meal Prep Books",
        [("best-chatgpt-prompt-for-meal-planning", "Meal Planning"), ("best-chatgpt-prompt-for-recipes", "Recipes")]
    ),
    short_page(
        "best-chatgpt-prompt-for-speech",
        "Best ChatGPT Prompt for Any Speech",
        "Write a speech that lands — graduation, retirement, award, or keynote — with hook, story, and memorable close.",
        """You are a professional speechwriter who has written for executives and public figures. Write a speech.

Type of speech: [GRADUATION / RETIREMENT / KEYNOTE / AWARD / TRIBUTE]
Audience: [WHO]
Length: [MINUTES]
Occasion details: [CONTEXT]
Speaker (me): [WHO YOU ARE, ROLE]
Core message (what you want them to feel/do): [GOAL]
Personal story I could tell: [BRIEF]

Structure:
1. Open with something unexpected (not 'thank you for having me')
2. Build to one clear message
3. Include 1-2 specific stories that earn their place
4. A moment of real emotion (earned, not forced)
5. Close with a line that could be quoted
6. Mark pacing, pauses, and emphasis

Requirements: Write for the ear, not the page. Short sentences. Test by reading out loud. Pacing: ~130 words per minute.""",
        "<p><strong>Opening:</strong> Twenty-five years ago I sat where you're sitting now. I had no plan, a cheap suit, and a resume my mother had typed...</p>",
        "public+speaking+book+speeches", "Speech Books",
        [("best-chatgpt-prompt-for-wedding-speech", "Wedding Speech"), ("best-chatgpt-prompt-for-podcast-script", "Podcast Script")]
    ),
    short_page(
        "best-chatgpt-prompt-for-poem",
        "Best ChatGPT Prompt for Writing a Poem",
        "Write a poem for an occasion, a person, or a feeling — with image, rhythm, and a clear voice.",
        """You are a contemporary poet. Write a poem for me.

Occasion or subject: [WHAT IT'S FOR]
Who it's for: [RECIPIENT if applicable]
Tone: [TENDER / FUNNY / GRIEF / CELEBRATORY / MEDITATIVE]
Style: [FREE VERSE / RHYMING / HAIKU / SONNET / OTHER]
Length: [SHORT / MEDIUM / LONGER]
Images to include: [CONCRETE THINGS FROM THEIR LIFE]
Words or phrases to avoid: [CLICHES YOU HATE]

Write:
- A poem that uses sensory detail, not abstractions
- Rhythm appropriate to the feeling (short lines for tension, longer for peace)
- An unexpected turn (volta) somewhere
- An ending that stops sharp, not drifts

Requirements: No Hallmark. Specific over general ('the blue mug she drank from' beats 'her cherished things'). Trust silence.""",
        "<p><strong>Example (for a retirement):</strong><br>For thirty years you woke before the light,<br>packed the lunch your wife had made,<br>and drove toward a door that wasn't home...</p>",
        "poetry+writing+craft+book", "Poetry Books",
        [("best-chatgpt-prompt-for-creative-writing", "Creative Writing"), ("best-chatgpt-prompt-for-birthday-message", "Birthday Messages")]
    ),
    short_page(
        "best-chatgpt-prompt-for-song-lyrics",
        "Best ChatGPT Prompt for Song Lyrics",
        "Write song lyrics with hook, narrative, and the right emotional arc — for any genre from folk to pop to country.",
        """You are a professional songwriter. Write lyrics for me.

Genre: [POP / COUNTRY / FOLK / RAP / INDIE / R&B]
Theme: [WHAT THE SONG IS ABOUT]
Mood: [EMOTIONAL FEEL]
Who's the 'I' / narrator: [PERSPECTIVE]
Specific details from real life: [MEMORY, OBJECT, PLACE]
Structure: [VERSE-CHORUS-VERSE-CHORUS-BRIDGE-CHORUS / CUSTOM]

Write:
- Verse 1 (set the scene)
- Pre-chorus (build tension)
- Chorus (the hook — singable, quotable)
- Verse 2 (raise stakes, shift perspective)
- Pre-chorus
- Chorus
- Bridge (new angle or reveal)
- Final chorus (hits different now)

Requirements: Concrete images over abstractions. Use rhyme but not forced. One central metaphor. Under 3 syllables on stressed beats of the chorus hook.""",
        "<p><strong>Hook:</strong> 'I still drive past your street / just to not be alone' — concrete, specific, singable.</p>",
        "songwriting+book+craft+music", "Songwriting Books",
        [("best-chatgpt-prompt-for-poem", "Poem"), ("best-chatgpt-prompt-for-creative-writing", "Creative Writing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-children-book",
        "Best ChatGPT Prompt for Children's Book",
        "Draft a children's book concept — premise, arc, page breakdown — that rewards re-reading for kids and parents.",
        """You are a children's book author and editor. Help me write a picture book.

Age range: [0-3 / 3-5 / 5-8]
Concept: [CORE IDEA]
Main character: [WHO]
Emotional truth / lesson: [WHAT KIDS TAKE AWAY]
Length: [STANDARD 32 PAGES OR DIFFERENT]
Tone: [FUNNY / TENDER / ADVENTURE / SURREAL]

Give me:
1. One-line pitch
2. Character design note (what makes them distinct)
3. 32-page breakdown (illustration + text per spread)
4. Emotional arc (setup, conflict, resolution)
5. 3-5 repeating phrases or refrains
6. A final line that lands
7. Notes on illustration style that would fit

Requirements: No moralizing. Show, don't tell. Kids spot fake. Rhyme only if genuinely strong. Re-readable — parents read 100x.""",
        "<p><strong>Spread 12:</strong> [Illustration: Mabel under the bed, eyes wide, stuffed animal clutched]<br>TEXT: Maybe the dark wasn't the scariest thing after all. Maybe it was a very quiet friend.</p>",
        "children+book+writing+illustration+book", "Children's Book Writing",
        [("best-chatgpt-prompt-for-creative-writing", "Creative Writing"), ("best-chatgpt-prompt-for-book-writing", "Book Writing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-short-story",
        "Best ChatGPT Prompt for Short Story",
        "Draft a short story with strong structure — inciting incident, turn, ending — in under 5,000 words.",
        """You are a short story writer published in literary magazines. Help me write a short story.

Genre: [LITERARY / SCI-FI / FANTASY / CRIME / HORROR / ROMANCE]
Length: [FLASH 500 / SHORT 2K-5K / LONG 7K-12K]
Central idea or premise: [CONCEPT]
Setting (time + place): [SPECIFICS]
Main character in one sentence: [WHO AND WHAT THEY WANT]
Conflict: [OBSTACLE]
Tone: [SPARSE / LYRICAL / DARK / COMIC]

Develop:
1. Opening line that starts in-scene
2. Inciting incident by 20% mark
3. Midpoint shift
4. Climax
5. Ending that echoes the opening
6. POV and tense decision
7. Three specific details to include

Requirements: Compression. Every scene must do double duty. Character reveals character through action and specific dialog, not internal thought dumps.""",
        "<p><strong>Opening:</strong> The letter arrived on a Tuesday, which was the kind of day that couldn't hold news.</p>",
        "short+story+fiction+craft+book", "Fiction Books",
        [("best-chatgpt-prompt-for-creative-writing", "Creative Writing"), ("best-chatgpt-prompt-for-book-writing", "Book Writing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-dnd-campaign",
        "Best ChatGPT Prompt for D&D Campaign",
        "Design a D&D campaign arc — world, villains, dungeons, and plot hooks — that keeps players hooked for 20+ sessions.",
        """You are a veteran D&D Dungeon Master. Help me design a campaign.

Party level at start: [LEVEL]
Campaign length: [SHORT 6-10 SESSIONS / LONG 20+]
Setting type: [HIGH FANTASY / DARK / POLITICAL / HORROR / PLANAR]
Starting town: [IDEA OR BLANK]
Themes you want: [BETRAYAL / REDEMPTION / POLITICAL / COSMIC]
Party composition (if known): [CLASSES]

Build:
1. Overall plot arc in 3 acts
2. Main BBEG with motivation (not cartoonish evil)
3. 3-5 secondary antagonists or factions
4. Starting dungeon/quest
5. 10 side hooks players can pull
6. One recurring NPC per party member's backstory
7. 3 twists that reframe the main plot
8. Endgame options based on player choices

Requirements: Avoid railroading. Every faction wants something. Leave space for player agency. Plant clues for later reveals in session 1.""",
        "<p><strong>BBEG:</strong> Lord Arden believes he can prevent a prophesied catastrophe by sacrificing a city. He's not wrong about the catastrophe — he's wrong about the sacrifice.</p>",
        "dungeons+dragons+book+DM+guide", "D&D Books",
        [("best-chatgpt-prompt-for-creative-writing", "Creative Writing"), ("best-chatgpt-prompt-for-short-story", "Short Story")]
    ),
    short_page(
        "best-chatgpt-prompt-for-escape-room",
        "Best ChatGPT Prompt for Escape Room Design",
        "Design an escape room experience — puzzles, themes, and flow — for a home game, party, or professional build.",
        """You are an escape room designer. Design an experience for me.

Setting/theme: [LAB / MANOR / SPACESHIP / HEIST / OCCULT]
Difficulty: [EASY / MEDIUM / HARD]
Time limit: [MINUTES]
Players: [NUMBER]
Budget: $[TOTAL]
Space: [ROOM SIZE]

Design:
1. Narrative backstory (2 paragraphs)
2. 6-8 puzzles in linear, parallel, or branching flow
3. Required materials per puzzle (specific items)
4. Solution sequences with answer keys
5. Difficulty calibration + hint triggers
6. Reveal moments for dramatic effect
7. Finale mechanism
8. Setup and reset time

Requirements: Puzzles layer information, not just luck. Balance physical, observational, and logical. Test solution times realistically.""",
        "<p><strong>Puzzle 3:</strong> UV light reveals hidden message on wall map — coordinates point to floor safe opened by cipher from Puzzle 1.</p>",
        "escape+room+puzzle+book+design", "Puzzle Books",
        [("best-chatgpt-prompt-for-dnd-campaign", "D&D Campaign"), ("best-chatgpt-prompt-for-creative-writing", "Creative Writing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-trivia-questions",
        "Best ChatGPT Prompt for Trivia Questions",
        "Write trivia questions for a party, fundraiser, or bar night — balanced difficulty across categories.",
        """You are a trivia writer for pub quizzes. Write me a trivia set.

Occasion: [PARTY / FUNDRAISER / CLASSROOM / BAR]
Number of questions: [TOTAL]
Categories: [e.g. history, pop culture, sports, science, local]
Difficulty level: [EASY 80% / MEDIUM 65% / HARD 40% solve rate]
Audience: [AGE RANGE + INTERESTS]
Time per question: [SECONDS]

Write:
- Mix of multiple choice, fill-in, true/false, picture
- Balanced difficulty across the set
- Trick rounds (lightning, themed, visual)
- Tie-breaker question at end
- Answer key with brief explanation why answer is right
- Scoring system

Requirements: Verify all facts (I'll double-check). Avoid obscure trivia that feels like 'gotcha.' Mix era and regions for cultural inclusivity.""",
        "<p><strong>Q7 (Medium):</strong> Which country has won the most FIFA World Cups?<br>Answer: Brazil (5)</p>",
        "trivia+party+game+book", "Trivia Books",
        [("best-chatgpt-prompt-for-event-planning", "Event Planning"), ("best-chatgpt-prompt-for-gift-ideas", "Gift Ideas")]
    ),
    short_page(
        "best-chatgpt-prompt-for-icebreakers",
        "Best ChatGPT Prompt for Icebreakers",
        "Get icebreakers that don't suck — for team meetings, workshops, classrooms, or social events.",
        """You are a facilitator. Give me icebreakers.

Setting: [CORPORATE MEETING / WORKSHOP / CLASSROOM / SOCIAL / CONFERENCE]
Group size: [NUMBER]
Time available: [MINUTES]
Group familiarity: [STRANGERS / ACQUAINTANCES / CLOSE TEAM]
Energy level desired: [CALM / MEDIUM / HIGH]
Goal: [WARM UP / BUILD TRUST / REVEAL SKILLS / FUN]

Give me:
- 5 icebreakers matched to the setting
- Setup and time required for each
- Follow-up questions to deepen them
- Which ones work remote vs in-person
- Which ones to avoid and why (the cringe ones)

Requirements: No 'tell us an interesting fact.' No public vulnerability that risks backfiring. Everyone should be able to participate.""",
        "<p><strong>Icebreaker 1 (5 min):</strong> What was the soundtrack of your high school — not the band, the ONE song that defined it? (Then play 10 seconds of each on Spotify.)</p>",
        "icebreaker+team+building+book", "Team Books",
        [("best-chatgpt-prompt-for-event-planning", "Event Planning"), ("best-chatgpt-prompt-for-performance-review", "Performance Review")]
    ),
    short_page(
        "best-chatgpt-prompt-for-sales-cold-call",
        "Best ChatGPT Prompt for Sales Cold Call Script",
        "Write cold call scripts that get past the gatekeeper, hook the prospect, and book the meeting.",
        """You are a sales rep who has booked 1,000+ meetings cold. Write a cold call script.

What I sell: [PRODUCT/SERVICE]
Target prospect: [TITLE + COMPANY SIZE + INDUSTRY]
Value prop: [ONE SENTENCE]
Proof / traction: [CUSTOMER OR DATA POINT]
Call goal: [BOOK DEMO / QUALIFY / DISCOVERY]
Call time budget: [MINUTES]

Write:
1. Opener (10 seconds — earn the next 30)
2. Permission (do you have a moment)
3. Value hook (why they might care)
4. Discovery question
5. Transition to meeting ask
6. Meeting ask with specific time
7. Responses to top 5 objections ('not interested,' 'send info,' 'we already have something,' 'not the right time,' 'remove us')
8. Voicemail script (under 20 seconds)

Requirements: Permission-based. Don't sound like a script. Short sentences. Ask more than you pitch.""",
        "<p><strong>Opener:</strong> Hi [First Name], it's Alex from Acme. I know I'm calling cold — got 27 seconds to tell you why?</p>",
        "cold+calling+sales+book+script", "Sales Books",
        [("best-chatgpt-prompt-for-sales-pitch", "Sales Pitch"), ("best-chatgpt-prompt-for-negotiation", "Negotiation")]
    ),
    short_page(
        "best-chatgpt-prompt-for-saas-landing-page",
        "Best ChatGPT Prompt for SaaS Landing Page",
        "Write SaaS landing page copy that converts — from above-the-fold headline to pricing CTA.",
        """You are a SaaS copywriter. Write landing page copy.

Product: [NAME + ONE-LINE PITCH]
Target customer: [ICP WITH PAIN POINT]
Biggest competitor: [NAME + HOW YOU BEAT THEM]
Pricing: [TIERS]
Social proof available: [LOGOS / TESTIMONIALS / STATS]
Primary CTA: [START TRIAL / BOOK DEMO / SIGN UP]

Write:
1. Hero headline (value prop in one line) + subheadline
2. Hero CTA
3. Logo strip headline
4. 3-feature section with benefit-led headlines
5. How it works (3-step visual with copy)
6. Use case / customer story
7. Testimonial block
8. Pricing section copy
9. FAQ (top 8)
10. Footer CTA

Requirements: Benefit > feature. Specific numbers in headlines. Under 600 words total. Remove any 'empower,' 'synergize,' 'unlock.'""",
        "<p><strong>Hero:</strong> Ship code faster than ever — without the 3am incidents. Subhead: The observability platform that catches bugs before your users do.</p>",
        "SaaS+copywriting+marketing+book", "SaaS Marketing Books",
        [("best-chatgpt-prompt-for-copywriting", "Copywriting"), ("best-chatgpt-prompt-for-email-marketing", "Email Marketing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-slide-deck",
        "Best ChatGPT Prompt for Slide Deck",
        "Structure a slide deck that holds attention and moves the room — internal, external, or keynote.",
        """You are a presentation designer who has built decks for Fortune 500 execs. Structure a deck for me.

Audience: [WHO]
Purpose: [INFORM / PERSUADE / SELL / INSPIRE]
Length: [SLIDES OR MINUTES]
Key message (what you want them to do): [ACTION]
Evidence you have: [DATA / STORIES / EXAMPLES]

Structure:
1. Title slide (hook, not logo)
2. Opening (the stakes — why this matters now)
3. Problem setup
4. Insight (the reframe)
5. Solution or path forward
6. Evidence and proof
7. Action / ask
8. Q&A (with anticipated tough questions)

Per slide guidance:
- One idea per slide
- Headline states the takeaway (not the topic)
- Visual > text
- Notes field has the full spoken version

Requirements: No bullet slides with 20 sub-bullets. Every slide earns its place.""",
        "<p><strong>Slide 5 headline:</strong> 'Our activation dropped 23% last quarter — here's why' (not 'Q3 Activation Review')</p>",
        "presentation+slide+deck+book+design", "Presentation Books",
        [("best-chatgpt-prompt-for-pitch-deck", "Pitch Deck"), ("best-chatgpt-prompt-for-webinar-script", "Webinar Script")]
    ),
    short_page(
        "best-chatgpt-prompt-for-product-launch",
        "Best ChatGPT Prompt for Product Launch Plan",
        "Plan a product launch — pre-launch, launch week, post-launch — with channels, assets, and metrics.",
        """You are a product marketer who has launched 20+ products. Plan my launch.

Product: [WHAT IT IS + TARGET CUSTOMER]
Launch date: [DATE]
Budget: $[AMOUNT]
Existing audience: [EMAIL LIST / SOCIAL / PAID REACH]
Goal: [REVENUE / SIGNUPS / DOWNLOADS / AWARENESS]

Build:
1. Pre-launch plan (T-30 to T-7)
2. Launch week playbook (day by day)
3. Post-launch follow-up (week 2-4)
4. Asset checklist (announcement, landing page, emails, social)
5. PR and influencer outreach list template
6. Success metrics and measurement plan
7. Risk mitigation (what if crickets, what if flooded)

Requirements: Realistic budget allocation. Over-invest in pre-launch list building. Plan for low-traffic day 1.""",
        "<p><strong>T-14:</strong> Open waitlist with limited early-bird pricing. Email list 3x/week with teasers. Influencer package mailers go out.</p>",
        "product+launch+marketing+book", "Launch Books",
        [("best-chatgpt-prompt-for-press-release", "Press Release"), ("best-chatgpt-prompt-for-email-marketing", "Email Marketing")]
    ),
    short_page(
        "best-chatgpt-prompt-for-roast",
        "Best ChatGPT Prompt for Roast Speech",
        "Write a roast speech that gets real laughs without crossing the line — for birthdays, retirements, or friendly occasions.",
        """You are a comedy writer who has written for roasts and celebrity shows. Help me write a roast.

Who's being roasted: [NAME + RELATIONSHIP TO YOU]
Occasion: [BIRTHDAY / RETIREMENT / FAREWELL]
Audience: [WHO WILL HEAR IT]
5 specific true things about them worth roasting: [LIST — real quirks, jobs, stories, habits]
What they love: [TO MAKE WARM CALLBACKS]
Topics OFF-LIMITS: [ANYTHING SENSITIVE]
Length: [MINUTES]

Structure:
1. Opening compliment that's a setup for the first burn
2. 3-5 roast jokes based on their real traits
3. One callback through the whole set
4. Sincere turn near the end
5. Close with a line they'll quote for years

Requirements: Punch down = never. Ratio 3:1 roast to love. Specific > generic. No stolen jokes. The warmth at the end is what people remember.""",
        "<p><strong>Setup/burn:</strong> Dave has been my friend for 30 years. In those 30 years, he has never once — and I mean never — picked the right parking spot.</p>",
        "comedy+writing+speech+book", "Comedy Writing Books",
        [("best-chatgpt-prompt-for-wedding-speech", "Wedding Speech"), ("best-chatgpt-prompt-for-speech", "Any Speech")]
    ),
    short_page(
        "best-chatgpt-prompt-for-nonprofit-appeal",
        "Best ChatGPT Prompt for Nonprofit Donation Appeal",
        "Write donation appeals that move people to give — year-end, email, direct mail, or event.",
        """You are a direct-response fundraiser who has raised $100M+ for nonprofits. Write an appeal.

Organization: [NAME + MISSION]
Appeal type: [YEAR-END / EMERGENCY / MONTHLY / CAPITAL]
Audience: [DONOR SEGMENT]
Goal: $[AMOUNT]
Channel: [EMAIL / LETTER / LANDING PAGE]
Key story / beneficiary: [SPECIFIC PERSON OR SITUATION]
Specific outcome funded: [WHAT $50 DOES, WHAT $500 DOES]
Match or deadline: [IF ANY]

Write:
1. Subject/headline that makes donor stop
2. Opening scene (one person, specific detail)
3. The stakes (what's lost without donors)
4. Our role in the solution
5. Specific impact of their gift at multiple amounts
6. Direct ask
7. P.S. with urgency or match

Requirements: Emotional anchor in real story. Concrete dollar → impact. Avoid 'help us help them.' Donor is the hero, not the org.""",
        "<p><strong>Opening:</strong> Maria was 8 months pregnant and sleeping in her car when she called us. By morning, we had her in a safe apartment with a working lock and a pediatrician's appointment...</p>",
        "nonprofit+fundraising+book+appeal", "Fundraising Books",
        [("best-chatgpt-prompt-for-grant-writing", "Grant Writing"), ("best-chatgpt-prompt-for-copywriting", "Copywriting")]
    ),
    short_page(
        "best-chatgpt-prompt-for-debate-argument",
        "Best ChatGPT Prompt for Debate Argument",
        "Build a debate argument with strong claims, evidence, rebuttals, and anticipated counterarguments.",
        """You are a debate coach. Help me build an argument.

Resolution or topic: [STATEMENT]
My side: [AFFIRM / NEGATE]
Format: [POLICY / LINCOLN-DOUGLAS / PUBLIC FORUM / CASUAL]
Time limit: [MINUTES for main speech]
Audience: [JUDGE TYPE OR GENERAL]

Build:
1. Overview of my position in one sentence
2. 3 strongest arguments with warrants + evidence
3. Anticipated counterarguments from opposing side
4. Rebuttals to each counterargument
5. The ONE question I want the judge to consider
6. Strongest framing (values, impact, methodology)
7. Closing statement that returns to the framing

Requirements: Every claim needs a warrant + evidence. Concede small points to win bigger ones. No ad hominem.""",
        "<p><strong>Argument 1:</strong> Claim — A 4-day work week increases productivity. Warrant — Reduced decision fatigue. Evidence — Iceland 2015-2019 study, 2,500 workers, maintained output, increased well-being.</p>",
        "debate+argument+rhetoric+book", "Debate Books",
        [("best-chatgpt-prompt-for-essay-writing", "Essay Writing"), ("best-chatgpt-prompt-for-negotiation", "Negotiation")]
    ),
    short_page(
        "best-chatgpt-prompt-for-customer-persona",
        "Best ChatGPT Prompt for Customer Persona",
        "Build a detailed customer persona from interviews or observations — to guide marketing, product, and sales.",
        """You are a customer research strategist. Build a persona from my inputs.

My product/service: [WHAT YOU SELL]
Interviews or data I have (paste): [NOTES, QUOTES, STATS]
Market category: [INDUSTRY]

Create persona with:
1. Name + stock photo description
2. Demographics (age, role, income, location)
3. Professional context (company size, responsibilities)
4. Goals they're trying to achieve
5. Pains and frustrations (specific quotes if available)
6. What they've tried before (and why it failed)
7. Information sources (where they learn)
8. Objections to products like yours
9. Trigger event that makes them seek a solution
10. A 'day in the life' vignette

Requirements: Ground in real data, not imagination. Specific over generic. Flag where you lack information.""",
        "<p><strong>Pain:</strong> 'I spend Sunday nights re-building the spreadsheet because someone always breaks a formula.' — Priya, Ops Lead at 50-person startup</p>",
        "customer+research+marketing+persona+book", "Marketing Books",
        [("best-chatgpt-prompt-for-customer-survey", "Customer Survey"), ("best-chatgpt-prompt-for-content-ideas", "Content Ideas")]
    ),
    short_page(
        "best-chatgpt-prompt-for-landing-page-audit",
        "Best ChatGPT Prompt for Landing Page Audit",
        "Audit your landing page for conversion-killing mistakes — with specific fixes ranked by impact.",
        """You are a conversion rate optimization expert. Audit my landing page.

Page URL or text (paste): [CONTENT]
Goal: [WHAT CONVERSION MATTERS]
Current conversion rate (if known): [%]
Traffic source: [SEO / ADS / SOCIAL / EMAIL]

Audit:
1. First 5 seconds — does visitor know what this is?
2. Headline clarity + benefit
3. Above the fold CTA visibility
4. Social proof placement
5. Friction points (form length, steps, jargon)
6. Mobile readability
7. Trust signals and objection handling
8. Copy concreteness (benefit vs feature)
9. Page speed and visual hierarchy
10. One big recommendation

Output format:
- Top 5 issues ranked by impact
- Specific fix for each
- A/B test suggestions
- Quick wins vs bigger overhauls""",
        "<p><strong>Issue 1 (High Impact):</strong> Headline says 'Transform your workflow' — no one Googles that. Change to 'Automate QuickBooks invoicing in under 5 min' — specific outcome + tool.</p>",
        "conversion+optimization+landing+page+book", "CRO Books",
        [("best-chatgpt-prompt-for-copywriting", "Copywriting"), ("best-chatgpt-prompt-for-seo", "SEO")]
    ),
    short_page(
        "best-chatgpt-prompt-for-book-club-questions",
        "Best ChatGPT Prompt for Book Club Discussion Questions",
        "Generate book club discussion questions that go beyond 'did you like it?' — with depth across character, theme, and craft.",
        """You are a book club facilitator. Write discussion questions for a book.

Book: [TITLE + AUTHOR]
Genre: [FICTION / MEMOIR / HISTORY / OTHER]
Main themes: [KEY IDEAS]
Group's typical depth: [CASUAL / LITERARY / MIXED]
Meeting time: [MINUTES]

Generate 12 questions covering:
1. Opening warm-up (low stakes, personal)
2. Character (motivation, change, sympathy)
3. Plot choices (why this, not that)
4. Theme (what is the book really about)
5. Craft (pov, structure, prose)
6. Ethical or philosophical (debate-worthy)
7. Comparative (other books, real life)
8. Ending (satisfying? earned?)
9. What you'd ask the author
10. What you'd change if you could
11. Who would you recommend this to and who would you NOT
12. Closing — the one image or line that stays

Requirements: Open-ended. Avoid trivia. Questions should generate disagreement, not consensus.""",
        "<p><strong>Q6:</strong> The protagonist makes a choice at p.214 that many readers find indefensible. Do you think the book is asking us to agree, understand, or judge?</p>",
        "book+club+discussion+guide+book", "Book Club Books",
        [("best-chatgpt-prompt-for-book-summary", "Book Summaries"), ("best-chatgpt-prompt-for-book-recommendations", "Book Recommendations")]
    ),
    short_page(
        "best-chatgpt-prompt-for-slide-bio",
        "Best ChatGPT Prompt for Professional Bio",
        "Write a professional bio that works everywhere — speaker intros, LinkedIn summary, website about page — in 3 lengths.",
        """You are a personal branding expert. Write my professional bio.

Name: [NAME]
Current role: [TITLE at COMPANY]
Industry: [FIELD]
Key accomplishments: [TOP 3]
Unique angle: [WHAT SETS YOU APART]
Tone: [AUTHORITATIVE / WARM / WITTY / MIXED]
Where it will appear: [WEBSITE / LINKEDIN / SPEAKER SITE]

Write three versions:
1. 1-sentence bio (for Twitter, speaker intro line)
2. 3-sentence bio (for LinkedIn summary, website)
3. Longer 150-word bio (for keynote intros, about pages)

Each should:
- Lead with value, not title
- Include one specific achievement
- Have one humanizing detail
- Match the tone requested
- Be third-person for speaker/media, first-person for LinkedIn/personal

Requirements: Avoid 'passionate about,' 'thought leader,' 'guru.' Use specifics instead of adjectives.""",
        "<p><strong>1-sentence:</strong> Sarah Chen builds product teams at companies that have outgrown 'move fast and break things.'</p>",
        "personal+branding+professional+bio+book", "Branding Books",
        [("best-chatgpt-prompt-for-linkedin-profile", "LinkedIn Profile"), ("best-chatgpt-prompt-for-writing-a-resume", "Writing a Resume")]
    ),
    short_page(
        "best-chatgpt-prompt-for-instagram-story-ideas",
        "Best ChatGPT Prompt for Instagram Story Ideas",
        "Get a week of Instagram Story content ideas that build engagement and drive profile visits.",
        """You are an Instagram strategist for creators and small businesses. Plan my Stories.

Account niche: [WHAT YOU POST ABOUT]
Goal: [ENGAGEMENT / DRIVING TO LINK / SAVES / PROFILE VISITS]
Weekly posting cadence: [HOW OFTEN]
Story lengths: [QUICK 3-5 FRAMES / LONGER 10+]
Current follower count: [APPROX]
Existing assets: [VIDEO / PHOTOS / BTS]

Give me:
1. 7-day Story plan (one theme per day)
2. 3 frame ideas per day with CTAs (poll, slider, question box, DM prompt)
3. Content pillars Stories should support
4. Template for 'About Me' or 'Start Here' evergreen highlight
5. Tactics that drive profile visits (controversy, teases, question prompts)
6. What NOT to post (stuff that kills reach)

Requirements: Interactive stickers where natural. Avoid constant promotion. Balance value, personality, proof, CTAs.""",
        "<p><strong>Monday — 'Mailbag Monday':</strong> Frame 1: question sticker 'what's frustrating you at work this week?' Frames 2-4: answer 2-3 responses with helpful tips.</p>",
        "Instagram+marketing+book+content", "Instagram Books",
        [("best-chatgpt-prompt-for-instagram-bio", "Instagram Bio"), ("best-chatgpt-prompt-for-social-media-captions", "Social Media Captions")]
    ),
    short_page(
        "best-chatgpt-prompt-for-retention-email",
        "Best ChatGPT Prompt for Retention / Winback Emails",
        "Win back churned customers or re-engage inactive users with sequences that actually work — not desperate discounts.",
        """You are a lifecycle email specialist. Design a retention sequence.

Sequence type: [WINBACK / RE-ENGAGEMENT / ANTI-CHURN PRE-EMPTIVE]
My product: [WHAT YOU SELL]
Customer segment: [WHO GETS THIS]
Last activity: [WHEN THEY LAST USED OR BOUGHT]
Known reason for leaving / going quiet: [IF KNOWN]
Offer I can make: [DISCOUNT / NEW FEATURE / CHECK-IN ONLY]

Design:
1. 4-5 email sequence with timing (e.g. day 0, 3, 7, 14, 30)
2. Purpose of each email (acknowledge, resume value, remind of ROI, ask why, final ask)
3. Subject lines per email
4. Body copy skeleton per email
5. CTA per email (not the same every time)
6. When to give up and when to stop emailing
7. Segment-specific branches

Requirements: Don't lead with discount. Ask 'why did you leave' before fixing. Last email should respectfully let them go.""",
        "<p><strong>Email 2 (Day 7) subject:</strong> Can I ask you something? (Body: one question — what was missing? — no pitch, just reply CTA)</p>",
        "email+lifecycle+marketing+book", "Lifecycle Books",
        [("best-chatgpt-prompt-for-email-marketing", "Email Marketing"), ("best-chatgpt-prompt-for-copywriting", "Copywriting")]
    ),
]

count = 0
for page in PAGES:
    make_page(**page)
    count += 1
    print(f"Created: {page['slug']}.html")
print(f"\nTotal pages created: {count}")
