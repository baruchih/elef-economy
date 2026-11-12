"""The honest side of the stake's table (§106's addendum, addendum 8's H3.2; November 13, 2026): the careful population in each stake's cell
(payoff/honest/<cell>/eval.json, run_q --policies careful on seeds 21–30), the columns §106's addendum carried — the members' nominal surplus, the slots'
real lifetime, idle for bond, the underfunded careful reviews, the slots alive, the state's seats per real root and its share of the awards, the system's
overhead a vested task and the cost of truth, P_t and the customers' tasks per 1,000 — means over the ten seeds. Usage: honest_read.py OUT.md cell [cell ...]"""
import json, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress/payoff/honest"
def g(E, k):
    v = []
    for e in E:
        try: v.append(float(e[k]))
        except (KeyError, TypeError, ValueError): pass
    return float(np.mean(v)) if v else float("nan")
L = ["| cell (the careful population, ten seeds) | surplus (nominal) | the slots' real lifetime | idle for bond (ticks a run) | underfunded careful reviews | slots alive | the state's seats per real root; its share of the awards | overhead a task; cost of truth | P_t; tasks per 1,000 |", "|---|---|---|---|---|---|---|---|---|"]
for c in sys.argv[2:]:
    try: E = json.load(open(f"{R}/{c}/eval.json"))["episodes"]["careful"]
    except FileNotFoundError: L.append(f"| {c} | (pending) | | | | | | | |"); continue
    L.append(f"| {c} | {g(E,'pop_surplus_nominal'):,.0f} | {g(E,'learner_lifetime_real'):,.0f} | {g(E,'idle_for_bond_ticks'):.0f} | {g(E,'underfunded_careful_reviews'):.1f} | {g(E,'learner_pop_n'):.1f} | {g(E,'life_real_state_seats'):.2f}; {g(E,'state_share'):.3f} | {g(E,'sys_overhead_per_vested'):.1f}; {g(E,'cost_of_truth'):,.0f} | {g(E,'P_t'):.1f}; {g(E,'pop_tasks_per_1000'):.1f} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
