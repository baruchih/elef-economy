"""2.8.0 §8.7 beside the three cells — the `log` tell-reader against `freshname` by hand (logtell/runs, seeds 21–40, 2.8.0 and the flag off) and the
audit-only stamper through run_q (auditstamper-280 / auditstamper-270). Writes hand.md. Usage: python3 readout_hand.py"""
import csv, glob, json, math, os
from collections import defaultdict
here = os.path.dirname(os.path.abspath(__file__))
def num(x):
    try: return float(x)
    except (TypeError, ValueError): return float("nan")
def mse(xs):
    xs = [x for x in xs if not math.isnan(x)]
    if not xs: return float("nan"), float("nan")
    m = sum(xs) / len(xs); return m, ((sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5 / len(xs) ** 0.5 if len(xs) > 1 else float("nan"))
def fmt(ms, d=2): return "—" if math.isnan(ms[0]) else f"{ms[0]:,.{d}f} ± {ms[1]:,.{d}f}"
rows = defaultdict(dict)
for f in glob.glob(os.path.join(here, "logtell", "runs", "*", "metrics.csv")):
    name = os.path.basename(os.path.dirname(f)).split("-", 2)[-1]; tell, rules, seed = name.rsplit("-", 2)
    rows[(tell, rules)][int(seed[1:])] = list(csv.DictReader(open(f)))[-1]
TELLS = sorted({k[0] for k in rows}, key=lambda x: ["log", "logcare", "freshname"].index(x) if x in ("log", "logcare", "freshname") else 9)
COLS = [("tell_plant_read_plant", "plant reviews read as a plant"), ("tell_plant_read_real", "plant reviews read as real (stamped, or cared at a first review under tell-initial care)"),
        ("tell_real_read_plant", "real reviews read as a plant"), ("tell_real_read_real", "real reviews read as real (stamped)"),
        ("tell_plant_pass_rate", "plant pass rate"), ("tell_real_stamp_rate", "real stamp rate"), ("tell_false_approvals", "the reader's false approvals"),
        ("tell_plant_failures", "the reader's plant failures"), ("tell_suspended", "suspended (reader-runs)"), ("tell_wealth_real_lifetime", "the reader's lifetime real wealth"),
        ("careful_wealth", "careful member's nominal wealth (mean)"), ("tell_wealth", "the reader's nominal wealth"), ("false_approvals", "standing false approvals (run)"),
        ("tell_departed", "reader departed"), ("tell_reviews", "the reader's reviews"), ("tell_overturned", "the reader's reviews overturned"),
        ("tell_bonds_forfeited", "the reader's bonds forfeited"), ("tell_p_audit", "the reader's applied odds at the end"),
        ("tell_initial_cared", "first reviews cared (tell-initial care)"), ("tell_later_plant_stamped", "later seats: plants stamped"),
        ("tell_later_real_stamped", "later seats: real stamped"), ("tell_later_plant_cared", "later seats: plants cared"), ("tell_later_real_cared", "later seats: real cared")]
L = ["# §8.7 beside the cells — the `log` tell-reader and the audit-only stamper\n", "## The `log` tell-reader (one reader in eight careful actors, run 24's entry cell, seeds 21–40) against `freshname`\n",
     "| reading | " + " | ".join(f"{tl}, {ru}" for tl in TELLS for ru in ("2.7.0", "2.8.0")) + " |\n|---|" + "---|" * (2 * len(TELLS))]
for c, lab in COLS:
    L.append(f"| {lab} | " + " | ".join(fmt(mse([num(r.get(c)) for r in rows[(t, ru)].values()])) for t in TELLS for ru in ("2.7.0", "2.8.0")) + " |")
# the by-seat split of the reader's plant readings is not in the row; the seat kinds a reader reaches are read from the run logs if needed
L.append("\n## The audit-only stamper (a lone slot, run 24's entry cell, seeds 21–40; run_q)\n")
L.append("| policy | rules | lifetime real | vs careful (paired) | care / approve / reject | stamp by seat: initial p/r · audit p/r · panel p/r | slot suspensions | slot plant failures | run's false approvals |\n|---|---|---|---|---|---|---|---|---|")
for ru, d in (("2.8.0", "auditstamper-280"), ("2.7.0", "auditstamper-270")):
    f = os.path.join(here, d, "eval.json")
    if not os.path.exists(f): continue
    e = json.load(open(f))
    for pol, s in e["summary"].items():
        eps = e["episodes"][pol]
        def rate(st, k):
            n = sum(ep.get(f"seat_{st}_{k}_seen", 0) or 0 for ep in eps); x = sum(ep.get(f"seat_{st}_{k}_stamped", 0) or 0 for ep in eps)
            return f"{x / n:.2f}" if n else "—"
        pm = s.get("paired_minus_careful"); pm = fmt(tuple(pm), 1) if isinstance(pm, list) else "—"
        L.append(f"| {pol} | {ru} | {fmt(tuple(s['lifetime_real_wealth']), 1)} | {pm} | {s['care_share'][0]:.2f} / {s['approve_blind_share'][0]:.2f} / {s['reject_blind_share'][0]:.2f} | "
                 + " · ".join(f"{rate(st, 'plant')}/{rate(st, 'real')}" for st in ("initial", "audit", "panel"))
                 + f" | {fmt(tuple(s['slot_suspensions']), 2) if isinstance(s.get('slot_suspensions'), list) else s.get('slot_suspensions')} | {mse([float(ep.get('slot_plant_failures', float('nan'))) for ep in eps])[0]:.2f} | {fmt(tuple(s['false_approvals_run']), 1) if isinstance(s.get('false_approvals_run'), list) else s.get('false_approvals_run')} |")
open(os.path.join(here, "hand.md"), "w").write("\n".join(L) + "\n"); print("wrote hand.md", {k: len(v) for k, v in rows.items()})
