"""Batch 3: 20 more high-traffic pages."""
import sys
sys.path.insert(0, 'scripts')
from page_template import make_page

PAGES = [
    {
        "slug": "best-chatgpt-prompt-for-book-writing",
        "title": "Best ChatGPT Prompt for Book Writing",
        "subtitle": "Outline a novel, develop characters, and write chapters with AI as your writing partner — not your ghostwriter.",
        "prompt": """You are a bestselling novelist and editor who has worked with first-time authors to finished manuscript. Help me write a book.

What I need help with: [pick one]
- Outline a novel from my premise: [PREMISE]
- Develop the main character: [BRIEF DESCRIPTION]
- Fix a structural problem in my plot: [DESCRIBE THE ISSUE]
- Write a chapter outline: [CHAPTER GOAL]
- Edit a scene I wrote: [PASTE SCENE]

Book details:
- Genre: [literary / thriller / romance / sci-fi / fantasy / mystery / memoir / nonfiction]
- Target length: [word count]
- POV: [first / third limited / third omniscient]
- Tone: [dark / funny / literary / pulpy]
- My experience: [first novel / published before / hobbyist]

Requirements:
- Don't write prose for me — give me structure, questions, options
- For outlines, use a proven framework (Save the Cat, Three-Act, Hero's Journey) matched to genre
- For character work, ask questions I need to answer about wants/fears/wounds
- For plot fixes, identify the root cause (often character motivation)
- For editing, mark specific sentences and say why they work or don't
- Always preserve my voice — don't rewrite into generic AI prose""",
        "how_to_use": [
            "Use AI for structure and problem-solving, never for the actual prose",
            "Write your own sentences — they're what readers connect with",
            "When stuck, ask 'What's the scene I'm avoiding?' — usually that's the scene that matters most",
            "Track progress with chapter outlines, not daily word counts",
        ],
        "example_output": """<p><strong>Request:</strong> Three-act outline for a literary thriller about a woman who realizes her new husband killed his first wife.</p>
<p><strong>Act One — setup (25% of book):</strong></p>
<ul><li>Open: Protagonist's genuine happiness with new husband — we need to feel the loss before the revelation hits.</li>
<li>Inciting incident (around 10%): Discovery of something small that doesn't fit. A key, a photograph, a date that's wrong.</li>
<li>Break into Act Two: She asks him about it. His answer is reasonable. Too reasonable. That's the last moment of her innocence.</li></ul>
<p><strong>Key question to answer before writing:</strong> What does she believe about herself that would make her NOT want to see the truth? That belief is the core of the book. Without it, there's no tension — just an investigation.</p>""",
        "tips": [
            "<strong>Start with the ending.</strong> Ask 'Draft the last scene first. What's the emotional resolution?'",
            "<strong>Character wound.</strong> Ask 'What's the wound my protagonist carries that shapes every decision?'",
            "<strong>Plot vs. character.</strong> Ask 'Is this a plot problem or a character motivation problem?' Usually the latter.",
            "<strong>Cut the opening.</strong> After drafting, ask 'Where should my book actually start? Often not at page 1.'",
        ],
        "amazon_keywords": "writing+novel+book+craft",
        "amazon_text": "Writing Craft Books",
        "related": [("best-chatgpt-prompt-for-creative-writing", "Creative Writing"), ("best-chatgpt-prompt-for-essay-writing", "Essay Writing")],
    },
    {
        "slug": "best-chatgpt-prompt-for-pitch-deck",
        "title": "Best ChatGPT Prompt for Pitch Deck",
        "subtitle": "Build an investor-ready pitch deck with a compelling story, clear metrics, and the 10 slides that actually close rounds.",
        "prompt": """You are a seed and Series A investor who has seen 1,000+ pitch decks and invested in 50+ startups. Help me build a pitch deck.

Company: [NAME]
Stage: [pre-seed / seed / Series A]
Industry: [INDUSTRY]
What we do in one sentence: [THE SIMPLE VERSION]
Who we sell to: [CUSTOMER PROFILE]
Traction to date: [REVENUE, USERS, GROWTH — BE SPECIFIC]
Team: [FOUNDERS AND KEY PEOPLE]
Raising: $[AMOUNT]
Use of funds: [WHAT YOU'LL SPEND IT ON]
Unfair advantage: [WHAT MAKES THIS WORK THAT OTHERS CAN'T COPY]

Build me a 10-slide deck with:
1. Title slide — company name, tagline, contact
2. Problem — what pain exists, with evidence (not "people want more of X")
3. Solution — what we built, with a concrete demo image/flow
4. Why now — what's changed in the world that makes this inevitable
5. Market size — TAM/SAM/SOM with bottom-up math, not top-down
6. Business model — how we make money, unit economics
7. Traction — growth over time, with real numbers
8. Competition — who else does this, why we win (2x2 matrix works)
9. Team — why us, specifically
10. Ask — how much, what it buys, key milestones to next round

Requirements:
- Each slide: one key message, not a wall of text
- Numbers over adjectives. Specific over general.
- Cut any slide that doesn't move the investor closer to "yes"
- Include speaker notes for each slide (what to say, not read)
- Flag slides that need design work vs. slides that are prose""",
        "how_to_use": [
            "Be ruthlessly specific — investors see 100 decks a week, yours needs real numbers",
            "Do the bottom-up market sizing math — top-down TAM slides are red flags",
            "After the outline, ask for slide copy: 'Write slide 2 with headline, 3 bullets, and speaker notes'",
            "Practice the pitch out loud — a great deck can't save a bad pitch",
        ],
        "example_output": """<p><strong>Slide 2 — Problem (Example for a B2B SaaS):</strong></p>
<p><strong>Headline:</strong> Sales teams waste 37% of their day on CRM data entry. [Source: Salesforce 2024]</p>
<p><strong>Supporting points:</strong></p>
<ul><li>Average AE logs 2.4 hrs/day of activities that could be automated</li>
<li>70% of deals have incomplete or wrong CRM data, costing pipeline visibility</li>
<li>Existing tools (Outreach, Gong) capture conversations but don't update CRM automatically</li></ul>
<p><strong>Speaker notes:</strong> "This isn't a new problem. What's new is that AI finally makes it solvable at scale. We talked to 200 sales leaders over the last 6 months. Every single one said the same thing: reps spend too much time as typists, not sellers."</p>""",
        "tips": [
            "<strong>Top 3 slides matter most.</strong> Problem, solution, traction. If these don't land, the rest won't save you.",
            "<strong>Traction is your best slide.</strong> Ask 'How do I visualize my growth clearly — chart type, time period, y-axis scale?'",
            "<strong>Competition honesty.</strong> Ask 'What's the strongest argument a competitor could make against us?' Address it.",
            "<strong>10 slides, max.</strong> Ask 'Which slides could I cut?' — shorter is always better than longer.",
        ],
        "amazon_keywords": "pitch+deck+startup+funding+book",
        "amazon_text": "Startup Books on Amazon",
        "related": [("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan"), ("best-chatgpt-prompt-for-sales-pitch", "Sales Pitch")],
    },
    {
        "slug": "best-chatgpt-prompt-for-press-release",
        "title": "Best ChatGPT Prompt for Press Release",
        "subtitle": "Write press releases that journalists actually read — with the angle, quotes, and structure that get coverage.",
        "prompt": """You are a PR professional who has placed stories in TechCrunch, NYT, Wall Street Journal, and trade publications. Write a press release for me.

What the release is about: [e.g. product launch, funding round, hire, milestone, partnership]
Company: [NAME, ONE-LINE DESCRIPTION]
Key news: [THE ACTUAL NEWS IN ONE SENTENCE]
Why this matters beyond the company: [THE BROADER STORY]
Target audience: [tech press / industry trade / local news / business press]
Dateline location: [CITY, STATE]
Quote from executive: [WHO + WHAT THEY WANT TO SAY]
Quote from customer/partner (if available): [NAME + COMPANY + POTENTIAL QUOTE DIRECTION]
Available assets: [high-res images, demo video, founder photos]

Write:
1. Headline — clear, specific, news-forward (not marketing hype)
2. Subhead — one line adding context
3. Dateline
4. Lead paragraph — the 5 W's in the first 2 sentences
5. Second paragraph — context and significance
6. Executive quote
7. Supporting details (2-3 paragraphs)
8. Customer or partner quote (if applicable)
9. Boilerplate company description
10. Media contact

Requirements:
- No marketing language ('revolutionary,' 'game-changing,' 'disruptive')
- Lead with the news, not the company
- Keep headline under 12 words
- Total length under 500 words
- Quotes should sound like humans talking, not press release robots
- Include a clear "why should a journalist care" angle""",
        "how_to_use": [
            "Write the headline last — once you know the story, the headline writes itself",
            "Send the release TO a journalist with a short 3-line pitch email, not as an attachment dump",
            "Target 3-5 specific journalists covering your beat, not 100 random press contacts",
            "After sending, follow up ONCE after 3 business days — then let it go",
        ],
        "example_output": """<p><strong>Headline:</strong> Acme Labs Raises $12M Series A to Automate Supply Chain Audits</p>
<p><strong>Subhead:</strong> Funding will triple engineering team to address compliance backlog affecting thousands of mid-market manufacturers.</p>
<p><strong>SAN FRANCISCO, CA — April 16, 2026</strong> — Acme Labs, an AI-powered compliance platform for manufacturers, today announced a $12 million Series A round led by Benchmark Partners, with participation from Initialized Capital and existing investors.</p>
<p>The funding addresses a growing bottleneck: new trade regulations require manufacturers to audit supply chains quarterly, but most mid-market firms lack the staff or tooling to do it. Acme's platform automates 80% of that work.</p>
<p>"Compliance used to be a back-office headache," said Sarah Chen, CEO and co-founder of Acme Labs. "Now it's a front-office priority, and the companies that can move fastest will win. We're building the tools that make that possible."</p>""",
        "tips": [
            "<strong>Lead with news.</strong> Ask 'Is the first sentence actually news, or is it company description?'",
            "<strong>Kill weak quotes.</strong> Ask 'Rewrite this quote to sound like a real person — cut buzzwords.'",
            "<strong>One angle only.</strong> Ask 'What's the single story hook here? Sharpen everything around it.'",
            "<strong>Pitch email too.</strong> After the release: 'Write the 3-sentence email pitching this to a TechCrunch reporter.'",
        ],
        "amazon_keywords": "public+relations+book+media",
        "amazon_text": "PR Books on Amazon",
        "related": [("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post"), ("best-chatgpt-prompt-for-email-marketing", "Email Marketing")],
    },
    {
        "slug": "best-chatgpt-prompt-for-linkedin-posts",
        "title": "Best ChatGPT Prompt for LinkedIn Posts",
        "subtitle": "Write LinkedIn posts that actually get engagement — without sounding like a LinkedIn influencer.",
        "prompt": """You are a LinkedIn content strategist who has grown executive accounts from 0 to 50K+ followers. Write a LinkedIn post for me.

Post type: [personal story / industry insight / hot take / resource / team shoutout / hiring / announcement]
My role: [YOUR TITLE / INDUSTRY]
My audience: [WHO I WANT TO REACH]
Post goal: [grow followers / attract clients / promote something / share expertise / hire someone]
Core idea or story: [THE THING YOU WANT TO SHARE]
My voice: [authoritative / conversational / funny / direct / warm]
Length: [short (under 100 words) / medium (200-400) / long (500+)]

Requirements:
- Hook in the first line — it has to stop the scroll
- Break up the post with white space (LinkedIn compresses walls of text)
- Use short paragraphs — 1-2 lines each
- Avoid 'Here are 5 lessons I learned' if it's overused in your niche
- No inspirational poster language ('Believe in yourself! 💪')
- End with a question to drive comments, OR a quiet, definitive close — no cliche CTAs like 'Agree?'
- If it's a story, make it feel earned — real specifics, not motivational arc
- If it's an insight, give real evidence, not opinion framed as insight""",
        "how_to_use": [
            "Write from your actual experience — generic LinkedIn posts get generic engagement",
            "Test 3 different hooks — the first line is 80% of the post",
            "Post at the right time — 9-10am Tuesday/Wednesday/Thursday for B2B",
            "Don't chase engagement — the right 10 comments from your audience beat 100 generic likes",
        ],
        "example_output": """<p><strong>Post type:</strong> Personal story for a VP of Product</p>
<p>I killed a feature last week that three senior engineers had spent two months building.</p>
<p>Everyone on the team knew it wasn't working. The data was clear. But no one wanted to be the one to say it.</p>
<p>I called the meeting on Monday. It took 11 minutes.</p>
<p>Here's what I learned: the cost of killing a bad project isn't the project. It's the trust you build with your team when you prove you'll make the hard call yourself, so they don't have to.</p>
<p>The engineers thanked me privately that week. Three of them separately said "I've been wanting to quit this feature for a month."</p>
<p>Bad projects die quietly when they should die loudly.</p>""",
        "tips": [
            "<strong>First line test.</strong> Ask 'Does my first line make someone stop scrolling?'",
            "<strong>Cut weak middles.</strong> Ask 'Delete any paragraph that doesn't earn its spot.'",
            "<strong>Engagement trap.</strong> Ask 'Is my CTA authentic or desperate?' Desperate CTAs tank posts.",
            "<strong>Study top posts.</strong> Paste a top post in your niche and ask 'Why did this work?' — learn the pattern.",
        ],
        "amazon_keywords": "LinkedIn+marketing+book+content",
        "amazon_text": "LinkedIn Books on Amazon",
        "related": [("best-chatgpt-prompt-for-linkedin-profile", "LinkedIn Profile"), ("best-chatgpt-prompt-for-content-ideas", "Content Ideas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-twitter-threads",
        "title": "Best ChatGPT Prompt for Twitter Threads",
        "subtitle": "Write Twitter/X threads that go viral — with hooks, pacing, and structure that keeps people reading all the way down.",
        "prompt": """You are a content creator with 500K+ followers on X, known for threads that regularly get 1M+ impressions. Write a thread for me.

Thread topic: [WHAT IT'S ABOUT]
Core insight: [THE ONE IDEA THE THREAD HAS TO LAND]
My account's niche: [WHAT YOUR FOLLOWERS EXPECT FROM YOU]
Thread length: [5-7 tweets / 8-15 tweets / long form 20+]
Purpose: [grow followers / drive engagement / promote something / establish authority]
Tone: [educational / contrarian / story-driven / numbered list]

Requirements:
- Tweet 1 is the hook — it decides whether anyone reads the rest
- Each tweet advances the idea, no filler
- Break complex ideas into tweet-sized chunks naturally
- Tweet 1 can be bold or controversial — earn it with substance in the thread
- No 'a thread 🧵' as the hook — use a real hook
- Last tweet is either a summary, a callback to tweet 1, or a clear CTA
- Character limit 280 per tweet — pack density, don't pad
- Use formatting sparingly — line breaks within tweets work, all caps doesn't""",
        "how_to_use": [
            "Write tweet 1 for an audience that has never heard of you and owes you nothing",
            "Cut 20% of your tweets on the second pass — threads are tighter than you think",
            "For threads with lessons, number them inside the tweet, not as a separate tweet each",
            "Post threads when your audience is awake — usually 9am-11am or 7pm-9pm in their timezone",
        ],
        "example_output": """<p><strong>Topic:</strong> Why most productivity advice is wrong for ADHD</p>
<p><strong>Tweet 1 (Hook):</strong> Every productivity book tells ADHD people the same useless thing: "Just start with the hardest task first."</p>
<p>This is like telling someone with a broken leg that the key to running is strong legs.</p>
<p>Here's what actually works — from 10 years of trying (and failing) everything.</p>
<p><strong>Tweet 2:</strong> The real problem isn't willpower. It's activation energy.</p>
<p>ADHD brains have unpredictable dopamine response. Starting anything requires more mental fuel than average.</p>
<p>Most advice assumes you already have fuel. We don't.</p>
<p><strong>Tweet 3:</strong> Fix #1: Body double.</p>
<p>Work near another human — coffee shop, coworker on video call, even a stranger's live stream.</p>
<p>Your brain gets just enough accountability to start. This one technique changed my career.</p>""",
        "tips": [
            "<strong>Hook test.</strong> Ask 'If someone only reads tweet 1, did they learn something useful?'",
            "<strong>Bold claims need proof.</strong> Ask 'Every opinion needs a specific example or data point.'",
            "<strong>Cut ruthlessly.</strong> Ask 'Which tweets are redundant or skippable?' Most threads are 30% too long.",
            "<strong>Thread finale.</strong> Ask 'Make the last tweet callback to the first in a satisfying way.'",
        ],
        "amazon_keywords": "Twitter+X+social+media+book",
        "amazon_text": "Social Media Books",
        "related": [("best-chatgpt-prompt-for-linkedin-posts", "LinkedIn Posts"), ("best-chatgpt-prompt-for-content-ideas", "Content Ideas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-tiktok-scripts",
        "title": "Best ChatGPT Prompt for TikTok Scripts",
        "subtitle": "Write TikTok scripts with hooks that grab attention in the first 2 seconds — and keep people until the end.",
        "prompt": """You are a TikTok creator and short-form video strategist who has grown accounts to 1M+ followers. Write a TikTok script for me.

Video topic: [WHAT IT'S ABOUT]
Account niche: [WHAT YOUR ACCOUNT IS ABOUT]
Video length: [15 sec / 30 sec / 60 sec / 90 sec]
Video format: [talking head / POV / voiceover over b-roll / green screen / tutorial / story]
Goal: [growth / engagement / sales / information]
Tone: [energetic / dry / funny / educational / sincere]

Write:
1. Hook (first 2 seconds) — scroll-stopping, specific, visual
2. Opening line (seconds 2-5) — payoff starts here
3. Main content — broken into beats with timestamps
4. Ending — loop back to hook, or cliffhanger, or clear CTA
5. On-screen text captions (TikTok strips audio captions)
6. Suggested background sound or music style
7. Call-to-action that feels natural

Requirements:
- Hook must work without audio (many watch muted)
- No 'Hey guys, today I'm going to talk about...' — cut to the point
- Use pattern interrupts every 3-5 seconds
- Script timing: aim for ~2 words per second of speaking
- Include emoji/text suggestions that will stay on screen
- Avoid overused hooks ('Wait for it,' 'You won't believe,' 'POV:')""",
        "how_to_use": [
            "Time your script out loud — if it runs over, cut",
            "Shoot the hook 3-5 different ways and use the strongest one",
            "Caption every video — 70%+ of viewers watch muted",
            "Watch your last 5 videos and note what worked — feed that into the AI for better future scripts",
        ],
        "example_output": """<p><strong>Video:</strong> 30-second video on "stuff no one tells you about freelancing"</p>
<p><strong>Hook (0:00-0:02):</strong><br><em>On screen text: "I made $120K freelancing last year. Here's what I wish someone told me in year 1."</em><br><em>Visual: Close-up of my face, dramatic lighting</em></p>
<p><strong>Opening (0:02-0:08):</strong><br>"Stop quoting hourly. Your clients don't care about your hours. They care about the outcome. Quote by project."</p>
<p><strong>Beat 2 (0:08-0:15):</strong><br>"And charge more than you think you should. If 30% of clients don't push back on price, you're too cheap."</p>
<p><strong>Beat 3 (0:15-0:24):</strong><br>"Finally: get paid 50% upfront. Non-negotiable. This alone will change your business."</p>
<p><strong>Close (0:24-0:30):</strong><br>"Which of these do you wish someone told you earlier?"</p>""",
        "tips": [
            "<strong>Hook works silent.</strong> Ask 'If someone watched this muted with only captions, would they keep watching?'",
            "<strong>First word matters.</strong> Ask 'Make the first word more specific and concrete.'",
            "<strong>Pattern interrupts.</strong> Ask 'Add a visual or tone shift every 4 seconds.'",
            "<strong>Series potential.</strong> Ask 'Can this video become a 5-part series?' More context with each post.",
        ],
        "amazon_keywords": "TikTok+short+form+video+content",
        "amazon_text": "TikTok Content Books",
        "related": [("best-chatgpt-prompt-for-youtube-scripts", "YouTube Scripts"), ("best-chatgpt-prompt-for-social-media-captions", "Social Media Captions")],
    },
    {
        "slug": "best-chatgpt-prompt-for-newsletter",
        "title": "Best ChatGPT Prompt for Writing a Newsletter",
        "subtitle": "Write newsletters people actually open — Substack, email list, or internal comms — that build a real audience.",
        "prompt": """You are a newsletter writer who has grown a paid newsletter to 25,000 subscribers. Help me write an issue.

Newsletter topic/niche: [YOUR NEWSLETTER'S FOCUS]
Audience: [WHO SUBSCRIBES]
Issue topic: [WHAT THIS ISSUE IS ABOUT]
Issue type: [deep dive / link roundup / personal essay / interview / how-to / industry analysis]
Target length: [500 / 1000 / 2000 words]
Frequency: [weekly / bi-weekly / monthly]
Tone: [conversational / authoritative / funny / literary]

Write:
1. Subject line — 3 options, each with a different hook angle
2. Preview text (shows next to subject line in inbox)
3. Opening paragraph — hook that's personal, not generic
4. Main body — 2-4 clear sections with subheadings
5. One concrete takeaway or action
6. Close — signature-style outro with a genuine question or thought
7. P.S. — the second most-read part of any email; make it matter

Requirements:
- Write like you're emailing ONE person, not broadcasting
- Short paragraphs. White space. Scanability matters.
- Cut corporate language — newsletters die when they feel corporate
- Include one specific story or example, not all abstraction
- Subject line over 40 chars get truncated on mobile — aim for under 35
- Don't use 'In this issue...' or 'Dear subscribers'""",
        "how_to_use": [
            "Write the email to one specific person you know — even an imaginary one",
            "Test subject lines in your email tool (Beehiiv, Substack, ConvertKit all support A/B)",
            "Send on weekdays before 9am in your audience's timezone",
            "Read it out loud before sending — if it sounds like a corporate email, rewrite",
        ],
        "example_output": """<p><strong>Subject line:</strong> I was wrong about delegation</p>
<p><strong>Preview text:</strong> For ten years I told managers to "delegate more." Then I actually studied what happens when they do.</p>
<p><strong>Opening:</strong></p>
<p>For years, I gave the same advice to every overwhelmed manager: delegate more.</p>
<p>Then last quarter I did something I should have done earlier — I actually watched what happens when mid-career managers try to delegate for the first time.</p>
<p>It doesn't go well.</p>
<p><strong>The pattern I saw:</strong></p>
<p>Managers delegate the wrong things. Not the hard decisions — the busywork. They hand off tasks they don't want, not work that will develop their team.</p>
<p><strong>P.S.</strong> If this resonated, hit reply and tell me one thing you delegated this month that actually helped someone grow. I read every reply.</p>""",
        "tips": [
            "<strong>Subject line test.</strong> Ask 'Give me 10 subject lines, then pick the 3 strongest.'",
            "<strong>One idea per issue.</strong> Ask 'What's the ONE thing this email is about?'",
            "<strong>P.S. power.</strong> Ask 'Write a P.S. that makes people reply.'",
            "<strong>Cut the opening.</strong> Often the real start is paragraph 2. Ask 'Is there a stronger first sentence hiding in paragraph 2?'",
        ],
        "amazon_keywords": "email+newsletter+substack+book",
        "amazon_text": "Newsletter Books on Amazon",
        "related": [("best-chatgpt-prompt-for-email-marketing", "Email Marketing"), ("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post")],
    },
    {
        "slug": "best-chatgpt-prompt-for-weight-loss",
        "title": "Best ChatGPT Prompt for Weight Loss Plan",
        "subtitle": "Get a realistic, science-based weight loss plan with calories, workouts, and habits that actually fit your life.",
        "prompt": """You are a registered dietitian and evidence-based fitness coach. Build a weight loss plan for me.

About me:
- Age: [AGE] | Height: [HEIGHT] | Current weight: [WEIGHT] | Goal weight: [WEIGHT]
- Activity level: [sedentary / light / moderate / active]
- Timeline: [months to reach goal]
- Diet preferences or restrictions: [e.g. vegetarian, no dairy, allergies]
- Exercise access: [home / gym / neither]
- Past attempts: [WHAT YOU'VE TRIED AND WHY IT STOPPED WORKING]
- Biggest challenge: [late night eating / no time / emotional eating / plateau]
- Medical considerations: [any, or 'see a doctor if relevant']

Requirements:
- Calculate an estimated calorie target based on TDEE math
- Recommend a 500 cal/day deficit MAX (1 lb/week) — no extreme deficits
- Split macros (protein, carbs, fat) appropriately
- Provide a 3-day sample meal plan at my target calories
- Suggest a realistic exercise plan (4-5 hrs/week, not crazy)
- Address my specific biggest challenge with a plan
- Include non-scale metrics to track (measurements, energy, sleep)
- Tell me when to see a doctor / registered dietitian
- Flag weight-loss claims I should ignore (detoxes, 'fat-burning' foods)""",
        "how_to_use": [
            "Be honest about past attempts — the reasons they failed matter more than the plan itself",
            "Weekly weight fluctuates — track the 7-day average, not daily",
            "Focus on habits you can sustain at your goal weight, not temporary restriction",
            "If you have a medical condition or a BMI >30 or <18.5, work with a doctor, not an AI",
        ],
        "example_output": """<p><strong>Setup:</strong> 32F, 5'6", 180 lbs → 150 lbs goal, moderate activity, 6 months.</p>
<p><strong>TDEE math:</strong> Estimated maintenance ~2,100 cal. Deficit target: 1,600 cal/day = ~1 lb/week loss.</p>
<p><strong>Macros:</strong> Protein 130g (520 cal), Fat 55g (500 cal), Carbs 145g (580 cal).</p>
<p><strong>Sample day (1,600 cal):</strong></p>
<ul><li><strong>Breakfast:</strong> 2 eggs + 1 egg white scrambled, 1 slice whole grain toast, 1/2 avocado. ~400 cal, 25g protein.</li>
<li><strong>Lunch:</strong> Chicken salad bowl — 5oz chicken, greens, roasted veggies, 2 tbsp olive oil dressing, 1/2 cup quinoa. ~500 cal, 40g protein.</li>
<li><strong>Snack:</strong> Greek yogurt (0% fat) with berries. ~200 cal, 20g protein.</li>
<li><strong>Dinner:</strong> Salmon 5oz, roasted sweet potato, sautéed broccoli. ~500 cal, 35g protein.</li></ul>
<p><strong>Non-scale tracking:</strong> Waist, hips, and arm measurements weekly. Sleep quality. Energy levels (1-10). How clothes fit.</p>""",
        "tips": [
            "<strong>Protein first.</strong> Ask 'What's the easiest way to hit my protein target daily?'",
            "<strong>Weekly check-ins.</strong> After 2 weeks: 'Here's my weight trend and measurements. Adjust the plan.'",
            "<strong>Plateau plan.</strong> Ask 'What do I do if I stall for 2+ weeks? How should I reassess?'",
            "<strong>Weekend strategy.</strong> Ask 'How do I handle social eating on weekends without derailing?'",
        ],
        "amazon_keywords": "weight+loss+book+nutrition+fitness",
        "amazon_text": "Weight Loss Books",
        "related": [("best-chatgpt-prompt-for-workout-plan", "Workout Plan"), ("best-chatgpt-prompt-for-meal-planning", "Meal Planning")],
    },
    {
        "slug": "best-chatgpt-prompt-for-running-training-plan",
        "title": "Best ChatGPT Prompt for Running Training Plan",
        "subtitle": "Get a custom running plan — 5K, 10K, half marathon, or marathon — matched to your fitness level and schedule.",
        "prompt": """You are a certified running coach who has trained 1,000+ runners from beginner to Boston qualifier. Build me a running plan.

Goal race: [5K / 10K / half marathon / marathon / general fitness]
Goal date: [DATE]
Target time (if any): [TIME GOAL or 'just finish']
Current fitness: [complete beginner / can run X miles / specific recent race time]
Running experience: [new / returning after break / consistent for X months/years]
Days per week available: [NUMBER]
Time per run: [AVERAGE MINUTES]
Injury history: [list any, or 'none']
Cross-training access: [gym / bike / swim / none]

Build me:
1. Total weeks until race day
2. Week-by-week schedule with run types (easy, long, tempo, intervals, recovery)
3. Target paces for each run type, based on my current ability
4. Specific mileage progression (respecting 10% rule)
5. Tapering plan for the final 2-3 weeks
6. Cross-training and strength recommendations
7. Race-day strategy (pacing, fueling, what to do the night before)
8. What to do if I miss a run (or a full week)
9. Red flags that mean I should see a doctor or PT

Requirements:
- Progress gradually — no mileage jumps over 10% per week
- Include at least 1 full rest day per week for injury prevention
- For half/full marathons, include long run peak 2-3 weeks before race
- Adjust if my timeline is unrealistic — be honest about what's safe""",
        "how_to_use": [
            "Be honest about your current mileage — overestimating leads to injuries",
            "Easy runs should feel EASY (you can talk) — most people run them too hard",
            "Don't add intensity AND volume in the same week — one at a time",
            "After 4-6 weeks: 'Here's what I've completed and how I feel. Adjust the plan.'",
        ],
        "example_output": """<p><strong>Setup:</strong> First half marathon in 14 weeks. Currently runs 2x/week, ~2 miles per run. Goal: finish feeling strong.</p>
<p><strong>Week 1 (base building):</strong></p>
<ul><li><strong>Mon:</strong> Rest or walk</li>
<li><strong>Tue:</strong> 2 miles easy pace (conversational)</li>
<li><strong>Wed:</strong> Strength training, 30 min (body weight)</li>
<li><strong>Thu:</strong> 2 miles easy</li>
<li><strong>Fri:</strong> Rest</li>
<li><strong>Sat:</strong> Long run: 3 miles, very slow</li>
<li><strong>Sun:</strong> Recovery walk 30-45 min</li></ul>
<p><strong>Peak week (week 12, before taper):</strong></p>
<ul><li><strong>Tue:</strong> 4 miles easy</li>
<li><strong>Thu:</strong> 4 miles with 2 miles at race pace mid-run</li>
<li><strong>Sat:</strong> Long run: 11 miles (dress rehearsal for race)</li>
<li><strong>Total:</strong> ~22 miles</li></ul>
<p><strong>Race day fueling:</strong> Practice this during your long runs — use same gels/drinks you'll use on race day. Never try anything new on race day.</p>""",
        "tips": [
            "<strong>Easy miles dominate.</strong> Ask 'What percentage of my weekly mileage should be easy?' 80/20 rule.",
            "<strong>Long run rules.</strong> Ask 'How should I fuel and hydrate on long runs over 90 minutes?'",
            "<strong>Injury check.</strong> Ask 'What are early signs of [overuse injury] and when should I take a rest week?'",
            "<strong>Race week.</strong> Ask 'Write me a race-week schedule from 7 days out through the morning of.'",
        ],
        "amazon_keywords": "running+marathon+training+book",
        "amazon_text": "Running Books on Amazon",
        "related": [("best-chatgpt-prompt-for-workout-plan", "Workout Plan"), ("best-chatgpt-prompt-for-weight-loss", "Weight Loss Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-sleep-better",
        "title": "Best ChatGPT Prompt for Sleeping Better",
        "subtitle": "Diagnose why you're sleeping badly and get a step-by-step plan to actually fix it — based on sleep science, not myths.",
        "prompt": """You are a sleep medicine specialist and behavioral sleep coach. Help me fix my sleep.

My main sleep problem (pick all that apply):
- Can't fall asleep
- Wake up in the middle of the night
- Wake up too early
- Wake up exhausted
- Inconsistent sleep schedule
- Feeling groggy all morning

How long has this been going on: [DAYS / WEEKS / MONTHS / YEARS]
My current sleep times: [BEDTIME → WAKE TIME]
Sleep I'd like: [TARGET HOURS AND TIMES]
Caffeine: [WHEN + HOW MUCH]
Alcohol: [WHEN + HOW OFTEN]
Exercise: [TYPE + WHEN]
Screens at night: [WHAT + FOR HOW LONG BEFORE BED]
Bedroom environment: [temperature, light, noise]
Stress level: [1-10]
Any medications: [list any]

Build me:
1. Most likely root cause based on what I described
2. 2-week reset plan — what to change each week
3. Bedtime routine (30-60 min) that supports sleep
4. Morning routine that sets up tonight's sleep
5. What to do when I wake up in the middle of the night
6. Sleep hygiene rules I'm probably breaking
7. Environmental tweaks (temperature, darkness, noise)
8. When to see a doctor (signs of real sleep disorder)

Requirements:
- Base advice on sleep science, not sleep myths (sleep need is individual, 8 hours is an average not a rule)
- Prioritize behavior change over supplements
- Flag any pattern that needs medical attention (loud snoring + daytime sleepiness = possible sleep apnea)
- Don't recommend melatonin as default — it's misused 90% of the time""",
        "how_to_use": [
            "Be honest about caffeine and alcohol — they're the top two fixable sleep killers",
            "Track for 2 weeks before making big changes — you need a baseline",
            "Fix consistency first — same wake time every day beats any other intervention",
            "If symptoms persist or include loud snoring/gasping, see a sleep doctor — ChatGPT can't diagnose",
        ],
        "example_output": """<p><strong>Symptom:</strong> Fall asleep fine, wake at 3am, can't get back to sleep.</p>
<p><strong>Most likely cause:</strong> Alcohol in evening, elevated stress, or late caffeine. Night waking at 3am is often cortisol spiking too early.</p>
<p><strong>Week 1 reset:</strong></p>
<ul><li>Same wake time every day (including weekends)</li>
<li>Caffeine cutoff: 12pm</li>
<li>Alcohol: skip for 2 weeks to see baseline</li>
<li>Phone in another room at night</li></ul>
<p><strong>If you wake at 3am:</strong> Don't look at the clock. Don't pick up your phone. Get out of bed, sit in dim light for 15-20 min doing something boring (book, not screen). Return when drowsy. Staying in bed awake trains your brain that bed = anxiety.</p>
<p><strong>Red flag:</strong> If you snore loudly + feel unrested no matter how many hours, see a doctor about sleep apnea.</p>""",
        "tips": [
            "<strong>Wake time is king.</strong> Ask 'Why is consistent wake time more important than bedtime?'",
            "<strong>Light is the biggest lever.</strong> Ask 'How should I use morning and evening light to fix my circadian rhythm?'",
            "<strong>Temperature.</strong> Ask 'What's the optimal bedroom temperature and why does it matter for sleep?'",
            "<strong>Anxiety loops.</strong> Ask 'What's the CBT-I technique for getting back to sleep without spiraling?'",
        ],
        "amazon_keywords": "sleep+book+insomnia+science",
        "amazon_text": "Sleep Books on Amazon",
        "related": [("best-chatgpt-prompt-for-meditation-script", "Meditation Scripts"), ("best-chatgpt-prompt-for-habit-building", "Building a Habit")],
    },
    {
        "slug": "best-chatgpt-prompt-for-morning-routine",
        "title": "Best ChatGPT Prompt for Morning Routine",
        "subtitle": "Design a morning routine you'll actually keep — based on your schedule, energy, and goals, not influencer fantasy.",
        "prompt": """You are a behavioral coach who designs realistic morning routines for busy people. Build a morning routine for me.

My situation:
- What time I currently wake up: [TIME]
- What time I NEED to leave or start work: [TIME]
- Current routine (honest): [WHAT YOU ACTUALLY DO]
- How I feel in the morning: [energized / groggy / anxious / rushed]
- Kids or dependents in the morning: [YES - how many and ages / NO]
- Goals for my morning: [more energy / calm start / exercise / creative work / spiritual practice]
- What I tried before that didn't stick: [WHAT DIDN'T WORK AND WHY]

Build me:
1. A realistic minute-by-minute routine based on the time I have
2. Non-negotiables (3 things I MUST do)
3. Nice-to-haves (things I do when I have extra time)
4. A "survival mode" 5-minute version for bad days
5. What to prepare the night before (huge leverage)
6. What to CUT from my current routine
7. A 30-day plan to transition from current → new routine
8. The single habit that will drive everything else

Requirements:
- Start with what I actually have — not an idealized 5am wake-up
- Front-load high-value actions (exercise, thinking) before life takes over
- Minimize decisions in the morning (prep the night before)
- Be realistic — 10-step routines fail, 3-step routines stick
- Phone comes out LAST, not first — protect the first hour""",
        "how_to_use": [
            "Design for your actual life — if you have kids, the routine has to work with interruptions",
            "Start with 2-3 anchors and build gradually — full routines fail on day 3",
            "Prepare the night before — it's the highest-leverage morning hack",
            "After 2 weeks: 'Here's what stuck and what didn't. Redesign based on reality.'",
        ],
        "example_output": """<p><strong>Setup:</strong> Wakes at 6:30am, needs to be at work 8:30am. Groggy mornings. Goals: more energy + one focused hour before work.</p>
<p><strong>Non-negotiables:</strong></p>
<ol><li>Wake same time every day (yes, including weekends for first month)</li>
<li>Sunlight in first 10 minutes (go outside even for 2 min)</li>
<li>No phone until 7:15am</li></ol>
<p><strong>Routine:</strong></p>
<ul><li><strong>6:30:</strong> Alarm. Feet on floor immediately (don't negotiate with yourself)</li>
<li><strong>6:32-6:35:</strong> Water (16oz, left next to bed the night before)</li>
<li><strong>6:35-6:45:</strong> Outside for 5-10 min. Walk around the block or sit on porch. Phone stays inside.</li>
<li><strong>6:45-7:15:</strong> Focused work block — whatever matters most (writing, workout, reading). NO phone.</li>
<li><strong>7:15-7:45:</strong> Shower, breakfast. Phone allowed now.</li>
<li><strong>7:45-8:15:</strong> Getting ready + commute prep.</li></ul>
<p><strong>Night-before setup:</strong> Clothes laid out. Water by bed. Phone charging in kitchen, not bedroom.</p>""",
        "tips": [
            "<strong>Phone last, not first.</strong> Ask 'Why does checking my phone first kill the rest of the morning?'",
            "<strong>Anchor to one habit.</strong> Ask 'What's the keystone habit that makes everything else possible?'",
            "<strong>Rushed mornings.</strong> Ask 'Write me a 5-minute version for days I oversleep.'",
            "<strong>Kids version.</strong> Ask 'Adapt this for someone with 2 kids under 5 who wake up needing attention.'",
        ],
        "amazon_keywords": "morning+routine+book+productivity",
        "amazon_text": "Morning Routine Books",
        "related": [("best-chatgpt-prompt-for-habit-building", "Building a Habit"), ("best-chatgpt-prompt-for-goal-setting", "Goal Setting")],
    },
    {
        "slug": "best-chatgpt-prompt-for-decluttering",
        "title": "Best ChatGPT Prompt for Decluttering",
        "subtitle": "Declutter your home room-by-room with a realistic plan that doesn't require a weekend-long marathon.",
        "prompt": """You are a professional organizer certified in the KonMari method with 10 years of experience. Help me declutter.

My situation:
- Home type: [apartment / house / specific rooms I want to tackle]
- How overwhelmed I am: [1-10 scale]
- Sentimental clutter challenge: [kid's stuff / parent's stuff / my own / none]
- Time I can commit: [hours per week / per day]
- Kids/roommates/partner: [how decisions get made]
- Worst room first, or easiest first: [preference]

Build me:
1. A realistic declutter plan broken into 1-2 hour sessions
2. Order of areas to tackle (easiest to hardest, or most impactful first)
3. For each area, a specific checklist of categories
4. Decision rules for what to keep, donate, or trash
5. Strategies for the sentimental stuff (not 'just throw it away')
6. How to handle items that belong to someone else
7. How to maintain it after — prevent the 're-cluttering'
8. What to do with the donate/trash piles so they actually leave my house

Requirements:
- Acknowledge this is emotional work, not just physical work
- Break big rooms into small sessions (closet, not bedroom)
- Start with categories you have LOTS of (clothes, kitchen tools)
- End each session with one bag out the door — don't let stuff linger
- Don't ask me to make 1,000 decisions in one day — small sessions, multiple weeks""",
        "how_to_use": [
            "Don't try to do a whole room in one session — one drawer at a time beats a marathon",
            "Use the 'box it for 30 days' rule for maybes — if you don't reach for it, donate it",
            "Start with clothes — most people have too many, and decisions are easier than with sentimental items",
            "Take the donate bag to the car the same day — don't let it sit in the garage for 6 months",
        ],
        "example_output": """<p><strong>Week 1 — Easy wins (build momentum):</strong></p>
<ul><li><strong>Session 1 (60 min):</strong> One bathroom cabinet. Throw expired products, donate duplicates.</li>
<li><strong>Session 2 (60 min):</strong> Kitchen drawer #1 (utensils). Keep only what you use.</li>
<li><strong>Session 3 (90 min):</strong> Tupperware cabinet — match lids and containers, toss mismatches.</li></ul>
<p><strong>Week 2 — Clothes (highest volume):</strong></p>
<ul><li><strong>Session 1:</strong> All T-shirts. Pile on bed. Keep only what fits, you love, and you've worn in 12 months.</li>
<li><strong>Session 2:</strong> Pants + jeans. Same rule.</li>
<li><strong>Session 3:</strong> Shoes. Same rule.</li></ul>
<p><strong>Decision rule:</strong> "If I found this at a store today at full price, would I buy it?" If no, donate.</p>
<p><strong>Exit rule:</strong> Donate bag in trunk by 9pm same night. Drop at donation center within 7 days or it counts as re-buying.</p>""",
        "tips": [
            "<strong>Sentimental last.</strong> Ask 'How do I tackle sentimental clutter without feeling guilty?'",
            "<strong>Partner objections.</strong> Ask 'How do I have a productive conversation with my partner about their clutter?'",
            "<strong>Maintain it.</strong> Ask 'What's the weekly 15-minute routine to prevent re-cluttering?'",
            "<strong>Digital declutter.</strong> Ask 'Design me a plan to declutter my digital life — email, files, photos.'",
        ],
        "amazon_keywords": "decluttering+book+organizing",
        "amazon_text": "Decluttering Books",
        "related": [("best-chatgpt-prompt-for-habit-building", "Building a Habit"), ("best-chatgpt-prompt-for-home-improvement", "Home Improvement")],
    },
    {
        "slug": "best-chatgpt-prompt-for-debt-payoff",
        "title": "Best ChatGPT Prompt for Debt Payoff Plan",
        "subtitle": "Get out of debt faster with a personalized payoff strategy — avalanche, snowball, or hybrid — that fits your cash flow.",
        "prompt": """You are a certified financial planner who specializes in helping people get out of debt. Build me a debt payoff plan.

My debts (list each):
- [Type (credit card / student loan / car / medical / personal): Balance $[AMT], Interest [APR]%, Minimum payment $[AMT]]

My income and expenses:
- Monthly take-home: $[AMOUNT]
- Essential monthly expenses (rent, food, utilities, transport): $[AMOUNT]
- Current minimum debt payments total: $[AMOUNT]
- Extra money I could put toward debt: $[AMOUNT]

Build me:
1. A total picture of my debt — balance, interest I'll pay if I only make minimums
2. Compare avalanche (highest interest first) vs snowball (smallest balance first) — tell me which saves more and which is more likely to work for my situation
3. Month-by-month payoff schedule with my chosen strategy
4. Exact month I'll be debt-free
5. Total interest I'll save vs. minimum payments
6. Where to find more money (debt consolidation, 0% balance transfer, side income)
7. How to avoid going back into debt after payoff
8. When to consider credit counseling or bankruptcy

Requirements:
- Be honest if my plan is unrealistic — if I can't cover minimums + essentials, say so
- Flag high-interest cards that make debt consolidation worth it
- Warn about common traps (paying off a card then closing it hurts credit)
- Include a small 'emergency fund' buffer before aggressive payoff — unexpected costs shouldn't put me back in debt""",
        "how_to_use": [
            "List every debt with accurate numbers — half-info gets a half-useful plan",
            "Build a $1,000 emergency fund before aggressive payoff — one emergency otherwise undoes months of progress",
            "Automate minimum payments on every debt, then attack one at a time with extra",
            "Track progress monthly — watching the balance drop is its own motivation",
        ],
        "example_output": """<p><strong>Debts:</strong></p>
<ul><li>Credit card A: $4,200 @ 24.9% APR, min $95/mo</li>
<li>Credit card B: $1,500 @ 19.9% APR, min $45/mo</li>
<li>Car loan: $12,000 @ 6.5% APR, min $310/mo</li></ul>
<p><strong>Strategy comparison:</strong></p>
<ul><li><strong>Avalanche (highest APR first):</strong> Extra payments to Card A. Total payoff: 28 months. Total interest: $2,780.</li>
<li><strong>Snowball (smallest balance first):</strong> Extra payments to Card B. Total payoff: 30 months. Total interest: $3,120. Costs $340 more — but you kill a debt in 8 months for motivation.</li></ul>
<p><strong>Recommendation:</strong> Avalanche saves more. But if you've failed payoff plans before, snowball's psychological wins matter more than math. Pick what you'll stick with.</p>
<p><strong>Balance transfer opportunity:</strong> If your credit score is 680+, a 0% APR 18-month transfer card could save you $600-900 in interest on Card A. Factor the 3% transfer fee.</p>""",
        "tips": [
            "<strong>Emergency fund first.</strong> Ask 'Why should I build $1,000 savings before aggressive payoff?'",
            "<strong>0% balance transfers.</strong> Ask 'Is a balance transfer worth it for my debt? What are the traps?'",
            "<strong>Negotiation.</strong> Ask 'How do I call my credit card company and negotiate a lower rate? Script it for me.'",
            "<strong>Post-payoff.</strong> Ask 'What should I do after this debt is gone to avoid going back?'",
        ],
        "amazon_keywords": "debt+payoff+financial+planning+book",
        "amazon_text": "Personal Finance Books",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-car-buying", "Car Buying")],
    },
    {
        "slug": "best-chatgpt-prompt-for-investing-beginners",
        "title": "Best ChatGPT Prompt for Investing (Beginners)",
        "subtitle": "Get the basics of investing without the jargon — index funds, retirement accounts, and how to start with a few hundred dollars.",
        "prompt": """You are a fee-only fiduciary financial planner who specializes in helping young professionals start investing. Teach me the basics and help me set up a plan.

About me:
- Age: [AGE]
- Income: $[MONTHLY TAKE-HOME]
- Employment: [W-2 / self-employed / contractor]
- Current retirement accounts: [401K YES/NO with match / IRA YES/NO / nothing]
- Savings available to invest: $[AMOUNT]
- Existing debt: [HIGH-INTEREST CARDS / STUDENT LOANS / NONE]
- Risk tolerance: [very uncomfortable with losses / somewhat comfortable / fine with 20%+ drops]
- Timeline: [retirement in X years / shorter goals]

Teach me:
1. What accounts I should open and in what order (401k match → Roth IRA → etc.)
2. What 'index fund' means in plain English and why it matters
3. Specific fund types to look for (total market, target-date, etc.) — not specific tickers
4. How much to contribute monthly based on my situation
5. Asset allocation appropriate for my age/risk
6. Common beginner mistakes to avoid (stock picking, day trading, lifestyle creep)
7. When to see a fiduciary advisor (not a commission-based 'advisor')
8. A 12-month action plan

Requirements:
- Never recommend specific individual stocks
- Never promise returns — markets are unpredictable in short term
- Emphasize tax-advantaged accounts before taxable accounts
- Warn about high-fee products (actively managed funds, annuities sold by brokers, whole life insurance)
- Be clear: this is education, not financial advice""",
        "how_to_use": [
            "Open a Roth IRA at a low-fee provider (Fidelity, Schwab, Vanguard) — takes 15 minutes",
            "Start with a target-date index fund — one fund, done, rebalances automatically",
            "Automate contributions monthly — set it and ignore it",
            "Never check your portfolio more than monthly — short-term checking = anxiety and bad decisions",
        ],
        "example_output": """<p><strong>Profile:</strong> 28yo, $4,500/mo take-home, no debt, $5,000 savings, employer 401k with 4% match, no IRA yet.</p>
<p><strong>Priority order:</strong></p>
<ol><li><strong>401k to the match:</strong> If employer matches 4%, contribute at least 4%. This is free money — ~$180/mo for you.</li>
<li><strong>Emergency fund:</strong> Keep 3-6 months expenses in a high-yield savings account. You have $5K — decide if that's enough.</li>
<li><strong>Roth IRA max:</strong> $7,000/year = $583/mo. Opens at Fidelity/Schwab/Vanguard in 15 minutes.</li>
<li><strong>Back to 401k:</strong> After maxing Roth, increase 401k contribution.</li></ol>
<p><strong>What to buy inside those accounts:</strong></p>
<ul><li>Target-date fund matched to your retirement year (around 2060) — simplest option</li>
<li>OR total stock market index fund + international index fund (80/20 split)</li></ul>
<p><strong>Annual cost you want:</strong> Expense ratios under 0.20%. Anything over 0.75% is usually a red flag.</p>""",
        "tips": [
            "<strong>Match first, always.</strong> Ask 'Why is employer match the best ROI in investing?'",
            "<strong>Avoid commissioned advisors.</strong> Ask 'How do I find a fee-only fiduciary vs. a broker?'",
            "<strong>Fees kill returns.</strong> Ask 'Show me the math on how 1% fees reduce my retirement.'",
            "<strong>Stay in the market.</strong> Ask 'Why is timing the market worse than time in the market?'",
        ],
        "amazon_keywords": "investing+beginners+book+index+funds",
        "amazon_text": "Investing Books",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-debt-payoff", "Debt Payoff Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-saving-money",
        "title": "Best ChatGPT Prompt for Saving Money",
        "subtitle": "Find hundreds of dollars of savings in your current budget — without giving up everything you enjoy.",
        "prompt": """You are a consumer financial analyst who helps households find real savings in their monthly spending. Help me save more.

My situation:
- Monthly take-home income: $[AMOUNT]
- Monthly expenses I know of (list by category):
  - Rent/mortgage: $[AMT]
  - Utilities: $[AMT]
  - Groceries: $[AMT]
  - Dining out: $[AMT]
  - Subscriptions: $[LIST THEM]
  - Transportation: $[AMT]
  - Insurance: $[AMT]
  - Other: $[LIST]
- Current monthly savings: $[AMT]
- Savings goal: $[AMT/MONTH]
- Savings purpose: [emergency / down payment / vacation / general]

Give me:
1. Likely areas where I'm overspending vs. typical households (be specific by category)
2. The 5 biggest wins (most savings for least pain)
3. Scripts or steps for each win (what to call, what to say)
4. Subscriptions I should probably cut
5. Insurance categories worth reshopping (auto, home, renters) — average savings
6. One bigger move I might be avoiding (moving, selling a car) with realistic pros/cons
7. 'Painless' cuts vs. 'lifestyle change' cuts — labeled honestly
8. How to automate saving so I don't have to rely on willpower

Requirements:
- Don't shame me for any category — focus on action
- Prioritize changes with real dollar impact over $5-a-month stuff
- Recognize that some expenses are needs I can't just cut
- Suggest income strategies only after spending audit""",
        "how_to_use": [
            "Pull 3 months of actual bank/credit card statements — estimates hide the real spending",
            "Start with the biggest 3 categories — that's where meaningful savings live",
            "Make one change per week — 4 in a month compound into real money",
            "Automate savings to hit your account BEFORE you see it — out of sight, out of spending",
        ],
        "example_output": """<p><strong>Profile:</strong> $4,800 take-home, $600/mo dining out, $180/mo subscriptions (itemized), paying $165/mo for car insurance, hasn't reshopped in 3 years.</p>
<p><strong>Top 5 wins:</strong></p>
<ol><li><strong>Reshop car insurance ($40-60/mo potential savings):</strong> Call current insurer first and ask for "retention department." Then get quotes from Geico, Progressive, and a regional option. Most people save $300-900/year.</li>
<li><strong>Audit subscriptions ($60-80/mo):</strong> List all. Cut: services you haven't used in 30 days. Downgrade: premium tiers you don't fully use (YouTube Premium → free with ads, maybe).</li>
<li><strong>Dining out ($200-300/mo):</strong> Reframe — not "stop eating out" but "eat out twice a week instead of 5x." Savings compound to $1,500/yr without feeling deprived.</li>
<li><strong>Meal plan 3 dinners (stops impulse takeout).</strong></li>
<li><strong>Negotiate phone/internet ($20-40/mo):</strong> Call, mention competitor prices, ask for "loyalty discount."</li></ol>
<p><strong>Automation plan:</strong> Set up automatic transfer of $400/mo to savings on payday. The money you don't see, you don't spend.</p>""",
        "tips": [
            "<strong>Call scripts.</strong> Ask 'Write the exact script to call my cable company and lower my bill.'",
            "<strong>Subscription audit.</strong> Ask 'Here are my subscriptions. Which should I cut and why?'",
            "<strong>Low-effort wins.</strong> Ask 'What's the highest $/effort thing I haven't done?'",
            "<strong>Behavioral tricks.</strong> Ask 'What's the single best trick to stop impulse spending?'",
        ],
        "amazon_keywords": "personal+finance+saving+money+book",
        "amazon_text": "Personal Finance Books",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-debt-payoff", "Debt Payoff Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-road-trip-planning",
        "title": "Best ChatGPT Prompt for Road Trip Planning",
        "subtitle": "Plan a road trip with the right route, stops, and daily timing — without the chaos of Google-ing 47 things.",
        "prompt": """You are a travel writer and road trip planner who has driven every major US route. Plan a road trip for me.

Trip details:
- Starting city: [WHERE YOU LEAVE FROM]
- Ending city: [WHERE YOU'RE GOING — or round trip]
- Must-see stops: [LIST ANY]
- Total days: [HOW LONG YOU HAVE]
- Travelers: [WHO — number, ages]
- Budget: $[TOTAL or per day]
- Pace: [slow — fewer miles, more exploration / fast — mostly driving to get there]
- Road trip style: [national parks / food + cities / historical / scenic drives / beach]
- Vehicle: [car / RV / motorcycle / rental]

Build me:
1. A day-by-day itinerary with driving distances and realistic times
2. Specific stops worth stopping for (not "take a break at a rest stop")
3. Where to sleep each night (specific towns/hotels/campgrounds)
4. The single most interesting stop I'd miss without a local tip
5. Food worth eating (specific places, not "a local diner")
6. Driving times honest — factor in stops, traffic, photos
7. Budget breakdown (gas, food, lodging, activities)
8. Packing checklist for the trip style
9. Backup plan for bad weather

Requirements:
- Don't overload days — a road trip with 10-hour drives every day is a job, not a vacation
- Include a mix of famous and hidden stops
- Suggest 2-3 hours of actual sightseeing at main stops, not "drive-by" photo ops
- Call out any route with notoriously bad traffic or tricky driving
- Flag best and worst months to do the trip""",
        "how_to_use": [
            "Be realistic about pace — most people plan way too much per day",
            "Book lodging ahead in peak season (especially national parks)",
            "Download offline maps before leaving — signal gets spotty",
            "Ask follow-ups: 'What should I do if my 3rd day gets rained out?' for backup plans",
        ],
        "example_output": """<p><strong>Trip:</strong> 7 days, SF → LA via Highway 1, couple in their 30s, slow pace, food + scenery focus.</p>
<p><strong>Day 3: Big Sur</strong></p>
<ul><li><strong>Morning:</strong> Stay put at your lodging in Carmel. Drive south on Highway 1 by 9am — early light is magic.</li>
<li><strong>10:00 AM — Bixby Bridge:</strong> Pull off at the north vista for the iconic photo. 20 min.</li>
<li><strong>10:45 AM — Point Sur Lighthouse:</strong> Guided tour only (check schedule in advance). Skip if no tour available.</li>
<li><strong>12:30 PM — Lunch at Nepenthe:</strong> Reservations strongly recommended. Sit on the terrace. Order the Ambrosia burger.</li>
<li><strong>2:30 PM — McWay Falls:</strong> 15-min walk from the parking lot. One of the only waterfalls in North America that falls directly onto a beach.</li>
<li><strong>Sleep:</strong> Drive back to Carmel (2 hrs). Two-night stay means you don't pack and unpack every day.</li></ul>
<p><strong>Hidden tip:</strong> Stop at Sand Dollar Beach for sunset. 10 miles south of McWay, way less crowded.</p>""",
        "tips": [
            "<strong>Drive time math.</strong> Ask 'Adjust my itinerary so no driving day is more than 5 hours with stops.'",
            "<strong>Weather backup.</strong> Ask 'If day 4 gets fog or rain, what should I do instead?'",
            "<strong>Food specifics.</strong> Ask 'For each overnight town, give me one dinner spot worth eating at.'",
            "<strong>Packing list.</strong> Ask 'Generate a specific packing checklist for this trip including car essentials.'",
        ],
        "amazon_keywords": "road+trip+guide+book+USA",
        "amazon_text": "Road Trip Books",
        "related": [("best-chatgpt-prompt-for-travel-planning", "Travel Planning"), ("best-chatgpt-prompt-for-gift-ideas", "Gift Ideas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-toddler-activities",
        "title": "Best ChatGPT Prompt for Toddler Activities",
        "subtitle": "Get age-appropriate activities that keep your toddler engaged — educational, fun, and using stuff you already have.",
        "prompt": """You are an early childhood educator with 20 years of experience designing activities for toddlers (ages 1-3). Suggest activities for me.

My child's age: [MONTHS or YEARS]
Development focus: [gross motor / fine motor / language / social / sensory / imaginative play / all of the above]
How long the activity should take: [10 min / 30 min / 1 hr]
Materials available: [common household items only / willing to buy a few things / art supplies on hand]
Context: [just me and child / with other kids / indoor / outdoor / rainy day]
Energy level of child right now: [high / medium / low / already overstimulated]
Things my child loves: [e.g. trucks, animals, music, water]
Things to avoid: [mess / noise / choking hazards / screens]

Give me:
1. 5 activities matched to my setup, age, and energy level
2. For each: materials needed, time, skills it builds, setup and cleanup time
3. Variations if my child loses interest in 5 minutes (many do)
4. Safety considerations for any activity with small parts or water
5. Quick brain-engaging activities for 5-min stretches
6. 'Low-energy me' activities (for when I'm tired) that don't require active supervision

Requirements:
- Never use materials with choking hazards for under 3
- Keep it realistic — no 12-step Pinterest crafts
- Acknowledge that toddlers have 2-10 minute attention spans
- Include at least one screen-free activity I can lean on regularly
- No sugar-bribing or 'behavior charts' for toddlers — they don't work""",
        "how_to_use": [
            "Keep materials in a dedicated 'activity bin' so setup takes 30 seconds, not 15 minutes",
            "Rotate activities weekly — novelty is half the fun",
            "Don't force it — if they lose interest in 5 min, that's normal; come back another day",
            "Ask for specific ages: a 14-month-old plays very differently than a 30-month-old",
        ],
        "example_output": """<p><strong>Profile:</strong> 22-month-old, high energy, indoors, kitchen table, loves animals.</p>
<p><strong>Activity 1: Animal bath (20 min)</strong></p>
<ul><li><strong>Materials:</strong> Plastic toy animals + shallow bin + water + sponge + towel</li>
<li><strong>Setup:</strong> Bin on floor with towel under, 1 inch of water, 5-6 animals</li>
<li><strong>The activity:</strong> "Oh no, the elephants are dirty! Can you wash them?" Hand them the sponge.</li>
<li><strong>Builds:</strong> Fine motor, language (naming animals), cause-and-effect</li>
<li><strong>Bail-out variation:</strong> If they dump the water within 2 min (they will eventually): embrace it. Sensory play.</li></ul>
<p><strong>Activity 2 (low-energy-parent friendly):</strong> Sticker book. Print stickers pre-peeled onto a sheet. Give them a blank notebook. Sit on couch drinking coffee.</p>""",
        "tips": [
            "<strong>Age-specific ideas.</strong> Ask 'What's developmentally optimal for a child at exactly [X] months?'",
            "<strong>Rainy day bank.</strong> Ask 'Give me 20 indoor activities I can rotate through on rainy days.'",
            "<strong>Activity bin.</strong> Ask 'What should I stock in an activity bin for quick pulls?'",
            "<strong>Screen alternatives.</strong> Ask 'What's a parent-low-energy activity that isn't screens?'",
        ],
        "amazon_keywords": "toddler+activities+learning+book",
        "amazon_text": "Toddler Books on Amazon",
        "related": [("best-chatgpt-prompt-for-meal-planning", "Meal Planning"), ("best-chatgpt-prompt-for-gift-ideas", "Gift Ideas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-homeschooling",
        "title": "Best ChatGPT Prompt for Homeschooling",
        "subtitle": "Plan a homeschool curriculum or tackle a tough subject — realistic lesson plans for real homeschool life.",
        "prompt": """You are a veteran homeschool educator who has taught K-12 across multiple approaches (classical, Charlotte Mason, eclectic, unschooling). Help me homeschool.

What I need help with: [pick one]
- Plan a full curriculum for [GRADE]
- Teach a specific subject my kid is stuck on: [SUBJECT + ISSUE]
- Design a weekly schedule for multiple grade levels
- Choose curriculum: evaluate options for [SUBJECT]
- Create unit study on [TOPIC]
- Help with a struggling subject

My situation:
- Kids' ages and grades: [LIST EACH]
- My background: [first-year homeschooler / experienced / came from public school]
- Approach preference: [structured / flexible / interest-led / Charlotte Mason / classical / unschooling]
- Time available for instruction: [hours per day]
- Tough subjects for me: [what I feel least equipped to teach]
- Goal: [college prep / life skills / love of learning / meet state requirements]

Requirements:
- Match the approach I said I prefer — don't push one philosophy
- Recommend REAL curriculum or resources (verify names, but OK to suggest common ones)
- Keep daily work realistic — not 6-hour school days
- Build in margin for life (sick days, field trips, curiosity tangents)
- For multiple grades, show how to layer or combine subjects
- Note state requirements I need to be aware of""",
        "how_to_use": [
            "Homeschool is more efficient than public school — 3-4 focused hours beats 7 hours of school busywork",
            "Loop schedules beat rigid daily schedules — you'll miss days, plan for it",
            "Mix structured work with interest-led projects — best of both worlds",
            "Join a local co-op or homeschool group — community is a huge part of success",
        ],
        "example_output": """<p><strong>Setup:</strong> 1st year homeschooling. 2nd grader + kindergartener. Eclectic approach. 3 hrs/day.</p>
<p><strong>Daily flow:</strong></p>
<ul><li><strong>9:00-9:30:</strong> Morning basket (together): read-aloud picture book, poem, song, prayer or gratitude, calendar</li>
<li><strong>9:30-10:15:</strong> Math — kindergartener with manipulatives (15 min one-on-one), 2nd grader independent (30 min)</li>
<li><strong>10:15-10:30:</strong> Break / snack</li>
<li><strong>10:30-11:15:</strong> Language arts — flip roles from math time</li>
<li><strong>11:15-12:00:</strong> Together subject (rotates by day: history Mon/Wed, science Tue/Thu, art Fri)</li></ul>
<p><strong>Curriculum suggestions:</strong></p>
<ul><li><strong>Math:</strong> Math-U-See (manipulative-based, gentle progression) or Singapore Math (challenging, well-respected)</li>
<li><strong>Reading/LA:</strong> All About Reading for K, Brave Writer or IEW for 2nd</li>
<li><strong>History:</strong> Story of the World (both kids can listen together — this is the magic of homeschooling multiple ages)</li></ul>""",
        "tips": [
            "<strong>Loop scheduling.</strong> Ask 'How do I structure a loop schedule so skipping a day doesn't throw everything off?'",
            "<strong>Multi-age magic.</strong> Ask 'Which subjects can I teach to both my kids at the same time?'",
            "<strong>Burnout prevention.</strong> Ask 'What are signs of homeschool burnout and how do I prevent it?'",
            "<strong>State requirements.</strong> Ask 'What's a state-by-state overview of homeschool requirements?' (verify specifics)",
        ],
        "amazon_keywords": "homeschool+curriculum+book",
        "amazon_text": "Homeschool Books",
        "related": [("best-chatgpt-prompt-for-lesson-plans", "Lesson Plans"), ("best-chatgpt-prompt-for-studying", "Studying")],
    },
    {
        "slug": "best-chatgpt-prompt-for-photography-tips",
        "title": "Best ChatGPT Prompt for Photography Tips",
        "subtitle": "Level up your photos with specific, practical advice — not generic 'rule of thirds' listicles — for your camera and subject.",
        "prompt": """You are a professional photographer with 20 years of experience shooting weddings, portraits, and commercial work. Help me improve my photography.

What I need help with: [pick one]
- Learn a specific skill: [e.g. low-light, portraits, product photography, sports]
- Fix a specific problem in my photos: [DESCRIBE THE PROBLEM]
- Understand my camera settings better: [CAMERA MODEL]
- Plan a shoot: [TYPE OF SUBJECT + CONTEXT]
- Post-processing advice for a specific look

My setup:
- Camera: [BRAND + MODEL, or phone]
- Lenses (if DSLR/mirrorless): [LIST]
- Experience level: [beginner / hobbyist / semi-pro]
- Editing software: [Lightroom / Photoshop / phone apps / none]
- Typical subjects: [WHAT YOU SHOOT MOST]

Give me:
1. Specific technical settings for my situation (not 'depends')
2. Composition principles that apply to my subject — beyond rule of thirds
3. Lighting approach — natural vs. artificial, when to use each
4. 3 exercises to practice this skill this week
5. One advanced technique to try when I have the basics down
6. Common beginner mistakes I should watch for
7. Editing workflow — how to enhance the photo without overdoing it
8. One inspirational photographer I should study for this style

Requirements:
- Be specific with numbers — "f/2.8, 1/200, ISO 800" beats "use a wide aperture"
- Explain the WHY, not just the setting
- Match advice to my camera's real capabilities (phone and DSLR are very different)
- Don't recommend gear unless I ask — working with what you have matters most""",
        "how_to_use": [
            "Take your camera off auto for 30 days — learn manual one setting at a time",
            "Shoot the same subject in 10 different lights — lighting is 90% of photography",
            "Study photos you love and reverse-engineer them — composition, light, editing",
            "Post-processing isn't cheating — it's part of photography since the darkroom era",
        ],
        "example_output": """<p><strong>Goal:</strong> Portrait photography with a Sony a6400 + 50mm f/1.8 lens, beginner.</p>
<p><strong>Settings for outdoor portraits (golden hour):</strong></p>
<ul><li>Aperture: f/2.0-f/2.8 (shallow depth of field, background blur)</li>
<li>Shutter: 1/250 or faster (frozen subject)</li>
<li>ISO: Auto, capped at 800 (keeps image clean)</li>
<li>Focus: Single-point AF, eye on nearer eye</li></ul>
<p><strong>Composition beyond rule of thirds:</strong></p>
<ul><li><strong>Leading lines:</strong> Use fences, paths, walls to pull the eye to your subject.</li>
<li><strong>Negative space:</strong> Let the subject breathe. Empty sky or wall makes the person more powerful, not less.</li>
<li><strong>Frame within frame:</strong> Doorways, archways, tree branches create depth.</li></ul>
<p><strong>Exercise:</strong> Shoot 50 portraits this week. Only change ONE thing each time (angle, distance, lighting direction). Compare side-by-side.</p>""",
        "tips": [
            "<strong>Light direction.</strong> Ask 'How do side, front, and back light change a portrait? When do I use each?'",
            "<strong>Golden hour.</strong> Ask 'What's happening in golden hour light and why do photos look better?'",
            "<strong>Expose for highlights.</strong> Ask 'Why should I expose for the brightest part of a photo?'",
            "<strong>Editing style.</strong> Ask 'Walk me through a basic Lightroom edit for a portrait in 10 minutes.'",
        ],
        "amazon_keywords": "photography+book+lighting+composition",
        "amazon_text": "Photography Books",
        "related": [("best-chatgpt-prompt-for-midjourney", "Midjourney Prompts"), ("best-chatgpt-prompt-for-content-ideas", "Content Ideas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-logo-design",
        "title": "Best ChatGPT Prompt for Logo Design Brief",
        "subtitle": "Write a logo design brief that gets you actually useful results — from a designer, AI tool, or doing it yourself.",
        "prompt": """You are a senior brand designer who has created logos for Fortune 500 brands and early-stage startups. Write a logo brief for me.

Company:
- Name: [COMPANY NAME]
- What it does: [ONE SENTENCE]
- Industry: [INDUSTRY]
- Target customer: [WHO BUYS FROM YOU]
- Stage: [pre-launch / early-stage / rebrand]
- Budget: $[AMOUNT — will change advice]

Brand:
- Personality in 3 words: [CHOOSE 3]
- Brands whose look I admire: [LIST 2-3]
- Brands whose look I want to avoid: [LIST 1-2]
- Color direction (if any): [e.g. modern tech = blue/black, earthy = greens, none]
- Logo style preferences: [wordmark / icon + wordmark / abstract / literal / monogram / mascot]

Write me a detailed logo brief including:
1. Project overview
2. Brand values and personality
3. Audience description
4. Visual direction (inspiration, tone)
5. 'Must be' and 'must not be' lists for the final logo
6. Usage requirements (web, print, social, business cards, signage)
7. Files I'll need to ask for (SVG, PNG transparent, high-res)
8. 3 adjectives the final logo should evoke
9. 3 concept directions to explore (so the designer has options, not blank page)
10. Red flags to watch for in bad proposals

Requirements:
- Specific enough that the designer doesn't have to guess
- Not so restrictive that it kills creativity
- Include a realistic revision process (usually 2-3 rounds for $500-5K budgets)
- If I'm doing it myself with a tool (Canva, AI), adapt the brief format""",
        "how_to_use": [
            "Fill this in before talking to any designer — clear briefs = better results",
            "Don't show competitor logos and say 'like that' — show mood boards of what you like",
            "Budget reality: great logos cost $1,500-15,000 from an experienced designer. Cheap logos usually look cheap.",
            "Test the final logo at 16px favicon size before approving — most don't work tiny",
        ],
        "example_output": """<p><strong>Sample brief: Acme Yoga Studio</strong></p>
<p><strong>Overview:</strong> Acme Yoga is a new yoga studio in Denver targeting women 30-55 who want strength, not flexibility, as the outcome of yoga. We're launching in September and need a logo for storefront signage, Instagram, website, and business cards.</p>
<p><strong>Brand personality:</strong> Grounded. Strong. Warm.</p>
<p><strong>Not:</strong> Delicate, flowing, ethereal, spa-like.</p>
<p><strong>Visual direction:</strong></p>
<ul><li>Think: hand-drawn but refined. Like typography from the 1960s — confident but human.</li>
<li>Admire: Lululemon (clean, confident), Away luggage (warm minimalism)</li>
<li>Avoid: Generic yoga (lotus flowers, silhouettes of women stretching, cursive scripts)</li></ul>
<p><strong>Directions to explore:</strong></p>
<ol><li>Custom wordmark only, strong letterforms</li>
<li>Minimal icon + wordmark (icon could be abstract like a cairn/stacked stones representing balance + strength)</li>
<li>Monogram "AY" with warm typography</li></ol>""",
        "tips": [
            "<strong>Favicon test.</strong> Ask 'Will this logo still be readable at 16px?' Many logos fail here.",
            "<strong>Black and white test.</strong> Ask 'Does this logo work in pure B&W without color crutches?'",
            "<strong>Versatility.</strong> Ask 'What versions of this logo will I need?' (horizontal, stacked, icon-only, monochrome)",
            "<strong>Trademark search.</strong> Ask 'Before finalizing, what trademark classes should I check for similar marks?'",
        ],
        "amazon_keywords": "logo+design+branding+book",
        "amazon_text": "Branding Books on Amazon",
        "related": [("best-chatgpt-prompt-for-naming-a-business", "Naming a Business"), ("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-tax-prep",
        "title": "Best ChatGPT Prompt for Tax Prep",
        "subtitle": "Organize for tax season, understand deductions, and decide between DIY software or hiring a CPA — without fear.",
        "prompt": """You are a CPA who has prepared 5,000+ returns and understands how to explain taxes in plain English. Help me prepare for tax season.

My tax situation:
- Filing status: [single / married filing jointly / married filing separately / head of household]
- Employment: [W-2 only / W-2 + side income / full self-employed / multiple 1099s / retired / student]
- Income range: $[ROUGH AMOUNT] — for bracket context
- State: [STATE]
- Homeowner: [YES — when purchased / NO, rent]
- Dependents: [number and ages]
- Investment accounts: [401k, IRA, brokerage, HSA — list each]
- Side income or business: [YES — describe / NO]
- Major life events this year: [moved, married, had child, sold home, inherited, etc.]

Help me:
1. List of every document I need to gather
2. Deductions I probably qualify for based on my situation (not general IRS list — my specific situation)
3. Credits to check (Child Tax Credit, EV credit, education credits, etc.)
4. DIY software recommendation vs. hiring a CPA for my complexity
5. Red flags that mean I should definitely use a pro
6. Estimated tax liability or refund range
7. What to do NOW (before year end) to save next year
8. Common mistakes for my situation

Requirements:
- Be clear this is education, not tax advice
- For anything unusual (business sales, foreign income, back taxes), recommend a CPA
- Don't fabricate tax law or deduction details
- Mention free options (FreeTaxUSA, Cash App Taxes, IRS Free File) where applicable
- Remind me of deadlines and extension options""",
        "how_to_use": [
            "Gather documents BEFORE you sit down to do taxes — half-done returns get ignored",
            "Keep a tax folder year-round — receipts, statements, mileage logs",
            "Don't trust any 'deduction' you can't back up with a receipt or statement",
            "For complex situations (self-employed, rental property, investments), hiring a CPA usually saves more than it costs",
        ],
        "example_output": """<p><strong>Profile:</strong> Single, $75K W-2, Colorado, rents, no dependents, 401k + Roth IRA.</p>
<p><strong>Documents to gather:</strong></p>
<ul><li>W-2 from employer (arrives by Jan 31)</li>
<li>1099-INT if you have a savings account earning interest</li>
<li>1099-DIV if you have a brokerage outside retirement accounts</li>
<li>1098-E if you paid student loan interest</li>
<li>Records of charitable donations (if you itemize — unlikely at your income unless you donate a lot)</li></ul>
<p><strong>Likely deductions/credits for you:</strong></p>
<ul><li>Standard deduction: $14,600 (2024). Itemizing rarely wins for renters without big medical/charity costs.</li>
<li>Student loan interest deduction up to $2,500 if you paid any</li>
<li>Saver's Credit if income is below ~$36,500 (probably not you at $75K)</li></ul>
<p><strong>DIY vs. CPA:</strong> Your situation is simple enough for software. Cash App Taxes or FreeTaxUSA (both free-ish) handle this well. Save $200-400 vs. H&R Block office.</p>
<p><strong>Now (before year-end) to save next year:</strong> Max your Roth IRA if income allows. Contribute more to 401k if not at max. HSA if you have access.</p>""",
        "tips": [
            "<strong>Organizer.</strong> Ask 'Build me a checklist of every doc I need, in the order I'll enter them.'",
            "<strong>Side hustle taxes.</strong> Ask 'If I made $3K on a side hustle, what do I need to report and what can I deduct?'",
            "<strong>Estimated taxes.</strong> Ask 'Do I need to pay quarterly estimated taxes for my side income?'",
            "<strong>CPA check.</strong> Ask 'Is my situation complex enough to hire a CPA vs. software?'",
        ],
        "amazon_keywords": "tax+preparation+book+guide",
        "amazon_text": "Tax Books on Amazon",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-investing-beginners", "Investing for Beginners")],
    },
]

count = 0
for page in PAGES:
    make_page(**page)
    count += 1
    print(f"Created: {page['slug']}.html")

print(f"\nTotal pages created: {count}")
