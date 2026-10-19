"""Sweeps of the stamping run: a set of cells × seeds, each cell a `drivers.stamping` run with its own
results directory, plus one summary directory with every run's final row and the per-cell means and
spreads. Everything a sweep writes goes under one study folder (`--root`), so a study is one directory.

    # the 1.1.0 rerun of strategy run 1 (design revision 1, §8 step 2): a full grid
    python3 -m drivers.sweep --root results/studies/1.1.0-stamping/rerun --name stamping-rerun-1.1.0 \\
        --grid stampers=0.5,0.9 fee=2,4 on-duty=4,8 --seeds 20

    # the default sweep (§8 step 3): one factor at a time around the defaults, at both splits
    python3 -m drivers.sweep --root results/studies/1.1.0-stamping/default-sweep --name default-sweep \\
        --grid stampers=0.5,0.9 --ofat band=0.05:0,0.2 p-floor=0.2:0.05,0.5 gv=5:10,20 --seeds 20

A factor is a `drivers.stamping` option. `--grid` factors are crossed in full; `--ofat` factors vary one
at a time from the stated baseline (`name=baseline:alt1,alt2`), the others held at their baseline, and
the all-baseline cell is run once. φ^F is sized with the fee (2.5 f, §4.3) unless --phi-f-per-fee 0.
Means are over seeds; "stampers richer" counts the seeds in which the stamper population ended with
more wealth per actor.
"""
from __future__ import annotations
import argparse
import itertools
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
        "appeals_filed", "appeals_unfunded", "appeals_won", "appeals_lost", "false_rejections_total",
        "false_rejections_appealed", "false_rejections_overturned", "true_rejections_appealed", "true_rejections_overturned",
        "disputes_filed", "disputes_refused", "disputes_won", "disputes_lost", "false_approvals_disputed",
        "false_approvals_overturned", "true_approvals_disputed", "true_approvals_overturned", "grade_human-explicit_n",
        "grade_human-explicit_acc", "duty_short_of_bond_ticks",
        "grade_procedural_n", "grade_procedural_acc", "grade_protocol-default_n", "grade_protocol-default_acc",
        "grade_plant_n", "grade_plant_acc", "omega", "omega_total", "omega_in_plants", "omega_net",
        # 1.2.0: the clock and the plant record
        "m", "pi", "X_t", "on_duty", "F_hat", "periods", "suspensions", "alarms", "eligibility_shortfall", "plant_shortfall",
        "plants_created", "plants_unfunded", "plants_bad", "plants_stood", "plants_failed", "plants_spent",
        "bad_plants_approved", "good_plants_rejected", "omega_plant_spend",
        "careful_plant_reviews", "stamper_plant_reviews", "careful_plant_failures", "stamper_plant_failures",
        "careful_a_hat", "stamper_a_hat", "careful_suspended", "stamper_suspended",
        "careful_duty_eligible", "stamper_duty_eligible", "careful_panel_eligible", "stamper_panel_eligible",
        "stamper_share", "disposition_switches", "careful_n", "stamper_n",
        # 1.3.0: membership and the fund
        "members_on_duty", "probationers_on_duty", "member_seats", "readmissions", "readmission_ticks_mean",
        "duty_fund", "fund_in", "fund_out", "awards_refused_members_only_ticks", "probation_false_approvals",
        "careful_members", "stamper_members", "careful_probationers", "stamper_probationers",
        "careful_fee_uplift", "stamper_fee_uplift", "careful_probation_reviews", "stamper_probation_reviews",
        "careful_probation_approvals", "stamper_probation_approvals",
        # 1.4.0: troops
        "audit_obligations", "troop_reviews", "troop_audits", "troop_deliveries", "troop_delivered_vested",
        "troop_delivered_final_n", "troop_false_approvals", "troops_active_reviews", "troops_active_deliveries",
        "troop_summons_reviews", "troop_summons_deliveries", "troop_shortfall_seats", "troop_shortfall_awards",
        "troop_held_ticks", "troop_ticks_reviews", "troop_ticks_deliveries", "held_market_audit_now",
        "held_market_audit_max_age", "fund_reserve", "advance_outstanding", "B_bar",
        # 1.5.0: the demand-sized reserve, the route-and-kind reading, the decliners
        "troop_demand", "troop_demand_refused", "demand_peak_refused", "pfa_route_upheld", "pfa_route_overturned",
        "pfa_route_other", "pfa_kind_troop", "pfa_kind_standing", "pfa_kind_lag", "pfa_kind_readmitted",
        "decliner_wealth", "careful_offering_wealth", "decliner_awards", "careful_offering_awards",
        # 1.6.0: the network rating, Ω's readings, the seats
        "on_time", "late", "on_time_share", "mean_lateness", "rebates_owed", "rebates_paid", "omega_liability",
        "liabilities_accrued", "open_late", "omega_unlocked", "omega_min_period", "plant_reserve", "x_target",
        "waiting_initial", "waiting_panel", "troop_panel_seats", "active_cases", "reviews_unassignable_ticks",
        "careful_delivery", "stamper_delivery", "members_on_duty", "probationers_on_duty", "plants_unfunded", "withdrawn_unawarded",
        # 1.7.0: the accounts and Ω's record by source
        "troop_account", "troop_surplus", "omega_fee_income", "advances_made", "advances_repaid", "liabilities_paid",
        "liabilities_old", "members_total", "members_free", "members_committed", "suspended_waiting", "probationers", "awards_waiting",
        # 1.7.1: the per-request summons
        "awards_waiting_w_a", "members_free_at_seating", "awards_left_to_members",
        # 2.0.0: the price level, the deficit, issuance and departures, the flags, the capacity case, real wealth, the demand side
        "P_t", "price_index", "credit_value", "deficit", "deficit_created", "deficit_retired", "deficit_peak", "deficit_age",
        "omega_net_position", "issued", "departed", "below_market_flagged", "below_market_waiting", "ceilings_raised", "places_held",
        "refused_capacity_seats", "refused_capacity_awards", "refused_capacity_waiting", "capacity_wait_max",
        "careful_wealth_real", "stamper_wealth_real", "requester_wallet_mean", "requester_unlocked_mean", "crowd_present",
        "crowd_wallet_mean", "member_price_mean", "troop_price_mean", "c_d_now", "margin_mean", "posts_unaffordable", "posts_k_open", "awarded",
        "effort_burned", "effort_unpaid", "crowd_arrived", "crowd_departed", "shock_created", "M",
        "lowballer_n", "lowballer_wealth_real", "lowballer_awards", "lowballer_rho", "stingy_n", "stingy_open", "stingy_wallet_mean"]
SHORT = {"stampers": "s", "fee": "f", "on-duty": "X", "gv": "gv", "p-floor": "pf", "p-start": "p", "p-cap": "pc", "band": "band",
         "fail-rate": "b", "accuracy": "a", "ruling-accuracy": "r", "appeal-policy": "appeal", "dispute-policy": "dispute",
         "dispute-rate": "dr", "assignment": "assign", "rules": "rules", "pi0": "pi", "dial": "dial", "beta-p": "bp",
         "camouflage": "cam", "omega0": "om", "drift-to": "drift", "adapt-rate": "adapt", "fund": "fund", "m-max": "mmax",
         "stamper-mode": "mode", "troops": "troops", "w-r": "wR", "w-a": "wA", "c-d-t": "cD", "eps-t": "eT", "a-t": "AT",
         "decline-awards": "dec", "tasks": "k", "clock": "clk", "backing": "bak", "seat-queue": "sq", "panel-determined": "pd",
         "reserve-periods": "rp", "duty-cap": "cap", "t-s": "Ts", "beta-low": "bl", "beta-low-share": "bls", "accounts": "acc", "omega-rate": "rate", "r-s": "rs", "t-susp": "tsusp",
         "plant-reserve": "pr", "theta-panel": "thp", "record-window": "nP", "withdraw-after": "wd",
         "spike-tasks": "spk", "spike-ticks": "spkT", "spike-from": "spkF", "drift-from": "dfrom", "drift-every": "devery", "drift-step": "dstep",
         "spike-requesters": "crowd", "n-t": "NT", "c-d": "cd", "c-d-t-mode": "cdt", "lam": "lam", "issuance": "iss", "wallet": "wal", "beta-max": "bmax",
         "k-open": "kopen", "bid": "bid", "c-d-adaptive": "cda", "create-at": "crAt", "create-amount": "cr", "requesters": "nreq", "lowball-share": "low", "stingy-requesters": "stingy", "bbar-troops": "bbt"}


def _num(x: str):
    try:
        return int(x) if x.lstrip("-").isdigit() else float(x)
    except ValueError:
        return x                      # a categorical factor, e.g. appeal-policy=none,truthful,always


def parse_factors(specs, ofat: bool):
    """`name=v1,v2` (grid) or `name=base:alt1,alt2` (one at a time) -> list of (name, baseline, values)."""
    out = []
    for spec in specs:
        name, _, vals = spec.partition("=")
        if ofat:
            base, _, alts = vals.partition(":")
            out.append((name, _num(base), [_num(base)] + [_num(v) for v in alts.split(",") if v]))
        else:
            vs = [_num(v) for v in vals.split(",")]
            out.append((name, vs[0], vs))
    return out


def cells_of(grid, ofat):
    """Each cell: an ordered dict factor -> value."""
    grid_points = [dict(zip([g[0] for g in grid], combo)) for combo in itertools.product(*[g[2] for g in grid])] or [{}]
    ofat_points = [{name: base for name, base, _ in ofat}]
    for name, base, values in ofat:
        for v in values:
            if v != base:
                pt = {n: b for n, b, _ in ofat}
                pt[name] = v
                ofat_points.append(pt)
    return [{**g, **o} for g in grid_points for o in ofat_points]


def cell_name(cell):
    return "-".join(f"{SHORT.get(k, k)}{v:g}" if isinstance(v, (int, float)) else f"{SHORT.get(k, k)}-{v}" for k, v in cell.items())


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--root", default=RESULTS, help="the study folder; runs go to <root>/runs/")
    ap.add_argument("--name", default="sweep")
    ap.add_argument("--grid", nargs="*", default=[], help="factors crossed in full: name=v1,v2,...")
    ap.add_argument("--ofat", nargs="*", default=[], help="factors varied one at a time: name=baseline:alt1,alt2")
    ap.add_argument("--seeds", type=int, default=20)
    ap.add_argument("--seed-from", type=int, default=1)
    ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("--actors", type=int, default=20)
    ap.add_argument("--log-every", type=int, default=100)
    ap.add_argument("--phi-f-per-fee", type=float, default=2.5,
                    help="φ^F = this × f (§4.3 default: f·(w_ordinary + w_audit) = 2.5 f); 0 keeps the driver's default")
    ap.add_argument("--extra", nargs=argparse.REMAINDER, default=[], help="passed through to drivers.stamping")
    a = ap.parse_args(argv)

    grid, ofat = parse_factors(a.grid, False), parse_factors(a.ofat, True)
    cells = cells_of(grid, ofat)
    seeds = list(range(a.seed_from, a.seed_from + a.seeds))
    os.makedirs(os.path.join(a.root, "runs"), exist_ok=True)
    rec = RunRecorder(a.name, kind="sweep summary over drivers.stamping cells × seeds", params=Params(), root=a.root,
                      declared={"cells": [cell_name(c) for c in cells], "factors_grid": a.grid, "factors_ofat": a.ofat,
                                "seeds": seeds, "ticks": a.ticks, "actors": a.actors,
                                "per_run": "drivers.stamping at its defaults except the cell's factors and --seed; "
                                           "--phi-f = phi_f_per_fee × fee", "phi_f_per_fee": a.phi_f_per_fee,
                                "extra_args": a.extra})
    runs, finals = [], {}
    t0 = time.time()
    for cell in cells:
        cname = cell_name(cell)
        for seed in seeds:
            name = f"{a.name}-{cname}-seed{seed}"
            argv_run = ["--actors", str(a.actors), "--ticks", str(a.ticks), "--seed", str(seed),
                        "--log-every", str(a.log_every), "--name", name, "--results-root", a.root]
            for k, v in cell.items():
                argv_run += [f"--{k}", str(v)]
            fee = cell.get("fee", 2.0)
            if a.phi_f_per_fee > 0:
                argv_run += ["--phi-f", str(a.phi_f_per_fee * fee)]
            argv_run += a.extra
            runs_dir = os.path.join(a.root, "runs")
            before = set(os.listdir(runs_dir))
            rc = stamping.main(argv_run)
            new = [d for d in os.listdir(runs_dir) if d not in before and d.endswith(name)]
            with open(os.path.join(runs_dir, new[0], "manifest.json")) as f:
                m = json.load(f)
            final = m["final"]
            row = {"cell": cname, **cell, "seed": seed, "run_id": m["run_id"], "status": m["status"], "head": m["head"]}
            row.update({k: final.get(k, "") for k in KEYS})
            rec.tick(row)
            runs.append({"run_id": m["run_id"], "status": m["status"], "rc": rc})
            finals.setdefault(cname, []).append(final)
    summary = {}
    for cname, rows in finals.items():
        st = {}
        for k in KEYS:
            vals = [r[k] for r in rows if isinstance(r.get(k), (int, float))]
            if vals:
                st[k] = {"mean": round(statistics.fmean(vals), 3), "sd": round(statistics.stdev(vals), 3) if len(vals) > 1 else 0.0,
                         "min": round(min(vals), 3), "max": round(max(vals), 3)}
        diffs = [r["stamper_wealth"] - r["careful_wealth"] for r in rows]
        sd = statistics.stdev(diffs) if len(diffs) > 1 else 0.0
        st["stamper_minus_careful_wealth"] = {"mean": round(statistics.fmean(diffs), 3), "sd": round(sd, 3),
                                              "se": round(sd / len(diffs) ** 0.5, 3)}
        st["stampers_richer_in"] = f"{sum(1 for d in diffs if d > 0)} of {len(diffs)}"
        summary[cname] = st
    ok = all(r["status"] == "completed" for r in runs)
    lines = [f"# {a.name}: {len(runs)} runs, {len(cells)} cells × {len(seeds)} seeds, {a.actors} actors × {a.ticks} ticks", "",
             "| cell | careful wealth | stamper wealth | stamper − careful (se) | stampers richer | stamper overturned % "
             "| false approvals | final N | audits assigned | reviews unassignable ticks | Ω unrecovered "
             "| m | X_t | plants | suspensions | alarms | elig. shortfall | Ω plant spend | Ω net |",
             "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for cname, st in summary.items():
        g = lambda k: st[k]["mean"] if k in st else float("nan")
        ov = 100 * g("stamper_overturned") / max(1e-9, g("stamper_reviews"))
        lines.append(f"| {cname} | {g('careful_wealth'):.0f} ± {st['careful_wealth']['sd']:.0f} | {g('stamper_wealth'):.0f} ± {st['stamper_wealth']['sd']:.0f} "
                     f"| {st['stamper_minus_careful_wealth']['mean']:+.0f} ({st['stamper_minus_careful_wealth']['se']:.0f}) | {st['stampers_richer_in']} "
                     f"| {ov:.1f} | {g('false_approvals'):.0f} | {g('final_n'):.0f} | {g('audits_assigned'):.0f} "
                     f"| {g('reviews_unassignable_ticks'):.0f} | {g('omega_unrecovered_advances'):.1f} "
                     f"| {g('m'):.2f} | {g('X_t'):.1f} | {g('plants_created'):.0f} | {g('suspensions'):.0f} | {g('alarms'):.1f} "
                     f"| {g('eligibility_shortfall'):.0f} | {g('omega_plant_spend'):.0f} | {g('omega_net'):.0f} |")
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
