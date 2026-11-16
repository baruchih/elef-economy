"""Addendum 14's N3 from the record (November 16, 2026; notes §113): (2) M4's conduct cells on the three lifetimes — of record, with the reservation counted
(M3.2's form: the ticks from a slot's departure to the run's end at 0.8 real a tick, nothing before an arrival) and like for like (M3.1's form: the careful
group's income in good standing less the skipping group's good-standing rate over the careful's good ticks) — each with its level temptation (one plus the gap over
the benefit; like for like by J3.1's form); (6) the pin against arm 4 paired by seed for the five pairs of worlds on record that differ only in the arm (the entry
test's two learners at 1 in 10; the dose at 0.1, 0.3 and 1 at every seat), the skipping slot's gap under the pin less under arm 4 on the three lifetimes, with the
paired error and the unpaired one beside. From stress/conduct/ and stress/standing/.  Usage: addendum14_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
T = 1000; RES = 0.8
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def groups(e):
    S = json.loads(e["learner_slots_json"]); share = float(e.get("half_share") or 0.5); seed = int(e["seed"]); grp = {"claim": [], "care": []}
    for x, v in S.items():
        h = int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big"); grp["claim" if h < share * 65536 else "care"].append(v)
    return grp
def life(v): return v["wealth_real"] + v["private_real"]
def after(v): return (T - v["t_out"]) if (not v["alive"] and v["t_out"] is not None and v["t_out"] < T) else 0
def three(E):
    """Per seed: the gap on the three lifetimes (careful − skipping, a slot), the skipping group's benefit a slot and the like-for-like denominator (its benefit a good tick × the careful's good ticks)."""
    out = {k: [] for k in ("seed", "rec", "res", "lfl", "ben", "den", "after_s", "after_c")}
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"]: continue
        row = {}
        for k, V in g.items():
            n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
            row[k] = dict(good=good, ig=ig, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n,
                          lres=sum(life(v) + RES * after(v) for v in V) / n, aft=sum(after(v) for v in V) / n, ben=sum(v["private_real"] for v in V) / n)
        c, s = row["care"], row["claim"]
        out["seed"].append(int(e["seed"])); out["rec"].append(c["life"] - s["life"]); out["res"].append(c["lres"] - s["lres"]); out["lfl"].append(c["ig"] - s["rate"] * c["good"])
        out["ben"].append(s["ben"]); out["den"].append(s["brate"] * c["good"]); out["after_s"].append(s["aft"]); out["after_c"].append(c["aft"])
    return {k: np.array(v, float) for k, v in out.items()}
def temps(d):
    tr = ratio_se(d["rec"], d["ben"]); ts = ratio_se(d["res"], d["ben"]); tl = ratio_se(d["lfl"], d["den"]); return (1 + tr[0], tr[1]), (1 + ts[0], ts[1]), (1 + tl[0], tl[1])
L = ["# Addendum 14's N3 from the record (November 16, 2026)\n",
     "## 2. M4's conduct cells on the three lifetimes (the four finals frozen among careful members; seeds 21–60)\n",
     "Per cell, learner and share: the careful slots less the policy's slots, real a slot, paired by seed ± SE — the lifetime of record (wallet + benefit); with the reservation counted (M3.2's form); like for like (M3.1's form) — each with its level temptation (of record and with the reservation: one plus the gap over the policy's slots' benefit a slot; like for like: J3.1's form, one plus the gap over the policy's benefit a good tick × the careful's good ticks), ± SE by the delta method on the ratio of seed means. The ticks after a departure a slot (policy / careful) beside.\n",
     "| cell, learner | share | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation | ticks after a departure a slot: policy / careful |", "|---|---|---|---|---|---|---|---|---|---|"]
CELLS = [("pa10", "the pin, π^A 0.10"), ("arm4", "arm 4")]; LRN = [("direct", "direct", "the direct"), ("wm", "greedy", "the return head")]
for k, kn in CELLS:
    for sub, pol, ln in LRN:
        j = json.load(open(f"{R}/conduct/{k}-{sub}/eval.json"))
        for share in ("0.25", "0.75"):
            d = three(j["episodes"][f"mix:{pol}:{share}"]); tr, ts, tl = temps(d)
            L.append(f"| {kn}, {ln} | {'1 in 4' if share == '0.25' else '3 in 4'} | {len(d['rec'])} | **{mse(d['rec'])[0]:+.0f} ± {mse(d['rec'])[1]:.0f}** | {tr[0]:.1f} ± {tr[1]:.1f} | **{mse(d['res'])[0]:+.0f} ± {mse(d['res'])[1]:.0f}** | {ts[0]:.1f} ± {ts[1]:.1f} | **{mse(d['lfl'])[0]:+.0f} ± {mse(d['lfl'])[1]:.0f}** | {tl[0]:.1f} ± {tl[1]:.1f} | {np.mean(d['after_s']):.0f} / {np.mean(d['after_c']):.0f} |")
L += ["", "## 6. The pin against arm 4, paired by seed — the five pairs of worlds on record that differ only in the arm\n",
      "For each pair: the skipping slot's gap (careful − skipping, a slot) under the pin and under arm 4 on the three lifetimes, and **the pin's gap less arm 4's, paired by seed** (mean ± SE over the shared seeds); the unpaired error (the two worlds taken as independent, √(SE₁² + SE₂²)) beside. The worlds of stress/standing/ (the entry test's worlds and the dose worlds run again whole at 1a02e69ec with the standing tally; every group figure of record identical).\n",
      "| pair | seeds | lifetime | the pin: gap | arm 4: gap | **pin − arm 4, paired** | SE from nothing | unpaired SE |", "|---|---|---|---|---|---|---|---|"]
PAIRS = [("entry-pa10-direct-s0.1", "entry-arm4-direct-s0.1", "the entry test, direct, 1 in 10"), ("entry-pa10-wm-s0.1", "entry-arm4-wm-s0.1", "the entry test, head alone, 1 in 10"),
         ("dose-pa10-dose0.1", "dose-arm4-dose0.1", "the dose, 0.1 at every seat"), ("dose-pa10-dose0.3", "dose-arm4-dose0.3", "the dose, 0.3 at every seat"), ("dose-pa10-dose1", "dose-arm4-dose1", "the dose, 1 at every seat")]
summary = {"rec": [], "res": [], "lfl": []}
for a, b, nm in PAIRS:
    D = {}
    for w in (a, b):
        j = json.load(open(f"{R}/standing/{w}/eval.json")); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; D[w] = three(j["episodes"][pol])
    common = sorted(set(D[a]["seed"]) & set(D[b]["seed"])); ia = [list(D[a]["seed"]).index(s) for s in common]; ib = [list(D[b]["seed"]).index(s) for s in common]
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        x, y = D[a][key][ia], D[b][key][ib]; ok = ~(np.isnan(x) | np.isnan(y)); x, y = x[ok], y[ok]; d = x - y; dm = mse(d); ma, mb = mse(x), mse(y); unp = np.sqrt(ma[1]**2 + mb[1]**2)
        summary[key].append(dm[0])
        L.append(f"| {nm} | {len(d)} | {kn} | {ma[0]:+.0f} ± {ma[1]:.0f} | {mb[0]:+.0f} ± {mb[1]:.0f} | **{dm[0]:+.0f} ± {dm[1]:.0f}** | {dm[0] / dm[1]:.1f} | {unp:.0f} |")
L.append(f"\nThe five pairs' means of the paired difference: of record {', '.join(f'{x:.0f}' for x in summary['rec'])}; with the reservation {', '.join(f'{x:.0f}' for x in summary['res'])}; like for like {', '.join(f'{x:.0f}' for x in summary['lfl'])}.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
