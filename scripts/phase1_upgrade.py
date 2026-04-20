"""Phase 1 upgrade — swap generic Amazon links for real bestsellers,
add course recommendations, add email capture on 10 priority pages."""
import re
from pathlib import Path

AMAZON_TAG = "promptguide-20"

def amz(asin):
    """Build an Amazon affiliate link from an ASIN."""
    return f"https://www.amazon.com/dp/{asin}?tag={AMAZON_TAG}"

def amz_search(query):
    """Fallback: build an Amazon search affiliate link."""
    q = query.replace(" ", "+")
    return f"https://www.amazon.com/s?k={q}&tag={AMAZON_TAG}"

# Real bestsellers with ASINs. Verified format — the 10-char ISBN/ASIN.
# For each priority page, 3 book picks + 1 course recommendation.
PAGE_UPGRADES = {
    "best-chatgpt-prompt-for-writing-a-resume": {
        "books": [
            ("Knock 'em Dead Resumes", "1507210574", "Martin Yate"),
            ("The Resume Writing Guide", "1542852870", "Lisa McGrimmon"),
            ("What Color Is Your Parachute?", "1984860364", "Richard N. Bolles"),
        ],
        "course_title": "Resume Writing & Job Interview Masterclass",
        "course_url": "https://www.udemy.com/topic/resume-writing/",
        "course_blurb": "When you want a deeper walkthrough with video examples, Udemy has full courses on resume writing and job searching — usually $12-20.",
    },
    "best-chatgpt-prompt-for-writing-a-cover-letter": {
        "books": [
            ("Cover Letter Magic", "1593575904", "Wendy S. Enelow"),
            ("The Damn Good Resume Guide", "1607741709", "Yana Parker"),
            ("Knock 'em Dead Cover Letters", "1507210582", "Martin Yate"),
        ],
        "course_title": "Job Application & Cover Letter Course",
        "course_url": "https://www.udemy.com/topic/cover-letter/",
        "course_blurb": "Want someone to walk you through cover letter writing step by step? Udemy has affordable courses with real examples.",
    },
    "best-chatgpt-prompt-for-job-interview-prep": {
        "books": [
            ("Cracking the Coding Interview", "0984782850", "Gayle Laakmann McDowell"),
            ("Decode and Conquer", "0615932924", "Lewis C. Lin"),
            ("60 Seconds and You're Hired!", "0143129155", "Robin Ryan"),
        ],
        "course_title": "Interview Skills Courses",
        "course_url": "https://www.coursera.org/search?query=job%20interview",
        "course_blurb": "Coursera has free-to-audit courses from top universities on interview skills — great if you want structured practice beyond AI.",
    },
    "best-chatgpt-prompt-for-linkedin-profile": {
        "books": [
            ("LinkedIn Profile Optimization For Dummies", "1119651425", "Donna Serdula"),
            ("LinkedIn Riches", "1500651796", "John Nemo"),
            ("The LinkedIn Sales Playbook", "1535428554", "Brynne Tillman"),
        ],
        "course_title": "LinkedIn Marketing Courses",
        "course_url": "https://www.linkedin.com/learning/topics/linkedin",
        "course_blurb": "LinkedIn Learning itself has the best courses on optimizing LinkedIn. First month is free.",
    },
    "best-chatgpt-prompt-for-writing-a-business-plan": {
        "books": [
            ("The $100 Startup", "0307951529", "Chris Guillebeau"),
            ("The Lean Startup", "0307887898", "Eric Ries"),
            ("Business Model Generation", "0470876417", "Alexander Osterwalder"),
        ],
        "course_title": "Business Plan Writing Course",
        "course_url": "https://www.coursera.org/courses?query=business%20plan",
        "course_blurb": "Coursera and edX have free university courses on entrepreneurship and business planning — auditable at no cost.",
    },
    "best-chatgpt-prompt-for-copywriting": {
        "books": [
            ("The Boron Letters", "1483431509", "Gary Halbert"),
            ("Breakthrough Advertising", "1732538107", "Eugene M. Schwartz"),
            ("Ogilvy on Advertising", "039472903X", "David Ogilvy"),
        ],
        "course_title": "Copywriting Courses",
        "course_url": "https://copyhackers.com/copy-school/",
        "course_blurb": "CopyHackers runs the best copywriting school online. If you want to go pro, their Copy School is the standard.",
    },
    "best-chatgpt-prompt-for-seo": {
        "books": [
            ("SEO 2024", "B0C5L5Q2M7", "Adam Clarke"),
            ("The Art of SEO", "149209740X", "Eric Enge"),
            ("SEO for Growth", "069274444X", "John Jantsch"),
        ],
        "course_title": "Ahrefs Free SEO Course",
        "course_url": "https://ahrefs.com/academy",
        "course_blurb": "Ahrefs Academy is free and excellent — video lessons from the company that makes the most popular SEO tool.",
    },
    "best-chatgpt-prompt-for-email-marketing": {
        "books": [
            ("DotCom Secrets", "1788179323", "Russell Brunson"),
            ("Email Persuasion", "0989247910", "Ian Brodie"),
            ("Invisible Selling Machine", "0692475338", "Ryan Deiss"),
        ],
        "course_title": "Email Marketing Courses",
        "course_url": "https://www.skillshare.com/browse/email-marketing",
        "course_blurb": "Skillshare has practical, project-based email marketing classes. Free trial covers most beginners' needs.",
    },
    "best-chatgpt-prompt-for-investing-beginners": {
        "books": [
            ("The Intelligent Investor", "0060555661", "Benjamin Graham"),
            ("A Random Walk Down Wall Street", "0393358380", "Burton G. Malkiel"),
            ("The Simple Path to Wealth", "1533667926", "JL Collins"),
        ],
        "course_title": "Investing for Beginners (Coursera)",
        "course_url": "https://www.coursera.org/courses?query=investing",
        "course_blurb": "Yale, Michigan, and Rice all offer free intro-to-investing courses on Coursera. Solid next step after the basics.",
    },
    "best-chatgpt-prompt-for-debt-payoff": {
        "books": [
            ("The Total Money Makeover", "1595555277", "Dave Ramsey"),
            ("Your Money or Your Life", "0143115766", "Vicki Robin"),
            ("I Will Teach You to Be Rich", "1523505745", "Ramit Sethi"),
        ],
        "course_title": "Financial Peace University",
        "course_url": "https://www.ramseysolutions.com/ramseyplus/financial-peace",
        "course_blurb": "Dave Ramsey's Financial Peace University is the best-known structured debt payoff program. Paid, but has a money-back guarantee.",
    },
}

def build_recommended_reads_section(upgrade):
    """Build a rich 'recommended books + course' section."""
    books_html = ""
    for title, asin, author in upgrade["books"]:
        link = amz(asin)
        books_html += f'''<li><a href="{link}" target="_blank" rel="noopener nofollow"><strong>{title}</strong></a> by {author}</li>\n'''

    course_link = upgrade["course_url"]
    course_title = upgrade["course_title"]
    course_blurb = upgrade["course_blurb"]

    return f'''<section class="tools-section" style="margin-top:32px;">
<h2>Go Deeper: Recommended Resources</h2>
<p style="color:#aaa;font-size:14px;margin-bottom:12px;">The prompt on this page gets you 80% of the way. If you want to become genuinely excellent at this, here's what I'd read and study next:</p>
<h3 style="font-size:16px;color:#fff;margin-top:16px;">📚 Best Books on This Topic</h3>
<ul style="list-style:none;padding-left:0;">
{books_html}</ul>
<h3 style="font-size:16px;color:#fff;margin-top:20px;">🎓 {course_title}</h3>
<p style="color:#ccc;font-size:14px;">{course_blurb} <a href="{course_link}" target="_blank" rel="noopener nofollow" style="color:#6c63ff;">Browse courses →</a></p>
<p style="color:#666;font-size:12px;margin-top:16px;font-style:italic;">Some of these links are affiliate links. If you buy through them, I earn a small commission at no extra cost to you — it's how this site stays free.</p>
</section>'''

EMAIL_CAPTURE_HTML = '''<section style="margin-top:40px;padding:28px;background:linear-gradient(135deg,#1a1a2e 0%,#16213e 100%);border:1px solid #333;border-radius:12px;text-align:center;">
<h2 style="color:#fff;font-size:22px;margin-bottom:8px;">Get 50 More Prompts — Free</h2>
<p style="color:#aaa;margin-bottom:20px;">Drop your email and I'll send you my 50 best prompts (not on the site) for writing, business, and productivity.</p>
<form action="CONVERTKIT_FORM_URL_HERE" method="post" style="display:flex;gap:8px;max-width:420px;margin:0 auto;flex-wrap:wrap;justify-content:center;">
<input type="email" name="email_address" placeholder="you@email.com" required style="flex:1;min-width:220px;padding:12px 14px;border:1px solid #333;border-radius:8px;background:#0f0f0f;color:#e0e0e0;font-size:15px;">
<button type="submit" style="padding:12px 20px;background:#6c63ff;color:#fff;border:none;border-radius:8px;font-size:15px;font-weight:600;cursor:pointer;">Send Me the Prompts</button>
</form>
<p style="color:#666;font-size:12px;margin-top:12px;">No spam. Unsubscribe any time.</p>
</section>'''

def upgrade_page(slug, upgrade):
    """Apply all Phase 1 changes to a single page."""
    path = Path(f"prompts/{slug}.html")
    content = path.read_text()

    # Build new recommended reads section
    new_section = build_recommended_reads_section(upgrade)

    # Build the email capture block
    email_block = EMAIL_CAPTURE_HTML

    # Find the existing "Best AI Tools for This" section and REPLACE it with:
    # 1. The new "Go Deeper" section (books + course)
    # 2. Keep the ChatGPT + Claude links as a small footer
    # Use regex to replace the whole tools-section

    # Match the existing tools-section block
    tools_pattern = re.compile(
        r'<section class="tools-section">.*?</section>',
        re.DOTALL
    )

    simple_tools_footer = '''<section class="tools-section">
<h3 style="font-size:14px;color:#888;text-transform:uppercase;letter-spacing:0.5px;">Use these prompts with:</h3>
<a href="https://chat.openai.com" target="_blank" rel="noopener">ChatGPT</a>
<a href="https://claude.ai" target="_blank" rel="noopener">Claude</a>
</section>'''

    new_content = tools_pattern.sub(new_section + "\n" + simple_tools_footer, content, count=1)

    # Insert the email capture block right before </article>
    if '</article>' in new_content:
        new_content = new_content.replace(
            '</article>',
            email_block + '\n</article>',
            1
        )

    if new_content == content:
        return False

    path.write_text(new_content)
    return True

# Execute
updated = 0
for slug, upgrade in PAGE_UPGRADES.items():
    if upgrade_page(slug, upgrade):
        print(f"Upgraded: {slug}")
        updated += 1
    else:
        print(f"Skipped (no change): {slug}")

print(f"\n{updated}/{len(PAGE_UPGRADES)} pages upgraded")
