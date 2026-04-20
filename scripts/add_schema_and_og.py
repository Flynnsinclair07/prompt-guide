"""Overnight job: add JSON-LD schema (HowTo + FAQPage + BreadcrumbList)
and Open Graph + Twitter card tags to all 134 prompt pages."""
import re
import json
from pathlib import Path

BASE_URL = "https://flynnsinclair07.github.io/prompt-guide"
SITE_NAME = "PromptGuide"

def build_schema(title, description, slug, h1):
    """Build JSON-LD structured data for a prompt page."""
    url = f"{BASE_URL}/prompts/{slug}.html"

    # HowTo schema — tells Google this is a step-by-step guide
    how_to = {
        "@context": "https://schema.org",
        "@type": "HowTo",
        "name": h1,
        "description": description,
        "url": url,
        "totalTime": "PT2M",
        "supply": [{"@type": "HowToSupply", "name": "ChatGPT or Claude account"}],
        "tool": [{"@type": "HowToTool", "name": "AI chatbot"}],
        "step": [
            {"@type": "HowToStep", "position": 1, "name": "Copy the prompt",
             "text": "Click the copy button to grab the full prompt template."},
            {"@type": "HowToStep", "position": 2, "name": "Fill in your details",
             "text": "Replace everything in [BRACKETS] with your specific information."},
            {"@type": "HowToStep", "position": 3, "name": "Paste into your AI",
             "text": "Paste the filled-in prompt into ChatGPT or Claude and hit enter."},
            {"@type": "HowToStep", "position": 4, "name": "Iterate the result",
             "text": "Review the output and ask follow-up questions to refine it."}
        ]
    }

    # FAQPage schema — eligible for Google's FAQ rich results
    faq = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [
            {
                "@type": "Question",
                "name": f"Is this prompt free to use?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Yes — every prompt on PromptGuide is free to copy and use with ChatGPT, Claude, or any AI assistant. No account required."
                }
            },
            {
                "@type": "Question",
                "name": "Does this work with ChatGPT and Claude?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Yes, this prompt works with ChatGPT (free and paid plans), Claude, Gemini, and most other AI chatbots. Just paste it in and fill in your details."
                }
            },
            {
                "@type": "Question",
                "name": "How do I get better results from this prompt?",
                "acceptedAnswer": {
                    "@type": "Answer",
                    "text": "Be specific when filling in the brackets. Generic input produces generic output. Include real details, numbers, and context. Follow up with 'make it shorter' or 'try a different angle' to iterate."
                }
            }
        ]
    }

    # BreadcrumbList — shows breadcrumb in Google SERP
    breadcrumb = {
        "@context": "https://schema.org",
        "@type": "BreadcrumbList",
        "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "PromptGuide", "item": BASE_URL + "/"},
            {"@type": "ListItem", "position": 2, "name": "Prompts",
             "item": f"{BASE_URL}/categories.html"},
            {"@type": "ListItem", "position": 3, "name": h1, "item": url}
        ]
    }

    # Combine into one script block
    combined = [how_to, faq, breadcrumb]
    return f'<script type="application/ld+json">{json.dumps(combined, ensure_ascii=False)}</script>'

def build_og_tags(title, description, slug, h1):
    """Open Graph + Twitter card meta tags."""
    url = f"{BASE_URL}/prompts/{slug}.html"
    return f'''<meta property="og:type" content="article">
<meta property="og:title" content="{h1}">
<meta property="og:description" content="{description}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{h1}">
<meta name="twitter:description" content="{description}">
<link rel="canonical" href="{url}">'''

def extract_meta(html):
    """Pull title, description, h1, slug from existing page."""
    title_m = re.search(r'<title>(.*?)</title>', html)
    desc_m = re.search(r'<meta name="description" content="(.*?)">', html)
    h1_m = re.search(r'<h1>(.*?)</h1>', html)
    return {
        "title": title_m.group(1) if title_m else "",
        "description": desc_m.group(1) if desc_m else "",
        "h1": h1_m.group(1) if h1_m else "",
    }

def upgrade_prompt_page(path):
    """Add schema + OG tags to a single prompt page."""
    html = path.read_text()

    # Skip if already has schema
    if 'application/ld+json' in html:
        return False

    meta = extract_meta(html)
    if not meta["h1"]:
        return False

    slug = path.stem

    schema_block = build_schema(meta["title"], meta["description"], slug, meta["h1"])
    og_block = build_og_tags(meta["title"], meta["description"], slug, meta["h1"])

    # Insert right before </head>
    injection = og_block + "\n" + schema_block + "\n"
    new_html = html.replace('</head>', injection + '</head>', 1)

    if new_html == html:
        return False

    path.write_text(new_html)
    return True

# Run across all prompt pages
prompts_dir = Path("prompts")
pages = sorted(prompts_dir.glob("*.html"))

updated = 0
skipped = 0
for page in pages:
    if upgrade_prompt_page(page):
        updated += 1
    else:
        skipped += 1

print(f"Schema + OG tags added to {updated} pages. Skipped {skipped}.")

# Also update homepage and categories page with basic OG tags
for static_page, title, desc, h1 in [
    ("index.html", "PromptGuide — Best AI Prompts", "Free, copy-paste AI prompts for ChatGPT and Claude. 134+ prompts for writing, business, marketing, and more.", "The Best AI Prompt for Anything"),
    ("categories.html", "All AI Prompts by Category", "Browse all 134 AI prompts by category — career, business, marketing, education, lifestyle, finance, tech.", "All Prompts by Category"),
]:
    p = Path(static_page)
    if not p.exists():
        continue
    html = p.read_text()
    if 'og:title' in html:
        continue

    url = f"{BASE_URL}/" if static_page == "index.html" else f"{BASE_URL}/{static_page}"
    og = f'''<meta property="og:type" content="website">
<meta property="og:title" content="{h1}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:site_name" content="{SITE_NAME}">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{h1}">
<meta name="twitter:description" content="{desc}">
<link rel="canonical" href="{url}">
'''

    # WebSite schema with SearchAction (shows Google a sitelinks search box)
    website_schema = {
        "@context": "https://schema.org",
        "@type": "WebSite",
        "name": SITE_NAME,
        "url": BASE_URL + "/",
        "description": desc,
        "potentialAction": {
            "@type": "SearchAction",
            "target": f"{BASE_URL}/?q={{search_term_string}}",
            "query-input": "required name=search_term_string"
        }
    }
    schema_block = f'<script type="application/ld+json">{json.dumps(website_schema)}</script>\n'

    new_html = html.replace('</head>', og + schema_block + '</head>', 1)
    p.write_text(new_html)
    print(f"Also upgraded: {static_page}")
