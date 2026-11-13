"""Addendum 10's J3.3 (November 13, 2026; notes §111): whether a skipper is ahead until it is first caught — for the returning operator's first name and for the
claimer that never leaves, the tick of the first suspension, its wallet and its benefit by that tick, and the careful slot's wallet at the same tick on the same
seed; from §110's returner worlds run again whole with the trace (stress/returner2/ at ffd23d851: `learner_trace_json` — [t, the lifetime real wealth as the
measure reads it, the private benefit to then] at each decision's observation — and `susp_ticks` in the per-slot export). The wallet at a tick is the
lifetime read at the latest observation at or before it, less the benefit to then. Checks every figure of record against stress/returner/.  Usage: returner_trace_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def at(trace, t):                                                       # the latest observation at or before tick t: (lifetime real, benefit to then)
    best = None
    for row in trace:
        if row[0] <= t: best = row
        else: break
    return (best[1], best[2]) if best else (0.0, 0.0)
L = ["# J3.3 — is a skipper ahead until it is first caught? The first name's wallet and benefit at its first suspension against the careful slot's wallet at the same tick, same seed\n",
     "Seeds 21–40; the operator's first name (a genesis member, no loan) and the claimer that never leaves; the careful on the same slot. `ahead` counts the seeds where wallet + benefit at the first suspension's tick exceeds the careful's wallet at that tick; "
     "`by wallet alone` the seeds where the wallet alone does. Every figure of record (the lifetimes, the gaps) identical in the re-run (checked below).\n",
     "| world | policy | first suspension at tick (mean; min–max) | its wallet by then (real) | its benefit by then | wallet + benefit | the careful's wallet at that tick | **(wallet + benefit) − careful** | ahead (seeds) | by wallet alone | never suspended |",
     "|---|---|---|---|---|---|---|---|---|---|---|"]
checks = []
for k, kn in (("pa10", "the pin"), ("arm4", "arm 4")):
    for pop, pn in (("careful", "a careful population"), ("hand", "Q1's 60/40 population")):
        j = json.load(open(f"{R}/returner2/{k}-{pop}/eval.json")); j0 = json.load(open(f"{R}/returner/{k}-{pop}/eval.json"))
        for pol in ("claimreturner", "claimer", "careful"):
            a = [f(e, "lifetime_real_wealth") for e in j["episodes"][pol]]; b = [f(e, "lifetime_real_wealth") for e in j0["episodes"][pol]]
            checks.append((kn, pn, pol, float(np.nanmax(np.abs(np.array(a) - np.array(b))))))
        C = {int(e["seed"]): json.loads(e["learner_trace_json"]) for e in j["episodes"]["careful"]}
        for pol in ("claimreturner", "claimer"):
            s0s, wal, ben, car, never = [], [], [], [], 0
            for e in j["episodes"][pol]:
                S = json.loads(e["learner_slots_json"]); first = [v for v in S.values() if v["t_in"] == 0]
                if not first or not first[0]["susp_ticks"]: never += 1; continue
                s0 = first[0]["susp_ticks"][0]; tr = json.loads(e["learner_trace_json"])
                lw, pb = at(tr, s0); cw, _ = at(C[int(e["seed"])], s0)
                s0s.append(s0); wal.append(lw - pb); ben.append(pb); car.append(cw)
            wal, ben, car = np.array(wal), np.array(ben), np.array(car); d = wal + ben - car
            L.append(f"| {kn}, {pn} | {pol} | {np.mean(s0s):.0f}; {min(s0s)}–{max(s0s)} | {wal.mean():.0f} ± {mse(wal)[1]:.0f} | {ben.mean():.0f} ± {mse(ben)[1]:.0f} | {(wal + ben).mean():.0f} | {car.mean():.0f} ± {mse(car)[1]:.0f} | "
                     f"**{d.mean():+.0f} ± {mse(d)[1]:.0f}** | {(d > 0).sum()} of {len(d)} | {((wal - car) > 0).sum()} of {len(d)} | {never} |")
L.append("\n**The re-run against the record** (the largest difference in any policy's lifetime on any seed): " + "; ".join(f"{kn}, {pn}, {pol}: {d:.2e}" for kn, pn, pol, d in checks) + ".")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
