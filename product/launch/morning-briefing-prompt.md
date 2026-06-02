# Morning briefing — manual trigger prompt

**How to use:** When you wake up, open the Claude Code chat and say:

> run morning briefing

That triggers Claude to read this file and execute the briefing system. ~10 min total. Output saved to `product/launch/daily-briefings/briefing-YYYY-MM-DD.md`.

**When the cloud schedule (`/schedule`) is fixed:** swap to autonomous daily 9 AM MT run. Until then, manual trigger.

---

## The briefing system (what Claude does when you say "run morning briefing")

Spawn 4 parallel sub-agents. Each handles one research stream. All run simultaneously, finish in ~5-8 min. Then Claude compiles into one briefing doc.

### Agent A — Reddit thread scout

**Goal:** find 3 active threads in r/cscareerquestions, r/jobs, r/csmajors, r/recruitinghell where someone's asking a specific question that one of the snipprompts pages directly answers.

**Tools:** WebSearch + WebFetch.

**Output (in the briefing):**
- Thread title + URL
- The specific question they're asking
- Suggested 2-3 sentence reply (lowercase, Flynn voice, no exclamation points)
- Which snipprompts page to link IF relevant (none if it would feel forced)
- Comment count + age (skip threads >100 comments or >24h old)

### Agent B — HN / IH watch

**Goal:** check for any new comments on Flynn's IH post-mortem, any new HN threads about ChatGPT for resumes/AI tells/job hunting that he could comment on.

**Tools:** WebFetch (https://news.ycombinator.com/newest, https://www.indiehackers.com/post/launched-on-product-hunt-yesterday-2-upvotes-0-sales-what-the-data-actually-said-259e99ca68).

**Output:**
- New comments on Flynn's IH post (if any) — quoted + suggested reply
- Today's HN front page items relevant to SnipPrompts wedge (1-3 picks)
- IH community digest — top 3 posts in Growth or Milestones group worth a comment

### Agent C — Content drafter

**Goal:** draft today's content based on the day-of-week cadence.

**Day-of-week schedule:**
- Mon: 1 LinkedIn-style personal post draft (or skip if Flynn isn't using personal LinkedIn)
- Tue: 1 short Reddit comment template (general use, not tied to specific thread)
- Wed: 1 IH comment draft on someone else's post (read Growth group, find one to engage)
- Thu: 1 TikTok script (~30 sec)
- Fri: 1 weekly recap draft for the newsletter (if Kit list ≥ 20 subscribers)
- Sat: skip — rest day
- Sun: 1 YouTube script outline for the week's Sunday upload (if not already drafted)

**Output:** the draft, ready to copy-paste, with the platform's voice rules applied.

### Agent D — Site health + monitoring

**Goal:** quick public-facing health check on snipprompts.com.

**Tools:** WebFetch.

**Output:**
- Is snipprompts.com responding? (200 OK)
- Has any new Reddit/Twitter/forum mention of "snipprompts.com" appeared in the last 24 hours?
- Any new SEO ranking signal worth noting (e.g., did Google start ranking a specific prompt page)?
- Any obvious issues — broken images, expired CMP banner, broken link in nav

### Compiler — Claude writes the briefing doc

After all 4 agents finish, Claude writes:

```
# Morning briefing — [DATE] [DAY OF WEEK]

## Show HN status (if recent)
[Pulled from Flynn's most recent HN post URL if applicable]

## Career-center inbox status
[Note for Flynn to manually check inbox in 5 min and add: # new replies, # bounces, action items]

## Reddit picks (3 threads)
[From Agent A]

## HN / IH watch
[From Agent B]

## Today's content draft
[From Agent C — based on day-of-week]

## Site health
[From Agent D]

## Today's recommended priority order

1. [Highest-leverage action — usually inbox replies if any]
2. [Second-priority — usually engage with the 3 Reddit picks]
3. [Third-priority — today's content draft, ship if you have time]

## Manual additions (Flynn fills in over coffee, 5 min)

- GA4 weekly users: [paste from https://analytics.google.com/]
- Kit subscribers: [paste from https://app.kit.com/]
- Gumroad sales today / this week: [paste from https://app.gumroad.com/]
- One thing that surprised me yesterday: 
- One thing I'm worried about today:

## Notes
[Anything else worth flagging]
```

---

## What the agents do NOT do

- They don't post anything to Reddit/IH/HN. They DRAFT. You review and post.
- They don't reply to career-center directors. Those need your judgment + voice.
- They don't pull data from Flynn's private dashboards (no API setup). Flynn pastes that manually under "Manual additions."
- They don't make decisions. They surface options, you decide.

---

## Output location

Each briefing saves to:

`product/launch/daily-briefings/briefing-YYYY-MM-DD.md`

Open in TextEdit each morning. Read while you drink coffee. Done.

---

## When to update this file

- If you find the briefings are missing something useful → add it to the agent goals above
- If an agent is producing noise → tighten the goal
- If you change your daily routine → update the day-of-week content schedule above
- If Show HN, PH, or other one-off events are happening → I'll add temporary sections for that day

---

## First briefing — Wed June 3, ~9:00 AM MT

Tomorrow's briefing will be Show-HN-focused. Special agents fire instead of the standard four:

- Agent A: HN current top-50 — what's on the front page right now (so you know what you're posting next to)
- Agent B: HN posting best practices — quick reminder of "things to do in the first hour"
- Agent C: Show HN reply check — re-read the 3 pre-drafted replies in `show-hn-replies-pre-drafted.md` and surface any tone changes needed based on today's HN climate
- Agent D: Site health + readiness check — is snipprompts.com responding, is the homepage rendering correctly on mobile

Output: `product/launch/daily-briefings/briefing-2026-06-03-show-hn-day.md`
