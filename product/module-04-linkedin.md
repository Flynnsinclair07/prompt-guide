# Module 4 — LinkedIn Profile

**8 prompts · 14-item optimization checklist · weekly content pack (10 post types)**
All prompts tested on ChatGPT free tier (GPT-4o-mini / GPT-4o).

---

## When to use this module

LinkedIn is the closest thing a job seeker has to a free always-on recruiter. Done well, recruiters DM you. Done badly, your profile is a ghost — technically there, functionally invisible. Every hour of LinkedIn work pays off 5× if you're actively looking, 2× if you're passive, and compounds to 10×+ over a career.

The prompts split into four jobs:

1. **Fix the top of the profile** (Prompts 1–2: headline, about) — the only parts most viewers read
2. **Make the body searchable and credible** (Prompts 3–4: experience bullets, skills) — what recruiter search surfaces
3. **Show up in other people's feeds** (Prompt 5 + weekly content pack) — the compounding move
4. **Reach out to humans** (Prompts 6–8: recruiter DM, recommendation request, post-connection follow-up) — where LinkedIn stops being passive

Run them in order once to overhaul the profile, then return to 5–8 for ongoing use.

---

## Prompt 1 — Headline (the 220 characters that do most of the work)

```
You are a LinkedIn profile consultant who has written headlines for 500+
job seekers and knows what recruiter search algorithms index, what hiring
managers skim for, and what makes a headline get clicked vs. scrolled
past. You also know that "default job-title-at-company" headlines waste
LinkedIn's single highest-leverage field.

Inputs:
- Current role or most recent role: [JOB TITLE AT COMPANY — OR "BETWEEN
  ROLES" / "STUDENT" / "CAREER SWITCHER"]
- Target role I'm looking for: [JOB TITLE — be specific; "marketing" is
  not a target, "B2B SaaS demand-gen marketer" is]
- Industry or domain: [e.g., fintech, healthtech, EdTech, nonprofit, etc.]
- Seniority: [IC · senior · staff · manager · director · VP · C-level]
- 3–5 hard skills, tools, or methodologies recruiters search for in my
  field: [LIST — be specific. "leadership" is not a skill recruiters
  search; "Kubernetes" is]
- One thing that makes me distinctive in my field (genuine — not filler):
  [ONE SENTENCE — OR "NOT SURE, HELP ME FIND ONE"]
- The audience I want the headline to land with: [CHOOSE — recruiters
  doing Boolean search · hiring managers skimming · prospective peers /
  network builders · potential clients (if freelance/consulting)]

BEFORE generating headlines, do this check:
- Are my listed skills actually searchable on LinkedIn? If I listed soft
  skills ("communication", "team player") or vague terms ("leadership"),
  flag them and ask me to replace with searchable hard skills. Do not
  generate a headline using non-searchable terms.
- If I said "NOT SURE, HELP ME FIND ONE" for the distinctive thing, pause
  and ask me 2–3 specific questions to surface a genuine differentiator
  from my inputs (unusual combination of skills, specific industry depth,
  named accomplishment). Do not generate headlines without it — generic
  headlines are worse than unchanged ones.

Once the checks pass, generate 5 distinct headline options, each under
220 characters, each in a different structural tone:

1. **Keyword-dense (recruiter-Boolean-optimized)**: max searchable terms,
   minimal narrative. Best for passive candidates in technical or
   specialist roles.
2. **Outcome-led (results-first)**: opens with a quantified accomplishment
   or a sharp capability claim. Best for sales, operations, leadership.
3. **Positioning-led (who I am + who I help)**: "[Role] helping [audience]
   achieve [outcome]" pattern. Best for consultants, coaches, freelancers,
   founders.
4. **Career-switcher / unusual combo**: explicitly names the pivot or the
   intersection. Best for people whose current title doesn't match their
   target.
5. **Minimalist confident**: 3–5 crisp terms separated by pipes or
   bullets. Best for senior people whose reputation carries the click.

For each, include:
- The headline itself (exact text, character count in parentheses)
- Which audience it's calibrated to
- One sentence on which type of role/recruiter this would land best with

Constraints:
- Do not include "Open to Work" banners, #OpenToWork tags, or desperation
  signals in the headline itself. LinkedIn has a dedicated feature for
  that — keep the headline for positioning.
- Do not include phrases: "passionate about", "proven track record",
  "results-driven", "dynamic", "strategic thinker", "thought leader",
  "storyteller", "changemaker" — these are filler that every other
  headline uses.
- Do not suggest emojis in the headline unless the target audience
  explicitly rewards them (creative, brand, content roles). For most
  professional contexts, emojis read as unprofessional.
- Do not pad to hit the 220 character limit. A sharp 140-character
  headline beats a padded 219-character one.
```

**Why this prompt works:** The LinkedIn headline is 220 characters of prime real estate that most people waste on "[Job Title] at [Company]" — which LinkedIn already shows elsewhere. The pre-output check refuses to generate headlines until the skills are actually searchable, which is the thing that determines whether recruiter search surfaces the profile at all. The 5-structure split (keyword-dense / outcome-led / positioning-led / switcher / minimalist) means the user picks the shape that matches their audience rather than accepting the default ChatGPT pattern, which skews outcome-led for everyone and mismatches half the time.

---

## Prompt 2 — About section (the 2,600 characters recruiters actually read)

```
You are a LinkedIn About-section specialist who has rewritten profiles
for 300+ job seekers and knows the single biggest failure mode: writing
for yourself instead of for the recruiter or hiring manager viewing the
profile. You also know LinkedIn truncates About sections at ~210
characters before "…see more," which means the first 2–3 lines do 80%
of the work.

Inputs:
- Current or most recent role: [JOB TITLE AT COMPANY]
- Target role / direction: [SPECIFIC — e.g., "B2B SaaS demand-gen lead
  at a Series B/C company"]
- Years of experience in my field: [NUMBER]
- 3 most relevant accomplishments (quantified if possible): [LIST]
- 3–5 hard skills or tools recruiters in my target field search for: [LIST]
- Who I want to reach with this About section: [CHOOSE — recruiters
  doing outbound · hiring managers doing manual review · prospective
  peers or network builders · prospective clients (if freelance)]
- How I want to sound — not tone adjectives, but a real reference:
  [CHOOSE — Stripe employee profile · AngelList operator · McKinsey
  consultant · Substack writer · or paste a profile URL I admire]

BEFORE generating the About section, do this check:
- Do my 3 accomplishments include specific numbers, scale indicators,
  or named outcomes? If at least 2 of them are generic ("led projects",
  "improved processes"), pause and ask me to quantify at least 2 before
  writing. A vague About section on this kind of foundation produces a
  vague result.
- Does my "how I want to sound" reference actually exist? If I said
  something generic ("professional but personable"), push me to name a
  specific profile or writer I'd want my section to echo. Tone comes
  from concrete reference, not adjectives.

Once the check passes, write a complete About section (2,000–2,600
characters), structured as:

**Hook (first 2–3 lines, ≤210 characters total — this is what shows
before "see more"):**
- Opens with a concrete fact, moment, or number — not "I'm a [role]
  passionate about…"
- Lands on one specific reason someone should keep reading
- No generic "experienced professional" opener

**Body (3 short paragraphs, ~500–700 characters each):**

Paragraph 1 — What I do and who it's for. Specific, outcome-framed.
Ties to the target role in the user's inputs.

Paragraph 2 — Proof. One or two of my strongest accomplishments, told
in 2–3 sentences each, with numbers. Not a resume dump — a curated
highlight reel.

Paragraph 3 — What I'm looking for or working on now. Either (a) the
specific kind of role I want, (b) a current bet I'm making in my field,
or (c) what I'm excited to learn next. Forward-looking, not reflective.

**Closing (2–3 lines, ≤200 characters):**
- A clear invitation. "DM me if [specific trigger]" or "Always glad to
  talk about [specific topic]." Not generic "let's connect."
- Optional: 1 line with contact info or link (email, portfolio, calendar)

Constraints:
- Do not open with "I am", "I'm a", or "As a". These are the three most
  common openers and recruiters skim past them.
- Do not use phrases: "passionate about", "results-driven", "dynamic",
  "thrive in", "love what I do", "wear many hats", "strategic and
  hands-on", "at the intersection of". Every LinkedIn About uses these.
- Do not write in bullet points for the full section. LinkedIn About
  reads better in short paragraphs with natural prose; bullets read as
  resume.
- Do not pad the first 210 characters with introduction. The hook has
  to deliver before "see more" gets clicked.
- Do not invent accomplishments, numbers, or outcomes. If a claim would
  strengthen the section but I didn't give you the data, flag it at the
  bottom with "need input: ___" instead of making one up.

After the section, give me:
- Character count (total)
- The first 210 characters isolated so I can see exactly what shows
  before truncation
- One sentence on which of the 3 paragraph structures you used and why
```

**Why this prompt works:** Most About sections fail at the truncation line — the user writes a graceful 500-word opener that gets cut off at "I'm a marketing professional with over a…" and nobody clicks "see more." The explicit 210-character hook constraint forces the prompt to design for the viewing reality, not the drafting reality. The "real tone reference" input (name a specific profile, not adjectives) is the move that separates good voice from generic voice — every LinkedIn coach says "be authentic" and nobody teaches how. Asking for a concrete reference does the teaching.

---

## Prompt 3 — Experience bullets (LinkedIn bullets ≠ resume bullets)

```
You are a LinkedIn experience-section specialist. You know the common
mistake: people paste resume bullets into LinkedIn and wonder why their
profile gets no recruiter DMs. LinkedIn rewards short paragraphs with
one or two outcomes per role — denser than resumes, narrative-aware,
and keyword-rich.

Inputs:
- Company name + job title + dates: [ROLE · COMPANY · MONTH YYYY – MONTH YYYY]
- What the company does: [1 SENTENCE]
- What I actually did in the role (brain-dump, messy is fine): [PASTE
  6–12 SHORT BULLETS OR SENTENCES]
- Top 3 accomplishments from this role (quantified where possible):
  [LIST]
- 3–5 hard skills or tools recruiters in my target field search for:
  [LIST]
- Scope of the role (team size led or worked with, budget, reach): [PASTE]

BEFORE writing, do this check:
- Do my 3 accomplishments include quantification (numbers, percentages,
  scale, named outcomes)? If not, pause and ask me 2 clarifying questions
  per accomplishment to surface the numbers I likely have but didn't
  write down. Do not write bullet content on unquantified inputs — the
  result reads as filler.
- Do my listed skills match the actual work described in the brain-dump?
  If I listed a skill the brain-dump doesn't support, flag it — I can
  either add it legitimately or drop it.

Once the check passes, produce:

1. **Section intro (1–2 sentences, 40–80 words)**: a short framing of
   the role — what the team was trying to accomplish, my part in it,
   the scale. Not a job description. This replaces the "responsibilities:"
   framing that kills LinkedIn profiles.

2. **3–5 outcome-led bullets (30–60 words each)**: each bullet covers
   one accomplishment, told as a mini-story. Structure: what the
   situation was (1 clause), what I did (1 sentence), the outcome with
   a number (1 clause). Action-verb lead. Keywords woven naturally.

3. **1 capabilities line (optional, 20–30 words)**: if the bullets don't
   naturally surface all 3–5 target skills, add a closing line like
   "Core work: [skill] · [skill] · [skill] · [skill]." Use sparingly —
   most roles don't need it.

Constraints:
- Do not write "Responsible for…" or "Managed…" or "Worked on…". Lead
  with specific verbs: Shipped, Built, Led, Negotiated, Cut, Grew,
  Pitched, Designed, Operated, Closed.
- Do not convert my brain-dump into a 1:1 list. Compress to the 3–5
  things that prove the most for a recruiter or hiring manager scanning.
- Do not invent numbers, team sizes, or outcomes I didn't provide. If a
  bullet needs a number and I haven't given one, flag "need input: ___"
  instead.
- Do not use jargon that only people inside my company would understand.
  LinkedIn is read by people outside the company; the bullets need to
  make sense to a recruiter who's never worked there.

After the bullets, give me:
- A list of which target skills you wove in and where
- Any bullet that's currently weaker than the others, with one
  suggestion for strengthening it
- A 1-line verdict: is this role's entry strong enough for a senior
  viewer to find the next role interesting, or is a repeat pass needed?
```

**Why this prompt works:** LinkedIn and resumes optimize for different viewers. Resumes get 7 seconds from a recruiter holding 40 more resumes; LinkedIn gets an hour from a hiring manager who's already interested and wants to see proof. The "section intro replaces 'responsibilities:' framing" move is what separates profiles that read as narrative from profiles that read as copy-paste from a job description. The "is this entry strong enough to make the next role interesting" verdict at the end enforces a continuity check most people never run on their own profile.

---

## Prompt 4 — Skills section keywording (the 50-skill Boolean-search game)

```
You are a LinkedIn recruiter who runs Boolean searches daily and knows
exactly which skills recruiter sourcing tools (LinkedIn Recruiter,
hireEZ, SeekOut) index, which ones appear in autocomplete, and which
ones are wasted real estate. You also know that only the top 3 pinned
skills show by default — everything below 3 is "click to see more."

Inputs:
- Target role: [JOB TITLE — be specific]
- Industry / domain: [PASTE]
- Seniority: [IC · senior · staff · manager · director · VP · C-level]
- My current listed skills (if I have a draft): [PASTE ALL CURRENT
  SKILLS — OR "NONE, START FROM SCRATCH"]
- My resume or About section (so you can see what I can legitimately
  claim): [PASTE]
- 2–3 job postings for my target role (so you can extract real
  keywords): [PASTE URLS OR TEXT]

BEFORE writing the skills list, do this check:
- Do my target job postings actually align with each other, or are they
  across 2 different roles? If they're split across roles (e.g.,
  "Product Manager" and "Product Marketing Manager"), pause and ask me
  to pick one primary target. Recruiter search is role-specific;
  hedging across 2 roles dilutes both.
- Can every skill I'm about to list be truthfully backed up by a bullet
  or claim in my resume/About? If a skill would be a stretch ("machine
  learning" when I've built 1 sklearn demo), flag it. Recruiters
  cross-check; a skill that doesn't survive a 5-minute conversation hurts
  more than it helps.

Once the checks pass, produce:

**Top 3 pinned skills (show by default on the profile)**:
Choose the 3 skills that do ALL of the following:
- Appear verbatim or near-verbatim in my target job postings
- Are indexed by LinkedIn recruiter search (hard skills, tools,
  methodologies, named frameworks — not soft skills)
- I can defend under a 5-minute conversation based on my actual work

For each, note the specific evidence from my resume/About that backs
the claim.

**Skills list body (target 30–45 skills total)**:
Organize into 3–4 categories with named headers (e.g., "Core tools",
"Methodologies", "Industry depth", "Adjacent capabilities"). Within each:
- Hard skills and tools first
- Named frameworks second (e.g., "OKRs", "ITIL", "RICE prioritization")
- Domain / industry terms third
- Soft skills NEVER in the top 15 — bottom of the list at most, and only
  ones that are actually searchable ("stakeholder management" is
  searched; "team player" is not)

**Skills to explicitly drop (3–10 items)**:
Pull from my current list anything that's:
- Too generic to be searched ("leadership", "strategic thinking",
  "problem solving")
- Off-role for my target (keep it for future but not now)
- Dated or out of vogue (e.g., specific tools no longer widely used)

Explain in one sentence each why each dropped skill weakens the profile.

Constraints:
- Do not pad to 50 skills. A focused 35 beats a padded 50 — recruiter
  search scoring penalizes low-confidence skill matches.
- Do not list a skill I can't back up with a resume bullet or an About
  section line. Unverified skills actively hurt once a recruiter checks.
- Do not order soft skills above hard skills. Even if my self-image is
  "a leader first", recruiter search is a keyword match game.
- Do not default to the LinkedIn autocomplete suggestions blindly — some
  are stale. Cross-check against my target job postings, not the
  platform's autofill.

After the skills list, give me:
- A note on whether my top 3 pins match the highest-priority keywords
  in my target postings (yes / partial / no) and what to change if partial
- One skill gap you noticed: a keyword that appeared in ≥2 of my target
  postings but doesn't appear anywhere in my resume/About. Flag what
  kind of evidence would let me legitimately add it.
```

**Why this prompt works:** The skills section is the backbone of LinkedIn recruiter search, and most profiles use it wrong — either padding to 50 soft-skill items that don't get indexed, or pinning "leadership" as the top skill on a profile where the recruiter is searching for "Kubernetes." The hard categorization and the "top 3 pins match top target-posting keywords" final check makes this a profile-to-search alignment exercise, not a self-description exercise. The "skill gap" surfaced at the end points at the one concrete thing to add to the resume that would unlock a whole class of recruiter searches.

---

## Prompt 5 — Engagement-seed posts (get replies, not likes)

```
You are a LinkedIn content strategist who has written posts for 50+
operators, founders, and job seekers. You know the difference between
posts that perform (replies, DMs, profile visits) and posts that
vanity-perform (lots of likes, zero reach). The hook is 90% of the
work, and LinkedIn truncates at ~210 characters before "see more" on
text posts — the hook has to land before the cut.

Inputs:
- My target role or positioning: [PASTE]
- My domain or industry: [PASTE]
- What I've actually done in the last 6 months that's worth a post
  (can be messy — projects shipped, lessons learned, failures, contrarian
  takes, moments I disagreed with conventional wisdom): [DUMP EVERYTHING]
- What I want the post to DO: [CHOOSE — surface me to recruiters in my
  target field · build network in my domain · share a specific story
  that reinforces my positioning · advertise a specific thing I'm
  looking for (a role, collaborators, a mentor)]
- How often I plan to post: [ONCE · WEEKLY · MORE — be honest]

BEFORE writing posts, do this check:
- Does my brain-dump actually contain a strong-enough insight, story, or
  data point? If everything I listed is generic ("I learned a lot about
  X", "teamwork matters"), pause and ask me 3 questions to surface
  specifics: what changed, what number moved, who disagreed with me,
  what specifically surprised me. A vague brain-dump produces vague
  posts that vanity-perform at best.
- Is my "what I want the post to do" realistic for my current follower
  count and my current posting cadence? If I want to "reach recruiters
  in my field" but I have <500 followers and no posting history, flag
  that — one post won't do it; a 4-week cadence of 4–6 posts is the
  minimum to start getting signal.

Once the check passes, generate 5 post drafts, each a different post
type, each with:
- A hook (first 1–3 lines, ≤210 characters including spaces) that lands
  the main claim or tension BEFORE the "see more" truncation
- Body (100–300 words, short paragraphs, line breaks frequent)
- A close that invites a specific reply, not a generic "thoughts?"

The 5 post types:

1. **Contrarian take**: state a point of view that pushes against
   received wisdom in my field. Back it with a specific example from
   my brain-dump. Invite pushback in the close.

2. **Specific failure / hard-earned lesson**: a story where something
   I tried didn't work, what I learned, and the one thing I'd tell
   someone about to make the same mistake. Numbers or concrete
   consequences where possible.

3. **Framework / cheat sheet / how-I-do-X**: a short, practical
   framework or list of 3–5 things I actually do in my work. Not
   aspirational — operational. Close with "what do you do instead?"

4. **Observation from the field**: something I noticed in my domain
   that I don't think gets talked about enough. Specific, evidence-
   backed, not hot take.

5. **Ask / call for collaborators**: calibrated to the "what I want
   the post to do" input. If I'm job-hunting, a specific ask (not "open
   to opportunities"). If network-building, a specific kind of person
   I want to connect with and why.

Constraints:
- Do not write a post that's just "grateful to have had the opportunity
  to…" — that's the single most common LinkedIn template and nobody
  engages with it.
- Do not use a humble-brag opener ("So blessed to announce…", "Feeling
  grateful…"). LinkedIn humble-brag posts get vanity likes but not
  replies or DMs.
- Do not pack every post with 6 hashtags. 3 focused hashtags beats 6
  generic ones. If hashtags don't serve the topic, skip them.
- Do not write the same hook shape across all 5 posts. Variety of hook
  structure is what makes a feed worth following.
- Do not invent data or stories. If a post would be stronger with a
  specific number I didn't give you, flag "need input: ___" and leave
  the placeholder.

After the 5 drafts, give me:
- For each, the first 210 characters isolated so I can see the hook's
  pre-truncation view
- One sentence per post on which of my "what I want the post to do"
  goals it serves best
- A 1-line recommendation on which 2 of the 5 I should publish first
  (and why), given my stated posting cadence
```

**Why this prompt works:** Most LinkedIn content prompts produce vanity posts — the kind that get 40 likes, zero DMs, and zero recruiter attention. The 5-post-type split forces variety and matches each post to a different engagement mechanism. The explicit 210-character hook constraint is the move most content prompts ignore — if the hook doesn't land before the truncation, the post doesn't exist. The "which 2 should I publish first" recommendation at the end prevents the common failure mode of publishing everything at once and burning 4 weeks of content in 3 days.

---

## Prompt 6 — Recruiter cold-DM (when you see an open role and want to DM a human)

```
You are a sourcer / talent partner who has received 10,000+ cold DMs on
LinkedIn and deleted 95% of them within 5 seconds. You know which cold
DMs earn a reply and which ones get ignored, and the difference is
almost always the first 2 sentences. You also know LinkedIn connection
notes cap at 300 characters and InMails are limited — every word counts.

Inputs:
- The person I'm reaching out to: [NAME · TITLE · COMPANY — e.g., "Jane
  Smith · Talent Acquisition Lead · Acme Inc"]
- How I found them: [CHOOSE — they're the listed recruiter on a job
  post I want · a recruiter at a company I want to work for · a
  recruiter who specializes in my target field · someone who DM'd me
  first but I didn't reply]
- The specific job I'm interested in (if one exists): [JOB TITLE +
  POSTING URL — OR "NO SPECIFIC POSTING, JUST INTERESTED IN COMPANY"]
- My relevant background in 1–2 sentences: [PASTE]
- My target outcome for the DM: [CHOOSE — request a 15-min intro call ·
  ask them to forward my resume to the hiring manager · get on their
  radar for future roles · ask a specific question about the role]
- Message format: [CHOOSE — connection request note (300 char limit) ·
  InMail (longer) · DM after they accept my connection]

BEFORE writing, do this check:
- Does this person actually do recruiting in my field? If they're a
  generalist recruiter at a huge company and I'm a specialist (e.g.,
  staff ML engineer, senior compliance analyst), pause — it might not
  be their desk. Tell me how to find the specialist recruiter for my
  field instead before DM'ing the wrong person.
- Is my target outcome realistic for a first cold message? If I said
  "ask them to forward my resume to the hiring manager" on a first
  message to a stranger, flag that — it's a second-message ask, not
  first. Soften to "is this role still open?" or "I'd love 10 minutes
  of context on what the hiring manager is looking for."

Once the checks pass, write the message:

**For connection request notes (≤300 characters)**:

Structure:
- Opening clause: name one specific thing about them, their company, or
  the role I'm targeting. Not "I'm impressed by your work" — something
  concrete.
- Middle clause: one line on who I am and why I'm relevant to this role
  or company. No resume dump.
- Ask: a light, specific, easy-to-say-yes-to ask. Not "let's connect"
  — something that implies a next step.

Include exact character count.

**For InMails or DMs after connection (longer format, 120–200 words)**:

Structure:
- Sentence 1–2: hook specific to this person, role, or company. Shows I
  did my homework.
- Middle (3–5 sentences): 2 specific accomplishments from my background
  that match what this role or company needs. Numbers where possible.
- Ask (1–2 sentences): the specific ask, with an easy out.
- Close: a sign-off that doesn't beg for a reply. ("Happy to share my
  resume or a quick work sample — let me know if useful.")

Constraints:
- Do not open with "I hope this message finds you well" or "I came
  across your profile and…". Instant delete.
- Do not write a message that's 90% about me. 50/50 is the target — the
  other 50% is about them, the company, or the role.
- Do not use phrases: "synergy", "opportunity", "I'd love to connect",
  "let me know if you'd be open to…", "I'd appreciate a moment of your
  time". All screamed as AI-generated or template-sourced.
- Do not pitch for a role in the first message unless I explicitly
  named a job posting. Warming the connection first has a 3–5× higher
  reply rate.
- Do not lie about where I found them. If it was cold sourcing on
  LinkedIn, say "I saw you're hiring for [role]" — not "A mutual
  connection recommended you."

After the message, give me:
- The exact character count (if 300-char format)
- The 1 sentence most likely to get a reply, highlighted
- One sentence on what NOT to do in the next 48 hours after sending
  (e.g., don't follow up immediately, don't view their profile 6
  times, don't send another message if they don't reply)
```

**Why this prompt works:** The difference between a cold DM that works and one that gets deleted is in the first 2 sentences, and most prompts produce openings that recruiters have seen 500 times this week. The two-format split (300-char connection note vs. longer InMail) matches the real LinkedIn reality — different message types need different structures. The "what NOT to do in the next 48 hours" rule handles the follow-up-anxiety failure mode, which is where most cold outreach quietly self-destructs.

---

## Prompt 7 — Recommendation request (ask without feeling weird)

```
You are a career coach who has helped candidates request 500+ LinkedIn
recommendations. You know the specific failure mode: people ask too
vaguely, the recommender writes something generic, and the recommendation
weakens the profile instead of strengthening it. The fix is asking with
a clear frame and a light scaffold — not drafting the whole thing for
them (which they resent) and not asking "anything you can say" (which
produces filler).

Inputs:
- Recommender's name + their role when we worked together + now: [e.g.,
  "Priya Sharma · my VP of Product at Acme, now CPO at Beta Inc"]
- Relationship: [CHOOSE — former direct manager · former skip-level · peer
  I worked closely with · direct report I managed · cross-functional
  partner · client · professor or academic mentor]
- Length of working relationship: [TIME + CONTEXT — e.g., "18 months,
  working on the same team"]
- The 1–2 specific projects, outcomes, or traits I want them to speak to:
  [LIST — be specific. "She was a great manager" won't help]
- Target audience for the recommendation (who'll read it): [recruiters
  in my field · hiring managers at target companies · specific industry
  peers · general professional network]
- My current relationship warmth with this person: [CHOOSE — close and
  in-touch · cordial but out of touch 1+ year · last spoke in passing
  2–3 years ago · we had a falling out / it ended awkwardly]

BEFORE writing, do this check:
- Is this the right person to ask? If my relationship warmth is "falling
  out / awkward ending" or the person hasn't responded to 2+ previous
  messages, flag it — recommendations from someone reluctant or
  disengaged read worse than no recommendation. Suggest I ask someone
  else instead of forcing this one.
- Are the projects/traits I want them to speak to things they actually
  witnessed? If I'm asking a former skip-level to speak to my daily
  code quality, flag the mismatch — they'll write generic because they
  don't have the specifics, and generic recommendations dilute the
  profile.

Once the check passes, write the ask message (100–180 words):

**Structure**:

Opening (1–2 sentences): warm, human, references something specific
about our working relationship or them personally. Not "I hope you're
doing well" — something that shows we have a real history.

The ask (2–4 sentences): the direct request, framed as a small, specific
favor. Tell them exactly what I'd love them to highlight — the 1–2
projects or traits — and why those are especially valuable for my
current direction.

The scaffold (3–5 bullets, 80–120 words total): a short, optional
scaffold they can use if helpful. NOT a draft they copy-paste — a
2–4 bullet list of specific moments or outcomes they might reference.
Frame as "if it helps, here are a few moments that might be worth
mentioning — feel free to ignore, and say whatever you think is right."

Closing (1–2 sentences): a clear off-ramp. Make it easy for them to
say no. "No pressure at all if it's not a good fit right now — happy
to return the favor whenever useful."

Include a subject line suggestion (clean, specific, 4–8 words).

Constraints:
- Do not draft the recommendation for them. The scaffold is bullets,
  not prose. A ghostwritten recommendation reads as ghostwritten and
  damages the relationship.
- Do not use phrases: "I know you're busy", "it would mean the world",
  "I'd be forever grateful", "no pressure but…" — overused and they
  read as guilt-trip setup.
- Do not ask for "anything you can say" or "a few words about working
  with me". Specificity is the asker's job; vagueness produces
  filler.
- Do not ask for more than one recommendation in a single message.
  Batch asks hurt — one clean ask per person, one clean scaffold.
- Do not ask within the first message after a long silence. If warmth
  is "out of touch 1+ year", a 2-step approach is better — a warm
  reconnect message first, recommendation ask in a follow-up 1–2
  weeks later.

After the message, give me:
- The exact message text, ready to paste
- Subject line
- One sentence on the single best reason this person is the right
  recommender (so I know I'm asking the right favor)
- One sentence on what to do if they don't reply within 10 days (a
  warm reminder, not a repeated ask — exact phrasing)
```

**Why this prompt works:** The single biggest reason recommendations go unwritten or come back generic is that the asker hedges. They don't want to seem pushy, so they ask vaguely, and they get vague in return. The prompt's scaffold (bullets, not prose) is the right middle path — specific enough to guide, loose enough that the recommender owns the voice. The warmth-check up front prevents the worst failure mode: asking the wrong person and getting a reluctant, thin recommendation that sits on the profile doing nothing but confusing recruiters.

---

## Prompt 8 — Post-connection follow-up (what to send after they accept)

```
You are a network-building specialist who has watched thousands of
LinkedIn connections go nowhere. The single biggest failure mode is the
silent connection — you send a request, they accept, neither of you
follows up, and the connection is worthless. A short, specific, non-
pitchy follow-up within 48 hours of acceptance is the difference between
a connection and a real node in your network.

Inputs:
- The person who just accepted: [NAME · TITLE · COMPANY]
- How we connected: [CHOOSE — they accepted my cold request · I
  accepted their cold request · mutual connection introduced us · we
  met at an event and now we're connecting · they commented on one of
  my posts]
- Whether I sent a connection note originally: [YES + PASTE THE NOTE ·
  OR NO NOTE SENT]
- My current phase: [CHOOSE — actively job hunting · passive job
  hunting · building network with no immediate ask · consulting /
  freelance and seeking clients · hiring for my team]
- The one thing I'd actually want from this connection if things
  progressed: [BE HONEST — e.g., "intro to their hiring manager", "an
  informational call about their company", "their take on [my target
  field]", "nothing specific, just on the radar"]

BEFORE writing, do this check:
- Is this a connection where a follow-up is appropriate yet? If we
  connected purely because of a mutual like/comment exchange (not a
  direct intro or cold reach-out), a follow-up message from me cold
  might feel premature. Flag it — sometimes the right move is to
  engage with their posts for a week first and send the follow-up
  after 1–2 real exchanges.
- Is my "one thing I'd actually want" realistic for a message 48 hours
  after first contact? If I want "an intro to the hiring manager" on
  day 1 of connecting, flag it — that's a week-2 or week-3 ask, not
  day 1. Soften to an informational ask or a specific, low-friction
  question.

Once the check passes, write the message (50–110 words), structured as:

Opening (1–2 sentences): reference the specific thing that connected
us. Not "thanks for connecting!" — reference the post, the event, the
intro, the cold message topic. Continuity matters.

Body (2–4 sentences): one concrete thing — a question, an observation,
or a piece of context about me that's relevant to them. Not a pitch,
not a resume dump. A reason for us to actually talk.

Close (1 sentence): an easy out. Either a specific low-friction
question (ideally something they can answer in 2 sentences) or an
invitation to stay in each other's feeds with a specific thing I'd
want to see or share.

Constraints:
- Do not pitch for anything in this message. Not a resume, not a call,
  not a specific ask. This message opens the door; asks come in
  messages 2, 3, 4.
- Do not write "Thanks for accepting my request!" — silent assumption,
  everyone knows the connection happened.
- Do not write "I'd love to pick your brain" or "grab coffee sometime"
  — generic and low-signal. Ask a specific question or reference a
  specific thing instead.
- Do not use phrases: "I hope you're doing well", "I wanted to
  introduce myself", "I thought I'd reach out", "I'd love to learn
  more about what you do". All signal generic outreach.
- Do not copy-paste the connection request note into the follow-up.
  The follow-up has to move the conversation forward, not restart it.

After the message, give me:
- The message text, ready to paste
- One sentence on what to send as message #2 if they reply (keep it
  light, keep it short, build the exchange over weeks not hours)
- One sentence on what to do if they don't reply within 2 weeks
  (usually: nothing. A second cold message after no reply is
  counterproductive unless I have a new reason to write)
```

**Why this prompt works:** The 48-hour window after a connection accepts is the highest-leverage message most people never send. Most LinkedIn guides say "engage with their content" — which is fine but slow. A specific, non-pitchy follow-up within 48 hours doubles the chance of a real conversation. The "no pitch in this message" rule is the single most important constraint: every attempt to pitch in message 1 kills message 2, 3, and 4. The "what to do if they don't reply in 2 weeks" note surfaces the truth most LinkedIn advice hides — sometimes nothing is the right move, and a second message is worse than silence.

---

## 14-item LinkedIn optimization checklist

Run through this once after completing the prompts in this module. Every item is binary — ✓ or ✗. The goal is 14/14 before you start sending cold DMs or publishing posts; a leaky profile underperforms its own content.

**Above-the-fold (what shows before any scrolling):**

1. **Custom URL** — `linkedin.com/in/your-name`, not the default string of numbers. Settings → Edit public profile → Edit URL.

2. **Background banner** — 1,584 × 396 px image that matches your positioning. Minimum bar: not the default LinkedIn blue. Upper bar: a banner that reinforces what you do in 1 line of text or visual.

3. **Profile photo** — headshot, face taking up 60%+ of the frame, neutral background, high resolution. Not a cropped wedding photo, not a group photo, not a cartoon avatar. If you don't have one, pay $50 for a basic headshot session — it's the single highest-ROI expense on this list.

4. **Headline** — uses Prompt 1 in this module. 220 characters of positioning, not "[Title] at [Company]."

5. **Current location and industry** — set correctly. Recruiter search filters on both.

**Upper profile sections:**

6. **About section** — uses Prompt 2. First 210 characters deliver a hook that stands alone without needing "see more."

7. **Featured section** — pinned above experience. Include 2–4 items: best-performing post, portfolio link, one piece of published writing, or a link to your resume / portfolio / calendar. If this is empty, the profile looks like a shell.

8. **Services (if freelance / consulting / open to services work)** — enabled with 2–5 specific services and rate context. Skip if fully employed and not freelancing.

9. **Open to Work (if job-hunting)** — use the platform feature, not the headline. Choose the "recruiters only" visibility unless you're openly public about the search. The green frame around the profile photo is fine; the #OpenToWork banner on the headshot is too loud for most industries — skip.

**Body sections:**

10. **Experience section** — every role uses Prompt 3 structure (short intro + 3–5 outcome bullets). No "responsibilities" framing. Current role especially well-written.

11. **Skills section** — uses Prompt 4. Top 3 pinned skills match highest-priority keywords in target job postings. 30–45 total, categorized, no soft-skill padding.

12. **Education** — listed with dates. Add 1–2 relevant courses, certifications, or honors if they strengthen the role target.

**Social proof:**

13. **Recommendations** — at least 3 on the profile. Uses Prompt 7 to request. Each is specific, not generic. Mix of relationship types (former manager, peer, cross-functional partner) carries more weight than 3 from the same angle.

14. **Activity** — visible posting or commenting history in the last 60 days. If the most recent activity is 8 months ago, the profile reads as abandoned. Minimum bar: 1 thoughtful comment per week on relevant posts. Upper bar: 1 post every 1–2 weeks.

---

## Weekly content pack — 10 post types

Use this as a library. Rotate through types; don't post the same type twice in a row. Each type below references Prompt 5 in this module for the full writing prompt — these descriptions are just the type, its use case, and the calibration guide.

**1. Contrarian take**
*When to use*: you have a position on something most people in your field get wrong. Not hot takes — earned takes.
*Calibration*: post monthly max. Overuse reads as performative disagreement.

**2. Specific failure / lesson learned**
*When to use*: something you tried didn't work, and the lesson is concrete.
*Calibration*: strong every time if the story is specific. Weak if generalized ("I learned the importance of communication" — skip).

**3. Framework or cheat sheet**
*When to use*: you have a repeatable process you use in your work and can explain in 3–5 steps.
*Calibration*: these travel — often the most-saved post type.

**4. Observation from the field**
*When to use*: you noticed something happening in your industry that deserves a post but isn't hot take territory.
*Calibration*: needs specific evidence, not just "I think X is trending."

**5. Ask / call for collaborators or help**
*When to use*: you want something specific — intros, collaborators, a mentor, a role. Specificity earns responses.
*Calibration*: once per month max. Reads as selfish if overused.

**6. Behind-the-scenes / work-in-progress**
*When to use*: you're shipping something and want to narrate the process. Strong for builders, consultants, founders.
*Calibration*: weekly okay if you're actually building something visible.

**7. Credit someone else**
*When to use*: someone on your team, in your network, or in your field did something worth calling out. Tag them.
*Calibration*: monthly. Builds network. Reads as genuine only if it's specific and the credit isn't self-serving.

**8. Numbers post / data snapshot**
*When to use*: you ran a number, an experiment, or a report and have findings worth sharing.
*Calibration*: strongest post type for technical or data-heavy fields. Needs real numbers and honest framing.

**9. Industry reading / recommendation**
*When to use*: a book, article, podcast, or framework changed how you think about your work.
*Calibration*: monthly. Keep it short — not a book review; one takeaway and why it matters.

**10. Retrospective / milestone**
*When to use*: a project, a year, a launch just ended. Reflect on what shipped and what you learned.
*Calibration*: rare use — anniversaries, launches, year-ends. Overuse reads as self-congratulatory.

**Posting cadence rule**: start at 1 post per week for 4 weeks, then evaluate response rates before scaling. Posting 3× per week without a follower base burns content and generates no reach.
