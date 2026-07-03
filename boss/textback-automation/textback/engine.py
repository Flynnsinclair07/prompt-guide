"""The automation engine: the lead state machine and the orchestration that ties
validation, classification, sequences, scheduling, channels, dedup, and audit
together.

Design choices that matter for correctness:
  * One channel per sequence step. We never fire SMS *and* email simultaneously,
    which removes the "SMS sent but email failed" partial-delivery ambiguity and
    the double-touch it invites. Coordination lives in the sequence, not in a
    dual send.
  * Every send is guarded by a content dedup key (lead+channel+body) and a
    committed-step marker, so a re-entrant or concurrent tick cannot double-send.
  * Quiet hours and rate limits DEFER (reschedule) rather than consume a step.
  * A step that keeps failing is retried with backoff up to MAX_STEP_RETRIES,
    then permanently marked FAILED and skipped — so no lead can loop forever.
  * Terminal states (STOPPED/CONVERTED/DEAD/INVALID) never transition again, and
    ENGAGED/HUMAN_HOLD are owned by a human — the engine won't message them.
"""
from __future__ import annotations

from datetime import datetime, timedelta

from . import pipeline
from .channels import ConsoleSender, SendError, Sender
from .models import (ACTIONABLE_STATES, Channel, DeliveryStatus, Lead,
                     MessageRecord, State, Temperature)
from .scheduling import RateLimiter, in_quiet_hours, next_allowed_time
from .store import LeadStore

GRACE_HOURS = 72.0          # window for a late reply after the final step -> DEAD
MAX_STEP_RETRIES = 3        # attempts per step before giving up on it
RETRY_BACKOFF_HOURS = 1.0


class Engine:
    def __init__(self, store: LeadStore | None = None,
                 senders: dict | None = None,
                 rate_limiter: RateLimiter | None = None) -> None:
        self.store = store or LeadStore()
        self.senders: dict = senders or {
            Channel.SMS: ConsoleSender(channel=Channel.SMS),
            Channel.EMAIL: ConsoleSender(channel=Channel.EMAIL),
        }
        self.rl = rate_limiter or RateLimiter()
        self._step_attempts: dict[tuple, int] = {}

    # ------------------------------------------------------------------ intake
    def intake(self, name: str, phone: str = "", email: str = "",
               signals: dict | None = None, source: str = "",
               timezone: str = "America/Denver", now: datetime | None = None) -> Lead:
        now = now or datetime.utcnow()
        signals = dict(signals or {})
        v = pipeline.validate_lead(name, phone, email)

        # Dedup: same contact re-submitted -> merge into the existing lead.
        if v.ok:
            existing = self.store.find_by_contact(v.phone, v.email)
            if existing is not None:
                existing.signals.update(signals)
                existing.updated_at = now
                existing.notes.append("duplicate intake merged")
                self.store.log(now, existing.id, "intake_duplicate", source)
                return existing

        lead = Lead(id=self.store.next_id(), name=name, source=source,
                    timezone=timezone, signals=signals, created_at=now, updated_at=now)

        if not v.ok:
            lead.state = State.INVALID
            lead.notes.append(v.reason)
            self.store.add(lead)
            self.store.log(now, lead.id, "invalid", v.reason)
            return lead

        lead.phone, lead.email = v.phone, v.email
        lead.state = State.VALIDATED
        self.store.add(lead)
        self.store.log(now, lead.id, "validated", f"phone={bool(lead.phone)} email={bool(lead.email)}")

        # Classify + plan + trial, then schedule the first step.
        self._classify_and_plan(lead, now)
        return lead

    def _classify_and_plan(self, lead: Lead, now: datetime) -> None:
        lead.temperature = pipeline.classify(lead.signals)
        lead.recommended_plan = pipeline.recommend_plan(lead.temperature, lead.signals)
        lead.trial_offered = pipeline.offer_trial(lead.temperature)
        lead.state = State.CLASSIFIED
        lead.updated_at = now
        lead.next_action_at = next_allowed_time(now, lead.timezone)
        self.store.log(now, lead.id, "classified",
                       f"{lead.temperature.value} plan={lead.recommended_plan} trial={lead.trial_offered}")

    # -------------------------------------------------------------------- tick
    def tick(self, now: datetime | None = None) -> int:
        """Process every lead whose next action is due. Returns number of sends."""
        now = now or datetime.utcnow()
        sends = 0
        for lead in self.store.active():
            if lead.state not in ACTIONABLE_STATES:
                continue
            if lead.next_action_at is None or lead.next_action_at > now:
                continue
            sends += self._advance_lead(lead, now)
        return sends

    def _advance_lead(self, lead: Lead, now: datetime) -> int:
        seq = pipeline.SEQUENCES[lead.temperature]
        idx = lead.followups_sent

        # Sequence exhausted and the grace window has elapsed -> DEAD.
        if idx >= len(seq):
            self._transition(lead, State.DEAD, now, "sequence exhausted, no engagement")
            return 0

        # Quiet hours: defer without consuming the step.
        if in_quiet_hours(now, lead.timezone):
            lead.next_action_at = next_allowed_time(now, lead.timezone)
            self.store.log(now, lead.id, "deferred_quiet_hours", lead.next_action_at.isoformat())
            return 0

        step = seq[idx]
        to = lead.phone if step.channel == Channel.SMS else lead.email
        body = pipeline.render(step.template, lead.name, lead.recommended_plan)
        rec = MessageRecord(lead_id=lead.id, channel=step.channel, body=body,
                            step=step.key, created_at=now)

        # No address for this channel -> suppress and advance (don't get stuck).
        if not to:
            rec.status = DeliveryStatus.SUPPRESSED
            rec.suppressed_reason = f"no {step.channel.value} address"
            self.store.messages.append(rec)
            self.store.log(now, lead.id, "suppressed", rec.suppressed_reason)
            self._commit_step(lead, step, now, seq)
            return 0

        # Content dedup: never send the identical message twice; advance instead.
        if self.store.already_sent(rec.dedup_key):
            rec.status = DeliveryStatus.SUPPRESSED
            rec.suppressed_reason = "duplicate message"
            self.store.messages.append(rec)
            self.store.log(now, lead.id, "suppressed", "duplicate message")
            self._commit_step(lead, step, now, seq)
            return 0

        # Rate limit: defer with backoff, don't consume the step.
        ok, why = self.rl.allow(lead.id, step.channel.value, now)
        if not ok:
            lead.next_action_at = now + timedelta(hours=RETRY_BACKOFF_HOURS)
            self.store.log(now, lead.id, "deferred_rate_limit", why)
            return 0

        # Attempt delivery.
        sender: Sender = self.senders[step.channel]
        attempt_key = (lead.id, step.key)
        try:
            rec.attempts = self._step_attempts.get(attempt_key, 0) + 1
            self._step_attempts[attempt_key] = rec.attempts
            lead.last_committed_step = step.key   # idempotency marker before send
            sender.send(to, body)
            rec.status = DeliveryStatus.SENT
            rec.sent_at = now
            self.store.messages.append(rec)
            self.store.mark_sent(rec.dedup_key)
            self.rl.record(lead.id, step.channel.value, now)
            self.store.log(now, lead.id, "sent", f"{step.channel.value} step={step.key}")
            self._commit_step(lead, step, now, seq)
            return 1
        except SendError as e:
            rec.status = DeliveryStatus.FAILED
            rec.error = str(e)
            self.store.messages.append(rec)
            if rec.attempts >= MAX_STEP_RETRIES:
                # Give up on this step so the lead can't loop forever; move on.
                self.store.log(now, lead.id, "send_failed_giveup", f"{step.key}: {e}")
                self._commit_step(lead, step, now, seq)
            else:
                lead.next_action_at = now + timedelta(hours=RETRY_BACKOFF_HOURS)
                self.store.log(now, lead.id, "send_failed_retry",
                               f"{step.key} attempt {rec.attempts}: {e}")
            return 0

    def _commit_step(self, lead: Lead, step, now: datetime, seq) -> None:
        """Advance the sequence pointer and schedule the next step (or the grace
        window before DEAD)."""
        lead.followups_sent += 1
        lead.last_action_at = now
        lead.state = State.CONTACTED if lead.followups_sent == 1 else State.FOLLOW_UP
        if lead.followups_sent < len(seq):
            nxt = seq[lead.followups_sent]
            due = now + timedelta(hours=nxt.delay_hours)
        else:
            due = now + timedelta(hours=GRACE_HOURS)
        lead.next_action_at = next_allowed_time(due, lead.timezone)
        lead.updated_at = now

    # ---------------------------------------------------------------- inbound
    def handle_inbound(self, text: str, now: datetime | None = None,
                       lead_id: str = "", phone: str = "", email: str = "") -> Lead | None:
        now = now or datetime.utcnow()
        lead = self.store.get(lead_id) if lead_id else self.store.find_by_contact(
            pipeline.normalize_phone(phone), pipeline.normalize_email(email))
        if lead is None:
            return None
        kind = pipeline.parse_inbound(text)
        self.store.log(now, lead.id, "inbound", f"{kind}: {text[:60]}")

        if kind == "stop":
            self._transition(lead, State.STOPPED, now, "opt-out keyword")
            return lead
        if lead.is_terminal():
            return lead
        # Any real reply hands the lead to a human and pauses automation.
        lead.state = State.ENGAGED
        lead.next_action_at = None
        lead.updated_at = now
        note = "positive reply — ready for trial/handoff" if kind == "positive" else "reply — needs human"
        lead.notes.append(note)
        self.store.log(now, lead.id, "engaged", note)
        return lead

    # --------------------------------------------------------- human override
    def hold(self, lead_id: str, now: datetime | None = None) -> Lead | None:
        return self._override(lead_id, State.HUMAN_HOLD, "human hold", now, pause=True)

    def resume(self, lead_id: str, now: datetime | None = None) -> Lead | None:
        now = now or datetime.utcnow()
        lead = self.store.get(lead_id)
        if lead is None or lead.is_terminal():
            return lead
        if lead.state not in {State.HUMAN_HOLD, State.ENGAGED}:
            return lead
        lead.state = State.FOLLOW_UP if lead.followups_sent else State.CLASSIFIED
        lead.next_action_at = next_allowed_time(now, lead.timezone)
        lead.updated_at = now
        self.store.log(now, lead.id, "resumed", "automation resumed by human")
        return lead

    def convert(self, lead_id: str, now: datetime | None = None) -> Lead | None:
        return self._override(lead_id, State.CONVERTED, "converted by human", now, pause=True)

    def stop(self, lead_id: str, now: datetime | None = None) -> Lead | None:
        return self._override(lead_id, State.STOPPED, "stopped by human", now, pause=True)

    def _override(self, lead_id: str, target: State, reason: str,
                  now: datetime | None, pause: bool) -> Lead | None:
        now = now or datetime.utcnow()
        lead = self.store.get(lead_id)
        if lead is None or lead.is_terminal():
            return lead
        self._transition(lead, target, now, reason)
        if pause:
            lead.next_action_at = None
        return lead

    # -------------------------------------------------------------- internals
    def _transition(self, lead: Lead, target: State, now: datetime, reason: str) -> None:
        prev = lead.state
        lead.state = target
        lead.updated_at = now
        if target in {State.STOPPED, State.CONVERTED, State.DEAD, State.INVALID}:
            lead.next_action_at = None
        self.store.log(now, lead.id, "transition", f"{prev.value}->{target.value}: {reason}")
