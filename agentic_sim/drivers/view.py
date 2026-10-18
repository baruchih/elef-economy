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

    def roll_audit(self, cid: str):
        """1.4.0 §2.2: the driver's roll said yes — record the audit as an obligation of the case."""
        self._w.roll_audit(cid)

    def audit_odds(self, cid: str) -> float:
        """The odds to roll for a pending approval (1.3.0 §2.2 applied odds; 1 for the state's own work)."""
        return self._w.audit_odds(cid)

    def is_troop(self, wid) -> bool:
        return self._w.is_troop(wid)

    def troops(self) -> dict:
        """1.4.0 §2.5 readings: the troops and the counters."""
        w = self._w
        return {"troops": {k: dict(v) for k, v in w.troops.items()},
                "active_reviews": sum(1 for t in w.troops.values() if t["kind"] == "review" and t["t_release"] is None),
                "active_deliveries": sum(1 for t in w.troops.values() if t["kind"] == "delivery" and t["t_release"] is None),
                "summons_reviews": w.troop_summons_reviews, "summons_deliveries": w.troop_summons_deliveries,
                "shortfall_seats": w.troop_shortfall_seats, "shortfall_awards": w.troop_shortfall_awards,
                "held_ticks": w.troop_held_ticks, "troop_ticks_reviews": w.troop_ticks_reviews,
                "troop_ticks_deliveries": w.troop_ticks_deliveries,
                "held_market_audit_now": w.held_market_audit_now, "held_market_audit_max_age": w.held_market_audit_max_age,
                "fund_reserve": w.R_T, "advance_outstanding": w.advance_outstanding, "B_bar": w.mean_awarded_price(),
                # 1.7.1: the award summons per request — the w_A-old requests at the last seating, the members free for them,
                # and the requests left to those members, summed
                "awards_waiting_now": w.awards_waiting_now, "members_free_now": w.members_free_now,
                "awards_left_to_members": w.awards_left_to_members,
                # 1.5.0 §2.1: the troop demand at the last seating and its components
                "demand": w.troop_demand_now, "demand_held": w.troop_demand_held, "demand_refused": w.troop_demand_refused,
                "demand_peak_refused": w.troop_demand_peak_refused,
                # 1.6.0: panels held by troops this period, the seats and the queue, Ω's readings
                "troop_panel_summons_period": w.period["troop_panel_summons"],
                "x_target": w._x_target, "waiting_initial": w._waiting_initial, "waiting_panel": w._waiting_panel,
                "omega_unlocked": w.ledger.wallet(w.ledger.OMEGA).U, "omega_min_period": w.period["omega_min"],
                "plant_reserve": w._plant_reserve(), "first_plant_adjudicated_at": w.first_plant_adjudicated_at}

    def service(self) -> dict:
        """1.6.0 §2.1 readings: the network rating and Ω's liabilities."""
        w = self._w
        return {"on_time": w.on_time_n, "late": w.late_n, "lateness_sum": w.lateness_sum,
                "rebates_owed": w.rebates_owed, "rebates_paid": w.rebates_paid,
                "liabilities_accrued": w.liabilities_accrued, "liabilities_paid": w.liabilities_paid,
                "liabilities_outstanding": sum(l["amount"] for l in w.omega_liabilities),
                # the part older than a period — what Ω pays before it advances (1.6.0 §2.2)
                "liabilities_old": sum(l["amount"] for l in w.omega_liabilities if w.t - l["t"] >= w.p.period_ticks),
                "open_late": w.open_late()}

    # -- the orchestrator's planted work and its clock (1.2.0 §2.1–§2.3) -----------
    def create_plant(self, truth: bool, B: float) -> str:
        """A case whose fulfillment the orchestrator knows by construction, funded by Ω."""
        return self._w.create_plant(truth, B)

    def plants_due(self) -> int:
        """Whole plants the plant rate calls for that have not been created."""
        return self._w.plants_due()

    def p_effective(self, aid: str) -> float:
        """The audit odds to roll for a reviewer: min(1, m_t · p_j)."""
        return self._w.actors[aid].p_eff

    def dial(self) -> dict:
        """The dial's public state: m_t, π_t, X_t, the counters and the period records."""
        w = self._w
        return {"m": w.m_t, "pi": w.pi_t, "X_t": w.X_t, "plant_credit": w.plant_credit,
                "plants_created": w.plants_created, "plant_shortfall": w.plant_shortfall,
                "eligibility_shortfall": w.eligibility_shortfall, "reserve_shortfall_now": w.reserve_shortfall_now,
                "suspensions": w.suspensions, "alarms": w.alarms, "alarm_streak": w.alarm_streak,
                "member_seats": w.member_seats, "readmissions": w.readmissions,
                "readmission_ticks_mean": (w.readmission_ticks_sum / w.readmissions) if w.readmissions else None,
                "periods": list(w.periods), "period": dict(w.period)}

    def membership(self, aid: str) -> str:
        """1.3.0: member | suspended | probationer."""
        a = self._w.actors[aid]
        return "suspended" if a.suspended_until is not None else ("probationer" if a.probation else "member")

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
        from sim.engine import PLANT_REQ, PLANT_ACT, DUTY_FUND, TROOP_ACCT
        plant_wallets = L.wallet(PLANT_REQ).W + L.wallet(PLANT_ACT).W
        return {"M": L.M, "Res": L.Res, "v": L.v, "omega": L.wallet(L.OMEGA).U,
                "omega_total": L.wallet(L.OMEGA).W + plant_wallets,      # Ω's money, plants' working capital included
                "omega_in_plants": plant_wallets,
                "duty_fund": L.wallet(DUTY_FUND).U, "fund_in": self._w.fund_in, "fund_out": self._w.fund_out,
                # 1.7.0 §2.1: the troop account and Ω's record by source
                "troop_account": L.wallet(TROOP_ACCT).U, "troop_surplus_paid": self._w.troop_surplus_paid,
                "omega_fee_income": self._w.omega_fee_income, "advances_made": self._w.advances_made,
                "advances_repaid": self._w.advances_repaid,
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
