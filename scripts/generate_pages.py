"""Generate 15+ new prompt pages covering high-traffic topics."""
import sys
sys.path.insert(0, 'scripts')
from page_template import make_page

PAGES = [
    {
        "slug": "best-chatgpt-prompt-for-naming-a-business",
        "title": "Best ChatGPT Prompt for Naming a Business",
        "subtitle": "Generate brandable, memorable business names with available domains — in seconds.",
        "prompt": """You are a branding expert who has named 100+ successful companies. Help me name my business.

Industry: [WHAT INDUSTRY]
What my business does: [DESCRIBE IT IN 1-2 SENTENCES]
Target customer: [WHO BUYS FROM ME]
Brand personality: [professional / playful / luxurious / edgy / minimalist / wholesome]
Tone preference: [serious / fun / modern / classic / quirky]
Avoid: [words, themes, or existing brand names I want to avoid]
Length preference: [short 1-word / 2-word combo / longer phrase]

Requirements:
- Generate 25 name options across 5 different naming styles:
  - Descriptive (what you do)
  - Evocative (a feeling or image)
  - Invented (made-up word)
  - Founder/personal
  - Abstract compound (two words combined)
- For each name, suggest whether the .com might be available
- Explain the meaning or vibe of each name in one line
- Flag any that could be confused with existing major brands
- My top 5 favorites — rank them by memorability""",
        "how_to_use": [
            "Fill in your industry and brand personality",
            "Be specific about what you want to avoid — generic names waste your time",
            "Get 25 options, then follow up with: 'Expand on #7 — give me 10 variations of that name'",
            "Always check domain availability before falling in love with a name",
        ],
        "example_output": """<p><strong>Industry:</strong> Sustainable coffee brand</p>
<p><strong>Generated names:</strong></p>
<ul><li><strong>Kindground</strong> — kind + ground (coffee). Warm, ethical, memorable.</li>
<li><strong>Roastwell</strong> — quality + wellness. Descriptive but distinct.</li>
<li><strong>Mornsip</strong> — morning + sip. Invented, short, memorable.</li>
<li><strong>Bean Republic</strong> — coffee + community vibe. Descriptive + evocative.</li>
<li><strong>Third Wave Co.</strong> — references the specialty coffee movement.</li></ul>""",
        "tips": [
            "<strong>Say it out loud.</strong> Names that are hard to pronounce die fast.",
            "<strong>Check trademark.</strong> Ask the AI: 'Which of these are least likely to have trademark issues?'",
            "<strong>Get domain variations.</strong> Say 'Give me .com alternatives for these names' if the .com is taken.",
            "<strong>Test with friends.</strong> Show your top 5 to 10 people and see which they remember the next day.",
        ],
        "amazon_keywords": "branding+business+naming+guide",
        "amazon_text": "Branding Books on Amazon",
        "related": [("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan"), ("best-chatgpt-prompt-for-product-descriptions", "Product Descriptions")],
    },
    {
        "slug": "best-chatgpt-prompt-for-email-marketing",
        "title": "Best ChatGPT Prompt for Email Marketing",
        "subtitle": "Write high-converting email marketing campaigns — newsletters, promos, launches, and nurture sequences.",
        "prompt": """You are a direct-response email marketing expert who has generated $50M+ in email revenue. Write an email marketing campaign for me.

Campaign type: [newsletter / product launch / promo / abandoned cart / welcome sequence / re-engagement]
Business: [WHAT YOU SELL]
Audience: [WHO YOU'RE EMAILING — customers, prospects, subscribers]
Goal: [open rate / click rate / sales / nurture / feedback]
Brand voice: [professional / casual / witty / luxurious / urgent]
Offer (if any): [discount, free resource, new product, etc.]
Send volume: [single email / sequence of X emails]

Requirements:
- Write 5 subject line variations — each with a different psychological angle (curiosity, urgency, benefit, social proof, personal)
- Include preview text for each subject line
- Write the full email body (150-300 words depending on campaign)
- Include a clear, single CTA
- Write for mobile — short paragraphs, scannable
- Open with a hook that isn't "I hope this email finds you well"
- If it's a sequence, show timing and sequence logic (email 1 day 0, email 2 day 2, etc.)
- A/B test suggestions at the end""",
        "how_to_use": [
            "Specify the exact campaign type — a newsletter is very different from a launch email",
            "Include real details about your audience — 'busy moms' gets different copy than 'tech executives'",
            "Get 5 subject line options and test 2 of them against each other in your email tool",
            "Ask follow-ups like 'Rewrite this for people who haven't opened any email in 30 days'",
        ],
        "example_output": """<p><strong>Subject Line Options:</strong></p>
<ol><li><strong>Curiosity:</strong> "The one thing we changed that tripled our revenue"</li>
<li><strong>Urgency:</strong> "Last 48 hours — 40% off your first order"</li>
<li><strong>Benefit:</strong> "Save 3 hours a week with this simple workflow"</li>
<li><strong>Social proof:</strong> "How 5,000+ founders use this in their business"</li>
<li><strong>Personal:</strong> "Quick question (I'm genuinely curious)"</li></ol>
<p><strong>Email body (variation #3):</strong> Last month, I talked to 20 of our customers about what they actually do on Mondays. One answer came up 14 times: 'I waste the morning in meetings deciding what to work on.'...</p>""",
        "tips": [
            "<strong>Test subject lines always.</strong> A 5% improvement in open rate compounds across every send.",
            "<strong>Segment aggressively.</strong> Tell the AI: 'Rewrite this for [segment]' for each major audience group.",
            "<strong>Track the metric.</strong> Open rate for subject lines. Click rate for email body. Know which you're optimizing.",
            "<strong>Plain text wins.</strong> Ask for a 'plain text version, no HTML' for higher deliverability on some lists.",
        ],
        "amazon_keywords": "email+marketing+book+copywriting",
        "amazon_text": "Email Marketing Books",
        "related": [("best-chatgpt-prompt-for-writing-emails", "Writing Emails"), ("best-chatgpt-prompt-for-social-media-captions", "Social Media Captions")],
    },
    {
        "slug": "best-chatgpt-prompt-for-seo",
        "title": "Best ChatGPT Prompt for SEO",
        "subtitle": "Use AI to research keywords, optimize content, build topic clusters, and outrank competitors.",
        "prompt": """You are an SEO strategist who has grown sites to 1M+ monthly visitors. Help me with my SEO.

What I need help with: [pick one]
- Keyword research for [TOPIC OR NICHE]
- Content gap analysis vs these competitors: [LIST COMPETITOR URLS]
- Optimize this existing page: [PASTE URL OR TITLE]
- Build a topic cluster around [MAIN TOPIC]
- Title tag and meta description for [PAGE TOPIC]
- Internal linking strategy for my site

My site: [WEBSITE URL]
My niche: [NICHE]
Target audience: [WHO I'M WRITING FOR]
Current traffic: [ROUGH MONTHLY VISITORS if known]

Requirements:
- Prioritize long-tail keywords (3+ words) with clear buyer intent
- Include estimated difficulty (easy / medium / hard) for each keyword
- Group keywords by search intent (informational, navigational, transactional)
- Suggest content formats (guide, listicle, comparison, review) for each
- For optimization, give me specific on-page changes with character counts
- Focus on actionable recommendations, not generic SEO advice""",
        "how_to_use": [
            "Pick one focus area per session — don't try to do all of SEO at once",
            "Provide real competitor URLs for content gap analysis",
            "Always validate keyword suggestions in a real tool like Ahrefs, Semrush, or Ubersuggest",
            "Ask 'What's the search intent behind [keyword]?' if you're unsure what kind of content to create",
        ],
        "example_output": """<p><strong>Topic cluster for 'home coffee brewing':</strong></p>
<p><strong>Pillar page:</strong> Complete Guide to Home Coffee Brewing</p>
<p><strong>Supporting pages (informational):</strong></p>
<ul><li>Pour over vs French press: which is right for you (medium difficulty, transactional intent)</li>
<li>Best grind size for every brew method (easy, informational)</li>
<li>How to fix bitter coffee: 7 common mistakes (easy, informational)</li></ul>
<p><strong>Transactional pages:</strong></p>
<ul><li>Best beginner espresso machines under $500 (easy, transactional — high affiliate potential)</li>
<li>Chemex vs Hario V60: which to buy (medium, transactional)</li></ul>""",
        "tips": [
            "<strong>Target the 'near zero' keywords.</strong> Very long queries with low volume often have near-zero competition and instant ranking.",
            "<strong>Write for the search intent, not the keyword.</strong> Ask 'What does someone searching this actually want to find?'",
            "<strong>Update old content.</strong> Ask 'Here's a post from 2023 — how should I update it for 2026?'",
            "<strong>Get the title tag right.</strong> Ask specifically for 'title tag under 60 characters with target keyword at the start.'",
        ],
        "amazon_keywords": "SEO+guide+book+keyword+research",
        "amazon_text": "SEO Books on Amazon",
        "related": [("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post"), ("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-copywriting",
        "title": "Best ChatGPT Prompt for Copywriting",
        "subtitle": "Write sales copy that converts — landing pages, ads, headlines, and product copy that actually sells.",
        "prompt": """You are a senior direct-response copywriter who has written for brands generating $100M+ in sales. Write copy for me.

Copy type: [landing page / Facebook ad / Google ad / sales page / headline / product copy / VSL script]
Product/service: [WHAT YOU'RE SELLING]
Price: $[AMOUNT]
Target audience: [BE SPECIFIC — demographics, pain points, desires]
Main benefit: [WHAT PROBLEM YOU SOLVE]
Proof/credentials: [what makes your offer believable — testimonials, results, credentials]
Offer: [guarantee, bonus, price, deadline]
Competitor being beaten: [who they'd otherwise buy from]

Requirements:
- Use proven direct-response copy frameworks (AIDA, PAS, or Before-After-Bridge)
- Write 3 headline options — each with a different angle (benefit, curiosity, urgency)
- Hook the reader in the first sentence, don't warm up
- Specificity beats generality — "saves 3.2 hours a week" beats "saves time"
- Address 2-3 of the biggest objections preemptively
- End with a clear CTA that reduces friction
- No corporate fluff, no hype language, no exclamation points
- Write at a 7th grade reading level — short sentences, simple words""",
        "how_to_use": [
            "Be specific about your audience — 'busy parents' is too broad, 'working moms of kids 2-5' gets better copy",
            "Always include the price — copy for a $9 product is different from a $999 product",
            "Test 2-3 versions against each other — never trust version 1 to be the best",
            "After getting copy, ask: 'What objections did you miss?' to strengthen it further",
        ],
        "example_output": """<p><strong>Headline (benefit-driven):</strong> The 12-minute morning routine that turned my 3am anxiety into focus.</p>
<p><strong>Opening:</strong></p>
<p>Last March, I started waking up at 3am with my heart racing. Not every night — just often enough to make coffee taste like dread.</p>
<p>My doctor suggested meditation. My therapist suggested journaling. Both worked. Neither was a routine I'd actually keep.</p>
<p>Then I tried something stupid: 12 minutes. That's it. Same 12 minutes every morning, no skipping. Three weeks in, the 3am thing stopped. Not gone — just stopped running the show.</p>
<p><strong>CTA:</strong> Get the 12-Minute Morning — $9 one-time. No subscription. If it doesn't work in 30 days, refund, no questions.</p>""",
        "tips": [
            "<strong>Study the best, don't ask AI blindly.</strong> Paste a copy ad you love and say 'Write copy like this for my product.'",
            "<strong>Test headlines first.</strong> 80% of copy success is the headline. Get 10 options before touching the body.",
            "<strong>Add proof.</strong> Ask 'Where should I add testimonials or proof points?' for max impact placement.",
            "<strong>Remove, don't add.</strong> After your first draft, ask 'What can I cut without losing persuasion?'",
        ],
        "amazon_keywords": "copywriting+books+sales+copy+bestseller",
        "amazon_text": "Copywriting Books on Amazon",
        "related": [("best-chatgpt-prompt-for-product-descriptions", "Product Descriptions"), ("best-chatgpt-prompt-for-email-marketing", "Email Marketing")],
    },
    {
        "slug": "best-chatgpt-prompt-for-python-code",
        "title": "Best ChatGPT Prompt for Python Code",
        "subtitle": "Write, debug, and understand Python scripts — for automation, data analysis, web scraping, and more.",
        "prompt": """You are a senior Python developer with 15 years of experience. Help me with a Python task.

What I'm trying to do: [DESCRIBE THE GOAL IN PLAIN ENGLISH]
Python version: [3.10 / 3.11 / 3.12 / don't know]
Libraries allowed: [list any restrictions, or 'anything on PyPI']
My current code (if any):
```python
[PASTE YOUR CODE]
```
The problem: [what's not working, or what needs to be built]
Expected input format: [what the script receives]
Expected output format: [what the script should produce]
My skill level: [beginner / intermediate / advanced]

Requirements:
- Write clean, Pythonic code (follow PEP 8)
- Use type hints for function signatures
- Add docstrings for functions
- Include error handling for edge cases (empty input, missing files, network errors)
- Show an example of running the code with sample input
- If there's a simpler/more efficient approach, mention it
- Use the standard library when possible — only pull in pip packages when necessary""",
        "how_to_use": [
            "Describe what the script should do end-to-end, not just the next step",
            "Paste error messages fully — the AI can usually diagnose from the traceback",
            "For data scripts, paste 2-3 sample rows of your real data",
            "For automation scripts, describe what you currently do manually step by step",
        ],
        "example_output": """<p><strong>Task:</strong> Read a CSV of transactions and produce a monthly summary</p>
<pre style="color:#ccc;font-size:13px;">import csv
from collections import defaultdict
from datetime import datetime

def summarize_by_month(csv_path: str) -> dict[str, float]:
    \"\"\"Sum transaction amounts by YYYY-MM month.\"\"\"
    totals: dict[str, float] = defaultdict(float)
    with open(csv_path, newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            date = datetime.strptime(row['date'], '%Y-%m-%d')
            key = date.strftime('%Y-%m')
            totals[key] += float(row['amount'])
    return dict(sorted(totals.items()))

if __name__ == '__main__':
    summary = summarize_by_month('transactions.csv')
    for month, total in summary.items():
        print(f"{month}: ${total:,.2f}")</pre>""",
        "tips": [
            "<strong>Ask for tests.</strong> Say 'Write pytest tests for this function' to catch bugs early.",
            "<strong>Explain before rewriting.</strong> For code you don't understand, say 'Explain this script line by line.'",
            "<strong>Compare approaches.</strong> Ask 'Is there a pandas way and a vanilla Python way? Show me both with tradeoffs.'",
            "<strong>Small scripts.</strong> For one-off tasks, say 'Write the shortest Python that does this, no error handling' — save yourself time.",
        ],
        "amazon_keywords": "Python+programming+book+beginners",
        "amazon_text": "Python Books on Amazon",
        "related": [("best-chatgpt-prompt-for-coding", "Coding"), ("best-chatgpt-prompt-for-excel-formulas", "Excel Formulas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-sql-queries",
        "title": "Best ChatGPT Prompt for SQL Queries",
        "subtitle": "Write, debug, and optimize SQL queries — for any database (PostgreSQL, MySQL, SQL Server, SQLite, BigQuery).",
        "prompt": """You are a SQL expert and database administrator. Help me write or fix a SQL query.

Database: [PostgreSQL / MySQL / SQL Server / SQLite / BigQuery / Snowflake]
What I'm trying to do: [DESCRIBE THE RESULT YOU WANT IN PLAIN ENGLISH]
My tables:
```
[TABLE 1]: columns (column1 type, column2 type, ...)
[TABLE 2]: columns (column1 type, column2 type, ...)
```
Sample data (3-5 rows per table):
[PASTE SAMPLE]
My current query (if any):
```sql
[PASTE QUERY]
```
The problem: [wrong result / error message / too slow]

Requirements:
- Write the correct query with proper formatting
- Explain what each JOIN, WHERE, and aggregate does
- Warn about NULL handling if relevant
- Suggest indexes if the query would be slow on large tables
- If my approach is off, suggest a better structure
- Show the expected output given my sample data""",
        "how_to_use": [
            "Paste your actual table structure with data types — guessing leads to wrong queries",
            "Include 3-5 sample rows so the AI knows what the data actually looks like",
            "For slow queries, paste EXPLAIN output if you have it",
            "Specify your database engine — syntax differs across PostgreSQL, MySQL, and SQL Server",
        ],
        "example_output": """<p><strong>Task:</strong> Find customers who bought in January but not February</p>
<pre style="color:#ccc;font-size:13px;">SELECT c.customer_id, c.name
FROM customers c
WHERE EXISTS (
  SELECT 1 FROM orders o
  WHERE o.customer_id = c.customer_id
    AND o.order_date >= '2026-01-01'
    AND o.order_date &lt; '2026-02-01'
)
AND NOT EXISTS (
  SELECT 1 FROM orders o
  WHERE o.customer_id = c.customer_id
    AND o.order_date >= '2026-02-01'
    AND o.order_date &lt; '2026-03-01'
);</pre>
<p><strong>Explanation:</strong> The EXISTS clause is typically faster than LEFT JOIN + NULL check for 'has X but not Y' queries on large tables.</p>""",
        "tips": [
            "<strong>Use CTEs for clarity.</strong> Ask 'Rewrite with CTEs to make this readable.'",
            "<strong>Optimize by stages.</strong> For slow queries, ask 'What indexes would speed this up?' then 'Can the query itself be rewritten to avoid the slow part?'",
            "<strong>Test with LIMIT.</strong> Always add LIMIT 10 when testing. Ask the AI to remove it once correct.",
            "<strong>Understand the plan.</strong> Ask 'Explain the query execution plan' for queries hitting production.",
        ],
        "amazon_keywords": "SQL+database+book+guide",
        "amazon_text": "SQL Books on Amazon",
        "related": [("best-chatgpt-prompt-for-python-code", "Python Code"), ("best-chatgpt-prompt-for-excel-formulas", "Excel Formulas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-data-analysis",
        "title": "Best ChatGPT Prompt for Data Analysis",
        "subtitle": "Turn messy data into clear insights — statistical analysis, chart recommendations, and actionable takeaways.",
        "prompt": """You are a senior data analyst with expertise in statistics, visualization, and business interpretation. Help me analyze some data.

What I'm analyzing: [DESCRIBE THE DATASET]
My sample data (10-30 rows) or description:
[PASTE DATA OR DESCRIBE COLUMNS]

My question: [WHAT DO YOU WANT TO KNOW — e.g. "what's driving churn?" or "are sales trending up or down?"]
Tool I'll use: [Excel / Google Sheets / Python / R / SQL / BI tool]
Audience: [executives / peer analysts / customers / personal use]

Requirements:
- Start with 3 key takeaways (before any details)
- Suggest the most appropriate analysis type (comparison, trend, correlation, segmentation)
- If statistical tests apply, name the test and why
- Recommend 2-3 chart types to visualize the findings, with reasoning
- Call out any data quality issues or missing context
- Suggest 2-3 follow-up questions worth investigating
- Translate findings into specific actions or decisions""",
        "how_to_use": [
            "Paste real data when possible — make up sample rows if you're testing the prompt",
            "Be specific about the business question — 'what's going on' is too vague",
            "Tell the AI the audience — executives need different analysis than peer analysts",
            "Ask for the 'so what?' — every analysis should lead to a decision",
        ],
        "example_output": """<p><strong>Dataset:</strong> Monthly churn rate and feature usage data for a SaaS product</p>
<p><strong>Top 3 Takeaways:</strong></p>
<ol><li>Churn is 3.2x higher among users who never used the integration features — integrations are a leading indicator of retention</li>
<li>The top churn driver isn't price, it's time-to-first-value — users who don't complete setup in 7 days churn at 68%</li>
<li>Customers who email support within 30 days have 40% lower churn — support contact correlates with retention, not frustration</li></ol>
<p><strong>Recommended analysis:</strong> Logistic regression on churn with usage features as predictors, plus a cohort analysis by onboarding completion.</p>
<p><strong>Charts:</strong> Cohort retention heatmap (onboarding cohorts x months active), and a bar chart of churn rate by feature adoption tier.</p>""",
        "tips": [
            "<strong>Start with takeaways, not tables.</strong> Ask 'What are the 3 most important findings?' before the details.",
            "<strong>Correlation vs causation.</strong> Always ask 'Is this a real cause or just correlated?' before taking action.",
            "<strong>Compare to a baseline.</strong> Numbers mean nothing alone. Ask 'What's the benchmark for this metric in [industry]?'",
            "<strong>Sanity check.</strong> Ask 'What would make this analysis wrong?' — catches assumption errors.",
        ],
        "amazon_keywords": "data+analysis+book+business+analytics",
        "amazon_text": "Data Analysis Books",
        "related": [("best-chatgpt-prompt-for-sql-queries", "SQL Queries"), ("best-chatgpt-prompt-for-excel-formulas", "Excel Formulas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-gift-ideas",
        "title": "Best ChatGPT Prompt for Gift Ideas",
        "subtitle": "Get personalized gift ideas for any person, budget, and occasion — no more generic gift guides.",
        "prompt": """You are a thoughtful, creative gift-giver who finds the perfect gift every time. Help me find a gift.

Who it's for: [RELATIONSHIP — e.g. mom, best friend, coworker, partner]
Their age: [AGE]
Occasion: [birthday / anniversary / wedding / holiday / just because / apology / promotion]
My budget: $[AMOUNT] or range [$X-$Y]
What they like: [HOBBIES, INTERESTS, SHOWS THEY WATCH, THINGS THEY TALK ABOUT]
What they already have: [things they own related to their interests — avoid duplicates]
Their personality: [practical / sentimental / adventurous / homebody / luxury-minded / minimalist]
Any constraints: [no alcohol / no clutter / must ship to X country]

Requirements:
- Give me 10 gift ideas across different price points within my budget
- Each idea should explain WHY this person would like it (based on their interests)
- Flag anything that's a 'safe' choice vs 'thoughtful' choice
- Include at least 2 experiences, not just physical gifts
- For each idea, suggest where to buy it
- Avoid cliches (candles, generic wine, 'world's best ___' mugs)
- If a DIY/personalized version exists, mention it""",
        "how_to_use": [
            "Be specific about what they like — 'she likes reading' gets generic ideas, 'she's into historical fiction especially about Cold War espionage' gets great ones",
            "Include what they already have so you avoid duplicates",
            "Tell the AI what you've already tried or ruled out",
            "Ask for follow-ups like 'Give me 5 more ideas in the $50-75 range'",
        ],
        "example_output": """<p><strong>For:</strong> Dad, 65, retired, into woodworking and history podcasts. Budget: $100.</p>
<p><strong>Gift ideas:</strong></p>
<ul>
<li><strong>$80 — Custom engraved woodworking ruler</strong> — Practical for his hobby and personalized. Check Etsy for a combo square or marking gauge with his name.</li>
<li><strong>$60 — A History of Private Life (5-volume series)</strong> — Since he loves history podcasts, this is a beautifully written social history he can dip into.</li>
<li><strong>$100 — Experience: Woodworking class tuition</strong> — Local makerspaces offer classes on specific techniques (hand-cut dovetails, finishing). Gives him a story, not just a thing.</li>
</ul>""",
        "tips": [
            "<strong>Drill into interests.</strong> Don't just say 'loves cooking' — say 'makes his own pizza dough and has been experimenting with sourdough for 2 years.'",
            "<strong>Ask for a 'safe + wild' pair.</strong> Say 'Give me one safe bet and one surprising gift' so you have options.",
            "<strong>Consumables are underrated.</strong> Ask 'What are the best consumable gifts so I don't add clutter?'",
            "<strong>Personalize it.</strong> Say 'Which of these could I customize or personalize in a meaningful way?'",
        ],
        "amazon_keywords": "best+selling+gifts",
        "amazon_text": "Shop Gift Ideas on Amazon",
        "related": [("best-chatgpt-prompt-for-dating-profile", "Dating Profile"), ("best-chatgpt-prompt-for-travel-planning", "Travel Planning")],
    },
    {
        "slug": "best-chatgpt-prompt-for-recipes",
        "title": "Best ChatGPT Prompt for Recipes",
        "subtitle": "Get recipes customized to what's in your fridge, your skill level, and your dietary needs.",
        "prompt": """You are a professional chef and recipe developer. Create a recipe for me.

What I want: [pick one]
- A recipe using these ingredients I have: [LIST INGREDIENTS]
- A specific dish: [DISH NAME]
- A recipe for [meal type] that's [dietary requirement]
- Something new — surprise me based on what I like

Cooking skill level: [beginner / intermediate / advanced]
Time available: [e.g. under 30 min, 1 hour, all afternoon]
Equipment I have: [stove, oven, air fryer, slow cooker, instant pot, grill — list yours]
Dietary restrictions: [e.g. vegetarian, gluten-free, dairy-free, low-carb, allergies]
Servings: [NUMBER OF PEOPLE]

Requirements:
- Give me the recipe with exact measurements (not 'a pinch' — tell me teaspoons)
- List ingredients in the order I'll use them
- Number each step clearly
- Flag any technique that's critical (don't overcook, room temp butter, etc.)
- Include substitutions for common ingredient swaps
- Suggest what to serve it with
- If it stores or freezes well, tell me how
- Include approximate nutritional info per serving if possible""",
        "how_to_use": [
            "If you're improvising, list what's in your fridge/pantry — the AI will work with constraints",
            "Be honest about skill level — a beginner shouldn't try a three-hour recipe as their first effort",
            "Include allergies and dietary needs upfront — they change the whole recipe",
            "Ask follow-ups like 'Can I make this ahead?' or 'Give me a lazier version of this for Wednesday night'",
        ],
        "example_output": """<p><strong>Recipe:</strong> 20-minute weeknight lemon garlic shrimp pasta (serves 4)</p>
<p><strong>Ingredients:</strong></p>
<ul><li>12 oz linguine</li>
<li>1.5 lb shrimp, peeled and deveined</li>
<li>4 tbsp butter</li>
<li>6 garlic cloves, thinly sliced</li>
<li>1/4 tsp red pepper flakes</li>
<li>1 lemon (zest and juice)</li>
<li>1/4 cup reserved pasta water</li>
<li>1/4 cup fresh parsley, chopped</li>
<li>Salt and pepper to taste</li></ul>
<p><strong>Steps:</strong></p>
<ol><li>Cook pasta to 1 minute before al dente. Reserve 1/4 cup water, drain.</li>
<li>While pasta cooks: melt 2 tbsp butter in a large skillet over medium-high. Add shrimp in single layer — don't crowd. Salt lightly. Flip after 90 seconds. Transfer to a plate after another 60 seconds.</li>
<li>Reduce heat to medium. Add remaining 2 tbsp butter, garlic, and pepper flakes. Cook 30 seconds — don't let garlic brown.</li>
<li>Add pasta, shrimp, lemon zest, lemon juice, and reserved water. Toss 1 minute until glossy. Taste, add salt. Top with parsley.</li></ol>""",
        "tips": [
            "<strong>Ask for variations.</strong> 'Give me 3 ways to change this recipe based on what's in season.'",
            "<strong>Meal prep mode.</strong> Say 'Scale this to 8 servings and tell me how to store it for the week.'",
            "<strong>Budget-aware.</strong> Add 'Keep ingredient cost under $15' for realistic weeknight meals.",
            "<strong>Sub intelligently.</strong> Ask 'If I don't have [ingredient], what's the best substitute and how does it change the dish?'",
        ],
        "amazon_keywords": "cookbook+bestseller",
        "amazon_text": "Cookbooks on Amazon",
        "related": [("best-chatgpt-prompt-for-meal-planning", "Meal Planning"), ("best-chatgpt-prompt-for-workout-plan", "Workout Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-book-summary",
        "title": "Best ChatGPT Prompt for Book Summaries",
        "subtitle": "Get the key ideas, quotes, and takeaways from any book in minutes — without reading the whole thing.",
        "prompt": """You are an expert at distilling books into their most useful ideas. Summarize a book for me.

Book title: [TITLE]
Author: [AUTHOR]
Why I'm reading it: [e.g. for work / personal growth / research / I read the first chapter and want an overview]
My existing knowledge: [beginner in this topic / familiar with similar books / expert in the field]
How deep do I want to go: [quick 200-word summary / detailed breakdown with chapter-by-chapter / just the key ideas I can apply]

Requirements:
- Start with a 2-sentence TLDR
- List the 5-7 core ideas/arguments of the book
- For each core idea: explain it in plain language, then give one concrete example
- Include 3-5 memorable quotes (with page numbers if known)
- List the practical takeaways — what should I actually do differently after reading this
- Flag any weaknesses or common criticisms of the book
- Recommend 2-3 similar books I should read next if I liked this one""",
        "how_to_use": [
            "Specify the book and your purpose — a summary for a work presentation is different from one for personal insight",
            "Tell the AI your existing knowledge so it doesn't waste time on basics",
            "Ask follow-ups like 'Expand on idea #3' for deeper dives on the parts that matter",
            "Never rely only on a summary for important decisions — read the real book for anything high-stakes",
        ],
        "example_output": """<p><strong>Book:</strong> 'Atomic Habits' by James Clear</p>
<p><strong>TLDR:</strong> Small changes to your systems (not goals) compound into massive results. You don't rise to the level of your goals — you fall to the level of your systems.</p>
<p><strong>Core ideas:</strong></p>
<ol><li><strong>The 1% rule:</strong> Getting 1% better daily makes you 37x better in a year. Tiny improvements compound.</li>
<li><strong>Identity over outcome:</strong> Don't say 'I'm trying to quit smoking.' Say 'I'm not a smoker.' Identity-based habits stick; outcome-based ones don't.</li>
<li><strong>The four laws:</strong> Make good habits obvious, attractive, easy, and satisfying. Make bad ones invisible, unattractive, hard, and unsatisfying.</li></ol>""",
        "tips": [
            "<strong>Read the summary, then skim the book.</strong> Summaries give you the map, but the details are where it lands emotionally.",
            "<strong>Compare books.</strong> Ask 'How does this book's advice differ from [another book]?' to find the unique insights.",
            "<strong>Ask for objections.</strong> 'What would a skeptic say about this book's main argument?' sharpens your understanding.",
            "<strong>Turn ideas into actions.</strong> Say 'Pick the 3 ideas most applicable to [my situation] and give me a 30-day plan.'",
        ],
        "amazon_keywords": "bestselling+books+personal+development",
        "amazon_text": "Bestsellers on Amazon",
        "related": [("best-chatgpt-prompt-for-summarizing-articles", "Summarizing Articles"), ("best-chatgpt-prompt-for-studying", "Studying")],
    },
    {
        "slug": "best-chatgpt-prompt-for-podcast-script",
        "title": "Best ChatGPT Prompt for Podcast Scripts",
        "subtitle": "Write podcast scripts with compelling intros, story-driven structure, and CTAs that grow your show.",
        "prompt": """You are a podcast producer who has worked on shows with 10M+ downloads. Write a podcast script for me.

Episode topic: [WHAT IT'S ABOUT]
Show format: [solo / interview / co-hosted / narrative / news/commentary]
Target episode length: [NUMBER] minutes
Show niche: [e.g. business, true crime, comedy, health, personal finance]
Target audience: [WHO LISTENS TO YOUR SHOW]
Tone: [professional / conversational / funny / dramatic / educational]
Guest info (if applicable): [NAME, what they're known for]

Requirements:
- Open with a 30-60 second hook that creates curiosity
- Clear intro (what listeners will learn, why it matters)
- Main content structured into 3-5 segments with natural transitions
- Include a mid-roll break with a light CTA (subscribe, review, social)
- Strong close that teases the next episode
- Write in spoken language — no essay-style sentences
- Mark pauses [PAUSE], emphasis [EMPHASIS], and music cues [MUSIC] where helpful
- Include timestamps for each segment
- For interviews: 10-15 questions in a logical order, with natural follow-ups""",
        "how_to_use": [
            "Specify the show format up front — solo scripts are very different from interviews",
            "Match the length to your average episode — longer formats need more hooks and breaks",
            "Read the script out loud before recording — rewrite anything that sounds written",
            "For interviews, ask 'What are the 3 questions this guest has NEVER been asked?' for unique content",
        ],
        "example_output": """<p><strong>Episode: 'Why You're Not Actually Lazy' (Solo, 25 min)</strong></p>
<p><strong>[HOOK — 0:00]</strong></p>
<p>For five years, I told myself I was lazy. I had the evidence: unread books, skipped workouts, half-finished projects. Case closed.</p>
<p>Then a therapist said something that reframed everything: "You're not lazy. You're exhausted from decisions you don't know you're making." [PAUSE]</p>
<p>That sentence cost me $300. It was worth $10,000.</p>
<p><strong>[INTRO — 1:15]</strong></p>
<p>Today we're going deep on decision fatigue — what it actually is, why we mistake it for laziness, and the three changes I made that freed up 4 hours of mental bandwidth a day...</p>""",
        "tips": [
            "<strong>Write for the ear, not the eye.</strong> Sentences should match how you actually talk.",
            "<strong>Use 'you' liberally.</strong> Talking to one listener, not an audience, creates intimacy.",
            "<strong>Get 3 CTAs.</strong> Ask 'Write me 3 different ways to ask for a review that don't feel desperate.'",
            "<strong>Repurpose.</strong> After the script, say 'Pull 5 quote-worthy lines from this for social media.'",
        ],
        "amazon_keywords": "podcast+guide+book+audio",
        "amazon_text": "Podcasting Books on Amazon",
        "related": [("best-chatgpt-prompt-for-youtube-scripts", "YouTube Scripts"), ("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post")],
    },
    {
        "slug": "best-chatgpt-prompt-for-negotiation",
        "title": "Best ChatGPT Prompt for Negotiation",
        "subtitle": "Get a negotiation strategy, scripts, and response handling for salary, contracts, or deals.",
        "prompt": """You are a negotiation expert trained at the Harvard Program on Negotiation. Help me prepare for a negotiation.

What I'm negotiating: [SALARY / CONTRACT / DEAL / PRICE / TERMS]
Who I'm negotiating with: [RELATIONSHIP — e.g. potential employer, vendor, client, landlord]
My goal: [IDEAL OUTCOME — include specific numbers]
My BATNA (best alternative if this fails): [WHAT YOU'LL DO IF YOU CAN'T REACH A DEAL]
What I think their goal is: [WHAT THEY WANT — your best guess]
Current state of negotiation: [haven't started / they made an offer / I made an offer / stuck on [specific issue]]
My leverage: [what gives me bargaining power]
Their leverage: [what gives them bargaining power]

Give me:
1. A specific opening position (anchor) with justification
2. My walk-away number/terms
3. A script for the opening conversation (3-4 lines)
4. Responses to 5 likely pushbacks from them
5. 3 creative 'expand the pie' options that add value for both sides
6. Red flags — what would signal I should walk away
7. How to close when we reach agreement""",
        "how_to_use": [
            "Be specific about numbers — 'more money' isn't a negotiation strategy",
            "Always define your BATNA first — it's the foundation of any good negotiation",
            "Practice the scripts out loud — tone matters more than the exact words",
            "Do a post-mortem: after the negotiation, come back with 'Here's what happened — what could I have done better?'",
        ],
        "example_output": """<p><strong>Scenario:</strong> Salary negotiation for a Senior PM role. Offered $145K. Researched market is $150-170K.</p>
<p><strong>Opening anchor:</strong> "$172K base, given my 8 years of experience and the product leadership scope of this role."</p>
<p><strong>Walk-away:</strong> $158K base + equity refresh, or I take my other offer at $160K + RSUs.</p>
<p><strong>Script:</strong></p>
<p>"Thanks for the offer — I'm excited about the role. Based on my research of comparable Senior PM comp in [city] and the scope you described, I was expecting total comp around $175K. Can we get to $172K on the base, or is there flexibility in the equity to close the gap?"</p>
<p><strong>Pushback: 'Our range maxes out at $150K.'</strong></p>
<p>Response: "I understand ranges are tight. If the base is capped, can we look at a signing bonus or accelerated equity vesting? Those would close the gap without breaking the band."</p>""",
        "tips": [
            "<strong>Silence is a tool.</strong> Ask 'What happens if I just don't respond for 24 hours after their offer?' — patience is leverage.",
            "<strong>Reframe concessions.</strong> Ask 'How do I ask for X without framing it as a demand?' for softer delivery.",
            "<strong>Know your second-best offer.</strong> Ask 'What's the minimum I should accept given my BATNA?'",
            "<strong>Practice the hard questions.</strong> Say 'Role-play as the toughest version of my counterparty and push back on my asks.'",
        ],
        "amazon_keywords": "negotiation+book+bestseller",
        "amazon_text": "Negotiation Books on Amazon",
        "related": [("best-chatgpt-prompt-for-job-interview-prep", "Job Interview Prep"), ("best-chatgpt-prompt-for-writing-emails", "Writing Emails")],
    },
    {
        "slug": "best-chatgpt-prompt-for-content-ideas",
        "title": "Best ChatGPT Prompt for Content Ideas",
        "subtitle": "Generate a month of content ideas tailored to your niche — blog posts, videos, and social posts that your audience wants.",
        "prompt": """You are a content strategist who has built audiences from zero to 1M+ followers. Generate content ideas for me.

My niche: [YOUR NICHE — be specific, 'personal finance' is too broad, 'personal finance for Gen Z freelancers' is better]
My platform(s): [blog / YouTube / Instagram / TikTok / LinkedIn / Twitter / newsletter]
My audience: [WHO THEY ARE — demographics, pain points, goals]
Content I've already made: [LIST 3-5 TITLES that performed well]
Content that flopped: [LIST 2-3 that didn't work, if you know]
Frequency: [HOW OFTEN YOU POST]

Requirements:
- Generate 30 content ideas across 5 categories:
  1. Evergreen tutorials (teach something timeless)
  2. Opinion/hot take pieces
  3. Personal story with a lesson
  4. Listicle / comparison
  5. News/timely commentary on current events in my niche
- For each idea, write a compelling working title
- Suggest the best format for each (short-form, long-form, thread, video, etc.)
- Rank them by estimated engagement (high/medium/low) with reasoning
- Flag 3 ideas that could become a series of 5+ posts""",
        "how_to_use": [
            "Specify your niche tightly — specificity is your friend, not your enemy",
            "Include what's already worked — the AI will build on your proven angles",
            "Pick 3-5 ideas from the list and batch-create them in one sitting",
            "Come back monthly: 'I posted these 5, here's what performed. Generate the next 30 based on this data.'",
        ],
        "example_output": """<p><strong>Niche:</strong> Productivity for remote software engineers</p>
<p><strong>Evergreen tutorial:</strong></p>
<ul><li>"The 3-folder system I use to find any file in under 10 seconds" (High engagement — specific, actionable, personal framing)</li></ul>
<p><strong>Hot take:</strong></p>
<ul><li>"Async communication is the most overrated productivity idea of 2026" (High engagement — controversial, niche-specific, invites debate)</li></ul>
<p><strong>Personal story:</strong></p>
<ul><li>"I took a 3-month break from Slack. Here's what happened to my career." (Medium-high — personal stakes, taboo topic for remote workers)</li></ul>""",
        "tips": [
            "<strong>Mine your comments.</strong> Tell the AI: 'Here are 10 questions from my comments — turn each into a content idea.'",
            "<strong>Steal from other niches.</strong> Ask 'What ideas are crushing it in [adjacent niche] that I could adapt?'",
            "<strong>Build series.</strong> Single posts drive traffic. Series drive subscribers. Ask 'Turn this into a 7-part series.'",
            "<strong>Repurpose ruthlessly.</strong> After a piece performs well, say 'Give me 5 ways to turn this into other formats.'",
        ],
        "amazon_keywords": "content+marketing+book+strategy",
        "amazon_text": "Content Marketing Books",
        "related": [("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post"), ("best-chatgpt-prompt-for-social-media-captions", "Social Media Captions")],
    },
    {
        "slug": "best-chatgpt-prompt-for-wedding-planning",
        "title": "Best ChatGPT Prompt for Wedding Planning",
        "subtitle": "Get a detailed wedding planning checklist, vendor questions, and timeline tailored to your budget and style.",
        "prompt": """You are a wedding planner with 15 years of experience planning 500+ weddings. Help me plan my wedding.

Wedding date: [DATE]
Current date: [TODAY'S DATE] — so you know how much time I have
Budget: $[TOTAL AMOUNT]
Guest count: [NUMBER]
Location/venue: [LOCATION — indoor/outdoor, already booked or still deciding]
Style: [e.g. rustic, modern, traditional, destination, backyard, formal]
Season: [FALL / SPRING / SUMMER / WINTER]
Priorities (rank 1-3): [photography / food / music / venue / decor / dress / other]
What I want to skip: [anything I don't care about or don't want]
Help I already have: [family planner / wedding planner / just me]

Give me:
1. A month-by-month checklist from now until the wedding
2. A realistic budget breakdown by category (what % of budget to spend where)
3. The 5 vendors I need to book FIRST and questions to ask each
4. DIY opportunities to save money without lowering quality
5. 5 common wedding planning mistakes I should avoid
6. A wedding day timeline template (hour-by-hour)
7. Etiquette questions I might forget to think about""",
        "how_to_use": [
            "Include your actual budget and guest count — a $20K wedding for 50 is totally different from $100K for 200",
            "Tell the AI your priorities so it knows where to splurge and where to save",
            "Follow up with questions like 'I got the florist quote — is $4K reasonable?' for sanity checks",
            "Ask 'Draft an email to my photographer asking [specific question]' when you need vendor communication help",
        ],
        "example_output": """<p><strong>Budget breakdown for $30K, 100 guests:</strong></p>
<ul><li><strong>Venue + catering (40%):</strong> $12,000</li>
<li><strong>Photography/videography (12%):</strong> $3,600</li>
<li><strong>Attire (8%):</strong> $2,400</li>
<li><strong>Flowers/decor (8%):</strong> $2,400</li>
<li><strong>Music/entertainment (8%):</strong> $2,400</li>
<li><strong>Cake + extras (6%):</strong> $1,800</li>
<li><strong>Stationery (3%):</strong> $900</li>
<li><strong>Hair/makeup (3%):</strong> $900</li>
<li><strong>Officiant/license (2%):</strong> $600</li>
<li><strong>Buffer (10%):</strong> $3,000 — Every wedding goes over. Plan for it.</li></ul>""",
        "tips": [
            "<strong>Book venue and photographer first.</strong> Ask 'Why are these the two things I need to book 9+ months ahead?' if you need convincing.",
            "<strong>Contract questions.</strong> Say 'What should I look for in a photographer contract before signing?' for every major vendor.",
            "<strong>Rehearsal dinner gets skipped.</strong> Ask 'What do most couples underestimate when planning?' to avoid common gotchas.",
            "<strong>Day-of timeline.</strong> Ask 'Build me an hour-by-hour day-of timeline starting from hair/makeup at 8am.'",
        ],
        "amazon_keywords": "wedding+planner+book+organizer",
        "amazon_text": "Wedding Planning Books",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-travel-planning", "Travel Planning")],
    },
    {
        "slug": "best-chatgpt-prompt-for-birthday-message",
        "title": "Best ChatGPT Prompt for Birthday Messages",
        "subtitle": "Write thoughtful, personal birthday messages for anyone in your life — in any tone.",
        "prompt": """You are a writer who specializes in heartfelt, personal messages. Write a birthday message for me.

Who it's for: [RELATIONSHIP — e.g. best friend, mom, partner, coworker, grandparent]
Their name: [NAME]
Age they're turning: [AGE]
Their personality: [funny / serious / sentimental / low-key / extra]
Our relationship (in 2 sentences): [HOW YOU KNOW EACH OTHER, WHAT YOU MEAN TO EACH OTHER]
Inside jokes or shared memories: [LIST ANY if relevant]
Tone I want: [funny / sentimental / sweet / roasty / formal / heartfelt]
Length: [short (text/card) / medium (social post) / long (letter)]
Where it's going: [text / social media post / card / toast / email]

Requirements:
- Write 3 different versions in different tones so I can pick
- Make it feel like I wrote it, not generic
- Reference our real relationship or shared history, not generic birthday phrases
- Avoid cliches like "another year older, another year wiser"
- If sentimental, earn the sentiment — don't just declare it
- Match the length to the format — texts are short, toasts can be longer""",
        "how_to_use": [
            "Give real details about your relationship — generic input means generic output",
            "Include inside jokes or shared memories if you have them — specificity is what makes messages feel personal",
            "Pick the tone that matches your normal communication style with this person",
            "Always edit the AI's version to sound like you — small changes matter",
        ],
        "example_output": """<p><strong>For:</strong> Best friend turning 30. Tone: funny + sentimental.</p>
<p><strong>Version 1 (Sentimental with humor):</strong></p>
<p>Happy 30th, Sarah. I've known you since you used to think Diet Coke was a vegetable, and somehow you've become one of the most grounded people I know — except for the Diet Coke thing, which is still happening.</p>
<p>You've seen me through three jobs, two bad boyfriends, and that phase where I thought I could become a ceramicist. You always have the right thing to say, which is usually "that's a terrible idea," delivered with love.</p>
<p>Thanks for being my person. Here's to 30 more years of your very specific brand of honesty.</p>""",
        "tips": [
            '<strong>Reference something specific.</strong> "You are amazing" is nothing. "Remember when you drove 4 hours to help me move my couch" is everything.',
            "<strong>End strong.</strong> Ask 'Give me 3 different closings for this message' — the last line is what they'll remember.",
            "<strong>Match the medium.</strong> A text should feel like a text. A toast should feel spoken, not written.",
            "<strong>For speeches, time it out.</strong> Say 'How long will this take to read out loud at a normal pace?' — keep toasts under 2 minutes.",
        ],
        "amazon_keywords": "greeting+cards+birthday+personalized",
        "amazon_text": "Birthday Cards on Amazon",
        "related": [("best-chatgpt-prompt-for-gift-ideas", "Gift Ideas"), ("best-chatgpt-prompt-for-writing-emails", "Writing Emails")],
    },
    {
        "slug": "best-chatgpt-prompt-for-pet-training",
        "title": "Best ChatGPT Prompt for Pet Training",
        "subtitle": "Get a step-by-step training plan for your dog or cat — built around their age, breed, and behavior issues.",
        "prompt": """You are a certified professional dog (or cat) trainer with 15 years of experience in positive reinforcement training. Build me a training plan.

Pet type: [DOG / CAT]
Breed: [BREED OR MIX]
Age: [AGE]
Current behavior I want to change: [BE SPECIFIC — e.g. "pulls on leash," "jumps on guests," "doesn't come when called," "scratches furniture"]
How long has this been a problem: [NEW / MONTHS / YEARS]
Training experience: [BEGINNER / INTERMEDIATE / ADVANCED]
Daily time available: [MINUTES PER DAY]
Pet's motivators: [what they love — specific treats, toys, praise, play]
Other pets/kids in the home: [any factors]
Vet issues: [any health issues that might affect training]

Requirements:
- Start by explaining WHY the pet is doing this behavior — root cause matters
- Give me a 2-4 week progressive training plan (day by day for week 1, then by week)
- Each day: what to work on, for how long, how to know if we're making progress
- Use positive reinforcement only — no aversive methods
- Flag exactly when to reward and what the reward should be
- Include what NOT to do — common mistakes that reinforce the bad behavior
- Tell me when to contact a professional trainer or vet behaviorist""",
        "how_to_use": [
            "Be very specific about the behavior — 'bad on walks' could mean 5 different things",
            "Include the pet's breed and age — a 3-month-old puppy and a 7-year-old dog need different approaches",
            "Track progress daily — come back after a week with 'Day 7 update: [what happened]. Adjust the plan.'",
            "If a behavior could be medical (sudden changes, aggression, accidents), see a vet before a trainer",
        ],
        "example_output": """<p><strong>Scenario:</strong> 6-month-old Golden Retriever puppy who jumps on everyone.</p>
<p><strong>Why it happens:</strong> Jumping is an attention-seeking behavior. Every time someone reacts — talking, pushing them down, making eye contact — the jump gets reinforced. Puppies do it because it works.</p>
<p><strong>Week 1 goal:</strong> Break the reinforcement loop.</p>
<ul><li><strong>Days 1-3:</strong> No attention when he jumps. Turn away, no eye contact, no "no." The instant all four paws are on the floor, say "yes!" and give a treat. Practice 5 times per entry, 5 short sessions per day.</li>
<li><strong>Days 4-7:</strong> Add "sit" command when visitors arrive. Reward the sit, not the absence of jumping. Visitors only give attention when dog is sitting.</li></ul>
<p><strong>Common mistakes:</strong> Telling guests "it's fine" and letting them pet a jumping dog. Every time this happens, you've undone a week of work.</p>""",
        "tips": [
            "<strong>Consistency > intensity.</strong> 5 minutes, 3 times a day beats an hour on weekends.",
            "<strong>Find the right reward.</strong> Ask 'My dog ignores kibble — what higher-value rewards should I use?'",
            "<strong>Environmental management.</strong> Ask 'How can I set up the environment to prevent the behavior while training?' — prevention is half the work.",
            "<strong>Rule out medical.</strong> For sudden behavior changes, always see a vet before assuming it's training.",
        ],
        "amazon_keywords": "dog+training+book+positive+reinforcement",
        "amazon_text": "Pet Training Books",
        "related": [("best-chatgpt-prompt-for-meal-planning", "Meal Planning"), ("best-chatgpt-prompt-for-workout-plan", "Workout Plan")],
    },
]

count = 0
for page in PAGES:
    make_page(**page)
    count += 1
    print(f"Created: {page['slug']}.html")

print(f"\nTotal pages created: {count}")
