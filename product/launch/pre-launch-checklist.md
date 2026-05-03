# Pre-Launch Checklist — Run May 15

**Pass threshold: every item checked. Any unchecked item = launch blocked.**

---

## PDF
- [ ] `product/build/output/job-hunters-bundle.pdf` exists and is 119 pages
- [ ] PDF opens without errors in Preview
- [ ] PDF opens without errors in Adobe Acrobat (test cross-reader compatibility)
- [ ] PDF opens without errors on iPhone (test mobile reading)
- [ ] All emojis render (🟢🟡🟠🔴 on M3 P12 page) — check at 100% zoom
- [ ] All checkmarks render (✓ ✗ on M1 P4 page)
- [ ] All arrows render (→ in TOC, in M1 P8 title)
- [ ] No blank pages anywhere (programmatic check: `for i in $(seq 1 119); do txt=$(pdftotext -f $i -l $i job-hunters-bundle.pdf - | tr -d '[:space:]'); [ ${#txt} -lt 50 ] && [ -n "$txt" ] && echo "blank: p$i"; done`)
- [ ] No en-dash corruption (programmatic check: `pdftotext job-hunters-bundle.pdf - | grep -E '–[0-9]{2}'` should return only legitimate uses like "2023–2025", not "–23")
- [ ] PDF size under 10MB (currently 514KB — easy)
- [ ] Filename matches what Gumroad delivers: `job-hunters-bundle.pdf`

## Notion workspace
- [ ] All 14 pages exist (8 scripts + 3 worksheets + M3 answer-scoring + M3 rehearsal + M4 checklist + M4 weekly content pack)
- [ ] Top-level page set to "Anyone with link can view" (read-only)
- [ ] Share URL copied
- [ ] Share URL works in incognito browser (no Notion login required)
- [ ] BATNA worksheet renders as interactive Notion database
- [ ] Comp research table works as Notion database with table view
- [ ] Walkaway math has formula fields that auto-calculate total comparable comp

## Gumroad listing
- [ ] Listing is published (not draft)
- [ ] Price set to $39
- [ ] PDF uploaded as primary file
- [ ] Notion workspace URL pasted in "additional content" field
- [ ] Listing description matches `gumroad-listing.md` Description field
- [ ] FAQ entries match `gumroad-listing.md` FAQ entries
- [ ] All 5 preview images uploaded
- [ ] Cover image set
- [ ] Tags added: `job search, resume, salary negotiation, AI prompts, career`
- [ ] Refund policy set to 30-day no-questions
- [ ] Welcome message matches `gumroad-listing.md` delivery email body
- [ ] Welcome message has correct Notion link
- [ ] Test purchase URL: paste into incognito browser, complete purchase (or test mode), confirm:
  - [ ] PDF downloads correctly
  - [ ] Notion link in delivery email works
  - [ ] Welcome email arrives within 60 seconds
  - [ ] Library page shows the bundle correctly

## ConvertKit broadcast
- [ ] Broadcast created with subject line + body from `convertkit-broadcast.md`
- [ ] Gumroad URL inserted (replaced the placeholder)
- [ ] Send time scheduled: May 17, 9:00 AM your timezone
- [ ] Subscriber list selected (verify count)
- [ ] Test send to your own email — render check, all links work
- [ ] No typos in subject line (most-checked, most-broken element)

## Pinterest
- [ ] All 10 pins created with copy from `pinterest-pins.md`
- [ ] Each pin has 1000x1500 image (or 2:3 ratio)
- [ ] Each pin links to Gumroad URL
- [ ] All pins on "AI Prompts for Job Seekers" board
- [ ] Launch pin (Pin 10) scheduled for May 17 morning OR pinned-to-top May 17

## Tracking / monitoring
- [ ] Gumroad dashboard tab open in browser May 17 morning
- [ ] ConvertKit dashboard tab open in browser May 17 morning
- [ ] Email notifications enabled for new Gumroad purchases
- [ ] Set 3 check-in times for May 17: noon, 6pm, midnight (don't refresh constantly)

## Mental / logistics
- [ ] May 16 = full rest day (NON-NEGOTIABLE)
- [ ] May 17 morning: clear calendar, eat breakfast, no meetings
- [ ] Have refund SOP ready: "Reply, ask why if it would help v2, refund within 24 hours"
- [ ] First-sale celebration plan (this matters for morale)

---

## Launch-blocker definitions

**🔴 Critical (don't launch without fix):**
- PDF won't open
- Gumroad delivery doesn't trigger email
- Notion link doesn't work
- ConvertKit broadcast doesn't render correctly

**🟠 High (launch but fix in 24 hours):**
- Pinterest pins missing or wrong link
- Cover image wrong
- Refund policy not clear in listing

**🟡 Medium (fix post-launch):**
- Typos in non-customer-facing copy
- Suboptimal subject line A/B
- Missing FAQ entries

---

## If launch breaks

1. **Don't panic.** Most launch breaks are fixable in <30 min.
2. **Identify the break:** PDF? Delivery? Email? Listing copy?
3. **Roll back if necessary:** Gumroad can unpublish a listing while you fix
4. **Communicate:** if you've sold something and there's a real break, email buyers proactively. "Hi — quick note: [issue], [what I'm doing], [ETA fix]" beats silence every time.
5. **Refund without question** if asked.
