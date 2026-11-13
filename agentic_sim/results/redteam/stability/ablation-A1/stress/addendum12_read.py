"""Addendum 12's L3.1 from the record (November 13, 2026; notes §111): claims for each suspension — for the dosing slots of §110's eight dose worlds (stress/dose/)
and the claiming slots of the entry test at 1 in 10 (stress/entry/*-at-b5961bf9f), the claims a slot makes for each suspension (the group's claims over its
suspensions, the ratio of the seed means ± SE by the delta method) and the benefit it saves between two suspensions (the group's benefit over its suspensions),
beside the claims, the suspensions and the benefit a slot.  Usage: addendum12_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
W = [("entry/pa10-direct-s0.1-at-b5961bf9f", "the entry test, the pin, direct, 1 in 10"), ("entry/pa10-wm-s0.1-at-b5961bf9f", "the entry test, the pin, head alone, 1 in 10"), ("entry/arm4-direct-s0.1-at-b5961bf9f", "the entry test, arm 4, direct, 1 in 10"), ("entry/arm4-wm-s0.1-at-b5961bf9f", "the entry test, arm 4, head alone, 1 in 10"),
     ("dose/pa10-dose0.1", "the dose, the pin, 0.1 at every seat"), ("dose/pa10-dose0.3", "the dose, the pin, 0.3 at every seat"), ("dose/pa10-dose1", "the dose, the pin, 1 at every seat"), ("dose/pa10-dose0.3first", "the dose, the pin, 0.3 at the first review only"), ("dose/pa10-dose0.3audit", "the dose, the pin, 0.3 at the member's audit seat only"),
     ("dose/arm4-dose0.1", "the dose, arm 4, 0.1 at every seat"), ("dose/arm4-dose0.3", "the dose, arm 4, 0.3 at every seat"), ("dose/arm4-dose1", "the dose, arm 4, 1 at every seat")]
L = ["# L3.1 — claims for each suspension, and the benefit saved between two suspensions (the claiming / dosing slots; from the record)\n",
     "| world | seeds | claims a slot | suspensions a slot | benefit a slot (real) | **claims for each suspension** | **benefit between two suspensions (real, at a temptation of 1)** | slots never suspended (of the group) |", "|---|---|---|---|---|---|---|---|"]
for d, name in W:
    j = json.load(open(f"{R}/{d}/eval.json")); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; E = j["episodes"][pol]
    cl, su, be, ns, n = [], [], [], 0, 0
    for e in E:
        S = json.loads(e["learner_slots_json"]); share = float(e.get("half_share") or 0.5); seed = int(e["seed"])
        V = [v for x, v in S.items() if int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big") < share * 65536]
        cl.append(sum(v["claims"] for v in V) / len(V)); su.append(sum(v["suspensions"] for v in V) / len(V)); be.append(sum(v["private_real"] for v in V) / len(V)); ns += sum(v["suspensions"] == 0 for v in V); n += len(V)
    cs = ratio_se(cl, su); bs = ratio_se(be, su)
    L.append(f"| {name} | {len(E)} | {mse(cl)[0]:.1f} ± {mse(cl)[1]:.1f} | {mse(su)[0]:.2f} ± {mse(su)[1]:.2f} | {mse(be)[0]:.0f} ± {mse(be)[1]:.0f} | **{cs[0]:.1f} ± {cs[1]:.1f}** | **{bs[0]:.0f} ± {bs[1]:.0f}** | {ns} of {n} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
