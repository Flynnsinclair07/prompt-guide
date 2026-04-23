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

## Prompts 6–10 · Scripts 4–8 · Worksheets *(Batch 2 — pending boss QA on Batch 1)*

- Prompt 6: deferred-start negotiation
- Prompt 7: equity / RSU negotiation
- Prompt 8: sign-on bonus negotiation
- Prompt 9: remote / relocation negotiation
- Prompt 10: justify your ask
- Script 4: Rebuttal — "is that your final answer?"
- Script 5: Accept — lock in final terms
- Script 6: Leverage — "I have another offer"
- Script 7: PTO / benefits negotiation script
- Script 8: 30-day review revisit script (for when you accept below ask)
- Worksheet 1: BATNA worksheet (with 2-sentence teach + scaffold)
- Worksheet 2: Comp research template (specific sources per field)
- Worksheet 3: Walkaway math (benefit-equivalency calculator)
