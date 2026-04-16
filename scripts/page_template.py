"""Helper script — generate a prompt page from structured data."""

TEMPLATE = '''<!DOCTYPE html>
<html lang="en">
<head>
<!-- Google Search Console verification (replace content with your verification code) -->
<meta name="google-site-verification" content="REPLACE_WITH_GSC_VERIFICATION_CODE">
<!-- Google Analytics (GA4) - replace G-XXXXXXXXXX with your measurement ID -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXXXXXXXXX"></script>
<script>
window.dataLayer = window.dataLayer || [];
function gtag(){{dataLayer.push(arguments);}}
gtag('js', new Date());
gtag('config', 'G-XXXXXXXXXX');
</script>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title} | PromptGuide</title>
<meta name="description" content="{meta_description}">
<link rel="stylesheet" href="/prompt-guide/style.css">
</head>
<body>
<nav><a href="/prompt-guide/" class="logo">PromptGuide</a><a href="/prompt-guide/categories.html">All Prompts</a></nav>
<main><article>
<h1>{title}</h1>
<p class="subtitle">{subtitle}</p>
<div class="prompt-box"><div class="prompt-header"><span>The Prompt</span><button onclick="copyPrompt(this)">Copy</button></div>
<pre class="prompt-text">{prompt}</pre>
</div>
<section><h2>How to Use This Prompt</h2>{how_to_use}</section>
<section><h2>Example Output</h2><div class="example-box">{example_output}</div></section>
<section><h2>Tips to Get Better Results</h2><ul>{tips}</ul></section>
<section class="tools-section"><h2>Best AI Tools for This</h2>
<a href="https://chat.openai.com" target="_blank" rel="noopener">ChatGPT</a>
<a href="{amazon_link}" target="_blank" rel="noopener">{amazon_text}</a>
<a href="https://claude.ai" target="_blank" rel="noopener">Claude</a></section>
<section><h2>Related Prompts</h2><div class="related">{related}</div></section>
</article></main>
<footer>
<p>&copy; 2026 PromptGuide. AI prompts for every use case.</p>
<p style="margin-top:8px;">
<a href="/prompt-guide/about.html" style="color:#888;margin-right:16px;">About</a>
<a href="/prompt-guide/privacy.html" style="color:#888;margin-right:16px;">Privacy</a>
<a href="/prompt-guide/affiliate-disclosure.html" style="color:#888;">Affiliate Disclosure</a>
</p>
</footer>
<script>function copyPrompt(btn){{const text=btn.parentElement.nextElementSibling.textContent;navigator.clipboard.writeText(text).then(()=>{{btn.textContent='Copied!';setTimeout(()=>btn.textContent='Copy',2000)}});}}</script>
</body></html>
'''

def make_page(slug, title, subtitle, prompt, how_to_use, example_output, tips, amazon_keywords, amazon_text, related):
    """Create a prompt page file."""
    amazon_link = f"https://www.amazon.com/gp/search?ie=UTF8&tag=promptguide-20&linkCode=ur2&camp=1789&creative=9325&keywords={amazon_keywords}"
    meta_description = subtitle[:160]
    related_html = "".join(f'<a href="/prompt-guide/prompts/{r[0]}.html">{r[1]}</a>' for r in related)
    how_to_use_html = "<ol>" + "".join(f"<li>{step}</li>" for step in how_to_use) + "</ol>"
    tips_html = "".join(f"<li>{tip}</li>" for tip in tips)

    content = TEMPLATE.format(
        title=title,
        meta_description=meta_description,
        subtitle=subtitle,
        prompt=prompt,
        how_to_use=how_to_use_html,
        example_output=example_output,
        tips=tips_html,
        amazon_link=amazon_link,
        amazon_text=amazon_text,
        related=related_html,
    )

    path = f"prompts/{slug}.html"
    with open(path, 'w') as f:
        f.write(content)
    return path
