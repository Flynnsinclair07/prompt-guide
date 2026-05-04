# Job tracker

A database template for every role you're considering, applying to, or actively in process for. The table below is set up to import as a Notion database — convert it after import (right-click the table → "Turn into database") and you can group by **Stage**, sort by **Last contact**, filter by **Priority**, and add columns as you need.

The two pre-filled rows are examples to show the shape. Delete them before you start using it for real (or keep them and watch how your real entries look next to them).

## How this fits with the prompts

Every prompt in the bundle expects you to know which role you're working on. The tracker is where you keep that. When Module 1 says "[PASTE THE FULL JOB DESCRIPTION]" or Module 5 says "[COMPANY · STAGE · ROLE]," you grab those from here.

A few field-level notes:

- **Stage** uses the funnel most searches actually go through. Adapt freely — if your industry has a different shape (e.g., consulting partner-fit interviews, academic faculty searches), add stages.
- **Resume version** is the filename or doc title of the tailored resume you sent. Tailoring is a Module 1 prompt — keeping a record means you can re-use the right one if a referral asks for a copy a week later.
- **Notes** is the catch-all. Use it for the recruiter's reading vibe, the salary range you saw on Levels, the question they asked twice in screening, anything you'd want before round 4.

## The tracker

| Company | Role | Source | Stage | Date applied | Last contact | Recruiter | Resume version | Cover letter? | Comp range (Levels.fyi) | Priority | Notes |
|---|---|---|---|---|---|---|---|---|---|---|---|
| Acme Corp | Senior PM, Growth | LinkedIn (recruiter DM) | Final round | 2026-04-22 | 2026-05-01 | Sarah K. | resume-acme-pm-growth-v2.pdf | yes (referral version) | $185–235K | High | Loved the panel; CFO interview was sharp. They asked twice about my work on the migration project — that's the leverage point if they make an offer. |
| Beta Industries | Director of Engineering | Referral (Mei) | Phone screen | 2026-05-02 | 2026-05-02 | (no recruiter, hiring manager direct) | resume-beta-director-eng.pdf | no | $220–280K | Medium | Hiring manager wrote back same day. They're early-stage and moving fast. Need to understand the equity package before going further. |

## Stage values (a controlled vocabulary so the database filters work)

Suggested values for the **Stage** column (in funnel order):

- **Bookmarked** — saw the role, thinking about it
- **Researching** — checking levels, blind, network for warm intros
- **Applied** — submitted, waiting on recruiter reply
- **Recruiter screen** — first call scheduled or done
- **Hiring manager** — second call
- **Phone screen** — early technical / fit screen
- **Take-home / case** — async exercise in flight
- **Onsite / panel** — final-round day
- **Final round** — last decision-makers
- **Reference check** — they're calling references
- **Offer pending** — verbal / waiting on letter
- **Offer received** — letter in hand, negotiating
- **Accepted** — signed
- **Withdrew** — I pulled out
- **Rejected** — they passed
- **Ghosted** — radio silence > 2 weeks; treat as rejected for planning, but log so the pattern is visible

When you turn this table into a database in Notion, change the **Stage** column to a Select field with these values. You'll get color-coded chips and groupings for free.

## Priority values

- **High** — would say yes today if the offer was right
- **Medium** — interested, but it's not a stretch reach
- **Low** — keeping options open, would only proceed if they came after me

## Suggested views to set up after database conversion

1. **Active pipeline** — filter Stage ≠ Accepted / Withdrew / Rejected / Ghosted. Sort by Last contact ascending (so the stalest roles surface).
2. **High priority** — filter Priority = High. Reminds you to invest your prep time on the roles that actually matter.
3. **Awaiting response** — filter Stage = Applied OR Recruiter screen OR Phone screen, AND Last contact > 7 days ago. The follow-up list.
4. **Negotiation queue** — filter Stage = Offer pending OR Offer received. When this view has rows, drop everything else and run Module 5.

## Quick-add rows

The fastest way to add rows in Notion is the inline + button (top of the database). Don't over-engineer — when you see a role you might apply to, add the row in 10 seconds with just Company, Role, Source, Stage = Bookmarked. Backfill the rest later if it gets serious.
