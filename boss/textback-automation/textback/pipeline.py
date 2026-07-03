"""Pure lead-processing logic: validation, classification, plan recommendation,
and the follow-up sequence definitions. All deterministic and side-effect free so
it's trivial to unit-test.
"""
from __future__ import annotations

import re
from dataclasses import dataclass

from .models import Channel, Temperature

# ---------------------------------------------------------------------------
# Validation / normalization
# ---------------------------------------------------------------------------
_EMAIL_RE = re.compile(r"^[^@\s]+@[^@\s]+\.[^@\s]+$")


def normalize_phone(raw: str, default_country: str = "1") -> str:
    """Return E.164 (+1XXXXXXXXXX) or '' if it can't be made into a valid number."""
    if not raw:
        return ""
    digits = re.sub(r"[^\d]", "", raw)
    if raw.strip().startswith("+"):
        return "+" + digits if 8 <= len(digits) <= 15 else ""
    if len(digits) == 10:                       # US local
        return f"+{default_country}{digits}"
    if len(digits) == 11 and digits.startswith("1"):
        return f"+{digits}"
    if 8 <= len(digits) <= 15:
        return f"+{digits}"
    return ""


def normalize_email(raw: str) -> str:
    e = (raw or "").strip().lower()
    return e if _EMAIL_RE.match(e) else ""


@dataclass
class Validation:
    ok: bool
    phone: str
    email: str
    reason: str = ""


def validate_lead(name: str, phone: str, email: str) -> Validation:
    """A lead is contactable if it has at least one valid channel."""
    p = normalize_phone(phone)
    e = normalize_email(email)
    if not p and not e:
        return Validation(False, "", "", "no valid phone or email")
    return Validation(True, p, e)


# ---------------------------------------------------------------------------
# Classification: HOT / WARM / COLD from signals
# ---------------------------------------------------------------------------
def classify(signals: dict) -> Temperature:
    """Score a lead from behavioral/intent signals.

    Recognized signals (all optional):
      requested_callback: bool   +3
      replied_inbound:    bool    (handled upstream, but boosts here) +3
      visited_pricing:    bool   +2
      opened_email:       bool   +1
      form_completeness:  0..1    up to +2
      budget_confirmed:   bool   +2
      source in {referral, demo_request}: +2
    """
    score = 0.0
    if signals.get("requested_callback"):
        score += 3
    if signals.get("replied_inbound"):
        score += 3
    if signals.get("visited_pricing"):
        score += 2
    if signals.get("opened_email"):
        score += 1
    score += 2 * float(signals.get("form_completeness", 0) or 0)
    if signals.get("budget_confirmed"):
        score += 2
    if signals.get("source") in {"referral", "demo_request"}:
        score += 2

    if score >= 6:
        return Temperature.HOT
    if score >= 3:
        return Temperature.WARM
    return Temperature.COLD


# ---------------------------------------------------------------------------
# Plan recommendation + trial
# ---------------------------------------------------------------------------
PLANS = ("Starter", "Pro", "Enterprise")


def recommend_plan(temp: Temperature, signals: dict) -> str:
    seats = int(signals.get("seats", 1) or 1)
    if signals.get("budget_confirmed") and seats >= 20:
        return "Enterprise"
    if temp == Temperature.HOT or seats >= 5:
        return "Pro"
    return "Starter"


def offer_trial(temp: Temperature) -> bool:
    """Trials are offered to HOT/WARM leads to accelerate conversion; COLD leads
    get nurtured first (a trial clock would just expire unused)."""
    return temp in {Temperature.HOT, Temperature.WARM}


# ---------------------------------------------------------------------------
# Follow-up sequences
# ---------------------------------------------------------------------------
@dataclass(frozen=True)
class Step:
    key: str
    channel: Channel
    delay_hours: float             # hours after the previous step
    template: str                  # {name}, {plan} interpolated


# Each temperature drives a different cadence. HOT = fast + high touch; COLD = slow.
SEQUENCES: dict[Temperature, list[Step]] = {
    Temperature.HOT: [
        Step("hot_1", Channel.SMS,   0.0,
             "Hi {name}, thanks for reaching out! Based on what you shared, {plan} looks like the right fit. "
             "Want me to set up your free trial? Reply YES and I'll send the link. Reply STOP to opt out."),
        Step("hot_2", Channel.EMAIL, 1.0,
             "Your {plan} trial is ready\nHi {name}, following up by email too — here's everything about your {plan} "
             "trial. Reply anytime and a real person will help you get set up."),
        Step("hot_3", Channel.SMS,   24.0,
             "Hi {name}, just checking in — still happy to get your {plan} trial going whenever you're ready. Reply STOP to opt out."),
    ],
    Temperature.WARM: [
        Step("warm_1", Channel.EMAIL, 0.0,
             "A quick hello from us\nHi {name}, thanks for your interest. {plan} is a popular starting point — "
             "here's a short overview. Happy to answer any questions."),
        Step("warm_2", Channel.SMS,   48.0,
             "Hi {name}, wanted to make sure you saw our note about {plan}. Any questions I can help with? Reply STOP to opt out."),
        Step("warm_3", Channel.EMAIL, 96.0,
             "Still here when you're ready\nHi {name}, no rush at all — whenever you'd like to explore {plan}, just reply."),
    ],
    Temperature.COLD: [
        Step("cold_1", Channel.EMAIL, 0.0,
             "Nice to meet you\nHi {name}, thanks for stopping by. Here are a few resources you might find useful — no pressure."),
        Step("cold_2", Channel.EMAIL, 168.0,
             "One more resource\nHi {name}, sharing one more piece that tends to help folks in your situation. Reply anytime."),
    ],
}

MAX_FOLLOWUPS = {t: len(steps) for t, steps in SEQUENCES.items()}


def render(template: str, lead_name: str, plan: str) -> str:
    name = lead_name.split()[0] if lead_name else "there"
    return template.format(name=name, plan=plan or "our plan")


# Inbound reply parsing -------------------------------------------------------
_STOP_WORDS = {"stop", "unsubscribe", "quit", "cancel", "end", "optout", "opt-out", "remove"}
_YES_WORDS = {"yes", "y", "yeah", "yep", "sure", "ok", "okay", "interested", "sounds good"}


def parse_inbound(text: str) -> str:
    """Classify an inbound reply into: 'stop', 'positive', or 'other'."""
    t = (text or "").strip().lower()
    if not t:
        return "other"
    first = re.sub(r"[^a-z-]", "", t.split()[0])
    if first in _STOP_WORDS or t in _STOP_WORDS:
        return "stop"
    if first in _YES_WORDS or t in _YES_WORDS:
        return "positive"
    return "other"
