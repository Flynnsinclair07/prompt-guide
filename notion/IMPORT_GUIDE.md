# IMPORT_GUIDE

How to take the six markdown files in this folder and turn them into a working buyer-facing Notion workspace, ready to share via duplication URL.

**Prerequisite**: a Notion account. Free tier works for hosting; the buyer needs free tier to duplicate. Don't put this in a Team workspace — duplication of Team pages requires the duplicating user to be invited, which defeats the point.

---

## TL;DR

1. Create a personal Notion page called **The Job Hunter's AI Bundle**.
2. Drag-and-drop all six markdown files (`00` through `05`) into it.
3. For three of those imported pages, convert the inline table to a Notion database (right-click the table → "Turn into database"). Pages: `01-prompt-library`, `02-templates` is fine as-is, `03-job-tracker`.
4. Set Share → "Allow duplicate as template" → copy the URL.
5. Paste that URL into the `NOTION_DUPLICATION_URL` placeholders in [GUMROAD_LISTING.md](../GUMROAD_LISTING.md) Field 12 and [DELIVERY_EMAIL.md](../DELIVERY_EMAIL.md) (HTML body + plain-text fallback — two replacements).

That's it. The rest of this guide is the long version with screenshots-worth-of-detail in case any step is unclear.

---

## Step 1 — Create the parent page

In your personal Notion workspace, create a new page.

- **Page title**: `The Job Hunter's AI Bundle`
- **Cover image**: optional. If you use one, match the cover-image direction in `product/job-hunter-bundle-outline.md` Section 6 — navy + cream, serif headline. The Gumroad cover (when designed) can serve double-duty.
- **Icon**: optional. A simple 📘 or no icon at all both work. Don't use the bundle's emoji palette (🟢🟡🟠🔴) — those are interview-prep semaphore, not branding.

This page is the workspace root. Everything else lives as a sub-page under it.

---

## Step 2 — Import the six markdown files

In the parent page, click `/` and choose **Import** (or use the "Import" item from the parent page's `...` menu).

Notion's importer accepts `.md` files. Drag and drop or select all six files at once:

- `00-START_HERE.md`
- `01-prompt-library.md`
- `02-templates.md`
- `03-job-tracker.md`
- `04-progress-checklist.md`
- `05-changelog.md`

Notion will create one sub-page per file, named after the file's H1. After import, the sidebar should look like:

```
The Job Hunter's AI Bundle
├── Start here
├── Prompt library
├── Templates
├── Job tracker
├── 7-day progress checklist
└── Changelog
```

If Notion gives you an "Untitled" page or two, that means there were extra blank H1 splits. Just delete those and re-import the offenders.

---

## Step 3 — Convert the two tables to databases

Two of the imported pages have markdown tables that should become Notion databases:

### 3a. Prompt library (`01-prompt-library`)

The page opens with a 44-row table (Module / # / Title / Use case / Stage). After import, right-click anywhere in the table → **Turn into database** → choose **Inline**.

Notion will create a database from the table rows. After conversion:

- **Module** column: change from text to **Select**. Add color tags for Resume, Cover Letter, Interview, LinkedIn, Negotiation.
- **Stage** column: change from text to **Select**. Add color tags for Resume, Application, Search prep, Outreach, Interview, Negotiation.
- **#** column: change from text to **Number**. Allows numeric sort.
- **Title** column: keep as Title (the linkable column).
- **Use case** column: keep as text.

Now you have a filterable, sortable prompt index. Suggested view to set up for buyers:

- **By stage** — group by Stage. So a buyer with an offer in hand sees the Negotiation prompts grouped together; a buyer just starting sees Resume prompts.
- **Search** — Notion's built-in search across the database hits Title and Use case both. No setup needed.

The full prompt text for each of the 44 prompts lives below the table, in code blocks. Leave those as-is — they don't need to be inside the database; they're sibling sections on the same page. Buyers scroll to find a specific prompt's full text or use the page's TOC.

### 3b. Job tracker (`03-job-tracker`)

This one was designed as a database from the jump. The pre-filled rows (Acme, Beta) are there to show the shape — buyers can delete or keep them.

Right-click the table → **Turn into database** → **Inline**. Then:

- **Stage**: Select. Add the values from the "Stage values" section below the table.
- **Priority**: Select. Add High / Medium / Low with color tags.
- **Date applied** + **Last contact**: change to Date type.
- **Cover letter?**: change to Checkbox.
- **Comp range**: keep as text (a range like "$185–235K" doesn't fit Number).

Then create the suggested views (Active pipeline / High priority / Awaiting response / Negotiation queue) per the instructions in the page itself.

---

## Step 4 — Don't convert these tables

The other markdown files have tables that should **stay** as tables, not become databases:

- **`02-templates`** — no top-level tables; just headings + code blocks. Leave alone.
- **`04-progress-checklist`** — no tables; just checkboxes (Notion converts `- [ ]` to checkboxes automatically). Leave alone.
- **`05-changelog`** — no tables. Leave alone.

If Notion converted any code block to a quote or paragraph (it sometimes does on long fenced blocks with special characters), select the block, hit `/` and choose **Code** to fix it. Set language = "Plain Text" or leave unset.

---

## Step 5 — Set up the duplication URL

This is what the buyer clicks to get their own copy.

1. On the **The Job Hunter's AI Bundle** parent page, click **Share** (top-right).
2. Toggle **Share to web** ON.
3. Toggle **Allow duplicate as template** ON.
4. Toggle **Allow editing** OFF (this is critical — without it, the buyer's edits would write back to your master, breaking it for the next buyer).
5. Toggle **Allow comments** OFF (same reason).
6. Click **Copy web link**.

The URL will look like:

```
https://flynnsinclair.notion.site/The-Job-Hunters-AI-Bundle-XXXXXXXX
```

That's the URL to paste into:

- [GUMROAD_LISTING.md](../GUMROAD_LISTING.md) Field 12 — `NOTION_DUPLICATION_URL` placeholder (1 location, in the receipt-email body block that points to DELIVERY_EMAIL.md)
- [DELIVERY_EMAIL.md](../DELIVERY_EMAIL.md) — `NOTION_DUPLICATION_URL` placeholder appears twice (HTML body + plain-text fallback)

Find/replace `NOTION_DUPLICATION_URL` with the actual URL across both files. Commit the change to `launch-prep`.

**Test the duplication flow before launch**: open the URL in an incognito window, click "Duplicate" (top-right of the Notion page), verify it duplicates into a fresh Notion workspace cleanly. If it asks for a paid plan, your share settings are wrong — check that "Allow editing" is OFF.

---

## Step 6 — Upload the link as a Gumroad file

Per [GUMROAD_LISTING.md](../GUMROAD_LISTING.md) Field 8, the Gumroad product gets two files:

1. `job-hunters-bundle.pdf` — the primary deliverable
2. `job-hunters-bundle-notion-link.txt` — a one-line text file containing the duplication URL

Create the second file by saving the duplication URL to a `.txt`. Buyers download both files; the `.txt` ensures they have the Notion URL even if they lose the receipt email.

---

## Maintaining the workspace post-launch

When you ship a new bundle version (v1.1 etc.):

1. Update the master Notion workspace directly — edit the prompt library, add the new prompts, add a changelog entry.
2. Buyers who duplicated v1.0 keep their copy as-is (their tracker rows, their notes, etc.). They have to manually re-duplicate to get the v1.1 page templates if they want them, OR you can email them a list of what changed.
3. The `05-changelog.md` page in this folder is the source of truth for the changelog. Keep it updated in the repo too — it's a recurring artifact.

---

## Troubleshooting

**The imported page has weird formatting on tables.** Notion sometimes mangles tables with too many columns. The job tracker has 12 columns — if it imports broken, copy the table from `03-job-tracker.md` and paste into a fresh Notion table block manually. (10 minutes max.)

**The code blocks in `02-templates.md` got converted to quotes.** Select the offending blocks, `/code` to convert. Long code blocks with special characters (the BATNA worksheet has some) sometimes trip up Notion's importer.

**The duplication URL forces buyers to a paid plan.** Your master workspace is in a Team plan. Move it to a personal workspace (drag in the sidebar) or create a new personal workspace and re-import.

**A buyer reports their duplicated workspace shows old content.** They duplicated before you updated the master. Notion duplications are point-in-time snapshots — there's no live sync. Either email them the new content or have them re-duplicate (their tracker data is in their workspace, not yours, so re-duplicating won't lose it).

---

## Why this folder exists in the repo

The Notion workspace itself lives in Notion. But the **content** of each page lives in this `notion/` folder as version-controlled markdown — so when a v1.1 ships, you edit these files first, then re-import or hand-update Notion. The repo is the source of truth; Notion is the published surface. Keeps drift down and lets you grep across the workspace from a terminal when you need to.
