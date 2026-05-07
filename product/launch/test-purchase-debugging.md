# Test-purchase debugging guide

For owner's May 9 walkthrough (and again May 14 final dry-run, per `sprint-plan-may-4-17.md`). If something breaks during the test purchase, find the symptom below and follow the fix. Don't burn 20 minutes Googling — every failure mode here has been anticipated.

**Test-purchase setup** (per `day-1-launch-checklist.md` item 9): create a 100% Gumroad discount code (e.g., `TEST100`), 1 use, then buy the bundle from yourself in an incognito window using a real personal email you control. After the test, refund and disable the code.

---

## Failure mode 1 — Gumroad publish fails ("Connect a payment method" or "Account in review")

**Symptom**: clicking "Publish" on the Gumroad listing returns an error like "Connect a payment method to publish" or "Your account is under review." The listing stays in Draft state.

**Likely cause**: Gumroad payouts not configured (Stripe Connect not finished), OR account flagged for ID verification.

**Fix**:
1. Gumroad → Settings → Payments — verify Stripe Connect shows "Active" (not "Pending" or "Action required").
2. If Stripe shows **Pending verification**: check email for a Stripe message asking for ID/business docs. Submit; verification takes 1–24 hours. **Do not wait silently** — Stripe sometimes drops the verification email; if no reply within 6 hours, log into Stripe directly (dashboard.stripe.com) and complete the prompted steps.
3. If Stripe shows **Awaiting micro-deposits** (US bank verification): two small deposits ($0.01–$0.99) hit your linked bank within 1–2 business days. You enter the amounts in Stripe to verify. Until then, you can't publish. **For launch**: only relevant if you switched payout banks recently. If you're already through this from a prior product, skip.
4. If Gumroad shows **Account in review**: check the email Gumroad sent at signup, reply to support@gumroad.com with what you sell. Usually 1–3 business days.

**Severity**: 🔴 **ship-blocking** if Stripe isn't Active by May 16 evening. **Action now**: verify Stripe Connect status today (May 6). If pending, that's your highest-priority blocker — everything else waits on this.

---

## Failure mode 2 — Receipt email doesn't arrive within 5 minutes

**Symptom**: test purchase completes (Gumroad shows "Sale received"), but the receipt email isn't in your inbox after 5 minutes.

**Likely cause** (most → least common):
1. **In Promotions / spam tab** — Option A's `noreply@customers.gumroad.com` lands there frequently
2. **ConvertKit Sequence not triggered** (Option B only) — Gumroad → ConvertKit integration silent failure
3. **Receipt email disabled in Gumroad** — Workflows tab toggle off
4. **Your inbox provider rate-limiting** — Gmail, Outlook sometimes delay first emails from new senders

**Fix**:
1. **Check Promotions / spam** — Gmail's Promotions tab is the #1 cause. Search inbox + all-mail for "Gumroad" or "bundle" — if found in Promotions, mark "Move to Primary."
2. **Verify Gumroad sent the email**: Gumroad → Sales → click the test sale → scroll to "Email status." If shows "Sent" — it's a delivery issue (your end). If shows "Pending" or "Failed" — Gumroad's end.
3. **If Option B (ConvertKit)**: ConvertKit → Subscribers → search for the test email. If subscriber doesn't exist with `bundle-buyer-2026-may` tag, the integration silently failed. Re-auth in Gumroad → Settings → Integrations → ConvertKit → reconnect.
4. **If receipt email toggle is off**: Gumroad → Products → Job Hunter's AI Bundle → Workflows tab → Receipt email — verify "Send to buyers" is ON.
5. **Test from a different inbox**: if your primary inbox is Gmail, also test from a Yahoo / iCloud / Outlook address. If the email arrives there but not Gmail, you have a Gmail-specific deliverability problem — log it for Option B switch (the Day-2 fix).

**Severity**: 🔴 **ship-blocking** if no receipt arrives at all (Gumroad-side failure). 🟠 **can-launch-with** if it arrives in Promotions consistently — `support-templates.md` Template 2 catches the resulting buyer questions.

---

## Failure mode 3 — PDF download is the wrong version

**Symptom**: download from Gumroad library shows old "Scripts (Batch 2)" header, or 141 pages instead of 119, or other artifacts the May 3 PDF QA pass already fixed.

**Likely cause**: Gumroad's CDN cached the original upload; new upload didn't replace cleanly.

**Fix**:
1. **Verify the file you uploaded matches the latest commit**: in your local repo, run:
   ```
   shasum -a 256 product/build/output/job-hunters-bundle.pdf
   ```
   Note the hash. Compare to the file you downloaded from Gumroad — same command on the downloaded file.
2. **If hashes don't match**: Gumroad is serving an old version. Re-upload:
   - Gumroad → Products → Job Hunter's AI Bundle → Edit → Files → delete the old PDF → upload the fresh one from `product/build/output/job-hunters-bundle.pdf`.
   - **Wait 2–5 minutes** for Gumroad's CDN to flush. Re-test the download in incognito.
3. **If hashes match but content looks wrong**: you may have built the PDF from a stale source. Re-run `cd product/build && ./build.sh full`, verify pdfinfo shows 119 pages, then re-upload.
4. **Don't trust browser cache**: always test downloads in an incognito window or a different browser. Chrome aggressively caches downloads, especially on slow networks.

**Severity**: 🔴 **ship-blocking** if buyers receive a PDF with the "Scripts (Batch 2)" artifact or other May-3-fix-state artifacts — the structural issue PDF_QA_REPORT documented as "would read as draft / pirated". 🟠 if mismatch is cosmetic (e.g., minor formatting differences from a stale build).

---

## Failure mode 4 — Notion link in the .txt file is the placeholder

**Symptom**: open `job-hunters-bundle-notion-link.txt` from the Gumroad download (the second file per Field 8). Contents are literal `NOTION_DUPLICATION_URL` (placeholder) instead of the actual Notion URL.

**Likely cause**: when uploading the .txt to Gumroad, owner used the source-file template version that still had the placeholder, instead of replacing with the live URL first.

**Fix**:
1. Open `job-hunters-bundle-notion-link.txt` locally — verify the contents.
2. If still placeholder, replace with:
   ```
   https://learned-guilty-545.notion.site/The-Job-Hunter-s-AI-Bundle-35634cf5abb9800babe5c22b28888ccf
   ```
3. Save, then re-upload to Gumroad → Products → Files. Delete old .txt, upload new.
4. **Cross-check**: the same URL must also be replaced in `DELIVERY_EMAIL.md` body (line ~58 + ~131) and pasted into Gumroad's receipt-email body OR the ConvertKit sequence body (depending on Option A vs B). The verification scan in `VERIFICATION_PASS_2026-05-06.md` confirmed these 3 spots have the real URL — verify yours match.

**Severity**: 🔴 **ship-blocking** if owner uploads the placeholder version — buyers can't access the Notion workspace and the receipt email's claim is broken. 5-min recovery once spotted.

---

## Failure mode 5 — Notion duplicate fails ("Requires paid plan")

**Symptom**: click the Notion duplication URL in incognito, hit "Duplicate" top-right, Notion prompts "This requires a paid plan to duplicate" or similar.

**Likely cause**: the master Notion workspace is in a Team plan (paid). Duplicating from Team plans requires the duplicating user to be invited to the Team. The fix is to host the master in a personal workspace OR adjust share settings.

**Fix**:
1. Open the master Notion workspace (the one you control).
2. Top-right "Share" → verify settings:
   - **Share to web**: ON
   - **Allow duplicate as template**: ON
   - **Allow editing**: OFF (critical — without this, the buyer's edits would write back to your master)
   - **Allow comments**: OFF
3. If "Allow duplicate as template" is grayed out: your workspace is in a plan that doesn't support template-duplication. Solutions:
   - Move the workspace to a personal (free-tier) Notion workspace — drag the parent page in the sidebar to "Private" workspace.
   - Re-publish from the personal workspace, get the new URL, update `DELIVERY_EMAIL.md` line ~58 + ~131, and re-upload `job-hunters-bundle-notion-link.txt`.
4. **Test in incognito** after change — confirm Duplicate button works without prompting for paid plan.

**Severity**: 🔴 **ship-blocking** if buyers can't duplicate — the Notion workspace is sold as a bundle benefit. ~10 min recovery if it's a settings issue; ~30 min if requires moving the workspace between Notion accounts.

---

## Failure mode 6 — Welcome message subject is wrong

**Symptom**: receipt email arrives, but subject says something other than the configured Subject A ("Your Job Hunter's AI Bundle is here") — possibly Gumroad's default subject ("Receipt from [Your Storefront]") or an old Subject B/C variant.

**Likely cause**: confusion between Gumroad's two email-customization surfaces:
- **Workflows tab** → **Receipt email** — what most people configure (matches `DELIVERY_EMAIL.md` Option A path)
- **Product → Email tab** → an older/legacy subject field that overrides Workflows

**Fix**:
1. Gumroad → Products → Job Hunter's AI Bundle → **Workflows** tab → Receipt email.
2. Verify Subject field reads exactly: `Your Job Hunter's AI Bundle is here` (no quotes, no extra spaces).
3. If Workflows looks correct but emails still arrive with wrong subject: Gumroad → Product → **Email** tab (older surface). Some accounts have a legacy "Send a custom message" toggle there. If present, ensure it's OFF or matches Workflows exactly.
4. **A/B/C testing**: if testing variants, verify only ONE is active in Workflows. Gumroad doesn't natively split-test subject lines — you have to manually rotate or use ConvertKit (Option B).

**Severity**: 🟠 **can-launch-with** — buyers still receive the email, just with a less-optimized subject. Cosmetic compared to delivery failures. Fix when spotted; don't block launch over it.

---

## Failure mode 7 — Discount code LAUNCH doesn't activate (or activates wrong)

**Symptom**: at 9 AM ET on May 17, you toggle `LAUNCH` to active in Gumroad → Discounts. Test the URL `[your-storefront]/l/job-hunters-ai-bundle/LAUNCH` in incognito — price still shows $39 (not $29). OR the discount activates but the code limits don't match the spec.

**Likely cause** (most → least common):
1. **Time zone confusion** — Gumroad uses UTC for discount-window dates. May 19 23:59 UTC is May 19 7:59 PM ET (not midnight ET). Easy to set the wrong end-time.
2. **Code is product-specific but typo'd as universal** (or vice versa) — Gumroad has two scopes: applies to specific product, or to all products in account.
3. **URL pattern wrong** — `/LAUNCH` URL trick only works on certain Gumroad URL formats. If your storefront URL is different from `gumroad.com/l/...`, the URL pattern may not auto-apply.
4. **Code requires manual entry** — if "Apply via URL" isn't toggled, buyers must paste the code at checkout instead of getting auto-applied.

**Fix**:
1. **Verify code config** in Gumroad → Discounts → LAUNCH → Edit:
   - Code: `LAUNCH` (uppercase, no spaces)
   - Discount: $10 off (NOT percentage — fixed dollar amount)
   - Valid: from May 17 9:00 AM ET to May 19 9:00 AM ET (which is **May 17 13:00 UTC to May 19 13:00 UTC** in Gumroad's UTC display)
   - Limit: 100 uses OR May 19 — toggle whichever expires first
   - Applies to: Job Hunter's AI Bundle (product-specific, NOT all products)
   - **Toggle "Allow URL parameter"** — without this, /LAUNCH URL won't auto-apply
2. **Test in incognito** with `[your-storefront]/l/job-hunters-ai-bundle/LAUNCH`. Price should show **$29** at the top of the listing, not $39.
3. **Time-zone sanity check**: open Gumroad → Discounts → LAUNCH. The "Valid from / Valid to" times in Gumroad's UI display in UTC by default. Confirm:
   - Valid from: 2026-05-17 13:00 UTC (= May 17 9:00 AM ET)
   - Valid to: 2026-05-19 13:00 UTC (= May 19 9:00 AM ET)
4. **If still showing $39**: clear Gumroad's CDN cache by editing-and-re-saving the discount code (any field) — sometimes triggers a CDN flush.

**Severity**: 🔴 **ship-blocking** on launch morning — if the code doesn't activate, the entire Email 4 send is undermined (the email promises $29 via /LAUNCH URL). Test the URL at 8:30 AM ET May 17 with the code toggled active, before Email 4 sends at 9:00 AM.

**For test purchase** (May 9): create a separate code `TEST100` (100% off, 1 use) and use that — don't test against `LAUNCH` itself, you'll burn one of the 100 uses and confuse the launch-window analytics.

---

## Failure mode 8 — Refund doesn't process

**Symptom**: in test purchase, click Gumroad → Sales → find your test sale → Refund. Either button is grayed out, or click returns an error.

**Likely cause** (most → least common):
1. **Payout cycle hasn't run** — Gumroad batches payouts; if the sale hasn't been paid out yet (typically 24–72h after sale), refund is instant. If it has been paid out, Gumroad may need to deduct from your next payout.
2. **Payment method on file expired** — Gumroad refunds to the card the buyer used. If the buyer's card on Gumroad's records expired or was reported lost, the refund fails.
3. **Refunding a $0 test purchase** — Gumroad sometimes refuses $0 refunds because there's nothing to reverse. Use the "Mark as refunded" override.
4. **Account suspension** — if Gumroad has flagged your account, refund actions get held.

**Fix**:
1. **For $0 test purchase**: Gumroad → Sales → click test sale → "More actions" → "Mark as refunded" (cosmetic only — no money was charged). This is the typical path for the May 9 walkthrough.
2. **For paid sale**: Gumroad → Sales → Refund button — clicks succeed if payment is still in escrow. If "Refund failed: Cannot refund a payout-completed sale" — file a refund-from-balance: Gumroad → Settings → Refund from balance → enter the amount. Refund processes within 5 business days.
3. **For expired card**: Gumroad will flag this with "Refund failed: Buyer card invalid." Reply to buyer (use `support-templates.md` Template 1) explaining the situation, ask if they have an alternate refund route (PayPal, etc.). Most buyers accept a Gumroad credit instead.
4. **Document refund pattern**: per `post-launch-week-1-plan.md`, log every refund + reason in `product/launch/refund-log-2026-05.md`. If refunds cluster on one of the failure modes above, it's a v1.1 fix candidate.

**Severity**: 🟠 **can-launch-with** — refund failures are buyer-by-buyer, not launch-blocking. The 30-day refund window gives owner time to handle edge cases. But if refund fails consistently in test purchase, fix before launch (it'll fail under load too).

---

## What this debugging guide deliberately does NOT cover

- **Stripe-specific dashboard issues** — those are Stripe's UI, not Gumroad's. If Stripe blocks payouts entirely (rare), escalate via Stripe Support directly; Gumroad's support can't fix Stripe's account holds.
- **Gumroad outages** — if Gumroad itself is down (status.gumroad.com), nothing in this guide helps. Wait it out, communicate via Pinterest pin description or Twitter.
- **Email deliverability tuning** (SPF/DKIM/DMARC) — too deep for a debugging guide. If Option A's noreply consistently lands in spam, switch to Option B (ConvertKit) which uses your verified domain.
- **Notion API automation** — owner doesn't need this for v1. If post-launch you want to programmatically update the Notion workspace, that's a v1.1 question.

---

## Pre-walkthrough checklist (run before May 9 test purchase)

5-min sanity check before clicking "Buy" on the test purchase, so you don't burn the test on an obvious config issue:

- [ ] Gumroad Stripe Connect status: **Active** (not Pending) — Failure mode 1
- [ ] PDF in Gumroad library matches the SHA256 of `product/build/output/job-hunters-bundle.pdf` — Failure mode 3
- [ ] Notion .txt file contains the live URL (not `NOTION_DUPLICATION_URL` placeholder) — Failure mode 4
- [ ] Notion duplication URL works in incognito (test the duplicate flow without completing it) — Failure mode 5
- [ ] Workflows → Receipt email subject matches `Your Job Hunter's AI Bundle is here` — Failure mode 6
- [ ] LAUNCH discount config matches spec (UTC times, $10 off, product-specific, URL-parameter ON) — Failure mode 7
- [ ] `TEST100` discount code created (100% off, 1 use) for the actual test purchase — debugging-guide setup

If any of these is unchecked, fix that first; don't run the test purchase against a known-broken config — the test won't tell you what you don't already know.

---

## After the walkthrough

If everything passes May 9: log results in `tracking/daily-metrics-template.csv` notes column ("walkthrough 1 passed clean") and proceed to the May 14 walkthrough on schedule.

If anything fails: fix the failure, re-run the failed step, log the issue + fix in this file (under the appropriate failure mode) so May 14 walkthrough gets the benefit. Don't proceed to launch with a known-broken step.

If May 14 walkthrough fails on the same issue May 9 surfaced: that's a launch-blocking situation — escalate to a focused fix block before May 16 evening pre-flight.
