#!/usr/bin/env python3
"""Runnable end-to-end demo of the Text-Back + Email automation system.

Simulates a batch of leads through their full lifecycle against the dry-run
console adapter (no credentials, no external calls), advancing a virtual clock so
the whole month happens in a fraction of a second. Prints the outbound messages,
the audit trail, and the final metrics.

    python3 run_demo.py
"""
from datetime import datetime, timedelta

from textback import Engine, LeadStore
from textback.channels import ConsoleSender
from textback.models import Channel

START = datetime(2026, 7, 1, 16, 0, 0)   # 10:00 America/Denver — inside allowed hours


def main() -> None:
    senders = {
        Channel.SMS: ConsoleSender(channel=Channel.SMS, echo=True),
        Channel.EMAIL: ConsoleSender(channel=Channel.EMAIL, echo=True),
    }
    eng = Engine(store=LeadStore(), senders=senders)

    print("=== INTAKE ===")
    hot = eng.intake("Dana Hot", phone="(303) 555-0111", email="dana@example.com",
                     signals=dict(requested_callback=True, visited_pricing=True,
                                  budget_confirmed=True, seats=25),
                     source="demo_request", now=START)
    warm = eng.intake("Will Warm", email="will@example.com",
                      signals=dict(visited_pricing=True, opened_email=True), now=START)
    cold = eng.intake("Cora Cold", phone="303-555-0133",
                      signals=dict(opened_email=False), now=START)
    dup = eng.intake("Dana Again", phone="303-555-0111", now=START)   # merges into `hot`
    bad = eng.intake("No Contact", phone="123", email="nope", now=START)

    for l in (hot, warm, cold):
        print(f"  {l.id} {l.name:12} {l.temperature.value:5} "
              f"plan={l.recommended_plan:10} trial={l.trial_offered}")
    print(f"  duplicate of {hot.name}: merged -> {dup.id} (same lead)")
    print(f"  invalid lead: {bad.id} state={bad.state.value}")

    print("\n=== RUN THE MONTH (virtual clock) ===")
    t = START
    for _ in range(24 * 20):        # hourly for 20 days
        if t == START + timedelta(hours=2):
            # Dana replies YES two hours in -> engages, automation pauses for a human.
            print(">> Dana replies 'YES please'")
            eng.handle_inbound("YES please", phone="303-555-0111", now=t)
        if t == START + timedelta(hours=30):
            # Cora texts STOP -> permanent opt-out.
            print(">> Cora replies 'STOP'")
            eng.handle_inbound("STOP", phone="303-555-0133", now=t)
        eng.tick(now=t)
        t += timedelta(hours=1)

    print("\n=== FINAL STATES ===")
    for l in eng.store.all():
        print(f"  {l.id} {l.name:12} {l.state.value:10} followups={l.followups_sent}")

    print("\n=== METRICS ===")
    for k, v in eng.store.metrics().items():
        print(f"  {k}: {v}")

    print("\n=== AUDIT (last 12 events) ===")
    for ev in eng.store.audit[-12:]:
        print(f"  {ev.at.isoformat()}  {ev.lead_id}  {ev.action:22} {ev.detail}")


if __name__ == "__main__":
    main()
