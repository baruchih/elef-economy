"""Reference implementation of the Agentic Economics task/verification/dispute loop, baseline v1.0.1.

This package encodes the *rules* of the specification. It makes no decisions:
every bid, verdict, appeal, audit assignment, ruling and human action is injected by
the caller (a test, or later a policy). After every tick the §17 invariants are checked.
"""
from .params import Params
from .ledger import Ledger, LedgerError, History
from .engine import World, RuleError, ReviewView
from .invariants import InvariantError, check_all

__all__ = ["Params", "Ledger", "LedgerError", "History", "World", "RuleError", "ReviewView",
           "InvariantError", "check_all"]
