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

- **COLD sequence is email-only.** A COLD lead with *only* a phone number gets
  every step suppressed and ends `DEAD` without outreach (the suppressions are
  logged and counted, not silent). Mitigation: capture an email for cold leads, or
  add SMS steps to the cold sequence in `pipeline.py`.
- **Store is in-memory** (with JSON export). Fine for a single worker; for
  multi-process concurrency you'd back it with a real datastore and rely on the
  existing dedup keys / committed-step marker for idempotency.
- **Inbound is a function call.** Wire `handle_inbound()` to your Twilio SMS
  webhook and email reply handler; the parsing (STOP / positive / other) is done.
- **No hosting/scheduler included.** You drive `tick()` from your own cron/worker.

## Layout

```
textback/
  models.py       # states, enums, Lead, MessageRecord
  pipeline.py     # validation, classification, plan rec, sequences, inbound parsing
  scheduling.py   # quiet hours + rate limiter
  channels.py     # Sender interface + Console (default) / Twilio / SMTP / Scripted
  store.py        # lead store, dedup index, audit log, metrics
  engine.py       # the state machine + orchestration
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
