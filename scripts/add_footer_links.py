#!/usr/bin/env python3
"""Add FAQ + Resources links to the standard footer across all pages."""
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

OLD = '<a href="/terms.html" style="color:#999;margin-right:16px;">Terms</a>\n<a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>'

NEW = '<a href="/terms.html" style="color:#999;margin-right:16px;">Terms</a>\n<a href="/faq.html" style="color:#999;margin-right:16px;">FAQ</a>\n<a href="/resources.html" style="color:#999;margin-right:16px;">Resources</a>\n<a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>'

ALSO_OLD = '<a href="/terms.html" style="color:#999;margin-right:16px;">Terms</a>\n    <a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>'
ALSO_NEW = '<a href="/terms.html" style="color:#999;margin-right:16px;">Terms</a>\n    <a href="/faq.html" style="color:#999;margin-right:16px;">FAQ</a>\n    <a href="/resources.html" style="color:#999;margin-right:16px;">Resources</a>\n    <a href="/affiliate-disclosure.html" style="color:#999;">Affiliate Disclosure</a>'

updated = 0
skipped = 0
for html in REPO.rglob("*.html"):
    if "/notion/" in str(html) or "/research/" in str(html):
        continue
    text = html.read_text()
    if "/faq.html" in text and "/resources.html" in text:
        skipped += 1
        continue
    new_text = text
    if OLD in new_text:
        new_text = new_text.replace(OLD, NEW)
    elif ALSO_OLD in new_text:
        new_text = new_text.replace(ALSO_OLD, ALSO_NEW)
    if new_text != text:
        html.write_text(new_text)
        updated += 1
print(f"Updated: {updated} files. Skipped (already had links): {skipped}")
