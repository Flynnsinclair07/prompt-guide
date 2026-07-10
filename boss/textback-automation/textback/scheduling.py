"""Timing rules: quiet hours (per-lead timezone) and rate limiting / anti-spam.

All time math takes an explicit `now`/timezone so the engine stays deterministic
under test — no hidden calls to the system clock.
"""
from __future__ import annotations

from dataclasses import dataclass, field
from datetime import datetime, timedelta

try:
    from zoneinfo import ZoneInfo
except Exception:  # pragma: no cover
    ZoneInfo = None  # type: ignore


# Quiet hours: don't message a lead outside these local hours (anti-annoyance +
# TCPA-style courtesy). Inclusive start, exclusive end.
QUIET_START_HOUR = 8    # 08:00 local
QUIET_END_HOUR = 21     # 21:00 local


def _localize(dt: datetime, tz_name: str) -> datetime:
    if ZoneInfo is None:
        return dt
    try:
        tz = ZoneInfo(tz_name)
    except Exception:
        tz = ZoneInfo("UTC")
    if dt.tzinfo is None:
        dt = dt.replace(tzinfo=ZoneInfo("UTC"))
    return dt.astimezone(tz)


def in_quiet_hours(now: datetime, tz_name: str) -> bool:
    local = _localize(now, tz_name)
    return not (QUIET_START_HOUR <= local.hour < QUIET_END_HOUR)


def next_allowed_time(now: datetime, tz_name: str) -> datetime:
    """If `now` is inside quiet hours, return the next local QUIET_START_HOUR
    (as an aware UTC-comparable datetime); otherwise return `now` unchanged."""
    if not in_quiet_hours(now, tz_name):
        return now
    local = _localize(now, tz_name)
    target = local.replace(hour=QUIET_START_HOUR, minute=0, second=0, microsecond=0)
    if local.hour >= QUIET_END_HOUR:      # past tonight's window -> tomorrow morning
        target = target + timedelta(days=1)
    # (if before QUIET_START_HOUR, target is later today — already correct)
    # Return in the system's naive-UTC convention so it compares with `now`.
    if ZoneInfo is not None and target.tzinfo is not None:
        target = target.astimezone(ZoneInfo("UTC")).replace(tzinfo=None)
    return target


@dataclass
class RateLimiter:
    """Two guards:
      - global per-channel cap within a rolling window (spam / provider throttle)
      - per-lead minimum spacing between any two messages (anti-annoyance)
    """
    per_channel_limit: int = 100
    window: timedelta = timedelta(hours=1)
    # A safety FLOOR against accidental bursts / concurrent triggers — deliberately
    # below the tightest designed cadence (HOT re-sends at +1h) so it never fights
    # the sequence. The sequences themselves are the primary spacer.
    per_lead_min_gap: timedelta = timedelta(minutes=30)

    _channel_hits: dict = field(default_factory=dict)   # channel -> [datetimes]
    _lead_last: dict = field(default_factory=dict)      # lead_id -> datetime

    def _prune(self, channel: str, now: datetime) -> None:
        cutoff = now - self.window
        hits = [t for t in self._channel_hits.get(channel, []) if t >= cutoff]
        self._channel_hits[channel] = hits

    def allow(self, lead_id: str, channel: str, now: datetime) -> tuple[bool, str]:
        self._prune(channel, now)
        if len(self._channel_hits.get(channel, [])) >= self.per_channel_limit:
            return False, f"rate limit: {channel} cap {self.per_channel_limit}/{self.window}"
        last = self._lead_last.get(lead_id)
        if last is not None and (now - last) < self.per_lead_min_gap:
            return False, f"per-lead min gap {self.per_lead_min_gap} not elapsed"
        return True, ""

    def record(self, lead_id: str, channel: str, now: datetime) -> None:
        self._channel_hits.setdefault(channel, []).append(now)
        self._lead_last[lead_id] = now
