"""Addendum 13's M3 from the record (November 16, 2026; notes §112): (1) K3 like for like — the careful slot's income in good standing less the skipping slot's
good-standing rate (benefit included) over the careful's good-standing ticks, paired by seed with its error, the level temptation on it by J3.1's form (one plus the
gap over the benefit the skipper would earn at its good-standing benefit rate over the same ticks), and what the lifetime of record carries beyond the two
states' income and benefit; (2) the lifetime with the reservation counted — each group's lifetime a slot with the ticks from a departure to the run's end at the
reservation (0.8 real a tick), nothing before an arrival, the gap and the level temptation on it; (3) J3.3's level temptation at the first suspension (one plus the
gap at that tick over the benefit by then), per seed with its error, and whether the first name is a genesis member; (6) J4 against the all-careful population,
paired by seed, and the level temptation at the seat by J3.4's form; and the three sentences of §111 read against their tables (the slots never suspended,
J4's overhead against the all-careful's, the good-standing rate under the careful's). All from stress/standing/, stress/returner2/ and stress/audit-stakes/.
Usage: addendum13_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
T = 1000; RES = 0.8
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
WORLDS = [("entry-pa10-direct-s0.1", "the entry test, the pin, direct, 1 in 10"), ("entry-pa10-wm-s0.1", "the entry test, the pin, head alone, 1 in 10"),
          ("entry-arm4-direct-s0.1", "the entry test, arm 4, direct, 1 in 10"), ("entry-arm4-wm-s0.1", "the entry test, arm 4, head alone, 1 in 10"),
          ("dose-pa10-dose0.1", "the dose, the pin, 0.1 at every seat"), ("dose-pa10-dose0.3", "the dose, the pin, 0.3 at every seat"), ("dose-pa10-dose1", "the dose, the pin, 1 at every seat"),
          ("dose-pa10-dose0.3first", "the dose, the pin, 0.3 at the first review only"), ("dose-pa10-dose0.3audit", "the dose, the pin, 0.3 at the member's audit seat only"),
          ("dose-arm4-dose0.1", "the dose, arm 4, 0.1 at every seat"), ("dose-arm4-dose0.3", "the dose, arm 4, 0.3 at every seat"), ("dose-arm4-dose1", "the dose, arm 4, 1 at every seat")]
def groups(e):
    S = json.loads(e["learner_slots_json"]); share = float(e.get("half_share") or 0.5); seed = int(e["seed"]); grp = {"claim": [], "care": []}
    for x, v in S.items():
        h = int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big"); grp["claim" if h < share * 65536 else "care"].append(v)
    return grp
def life(v): return v["wealth_real"] + v["private_real"]
def after(v): return (T - v["t_out"]) if (not v["alive"] and v["t_out"] is not None and v["t_out"] < T) else 0   # the ticks from a departure to the run's end
L = ["# Addendum 13's M3 from the record (November 16, 2026)\n"]
L += ["## 1. K3 like for like — the careful slot's income in good standing less the skipping slot's good-standing rate over the careful's good-standing ticks (paired by seed)\n",
      "Per seed: each group's figures a slot (the group's sum over its slots divided by its slots); `rate` the claiming group's (income + benefit) in good standing over its ticks in good standing; the gap = the careful group's income in good standing − rate × the careful group's ticks in good standing; "
      "the level temptation = 1 + gap / (the claiming group's benefit a good tick × the careful group's good ticks) — J3.1's form. ± SE over seeds; the temptation's by the delta method on the ratio of seed means. The last two columns: what the lifetime of record carries beyond the two states' income and benefit (lifetime − income good − income down − benefit good − benefit down), each group a slot, and of it the part on the slots in place from tick 0 (the genesis wallets).\n",
      "| world | seeds | careful: income good; good ticks | skipper: rate a good tick; benefit a good tick | **gap (careful − like for like)** | **level temptation** | beyond the two states: skipper / careful | of it on the genesis slots: skipper / careful |", "|---|---|---|---|---|---|---|---|"]
L2 = ["## 2. The lifetime with the reservation counted (the ticks from a departure to the run's end at 0.8 real a tick; nothing before an arrival)\n",
      "| world | seeds | skipping group: lifetime of record → with the reservation (ticks after a departure, a slot) | careful group: the same | **gap of record → with the reservation** | **level temptation of record → with the reservation** |", "|---|---|---|---|---|---|"]
SENT = ["## The three sentences against their tables\n", "| world | claiming slots never suspended (of the group) | the skipper's good-standing rate under the careful's (in 100) |", "|---|---|---|"]
RESID = []
for new, name in WORLDS:
    j = json.load(open(f"{R}/standing/{new}/eval.json")); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; E = j["episodes"][pol]
    gap, temp_num, temp_den, ig_c, good_c, rate_s, brate_s = [], [], [], [], [], [], []
    beyond = {"claim": [], "care": []}; gen_share = {"claim": [], "care": []}; lrec = {"claim": [], "care": []}; lres = {"claim": [], "care": []}; gone_after = {"claim": [], "care": []}
    ben, rate_c = [], []; ns, n_slots = 0, 0
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"]: continue
        row = {}
        for k, V in g.items():
            n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; idn = sum(v["income_down"] for v in V) / n
            bg = sum(v["benefit_good"] for v in V) / n; bd = sum(v["benefit_down"] for v in V) / n; lf = sum(life(v) for v in V) / n
            row[k] = dict(good=good, ig=ig, bg=bg, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=lf, beyond=lf - ig - idn - bg - bd)   # a group with no good tick on a seed reads nan (dropped from the means)
            beyond[k].append(row[k]["beyond"]); lrec[k].append(lf); lres[k].append(sum(life(v) + RES * after(v) for v in V) / n); gone_after[k].append(sum(after(v) for v in V) / n)
            gen_share[k].append(sum(life(v) - v["income_good"] - v["income_down"] - v["benefit_good"] - v["benefit_down"] for v in V if v["t_in"] == 0) / n)
        c, s = row["care"], row["claim"]
        gap.append(c["ig"] - s["rate"] * c["good"]); temp_num.append(gap[-1]); temp_den.append(s["brate"] * c["good"])
        ig_c.append(c["ig"]); good_c.append(c["good"]); rate_s.append(s["rate"]); brate_s.append(s["brate"]); rate_c.append(c["rate"]); ben.append(sum(v["private_real"] for v in g["claim"]) / len(g["claim"]))
        ns += sum(v["suspensions"] == 0 for v in g["claim"]); n_slots += len(g["claim"])
    gm = mse(gap); tr = ratio_se(temp_num, temp_den)
    n_ok = int((~np.isnan(np.array(gap))).sum())
    L.append(f"| {name} | {len(gap)}{'' if n_ok == len(gap) else f' ({n_ok} with a good tick in both groups)'} | {np.mean(ig_c):.0f}; {np.mean(good_c):.0f} | {np.nanmean(rate_s):.3f}; {np.nanmean(brate_s):.3f} | **{gm[0]:+.0f} ± {gm[1]:.0f}** | **{1 + tr[0]:.1f} ± {tr[1]:.1f}** | {np.mean(beyond['claim']):.0f} / {np.mean(beyond['care']):.0f} | {np.mean(gen_share['claim']):.0f} / {np.mean(gen_share['care']):.0f} |")
    for k in ("claim", "care"):                                                  # the residual a slot by kind, pooled over the world's slots: the genesis slots (t_in 0) against the arrivals
        gen = [life(v) - v["income_good"] - v["income_down"] - v["benefit_good"] - v["benefit_down"] for e in E for v in groups(e)[k] if v["t_in"] == 0]
        arr = [life(v) - v["income_good"] - v["income_down"] - v["benefit_good"] - v["benefit_down"] for e in E for v in groups(e)[k] if v["t_in"] > 0]
        RESID.append((name, k, len(gen), np.mean(gen) if gen else np.nan, len(arr), np.mean(arr) if arr else np.nan))
    d_rec = np.array(lrec["care"]) - np.array(lrec["claim"]); d_res = np.array(lres["care"]) - np.array(lres["claim"]); b = np.array(ben)
    t_rec = ratio_se(d_rec, b); t_res = ratio_se(d_res, b)
    L2.append(f"| {name} | {len(b)} | {np.mean(lrec['claim']):.0f} → {np.mean(lres['claim']):.0f} ({np.mean(gone_after['claim']):.0f}) | {np.mean(lrec['care']):.0f} → {np.mean(lres['care']):.0f} ({np.mean(gone_after['care']):.0f}) | **{mse(d_rec)[0]:+.0f} ± {mse(d_rec)[1]:.0f} → {mse(d_res)[0]:+.0f} ± {mse(d_res)[1]:.0f}** | **{1 + t_rec[0]:.1f} ± {t_rec[1]:.1f} → {1 + t_res[0]:.1f} ± {t_res[1]:.1f}** |")
    SENT.append(f"| {name} | {ns} of {n_slots} ({100 * ns / n_slots:.0f} in 100) | {100 * (1 - np.nanmean(rate_s) / np.nanmean(rate_c)):.0f} |")
L += ["", "**What the lifetime carries beyond the two states** (the residual a slot, pooled over the world's slots of each kind): the slots in place from tick 0 against the arrivals.\n",
      "| world | group | genesis slots: n; residual a slot | arrivals: n; residual a slot |", "|---|---|---|---|"]
L += [f"| {nm} | {'skipping' if k == 'claim' else 'careful'} | {ng}; {rg:.0f} | {na}; {ra:.0f} |" for nm, k, ng, rg, na, ra in RESID]
L += [""] + L2 + [""]
L += ["## 3. J3.3's level temptation at the first suspension (one plus the gap at that tick over the benefit by then; per seed, ± SE)\n",
      "| world | seeds suspended | gap at the first suspension (careful's wallet − wallet − benefit) | benefit by then | **level temptation (per seed, mean ± SE)** | on the means | the first name |", "|---|---|---|---|---|---|---|"]
def at(trace, t):
    best = None
    for row in trace:
        if row[0] <= t: best = row
        else: break
    return (best[1], best[2]) if best else (0.0, 0.0)
for k, kn in (("pa10", "the pin"), ("arm4", "arm 4")):
    for pop, pn in (("careful", "a careful population"), ("hand", "Q1's 60/40 population")):
        j = json.load(open(f"{R}/returner2/{k}-{pop}/eval.json")); C = {int(e["seed"]): json.loads(e["learner_trace_json"]) for e in j["episodes"]["careful"]}
        gaps, bens, temps, first_kind = [], [], [], set()
        for e in j["episodes"]["claimer"]:
            S = json.loads(e["learner_slots_json"]); first = [v for v in S.values() if v["t_in"] == 0]
            first_kind.add("in place from tick 0 (t_in 0, no loan)" if first and first[0]["loan_repaid"] == 0 and first[0]["loan_outstanding"] == 0 else "an arrival")
            if not first or not first[0]["susp_ticks"]: continue
            s0 = first[0]["susp_ticks"][0]; lw, pb = at(json.loads(e["learner_trace_json"]), s0); cw, _ = at(C[int(e["seed"])], s0)
            gaps.append(cw - lw); bens.append(pb); temps.append(1 + (cw - lw) / pb if pb > 0 else np.nan)
        g, b, t = mse(gaps), mse(bens), mse(temps)
        L.append(f"| {kn}, {pn} | {len(gaps)} | {g[0]:+.0f} ± {g[1]:.0f} | {b[0]:.0f} ± {b[1]:.0f} | **{t[0]:.1f} ± {t[1]:.1f}** | {1 + g[0] / b[0]:.1f} | {'; '.join(sorted(first_kind))} |")
L.append("")
L += ["## 6. J4 against the all-careful population, paired by seed (sixty seeds a world)\n",
      "| world | **dosing − all-careful (real a slot)** | careful group − all-careful | care − dose (the record) | dosing slots' benefit a slot | **level temptation at the seat, J3.4's form (care − dose over the benefit)** | the same against the all-careful | overhead a task: dosing world − all-careful |", "|---|---|---|---|---|---|---|---|"]
W = [("w1", "world 1: π^A 0.10, ×1, the fee of record, dose 0.3"), ("w2", "world 2: π^A 0.10, ×1, the fee of record, dose 1"), ("w3", "world 3: π^A 0.10, ×1, the fee doubled, dose 0.3"),
     ("w4", "world 4: π^A 0.30, ×1, the fee of record, dose 0.3"), ("w5", "world 5: π^A 0.30, ×1, the fee doubled, dose 0.3"), ("w6", "world 6: π^A 0.20, ×4, the fee of record, dose 0.3")]
for k, kn in W:
    j = json.load(open(f"{R}/audit-stakes/{k}/eval.json")); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; E = j["episodes"][pol]; C = {int(e["seed"]): e for e in j["episodes"]["careful"]}
    d_all, dc_all, cd, ben, oh = [], [], [], [], []
    for e in E:
        c = C[int(e["seed"])]; Sc = json.loads(c["learner_slots_json"]); all_care = sum(life(v) for v in Sc.values()) / len(Sc)
        d_all.append(f(e, "half_claim_lifetime_per_slot") - all_care); dc_all.append(f(e, "half_care_lifetime_per_slot") - all_care); cd.append(f(e, "half_d_lifetime_per_slot"))
        ben.append(f(e, "half_claim_private_real") / f(e, "half_claim_slots")); oh.append(f(e, "sys_overhead_per_vested") - f(c, "sys_overhead_per_vested"))
    t1 = ratio_se(cd, ben); t2 = ratio_se(-np.array(d_all), ben)
    L.append(f"| {kn} | **{mse(d_all)[0]:+.0f} ± {mse(d_all)[1]:.0f}** | {mse(dc_all)[0]:+.0f} ± {mse(dc_all)[1]:.0f} | {mse(cd)[0]:+.0f} ± {mse(cd)[1]:.0f} | {np.mean(ben):.1f} | **{1 + t1[0]:.1f} ± {t1[1]:.1f}** | {1 + t2[0]:.1f} ± {t2[1]:.1f} | {mse(oh)[0]:+.2f} ± {mse(oh)[1]:.2f} |")
L += [""] + SENT
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
