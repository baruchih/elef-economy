"""Addendum 13's M4 (November 16, 2026; notes §112): the horizon learners' conduct among careful members, read as the dose. From stress/conduct/ (launch.sh at
25aab307e): for each cell (the pin at π^A 0.10, arm 4) and learner (the direct, the world model's return head), (a) the policy on 1 in 4 of the learner slots and the
careful on the rest, (b) the reverse, the all-careful population on the same seeds (21–60). For each: the careful slots less the policy's slots, real a slot, paired
by seed (± SE); for the policy's slots the claims a slot by seat and by standing (the mix wrapper's tally), the benefit, the suspensions, the audit seats a slot, the
ticks in good standing, the lifetime lost for each claim (the gap over the claims a slot, the delta method); the world's leak and overhead with the all-careful's;
the expectations stated before the run. Usage: conduct_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress/conduct"
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def f0(e, k): v = e.get(k); return float(v) if v not in (None, "") else 0.0      # a seat key the wrapper never wrote is a count of zero
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def groups(e):
    S = json.loads(e["learner_slots_json"]); share = float(e.get("half_share") or 0.5); seed = int(e["seed"]); grp = {"claim": [], "care": []}
    for x, v in S.items():
        h = int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big"); grp["claim" if h < share * 65536 else "care"].append(v)
    return grp
CELLS = [("pa10", "the pin, π^A 0.10"), ("arm4", "arm 4")]; LRN = [("direct", "direct", "the direct"), ("wm", "greedy", "the return head")]
EXP = {"pa10": (100, 450, 100), "arm4": (40, 350, 40)}        # (a): behind by lo..hi and ≥ 2 SE; (b): the careful ahead by at least the third
L = ["# M4 — the horizon learners' conduct among careful members (the four finals frozen, no exploration; seeds 21–60; the all-careful beside)\n",
     "Each row one cell, learner and share. `careful − policy` the careful slots' lifetime a slot (wallet + benefit, real) less the policy's slots', paired by seed ± SE; the policy's slots' claims a slot by seat (first review / member audit / panel) and by standing (member / probation) as rates of the seats held; "
     "the benefit a slot; the suspensions a slot; the audit seats a slot (policy / careful slots); the ticks in good standing a slot (policy / careful); the lifetime lost for each claim (the gap over the claims a slot); the world's standing false approvals, leak per thousand bad deliveries and overhead a vested task, the all-careful's beside.\n",
     "| cell, learner | share on the policy | seeds | **careful − policy, real a slot** | SE from nothing | claim rate: first / audit / panel | claim rate by standing: member / probation | claims a slot | benefit a slot | suspensions a slot: policy / careful | audit seats a slot: policy / careful | good ticks a slot: policy / careful | **lost for each claim** | world FA; leak ‰; overhead (all-careful) |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
V = []
for k, kn in CELLS:
    for sub, pol, ln in LRN:
        p = f"{R}/{k}-{sub}/eval.json"
        if not os.path.exists(p): L.append(f"| {kn}, {ln} | (pending) | | | | | | | | | | | | |"); continue
        j = json.load(open(p)); C = {int(e["seed"]): e for e in j["episodes"]["careful"]}
        for share in ("0.25", "0.75"):
            E = j["episodes"][f"mix:{pol}:{share}"]
            d = [f(e, "half_d_lifetime_per_slot") for e in E]; dm = mse(d)
            cl = [f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E]; ben = [f(e, "half_claim_private_real") / f(e, "half_claim_slots") for e in E]
            sus = [f(e, "half_claim_suspensions") / f(e, "half_claim_slots") for e in E]; susc = [f(e, "half_care_suspensions") / f(e, "half_care_slots") for e in E]
            aud = [f0(e, "half_claim_seats_audit") / f(e, "half_claim_slots") for e in E]; audc = [f0(e, "half_care_seats_audit") / f(e, "half_care_slots") for e in E]
            rate = {s: (sum(f0(e, f"half_claim_claimed_{s}") for e in E) / max(1, sum(f0(e, f"half_claim_seats_{s}") for e in E))) for s in ("initial", "audit", "panel")}
            nseat = {s: sum(f0(e, f"half_claim_seats_{s}") for e in E) / len(E) / np.mean([f(e, "half_claim_slots") for e in E]) for s in ("initial", "audit", "panel")}
            st = {s: (sum(sum(f(e, f"half_claim_claimed_{x}_{s}") if not np.isnan(f(e, f"half_claim_claimed_{x}_{s}")) else 0 for x in ("initial", "audit", "panel", "resumed")) for e in E)
                      / max(1, sum(sum(f(e, f"half_claim_seats_{x}_{s}") if not np.isnan(f(e, f"half_claim_seats_{x}_{s}")) else 0 for x in ("initial", "audit", "panel", "resumed")) for e in E))) for s in ("member", "probation")}
            good, goodc = [], []
            for e in E:
                g = groups(e); good.append(sum(v["ticks_good"] for v in g["claim"]) / max(1, len(g["claim"]))); goodc.append(sum(v["ticks_good"] for v in g["care"]) / max(1, len(g["care"])))
            lost = ratio_se(d, cl)
            w = dict(fa=mse([f(e, "false_approvals") for e in E])[0], leak=1000 * mse([f(e, "leak_bad") for e in E])[0], oh=mse([f(e, "sys_overhead_per_vested") for e in E])[0],
                     fa0=mse([f(C[int(e["seed"])], "false_approvals") for e in E])[0], leak0=1000 * mse([f(C[int(e["seed"])], "leak_bad") for e in E])[0], oh0=mse([f(C[int(e["seed"])], "sys_overhead_per_vested") for e in E])[0])
            L.append(f"| {kn}, {ln} | {'1 in 4 (a)' if share == '0.25' else '3 in 4 (b)'} | {len(d)} | **{dm[0]:+.0f} ± {dm[1]:.0f}** | {dm[0] / dm[1]:.1f} | {rate['initial']:.3f} / {rate['audit']:.3f} / {rate['panel']:.3f} (seats a slot {nseat['initial']:.0f} / {nseat['audit']:.1f} / {nseat['panel']:.1f}) | {st['member']:.3f} / {st['probation']:.3f} | {np.mean(cl):.1f} | {np.mean(ben):.0f} | {np.mean(sus):.2f} / {np.mean(susc):.2f} | {np.mean(aud):.1f} / {np.mean(audc):.1f} | {np.mean(good):.0f} / {np.mean(goodc):.0f} | **{lost[0]:.1f} ± {lost[1]:.1f}** | {w['fa']:.1f}; {w['leak']:.0f}; {w['oh']:.1f} ({w['fa0']:.1f}; {w['leak0']:.0f}; {w['oh0']:.1f}) |")
            V.append((k, kn, ln, share, dm))
L += ["", "## Against the expectations stated before the run\n", "| cell, learner | share | expected | read | |", "|---|---|---|---|---|"]
refuted = []
for k, kn, ln, share, dm in V:
    lo, hi, b = EXP[k]
    if share == "0.25":
        ok = (lo <= dm[0] <= hi) and (dm[0] >= 2 * dm[1]); exp = f"the policy's slots behind by {lo} to {hi}, at least 2 SE"
        if dm[0] < 2 * dm[1]: refuted.append(f"{kn}, {ln}: {dm[0]:+.0f} ± {dm[1]:.0f}")
    else:
        ok = dm[0] >= b; exp = f"the careful slots ahead by at least {b}"
    L.append(f"| {kn}, {ln} | {'1 in 4 (a)' if share == '0.25' else '3 in 4 (b)'} | {exp} | {dm[0]:+.0f} ± {dm[1]:.0f} ({dm[0] / dm[1]:.1f} SE) | {'met' if ok else 'MISSED'} |")
L.append("\n**Refuted if in (a) the policy's slots are level or ahead in any cell** (within two standard errors of nothing, or ahead): " + ("**refuted** — " + "; ".join(refuted) if refuted else "**not refuted** — behind by more than two standard errors in every cell") + ".")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
