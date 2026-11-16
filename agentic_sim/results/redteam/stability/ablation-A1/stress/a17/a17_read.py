"""Addendum 17 (November 16, 2026; notes §116): V3's five readings from the worlds on record (a15/, a16/ — no run) and V4's three reads without training (a17/r12,
r13, r14 by launch.sh), read as P4, Q4 and Q3's item 6 were (a16_read.py's helpers copied: the three lifetimes paired by seed, the level temptations, both groups a
slot, the lifetime lost for each claim, the cut at the first failure), with the expectations stated before the run and the three refutations or showings.
Usage: a17_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; A = f"{R}/a15"; B = f"{R}/a16"; C = f"{R}/a17"
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
# ---------------------------------------------------------------- the worlds of record (a15, a16) and the new ones (a17)
D = {}
for k, dirs in {"w1": [f"{A}/rerun/w1-s21-70", f"{A}/rerun/w1-s71-120"], "w2": [f"{A}/rerun/w2"], "w3": [f"{A}/rerun/w3"], "w4": [f"{A}/rerun/w4"], "w6": [f"{A}/rerun/w6-s21-70", f"{A}/rerun/w6-s71-120"]}.items():
    D[k] = load(dirs, "mix:dose0.1:0.25")
CW = {k: dict(D[k][1]) for k in D}
CW["w4"].update(load([f"{A}/p4/r2-s81-120"], "careful")[1]); CW["w3"].update(load([f"{B}/r9/careful-w3-s81-120"], "careful")[1])
CW["w4"].update(load([f"{B}/r10/careful-w4-s121-125", f"{B}/r10/s126-170", f"{B}/r10/s171-215", f"{B}/r10/s216-260"], "careful")[1])
CW3_NEW = load([f"{C}/r12/s121-170", f"{C}/r12/s171-215", f"{C}/r12/s216-260"], "careful")[1]; CW["w3"].update(CW3_NEW)
P4 = {}
for rid, dirs, pol in (("r2", [f"{A}/p4/r2-s21-80", f"{A}/p4/r2-s81-120"], "mix:doseM0.1:0.25"), ("r3", [f"{A}/p4/r3-s21-70", f"{A}/p4/r3-s71-120"], "mix:doseM0.1:0.25"), ("r4", [f"{A}/p4/r4"], "mix:doseM0.3:0.25"), ("r5", [f"{A}/p4/r5"], "mix:doseF0.3:0.25")):
    P4[rid] = load(dirs, pol)[0]
R9 = load([f"{B}/r9/s21-70", f"{B}/r9/s71-120"], "mix:doseM0.1:0.25")[0]; R11 = load([f"{B}/r11/s21-80"], "mix:doseM0.1:0.75")[0]
R10 = load([f"{B}/r5b"], "mix:doseF0.3:0.25")[0] + load([f"{B}/r10/s81-125", f"{B}/r10/s126-170", f"{B}/r10/s171-215", f"{B}/r10/s216-260"], "mix:doseF0.3:0.25")[0]   # the 240 seeds (read 5 at b1fa10d2c + read 10)
R6B = load([f"{B}/r6b"], "mix:doseF0.3:0.25")[0]
R12 = load([f"{C}/r12/s21-70", f"{C}/r12/s71-120", f"{C}/r12/s121-170", f"{C}/r12/s171-215", f"{C}/r12/s216-260"], "mix:doseF0.3:0.25")[0]
R13 = load([f"{C}/r13/s21-70", f"{C}/r13/s71-120", f"{C}/r13/s121-170", f"{C}/r13/s171-215", f"{C}/r13/s216-260"], "mix:doseG0.3:0.25")[0]
R14 = load([f"{C}/r14b/s{a}-{b}" for a, b in ((21, 50), (51, 80), (81, 110), (111, 140))], "mix:doseF1.0:0.25")[0] or load([f"{C}/r14/s21-80", f"{C}/r14/s81-140"], "mix:doseF1.0:0.25")[0]   # r14b (575e405b1, with claims_pre_susp) where it exists, else r14 (59ce02e20)
F0 = lambda v: v["t_in"] == 0; F1 = lambda v: v["t_in"] > 0; ALL = lambda v: True
L = ["# Addendum 17: V3's five readings from the worlds on record, and V4's three reads without training (November 16, 2026; a17/launch.sh)\n"]
# ---------------------------------------------------------------- V3.1 the scale
def stats(V):
    n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
    return dict(n=n, good=good, ig=ig, bg=bg, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n,
                lres=sum(life(v) + RES * after(v) for v in V) / n, ben=sum(v["private_real"] for v in V) / n, claims=sum(v["claims"] for v in V) / n, susp=sum(v["suspensions"] for v in V) / n,
                ticks=sum(v["ticks"] for v in V) / n, dep=sum(1 for v in V if not v["alive"]) / n)
L += ["## V3.1. The scale: a careful slot's mean lifetime in the all-careful populations (seeds 21–120; real; the mean over the seeds of the seed's mean a slot, ± its standard error)\n",
      "Of record the wallet's real wealth at the exit (plus the benefit, nothing for the careful); with the reservation the same plus 0.8 real a tick from a departure to the run's end; like for like the slot's income in good standing (the careful's own good-standing income, the quantity the like-for-like gap is taken from). The slots in place from tick 0 are the founders; an arrival enters later as a probationer.\n",
      "| world | slots | slots a seed | **of record** | **with the reservation** | **like for like (income in good standing)** | good ticks a slot | ticks in place | departed share | suspensions a slot |", "|---|---|---|---|---|---|---|---|---|---|"]
SCALE = {}
for k in ("w1", "w3", "w4", "w6"):
    for nm, filt in (("all", ALL), ("the founders", F0), ("the arrivals", F1)):
        rows = []
        for s, c in sorted(CW[k].items()):
            if s > 120: continue
            V = [v for v in json.loads(c["learner_slots_json"]).values() if filt(v)]
            if V: rows.append(stats(V))
        m = {key: mse([r[key] for r in rows]) for key in ("life", "lres", "ig", "good", "ticks", "dep", "susp", "n")}; SCALE[(k, nm)] = m
        L.append(f"| {WN[k]} | {nm} | {m['n'][0]:.1f} | **{m['life'][0]:.0f} ± {m['life'][1]:.0f}** | **{m['lres'][0]:.0f} ± {m['lres'][1]:.0f}** | **{m['ig'][0]:.0f} ± {m['ig'][1]:.0f}** | {m['good'][0]:.0f} | {m['ticks'][0]:.0f} | {m['dep'][0]:.2f} | {m['susp'][0]:.2f} |")
# ---------------------------------------------------------------- V3.2 the conduct's slots against the all-careful world's slots
def rows_vs_all(E, C, filt=ALL, group="claim"):
    """Per seed: the conduct's slots (or both groups, group='both') less the all-careful population's slots of the same seed, on the three lifetimes (negative = behind); like for like
    the conduct's good-standing rate times the all-careful's good ticks less the all-careful's good-standing income; the shares against the all-careful's own figure."""
    out = []
    for e in E:
        g = groups(e); V = [v for kk in (("claim", "care") if group == "both" else (group,)) for v in g[kk] if filt(v)]
        if not V or int(e["seed"]) not in C: continue
        Vc = [v for v in json.loads(C[int(e["seed"])]["learner_slots_json"]).values() if filt(v)]
        if not Vc: continue
        s, a = stats(V), stats(Vc)
        out.append(dict(seed=int(e["seed"]), s=s, a=a, rec=s["life"] - a["life"], res=s["lres"] - a["lres"], lfl=s["rate"] * a["good"] - a["ig"], den=s["brate"] * a["good"], ben=s["ben"], claims=s["claims"],
                        sh_rec=(s["life"] - a["life"]) / a["life"], sh_res=(s["lres"] - a["lres"]) / a["lres"], sh_lfl=(s["rate"] * a["good"] - a["ig"]) / a["ig"]))
    return out
def vs_all_row(name, rows, R_=""):
    if not rows: return f"| {name} | (pending) | | | | |"
    m = {k: mse(col(rows, k)) for k in ("rec", "res", "lfl", "sh_rec", "sh_res", "sh_lfl")}
    return (f"| {name} | {len(rows)} | **{m['rec'][0]:+.0f} ± {m['rec'][1]:.0f}** ({100 * m['sh_rec'][0]:+.1f} in 100) | **{m['res'][0]:+.0f} ± {m['res'][1]:.0f}** ({100 * m['sh_res'][0]:+.1f}) | "
            f"**{m['lfl'][0]:+.0f} ± {m['lfl'][1]:.0f}** ({100 * m['sh_lfl'][0]:+.1f}) | {R_} |")
HDR_V = ["| read | seeds | **of record** (share of the all-careful's) | **with the reservation** (share) | **like for like** (share) | the reviewer's figure (R) |", "|---|---|---|---|---|---|"]
L += ["", "## V3.2. The conduct's slots less the all-careful world's slots, paired by seed (negative = behind; the share against the all-careful population's own mean a slot)\n",
      "The all-careful population's slots are every slot of the all-careful world at the seed, founders and arrivals alike; the conduct's slots are the conduct's group in the mixed world. Like for like: the conduct's good-standing rate (income and benefit over good ticks) times the all-careful's good ticks, less the all-careful's good-standing income.\n"] + HDR_V
VS = {}
for name, E, w, grp_, R_ in (("2. conduct M at 0.1, world 4's cell, 1 in 4 (seeds 21–120)", P4["r2"], "w4", "claim", "−101"), ("4. conduct M at 0.3, world 4's cell, 1 in 4 (21–80)", P4["r4"], "w4", "claim", "−303"),
                             ("9. conduct M at 0.1, world 3's cell, 1 in 4 (21–120)", R9, "w3", "claim", "−83"), ("10. conduct F at 0.3, world 4's cell, 1 in 4 (the 240 seeds)", R10, "w4", "claim", "−51"),
                             ("11. conduct M at 0.1, world 4's cell, 3 in 4 (21–80) — the conduct's slots", R11, "w4", "claim", "−50"), ("11. … the whole population (both groups) less the all-careful's", R11, "w4", "both", "")):
    VS[name] = rows_vs_all(E, CW[w], ALL, grp_); L.append(vs_all_row(name, VS[name], R_))
# ---------------------------------------------------------------- V3.3 the careful members' own wrong planted verdicts for each planted case
L += ["", "## V3.3. The careful members' wrong planted verdicts for each planted case, and the planted cases that reach a slot in a hundred ticks, by seat — the all-careful populations of worlds 3 and 6\n",
      "From the record (seeds 21–120): the first review's split by the case's kind is of record (the dial's clock: `bad_plants_approved`, `good_plants_rejected` against the bad plants met there and the good); the seats past it (audit, panel, resumed) carry their failures together — the slots' failure ticks less the first review's — over the plants met there, with the bad share among them. The split by seat and by kind at every seat is exact on world 3's all-careful of seeds 121–260 (run beside read 12 with the reading added at the harness commit: `plant_fail_{bad,good}_<seat>` over `bad_met_<seat>` and the good met). Rates are ratios of sums over the seeds, ± the delta-method error; the plants a slot in a hundred ticks are the learners' decisions on plants at the seat over the slots' ticks in place.\n",
      "| world | seeds | **first review: bad work approved / bad met** | **first review: good work rejected / good met** | **later seats (audit, panel, resumed): failures / plants met** (bad share of the plants met there) | plants reaching a slot in 100 ticks: first review / audit / panel / resumed |", "|---|---|---|---|---|---|"]
def v33(k, C, seeds):
    ba, bm, gr, gm, lf, lm, lb, tk = [], [], [], [], [], [], [], []; seen = {s_: [] for s_ in ("initial", "audit", "panel", "resumed")}
    for s, e in sorted(C.items()):
        if not seeds(s): continue
        V = list(json.loads(e["learner_slots_json"]).values()); tot = sum(len(v["pfail_ticks"]) for v in V)
        ba.append(f0(e, "bad_plants_approved")); bm.append(f0(e, "bad_met_initial")); gr.append(f0(e, "good_plants_rejected")); gm.append(f0(e, "seat_initial_plant_seen") - f0(e, "bad_met_initial"))
        later = sum(f0(e, f"seat_{s_}_plant_seen") for s_ in ("audit", "panel", "resumed")); lf.append(tot - f0(e, "bad_plants_approved") - f0(e, "good_plants_rejected")); lm.append(later)
        lb.append(sum(f0(e, f"bad_met_{s_}") for s_ in ("audit", "third", "appeal", "dispute", "resumed"))); tk.append(sum(v["ticks"] for v in V) / 100.0)
        for s_ in seen: seen[s_].append(f0(e, f"seat_{s_}_plant_seen"))
    r1, r2, r3, r4 = ratio_se(ba, bm), ratio_se(gr, gm), ratio_se(lf, lm), ratio_se(lb, lm); per = [ratio_se(seen[s_], tk)[0] for s_ in ("initial", "audit", "panel", "resumed")]
    return (f"**{r1[0]:.3f} ± {r1[1]:.3f}** ({sum(ba):.0f} / {sum(bm):.0f}) | **{r2[0]:.3f} ± {r2[1]:.3f}** ({sum(gr):.0f} / {sum(gm):.0f}) | **{r3[0]:.3f} ± {r3[1]:.3f}** ({sum(lf):.0f} / {sum(lm):.0f}; bad {r4[0]:.2f}) | "
            f"{per[0]:.2f} / {per[1]:.2f} / {per[2]:.2f} / {per[3]:.2f}", len(ba))
for k in ("w3", "w6"):
    t, n = v33(k, CW[k], lambda s: s <= 120); L.append(f"| {WN[k]} | {n} (21–120) | {t} |")
if CW3_NEW:
    t, n = v33("w3", CW3_NEW, lambda s: s > 120); L.append(f"| {WN['w3']} | {n} (121–260) | {t} |")
    L += ["", "**World 3's all-careful on seeds 121–260, exact by seat and by kind** (the members' wrong planted verdicts over the plants met at the seat; the third seat, the appeal and the dispute panels apart):\n",
          "| seat | plants met a seed (bad / good) | **bad work approved / bad met** | **good work rejected / good met** | failures a seed |", "|---|---|---|---|---|"]
    for s_ in ("initial", "audit", "third", "appeal", "dispute", "resumed"):
        E_ = list(CW3_NEW.values()); bm = [f0(e, f"bad_met_{s_}") for e in E_]; gm = [f0(e, f"plant_adj_{s_}") - f0(e, f"bad_met_{s_}") for e in E_]; fb = [f0(e, f"plant_fail_bad_{s_}") for e in E_]; fg = [f0(e, f"plant_fail_good_{s_}") for e in E_]
        r1, r2 = ratio_se(fb, bm), ratio_se(fg, gm)
        L.append(f"| {s_} | {np.mean(bm):.1f} / {np.mean(gm):.1f} | **{r1[0]:.3f} ± {r1[1]:.3f}** | **{r2[0]:.3f} ± {r2[1]:.3f}** | {np.mean(fb) + np.mean(fg):.2f} |")
# ---------------------------------------------------------------- V3.4 which of arm 4's founders moved
L += ["", "## V3.4. Which of arm 4's founders moved — world 6 under the plain dose and world 6's cell under conduct M: the dosing founders and the careful founders, each less the all-careful founders of the same seeds (negative = behind)\n"] + HDR_V
for name, E, grp_ in (("the plain dose at 0.1 (N4's world 6): the dosing founders", D["w6"][0], "claim"), ("… the careful founders beside them", D["w6"][0], "care"), ("conduct M at 0.1 (read 3): the dosing founders", P4["r3"], "claim"), ("… the careful founders beside them", P4["r3"], "care")):
    L.append(vs_all_row(name, rows_vs_all(E, CW["w6"], F0, grp_)))
L += ["", "The same two worlds, paired by seed, the dosing founders of conduct M less the plain dose's (each against the all-careful founders of the seed):\n"] + HDR_P
paired_rows(L, "conduct M's dosing founders less the plain dose's, against the all-careful founders (world 6)", [dict(r, rec=-r["rec"], res=-r["res"], lfl=-r["lfl"]) for r in rows_vs_all(D["w6"][0], CW["w6"], F0, "claim")], [dict(r, rec=-r["rec"], res=-r["res"], lfl=-r["lfl"]) for r in rows_vs_all(P4["r3"], CW["w6"], F0, "claim")])
paired_rows(L, "conduct M's careful founders less the plain dose's, against the all-careful founders (world 6)", [dict(r, rec=-r["rec"], res=-r["res"], lfl=-r["lfl"]) for r in rows_vs_all(D["w6"][0], CW["w6"], F0, "care")], [dict(r, rec=-r["rec"], res=-r["res"], lfl=-r["lfl"]) for r in rows_vs_all(P4["r3"], CW["w6"], F0, "care")])
# ---------------------------------------------------------------- V3.5 two lines
L += ["", "## V3.5. Two lines of §115\n"]
cnt = {}
for d in ("r9/s21-70", "r9/s71-120", "r9/careful-w3-s81-120", "r10/s81-125", "r10/s126-170", "r10/s171-215", "r10/s216-260", "r10/careful-w4-s121-125", "r11/s21-80", "r5b", "r6b"):
    j = json.load(open(f"{B}/{d}/eval.json")); cnt[d] = sum(len(v) for v in j["episodes"].values())
q4 = sum(v for d, v in cnt.items() if d not in ("r5b", "r6b")); rb = cnt["r5b"] + cnt["r6b"]
L.append(f"- §115a's episode count: a16's evaluations hold {q4 + rb} episodes — reads 9, 10 and 11 with their all-careful populations {q4} (read 9: {cnt['r9/s21-70'] + cnt['r9/s71-120']} + {cnt['r9/careful-w3-s81-120']}; read 10: 180 + 140 the all-careful on 121–260; read 11: {cnt['r11/s21-80']}), reads 5 and 6 run again {rb}. The '460' was a slip for {q4}; the whole and the 26 minutes stand.")
CF = {}
for k in ("w1", "w4", "w6"):
    V = [v for s, c in CW[k].items() if s <= 120 for v in json.loads(c["learner_slots_json"]).values()]; Fv = [v for v in V if v.get("pfail_ticks")]
    inc = lambda ph: sum(v[f"pf_income_{ph}"] for v in Fv) / max(1, sum(v[f"pf_ticks_{ph}"] for v in Fv)); back = [v for v in Fv if v.get("pf_back_t") is not None]
    tl = np.mean([v["pf_ticks_lost"] for v in back]) if back else np.nan; CF[k] = ((inc("after") - inc("lost")) * tl, (inc("before") - inc("lost")) * tl, inc("before"), inc("lost"), inc("after"), tl)
def per_further(rows):
    x = col(rows, "rec"); dm = np.array([r["F"]["more"] - r["C"]["more"] for r in rows]); r_ = ratio_se(x, dm); return r_
PF = {"w4": per_further(failed_rows(R10, "r10")), "w6": per_further(failed_rows(R6B, "r6b"))}
L.append(f"- §115b.5's cost of a further failure: with the income after the earned seats return (the survivors', §114's word) it is {CF['w1'][0]:.0f} / {CF['w4'][0]:.0f} / {CF['w6'][0]:.0f} real in worlds 1, 4 and 6 (the income a tick before the failure {CF['w1'][2]:.2f} / {CF['w4'][2]:.2f} / {CF['w6'][2]:.2f}, while the seats are lost {CF['w1'][3]:.2f} / {CF['w4'][3]:.2f} / {CF['w6'][3]:.2f}, after they return {CF['w1'][4]:.2f} / {CF['w4'][4]:.2f} / {CF['w6'][4]:.2f}; the ticks lost {CF['w1'][5]:.0f} / {CF['w4'][5]:.0f} / {CF['w6'][5]:.0f}); with the income before the failure it is **{CF['w1'][1]:.0f} / {CF['w4'][1]:.0f} / {CF['w6'][1]:.0f}** (the reviewer's 20 / 27 / 12). Item 6's own figures — the failed slots' gap of record over the further failures F takes beyond the careful's — give **{PF['w4'][0]:.0f} ± {PF['w4'][1]:.0f} real for each further failure in world 4's cell on the 240 seeds** (117 over 1.62 less 0.48 is 103) and {PF['w6'][0]:.0f} ± {PF['w6'][1]:.0f} under arm 4. The notes keep item 6's measured figure as the cost of a further failure on a marked record (it carries the bond, the seats, the suspension and the departure together, on the slots that bore it); §115b.5's phase arithmetic is withdrawn as that cost — the 'after' income was the survivors' and the 'before' one gives the lost seats' income alone, a part, not the whole.")
# ---------------------------------------------------------------- V4 reads 12, 13 and 14
L += ["", "## V4. Reads 12, 13 and 14 — the three lifetimes with their level temptations (read as P4 and Q4 were: the conduct's slots less the careful slots beside them in the same world, paired by seed; world 3's cell, the conduct on 1 slot in 4)\n"] + HDR_L
Q = {}
Q["r12"] = rows_of(R12, CW["w3"]); Q["r12h"] = [r for r in Q["r12"] if r["seed"] <= 120]; Q["r12g"] = rows_of(R12, CW["w3"], F0); Q["r12a"] = rows_of(R12, CW["w3"], F1)
Q["r13"] = rows_of(R13, CW["w3"]); Q["r13g"] = rows_of(R13, CW["w3"], F0); Q["r14"] = rows_of(R14, CW["w3"]); Q["r14g"] = rows_of(R14, CW["w3"], F0)
Q["r10"] = rows_of(R10, CW["w4"]); Q["r9"] = rows_of(R9, CW["w3"])
for nm, key in (("12. conduct F at 0.3, world 3's cell, 1 in 4 (seeds 21–260)", "r12"), ("12. … the first hundred seeds (21–120)", "r12h"), ("12. … the founders (in place from tick 0)", "r12g"), ("12. … the arrivals", "r12a"),
                ("13. conduct G at 0.3 (while the earned seats are lost), world 3's cell, 1 in 4 (21–260)", "r13"), ("13. … the founders", "r13g"),
                ("14. conduct F at 1.0, world 3's cell, 1 in 4 (21–140)", "r14"), ("14. … the founders", "r14g"),
                ("10. conduct F at 0.3, world 4's cell, the 240 seeds (for comparison)", "r10"), ("9. conduct M at 0.1, world 3's cell, 1 in 4 (for comparison)", "r9")):
    L.append(lifetimes_row(nm, Q[key]))
L += ["", "## V4. Both groups a slot, the lifetime lost for each claim, and the honest side\n"] + HDR_G
for nm, key in (("12. conduct F at 0.3, world 3's cell", "r12"), ("12. … the founders", "r12g"), ("13. conduct G at 0.3, world 3's cell", "r13"), ("14. conduct F at 1.0, world 3's cell", "r14"), ("10. conduct F at 0.3, world 4's cell (240)", "r10")):
    L.append(groups_row(nm, Q[key]))
L += ["", "**The failure's share, the tick of the first and the claims (the conduct's slots):**\n", "| read | slots with a wrong planted verdict (share) | tick of the first (mean) | claims a slot: all / as a member / on probation | claims a failed slot |", "|---|---|---|---|---|"]
for nm, key in (("12. conduct F at 0.3, world 3's cell", "r12"), ("13. conduct G at 0.3", "r13"), ("14. conduct F at 1.0", "r14"), ("10. conduct F at 0.3, world 4's cell", "r10")):
    rows = Q[key]
    if rows: L.append(f"| {nm} | {grp(rows, 'claim', 'failed'):.3f} | {np.nanmean(col([r['claim'] for r in rows], 'first_t')):.0f} | {grp(rows, 'claim', 'claims'):.1f} / {grp(rows, 'claim', 'cm'):.1f} / {grp(rows, 'claim', 'cp'):.1f} | {grp(rows, 'claim', 'claims') / max(1e-9, grp(rows, 'claim', 'failed')):.1f} |")
# ---------------------------------------------------------------- from the first failure on
L += ["", "## V4. From the first failure on — among the slots that ever had a wrong planted verdict, the conduct's less the careful slots' of the same world and seeds, the three lifetimes cut at that tick (as Q3's item 6)\n"] + HDR_F
FR = {"r12": failed_rows(R12, ""), "r13": failed_rows(R13, ""), "r14": failed_rows(R14, ""), "r10": failed_rows(R10, ""), "r6": failed_rows(R6B, "")}
failed_table(L, "12. conduct F at 0.3, world 3's cell (21–260)", FR["r12"]); failed_table(L, "13. conduct G at 0.3, world 3's cell (21–260)", FR["r13"]); failed_table(L, "14. conduct F at 1.0, world 3's cell (21–140)", FR["r14"])
failed_table(L, "10. conduct F at 0.3, world 4's cell, the 240 seeds (Q3.6)", FR["r10"]); failed_table(L, "6. conduct F at 0.3, world 6's cell (Q3.6)", FR["r6"])
def per_claim(rows): return [ratio_se(col(rows, k), col(rows, "claims")) for k in ("rec", "res", "lfl")]
L += ["", "**For each claim after the first failure** (the failed slots' gap over their claims; of record / with the reservation / like for like):\n", "| read | claims a failed slot | **lost for each claim** |", "|---|---|---|"]
for nm, key in (("12. conduct F at 0.3, world 3's cell", "r12"), ("13. conduct G at 0.3", "r13"), ("14. conduct F at 1.0", "r14"), ("10. conduct F at 0.3, world 4's cell", "r10")):
    rows = FR[key]
    if rows: pc = per_claim(rows); L.append(f"| {nm} | {np.mean([r['F']['claims'] for r in rows]):.1f} | **{pc[0][0]:.1f} ± {pc[0][1]:.1f} / {pc[1][0]:.1f} ± {pc[1][1]:.1f} / {pc[2][0]:.1f} ± {pc[2][1]:.1f}** |")
# read 14: from the first failure to the first suspension
def to_susp(E):
    tk, cl, ns, nf, cs = [], [], 0, 0, []
    for e in E:
        for v in groups(e)["claim"]:
            if not v.get("pfail_ticks"): continue
            nf += 1; f0_ = v["pfail_ticks"][0]; ss = [t for t in v["susp_ticks"] if t >= f0_]
            if ss: ns += 1; tk.append(ss[0] - f0_); cl.append(v.get("claims_pre_susp", np.nan))
            else: cs.append(v.get("claims_pre_susp", np.nan))
    return nf, ns, tk, cl, cs
L += ["", "**From the first failure to the first suspension** (the conduct's failed slots; the claims made in that interval are the slot's claims before its first suspension — for these conducts every claim comes after the failure):\n",
      "| read | failed slots | suspended after the failure (share) | ticks from the first failure to the first suspension: mean / median | claims in them a suspended slot: mean / median | claims a never-suspended failed slot |", "|---|---|---|---|---|---|"]
for nm, E in (("14. conduct F at 1.0, world 3's cell", R14), ("12. conduct F at 0.3, world 3's cell", R12), ("13. conduct G at 0.3", R13)):
    nf, ns, tk, cl, cs = to_susp(E)
    if nf: L.append(f"| {nm} | {nf} | {ns} ({ns / nf:.2f}) | {np.mean(tk) if tk else float('nan'):.0f} / {np.median(tk) if tk else float('nan'):.0f} | {np.nanmean(cl) if cl else float('nan'):.1f} / {np.nanmedian(cl) if cl else float('nan'):.0f} | {np.nanmean(cs) if cs else float('nan'):.1f} |")
# ---------------------------------------------------------------- paired contrasts
L += ["", "## Paired contrasts on the shared seeds (the gap careful − conduct in the second less in the first; positive = the second conduct or cell loses more)\n"] + HDR_P
paired_rows(L, "read 12 less read 10: world 4's cell less world 3's for conduct F at 0.3, the whole life (seeds 21–260)", Q["r12"], Q["r10"])
paired_rows(L, "… from the first failure on (the failed slots)", FR["r12"], FR["r10"])
paired_rows(L, "read 13 less read 12: conduct G less conduct F at 0.3, world 3's cell, the whole life", Q["r12"], Q["r13"])
paired_rows(L, "… from the first failure on", FR["r12"], FR["r13"])
paired_rows(L, "read 14 less read 12: conduct F at 1.0 less F at 0.3, world 3's cell, the whole life (21–140)", Q["r12"], Q["r14"])
paired_rows(L, "… from the first failure on", FR["r12"], FR["r14"])
paired_rows(L, "read 12 less read 9: conduct F at 0.3 less conduct M at 0.1, world 3's cell, the whole life (21–120)", Q["r9"], Q["r12"])
# ---------------------------------------------------------------- expectations and refutations
L += ["", "## Against the expectations stated before the run\n", "| statement | read | |", "|---|---|---|"]
def chk(name, cond, read): L.append(f"| {name} | {read} | {'met' if cond else 'MISSED'} |")
def g(key, k): rows = Q[key]; return mse(col(rows, k)) if rows else (np.nan, np.nan)
def gf(key, k): rows = FR[key]; return mse(col(rows, k)) if rows else (np.nan, np.nan)
if Q["r12"]:
    a, b, c = g("r12", "rec"), g("r12", "res"), g("r12", "lfl"); ts = [temp(Q["r12"], "rec", "ben"), temp(Q["r12"], "res", "ben"), temp(Q["r12"], "lfl", "den")]
    chk("read 12: F behind at the point value on each lifetime", a[0] > 0 and b[0] > 0 and c[0] > 0, f"{a[0]:+.0f} / {b[0]:+.0f} / {c[0]:+.0f}"); chk("read 12: by 10 to 90 of record", 10 <= a[0] <= 90, f"{a[0]:+.0f} ± {a[1]:.0f}")
    chk("read 12: by two standard errors or more like for like", c[0] >= 2 * c[1], f"{c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE)"); chk("read 12: level at 1.5 to 4 on each lifetime", all(1.5 <= t[0] <= 4 for t in ts), " / ".join(f"{t[0]:.1f} ± {t[1]:.1f}" for t in ts))
    fa = gf("r12", "rec"); chk("read 12: from the first failure on, the failed slots behind the careful's failed slots by 50 to 150 of record", 50 <= fa[0] <= 150, f"{fa[0]:+.0f} ± {fa[1]:.0f}")
    A_ = {r["seed"]: r for r in Q["r12"]}; B_ = {r["seed"]: r for r in Q["r10"]}; seeds = sorted(set(A_) & set(B_))
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        m = mse([B_[s][key] - A_[s][key] for s in seeds]); chk(f"read 12: world 4's cell less world 3's within two standard errors of nothing, {kn} (the whole life)", abs(m[0]) <= 2 * m[1], f"{m[0]:+.0f} ± {m[1]:.0f} ({m[0] / m[1]:.1f} SE)")
if Q["r13"] and FR["r13"]:
    cf = np.mean([r["F"]["claims"] for r in FR["r13"]]); a = gf("r13", "rec"); ta = temp(FR["r13"], "rec", "ben"); pc13, pc12 = per_claim(FR["r13"])[0], per_claim(FR["r12"])[0]
    chk("read 13: G makes fewer than 9 claims for a slot that had a failure", cf < 9, f"{cf:.1f}"); chk("read 13: from the first failure on, behind at the point value of record", a[0] > 0, f"{a[0]:+.0f} ± {a[1]:.0f}")
    chk("read 13: for each claim it loses less than conduct F of read 12 (from the first failure on, of record)", pc13[0] < pc12[0], f"{pc13[0]:.1f} ± {pc13[1]:.1f} against {pc12[0]:.1f} ± {pc12[1]:.1f}"); chk("read 13: level at 1.2 to 3.5 of record, from the first failure on", 1.2 <= ta[0] <= 3.5, f"{ta[0]:.1f} ± {ta[1]:.1f}")
if Q["r14"] and FR["r14"]:
    a = gf("r14", "rec"); ta = temp(FR["r14"], "rec", "ben"); pc14, pc12 = per_claim(FR["r14"])[0], per_claim(FR["r12"])[0]; s14 = np.mean([r["F"]["susp"] for r in FR["r14"]]); s12 = np.mean([r["F"]["susp"] for r in FR["r12"]])
    chk("read 14: from the first failure on, behind at the point value of record by 50 to 400", 50 <= a[0] <= 400, f"{a[0]:+.0f} ± {a[1]:.0f}"); chk("read 14: level at 1.2 to 3.5 of record, from the first failure on", 1.2 <= ta[0] <= 3.5, f"{ta[0]:.1f} ± {ta[1]:.1f}")
    chk("read 14: for each claim it loses less than F at 0.3 of read 12 (from the first failure on, of record)", pc14[0] < pc12[0], f"{pc14[0]:.1f} ± {pc14[1]:.1f} against {pc12[0]:.1f} ± {pc12[1]:.1f}"); chk("read 14: its suspensions for a slot that had a failure are above read 12's", s14 > s12, f"{s14:.2f} against {s12:.2f}")
L.append("")
if FR["r12"]:
    a = gf("r12", "rec"); L.append(f"**Refuted or shown, each apart.** *A marked record has something left to lose at the rulebook's weights* — refuted if in read 12, from the first failure on, conduct F is within two standard errors of nothing on the lifetime of record: {a[0]:+.0f} ± {a[1]:.0f} ({a[0] / a[1]:.1f} SE) — **{'REFUTED' if a[0] <= 2 * a[1] else 'not refuted'}**.")
if FR["r13"]:
    gs = [gf("r13", k) for k in ("rec", "res", "lfl")]; ts = [temp(FR["r13"], "rec", "ben"), temp(FR["r13"], "res", "ben"), temp(FR["r13"], "lfl", "den")]
    L.append(f"*Skipping pays while the earned seats are lost* — shown if in read 13, from the first failure on, conduct G is ahead by two standard errors on any lifetime, or level at a temptation under 1 on all three: {', '.join(f'{x[0]:+.0f} ± {x[1]:.0f} ({x[0] / x[1]:.1f} SE)' for x in gs)}; level at {', '.join(f'{t[0]:.1f} ± {t[1]:.1f}' for t in ts)} — **{'SHOWN' if (any(x[0] < -2 * x[1] for x in gs) or all(t[0] < 1 for t in ts)) else 'not shown'}**.")
if FR["r14"]:
    gs = [gf("r14", k) for k in ("rec", "res")]; ts = [temp(FR["r14"], "rec", "ben"), temp(FR["r14"], "res", "ben")]; c = gf("r14", "lfl"); tc = temp(FR["r14"], "lfl", "den")
    L.append(f"*Once marked, a member does best to skip everything* — shown if in read 14, from the first failure on, conduct F at 1.0 is ahead by two standard errors of record or with the reservation counted, or level at a temptation under 1 on both: {', '.join(f'{x[0]:+.0f} ± {x[1]:.0f} ({x[0] / x[1]:.1f} SE)' for x in gs)}; level at {', '.join(f'{t[0]:.1f} ± {t[1]:.1f}' for t in ts)} — **{'SHOWN' if (any(x[0] < -2 * x[1] for x in gs) or all(t[0] < 1 for t in ts)) else 'not shown'}** (like for like, reported and not the test: {c[0]:+.0f} ± {c[1]:.0f}, level at {tc[0]:.1f}).")
# reproduction of r14 at 575e405b1
R14A = load([f"{C}/r14/s21-80", f"{C}/r14/s81-140"], "mix:doseF1.0:0.25")[0]; R14B = load([f"{C}/r14b/s{a}-{b}" for a, b in ((21, 50), (51, 80), (81, 110), (111, 140))], "mix:doseF1.0:0.25")[0]
if R14A and R14B:
    a = {int(e["seed"]): (f(e, "half_d_lifetime_per_slot"), f(e, "half_claim_claims"), f(e, "false_approvals")) for e in R14A}; b = {int(e["seed"]): (f(e, "half_d_lifetime_per_slot"), f(e, "half_claim_claims"), f(e, "false_approvals")) for e in R14B}
    com = sorted(set(a) & set(b)); L.append(f"\nReproduction: read 14 run again at 575e405b1 for the pre-suspension claims on {len(com)} seeds {'**to the digit**' if com and all(all(abs(x - y) < 1e-9 for x, y in zip(a[s], b[s])) for s in com) else '**DIFFERS**'} (the gap, the claims, the false approvals); the figures above read r14b/ where it exists.")
open(sys.argv[1], "w").write("\n".join(L) + "\n")
