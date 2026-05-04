# Buyer support email templates

Copy-paste-ready responses for the 7 most likely buyer support emails in the first 24–72 hours after launch. Each is 1–3 sentences. Voice matches `DELIVERY_EMAIL.md` — lowercase `hey,` opener, sentence case body, properly cased proper nouns, signed `— Flynn`.

Drop into your reply, edit the bracketed bits if any (most don't need editing), send. No subject line needed — your client will auto-prefix "Re: " on the buyer's original.

If a support question doesn't fit any template here, write a fresh reply in the same voice and add the new template below. The catalog grows from real buyer questions, not anticipated ones.

---

## 1. Refund request

```
hey,

Refund processed — Gumroad will reverse the charge within 24 hours and you'll get a confirmation email from them. No need to delete the files; consider them yours regardless. If anything in the bundle ended up useful even if it wasn't a fit overall, I'd love to hear what.

— Flynn
```

**Operational note**: process the refund in Gumroad → Sales → find the buyer → Refund. Do this BEFORE replying so the email lands after the refund hits. Buyer trust is in the speed of the action, not the apology.

---

## 2. "I can't find the Notion link"

```
hey,

Three places it should be: (1) your Gumroad library at gumroad.com/library — there's a .txt file in the bundle download with the URL, (2) the welcome email I sent right after you bought (search subject "Job Hunter's AI Bundle is here"), and (3) here it is directly: https://learned-guilty-545.notion.site/The-Job-Hunter-s-AI-Bundle-35634cf5abb9800babe5c22b28888ccf. Click "Duplicate" in the top-right when it loads to copy it into your own Notion.

— Flynn
```

**Operational note**: the inline URL is the live duplication-template URL from the wired-in workspace. If the URL ever changes (rare — only if the workspace is recreated), update this template to match. Source of truth: `DELIVERY_EMAIL.md` line 58.

---

## 3. "The PDF won't open"

```
hey,

Try (1) re-downloading from your Gumroad library at gumroad.com/library — sometimes the first download corrupts on slower connections, and (2) opening in a different reader — Apple Preview, Adobe Acrobat (free), or any browser will all render it. If both fail, reply with the error you're seeing and your device, and I'll dig in.

— Flynn
```

**Operational note**: 95% of PDF-won't-open issues are partial downloads. The two-step fix solves them without escalation. If a buyer escalates after both, ask for the exact error string + device + reader; almost always a font-render edge case (Adobe Reader on old Windows is the usual culprit).

---

## 4. "Does this work with Claude / Gemini / [model X]?"

```
hey,

Yes. The prompts were written and tested on ChatGPT (free tier — GPT-4o-mini and GPT-4o), but they run cleanly on Claude, Gemini, and any modern LLM with a 4K+ context window. The only model-specific thing is the bracketed input placeholders, which every assistant handles the same way.

— Flynn
```

**Operational note**: also covered in the Gumroad listing FAQ ("Works with Claude or Gemini?"). If a buyer asks anyway it's because they didn't read the listing — answer cleanly, don't snark about FAQ.

---

## 5. "I bought this for my friend / can I share?"

```
hey,

The license is per-buyer, not per-account — you're welcome to walk a friend through any specific prompt or share what you've learned, but the PDF and Notion access is meant for the person who paid. If you want to gift it cleanly, Gumroad has a gift-purchase option at checkout that delivers the same bundle to a recipient's email.

— Flynn
```

**Operational note**: don't enforce sharing technically (no DRM, no watermarks v1). The honor-system framing converts more buyers than it loses. If someone asks the question, they're respecting the boundary by asking — answer warmly.

---

## 6. "When is the day-5 comp prompt coming?"

```
hey,

That wasn't promised in the launch bundle — early drafts of the post-purchase email mentioned a follow-up prompt but the final cut dropped it to keep launch-week focus. A comp-triangulator prompt is in the v1.1 backlog, so it'll ship as a free update for buyers when it does. No action needed from you; I'll send a separate email when it's ready.

— Flynn
```

**Operational note**: this question only fires if a buyer saw an earlier draft of `DELIVERY_EMAIL.md` (e.g., from social-media leak, screenshot share, archive). The final delivery email doesn't promise it. Acknowledging the original mention without re-committing is the right move — don't pretend it never existed; don't re-promise.

---

## 7. "Will there be a v2?"

```
hey,

Yes — buyers get all future versions free via the same Gumroad library link. No committed timeline (I'd rather ship a real upgrade than hit a date), but the v1.1 backlog includes a comp-triangulator prompt, a quick-reference card, and a US Letter PDF variant. If there's a specific gap in v1 you'd want closed, hit reply and tell me what — that's what shapes the v1.1 priority list.

— Flynn
```

**Operational note**: this is the highest-leverage support reply — it converts a passive buyer into an active feedback source. Make a note of every reply that comes back; that's your v1.1 spec.

---

## Catalog grows from real questions

Add a new section here whenever you reply to something that doesn't fit any of the 7 above. The format:

```
## N. "[Buyer's question, condensed]"

```
hey,

[1–3 sentences. Voice matches DELIVERY_EMAIL.md.]

— Flynn
```

**Operational note**: [why this template exists, when to use, what to watch for]
```

Keep responses short. Don't ramble. Don't over-explain. The buyer wants a clear answer, not a mini-essay.
