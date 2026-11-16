"""Addendum 14's N3.1 (November 16, 2026; notes §113): M4's first reviews by action for the policy's slots at 1 in 4 — from the four cells run again at 7bd5dd5fc
(launch-actions.sh: the same rollouts, with run_q's tallies by action), every figure of record checked to the digit against stress/conduct/<cell>/eval.json.
For the policy's slots: the first reviews inspected, claimed, approved blind with no claim and rejected blind with no claim (shares of the seats held); the planted
cases failed and the bonds forfeited a slot on each blind kind; the claims made on probation; the lifetime lost for each blind verdict, claimed or not (the gap of
record over the blind verdicts a slot — at the first review, and at every seat); the other seats' split beside.  Usage: conduct_actions_read.py OUT.md"""
import json, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress/conduct"
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else 0.0
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
CH = [("pa10", "direct", "direct", "the pin, the direct"), ("pa10", "wm", "greedy", "the pin, the return head"), ("arm4", "direct", "direct", "arm 4, the direct"), ("arm4", "wm", "greedy", "arm 4, the return head")]
L = ["# M4's first reviews by action — the policy's slots at 1 in 4 (the four finals frozen among careful members; seeds 21–60; the rollouts of record run again with the tallies by action)\n",
     "| cell, learner | reproduced | first reviews a slot | **inspected / claimed / approved blind, no claim / rejected blind, no claim** (shares) | planted cases failed a slot: claimed / approved blind / rejected blind | bonds forfeited a slot (real): inspected / claimed / approved blind / rejected blind | claims on probation (of the claims; the probation first reviews claimed) | blind verdicts a slot: first review / every seat | **lost for each blind verdict: first review / every seat** | **lost for each claim** | the audit seat: inspected / claimed / approved blind / rejected blind (seats a slot) | the panel: the same |",
     "|---|---|---|---|---|---|---|---|---|---|---|---|"]
for k, sub, pol, nm in CH:
    j = json.load(open(f"{R}/{k}-{sub}-actions/eval.json")); E = j["episodes"][f"mix:{pol}:0.25"]; j0 = json.load(open(f"{R}/{k}-{sub}/eval.json")); E0 = {int(e["seed"]): e for e in j0["episodes"][f"mix:{pol}:0.25"]}
    same = all(abs(f(e, "half_d_lifetime_per_slot") - f(E0[int(e["seed"])], "half_d_lifetime_per_slot")) < 1e-9 and f(e, "half_claim_claims") == f(E0[int(e["seed"])], "half_claim_claims") for e in E)
    n = np.array([f(e, "half_claim_slots") for e in E]); d = [f(e, "half_d_lifetime_per_slot") for e in E]
    A = {a: np.array([f(e, f"half_claim_act{a}_initial") for e in E]) for a in range(4)}; seats = sum(A.values())
    PF = {a: np.array([f(e, f"half_claim_pfail{a}_initial") for e in E]) for a in (1, 2, 3)}; BL = {a: np.array([f(e, f"half_claim_bondlost{a}_initial") for e in E]) for a in range(4)}
    claims = np.array([f(e, "half_claim_claims") for e in E]); cp = np.array([f(e, "half_claim_claimed_initial_probation") for e in E]); sp = np.array([f(e, "half_claim_seats_initial_probation") for e in E])
    blind_first = A[1] + A[2] + A[3]; blind_all = sum(np.array([f(e, f"half_claim_act{a}_{s}") for e in E]) for a in (1, 2, 3) for s in ("initial", "audit", "panel", "resumed"))
    lf = ratio_se(d, blind_first / n); la = ratio_se(d, blind_all / n); lc = ratio_se(d, claims / n)
    def seatrow(s):
        B = {a: np.array([f(e, f"half_claim_act{a}_{s}") for e in E]) for a in range(4)}; tot = sum(B.values())
        return "—" if tot.sum() == 0 else " / ".join(f"{B[a].sum() / tot.sum():.2f}" for a in range(4)) + f" ({tot.sum() / n.sum():.1f})"
    L.append(f"| {nm} | {'to the digit' if same else '**DIFFERS**'} | {seats.sum() / n.sum():.0f} | **{A[0].sum() / seats.sum():.3f} / {A[3].sum() / seats.sum():.3f} / {A[1].sum() / seats.sum():.3f} / {A[2].sum() / seats.sum():.3f}** | {PF[3].sum() / n.sum():.2f} / {PF[1].sum() / n.sum():.2f} / {PF[2].sum() / n.sum():.2f} | "
             f"{BL[0].sum() / n.sum():.1f} / {BL[3].sum() / n.sum():.1f} / {BL[1].sum() / n.sum():.1f} / {BL[2].sum() / n.sum():.1f} | {cp.sum() / max(1, A[3].sum()):.2f} ({cp.sum() / max(1, sp.sum()):.3f}) | {blind_first.sum() / n.sum():.1f} / {blind_all.sum() / n.sum():.1f} | **{lf[0]:.1f} ± {lf[1]:.1f} / {la[0]:.1f} ± {la[1]:.1f}** | {lc[0]:.1f} ± {lc[1]:.1f} | {seatrow('audit')} | {seatrow('panel')} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
