"""Addendum 10's J3 from the worlds on record (November 13, 2026; notes §111), no run: (1) the temptation at which a lone skipper draws level in the returning
name's cell (stress/returner/ at 848e1d22c), with its error — the reviewer's arithmetic, one plus the gap at a temptation of 1 over the benefit, confirmed or
corrected two ways (the ratio of the seed means with the delta method's SE; the mean over seeds of each seed's own level temptation); (4) the dosing slots'
benefit a slot in each of the eight dose worlds (stress/dose/ at b5961bf9f), a claim, and the level temptation by the same arithmetic.  Usage: addendum10_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
L = ["# Addendum 10's J3 from the record: the lone skipper's level temptation (J3.1) and the dosing slots' benefit (J3.4)\n",
     "## J3.1 — the temptation at which a lone skipper draws level, in the returning name's cell\n",
     "The operator's lifetime at a temptation T is its wallets carried out plus T × its benefit at 1 (the benefit off the ledger, unread by the scripted policies: §110). "
     "It is level with the careful on the same slot where wallet + T × benefit = the careful's lifetime, so T* = (careful − wallet) / benefit = 1 + (gap at 1) / benefit, with the gap = careful − (wallet + benefit) "
     "and the benefit summed over the operator's names. Two readings over seeds 21–40: the ratio of the seed means (± SE by the delta method over the paired seeds) — the reviewer's arithmetic on the table's figures — "
     "and the mean of each seed's own T* (± SE).\n",
     "| world | policy | gap at 1 (careful − lifetime) | benefit at 1 (summed over the names) | **T\\*, ratio of means** | T\\*, mean of the seeds' own (seeds with a benefit) | seeds level at ≤ 2 | the reviewer's figure |",
     "|---|---|---|---|---|---|---|---|"]
REV = {("pa10", "careful", "claimreturner"): 3.1, ("pa10", "careful", "claimer"): 3.5, ("arm4", "careful", "claimreturner"): 2.5, ("arm4", "careful", "claimer"): 2.7,
       ("pa10", "hand", "claimreturner"): 5.9, ("pa10", "hand", "claimer"): 7.8, ("arm4", "hand", "claimreturner"): 4.7, ("arm4", "hand", "claimer"): 7.7}
for k, kn in (("pa10", "the pin"), ("arm4", "arm 4")):
    for pop, pn in (("careful", "a careful population"), ("hand", "Q1's 60/40 population")):
        j = json.load(open(f"{R}/returner/{k}-{pop}/eval.json")); C = {int(e["seed"]): f(e, "lifetime_real_wealth") for e in j["episodes"]["careful"]}
        for pol in ("claimreturner", "claimer"):
            gaps, bens, ts = [], [], []
            for e in j["episodes"][pol]:
                S = json.loads(e["learner_slots_json"]); b = sum(v["private_real"] for v in S.values()); life = f(e, "lifetime_real_wealth"); g = C[int(e["seed"])] - life
                gaps.append(g); bens.append(b)
                if b > 0: ts.append(1 + g / b)                      # arm 4, the 60/40, seed 38: the slot was never asked (0 decisions, no benefit) — in the means, not in the seeds' own T*
            r = ratio_se(gaps, bens); tm = mse(ts); gm = mse(gaps); bm = mse(bens)
            L.append(f"| {kn}, {pn} | {pol} | {gm[0]:+.0f} ± {gm[1]:.0f} | {bm[0]:.0f} ± {bm[1]:.0f} | **{1 + r[0]:.2f} ± {r[1]:.2f}** | {tm[0]:.2f} ± {tm[1]:.2f} | {sum(t <= 2 for t in ts)} of {len(ts)} | {REV[(k, pop, pol)]} |")
L += ["\n## J3.4 — the dosing slots' benefit a slot in the eight dose worlds\n",
      "The benefit (real, summed over the dosing slots' life, a slot; ± SE over seeds), a claim (the ratio of the seed means), and the level temptation by the same arithmetic — "
      "1 + (the careful group's lifetime a slot − the dosing group's) / the benefit a slot (± SE by the delta method).\n",
      "| arm | dose | dosing slots | benefit a slot (real) | claims a slot | benefit a claim | care − dose at 1 | **T\\*, level at** |", "|---|---|---|---|---|---|---|---|"]
WORLDS = [("pa10", "the pin", "dose0.1", "0.1, every seat"), ("pa10", "the pin", "dose0.3", "0.3, every seat"), ("pa10", "the pin", "dose1", "1, every seat"),
          ("pa10", "the pin", "dose0.3first", "0.3, the first review only"), ("pa10", "the pin", "dose0.3audit", "0.3, the member's audit seat only"),
          ("arm4", "arm 4", "dose0.1", "0.1, every seat"), ("arm4", "arm 4", "dose0.3", "0.3, every seat"), ("arm4", "arm 4", "dose1", "1, every seat")]
for k, kn, d, dn in WORLDS:
    j = json.load(open(f"{R}/dose/{k}-{d}/eval.json")); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; E = j["episodes"][pol]
    ben = [f(e, "half_claim_private_real") / f(e, "half_claim_slots") for e in E]; cl = [f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E]; g = [f(e, "half_d_lifetime_per_slot") for e in E]
    bm = mse(ben); cm = mse(cl); bc = ratio_se([f(e, "half_claim_private_real") for e in E], [f(e, "half_claim_claims") for e in E]); gm = mse(g); ts = ratio_se(g, ben)
    L.append(f"| {kn} | {dn} ({len(E)} seeds) | {mse([f(e, 'half_claim_slots') for e in E])[0]:.1f} | **{bm[0]:.1f} ± {bm[1]:.1f}** | {cm[0]:.1f} ± {cm[1]:.1f} | {bc[0]:.2f} ± {bc[1]:.2f} | {gm[0]:+.0f} ± {gm[1]:.0f} | **{1 + ts[0]:.1f} ± {ts[1]:.1f}** |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
