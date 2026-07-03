"""In-memory lead store with a dedup index, plus an append-only audit log and
metrics. Persisting to JSON is provided for the CLI; the engine only depends on
the in-memory interface so tests stay fast and deterministic.
"""
from __future__ import annotations

import json
from dataclasses import asdict, dataclass, field
from datetime import datetime

from .models import Lead, MessageRecord, State


@dataclass
class AuditEvent:
    at: datetime
    lead_id: str
    action: str
    detail: str = ""


class LeadStore:
    def __init__(self) -> None:
        self._leads: dict[str, Lead] = {}
        # dedup: normalized phone/email -> lead_id, so re-submitting the same
        # person merges instead of creating a duplicate lead.
        self._by_contact: dict[str, str] = {}
        # message dedup keys already sent, to suppress identical resends.
        self._sent_message_keys: set[str] = set()
        self.messages: list[MessageRecord] = []
        self.audit: list[AuditEvent] = []
        self._seq = 0

    # -- ids ----------------------------------------------------------------
    def next_id(self) -> str:
        self._seq += 1
        return f"L{self._seq:05d}"

    # -- lead lookup / dedup ------------------------------------------------
    def find_by_contact(self, phone: str, email: str) -> Lead | None:
        for key in filter(None, (phone, email)):
            lid = self._by_contact.get(key)
            if lid:
                return self._leads.get(lid)
        return None

    def index_contact(self, lead: Lead) -> None:
        for key in filter(None, (lead.phone, lead.email)):
            self._by_contact[key] = lead.id

    def add(self, lead: Lead) -> None:
        self._leads[lead.id] = lead
        self.index_contact(lead)

    def get(self, lead_id: str) -> Lead | None:
        return self._leads.get(lead_id)

    def all(self) -> list[Lead]:
        return list(self._leads.values())

    def active(self) -> list[Lead]:
        return [l for l in self._leads.values() if not l.is_terminal()]

    # -- message dedup ------------------------------------------------------
    def already_sent(self, key: str) -> bool:
        return key in self._sent_message_keys

    def mark_sent(self, key: str) -> None:
        self._sent_message_keys.add(key)

    # -- audit / metrics ----------------------------------------------------
    def log(self, at: datetime, lead_id: str, action: str, detail: str = "") -> None:
        self.audit.append(AuditEvent(at, lead_id, action, detail))

    def metrics(self) -> dict:
        by_state: dict[str, int] = {}
        for l in self._leads.values():
            by_state[l.state.value] = by_state.get(l.state.value, 0) + 1
        sent = [m for m in self.messages if m.status.value == "SENT"]
        by_channel: dict[str, int] = {}
        for m in sent:
            by_channel[m.channel.value] = by_channel.get(m.channel.value, 0) + 1
        return {
            "leads_total": len(self._leads),
            "by_state": by_state,
            "messages_sent": len(sent),
            "messages_sent_by_channel": by_channel,
            "messages_failed": sum(1 for m in self.messages if m.status.value == "FAILED"),
            "messages_suppressed": sum(1 for m in self.messages if m.status.value == "SUPPRESSED"),
            "opt_outs": by_state.get(State.STOPPED.value, 0),
            "converted": by_state.get(State.CONVERTED.value, 0),
        }

    # -- persistence (CLI convenience) -------------------------------------
    def to_json(self) -> str:
        def enc(o):
            if isinstance(o, datetime):
                return o.isoformat()
            if hasattr(o, "value"):
                return o.value
            return str(o)
        return json.dumps({
            "leads": [asdict(l) for l in self._leads.values()],
            "messages": [asdict(m) for m in self.messages],
            "audit": [asdict(a) for a in self.audit],
        }, default=enc, indent=2)
