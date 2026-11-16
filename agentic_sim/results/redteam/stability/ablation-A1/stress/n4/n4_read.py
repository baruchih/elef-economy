"""Addendum 14's N4 (November 16, 2026; notes §113): a light skipper in the ruled design's nearest cell, read as the dose — six worlds (n4/launch.sh at 7bd5dd5fc;
worlds 1 and 6 of record on seeds 21–60 from stress/standing/ (the dose worlds run again whole at 1a02e69ec with the standing tally, every figure of record identical), with seeds 61–120 added here). Read on three lifetimes (of record; with the reservation counted, M3.2's
form; like for like, M3.1's form), each with its level temptation; both groups' claims, benefit, suspensions, audit seats and good ticks a slot, the lifetime lost for
each claim; the honest side (the careful group against the all-careful in the same world; arm 1's all-careful against arm 0's paired by seed; the penalties on
correct verdicts by seat; the orchestrator's seats; the leak and the overhead); worlds 1 and 6 paired by seed; the expectations stated before the run and the
refutation condition.  Usage: n4_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
T = 1000; RES = 0.8
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def f0(e, k): v = e.get(k); return float(v) if v not in (None, "") else 0.0
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
W = {"w1": ("the pin (π^A 0.10), the fee of record, dose 0.1", [(f"{R}/standing/dose-pa10-dose0.1", "mix:dose0.1:0.25"), (f"{R}/n4/w1-s61-120", "mix:dose0.1:0.25")]),
     "w2": ("the pin, the fee doubled (the weight at 3), dose 0.1", [(f"{R}/n4/w2", "mix:dose0.1:0.25")]),
     "w3": ("arm 1 with π^A held at 0.10, the fee of record, dose 0.1", [(f"{R}/n4/w3", "mix:dose0.1:0.25")]),
     "w4": ("arm 1 with π^A held at 0.10, the fee doubled, dose 0.1 — the ruled design's nearest cell", [(f"{R}/n4/w45-s21-50", "mix:dose0.1:0.25"), (f"{R}/n4/w45-s51-80", "mix:dose0.1:0.25")]),
     "w5": ("world 4 with a dose of 0.3", [(f"{R}/n4/w45-s21-50", "mix:dose0.3:0.25"), (f"{R}/n4/w45-s51-80", "mix:dose0.3:0.25")]),
     "w6": ("arm 4, the fee of record, dose 0.1", [(f"{R}/standing/dose-arm4-dose0.1", "mix:dose0.1:0.25"), (f"{R}/n4/w6-s61-120", "mix:dose0.1:0.25")])}
def read(k):
    E, C = [], {}
    for d, pol in W[k][1]:
        p = f"{d}/eval.json"
        if not os.path.exists(p): continue
        j = json.load(open(p)); E += j["episodes"][pol]; C.update({int(e["seed"]): e for e in j["episodes"]["careful"]})
    rows = []
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"]: continue
        c = C[int(e["seed"])]; Sc = json.loads(c["learner_slots_json"]); r = {"seed": int(e["seed"]), "all_care": sum(life(v) for v in Sc.values()) / len(Sc)}
        for kk, V in g.items():
            n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
            r[kk] = dict(n=n, good=good, ig=ig, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n,
                         ben=sum(v["private_real"] for v in V) / n, claims=sum(v["claims"] for v in V) / n, susp=sum(v["suspensions"] for v in V) / n, aud=sum(v["audits_done"] for v in V) / n)
        cc, s = r["care"], r["claim"]
        r.update(rec=cc["life"] - s["life"], res=cc["lres"] - s["lres"], lfl=cc["ig"] - s["rate"] * cc["good"], den=s["brate"] * cc["good"], ben=s["ben"], claims=s["claims"],
                 care_minus_all=cc["life"] - r["all_care"], fa=f(e, "false_approvals"), leak=1000 * f(e, "leak_bad"), oh=f(e, "sys_overhead_per_vested"), fa0=f(c, "false_approvals"), leak0=1000 * f(c, "leak_bad"), oh0=f(c, "sys_overhead_per_vested"),
                 pen=[f0(e, f"false_penalty_{x}") for x in ("initial", "audit", "appeal")], pen0=[f0(c, f"false_penalty_{x}") for x in ("initial", "audit", "appeal")],
                 state_seats=f0(e, "troop_reviews") + f0(e, "deciding_seats"), member_seats=sum(f0(e, x) for x in ("seated_initial_member", "seated_initial_probationer", "seated_audit_member", "seated_appeal_member")),
                 state_seats0=f0(c, "troop_reviews") + f0(c, "deciding_seats"), member_seats0=sum(f0(c, x) for x in ("seated_initial_member", "seated_initial_probationer", "seated_audit_member", "seated_appeal_member")),
                 careful_real0=f(c, "learner_lifetime_real") / f(c, "learner_pop_total"))
        rows.append(r)
    return rows
def col(rows, key): return np.array([r[key] for r in rows], float)
def temp(rows, key, den):
    t = ratio_se(col(rows, key), col(rows, den)); return 1 + t[0], t[1]
D = {k: read(k) for k in W}
L = ["# N4 — a light skipper in the ruled design's nearest cell, read as the dose (the stressed world, a temptation of 1, the dosing slots 1 in 4 with the dose at every seat, the bond ×1; the all-careful beside on the same seeds)\n",
     "## The dose on three lifetimes, each with its level temptation\n",
     "The careful slots less the dosing slots, real a slot, paired by seed ± SE: of record (wallet + benefit); with the reservation counted (the ticks from a departure to the run's end at 0.8 real a tick); like for like (the careful group's income in good standing less the dosing group's good-standing rate over the careful's good ticks). The level temptation: one plus the gap over the dosing slots' benefit a slot (of record, with the reservation); J3.1's form like for like.\n",
     "| world | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |", "|---|---|---|---|---|---|---|---|"]
for k in W:
    rows = D[k]
    if not rows: L.append(f"| {k}: {W[k][0]} | (pending) | | | | | | |"); continue
    a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl")); ta, tb, tc = temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")
    L.append(f"| {k}: {W[k][0]} | {len(rows)} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f} SE) | {ta[0]:.1f} ± {ta[1]:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f} SE) | {tb[0]:.1f} ± {tb[1]:.1f} | **{c[0]:+.0f} ± {c[1]:.0f}** ({c[0] / c[1]:.1f} SE) | {tc[0]:.1f} ± {tc[1]:.1f} |")
for k, lab, seeds in (("w1", "world 1 on the added seeds 61–120 alone", range(61, 121)), ("w6", "world 6 on the added seeds 61–120 alone", range(61, 121)), ("w1", "world 1 on seeds 21–60 (of record)", range(21, 61)), ("w6", "world 6 on seeds 21–60 (of record)", range(21, 61))):
    rows = [r for r in D[k] if r["seed"] in set(seeds)]
    if not rows: continue
    a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl")); ta, tb, tc = temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")
    L.append(f"| {lab} | {len(rows)} | {a[0]:+.0f} ± {a[1]:.0f} | {ta[0]:.1f} ± {ta[1]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {tb[0]:.1f} ± {tb[1]:.1f} | {c[0]:+.0f} ± {c[1]:.0f} | {tc[0]:.1f} ± {tc[1]:.1f} |")
L += ["", "## Both groups a slot, and the lifetime lost for each claim\n",
      "| world | dosing slots: claims; benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** |", "|---|---|---|---|"]
for k in W:
    rows = D[k]
    if not rows: continue
    s = lambda kk, key: np.mean([r[kk][key] for r in rows]); l1, l2, l3 = ratio_se(col(rows, "rec"), col(rows, "claims")), ratio_se(col(rows, "res"), col(rows, "claims")), ratio_se(col(rows, "lfl"), col(rows, "claims"))
    L.append(f"| {k} | {s('claim', 'claims'):.1f}; {s('claim', 'ben'):.1f}; {s('claim', 'susp'):.2f}; {s('claim', 'aud'):.1f}; {s('claim', 'good'):.0f} | {s('care', 'susp'):.2f}; {s('care', 'aud'):.1f}; {s('care', 'good'):.0f} | **{l1[0]:.1f} ± {l1[1]:.1f} / {l2[0]:.1f} ± {l2[1]:.1f} / {l3[0]:.1f} ± {l3[1]:.1f}** |")
L += ["", "## The honest side\n",
      "The careful group's lifetime a slot less the all-careful population's in the same world (paired by seed); the penalties on correct verdicts by seat a run (initial / audit / appeal: the bonds forfeited by a careful verdict later overturned — the dosing world and the all-careful's); the orchestrator's review seats a run (troop reviews + the deciding verdict's seats) and its share of every review seat (members' initial, audit and appeal seats beside); the leak per thousand bad deliveries and the overhead a vested task (the dosing world; the all-careful's).\n",
      "| world | **careful group − all-careful** | penalties on correct verdicts (initial / audit / appeal): dosing world; all-careful | orchestrator's seats; share: dosing world; all-careful | FA; leak ‰; overhead (all-careful) |", "|---|---|---|---|---|"]
for k in W:
    rows = D[k]
    if not rows: continue
    m = mse(col(rows, "care_minus_all")); pen = np.mean([r["pen"] for r in rows], axis=0); pen0 = np.mean([r["pen0"] for r in rows], axis=0)
    ss, ms, ss0, ms0 = (np.mean(col(rows, x)) for x in ("state_seats", "member_seats", "state_seats0", "member_seats0"))
    L.append(f"| {k} | **{m[0]:+.0f} ± {m[1]:.0f}** | {pen[0]:.1f} / {pen[1]:.1f} / {pen[2]:.1f}; {pen0[0]:.1f} / {pen0[1]:.1f} / {pen0[2]:.1f} | {ss:.0f}; {ss / (ss + ms):.3f}; {ss0:.0f}; {ss0 / (ss0 + ms0):.3f} | {np.mean(col(rows, 'fa')):.1f}; {np.mean(col(rows, 'leak')):.0f}; {np.mean(col(rows, 'oh')):.1f} ({np.mean(col(rows, 'fa0')):.1f}; {np.mean(col(rows, 'leak0')):.0f}; {np.mean(col(rows, 'oh0')):.1f}) |")
L += ["", "**Arm 1's all-careful against arm 0's, paired by seed (the careful's real lifetime a slot, the all-careful populations):**\n", "| pair | seeds | arm 0 | arm 1 | **arm 1 − arm 0** | in 100 | penalties on correct first verdicts: arm 0 → arm 1 |", "|---|---|---|---|---|---|---|"]
for a, b, nm in (("w1", "w3", "the fee of record (world 3 against 1)"), ("w2", "w4", "the fee doubled (world 4 against 2)")):
    A = {r["seed"]: r for r in D[a]}; B = {r["seed"]: r for r in D[b]}; seeds = sorted(set(A) & set(B))
    if not seeds: continue
    d = [B[s]["careful_real0"] - A[s]["careful_real0"] for s in seeds]; m = mse(d); base = np.mean([A[s]["careful_real0"] for s in seeds])
    L.append(f"| {nm} | {len(seeds)} | {base:.0f} | {np.mean([B[s]['careful_real0'] for s in seeds]):.0f} | **{m[0]:+.0f} ± {m[1]:.0f}** | {100 * m[0] / base:+.1f} ± {100 * m[1] / base:.1f} | {np.mean([A[s]['pen0'][0] for s in seeds]):.1f} → {np.mean([B[s]['pen0'][0] for s in seeds]):.1f} |")
L += ["", "**The fee's doubling under the pin, paired by seed (world 2 against world 1): the dosing slot's gap and the careful's real lifetime.**\n", "| lifetime | seeds | world 1 | world 2 | **world 2 − world 1, paired** |", "|---|---|---|---|---|"]
A = {r["seed"]: r for r in D["w1"]}; B = {r["seed"]: r for r in D["w2"]}; seeds = sorted(set(A) & set(B))
for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like"), ("careful_real0", "the all-careful's real lifetime a slot")):
    if seeds:
        d = [B[s][key] - A[s][key] for s in seeds]; m = mse(d); L.append(f"| {kn} | {len(seeds)} | {np.mean([A[s][key] for s in seeds]):+.0f} | {np.mean([B[s][key] for s in seeds]):+.0f} | **{m[0]:+.0f} ± {m[1]:.0f}** |")
L += ["", "## The pin less arm 4, worlds 1 and 6 paired by seed\n", "| seeds | lifetime | the pin | arm 4 | **pin − arm 4, paired** | SE from nothing |", "|---|---|---|---|---|---|"]
A = {r["seed"]: r for r in D["w1"]}; B = {r["seed"]: r for r in D["w6"]}
for lab, seeds in (("21–120", sorted(set(A) & set(B))), ("61–120 (the added seeds)", sorted(set(A) & set(B) & set(range(61, 121))))):
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        if seeds:
            x = np.array([A[s][key] for s in seeds]); y = np.array([B[s][key] for s in seeds]); ok = ~(np.isnan(x) | np.isnan(y)); d = x[ok] - y[ok]; m = mse(d)
            L.append(f"| {lab} | {kn} | {x[ok].mean():+.0f} | {y[ok].mean():+.0f} | **{m[0]:+.0f} ± {m[1]:.0f}** | {m[0] / m[1]:.1f} |")
# the expectations
L += ["", "## Against the expectations stated before the run\n", "| statement | read | |", "|---|---|---|"]
def g(k, key): rows = D[k]; return mse(col(rows, key)) if rows else (np.nan, np.nan)
def tp(k, key, den): return temp(D[k], key, den)[0] if D[k] else np.nan
def chk(name, cond, read): L.append(f"| {name} | {read} | {'met' if cond else 'MISSED'} |")
for k in ("w4", "w2"):
    a, b, c = g(k, "rec"), g(k, "res"), g(k, "lfl")
    chk(f"{k}: behind by 170 to 350 of record", 170 <= a[0] <= 350, f"{a[0]:+.0f} ± {a[1]:.0f}")
    chk(f"{k}: at least 120 with the reservation, ≥ 3 SE", b[0] >= 120 and b[0] >= 3 * b[1], f"{b[0]:+.0f} ± {b[1]:.0f} ({b[0] / b[1]:.1f} SE)")
    chk(f"{k}: at least 120 like for like, ≥ 3 SE", c[0] >= 120 and c[0] >= 3 * c[1], f"{c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE)")
    chk(f"{k}: level at a temptation of 4 or more on each of the three", all(x >= 4 for x in (tp(k, "rec", "ben"), tp(k, "res", "ben"), tp(k, "lfl", "den"))), f"{tp(k, 'rec', 'ben'):.1f} / {tp(k, 'res', 'ben'):.1f} / {tp(k, 'lfl', 'den'):.1f}")
A = {r["seed"]: r for r in D["w1"]}; B = {r["seed"]: r for r in D["w2"]}; seeds = sorted(set(A) & set(B))
for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
    if seeds: m = mse([B[s][key] - A[s][key] for s in seeds]); chk(f"the fee's doubling adds 50 to 150 to world 1's gap, {kn} (paired)", 50 <= m[0] <= 150, f"{m[0]:+.0f} ± {m[1]:.0f}")
for a, b in (("w1", "w3"), ("w2", "w4")):
    A = {r["seed"]: r for r in D[a]}; B = {r["seed"]: r for r in D[b]}; seeds = sorted(set(A) & set(B))
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        if seeds: m = mse([B[s][key] - A[s][key] for s in seeds]); chk(f"{b} within 70 of {a}, {kn} (paired)", abs(m[0]) <= 70, f"{m[0]:+.0f} ± {m[1]:.0f}")
    if seeds:
        p0 = np.mean([A[s]["pen0"][0] for s in seeds]); p1 = np.mean([B[s]["pen0"][0] for s in seeds]); chk(f"under arm 1 ({b}) the penalties on correct first verdicts under half of arm 0's ({a}), the all-careful", p1 < 0.5 * p0, f"{p0:.1f} → {p1:.1f}")
        pd0 = np.mean([A[s]["pen"][0] for s in seeds]); pd1 = np.mean([B[s]["pen"][0] for s in seeds]); chk(f"the same in the dosing worlds", pd1 < 0.5 * pd0, f"{pd0:.1f} → {pd1:.1f}")
        m = mse([B[s]["careful_real0"] - A[s]["careful_real0"] for s in seeds]); base = np.mean([A[s]["careful_real0"] for s in seeds]); chk(f"the careful's real lifetime under arm 1 ({b}) within 5 in 100 of arm 0's ({a})", abs(100 * m[0] / base) <= 5, f"{100 * m[0] / base:+.1f} ± {100 * m[1] / base:.1f} in 100")
a, b = g("w5", "rec"), g("w5", "res"); chk("w5: behind by 500 to 850 of record", 500 <= a[0] <= 850, f"{a[0]:+.0f} ± {a[1]:.0f}"); chk("w5: at least 350 with the reservation", b[0] >= 350, f"{b[0]:+.0f} ± {b[1]:.0f}")
for k, exp in (("w1", ((154, 108, 99), "within 40")), ("w6", ((110, 70, 55), "under"))):
    rows = [r for r in D[k] if r["seed"] >= 61]
    if rows:
        vals = [mse(col(rows, key))[0] for key in ("rec", "res", "lfl")]
        if k == "w1": chk("world 1 on the added seeds: 154, 108, 99 each within 40", all(abs(v - e) <= 40 for v, e in zip(vals, exp[0])), " / ".join(f"{v:+.0f}" for v in vals))
        else: chk("world 6 on the added seeds: under 110, 70, 55", all(v < e for v, e in zip(vals, exp[0])), " / ".join(f"{v:+.0f}" for v in vals))
A = {r["seed"]: r for r in D["w1"]}; B = {r["seed"]: r for r in D["w6"]}; seeds = sorted(set(A) & set(B))
for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
    if seeds: m = mse([A[s][key] - B[s][key] for s in seeds]); chk(f"paired, the pin further behind than arm 4 by 30 to 120, {kn}", 30 <= m[0] <= 120, f"{m[0]:+.0f} ± {m[1]:.0f}")
b, c = g("w4", "res"), g("w4", "lfl")
L.append(f"\n**Refuted if in world 4 the dosing slots are within two standard errors of nothing, with the reservation counted or like for like:** {b[0]:+.0f} ± {b[1]:.0f} ({b[0] / b[1]:.1f} SE) and {c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE) — **{'REFUTED' if (b[0] <= 2 * b[1] or c[0] <= 2 * c[1]) else 'not refuted'}**.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
