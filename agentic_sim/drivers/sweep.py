"""The rerun of strategy run 1 under 1.1.0 (design revision 1, §8 step 2), and the shape of any
later sweep over the stamping run: a grid of cells × seeds, each cell a `drivers.stamping` run with
its own results directory, plus one summary directory with every run's final row and the per-cell
means and spreads.

    python3 -m drivers.sweep --seeds 20 --on-duty 4 8 --fee 2 4 --stampers 0.5 0.9

The X = 4, f = 2 cell is the like-for-like comparison with run 1 (same actors, ticks, tasks, β, b,
accuracy, p_start, G^V, ruling accuracy; only the fee rule changed). The other cells separate the
fee level and the reviewer-capacity ceiling from the rule. Means are over seeds; "stampers richer"
counts the seeds in which the stamper population ended with more wealth per actor.
"""
from __future__ import annotations
import argparse
import json
import os
import statistics
import sys
import time

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from sim import Params                                              # noqa: E402
from drivers import stamping                                        # noqa: E402
from drivers.results import RunRecorder, RESULTS                    # noqa: E402

KEYS = ["careful_wealth", "stamper_wealth", "careful_fees", "stamper_fees", "careful_fee_fixed", "stamper_fee_fixed",
        "careful_fee_haircut", "stamper_fee_haircut", "careful_delivery", "stamper_delivery", "careful_costs",
        "careful_reimbursed", "careful_bonds_forfeited", "stamper_bonds_forfeited", "careful_awards", "stamper_awards",
        "careful_reviews", "stamper_reviews", "careful_overturned", "stamper_overturned", "careful_rho", "stamper_rho",
        "careful_p_audit", "stamper_p_audit", "posted", "vested", "final_n", "false_approvals", "false_rejections",
        "audits_rolled", "audits_assigned", "audit_unassignable_ticks", "challenges", "rulings",
        "reviews_unassignable_ticks", "awards_unfilled_ticks", "underfunded_careful_reviews",
        "omega_unrecovered_advances", "claims_outstanding", "allowance_refunded", "pot_refunded",
        "grade_procedural_n", "grade_procedural_acc", "grade_protocol-default_n", "grade_protocol-default_acc", "omega"]


def cell_name(split, fee, X):
    return f"s{split:g}-f{fee:g}-X{X}"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--seeds", type=int, default=20)
    ap.add_argument("--seed-from", type=int, default=1)
    ap.add_argument("--on-duty", type=int, nargs="+", default=[4, 8])
    ap.add_argument("--fee", type=float, nargs="+", default=[2.0, 4.0])
    ap.add_argument("--stampers", type=float, nargs="+", default=[0.5, 0.9])
    ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("--actors", type=int, default=20)
    ap.add_argument("--log-every", type=int, default=100)
    ap.add_argument("--name", default="stamping-rerun-1.1.0")
    ap.add_argument("--phi-f-per-fee", type=float, default=2.5,
                    help="φ^F = this × f for each fee level (§4.3 default: f·(w_ordinary + w_audit) = 2.5 f); "
                         "0 keeps the stamping driver's own default (5) at every fee level")
    ap.add_argument("--extra", nargs=argparse.REMAINDER, default=[], help="passed through to drivers.stamping")
    a = ap.parse_args(argv)

    cells = [(s, f, X) for s in a.stampers for f in a.fee for X in a.on_duty]
    seeds = list(range(a.seed_from, a.seed_from + a.seeds))
    rec = RunRecorder(a.name, kind="sweep summary — strategy run 1 rerun under 1.1.0 with only the fee rule changed (§8 step 2)",
                      params=Params(),
                      declared={"cells": [cell_name(*c) for c in cells], "seeds": seeds, "ticks": a.ticks, "actors": a.actors,
                                "per_run": "drivers.stamping at its defaults except --stampers, --fee, --on-duty, --seed, "
                                           "and --phi-f = phi_f_per_fee × fee",
                                "phi_f_per_fee": a.phi_f_per_fee,
                                "extra_args": a.extra, "comparison": "the s0.5/s0.9, f2, X4 cells against run 1 (v1.0.1, 5 seeds)"})
    runs, finals = [], {}
    t0 = time.time()
    for (split, fee, X) in cells:
        for seed in seeds:
            name = f"rerun110-{cell_name(split, fee, X)}-seed{seed}"
            argv_run = ["--actors", str(a.actors), "--ticks", str(a.ticks), "--stampers", str(split), "--fee", str(fee),
                        "--on-duty", str(X), "--seed", str(seed), "--log-every", str(a.log_every), "--name", name] + a.extra
            if a.phi_f_per_fee > 0:
                argv_run += ["--phi-f", str(a.phi_f_per_fee * fee)]       # the pot sized for one review and one audit
            before = set(os.listdir(os.path.join(RESULTS, "runs")))
            rc = stamping.main(argv_run)
            new = [d for d in os.listdir(os.path.join(RESULTS, "runs")) if d not in before and d.endswith(name)]
            run_dir = os.path.join(RESULTS, "runs", new[0])
            with open(os.path.join(run_dir, "manifest.json")) as f:
                m = json.load(f)
            final = m["final"]
            row = {"cell": cell_name(split, fee, X), "stampers": split, "fee": fee, "on_duty": X, "seed": seed,
                   "run_id": m["run_id"], "status": m["status"], "head": m["head"]}
            row.update({k: final.get(k, "") for k in KEYS})
            rec.tick(row)
            runs.append({"run_id": m["run_id"], "status": m["status"], "rc": rc})
            finals.setdefault(cell_name(split, fee, X), []).append(final)
    # per-cell statistics
    summary = {}
    for cell, rows in finals.items():
        st = {}
        for k in KEYS:
            vals = [r[k] for r in rows if isinstance(r.get(k), (int, float))]
            if vals:
                st[k] = {"mean": round(statistics.fmean(vals), 3),
                         "sd": round(statistics.stdev(vals), 3) if len(vals) > 1 else 0.0,
                         "min": round(min(vals), 3), "max": round(max(vals), 3)}
        diffs = [r["stamper_wealth"] - r["careful_wealth"] for r in rows]
        st["stamper_minus_careful_wealth"] = {"mean": round(statistics.fmean(diffs), 3),
                                              "sd": round(statistics.stdev(diffs), 3) if len(diffs) > 1 else 0.0,
                                              "se": round(statistics.stdev(diffs) / len(diffs) ** 0.5, 3) if len(diffs) > 1 else 0.0}
        st["stampers_richer_in"] = f"{sum(1 for d in diffs if d > 0)} of {len(diffs)}"
        per_review = [((r["stamper_fees"] - r["stamper_costs"] if "stamper_costs" in r else r["stamper_fees"]) / max(1, r["stamper_reviews"]))
                      - ((r["careful_fees"] + r["careful_reimbursed"] - r["careful_costs"]) / max(1, r["careful_reviews"])) for r in rows]
        st["stamper_minus_careful_net_fee_per_review"] = {"mean": round(statistics.fmean(per_review), 3),
                                                          "sd": round(statistics.stdev(per_review), 3) if len(per_review) > 1 else 0.0}
        summary[cell] = st
    ok = all(r["status"] == "completed" for r in runs)
    lines = [f"# {a.name}: {len(runs)} runs, {len(cells)} cells × {len(seeds)} seeds, {a.actors} actors × {a.ticks} ticks", ""]
    lines.append("| cell | careful wealth | stamper wealth | stamper − careful (se) | stampers richer | net fee/review Δ | false approvals | final N | audits assigned/rolled | reviews unassignable ticks | Ω unrecovered |")
    lines.append("|---|---|---|---|---|---|---|---|---|---|---|")
    for cell, st in summary.items():
        g = lambda k: st[k]["mean"]
        lines.append(f"| {cell} | {g('careful_wealth'):.0f} ± {st['careful_wealth']['sd']:.0f} | {g('stamper_wealth'):.0f} ± {st['stamper_wealth']['sd']:.0f} "
                     f"| {st['stamper_minus_careful_wealth']['mean']:+.0f} ({st['stamper_minus_careful_wealth']['se']:.0f}) | {st['stampers_richer_in']} "
                     f"| {st['stamper_minus_careful_net_fee_per_review']['mean']:+.2f} | {g('false_approvals'):.0f} | {g('final_n'):.0f} "
                     f"| {g('audits_assigned'):.0f}/{g('audits_rolled'):.0f} | {g('reviews_unassignable_ticks'):.0f} | {g('omega_unrecovered_advances'):.1f} |")
    with open(os.path.join(rec.dir, "summary.md"), "w") as f:
        f.write("\n".join(lines) + "\n")
    out = rec.finish(fp={"head": "sweep summary: each run's head is in metrics.csv and its own directory", "runs": len(runs)},
                     status="completed" if ok else "FAILED", runs=runs, summary=summary,
                     elapsed_total_s=round(time.time() - t0, 1))
    print("\n".join(lines))
    print(f"summary in {os.path.relpath(out)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
