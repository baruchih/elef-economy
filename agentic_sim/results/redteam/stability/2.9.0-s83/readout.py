"""2.9.0 §8.3 / §8.6 on the corrected engine at the roll's new defaults (notes §75): the four honest populations by hand, four arms on the
identical seeds — new (2.9.0 at p_floor 0.5 / the window 20), old (2.9.0 at 0.2 / 5), 280 (--rules 2.8.0 at the new defaults), 280old
(--rules 2.8.0 at the old). Reads the final row of every run under runs/ (named <cell>-<arm>-s<seed>) and writes finals.md: per cell the
levels under each arm and four paired differences — new − old (the defaults' cost under 2.9.0, the ruling's condition), 280 − 280old (under
2.8.0), new − 280 (2.9.0 against 2.8.0 at the new defaults), old − 280old (at the old: the rc's §8.3 as written) — and a summary of the
defaults' cost across the cells. Usage: python3 readout.py [runs dir] [out md]"""
import csv, glob, math, os, sys
from collections import defaultdict

root = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "runs")
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "finals.md")
CELLS = ["entry60", "fixed60", "careful", "disputes"]
LABEL = {"entry60": "run 24's entry cell (60/40, the entry pool of 20)", "fixed60": "the fixed population's 60/40",
         "careful": "all-careful with entry", "disputes": "the entry cell with truthful disputes"}
ARMS = ["280old", "280", "old", "new"]
ARM_LABEL = {"new": "2.9.0, new defaults", "old": "2.9.0, old defaults", "280": "2.8.0, new defaults", "280old": "2.8.0, old defaults"}
PAIRS = [("new", "old", "new − old (the defaults' cost under 2.9.0)"), ("280", "280old", "280 − 280old (under 2.8.0)"),
         ("new", "280", "new − 280 (2.9.0 − 2.8.0, new defaults)"), ("old", "280old", "old − 280old (2.9.0 − 2.8.0, old defaults)")]
PLANT_SEATS = ["initial", "audit", "third", "appeal", "dispute", "resumed", "state"]
COLS = [
    ("false_approvals", "standing false approvals"), ("false_rejections", "false rejections"), ("suspensions", "suspensions"),
    ("bad_plants_approved", "bad plants approved (initial seat)"), ("good_plants_rejected", "good plants rejected (initial seat)"),
    ("F_hat", "F̂ (the dial's)"), ("audit_overturn_rate", "audit layer's overturn rate"),
    ("audits_rolled", "audits rolled (the obligations)"), ("audits_assigned", "audit seats a member took"), ("troop_summons_reviews", "review seats the state took (all kinds)"),
    ("audits_held", "audits held"), ("audits_overturning", "audits overturning"),
    ("appeals_filed", "appeals filed"), ("appeals_won", "appeals won"), ("disputes_filed", "disputes filed"), ("disputes_won", "disputes won"),
    ("awarded", "awarded"), ("state_share", "state's share"), ("P_t", "P_t"), ("pop_tasks_per_1000", "tasks per 1,000 nominal (customers)"),
    ("careful_wealth", "careful member's nominal wealth (mean)"), ("stamper_wealth", "stamper's nominal wealth (mean)"),
    ("careful_n", "careful alive"), ("stamper_n", "stampers alive"), ("arrivals", "arrivals"), ("departures", "departures"),
    ("omega", "Ω"), ("omega_net", "Ω net"), ("omega_fee_income", "Ω's fee income"), ("omega_review_fee_income", "Ω's review-fee income (troop seats)"),
    ("troop_deliveries", "state deliveries"),
    ("plants_posted", "plants posted"), ("periods", "periods"), ("plants_per_period", "plants per period"),
    ("seats_per_plant", "adjudicated seats per plant (all kinds / initial)"),
    ("pa_posted", "planted approvals posted (2.9.0)"), ("pa_audited", "planted approvals audited"), ("pa_confirmed", "planted approvals confirmed at the audit seat"),
    ("pa_disputed", "planted approvals disputed"), ("pa_unseated", "planted approvals unseated"), ("F_hat_A", "F̂^A"), ("m_A", "m^A"), ("pi_A", "π^A"),
    ("plant_lies_filed_appeal", "planted lies filed: appeals"), ("plant_lies_filed_dispute", "planted lies filed: disputes"),
    ("lie_sided_appeal", "panels siding with the planted appeal"), ("lie_sided_dispute", "panels siding with the planted dispute"),
    ("F_hat_La", "F̂^La"), ("F_hat_Ld", "F̂^Ld"), ("m_La", "m^La"), ("m_Ld", "m^Ld"),
    ("minted_plant", "bank: plant mint"), ("destroyed_plant", "bank: plant destroyed"), ("plant_mint_approval", "mint: planted approvals"), ("plant_mint_lie", "mint: planted lies"),
    ("cost_of_truth", "cost of truth"),
    ("plant_share_of_reviews", "plants' share of all reviews"), ("care_cost_plant", "care spent on plants"), ("care_cost_real", "care spent on real cases"),
    ("care_reviews_plant", "careful reviews on plants"), ("care_reviews_real", "careful reviews on real cases"), ("care_share_plants", "share of the care spent on plants"),
    ("plant_top_ups", "pots topped up"), ("plant_fees_destroyed", "court fee destroyed"), ("plant_seats_at_state", "plant seats the state took"),
] + [(f"plant_adj_{k}", f"plant seats adjudicated: {k}") for k in PLANT_SEATS] + [(f"plant_fail_{k}", f"plant seat failures: {k}") for k in PLANT_SEATS]
DERIVED = {"plants_per_period", "seats_per_plant", "care_share_plants"}

def num(x):
    try: return float(x)
    except (TypeError, ValueError): return float("nan")

rows = defaultdict(dict)   # (cell, arm) -> seed -> final row
for f in glob.glob(os.path.join(root, "*", "metrics.csv")):
    name = os.path.basename(os.path.dirname(f)).split("-", 2)[-1]       # <cell>-<arm>-s<seed>
    cell, arm, seed = name.rsplit("-", 2); seed = int(seed[1:])
    import json
    man = os.path.join(os.path.dirname(f), "manifest.json")
    if not os.path.exists(man) or json.load(open(man)).get("status") != "completed": continue      # a run still going, or failed
    r = list(csv.DictReader(open(f)))[-1]
    d = {c: num(r.get(c)) for c, _ in COLS if c not in DERIVED}
    d["plants_per_period"] = d["plants_posted"] / d["periods"] if d["periods"] else float("nan")
    tot = d["care_cost_plant"] + d["care_cost_real"]
    d["care_share_plants"] = d["care_cost_plant"] / tot if tot > 0 else float("nan")
    adj = sum(num(r.get(f"plant_adj_{k}")) for k in PLANT_SEATS)
    d["seats_per_plant"] = adj / num(r.get("plant_adj_initial")) if num(r.get("plant_adj_initial")) else float("nan")
    rows[(cell, arm)][seed] = d

def mse(xs):
    xs = [x for x in xs if not math.isnan(x)]
    if not xs: return float("nan"), float("nan")
    m = sum(xs) / len(xs); se = (sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5 / len(xs) ** 0.5 if len(xs) > 1 else float("nan")
    return m, se
def fmt(m, se, d=2):
    if math.isnan(m): return "—"
    return f"{m:,.{d}f} ± {se:,.{d}f}" if not math.isnan(se) else f"{m:,.{d}f}"
def dec(c): return 4 if c in ("F_hat", "audit_overturn_rate", "state_share", "plant_share_of_reviews", "care_share_plants", "pi_A") else (3 if c in ("seats_per_plant", "plants_per_period", "F_hat_A", "F_hat_La", "F_hat_Ld") else (1 if c in ("P_t", "pop_tasks_per_1000") else 2))
def pd(cell, a, b, c):
    A, B = rows.get((cell, a), {}), rows.get((cell, b), {}); seeds = sorted(set(A) & set(B))
    return mse([A[s][c] - B[s][c] for s in seeds]), len(seeds)
def cellf(m, se, d):
    bold = (not math.isnan(se)) and se > 0 and abs(m) > 2 * se
    return f"{'**' if bold else ''}{fmt(m, se, d)}{'**' if bold else ''}"

L = [f"# 2.9.0 §8.3 / §8.6 — the honest populations by hand at the roll's new defaults (seeds 21–40, four arms on the identical seeds, paired)\n",
     f"Runs: `{root}`. Arms: " + "; ".join(f"`{a}` {ARM_LABEL[a]}" for a in ARMS) + ". The new defaults p_floor 0.5 and the halving window 20 (Appendix A from faf968aa4), the old 0.2 and 5. Bold: beyond two SE.\n"]
HEAD = [("false_approvals", "standing false approvals"), ("audits_assigned", "audit seats a member took"), ("troop_summons_reviews", "review seats the state took"),
        ("audits_overturning", "audits overturning"), ("suspensions", "suspensions"), ("care_cost_real", "care spent on real cases"), ("cost_of_truth", "cost of truth"),
        ("omega_review_fee_income", "Ω's review-fee income"), ("careful_wealth", "careful member's nominal wealth"), ("pop_tasks_per_1000", "tasks per 1,000 nominal"), ("awarded", "awarded"), ("P_t", "P_t")]
for a, b, lab in PAIRS:
    L.append(f"\n## Summary — {lab}\n")
    L.append("| reading | " + " | ".join(LABEL[c] for c in CELLS) + " |\n|---|" + "---|" * len(CELLS))
    for c, cl in HEAD:
        cells = []
        for cell in CELLS:
            (m, se), n = pd(cell, a, b, c); lvl, _ = mse([rows.get((cell, b), {})[s][c] for s in rows.get((cell, b), {})])
            cells.append(f"{cellf(m, se, dec(c))} ({fmt(lvl, float('nan'), dec(c))})")
        L.append(f"| {cl} | " + " | ".join(cells) + " |")
    L.append(f"\n(in parentheses: the level under `{b}`)")
for cell in CELLS:
    seeds = sorted(set.intersection(*[set(rows.get((cell, a), {})) for a in ARMS])) if all((cell, a) in rows for a in ARMS) else []
    L.append(f"\n## {LABEL[cell]} (`{cell}`; {len(seeds)} seeds paired)\n")
    L.append("| reading | " + " | ".join(ARM_LABEL[a] for a in ARMS) + " | " + " | ".join(p[2] for p in PAIRS) + " |\n|---|" + "---|" * (len(ARMS) + len(PAIRS)))
    for c, lab in COLS:
        lv = [fmt(*mse([rows[(cell, a)][s][c] for s in seeds]), dec(c)) for a in ARMS]
        df = [cellf(*pd(cell, a, b, c)[0], dec(c)) for a, b, _ in PAIRS]
        L.append(f"| {lab} | " + " | ".join(lv) + " | " + " | ".join(df) + " |")
open(out, "w").write("\n".join(L) + "\n"); print("wrote", out, {k: len(v) for k, v in sorted(rows.items())})
