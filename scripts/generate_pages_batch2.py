"""Generate batch 2 of high-traffic prompt pages."""
import sys
sys.path.insert(0, 'scripts')
from page_template import make_page

PAGES = [
    {
        "slug": "best-chatgpt-prompt-for-sales-pitch",
        "title": "Best ChatGPT Prompt for Sales Pitch",
        "subtitle": "Write sales pitches that close deals — cold pitches, elevator pitches, and discovery call openers.",
        "prompt": """You are a top 1% B2B sales professional who has closed $100M+ in deals. Write a sales pitch for me.

Pitch type: [cold email / elevator pitch / discovery call opener / demo close / follow-up]
What I sell: [PRODUCT/SERVICE]
Price point: $[AMOUNT]
My target buyer: [TITLE, COMPANY SIZE, INDUSTRY]
Their main pain point: [SPECIFIC PROBLEM YOU SOLVE]
Why me vs. competitors: [YOUR UNIQUE ADVANTAGE]
Proof: [TESTIMONIAL, CASE STUDY, OR RESULT]
Goal of this pitch: [book a meeting / get a reply / close the deal / upsell]

Requirements:
- Open with a hook about THEIR world, not mine
- Keep it under 100 words for cold pitches
- Use specific numbers, not vague claims
- Address one objection preemptively
- End with a clear, low-friction next step
- No buzzwords ('synergy,' 'leverage,' 'game-changer')
- Sound human — write like you talk""",
        "how_to_use": [
            "Be specific about your buyer — a CFO at a startup reads very differently than a VP Sales at enterprise",
            "Include a real case study or result — proof is your single biggest weapon",
            "Write 3 versions and A/B test the subject lines on cold emails",
            "After the pitch, say 'Now write 3 follow-up emails in a 10-day sequence if they don't reply'",
        ],
        "example_output": """<p><strong>Cold email for a sales intelligence tool, $5K ACV, targeting VP Sales at Series B startups:</strong></p>
<p><strong>Subject:</strong> Your team's 40% close rate (or is it lower?)</p>
<p>Hey Sarah,</p>
<p>Most VPs I talk to think their close rate is around 40% — but when we plug in their CRM data, it's usually 22-28%. The gap is almost always in the handoff from SDR to AE.</p>
<p>We help sales teams fix that gap. For [similar company], it meant $2.1M in recovered pipeline in Q1.</p>
<p>Worth 20 minutes next week to see if the same gap exists on your team? I can come with 3 specific observations from looking at your team's public-facing data.</p>
<p>— Alex</p>""",
        "tips": [
            "<strong>Research first.</strong> Say 'Write this email after you've read their LinkedIn, company news, and funding announcements.'",
            "<strong>Open with them.</strong> Ask 'Make the first sentence about the prospect, not about us.'",
            "<strong>Low-friction CTA.</strong> 'Worth 20 minutes' converts better than 'book a call.'",
            "<strong>Personalize 1 thing.</strong> Ask 'How do I personalize the opener based on [specific detail]?'",
        ],
        "amazon_keywords": "sales+book+bestseller+closing",
        "amazon_text": "Sales Books on Amazon",
        "related": [("best-chatgpt-prompt-for-copywriting", "Copywriting"), ("best-chatgpt-prompt-for-email-marketing", "Email Marketing")],
    },
    {
        "slug": "best-chatgpt-prompt-for-resignation-letter",
        "title": "Best ChatGPT Prompt for Resignation Letter",
        "subtitle": "Write a professional resignation letter that protects your reputation and leaves doors open.",
        "prompt": """You are an HR consultant who has reviewed thousands of resignation letters. Write one for me.

My current role: [JOB TITLE]
Company: [COMPANY NAME]
Manager name: [NAME]
Tenure: [HOW LONG I'VE BEEN THERE]
Last day I want to work: [DATE — typically 2 weeks out, unless negotiated otherwise]
Reason for leaving (optional, kept private): [for context only — new job / career change / personal / toxic environment]
Tone I want: [professional and warm / purely formal / brief and neutral]
Relationship with manager: [great / okay / strained]

Requirements:
- Keep it under 200 words
- State the fact of resignation in the first sentence
- Include last day of work clearly
- Express gratitude briefly (if authentic — don't force it)
- Offer to help with transition
- Never burn bridges, even if the situation was bad
- No specific reason required — 'I've accepted another opportunity' is enough
- Avoid anything that could be used against me in a reference later""",
        "how_to_use": [
            "The letter is for HR/record — don't put venting or grievances in it",
            "Have a separate conversation with your manager before sending the letter",
            "Keep it short — short letters are always safer than long ones",
            "If the environment was toxic, be especially careful — neutral tone protects you",
        ],
        "example_output": """<p><strong>Subject:</strong> Resignation — Alex Martinez</p>
<p>Dear Jennifer,</p>
<p>I'm writing to formally resign from my position as Senior Product Manager, with my last day on April 30, 2026.</p>
<p>Thank you for the opportunity to work with you and the product team over the past three years. I've learned a tremendous amount here, and I'm especially grateful for your mentorship during the platform launch last year.</p>
<p>I'll do everything I can to make this transition smooth. I'm happy to document my current projects, train whoever takes over my responsibilities, and be available for questions after I leave.</p>
<p>I look forward to staying in touch.</p>
<p>Best regards,<br>Alex Martinez</p>""",
        "tips": [
            "<strong>Always go in person first.</strong> Ask 'Script what I should say to my manager before handing over the letter.'",
            "<strong>Don't explain too much.</strong> Ask 'How do I decline if they ask why I'm leaving?'",
            "<strong>Counter-offer prep.</strong> Ask 'How do I respond if they make a counter-offer?'",
            "<strong>Get it in writing.</strong> Ask 'Write the follow-up email confirming the last day and handover plan.'",
        ],
        "amazon_keywords": "career+change+book+job+search",
        "amazon_text": "Career Books on Amazon",
        "related": [("best-chatgpt-prompt-for-writing-a-cover-letter", "Writing a Cover Letter"), ("best-chatgpt-prompt-for-job-interview-prep", "Job Interview Prep")],
    },
    {
        "slug": "best-chatgpt-prompt-for-thank-you-note",
        "title": "Best ChatGPT Prompt for Thank You Notes",
        "subtitle": "Write thoughtful thank you notes for any occasion — job interviews, gifts, favors, or just because.",
        "prompt": """You are a writer who specializes in warm, personal notes. Write a thank you message for me.

Thank you for: [WHAT THEY DID — be specific]
Recipient: [RELATIONSHIP — e.g. interviewer, grandma, coworker, friend, vendor]
Format: [handwritten card / email / text / LinkedIn message / formal letter]
How well you know them: [close / professional / met once / don't know them well]
Tone: [warm / formal / casual / heartfelt / funny]
Anything specific they did that stood out: [DETAIL YOU WANT TO REFERENCE]
Length: [short (2-3 sentences) / medium / longer note]

Requirements:
- Reference the specific thing they did, not generic 'thank you for everything'
- Mention one thing you'll remember or that made an impact
- Keep it personal — avoid corporate-sounding phrases
- Write 3 versions in slightly different tones
- Match the format — a text is way shorter than a card
- For job interview thank yous: reference a specific moment from the conversation""",
        "how_to_use": [
            "Always reference a specific detail — generic thanks feels hollow",
            "For job interview thank yous, send within 24 hours or don't bother",
            "Handwritten notes for anything meaningful — email for professional efficiency",
            "Match the energy of your relationship — don't force warmth that isn't there",
        ],
        "example_output": """<p><strong>Post-interview thank you (email, within 24 hours):</strong></p>
<p>Hi Jordan,</p>
<p>Thank you for taking the time to meet with me today. I really enjoyed our conversation, especially when we got into the challenges around the platform migration — your point about prioritizing developer experience over feature velocity stuck with me.</p>
<p>The role sounds like exactly the kind of scope I'm looking for, and I'd love the chance to help tackle the problems you described.</p>
<p>If there's anything else you need from me to move forward, just let me know.</p>
<p>Best,<br>Maya</p>""",
        "tips": [
            "<strong>Be specific or don't bother.</strong> 'Thanks for your time' is worse than no note at all.",
            "<strong>Timing matters.</strong> Ask 'How soon after [event] should I send this?'",
            "<strong>Handwritten for wedding, funeral, major favor.</strong> Email is fine for work.",
            "<strong>Include a small gift gesture?</strong> Ask 'What small follow-up gesture would be appropriate here?'",
        ],
        "amazon_keywords": "thank+you+cards+stationery",
        "amazon_text": "Thank You Cards on Amazon",
        "related": [("best-chatgpt-prompt-for-birthday-message", "Birthday Messages"), ("best-chatgpt-prompt-for-writing-emails", "Writing Emails")],
    },
    {
        "slug": "best-chatgpt-prompt-for-apology-letter",
        "title": "Best ChatGPT Prompt for Apology Letter",
        "subtitle": "Write a sincere apology that takes responsibility, acknowledges harm, and repairs the relationship.",
        "prompt": """You are a communication expert who specializes in repairing relationships. Write a sincere apology for me.

Who I'm apologizing to: [RELATIONSHIP]
What happened: [DESCRIBE WHAT YOU DID — be honest, not spin]
Why it was wrong: [WHAT HARM IT CAUSED OR COULD HAVE CAUSED]
My actual responsibility: [YOUR PART — no 'we both' or 'they also']
What I should have done: [THE BETTER CHOICE YOU WILL NOW MAKE]
Format: [in-person script / text / email / letter / voicemail script]
Relationship status: [currently estranged / tense / still talking but hurt / long silence]

Requirements:
- Lead with 'I was wrong about X' or 'I'm sorry for X' — specific, not vague
- No 'I'm sorry you felt' or 'if I hurt you' — take full responsibility
- Don't list excuses or context unless they asked for it
- Acknowledge the specific harm my actions caused
- State what I will do differently going forward
- Don't demand forgiveness or closure — give them space
- Keep it shorter than feels comfortable — rambling undermines sincerity""",
        "how_to_use": [
            "Be brutally honest in the input — the AI can't write a real apology if your input is full of justifications",
            "If you can't write this without blaming the other person, you're not ready to apologize",
            "Read it out loud before sending — if it sounds defensive, it is",
            "Don't expect a response. Apology is about acknowledgment, not a transaction",
        ],
        "example_output": """<p><strong>Apology to a friend after breaking their trust (text message):</strong></p>
<p>Sam — I've been thinking a lot about the conversation Tuesday. You told me something in confidence, and I repeated it to Jess. That was a betrayal of your trust, and I'm sorry.</p>
<p>I don't have a good reason for why I did it. It wasn't a slip — I made a choice to share something that wasn't mine to share. I understand if you don't trust me with anything personal for a long time, and I get why.</p>
<p>I'm not asking for anything from you right now. Just wanted you to know I see what I did and I'm working on why I did it.</p>""",
        "tips": [
            "<strong>Avoid 'but.'</strong> Ask 'Rewrite this without the word but anywhere.' Every 'but' negates what came before.",
            "<strong>Name the specific harm.</strong> 'I hurt your trust' beats 'you got hurt.'",
            "<strong>Don't over-apologize.</strong> One clear apology beats ten desperate ones.",
            "<strong>Prepare for any response.</strong> Ask 'What if they're still angry? What if they ignore it? What if they forgive quickly?'",
        ],
        "amazon_keywords": "communication+book+relationships",
        "amazon_text": "Communication Books",
        "related": [("best-chatgpt-prompt-for-writing-emails", "Writing Emails"), ("best-chatgpt-prompt-for-birthday-message", "Birthday Messages")],
    },
    {
        "slug": "best-chatgpt-prompt-for-wedding-speech",
        "title": "Best ChatGPT Prompt for Wedding Speech",
        "subtitle": "Write a memorable wedding speech — maid of honor, best man, parent, or couple toasts that land every time.",
        "prompt": """You are a professional toastmaster who has helped write 200+ wedding speeches. Write a wedding speech for me.

Role: [best man / maid of honor / father of bride / mother of groom / bride / groom / sibling / friend]
Bride's name: [NAME]
Groom's name: [NAME]
How you know them: [YOUR RELATIONSHIP — years, how you met]
3 stories or memories you could share: [LIST — funny, heartfelt, or telling]
One thing that makes their relationship special: [WHAT YOU ADMIRE ABOUT THEM TOGETHER]
Inside jokes or references that work for this crowd: [LIST ANY, or 'keep it universal']
Crowd: [mixed ages — grandparents present? / young and casual / formal]
Target length: [2-3 minutes / 4-5 minutes]
Tone: [funny / heartfelt / balanced / roast-friendly]

Requirements:
- Open with something that gets attention — a laugh or a hook, not 'hi everyone'
- Include ONE short story that shows who they are (not 5)
- Avoid inside jokes that only 3 people get
- Build to a genuine moment — earn the emotion
- End with a clear toast: 'Please raise your glass to...'
- Keep it under the target length when timed at normal speaking pace
- Never embarrass either person, ever
- No mentions of exes, drunk stories, or anything cringey""",
        "how_to_use": [
            "Give the AI real stories with specific details — vague input = generic speech",
            "Time your speech out loud before the wedding — it should take 2-4 minutes max",
            "Practice in front of a friend and cut anything that doesn't land",
            "Print it and use bullet points on note cards, not the full script",
        ],
        "example_output": """<p><strong>Best man speech, 3 minutes, funny + heartfelt:</strong></p>
<p>Good evening everyone — for those who don't know me, I'm Marcus, and I've been Jake's best friend since we were 8 years old, when we both got sent to the principal's office for the same thing, on the same day, from opposite ends of the school. [pause for laugh]</p>
<p>I've watched Jake date people before. I've never once called them the wrong name. That's because Jake has always called them something worse. [pause] There was Sarah-From-Work, Rachel-Who-Won't-Eat-Onions, and of course, his college girlfriend who he only ever referred to as 'the crisis.' [pause]</p>
<p>And then Jake met Priya. I remember the exact moment I knew it was different. He came back from their second date and said her actual name. Not a nickname. Not a qualifier. Just — Priya. [beat]</p>
<p>Priya — from the moment you walked into Jake's life, he became softer, kinder, and way better at doing dishes. He became the version of himself we all knew was in there. [raise glass]</p>
<p>To Jake and Priya — may you keep finding that version of each other for the rest of your lives.</p>""",
        "tips": [
            "<strong>One story rule.</strong> Ask 'Pick the single best story and cut the others.'",
            "<strong>End with a real toast.</strong> 'To Jake and Priya' is non-negotiable — raise the glass.",
            "<strong>Don't open with jokes about yourself.</strong> Jokes about the couple land better.",
            "<strong>Roast with love.</strong> For best man/maid of honor, ask 'Make the roast gentler — how can I tease without embarrassing?'",
        ],
        "amazon_keywords": "wedding+speech+book+toast",
        "amazon_text": "Wedding Speech Books",
        "related": [("best-chatgpt-prompt-for-wedding-planning", "Wedding Planning"), ("best-chatgpt-prompt-for-birthday-message", "Birthday Messages")],
    },
    {
        "slug": "best-chatgpt-prompt-for-lesson-plans",
        "title": "Best ChatGPT Prompt for Lesson Plans",
        "subtitle": "Generate detailed, standards-aligned lesson plans for any grade and subject in minutes.",
        "prompt": """You are a veteran teacher and curriculum designer with 20 years of classroom experience. Build a lesson plan for me.

Subject: [SUBJECT AREA]
Grade level: [GRADE]
Topic: [SPECIFIC TOPIC OR STANDARD]
Lesson length: [MINUTES]
Class size: [STUDENTS]
Student context: [e.g. mixed ability, ELLs, IEPs, advanced, general ed]
Learning standard: [STATE/COMMON CORE standard if applicable, or SKIP]
Available materials: [chromebooks / projector / manipulatives / just paper / etc.]
Student's prior knowledge: [what they already know]

Give me:
1. Learning objective (one clear SWBAT statement)
2. Warm-up / bell-ringer (5 min)
3. Direct instruction with key questions (10-15 min)
4. Guided practice activity (10-15 min)
5. Independent practice or exit ticket (5-10 min)
6. Assessment / how I'll know they got it
7. Differentiation strategies for struggling students and advanced learners
8. Common misconceptions students have with this topic
9. Materials list (copy-ready if possible)

Requirements:
- Ground everything in the standard
- Include student-facing questions, not just teacher talk
- Build in at least one opportunity for student talk/discussion
- Assessment must be quick and tell me whether they mastered the objective""",
        "how_to_use": [
            "Include the specific standard — lesson plans without standards get dinged in evaluations",
            "Be honest about your class — a lesson for advanced students is different from mixed-ability",
            "Ask for a unit plan after: 'Now give me a 5-lesson unit plan leading to this lesson'",
            "Ask for parent communication: 'Write a parent email explaining what we're learning this week'",
        ],
        "example_output": """<p><strong>Lesson:</strong> 6th grade math — Ratios and Proportional Relationships (6.RP.A.1)</p>
<p><strong>SWBAT:</strong> Students will be able to describe a ratio relationship between two quantities using ratio language.</p>
<p><strong>Warm-up (5 min):</strong> "If I have 3 apples for every 2 oranges in this fruit bowl, what does that tell us?" Show image. Think-pair-share (1 min each).</p>
<p><strong>Direct instruction (12 min):</strong> Define ratio. Show 3 representations: words ('for every'), colon notation (3:2), fraction form (3/2). Key question: "Why might we use one form over another?"</p>
<p><strong>Guided practice (12 min):</strong> Work in pairs on 5 problems ranging from basic identification to word problems. Circulate and collect data.</p>
<p><strong>Exit ticket (5 min):</strong> "Write the ratio of desks to students in our classroom in all three forms."</p>""",
        "tips": [
            "<strong>Ask for rubrics.</strong> 'Build me a simple 4-point rubric for this assignment.'",
            "<strong>Scaffold for ELLs.</strong> Ask 'What sentence stems and visuals would help ELL students access this lesson?'",
            "<strong>Substitute plans.</strong> Ask 'Write this so a substitute can teach it without me.'",
            "<strong>Reflection.</strong> After teaching, say 'Here's what worked/didn't in the lesson. Adjust for tomorrow.'",
        ],
        "amazon_keywords": "teacher+resources+curriculum+book",
        "amazon_text": "Teacher Books on Amazon",
        "related": [("best-chatgpt-prompt-for-studying", "Studying"), ("best-chatgpt-prompt-for-essay-writing", "Essay Writing")],
    },
    {
        "slug": "best-chatgpt-prompt-for-research-paper",
        "title": "Best ChatGPT Prompt for Research Papers",
        "subtitle": "Plan, outline, and structure a research paper — thesis, argument, sources, and academic writing polish.",
        "prompt": """You are a research librarian and academic writing coach. Help me with my research paper.

Paper topic: [TOPIC]
Discipline: [e.g. history, psychology, biology, literature]
Academic level: [high school / undergraduate / graduate]
Required length: [PAGES or WORD COUNT]
Citation style: [MLA / APA / Chicago / Turabian / IEEE]
My current stage: [picking topic / have thesis / have outline / have draft]
What I need help with: [thesis development / outline / source suggestions / argument structure / revision]

For each task:
- Thesis development: Give me 3 thesis options with different angles
- Outline: Create a detailed outline with section headings and main points
- Source suggestions: Suggest 5-8 types of sources I should look for (books, journals, databases) — I'll find the actual sources
- Argument structure: Show me how claims, evidence, and analysis should connect
- Revision: Identify weak spots, logical gaps, and grammar issues

Requirements:
- Never fabricate sources, authors, or citations
- Keep the thesis specific and arguable — no 'X is interesting' theses
- For outlines, each section should advance the thesis
- Acknowledge counterarguments in the structure
- Use academic tone but not purple prose""",
        "how_to_use": [
            "Specify what stage you're at — help for choosing a topic is different from help with revision",
            "Never cite AI-suggested sources without verifying — always find the real source",
            "Ask for questions to investigate: 'What questions would a skeptical reader ask about my thesis?'",
            "Use AI for structure and review, not for writing the paper — check your school's AI policy",
        ],
        "example_output": """<p><strong>Thesis options for a 10-page undergrad history paper on the Marshall Plan:</strong></p>
<ol>
<li><strong>Argument A:</strong> "While the Marshall Plan is remembered primarily as humanitarian aid, the primary driver was containment of Soviet influence, revealed by its selective exclusion of Eastern European states and its integration with NATO's founding."</li>
<li><strong>Argument B:</strong> "The Marshall Plan's economic success has overshadowed its most lasting legacy — the template it established for Cold War economic statecraft, which would shape US foreign policy for the next 50 years."</li>
<li><strong>Argument C:</strong> "Revisionist historians have argued the Marshall Plan was more about American market expansion than European recovery; evidence from trade data and congressional testimony suggests this interpretation understates the geopolitical motivations but overstates the economic ones."</li>
</ol>
<p>Argument A is the most focused and arguable — it takes a clear position against a common misconception.</p>""",
        "tips": [
            "<strong>Verify every source.</strong> AI often invents plausible-sounding authors and papers. Google every source before citing.",
            "<strong>Ask for counterarguments.</strong> 'What's the strongest argument against my thesis?' — include it in your paper.",
            "<strong>Test the thesis.</strong> Ask 'Is this thesis arguable, specific, and supported by evidence?'",
            "<strong>Revision pass.</strong> Paste your draft and ask 'Identify weak arguments, logical gaps, or unclear sentences.'",
        ],
        "amazon_keywords": "research+paper+academic+writing+book",
        "amazon_text": "Academic Writing Books",
        "related": [("best-chatgpt-prompt-for-essay-writing", "Essay Writing"), ("best-chatgpt-prompt-for-studying", "Studying")],
    },
    {
        "slug": "best-chatgpt-prompt-for-creative-writing",
        "title": "Best ChatGPT Prompt for Creative Writing",
        "subtitle": "Use AI as a creative writing partner — short stories, character development, plot brainstorming, and feedback.",
        "prompt": """You are an award-winning fiction writer and writing workshop leader. Help me with my creative writing.

What I need: [pick one]
- Brainstorm a story idea around [THEME OR PREMISE]
- Develop a character: [BRIEF DESCRIPTION — flesh them out]
- Solve a plot problem: [DESCRIBE WHERE I'M STUCK]
- Write an opening paragraph for this idea: [PREMISE]
- Give me feedback on this scene: [PASTE SCENE]
- Explore a 'what if' question in my world

Genre: [literary / mystery / sci-fi / romance / horror / fantasy / memoir]
POV: [first / third limited / third omniscient]
Tone: [dark / whimsical / literary / pulpy / dreamlike]
Length of piece: [flash fiction / short story / novella / novel]

Requirements:
- Don't write my whole story — I want to write it, you help me think
- Suggest options, not commands
- For character work, ask me questions that reveal who they are
- For plot problems, offer 3 different solutions with tradeoffs
- For feedback, identify the strongest sentence AND the weakest
- Respect my voice — don't rewrite things into your style
- Cite specific craft principles when giving feedback (Chekhov's gun, showing vs telling, pacing)""",
        "how_to_use": [
            "Use AI for brainstorming and feedback, not to write the actual prose — your voice matters",
            "For character development, answer the AI's questions yourself — don't let it make decisions",
            "When stuck on plot, ask for 3 options and pick the one that feels truest",
            "Paste 500 words of your own writing and ask for feedback on craft specifics, not general praise",
        ],
        "example_output": """<p><strong>Request:</strong> Help me develop a character — a 40-year-old landscape architect whose ex just got engaged.</p>
<p><strong>AI response:</strong></p>
<p>Let's go deeper. Before I suggest anything, tell me:</p>
<ul><li>Why did they break up? Not the clean version — the version with the stuff they don't admit out loud.</li>
<li>What did she build for him that he never got to finish? (Landscape architects shape space for other people — there's metaphor here.)</li>
<li>Is she the kind of person who cries about the engagement, or the kind who Googles the fiancée and finds peace in the fact that he has bad taste?</li>
<li>What's one concrete object in her life that reminds her of him? A chair, a tree she planted, a particular recipe?</li></ul>
<p>Your answers will shape her much more than anything I could invent.</p>""",
        "tips": [
            "<strong>Ask for writer-mode feedback.</strong> Say 'Be a tough workshop leader — what's not working and why?'",
            "<strong>Mine your own life.</strong> Say 'Give me 10 questions to ask myself about this character that connect to real experiences I've had.'",
            "<strong>Study craft.</strong> Ask 'What technique would [admired author] use in this scene?'",
            "<strong>Kill darlings.</strong> Paste a paragraph and ask 'What could I cut without losing anything essential?'",
        ],
        "amazon_keywords": "creative+writing+craft+fiction+book",
        "amazon_text": "Writing Craft Books",
        "related": [("best-chatgpt-prompt-for-essay-writing", "Essay Writing"), ("best-chatgpt-prompt-for-writing-a-blog-post", "Writing a Blog Post")],
    },
    {
        "slug": "best-chatgpt-prompt-for-journaling",
        "title": "Best ChatGPT Prompt for Journaling",
        "subtitle": "Get thoughtful journaling prompts for self-reflection, gratitude, goal-setting, and processing hard moments.",
        "prompt": """You are a therapist and journaling expert who helps people use writing for self-reflection. Generate journaling prompts for me.

My current state: [e.g. stressed, grieving, transitioning careers, stuck in a rut, feeling good and want to deepen it]
What I want to explore: [e.g. anxiety triggers, relationship patterns, what I actually want from life, why I keep self-sabotaging]
How much time I have: [5 min / 15 min / 30 min+ sessions]
Experience with journaling: [first-timer / do it occasionally / daily practice]
Format preference: [single deep question / series of connected questions / checklist-style]

Give me:
1. A core prompt that gets at the heart of what I'm exploring
2. 3-5 deeper follow-up questions to dig further
3. One question designed to surface something uncomfortable but useful
4. A closing question that helps me integrate what came up
5. If I asked for it, a grounding or breathing exercise for before journaling

Requirements:
- Ask open-ended questions, not yes/no
- Avoid advice — just surface the questions
- Don't be therapy-speak — use human language
- Range from surface to deep, not all deep
- End with integration, not more darkness""",
        "how_to_use": [
            "Be honest about your state — the prompts calibrate based on where you are",
            "Write by hand if possible — it accesses different parts of the brain than typing",
            "Set a timer and don't stop writing until it goes off, even if you repeat yourself",
            "Don't re-read for at least a few hours — let it settle before editing your thoughts",
        ],
        "example_output": """<p><strong>Topic:</strong> Why do I keep saying yes to things I don't want to do?</p>
<p><strong>Core prompt:</strong> Think of the last three times you said yes when your body wanted to say no. What did you tell yourself in the moment about why you had to agree?</p>
<p><strong>Follow-ups:</strong></p>
<ul><li>Who taught you that your preference was less important than theirs?</li>
<li>What would happen if you said no this week to something small? What's the actual risk?</li>
<li>What do you imagine people would think of you if you protected your time more? Is that true, or inherited fear?</li></ul>
<p><strong>Uncomfortable question:</strong> Whose love do you think you'd lose if you stopped being so accommodating?</p>
<p><strong>Integration:</strong> What's one small no you could say this week that would honor what you actually want?</p>""",
        "tips": [
            "<strong>Write without editing.</strong> Ask the AI: 'Before I start, remind me I'm writing for myself, not anyone else.'",
            "<strong>Track patterns.</strong> After 30 days: 'Give me a prompt to look back at my journals and find themes.'",
            "<strong>Seasonal resets.</strong> Quarterly, ask 'Give me prompts for a seasonal life review — what's ending, starting, continuing.'",
            "<strong>Hard days.</strong> Ask 'Give me a 5-minute crisis journaling prompt for when I'm overwhelmed.'",
        ],
        "amazon_keywords": "journal+notebook+daily+journaling",
        "amazon_text": "Journals on Amazon",
        "related": [("best-chatgpt-prompt-for-studying", "Studying"), ("best-chatgpt-prompt-for-book-summary", "Book Summaries")],
    },
    {
        "slug": "best-chatgpt-prompt-for-goal-setting",
        "title": "Best ChatGPT Prompt for Goal Setting",
        "subtitle": "Set goals you'll actually achieve — with clear metrics, realistic timelines, and weekly action plans.",
        "prompt": """You are a performance coach who has helped executives and high-performers achieve their goals. Help me set and plan a goal.

My big goal: [WHAT YOU WANT TO ACHIEVE — be specific]
Timeframe: [BY WHEN]
Why this matters to me: [THE REAL REASON — not what sounds good]
Where I am now: [STARTING POINT WITH SPECIFICS]
What's gotten in the way before: [HONEST REASONS PAST ATTEMPTS FAILED]
How much time I can commit weekly: [HOURS]
Support/resources I have: [PEOPLE, MONEY, TOOLS]
Constraints I'm working around: [JOB, KIDS, HEALTH, ETC.]

Build me:
1. A clear, measurable version of this goal (if it's not already specific enough)
2. The 3 key metrics I'll track weekly
3. A milestone plan: monthly targets from now until the deadline
4. Weekly actions for Week 1 (exactly what to do)
5. The 2 biggest likely obstacles and how I'll respond when they show up
6. A 'minimum viable effort' version for bad weeks
7. One question to ask myself if I start drifting off track

Requirements:
- Make the goal measurable — 'get healthier' is not a goal
- Focus on process (actions) over outcomes (results) for weekly tracking
- Build in flexibility for the weeks life gets hard
- If the goal is unrealistic for my time/resources, say so and suggest a more realistic version""",
        "how_to_use": [
            "Be honest about what's failed before — the plan should address the specific reasons",
            "Track weekly, not daily — daily tracking is a trap that leads to guilt",
            "Revisit monthly: 'Here's my progress. Adjust the plan.'",
            "Don't chase the perfect plan — start executing the mediocre plan now",
        ],
        "example_output": """<p><strong>Goal:</strong> Run a half-marathon in 6 months</p>
<p><strong>Measurable version:</strong> Complete a 13.1-mile race on October 15 with no walking breaks, aiming for a time under 2:15.</p>
<p><strong>Key weekly metrics:</strong></p>
<ul><li>Miles run per week (target: progressively 10 → 25)</li>
<li>Longest single run (progressively 3 → 11 miles)</li>
<li>Consecutive weeks without missing 2+ runs</li></ul>
<p><strong>Milestone plan:</strong></p>
<ul><li><strong>Month 1:</strong> Build base. 3 runs/week, 10-15 miles/week total.</li>
<li><strong>Month 2:</strong> Introduce long run. 3-4 runs/week, long run building 4 → 7 miles.</li>
<li><strong>Month 3:</strong> Tempo work. 4 runs/week, long run 8 miles.</li>
<li><strong>Month 4:</strong> Peak training. Long run reaches 10 miles.</li>
<li><strong>Month 5:</strong> Peak + first 11-mile long run. Test race pace.</li>
<li><strong>Month 6:</strong> Taper 2 weeks before race.</li></ul>
<p><strong>Minimum viable effort for bad weeks:</strong> 2 short 20-min runs. Maintains the habit.</p>""",
        "tips": [
            "<strong>Process goals over outcome goals.</strong> Ask 'Rewrite my goal around things I control (effort) not things I don't (results).'",
            "<strong>Visible tracking.</strong> Ask 'Design a simple weekly tracker I can keep on my fridge.'",
            "<strong>Pre-commit to obstacles.</strong> Ask 'Help me write if-then plans for the top 3 obstacles.'",
            "<strong>Quarterly review.</strong> Ask 'Build me a 30-minute quarterly review to assess progress.'",
        ],
        "amazon_keywords": "planner+goal+setting+productivity",
        "amazon_text": "Planners on Amazon",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-workout-plan", "Workout Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-habit-building",
        "title": "Best ChatGPT Prompt for Building a Habit",
        "subtitle": "Build a habit that actually sticks — using proven behavior change principles and a 60-day plan.",
        "prompt": """You are a behavior change coach trained in the methods of BJ Fogg and James Clear. Help me build a habit.

The habit I want to build: [BE SPECIFIC — 'run 3x per week' not 'exercise more']
Why this habit matters to me: [THE REAL WHY]
When do I want to do it: [TIME OF DAY]
Where: [PHYSICAL LOCATION]
What triggers or cues exist: [WHAT ALREADY HAPPENS RIGHT BEFORE THIS TIME]
What's gotten in the way before: [PAST OBSTACLES]
What would make this habit enjoyable, or at least bearable: [REWARDS, MUSIC, COMPANIONSHIP]
How willing am I to scale it down: [not at all / somewhat / start tiny]

Build me:
1. A 'tiny' version of this habit that takes under 2 minutes
2. A clear habit stack: 'After [existing habit], I will [new habit] for [time/reps]'
3. Environmental setup: what to change in my space to make the habit obvious and easy
4. A 60-day progression plan with when to scale up
5. What to do on days I don't want to — the 'never miss twice' rule
6. How to track it simply (no apps needed unless I want)
7. A reward system that reinforces without being junky

Requirements:
- Start way smaller than I think is reasonable
- Focus on consistency first, intensity later
- Build on existing habits rather than creating new ones in isolation
- Remove friction from the good habit, add friction to the bad one
- Plan for failure — it's part of the process, not a sign to quit""",
        "how_to_use": [
            "Start smaller than feels worth doing — 'one pushup' is better than 'do an actual workout'",
            "Track on paper with a simple X on a calendar — digital trackers often fail",
            "Never miss twice — missing one day is normal, missing two days starts a new pattern",
            "After 30 days, ask: 'Here's what's working/not. Adjust the plan for the next 30.'",
        ],
        "example_output": """<p><strong>Habit:</strong> Daily meditation.</p>
<p><strong>Tiny version:</strong> 1 minute of sitting with eyes closed after making morning coffee.</p>
<p><strong>Habit stack:</strong> After I pour my morning coffee, I will sit in the chair by the window and close my eyes for 1 minute.</p>
<p><strong>Environmental setup:</strong></p>
<ul><li>Put a meditation cushion next to the coffee maker</li>
<li>Remove phone from morning routine entirely — charge in another room</li>
<li>Set a visible timer (not the phone) to 1 minute</li></ul>
<p><strong>60-day progression:</strong></p>
<ul><li>Days 1-14: 1 minute, every day, no increase</li>
<li>Days 15-30: 3 minutes</li>
<li>Days 31-60: 5-10 minutes, depending on the day</li></ul>
<p><strong>Missed day protocol:</strong> Never skip two days. If you miss, do the tiny version (1 minute) the next day — don't try to 'make up' by doing more.</p>""",
        "tips": [
            "<strong>Stack on strongest habit.</strong> Ask 'What's the most consistent daily thing I already do?' Anchor there.",
            "<strong>Make it obvious.</strong> Ask 'What should be visible in my environment to trigger this habit?'",
            "<strong>Identity frame.</strong> Say 'Rewrite my habit in identity terms — not I want to X, but I am the kind of person who X.'",
            "<strong>Log it simply.</strong> Ask 'Design the dumbest possible tracking system.' Often wins vs. apps.",
        ],
        "amazon_keywords": "habit+tracker+book+behavior+change",
        "amazon_text": "Habit Books on Amazon",
        "related": [("best-chatgpt-prompt-for-goal-setting", "Goal Setting"), ("best-chatgpt-prompt-for-workout-plan", "Workout Plan")],
    },
    {
        "slug": "best-chatgpt-prompt-for-gardening",
        "title": "Best ChatGPT Prompt for Gardening",
        "subtitle": "Get a custom gardening plan — what to plant, when, where, and how to keep it alive in your climate.",
        "prompt": """You are a master gardener with 25 years of experience. Help me with my garden.

Location: [CITY, STATE — for climate zone]
Garden type: [container / raised beds / in-ground / indoor / balcony]
Sun exposure: [full sun 6+ hours / partial / shade]
Garden size: [SQUARE FEET OR POT COUNT]
Soil type (if known): [sandy / clay / loam / potting mix / don't know]
Experience level: [beginner / intermediate / advanced]
What I want to grow: [vegetables / flowers / herbs / fruit / mix — be specific]
Time I can commit weekly: [HOURS]
Current season: [MONTH]
Issues I'm facing (if any): [pests / diseases / dying plants / etc.]

Give me:
1. A month-by-month planting and care calendar for my climate zone
2. A list of 5-8 plants well-suited to my conditions and skill level
3. Spacing and layout recommendations for my available space
4. Watering schedule based on the plants and my climate
5. Common pests/diseases I should watch for and prevention
6. What to plant together (companion planting) and what to keep apart
7. A beginner-friendly troubleshooting guide
8. Tools I actually need vs. tools I can skip

Requirements:
- Base advice on my specific USDA climate zone
- Match plant suggestions to my experience level — not 'grow heirloom tomatoes' if I've never grown anything
- Be practical — consider my time commitment
- Include both easy wins and 1-2 learning stretches""",
        "how_to_use": [
            "Include your city so the AI can match advice to your climate zone",
            "Be honest about time commitment — a lush garden takes hours/week",
            "For troubleshooting, describe symptoms in detail: 'yellowing bottom leaves, drooping' beats 'it looks bad'",
            "Take photos and describe to the AI: 'Leaves have white spots — what's wrong?'",
        ],
        "example_output": """<p><strong>Setup:</strong> Raised bed garden in Denver, CO (Zone 5b), full sun, 4x8 ft, beginner, 3 hours/week.</p>
<p><strong>Recommended plants:</strong></p>
<ul><li><strong>Easy wins:</strong> Cherry tomatoes, zucchini, basil, lettuce mix, radishes</li>
<li><strong>Stretch (still beginner-friendly):</strong> Peppers, bush beans</li></ul>
<p><strong>Layout:</strong></p>
<ul><li>North end: 2 tomato plants (they'll grow tall, so they don't shade other plants)</li>
<li>Middle: 4 pepper plants, basil tucked between tomatoes (companion plant)</li>
<li>South end: lettuce and radishes (quick-growing, can be replanted mid-summer)</li>
<li>Edges: bush beans</li></ul>
<p><strong>May-June schedule:</strong> Water deeply 2-3x/week in morning. Mulch to reduce watering by half. Check for aphids weekly — spray off with hose if found.</p>""",
        "tips": [
            "<strong>Start small.</strong> Ask 'What's the smallest version of this garden that would still feel rewarding?'",
            "<strong>Match your climate.</strong> Say 'What's the biggest mistake beginners make in [your state]?'",
            "<strong>Succession planting.</strong> Ask 'How can I replant to get 3 harvests from one bed?'",
            "<strong>Pest ID.</strong> Describe symptoms and ask 'What's likely attacking my plant and what's the least-chemical fix?'",
        ],
        "amazon_keywords": "gardening+book+beginner+vegetable",
        "amazon_text": "Gardening Books on Amazon",
        "related": [("best-chatgpt-prompt-for-meal-planning", "Meal Planning"), ("best-chatgpt-prompt-for-recipes", "Recipes")],
    },
    {
        "slug": "best-chatgpt-prompt-for-skincare-routine",
        "title": "Best ChatGPT Prompt for Skincare Routine",
        "subtitle": "Get a skincare routine tailored to your skin type, concerns, and budget — no gimmicky products.",
        "prompt": """You are a licensed esthetician and dermatology researcher who understands ingredients, not marketing. Build me a skincare routine.

Skin type: [dry / oily / combination / normal / sensitive]
Age: [AGE]
Main concerns (pick 1-3): [acne / aging/fine lines / hyperpigmentation / redness / dullness / large pores / dryness / oiliness / sensitivity]
Current products I use: [LIST THEM]
Budget: [drugstore / mid-range / luxury / mix]
Willingness to layer products: [minimalist 3 steps / willing to do 5-7 steps]
Any known sensitivities: [fragrance, retinoids, acids, essential oils, etc.]

Give me:
1. A morning routine with product categories (not specific brands) and active ingredients to look for
2. An evening routine following the same format
3. What to introduce gradually vs. immediately — order matters for actives
4. Ingredients to LOOK FOR for my concerns, and what % strengths to target
5. Ingredients to AVOID together (irritating combinations)
6. Realistic timeline for seeing results — what changes when
7. A budget-friendly starter stack (name categories, not brands — I'll research)
8. When to see a dermatologist

Requirements:
- Focus on evidence-backed ingredients (retinoids, vitamin C, niacinamide, salicylic acid, AHAs/BHAs)
- Don't recommend specific brand names — recommend categories and active %
- Be honest about what skincare can and can't do
- If my concern needs a dermatologist (severe acne, suspected rosacea, dark spots with irregular shape), say so""",
        "how_to_use": [
            "Be specific about skin type — 'normal' and 'combination' need different routines",
            "Don't skip the 'how long to see results' part — skincare takes 8-12 weeks minimum",
            "Introduce one active ingredient at a time — layering too fast destroys your barrier",
            "For serious concerns (persistent acne, sudden changes), see a dermatologist before any routine",
        ],
        "example_output": """<p><strong>Setup:</strong> 28yo, combination skin, main concerns: mild acne + early fine lines + some hyperpigmentation from old breakouts.</p>
<p><strong>Morning:</strong></p>
<ol><li>Gentle cleanser (cream or gel, pH balanced)</li>
<li>Vitamin C serum (10-20% L-ascorbic acid, or 5% for sensitivity)</li>
<li>Moisturizer (with niacinamide 4-5% for both oil control and fine lines)</li>
<li>Sunscreen SPF 30+ (broad spectrum, mineral or chemical — whichever you'll actually wear daily)</li></ol>
<p><strong>Evening:</strong></p>
<ol><li>Same gentle cleanser (or oil cleanser first if wearing makeup/SPF)</li>
<li>3-4x/week: salicylic acid 1-2% (acne) OR retinoid (fine lines) — NOT same night, rotate</li>
<li>Moisturizer</li></ol>
<p><strong>Timeline:</strong> Expect worse skin in weeks 2-4 (purging from retinoid), improvement at week 6-8, visible difference at 12 weeks.</p>""",
        "tips": [
            "<strong>Less is more.</strong> Ask 'What's the minimum routine for real results?'",
            "<strong>Patch test.</strong> Ask 'How do I patch test a new active and know if my skin accepts it?'",
            "<strong>Sunscreen daily.</strong> It's not optional. Ask 'Why is SPF the most important step?'",
            "<strong>Ingredient check.</strong> Paste an ingredient list and ask 'Any red flags or unnecessary ingredients?'",
        ],
        "amazon_keywords": "skincare+routine+book+skincare+ingredients",
        "amazon_text": "Skincare Books on Amazon",
        "related": [("best-chatgpt-prompt-for-workout-plan", "Workout Plan"), ("best-chatgpt-prompt-for-meal-planning", "Meal Planning")],
    },
    {
        "slug": "best-chatgpt-prompt-for-car-buying",
        "title": "Best ChatGPT Prompt for Car Buying",
        "subtitle": "Pick the right car, negotiate the best price, and avoid dealer tricks — with a research and negotiation plan.",
        "prompt": """You are a consumer advocate and former car dealer who now helps buyers get the best deal. Help me buy a car.

What I need help with: [pick one]
- Choose what car to buy for my needs
- Research a specific car: [MAKE/MODEL/YEAR]
- Negotiation plan for a car I've picked
- Trade-in strategy for my current car
- Used vs. new decision

My situation:
- Budget: $[TOTAL] or monthly payment I can afford: $[PER MONTH]
- Primary use: [commuting / family / road trips / off-road / luxury / work truck]
- Must-haves: [e.g. AWD, 3rd row, good MPG, towing capacity, specific brand]
- New or used: [new / used / certified pre-owned / flexible]
- Trade-in: [YES — describe the car / NO]
- Financing: [cash / dealer / credit union / pre-approved elsewhere]
- Location: [CITY, STATE — affects pricing and taxes]

Give me:
1. A clear recommendation with reasoning
2. True cost of ownership over 5 years (not just sticker price) — insurance, fuel, maintenance, depreciation
3. A pricing target: invoice price, expected dealer discount, out-the-door price
4. Scripts for the 3 dealer tactics to expect (payment-focused selling, 'what will it take to get you in this car today,' finance office upsells)
5. How to research fair market value for this model in my area
6. Whether to wait for a better time to buy
7. Red flags that mean I should walk away

Requirements:
- Always recommend getting pre-approved financing BEFORE walking into a dealer
- Always negotiate out-the-door price, not monthly payment
- Warn about common markup traps: VIN etching, extended warranties, GAP insurance pricing
- If used, recommend a pre-purchase inspection from an independent mechanic""",
        "how_to_use": [
            "Get pre-approved through your bank or credit union before you step on a dealer lot",
            "Negotiate over email first — pit 3-4 dealers against each other on out-the-door price",
            "Never negotiate monthly payment — always negotiate total price",
            "Walk into the finance office knowing every single upsell to decline",
        ],
        "example_output": """<p><strong>Setup:</strong> Looking at a 2022 Toyota RAV4 Hybrid XLE, 35K miles, CPO. Dealer asking $31,500.</p>
<p><strong>Pricing target:</strong></p>
<ul><li>Market value (KBB, Edmunds, CarGurus for your ZIP): $28,500-29,500</li>
<li>Your negotiation target: $29,000 pre-tax</li>
<li>Out-the-door (with tax/fees in your state): ~$31,000</li></ul>
<p><strong>Dealer tactics to expect:</strong></p>
<ul><li><strong>"What monthly payment works for you?"</strong> Decline. Say "Let's talk out-the-door price first. I've already arranged financing."</li>
<li><strong>Extended warranty pitch ($2,000-3,000):</strong> Toyota reliability is strong — skip or buy separately from a third party for half the cost.</li>
<li><strong>GAP insurance at finance office:</strong> If you need it, your insurance company sells it for $20-40/year vs. $500-800 one-time at the dealer.</li></ul>
<p><strong>Walk-away signal:</strong> If they won't show you the Carfax or let you do a pre-purchase inspection at your mechanic, leave.</p>""",
        "tips": [
            "<strong>Email-first negotiation.</strong> Ask 'Write 3 dealers the same email asking for their best out-the-door price.'",
            "<strong>Time of month matters.</strong> Ask 'When in the month/quarter/year do dealers give the best deals?'",
            "<strong>Finance office prep.</strong> Ask 'What will they try to upsell in the F&I office and how do I politely decline each one?'",
            "<strong>Know the fees.</strong> Ask 'Which dealer fees are negotiable and which are government-mandated?'",
        ],
        "amazon_keywords": "car+buying+guide+book+negotiate",
        "amazon_text": "Car Buying Books",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-negotiation", "Negotiation")],
    },
    {
        "slug": "best-chatgpt-prompt-for-side-hustle-ideas",
        "title": "Best ChatGPT Prompt for Side Hustle Ideas",
        "subtitle": "Get realistic side hustle ideas based on your skills, time, and money goals — not the same recycled lists.",
        "prompt": """You are a business coach who has helped 500+ people start profitable side hustles. Help me find a side hustle.

About me:
- My skills: [LIST 5-7 THINGS YOU'RE GOOD AT]
- My current job: [WHAT YOU DO]
- Free time per week: [HOURS]
- Starting budget: $[AMOUNT]
- Money goal: $[PER MONTH]
- Timeline to first $: [WEEKS/MONTHS]
- Things I won't do: [e.g. no social media content, no sales calls, no physical products]
- Things I like: [e.g. solo work, writing, teaching, physical work]

Requirements:
- Give me 5 side hustle ideas that match my actual skills, not generic lists
- For each idea: how it works, how you'd get first customer, realistic income range at 6 months, startup cost, time to first $
- Rank them by fit for my situation
- Skip ideas that are saturated (driving for rideshare, generic freelance writing, POD t-shirts)
- Flag any that require skills I'd have to learn first — include a 'ramp-up time'
- For each idea, identify the single biggest reason it might fail
- Suggest 1 unconventional option I probably haven't thought about""",
        "how_to_use": [
            "Be honest about your skills — generic input gets generic ideas",
            "Include what you WON'T do — eliminating bad options is half the work",
            "Focus on one idea for 90 days before deciding it doesn't work",
            "Come back with: 'I tried [idea]. Here's what happened. What should I adjust or switch to?'",
        ],
        "example_output": """<p><strong>Profile:</strong> Works in marketing at a SaaS company, good at copy and analytics, 6 hrs/week, $500 budget, wants $1,000/mo in 6 months, won't do video content.</p>
<p><strong>Top ideas ranked by fit:</strong></p>
<ol>
<li><strong>Email newsletter copywriting for B2B SaaS founders ($2,000-5,000/mo at 6 months)</strong><br>Your exact skill. Outreach via LinkedIn to early-stage founders. 3-5 retainer clients at $500-1,500/mo.<br>Biggest failure risk: Not doing outreach consistently. This only works if you DM 10 founders/day for 60 days.</li>
<li><strong>Landing page audits (one-off $500-1,500 projects)</strong><br>Your analytics skill. Productized service. Audit their landing page, send a 1-page report + Loom.<br>Failure risk: Selling the first one. Start with free audits to friends' companies to build portfolio.</li>
<li><strong>LinkedIn ghostwriting for B2B executives ($1,500-4,000/mo)</strong><br>Interview them 30 min/week, write 3 posts. Copy skills transfer directly.<br>Failure risk: Finding your first client. Best paths: offering to write for your current exec as portfolio.</li>
</ol>
<p><strong>Unconventional option:</strong> Build a tiny SaaS tool that solves a single pain for marketers you work with. You have the customer empathy already.</p>""",
        "tips": [
            "<strong>Skill audit first.</strong> Ask 'List skills I have that people actually pay for — rank them by demand.'",
            "<strong>Validate before building.</strong> Ask 'How do I get 3 people to pay me before I build anything?'",
            "<strong>Copy existing success.</strong> Ask 'Show me people making money doing [idea] and how they got started.'",
            "<strong>Exit criteria.</strong> Ask 'How will I know at month 3 if this is working or if I should quit?'",
        ],
        "amazon_keywords": "side+hustle+book+passive+income",
        "amazon_text": "Side Hustle Books on Amazon",
        "related": [("best-chatgpt-prompt-for-writing-a-business-plan", "Writing a Business Plan"), ("best-chatgpt-prompt-for-budgeting", "Budgeting")],
    },
    {
        "slug": "best-chatgpt-prompt-for-performance-review",
        "title": "Best ChatGPT Prompt for Performance Review",
        "subtitle": "Write a self-review that captures your impact — or review your report with clear, actionable feedback.",
        "prompt": """You are a VP of HR who has reviewed thousands of performance reviews. Help me write one.

Type: [self-review / review for my direct report / peer review / 360 review]
My role: [YOUR TITLE]
Review period: [e.g. H1 2026, full year 2025]
Company's rating system: [1-5 / meets/exceeds / narrative only]
Goals set at start of period: [LIST 3-5]
Key accomplishments: [LIST WITH SPECIFIC IMPACT — numbers, outcomes]
Challenges or areas of growth: [HONEST LIST]
Feedback I've received during the period: [what peers/managers have said]

For self-reviews:
- Frame accomplishments in terms of business impact, not activities
- Use STAR method for top 3 wins
- Address growth areas honestly with concrete improvement plans
- Quantify everything possible
- Don't undersell OR oversell

For reviews of a direct report:
- Lead with specific examples of impact
- Give balanced feedback — what went well, what needs to grow
- Tie feedback to career trajectory, not just this review
- End with 2-3 development goals for next period
- Avoid vague words ('great team player,' 'works hard') — always be specific

Requirements:
- Every claim should have evidence
- Growth areas should have a plan attached, not just an identification
- Match the formality of my company's culture
- Keep it under 600 words""",
        "how_to_use": [
            "Write down specific wins BEFORE writing the review — you'll remember more on paper than in your head",
            "Every strength gets a concrete example. Every growth area gets a plan.",
            "For self-reviews, share a draft with a trusted peer before submitting — they'll catch under- and over-selling",
            "For direct reports, review your feedback for patterns across your team — same praise for everyone is a red flag",
        ],
        "example_output": """<p><strong>Self-review excerpt for a Senior PM:</strong></p>
<p><strong>Accomplishment 1: Launched Subscription 2.0</strong><br>
Led cross-functional team of 8 (engineering, design, data, marketing) to launch the new subscription flow on March 15. Result: trial-to-paid conversion rose from 12% to 19%, adding ~$2.1M in projected annual revenue. Key contributions: scoped the problem through 40 customer interviews, built the pricing model, drove launch decisions when stakeholders disagreed.</p>
<p><strong>Growth area: Delegation</strong><br>
I took on too many design decisions personally, creating a bottleneck in weeks 4-6 of the launch. Feedback from Alex confirmed the pattern. Plan for H2: identify one decision per project that I'll explicitly delegate, then resist re-making the call. Will review monthly with Alex.</p>""",
        "tips": [
            "<strong>Start with outcomes.</strong> Ask 'Rewrite this so every accomplishment leads with business impact, not activity.'",
            "<strong>Peer comparison.</strong> Ask 'How does this compare to what a strong senior [role] would write?'",
            "<strong>Growth area trap.</strong> Say 'Is my growth area specific and paired with a concrete plan, or is it vague?'",
            "<strong>Career conversation.</strong> Ask 'Write follow-up questions I should ask my manager about next-level growth after this review.'",
        ],
        "amazon_keywords": "management+performance+review+book",
        "amazon_text": "Management Books",
        "related": [("best-chatgpt-prompt-for-writing-a-resume", "Writing a Resume"), ("best-chatgpt-prompt-for-job-interview-prep", "Job Interview Prep")],
    },
    {
        "slug": "best-chatgpt-prompt-for-meditation-script",
        "title": "Best ChatGPT Prompt for Meditation Scripts",
        "subtitle": "Get custom guided meditation scripts for sleep, stress, focus, or any situation you're working through.",
        "prompt": """You are a meditation teacher trained in mindfulness, loving-kindness, and body scan traditions. Write a guided meditation script for me.

Purpose: [sleep / anxiety / focus / grief / pain / morning energy / stress relief / gratitude / difficult emotion]
Length: [5 / 10 / 15 / 20 minutes]
Style: [mindfulness / breath-focused / body scan / visualization / loving-kindness / counting / sound-based]
Experience level: [new to meditation / some practice / experienced]
Context: [e.g. for a hard week / right before a big presentation / can't sleep / dealing with anger]
Voice I'll read this in: [my own / recording for someone else]

Requirements:
- Use second person ('you') and present tense
- Include [PAUSE — 10 sec] markers for natural rests
- Start with 1-2 minutes of settling and arrival
- Build to the main practice
- End with a gentle transition back to the everyday
- Word the invitation as options, not commands ('you might notice...' not 'notice...')
- Keep language simple — no jargon, no mystical flourishes
- For sleep meditations, fade out rather than ending abruptly""",
        "how_to_use": [
            "Time your read — aim for 120-140 words per minute with pauses",
            "Record yourself if reading for others — a friendly voice beats a perfect one",
            "Read it yourself once before recording to catch anything awkward",
            "For sleep meditations, ask: 'Make the ending softer — no clear wake-up.'",
        ],
        "example_output": """<p><strong>10-min body scan for anxiety, for beginners:</strong></p>
<p>Start by finding a comfortable position, whatever feels right for your body. [PAUSE — 8 sec]</p>
<p>You can let your eyes close, or keep a soft gaze at the floor in front of you — whichever feels easier. [PAUSE — 5 sec]</p>
<p>Take a breath in through the nose, and let it out through the mouth with a little audible sigh. [PAUSE — 5 sec] You can do this two more times, if you'd like. [PAUSE — 15 sec]</p>
<p>Now let your breath return to its natural rhythm. You don't need to control it. [PAUSE — 10 sec]</p>
<p>Bring your attention to your feet — the soles, the toes, anywhere you might notice sensation. [PAUSE — 20 sec] There's nothing to find here. Just being with whatever is.</p>""",
        "tips": [
            "<strong>Shorter is often better.</strong> Ask 'Shorten this to 5 minutes without losing its core.'",
            "<strong>Match the need.</strong> Ask 'Rewrite this for panic vs. chronic low-grade anxiety — they need different approaches.'",
            "<strong>Voice options.</strong> Ask 'Rewrite for a softer, slower voice' if your default is energetic.'",
            "<strong>Bookend routines.</strong> Ask 'Give me a 3-minute morning version and a 3-minute evening version I can pair.'",
        ],
        "amazon_keywords": "meditation+mindfulness+book+guided",
        "amazon_text": "Meditation Books",
        "related": [("best-chatgpt-prompt-for-journaling", "Journaling"), ("best-chatgpt-prompt-for-goal-setting", "Goal Setting")],
    },
    {
        "slug": "best-chatgpt-prompt-for-home-improvement",
        "title": "Best ChatGPT Prompt for Home Improvement",
        "subtitle": "Plan DIY home projects, diagnose issues, and decide when to hire a pro — with step-by-step guidance.",
        "prompt": """You are a licensed contractor with 25 years of experience. Help me with a home improvement project.

What I need help with: [pick one]
- DIY project: how to do [PROJECT]
- Diagnose a problem: [DESCRIBE WHAT'S WRONG]
- Decide DIY vs. hire a pro: [PROJECT]
- Get a quote sanity check: [WHAT A CONTRACTOR QUOTED ME AND FOR WHAT]
- Material list for: [PROJECT]

Project details:
- Home type: [house / condo / apartment / rental]
- My DIY experience: [beginner / intermediate / advanced]
- My budget: $[AMOUNT]
- Tools I have: [basic / moderate / well-stocked]
- Time available: [weekend / week / longer]
- Location: [CITY, STATE for permits/codes]

For DIY projects, give me:
1. Whether this is actually DIY-appropriate for my skill level
2. Permits required (if any) in my area
3. A materials list with quantities
4. Tools needed — flag anything I'd have to buy/rent
5. Step-by-step instructions
6. The top 3 mistakes beginners make on this project
7. When to stop and call a pro
8. Estimated total cost if I DIY vs. hire

Requirements:
- Never recommend DIY on electrical past swapping fixtures, gas, roof peaks, or structural work — always call licensed pros
- If the risk of a mistake is catastrophic (water damage, electrocution, structural failure), say so clearly
- Include safety steps that beginners skip
- Ground advice in real codes and best practices""",
        "how_to_use": [
            "Be honest about your skill level — starting a project you can't finish costs more than hiring from day one",
            "Always check local permit requirements before starting — some 'minor' projects need them",
            "If your gut says 'I shouldn't do this,' trust it. Ask the AI for referrals on what to look for in a contractor instead",
            "For quotes, paste the scope and dollar amount and ask 'Is this fair for [city]?'",
        ],
        "example_output": """<p><strong>Project:</strong> Install a new bathroom vanity, beginner DIY.</p>
<p><strong>DIY verdict:</strong> Reasonable for a beginner IF plumbing connections stay in the same position. If you're moving plumbing, hire a plumber.</p>
<p><strong>Permits:</strong> Replacement (same location) typically doesn't require permits. Moving plumbing usually does.</p>
<p><strong>Materials list:</strong></p>
<ul><li>New vanity + top (measure TWICE before ordering)</li>
<li>New faucet (if not reusing) — size matches vanity hole count (1-hole or 3-hole)</li>
<li>Supply lines (braided stainless, 20")</li>
<li>P-trap kit if old one is in bad shape</li>
<li>Plumber's putty or silicone</li>
<li>Shims + wood screws (to level)</li></ul>
<p><strong>Top 3 beginner mistakes:</strong></p>
<ol><li>Not shutting off the water BEFORE disconnecting supply lines (flood).</li>
<li>Over-tightening plastic P-trap nuts (cracks the threads → slow leak).</li>
<li>Installing without leveling — every drawer will slam shut or not close at all.</li></ol>""",
        "tips": [
            "<strong>Always price the option of hiring.</strong> Ask 'What would it cost to hire this out?' Sometimes the math favors pros.",
            "<strong>Verify code.</strong> Ask 'What permits or inspections does [city] require for this project?'",
            "<strong>Two-person jobs.</strong> Say 'Which parts absolutely need a second person?' Safety matters.",
            "<strong>Red flag quotes.</strong> Paste contractor quote and ask 'Any red flags in this scope or price?'",
        ],
        "amazon_keywords": "home+improvement+book+DIY+guide",
        "amazon_text": "DIY Home Books on Amazon",
        "related": [("best-chatgpt-prompt-for-budgeting", "Budgeting"), ("best-chatgpt-prompt-for-gardening", "Gardening")],
    },
    {
        "slug": "best-chatgpt-prompt-for-movie-recommendations",
        "title": "Best ChatGPT Prompt for Movie Recommendations",
        "subtitle": "Get movie and TV show recommendations you'll actually like — based on your taste, mood, and what's available.",
        "prompt": """You are a film critic and personal taste curator. Recommend movies or shows for me.

What I'm in the mood for: [genre, feeling, specific vibe — e.g. 'something smart but not exhausting']
Movies/shows I've loved: [LIST 5-10 TITLES that represent your taste]
Things I usually dislike: [e.g. gore, slow pacing, musicals, romance as main plot]
Available platforms: [Netflix / Hulu / HBO / Prime / Apple / Disney+ / library DVD / etc.]
Solo or group: [solo / with partner / family with [AGES] kids / friends]
Length: [90-min movie / longer film / series]
When: [tonight / weekend binge / ongoing weekly watch]

Give me:
1. 5 specific recommendations with title, year, and where to watch
2. For each, one sentence explaining why I'll like it based on my taste
3. Rank them by confidence (which is the safest bet, which is the stretch pick)
4. Flag anything potentially triggering (violence, themes) so I know what I'm getting into
5. Include at least 2 films I probably haven't heard of
6. Skip anything overly discussed in mainstream culture right now — I want picks, not headlines

Requirements:
- Real titles only — never invent movies
- Match the mood, not just the genre
- Don't recommend the obvious ones (Shawshank, Godfather, Breaking Bad) unless explicitly asked
- Vary the decade and country — don't pile on US 2010s options""",
        "how_to_use": [
            "Give 5-10 specific titles you've loved — that's the signal the AI reads",
            "Be specific about mood — 'smart and emotional' is different from 'smart and cold'",
            "Verify availability — AI sometimes gets streaming services wrong; check before committing",
            "Come back with 'I watched [X]. Loved/hated because [Y]. Adjust recommendations.'",
        ],
        "example_output": """<p><strong>Request:</strong> Loved Past Lives, Whiplash, Lost in Translation. Don't like horror or slow-burn.</p>
<p><strong>Recommendations (ranked by confidence):</strong></p>
<ol>
<li><strong>Before Sunset (2004)</strong> — You're drawn to intimate, dialogue-driven films about longing. This is the gold standard. On Prime.</li>
<li><strong>The Worst Person in the World (2021)</strong> — Norwegian film about navigating your 20s and 30s. Past Lives DNA. On Hulu.</li>
<li><strong>Aftersun (2022)</strong> — Emotional but contained. Not slow — it builds quietly. On MUBI or rent.</li>
<li><strong>Once (2007)</strong> — Low-stakes but resonant, music-driven like Whiplash but gentler. On Prime.</li>
<li><strong>A Ghost Story (2017)</strong> — STRETCH PICK. Slower than what you said you want but might hit on feeling what Lost in Translation hit. Rent.</li>
</ol>""",
        "tips": [
            "<strong>Be specific about mood.</strong> Ask 'What's a Saturday-afternoon mood vs. a Sunday-evening mood?'",
            "<strong>International picks.</strong> Ask 'Give me 5 international films I'd love — outside US/UK.'",
            "<strong>Double features.</strong> Ask 'Pair 2 films I should watch back-to-back.' Often reveals tastes you didn't know you had.",
            "<strong>Build a watchlist.</strong> Ask 'Give me 20 films across moods so I have options for any night.'",
        ],
        "amazon_keywords": "movies+film+streaming+guide",
        "amazon_text": "Movie Books on Amazon",
        "related": [("best-chatgpt-prompt-for-book-summary", "Book Summaries"), ("best-chatgpt-prompt-for-gift-ideas", "Gift Ideas")],
    },
    {
        "slug": "best-chatgpt-prompt-for-book-recommendations",
        "title": "Best ChatGPT Prompt for Book Recommendations",
        "subtitle": "Get book recommendations that match your taste, current mood, and reading goals — not just bestseller lists.",
        "prompt": """You are a well-read librarian and literary critic. Recommend books for me.

What I'm in the mood for: [GENRE OR VIBE — e.g. 'nonfiction I won't hate,' 'smart sci-fi with female leads']
Books I've loved: [LIST 5-10 TITLES AND AUTHORS — this is the most important field]
Books I've tried and bounced off: [LIST ANY, with why]
What I want from reading right now: [escape / learn something / feel less alone / challenge my thinking / comfort]
Reading speed: [slow / medium / fast]
Length preference: [under 300 pages / 300-500 / long and deep]
Format: [physical / ebook / audio]

Give me:
1. 5 specific recommendations with title, author, year
2. One sentence each on why YOU (based on what I told you) will like it
3. Rank by confidence (safest bet → bold pick)
4. Include at least 2 I probably haven't heard of — not bestseller shelf picks
5. Vary format (not all novels, include memoir, essay, or nonfiction if my taste allows)
6. Flag content warnings if relevant (grief, violence, difficult material)

Requirements:
- Only recommend books that exist — never make up titles or authors
- Don't repeat books I said I've already loved
- Match mood AND taste, not just genre
- Don't default to the 'if you like X you'll like Y' cliches that dominate most lists""",
        "how_to_use": [
            "Give real titles from your shelf — not what you think sounds impressive",
            "Include books you hated — what you don't like is as useful as what you do",
            "Check your library before buying — most recommendations are available via libby.app",
            "After reading: 'I finished [X]. Rated it [Y] because [Z]. What's next?'",
        ],
        "example_output": """<p><strong>Taste profile:</strong> Loved <em>Station Eleven, The Overstory, A Little Life</em>. Mood: emotional but not devastating.</p>
<p><strong>Recommendations:</strong></p>
<ol>
<li><strong>The Remains of the Day (1989) by Kazuo Ishiguro</strong> — You're drawn to quiet emotional weight. Ishiguro does restraint perfectly.</li>
<li><strong>Sea of Tranquility (2022) by Emily St. John Mandel</strong> — Same author as Station Eleven, same understated beauty, different scope.</li>
<li><strong>Piranesi (2020) by Susanna Clarke</strong> — A smaller, stranger novel. Feels like a dream you remember a week later.</li>
<li><strong>Gilead (2004) by Marilynne Robinson</strong> — Deeply interior. If A Little Life drew you in with voice, Robinson's voice will hold you.</li>
<li><strong>STRETCH: The Left Hand of Darkness (1969) by Ursula K. Le Guin</strong> — Lit-fic dressed as sci-fi. Patient, wise, humane.</li>
</ol>""",
        "tips": [
            "<strong>Seasonal mood.</strong> Ask 'What should I read for [this season/life phase]?'",
            "<strong>Author deep-dives.</strong> Ask 'I loved [one book by X]. Which of their others should I read next?'",
            "<strong>Theme runs.</strong> Ask 'Build me a 5-book sequence on [theme] — read in this order for maximum impact.'",
            "<strong>Audiobook considerations.</strong> Ask 'Which of these is best in audio vs. print?'",
        ],
        "amazon_keywords": "bestselling+books",
        "amazon_text": "Books on Amazon",
        "related": [("best-chatgpt-prompt-for-book-summary", "Book Summaries"), ("best-chatgpt-prompt-for-movie-recommendations", "Movie Recommendations")],
    },
]

count = 0
for page in PAGES:
    make_page(**page)
    count += 1
    print(f"Created: {page['slug']}.html")

print(f"\nTotal pages created: {count}")
