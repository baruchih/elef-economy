"""Addendum 10's J4 (November 13, 2026; notes §111): the member's audit seat under the stakes, read as the dose — six worlds on arm 0 with π^A held, the dosing slots
1 in 4 with the dose at the member's audit seat alone, a temptation of 1, the all-careful population beside, seeds 21–80 (stress/audit-stakes/ by launch.sh at
f9c0dbb3e). Each world: the careful group's lifetime a slot less the dosing group's (± SE over seeds), the audit seats a slot of both groups, the dosing slots'
benefit a slot, the lifetime lost for each claim (the gap over the claims a slot, ± SE by the delta method), the suspensions; and from the all-careful
populations paired by seed the careful's real lifetime a slot in world 3 against 1 and in world 5 against 4 (the fee's doubling at each rate).  Usage: audit_stakes_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress/audit-stakes"
W = [("w1", "π^A 0.10, ×1, the fee of record, dose 0.3"), ("w2", "π^A 0.10, ×1, the fee of record, dose 1"), ("w3", "π^A 0.10, ×1, the fee doubled, dose 0.3"),
     ("w4", "π^A 0.30, ×1, the fee of record, dose 0.3"), ("w5", "π^A 0.30, ×1, the fee doubled, dose 0.3"), ("w6", "π^A 0.20, ×4, the fee of record, dose 0.3")]
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
L = ["# J4 — the member's audit seat under the stakes, read as the dose (1 slot in 4 dosing at the member's audit seat alone; arm 0, π^A held; a temptation of 1; seeds 21–80)\n",
     "Each row one world; `care − dose` the careful group's lifetime a slot less the dosing group's (± SE over seeds); the all-careful population's lifetime a slot beside (the `careful` policy, the same seeds). "
     "The lifetime lost for each claim is the gap over the dosing slots' claims a slot. The world's standing false approvals, leak per thousand bad deliveries and overhead a vested task, the all-careful world's beside.\n",
     "| world | seeds | **care − dose, real a slot** | dosing: lifetime a slot; alive of ~9.8; suspensions a slot; claims a slot | audit seats a slot: dosing / careful group | **dosing slots' benefit a slot** | careful group: lifetime; suspensions | all-careful: lifetime a slot | **lost for each claim** | world: FA; leak ‰; overhead (all-careful) |",
     "|---|---|---|---|---|---|---|---|---|---|"]
res = {}
for k, kn in W:
    p = f"{R}/{k}/eval.json"
    if not os.path.exists(p): L.append(f"| {k}: {kn} | (pending) | | | | | | | | |"); continue
    j = json.load(open(p)); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; E = j["episodes"][pol]; C = {int(e["seed"]): e for e in j["episodes"]["careful"]}
    g = mse([f(e, "half_d_lifetime_per_slot") for e in E])
    cl = dict(life=mse([f(e, "half_claim_lifetime_per_slot") for e in E])[0], alive=mse([f(e, "half_claim_alive") for e in E])[0], susp=mse([f(e, "half_claim_suspensions") / f(e, "half_claim_slots") for e in E]),
              claims=mse([f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E]), aud=mse([f(e, "half_claim_seats_audit") / f(e, "half_claim_slots") for e in E]),
              ben=mse([f(e, "half_claim_private_real") / f(e, "half_claim_slots") for e in E]))
    ca = dict(life=mse([f(e, "half_care_lifetime_per_slot") for e in E])[0], susp=mse([f(e, "half_care_suspensions") / f(e, "half_care_slots") for e in E]), aud=mse([f(e, "half_care_seats_audit") / f(e, "half_care_slots") for e in E]))
    ref = mse([f(C[int(e["seed"])], "learner_lifetime_real") / f(C[int(e["seed"])], "learner_pop_total") for e in E])
    lost = ratio_se([f(e, "half_d_lifetime_per_slot") for e in E], [f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E])
    w = dict(fa=mse([f(e, "false_approvals") for e in E])[0], leak=1000 * mse([f(e, "leak_bad") for e in E])[0], oh=mse([f(e, "sys_overhead_per_vested") for e in E])[0],
             fa0=mse([f(C[int(e["seed"])], "false_approvals") for e in E])[0], leak0=1000 * mse([f(C[int(e["seed"])], "leak_bad") for e in E])[0], oh0=mse([f(C[int(e["seed"])], "sys_overhead_per_vested") for e in E])[0])
    res[k] = dict(g=g, lost=lost, ref={int(e["seed"]): f(C[int(e["seed"])], "learner_lifetime_real") / f(C[int(e["seed"])], "learner_pop_total") for e in E}, n=len(E))
    L.append(f"| {k}: {kn} | {len(E)} | **{g[0]:+.0f} ± {g[1]:.0f}** | {cl['life']:.0f}; {cl['alive']:.1f}; {cl['susp'][0]:.2f} ± {cl['susp'][1]:.2f}; {cl['claims'][0]:.1f} ± {cl['claims'][1]:.1f} | {cl['aud'][0]:.1f} / {ca['aud'][0]:.1f} | **{cl['ben'][0]:.1f} ± {cl['ben'][1]:.1f}** | "
             f"{ca['life']:.0f}; {ca['susp'][0]:.2f} ± {ca['susp'][1]:.2f} | {ref[0]:.0f} ± {ref[1]:.0f} | **{lost[0]:.1f} ± {lost[1]:.1f}** | {w['fa']:.1f}; {w['leak']:.0f}; {w['oh']:.1f} ({w['fa0']:.1f}; {w['leak0']:.0f}; {w['oh0']:.1f}) |")
L.append("\n## The fee's doubling on the all-careful populations, paired by seed (the careful's real lifetime a slot)\n")
L.append("| step | fee of record | fee doubled | **doubled − record** | in 100 |"); L.append("|---|---|---|---|---|")
pairs = {}
for a, b, nm in (("w1", "w3", "π^A 0.10, ×1"), ("w4", "w5", "π^A 0.30, ×1")):
    if a in res and b in res:
        seeds = sorted(set(res[a]["ref"]) & set(res[b]["ref"])); d = [res[b]["ref"][s] - res[a]["ref"][s] for s in seeds]; m = mse(d); base = np.mean([res[a]["ref"][s] for s in seeds])
        pairs[nm] = (m, base); L.append(f"| {nm} (w{b[1]} against w{a[1]}; {len(seeds)} seeds) | {base:.0f} | {np.mean([res[b]['ref'][s] for s in seeds]):.0f} | **{m[0]:+.0f} ± {m[1]:.0f}** | {100 * m[0] / base:+.1f} ± {100 * m[1] / base:.1f} |")
L.append("\n## Against addendum 10's expectations\n")
L.append("| world | expected | read | |"); L.append("|---|---|---|---|")
EXP = {"w1": ("behind by 10 to 110", lambda g: 10 <= g[0] <= 110), "w2": ("behind by 40 to 200", lambda g: 40 <= g[0] <= 200), "w3": ("behind by at least 50", lambda g: g[0] >= 50),
       "w4": ("behind by at least 40", lambda g: g[0] >= 40), "w5": ("behind by at least 100, and by more than worlds 3, 4 and 6", lambda g: g[0] >= 100 and all(g[0] > res[x]["g"][0] for x in ("w3", "w4", "w6") if x in res)),
       "w6": ("behind by at least 40", lambda g: g[0] >= 40)}
for k, kn in W:
    if k in res:
        g = res[k]["g"]; L.append(f"| {k}: {kn} | {EXP[k][0]} | {g[0]:+.0f} ± {g[1]:.0f} ({g[0] / g[1]:.1f} SE from nothing) | {'met' if EXP[k][1](g) else 'MISSED'} |")
for nm, (m, base) in pairs.items():
    L.append(f"| the careful's lifetime with the fee doubled, {nm} | 2 to 8 in 100 above the fee of record | {100 * m[0] / base:+.1f} ± {100 * m[1] / base:.1f} in 100 | {'met' if 2 <= 100 * m[0] / base <= 8 else 'MISSED'} |")
if "w5" in res:
    g = res["w5"]["g"]; L.append(f"\n**Refuted if the dosing slots in world 5 are level (within two standard errors of nothing):** {g[0]:+.0f} ± {g[1]:.0f} — **{'REFUTED' if g[0] <= 2 * g[1] else 'not refuted'}**.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
