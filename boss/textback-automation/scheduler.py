#!/usr/bin/env python3
"""Scheduler / runner for the Text-Back automation system.

This is the piece that drives `engine.tick()` on a cadence. It loads a persisted
JSON store, runs due actions, and saves atomically — so state survives restarts
(single-worker). It uses live Twilio/SMTP senders when their env vars are set,
otherwise the dry-run console adapter.

    # one pass then exit — put this in cron/launchd every ~15 min:
    python3 scheduler.py --once

    # long-running worker:
    python3 scheduler.py --loop --interval 900

    # add a lead from the command line (e.g. from a form handler):
    python3 scheduler.py --add --name "Dana Lee" --phone "(303) 555-0111" \
        --email dana@example.com --signal visited_pricing=1 --signal budget_confirmed=1

    # record an inbound reply (wire your SMS/email webhook to call this or the API):
    python3 scheduler.py --inbound "STOP" --phone "(303) 555-0111"

    # show current metrics:
    python3 scheduler.py --metrics

Cron example (every 15 minutes):
    */15 * * * * cd /path/to/textback-automation && /usr/bin/python3 scheduler.py --once >> ~/.textback/run.log 2>&1
"""
from __future__ import annotations

import argparse
import os
import time
from datetime import datetime

from textback import Engine, LeadStore
from textback.channels import default_senders

DEFAULT_STORE = os.environ.get("TEXTBACK_STORE", "~/.textback/store.json")


def build_engine(store_path: str) -> Engine:
    store = LeadStore.load_json(store_path)
    return Engine(store=store, senders=default_senders())


def _parse_signals(pairs: list[str]) -> dict:
    out: dict = {}
    for p in pairs or []:
        k, _, v = p.partition("=")
        v = v.strip()
        if v.lower() in {"1", "true", "yes"}:
            out[k] = True
        elif v.lower() in {"0", "false", "no"}:
            out[k] = False
        else:
            try:
                out[k] = float(v) if "." in v else int(v)
            except ValueError:
                out[k] = v
    return out


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--store", default=DEFAULT_STORE, help=f"store path (default {DEFAULT_STORE})")
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--once", action="store_true", help="run one tick then exit (for cron)")
    mode.add_argument("--loop", action="store_true", help="run forever")
    mode.add_argument("--add", action="store_true", help="intake a new lead")
    mode.add_argument("--inbound", metavar="TEXT", help="record an inbound reply")
    mode.add_argument("--metrics", action="store_true", help="print metrics and exit")
    ap.add_argument("--interval", type=int, default=900, help="--loop seconds between ticks")
    # --add / --inbound fields
    ap.add_argument("--name", default="")
    ap.add_argument("--phone", default="")
    ap.add_argument("--email", default="")
    ap.add_argument("--source", default="")
    ap.add_argument("--timezone", default="America/Denver")
    ap.add_argument("--signal", action="append", default=[], help="signal k=v (repeatable)")
    args = ap.parse_args(argv)

    eng = build_engine(args.store)

    if args.metrics:
        for k, v in eng.store.metrics().items():
            print(f"{k}: {v}")
        return 0

    if args.add:
        lead = eng.intake(args.name, phone=args.phone, email=args.email,
                          signals=_parse_signals(args.signal), source=args.source,
                          timezone=args.timezone, now=datetime.utcnow())
        eng.store.save_json(args.store)
        t = lead.temperature.value if lead.temperature else "-"
        print(f"added {lead.id} state={lead.state.value} temp={t} plan={lead.recommended_plan}")
        return 0

    if args.inbound is not None:
        lead = eng.handle_inbound(args.inbound, phone=args.phone, email=args.email,
                                  now=datetime.utcnow())
        eng.store.save_json(args.store)
        print(f"inbound -> {lead.id if lead else 'no match'}"
              + (f" state={lead.state.value}" if lead else ""))
        return 0

    if args.loop:
        print(f"[scheduler] loop every {args.interval}s, store={args.store}")
        while True:
            n = eng.tick(now=datetime.utcnow())
            eng.store.save_json(args.store)
            if n:
                print(f"[{datetime.utcnow().isoformat()}] sent {n}")
            time.sleep(args.interval)

    # default / --once
    n = eng.tick(now=datetime.utcnow())
    eng.store.save_json(args.store)
    print(f"[{datetime.utcnow().isoformat()}] tick complete, {n} sent; "
          f"{len(eng.store.active())} active leads")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
