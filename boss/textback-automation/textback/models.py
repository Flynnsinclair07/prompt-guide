"""Domain model for the Text-Back + Email automation system.

Everything here is plain data + enums. Behavior lives in engine.py so the state
model stays easy to reason about and test.
"""
from __future__ import annotations

import enum
import hashlib
from dataclasses import dataclass, field
from datetime import datetime


class State(str, enum.Enum):
    """Lead lifecycle states. Terminal states never transition out again."""
    NEW = "NEW"                    # just entered, not yet validated
    INVALID = "INVALID"            # failed validation (terminal)
    VALIDATED = "VALIDATED"        # contactable, not yet classified
    CLASSIFIED = "CLASSIFIED"      # HOT/WARM/COLD assigned, ready for first outreach
    CONTACTED = "CONTACTED"        # first outreach sent, awaiting reply
    FOLLOW_UP = "FOLLOW_UP"        # in the follow-up drip
    ENGAGED = "ENGAGED"            # lead replied positively; automation paused for human
    HUMAN_HOLD = "HUMAN_HOLD"      # a human explicitly paused automation
    CONVERTED = "CONVERTED"        # won (terminal)
    STOPPED = "STOPPED"            # opted out / STOP keyword (terminal, do-not-contact)
    DEAD = "DEAD"                  # sequence exhausted, no engagement (terminal)


TERMINAL_STATES = {State.INVALID, State.CONVERTED, State.STOPPED, State.DEAD}

# Which states the automation engine is allowed to act on (send messages for).
# ENGAGED and HUMAN_HOLD are intentionally excluded: a human owns the lead there.
ACTIONABLE_STATES = {State.CLASSIFIED, State.CONTACTED, State.FOLLOW_UP}


class Temperature(str, enum.Enum):
    HOT = "HOT"
    WARM = "WARM"
    COLD = "COLD"


class Channel(str, enum.Enum):
    SMS = "SMS"
    EMAIL = "EMAIL"


class DeliveryStatus(str, enum.Enum):
    PENDING = "PENDING"
    SENT = "SENT"
    FAILED = "FAILED"
    SUPPRESSED = "SUPPRESSED"     # deliberately not sent (opt-out, dedup, quiet hours, rate limit)


@dataclass
class MessageRecord:
    """One attempt to send one message on one channel."""
    lead_id: str
    channel: Channel
    body: str
    step: str                      # sequence step key, e.g. "hot_1", "warm_2"
    status: DeliveryStatus = DeliveryStatus.PENDING
    attempts: int = 0
    created_at: datetime | None = None
    sent_at: datetime | None = None
    error: str = ""
    suppressed_reason: str = ""

    @property
    def dedup_key(self) -> str:
        """Identity of a message for duplicate suppression: same lead+channel+body."""
        h = hashlib.sha1(self.body.strip().lower().encode()).hexdigest()[:12]
        return f"{self.lead_id}:{self.channel.value}:{h}"


@dataclass
class Lead:
    id: str
    name: str = ""
    phone: str = ""                # normalized E.164 once validated
    email: str = ""                # normalized lower-case once validated
    timezone: str = "America/Denver"
    source: str = ""
    state: State = State.NEW
    temperature: Temperature | None = None
    recommended_plan: str = ""
    trial_offered: bool = False
    signals: dict = field(default_factory=dict)   # arbitrary scoring inputs

    followups_sent: int = 0
    last_action_at: datetime | None = None
    next_action_at: datetime | None = None
    created_at: datetime | None = None
    updated_at: datetime | None = None

    # idempotency: the step key we most recently *committed* to sending, so a
    # re-entrant/concurrent tick can't double-send the same step.
    last_committed_step: str = ""

    notes: list[str] = field(default_factory=list)

    @property
    def contactable(self) -> bool:
        return bool(self.phone or self.email) and self.state not in TERMINAL_STATES

    def is_terminal(self) -> bool:
        return self.state in TERMINAL_STATES
