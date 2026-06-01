# Pinterest pin variants — test session

**Scheduled date:** Saturday, July 19, 2026

**Why July 19:** Pinterest batch 2 starts publishing June 7. By July 19, batch 2 has been live for 6 weeks — enough Pinterest data to see which pin formats are actually performing before generating variants. Batch 3 doesn't start until July 17 (per `PINS-BATCH-3.md` schedule), so two days into batch 3 you'll have early signal there too.

**Add to calendar:** Calendar.app → New Event → "Pinterest pin variants — test session" → Saturday July 19 9 AM-12 PM MT → save.

---

## What to do that day

1. **(30 min) Pull Pinterest analytics** for batch 2 (pin-21 to pin-40)
   - Open https://analytics.pinterest.com
   - Sort by Impressions descending. Note the top 5 and bottom 5
   - Sort by Click-through rate. Note the top 5 and bottom 5
   - Are the high-performers career or finance? NAVY or FOREST? Are headlines question-format, stat-format, or topic-format?
2. **(15 min) Identify the pattern** behind the top 5 performers — color, density, format
3. **(60 min) Build the 5 variants below** by editing `pins/generate_pins.py` and regenerating
4. **(15 min) Add 5 variants to `pins/PINS-BATCH-4.md`** with scheduling (start September 1 or later)

---

## The 5 variants to test (from 2026-06-02 brainstorm)

### 1. Tighter visual hierarchy

Most current pins are text-dense. Cut the text by 50%, double the whitespace, increase headline font size 20-30%.

**Test pair:**
- pin-41-tailor-resume.png (current, "TAILOR YOUR / RESUME IN / 20 MINUTES" + 3 benefit lines)
- pin-61-tailor-resume-tight.png (new, "TAILOR YOUR RESUME" + 1 benefit line + bigger negative space)

### 2. Stat-first variant

Pinterest performance favors stat hooks over topic hooks.

**Test pin idea:**
- Replace headline with a specific stat: "8 SECONDS TO CUT YOUR COVER LETTER" or "$12K MORE ON YOUR FIRST OFFER"
- Subhead becomes the topic ("how recruiters skim" / "the BATNA worksheet")
- Same destination URLs as the current pin

**Build 3 variants:**
- pin-62-cover-letter-8sec.png (8-second cover letter cut)
- pin-63-salary-12k.png ($12K negotiation increase)
- pin-64-resume-20min.png (tailored resume in 20 min)

### 3. Before/after format

Visual split-screen pin showing AI tells vs the fix.

**Test pin idea:**
- Top half: "BEFORE: I am writing to express my strong interest..." (set in cream-on-navy)
- Bottom half: "AFTER: Three months ago I sat through your CTO's QCon talk..." (set in cream-on-violet for contrast)
- One line of source: "the snipprompts cover letter prompt"

**Build 2 variants:**
- pin-65-cover-letter-before-after.png
- pin-66-resume-bullet-before-after.png

### 4. Question-format pin

Question headlines drive click-for-the-answer behavior on Pinterest.

**Test pin idea:**
- "WHAT'S THE WORST OPENING LINE FOR A COVER LETTER?"
- "WHAT 4 PHRASES DO RECRUITERS GREP FOR?"
- "WHAT'S THE ONE LINE THAT STOPS CHATGPT FROM INVENTING METRICS?"

**Build 3 variants:**
- pin-67-worst-opening.png
- pin-68-4-phrases.png
- pin-69-one-line-invent.png

### 5. Color test — inverted palette

Current pins: NAVY background, CREAM text. Pinterest algorithm favors high-contrast pins; inverted may rank differently.

**Test pin idea:**
- Same content as a top-performing existing pin (whichever pin-21 to pin-40 has the highest CTR)
- New version: CREAM background, NAVY text
- Add subtle violet accent line for brand consistency

**Build 1 variant:**
- pin-70-inverted-[topic].png (topic = whatever the top-performer was)

---

## After the test

1. Schedule the 10 new variants (pin-61 to pin-70) to start **September 1, 2026** (gives batch 3 time to run + a clean monthly boundary for comparison)
2. Tag each pin in `PINS-BATCH-4.md` with its hypothesis ("tight hierarchy," "stat hook," etc.)
3. Set a reminder for **October 15, 2026** to review batch 4 performance and decide which formats to scale into batch 5

---

## Don't deviate

- Don't decide which format wins after 7 days. Pinterest takes 30-45 days to surface real signal.
- Don't generate variants for prompts/landing pages that haven't already been pinned. Test against existing data, not new ground.
- Don't redesign the brand. The NAVY/FOREST/CREAM palette is fine. We're testing pin-level format variations, not a rebrand.
