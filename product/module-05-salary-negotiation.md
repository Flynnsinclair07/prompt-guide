# Module 5 — Salary Negotiation

**FLAGSHIP MODULE**

**Target on completion**: 10 prompts · 8 scripts · 3 worksheets (BATNA · Comp research · Walkaway math)
**This commit — Batch 1**: 5 prompts + 3 scripts (for boss QA before Batch 2)
All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o).

---

## When to use this module

Salary negotiation is the single highest-dollar-per-hour workflow in any job search. A typical 3-hour negotiation spread across 3–5 conversations swings total comp by $5,000–$50,000+ on average, often more at senior levels — and the negotiation window closes when you sign the offer. Every hour of prep here returns at a rate nothing else in the bundle touches.

Most candidates under-negotiate for three reasons:
1. They don't know what the role actually pays (Prompt 1 fixes this)
2. They don't know what they just got offered (Prompt 2 fixes this)
3. They freeze or apologize when they ask for more (Prompts 3–10 + scripts fix this)

This module is built to fix all three, in order. Run the prompts in sequence the first time you negotiate. Then return to the specific prompts and scripts for the situations you hit — exploding offer, multiple offers, equity questions, PTO, the "we don't have budget" response.

**Critical rule**: every prompt in this module has a heavy post-output section — what to do AFTER the conversation or message. Negotiation is more about what happens in the silence between rounds than about the asks themselves. Read the post-output rules as carefully as the prompts.

---

## Prompt 1 — Market-rate research (the number you must know before you open your mouth)

```
You are a compensation strategist who has run comp data for 200+
candidates across tech, finance, healthcare, and nonprofit. You know
which sources are accurate, which are self-selection-biased, and which
lie. You also know that "what this role pays" is a distribution, not a
point — and that candidates who walk into negotiations without knowing
the distribution get anchored low.

Inputs:
- Target role: [JOB TITLE — be specific. "Software engineer" is not
  specific; "Senior backend engineer, Python + distributed systems,
  5 years experience" is]
- Seniority level: [IC · senior IC · staff · manager · director · VP]
- Location (or location tier if remote): [CITY + STATE · OR "REMOTE,
  US" · OR "REMOTE, GLOBAL"]
- Company stage / size: [e.g., "Series B, 120 people" · "public,
  5000+ employees" · "nonprofit, 50 people" · "federal government"]
- Industry: [PASTE]
- My current comp (base · bonus · equity, annualized if possible):
  [PASTE — OR "UNEMPLOYED / NOT RELEVANT"]
- What I've already researched, with source names: [LIST — e.g.,
  "Levels.fyi, 2 reference calls, Glassdoor" · OR "NOTHING YET"]

BEFORE giving me numbers, do this check:
- Is my target-role input specific enough to produce a real number? If
  I gave you a generic title (e.g., "marketing manager" with no
  specialty, seniority, or domain), pause and ask me 2–3 questions to
  tighten it. A range for "marketing manager at a B2B SaaS company,
  mid-size, demand-gen specialty" is very different from "marketing
  manager at a Fortune 500 consumer brand" — the numbers shouldn't be
  averaged.
- Have I checked the RIGHT sources for my field? If I said "NOTHING
  YET," stop and walk me through which sources are authoritative for
  MY specific industry and role before producing any numbers. Do not
  give me a range built from weak or mismatched sources.

Source authority by field (use this to guide me, not to fabricate
numbers):

- **Tech / software / engineering / product / design**: Levels.fyi is
  the gold standard. Blind for anonymous current-employee posts.
  Glassdoor for fallback only — it skews low and older. LinkedIn
  Salary as a distribution reference.
- **Finance / banking / consulting**: Wall Street Oasis, eFinancial-
  Careers, Transparent Career. Glassdoor is low-value here.
- **Healthcare / nursing / physician**: Doximity (for MDs), AAMC,
  Medscape Physician Compensation Report. For nursing: Indeed plus
  state-specific union contracts when applicable.
- **Marketing / design / content / sales**: Built In for tech-
  adjacent roles. Glassdoor + Payscale. 1:1 reference conversations
  matter more here (fewer standardized sources).
- **Nonprofit**: GuideStar 990 filings (legally public), Idealist.
  Salaries are 20–40% below for-profit equivalents; counter with
  mission + benefits framing, not market comparables.
- **Government / public sector**: pay grades are public. Federal: GS
  scale + locality pay adjustments. State/local: each jurisdiction
  publishes.

Once the input check passes, produce:

1. **The distribution** (not a point): give me a range with 3 anchors —
   25th percentile, 50th percentile (median), 75th percentile — for
   MY specific role + seniority + location + stage. If stage or
   location materially shifts the number, call out the shift (e.g.,
   "Series B pays 85% of public-co equivalent on base but adds
   equity that can equalize or exceed").

2. **Source attribution**: for each anchor, cite which type of source
   it's built on (e.g., "median based on Levels.fyi self-reported for
   L5 backend engineers at Series B/C companies, SF or remote US,
   2024–2026"). If any anchor relies on general industry benchmarks
   rather than role-specific data, flag that.

3. **Component breakdown**: split the distribution into base · bonus ·
   equity · benefits where applicable. At some seniorities (staff+ in
   tech, Director+ in finance), equity or bonus is >40% of total comp
   — a base-only number is misleading at those levels.

4. **My leverage read**: based on my current-comp input, where does my
   current comp sit in the distribution for my target role? (Under
   25th, between 25-50, at median, above 75, etc.) This tells me how
   much room I have to negotiate.

5. **What to actually go find** (if my research inputs are thin): a
   specific, prioritized list of 3 sources and 1–2 reference
   conversations to close the gap. Not generic "do more research" —
   name the exact sources for MY field.

Constraints:
- Do not produce a single point estimate. "This role pays $140K" is
  worse than "this role pays $125–165K, with median around $145K at
  my stage/location." Point estimates anchor me wrong.
- Do not cite sources you can't verify. If you don't have current data
  for a specific field or geography, say so and tell me where to go.
- Do not rely on a single source. Triangulate from at least 2 where
  possible; flag it if only one source is available.
- Do not claim specific numbers from Levels.fyi, Blind, or similar
  platforms as facts (you can't verify them in real time). Use them
  as direction-setting benchmarks, always paired with "verify at
  current data."
- Do not make legal or tax claims about comp structure (e.g., "equity
  vests over 4 years") without noting that specific terms vary and
  I need to read the actual offer.

**Post-output — after you have the distribution, here's what to do
next (before any negotiation conversation)**:

- **Stress-test the median**: the 50th percentile number should
  "click" as plausible given the role's responsibility level. If the
  median looks way higher than you expected, double-check with one
  reference call. If way lower, you may have mis-spec'd the role
  (e.g., called yourself "senior" but researched "staff" numbers).
- **Don't anchor to the 25th percentile in your head**. Candidates
  with research often subconsciously aim for the low end "just to be
  safe." Aim for 50th–75th depending on leverage; the recruiter has
  already anchored low for you, don't do it twice.
- **Write your 3-anchor number down before any offer conversation**:
  (a) walkaway floor, (b) real target, (c) ambitious ask. All three
  should sit inside or above the distribution you just produced. The
  ambitious ask is usually 10–15% above target, not a wishlist
  number.
- **Do not share any of these numbers with the recruiter yet.** The
  salary screen / first comp conversation is a separate prompt (see
  Module 3 Prompt 8).
```

**Why this prompt works:** Most salary research produces one number from one source, which is exactly the wrong input for a negotiation. The distribution-with-three-anchors output mirrors how real comp conversations actually work — recruiters and hiring managers talk in ranges, and the candidate who shows up with a range outperforms the candidate with a point estimate. The source-authority-by-field block is the kind of specific, non-generic guidance every other salary prompt skips. The post-output rule against anchoring to the 25th percentile names a common self-sabotage pattern that well-researched candidates still fall into.

---

## Prompt 2 — Offer evaluation (decode what you just got, before you respond)

```
You are an executive compensation consultant who has reviewed 500+ offer
letters across levels and industries. You know the single biggest
failure mode in offer evaluation: the candidate anchors on base salary,
misses a high-value component (equity refresh, sign-on, bonus target),
and says yes to a package that leaves $20K–$100K+ on the table. You
also know that the first offer is almost always negotiable — the
recruiter expects a counter.

Inputs:
- The offer, in detail — paste everything you have: [BASE · BONUS
  STRUCTURE · EQUITY (grant size, vest schedule, strike price if
  options) · SIGN-ON · RELOCATION · PTO · BENEFITS · START DATE · ANY
  OTHER TERMS]
- Company stage: [e.g., "Series B, 120 people" · "public, 5000+" ·
  "nonprofit" · "government"]
- Role + seniority: [JOB TITLE · LEVEL]
- Location: [CITY, STATE · OR "REMOTE, US" etc.]
- Market-rate distribution I researched (from Prompt 1 or independent):
  [PASTE THE 25/50/75 ANCHORS — OR "HAVEN'T RESEARCHED"]
- My current comp (base · bonus · equity): [PASTE — OR "UNEMPLOYED /
  NOT RELEVANT"]
- Any verbal promises the recruiter made that aren't in the letter:
  [LIST — OR "NONE"]
- My target: [PASTE THE 3 ANCHORS I WROTE DOWN: WALKAWAY · TARGET ·
  AMBITIOUS ASK — OR "HAVEN'T SET THESE"]

BEFORE evaluating, do this check:
- Do I have the full offer in writing? If the offer is still verbal or
  partial (e.g., "they said around $140K base, equity TBD"), pause —
  tell me to ask for a written offer letter with all components before
  we evaluate. You cannot negotiate against a number that doesn't exist
  on paper.
- Have I done market research? If "HAVEN'T RESEARCHED" — stop. Do
  Prompt 1 (or equivalent) first. Evaluating an offer without a market
  range is guessing; I'll either miss room I had or demand room I
  didn't.
- Do I have walkaway / target / ambitious anchors? If "HAVEN'T SET
  THESE" — stop. Write them down before continuing. Evaluating an
  offer with no target is evaluating against the recruiter's anchor.

Once all 3 checks pass, produce:

1. **Component-by-component scorecard**: for each major component of
   the offer, give:
   - The offered value
   - Where it sits vs. my market research (below 25th, at 25–50,
     median, 50–75, above 75)
   - Negotiation difficulty on a 1–10 scale (1 = usually flexes easily;
     10 = almost never moves — e.g., some benefits plans, some equity
     refresh cycles)
   - One sentence on WHY this component is high/low

Components to cover (skip what doesn't apply):
- Base salary
- Annual bonus (target % · guarantee · metrics)
- Equity (grant value · vest schedule · cliff · refresh expectation)
- Sign-on bonus (cash · timing · clawback)
- Relocation / remote setup allowance
- PTO (days · carry-over · buyback)
- Start date flexibility
- Benefits (health, retirement match, learning budget, parental leave)
- Non-comp terms (non-compete, IP, severance, promotion timing)

2. **Top 3 levers — where to negotiate**: rank the 3 components with
   the best ratio of "how much it's below market" × "how likely it
   is to flex." For each, give me:
   - The specific ask (a number or concrete term, not "more")
   - The rationale I'd give the recruiter (1 sentence, in first
     person, spoken cadence)
   - Likelihood of movement (rough %)

3. **Hidden traps — components to examine before signing**:
   - Any clawback language on sign-on (typical: repay pro-rata if I
     leave in <12 months)
   - Any non-compete or IP clause that's broader than industry norm
   - Any promotion / review timing promise that's verbal only
   - Equity strike price (if options) and its current fair market
     value ratio — a low-strike grant at a company with low recent
     409A valuation is worth much less than a high-strike grant at a
     company trending up

4. **Verbal vs. written gap flag**: for any verbal promise the
   recruiter made that isn't in the letter (promotion timeline, team
   assignment, remote flexibility, equity refresh), call it out and
   give me the exact 1-line ask to get it added in writing.

5. **Overall verdict (1 line)**: is the offer strong (close to or
   above my target), negotiable (below target but fixable), or weak
   (so far below market that a counter is the minimum and walking
   away is on the table)?

Constraints:
- Do not tell me to accept the offer as-is unless it's clearly above
  my ambitious ask AND has no traps in hidden terms.
- Do not default to "negotiate base only." At senior levels, equity
  and bonus are where the real money lives; at mid-levels, sign-on
  and PTO often have surprising flex.
- Do not make legal claims about clauses (non-compete enforceability,
  clawback legality) without flagging that I should have an employment
  lawyer review anything unusual.
- Do not produce a scorecard if my market research inputs are weak.
  The scorecard is only as good as the range I'm comparing against.

**Post-output — after you have the scorecard, here's what to do before
responding to the recruiter**:

- **Wait 24 hours minimum before responding** (unless the offer is
  exploding — separate prompt). Nothing good comes from negotiating
  on the same call the offer landed. Thank them, say you'll review
  carefully and come back within 1–2 business days.
- **Cross-check my top-3 levers with a reference call if possible** —
  someone currently at the company or at a peer company at similar
  level. 30 minutes of talking to a human is worth more than 3 hours
  of research alone at this stage.
- **Write out my counter-offer BEFORE the next call**. Don't improvise
  on the phone. Use Prompt 3 to script the ask.
- **Keep the recruiter warm**: a 1-line "Got the offer, reviewing it
  carefully — I'll come back with questions shortly" is better than
  silence. Silence from the candidate often reads as losing interest,
  which weakens leverage.
```

**Why this prompt works:** Most offer-evaluation prompts produce "is this good or bad?" — which is the wrong question. The right question is "what's the best ratio of below-market × will-flex across these 6 components?" The top-3 levers output with ask · rationale · likelihood-of-movement is how real comp consultants structure advice. The verbal-vs-written gap flag catches the single most common offer trap (promises that never make it into the letter). The "don't negotiate on the same call" post-output rule names the biggest procedural mistake candidates make when the offer is exciting.

---

## Prompt 3 — Counter-offer scripting (the core negotiation move)

```
You are a negotiation coach who has scripted 300+ counter-offers for
candidates across IC to exec levels. You know the counter-offer is not
a conflict — it's an expected step the recruiter has budget, authority,
and social permission for. You also know candidates blow counters in
predictable ways: apologizing, weakening, splitting their own
difference before the recruiter even pushes back, and failing to leave
silence after the ask.

Inputs:
- The offer, in writing: [PASTE — or reference if it's in Prompt 2
  output]
- My target-comp anchors (walkaway · target · ambitious ask): [PASTE
  ALL 3 — if any are missing, do the check below]
- My 3 strongest leverage points (why they should pay me more): [LIST
  — e.g., competing offer, rare skill, unusual depth, business
  outcomes I've shipped that map to their top priority]
- Do I have a BATNA (Best Alternative To Negotiated Agreement)? [YES,
  it's ___ · OR NO, CURRENT ROLE IS THE FLOOR · OR I DON'T KNOW WHAT
  BATNA MEANS]
- The specific components I want to counter: [PASTE — e.g., "base up
  $15K, sign-on add $10K, equity refresh clarification"]
- Company stage + role seniority: [PASTE]
- How the offer came in (email · phone · verbal with written to
  follow): [CHOOSE]
- What the recruiter's signaled so far (warmth, urgency, flexibility
  hints): [DESCRIBE IN 2 SENTENCES]

BEFORE writing the counter, do these checks:

**BATNA check** — if I said "I DON'T KNOW WHAT BATNA MEANS," here's
the 2-sentence teach: your BATNA is your concrete backup if this
negotiation fails — another live offer, your current job, a confirmed
contract role, savings that buy you 6 months. A negotiation without a
BATNA is a negotiation where you cannot walk, which means you cannot
push. If you don't have one, we'll script a softer counter that
doesn't rely on leverage you don't have. If you DO have one, we'll
script a firm counter.

**Anchor check** — if my anchors are missing, pause. Tell me to write
down walkaway / target / ambitious. The counter-offer is 10–15% above
target (ambitious ask), not a random round number. Without anchors, I
will either counter too softly (leaving money) or too aggressively
(losing credibility).

**Leverage check** — if my 3 leverage points are generic ("I have
experience", "I work hard"), flag them. A counter-offer needs specific
leverage: a number, a rare skill, a competing offer, a business
outcome that matches what they just hired for. Push me to name 3
specific leverage points before writing the counter.

Once all 3 checks pass, produce:

1. **The counter-offer email** (if offer came via email or I'm
   responding in writing, 150–220 words):
   - Open warm. One sentence thanking them and expressing genuine
     interest in the role / company (specific, not generic)
   - Transition to the counter in a single sentence. No apology. No
     "I hate to ask" hedge. No "I was hoping for…"
   - The specific asks — number them, 1–3 items max. Each ask is a
     specific number or term, not a range, not vague.
   - The rationale in 2–3 sentences. Ground it in market data and
     specific leverage. Not "I believe I deserve…" — "Based on market
     data for this role at this level and my track record on [X], the
     [base / equity / sign-on] I'd be able to accept is [$NUMBER /
     SPECIFIC TERM]."
   - Close with a signal of continued enthusiasm and an explicit
     invitation to discuss. "Happy to jump on a call to walk through
     any of this."
   - Sign off. No "thanks in advance" (pressuring). No "sorry for the
     trouble" (weakening).

2. **The counter-offer phone version** (if the offer is being
   discussed live, 60–90 seconds spoken, 120–180 words):
   - Lead with one warm sentence.
   - Pivot to the ask with a specific transition phrase: "There's one
     thing I'd like to talk through before we move forward on this."
   - State the asks clearly. Numbered out loud if 2–3 items.
   - Give the rationale. Specific, market-anchored.
   - Stop talking. Explicitly note: "Then stop. Do not fill silence.
     The recruiter needs to process, and the first person to speak
     after a counter-offer ask usually loses."
   - If they push back immediately, pivot to the "we don't have
     budget" rebuttal (see Module 5 script).

3. **Calibration note**: based on my inputs, is this counter-offer
   tuned right? Flag if the asks look too aggressive for the company
   stage, or too soft for my leverage position. One honest sentence,
   not a rubber stamp.

4. **Likelihood assessment**: rough % chance each ask moves, based on
   typical patterns at my company stage and the components I named.

Constraints:
- Do not write "I was hoping for…" or "I was wondering if…" or "Any
  chance…" — all weakeners. Use "Based on [X], the [component] I can
  accept is [Y]" or similar direct framing.
- Do not apologize for the counter. The counter is expected.
- Do not split my own difference before the recruiter has pushed back.
  A common mistake: asking for $15K more, then in the same email
  saying "but I'd be flexible if [Y]." Make them do the counter-push.
- Do not list more than 3 asks. A 5-item counter dilutes focus and
  invites partial wins on everything instead of full wins on 1–2.
- Do not anchor the counter at my TARGET. Anchor at my AMBITIOUS ASK
  (usually 10–15% above target). Expect to land at target or between
  target and ask.
- Do not reveal my walkaway number. Walkaway is internal only; if
  they hit it, I accept, but they should never know it's the floor.

**Post-output — what to do after you send the counter**:

- **Wait at least 24 hours for a response** before any follow-up
  contact. The recruiter often needs to go back to the hiring manager
  and/or comp committee. A nudge before they've had time to process
  reads as anxious.
- **Do not send a second counter before you hear back on the first.**
  Exactly one counter-offer round is expected. Two rounds without a
  response in between is the negotiation equivalent of begging.
- **If they come back with a partial improvement**, evaluate against
  my target, not against the original offer. Improvement from a
  lowball is still potentially below target.
- **If they come back with a flat no on all 3 asks**, that's a data
  point about flexibility — not necessarily the end. Consider (a)
  pivoting one of the asks to a component with more flex (equity
  refresh, sign-on, start date, PTO), or (b) accepting if the offer
  is above my walkaway. The "we don't have budget" rebuttal script
  handles this exact moment.
- **Keep the tone identical between the counter and the response to
  their reply**. If I went in warm and direct, I stay warm and direct.
  Warming up when they say no reads as backpedaling; cooling off reads
  as pouting.
```

**Why this prompt works:** The counter-offer is where most candidates lose the most money — not because they don't counter, but because they counter weakly. The 3-check pre-output gate (BATNA teach, anchor check, leverage check) refuses to write a counter until the candidate has the scaffolding they need to land it. The "stop talking after the ask" rule in the phone version is the single most important move in live negotiation and the one most prompts don't mention. The post-output rule against sending a second counter before hearing back on the first is a specific trap candidates fall into out of anxiety — and losing that trap alone is worth the $39.

---

## Prompt 4 — Multiple-offer leverage (when you have — or think you have — options)

```
You are a senior recruiter who has watched 1,000+ candidates play the
multiple-offer game. You have seen candidates use real leverage
masterfully and watched other candidates light their only leverage on
fire by mis-playing a signal. You know the single line between
"leverage" and "bluffing" — and you know recruiters can usually tell
the difference.

Inputs:
- My situation — be honest, this only works if honest: [CHOOSE —
  "I have a second LIVE offer in writing" · "I have a second company
  in final round, verbal interest, no offer yet" · "I have early-
  stage conversations with other companies but no offer soon" · "I
  have nothing else active, but I could re-open conversations" ·
  "I have no other options and I'm bluffing — should I?"]
- If I have a real or near-real other offer — paste the details I
  have: [COMPANY · OFFER AMOUNT (if received) · TIMELINE · MY
  INTEREST LEVEL RELATIVE TO THE PRIMARY OFFER]
- Primary offer company name + role + current comp in their offer:
  [PASTE]
- My top priority between the two: [WHICH ROLE DO I ACTUALLY WANT
  MORE? BE HONEST]
- Why I'd pick the primary if the comp matched or exceeded: [ONE
  SENTENCE — role scope, mission, team, location, whatever]
- Is the primary recruiter someone who seems sharp and well-
  connected (likely to call bluffs) or more junior? [CHOOSE]

BEFORE writing any leverage language, do this check:

**Bluff check** — if I chose "I have no other options and I'm
bluffing — should I?": stop and read this carefully. Bluffing a
competing offer is one of the highest-risk moves in comp negotiation.
If you're caught, the offer usually gets pulled; at minimum, trust is
destroyed. If your recruiter is sharp, they may ask: "Which company?"
"What level?" "What's the total comp?" A bluff cannot survive
three specific follow-up questions. Unless you have a real
near-offer you can speak about specifically, do not bluff — use
one of the non-leverage prompts (Prompt 3 counter-offer) instead. If
I still want to proceed with a bluff after reading this, I will
flag that in the output and give you cautious language that
minimizes exposure, but I'll also recommend against it one more
time.

**Timing check** — if I have a real competing offer but it's not yet
in writing, flag it. Using the leverage language before the competing
offer is written ("I'm waiting on a formal offer from [X] this week")
is still fine, but it's weaker than "I have a signed offer from [X]
for [$NUMBER]." Tell me to push the other company for written
confirmation before the next primary call if at all possible.

**Honesty check** — if my input says the OTHER offer is my real
priority but I'm pressuring the PRIMARY for more, flag that. Some
candidates use leverage language to bump the primary, then take the
other role anyway — which burns the primary company and spreads
reputation damage in tight industries. If the primary is my real
top choice, my leverage is honest; if not, I should think harder
about what I'm actually negotiating for.

Once the checks pass, produce the leverage language calibrated to my
exact situation:

**If I have a LIVE signed competing offer**:
- Exact language for the phone call: 60–90 seconds, warm tone,
  spoken cadence. Structure: enthusiasm about primary + specific
  competing-offer detail (amount, role, level, timeline if
  exploding) + why I prefer the primary if comp matches + the
  specific ask that would close the gap.
- Exact language for the email version: 150–200 words, same
  structure as phone but written, no hard ultimatum.
- What to do if they ask for proof: honest — offer to share (redact
  personal details) or describe the offer in enough specificity that
  they can verify the signal. Do not fabricate.

**If I have a NEAR-OFFER (final round, verbal, no letter)**:
- Language that honestly represents the stage: "I'm in final-round
  conversations with [COMPANY] and expect an offer this week. They've
  verbally indicated a range of [APPROX $]." Exact wording for email
  + phone, same 60–90 second target for phone.
- What to do if asked whether the competing offer is in writing:
  answer honestly. "Not yet, expected by [DATE]." A recruiter who
  hears the honest version still respects the signal — one who
  hears a lie will catch the delay and mark you as untrustworthy.
- When to hold the leverage play: if the other offer won't arrive
  for 2+ weeks and the primary is pressuring a decision, leverage
  language is weaker. In that case, ask the primary for a
  decision-window extension instead (see exploding-offer prompt if
  it becomes urgent).

**If I have EARLY-STAGE conversations elsewhere**:
- Leverage language here is a soft-touch signal — "I'm exploring a
  few other opportunities in the same space" — and even that is
  risky if deployed too aggressively. Calibrated wording for the
  phone + email that signals optionality without fabricating.
- Often the stronger play is NO leverage language — instead, make a
  strong counter on market-data grounds (see Prompt 3). Tell me
  honestly which would be better.

**If I want to RE-OPEN conversations with past companies to create
real leverage**:
- A specific playbook: which types of past contacts are worth
  re-opening (specific people who expressed interest in past 90
  days, first-round rejections where I was a "strong no-hire this
  round but come back when hiring for X"), which aren't. Sample
  re-open message to send to 3 past contacts today.

Constraints:
- Do not lie about offer amount, role level, or status. Every lie is
  a landmine the recruiter can detonate with one question.
- Do not name the competing company unprovoked. Naming creates
  anchors, pressure, and risk. If directly asked, "I'd rather not
  share unless it's relevant to what we decide here — happy to
  confirm we're in the same industry / same scale if that's useful"
  is a legitimate deflection.
- Do not use leverage language to push beyond your genuine walkaway.
  Getting a recruiter to match an inflated number means you may
  actually have to take that job at that number — and they'll
  expect performance to match.
- Do not use leverage language if you're in first-round conversations
  with the primary. This is a late-game move; deploying it at first-
  round comes across as aggressive and low-judgment.

**Post-output — what to do after deploying leverage**:

- **Go dark for 24–48 hours after the ask.** Deploying leverage
  successfully requires the recruiter to do work on their end (call
  the hiring manager, get budget approval, maybe loop in finance).
  Nudging during that window makes you look desperate and undercuts
  the signal.
- **Do not over-leverage**: one clean round of leverage language,
  then wait. If they come back with a specific counter, evaluate it
  against your target (not against the inflated ambitious ask).
- **If they call the bluff or push back hard**: the recovery
  language is not "you got me." The recovery is to pivot to a
  data-based counter. ("Understood the budget constraints — setting
  aside the other offer, based on market data for this role at this
  level, the ask I'd make is [$NUMBER] for [reason].") A clean
  pivot preserves dignity and often still closes the gap.
- **If the second offer falls through** after you've used it as
  leverage: say nothing to the primary. The leverage was real at
  the time you used it; the fact that it later fell through isn't
  something you owe the primary an update on. Proceed with the
  counter-offer outcome you already negotiated.
- **Watch for primary pulling the offer**: if leverage is mis-played,
  some companies will pull the offer rather than compete. This is
  rare but happens — which is why the honesty check at the top
  matters. If this happens, it's a signal the leverage was either
  mis-timed or mis-calibrated. Salvage by reaching out within 24h
  with a genuine expression of interest and a direct ask: "I'd like
  to continue this conversation; is there a path forward from here?"
```

**Why this prompt works:** Leverage is the highest-stakes, highest-risk negotiation move — and the one most prompt libraries handle badly, either by encouraging candidates to bluff recklessly or by avoiding leverage talk entirely out of fear. The explicit bluff-check with its 3-specific-question test is a reality check most candidates desperately need before they decide to fabricate. The 4-situation branching (live offer, near-offer, early-stage, re-open) matches the real candidate reality instead of assuming everyone has a signed competing offer. The post-output rule for when leverage gets called is the difference between salvaging a negotiation and losing the offer.

---

## Prompt 5 — Exploding offer response (when they give you 48 hours to say yes)

```
You are a negotiation coach who has handled 50+ exploding offers —
the high-pressure tactic where a company demands a decision in 24–72
hours. You know most "exploding" offers are not actually exploding —
they are tests of how a candidate handles pressure, and the candidates
who respond with anxiety lose leverage they didn't know they had. You
also know the real exploding offers exist (competitive late-stage
startup hiring, some big-tech new-grad, exec with exec-search firms),
and those require a different calibration.

Inputs:
- The exact language the recruiter used about the deadline: [PASTE —
  e.g., "we need an answer by end of day Friday" · "this offer
  expires in 48 hours" · "the hiring manager is ready to move, we'd
  like to hear back this week"]
- The company, stage, and role: [COMPANY · STAGE · ROLE]
- My genuine interest level in this offer (1-10): [NUMBER]
- Other live processes or offers: [LIST — OR "NONE"]
- How I was told (email, phone, in-person from recruiter · hiring
  manager · founder): [PASTE — the source matters]
- What I'd actually need more time FOR: [CHOOSE — waiting on another
  offer · family / life decision (relo, partner's job) · time to do
  market research · time to review the written letter carefully · due
  diligence on the company (references, financials) · simply need
  time to think]

BEFORE writing the response, do this check:

**Is this actually exploding?** In most cases "exploding" is
pressure theater, not a hard deadline. Evaluate:
- Who delivered the deadline (sharp recruiter at a big company
  doing end-of-quarter close = more likely real. Junior recruiter
  with no context = often artificial)
- Company stage (late-stage startup with another candidate in
  parallel = more likely real. Large established company with a
  standard process = usually artificial pressure)
- The phrasing (specific reason given ("the budget closes Friday")
  = more credible than vague ("we need to move fast"))
- How they delivered (signed letter with a written expiration = real
  constraint. Verbal pressure on a phone call = often flexible)

Tag this specific exploding offer as:
- **Likely REAL exploding** (specific budgetary / calendar reason,
  late-stage, sharp recruiter, written in the letter) — give me the
  exploding-real response track
- **Likely ARTIFICIAL pressure** (vague language, no specific reason,
  verbal only, early-stage or large-company boilerplate) — give me
  the artificial-pressure response track
- **AMBIGUOUS — could be either** — give me the extension-ask
  language that works for both

Once tagged, produce the appropriate response:

**ARTIFICIAL PRESSURE response (most common scenario)**:

Phone / spoken version (30–45 seconds):
- Warm acknowledgement of their timeline.
- Specific extension ask with a concrete reason. Not "I need more
  time" (vague, invites pushback) — "I want to give this the
  thought it deserves, and I'm in the middle of [finishing market
  research · a family decision · waiting for one other company's
  process to wrap]. Could we move the deadline to [SPECIFIC DATE]?"
- Re-affirm interest. "I'm genuinely excited about this role and
  want to say yes with full clarity."
- Stop talking. Wait for response.

Email version (80–120 words):
- Warm open, thanking them for the offer.
- Genuine interest in 1 sentence (specific to the role or company,
  not generic).
- Extension ask with specific reason and specific date.
- Invitation to discuss if they need to push back.

**REAL EXPLODING response** (when the deadline is actually binding):

Phone / spoken version (45–70 seconds):
- Warm acknowledgement of the constraint.
- Honest status: "I hear you — given the real deadline, let me tell
  you where I am. [Here's what I can decide now · here's what I'd
  need to know to decide in the window]."
- One of two tracks:
  (a) If I can decide within the window if one specific thing moves
      — state that specific thing clearly. "If [X] were at [Y], I
      would sign by Friday."
  (b) If the window is genuinely impossible — decline with dignity
      and leave a door open. "Given that timeline, I can't give you
      a responsible yes. If that changes, or if you're ever hiring
      again, I'd genuinely love to talk."

Email version (for real exploding offers, the response is often a
phone call — but if email is appropriate, mirror the phone structure
in 100–150 words).

**AMBIGUOUS response**:

Give me the phone language that asks for a small extension (48h)
while flagging that I'll be flexible if the timeline is genuinely
fixed. Specific wording. Then tell me what to watch for in their
response to diagnose whether it was real or artificial pressure.

Constraints:
- Do not accept under exploding-offer pressure just to stop the
  pressure. This is the most expensive decision in the entire process;
  a 48-hour discount on judgment is not worth $20K+ of mis-decided
  comp or a role mis-fit.
- Do not threaten to walk unless you're actually willing to walk.
  Bluffing here exposes the weakest hand.
- Do not decline a real exploding offer in pure email if you can
  reach the recruiter by phone. A live conversation preserves the
  relationship; a cold email decline burns it.
- Do not match "exploding" with counter-pressure ("You have to
  understand my situation"). The calibrated move is calm, specific,
  and grown-up.
- Do not assume the hiring manager knows about the exploding
  deadline or agrees with it. In many cases the recruiter invented
  the deadline for their funnel metrics. Ask directly: "Is this
  timeline coming from the hiring manager, or from the recruiting
  process?"

**Post-output — what happens next**:

- **If they grant the extension**: use the time well. Don't spend it
  waiting passively. Push the competing offer, do the reference
  calls, finalize your counter. Come back ON time with a clear
  answer — nothing kills credibility like missing a granted
  extension.
- **If they push back and hold the deadline**: they've just told
  you it's real (or at least close to real). Make the call with
  what you know. Do not waffle further — a second extension ask
  reads as weak.
- **If they pull the offer after an extension ask**: this is rare
  but it happens and it's almost always a signal that the company
  operates by intimidation. That's a data point — you likely
  dodged a bad culture. Reach out in 90 days with a warm note; many
  of these situations re-open when the company's first choice
  falls through.
- **If this was artificial pressure and you called it**: the
  dynamic with this recruiter just shifted in your favor. They
  know you have judgment and aren't manipulable. The rest of the
  negotiation will be more substantive. Do not gloat — proceed
  with counter-offer (Prompt 3) as if the pressure moment didn't
  happen.
```

**Why this prompt works:** The single most expensive moment in a salary negotiation is the exploding-offer panic decision — candidates say yes to avoid losing the offer, then discover they left $20K+ on the table. The 4-input artificial-vs-real diagnosis gives the candidate a framework for reading the situation before responding, which is the move that separates candidates who handle pressure from candidates who collapse under it. The "ask directly whether the timeline is from the hiring manager or the recruiting process" line is one of the sharpest moves in the module — it often exposes artificial pressure instantly. The post-output rules address the full tree of downstream outcomes instead of stopping at "here's what to say."

---

# Scripts

*These are copy-paste-and-adapt spoken or written templates. They're shorter than the prompts — designed to be used in-the-moment when a specific situation hits. Fill in the bracketed inputs and run.*

---

## Script 1 — Email: decline the first offer politely and counter

**Use when**: the offer came by email and you want to counter in writing.

**Length target**: 120–180 words

**Tone**: warm, direct, no apology, no weakeners

**Send timing**: 24–48 hours after receiving the offer (not same day, not a week later)

```
Subject: [My name] — offer response

Hi [RECRUITER FIRST NAME],

Thank you for sending the offer for the [JOB TITLE] role — I've had
a chance to review it carefully, and I remain genuinely excited about
the opportunity to join [COMPANY]. [ONE SPECIFIC SENTENCE ABOUT WHY:
a product decision, a team member, the mission, the scope].

Before finalizing, I'd like to discuss a few components of the package.
Based on my market research for this role at this level and my track
record on [ONE SPECIFIC LEVERAGE POINT — e.g., "leading the
$12M ARR migration at Acme" or "8 years in compliance for fintech"],
I'd be able to accept an offer at:

1. Base salary of $[AMBITIOUS ASK — typically 10–15% above target]
2. [SECOND COMPONENT — e.g., sign-on of $[X], or equity refresh at
   12-month mark, or an additional [N] days of PTO]
3. [OPTIONAL THIRD COMPONENT — only if it's genuinely load-bearing]

I'm happy to jump on a call to walk through any of this, and I want
to be honest: the role and team are my preference, and I'd like to
find a path forward together.

Looking forward to continuing the conversation.

Best,
[MY NAME]
```

**What this script is doing (so you can adapt it):**
- Subject line is identifying, not dramatic (not "Offer Negotiation" — that's formal and creates tension)
- Opens with genuine specific interest (not "I am writing to…")
- Transitions to the counter with no apology and no hedge
- Numbers the asks (1–3 max, never more)
- Grounds the ask in market research + one specific leverage point
- Closes with an invitation, not a demand
- Sign-off is warm, not begging

**Do not**:
- Write "I was hoping for…" — weakener
- Apologize for the counter
- List more than 3 asks (dilutes focus)
- Reveal your walkaway number
- Offer to split your own difference before they push back

**Post-send behavior (critical)**:
- Wait **at least 24 business hours** for a response. Do not nudge.
- If they come back with a partial improvement, evaluate against your target, not against the original offer.
- If they come back with a flat no, pivot to the "we don't have budget" rebuttal script.
- Do not send a second counter email before hearing a reply to the first. Exactly one counter round is expected; two is begging.

---

## Script 2 — Phone: 30-second opener for salary discussion

**Use when**: the recruiter has called (or is about to) and salary is likely to come up live.

**Length target**: 30 seconds spoken (~75–100 words)

**Tone**: warm, curious, firm under the warmth

**When to use which version**: there are two versions below — one when YOU initiate the salary conversation, one when THEY bring up salary first.

### Version A — You initiate (when they've offered and you're calling back)

```
"Hey [RECRUITER FIRST NAME], thanks for sending over the offer.
First — I want to say I'm genuinely excited about [SPECIFIC THING:
the role · the team · the mission]. That part is clear for me.

I've had a chance to review the package carefully, and there are a
couple of components I'd like to talk through. I want to be direct
so we can use this call well: based on market data for this role
at this level and [ONE SENTENCE OF LEVERAGE], the ask I'd make is
[$NUMBER / SPECIFIC COMPONENT AT SPECIFIC VALUE].

I'd love to hear your read."

[STOP TALKING. Wait. Do not fill silence.]
```

### Version B — They bring up salary on the phone (before an offer)

```
"Good question. Before I give you a number, can I ask — do you
have a sense of the range that's budgeted for this role at your
company, at this level?"

[Wait for their response. Most recruiters will either give you a
range or deflect. Either way you now have better information.]

"Got it — based on that, and market data I've looked at for [ROLE]
at [STAGE/SIZE], the range that works for me on base is [$X–$Y]."

[Stop talking. Wait.]
```

**What these scripts are doing:**
- Opening with specific genuine interest before any comp talk (anchors the conversation in fit)
- Version A: stating the ask directly, no hedge, grounded in data + leverage
- Version B: asking for the recruiter's range first (they usually know it) before committing to a number
- Ending with silence — the most important move in phone salary conversations

**Do not**:
- Ask "what are you thinking of offering?" without first warming the call (reads as transactional)
- Give a single number (always give a range on first comp disclosure)
- Talk past the ask. After you state the number, say nothing. The first person to speak after the comp number usually loses leverage.
- Apologize for the ask
- Use the word "hopefully" ("I was hopefully thinking around…")

**Post-call behavior**:
- **Write down everything the recruiter said about comp, immediately after the call.** Recruiters often verbally agree to things that don't make the letter; memory fades in 24 hours.
- **Follow up with a 1-line email** within 2 hours: "Thanks for the call — to summarize what we discussed on comp: [SPECIFIC RECAP]. Let me know if I got anything wrong." This creates a written record.
- **Do not re-negotiate on the same call they verbally agreed**. If they said "yes, we can do $X," the call is done. Say thank you, confirm next steps, and hang up. Pushing further on the same call is how candidates turn a yes into a re-traded no.

---

## Script 3 — Rebuttal: "We don't have budget"

**Use when**: you've made a counter and the recruiter pushes back with "we don't have budget" / "I can't go higher" / "that's the max for this role."

**Length target**: 45–70 seconds spoken

**Tone**: calm, understanding, pivots to creative structure without backing down on total value

**Why this script exists**: "we don't have budget" is the single most common pushback in salary negotiation. It's sometimes true (budgets are real), often partially true (base is capped but other components flex), and occasionally pressure tactic. This script handles all three.

```
"That makes sense — base salary is often the least flexible piece,
especially at [STAGE/SIZE]. So let me ask a different question:

Given that base is where it is, can we look at the other
components? Specifically:

[CHOOSE 1–2 OF THESE TO ASK ABOUT, IN ORDER OF FLEX AT YOUR
COMPANY STAGE]:

- **Sign-on bonus** — 'Is there room on the sign-on? A [$X] sign-on
  would help close the gap for me this year.'
- **Equity refresh** — 'Can we talk about the equity refresh
  schedule? A commitment to an equity refresh at the 12-month mark
  would make the total-comp math work.'
- **Start date flexibility** — 'If base is locked, could we look at
  a start date of [DATE], so I can wrap up [ONE THING] cleanly?'
- **PTO** — 'Could we add [N] additional PTO days?'
- **Promotion / review timing** — 'Could we commit to a comp review
  at the [6-month / 12-month] mark, with a specific target if I hit
  [MILESTONE]?'
- **Remote / location flexibility** — 'Could the role be structured
  as [FULLY REMOTE / HYBRID WITH X DAYS] instead?'
- **Benefits** — 'What's flexible on [learning budget · home office
  stipend · parental leave]?'

I'm open to creative structure — what I care about is finding a
total package that works for both of us."
```

**What this script is doing:**
- First line acknowledges the constraint without arguing (arguing "you must have budget somewhere" burns trust)
- Pivots to components that typically have more flex than base
- Asks specifically rather than "can you do more somewhere?" (vague asks get vague answers)
- Closes with "creative structure" framing — gives the recruiter permission to be inventive
- "Total package that works for both of us" signals partnership, not adversary

**Component flex, by company stage** (so you can pick which 1–2 to ask about):

- **Early-stage startup (Seed – Series A)**: equity has the most flex (they have more of it than cash), sign-on often possible as retention grant instead, base is the tightest.
- **Growth-stage (Series B – D)**: sign-on is most flexible, equity refresh clarity is high-leverage, base bands are real but sometimes flex for rare skills.
- **Late-stage private / public**: sign-on and equity refresh have most flex; base is tightly banded. PTO, learning budget, and promotion timing also negotiable.
- **Traditional / corporate**: base is heavily banded; PTO, title, and level sometimes flex; promotion-review timing and written commitment to a comp review milestone are often available.
- **Nonprofit / government**: base is fixed. Focus on title, responsibilities, PTO, remote flexibility, learning budget.

**Do not**:
- Argue that the company "must have budget." You don't know their spreadsheet; arguing burns trust.
- Accept the "no" as final without pivoting. The recruiter expects a pivot.
- List 4+ components in the pivot. 1–2 specific asks outperform a scattered list.
- Say "well, what CAN you do?" — passive. State what you want instead.

**Post-rebuttal behavior**:
- If they come back with a yes on one component: accept and move to close. Do not try to stack additional asks on the same call.
- If they come back with "let me check": thank them, give a specific timeline ("would end of week work?"), and wait. Don't nudge before then.
- If they come back with another flat no: evaluate against your walkaway. If the total comp is above walkaway, consider accepting. If below walkaway, it's decision time — and the exploding-offer prompt's "decline with dignity" track applies even though this isn't exploding.
- **Never use "we don't have budget" rebuttal twice in the same negotiation.** If they've said no to base AND to the pivot, pushing a third time is begging.

---

## Prompt 6 — Deferred-start negotiation (when you need a later start date)

```
You are a recruiter who has approved and denied 200+ deferred-start
requests. You know what companies will accept, what they'll quietly
pull the offer over, and which framings make a deferred start look
reasonable vs. suspicious. You also know most candidates hurt
themselves by asking too early in the process or asking for too long
without a concrete reason.

Inputs:
- Length of deferral I'm asking for: [CHOOSE — 1–2 weeks · 3–4 weeks ·
  1–2 months · 3–6 months · 6+ months]
- Reason for the deferral, honestly: [CHOOSE — wrapping up current
  role (notice period + handoff) · school completion · parental leave
  / family · pre-planned vacation or wedding · sabbatical between
  roles · visa / immigration timing · caregiving · medical · other —
  describe]
- Company stage: [e.g., "Series B, 120 people" · "public, 5000+" ·
  "nonprofit" · "government"]
- Where I am in the process: [CHOOSE — pre-offer still interviewing ·
  received offer, haven't responded · accepted offer, need to adjust
  start]
- What the role's current stated start date is: [DATE — OR "NOT
  SPECIFIED YET"]
- How critical is the start date to their hiring need: [CHOOSE — they
  have a project kicking off that requires me · they need backfill ·
  they just want to fill the seat · I don't know]

BEFORE writing the deferral ask, do these checks:

**Timing check** — if I'm pre-offer still interviewing, pause. Asking
for a deferred start before the offer is extended is one of the
highest-risk moves a candidate can make; many hiring managers reject
candidates who flag timing issues before being chosen. Unless the
deferral is existential (visa, medical, family), wait until you have
the offer in hand before raising it.

**Length calibration** — different deferral lengths need different
framings:
- 1–4 weeks: easy ask, usually just a polite note — most companies
  accommodate without friction
- 1–2 months: needs a specific reason and ideally a concrete date.
  Most companies flex; some push back.
- 3–6 months: serious ask. Needs a strong, concrete reason (school,
  parental leave, commitment elsewhere). Usually requires justifying
  why they should hold the seat.
- 6+ months: rare and risky. Usually declined unless the role is
  senior / specialized and the company is willing to wait. Consider
  whether you should decline and re-apply later instead.

If the combination of my asked-length and reason is weak (e.g., 3
months for a vacation), flag it and tell me to either (a) shorten the
ask or (b) strengthen the reason before writing.

**Reason check** — some reasons are "green" (easy to state plainly,
companies respect them): medical, family leave, school completion,
current-role wind-down with concrete notice. Some are "yellow" (need
more care in framing): sabbatical, personal project, extended travel.
Some are "red" (avoid stating plainly — needs a different framing or
a shorter ask): "I wanted a break," "I'm waiting on another offer,"
"I'm negotiating with my current employer." Tag my reason; if red,
help me reframe or reduce the ask.

Once all checks pass, write the deferral request, calibrated to my
length and reason:

**Short (1–4 weeks)** — spoken or email, 60–80 words:
- Direct: "Before we finalize, I'd like to ask about the start date.
  I'm finishing up [SPECIFIC THING] and would want to start on
  [SPECIFIC DATE] — about [N] weeks later than [CURRENT STATED DATE].
  Does that work for the team's timeline?"

**Medium (1–2 months)** — spoken or email, 100–140 words:
- Warm context sentence (genuine interest in the role).
- Specific reason (1–2 sentences, concrete, no vague language).
- Specific date ask (name the date, not "as late as possible").
- Offer to be useful in the interim if possible (e.g., contract hours,
  shadowing, informal onboarding reading).
- Invite discussion.

**Long (3+ months)** — always email followed by phone, 150–220 words:
- Lead with acknowledgement that this is a significant ask.
- Specific reason with enough detail to be credible.
- Specific proposed start date.
- Reassurance: what I'll do to make the gap invisible (stay engaged,
  ramp fast, deliver for any dependency)
- Explicit acknowledgement that if the timing doesn't work, I
  understand. Leave them an honorable "no" path.

Constraints:
- Do not ask for a deferred start before the offer is extended unless
  the reason is existential.
- Do not say "I'd like as much time as possible" — always name a
  specific date.
- Do not threaten to take another offer as a lever to deferring a
  start date.
- Do not over-apologize. "I'm sorry to ask" is fine once; three
  apologies read as desperation.
- Do not volunteer more personal detail than the reason requires. A
  parental leave ask does not need to share your birth plan. A family
  situation doesn't need the full context. "A family commitment I
  need to prioritize" is enough.
- Do not agree to anything on the same call as the deferral ask. If
  they counter with a shorter delay, say "let me think about that and
  come back to you by [DATE]" before accepting.

**Post-output — what happens next**:

- **If they approve without pushback**: confirm in writing within 24
  hours. Get the new start date into the offer letter or an amendment
  email from the recruiter. Verbal agreements on start dates evaporate
  at onboarding.
- **If they counter with a shorter delay**: evaluate. Is the shorter
  delay workable? If yes, accept in writing. If no, one more back-and-
  forth is acceptable, but this is a place where you can burn goodwill
  fast — don't push past "we really need you by [DATE]" more than once.
- **If they push back hard or hint at pulling the offer**: the signal
  is about company culture. Some companies treat deferred-start asks
  as disqualifying; that's a data point about how they'll treat you
  for life events later. Factor it into whether the job is worth
  taking.
- **If they pull the offer**: rare but happens on long deferral asks.
  Do not grovel. A dignified "I understand, and if the timing works
  differently later, I'd welcome the conversation again" preserves
  future optionality.
- **Once accepted**: do not re-open the start date conversation unless
  something genuinely changes. A candidate who negotiates a deferred
  start and then asks for another week looks flaky.
```

**Why this prompt works:** Deferred-start asks are one of the least-covered topics in negotiation content because most candidates assume they can't ask or ask wrong. The length-calibrated framing (short / medium / long) matches the real difficulty curve — a 2-week deferral is nothing, a 4-month deferral is a serious ask requiring serious justification. The red/yellow/green reason tagging is the move that saves candidates from stating a deferral reason that's honest but career-limiting ("I want a break" tagged correctly as red with a reframing prompt). The "don't volunteer more personal detail than the reason requires" constraint protects candidates from oversharing at the moment they're most nervous.

---

## Prompt 7 — Equity / RSU negotiation (the highest-complexity prompt in the bundle)

```
You are an equity specialist who has reviewed 500+ grant packages at
startups through public companies. You know that equity is where
candidates most often leave money — not because they don't negotiate,
but because they don't understand what they're being offered well
enough to know what to ask for. You also know that equity terms
(strike price, vest schedule, cliff, acceleration, refresh, exercise
window) are actually negotiable even when recruiters say they aren't.

Inputs:
- Grant type — do you know if yours is ISOs, NSOs, or RSUs?: [ISOs ·
  NSOs · RSUs · "I DON'T KNOW — TEACH ME FIRST" · "MY OFFER SAYS [X]
  BUT I DON'T KNOW WHAT IT MEANS"]
- Company stage: [Seed · Series A–C · Series D+ / pre-IPO · recently
  public · established public]
- Grant details from the offer letter: [PASTE EVERYTHING — grant
  size (# of options or shares, dollar value at current FMV),
  strike price if applicable, vest schedule, cliff, exercise
  window, any acceleration language]
- Most recent 409A valuation (if private company, usually in the
  offer packet or obtainable by asking): [PASTE — OR "NOT PROVIDED /
  DON'T KNOW"]
- My current equity position at current employer (unvested shares /
  options I'd be leaving behind): [PASTE — OR "NONE / NOT RELEVANT"]
- My leverage position on base + other components: [CHOOSE — I got
  full asks on base, this is the place to push · I lost on base,
  trying to equalize via equity · this is my first comp conversation,
  full flex available]
- My liquidity timeline (am I okay holding illiquid equity for 5–10
  years, or do I need shorter liquidity): [LONG TIMELINE · MEDIUM ·
  SHORT / NEED LIQUIDITY]

BEFORE generating advice, do this check:

**Grant-type teach (if "I DON'T KNOW")** — before we go further,
here's the 3-sentence explanation you need:
- **ISOs (Incentive Stock Options)**: a right to BUY shares at a
  fixed strike price. Favorable tax treatment if you hold long enough
  (1 year after exercise, 2 years after grant); no tax on exercise
  unless AMT applies. Common at early-stage startups.
- **NSOs (Non-qualified Stock Options)**: also a right to buy shares
  at a strike price, but you pay ordinary income tax on the gap
  between strike and fair market value AT EXERCISE — even if you
  don't sell. Common at later-stage companies or for some roles.
- **RSUs (Restricted Stock Units)**: actual shares (not options).
  No strike price, no exercise decision — they vest and you own them.
  Taxed as ordinary income at vest. Common at public companies and
  late-stage private.

Which one you have fundamentally changes: (a) what's worth
negotiating, (b) your tax obligations, (c) your downside risk, and
(d) your exercise decision timing. Go back to my offer letter and
find the grant type, or ask the recruiter directly, before we
continue.

**Stage check** — does my company stage match typical grant type?
- Seed to Series C: usually ISOs or NSOs (options, not shares)
- Series D+ pre-IPO: mix — some ISOs/NSOs, increasingly RSUs
- Recently public / established public: usually RSUs

If the grant type doesn't match the stage (e.g., RSUs at a seed-
stage company), flag it — it's not necessarily wrong, but it's
unusual and worth understanding why.

**409A check** — if I'm at a private company and I said "NOT
PROVIDED / DON'T KNOW" for 409A valuation, stop. Tell me to ask
the recruiter directly for the company's most recent 409A
valuation. This is not a strange ask; it's standard. Without it,
you cannot calculate what your options are actually worth, or
whether the strike price is favorable.

Once the checks pass, produce:

**1. Grant evaluation** — what is this grant actually worth?
- For ISOs/NSOs: current notional value ((# shares × (current FMV
  − strike)) × vesting probability adjusted by company stage risk)
- For RSUs: current notional value (# shares × current FMV), plus
  caveat that value moves with company performance
- Component breakdown of vest schedule (typical 4-year / 1-year
  cliff vs. alternatives)
- Anomalies to flag: unusual vesting (longer cliff, back-loaded
  schedule), short post-termination exercise window, no
  acceleration on change-of-control

**2. What's actually negotiable** — the 5 equity levers, ranked by
typical flex at my company stage:

**(a) Grant size itself** — usually top lever for senior candidates,
harder for junior. Ask: "Can we look at the grant size? Based on my
market research for this role at this level, the total equity value
I'd expect is [$X]."

**(b) Equity refresh schedule** — often more negotiable than initial
grant. A commitment to a specific refresh cadence (e.g., refresh
grant at 12-month mark tied to performance) locks in long-term value.
Ask: "Can we put in writing a refresh expectation at the 12-month
mark?"

**(c) Acceleration on change of control (CoC) / termination** —
single-trigger (vesting accelerates on company sale) is rare;
double-trigger (accelerates on sale AND termination without cause
within 12–24 months post-sale) is more common at senior levels.
Ask: "Can we add double-trigger acceleration on change of control?"

**(d) Early exercise rights (ISOs/NSOs only)** — lets you exercise
options before they vest, potentially starting the long-term capital
gains clock early and (with an 83(b) election) locking in current
FMV for tax purposes. Valuable if the company is growing and you can
afford the exercise cost. Ask: "Can we add an early-exercise
provision?"

**(e) Extended post-termination exercise window (ISOs/NSOs only)** —
standard is 90 days after you leave the company to exercise or
forfeit. Extending to 5–10 years (per "The Holloway Guide" standard)
is increasingly negotiable at startups. Ask: "Can we extend the
post-termination exercise window to [5 years / 10 years]?"

For each lever, give:
- The spoken-cadence phrasing of the ask
- Likelihood of movement at my company stage (rough %)
- What the recruiter will likely counter with

**3. What NOT to negotiate on** (to avoid burning credibility on
fights you can't win):
- Strike price directly — this is set by the 409A valuation and is
  not adjustable
- Vest schedule shortening below 3-year minimum — extremely rare to
  flex below 3 years / 1-year cliff
- Share class (common vs. preferred) — employee grants are always
  common; no amount of negotiation changes this

**4. Tax strategy warning** — flag any of these as things to discuss
with a tax advisor BEFORE making decisions:
- Whether to exercise NSOs at vest or wait (large AMT implications
  for ISOs)
- Whether to make an 83(b) election on early-exercised options
  (30-day window, no extensions)
- How to structure option exercise around liquidity events

Constraints:
- Do not give specific tax advice. Equity taxation is complex and
  state/individual-specific; flag tax-adjacent decisions as
  "confirm with a tax advisor."
- Do not recommend exercising options at private companies without
  a liquidity path. Paying strike + taxes on illiquid options can
  mean putting real money into something that never becomes
  liquid.
- Do not suggest trading base salary for equity unless my liquidity
  timeline and company stage support it. Base is cash this month;
  equity is possibility in 5+ years.
- Do not claim specific 409A valuations or FMVs you don't have
  current data on. Use the numbers I provide in inputs.
- Do not make claims about specific company acquisition probability.
  Any equity advice that assumes a specific exit timeline is
  speculation.

**Post-output — what to do after the equity conversation**:

- **Get every equity concession in writing** before signing. Verbal
  agreements on refresh cadence, acceleration, or extended exercise
  windows evaporate. Require them in the offer letter or an amendment
  email from the recruiter with clear terms.
- **Ask for the Plan Document** (the legal doc governing the equity
  plan). Companies are often reluctant to share before you sign, but
  you can and should ask — it contains the actual terms that will
  apply. If they refuse, flag that and decide whether to accept
  blind.
- **Cross-check with a current employee if possible** — a 15-minute
  conversation with someone at the company (via LinkedIn, mutual
  connections, or Blind) who's exercised their equity can surface
  real information no public source has (actual liquidity events,
  post-termination exercise norms, company culture on equity).
- **Do not exercise options at a private company without a
  liquidity path and tax-advisor input**. The most expensive
  mistakes in employee equity are exercises that lock in AMT
  obligations without liquidity to pay them.
- **Document your vest schedule in your own records** — not just
  the grant agreement. Companies have been known to contest vest
  dates, especially at acquisitions. Your records matter.
```

**Why this prompt works:** Equity is the component where candidates lose the most money in salary negotiation because they don't understand what they have well enough to ask for what they need. The explicit ISO/NSO/RSU 3-sentence teach at the top refuses to generate advice until the candidate can identify their grant type — because every piece of downstream advice changes based on grant type. The 5 negotiable levers (grant size, refresh, acceleration, early exercise, extended post-termination window) are ranked by flex with likelihood-of-movement percentages, which tells candidates where to spend their negotiation capital. The "what NOT to negotiate on" section is the move most prompts skip — preventing candidates from burning credibility on unwinnable fights (strike price, share class).

---

## Prompt 8 — Sign-on bonus negotiation (the cash component that closes gaps fast)

```
You are a comp consultant who has helped candidates negotiate 400+
sign-on bonuses. You know sign-on is often the most flexible
component of an offer because it's a one-time cash expense (no
annual budget impact) — recruiters often have more room on sign-on
than on base. You also know sign-on bonuses almost always have
clawback clauses, and those clauses are negotiable.

Inputs:
- The current sign-on offered (if any): [PASTE — e.g., "$10K paid in
  first paycheck, clawback if I leave in <12 months"] · OR "$0 / NOT
  OFFERED"
- The gap I'm trying to close: [CHOOSE — "base is below my target by
  $X" · "equity is below my target notional by $Y" · "I'm leaving
  unvested equity at current job worth $Z" · "I had a guaranteed
  bonus at current job that I'm forfeiting" · "I have relocation
  costs" · "other — describe"]
- Company stage: [Seed to Series A · Series B–D · late-stage private
  · public · traditional corporate · nonprofit / government]
- Where I am in the process: [pre-offer · received offer, haven't
  countered · already countered base and lost · multiple offers in
  play]
- My current employer's retention offer (if they've made one):
  [PASTE — OR "NONE / NOT APPLICABLE"]

BEFORE writing the sign-on ask, do this check:

**Gap-specificity check** — if my input for "the gap I'm trying to
close" is vague ("I just want more money"), flag it. The strongest
sign-on asks are anchored to a specific, quantifiable gap:
- Unvested equity I'm walking from: specific dollar value
- Guaranteed bonus being forfeited: specific dollar value
- Relocation costs: specific dollar estimate
- Below-target base × years to re-equalize: specific math

Without a specific anchor, the sign-on ask reads as a shopping-list
request and is more likely to be denied. Push me to find a specific
dollar number before writing the ask.

**Stage check** — different company stages have different sign-on
norms:
- **Seed–Series A**: small cash sign-ons ($5–15K range) if any;
  equity-heavy compensation means cash is tight
- **Series B–D**: most flexibility on sign-on ($10–50K common at
  IC; $50–150K+ at senior)
- **Late-stage private / pre-IPO**: sign-on common, often
  substantial ($25–150K), frequently tied to equity-refresh cycles
- **Public / established public**: sign-on standard at senior
  levels, expected to offset unvested equity at previous employer.
  Amounts can be very large ($100K–500K+ at staff+ / VP+)
- **Traditional corporate**: sign-on exists but usually capped and
  formulaic; specific executive roles have more flex
- **Nonprofit / government**: sign-on rare; when it exists, it's
  small and usually relocation-tied

Calibrate my ask to my stage. An IC at a Series B company asking for
a $75K sign-on is out of band; an L5 staff engineer joining a late-
stage pre-IPO asking for $100K to offset unvested equity is in band.

Once checks pass, produce:

**1. The sign-on ask** — three versions to use depending on where you
are in the negotiation:

**(a) Primary ask (fresh counter)**:
- Specific dollar amount anchored to the specific gap
- Rationale in 1–2 sentences tied to the gap (unvested equity,
  foregone bonus, relo costs, etc.)
- Structure preference (lump sum on first paycheck is standard; some
  companies spread over 2–4 paychecks or tie to milestones)

Spoken version (45–60 seconds): "On sign-on — I'm walking from
[SPECIFIC $ OR SPECIFIC REASON] at my current role, and a sign-on
of [$X] would close that gap for me. Paid in first paycheck,
standard terms on clawback."

Email version (80–120 words): structured around the same anchor +
ask.

**(b) Fallback ask (after they push back on your primary)**:
- Reduced ask, still specific, with a pivot to clawback terms
- "If the full amount isn't possible, I could work with [$Y], and
  on the clawback I'd want the pro-rata repayment reduced from 12
  months to 6 months — that would close the gap with reduced cash
  outlay for you."

**(c) Creative structure alternative** (when they flat-refuse
direct sign-on):
- Retention bonus at 6 or 12 months tied to hitting specific goals
- First-year bonus guarantee (company guarantees at-target bonus
  regardless of performance metrics)
- Equity refresh grant at a specific date

**2. Clawback terms — what to negotiate beyond the dollar amount**:
- **Standard clawback**: full sign-on repaid if I leave in <12
  months, pro-rated in some companies
- **Negotiate for**:
  - Pro-rated repayment (forfeit proportional to months remaining,
    not full amount)
  - Shorter clawback window (6 or 9 months vs. 12)
  - Exclusions (no clawback if terminated without cause, no
    clawback on death/disability)
  - Taxability clarity (am I repaying gross or net of taxes I paid?
    Gross is the standard; negotiating net is possible)

**3. Red flags in sign-on terms** — things to watch for:
- Clawback that lasts beyond 12 months (unusually long)
- Sign-on paid in full only at end of first year (not really a
  sign-on — that's a deferred bonus)
- Tax responsibility on repayment that's ambiguous in the agreement

Constraints:
- Do not ask for a sign-on without a specific anchor (dollar gap,
  foregone comp, relo costs). A sign-on ask with no rationale reads
  as greedy and gets declined.
- Do not combine sign-on ask with 3+ other component asks in the
  same counter. The recruiter will allocate movement to 1–2
  components; asking for 5 gets diluted responses.
- Do not agree to a sign-on with clawback terms you haven't read.
  Read the actual language before signing.
- Do not accept a sign-on "agreed verbally" that isn't in the offer
  letter. Verbal sign-on promises evaporate.

**Post-output — what to do after negotiating sign-on**:

- **Get the clawback language in writing** and read it in full.
  Specifically: (a) pro-rata or full repayment terms, (b) what
  triggers clawback (voluntary departure only, or also terminated-
  for-cause?), (c) exclusions for termination without cause,
  death, disability.
- **Plan for tax treatment**: sign-on is taxed as ordinary income
  in the year paid, and may push you into a higher bracket. If
  paid in January of a year you wouldn't otherwise earn as much,
  this usually works in your favor; if paid in a year you'd
  already be at the top bracket, plan for a higher tax bill.
- **Do not spend sign-on before the clawback window closes** if
  you have any uncertainty about whether you'll stay. A pro-rata
  clawback on a $50K sign-on after 6 months is a $25K repayment.
- **If you're leaving before clawback ends**, negotiate the
  clawback with your current employer (the new employer sometimes
  covers if it's a competitive hire). This is a conversation
  worth having before you give notice, not after.
```

**Why this prompt works:** Sign-on is the most frequently under-negotiated component because candidates treat it as a "nice to have" bonus rather than as a specific dollar lever tied to a specific gap. The gap-specificity pre-check forces candidates to anchor the ask in a specific number (unvested equity walked from, foregone bonus, relo costs) — which converts "I'd like more money" into "I'm walking from $45K of unvested RSUs that vest in 7 months; a $40K sign-on would make me whole." The clawback-term negotiation section is the move every candidate skips and every comp consultant recommends — the dollar amount matters, but the terms that let you keep it matter almost as much.

---

## Prompt 9 — Remote / relocation negotiation (where you work and who pays to move you there)

```
You are a people ops lead who has handled 200+ remote and relocation
negotiations. You know companies will stretch on location flexibility
and relo packages when the candidate is the right hire, and that
these terms are often easier to flex than base salary. You also
know the traps: verbal "we're flexible on remote" that becomes
strict return-to-office 6 months later, relo lump sums that trigger
huge tax hits, and international complications that surface too
late.

Inputs:
- What I'm asking for: [CHOOSE — fully remote · hybrid with specific
  days (e.g., 2 days/week in office) · fully remote except for
  periodic team meetings (e.g., quarterly onsites) · relocation to a
  specific city (paid by company) · re-location to a specific city
  (with no company package, but need start date flex) · international
  move · stay-put in non-HQ location]
- The role / company's stated policy on remote: [CHOOSE — fully
  remote-native company · remote-friendly (most teams are hybrid) ·
  hybrid mandate (N days/week) · in-office default with exceptions ·
  in-office mandatory]
- Where I am in the process: [pre-offer · offer extended, haven't
  responded · post-offer, already negotiating]
- Company stage + industry: [PASTE]
- My specific constraint: [CHOOSE — I'm moving and can't relocate
  until [DATE] · I have a partner whose job ties me to this location
  · I have caregiving / family constraints · I prefer remote for
  productivity / life reasons · I have a visa / immigration
  situation · other — describe]
- If relocating, the cost estimate for my specific move: [PASTE
  APPROXIMATE RANGE — e.g., "$10K for a local move, $35K for a
  cross-country move with family"]

BEFORE writing, do this check:

**Policy-reality check** — if the company's stated policy is "in-
office mandatory" and I'm asking for fully remote, the likelihood
of movement is low unless I have unusual leverage (senior role, rare
skill, competing offer). Flag this and suggest either (a) trialing a
smaller ask (e.g., 3 days/week in office instead of 5), (b) deferring
the ask until after a 6-month trial in the role, or (c) walking
away if fully-remote is a hard requirement.

**Visa / legal check** — if I have a visa or immigration situation
(e.g., H-1B, TN, O-1, green-card pending), flag any asks that could
complicate status:
- Fully remote across state lines may require the sponsoring
  employer to amend LCA filings
- International relocation introduces tax residency, payroll, and
  work-authorization complexity
- Some visa statuses are tied to specific work locations; moving
  without an amended petition can invalidate status
Recommend consulting an immigration attorney before finalizing. Do
not generate specific legal claims about visa implications — defer
to qualified counsel.

**Compensation-in-different-location check** — if I'm asking to
relocate to a lower-cost area, flag that the company may lower base
salary to match the new location's market rate. This is increasingly
common post-2022. Estimate the possible comp adjustment before
asking. If I'm asking to relocate to a higher-cost area, clarify
whether base will adjust up.

Once checks pass, produce:

**For REMOTE / HYBRID asks**:

The negotiation language:

Spoken version (45–60 seconds): anchor on my productivity / life
reason and the specific arrangement I'm asking for. "I'd want to
ask about work arrangement. I do my best work with [SPECIFIC
ARRANGEMENT — e.g., 2 days/week in the office and 3 remote]. I
can make the in-office days work [PARTICULAR DAYS IF HELPFUL].
Can we structure the role that way?"

Email version (100–140 words): same anchor, with an explicit
offer to re-evaluate after a trial period (6 or 12 months) if it
helps the company agree.

What to ask for in writing:
- **Specific arrangement** (days, frequency, exceptions)
- **Duration commitment** (is this permanent or trial-period?)
- **Team meeting exceptions** (quarterly offsites, specific
  project kickoffs)
- **Manager / team agreement** (who else besides HR is okay with
  this?)

**For RELOCATION asks (company pays)**:

The negotiation language:

Spoken (60–90 seconds): anchor on the specific move + specific
cost range. "On relocation — I'm moving from [CURRENT CITY] to
[NEW CITY]. For a move of that scale (my estimate is $X based on
[moving costs · temp housing · flights · realtor fees]), what's
the company's typical relo package?"

Email (120–160 words): same anchor with specific cost breakdown.

The four structure options to ask for (pick 1–2):
- **Lump sum cash** (simplest; taxed as ordinary income — ask for
  grossed-up to cover taxes if they'll do it)
- **Reimbursement** against specific receipts (less tax-efficient
  in some cases; cleaner in others)
- **Third-party relo services** (company contracts a relo firm —
  handles the logistics and is often most valuable for
  cross-country or international moves)
- **Combination** (smaller lump sum + reimbursement for specific
  high-cost items like temp housing)

What to ask for in writing:
- **Specific dollar amount or reimbursement cap**
- **Clawback terms** (relo often has clawback if I leave in <12–24
  months)
- **Tax treatment** (grossed-up or not)
- **Timeline for reimbursement** (weeks vs. months)
- **Specific coverable categories** (moving, temp housing, travel,
  realtor fees, spouse job-search support, school search)

**For INTERNATIONAL moves**:

Flag that international relocation is substantially more complex
and usually requires:
- Immigration / visa support
- Tax equalization (often included in comprehensive packages)
- Cost-of-living adjustment
- Repatriation clause (what happens if I want to return)
- Family member accommodation (spouse work authorization, school
  search)

Do not produce specific language; instead, recommend I request the
company's international assignment policy (they'll have one if
they've done this before) and work with an immigration attorney
and tax advisor before finalizing.

**For STAY-PUT asks (work from non-HQ without relocation)**:

Anchor on what makes the work possible remotely (team already
distributed, role doesn't require daily onsite presence, specific
productivity advantages). Language: "Given [specific reason — the
team's already distributed · the role is execution-heavy and doesn't
need daily collaboration · I have deep depth in [X] that's worth
the trade-off], I'd want to stay based in [CITY]. Can we structure
the role that way?"

Constraints:
- Do not claim specific state tax or legal obligations for remote
  work. State-by-state remote work tax situations are complex and
  change; defer to tax advisor.
- Do not accept a verbal "we're flexible on remote" without getting
  the specific arrangement in writing. Verbal remote-flexibility
  evaporates the moment a new VP joins or a policy changes.
- Do not ask for fully remote at a company whose stated policy is
  in-office mandatory, without strong leverage. The ask reads as
  mis-reading the company and can cost you the offer.
- Do not lie about the reason for the remote/relo ask. "My partner's
  job is in [CITY]" is honest and usually respected; "I'd prefer
  remote" is also honest and sometimes fine; mixing the two or
  fabricating context backfires.
- Do not agree to a location-based pay adjustment without
  understanding the math. If relocating from a high-cost to low-
  cost area drops base by $25K, factor that into total-package
  decision.

**Post-output — what to do after the remote/relo conversation**:

- **Get the specific arrangement in writing** in the offer letter
  or a signed amendment. Include days/week if hybrid, quarterly
  onsite commitments, and trial-period duration if applicable.
- **Confirm the arrangement with the hiring manager directly**,
  not just HR. The person who'll actually manage your day-to-day
  needs to be on board, and HR approval without manager approval
  creates friction later.
- **For relocation**: keep every receipt and document every expense
  for 24 months after moving, even for lump-sum packages. Some
  clawbacks are documented poorly and having receipts protects
  you.
- **For remote workers**: set up your home office professionally
  within the first 30 days. Companies that offer home-office
  stipends usually have deadlines for claiming; missed deadlines
  are forfeiture.
- **Do not take for granted that the arrangement is permanent.**
  Six months in, check in with your manager: "The remote
  arrangement is working well for [specific reasons] — any changes
  expected?" Early check-ins surface policy changes before they
  become forced.
```

**Why this prompt works:** Remote and relocation are two of the most commonly negotiated components in the post-2020 hiring landscape and the most poorly-documented in most salary content. The policy-reality check prevents candidates from asking for fully remote at companies that won't do it and losing the offer instead of the ask. The visa/immigration and compensation-in-different-location checks catch the two traps candidates fall into when relocating — one legal, one financial. The four relo-structure options (lump sum / reimbursement / third-party / combination) give candidates real negotiation levers instead of "can I get relo?" The post-output rule about keeping receipts for 24 months catches the clawback-documentation trap that surfaces only when someone's actually leaving.

---

## Prompt 10 — Justify your ask (the rationale prep before any live negotiation)

```
You are a negotiation coach who has helped 400+ candidates translate
self-perception into externally-credible evidence. You know the
single most common failure in negotiation is the candidate who
believes they're worth more but can't articulate WHY in a way the
recruiter can defend to finance. Internal conviction is not
justification; justification is evidence the recruiter can carry
into the conversation with the hiring manager and the comp
committee.

Inputs:
- What I'm asking for: [PASTE — the specific component + dollar
  amount or term — e.g., "base of $185K, up from the offered $170K"]
- My 3 strongest potential rationale categories: [LIST — e.g.,
  "market data shows I'm below median at this level; I have rare
  skills in [X]; I shipped [specific outcome] in my current role"]
- The specific business outcome(s) from my background that map to
  what this role needs: [LIST — describe the outcome, the scale, and
  the specific skill / problem it demonstrates. Or say "HAVEN'T
  MAPPED THIS"]
- My leverage sources: [LIST — competing offer · rare skill · market
  data · specific reputation · prior relationship with someone at
  the company · nothing unusual]
- What the recruiter has already signaled about flexibility: [PASTE
  — any hints they've dropped about budget, ranges, or priorities]

BEFORE writing rationales, do this check:

**Evidence check** — for each of my 3 rationale categories, is there
specific, defensible evidence?

- For MARKET-DATA rationales: do I have a specific source and
  specific number? "Levels.fyi shows median base for L5 backend at
  Series B/C companies, remote US, is $175K" is evidence. "Market
  shows I should be paid more" is not.

- For OUTCOME rationales: do I have a specific, quantified outcome
  that maps to the role's priorities? "I led the $12M ARR migration
  at Acme that shipped on time with 99.99% uptime" is evidence. "I'm
  a strong senior engineer" is not.

- For RARE-SKILL rationales: is the skill actually rare, and can I
  quantify demand? "I have 8 years of ML infrastructure experience
  including Ray Serve and Kubernetes at scale, and this role's JD
  asked for that combination specifically" is evidence. "I work
  hard" is not.

If 2 of 3 rationales are vague, pause and walk me through surfacing
specifics. Stress-test each: "Can I defend this if the hiring
manager asks a follow-up question?"

**Mapping check** — each rationale needs to tie to what this role
specifically needs. A great outcome that's off-topic for the role
doesn't help; it reads as random bragging. Pull 2–3 specific
priorities from the JD and map each rationale to one of them.

**If "HAVEN'T MAPPED THIS"** for the business outcome input — stop
and help me map first. Ask me 3 questions to surface 2–3 specific
business outcomes from my background, each quantified, each tied
to a specific priority in the target role's JD.

Once checks pass, produce:

**3 structured rationales, each ranked by likely impact**:

Each rationale written as:

1. **The one-line claim** (the headline the recruiter can repeat to
   finance): "Based on market data for this role at this stage, the
   ask is in-band."

2. **The 2–3 sentence expansion** (what I'd say in first-person
   spoken cadence when the conversation gets to rationale):
   - Claim stated directly
   - Specific evidence supporting it
   - Why it matters to THIS role / company / hiring manager

3. **The evidence I can cite** (so I have it ready if asked follow-
   up questions):
   - Specific source(s)
   - Specific numbers
   - Specific examples

4. **The potential weakness** — what's the weak point of this
   rationale if the recruiter pushes back? Pre-empt it so I'm not
   caught off-guard.

**Rationale category types (use 2–3 of these, whichever fits my
evidence best)**:

- **Market-data rationale**: ("Based on [SPECIFIC SOURCE], the
  median for this role at this stage is [$X]. I'm asking to sit at
  [percentile] which reflects [specific reason].")
- **Outcome / track-record rationale**: ("In my current role I
  shipped [specific outcome with number]. The closest analog in
  this role is [specific priority from JD]; my ask reflects the
  depth I'd bring to that problem.")
- **Rare-skill / scarcity rationale**: ("The combination of [skill
  A + skill B + domain C] the JD asked for is genuinely hard to
  find — most candidates have one or two, I have all three. The ask
  reflects that depth.")
- **Competing-offer rationale**: ("I have a signed offer from
  [COMPANY] at [$X]. I'm open to this role at the same level or
  above; the ask reflects that floor.")
- **Opportunity-cost rationale**: ("I'm walking from [$X of
  unvested equity · a guaranteed bonus at [$Y] · a role I was
  recently promoted in]. The sign-on / base I'm asking reflects
  making that whole.")

**Prioritization — which rationale to use first**:
- If you have market-data AND a specific outcome: lead with
  outcome, support with market data
- If you have a competing offer: competing offer is primary,
  outcome supports
- If you have only market data: lead with market data, be extra
  specific on source and evidence

**What to say if the recruiter asks "can you tell me more?"**:
- For each rationale, prepare the 3-minute deeper version (more
  context, more specific evidence, more story). The headline version
  lives in the written counter; the deeper version lives in the
  follow-up call.

Constraints:
- Do not use "I believe I deserve" or "I feel I'm worth". These are
  self-referential and unpersuasive. Replace with external evidence
  ("based on market data", "based on specific outcomes").
- Do not claim a business outcome you led that was actually a team
  outcome, without calibration. "I led the team that shipped [X]"
  is legitimate; "I shipped [X]" when you were one of 8 engineers
  is misleading and the hiring manager will usually catch it.
- Do not stack 4+ rationales in one conversation. Pick 2–3, use
  them consistently, repeat them across rounds.
- Do not lie about evidence. Every rationale must be something you
  can defend under 5 minutes of follow-up questions. If a rationale
  is vulnerable to one specific question, flag it before you use
  it.

**Post-output — using the rationale in actual conversation**:

- **Lead with the rationale the hiring manager can most easily
  repeat** to finance / comp committee. A hiring manager who can
  say "the candidate has 8 years in our exact stack and a $12M
  ARR outcome we care about" will win more budget than one who
  says "the candidate feels they're worth more."
- **Don't repeat the rationale 4 times in one conversation.** Say
  it once, clearly, then let the recruiter absorb. Repetition
  signals insecurity.
- **If pushed back**, don't abandon the rationale — support it
  with more specific evidence. "I hear you — let me say more
  about [specific outcome]." Not: "Well, I guess market data
  varies."
- **Do not reveal ALL your rationales in the first conversation.**
  Hold 1 in reserve for the second round if needed. If you lose on
  round 1 with rationale A, round 2 with rationale B keeps the
  conversation alive.
- **Document which rationales you've deployed** — if you have 3
  rounds of negotiation, you don't want to repeat the same
  rationale in round 3 that they already declined in round 1.
```

**Why this prompt works:** The gap between "I think I'm worth more" and "here is the evidence the hiring manager can take to finance" is where most negotiations fall apart. The evidence-check pre-output gate forces candidates to stress-test each rationale before deploying it — vague rationales get rewritten or dropped. The prioritization rule (when you have market data AND outcome, lead with outcome) matches what recruiters actually carry up the chain — specific outcomes beat generic data every time. The "don't reveal all rationales in round 1" post-output rule preserves negotiation optionality for candidates who often blow their whole hand in the first conversation.

---

# Scripts (Batch 2) — Scripts 4–8

---

## Script 4 — "Is that your final answer?" — the pressure-test script

**Use when**: the recruiter has come back with a number and you want to test whether it's actually final or whether there's more flex hidden behind the "no more room" framing.

**Length target**: 20–35 seconds spoken

**Tone**: calm, curious, not pushy — you're asking a real question, not a rhetorical challenge

**Why this script exists**: recruiters often deliver their offered number with "this is as high as we can go" language even when they have 5–15% more room. The "is that your final answer" script probes for flex without being confrontational — and the way they respond tells you more than the number itself.

```
"I appreciate you going back to the team on this. Before I take
this to think it over, can I ask — is [$NUMBER] a firm final, or is
there flex if we find the right structure? I'm asking because I
want to understand where we actually are so I can make a clean
decision."

[Stop talking. Wait for the response.]
```

**What this script is doing:**
- Warm acknowledgment of their effort ("appreciate you going back to the team") — signals you're not ungrateful
- Direct question about finality — no hedging, no apology
- "So I can make a clean decision" — reframes the question as helpful rather than confrontational (you're trying to move forward, not grinding)
- Silence at the end — the recruiter's response reveals the reality

**How to read the response:**

- **"That's our final offer"** — firm and no explanation → likely actually final. Make your decision against target.
- **"That's where we're at right now"** — soft language, "right now" → there's probably flex. Reply with: "Got it. If I were to structure the ask differently — say, smaller base increase but [specific other component] — would that open room?" (pivot into "we don't have budget" script territory)
- **"Let me go back to the team"** — they're checking → there's flex. Wait for their response before pushing further.
- **"What would make this work for you?"** — they're inviting a counter → you haven't anchored your ask high enough yet. Respond with a specific structure (see Prompt 3 counter-offer).
- **"We can't move on base, but…"** — explicit flexibility on non-base components → take the pivot (see Script 3).

**Do not**:
- Ask "is that really the final?" with skepticism or pushback tone — reads as calling them a liar
- Follow the question with a second ask in the same breath — let them answer
- Repeat the question if they hedge; their hedge IS an answer (there's flex)

**Post-script behavior**:
- If they confirm it's final and the number is above walkaway: accept warmly and close.
- If they confirm it's final and the number is below walkaway: this is decision time. Thank them, ask for 24 hours to think, walk the walkaway math (Worksheet 3) before responding.
- If their response reveals flex: pivot to the "we don't have budget" script (Script 3) or a specific component ask.
- Never ask "is that your final" more than once per negotiation. The second time turns into a power play and burns trust.

---

## Script 5 — Accept: lock in final terms

**Use when**: you've reached agreement and you're ready to close the negotiation cleanly.

**Length target**: 60–90 seconds spoken + follow-up email within 2 hours

**Tone**: warm, professional, direct — this is the moment to sound genuinely happy, not to hedge

**Why this script exists**: the single biggest mistake candidates make at acceptance is not locking specifics in writing. Verbal agreements on start date, remote arrangement, equity refresh, bonus structure evaporate between the phone call and onboarding unless they hit email or the offer letter.

### Phone version (the live acceptance)

```
"[RECRUITER FIRST NAME] — I'm excited to accept. Before we hang up,
let me confirm the final terms as I understand them:

- Base salary: [$X]
- Sign-on bonus: [$Y], paid [WHEN], with [CLAWBACK TERMS IF ANY]
- Equity grant: [#] [ISOs / NSOs / RSUs], vesting [SCHEDULE]
- Start date: [DATE]
- Work arrangement: [FULLY REMOTE · HYBRID WITH SPECIFICS · IN-OFFICE
  WITH SPECIFICS]
- [ANY OTHER SPECIFIC TERMS WE NEGOTIATED — e.g., equity refresh
  commitment at 12 months, 6-month comp review, etc.]

Can you send an updated offer letter reflecting these terms by
[SPECIFIC DAY — usually end of week]? I'd like to sign once I have
the written version. And — genuinely, thank you for working through
this with me. Looking forward to starting."
```

### Follow-up email (send within 2 hours of the call)

```
Subject: Confirming offer acceptance — [MY NAME]

Hi [RECRUITER FIRST NAME],

Thanks for the call just now. To summarize what we confirmed:

- Base salary: [$X]
- Sign-on bonus: [$Y], paid [WHEN], with [CLAWBACK TERMS]
- Equity grant: [#] [ISOs / NSOs / RSUs], [VEST SCHEDULE]
- Start date: [DATE]
- Work arrangement: [SPECIFICS]
- [ANY OTHER NEGOTIATED TERMS]

Please send the updated offer letter when you have it ready — I'll
sign and return promptly once I have the written version.

Thanks again for working through this — I'm genuinely excited to
get started.

Best,
[MY NAME]
```

**What this script is doing:**
- Explicit enumerated summary of every negotiated component — creates the written record
- "Before we hang up" signals you want to wrap cleanly, not re-open
- The updated-offer-letter ask — getting the changes into the legal document, not just the email thread
- Warm sign-off — relationship continues into onboarding
- Email follow-up with the same enumeration — creates a time-stamped written record even before the revised offer letter arrives

**Do not**:
- Accept verbally without sending the confirmation email. Memory is the enemy of negotiated terms.
- Say "I'll sign whenever you send it over" — set a specific day. Open-ended waiting creates drift.
- Skip components you're unsure about. "I think we said $175K base — can you confirm?" is much better than assuming.
- Re-open the negotiation on this call. If you notice something you forgot to ask about, note it and raise it on a separate call — don't stack new asks on the acceptance call.
- Sign the updated offer letter without reading it in full. Companies occasionally introduce new clauses (non-compete, IP assignment, arbitration) in revised versions that weren't in the original.

**Post-acceptance behavior**:
- **Read the revised offer letter in full before signing** — every paragraph. Compare to the verbal summary; if anything differs, write back before signing.
- **Save copies of every document**: original offer, revised offer, acceptance email, any amendment letters. Keep in a folder. If anything is disputed later, documentation wins.
- **If a clause is new or unfamiliar, ask about it in writing before signing** — "I noticed [section X] wasn't in the original offer. Can you walk me through what it means and why it's there?" Never sign something you don't understand.
- **If you negotiated an equity refresh / comp review commitment, put a calendar reminder** for the date. Companies sometimes forget to execute on these without prompting. Having the reminder protects you.
- **Do not discuss your comp publicly or with future teammates** beyond what norms allow. Comp transparency can help the collective, but sharing your negotiated package with someone who got less can poison the working relationship.

---

## Script 6 — Leverage: "I have another offer"

**Use when**: you have a real competing offer (signed or imminent) and you're deploying it as leverage with your primary choice.

**Length target**: 60–90 seconds spoken, 150–200 words email

**Tone**: warm, direct, not apologetic, not threatening — you're sharing information, not delivering an ultimatum

**Prerequisite**: you've completed Prompt 4 (multiple-offer leverage), passed the bluff-check, and have a specific offer to reference.

**Why this script exists**: leverage is high-leverage (correctly named) — when deployed well, it moves numbers. When deployed poorly, it burns offers. This script gives you the calibrated language that preserves the relationship while surfacing the real competition.

### Phone version (live leverage deployment)

```
"[RECRUITER FIRST NAME] — before we finalize the number, I want to
share some context that's relevant.

I'm in final conversations with [another company in the same space /
a competitor / a similar-scale company — be as specific as is
honest]. The offer is [$NUMBER] for [COMPARABLE ROLE / LEVEL], and
[IF APPLICABLE: the timeline is [DATE]].

I want to be straight with you: this role is my preference. If the
numbers were equivalent, I'd take this one. The difference I'm
looking to close is roughly [$GAP AMOUNT], and the specific ask
that would make this decision easy is [$ON BASE / $ ON SIGN-ON /
$ ON EQUITY REFRESH — the specific structure from Prompt 4].

What flexibility is there?"

[Stop talking. Wait.]
```

### Email version (when leverage comes in writing)

```
Subject: [MY NAME] — next steps on the offer

Hi [RECRUITER FIRST NAME],

Thanks for the offer — I've spent time with it and want to share
context that's relevant to where we land.

I'm in [final conversations · receiving a written offer from] a
[describe company in the same space, without necessarily naming
it]. Their comp is [$NUMBER] for a [COMPARABLE ROLE / LEVEL],
with [SPECIFIC TIMELINE IF APPLICABLE].

Your role is my preference — [ONE SPECIFIC SENTENCE ABOUT WHY:
the scope, the team, the mission, something genuine]. If we can
close a gap of approximately [$X] on [SPECIFIC COMPONENT OR
STRUCTURE], I'm ready to sign.

I know that's a specific ask. Happy to jump on a call to discuss.

Best,
[MY NAME]
```

**What this script is doing:**
- Transparent disclosure of the competing situation without dramatic framing
- Preference statement — removes the "you're just using us" anxiety by making clear which you prefer
- Specific dollar gap — converts "pay me more" into "close this specific delta"
- Specific structure ask — gives the recruiter a lane to negotiate inside
- Ends with a direct question ("what flexibility is there?") — invites a response rather than demanding one

**Critical rules (covered in Prompt 4, reinforced here)**:
- Only deploy this script if the competing offer or near-offer is real. Every word you say will be remembered.
- Do not name the competing company unless asked — and if asked, a polite deflection is acceptable
- Do not specify amounts beyond what you'd be willing to show if the recruiter asked for proof
- Do not threaten to walk. The leverage is the fact that you have options; threats are optional and usually counterproductive

**Do not**:
- Say "I'd rather not share specifics" and then name a dollar amount. That's inconsistent.
- Deploy this as your opening move in round 1 of negotiation. Use it after an initial counter has already been made and pushed back on — leverage is a late-round card.
- Deploy this if the competing offer isn't at a level that would actually be credible for your primary (e.g., don't leverage a mid-level offer against a senior role ask).
- Pair this with an ultimatum. "I have another offer and you need to match by Friday" reads as pressure play; they'll call it or walk.

**Post-deployment behavior**:

- **Go dark for 24–48 hours**. The recruiter needs to consult hiring manager + comp committee. Nudging during the window undermines the leverage.
- **If they respond with a match or close**: accept warmly, confirm in writing (Script 5), move to close. Don't press for more.
- **If they respond with "we can't match"**: evaluate against your walkaway. Two options: (a) accept the primary at their offered number if it's above walkaway (the primary may still be the right choice despite lower comp), or (b) take the competing offer. No middle ground once they've said can't-match.
- **If they respond by asking for proof** ("can you share the written offer?"): offer to describe the offer in enough detail that they can verify without you sharing a PDF with personal details. "Happy to share the range and level — it's at [COMPANY TYPE], [LEVEL], and the base is [$X], with [COMPONENT] at [$Y]." Refusing to share anything reads as bluffing; sharing everything sometimes inflates the anchor in ways you don't want.
- **If they pull the offer** after leverage deployment: extremely rare but possible. Reach out within 24 hours with: "I'd like to continue this conversation if there's still a path forward. My interest in the role is genuine." This salvages about 20% of pulled offers.
- **If the competing offer falls through later**: do not inform the primary. The leverage was real when deployed; downstream events aren't something you owe updates on.

---

## Script 7 — PTO / benefits negotiation

**Use when**: you've agreed on cash components and you want to close gaps on PTO, learning budget, parental leave, health benefits, retirement match, or other non-cash benefits.

**Length target**: 45–60 seconds spoken per component

**Tone**: pragmatic, matter-of-fact — these asks are lower-stakes than cash and should sound that way

**Why this script exists**: PTO and benefits are often overlooked in negotiation because candidates focus on cash. But at many companies, these components have more flex than base salary — and a few extra PTO days plus an improved retirement match add up to real value over years.

### Core PTO ask

```
"On PTO — the standard is [OFFERED DAYS]. I'd want to ask about
[SPECIFIC HIGHER NUMBER — usually 5–10 more days]. At my current
role I have [N DAYS] and I'd prefer not to take a step back on
that. Is there flexibility?"
```

### Learning / development budget ask

```
"On professional development — does the role include a learning
budget or conference allowance? If not, I'd want to ask for
[$SPECIFIC AMOUNT] annually earmarked for [CONFERENCES /
CERTIFICATIONS / COURSES]. It's something I use actively in my
current work."
```

### Parental leave ask

```
"On parental leave — what's the current policy? [IF POLICY IS LESS
THAN INDUSTRY STANDARD: I'd want to flag that [COMPARABLE COMPANIES]
offer [SPECIFIC NUMBER OF WEEKS] and I'd want to discuss whether
that's flexible for me.]"
```

### Retirement / 401k match ask

```
"On retirement benefits — is there flexibility on the match
structure or vesting schedule? [IF YES: ask about specific
improvement. IF NO: move on.]"
```

### Health benefits ask

```
"On health benefits — is there flexibility on the [SPECIFIC PLAN
TIER / SPECIFIC PREMIUM ISSUE]? [e.g., HSA contribution, premium
split, specific add-on coverage.]"
```

**Component flex patterns (pick your asks by what's likely to flex)**:

- **PTO**: highly negotiable at startups and senior levels; heavily banded at large corporates (but sometimes "unlimited" policies can flex into explicit guaranteed minimums)
- **Learning budget**: almost always flexible at tech and professional-services companies; harder at large bureaucratic companies
- **Parental leave**: flexible at mid-sized companies, harder at large corporates (policies are usually uniform), sometimes very flexible at startups (they just don't have a policy, so there's nothing to bend)
- **Retirement match**: rarely flexible — 401k match is usually uniform across employee base for compliance reasons
- **Health benefits**: rarely flexible on structure — usually uniform plans. Premium split or HSA contribution sometimes has room.

**Structure the conversation in order** (what to ask for first → last):

1. PTO (highest flex at senior levels)
2. Learning budget (almost always flexes)
3. Parental leave (policy-dependent)
4. Other component-specific asks
5. Retirement / health (save for last — less flex, but worth asking)

Do not ask for all 5 in one call. Pick 1–2 that matter most to you; ask them consecutively in the same call.

**Do not**:
- Ask for every benefit simultaneously. Dilutes focus and signals "wants everything."
- Bring up PTO / benefits before cash components are settled. The cash negotiation is primary; benefits are the close-out round.
- Ask for a benefit the company clearly doesn't offer ("can I get a 4-day work week?" at a traditional corporate) without significant leverage.
- Accept "that's not flexible" on the first question for EVERY benefit ask. Push once per component; if both asks get declined, move on.

**Post-ask behavior**:

- **Get any flexed benefit in writing** — especially PTO beyond standard, or a learning budget that wasn't in the original package. Verbal benefit promises evaporate.
- **If they say "we don't negotiate benefits"**: pivot to asking for a specific year-1 exception or an early review for benefit eligibility. Even if the plan is fixed, early access sometimes flexes.
- **If they offer a benefit you don't want** (e.g., larger 401k match that requires longer vesting): evaluate total-package value. Sometimes the "benefit" isn't valuable to you personally; it's fine to decline and ask for an alternative.
- **For PTO specifically**: if they agree to more days, ask about carry-over rules and buyback options at separation. PTO you can't use or take with you has lower real value.

---

## Script 8 — 30-day review revisit (when you accept below ask)

**Use when**: you've accepted an offer below your target, but with an understanding that comp will be revisited at 30, 60, or 90 days based on performance or proof-of-impact.

**Length target**: 60–90 seconds spoken at the initial acceptance + a specific written follow-up at the 30-day mark

**Tone at acceptance**: confident, forward-looking — you're framing this as collaboration, not consolation
**Tone at revisit**: professional, evidence-backed — you're demonstrating the impact you promised

**Why this script exists**: when the initial negotiation doesn't close the full gap, a documented 30-day (or 60, or 90) revisit commitment preserves future comp upside. The single biggest failure mode is that candidates accept the revisit commitment verbally, don't document it, and find themselves unable to re-open the conversation.

### Part A — Acceptance language (at initial offer close, when base is below target)

```
"[RECRUITER FIRST NAME] — I'm ready to accept at this number, but I
want to flag one thing. The base is below where my market research
and the ask landed. I understand the budget constraints this round.

I'd want to put an explicit [30-DAY / 60-DAY / 90-DAY] check-in on
the calendar where we revisit comp if I've demonstrated [SPECIFIC
IMPACT]. Specifically, if I've [SPECIFIC DELIVERABLE OR OUTCOME],
I'd want to revisit base.

Can we put that agreement in writing in the offer letter or an
amendment? That way we both have a clear marker."
```

**What this part is doing**:
- Explicitly names the gap (you're not pretending it's fine)
- Frames the revisit as mutual accountability (they see impact, you see comp)
- Specific deliverable = clear trigger for the revisit conversation
- "In writing" request is the protection

**Acceptance rules**:
- **Always specify the exact deliverable** ("ship the [X] migration" or "hit [Y] metrics for 2 consecutive months") — not "demonstrate good performance"
- **Always specify the revisit window** — 30, 60, or 90 days, not "soon" or "in a few months"
- **Always get it in writing** — offer-letter amendment or clear email confirmation. Verbal revisit agreements almost never happen on time.
- **Never accept a revisit offer if the current base is below your walkaway** — the revisit is probabilistic; the current base is guaranteed. Don't treat "30-day revisit" as making up for below-walkaway comp.

### Part B — The 30-day revisit message (written, sent 2 days before the agreed check-in)

```
Subject: [MY NAME] — comp revisit check-in

Hi [MANAGER FIRST NAME] [AND/OR RECRUITER],

As a reminder from when I signed, we agreed to revisit comp at the
30-day mark pending [SPECIFIC DELIVERABLE].

Over the last 30 days:
- [SPECIFIC OUTCOME 1 WITH NUMBER OR CONCRETE EVIDENCE]
- [SPECIFIC OUTCOME 2 WITH NUMBER OR CONCRETE EVIDENCE]
- [SPECIFIC OUTCOME 3 WITH NUMBER OR CONCRETE EVIDENCE]

Per the agreement, I'd want to schedule a comp revisit conversation
next week. What works for you?

Thanks — looking forward to it.

Best,
[MY NAME]
```

**What this part is doing**:
- Opens with the reference to the agreement — no ambiguity that this was pre-negotiated
- 3 specific outcomes with numbers — doing the work for the manager so they can make the case
- Specific ask for a meeting — converts vague "we'll revisit" into concrete calendar item

**Rules for the revisit message**:
- **Send 2 days before** the agreed check-in date. Earlier than that reads as anxious; day-of reads as last-minute.
- **Always include 3 specific outcomes**, each with a number or concrete evidence. "I've been doing good work" doesn't reopen a comp conversation.
- **Tie each outcome to the specific deliverable named in the original agreement**. If you agreed to "ship the X migration" and you shipped it, say so explicitly.
- **Copy the recruiter OR your manager, whoever was involved in the original agreement**. HR often forgets or was never looped in; having both people makes the agreement harder to walk back.

### Part C — In the revisit conversation itself

```
"Thanks for making time. As we agreed, I wanted to revisit comp now
that the [30-day mark] has hit. The outcomes I flagged in my note —
[BRIEFLY RESTATE 1–2 OF THEM] — were specifically what we agreed
would trigger this conversation.

Based on that, the ask I'd want to make is [SPECIFIC NUMBER OR
STRUCTURE — e.g., base raised to $X, or additional equity grant of
$Y].

What's the process from here?"

[Stop talking. Wait.]
```

**Do not**:
- Skip the 30-day revisit just because the role is going well. Accepting below-target on a promise and then not exercising the promise is leaving money.
- Revisit earlier than the agreed date. "I know we said 30 days, but I wanted to ask now" undermines the original agreement.
- Revisit with vague "I've been doing great" framing. Specific outcomes with numbers are the only thing that opens the comp conversation.
- Escalate the ask beyond what the original agreement implied. If you agreed to revisit base if you shipped X, don't then ask for base + equity refresh + sign-on. One agreement, one revisit.
- Give up after the first revisit if they delay. "We need another 30 days to confirm impact" is a reasonable counter; "we'll circle back eventually" is not. Set a specific next date if they push.

**Post-revisit behavior**:

- **If they grant the ask**: confirm in writing (Script 5). Move on.
- **If they counter with a partial**: evaluate against your original target. If partial gets you to target or close, accept. If well below, ask for a 60-day or 90-day follow-up.
- **If they say "the revisit isn't possible"**: refer back to the original written agreement. If the agreement specified conditions and those conditions were met, this is a renegotiation of an existing agreement — a serious signal about the employer. Consider (a) escalating above your manager, (b) documenting the exchange carefully, (c) whether this is the company you want to be at long-term.
- **If they grant the revisit but at a smaller amount than promised**: you now have two pieces of data — (1) they honored the revisit, (2) they didn't honor it at the level implied. Decide whether to continue with a 60-day second revisit or to treat this as the ceiling.

---

# Worksheets

---

## Worksheet 1 — BATNA

**What BATNA is, in 3 sentences**:

Your BATNA (Best Alternative To Negotiated Agreement) is your concrete backup plan if this negotiation fails to produce an acceptable outcome. It's not your target or your ideal — it's the specific, real, available option you'd actually take if this job falls through. In salary negotiation, your BATNA is the single most important thing determining how much room you have to push — because a negotiation without a BATNA is a negotiation where you cannot walk away, which means you cannot negotiate, only accept.

**The BATNA worksheet** (fill in honestly — your real answers, not aspirational ones):

```
CURRENT STATE:
1. Am I currently employed? [YES / NO]
2. If yes, what's my current comp (base · bonus · equity)?
3. If yes, am I satisfied enough to stay 6+ more months if this role falls through?
4. If no, how many months of savings do I have to fund a continued search?

LIVE ALTERNATIVES (as of today):
5. Do I have any other live offers right now? [YES / NO]
6. If yes, list each:
   - Company · Role · Comp · Timeline · My interest level vs. this offer
   - [repeat for each]
7. Do I have near-offers (final-round conversations)?
   - Company · Role · Expected timeline · My interest level
   - [repeat for each]

LATENT ALTERNATIVES (could be reopened):
8. Are there past companies where I reached final-round rejection but
   left on good terms that I could re-open? [LIST]
9. Are there people in my network who have offered to make intros or
   sponsor me? [LIST]

MY REAL BATNA (distill from above):
10. If this negotiation fails and this offer goes away, what's the
    single most likely path I'd take?
    [CHOOSE — stay in current role and restart search in [N] months ·
    take a specific other live offer · wait on a specific near-offer ·
    re-open a specific past conversation · search from unemployment
    with [N] months of runway]

11. What's the comp value of that BATNA (base + total comp)?
    $[NUMBER]

12. How does that BATNA comp compare to the offer I'm negotiating?
    [HIGHER · SIMILAR · LOWER · MUCH LOWER]
```

**How to use the BATNA in negotiation**:

- **If your BATNA is HIGHER or SIMILAR in comp value to the current offer**: you have strong leverage. You can push hard on the counter because you can genuinely walk.
- **If your BATNA is LOWER but not much lower**: you have moderate leverage. You can counter firmly but be ready to accept.
- **If your BATNA is MUCH LOWER** (e.g., unemployed with 2 months of savings and no other leads): your leverage is limited. Counter is still appropriate, but the stakes of the counter backfiring are higher. Calibrate ambition to your margin for error.
- **If you have NO BATNA** (not currently employed, no savings, no other leads): negotiate carefully. A too-aggressive counter that gets the offer pulled is a disaster you can't absorb. Use market-data rationale, not leverage-based rationale.

**Rules for using the BATNA**:
- **Do not reveal your BATNA to the recruiter** unless it's a genuine competing offer that you're leveraging intentionally (in which case, see Script 6).
- **Update your BATNA every 2–4 weeks during an active job search**. Your leverage changes as offers come and go.
- **Do not use an aspirational BATNA as if it's real**. "I could probably find another offer" is not a BATNA; "I have final-round conversations with [specific company] that are likely to produce an offer by [specific date]" is.
- **If your BATNA is weak, make market data and outcomes do the work your leverage can't**. You can still negotiate — just differently.

---

## Worksheet 2 — Comp research template

**Step-by-step template for triangulating what a role actually pays**:

```
ROLE SPEC (fill in fully — vague inputs produce vague outputs):
- Target role: [SPECIFIC JOB TITLE + SENIORITY + SPECIALIZATION]
- Industry / domain: [PASTE]
- Location / location tier: [CITY + STATE or REMOTE TIER]
- Company stage + size: [PASTE]
- Years of experience: [NUMBER]

SOURCE-BY-FIELD PRIMARY CHECKLIST (pick your field and start here):
```

### Tech / engineering / product / design
```
[ ] Levels.fyi — search target role + level + location + company stage.
    Look at distribution: 25th, 50th, 75th percentile.
[ ] Blind — search company name + level for anonymous current-
    employee posts. Bias: skews to complaints; useful for trends.
[ ] LinkedIn Salary — enter role + location. Useful as distribution
    reference, less granular than Levels.
[ ] Glassdoor — fallback only. Skews low and older.
[ ] 1–2 reference conversations with people at the company or at
    peer companies at similar level. 30 min each.
```

### Finance / banking / consulting
```
[ ] Wall Street Oasis (WSO) — salary threads by firm and level.
[ ] eFinancialCareers — salary surveys by region and specialty.
[ ] Transparent Career — niche but data-dense for banking.
[ ] Mergers & Inquisitions — articles + salary data for IB roles.
[ ] 1 reference conversation minimum — finance comp varies more than
    most industries by firm.
```

### Healthcare
```
[ ] For MDs: Doximity + AAMC salary reports + Medscape Physician
    Compensation Report (annual)
[ ] For nursing: Indeed filtered by state + union contracts where
    applicable
[ ] For allied health: Glassdoor + state labor reports
[ ] State medical society surveys when available
[ ] 1–2 reference conversations with current practitioners at peer
    facilities
```

### Marketing / design / content / sales
```
[ ] Built In — for tech-adjacent marketing/design roles
[ ] Glassdoor — useful here despite bias (less tech-specific data)
[ ] Payscale — aggregates broadly across industries
[ ] HubSpot / sales-specific industry reports
[ ] 2+ reference conversations — marketing comp varies a lot; data
    sources alone aren't enough
```

### Nonprofit
```
[ ] GuideStar (Form 990) — publicly-filed compensation for top 5
    highest-paid employees. Free.
[ ] Idealist — some posted ranges.
[ ] Council on Foundations salary surveys (if target org is
    philanthropic)
[ ] Candid — overlaps with GuideStar
[ ] Reference conversations — nonprofit comp is 20–40% below
    for-profit; people are often willing to share openly
```

### Government / public sector
```
[ ] Federal: OPM.gov — GS scale + locality pay tables (public)
[ ] State: each state publishes its pay bands (search "[state]
    employee salaries")
[ ] Municipal: same — usually public by law
[ ] Military: DFAS pay tables
[ ] No reference conversations needed — pay is transparent
```

### Other / cross-industry
```
[ ] Payscale — broad coverage
[ ] Glassdoor — basic distribution
[ ] LinkedIn Salary — if you have Premium
[ ] Salary.com — fallback
[ ] 2+ reference conversations are essential — published data alone
    is too broad
```

**Step 2 — triangulation table**:

```
Fill in what you found at each source:

| Source          | 25th %ile | Median | 75th %ile | Notes |
|-----------------|-----------|--------|-----------|-------|
| [Source 1]      | $         | $      | $         |       |
| [Source 2]      | $         | $      | $         |       |
| [Source 3]      | $         | $      | $         |       |
| [Reference call 1] | $      | $      | $         |       |
| [Reference call 2] | $      | $      | $         |       |

Triangulated range:
- Walkaway floor: $[LOW END OF WHAT YOU TRUST]
- Real target: $[MEDIAN OF TRUSTED SOURCES]
- Ambitious ask: $[TARGET × 1.10–1.15]
```

**Step 3 — reference call script** (for each of your 2 reference conversations):

```
"Hi [NAME] — thanks for taking the time. I'm exploring a [ROLE] role
at [COMPANY TYPE / STAGE], and I want to calibrate my comp
expectations honestly.

Two questions if you're open to them:

1. Based on what you know of similar roles, what range do you think
   is reasonable for this level?
2. Are there any specific components (equity, sign-on, bonus) where
   [STAGE/TYPE] tends to flex more or less than average?

And just to set expectations — I won't share any specifics you
mention; I'm just trying to triangulate."
```

**Rules**:
- **Never use a single source**. Every number you take to a negotiation should come from at least 2 sources.
- **Weight reference conversations heavily for fields with less-standardized data**. In marketing or nonprofit, 30 minutes with a peer is worth more than 3 hours of Glassdoor.
- **Re-run this worksheet at every new role**. Comp ranges shift quickly; last year's numbers are often stale.

---

## Worksheet 3 — Walkaway math / benefit-equivalency calculator

**Purpose**: convert a full offer package into a single comparable number so you can (a) compare offers apples-to-apples, (b) stress-test against your walkaway floor, (c) evaluate trade-offs between components.

**Step 1 — cash components (straightforward dollars)**:

```
Base salary (annual):                        $[        ]
Annual bonus target (% of base × probability):
    Target $ × typical-hit-rate of [80–100%] = $[        ]
Sign-on bonus (pro-rate over expected
    tenure if you plan to stay 2+ years, or
    count in full if short-tenure expected):  $[        ]

Cash subtotal:                                $[        ]
```

**Step 2 — equity (the illiquid and probabilistic component)**:

For RSUs at a public company:
```
RSU grant dollar value ÷ vest years:          $[        ] / year
```

For RSUs at a late-stage private:
```
(Grant value × discount for illiquidity) ÷ vest years = $[   ] / year
(Discount typically 20–40% depending on company runway)
```

For ISOs/NSOs at a startup:
```
(Grant value AT CURRENT 409A × discount for
 risk-adjusted probability of exit × years
 to likely liquidity) ÷ vest years = $[        ] / year

Discount ranges:
- Seed/Series A: discount 70–90% (most fail)
- Series B–C: discount 50–70%
- Series D+: discount 20–40%

(These are honest risk-adjusted estimates, not
 recruiter-pitch numbers.)
```

**Step 3 — benefits and time**:

```
PTO (annual days × daily base rate):          $[        ]
    (Base ÷ 250 = daily rate; × PTO days)

Retirement match (up to annual cap):          $[        ]

Health insurance premium subsidy (annual
    company contribution):                    $[        ]

Learning / development budget:                $[        ]

Parental / family leave (if planning use in
    next 2 years, calculate paid leave value): $[        ]

Other benefits (home office, gym, food,
    commuter, etc.) — annual value:          $[        ]

Benefits subtotal:                            $[        ]
```

**Step 4 — costs and subtractions**:

```
Commute cost (if in-office — annual):         −$[        ]
Relocation cost (if relocating — not
    reimbursed portion, prorated):            −$[        ]
Cost-of-living difference from current
    location (if moving):                     ±$[        ]
Income tax difference (if moving to new
    state — ballpark):                        ±$[        ]

Costs subtotal:                               $[        ]
```

**Step 5 — total comparable value**:

```
TOTAL FIRST-YEAR COMP =
  Cash subtotal
+ Equity subtotal (first-year vest)
+ Benefits subtotal
− Costs subtotal
= $[        ]
```

**Step 6 — compare to your walkaway**:

```
My walkaway total comp (what I said I would not go below): $[      ]

Offer total: $[      ]

Gap: $[ + / − ]

Decision rule:
- Offer > walkaway by 10%+: strong offer, accept or close with minor
  asks
- Offer 0–10% above walkaway: acceptable, consider accepting
- Offer at walkaway: accept if non-comp factors (role, team, mission)
  are strong; decline if they're neutral
- Offer below walkaway: counter firmly or walk; do not rationalize
  accepting below your stated floor
```

**Step 7 — comparing two offers** (if you have multiple):

Run Steps 1–5 for each offer side-by-side. Don't compare on base alone; compare on total comparable value.

Second comparison — non-comp factors (check all that apply):

```
Factor                         Offer A | Offer B
-----------------------------------------
Role interest / scope            [ / ]
Team / manager quality           [ / ]
Company trajectory / stage       [ / ]
Learning opportunity             [ / ]
Career path / advancement        [ / ]
Work-life balance                [ / ]
Flexibility (remote, schedule)   [ / ]
Risk / stability                 [ / ]
Brand / resume value             [ / ]
Geographic fit / life logistics  [ / ]
```

Weight each factor 1–5 based on YOUR priorities. Sum × weight for each offer. Total comparable comp + weighted non-comp score = your decision input.

**Rules**:
- **Do not treat equity at face value** — always apply risk-adjusted discount based on stage
- **Include PTO in the math** — companies offering "unlimited PTO" that nobody actually takes are different from companies offering 25 specific days
- **Re-run the math when something changes** — if they counter with more equity instead of base, the math changes
- **Trust the non-comp factors** — a 10% lower total at a better role with a better team usually wins long-term

---

**End of Module 5.** 10 prompts · 8 scripts · 3 worksheets. Flagship module complete.
