"""Addendum 11's K3 (November 13, 2026; notes §111): a skipper that loses no time. From the standing re-runs (stress/standing/): for the claiming slots of the entry
test at 1 in 10 (four worlds) and the dosing slots of §110's eight dose worlds, and the careful group beside each — (1) the ticks, the real income (the wallet's
change at each tick's index, net of the loan) and the private benefit in three states: a member in good standing, suspended or on probation, gone (the run's ticks
the slot was not in place: before its arrival, after its departure); (2) what a claiming or dosing slot would end with had it earned at its own good-standing rate,
benefit included, for as many ticks as a careful slot spends in good standing, and its gap to the careful slot (± SE over seeds, each seed's groups averaged a slot);
(3) the checks against the record (every group lifetime identical).  Usage: standing_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
WORLDS = [("entry-pa10-direct-s0.1", "entry/pa10-direct-s0.1-at-b5961bf9f", "the entry test, the pin, direct, 1 in 10", "entry"), ("entry-pa10-wm-s0.1", "entry/pa10-wm-s0.1-at-b5961bf9f", "the entry test, the pin, head alone, 1 in 10", "entry"),
          ("entry-arm4-direct-s0.1", "entry/arm4-direct-s0.1-at-b5961bf9f", "the entry test, arm 4, direct, 1 in 10", "entry"), ("entry-arm4-wm-s0.1", "entry/arm4-wm-s0.1-at-b5961bf9f", "the entry test, arm 4, head alone, 1 in 10", "entry"),
          ("dose-pa10-dose0.1", "dose/pa10-dose0.1", "the dose, the pin, 0.1 at every seat", "dose0.1pin"), ("dose-pa10-dose0.3", "dose/pa10-dose0.3", "the dose, the pin, 0.3 at every seat", "dose"), ("dose-pa10-dose1", "dose/pa10-dose1", "the dose, the pin, 1 at every seat", "dose"),
          ("dose-pa10-dose0.3first", "dose/pa10-dose0.3first", "the dose, the pin, 0.3 at the first review only", "dose"), ("dose-pa10-dose0.3audit", "dose/pa10-dose0.3audit", "the dose, the pin, 0.3 at the member's audit seat only", "dose"),
          ("dose-arm4-dose0.1", "dose/arm4-dose0.1", "the dose, arm 4, 0.1 at every seat", "dose0.1arm4"), ("dose-arm4-dose0.3", "dose/arm4-dose0.3", "the dose, arm 4, 0.3 at every seat", "dose"), ("dose-arm4-dose1", "dose/arm4-dose1", "the dose, arm 4, 1 at every seat", "dose")]
L = ["# K3 — a skipper that loses no time: the slots' ticks, income and benefit by standing, and the counterfactual of a claiming slot earning at its good-standing rate for a careful slot's good-standing ticks\n",
     "Each world's claiming (or dosing) group against its careful group, a slot (each seed's groups averaged a slot, then ± SE over seeds). `good` a member in good standing; `down` suspended or on probation; `gone` the run's ticks the slot was not in place. "
     "The income is the wallet's change tick by tick at each tick's index, net of the loan (so it is the lifetime's wallet up to the index's drift and the genesis wallet); the benefit the private benefit. The rate is (income + benefit) a tick in good standing. "
     "The counterfactual: the claiming slot's good-standing rate × the careful group's good-standing ticks a slot; its gap to the careful slot's lifetime (wallet + benefit) is the last column, negative where the skipper would be ahead.\n",
     "| world | group | ticks: good / down / gone | income (real): good / down | benefit: good / down | rate a good tick (income + benefit) | lifetime a slot (record) | **counterfactual lifetime; careful − it** |",
     "|---|---|---|---|---|---|---|---|"]
checks = []; verdict = {}
for new, old, name, kind in WORLDS:
    p = f"{R}/standing/{new}/eval.json"
    if not os.path.exists(p): L.append(f"| {name} | (pending) | | | | | | |"); continue
    j = json.load(open(p)); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; E = j["episodes"][pol]
    p0 = f"{R}/{old}/eval.json"
    if os.path.exists(p0):
        j0 = json.load(open(p0)); E0 = j0["episodes"][[x for x in j0["episodes"] if x.startswith("mix:")][0]]
        checks.append((name, max(abs(f(a, "half_d_lifetime_per_slot") - f(b, "half_d_lifetime_per_slot")) for a, b in zip(E, E0))))
    G = {"claim": {k: [] for k in ("good", "down", "gone", "ig", "id", "bg", "bd", "rate", "life")}, "care": {k: [] for k in ("good", "down", "gone", "ig", "id", "bg", "bd", "rate", "life")}}
    cf = []; cfl = []
    for e in E:
        S = json.loads(e["learner_slots_json"]); T = 1000
        import hashlib
        share = float(e.get("half_share") or 0.5); seed = int(e["seed"])
        grp = {}
        for x, v in S.items():
            h = int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big"); grp.setdefault("claim" if h < share * 65536 else "care", []).append(v)
        row = {}
        for g, V in grp.items():
            n = len(V); good = sum(v.get("ticks_good", 0) for v in V) / n; down = sum(v.get("ticks_down", 0) for v in V) / n; gone = T - good - down
            ig = sum(v.get("income_good", 0.0) for v in V) / n; idn = sum(v.get("income_down", 0.0) for v in V) / n; bg = sum(v.get("benefit_good", 0.0) for v in V) / n; bd = sum(v.get("benefit_down", 0.0) for v in V) / n
            life = sum(v["wealth_real"] + v["private_real"] for v in V) / n; rate = (ig + bg) / good if good else np.nan
            row[g] = dict(good=good, down=down, gone=gone, ig=ig, id=idn, bg=bg, bd=bd, rate=rate, life=life)
            for k in row[g]: G[g][k].append(row[g][k])
        if "claim" in row and "care" in row:
            cfl.append(row["claim"]["rate"] * row["care"]["good"]); cf.append(row["care"]["life"] - cfl[-1])
    cfm = mse(cf); verdict[name] = (kind, cfm)
    for g in ("claim", "care"):
        m = {k: mse(v) for k, v in G[g].items()}
        last = f"**{np.nanmean(cfl):.0f}; {cfm[0]:+.0f} ± {cfm[1]:.0f}**" if g == "claim" else "—"
        L.append(f"| {name} ({len(E)} seeds) | {'claiming' if (g == 'claim' and kind == 'entry') else ('dosing' if g == 'claim' else 'careful')} | {m['good'][0]:.0f} / {m['down'][0]:.0f} / {m['gone'][0]:.0f} | {m['ig'][0]:.0f} / {m['id'][0]:.0f} | {m['bg'][0]:.0f} / {m['bd'][0]:.0f} | {m['rate'][0]:.2f} ± {m['rate'][1]:.2f} | {m['life'][0]:.0f} | {last} |")
L.append("\n**The re-runs against the record** (the largest difference in the group gap a slot on any seed): " + "; ".join(f"{n}: {d:.2e}" for n, d in checks) + ".")
L.append("\n## Against addendum 11's expectations\n"); L.append("| world | expected (careful − counterfactual) | read | |"); L.append("|---|---|---|---|")
all_entry_behind_250 = True
for name, (kind, cfm) in verdict.items():
    if kind == "entry": exp, ok = "between 150 behind and 80 ahead (−80 … +150)", -80 <= cfm[0] <= 150; all_entry_behind_250 &= cfm[0] > 250
    elif kind == "dose0.1pin": exp, ok = "behind by 20 to 130", 20 <= cfm[0] <= 130
    elif kind == "dose0.1arm4": exp, ok = "within 60 either way", abs(cfm[0]) <= 60
    else: exp, ok = "—", None
    L.append(f"| {name} | {exp} | {cfm[0]:+.0f} ± {cfm[1]:.0f} | {'met' if ok else ('MISSED' if ok is not None else '')} |")
if any(k == "entry" for k, _ in verdict.values()):
    L.append(f"\n**Refuted if the entry test's skipper is still more than 250 behind in all four worlds:** {'REFUTED' if all_entry_behind_250 else 'not refuted'}.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
