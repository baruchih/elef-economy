"""2.9.0 §8.5 on the corrected engine (November 10, 2026; the policies of record under 2.9.0 and under --rules 2.7.0, both on the corrected engine) — the lone learners: two run_q finals paired by seed per policy (2.9.0 against 2.7.0). Usage:
python3 pair_evals.py <eval.json 2.7.0> <eval.json 2.9.0> [label]  — prints a markdown table: lifetime real (levels and the paired difference), the mix,
the plant / real stamp rates, the by-seat stamp rates where the eval carries them, the slot's suspensions and plant failures, the run's false approvals."""
import json, math, sys
a, b = json.load(open(sys.argv[1])), json.load(open(sys.argv[2])); label = sys.argv[3] if len(sys.argv) > 3 else ""
def mse(xs):
    xs = [x for x in xs if x is not None and not (isinstance(x, float) and math.isnan(x))]
    if not xs: return (float("nan"), float("nan"))
    m = sum(xs) / len(xs); return m, ((sum((x - m) ** 2 for x in xs) / (len(xs) - 1)) ** 0.5 / len(xs) ** 0.5 if len(xs) > 1 else float("nan"))
def fmt(ms, d=1): return "—" if math.isnan(ms[0]) else (f"{ms[0]:,.{d}f} ± {ms[1]:,.{d}f}" if not math.isnan(ms[1]) else f"{ms[0]:,.{d}f}")
def by_seed(e, pol): return {ep["seed"]: ep for ep in e["episodes"].get(pol, [])}
def rate(ep, seat, kind):
    n, k = ep.get(f"seat_{seat}_{kind}_seen"), ep.get(f"seat_{seat}_{kind}_stamped")
    return (k / n) if n else None
print(f"### {label}\n")
print("| policy | lifetime real 2.7.0 | 2.9.0 | 2.9.0 − 2.7.0 (paired) | care / approve / reject 2.7.0 → 2.9.0 | plant / real stamp 2.7.0 → 2.9.0 | 2.9.0 stamp by seat: initial p/r · audit p/r · panel p/r | slot suspensions 2.7.0 → 2.9.0 | run's false approvals 2.7.0 → 2.9.0 |")
print("|---|---|---|---|---|---|---|---|---|")
for pol in b["summary"]:
    A, B = by_seed(a, pol), by_seed(b, pol); seeds = sorted(set(A) & set(B))
    la, lb = mse([A[s]["lifetime_real_wealth"] for s in seeds]), mse([B[s]["lifetime_real_wealth"] for s in seeds])
    d = mse([B[s]["lifetime_real_wealth"] - A[s]["lifetime_real_wealth"] for s in seeds])
    mix = lambda E: " / ".join(f"{mse([E[s][k] for s in seeds])[0]:.2f}" for k in ("care_share", "approve_blind_share", "reject_blind_share"))
    def pr(E):
        ps = mse([E[s]["plants_stamped"] / E[s]["plants_seen"] for s in seeds if E[s].get("plants_seen")])[0]
        rs = mse([E[s]["real_stamped"] / E[s]["real_seen"] for s in seeds if E[s].get("real_seen")])[0]
        return f"{ps:.2f} / {rs:.2f}"
    seats = " · ".join(f"{(mse([rate(B[s], st, 'plant') for s in seeds])[0]):.2f}/{(mse([rate(B[s], st, 'real') for s in seeds])[0]):.2f}" for st in ("initial", "audit", "panel")) if any("seat_initial_real_seen" in B[s] for s in seeds) else "—"
    sus = f"{mse([A[s].get('slot_suspensions') for s in seeds])[0]:.2f} → {mse([B[s].get('slot_suspensions') for s in seeds])[0]:.2f}"
    fa = f"{mse([A[s].get('false_approvals_run') for s in seeds])[0]:.1f} → {mse([B[s].get('false_approvals_run') for s in seeds])[0]:.1f}"
    print(f"| {pol} | {fmt(la)} | {fmt(lb)} | **{fmt(d)}** | {mix(A)} → {mix(B)} | {pr(A)} → {pr(B)} | {seats} | {sus} | {fa} |")
