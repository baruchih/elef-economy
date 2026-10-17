"""The public surface of `World`, as a driver sees it.

`World` has no enforced read-only facade; "public operations only" is a convention (CLAUDE.md).
This wrapper makes the convention checkable: a driver that holds a `Public` and nothing else can
call exactly the operations listed here — the ones a participant or the orchestrator may take
under the rules — and read what the rules let them read. Nothing here decides anything.

Reads return the engine's own objects (cases, reviews, actors, wallets) for inspection; a driver
that assigns to one of their fields has reached into the engine, and that is what review of the
driver code checks for. Policies for reviewers get a `ReviewView` (`observe`), not a case.
"""
from __future__ import annotations
from typing import Iterable, Optional

from sim import World, ReviewView


class Public:
    def __init__(self, world: World):
        self._w = world

    # -- time -----------------------------------------------------------------
    @property
    def t(self) -> int:
        return self._w.t

    @property
    def params(self):
        return self._w.p

    def advance(self, to_t: int):
        self._w.advance(to_t)

    # -- requester operations (§5, §6) ------------------------------------------
    def post_root(self, requester: str, beta: float) -> str:
        return self._w.post_root(requester, beta)

    def withdraw_unawarded(self, cid: str):
        self._w.withdraw_unawarded(cid)

    def accept_explicit(self, cid: str, requester: str):
        self._w.accept_explicit(cid, requester)

    def dispute(self, cid: str, challenger: str, d: Optional[str] = None):
        self._w.dispute(cid, challenger, d)

    # -- orchestrator operations (§5.2, §8) --------------------------------------
    def award(self, cid: str, actor: str, B: float, tau: int):
        self._w.award(cid, actor, B, tau)

    def assign_initial(self, cid: str, reviewer: str) -> str:
        return self._w.assign_initial(cid, reviewer)

    def assign_audit(self, cid: str, reviewer: str) -> str:
        return self._w.assign_audit(cid, reviewer)

    def assign_appeal(self, cid: str, reviewer: str) -> str:
        return self._w.assign_appeal(cid, reviewer)

    def rule(self, cid: str, outcome: str, objection: Optional[str] = None):
        self._w.rule(cid, outcome, objection)

    # -- actor operations (§5, §6, §9) -------------------------------------------
    def submit(self, cid: str):
        self._w.submit(cid)

    def resubmit(self, cid: str):
        self._w.resubmit(cid)

    def spend(self, actor: str, real_cost: float, cid: Optional[str] = None) -> float:
        return self._w.spend(actor, real_cost, cid)

    def respond(self, cid: str, action: str, d: Optional[str] = None):
        self._w.respond(cid, action, d)

    def post_nested(self, parent: str, beta: float) -> str:
        return self._w.post_nested(parent, beta)

    def judge_nested(self, cid: str, verdict: str):
        self._w.judge_nested(cid, verdict)

    def cancel_nested(self, cid: str):
        self._w.cancel_nested(cid)

    def volunteer(self, actor: str, flag: bool = True):
        self._w.volunteer(actor, flag)

    # -- reviewer operations (§7, §8, §14) ---------------------------------------
    def observe(self, reviewer: str, rid: str) -> ReviewView:
        return self._w.observe(reviewer, rid)

    def complete_review(self, rid: str, verdict: str, cost: float, objection: Optional[str] = None):
        self._w.complete_review(rid, verdict, cost, objection)

    # -- human operations (§15) ---------------------------------------------------
    def override(self, cid: str, human: str, outcome: str, objection: Optional[str] = None):
        self._w.override(cid, human, outcome, objection)

    # -- reads --------------------------------------------------------------------
    def case(self, cid: str):
        return self._w.cases[cid]

    def review(self, rid: str):
        return self._w.reviews[rid]

    def actor(self, aid: str):
        return self._w.actors[aid]

    def actors(self) -> Iterable[str]:
        return self._w.actors.keys()

    def unlocked(self, wid: str) -> float:
        return self._w.ledger.wallet(wid).U

    def wealth(self, wid: str) -> float:
        return self._w.ledger.wallet(wid).W

    def money(self) -> dict:
        L = self._w.ledger
        return {"M": L.M, "Res": L.Res, "v": L.v, "omega": L.wallet(L.OMEGA).U,
                "claims_outstanding": sum(cl.amount for cl in self._w.omega_claims)}

    def events_since(self, n: int) -> list:
        """The ledger's event copy from position n on — the public record of money movements."""
        return self._w.ledger.events[n:]

    def n_events(self) -> int:
        return len(self._w.ledger.events)

    def head(self) -> str:
        return self._w.history.head

    def fingerprint(self) -> dict:
        from drivers.results import fingerprint
        return fingerprint(self._w)

    def close(self):
        self._w.close()
