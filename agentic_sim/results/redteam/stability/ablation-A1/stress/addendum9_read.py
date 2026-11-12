"""Addendum 9's readings from the worlds on record (I3.2–I3.5; November 12, 2026; notes §110): (2) the standard error of the careful group's suspensions a
slot at each share, beside the all-careful's; (3) the group figures averaged one way (the mean over seeds of each per-seed per-slot figure) so the lifetime is
the wallet plus the benefit to the unit; (4) the temptation at which the claiming group draws level with the careful, read by scaling the benefit — off the
ledger and unread by the frozen policies — T* = (the careful group's lifetime a slot − the claiming group's wallet a slot) / the claiming group's benefit a
slot at a temptation of 1, ± SE by the ratio's delta method over seeds; (5) the honest side in real terms paired by seed over §106's and addendum 8's cells
(payoff/honest/): the slots' real lifetime and the surplus deflated by the cell's own price level (× P_0/P_t, P_0 = 20).  Usage: addendum9_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
FIX = "-at-4df18f1bc"
ARMS = [("pa10", "the pin"), ("arm4", "arm 4")]; LEARN = [("direct", "direct", "mix:direct"), ("wm", "head alone", "mix:greedy")]; SHARES = [0.1, 0.25, 0.5, 0.75]
def load(k, l, s, pol):
    d = f"{R}/f41/{k}-{l}" if s == 0.5 else f"{R}/entry/{k}-{l}-s{s}"
    if os.path.exists(f"{d}{FIX}/eval.json"): d += FIX
    return json.load(open(f"{d}/eval.json"))["episodes"][pol if s == 0.5 else f"{pol}:{s}"]
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return x.mean(), x.std(ddof=1) / np.sqrt(len(x))
L = ["# Addendum 9's readings from the worlds on record (I3.2–I3.5)\n"]
# (2) and (3) and (4)
L.append("## I3.2–I3.4 — the entry test's worlds (the halves at 0.5 F4.1's), every figure the mean over seeds 21–40 of the per-seed per-slot figure, ± SE over seeds\n")
L.append("| arm, learner | share | careful: suspensions a slot | all-careful: suspensions a slot | claiming: lifetime a slot = wallet + benefit (each a per-seed mean) | claiming: suspensions a slot | careful: lifetime a slot | **T\\*: the temptation at which the claiming group is level** |")
L.append("|---|---|---|---|---|---|---|---|")
for k, kn in ARMS:
    ref = json.load(open(f"{R}/learned/{k}-t1-b1/direct/eval/final/eval.json"))["episodes"]["careful"]
    rs = mse([f(e, "suspensions") / f(e, "learner_pop_total") for e in ref])
    for l, ln, pol in LEARN:
        for s in SHARES:
            E = load(k, l, s, pol)
            cs = mse([f(e, "half_care_suspensions") / f(e, "half_care_slots") for e in E])
            ks = mse([f(e, "half_claim_suspensions") / f(e, "half_claim_slots") for e in E])
            life = mse([f(e, "half_claim_lifetime_per_slot") for e in E]); wal = mse([f(e, "half_claim_wealth_per_slot") for e in E])
            ben = mse([f(e, "half_claim_private_real") / f(e, "half_claim_slots") for e in E]); cl = mse([f(e, "half_care_lifetime_per_slot") for e in E])
            gap = np.array([f(e, "half_care_lifetime_per_slot") - f(e, "half_claim_wealth_per_slot") for e in E]); b = np.array([f(e, "half_claim_private_real") / f(e, "half_claim_slots") for e in E])
            n = len(E); g, bb = gap.mean(), b.mean(); T = g / bb
            cov = np.cov(gap, b, ddof=1); seT = T * np.sqrt(cov[0, 0] / g**2 + cov[1, 1] / bb**2 - 2 * cov[0, 1] / (g * bb)) / np.sqrt(n)
            L.append(f"| {kn}, {ln} | {s} | {cs[0]:.3f} ± {cs[1]:.3f} | {rs[0]:.3f} ± {rs[1]:.3f} | {life[0]:.0f} = {wal[0]:.0f} + {ben[0]:.0f} | {ks[0]:.2f} ± {ks[1]:.2f} | {cl[0]:.0f} ± {cl[1]:.0f} | **{T:.1f} ± {seT:.1f}** |")
# (5) the honest side in real terms, paired by seed
L.append("\n## I3.5 — the honest side in real terms, paired by seed (ten seeds, 21–30; the careful population in each stake's cell)\n")
L.append("| step | cells (B − A) | the slots' real lifetime, B − A | the surplus deflated by each cell's P_t (× 20/P_t), B − A | the nominal surplus, B − A | P_t: A → B |")
L.append("|---|---|---|---|---|---|")
H = f"{R}/payoff/honest"
def ep(c): return {int(e["seed"]): e for e in json.load(open(f"{H}/{c}/eval.json"))["episodes"]["careful"]}
def pair(a, b):
    A, B = ep(a), ep(b); seeds = sorted(set(A) & set(B))
    life = mse([f(B[s], "learner_lifetime_real") - f(A[s], "learner_lifetime_real") for s in seeds])
    defl = mse([f(B[s], "pop_surplus_nominal") * 20 / f(B[s], "P_t") - f(A[s], "pop_surplus_nominal") * 20 / f(A[s], "P_t") for s in seeds])
    nom = mse([f(B[s], "pop_surplus_nominal") - f(A[s], "pop_surplus_nominal") for s in seeds])
    pa, pb = np.mean([f(A[s], "P_t") for s in seeds]), np.mean([f(B[s], "P_t") for s in seeds])
    return f"{life[0]:+,.0f} ± {life[1]:,.0f}", f"{defl[0]:+,.0f} ± {defl[1]:,.0f}", f"{nom[0]:+,.0f} ± {nom[1]:,.0f}", f"{pa:.1f} → {pb:.1f}"
STEPS = [("the fee's doubling, π^A 0.20 ×2", "pa20-t1-b2", "pa20-t1-b2-w3"), ("the fee's doubling, π^A 0.20 ×4", "pa20-t1-b4", "pa20-t1-b4-w3"),
         ("the fee's doubling, π^A 0.30 ×1", "pa30-t1-b1", "pa30-t1-b1-w3"), ("the fee's doubling, π^A 0.30 ×2", "pa30-t1-b2", "pa30-t1-b2-w3"), ("the fee's doubling, π^A 0.30 ×4", "pa30-t1-b4", "pa30-t1-b4-w3"),
         ("π^A 0.20 → 0.30, ×1", "pa20-t1-b1", "pa30-t1-b1"), ("π^A 0.20 → 0.30, ×2", "pa20-t1-b2", "pa30-t1-b2"), ("π^A 0.20 → 0.30, ×4", "pa20-t1-b4", "pa30-t1-b4"),
         ("π^A 0.20 → 0.30, ×2, the weight 3", "pa20-t1-b2-w3", "pa30-t1-b2-w3"), ("π^A 0.20 → 0.30, ×4, the weight 3", "pa20-t1-b4-w3", "pa30-t1-b4-w3"),
         ("π^A 0.10 → 0.20, ×1 (§106's cells)", "pa10-t1-b1", "pa20-t1-b1"), ("π^A 0.10 → 0.30, ×1", "pa10-t1-b1", "pa30-t1-b1"), ("π^A 0.10 ×1 → 0.30 ×1 with the fee at 3 f", "pa10-t1-b1", "pa30-t1-b1-w3")]
for name, a, b in STEPS:
    L.append(f"| {name} | {b} − {a} | " + " | ".join(pair(a, b)) + " |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
