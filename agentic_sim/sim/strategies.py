"""Decision interfaces. The skeleton ships no strategies; these are the seams.

A simulation driver (not included) calls these each tick, in the §2.2 order, and
translates the answers into World actions. Tests bypass them and script the actions.

Reviewers are handed a `ReviewView` (World.observe), not the world: the view carries the
submission and the assignment's terms and omits the case's verdicts, challenge records,
reviewer identities, and whether the assignment is an audit (§14).
"""
from __future__ import annotations
from typing import Protocol, Optional
from .engine import ReviewView


class ActorPolicy(Protocol):
    def bid(self, world, case_id: str) -> Optional[tuple[float, int]]:
        """Return (B, tau) or None to pass. Must respect B <= beta."""

    def execute(self, world, case_id: str) -> None:
        """Spend resources, post nested requests, submit. One tick's worth of work."""

    def respond(self, world, case_id: str, verdict: str) -> str:
        """'accept' | 'appeal' | 'revise' | 'supply_evidence'."""

    def review(self, view: ReviewView) -> tuple[str, float, Optional[str]]:
        """Return (verdict, real_cost, objection). The view states its question and its
        admissible answers. For `question == "fulfillment"` return F or N, or P or ⊥ only
        when `view.responses_available` is True (the first review of an unrevised submission;
        the view does not say whether the question is an initial review or an audit, and the
        admissible answers do not depend on it); objection None. For an appeal of a ⊥
        (`question == "appeal"`, `appealed_assessment == "⊥"`) return F or N and objection
        'upheld' or 'rejected'; for any other appeal or dispute return F or N, objection None."""

    def judge_nested(self, world, case_id: str) -> str:
        """'F' | 'N'."""

    def volunteer_for_duty(self, world) -> bool: ...


class OrchestratorPolicy(Protocol):
    def select(self, world, case_id: str, bids: dict[str, tuple[float, int]]) -> Optional[str]:
        """Return the winning actor id, or None if no acceptable offer (§5.2)."""

    def should_audit(self, world, case_id: str, reviewer_id: str) -> bool:
        """Roll the reviewer's adaptive rate (§8.3)."""

    def rule(self, world, case_id: str) -> tuple[str, Optional[str]]:
        """('F'|'N', objection-or-None) on a split (§8.4)."""


class RequesterPolicy(Protocol):
    def post(self, world, t: int) -> Optional[float]:
        """Return a beta to post a root request this tick, or None."""

    def react(self, world, case_id: str) -> Optional[str]:
        """'accept' | 'dispute' | None (silence)."""
