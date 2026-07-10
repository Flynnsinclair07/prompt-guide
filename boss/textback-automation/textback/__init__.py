"""Text-Back + Email automation system.

Public surface:
    from textback import Engine, LeadStore
    from textback.models import State, Temperature, Channel
"""
from .engine import Engine
from .store import LeadStore

__all__ = ["Engine", "LeadStore"]
