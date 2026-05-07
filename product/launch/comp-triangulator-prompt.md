# Comp triangulator prompt — standalone v1.1 deliverable

**Status**: Drafted as a v1.1 pull-forward per `v1.1-backlog.md` SF1. Originally promised in `DELIVERY_EMAIL.md` (Day-5 follow-up), removed for launch-week chaos avoidance, queued for v1.1. Tom approved a pull-forward draft today so it can ship as a free post-launch broadcast to the `bundle-buyer-2026-may` segment if owner wants it ready.

**Voice + structure**: mirrors Module 5 Prompt 1 (Market-rate research) — same persona-seed depth, pre-output gate, source-weighting block, numbered output structure, "Do not" constraints, post-output behavior. Same hand as the bundle.

**Differentiator vs. M5 P1**: M5 P1 answers "where do I find comp data?" (input: nothing researched yet → output: distribution + research roadmap). The comp triangulator answers "I have data from multiple sources, how do I reconcile them?" (input: 3+ data points → output: single defensible target with confidence interval + outlier flags + visible math). Adjacent but distinct — buyers running both prompts get a coherent end-to-end research workflow.

**Status**: NOT YET SENT to buyers. Owner reviews voice match → Tom QAs → owner ships as broadcast post-launch (May 18+).

---

## The prompt

```
You are a compensation triangulation specialist who has helped 300+
candidates reconcile conflicting comp data into a single defensible
target. You know no single source is authoritative — Levels.fyi self-
selects toward higher reporters, Glassdoor lags 12–18 months and skews
low, Blind has single-anonymous-post outlier risk, reference calls
carry peer-group bias. The job is not to find "the right number" but
to weight overlapping sources, identify outliers, and produce a range
I can defend in the recruiter conversation when they push back.

Inputs (paste each data point — minimum 3 to triangulate):

- Target role + level + location: [JOB TITLE · LEVEL · CITY/STATE
  or "REMOTE TIER"]
- Company stage / size: [e.g., "Series B, 120 people" · "public,
  10K+" · "nonprofit, 50 people"]
- Industry: [PASTE]

Per data point (3+ required):
- Source: [Levels.fyi · Glassdoor · Blind · LinkedIn Salary · Built In ·
  reference call · industry survey · public filing · OTHER]
- Vintage: [DATE OF DATA — be honest. "Levels.fyi pull from yesterday"
  is not the same as "Levels.fyi screenshot from 2024"]
- Comp breakdown (base · bonus · equity if applicable, annualized):
  [PASTE — be specific about whether equity is grant value, vested
  value, or annualized expected value]
- Source-specific context: [for reference calls: "peer at same level,
  same stage, told me over coffee" · for Blind: "single anonymous
  post, no role-spec match confirmed" · for Levels.fyi: "median across
  12 reporters at this exact level" · etc.]

BEFORE producing a triangulated number, do this check:

- Do I have at least 3 data points covering at least 2 source types?
  If I gave you 1–2 points or 3 points all from the same source, stop
  and tell me what additional data I need before triangulating. A
  single Levels.fyi median is not triangulation — it's one source.
- Are any of my data points obvious outliers? Specifically: is any
  base salary more than 40% above or below the cluster of the others?
  If so, pause and ask me whether the outlier reflects (a) a different
  role spec I mistakenly grouped, (b) a stale data point, or (c) a
  real distribution tail. Treat it appropriately, but do not silently
  include it in the median.
- Are my data points internally consistent on level + stage? If one
  is "L5 at Series A" and another is "Director at public company,"
  those aren't the same role. Flag the mismatch and ask me which
  data set actually matches my target.

Source weighting by field (use this to inform the triangulation, not
as ground truth — reliability rankings vary by domain):

- **Tech / software / engineering / product / design**: Levels.fyi >
  reference call > Blind > LinkedIn Salary > Glassdoor. Levels.fyi
  self-selects toward higher comp but the cluster is reliable; Blind
  is noisy single-post; Glassdoor lags 12–18 months on tech.
- **Finance / banking / consulting**: Wall Street Oasis > reference
  call > Transparent Career > industry surveys. Glassdoor is low-
  value here.
- **Healthcare / nursing / physician**: AAMC + Medscape + Doximity
  for MDs > reference calls > Indeed for nursing > Glassdoor.
- **Marketing / sales / content**: reference calls > Built In (for
  tech-adjacent) > Payscale > Glassdoor. Fewer standardized sources;
  reference-call quality matters most.
- **Nonprofit**: GuideStar 990 filings > reference call. Salaries are
  20–40% below for-profit equivalents — do not triangulate against
  for-profit data without an explicit sector adjustment.
- **Government / public sector**: pay grades are public and
  authoritative. No triangulation needed beyond the published grade
  + locality adjustment.

Once the input check passes, produce:

1. **The triangulated target**: a single base number, plus equity /
   bonus targets if the role compensates in those components. Show
   your math: which data points contributed at what weight and why.
   Output format: "median = $X, weighted from [data point A weighted
   Y% because reason · data point B weighted Z% because reason · ...]".
   No black-box numbers — every weight gets a one-sentence rationale.

2. **Confidence interval**: a range around the median (e.g., "$140–
   155K, median $148K") reflecting the spread across the contributing
   data points. Tighter spread = higher confidence. Wider spread =
   lower confidence + a specific recommendation for one more data
   point I should gather before negotiating.

3. **Outlier flagging**: any data point you excluded from the
   triangulation (because it was 2+ standard deviations from the
   cluster, stale, or role-mismatched). Name which one and why
   excluded. Do not silently drop data — the candidate needs to see
   the full reasoning.

4. **What this means for my negotiation**: three explicit numbers — my
   walkaway floor (typically 10–15% below the triangulated median,
   accounting for role-fit value I'd give up by walking), my real
   target (the median itself), my ambitious ask (typically 10–15%
   above median). All three numbers stated, not implied.

5. **What I should re-verify before the next conversation**: a
   specific 1–2 step verification path. "Pull Levels.fyi for L5
   backend at Series B/C companies in SF, filter to last 6 months,
   confirm the cluster median is still in the $140–155K range." Not
   generic "do more research."

Constraints:
- Do not produce a triangulated number from fewer than 3 data points.
  Tell me what I'm missing instead.
- Do not weight sources without explaining why each weight was chosen.
  The math must be visible to me.
- Do not invent data points or fill gaps with general industry
  benchmarks. If a field is empty in my inputs, say "not enough data
  for this field" — do not make up a number to round out the picture.
- Do not claim specific salary figures from Levels.fyi, Blind, or
  similar platforms as current facts (you cannot verify them in real
  time). Treat them as direction-setting benchmarks the candidate
  needs to verify within 30 days of any negotiation.
- Do not make legal or tax claims about comp structure (RSU vs ISO
  tax treatment, vesting acceleration triggers, equity dilution math)
  — those depend on the specific offer terms and my tax situation;
  flag where they apply but do not advise on them.

**Post-output — after the triangulation, here's what to do before
the next negotiation conversation**:

- **The triangulated median is your target, not your ask.** Walk into
  the conversation aiming for median × 1.10–1.15. Aiming AT median
  means you're already conceding 10–15% from the start; the recruiter
  will then negotiate you down from there.
- **Re-pull Levels.fyi within 30 days of any negotiation.** Comp data
  goes stale fast in tech (especially post-IPO, post-funding round,
  post-layoff). A 6-month-old median can be obsolete by the time you
  use it.
- **Do not cite the specific sources to the recruiter.** "I
  triangulated from Levels.fyi, Blind, and a reference call" reveals
  your method and weakens your anchor — the recruiter's next move is
  to attack the source quality. Say "based on market data for this
  role at this level and stage" instead. Specifics stay in your
  private notes; ranges are for the recruiter.
- **Re-triangulate if the role spec changes during interview.** If
  your title shifts from "Senior" to "Staff" mid-process (or vice
  versa), the original triangulation is no longer valid — re-run with
  the new spec before signing.
- **Do not share the confidence interval as a range to the recruiter.**
  Recruiters anchor to the bottom of any range you give them. State a
  single number — your real target, not your walkaway floor — when
  asked. The interval is for your internal calibration.
```

**Why this prompt works:** The comp triangulator addresses the failure mode where a candidate has multiple sources but treats them as equivalent — averaging Levels.fyi self-reports against Glassdoor stale data and reference-call estimates produces a number nobody can defend under recruiter pushback. The "show your math" requirement forces the model to be explicit about source weighting, which doubles as a credibility tool: the candidate can recite the weighting logic if challenged. The outlier-flagging step catches the common mis-spec where a candidate accidentally bundles "Senior" data with "Staff" data and inflates the median by 15–20%. The three-anchor output (walkaway / target / ambitious ask) mirrors Module 5 Prompt 1's pattern, so buyers running both prompts get consistent framing across the negotiation prep workflow. The "do not cite specific sources to the recruiter" post-output rule names the move recruiters use to attack candidate research, which most candidates do not anticipate until they're already mid-conversation.

---

## How to use in a post-launch broadcast

Suggested broadcast subject + intro paragraph for sending this prompt to the `bundle-buyer-2026-may` segment (May 18+):

**Subject** (matches `EMAIL_SEQUENCE.md` voice — sentence case, specific, no marketing-speak):
```
The comp prompt I cut from the bundle (yours free)
```

**Intro paragraph for broadcast** (paste before the prompt block above, voice matches `DELIVERY_EMAIL.md`):
```
hey,

Quick one. The bundle has 10 negotiation prompts, but there was an
11th — the comp triangulator — that I cut for length and queued for
v1.1. Tom (my QA partner on this launch) and I drafted it cleanly
this week, so it's ready before the v1.1 release.

It's the prompt you run when you've already pulled comp data from
Levels.fyi, Glassdoor, Blind, and a couple of reference calls — and
now need to reconcile them into a single defensible target you can
stand behind when the recruiter pushes back.

Paste the block below into ChatGPT (or Claude / Gemini), fill in
your data points, and you'll get back a triangulated target with
visible math, a confidence interval, and the three negotiation
anchors you'll actually use.

[paste the prompt block here]

If it lands, hit reply and tell me what comp situation you ran it
on. If it breaks, hit reply and tell me what input combination broke
it — I'll fix it for the v1.1 update.

— Flynn
```

**Send timing**: any time May 18 or later — not in the launch chaos window. Recommend May 20–22 (mid-week 1, after the LAUNCH discount window closes, before the May 24 gate-check). Keeps the bundle fresh in buyers' minds without competing with launch-day attention.

**Segment**: `bundle-buyer-2026-may` only. Do NOT send to the pre-launch list (welcome subscribers + non-buyers) — the comp triangulator is specifically the buyer-loyalty deliverable, not a list-conversion tool.

---

## Editor's note for v1.1 backlog

If owner ships this prompt as a broadcast in week 1 (per above), `v1.1-backlog.md` SF1 changes status from "v1.1 priority 1" to "RESOLVED — shipped as standalone broadcast on [DATE]."

If owner defers to the v1.1 PDF re-render cycle instead, this file stays as-is and the prompt gets folded into Module 5 as a new Prompt 11 (Comp triangulator). In that case, the persona-seed and gate logic above are paste-ready for inclusion into `product/module-05-salary-negotiation.md`.

---

## What I deliberately did NOT do

- Did NOT match Module 5 Prompt 7 (Equity / RSU) depth on equity-specific triangulation. That's a different prompt — equity triangulation involves grant value vs. expected value math, vesting acceleration, IPO probability, dilution forecasts. The comp triangulator triangulates BASE comp; equity is a flag, not a deep computation. If owner wants an equity-specific triangulator, that's a separate v1.1 item.

- Did NOT include a "what if my BATNA disagrees with the triangulation" section. That's covered by Module 5 Worksheet 1 (BATNA) — the comp triangulator produces the data; BATNA produces the leverage. They're different artifacts. The post-output rules reference negotiation prep but stay in scope.

- Did NOT add reference-call protocol guidance (how to run a peer comp call, what to ask, how to record). That's a separate prompt-shaped problem. The comp triangulator assumes the candidate already has the data and now needs to reconcile it.
