# Launch Punchlist — Job Hunter's AI Bundle (May 17, 2026)

**Branch**: `launch-prep` (not pushed; review and merge when ready)
**Days to launch**: 14 (today is May 3, 2026)
**Status**: all autonomous prep work shipped. The remaining items below need a human at a keyboard — Notion login, Canva, ConvertKit dashboard, Gumroad dashboard. Each one has paste-ready copy in the files referenced.

---

## ✅ Done autonomously (this session)

| Deliverable | File | Notes |
|---|---|---|
| Gumroad listing copy | [GUMROAD_LISTING.md](GUMROAD_LISTING.md) | 14 fields, mapped to Gumroad's product-editor form. Paste-and-click. |
| ConvertKit pre-launch sequence | [EMAIL_SEQUENCE.md](EMAIL_SEQUENCE.md) | 4 broadcasts (announce / tease / launch-eve / launch-day) + optional reminder. Subjects, preview text, bodies all paste-ready. |
| Pinterest pin batch | [PINTEREST_PINS.md](PINTEREST_PINS.md) | 10 pin specs + Pinterest descriptions + alt text + drip schedule. Built to match existing `pins/pin-01-resume.png` aesthetic. |
| PDF build | [product/build/output/job-hunters-bundle.pdf](product/build/output/job-hunters-bundle.pdf) | Built clean from `product/build/build.sh full`. 119 pages, 514 KB, A4. No errors. |
| Homepage launch banner | [index.html](index.html) | Top-of-page banner teasing May 17 launch. Currently anchors to the email-capture section; HTML comment marks the line to swap to the live Gumroad URL on launch day. |
| Homepage email capture | [index.html](index.html) + [style.css](style.css) | Plain HTML form posting to ConvertKit form UID `d02eb77674`. Stacks cleanly on mobile (375px verified). |
| Launch-prep branch | git `launch-prep` | Two commits: one for paste-ready docs, one for site polish. Not pushed, not merged. |

**Voice/tone of all written deliverables** matches the existing snipprompts.com site voice — direct, lowercase-y, no fluff, specific numbers. Don't soften it on the way through.

---

## 🟡 Needs you at a keyboard (paste-and-click ops, all copy/specs ready)

These can't run autonomously because they require login to your accounts or graphic-design tools. Each one references the file with paste-ready content.

### 1. Build the Gumroad cover image (60 min)
- **Spec**: `product/job-hunter-bundle-outline.md` Section 6 (also recapped in `GUMROAD_LISTING.md` Field 7).
- **Tool**: Canva. 1200×1600, navy + cream, serif display headline, 5 module chips. No people, no checkmarks.
- **Save to**: `product/cover-1200x1600.png` and commit on `launch-prep` branch.
- **Why I couldn't do it**: graphic design needs visual judgment + Canva account access.

### 2. Build the Notion bonus workspace (2–4 hr)
- **Structure**: `product/job-hunter-bundle-outline.md` Section 4 (left sidebar, nested toggles, every prompt in a code block with copy button).
- **Content source**: paste from `product/module-01-resume.md` through `module-05-salary-negotiation.md` (each module already has every prompt formatted in a code block — Notion respects fenced code blocks on import).
- **Publishing**: Share → Publish → "Allow duplicate as template" → copy URL.
- **What to do with the URL**: paste it into two places — receipt email body in `GUMROAD_LISTING.md` Field 12 (replace `NOTION_DUPLICATION_URL`), and replace `[Access the Notion bundle →]` in the body.
- **Also**: save the URL in a one-line text file at `product/build/output/job-hunters-bundle-notion-link.txt`. Upload to Gumroad as the second product file.
- **Why I couldn't do it**: Notion has no programmatic page-builder API for this kind of content layout, and even if I could draft the markdown, your Notion login is needed to publish.

### 3. Build the 10 Pinterest pins in Canva (90 min total — drip across May 4–17)
- **Spec**: `PINTEREST_PINS.md` (one block per pin — headline lines, color, sub-line, benefits, alt text, description, post date).
- **Production**: open `pins/pin-01-resume.png` in Canva → "Use as template" → swap text per spec. Don't rebuild from scratch; the existing design is the brand.
- **Export**: PNG, 1000×1500. Upload to Pinterest directly (not via Canva's share-to-Pinterest, so you control description and alt text fields).
- **Why I couldn't do it**: pin generation requires Canva and a graphic-design judgment call on each pin.

### 4. Schedule the four ConvertKit broadcasts (15 min)
- **Spec**: `EMAIL_SEQUENCE.md` — paste the subject, preview, and body into ConvertKit's broadcast composer.
- **Send dates** (all 9:00 AM ET except #3 which is 5:00 PM Saturday):
  - Email 1: May 3 (today) 9 AM ET
  - Email 2: May 12 9 AM ET
  - Email 3: May 16 5 PM ET
  - Email 4: May 17 9 AM ET (replace `[GUMROAD_URL]` placeholder before scheduling)
  - Email 5 (optional reminder): May 18 5 PM ET — only schedule if Email 4 metrics warrant
- **Tag setup**: create the 5 tags listed in `EMAIL_SEQUENCE.md` "ConvertKit setup checklist" before scheduling.
- **Why I couldn't do it**: ConvertKit dashboard login required.

### 5. Set up the Gumroad listing (May 5–6, ~60 min)
- **Spec**: `GUMROAD_LISTING.md` — every Gumroad field is a numbered block in that file, paste-ready.
- **Order to do it in**:
  1. Create draft product (don't publish yet — keeps URL warm and un-indexed).
  2. Paste fields 1–10 (name, slug, price, summary, description, CTA text, tags, categories, refund policy, files-to-upload).
  3. Upload `product/build/output/job-hunters-bundle.pdf` and the Notion-link `.txt` file.
  4. Upload the 1200×1600 cover image (from punchlist item 1).
  5. Configure the receipt email (Field 12 in the listing doc) — paste verbatim, replace `NOTION_DUPLICATION_URL`.
  6. Connect Gumroad → ConvertKit integration with tag `bundle-buyer-2026-may` (Field 14).
  7. Create the `LAUNCH` discount code (Field 11). Leave it **toggled OFF** until launch morning.
  8. Save as Draft. Don't publish yet.
- **Why I couldn't do it**: Gumroad dashboard login required.

### 6. Merge `launch-prep` to `main` to push the homepage changes live (5 min)
- **Why now**: the launch banner and email-capture form go live the moment they hit `main` (GitHub Pages auto-deploys). Merging today gives the site 14 days to capture subscribers before launch — the whole point of the announce email is to convert site visitors to email subscribers, and they can't subscribe if the form isn't live.
- **What to review first**:
  - `git diff main..launch-prep -- index.html style.css` — visual changes
  - `git diff main..launch-prep -- GUMROAD_LISTING.md EMAIL_SEQUENCE.md PINTEREST_PINS.md` — paste-ready docs (these are documentation-only; they don't ship to the site)
- **Suggested merge command** (don't run autonomously per the rules):
  ```
  git checkout main
  git merge launch-prep --no-ff -m "Launch-prep: bundle banner, ConvertKit form, and paste-ready Gumroad/email/pin copy for May 17"
  git push origin main
  ```
- **Why I couldn't do it**: pushing to `main` and pushing to remote both need explicit permission per the global rules in `~/.claude/CLAUDE.md`.

### 7. Launch day (May 17 morning, 30 min)
- Gumroad: toggle product **Published**, toggle `LAUNCH` discount **Active**.
- Test the live URL with `/LAUNCH` appended in a private window — confirm price shows $29.
- Email: replace `[GUMROAD_URL]` in Email 4, schedule send for 9 AM ET.
- Pin 15 (launch-day pin): post to Pinterest with the live Gumroad URL.
- Edit `index.html` line 51 — replace the launch-banner `href="#email-capture"` with the live Gumroad URL. Commit and push to `main`.
- Watch Gumroad sales notifications + ConvertKit reply inbox.

---

## 🟢 Open questions — Tom's calls (May 3)

Tom triaged the open questions in the May 3 review. Resolutions below.

### Q1 — Gumroad URL pattern → owner verifies pre-launch (~30 sec)
Owner action: log into Gumroad → top-right profile → "View profile" — the URL bar shows the storefront subdomain. If it isn't `snipprompts.gumroad.com`, find/replace the placeholder across `GUMROAD_LISTING.md` and `EMAIL_SEQUENCE.md` before scheduling Email 4 and posting Pin 15.

### Q2 — ConvertKit form endpoint → owner verifies post-merge ($0 test signup, ~30 sec)
Owner action: after merging `launch-prep` to `main`, open snipprompts.com in an incognito window and submit the homepage form with a real address. If you land on ConvertKit's thank-you page, the universal POST endpoint works. If you hit a 404, swap the `<form>` block for the JS embed snippet from ConvertKit's dashboard (same form UID `d02eb77674`, different markup).

### Q3 — PDF page size: A4 vs. Letter → ship A4
Tom's call: digital-first product, US buyers rarely print AI prompts, not worth a regenerate. Letter variant logged in v1.1 backlog (`notion/05-changelog.md`); add if any buyer asks.

### Q4 — Notion duplication URL → blocker, build before launch
Owner action (May 4–6 window): build the Notion workspace by importing `notion/*.md`, set up duplicate-as-template, grab the URL. Then find/replace the `NOTION_DUPLICATION_URL` placeholder in `GUMROAD_LISTING.md` Field 12 and `DELIVERY_EMAIL.md` (HTML body + plain-text fallback — two replacements).

### Q5 — Day-5 comp-prompt promise → REMOVED from delivery email (May 3)
Tom's call: the Day-5 post-launch window is the chaos window — funnel debugging if sales are slow, support if sales are good, neither leaves room to write a new prompt. Removed the promise from `DELIVERY_EMAIL.md` (HTML body, plain-text fallback, setup notes warning, voice/craft notes — four locations). Comp triangulator prompt logged in v1.1 backlog (`notion/05-changelog.md`); ship as a separate broadcast post-launch if-and-when, not as a launch-day commitment.

### Q6 — Author identity on commits (deferred)
Optional cosmetic fix; commits are functional as-is. Run `git config --global user.email/.name` whenever convenient.

---

## What I deliberately did NOT touch

- **Existing prompt pages** (`prompts/*.html`): no edits. Out of scope for launch prep, and any change risks breaking the page-template Python generators in `scripts/`.
- **Existing pins** (`pins/pin-0[1-5]-*.png`): no edits. They're live and already pinned.
- **`prompts/` content**: no new prompts. Phase 2 content is paused per `README.md` — wait for Search Console signal.
- **`tracking/`**: no edits.
- **Anything on `main`**: no commits, no pushes, no merges. All work is on `launch-prep`.

---

## Recommended order over the next 14 days

| Day | Action |
|---|---|
| **May 3 (today)** | Merge `launch-prep` → `main` (item 6) so the banner + form go live. Schedule Email 1 to send 9 AM today (item 4). |
| **May 4** | Build Pin 6 in Canva, post to Pinterest. |
| **May 5–6** | Build Gumroad cover image (item 1). Set up Gumroad draft listing (item 5). Build Pins 7–8. |
| **May 7–9** | Build Notion workspace (item 2). Build Pins 9–11. |
| **May 11** | Build/post Pin 12. |
| **May 12** | Email 2 sends automatically (already scheduled). Build/post Pin 13. |
| **May 13–15** | Build/post Pins 13, 14. Final QA on Gumroad listing draft. |
| **May 16** | Email 3 sends automatically. Build/post Pin 14 if not already. |
| **May 17** | Launch day execution (item 7). |

Doing it in this order gives you ~3 days of slack — most things ship on day 1 or 2 of their window.
