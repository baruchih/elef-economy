"""The public surface of `World`, as a driver sees it.

`World` has no enforced read-only facade; "public operations only" is a convention (CLAUDE.md).
This wrapper makes the convention checkable: a driver that holds a `Public` and nothing else can
call exactly the operations listed here — the ones a participant or the orchestrator may take
under the rules — and read what the rules let them read. Nothing here decides anything.

Reads return live, read-only proxies of the engine's cases and reviews — every field as the engine holds it now — with their
case identifiers translated to the public surface's: since 2.6.0 (I40) a case's public identifier is a hash of the engine's,
carrying no order, translated both ways here. Events and the ReviewView come as translated copies; actors and wallets as the
engine's own. Assigning to a proxy's field is refused: a driver reads, it never reaches in. Policies for reviewers get a
`ReviewView` (`observe`), not a case.
"""
from __future__ import annotations
import copy
from typing import Iterable, Optional

from sim import World, ReviewView
from sim.invariants import public_id
from sim.engine import RuleError


class _Proxy:
    """A live, read-only view of an engine object: every attribute is read from the object as it stands now, with the id fields
    the surface translates passed through `_pub`; writes are refused (the convention made checkable)."""
    __slots__ = ("_o", "_tr")

    def __init__(self, o, tr):
        object.__setattr__(self, "_o", o)
        object.__setattr__(self, "_tr", tr)

    def __getattr__(self, name):
        v = getattr(self._o, name)
        f = self._tr.get(name)
        return f(v) if f else v

    def __setattr__(self, name, value):
        raise AttributeError(f"the public surface is read-only ({name}): a driver reads the engine, it never reaches in")

    def __eq__(self, other):
        return isinstance(other, _Proxy) and self._o is other._o

    def __hash__(self):
        return id(self._o)

    def __repr__(self):
        return f"<public view of {self._o!r}>"


class Public:
    def __init__(self, world: World):
        self._w = world
        self._eng_of: dict[str, str] = {}      # public id -> engine id, for every id this surface has handed out

    # -- identifiers (2.6.0 §2.3, I40): the public surface's ids are opaque; the engine's stay the counter ----------
    def _pub(self, cid):
        if cid is None:
            return None
        pid = public_id(cid)
        self._eng_of[pid] = cid
        return pid

    def _eng(self, pid):
        if pid is None:
            return None
        if pid in self._eng_of:
            return self._eng_of[pid]
        if pid in self._w.cases:                 # an engine id handed in (tests, the orchestrator's own bookkeeping): admitted
            return pid
        raise RuleError(f"unknown case {pid}")

    def _pub_case(self, c):
        pub = self._pub
        return _Proxy(c, {"id": pub, "root": pub, "parent": pub, "children": lambda xs: [pub(x) for x in xs]})

    def _pub_review(self, r):
        return _Proxy(r, {"case": self._pub})

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
        return self._pub(self._w.post_root(requester, beta))

    def withdraw_unawarded(self, cid: str):
        self._w.withdraw_unawarded(self._eng(cid))

    def raise_ceiling(self, cid: str, beta: float):
        """2.0.0 §2.1: a requester raises its own unawarded request's ceiling, locking the difference."""
        self._w.raise_ceiling(self._eng(cid), beta)

    def add_requester(self, name: str, wallet: float):
        """2.0.0 §2.1: a requester arrives with a wallet (a crowd's member)."""
        self._w.add_requester(name, wallet)

    def remove_requester(self, name: str):
        """2.0.0 (Appendix M): a requester leaves once its requests are served out; its wallet departs M."""
        self._w.remove_requester(name)

    def arrive(self, name: str):
        """2.3.0 §2.1: a fresh actor arrives as a probationer with a float the bank mints."""
        self._w.arrive(name)

    def depart(self, name: str):
        """2.3.0 §2.2: an actor with no live obligation leaves; its wallet departs M."""
        self._w.depart(name)

    def withdraw_pool_exhaustion(self, parent: str, nested: str):
        """§9.3: the parent exits a nested request unawarded past T_wait."""
        self._w.withdraw_pool_exhaustion(parent, self._eng(nested))

    def scenario_create(self, amount: float):
        """2.0.0 §8.3: the declared scenario operation — Ω creates a sum and pays the requesters (a money event)."""
        self._w.scenario_create(amount)

    def accept_explicit(self, cid: str, requester: str):
        self._w.accept_explicit(self._eng(cid), requester)

    def dispute(self, cid: str, challenger: str, d: Optional[str] = None):
        self._w.dispute(self._eng(cid), challenger, d)

    # -- orchestrator operations (§5.2, §8) --------------------------------------
    def award(self, cid: str, actor: str, B: float, tau: int):
        self._w.award(self._eng(cid), actor, B, tau)

    def assign_initial(self, cid: str, reviewer: str) -> str:
        return self._w.assign_initial(self._eng(cid), reviewer)

    def assign_audit(self, cid: str, reviewer: str) -> str:
        return self._w.assign_audit(self._eng(cid), reviewer)

    def assign_appeal(self, cid: str, reviewer: str) -> str:
        return self._w.assign_appeal(self._eng(cid), reviewer)

    def rule(self, cid: str, outcome: str, objection: Optional[str] = None):
        self._w.rule(self._eng(cid), outcome, objection)

    def roll_audit(self, cid: str):
        """1.4.0 §2.2: the driver's roll said yes — record the audit as an obligation of the case."""
        self._w.roll_audit(self._eng(cid))

    def audit_odds(self, cid: str) -> float:
        """The odds to roll for a pending approval (1.3.0 §2.2 applied odds; 1 for the state's own work)."""
        return self._w.audit_odds(self._eng(cid))

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
                # 2.4.0: the state's reservation — summonses declined for the floor, the state's price at its deliveries
                "summons_declined_floor": w.summons_declined_floor,
                "state_price_mean": (w.state_price_sum / w.state_price_n) if w.state_price_n else None,
                "state_price_period": (w.period["state_price_sum"] / w.period["state_price_n"]) if w.period["state_price_n"] else None,
                # 1.5.0 §2.1: the troop demand at the last seating and its components
                "demand": w.troop_demand_now, "demand_held": w.troop_demand_held, "demand_refused": w.troop_demand_refused,
                "demand_peak_refused": w.troop_demand_peak_refused,
                # 1.6.0: panels held by troops this period, the seats and the queue, Ω's readings
                "troop_panel_summons_period": w.period["troop_panel_summons"],
                "x_target": w._x_target, "waiting_initial": w._waiting_initial, "waiting_panel": w._waiting_panel,
                "omega_unlocked": w.ledger.wallet(w.ledger.OMEGA).U, "omega_min_period": w.period["omega_min"],
                "plant_reserve": w._plant_reserve(), "first_plant_adjudicated_at": w.first_plant_adjudicated_at}

    def market(self) -> dict:
        """2.0.0 readings: the price level and the market price, the deficit, issuance and departures, the flags, the capacity case;
        2.1.0: the refusals told by kind (the bank's books are `bank()`)."""
        w = self._w
        L = w.ledger
        # 2.6.0 §2.1: a plant counts among the available roots the view reports (a count that left it out would name it)
        avail = [c for c in w._live_cases.values() if c.is_root and (c.plant is None or c.plant_market) and c.state == "AVAILABLE"]
        B_bar = w.mean_awarded_price()
        return {"P_t": w.price_level(), "available_roots": len(avail), "P0": w.p.P0, "B_bar": B_bar, "index": L.index(), "v": L.v, "M": L.M,
                "created": w.deficit_created, "retired": w.deficit_retired, "deficit": w.deficit, "deficit_peak": w.deficit_peak,
                "deficit_since": w.deficit_since, "scenario_created": w.scenario_created,
                "omega_unlocked": L.wallet(L.OMEGA).U, "omega_net": L.wallet(L.OMEGA).U - w.deficit,
                "issued": w.issued, "departed": w.departed,
                "below_market_flagged": w.below_market_flagged, "below_market_waiting": sum(1 for c in avail if c.beta + 1e-9 < B_bar),
                "ceilings_raised": w.ceilings_raised,
                # 2.4.0 §2.1–2.2: the state's floor and price are public; the mark and its stock are readable by a requester's policy
                "state_floor": w._state_floor(), "state_price": w._state_price(),
                "below_reservation_marked": w.below_reservation_marked,
                "below_reservation_waiting": sum(1 for c in avail if c.below_reservation),
                "below_reservation_ticks": sum(w.t - c.below_reservation_since for c in avail if c.below_reservation and c.below_reservation_since is not None),
                "summons_declined_floor": w.summons_declined_floor,
                "places_held": w._places_held(), "N_T": w.p.N_T,
                "refused_capacity_seats": w.troop_refused_capacity_seats, "refused_capacity_awards": w.troop_refused_capacity_awards,
                "refused_capacity_waiting": sum(1 for c in avail if c.refused_capacity > 0),
                "capacity_wait_max": max([c.capacity_wait_max for c in w._live_cases.values()] + [0]),
                "price_n_period": w.period["price_n"], "award_n_period": w.period["award_n"],
                # 2.1.0 §2.6: the marks — requests waiting with a refusal told, by kind
                "refused_waiting": {"capacity": sum(1 for c in avail if c.refused == "capacity"),
                                    "credit": sum(1 for c in avail if c.refused == "credit")},
                "refused_credit_awards": w.troop_refused_credit_awards, "refused_credit_seats": w.troop_refused_credit_seats,
                # 2.3.0 §2.5: what an outsider may read — the market's counts and the gate's length, nothing per actor
                "members_total": sum(1 for a in w.actors.values() if a.is_member),
                "members_free": sum(1 for a in w.actors.values() if a.is_member and not a.on_duty and a.committed is None and a.open_review is None),
                "probationers": sum(1 for a in w.actors.values() if a.probation), "actors": len(w.actors),
                "arrivals": w.arrivals, "admissions": w.admissions, "actor_departures": w.actor_departures,
                "time_to_membership": (w.periods[-1].get("time_to_membership") if w.periods else None),
                "time_to_membership_run": (w.admission_ticks_sum / w.admissions) if w.admissions else None,
                "state_share_period": (w.period["troop_summons_deliveries"] / max(1, w.period["troop_summons_deliveries"] + w.period["award_n"])),
                "pool_advances": w.pool_advances}

    def bank(self) -> dict:
        """2.1.0 readings: the bank's books — minted and destroyed by kind, loans outstanding, the debt, the liabilities, the wall,
        Ω's retained income and net position, the cost of truth, the state's rate and burn."""
        w = self._w
        L = w.ledger
        liab = sum(l["amount"] for l in w.omega_liabilities)
        wall = w._debt_bound()
        return {"on": w.bank_on, "minted": dict(w.bank_minted), "destroyed": dict(w.bank_destroyed),
                "loans_outstanding": w.loans_outstanding, "loans_peak": w.loans_peak, "loans_open": len(w.loans),
                "debt": w.debt, "debt_created": w.debt_created, "debt_repaid": w.debt_repaid, "debt_peak": w.debt_peak,
                "debt_since": w.debt_since, "liabilities": liab, "liabilities_n": len(w.omega_liabilities),
                "liabilities_oldest": (w.t - min(l["t"] for l in w.omega_liabilities)) if w.omega_liabilities else 0,
                "wall": None if wall == float("inf") else wall, "wall_slack": None if wall == float("inf") else wall - w.debt,
                "omega_retained": L.wallet(L.OMEGA).U, "omega_net": L.wallet(L.OMEGA).U - w.debt - liab,
                "omega_fee_income": w.omega_fee_income, "omega_review_fee_income": w.omega_review_fee_income,
                "cost_of_truth": w.bank_minted["mint_plant"] - w.bank_destroyed["retire_plant"],
                "b_T": w._state_fail_rate(), "last_b_t": w.last_b_t, "last_c_d_t": w.last_c_d_t,
                "state_closed_period": w.period["state_closed"], "state_failed_period": w.period["state_failed"],
                "P_published": w._P_published, "P_published_at": w._P_published_at}

    def service(self) -> dict:
        """1.6.0 §2.1 readings: the network rating and Ω's liabilities."""
        w = self._w
        return {"on_time": w.on_time_n, "late": w.late_n, "lateness_sum": w.lateness_sum,
                "rebates_owed": w.rebates_owed, "rebates_paid": w.rebates_paid,
                "liabilities_accrued": w.liabilities_accrued, "liabilities_paid": w.liabilities_paid,
                "liabilities_outstanding": sum(l["amount"] for l in w.omega_liabilities),
                # the part older than a period — what Ω pays before it advances (1.6.0 §2.2)
                "liabilities_old": sum(l["amount"] for l in w.omega_liabilities if w.t - l["t"] >= w.p.period_ticks),
                "open_late": w.open_late(),
                # 2.2.0: the rebate from income — claims, paid, forgone and the forgone share (the run), the pool and this period's claims
                "pool_on": w.pool_on, "pool": w.omega_pool, "claims_period": w.period["claims_total"], "claims_n_period": len(w.period["claims"]),
                "rebates_forgone": w.rebates_forgone,
                "forgone_share": (w.rebates_forgone / (w.rebates_paid + w.rebates_forgone)) if (w.rebates_paid + w.rebates_forgone) > 1e-9 else 0.0,
                "omega_retained_period": (w.periods[-1].get("omega_retained_period", 0.0) if w.periods else 0.0),
                "forgone_share_period": (w.periods[-1].get("forgone_share", 0.0) if w.periods else 0.0)}

    # -- the orchestrator's planted work and its clock (1.2.0 §2.1–§2.3) -----------
    def create_plant(self, truth: bool, B: float) -> str:
        """A case whose fulfillment the orchestrator knows by construction, funded by Ω."""
        return self._pub(self._w.create_plant(truth, B))

    def post_plant(self, truth: bool) -> str:
        """2.6.0 §2.1: the orchestrator posts a plant as a root under a fresh name; the market takes it from there."""
        return self._pub(self._w.post_plant(truth))

    def submit_plant(self, cid: str):
        """2.6.0 §7.6: the orchestrator's instrument submits for the plant actor at its drawn tick, in the members' submission step."""
        self._w.submit_plant(self._eng(cid))

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
                # 2.6.0: the plant's life — live counters, the orchestrator's instrument (the published counts are the periods' records)
                "plants_posted": w.plants_posted, "plants_awarded": w.plants_awarded, "plants_at_floor": w.plants_awarded_at_floor,
                "plant_bids_lost": w.plant_bids_lost, "plant_market_ticks": w.plant_market_ticks, "plant_names": len(w.plant_names),
                "plants_refused_capacity": w.plants_refused_capacity, "plants_refused_credit": w.plants_refused_credit,
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
        self._w.submit(self._eng(cid))

    def resubmit(self, cid: str):
        self._w.resubmit(self._eng(cid))

    def spend(self, actor: str, real_cost: float, cid: Optional[str] = None) -> float:
        return self._w.spend(actor, real_cost, self._eng(cid))

    def respond(self, cid: str, action: str, d: Optional[str] = None):
        self._w.respond(self._eng(cid), action, d)

    def post_nested(self, parent: str, beta: float) -> str:
        return self._pub(self._w.post_nested(self._eng(parent), beta))

    def judge_nested(self, cid: str, verdict: str):
        self._w.judge_nested(self._eng(cid), verdict)

    def cancel_nested(self, cid: str):
        self._w.cancel_nested(self._eng(cid))

    def volunteer(self, actor: str, flag: bool = True):
        self._w.volunteer(actor, flag)

    # -- reviewer operations (§7, §8, §14) ---------------------------------------
    def observe(self, reviewer: str, rid: str) -> ReviewView:
        v = copy.copy(self._w.observe(reviewer, rid))
        v.case_id = self._pub(v.case_id)
        return v

    def complete_review(self, rid: str, verdict: str, cost: float, objection: Optional[str] = None):
        self._w.complete_review(rid, verdict, cost, objection)

    # -- human operations (§15) ---------------------------------------------------
    def override(self, cid: str, human: str, outcome: str, objection: Optional[str] = None):
        self._w.override(self._eng(cid), human, outcome, objection)

    # -- reads --------------------------------------------------------------------
    def case(self, cid: str):
        return self._pub_case(self._w.cases[self._eng(cid)])

    def review(self, rid: str):
        return self._pub_review(self._w.reviews[rid])

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
                "claims_outstanding": sum(cl.amount for cl in self._w.omega_claims),
                # 2.0.0: the price level and the deficit
                "P_t": self._w.price_level(), "deficit": self._w.deficit, "created": self._w.deficit_created,
                "retired": self._w.deficit_retired}

    def events_since(self, n: int) -> list:
        """The ledger's event copy from position n on — the public record of money movements (case ids on the public surface)."""
        out = []
        for e in self._w.ledger.events[n:]:
            k = copy.copy(e)
            k.case = self._pub(e.case)
            out.append(k)
        return out

    def n_events(self) -> int:
        return len(self._w.ledger.events)

    def head(self) -> str:
        return self._w.history.head

    def fingerprint(self) -> dict:
        from drivers.results import fingerprint
        return fingerprint(self._w)

    def close(self):
        self._w.close()
