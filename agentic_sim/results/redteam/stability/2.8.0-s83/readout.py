"""2.8.0 §8.3 / §8.6 — the honest populations by hand, 2.8.0 against the flag off (--rules 2.7.0), paired by seed. Reads the final row of every run
under runs/ (named <cell>-<rules>-s<seed>) and writes finals.md: per cell the levels (mean ± SE over seeds) under each rule and the paired
difference 2.8.0 − 2.7.0. Usage: python3 readout.py [runs dir] [out md]"""
import csv, glob, math, os, sys
from collections import defaultdict

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "finals.md")
CELLS = ["entry60", "fixed60", "careful", "disputes"]
LABEL = {"entry60": "run 24's entry cell (60/40, the entry pool of 20)", "fixed60": "the fixed population's 60/40",
         "careful": "all-careful with entry", "disputes": "the entry cell with truthful disputes"}
PLANT_SEATS = ["initial", "audit", "third", "appeal", "dispute", "resumed", "state"]
COLS = [  # (column, label, derived)
    ("false_approvals", "standing false approvals"), ("false_rejections", "false rejections"), ("suspensions", "suspensions"),
    ("bad_plants_approved", "bad plants approved (initial seat)"), ("good_plants_rejected", "good plants rejected (initial seat)"),
    ("F_hat", "F̂ (the dial's)"), ("audit_overturn_rate", "audit layer's overturn rate"),
    ("appeals_filed", "appeals filed"), ("appeals_won", "appeals won"), ("disputes_filed", "disputes filed"), ("disputes_won", "disputes won"),
    ("awarded", "awarded"), ("state_share", "state's share"), ("P_t", "P_t"), ("pop_tasks_per_1000", "tasks per 1,000 nominal (customers)"),
    ("careful_wealth", "careful member's nominal wealth (mean)"), ("stamper_wealth", "stamper's nominal wealth (mean)"),
    ("careful_n", "careful alive"), ("stamper_n", "stampers alive"), ("arrivals", "arrivals"), ("departures", "departures"),
    ("omega", "Ω"), ("omega_net", "Ω net"), ("omega_fee_income", "Ω's fee income"), ("omega_review_fee_income", "Ω's review-fee income (troop seats)"),
    ("troop_surplus", "troop surplus to Ω"), ("troop_deliveries", "state deliveries"), ("troop_summons_reviews", "troop review seats"),
    ("omega_plant_spend", "Ω's plant spend"), ("omega_in_plants", "Ω in plants"),
    ("plants_posted", "plants posted"), ("periods", "periods"), ("plants_per_period", "plants per period"),
    ("seats_per_plant", "adjudicated seats per plant (all kinds / initial)"),
    ("minted_plant", "bank: plant mint"), ("destroyed_plant", "bank: plant destroyed"), ("cost_of_truth", "cost of truth"),
    ("plant_share_of_reviews", "plants' share of all reviews"), ("care_cost_plant", "care spent on plants"), ("care_cost_real", "care spent on real cases"),
    ("care_reviews_plant", "careful reviews on plants"), ("care_reviews_real", "careful reviews on real cases"),
    ("care_share_plants", "share of the care spent on plants"),
    ("plant_top_ups", "pots topped up"), ("plant_fees_destroyed", "court fee destroyed"), ("plant_appeals_filed", "plant appeals filed"),
    ("plant_disputes_filed", "plant disputes filed"), ("plants_revised", "plants revised"), ("plant_seats_at_state", "plant seats the state took"),
] + [(f"plant_adj_{k}", f"plant seats adjudicated: {k}") for k in PLANT_SEATS] + [(f"plant_fail_{k}", f"plant seat failures: {k}") for k in PLANT_SEATS]

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return float("nan")

rows = defaultdict(dict)   # (cell, rules) -> seed -> final row
for f in glob.glob(os.path.join(root, "*", "metrics.csv")):
    name = os.path.basename(os.path.dirname(f)).split("-", 2)[-1]       # <cell>-<rules>-s<seed>
    cell, rules, seed = name.rsplit("-", 2); seed = int(seed[1:])
    r = list(csv.DictReader(open(f)))[-1]
    d = {c: num(r.get(c)) for c, _ in COLS if c not in ("plants_per_period", "seats_per_plant", "care_share_plants")}
    d["plants_per_period"] = d["plants_posted"] / d["periods"] if d["periods"] else float("nan")
    d["care_share_plants"] = d["care_cost_plant"] / (d["care_cost_plant"] + d["care_cost_real"]) if (d["care_cost_plant"] + d["care_cost_real"]) > 0 else float("nan")
    adj = sum(num(r.get(f"plant_adj_{k}")) for k in PLANT_SEATS)
    d["seats_per_plant"] = adj / num(r.get("plant_adj_initial")) if num(r.get("plant_adj_initial")) else float("nan")
    rows[(cell, rules)][seed] = d

def mse(xs):
    xs = [x for x in xs if not math.isnan(x)]
    if not xs: return float("nan"), float("nan")
    m = sum(xs) / len(xs); se = (sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5 / len(xs) ** 0.5 if len(xs) > 1 else float("nan")
    return m, se
def fmt(m, se, d=2):
    if math.isnan(m): return "—"
    return f"{m:,.{d}f} ± {se:,.{d}f}" if not math.isnan(se) else f"{m:,.{d}f}"
def dec(c): return 4 if c in ("F_hat", "audit_overturn_rate", "state_share", "plant_share_of_reviews", "care_share_plants") else (3 if c in ("seats_per_plant", "plants_per_period") else (1 if c in ("P_t", "pop_tasks_per_1000") else 2))

L = [f"# §8.3 — the honest populations by hand (2.8.0 against the flag off, seeds 21–40, paired)\n", f"Runs: `{root}`\n"]
for cell in CELLS:
    a, b = rows.get((cell, "2.8.0"), {}), rows.get((cell, "2.7.0"), {})
    seeds = sorted(set(a) & set(b))
    L.append(f"\n## {LABEL[cell]} (`{cell}`; {len(seeds)} seeds paired)\n")
    L.append("| reading | 2.7.0 (flag off) | 2.8.0 | 2.8.0 − 2.7.0 (paired) |\n|---|---|---|---|")
    for c, lab in COLS:
        m7, s7 = mse([b[s][c] for s in seeds]); m8, s8 = mse([a[s][c] for s in seeds]); md, sd = mse([a[s][c] - b[s][c] for s in seeds])
        bold = (not math.isnan(sd)) and sd > 0 and abs(md) > 2 * sd
        L.append(f"| {lab} | {fmt(m7, s7, dec(c))} | {fmt(m8, s8, dec(c))} | {'**' if bold else ''}{fmt(md, sd, dec(c))}{'**' if bold else ''} |")
open(out, "w").write("\n".join(L) + "\n"); print("wrote", out, {k: len(v) for k, v in rows.items()})
