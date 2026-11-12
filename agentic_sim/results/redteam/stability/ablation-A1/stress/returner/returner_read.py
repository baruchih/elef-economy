"""Addendum 9's name that returns (I4.2; November 12, 2026; notes §110): the operator (`claimreturner` — claim at every review seat, leave at the first
boundary at which it is suspended, return at once under a fresh name with the bank's loan and a probationer's standing) in Q1's re-arrival cell, beside the
careful on the same slot and the `claimer` that never leaves (paired by seed, seeds 21–40), in a careful population and in Q1's 60/40 population, on the pin
and arm 4 at a temptation of 1 and the bond ×1. Read for the operator over the run: the names used, the wallets carried out (summed, real), the private
benefit (summed, real; a name), the bank's loans to its names (lent, repaid from income, recovered at departure, defaulted; nominal), the seats its names
took (reviews, awards) and the plants it met (its suspensions); a temptation of 2 by scaling the benefit (off the ledger, unread by the scripted policies);
and for the loop the leak, the overhead and the bank's names line with the operator against without (the careful on the slot).  Usage: returner_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress/returner"
WORLDS = [("pa10", "the pin"), ("arm4", "arm 4")]; POPS = [("careful", "a careful population"), ("hand", "Q1's 60/40 population")]
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return x.mean(), x.std(ddof=1) / np.sqrt(len(x))
L = ["# The name that returns (I4.2): an operator in Q1's re-arrival cell — claim at every seat, leave once suspended, return under a fresh name\n",
     "Each row one policy on the learner's slot in one world (seeds 21–40): the lifetime real wealth summed across its names (the take-outs, the live name net of its loan, the private benefit), paired against the careful on the same slot; the names used; "
     "the wallets carried out and the benefit (real, summed over the run; the benefit a name); the bank's loans to its names (nominal); its names' reviews, awards and suspensions; the lifetime at a temptation of 2 (the benefit doubled) paired against the careful; "
     "the world's leak per thousand bad deliveries, overhead a vested task and the bank's defaults on names, with the careful's world beside.\n",
     "| arm, population | policy | lifetime (real) | **paired − careful** | names | carried out; benefit (a name) | loans: lent; repaid; recovered; defaulted | reviews; awards; suspensions | **at a temptation of 2: paired − careful** | world: leak ‰; overhead; names defaulted (careful's world) |",
     "|---|---|---|---|---|---|---|---|---|---|"]
checks = []
for k, kn in WORLDS:
    for pop, pn in POPS:
        p = f"{R}/{k}-{pop}/eval.json"
        if not os.path.exists(p): L.append(f"| {kn}, {pn} | (pending) | | | | | | | | |"); continue
        j = json.load(open(p)); C = {int(e["seed"]): e for e in j["episodes"]["careful"]}
        for pol in ("claimreturner", "claimer", "careful"):
            E = j["episodes"][pol]
            life = mse([f(e, "lifetime_real_wealth") for e in E]); d = mse([f(e, "lifetime_real_wealth") - f(C[int(e["seed"])], "lifetime_real_wealth") for e in E])
            names = mse([f(e, "learner_identities") for e in E])
            out, ben, lent, rep, rec, dfl, rev, aw, su, benn, live = ([] for _ in range(11))
            d2 = []
            for e in E:
                S = json.loads(e["learner_slots_json"]); V = list(S.values())
                o = sum(v["wealth_real"] for v in V if not v["alive"]); b = sum(v["private_real"] for v in V)
                out.append(o); ben.append(b); benn.append(b / len(V)); live.append(sum(v["wealth_real"] for v in V if v["alive"]))
                lent.append(sum(v["loan_repaid"] + v["loan_recovered"] + v["loan_defaulted"] + (v["loan_outstanding"] if v["alive"] else 0.0) for v in V)); rep.append(sum(v["loan_repaid"] for v in V)); rec.append(sum(v["loan_recovered"] for v in V)); dfl.append(sum(v["loan_defaulted"] for v in V))
                rev.append(sum(v["reviews"] for v in V)); aw.append(sum(v["awards"] for v in V)); su.append(sum(v["suspensions"] for v in V))
                d2.append(f(e, "lifetime_real_wealth") + b - f(C[int(e["seed"])], "lifetime_real_wealth"))
            dd2 = mse(d2)
            # the first name (a genesis member with its wallet) apart from the returning names (arrival-born under the loan): what each carries out, its benefit, its ticks in place
            first_out, ret_out, ret_n, ret_ben, ret_ticks, ret_rev, ret_susp, ret_adm = ([] for _ in range(8))
            for e in E:
                S = json.loads(e["learner_slots_json"]); V = list(S.values()); F = [v for v in V if v["t_in"] == 0]; Rn = [v for v in V if v["t_in"] > 0]
                first_out.append(sum(v["wealth_real"] for v in F if not v["alive"])); ret_out.append(sum(v["wealth_real"] for v in Rn if not v["alive"]) + sum(v["wealth_real"] for v in Rn if v["alive"]))
                ret_n.append(len(Rn)); ret_ben.append(sum(v["private_real"] for v in Rn) / len(Rn) if Rn else np.nan); ret_ticks.append(np.mean([v["ticks"] for v in Rn]) if Rn else np.nan)
                ret_rev.append(np.mean([v["reviews"] for v in Rn]) if Rn else np.nan); ret_susp.append(np.mean([v["suspensions"] for v in Rn]) if Rn else np.nan); ret_adm.append(np.mean([v["awards"] for v in Rn]) if Rn else np.nan)
            split = f"the first name carries out {np.mean(first_out):.0f}; the {np.mean(ret_n):.1f} returning names carry out {np.mean(ret_out):.0f} in all, each {np.nanmean(ret_ben):.0f} of benefit over {np.nanmean(ret_ticks):.0f} ticks, {np.nanmean(ret_rev):.1f} reviews, {np.nanmean(ret_adm):.1f} awards, {np.nanmean(ret_susp):.2f} suspensions"
            w = dict(leak=1000 * mse([f(e, "leak_bad") for e in E])[0], oh=mse([f(e, "sys_overhead_per_vested") for e in E])[0], dfl=mse([f(e, "names_defaulted") for e in E])[0],
                     leak0=1000 * mse([f(C[int(e["seed"])], "leak_bad") for e in E])[0], oh0=mse([f(C[int(e["seed"])], "sys_overhead_per_vested") for e in E])[0], dfl0=mse([f(C[int(e["seed"])], "names_defaulted") for e in E])[0])
            L.append(f"| {kn}, {pn} | {pol} | {life[0]:.0f} ± {life[1]:.0f} | **{d[0]:+.0f} ± {d[1]:.0f}** | {names[0]:.1f} ± {names[1]:.1f} | {np.mean(out):.0f}; {np.mean(ben):.0f} ({np.mean(benn):.0f}) | {np.mean(lent):.0f}; {np.mean(rep):.0f}; {np.mean(rec):.0f}; {np.mean(dfl):.0f} | "
                     f"{np.mean(rev):.0f}; {np.mean(aw):.0f}; {np.mean(su):.1f} | **{dd2[0]:+.0f} ± {dd2[1]:.0f}** | {w['leak']:.0f}; {w['oh']:.1f}; {w['dfl']:.0f} ({w['leak0']:.0f}; {w['oh0']:.1f}; {w['dfl0']:.0f}) |")
            if pol == "claimreturner": checks.append((kn, pn, d, names, np.mean(out), np.mean(benn), dd2)); L.append(f"| | *{pol}, the names apart* | {split} | | | | | | | |")
L.append("\n## Against addendum 9's expectations\n")
L.append("| arm, population | behind the careful by ≥ 300 at a temptation of 1 | names carry out about nothing | benefit under 40 a name | 5–15 names a run | at 2 still behind | refuted (level or ahead at 1)? |")
L.append("|---|---|---|---|---|---|---|")
for kn, pn, d, names, out, benn, dd2 in checks:
    L.append(f"| {kn}, {pn} | {'yes' if d[0] <= -300 else 'NO'} ({d[0]:+.0f} ± {d[1]:.0f}) | {out:.0f} real carried out | {'yes' if benn < 40 else 'NO'} ({benn:.0f}) | {'yes' if 5 <= names[0] <= 15 else 'NO'} ({names[0]:.1f}) | {'yes' if dd2[0] < -2 * dd2[1] else 'NO'} ({dd2[0]:+.0f} ± {dd2[1]:.0f}) | {'REFUTED' if d[0] >= -2 * d[1] else 'no'} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
