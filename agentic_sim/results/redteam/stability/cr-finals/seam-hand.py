"""The emission's seam alone at 2.9.0 (November 7, 2026; notes §77): the hand and careful arms re-run on the corrected engine at the roll's OLD
defaults (--p-floor 0.2 --p-halve-every 5, the defaults the finals of record were made at) paired by seed against the finals of record
(eval/final/, macOS, old defaults). The seam-290-own.md tables carry the defaults' move as well; this one isolates the episode's.
Usage: seam-hand.py NEW_EVAL_JSON RECORD_EVAL_JSON OUT.md"""
import json, sys, math, numpy as np
A = json.load(open(sys.argv[1])); B = json.load(open(sys.argv[2]))
KEYS = [("false_approvals_run", "standing false approvals", 1), ("bad_plants_approved", "bad plants approved", 1), ("good_plants_rejected", "good plants rejected", 1), ("suspensions_run", "suspensions", 1),
        ("audits_held", "audits held", 0), ("audit_overturn_rate", "audit overturn rate", 3), ("disputes_filed", "disputes filed", 1), ("disputes_won", "disputes won", 1), ("appeals_filed", "appeals filed", 1),
        ("true_rejections_overturned", "lying appeals paid", 1), ("pop_surplus_nominal", "nominal surplus", 0), ("lifetime_real_wealth", "real lifetime", 0), ("pop_tasks_per_1000", "tasks per 1,000", 1),
        ("P_t", "P_t", 1), ("member_price_mean", "members' price", 1), ("state_share", "state share", 3), ("awarded", "awarded", 0), ("cost_of_truth", "cost of truth", 0), ("decisions", "decisions", 0)]
def f(v):
    try: return float(v) if v not in (None, "") else np.nan
    except (TypeError, ValueError): return np.nan
L = [f"# The seam alone: the corrected engine at the old defaults ({sys.argv[1]}) − the finals of record ({sys.argv[2]}), paired by seed (mean ± SE over seeds 21–40)\n", "| reading | " + " | ".join(f"{p} (corrected, old defaults) | {p} (record) | {p}: paired difference" for p in ("hand", "careful")) + " |", "|---|" + "---|" * 6]
for key, label, d in KEYS:
    row = []
    for pol in ("hand", "careful"):
        EA = {e["seed"]: e for e in A["episodes"][pol]}; EB = {e["seed"]: e for e in B["episodes"][pol]}
        seeds = sorted(set(EA) & set(EB)); a = np.array([f(EA[s].get(key)) for s in seeds]); b = np.array([f(EB[s].get(key)) for s in seeds]); dd = a - b; ok = ~np.isnan(dd)
        if ok.sum() < 2: row += ["—", "—", "—"]; continue
        row += [f"{a[ok].mean():.{d}f}", f"{b[ok].mean():.{d}f}", f"{dd[ok].mean():+.{d}f} ± {dd[ok].std(ddof=1) / math.sqrt(ok.sum()):.{d}f}"]
    L.append(f"| {label} | " + " | ".join(row) + " |")
# how many seeds' hand episodes are identical on the measures (the episode differs by construction from tick 181's batch; the measures may still agree)
EA = {e["seed"]: e for e in A["episodes"]["hand"]}; EB = {e["seed"]: e for e in B["episodes"]["hand"]}
same = sum(1 for s in EA if s in EB and all(f(EA[s].get(k)) == f(EB[s].get(k)) for k, _, _ in KEYS[:5]))
L.append(f"\nSeeds whose hand episode agrees on the first five measures to the unit: {same} of {len(EA)} (the episodes differ from tick 181's settlement batch on by construction; agreement here is coincidence of the counts).")
open(sys.argv[3], "w").write("\n".join(L) + "\n"); print("\n".join(L))
