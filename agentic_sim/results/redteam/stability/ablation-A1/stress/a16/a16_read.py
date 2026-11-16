"""Addendum 16 (November 16, 2026; notes §115): Q3's six readings from the worlds on record (a15/, no run — items 1–5; item 6 from reads 5 and 6 run again whole at
b1fa10d2c for the split, a16/r5b, r6b, checked to the digit) and Q4's three reads without training (a16/r9, r10, r11 by launch.sh at b1fa10d2c), read as P4 was
(a15_read.py's helpers copied: the three lifetimes paired by seed, the level temptations, both groups a slot, the lifetime lost for each claim), with the
expectations stated before the run and the four refutations or showings. Usage: a16_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; A = f"{R}/a15"; B = f"{R}/a16"
T = 1000; RES = 0.8
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def f0(e, k): v = e.get(k); return float(v) if v not in (None, "") else 0.0
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num)
    if n < 2 or den.mean() == 0: return (np.nan, np.nan)
    a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1); r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def groups(e):
    S = json.loads(e["learner_slots_json"]); share = float(e.get("half_share") or 0.5); seed = int(e["seed"]); grp = {"claim": [], "care": []}
    for x, v in S.items():
        h = int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big"); grp["claim" if h < share * 65536 else "care"].append(v)
    return grp
def life(v): return v["wealth_real"] + v["private_real"]
def after(v): return (T - v["t_out"]) if (not v["alive"] and v["t_out"] is not None and v["t_out"] < T) else 0
def load(dirs, pol):
    E, C = [], {}
    for d in dirs:
        p = f"{d}/eval.json"
        if not os.path.exists(p): continue
        j = json.load(open(p))
        if pol in j["episodes"]: E += j["episodes"][pol]
        if "careful" in j["episodes"]: C.update({int(e["seed"]): e for e in j["episodes"]["careful"]})
    return E, C
def rows_of(E, C, filt=lambda v: True):
    out = []
    for e in E:
        g = {k: [v for v in V if filt(v)] for k, V in groups(e).items()}
        if not g["claim"] or not g["care"] or int(e["seed"]) not in C: continue
        c0 = C[int(e["seed"])]; Sc = [v for v in json.loads(c0["learner_slots_json"]).values() if filt(v)]
        r = {"seed": int(e["seed"]), "all_care": (sum(life(v) for v in Sc) / len(Sc)) if Sc else np.nan}
        for kk, V in g.items():
            n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
            r[kk] = dict(n=n, good=good, ig=ig, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n,
                         ben=sum(v["private_real"] for v in V) / n, claims=sum(v["claims"] for v in V) / n, cm=sum(v.get("claims_member", 0) for v in V) / n, cp=sum(v.get("claims_probation", 0) for v in V) / n,
                         susp=sum(v["suspensions"] for v in V) / n, aud=sum(v["audits_done"] for v in V) / n, failed=sum(1 for v in V if v.get("pfail_ticks")) / n,
                         first_t=np.mean([v["pfail_ticks"][0] for v in V if v.get("pfail_ticks")]) if any(v.get("pfail_ticks") for v in V) else np.nan)
        cc, s = r["care"], r["claim"]
        r.update(rec=cc["life"] - s["life"], res=cc["lres"] - s["lres"], lfl=cc["ig"] - s["rate"] * cc["good"], den=s["brate"] * cc["good"], ben=s["ben"], claims=s["claims"], care_minus_all=cc["life"] - r["all_care"],
                 fa=f(e, "false_approvals"), leak=1000 * f(e, "leak_bad"), oh=f(e, "sys_overhead_per_vested"), fa0=f(c0, "false_approvals"), leak0=1000 * f(c0, "leak_bad"), oh0=f(c0, "sys_overhead_per_vested"))
        out.append(r)
    return out
def col(rows, k): return np.array([r[k] for r in rows], float)
def grp(rows, kk, k): return np.mean([r[kk][k] for r in rows])
def temp(rows, key, den): t = ratio_se(col(rows, key), col(rows, den)); return 1 + t[0], t[1]
def lifetimes_row(name, rows, extra=""):
    if not rows: return f"| {name} | (pending) | | | | | | |{extra}"
    a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl")); ta, tb, tc = temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")
    return f"| {name} | {len(rows)} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {ta[0]:.1f} ± {ta[1]:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f}) | {tb[0]:.1f} ± {tb[1]:.1f} | **{c[0]:+.0f} ± {c[1]:.0f}** ({c[0] / c[1]:.1f}) | {tc[0]:.1f} ± {tc[1]:.1f} |{extra}"
def groups_row(name, rows):
    if not rows: return f"| {name} | (pending) | | | |"
    l1, l2, l3 = ratio_se(col(rows, "rec"), col(rows, "claims")), ratio_se(col(rows, "res"), col(rows, "claims")), ratio_se(col(rows, "lfl"), col(rows, "claims"))
    return (f"| {name} | {grp(rows, 'claim', 'claims'):.1f} ({grp(rows, 'claim', 'cm'):.1f} / {grp(rows, 'claim', 'cp'):.1f}); {grp(rows, 'claim', 'ben'):.1f}; {grp(rows, 'claim', 'susp'):.2f}; {grp(rows, 'claim', 'aud'):.1f}; {grp(rows, 'claim', 'good'):.0f} | "
            f"{grp(rows, 'care', 'susp'):.2f}; {grp(rows, 'care', 'aud'):.1f}; {grp(rows, 'care', 'good'):.0f} | **{l1[0]:.1f} ± {l1[1]:.1f} / {l2[0]:.1f} ± {l2[1]:.1f} / {l3[0]:.1f} ± {l3[1]:.1f}** | "
            f"{mse(col(rows, 'care_minus_all'))[0]:+.0f} ± {mse(col(rows, 'care_minus_all'))[1]:.0f}; {np.mean(col(rows, 'fa')):.1f}; {np.mean(col(rows, 'leak')):.0f}; {np.mean(col(rows, 'oh')):.1f} ({np.mean(col(rows, 'fa0')):.1f}; {np.mean(col(rows, 'leak0')):.0f}; {np.mean(col(rows, 'oh0')):.1f}) |")
HDR_L = ["| world / read | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |", "|---|---|---|---|---|---|---|---|"]
HDR_G = ["| world / read | conduct's slots: claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** | careful group − all-careful; FA; leak ‰; overhead (all-careful) |", "|---|---|---|---|---|"]
def paired_rows(L, nm, ra, rb):
    """second − first, paired on the shared seeds, the three lifetimes."""
    A_ = {r["seed"]: r for r in ra}; B_ = {r["seed"]: r for r in rb}; seeds = sorted(set(A_) & set(B_))
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        if seeds:
            x = np.array([A_[s][key] for s in seeds]); y = np.array([B_[s][key] for s in seeds]); ok = ~(np.isnan(x) | np.isnan(y)); m = mse(y[ok] - x[ok])
            L.append(f"| {nm} | {int(ok.sum())} | {kn} | {x[ok].mean():+.0f} | {y[ok].mean():+.0f} | **{m[0]:+.0f} ± {m[1]:.0f}** | {m[0] / m[1]:.1f} |")
HDR_P = ["| contrast | seeds | lifetime | first | second | **second − first, paired** | SE from nothing |", "|---|---|---|---|---|---|---|"]
WN = {"w1": "world 1: the pin, the weight of record", "w2": "world 2: the pin, the weight doubled", "w3": "world 3: arm 1, the weight of record", "w4": "world 4: arm 1, the weight doubled", "w6": "world 6: arm 4"}
# ---------------------------------------------------------------- the worlds of record (a15)
D = {}
for k, dirs in {"w1": [f"{A}/rerun/w1-s21-70", f"{A}/rerun/w1-s71-120"], "w2": [f"{A}/rerun/w2"], "w3": [f"{A}/rerun/w3"], "w4": [f"{A}/rerun/w4"], "w6": [f"{A}/rerun/w6-s21-70", f"{A}/rerun/w6-s71-120"]}.items():
    D[k] = load(dirs, "mix:dose0.1:0.25")
CW = {k: dict(D[k][1]) for k in D}
CW["w4"].update(load([f"{A}/p4/r2-s81-120"], "careful")[1]); CW["w3"].update(load([f"{B}/r9/careful-w3-s81-120"], "careful")[1])
CW["w4"].update(load([f"{B}/r10/careful-w4-s121-125", f"{B}/r10/s126-170", f"{B}/r10/s171-215", f"{B}/r10/s216-260"], "careful")[1])
P4 = {}
for rid, dirs, pol in (("r1", [f"{A}/p4/r1-s21-70", f"{A}/p4/r1-s71-120"], "mix:doseM0.1:0.25"), ("r2", [f"{A}/p4/r2-s21-80", f"{A}/p4/r2-s81-120"], "mix:doseM0.1:0.25"), ("r3", [f"{A}/p4/r3-s21-70", f"{A}/p4/r3-s71-120"], "mix:doseM0.1:0.25"),
                       ("r4", [f"{A}/p4/r4"], "mix:doseM0.3:0.25"), ("r5", [f"{A}/p4/r5"], "mix:doseF0.3:0.25"), ("r6", [f"{A}/p4/r6"], "mix:doseF0.3:0.25"), ("r7", [f"{A}/p4/r7"], "mix:dose0.3audit:0.25"), ("r8", [f"{A}/p4/r8"], "mix:dose0.3audit:0.25")):
    P4[rid] = load(dirs, pol)[0]
L = ["# Addendum 16: Q3's six readings from the worlds on record, and Q4's three reads without training (November 16, 2026; a16/launch.sh at b1fa10d2c)\n"]
# ---------------------------------------------------------------- Q3.1 the suspended slots' partition
L += ["## Q3.1. How the counts of the suspended divide (N4's worlds 2 and 3 of record, a15/rerun/)\n",
      "§114a's counts were over every suspended learner slot of the world, the careful 3 in 4 included, and 'regained good standing' was read as a slot whose ticks in good standing exceed the ticks from its entry to its first suspension — a reading that overlaps the two others (a slot that regained its standing then departed, or was alive at the end). Here the same slots partitioned once, with an arrival's ticks counted from its admission (so a slot that was a probationer first is not missed): regained and alive at the end / regained and departed / never regained and alive / never regained and departed; the dosing group alone beside.\n",
      "| world | group | suspended slots | **regained: alive / departed** | **never regained: alive / departed** | departed: ticks after the first suspension (mean) |", "|---|---|---|---|---|---|"]
for k in ("w2", "w3"):
    E, C = D[k]
    for gn, keep in (("every slot (§114a's count)", ("claim", "care")), ("the dosing slots", ("claim",)), ("the careful slots", ("care",))):
        n = 0; cnt = {"ra": 0, "rd": 0, "na": 0, "nd": 0}; dl = []
        for e in E:
            g = groups(e)
            for kk in keep:
                for v in g[kk]:
                    if not v["suspensions"]: continue
                    n += 1; s0 = v["susp_ticks"][0]
                    good_before = (s0 - v["adm_t"]) if v.get("adm_t") is not None else (s0 if v["t_in"] == 0 else 0)   # a founder a member from tick 0; an arrival from its admission; a probationer never
                    reg = v["ticks_good"] > good_before + 2; dep = not v["alive"]
                    cnt[("r" if reg else "n") + ("d" if dep else "a")] += 1
                    if dep: dl.append(v["t_out"] - s0)
        L.append(f"| {WN[k]} | {gn} | {n} | **{cnt['ra']} / {cnt['rd']}** | **{cnt['na']} / {cnt['nd']}** | {np.mean(dl) if dl else float('nan'):.0f} |")
# ---------------------------------------------------------------- Q3.2 three sentences against their tables
L += ["", "## Q3.2. Three sentences against their tables\n"]
rows31 = {}
for k in ("w1", "w4", "w6"):
    for kind, filt in (("founders", lambda v: v["t_in"] == 0), ("arrivals", lambda v: v["t_in"] > 0)): rows31[(k, kind)] = rows_of(D[k][0], D[k][1], filt)
rat = {k: {key: mse(col(rows31[(k, "founders")], key))[0] / mse(col(rows31[(k, "arrivals")], key))[0] for key in ("rec", "res", "lfl")} for k in ("w1", "w4", "w6")}
L.append("- §114b.1, the founders' loss against the arrivals' (P3.1's table): of record " + ", ".join(f"{100 * rat[k]['rec']:.0f}" for k in ("w1", "w4", "w6")) + " in 100 (the pin, arm 1 with the weight doubled, arm 4); with the reservation " + ", ".join(f"{100 * rat[k]['res']:.0f}" for k in ("w1", "w4", "w6")) + "; like for like " + ", ".join(f"{100 * rat[k]['lfl']:.0f}" for k in ("w1", "w4", "w6")) + ".")
def fees(k, kk):
    rows = rows_of(*D[k]); S = {}
    for key in ("fee_initial", "fee_audit", "fee_panel", "fee_other"):
        S[key] = np.mean([sum(v.get(key, 0.0) for v in groups(e)[kk]) / len(groups(e)[kk]) for e in D[k][0]])
    return S
FE = {k: {kk: fees(k, kk) for kk in ("claim", "care")} for k in ("w1", "w2", "w3", "w4")}
def fee_gap(a, b, keys): return sum(FE[b]["care"][x] - FE[b]["claim"][x] for x in keys) - sum(FE[a]["care"][x] - FE[a]["claim"][x] for x in keys)
L.append(f"- §114b.2, the fees' part of the doubling's gap (P3.2's table; the careful's fee income less the dosing slots', the doubled world less the world of record): on the first review and the audit seat alone {fee_gap('w1', 'w2', ('fee_initial', 'fee_audit')):+.1f} under the pin and {fee_gap('w3', 'w4', ('fee_initial', 'fee_audit')):+.1f} under arm 1; with the panels and the other seats {fee_gap('w1', 'w2', ('fee_initial', 'fee_audit', 'fee_panel', 'fee_other')):+.1f} and {fee_gap('w3', 'w4', ('fee_initial', 'fee_audit', 'fee_panel', 'fee_other')):+.1f}.")
cma = {rid: mse(col(rows_of(P4[rid], CW[w]), "care_minus_all")) for rid, w in (("r1", "w1"), ("r2", "w4"), ("r3", "w6"), ("r4", "w4"), ("r5", "w4"), ("r6", "w6"), ("r7", "w3"), ("r8", "w4"))}
L.append("- §114c, the careful group beside a conduct less the all-careful (P4's table, read by read): " + "; ".join(f"read {rid[1]} {m[0]:+.0f} ± {m[1]:.0f}" for rid, m in cma.items()) + ".")
# ---------------------------------------------------------------- Q3.3 the founders' two reads paired by seed
L += ["", "## Q3.3. The founders' two reads, paired by seed: conduct M's slots in place from tick 0 less the plain dose's, worlds 1, 4 and 6\n"] + HDR_P
F0 = lambda v: v["t_in"] == 0
for rid, w in (("r1", "w1"), ("r2", "w4"), ("r3", "w6")):
    paired_rows(L, f"conduct M at 0.1 less the plain dose at 0.1, {WN[w]} — the founders", rows_of(D[w][0], D[w][1], F0), rows_of(P4[rid], CW[w], F0))
# ---------------------------------------------------------------- Q3.4 conduct M between the designs
L += ["", "## Q3.4. Conduct M at 0.1 between the designs, paired by seed on the hundred seeds (the gap careful − M in one cell less the gap in the other)\n"] + HDR_P
M = {w: rows_of(P4[rid], CW[w]) for rid, w in (("r1", "w1"), ("r2", "w4"), ("r3", "w6"))}; Mg = {w: rows_of(P4[rid], CW[w], F0) for rid, w in (("r1", "w1"), ("r2", "w4"), ("r3", "w6"))}
paired_rows(L, "world 1's cell less world 6's (the pin less arm 4) — all its slots", M["w6"], M["w1"]); paired_rows(L, "world 1's cell less world 6's — the founders", Mg["w6"], Mg["w1"])
paired_rows(L, "world 4's cell less world 1's (arm 1 with the weight doubled less the pin) — all its slots", M["w1"], M["w4"]); paired_rows(L, "world 4's cell less world 1's — the founders", Mg["w1"], Mg["w4"])
# ---------------------------------------------------------------- Q3.5 the arithmetic of "13 to 7"
L += ["", "## Q3.5. The arithmetic behind \"13 (the pin) to 7 (arm 1 doubled) real a claim left to lose by P3.3's phases\" — the candidates recomputed\n",
      "What a further wrong planted verdict costs a marked record in the all-careful by P3.3 (the income a tick after the seats return less while they are lost, over the ticks lost), and the chance a claim on a marked record is a wrong planted verdict (conduct F's further failures over its claims after the first, reads 5 and 6 of record):\n",
      "| world | (after − lost) × ticks lost | (before − lost) × ticks lost | F: further failures a claim | **cost of a failure × the chance a claim fails** |", "|---|---|---|---|---|"]
CF = {}
for k, rid in (("w1", None), ("w4", "r5"), ("w6", "r6")):
    V = [v for c in D[k][1].values() for v in json.loads(c["learner_slots_json"]).values()]; Fv = [v for v in V if v.get("pfail_ticks")]
    inc = lambda ph: sum(v[f"pf_income_{ph}"] for v in Fv) / max(1, sum(v[f"pf_ticks_{ph}"] for v in Fv)); back = [v for v in Fv if v.get("pf_back_t") is not None]
    tl = np.mean([v["pf_ticks_lost"] for v in back]) if back else np.nan; c1 = (inc("after") - inc("lost")) * tl; c2 = (inc("before") - inc("lost")) * tl
    pf = np.nan
    if rid:
        fs = [v for e in P4[rid] for v in groups(e)["claim"] if v.get("pfail_ticks")]; pf = sum(len(v["pfail_ticks"]) - 1 for v in fs) / max(1, sum(v.get("claims_after_fail", 0) for v in fs))
    CF[k] = (c1, c2, pf); L.append(f"| {WN[k]} | {c1:.0f} | {c2:.0f} | {pf if not np.isnan(pf) else float('nan'):.3f} | **{c1 * pf if not np.isnan(pf) else float('nan'):.1f}** |")
# ---------------------------------------------------------------- Q3.6 conduct F from the first failure on
def failed_rows(E, pol_name):
    """Per seed, among the slots that ever had a wrong planted verdict: F's failed slots less the careful failed slots of the same world and seed, from the tick of the first failure to the exit — the income of record (the wallet's real change plus the benefit from that tick), with the reservation, and like for like (the careful's good-standing income from the failure less F's good-standing rate from it times the careful's good ticks from it); the tallies."""
    out = []
    for e in E:
        g = groups(e); Fs = [v for v in g["claim"] if v.get("pfail_ticks")]; Cs = [v for v in g["care"] if v.get("pfail_ticks")]
        if not Fs or not Cs or "pf_good_ticks_lost" not in Fs[0]: continue
        def agg(V):
            n = len(V); inc = sum(v["pf_income_lost"] + v["pf_income_after"] for v in V) / n; ben = sum(v["pf_benefit_lost"] + v["pf_benefit_after"] for v in V) / n
            gt = sum(v["pf_good_ticks_lost"] + v["pf_good_ticks_after"] for v in V) / n; gi = sum(v["pf_good_income_lost"] + v["pf_good_income_after"] for v in V) / n; gb = sum(v["pf_benefit_lost"] + v["pf_benefit_after"] for v in V) / n
            return dict(n=n, rec=inc + ben, res=inc + ben + RES * sum(after(v) for v in V) / n, gt=gt, gi=gi, rate=((gi + gb) / gt if gt else np.nan), brate=(gb / gt if gt else np.nan),
                        claims=sum(v.get("claims_after_fail", 0) for v in V) / n, held=sum(v.get("claims_member_held", 0) for v in V) / n, lost=sum(v.get("claims_member_lost", 0) for v in V) / n,
                        more=sum(len(v["pfail_ticks"]) - 1 for v in V) / n, tlost=sum(v["pf_ticks_lost"] for v in V) / n, susp=sum(v["suspensions"] for v in V) / n, dep=sum(1 for v in V if not v["alive"]) / n,
                        ticks=sum(v["pf_ticks_lost"] + v["pf_ticks_after"] for v in V) / n, back=sum(1 for v in V if v.get("pf_back_t") is not None) / n, ben=ben)
        a, c = agg(Fs), agg(Cs)
        out.append(dict(seed=int(e["seed"]), F=a, C=c, rec=c["rec"] - a["rec"], res=c["res"] - a["res"], lfl=c["gi"] - a["rate"] * c["gt"], den=a["brate"] * c["gt"], ben=a["ben"], claims=a["claims"]))
    return out
def failed_table(L, name, rows):
    if not rows: L.append(f"| {name} | (pending) | | | | | |"); return
    a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl")); ta, tb, tc = temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")
    gF = lambda k: np.mean([r["F"][k] for r in rows]); gC = lambda k: np.mean([r["C"][k] for r in rows])
    L.append(f"| {name} | {len(rows)} | {gF('n'):.1f} / {gC('n'):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({ta[0]:.1f}) | **{b[0]:+.0f} ± {b[1]:.0f}** ({tb[0]:.1f}) | **{c[0]:+.0f} ± {c[1]:.0f}** ({tc[0]:.1f}) | {gF('claims'):.1f} ({gF('held'):.1f} / {gF('lost'):.1f}) | {gF('more'):.2f} / {gC('more'):.2f} | {gF('tlost'):.0f} / {gC('tlost'):.0f} ({gF('back'):.2f} / {gC('back'):.2f}) | {gF('susp'):.2f} / {gC('susp'):.2f}; {gF('dep'):.2f} / {gC('dep'):.2f} | {gF('ticks'):.0f} / {gC('ticks'):.0f} |")
HDR_F = ["| read | seeds | failed slots a seed: F / careful | **from the first failure: of record** (level at) | **with the reservation** (level at) | **like for like** (level at) | F's claims after the first failure a slot (seats held / lost at the claim) | further wrong planted verdicts a slot: F / careful | ticks without the earned seats: F / careful (share whose seats returned) | suspensions a slot: F / careful; departed share: F / careful | ticks from the first failure to the exit: F / careful |", "|---|---|---|---|---|---|---|---|---|---|---|"]
L += ["", "## Q3.6. Conduct F from the first failure on — among the slots that ever had a wrong planted verdict, F's less the careful's of the same world and seeds (reads 5 and 6 run again whole at b1fa10d2c for the split, a16/r5b and r6b; read 10 on its 180 seeds and with read 5 on 240)\n",
      "The three lifetimes cut at the first failure's tick: of record the wallet's real change from that tick to the exit plus the benefit earned from it; with the reservation the same plus 0.8 real a tick from a departure to the run's end; like for like the careful failed slots' good-standing income from their first failure less F's good-standing rate from its first failure (income and benefit over good ticks) times the careful's good ticks from it. Level at: the temptation at which the gap closes (of record and with the reservation over the benefit from the failure; like for like over F's benefit rate times the careful's good ticks).\n"] + HDR_F
RB = {"r5b": load([f"{B}/r5b"], "mix:doseF0.3:0.25")[0], "r6b": load([f"{B}/r6b"], "mix:doseF0.3:0.25")[0]}
R10 = load([f"{B}/r10/s81-125", f"{B}/r10/s126-170", f"{B}/r10/s171-215", f"{B}/r10/s216-260"], "mix:doseF0.3:0.25")[0]
rep = []
for rid, ref in (("r5b", "r5"), ("r6b", "r6")):
    a = {int(e["seed"]): (f(e, "half_d_lifetime_per_slot"), f(e, "half_claim_claims"), f(e, "false_approvals")) for e in RB[rid]}; b = {int(e["seed"]): (f(e, "half_d_lifetime_per_slot"), f(e, "half_claim_claims"), f(e, "false_approvals")) for e in P4[ref]}
    com = sorted(set(a) & set(b)); rep.append(f"read {ref[1]} run again on {len(com)} seeds {'**to the digit**' if com and all(all(abs(x - y) < 1e-9 for x, y in zip(a[s], b[s])) for s in com) else '**DIFFERS**'}")
L.insert(len(L) - 2, "Reproduction: " + "; ".join(rep) + " (the gap, the claims, the false approvals).\n")
FR = {"r5": failed_rows(RB["r5b"], "r5"), "r6": failed_rows(RB["r6b"], "r6"), "r10": failed_rows(R10, "r10")}; FR["r5+r10"] = FR["r5"] + FR["r10"]
failed_table(L, "5. conduct F, world 4's cell, seeds 21–80", FR["r5"]); failed_table(L, "6. conduct F, world 6's cell (arm 4), seeds 21–80", FR["r6"])
failed_table(L, "10. conduct F, world 4's cell, seeds 81–260", FR["r10"]); failed_table(L, "5 + 10. conduct F, world 4's cell, the 240 seeds", FR["r5+r10"])
# ---------------------------------------------------------------- Q4 reads 9–11
L += ["", "## Q4. Reads 9, 10 and 11 — the three lifetimes with their level temptations (read as P4 was)\n"] + HDR_L
R9 = load([f"{B}/r9/s21-70", f"{B}/r9/s71-120"], "mix:doseM0.1:0.25")[0]; R11 = load([f"{B}/r11/s21-80"], "mix:doseM0.1:0.75")[0]
Q = {}
Q["r9"] = rows_of(R9, CW["w3"]); Q["r9g"] = rows_of(R9, CW["w3"], F0); L.append(lifetimes_row("9. conduct M at 0.1, world 3's cell (arm 1, π^A 0.10, the weight of record), 1 slot in 4", Q["r9"])); L.append(lifetimes_row("9. … the slots in place from tick 0 alone", Q["r9g"]))
Q["r10"] = rows_of(R10, CW["w4"]); Q["r5"] = rows_of(P4["r5"], CW["w4"]); Q["r10all"] = Q["r5"] + Q["r10"]
L.append(lifetimes_row("10. conduct F, world 4's cell, the seeds added (81–260)", Q["r10"])); L.append(lifetimes_row("10. … the first sixty seeds (read 5, 21–80)", Q["r5"])); L.append(lifetimes_row("10. … the 240 seeds together", Q["r10all"]))
Q["r11"] = rows_of(R11, CW["w4"]); Q["r11g"] = rows_of(R11, CW["w4"], F0); L.append(lifetimes_row("11. conduct M at 0.1, world 4's cell, 3 slots in 4", Q["r11"])); L.append(lifetimes_row("11. … the slots in place from tick 0 alone", Q["r11g"]))
L.append(lifetimes_row("2. conduct M at 0.1, world 4's cell, 1 slot in 4 (P4's read 2, for comparison)", rows_of(P4["r2"], CW["w4"])))
L += ["", "## Q4. Both groups a slot, the lifetime lost for each claim, and the honest side\n"] + HDR_G
for nm, key in (("9. conduct M at 0.1, world 3's cell, 1 in 4", "r9"), ("9. … in place from tick 0", "r9g"), ("10. conduct F, world 4's cell, seeds 81–260", "r10"), ("10. … the 240 seeds", "r10all"), ("11. conduct M at 0.1, world 4's cell, 3 in 4", "r11"), ("11. … in place from tick 0", "r11g")):
    L.append(groups_row(nm, Q[key]))
L.append(groups_row("2. conduct M at 0.1, world 4's cell, 1 in 4 (P4's read 2)", rows_of(P4["r2"], CW["w4"])))
L += ["", "**Conduct F — the failure's share, the tick of the first and the claims after it (the conduct's slots):**\n", "| read | slots with a wrong planted verdict (share) | tick of the first (mean) | claims a slot: all / as a member / on probation |", "|---|---|---|---|"]
for nm, key in (("10. seeds 81–260", "r10"), ("5 + 10. the 240 seeds", "r10all")):
    rows = Q[key]
    if rows: L.append(f"| {nm} | {grp(rows, 'claim', 'failed'):.3f} | {np.nanmean(col([r['claim'] for r in rows], 'first_t')):.0f} | {grp(rows, 'claim', 'claims'):.1f} / {grp(rows, 'claim', 'cm'):.1f} / {grp(rows, 'claim', 'cp'):.1f} |")
L += ["", "## Paired contrasts on the shared seeds\n"] + HDR_P
paired_rows(L, "read 9 less read 2: world 4's cell less world 3's for conduct M (the weight doubled less the weight of record) — all its slots", Q["r9"], rows_of(P4["r2"], CW["w4"]))
paired_rows(L, "… the founders", Q["r9g"], rows_of(P4["r2"], CW["w4"], F0))
paired_rows(L, "read 9 less the plain dose in world 3 (conduct M less the plain dose at 0.1, world 3's cell)", rows_of(*D["w3"]), Q["r9"])
paired_rows(L, "read 11 less read 2 (conduct M on 3 in 4 less on 1 in 4, world 4's cell)", rows_of(P4["r2"], CW["w4"]), Q["r11"])
# the world's side for read 11
r2 = rows_of(P4["r2"], CW["w4"])
if Q["r11"]:
    L += ["", "**Read 11's world beside the all-careful's and read 2's** (the standing false approvals a run; the leak per thousand bad deliveries; the system's overhead a vested task; mean over the seeds):\n", "| world | FA | leak ‰ | overhead |", "|---|---|---|---|",
          f"| read 11: conduct M on 3 in 4, world 4's cell | {np.mean(col(Q['r11'], 'fa')):.1f} | {np.mean(col(Q['r11'], 'leak')):.1f} | {np.mean(col(Q['r11'], 'oh')):.2f} |",
          f"| the all-careful, world 4, the same seeds | {np.mean(col(Q['r11'], 'fa0')):.1f} | {np.mean(col(Q['r11'], 'leak0')):.1f} | {np.mean(col(Q['r11'], 'oh0')):.2f} |",
          f"| read 2: conduct M on 1 in 4, world 4's cell (seeds 21–120) | {np.mean(col(r2, 'fa')):.1f} | {np.mean(col(r2, 'leak')):.1f} | {np.mean(col(r2, 'oh')):.2f} |"]
# ---------------------------------------------------------------- expectations and refutations
L += ["", "## Against the expectations stated before the run\n", "| statement | read | |", "|---|---|---|"]
def chk(name, cond, read): L.append(f"| {name} | {read} | {'met' if cond else 'MISSED'} |")
def g(key, k): rows = Q[key]; return mse(col(rows, k)) if rows else (np.nan, np.nan)
if Q["r9"]:
    a, ag, b, c = g("r9", "rec"), g("r9g", "rec"), g("r9", "res"), g("r9", "lfl"); tc = temp(Q["r9"], "lfl", "den")
    chk("read 9: M behind by 70 to 210 of record, all its slots", 70 <= a[0] <= 210, f"{a[0]:+.0f} ± {a[1]:.0f}"); chk("read 9: … the founders alone, 70 to 210", 70 <= ag[0] <= 210, f"{ag[0]:+.0f} ± {ag[1]:.0f}")
    chk("read 9: by 50 to 170 with the reservation", 50 <= b[0] <= 170, f"{b[0]:+.0f} ± {b[1]:.0f}"); chk("read 9: by 40 to 130 like for like", 40 <= c[0] <= 130, f"{c[0]:+.0f} ± {c[1]:.0f}"); chk("read 9: level at 3.5 to 7 like for like", 3.5 <= tc[0] <= 7, f"{tc[0]:.1f} ± {tc[1]:.1f}")
    A_ = {r["seed"]: r for r in Q["r9"]}; B_ = {r["seed"]: r for r in r2}; seeds = sorted(set(A_) & set(B_))
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        m = mse([B_[s][key] - A_[s][key] for s in seeds]); chk(f"read 9: world 4's cell less world 3's within two standard errors of nothing, {kn}", abs(m[0]) <= 2 * m[1], f"{m[0]:+.0f} ± {m[1]:.0f} ({m[0] / m[1]:.1f} SE)")
if Q["r10"]:
    rows = Q["r10all"]; a, b, c = g("r10all", "rec"), g("r10all", "res"), g("r10all", "lfl"); ts = [temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")]
    chk("read 10 (240 seeds): F behind at the point value on each lifetime", a[0] > 0 and b[0] > 0 and c[0] > 0, f"{a[0]:+.0f} / {b[0]:+.0f} / {c[0]:+.0f}"); chk("read 10: by 0 to 90 of record", 0 <= a[0] <= 90, f"{a[0]:+.0f} ± {a[1]:.0f}")
    chk("read 10: by two standard errors or more like for like", c[0] >= 2 * c[1], f"{c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE)"); chk("read 10: level at 1.5 to 4 on each lifetime", all(1.5 <= t[0] <= 4 for t in ts), " / ".join(f"{t[0]:.1f} ± {t[1]:.1f}" for t in ts))
    chk("read 10: under 8 claims a slot", grp(rows, "claim", "claims") < 8, f"{grp(rows, 'claim', 'claims'):.1f}")
    fr = FR["r5+r10"]; m = [mse(col(fr, k)) for k in ("rec", "res", "lfl")] if fr else [(np.nan, np.nan)] * 3
    chk("read 10: from the first failure on, F's failed slots behind the careful's failed slots at the point value", all(x[0] > 0 for x in m), " / ".join(f"{x[0]:+.0f} ± {x[1]:.0f}" for x in m))
if Q["r11"]:
    a, b = g("r11", "rec"), g("r11", "res"); lk = np.mean(col(Q["r11"], "leak")); oh = np.mean(col(Q["r11"], "oh")) - np.mean(col(Q["r11"], "oh0"))
    chk("read 11: the conduct's slots behind by 80 to 280 of record", 80 <= a[0] <= 280, f"{a[0]:+.0f} ± {a[1]:.0f}"); chk("read 11: by two standard errors or more with the reservation", b[0] >= 2 * b[1], f"{b[0]:+.0f} ± {b[1]:.0f} ({b[0] / b[1]:.1f} SE)")
    chk("read 11: the leak under 15 in a thousand", lk < 15, f"{lk:.1f}"); chk("read 11: the overhead within 1.5 a task of the all-careful's", abs(oh) <= 1.5, f"{oh:+.2f}")
L.append("")
if Q["r9"]:
    b, c = g("r9", "res"), g("r9", "lfl"); L.append(f"**Refuted or shown, each apart.** *The combination holds the conduct without the doubled weight* — refuted if in read 9 conduct M is within two standard errors of nothing with the reservation counted or like for like: {b[0]:+.0f} ± {b[1]:.0f} ({b[0] / b[1]:.1f} SE) and {c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE) — **{'REFUTED' if (b[0] <= 2 * b[1] or c[0] <= 2 * c[1]) else 'not refuted'}**.")
if Q["r10"]:
    rows = Q["r10all"]; ts = [temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")]; gs = [g("r10all", k) for k in ("rec", "res", "lfl")]
    L.append(f"*A marked record has less to lose than a clean one* — refuted if on the 240 seeds conduct F is level at a temptation of 5.5 or more on any lifetime: level at {', '.join(f'{t[0]:.1f} ± {t[1]:.1f}' for t in ts)} — **{'REFUTED' if any(t[0] >= 5.5 for t in ts) else 'not refuted'}**.")
    L.append(f"*Skipping pays once a record is marked* — shown if conduct F is ahead by two standard errors on any lifetime, or level at a temptation under 1 on all three: {', '.join(f'{x[0]:+.0f} ± {x[1]:.0f} ({x[0] / x[1]:.1f} SE)' for x in gs)}; level at {', '.join(f'{t[0]:.1f}' for t in ts)} — **{'SHOWN' if (any(x[0] < -2 * x[1] for x in gs) or all(t[0] < 1 for t in ts)) else 'not shown'}**.")
if Q["r11"]:
    b, c = g("r11", "res"), g("r11", "lfl"); L.append(f"*The combination holds the conduct when most members follow it* — refuted if in read 11 the conduct's slots are within two standard errors of nothing with the reservation counted or like for like: {b[0]:+.0f} ± {b[1]:.0f} ({b[0] / b[1]:.1f} SE) and {c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE) — **{'REFUTED' if (b[0] <= 2 * b[1] or c[0] <= 2 * c[1]) else 'not refuted'}**.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
