"""Ablation brief A1 r2 §7.2 — the scripted populations at seeds 21–40 under nine configurations: arm 0 (2.9.0 as in force), arm 0 with π^A
pinned at 0.10 and 0.20, arms 1, 1b (r 0.25), 1c, 2, 3, 4. Reads the final row of every run under runs/ (named <cell>-<arm>-s<seed>) and
writes finals.md: per cell the levels under each arm (mean ± SE over seeds) and the paired differences arm − arm 0 on the identical seeds, over
the brief's readings — the leak (standing false approvals; over vested roots; over bad deliveries), the false penalties by seat, the deciding
verdict's counts, the orchestrator's seats and its unreimbursed cost, the challenges by their truth, the two overhead views, the time to
vesting, the members' and the customers' measures, the roster. Usage: python3 readout.py [runs dir] [out md]"""
import csv, glob, math, os, sys
from collections import defaultdict
root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "finals.md")
CELLS = ["careful", "entry60", "fixed60", "disputes", "liars"]
LABEL = {"careful": "all-careful with arrivals", "entry60": "run 24's entry cell (60/40, the entry pool of 20)", "fixed60": "the fixed population's 60/40",
         "disputes": "the entry cell with truthful disputes", "liars": "the entry cell with liars at 0.1 (truthful disputes)"}
ARMS = ["arm0", "arm0-pa10", "arm0-pa20", "arm1", "arm1b", "arm1c", "arm2", "arm3", "arm4"]
ARM_LABEL = {"arm0": "arm 0 (2.9.0)", "arm0-pa10": "arm 0, π^A 0.10", "arm0-pa20": "arm 0, π^A 0.20", "arm1": "arm 1 trusted ruling", "arm1b": "arm 1b sampled 0.25",
             "arm1c": "arm 1c cheaper false alarm", "arm2": "arm 2 state's audit", "arm3": "arm 3 state's bench", "arm4": "arm 4 small core"}
COLS = [("false_approvals", "standing false approvals"), ("leak_paid", "leak over vested roots"), ("leak_bad", "leak over bad deliveries"), ("bad_deliveries", "bad deliveries"),
        ("vested", "vested"), ("false_rejections", "standing false rejections"),
        ("false_penalty_initial", "false penalties, initial"), ("false_penalty_audit", "false penalties, audit"), ("false_penalty_appeal", "false penalties, panel"),
        ("false_penalty_bond_kept", "… of which bond kept (1c)"),
        ("deciding_opened", "deciding verdicts"), ("deciding_seats", "deciding seats"), ("deciding_splits", "splits"), ("deciding_overturned", "deciding: overturned"),
        ("deciding_audit", "… from a member audit"), ("deciding_state_audit", "… from the state's audit"), ("deciding_panel", "… from a panel"), ("deciding_bench", "… the bench"),
        ("deciding_sampled", "… sampled"), ("confirmations_overturned", "sampled confirmations overturned"), ("lenient_bonds_kept", "bonds kept (1c)"),
        ("state_audit_seats", "state audit seats"), ("plant_audits_waived", "plant audits waived"), ("troop_reviews", "the orchestrator's review seats"),
        ("troop_review_cost", "the orchestrator's c_T (credits)"), ("state_cost_unreimbursed", "… unreimbursed"),
        ("audits_held", "audits held"), ("audits_overturning", "audits overturning"), ("audit_overturn_rate", "audit overturn rate"),
        ("disputes_won", "disputes won"), ("disputes_lost", "disputes lost"), ("true_approvals_overturned", "lying disputes paid"),
        ("appeals_won", "appeals won"), ("appeals_lost", "appeals lost"), ("true_rejections_overturned", "lying appeals paid"),
        ("suspensions", "suspensions"), ("cost_of_truth", "cost of truth"), ("care_cost_real", "care on real cases"), ("care_cost_plant", "care on plants"), ("plant_price_sum", "plants' prices"),
        ("cust_overhead_per_vested", "customer's overhead / task"), ("cust_overhead_share", "… share of price"), ("sys_overhead_per_vested", "system's overhead / task"), ("sys_overhead_share", "… share of price"),
        ("vest_ticks_mean", "submission → vesting, mean"), ("vest_ticks_p50", "… p50"), ("vest_ticks_p90", "… p90"),
        ("pop_surplus_nominal", "members' nominal surplus"), ("pop_tasks_per_1000", "customers' tasks per 1,000"), ("P_t", "P_t"), ("omega_fee_income", "Ω's fee income"), ("state_share", "the state's share of deliveries"),
        ("members_total", "members"), ("arrivals", "arrivals"), ("departures", "departures"), ("X_t", "X_t"), ("member_seats", "member seats")]
def f(x):
    try: return float(x)
    except (TypeError, ValueError): return float("nan")
def ms(v):
    v = [x for x in v if not math.isnan(x)]
    if not v: return "—"
    m = sum(v) / len(v); se = (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5 / len(v) ** 0.5 if len(v) > 1 else float("nan")
    return f"{m:.3f} ± {se:.3f}" if abs(m) < 10 else f"{m:.1f} ± {se:.1f}"
data = defaultdict(dict)   # (cell, arm) -> seed -> row
for cell in CELLS:
    for arm in ARMS:
        for fn in glob.glob(os.path.join(root, f"*{cell}-{arm}-s*", "metrics.csv")):
            name = os.path.basename(os.path.dirname(fn)); seed = int(name.rsplit("-s", 1)[1].split("-")[0].split("_")[0])
            rows = list(csv.DictReader(open(fn)))
            if rows: data[(cell, arm)][seed] = rows[-1]
L = ["# Ablation brief A1 r2 §7.2 — the scripted populations, nine configurations on seeds 21–40 (mean ± SE over seeds; the paired differences on the identical seeds)\n"]
for cell in CELLS:
    have = [a for a in ARMS if data[(cell, a)]]
    if not have: continue
    L.append(f"\n## {LABEL[cell]}\n")
    L.append("| reading | " + " | ".join(f"{ARM_LABEL[a]} (n={len(data[(cell, a)])})" for a in have) + " |"); L.append("|---|" + "---|" * len(have))
    for col, lab in COLS:
        L.append(f"| {lab} | " + " | ".join(ms([f(r.get(col)) for r in data[(cell, a)].values()]) for a in have) + " |")
    base = data[(cell, "arm0")]
    if base and len(have) > 1:
        L.append(f"\n**Paired against arm 0 on the same seeds (arm − arm 0):**\n")
        others = [a for a in have if a != "arm0"]
        L.append("| reading | " + " | ".join(ARM_LABEL[a] for a in others) + " |"); L.append("|---|" + "---|" * len(others))
        for col, lab in COLS:
            cells = []
            for a in others:
                d = [f(data[(cell, a)][s].get(col)) - f(base[s].get(col)) for s in data[(cell, a)] if s in base]
                cells.append(ms(d))
            L.append(f"| {lab} | " + " | ".join(cells) + " |")
open(out, "w").write("\n".join(L) + "\n"); print(f"{sum(len(v) for v in data.values())} runs read → {out}")
