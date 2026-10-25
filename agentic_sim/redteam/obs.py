"""The learner's observation: what a member observes — the public view, its own standing and history, the assignment's ReviewView,
and what it saw for sale as a free member (the seen set). Every field is named, so an ablation is "drop these names"; nothing per
other actor by name, no engine field, never the truth. `hide` lists fields zeroed for a question (Q1: own audit odds hidden). Since the
re-arrival ruling (after run 22) a decision has a kind: a review (the assignment's fields filled) or a period boundary (`decision_boundary`
1, no assignment — 0/2 stay, 1 leave and return under a fresh name); `n_fields` trims the vector for a model trained before the field.
Q3 (the learned deliverer): a second vector of the same width, `OBS_FIELDS_WORK` — the market, the dial and own standing as the reviewer's
(the first 31 fields), then the case the learner is about to submit (its price, ceiling, bond, nesting, the wait before its award, the work
ticks, the slack to the deadline, the fee) and its own record as a deliverer (deliveries settled, its bad deliveries approved and caught, its
guarantees forfeited, its live awards); `build_obs_work` fills it; the boundary decision reads the shared part with the flag, as the reviewer's does."""
from __future__ import annotations
import numpy as np

OBS_FIELDS = [
    # the market, from the public view
    "P_t_rel", "B_bar_rel", "state_price_rel", "members_total", "members_free", "probationers", "available_roots",
    "below_market_waiting", "refused_waiting", "state_share_period", "time_to_membership", "on_time_share", "forgone_share_period",
    # the dial's public state and the period's position
    "dial_m", "dial_pi", "period_pos",
    # own standing and history
    "own_wealth_real", "own_unlocked", "own_rho", "own_kappa", "own_p_eff", "own_member", "own_probationer", "own_suspended",
    "own_ticks_since_admission", "own_reviews", "own_overturned", "own_plant_bad_n", "own_plant_good_n", "own_plant_failures", "own_awards",
    # the assignment (the ReviewView — no actor, no role)
    "rv_gap", "rv_cap_rel", "rv_bond_rel", "rv_is_nested", "rv_q_fulfillment", "rv_q_appeal", "rv_q_dispute", "rv_responses_available", "rv_resumed",
    # the seen set (what this reader saw available as a free member) and its own bid on the case
    "seen_before", "seen_ticks_since", "seen_beta_rel", "my_bid_lost",
    # the decision's kind: 0 a review assignment, 1 a period boundary (stay or leave)
    "decision_boundary",
]
OBS_DIM = len(OBS_FIELDS)
IDX = {k: i for i, k in enumerate(OBS_FIELDS)}
N_SHARED = IDX["rv_gap"]                                   # the market, the dial and own standing — common to both roles' vectors
OBS_FIELDS_WORK = OBS_FIELDS[:N_SHARED] + [
    # Q3 — the case about to be submitted (the learner's own case: the record's fields about one's own cases are within the convention)
    "wk_price_rel", "wk_ceiling_rel", "wk_bond_rel", "wk_is_nested", "wk_wait_ticks", "wk_tau", "wk_slack", "wk_fee_rel", "wk_price_over_market",
    # own record as a deliverer (own outcomes: the brief's "its awards, verdicts, audits received, outcomes")
    "wk_own_settled", "wk_own_bad_approved", "wk_own_bad_caught", "wk_own_forfeited",
    "decision_boundary",
]
assert len(OBS_FIELDS_WORK) == OBS_DIM
IDX_WORK = {k: i for i, k in enumerate(OBS_FIELDS_WORK)}
OBS_FIELDS_PARENT = OBS_FIELDS[:N_SHARED] + [
    # Q5 — the learned parent: the decision's kind (one of three; a boundary is the 45th), the root it holds, its own cost against the child's expected
    # bid and the overhead (the rule's terms), the child's case once awarded, and its own record as a parent
    "pr_kind_delegate", "pr_kind_judge", "pr_kind_cancel", "pr_root_price_rel", "pr_root_slack", "pr_own_cost_rel", "pr_child_bid_exp_rel", "pr_overhead_rel",
    "pr_child_price_rel", "pr_child_bond_rel", "pr_child_since_award", "pr_child_slack", "pr_own_children",
    "decision_boundary",
]
assert len(OBS_FIELDS_PARENT) == OBS_DIM
IDX_PARENT = {k: i for i, k in enumerate(OBS_FIELDS_PARENT)}
OBS_FIELDS_BID = OBS_FIELDS[:N_SHARED] + [
    # Q6 — the learned bidder: its own cost and the ratchet's state (its margin, the bid the rule would make), what is for sale (the best ceiling it
    # fits under, the roots it could bid on, the free rivals), the market price over its cost, its idle ticks and the period's remainder, its own record as a bidder
    "bd_own_cost_rel", "bd_own_margin", "bd_ratchet_bid_rel", "bd_best_ceiling_rel", "bd_roots_affordable", "bd_free_rivals", "bd_price_over_cost",
    "bd_idle_ticks", "bd_ticks_to_boundary", "bd_own_bid_awards", "bd_own_bids_lost", "bd_own_held_real", "bd_last_won",
    "decision_boundary",
]
assert len(OBS_FIELDS_BID) == OBS_DIM
IDX_BID = {k: i for i, k in enumerate(OBS_FIELDS_BID)}
N_MARKET = IDX["own_wealth_real"]                          # the market and the dial alone — what a requester shares with a member's vector
OBS_FIELDS_REQ = OBS_FIELDS[:N_MARKET] + [
    # Q7 — the learned requester (not an actor: no standing, no reviewing): its wallet, its requests open and waiting, the three ceilings it chooses
    # among with their affordability, and its own record as a requester (the tasks received, paid for nothing, the credits spent, the wait, the price paid)
    "rq_wallet_real", "rq_unlocked_real", "rq_open_requests", "rq_open_room", "rq_waiting", "rq_waiting_age_max",
    "rq_market_ceiling_rel", "rq_patient_ceiling_rel", "rq_floor_ceiling_rel", "rq_all_in_market_rel", "rq_affordable_market", "rq_affordable_patient", "rq_affordable_floor",
    "rq_posted", "rq_tasks_received", "rq_paid_unfulfilled", "rq_final_n", "rq_free_fulfilled", "rq_state_deliveries", "rq_spent_real", "rq_tasks_per_1000",
    "rq_wait_mean", "rq_price_paid_rel", "rq_disputes_filed", "rq_disputes_won", "rq_raised", "rq_last_mode", "rq_ticks_to_boundary",
    "decision_boundary",
]
assert len(OBS_FIELDS_REQ) == OBS_DIM
IDX_REQ = {k: i for i, k in enumerate(OBS_FIELDS_REQ)}
FIELDS_BY_ROLE = {"reviewer": OBS_FIELDS, "deliverer": OBS_FIELDS_WORK, "child": OBS_FIELDS_WORK, "parent": OBS_FIELDS_PARENT, "bidder": OBS_FIELDS_BID, "requester": OBS_FIELDS_REQ}


def _market(run, put):
    """The market from the public view, the dial's state and the period's position — what every role's vector opens with."""
    w = run.w
    mk, dl, sv = w.market(), w.dial(), w.service()
    P0, Pt = mk["P0"], mk["P_t"] or mk["P0"]
    per = dl["period"]
    ttm = mk.get("time_to_membership") or 0.0
    put("P_t_rel", Pt / P0); put("B_bar_rel", (mk["B_bar"] or Pt) / P0); put("state_price_rel", mk["state_price"] / P0)
    put("members_total", mk["members_total"] / 20.0); put("members_free", mk["members_free"] / 20.0); put("probationers", mk["probationers"] / 20.0)
    put("available_roots", mk["available_roots"] / 20.0); put("below_market_waiting", mk["below_market_waiting"] / 20.0)
    put("refused_waiting", (mk["refused_waiting"]["capacity"] + mk["refused_waiting"]["credit"]) / 20.0)
    put("state_share_period", mk["state_share_period"]); put("time_to_membership", ttm / 500.0)
    put("on_time_share", sv["on_time"] / max(1, sv["on_time"] + sv["late"])); put("forgone_share_period", sv.get("forgone_share_period", 0.0))
    put("dial_m", dl["m"]); put("dial_pi", dl["pi"]); put("period_pos", (w.t - per["start"]) / max(1, w.params.period_ticks))
    return mk, dl, P0, Pt, P0 / Pt


def _shared(run, actor: str, o, put, idx):
    """The fields common to both roles: the market from the public view, the dial's state and the period's position, own standing and history."""
    w = run.w
    reviewer = actor                                      # the fields below were written for the reviewer; they read any member's own standing
    mk, dl, sv = w.market(), w.dial(), w.service()
    P0, Pt = mk["P0"], mk["P_t"] or mk["P0"]
    real = P0 / Pt
    ac = w.actor(actor)
    tally = run.tally[actor]
    per = dl["period"]
    ttm = mk.get("time_to_membership") or 0.0
    put("P_t_rel", Pt / P0); put("B_bar_rel", (mk["B_bar"] or Pt) / P0); put("state_price_rel", mk["state_price"] / P0)
    put("members_total", mk["members_total"] / 20.0); put("members_free", mk["members_free"] / 20.0); put("probationers", mk["probationers"] / 20.0)
    put("available_roots", mk["available_roots"] / 20.0); put("below_market_waiting", mk["below_market_waiting"] / 20.0)
    put("refused_waiting", (mk["refused_waiting"]["capacity"] + mk["refused_waiting"]["credit"]) / 20.0)
    put("state_share_period", mk["state_share_period"]); put("time_to_membership", ttm / 500.0)
    put("on_time_share", sv["on_time"] / max(1, sv["on_time"] + sv["late"])); put("forgone_share_period", sv.get("forgone_share_period", 0.0))
    put("dial_m", dl["m"]); put("dial_pi", dl["pi"]); put("period_pos", (w.t - per["start"]) / max(1, w.params.period_ticks))
    put("own_wealth_real", w.wealth(reviewer) * real / 1000.0); put("own_unlocked", w.unlocked(reviewer) * real / 1000.0)
    put("own_rho", ac.rho); put("own_kappa", ac.kappa / 50.0); put("own_p_eff", w.p_effective(reviewer))
    put("own_member", 1.0 if ac.is_member else 0.0); put("own_probationer", 1.0 if ac.probation else 0.0)
    put("own_suspended", 1.0 if ac.suspended_until is not None else 0.0)
    since = (w.t - ac.admitted_at) if getattr(ac, "admitted_at", None) is not None else w.t
    put("own_ticks_since_admission", since / 1000.0)
    put("own_reviews", tally.reviews / 100.0); put("own_overturned", tally.overturned / 10.0)
    put("own_plant_bad_n", len(ac.plant_bad) / 10.0); put("own_plant_good_n", len(ac.plant_good) / 10.0)
    put("own_plant_failures", tally.plant_failures / 10.0); put("own_awards", tally.awards / 100.0)
    return mk, P0, Pt, real


def build_obs(run, reviewer: str, view, r, hide=(), n_fields=None) -> np.ndarray:
    o = np.zeros(OBS_DIM, dtype=np.float32)
    def put(k, v):
        o[IDX[k]] = 0.0 if (v is None or k in hide) else float(v)
    mk, P0, Pt, real = _shared(run, reviewer, o, put, IDX)
    w = run.w
    if view is None:                                      # a period-boundary decision: no assignment
        put("decision_boundary", 1.0)
        return o if n_fields is None else o[:n_fields]
    put("rv_gap", (r.t_assign - view.t_submit) / 10.0 if view.t_submit is not None else 0.0)
    put("rv_cap_rel", view.cap / P0); put("rv_bond_rel", view.bond / P0); put("rv_is_nested", 1.0 if view.is_nested else 0.0)
    put("rv_q_fulfillment", 1.0 if view.question == "fulfillment" else 0.0); put("rv_q_appeal", 1.0 if view.question == "appeal" else 0.0)
    put("rv_q_dispute", 1.0 if view.question == "dispute" else 0.0)
    put("rv_responses_available", 1.0 if view.responses_available else 0.0); put("rv_resumed", 1.0 if view.resumed else 0.0)
    first = run.seen.get((reviewer, view.case_id))
    put("seen_before", 1.0 if first is not None else 0.0)
    put("seen_ticks_since", ((w.t - first[0]) / 10.0) if first is not None else 0.0)
    put("seen_beta_rel", (first[1] / P0) if first is not None else 0.0)
    put("my_bid_lost", 1.0 if (reviewer, view.case_id) in run.lost_bid else 0.0)
    return o if n_fields is None else o[:n_fields]


def build_obs_work(run, actor: str, c, hide=(), n_fields=None) -> np.ndarray:
    """Q3: the learned deliverer's observation at a submission — the shared fields, then its own case and its own record as a deliverer.
    `c` is the case as the view returns it (the learner's own); None is a period-boundary decision."""
    o = np.zeros(OBS_DIM, dtype=np.float32)
    def put(k, v):
        o[IDX_WORK[k]] = 0.0 if (v is None or k in hide) else float(v)
    mk, P0, Pt, real = _shared(run, actor, o, put, IDX_WORK)
    w = run.w
    if c is None:
        put("decision_boundary", 1.0)
        return o if n_fields is None else o[:n_fields]
    put("wk_price_rel", c.B / P0); put("wk_ceiling_rel", c.beta / P0); put("wk_bond_rel", (c.G_award if c.G_award is not None else c.G) / P0)
    put("wk_is_nested", 0.0 if c.is_root else 1.0)
    put("wk_wait_ticks", ((c.t_award - c.t_post) / 10.0) if c.t_award is not None else 0.0); put("wk_tau", c.tau / 10.0)
    put("wk_slack", ((c.deadline - w.t) / 10.0) if c.deadline is not None else 0.0)
    put("wk_fee_rel", c.omega / P0)                    # the case's fee as set at its posting
    put("wk_price_over_market", c.B / (mk["B_bar"] or Pt))
    cc = run.c
    put("wk_own_settled", (cc["learner_bad_approved"] + cc["learner_bad_caught"] + cc["learner_good_vested"] + cc["learner_good_final_n"]) / 20.0)
    put("wk_own_bad_approved", cc["learner_bad_approved"] / 10.0); put("wk_own_bad_caught", cc["learner_bad_caught"] / 10.0)
    put("wk_own_forfeited", cc["learner_forfeited"] * real / 100.0)
    return o if n_fields is None else o[:n_fields]


def build_obs_parent(run, parent: str, kind, root, child, hide=(), n_fields=None) -> np.ndarray:
    """Q5: the learned parent's observation — at a delegate decision (the root just awarded; `child` None), a judge decision (the child
    submitted) or a cancel decision (the child committed, not yet submitted); `kind` None with `root` None is a period-boundary decision."""
    o = np.zeros(OBS_DIM, dtype=np.float32)
    def put(k, v):
        o[IDX_PARENT[k]] = 0.0 if (v is None or k in hide) else float(v)
    mk, P0, Pt, real = _shared(run, parent, o, put, IDX_PARENT)
    w = run.w
    if kind is None:
        put("decision_boundary", 1.0)
        return o if n_fields is None else o[:n_fields]
    put({"delegate": "pr_kind_delegate", "judge": "pr_kind_judge", "cancel": "pr_kind_cancel"}[kind], 1.0)
    put("pr_root_price_rel", root.B / P0); put("pr_root_slack", ((root.deadline - w.t) / 10.0) if root.deadline is not None else 0.0)
    cost = run.cost_now(parent); bid = run.expected_child_bid()
    put("pr_own_cost_rel", cost / P0); put("pr_child_bid_exp_rel", bid / P0); put("pr_overhead_rel", run.nested_overhead(bid) / P0)
    if child is not None:
        put("pr_child_price_rel", child.B / P0); put("pr_child_bond_rel", (child.G_award if child.G_award is not None else child.G) / P0)
        put("pr_child_since_award", ((w.t - child.t_award) / 10.0) if child.t_award is not None else 0.0)
        put("pr_child_slack", ((child.deadline - w.t) / 10.0) if child.deadline is not None else 0.0)
    put("pr_own_children", run.parent_delegated.get(parent, 0) / 10.0)
    return o if n_fields is None else o[:n_fields]


def build_obs_bid(run, actor: str, roots, hide=(), n_fields=None) -> np.ndarray:
    """Q6: the learned bidder's observation at the tick's bid decision — the shared fields, then its own cost and margin, what is for sale and its own
    record as a bidder; `roots` None is a period-boundary decision."""
    o = np.zeros(OBS_DIM, dtype=np.float32)
    def put(k, v):
        o[IDX_BID[k]] = 0.0 if (v is None or k in hide) else float(v)
    mk, P0, Pt, real = _shared(run, actor, o, put, IDX_BID)
    w = run.w
    if roots is None:
        put("decision_boundary", 1.0)
        return o if n_fields is None else o[:n_fields]
    cost = run.cost_now(actor); m = run.margin.get(actor, 0.0)
    put("bd_own_cost_rel", cost / P0); put("bd_own_margin", m); put("bd_ratchet_bid_rel", cost * (1.0 + m) / P0)
    put("bd_best_ceiling_rel", max(c.beta for c in roots) / P0); put("bd_roots_affordable", len(roots) / 10.0)
    put("bd_free_rivals", (len(run.free_members()) - 1) / 20.0); put("bd_price_over_cost", (mk["B_bar"] or Pt) / cost)
    put("bd_idle_ticks", run.idle.get(actor, 0) / 10.0)
    per = w.dial()["period"]
    put("bd_ticks_to_boundary", (per["start"] + w.params.period_ticks - w.t) / max(1, w.params.period_ticks))
    put("bd_own_bid_awards", run.bid_awards_of.get(actor, 0) / 20.0); put("bd_own_bids_lost", run.bids_lost_of.get(actor, 0) / 20.0)   # the slot's own record (the population: each its own)
    put("bd_own_held_real", w.unlocked(actor) * real / 1000.0)
    lw = run.last_won_of.get(actor)
    put("bd_last_won", 1.0 if (lw is not None and lw >= w.t - 1) else 0.0)
    return o if n_fields is None else o[:n_fields]


def build_obs_req(run, requester: str, cands, hide=(), n_fields=None) -> np.ndarray:
    """Q7: the learned requester's observation at a posting decision — the market and the dial, then its wallet, its requests open and waiting, the
    three ceilings it chooses among (the market rule's, patient, the floor) with their affordability, and its own record as a requester.
    A requester is not an actor: no standing fields, and no boundary decision (`decision_boundary` stays 0)."""
    o = np.zeros(OBS_DIM, dtype=np.float32)
    def put(k, v):
        o[IDX_REQ[k]] = 0.0 if (v is None or k in hide) else float(v)
    mk, dl, P0, Pt, real = _market(run, put)
    w = run.w
    put("rq_wallet_real", w.wealth(requester) * real / 1000.0); put("rq_unlocked_real", w.unlocked(requester) * real / 1000.0)
    own = [cid for cid in run.active if run.owner.get(cid) == requester]
    waiting = [cid for cid in own if w.case(cid).state == "AVAILABLE"]
    k_open = run.a.k_open * 3 if requester in run.small else run.a.k_open
    put("rq_open_requests", len(own) / 10.0); put("rq_open_room", ((k_open - len(own)) / 10.0) if k_open > 0 else 1.0)
    put("rq_waiting", len(waiting) / 10.0); put("rq_waiting_age_max", (max((w.t - w.case(cid).t_post) for cid in waiting) / 10.0) if waiting else 0.0)
    b = cands["beta"]; aff = cands["affordable"]
    put("rq_market_ceiling_rel", b[0] / P0); put("rq_patient_ceiling_rel", b[1] / P0); put("rq_floor_ceiling_rel", b[2] / P0); put("rq_all_in_market_rel", cands["all_in"][0] / P0)
    put("rq_affordable_market", 1.0 if aff[0] else 0.0); put("rq_affordable_patient", 1.0 if aff[1] else 0.0); put("rq_affordable_floor", 1.0 if aff[2] else 0.0)
    cc = run.c
    put("rq_posted", cc["req_posted"] / 100.0); put("rq_tasks_received", cc["req_tasks_received"] / 100.0); put("rq_paid_unfulfilled", cc["req_paid_unfulfilled"] / 10.0)
    put("rq_final_n", cc["req_final_n"] / 10.0); put("rq_free_fulfilled", cc["req_free_fulfilled"] / 10.0); put("rq_state_deliveries", cc["req_state_deliveries"] / 10.0)
    spent = run.req_spent_real()
    put("rq_spent_real", spent / 1000.0); put("rq_tasks_per_1000", (cc["req_tasks_received"] / spent) if spent > 1e-9 else 0.0)
    put("rq_wait_mean", (cc["req_wait_sum"] / cc["req_awards"] / 10.0) if cc["req_awards"] else 0.0)
    put("rq_price_paid_rel", (cc["req_price_paid_sum"] / cc["req_awards"] / P0) if cc["req_awards"] else 0.0)
    put("rq_disputes_filed", cc["req_disputes_filed"] / 10.0); put("rq_disputes_won", cc["req_disputes_won"] / 10.0); put("rq_raised", cc["req_raised"] / 10.0)
    last = max(run.req_mode.items(), key=lambda kv: kv[0])[1] if run.req_mode else 0      # the case ids are minted in order; the latest posting's rule
    put("rq_last_mode", last / 2.0)
    per = dl["period"]
    put("rq_ticks_to_boundary", (per["start"] + w.params.period_ticks - w.t) / max(1, w.params.period_ticks))
    return o if n_fields is None else o[:n_fields]
