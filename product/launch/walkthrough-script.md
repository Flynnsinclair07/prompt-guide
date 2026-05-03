# Buyer Walkthrough Script — May 9 + May 14

This is the test-purchase script Tom runs to validate the buyer flow end-to-end.
Run it twice: May 9 (first walkthrough) + May 14 (final dress rehearsal).
Findings from May 9 → fix on May 10. Findings from May 14 → fix on May 15.

---

## Setup before running

1. Open these tabs in order:
   - Gumroad listing URL (the public-facing product page, not the editor)
   - Email inbox (the address you'll "buy" with — use a different email than the Gumroad seller account)
   - Empty new tab

2. Have a phone nearby for the mobile-test checks.

3. Set timer / note start time. The whole walkthrough should take 15–25 min.

---

## Phase 1 — Discovery (do you find the listing organically)

**Step 1.1** — Open the Pinterest "AI Prompts for Job Seekers" board.
- [ ] Bundle pins are visible
- [ ] Click on Pin 1. Does it open the right listing?
- [ ] Pin description matches what's on Gumroad

**Step 1.2** — Search Pinterest for "ChatGPT prompts resume."
- [ ] Bundle pins appear in search results (may take days post-launch for indexing)

**Step 1.3** — From the Gumroad listing page, scroll through everything a buyer would see:
- [ ] Product title is clear
- [ ] Price ($39) is visible
- [ ] Description reads cleanly (no broken markdown, no HTML showing)
- [ ] All 5 preview images load
- [ ] Cover image is set
- [ ] FAQ section is present and reads well
- [ ] "Buy" button is prominent
- [ ] Refund policy is mentioned

**Step 1.4** — Mobile check: open the same Gumroad URL on your phone.
- [ ] Listing renders correctly on mobile
- [ ] Preview images don't get cut off
- [ ] "Buy" button is tappable (not too small)

---

## Phase 2 — Purchase (the actual transaction)

**Step 2.1** — Click "Buy" or "I want this."
- [ ] Checkout flow loads quickly
- [ ] Price displayed matches listing

**Step 2.2** — Enter test email address (different from seller account).
- [ ] Email field accepts input

**Step 2.3** — Complete payment:
- **For May 9 (first walkthrough)**: use Gumroad's test mode if available, OR use a real card and refund yourself after
- **For May 14 (final walkthrough)**: real card, real purchase, real refund after

- [ ] Payment processes within 10 seconds
- [ ] Success confirmation page appears
- [ ] Confirmation page shows the bundle name + access instructions

---

## Phase 3 — Delivery (the email + access)

**Step 3.1** — Check inbox for delivery email.
- [ ] Email arrives within 60 seconds
- [ ] Email subject line is correct (`Your Job Hunter's Bundle is ready`)
- [ ] Email sender shows your name / brand (not "noreply@gumroad")
- [ ] Email body matches `gumroad-listing.md` welcome message
- [ ] All links in email work
- [ ] PDF download link in email works

**Step 3.2** — Click the PDF download link.
- [ ] PDF downloads (not opens in browser, unless that's the desired behavior)
- [ ] PDF filename is `job-hunters-bundle.pdf` (clean, no weird chars)
- [ ] PDF opens in default app
- [ ] PDF page count matches expected (119 pages)

**Step 3.3** — Find the Notion workspace link in delivery email or product page.
- [ ] Link is clickable
- [ ] Link opens to a Notion page
- [ ] Page is readable WITHOUT logging into Notion (incognito browser test)
- [ ] All 14 sub-pages are visible in the workspace
- [ ] BATNA worksheet renders as interactive
- [ ] Comp research table renders
- [ ] Walkaway math formulas calculate correctly when you fill values

**Step 3.4** — Open the Gumroad library page (the buyer's persistent access).
- [ ] Bundle appears in library
- [ ] Can re-download PDF anytime
- [ ] Notion link is accessible from library page too

---

## Phase 4 — Use (does it actually work for a buyer)

**Step 4.1** — Pretend you're a real buyer trying to use a prompt for the first time.
- Open the PDF
- Find M1 P1 (Resume from scratch)
- Copy the prompt block (everything between the ``` marks)
- Paste into ChatGPT free tier
- Fill in the bracketed inputs with fake but plausible data
- Submit

- [ ] ChatGPT processes the prompt without errors
- [ ] Output looks reasonable (resume-shaped, structured, no AI-tells from banned-phrase list)
- [ ] If you left an input vague, the pre-output gate triggers (asks clarifying questions)

**Step 4.2** — Repeat with a Notion script.
- Open the Notion workspace
- Find Script 3 ("We don't have budget" rebuttal)
- Read it as a buyer would
- Could you actually use this in a phone call? Is the language natural?

- [ ] Script reads as usable, not stilted
- [ ] No formatting issues that would break the copy-paste

**Step 4.3** — Try one worksheet end-to-end.
- Open Worksheet 3 (Walkaway math)
- Fill in fake offer values for all sections
- Verify it computes a total comparable comp number

- [ ] Worksheet is fillable
- [ ] Math works (if implemented as Notion formula)
- [ ] You'd actually use this on your next offer

---

## Phase 5 — Refund (the safety valve)

**Step 5.1** — Reply to the delivery email asking for a refund.
- [ ] Email reaches you (the seller)
- [ ] You can refund through Gumroad dashboard within 60 seconds
- [ ] Refund email confirmation arrives

(For May 9: refund yourself. For May 14: also refund yourself, then re-purchase if you want to keep the test record.)

---

## Findings template

For each break or friction found, log:

```
[SEVERITY] — [WHERE] — [WHAT]

Severity: 🔴 Critical | 🟠 High | 🟡 Medium | 🟢 Low
Where: Phase + Step (e.g., "Phase 3, Step 3.2")
What: 1-2 sentence description
Suggested fix: (worker fills in)
```

Send all findings to worker as a single message — worker batches fixes.

---

## Pass threshold

- **0 🔴 critical issues = greenlight launch**
- **Any 🔴 issue = fix before next walkthrough or launch**
- **🟠 high issues = fix before launch**
- **🟡 medium = ship, fix post-launch**
- **🟢 low = v2 backlog**
