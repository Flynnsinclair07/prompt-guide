# Text-Back + Email Automation System

A lead-follow-up engine: leads enter, get validated and classified (HOT/WARM/COLD),
receive a coordinated SMS + email follow-up sequence, and progress through a state
machine with proper stop conditions, dedup, rate limiting, quiet hours, human
override, and an audit trail.

**Runs with zero credentials** out of the box — a dry-run console adapter records
what *would* be sent, so the whole system is demoable and fully testable offline.
Twilio (SMS) and SMTP (email) plug in via env vars when you go live.

```bash
python3 run_demo.py            # full lifecycle against the dry-run adapter
python3 tests/test_system.py   # 18 tests, no dependencies
```

## Lead state machine

```
NEW ──validate──► INVALID (terminal: no valid phone/email)
      │
      └─valid──► VALIDATED ──classify──► CLASSIFIED ──1st send──► CONTACTED
                                                                     │
                                                        (time passes, no reply)
                                                                     ▼
                                                                  FOLLOW_UP ──seq exhausted──► DEAD
      any inbound reply ─────────────────────────────────────────► ENGAGED  (automation pauses; human owns it)
      "STOP" / unsubscribe ──────────────────────────────────────► STOPPED  (terminal, do-not-contact)
      human hold ────────────────────────────────────────────────► HUMAN_HOLD (paused) ──resume──► FOLLOW_UP
      human convert ─────────────────────────────────────────────► CONVERTED (terminal)
```

Terminal states (`INVALID`, `STOPPED`, `CONVERTED`, `DEAD`) never transition again.
The engine only sends for `CLASSIFIED / CONTACTED / FOLLOW_UP` — `ENGAGED` and
`HUMAN_HOLD` are human-owned and never receive automated messages.

## What's implemented

| Concern | How |
|---|---|
| **Validation** | phone → E.164, email normalized; a lead needs ≥1 valid channel or it's `INVALID` |
| **Classification** | HOT/WARM/COLD from intent signals (callback request, pricing visit, budget, form completeness, source…) |
| **Plan recommendation** | Starter / Pro / Enterprise from temperature + seats + budget |
| **Trial** | offered to HOT/WARM (COLD is nurtured first) |
| **Sequences** | per-temperature cadence; **one channel per step** (see below) |
| **Dedup — leads** | same phone/email re-submitted merges into the existing lead |
| **Dedup — messages** | identical lead+channel+body is suppressed, never re-sent |
| **Rate limiting** | global per-channel cap per rolling window + a per-lead min-gap safety floor |
| **Quiet hours** | no sends outside 08:00–21:00 in the lead's timezone; deferred to the next window |
| **Stop conditions** | STOP keyword, sequence exhaustion → DEAD, conversion, human hold |
| **Retries** | failed sends retry with backoff up to a cap, then skip the step (never loops forever) |
| **Human override** | `hold` / `resume` / `convert` / `stop` |
| **Audit + metrics** | every action is logged with a timestamp; `store.metrics()` summarizes states/sends/opt-outs |

### Why one channel per step

Each sequence step sends on exactly one channel (SMS *or* email), never both at
once. This removes the "SMS sent but email failed" partial-delivery ambiguity and
the double-touch it invites — coordination lives in the sequence, not in a
simultaneous dual send. Every send is also guarded by a content dedup key and a
committed-step marker, so a re-entrant or concurrent tick cannot double-send.

## Usage

```python
from datetime import datetime
from textback import Engine

eng = Engine()   # dry-run console adapters by default

lead = eng.intake(
    "Dana Lee", phone="(303) 555-0111", email="dana@example.com",
    signals=dict(requested_callback=True, visited_pricing=True, budget_confirmed=True, seats=25),
    source="demo_request", timezone="America/Denver",
)
# lead.temperature == HOT, lead.recommended_plan == "Enterprise", trial offered

eng.tick(now=datetime.utcnow())                       # send anything due
eng.handle_inbound("YES", phone="(303) 555-0111")     # reply -> ENGAGED (human takes over)
eng.hold(lead.id); eng.resume(lead.id)                # human override
print(eng.store.metrics())
```

Run `tick()` on a schedule (cron / launchd / a worker loop) — it's idempotent and
only acts on what's due.

## Scheduler (included)

`scheduler.py` drives `tick()` on a cadence with a **persisted JSON store** (atomic
writes, survives restarts for a single worker) and picks live Twilio/SMTP senders
automatically when configured:

```bash
python3 scheduler.py --once                 # one pass then exit (put in cron)
python3 scheduler.py --loop --interval 900  # long-running worker
python3 scheduler.py --add --name "Dana Lee" --phone "(303) 555-0111" \
    --email dana@example.com --signal visited_pricing=1 --signal budget_confirmed=1
python3 scheduler.py --inbound "STOP" --phone "(303) 555-0111"   # wire to your SMS webhook
python3 scheduler.py --metrics
```

Cron, every 15 minutes:
```
*/15 * * * * cd /path/to/textback-automation && /usr/bin/python3 scheduler.py --once >> ~/.textback/run.log 2>&1
```
Store location defaults to `~/.textback/store.json` (override with `--store` or `TEXTBACK_STORE`).

## Going live (swap the adapters)

The engine picks live providers automatically when their env vars are set, else
falls back to the console adapter:

```python
from textback import Engine, LeadStore
from textback.channels import default_senders
eng = Engine(store=LeadStore(), senders=default_senders())
```

- **SMS (Twilio):** set `TWILIO_ACCOUNT_SID`, `TWILIO_AUTH_TOKEN`, `TWILIO_FROM_NUMBER` and `pip install twilio`.
- **Email (SMTP):** set `SMTP_HOST`, `SMTP_USER`, `SMTP_PASSWORD`, `SMTP_FROM` (and optional `SMTP_PORT`). No package needed.

A misconfigured provider **never crashes the run** — it falls back to console so
the pipeline keeps moving and the gap is visible in the audit log.

## Known limitations (be honest)

- **Single-channel leads are rerouted, not lost.** If a step's native channel is
  missing (e.g. the email-only COLD sequence for a phone-only lead), the message
  reroutes to the channel the lead *does* have (email→SMS drops the subject line;
  SMS→email adds one). A lead with neither channel can't pass validation. So no
  contactable lead is silently skipped anymore.
- **Persistence is a single-worker JSON file** (atomic writes, survives restarts).
  Fine for one `scheduler.py` process; for *multiple concurrent* workers, back it
  with a real datastore — the dedup keys + committed-step marker already give you
  the idempotency to do so safely.
- **Inbound still needs wiring.** `scheduler.py --inbound` and `handle_inbound()`
  do the STOP/positive/other parsing; point your Twilio SMS webhook + email reply
  handler at them. This matters legally for opt-outs.
- **Message copy is placeholder.** Replace the templates in `pipeline.py` with your
  real brand voice before going live.

## Layout

```
textback/
  models.py       # states, enums, Lead, MessageRecord
  pipeline.py     # validation, classification, plan rec, sequences, inbound parsing
  scheduling.py   # quiet hours + rate limiter
  channels.py     # Sender interface + Console (default) / Twilio / SMTP / Scripted
  store.py        # lead store, dedup index, audit log, metrics, JSON persistence
  engine.py       # the state machine + orchestration
scheduler.py      # cron/worker runner with persisted store + live-provider selection
run_demo.py       # runnable end-to-end demo
tests/test_system.py
```

## Tests

```bash
python3 tests/test_system.py     # unittest, 18 tests
# or: python3 -m pytest tests/ -q
```

Covers validation, classification, plan/trial, lead + message dedup, the full
HOT lifecycle to DEAD, email-only channel skipping, STOP opt-out, positive-reply
engagement, human hold/resume/convert, quiet-hours deferral, rate-limit deferral,
retry-then-success, retry-giveup (no infinite loop), and metrics/termination.
