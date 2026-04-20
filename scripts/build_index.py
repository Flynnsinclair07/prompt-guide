"""Auto-generate homepage, categories page, and sitemap from prompt metadata."""

# Master list of all prompts with metadata
# slug, title, category, short description
PROMPTS = [
    # Career
    ("best-chatgpt-prompt-for-writing-a-cover-letter", "Writing a Cover Letter", "Career", "Land more interviews with a tailored, professional cover letter in seconds."),
    ("best-chatgpt-prompt-for-writing-a-resume", "Writing a Resume", "Career", "Turn your experience into a clean, ATS-friendly resume that gets noticed."),
    ("best-chatgpt-prompt-for-linkedin-profile", "LinkedIn Profile", "Career", "Optimize your headline, summary, and experience to attract recruiters."),
    ("best-chatgpt-prompt-for-job-interview-prep", "Job Interview Prep", "Career", "Practice questions, STAR answers, and company research for any role."),
    ("best-chatgpt-prompt-for-resignation-letter", "Resignation Letter", "Career", "Write a professional resignation letter that protects your reputation."),
    ("best-chatgpt-prompt-for-performance-review", "Performance Review", "Career", "Write a self-review that captures impact, or review your report clearly."),

    # Business
    ("best-chatgpt-prompt-for-writing-emails", "Writing Emails", "Business", "Professional emails in any tone — cold outreach, follow-ups, or replies."),
    ("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan", "Business", "Get a complete, investor-ready business plan with strategy and financials."),
    ("best-chatgpt-prompt-for-naming-a-business", "Naming a Business", "Business", "Generate brandable, memorable business names with available domains."),
    ("best-chatgpt-prompt-for-negotiation", "Negotiation", "Business", "Get a negotiation strategy, scripts, and responses for any deal."),
    ("best-chatgpt-prompt-for-product-descriptions", "Product Descriptions", "Business", "Write product descriptions that convert for Amazon, Shopify, or Etsy."),
    ("best-chatgpt-prompt-for-real-estate-listings", "Real Estate Listings", "Business", "Write property descriptions that make buyers schedule a showing."),
    ("best-chatgpt-prompt-for-amazon-fba", "Amazon FBA", "Business", "Product research, listing optimization, and launch strategy for Amazon."),
    ("best-chatgpt-prompt-for-sales-pitch", "Sales Pitch", "Business", "Write sales pitches that close deals — cold, elevator, or discovery calls."),
    ("best-chatgpt-prompt-for-side-hustle-ideas", "Side Hustle Ideas", "Business", "Get realistic side hustle ideas based on your skills and time."),

    # Marketing
    ("best-chatgpt-prompt-for-social-media-captions", "Social Media Captions", "Marketing", "Scroll-stopping captions for Instagram, LinkedIn, and Twitter."),
    ("best-chatgpt-prompt-for-instagram-bio", "Instagram Bio", "Marketing", "Write an Instagram bio that tells people who you are and makes them follow."),
    ("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post", "Marketing", "SEO-optimized blog posts with headlines, structure, and keywords."),
    ("best-chatgpt-prompt-for-youtube-scripts", "YouTube Scripts", "Marketing", "Write video scripts with hooks that keep viewers watching until the end."),
    ("best-chatgpt-prompt-for-podcast-script", "Podcast Scripts", "Marketing", "Compelling intros, story-driven structure, and CTAs that grow your show."),
    ("best-chatgpt-prompt-for-email-marketing", "Email Marketing", "Marketing", "High-converting email campaigns — newsletters, launches, and sequences."),
    ("best-chatgpt-prompt-for-copywriting", "Copywriting", "Marketing", "Write sales copy that converts — landing pages, ads, and headlines."),
    ("best-chatgpt-prompt-for-seo", "SEO", "Marketing", "Keyword research, content gaps, and optimization to outrank competitors."),
    ("best-chatgpt-prompt-for-content-ideas", "Content Ideas", "Marketing", "Generate a month of content ideas tailored to your niche and audience."),

    # Education
    ("best-chatgpt-prompt-for-studying", "Studying", "Education", "Turn any subject into flashcards, study guides, and practice tests."),
    ("best-chatgpt-prompt-for-essay-writing", "Essay Writing", "Education", "Get well-structured essays with strong thesis and supporting arguments."),
    ("best-chatgpt-prompt-for-learning-a-language", "Learning a Language", "Education", "Practice conversations and build vocabulary with a free AI language tutor."),
    ("best-chatgpt-prompt-for-book-summary", "Book Summaries", "Education", "Get the key ideas and takeaways from any book in minutes."),
    ("best-chatgpt-prompt-for-lesson-plans", "Lesson Plans", "Education", "Generate detailed, standards-aligned lesson plans for any grade and subject."),
    ("best-chatgpt-prompt-for-research-paper", "Research Papers", "Education", "Plan, outline, and structure a research paper with academic polish."),
    ("best-chatgpt-prompt-for-creative-writing", "Creative Writing", "Education", "Use AI as a creative writing partner for stories, characters, and plots."),

    # Lifestyle
    ("best-chatgpt-prompt-for-meal-planning", "Meal Planning", "Lifestyle", "Get a full week of meals with grocery lists based on your diet and budget."),
    ("best-chatgpt-prompt-for-recipes", "Recipes", "Lifestyle", "Get recipes customized to what's in your fridge and your dietary needs."),
    ("best-chatgpt-prompt-for-workout-plan", "Workout Plan", "Lifestyle", "Get a custom gym or home routine based on your goals and schedule."),
    ("best-chatgpt-prompt-for-travel-planning", "Travel Planning", "Lifestyle", "Get a complete day-by-day travel itinerary with activities and budget."),
    ("best-chatgpt-prompt-for-dating-profile", "Dating Profile", "Lifestyle", "Write a dating profile that sounds like you and gets more matches."),
    ("best-chatgpt-prompt-for-gift-ideas", "Gift Ideas", "Lifestyle", "Personalized gift ideas for any person, budget, and occasion."),
    ("best-chatgpt-prompt-for-birthday-message", "Birthday Messages", "Lifestyle", "Thoughtful, personal birthday messages for anyone in your life."),
    ("best-chatgpt-prompt-for-wedding-planning", "Wedding Planning", "Lifestyle", "A detailed checklist, vendor questions, and timeline for your big day."),
    ("best-chatgpt-prompt-for-wedding-speech", "Wedding Speech", "Lifestyle", "Write a memorable best man, maid of honor, or parent wedding speech."),
    ("best-chatgpt-prompt-for-pet-training", "Pet Training", "Lifestyle", "A step-by-step training plan for your dog or cat based on their behavior."),
    ("best-chatgpt-prompt-for-thank-you-note", "Thank You Notes", "Lifestyle", "Write thoughtful thank you notes for any occasion."),
    ("best-chatgpt-prompt-for-apology-letter", "Apology Letter", "Lifestyle", "Write a sincere apology that takes responsibility and repairs relationships."),
    ("best-chatgpt-prompt-for-gardening", "Gardening", "Lifestyle", "Get a custom gardening plan for your climate, space, and experience level."),
    ("best-chatgpt-prompt-for-skincare-routine", "Skincare Routine", "Lifestyle", "Get a skincare routine tailored to your skin type and concerns."),
    ("best-chatgpt-prompt-for-home-improvement", "Home Improvement", "Lifestyle", "Plan DIY projects and decide when to hire a pro."),
    ("best-chatgpt-prompt-for-movie-recommendations", "Movie Recommendations", "Lifestyle", "Get movie recommendations based on your taste and current mood."),
    ("best-chatgpt-prompt-for-book-recommendations", "Book Recommendations", "Lifestyle", "Get book recommendations that match your taste and reading goals."),

    # Finance
    ("best-chatgpt-prompt-for-budgeting", "Budgeting", "Finance", "A realistic monthly budget with savings goals tailored to your income."),
    ("best-chatgpt-prompt-for-car-buying", "Car Buying", "Finance", "Pick the right car, negotiate the best price, and avoid dealer tricks."),

    # Tech
    ("best-chatgpt-prompt-for-coding", "Coding", "Tech", "Write, debug, and understand code in any programming language."),
    ("best-chatgpt-prompt-for-python-code", "Python Code", "Tech", "Write, debug, and understand Python scripts for automation and analysis."),
    ("best-chatgpt-prompt-for-sql-queries", "SQL Queries", "Tech", "Write, debug, and optimize SQL queries for any database."),
    ("best-chatgpt-prompt-for-data-analysis", "Data Analysis", "Tech", "Turn messy data into clear insights, charts, and actionable takeaways."),
    ("best-chatgpt-prompt-for-excel-formulas", "Excel Formulas", "Tech", "Describe what you need in plain English, get the exact Excel formula."),
    ("best-chatgpt-prompt-for-midjourney", "Midjourney Prompts", "AI Art", "Generate detailed Midjourney prompts that produce stunning AI images."),

    # Productivity
    ("best-chatgpt-prompt-for-summarizing-articles", "Summarizing Articles", "Productivity", "Get key takeaways from any article or document in seconds."),
    ("best-chatgpt-prompt-for-journaling", "Journaling", "Productivity", "Get thoughtful journaling prompts for self-reflection and growth."),
    ("best-chatgpt-prompt-for-goal-setting", "Goal Setting", "Productivity", "Set goals you'll actually achieve with clear metrics and weekly plans."),
    ("best-chatgpt-prompt-for-habit-building", "Building a Habit", "Productivity", "Build a habit that actually sticks using proven behavior change methods."),
    ("best-chatgpt-prompt-for-meditation-script", "Meditation Scripts", "Productivity", "Get custom guided meditation scripts for sleep, stress, or focus."),

    # Batch 3 additions
    ("best-chatgpt-prompt-for-book-writing", "Book Writing", "Education", "Outline a novel, develop characters, and write chapters with AI as a partner."),
    ("best-chatgpt-prompt-for-pitch-deck", "Pitch Deck", "Business", "Build an investor-ready pitch deck with the 10 slides that close rounds."),
    ("best-chatgpt-prompt-for-press-release", "Press Release", "Marketing", "Write press releases that journalists actually read and cover."),
    ("best-chatgpt-prompt-for-linkedin-posts", "LinkedIn Posts", "Marketing", "Write LinkedIn posts that get engagement without sounding like an influencer."),
    ("best-chatgpt-prompt-for-twitter-threads", "Twitter Threads", "Marketing", "Write X/Twitter threads with hooks and pacing that keep people reading."),
    ("best-chatgpt-prompt-for-tiktok-scripts", "TikTok Scripts", "Marketing", "Write TikTok scripts with hooks that grab attention in 2 seconds."),
    ("best-chatgpt-prompt-for-newsletter", "Newsletter Writing", "Marketing", "Write newsletters people actually open — for Substack or any list."),
    ("best-chatgpt-prompt-for-weight-loss", "Weight Loss Plan", "Lifestyle", "Get a realistic, science-based weight loss plan with calories and workouts."),
    ("best-chatgpt-prompt-for-running-training-plan", "Running Training Plan", "Lifestyle", "Get a custom plan for 5K, 10K, half marathon, or marathon."),
    ("best-chatgpt-prompt-for-sleep-better", "Sleep Better", "Lifestyle", "Diagnose why you're sleeping badly and get a step-by-step plan to fix it."),
    ("best-chatgpt-prompt-for-morning-routine", "Morning Routine", "Lifestyle", "Design a morning routine you'll actually keep based on your schedule."),
    ("best-chatgpt-prompt-for-decluttering", "Decluttering", "Lifestyle", "Declutter your home room-by-room with a realistic plan."),
    ("best-chatgpt-prompt-for-debt-payoff", "Debt Payoff Plan", "Finance", "Get out of debt faster with a personalized avalanche or snowball plan."),
    ("best-chatgpt-prompt-for-investing-beginners", "Investing for Beginners", "Finance", "Get the basics of investing — index funds, IRAs, and starting with a few hundred dollars."),
    ("best-chatgpt-prompt-for-saving-money", "Saving Money", "Finance", "Find hundreds of dollars of savings in your current budget."),
    ("best-chatgpt-prompt-for-tax-prep", "Tax Prep", "Finance", "Organize for tax season, understand deductions, and decide DIY or CPA."),
    ("best-chatgpt-prompt-for-road-trip-planning", "Road Trip Planning", "Lifestyle", "Plan a road trip with routes, stops, and daily timing."),
    ("best-chatgpt-prompt-for-toddler-activities", "Toddler Activities", "Lifestyle", "Age-appropriate activities that keep your toddler engaged."),
    ("best-chatgpt-prompt-for-homeschooling", "Homeschooling", "Education", "Plan a homeschool curriculum or tackle a tough subject."),
    ("best-chatgpt-prompt-for-photography-tips", "Photography Tips", "Tech", "Level up your photos with specific, practical advice for your camera."),
    ("best-chatgpt-prompt-for-logo-design", "Logo Design Brief", "Business", "Write a logo design brief that gets actually useful results."),

    # Batch 4
    ("best-chatgpt-prompt-for-grant-writing", "Grant Writing", "Business", "Write grant proposals that win funding for nonprofits and projects."),
    ("best-chatgpt-prompt-for-personal-statement", "Personal Statement", "Education", "Write a college or grad school personal statement that stands out."),
    ("best-chatgpt-prompt-for-scholarship-essay", "Scholarship Essay", "Education", "Write scholarship essays that win — with story and specific details."),
    ("best-chatgpt-prompt-for-eulogy", "Eulogy", "Lifestyle", "Write a heartfelt, honest eulogy that honors someone's real life."),
    ("best-chatgpt-prompt-for-stock-analysis", "Stock Analysis", "Finance", "Analyze a stock's fundamentals, competition, and risks."),
    ("best-chatgpt-prompt-for-retirement-planning", "Retirement Planning", "Finance", "Build a retirement roadmap with savings targets and projections."),
    ("best-chatgpt-prompt-for-credit-score", "Credit Score", "Finance", "Get a specific plan to raise your credit score."),
    ("best-chatgpt-prompt-for-medical-school-admission", "Medical School Application", "Education", "Craft a med school application with personal statement and secondaries."),
    ("best-chatgpt-prompt-for-law-school-admission", "Law School Application", "Education", "Write a law school personal statement, diversity statement, and addenda."),
    ("best-chatgpt-prompt-for-mba-application", "MBA Application", "Education", "Write MBA application essays that win at top programs."),
    ("best-chatgpt-prompt-for-online-course-outline", "Online Course Outline", "Business", "Design an online course students actually finish."),
    ("best-chatgpt-prompt-for-webinar-script", "Webinar Script", "Marketing", "Write a webinar script that holds attention and sells."),
    ("best-chatgpt-prompt-for-youtube-thumbnails", "YouTube Thumbnail Ideas", "Marketing", "Generate YouTube thumbnail concepts that get clicks."),
    ("best-chatgpt-prompt-for-etsy-listing", "Etsy Listing", "Business", "Write Etsy listings that rank in search and convert buyers."),
    ("best-chatgpt-prompt-for-shopify-store", "Shopify Store Setup", "Business", "Plan and launch a Shopify store with a 30-day roadmap."),
    ("best-chatgpt-prompt-for-print-on-demand", "Print on Demand", "Business", "Find winning POD niches and launch plans."),
    ("best-chatgpt-prompt-for-freelance-proposal", "Freelance Proposal", "Business", "Write Upwork and cold freelance proposals that get responses."),
    ("best-chatgpt-prompt-for-consulting-proposal", "Consulting Proposal", "Business", "Write consulting proposals that close 5-figure engagements."),
    ("best-chatgpt-prompt-for-brand-voice", "Brand Voice Guide", "Marketing", "Define your brand voice with clear rules and examples."),
    ("best-chatgpt-prompt-for-case-study", "Customer Case Study", "Marketing", "Write customer case studies that close deals."),
    ("best-chatgpt-prompt-for-white-paper", "White Paper", "Marketing", "Write B2B white papers that establish authority."),
    ("best-chatgpt-prompt-for-customer-survey", "Customer Survey", "Business", "Write survey questions that produce actionable insights."),
    ("best-chatgpt-prompt-for-pricing-strategy", "Pricing Strategy", "Business", "Set the right price without leaving money on the table."),
    ("best-chatgpt-prompt-for-customer-service-reply", "Customer Service Reply", "Business", "Write customer service replies that solve problems and calm customers."),
    ("best-chatgpt-prompt-for-resume-bullets", "Resume Bullets", "Career", "Turn boring duties into resume bullets with numbers and impact."),
    ("best-chatgpt-prompt-for-networking-email", "Networking Email", "Career", "Write cold networking emails that get responses."),
    ("best-chatgpt-prompt-for-event-planning", "Event Planning", "Lifestyle", "Plan any event with timeline, checklist, and vendor questions."),
    ("best-chatgpt-prompt-for-hiking-route", "Hiking Route Planning", "Lifestyle", "Plan a hiking trip with gear, water, and bailout plans."),
    ("best-chatgpt-prompt-for-camping-trip", "Camping Trip Planning", "Lifestyle", "Plan a camping trip with gear, meals, and activities."),
    ("best-chatgpt-prompt-for-meal-prep-sunday", "Sunday Meal Prep", "Lifestyle", "Plan a 2-3 hour Sunday meal prep with shopping list and timing."),
    ("best-chatgpt-prompt-for-speech", "Any Speech", "Lifestyle", "Write any speech with hook, story, and memorable close."),
    ("best-chatgpt-prompt-for-poem", "Writing a Poem", "Education", "Write a poem for any occasion with image, rhythm, and voice."),
    ("best-chatgpt-prompt-for-song-lyrics", "Song Lyrics", "Education", "Write song lyrics with hook and emotional arc for any genre."),
    ("best-chatgpt-prompt-for-children-book", "Children's Book", "Education", "Draft a children's book with premise, arc, and page breakdown."),
    ("best-chatgpt-prompt-for-short-story", "Short Story", "Education", "Draft a short story with strong structure in under 5,000 words."),
    ("best-chatgpt-prompt-for-dnd-campaign", "D&D Campaign", "Lifestyle", "Design a D&D campaign arc with world, villains, and plot hooks."),
    ("best-chatgpt-prompt-for-escape-room", "Escape Room Design", "Lifestyle", "Design an escape room with puzzles, themes, and flow."),
    ("best-chatgpt-prompt-for-trivia-questions", "Trivia Questions", "Lifestyle", "Write trivia questions with balanced difficulty for any event."),
    ("best-chatgpt-prompt-for-icebreakers", "Icebreakers", "Business", "Get icebreakers that don't suck for meetings and workshops."),
    ("best-chatgpt-prompt-for-sales-cold-call", "Sales Cold Call Script", "Business", "Write cold call scripts that book meetings."),
    ("best-chatgpt-prompt-for-saas-landing-page", "SaaS Landing Page", "Marketing", "Write SaaS landing page copy that converts."),
    ("best-chatgpt-prompt-for-slide-deck", "Slide Deck", "Business", "Structure a slide deck that holds attention and moves the room."),
    ("best-chatgpt-prompt-for-product-launch", "Product Launch Plan", "Marketing", "Plan a product launch with channels, assets, and metrics."),
    ("best-chatgpt-prompt-for-roast", "Roast Speech", "Lifestyle", "Write a roast that gets real laughs without crossing lines."),
    ("best-chatgpt-prompt-for-nonprofit-appeal", "Nonprofit Donation Appeal", "Business", "Write donation appeals that move people to give."),
    ("best-chatgpt-prompt-for-debate-argument", "Debate Argument", "Education", "Build a debate argument with evidence and rebuttals."),
    ("best-chatgpt-prompt-for-customer-persona", "Customer Persona", "Marketing", "Build a detailed customer persona from interviews."),
    ("best-chatgpt-prompt-for-landing-page-audit", "Landing Page Audit", "Marketing", "Audit your landing page for conversion-killing mistakes."),
    ("best-chatgpt-prompt-for-book-club-questions", "Book Club Questions", "Education", "Generate book club discussion questions that go deep."),
    ("best-chatgpt-prompt-for-slide-bio", "Professional Bio", "Career", "Write a professional bio in 3 lengths for any use."),
    ("best-chatgpt-prompt-for-instagram-story-ideas", "Instagram Story Ideas", "Marketing", "Get a week of Instagram Story content ideas."),
    ("best-chatgpt-prompt-for-retention-email", "Retention / Winback Emails", "Marketing", "Win back churned customers with smart sequences."),
]

# ===== Build homepage =====
cards_html = ""
for slug, title, cat, desc in PROMPTS:
    cards_html += f'''  <a class="card" href="/prompts/{slug}.html">
    <span class="category-tag">{cat}</span>
    <h3>{title}</h3>
    <p>{desc}</p>
  </a>
'''

index_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google Search Console verification (replace content with your verification code) -->
<meta name="google-site-verification" content="UsbuShh_rEGpXp2XLU7L0fjjSZpzPejHGhc8Z9uCh-0">
<!-- Google Analytics (GA4) - replace G-1NQKX1S4E6 with your measurement ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1NQKX1S4E6"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', 'G-1NQKX1S4E6');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>PromptGuide — Best AI Prompts for Every Use Case</title>
<meta name="description" content="Free, copy-paste AI prompts for ChatGPT and Claude. {len(PROMPTS)}+ prompts for writing, business, marketing, coding, and more.">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<nav>
  <a href="/" class="logo">PromptGuide</a>
  <a href="/categories.html">All Prompts</a>
</nav>
<div class="hero">
  <h1>The Best AI Prompt for Anything</h1>
  <p>Free, tested prompts for ChatGPT &amp; Claude. Copy, paste, get results.</p>
  <div class="search-box">
    <input type="text" id="search" placeholder="Search {len(PROMPTS)} prompts..." oninput="filterCards(this.value)">
  </div>
</div>
<div class="card-grid" id="cardGrid">
{cards_html}</div>
<footer>
<p>&copy; 2026 PromptGuide. AI prompts for every use case.</p>
<p style="margin-top:8px;">
<a href="/about.html" style="color:#888;margin-right:16px;">About</a>
<a href="/privacy.html" style="color:#888;margin-right:16px;">Privacy</a>
<a href="/affiliate-disclosure.html" style="color:#888;">Affiliate Disclosure</a>
</p>
</footer>
<script>
function filterCards(q) {{
  const cards = document.querySelectorAll('.card');
  q = q.toLowerCase();
  cards.forEach(c => {{
    const text = c.textContent.toLowerCase();
    c.style.display = text.includes(q) ? '' : 'none';
  }});
}}
</script>
</body>
</html>
'''

with open('index.html', 'w') as f:
    f.write(index_html)

# ===== Build categories page =====
from collections import defaultdict
by_cat = defaultdict(list)
for slug, title, cat, desc in PROMPTS:
    by_cat[cat].append((slug, title))

cat_order = ["Career", "Business", "Marketing", "Education", "Lifestyle", "Finance", "Tech", "AI Art", "Productivity"]

cat_sections = ""
for cat in cat_order:
    if cat not in by_cat:
        continue
    items = ""
    for slug, title in by_cat[cat]:
        items += f'        <li><a href="/prompts/{slug}.html">{title}</a></li>\n'
    cat_sections += f'''    <section>
      <h2>{cat}</h2>
      <ul>
{items}      </ul>
    </section>

'''

categories_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google Search Console verification (replace content with your verification code) -->
<meta name="google-site-verification" content="UsbuShh_rEGpXp2XLU7L0fjjSZpzPejHGhc8Z9uCh-0">
<!-- Google Analytics (GA4) - replace G-1NQKX1S4E6 with your measurement ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-1NQKX1S4E6"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', 'G-1NQKX1S4E6');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>All AI Prompts — Browse by Category | PromptGuide</title>
<meta name="description" content="Browse all {len(PROMPTS)} AI prompts by category — career, business, marketing, education, lifestyle, finance, tech, and more. Free to copy and paste.">
<link rel="stylesheet" href="/style.css">
</head>
<body>
<nav>
  <a href="/" class="logo">PromptGuide</a>
  <a href="/categories.html">All Prompts</a>
</nav>
<main>
  <article>
    <h1>All Prompts by Category</h1>
    <p class="subtitle">Every prompt on PromptGuide, organized by category. Click any prompt to copy it.</p>

{cat_sections}  </article>
</main>
<footer>
<p>&copy; 2026 PromptGuide. AI prompts for every use case.</p>
<p style="margin-top:8px;">
<a href="/about.html" style="color:#888;margin-right:16px;">About</a>
<a href="/privacy.html" style="color:#888;margin-right:16px;">Privacy</a>
<a href="/affiliate-disclosure.html" style="color:#888;">Affiliate Disclosure</a>
</p>
</footer>
</body>
</html>
'''

with open('categories.html', 'w') as f:
    f.write(categories_html)

# ===== Build sitemap =====
base = "https://snipprompts.com"
date = "2026-04-16"

lines = ['<?xml version="1.0" encoding="UTF-8"?>', '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
static_pages = [
    (f"{base}/", "1.0"),
    (f"{base}/categories.html", "0.9"),
    (f"{base}/about.html", "0.5"),
    (f"{base}/privacy.html", "0.3"),
    (f"{base}/affiliate-disclosure.html", "0.3"),
]
for url, priority in static_pages:
    lines.append(f"  <url><loc>{url}</loc><lastmod>{date}</lastmod><priority>{priority}</priority></url>")
for slug, _, _, _ in PROMPTS:
    lines.append(f"  <url><loc>{base}/prompts/{slug}.html</loc><lastmod>{date}</lastmod><priority>0.8</priority></url>")
lines.append('</urlset>')

with open('sitemap.xml', 'w') as f:
    f.write('\n'.join(lines) + '\n')

print(f"Built:")
print(f"  index.html with {len(PROMPTS)} cards")
print(f"  categories.html with {len(by_cat)} categories")
print(f"  sitemap.xml with {len(PROMPTS) + len(static_pages)} URLs")
