"""The learner's observation: what a member observes — the public view, its own standing and history, the assignment's ReviewView,
and what it saw for sale as a free member (the seen set). Every field is named, so an ablation is "drop these names"; nothing per
other actor by name, no engine field, never the truth. `hide` lists fields zeroed for a question (Q1: own audit odds hidden)."""
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
]
OBS_DIM = len(OBS_FIELDS)
IDX = {k: i for i, k in enumerate(OBS_FIELDS)}


def build_obs(run, reviewer: str, view, r, hide=()) -> np.ndarray:
    w = run.w
    mk, dl, sv = w.market(), w.dial(), w.service()
    P0, Pt = mk["P0"], mk["P_t"] or mk["P0"]
    real = P0 / Pt
    ac = w.actor(reviewer)
    tally = run.tally[reviewer]
    per = dl["period"]
    ttm = mk.get("time_to_membership") or 0.0
    o = np.zeros(OBS_DIM, dtype=np.float32)
    def put(k, v):
        o[IDX[k]] = 0.0 if (v is None or k in hide) else float(v)
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
    return o
