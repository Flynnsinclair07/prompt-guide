# Launch Runbook — Job Hunter's Bundle

**Launch date: 2026-05-17 (LOCKED)**

This directory contains every text/file deliverable for the May 17 launch.
What's here = drafted by worker, ready for owner action.
What's NOT here = owner must execute manually (auth-gated).

---

## What's drafted (in this directory)

| File | Purpose | Owner action |
|------|---------|--------------|
| `notion-lite/*.md` | 14 ready-to-paste pages for Notion workspace | Create Notion workspace, paste each .md as a new page |
| `gumroad-listing.md` | Product listing copy, refund policy, FAQ, tags | Paste into Gumroad's "Edit product" form |
| `convertkit-broadcast.md` | Launch-day email broadcast | Paste into ConvertKit, schedule for May 17 |
| `pinterest-pins.md` | 10 pin copy variants for the launch pin pack | Create pins in Pinterest with these captions |
| `pre-launch-checklist.md` | May 15 go/no-go items | Walk through each item, check off |
| `walkthrough-script.md` | Buyer flow test script for May 9 & 14 | Boss/owner runs end-to-end purchase test |

---

## What's NOT drafted (auth-gated, owner must do)

### Notion (May 4)
1. Create new Notion workspace OR pick existing one
2. Create a top-level page: "Job Hunter's Bundle — Companion Workspace"
3. Inside, paste each `notion-lite/*.md` file as a new page (Notion auto-formats markdown)
4. For the 3 worksheet pages (BATNA, comp research, walkaway math): convert each to a Notion Database (instructions in each file's frontmatter)
5. Set sharing: "Anyone with link can view" (read-only)
6. Copy the share URL — needed for Gumroad delivery

### Gumroad (May 5–6)
1. Create Gumroad account if you don't have one (gumroad.com/signup)
2. New product → digital product → Job Hunter's Bundle
3. Upload `product/build/output/job-hunters-bundle.pdf`
4. Paste content from `gumroad-listing.md` (description, FAQ, tags)
5. Set price: $39
6. Set refund policy: 30-day no-questions
7. In delivery settings, paste the Notion share URL into the "additional content" field
8. Take 3-5 preview screenshots of the PDF (cover, sample prompt page, worksheet page, script page) — upload as preview images
9. Test purchase URL: should auto-deliver PDF + Notion link within 60 sec

### ConvertKit (May 11–17)
1. Log into ConvertKit
2. New broadcast → paste from `convertkit-broadcast.md`
3. Schedule send: May 17, 9am your time
4. Confirm subscriber list selected (currently 1 test subscriber)

### Pinterest (May 11–17)
1. Create 10 new pins using copy from `pinterest-pins.md`
2. Use the same preview screenshots as Gumroad for pin images
3. Pin to your "AI Prompts for Job Seekers" board
4. Schedule launch pin for May 17, 9am

### Buyer walkthroughs (May 9 + May 14)
- Boss Tom runs `walkthrough-script.md` end-to-end
- Flag every break, confusing handoff, or typo
- Worker fixes findings on May 10 + May 15

---

## Calendar mapping (Tom's plan)

| Date | Task | Status |
|------|------|--------|
| May 1 | Tooling install + smoke render + dingbat fix + wrap fix + full bundle render + M3 P12 emoji test | ✅ Complete |
| May 2 | Visual QA + fix critical issues (blank pages + en-dash) | ✅ Complete (commit `ccf3282`) |
| May 3 | Buffer / pulled forward to May 1 | Done early |
| May 4 | Notion Lite build | Drafts ready in `notion-lite/`, owner pastes |
| May 5 | Gumroad listing draft | Drafted in `gumroad-listing.md`, Tom QA |
| May 6 | Gumroad setup + delivery email wired | Owner action |
| May 7 | Buffer day | — |
| May 8 | Pre-walkthrough staging | Owner verifies |
| May 9 | First buyer walkthrough | Tom runs script |
| May 10 | Fix walkthrough findings | Worker action (after findings) |
| May 11 | Pinterest pins + ConvertKit broadcast prep | Drafted, owner uploads |
| May 12 | Tom QA on pins + broadcast | Tom |
| May 13 | Buffer day | — |
| May 14 | Second buyer walkthrough | Tom |
| May 15 | Final fixes + pre-launch checklist | Worker + owner |
| May 16 | Rest day (non-negotiable) | — |
| May 17 | LAUNCH | Owner clicks send |

---

## Decisions still needed from owner

1. **Gumroad vs ConvertKit for delivery email**: Gumroad has built-in delivery; ConvertKit gives more control but needs a Gumroad → ConvertKit Zapier hook. Recommend **Gumroad built-in** for simplicity at v1; ConvertKit for v2 if needed.
2. **Notion workspace name**: suggest "Job Hunter's Bundle — Companion Workspace" (matches Gumroad listing copy). Owner can pick differently.
3. **Refund window**: recommended 30-day no-questions in `gumroad-listing.md`. Owner can change.
4. **Pinterest pin schedule**: 1 pin/day Apr 28–May 17 OR all 10 pins May 17 morning? Recommend stagger (1/day) for steady traffic, plus the launch pin pinned-to-top May 17.
