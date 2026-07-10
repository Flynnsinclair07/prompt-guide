"""Message-delivery adapters.

The engine talks to an abstract Sender. The default ConsoleSender needs no
credentials and just records what *would* be sent — so the whole system runs and
is fully testable with zero external services. TwilioSender / SmtpSender are thin
stubs that activate only when their env vars are present.
"""
from __future__ import annotations

import os
from dataclasses import dataclass, field

from .models import Channel


class SendError(Exception):
    """Raised by a Sender when delivery fails (engine will retry/track)."""


@dataclass
class SendResult:
    ok: bool
    provider_id: str = ""
    error: str = ""


class Sender:
    """Interface. Implementations must be safe to call repeatedly."""
    channel: Channel

    def send(self, to: str, body: str) -> SendResult:  # pragma: no cover - interface
        raise NotImplementedError


@dataclass
class ConsoleSender(Sender):
    """Dry-run adapter: records outbound messages, always succeeds. Default."""
    channel: Channel = Channel.SMS
    outbox: list = field(default_factory=list)
    echo: bool = False

    def send(self, to: str, body: str) -> SendResult:
        self.outbox.append({"to": to, "body": body, "channel": self.channel.value})
        if self.echo:
            print(f"[{self.channel.value}->{to}] {body}")
        return SendResult(ok=True, provider_id=f"console-{len(self.outbox)}")


@dataclass
class ScriptedSender(Sender):
    """Test helper: fail the first `fail_times` calls, then succeed. Lets tests
    exercise retry, partial delivery, and backoff deterministically."""
    channel: Channel = Channel.SMS
    fail_times: int = 0
    calls: int = 0
    outbox: list = field(default_factory=list)

    def send(self, to: str, body: str) -> SendResult:
        self.calls += 1
        if self.calls <= self.fail_times:
            raise SendError(f"scripted failure {self.calls}/{self.fail_times}")
        self.outbox.append({"to": to, "body": body})
        return SendResult(ok=True, provider_id=f"scripted-{self.calls}")


class TwilioSender(Sender):
    """Live SMS via Twilio. Activated only when TWILIO_* env vars are set.

    Requires: TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN, TWILIO_FROM_NUMBER, and the
    `twilio` package. Kept as a thin adapter so the core stays provider-neutral.
    """
    channel = Channel.SMS

    def __init__(self) -> None:
        self.sid = os.environ.get("TWILIO_ACCOUNT_SID", "")
        self.token = os.environ.get("TWILIO_AUTH_TOKEN", "")
        self.from_number = os.environ.get("TWILIO_FROM_NUMBER", "")
        if not (self.sid and self.token and self.from_number):
            raise RuntimeError("TwilioSender needs TWILIO_ACCOUNT_SID / _AUTH_TOKEN / _FROM_NUMBER")

    def send(self, to: str, body: str) -> SendResult:  # pragma: no cover - needs creds
        try:
            from twilio.rest import Client
        except ImportError as e:
            raise SendError(f"twilio package not installed: {e}")
        try:
            client = Client(self.sid, self.token)
            msg = client.messages.create(to=to, from_=self.from_number, body=body)
            return SendResult(ok=True, provider_id=msg.sid)
        except Exception as e:
            raise SendError(str(e))


class SmtpSender(Sender):
    """Live email via SMTP. Activated only when SMTP_* env vars are set.

    Requires: SMTP_HOST, SMTP_USER, SMTP_PASSWORD, SMTP_FROM (and optional SMTP_PORT).
    """
    channel = Channel.EMAIL

    def __init__(self) -> None:
        self.host = os.environ.get("SMTP_HOST", "")
        self.port = int(os.environ.get("SMTP_PORT", "587"))
        self.user = os.environ.get("SMTP_USER", "")
        self.password = os.environ.get("SMTP_PASSWORD", "")
        self.from_addr = os.environ.get("SMTP_FROM", "")
        if not (self.host and self.user and self.password and self.from_addr):
            raise RuntimeError("SmtpSender needs SMTP_HOST / _USER / _PASSWORD / _FROM")

    def send(self, to: str, body: str) -> SendResult:  # pragma: no cover - needs creds
        import smtplib
        from email.mime.text import MIMEText
        try:
            # First line of body is the subject; the rest is the message.
            subject, _, message = body.partition("\n")
            msg = MIMEText(message or subject)
            msg["Subject"] = subject
            msg["From"] = self.from_addr
            msg["To"] = to
            with smtplib.SMTP(self.host, self.port, timeout=20) as s:
                s.starttls()
                s.login(self.user, self.password)
                s.sendmail(self.from_addr, [to], msg.as_string())
            return SendResult(ok=True, provider_id=f"smtp:{to}")
        except Exception as e:
            raise SendError(str(e))


def default_senders(echo: bool = False) -> dict:
    """Pick live providers when configured, else dry-run console. Never raises —
    a misconfigured provider falls back to console so the system always runs."""
    senders: dict = {}
    try:
        senders[Channel.SMS] = TwilioSender()
    except Exception:
        senders[Channel.SMS] = ConsoleSender(channel=Channel.SMS, echo=echo)
    try:
        senders[Channel.EMAIL] = SmtpSender()
    except Exception:
        senders[Channel.EMAIL] = ConsoleSender(channel=Channel.EMAIL, echo=echo)
    return senders
