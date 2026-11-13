"""Addendum 12's L3.2 (November 13, 2026; notes §111): what an admission costs and pays — for a careful arrival in the stressed world (the all-careful population
in the pin's cell and arm 4's, a temptation of 1, the bond ×1; stress/admission/ by launch.sh), from its arrival to its admission: the reviews, the ticks, the care
bought (the Tally's costs at admission, real at the admission's index), the fees and the allowances received (the fixed fees, the uplift, the emission; the
reimbursements), and the net; over every arrival-born slot admitted in the run, ± SE over seeds (each seed's admitted arrivals averaged). Against the reviewer's
expectations: 40–150 reviews; 100–400 real of care; the care covered by what is received.  Usage: admission_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress/admission"
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
L = ["# L3.2 — what an admission costs and pays: a careful arrival from its arrival to its admission (the all-careful population; seeds 21–40)\n",
     "| world | arrivals a run; admitted; never admitted (alive at the end / departed) | ticks to admission | reviews | care bought (real) | reimbursed (real) | fees: fixed + uplift + emission (real) | bonds forfeited (real) | **received − care bought (real)** | wallet at admission (nominal) |",
     "|---|---|---|---|---|---|---|---|---|---|"]
checks = {}
for k, kn in (("pa10", "the pin"), ("arm4", "arm 4")):
    p = f"{R}/{k}-careful/eval.json"
    if not os.path.exists(p): L.append(f"| {kn} | (pending) | | | | | | | | |"); continue
    j = json.load(open(p)); E = j["episodes"]["careful"]
    arr, adm, na_alive, na_gone, tk, rv, care, reimb, fees, bonds, net, wal = ([] for _ in range(12))
    for e in E:
        S = json.loads(e["learner_slots_json"]); A = [v for v in S.values() if v["t_in"] > 0]; D = [v for v in A if "adm_t" in v]
        arr.append(len(A)); adm.append(len(D)); na_alive.append(sum(1 for v in A if "adm_t" not in v and v["alive"])); na_gone.append(sum(1 for v in A if "adm_t" not in v and not v["alive"]))
        if D:
            r = lambda v: v["adm_real"]
            tk.append(np.mean([v["adm_ticks"] for v in D])); rv.append(np.mean([v["adm_reviews"] for v in D])); care.append(np.mean([v["adm_costs"] * r(v) for v in D])); reimb.append(np.mean([v["adm_reimbursed"] * r(v) for v in D]))
            fees.append(np.mean([v["adm_fees"] * r(v) for v in D])); bonds.append(np.mean([v["adm_bonds_forfeited"] * r(v) for v in D])); net.append(np.mean([(v["adm_reimbursed"] + v["adm_fees"] - v["adm_costs"] - v["adm_bonds_forfeited"]) * r(v) for v in D])); wal.append(np.mean([v["adm_wealth_nominal"] for v in D]))
    m = {k2: mse(v) for k2, v in dict(tk=tk, rv=rv, care=care, reimb=reimb, fees=fees, bonds=bonds, net=net, wal=wal).items()}
    checks[kn] = m
    L.append(f"| {kn} | {np.mean(arr):.1f}; {np.mean(adm):.1f}; {np.mean(na_alive):.1f} / {np.mean(na_gone):.1f} | {m['tk'][0]:.0f} ± {m['tk'][1]:.0f} | **{m['rv'][0]:.1f} ± {m['rv'][1]:.1f}** | **{m['care'][0]:.0f} ± {m['care'][1]:.0f}** | {m['reimb'][0]:.0f} ± {m['reimb'][1]:.0f} | {m['fees'][0]:.0f} ± {m['fees'][1]:.0f} | {m['bonds'][0]:.1f} ± {m['bonds'][1]:.1f} | **{m['net'][0]:+.0f} ± {m['net'][1]:.0f}** | {m['wal'][0]:.0f} |")
L.append("\n## Against addendum 12's expectations\n| world | 40 to 150 reviews | 100 to 400 real of care | the care covered by what is received |\n|---|---|---|---|")
for kn, m in checks.items():
    L.append(f"| {kn} | {'met' if 40 <= m['rv'][0] <= 150 else 'MISSED'} ({m['rv'][0]:.1f}) | {'met' if 100 <= m['care'][0] <= 400 else 'MISSED'} ({m['care'][0]:.0f}) | {'met' if m['net'][0] >= 0 else 'MISSED'} ({m['net'][0]:+.0f} ± {m['net'][1]:.0f}) |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
