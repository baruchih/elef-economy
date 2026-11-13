"""The learner with a horizon's first chains read (addendum 10's J5; November 13, 2026; notes §111): the horizon chains (learned/horizon/{pa10,arm4}-t1-b1-mc, the
decision's target its slot's own return to the slot's exit at γ 0.98) against the one-decision chains of record on the same cells (stress/learned/{pa10,arm4}-t1-b1)
and the unstressed chains (ablation-A1/learned/{pa10,arm4}), the finals on seeds 21–40 — the claim at the first review and at the member's audit seat (plant and real
pooled), the care share, the leak per thousand bad deliveries, the population's real lifetime a slot, the suspensions, the standing false approvals, the overhead;
against the reviewer's expectations (the first review claimed under 0.10 on both arms; the pin's audit seat 0.1–0.9; the leak within 1.5× the unstressed under arm 4
and within 2× under the pin; refuted if the first review is claimed above 0.2).  Usage: horizon_read.py OUT.md"""
import json, os, sys, numpy as np
A = "results/redteam/stability/ablation-A1"
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def pooled(S, seat):
    n = sum(S.get(f"seats_{seat}_{k}", 0) or 0 for k in ("plant", "real")); c = sum((S.get(f"claim_rate_{seat}_{k}") or 0) * (S.get(f"seats_{seat}_{k}", 0) or 0) for k in ("plant", "real"))
    return (c / n) if n else np.nan, n
L = ["# The learner with a horizon — the first chains (the pin and arm 4, a temptation of 1, the bond ×1; the slot's own return to its exit at γ 0.98) against the one-decision chains of record and the unstressed\n",
     "Each row a learner's final on seeds 21–40 (the policy of record of its chain; the careful, the stamper, the claimer and the hand on the same slots beside in each eval). "
     "The claim rates pool plant and real cases at the seat; the leak per thousand bad deliveries; the lifetime the population's real lifetime a slot, paired against the careful on the same seeds where both evals carry it.\n",
     "| cell | learner | chain | claim at the first review | at the member's audit seat (seats) | at the panels | care | leak ‰ | lifetime a slot (− careful, paired) | suspensions | FA | overhead |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|"]
res = {}
for k, kn in (("pa10", "the pin"), ("arm4", "arm 4")):
    for lrn, pol in (("direct", "direct"), ("wm", "greedy")):
        for chain, path in (("horizon (mc, γ 0.98)", f"{A}/stress/learned/horizon/{k}-t1-b1-mc/{'wm-ret' if lrn == 'wm' else lrn}/eval/final/eval.json"), ("one decision (record)", f"{A}/stress/learned/{k}-t1-b1/{lrn}/eval/final/eval.json"), ("unstressed (record)", f"{A}/learned/{k}/{lrn}/eval/final/eval.json")):
            if not os.path.exists(path): L.append(f"| {kn} | {lrn} | {chain} | (pending) | | | | | | | | |"); continue
            j = json.load(open(path)); S = j["summary"][pol]; E = j["episodes"][pol]; C = {int(e["seed"]): e for e in j["episodes"]["careful"]}
            fr, _ = pooled(S, "initial"); au, na = pooled(S, "audit"); pa, _ = pooled(S, "panel")
            life = [f(e, "learner_lifetime_real") / f(e, "learner_pop_total") for e in E]; d = [f(e, "learner_lifetime_real") / f(e, "learner_pop_total") - f(C[int(e["seed"])], "learner_lifetime_real") / f(C[int(e["seed"])], "learner_pop_total") for e in E]
            leak = 1000 * mse([f(e, "leak_bad") for e in E])[0]
            r = dict(fr=fr, au=au, na=na, pa=pa, care=S["care_share"][0], leak=leak, life=mse(life), d=mse(d), susp=mse([f(e, "suspensions") for e in E])[0], fa=mse([f(e, "false_approvals") for e in E])[0], oh=mse([f(e, "sys_overhead_per_vested") for e in E])[0])
            res[(k, lrn, chain)] = r
            nn = lambda x, fmt: "—" if x != x else format(x, fmt)
            L.append(f"| {kn} | {lrn} | {chain} | **{nn(fr, '.3f')}** | {nn(au, '.3f')} ({na}) | {nn(pa, '.3f')} | {r['care']:.3f} | {leak:.0f} | {r['life'][0]:.0f} ({r['d'][0]:+.0f} ± {r['d'][1]:.0f}) | {r['susp']:.1f} | {r['fa']:.1f} | {r['oh']:.1f} |")
L.append("\n## Against addendum 10's expectations (J5)\n"); L.append("| cell, learner | the first review claimed under 0.10 | the pin's audit seat still claimed (0.1–0.9) | the leak within 1.5× (arm 4) / 2× (the pin) the unstressed | refuted (the first review above 0.2)? |"); L.append("|---|---|---|---|---|")
for k, kn in (("pa10", "the pin"), ("arm4", "arm 4")):
    for lrn in ("direct", "wm"):
        h = res.get((k, lrn, "horizon (mc, γ 0.98)")); u = res.get((k, lrn, "unstressed (record)"))
        if not h: continue
        mult = 2.0 if k == "pa10" else 1.5
        L.append(f"| {kn}, {lrn} | {'yes' if h['fr'] < 0.10 else 'NO'} ({h['fr']:.3f}) | {('yes' if 0.1 <= h['au'] <= 0.9 else 'NO') if k == 'pa10' else '—'} ({h['au']:.3f}) | {('yes' if (u and h['leak'] <= mult * u['leak']) else 'NO')} ({h['leak']:.0f} against {u['leak'] if u else float('nan'):.0f} × {mult}) | {'**REFUTED**' if h['fr'] > 0.2 else 'no'} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
