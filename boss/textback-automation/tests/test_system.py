"""End-to-end + edge-case tests for the Text-Back automation system.

Run:  python3 -m pytest tests/ -q       (or)   python3 tests/test_system.py
Deterministic: every test injects an explicit clock; leads use UTC so quiet-hour
math needs no timezone database.
"""
import os
import sys
import unittest
from datetime import datetime, timedelta

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from textback import Engine, LeadStore                       # noqa: E402
from textback import pipeline, channels                      # noqa: E402
from textback.channels import ConsoleSender, ScriptedSender  # noqa: E402
from textback.models import Channel, DeliveryStatus, State, Temperature  # noqa: E402
from textback.scheduling import RateLimiter                  # noqa: E402

# 18:00 UTC is daytime in UTC *and* in America/Denver (12:00), so default-tz
# leads send immediately regardless of whether a tz database is installed.
DAY = datetime(2026, 7, 15, 18, 0, 0)
NIGHT = datetime(2026, 7, 15, 3, 0, 0)  # 03:00 UTC -> quiet hours (used with tz=UTC)


def fresh(**kw):
    senders = {Channel.SMS: ConsoleSender(channel=Channel.SMS),
               Channel.EMAIL: ConsoleSender(channel=Channel.EMAIL)}
    return Engine(store=LeadStore(), senders=senders, **kw)


HOT = dict(requested_callback=True, visited_pricing=True, budget_confirmed=True)
COLD = dict(opened_email=False)


class Validation(unittest.TestCase):
    def test_phone_normalization(self):
        self.assertEqual(pipeline.normalize_phone("(303) 555-0142"), "+13035550142")
        self.assertEqual(pipeline.normalize_phone("303-555-0142"), "+13035550142")
        self.assertEqual(pipeline.normalize_phone("+44 20 7946 0958"), "+442079460958")
        self.assertEqual(pipeline.normalize_phone("12345"), "")

    def test_email_normalization(self):
        self.assertEqual(pipeline.normalize_email("  Bob@Example.COM "), "bob@example.com")
        self.assertEqual(pipeline.normalize_email("not-an-email"), "")

    def test_invalid_lead_goes_invalid(self):
        e = fresh()
        lead = e.intake("No Contact", phone="123", email="bad", now=DAY)
        self.assertEqual(lead.state, State.INVALID)


class Classification(unittest.TestCase):
    def test_hot_warm_cold(self):
        self.assertEqual(pipeline.classify(HOT), Temperature.HOT)
        self.assertEqual(pipeline.classify(dict(visited_pricing=True, opened_email=True)), Temperature.WARM)
        self.assertEqual(pipeline.classify(COLD), Temperature.COLD)

    def test_plan_and_trial(self):
        self.assertEqual(pipeline.recommend_plan(Temperature.HOT, {}), "Pro")
        self.assertEqual(pipeline.recommend_plan(Temperature.COLD, {}), "Starter")
        self.assertEqual(pipeline.recommend_plan(Temperature.WARM, dict(budget_confirmed=True, seats=30)), "Enterprise")
        self.assertTrue(pipeline.offer_trial(Temperature.HOT))
        self.assertFalse(pipeline.offer_trial(Temperature.COLD))


class Dedup(unittest.TestCase):
    def test_duplicate_lead_merges(self):
        e = fresh()
        a = e.intake("Ann", phone="303-555-0142", signals={"visited_pricing": True}, now=DAY)
        b = e.intake("Ann Again", phone="(303) 555-0142", signals={"budget_confirmed": True}, now=DAY)
        self.assertEqual(a.id, b.id)                       # same lead, not a new one
        self.assertEqual(len(e.store.all()), 1)
        self.assertTrue(a.signals.get("budget_confirmed"))  # signals merged

    def test_duplicate_message_suppressed(self):
        # Force the same body twice by resetting the pointer; the content dedup
        # key must suppress the second identical send.
        e = fresh()
        lead = e.intake("Ann", phone="303-555-0142", signals=HOT, now=DAY)
        e.tick(now=DAY)                                   # sends hot_1 (SMS)
        sent1 = [m for m in e.store.messages if m.status == DeliveryStatus.SENT]
        lead.followups_sent = 0                           # simulate a re-trigger of step 0
        lead.state = State.CLASSIFIED
        lead.next_action_at = DAY
        e.tick(now=DAY)
        suppressed = [m for m in e.store.messages if m.status == DeliveryStatus.SUPPRESSED]
        self.assertEqual(len(sent1), 1)
        self.assertTrue(any(m.suppressed_reason == "duplicate message" for m in suppressed))


class Lifecycle(unittest.TestCase):
    def test_hot_full_sequence_then_dead(self):
        e = fresh()
        lead = e.intake("Hank Hot", phone="303-555-0142", email="hank@x.com", signals=HOT, now=DAY)
        self.assertEqual(lead.temperature, Temperature.HOT)
        self.assertEqual(lead.state, State.CLASSIFIED)

        e.tick(now=DAY)                                   # hot_1 SMS
        self.assertEqual(lead.state, State.CONTACTED)
        self.assertEqual(lead.followups_sent, 1)

        t = DAY + timedelta(hours=1)
        e.tick(now=t)                                     # hot_2 email
        self.assertEqual(lead.followups_sent, 2)
        self.assertEqual(lead.state, State.FOLLOW_UP)

        t = t + timedelta(hours=24)
        e.tick(now=t)                                     # hot_3 SMS (final)
        self.assertEqual(lead.followups_sent, 3)

        t = t + timedelta(hours=100)                      # past grace window
        e.tick(now=t)
        self.assertEqual(lead.state, State.DEAD)

        # Three distinct channels/steps actually delivered.
        sent = [m for m in e.store.messages if m.status == DeliveryStatus.SENT]
        self.assertEqual(len(sent), 3)

    def test_email_only_lead_reroutes_sms_steps_to_email(self):
        e = fresh()
        lead = e.intake("Eve Email", email="eve@x.com", signals=HOT, now=DAY)
        e.tick(now=DAY)                                   # hot_1 is SMS -> no phone -> reroute to email
        self.assertEqual(lead.followups_sent, 1)
        self.assertTrue(any(a.action == "rerouted" for a in e.store.audit))
        e.tick(now=DAY + timedelta(hours=1))              # hot_2 email -> sent natively
        sent = [m for m in e.store.messages if m.status == DeliveryStatus.SENT]
        self.assertTrue(sent and all(m.channel == Channel.EMAIL for m in sent))
        self.assertFalse(any(m.status == DeliveryStatus.SUPPRESSED for m in e.store.messages))


class StopAndReply(unittest.TestCase):
    def test_stop_keyword_opts_out_permanently(self):
        e = fresh()
        lead = e.intake("Sam Stop", phone="303-555-0142", signals=HOT, now=DAY)
        e.tick(now=DAY)
        e.handle_inbound("STOP", phone="303-555-0142", now=DAY)
        self.assertEqual(lead.state, State.STOPPED)
        before = len(e.store.messages)
        for h in range(0, 300, 6):                        # keep ticking; must never message again
            e.tick(now=DAY + timedelta(hours=h))
        self.assertEqual(len(e.store.messages), before)

    def test_positive_reply_engages_and_pauses(self):
        e = fresh()
        lead = e.intake("Paula Positive", phone="303-555-0142", signals=HOT, now=DAY)
        e.tick(now=DAY)
        e.handle_inbound("YES please", phone="303-555-0142", now=DAY)
        self.assertEqual(lead.state, State.ENGAGED)
        self.assertIsNone(lead.next_action_at)
        before = len(e.store.messages)
        e.tick(now=DAY + timedelta(hours=48))             # engaged leads are human-owned
        self.assertEqual(len(e.store.messages), before)


class HumanOverride(unittest.TestCase):
    def test_hold_and_resume(self):
        e = fresh()
        lead = e.intake("Holly Hold", phone="303-555-0142", signals=HOT, now=DAY)
        e.tick(now=DAY)
        e.hold(lead.id, now=DAY)
        self.assertEqual(lead.state, State.HUMAN_HOLD)
        before = len(e.store.messages)
        e.tick(now=DAY + timedelta(hours=48))
        self.assertEqual(len(e.store.messages), before)   # paused
        e.resume(lead.id, now=DAY + timedelta(hours=48))
        e.tick(now=DAY + timedelta(hours=48))
        self.assertGreater(len(e.store.messages), before) # flows again

    def test_convert_is_terminal(self):
        e = fresh()
        lead = e.intake("Cara Convert", phone="303-555-0142", signals=HOT, now=DAY)
        e.convert(lead.id, now=DAY)
        self.assertEqual(lead.state, State.CONVERTED)
        e.tick(now=DAY + timedelta(hours=48))
        self.assertEqual(lead.state, State.CONVERTED)


class QuietHoursAndRate(unittest.TestCase):
    def test_quiet_hours_defer(self):
        e = fresh()
        lead = e.intake("Nina Night", phone="303-555-0142", signals=HOT,
                        timezone="UTC", now=NIGHT)
        # Created at 03:00 -> first action is deferred to 08:00, not sent overnight.
        self.assertEqual(lead.next_action_at.hour, 8)
        e.tick(now=NIGHT)                                 # still quiet & not due
        self.assertEqual(lead.followups_sent, 0)
        e.tick(now=datetime(2026, 7, 15, 8, 0, 0))        # morning -> sends
        self.assertEqual(lead.followups_sent, 1)

    def test_rate_limit_defers(self):
        rl = RateLimiter(per_channel_limit=1, window=timedelta(hours=1))
        e = Engine(store=LeadStore(),
                   senders={Channel.SMS: ConsoleSender(channel=Channel.SMS),
                            Channel.EMAIL: ConsoleSender(channel=Channel.EMAIL)},
                   rate_limiter=rl)
        a = e.intake("A", phone="303-555-0101", signals=HOT, timezone="UTC", now=DAY)
        b = e.intake("B", phone="303-555-0102", signals=HOT, timezone="UTC", now=DAY)
        e.tick(now=DAY)                                   # one SMS allowed, the other deferred
        sent = [m for m in e.store.messages if m.status == DeliveryStatus.SENT]
        self.assertEqual(len(sent), 1)
        self.assertTrue(any(x.action == "deferred_rate_limit" for x in e.store.audit))


class Retries(unittest.TestCase):
    def test_retry_then_success(self):
        sms = ScriptedSender(channel=Channel.SMS, fail_times=2)
        e = Engine(store=LeadStore(),
                   senders={Channel.SMS: sms, Channel.EMAIL: ConsoleSender(channel=Channel.EMAIL)})
        lead = e.intake("Rita Retry", phone="303-555-0142", signals=HOT, timezone="UTC", now=DAY)
        t = DAY                                           # 18:00; retry backoff is 1h
        for _ in range(3):                                # 18,19,20h -> fail, fail, succeed
            e.tick(now=t)
            t = t + timedelta(hours=1)
        self.assertEqual(lead.followups_sent, 1)          # step 0 committed after retry success
        self.assertEqual(sms.calls, 3)                    # 2 failures + 1 success
        self.assertTrue(any(m.status == DeliveryStatus.SENT and m.channel == Channel.SMS
                            for m in e.store.messages))

    def test_retry_giveup_does_not_loop_forever(self):
        sms = ScriptedSender(channel=Channel.SMS, fail_times=999)
        e = Engine(store=LeadStore(),
                   senders={Channel.SMS: sms, Channel.EMAIL: ConsoleSender(channel=Channel.EMAIL)})
        lead = e.intake("Fred Fail", phone="303-555-0142", signals=HOT, timezone="UTC", now=DAY)
        t = DAY
        for _ in range(300):                              # hourly for ~12 days: covers all
            e.tick(now=t)                                 # steps + 24h gaps + 72h grace
            t = t + timedelta(hours=1)
        # It must not be wedged on step 0 forever; it should have moved on and ended.
        self.assertGreaterEqual(lead.followups_sent, 1)
        self.assertEqual(lead.state, State.DEAD)
        failed = [m for m in e.store.messages if m.status == DeliveryStatus.FAILED]
        # This lead is phone-only, so all three HOT steps land on SMS (hot_2's email
        # step reroutes to SMS) and each fails exactly MAX_STEP_RETRIES: 3 x 3 = 9.
        self.assertEqual(len(failed), 9)
        self.assertEqual(sum(1 for m in failed if m.step == "hot_1"), 3)


class ChannelFallback(unittest.TestCase):
    def test_cold_phone_only_lead_gets_sms_reroute(self):
        # COLD sequence is email-only; a phone-only cold lead must still be
        # contacted (rerouted to SMS) rather than silently dying.
        e = fresh()
        lead = e.intake("Cid Cold", phone="303-555-0142", signals=COLD,
                        timezone="UTC", now=DAY)
        self.assertEqual(lead.temperature, Temperature.COLD)
        e.tick(now=DAY)
        sent = [m for m in e.store.messages if m.status == DeliveryStatus.SENT]
        self.assertEqual(len(sent), 1)
        self.assertEqual(sent[0].channel, Channel.SMS)        # rerouted from email
        self.assertNotIn("\n", sent[0].body)                  # subject line stripped
        self.assertTrue(any(a.action == "rerouted" for a in e.store.audit))

    def test_no_channel_at_all_suppresses(self):
        # A lead with neither channel can't exist (validation blocks it), but if a
        # lead somehow loses both, the step suppresses rather than crashing.
        e = fresh()
        lead = e.intake("Cid", phone="303-555-0142", signals=COLD, timezone="UTC", now=DAY)
        lead.phone = ""; lead.email = ""
        e.tick(now=DAY)
        self.assertTrue(any(m.status == DeliveryStatus.SUPPRESSED for m in e.store.messages))


class Persistence(unittest.TestCase):
    def test_save_load_roundtrip_survives_restart(self):
        import tempfile, os as _os
        e = fresh()
        h = e.intake("Ren", phone="303-555-0101", signals=HOT, timezone="UTC", now=DAY)
        e.tick(now=DAY)
        path = _os.path.join(tempfile.mkdtemp(), "store.json")
        e.store.save_json(path)

        # Simulate a process restart: brand-new store loaded from disk.
        store2 = LeadStore.load_json(path)
        self.assertEqual(len(store2.all()), 1)
        r = store2.get(h.id)
        self.assertEqual(r.state, State.CONTACTED)
        self.assertEqual(r.temperature, Temperature.HOT)
        self.assertEqual(r.followups_sent, 1)
        self.assertIsInstance(r.next_action_at, datetime)
        # dedup memory persists too, so the same message isn't re-sent post-restart.
        sent_key = next(m.dedup_key for m in e.store.messages if m.status == DeliveryStatus.SENT)
        self.assertTrue(store2.already_sent(sent_key))

    def test_dedup_index_rebuilt_on_load(self):
        import tempfile, os as _os
        e = fresh()
        a = e.intake("Ann", phone="303-555-0142", now=DAY)
        path = _os.path.join(tempfile.mkdtemp(), "s.json")
        e.store.save_json(path)
        store2 = LeadStore.load_json(path)
        self.assertIs(store2.find_by_contact("+13035550142", ""), store2.get(a.id))


class Determinism(unittest.TestCase):
    def test_metrics_and_no_leftover_actionable(self):
        e = fresh()
        e.intake("H", phone="303-555-0101", signals=HOT, timezone="UTC", now=DAY)
        e.intake("C", email="c@x.com", signals=COLD, timezone="UTC", now=DAY)
        t = DAY
        for _ in range(200):                              # run the world forward a long way
            e.tick(now=t)
            t = t + timedelta(hours=6)
        m = e.store.metrics()
        self.assertEqual(m["leads_total"], 2)
        # everyone reaches a terminal state; nothing left mid-flight
        self.assertTrue(all(l.is_terminal() or l.state in {State.ENGAGED, State.HUMAN_HOLD}
                            for l in e.store.all()))
        self.assertTrue(len(e.store.audit) > 0)


if __name__ == "__main__":
    unittest.main(verbosity=2)
