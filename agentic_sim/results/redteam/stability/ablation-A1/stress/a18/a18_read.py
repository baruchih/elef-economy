"""Addenda 18–19 (November 17, 2026; notes §117): from the record — Y3.2's two costs of a claim by the state of the earned seats (a fit over the seeds and over the
slots of reads 12, 13 and 14), W2's identity and the level savings from the tallies, W3's three counts (the worlds of reads 2, 4, 9 and 11 and the all-careful of
worlds 3 and 4 run again whole at f16e1ffee for the per-slot tallies, checked to the digit) — and the three reads without training in world 3's cell (a18/launch.sh:
r15 conduct M at 0.5, r16 conduct M at 1.0, r17 conduct G at 1.0), read as P4, Q4 and V4 were (a17_read.py's helpers copied), with the expectations stated before
the run and the refutations or showings. Usage: a18_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; A = f"{R}/a15"; B = f"{R}/a16"; C = f"{R}/a17"; D18 = f"{R}/a18"
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
# ---------------------------------------------------------------- the worlds of record, the reruns at bb0ada7af and the new reads
def ols(X, y):
    """Least squares with the coefficients' standard errors (homoskedastic) and R²."""
    X = np.asarray(X, float); y = np.asarray(y, float); ok = ~np.isnan(y) & ~np.isnan(X).any(axis=1); X, y = X[ok], y[ok]; n, k = X.shape
    if n <= k: return None
    beta, *_ = np.linalg.lstsq(X, y, rcond=None); res = y - X @ beta; s2 = (res @ res) / (n - k)
    se = np.sqrt(np.diag(s2 * np.linalg.inv(X.T @ X))); tss = ((y - y.mean()) ** 2).sum(); return beta, se, (1 - (res @ res) / tss if tss else np.nan), n
CW = {"w1": load([f"{A}/rerun/w1-s21-70", f"{A}/rerun/w1-s71-120"], "x")[1], "w6": load([f"{A}/rerun/w6-s21-70", f"{A}/rerun/w6-s71-120"], "x")[1], "w3": load([f"{A}/rerun/w3"], "x")[1], "w4": load([f"{A}/rerun/w4"], "x")[1]}
CW["w3"].update(load([f"{B}/r9/careful-w3-s81-120"], "careful")[1]); CW["w3"].update(load([f"{C}/r12/s121-170", f"{C}/r12/s171-215", f"{C}/r12/s216-260"], "careful")[1])
CW["w4"].update(load([f"{A}/p4/r2-s81-120"], "careful")[1]); CW["w4"].update(load([f"{B}/r10/careful-w4-s121-125", f"{B}/r10/s126-170", f"{B}/r10/s171-215", f"{B}/r10/s216-260"], "careful")[1])
REC = {"r1": load([f"{A}/p4/r1-s21-70", f"{A}/p4/r1-s71-120"], "mix:doseM0.1:0.25")[0], "r2": load([f"{A}/p4/r2-s21-80", f"{A}/p4/r2-s81-120"], "mix:doseM0.1:0.25")[0],
       "r3": load([f"{A}/p4/r3-s21-70", f"{A}/p4/r3-s71-120"], "mix:doseM0.1:0.25")[0], "r4": load([f"{A}/p4/r4"], "mix:doseM0.3:0.25")[0],
       "r9": load([f"{B}/r9/s21-70", f"{B}/r9/s71-120"], "mix:doseM0.1:0.25")[0], "r11": load([f"{B}/r11/s21-80"], "mix:doseM0.1:0.75")[0]}
RR = {"r2": load([f"{D18}/rerun/r2-s21-70", f"{D18}/rerun/r2-s71-120"], "mix:doseM0.1:0.25")[0], "r4": load([f"{D18}/rerun/r4-s21-80"], "mix:doseM0.3:0.25")[0],
      "r9": load([f"{D18}/rerun/r9-s21-70", f"{D18}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0], "r11": load([f"{D18}/rerun/r11-s21-80"], "mix:doseM0.1:0.75")[0]}
CWN = {"w3": load([f"{D18}/rerun/cw3-s21-70", f"{D18}/rerun/cw3-s71-120"], "careful")[1], "w4": load([f"{D18}/rerun/cw4-s21-70", f"{D18}/rerun/cw4-s71-120"], "careful")[1]}
R12 = load([f"{C}/r12/s21-70", f"{C}/r12/s71-120", f"{C}/r12/s121-170", f"{C}/r12/s171-215", f"{C}/r12/s216-260"], "mix:doseF0.3:0.25")[0]
R13 = load([f"{C}/r13/s21-70", f"{C}/r13/s71-120", f"{C}/r13/s121-170", f"{C}/r13/s171-215", f"{C}/r13/s216-260"], "mix:doseG0.3:0.25")[0]
R14 = load([f"{C}/r14b/s{a}-{b}" for a, b in ((21, 50), (51, 80), (81, 110), (111, 140))], "mix:doseF1.0:0.25")[0]
R15 = load([f"{D18}/r15/s21-70", f"{D18}/r15/s71-120"], "mix:doseM0.5:0.25")[0]; R16 = load([f"{D18}/r16/s21-70", f"{D18}/r16/s71-120"], "mix:doseM1.0:0.25")[0]
R17 = load([f"{D18}/r17/s21-80", f"{D18}/r17/s81-140"], "mix:doseG1.0:0.25")[0]
WORLD = {"r1": "w1", "r2": "w4", "r3": "w6", "r4": "w4", "r9": "w3", "r11": "w4", "r15": "w3", "r16": "w3", "r17": "w3"}
Q = {"r1": 0.1, "r2": 0.1, "r3": 0.1, "r4": 0.3, "r9": 0.1, "r11": 0.1, "r15": 0.5, "r16": 1.0}
RN = {"r1": "read 1: conduct M at 0.1, world 1's cell (the pin)", "r2": "read 2: conduct M at 0.1, world 4's cell", "r3": "read 3: conduct M at 0.1, world 6's cell (arm 4)", "r4": "read 4: conduct M at 0.3, world 4's cell",
      "r9": "read 9: conduct M at 0.1, world 3's cell", "r11": "read 11: conduct M at 0.1 on 3 slots in 4, world 4's cell", "r15": "read 15: conduct M at 0.5, world 3's cell", "r16": "read 16: conduct M at 1.0, world 3's cell", "r17": "read 17: conduct G at 1.0, world 3's cell"}
L = ["# Addenda 18–19: the record's three readings and the three reads without training (November 17, 2026; a18/launch.sh at f16e1ffee)\n"]
# ---------------------------------------------------------------- the reproduction check
def repro(new, old, careful_new=None, careful_old=None):
    """The rerun against the record on the shared seeds: every row column (the per-slot export apart) and every per-slot key the record carries."""
    O = {int(e["seed"]): e for e in old}; N_ = {int(e["seed"]): e for e in new}; seeds = sorted(set(O) & set(N_)); rows = slots = 0; bad_r = bad_s = 0
    for s in seeds:
        a, b = N_[s], O[s]
        bad_r += sum(1 for k in b if k != "learner_slots_json" and a.get(k) != b.get(k)); rows += 1
        SA, SB = json.loads(a["learner_slots_json"]), json.loads(b["learner_slots_json"])
        for x in SB:
            bad_s += sum(1 for k in SB[x] if SA.get(x, {}).get(k) != SB[x][k]); slots += 1
    return len(seeds), bad_r, bad_s, slots
L += ["## The reruns at f16e1ffee against the record (W3's counts and W2's tallies need per-slot readings the record does not carry; the worlds of reads 2, 4, 9 and 11 and the all-careful of worlds 3 and 4 run again whole — nothing collected anew)\n",
      "| world | seeds shared | row columns differing | per-slot keys of the record differing (slots compared) |", "|---|---|---|---|"]
for rid in ("r2", "r4", "r9", "r11"):
    if RR[rid]: n, br, bs, ns = repro(RR[rid], REC[rid]); L.append(f"| {RN[rid]} | {n} | {br} | {bs} ({ns}) |")
    else: L.append(f"| {RN[rid]} | (pending) | | |")
for wk in ("w3", "w4"):
    if CWN[wk]: n, br, bs, ns = repro(list(CWN[wk].values()), [c for s, c in CW[wk].items() if s <= 120]); L.append(f"| the all-careful of {WN[wk]} (21–120) | {n} | {br} | {bs} ({ns}) |")
    else: L.append(f"| the all-careful of {WN[wk]} | (pending) | | |")
# ---------------------------------------------------------------- Y3.2: two costs of a claim by the state of the earned seats
L += ["\n## Y3.2. A claim's cost by the state of the earned seats — the failed slots' gap from the first failure on against their claims with the seats held and with them lost (reads 12, 13 and 14)\n",
      "The gap is the careful failed slots' lifetime from the first failure on less the conduct's failed slots' (positive: the conduct behind), on the three lifetimes; the claims are the conduct's per failed slot after the first failure, split by the engine's `panel_eligible` at the claim (held / lost). Conduct F at 0.3 (240 seeds), conduct G at 0.3 (240; no claim with the seats held by construction) and conduct F at 1.0 (120) pooled. By the seeds: each seed's means, one row a seed and read, least squares of the gap on the two claim counts; by the slots: each failed conduct slot against the careful failed slots' mean of its seed. The fit with no intercept is the reviewer's form (a cost for each claim in each state); the fit with an intercept reads what a marked record loses with no claim at all. Standard errors homoskedastic.\n"]
FR = {"r12": failed_rows(R12, "F"), "r13": failed_rows(R13, "G"), "r14": failed_rows(R14, "F")}
def slot_rows(E):
    out = []
    for e in E:
        g = groups(e); Fs = [v for v in g["claim"] if v.get("pfail_ticks")]; Cs = [v for v in g["care"] if v.get("pfail_ticks")]
        if not Fs or not Cs or "pf_good_ticks_lost" not in Fs[0]: continue
        n = len(Cs); c_rec = sum(v["pf_income_lost"] + v["pf_income_after"] + v["pf_benefit_lost"] + v["pf_benefit_after"] for v in Cs) / n
        c_res = c_rec + RES * sum(after(v) for v in Cs) / n; c_gi = sum(v["pf_good_income_lost"] + v["pf_good_income_after"] for v in Cs) / n; c_gt = sum(v["pf_good_ticks_lost"] + v["pf_good_ticks_after"] for v in Cs) / n
        for v in Fs:
            rec = v["pf_income_lost"] + v["pf_income_after"] + v["pf_benefit_lost"] + v["pf_benefit_after"]; gt = v["pf_good_ticks_lost"] + v["pf_good_ticks_after"]
            rate = ((v["pf_good_income_lost"] + v["pf_good_income_after"] + v["pf_benefit_lost"] + v["pf_benefit_after"]) / gt) if gt else np.nan
            out.append(dict(seed=int(e["seed"]), rec=c_rec - rec, res=c_res - rec - RES * after(v), lfl=(c_gi - rate * c_gt) if gt else np.nan, held=v.get("claims_member_held", 0), lost=v.get("claims_member_lost", 0)))
    return out
SR = {k: slot_rows(E) for k, E in (("r12", R12), ("r13", R13), ("r14", R14))}
def fit_table(L, rows_by, label):
    for sel, nm in ((("r12", "r13", "r14"), "the three reads pooled"), (("r12", "r14"), "reads 12 and 14 (the reviewer's pair)"), (("r12", "r13"), "reads 12 and 13"), (("r13",), "read 13 alone (the lost state alone)")):
        rows = [r for k in sel for r in rows_by[k]]
        if not rows: continue
        held = np.array([r["held"] if isinstance(r["held"], (int, float)) else r["F"]["held"] for r in rows], float); lost = np.array([r["lost"] if isinstance(r["lost"], (int, float)) else r["F"]["lost"] for r in rows], float)
        for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
            y = np.array([r[key] for r in rows], float)
            if "r13" in sel and len(sel) == 1:
                f1 = ols(np.column_stack([lost]), y); f2 = ols(np.column_stack([np.ones_like(lost), lost]), y)
                if f1 and f2: L.append(f"| {label}, {nm} | {kn} | {f1[3]} | — | **{f1[0][0]:.1f} ± {f1[1][0]:.1f}** | {f2[0][0]:+.0f} ± {f2[1][0]:.0f} | — | {f2[0][1]:.1f} ± {f2[1][1]:.1f} | {f2[2]:.2f} |")
                continue
            f1 = ols(np.column_stack([held, lost]), y); f2 = ols(np.column_stack([np.ones_like(held), held, lost]), y)
            if f1 and f2: L.append(f"| {label}, {nm} | {kn} | {f1[3]} | **{f1[0][0]:.1f} ± {f1[1][0]:.1f}** | **{f1[0][1]:.1f} ± {f1[1][1]:.1f}** | {f2[0][0]:+.0f} ± {f2[1][0]:.0f} | {f2[0][1]:.1f} ± {f2[1][1]:.1f} | {f2[0][2]:.1f} ± {f2[1][2]:.1f} | {f2[2]:.2f} |")
L += ["| fit | lifetime | rows | **a claim with the seats held, no intercept** | **a claim with the seats lost, no intercept** | intercept | held, with the intercept | lost, with the intercept | R² (with the intercept) |", "|---|---|---|---|---|---|---|---|---|"]
fit_table(L, {k: [dict(seed=r["seed"], rec=r["rec"], res=r["res"], lfl=r["lfl"], held=r["F"]["held"], lost=r["F"]["lost"]) for r in v] for k, v in FR.items()}, "by the seeds")
fit_table(L, SR, "by the slots")
# the means' arithmetic (the reviewer's), with a bootstrap over the seeds; and why the within-read fits cannot part the states
mF = lambda rows, k: np.nanmean([r["F"][k] for r in rows])
def boot_costs(key, nb=2000, rng=np.random.default_rng(7)):
    """Resample the seeds of each read; from the resampled means solve (held, lost) from reads 12 and 14 alone, and lost from read 13 with held from read 12 and from read 14."""
    out = []
    S = {k: FR[k] for k in ("r12", "r13", "r14")}
    def means(rows):
        return (np.nanmean([r[key] for r in rows]), np.nanmean([r["F"]["held"] for r in rows]), np.nanmean([r["F"]["lost"] for r in rows]))
    pts = {k: means(v) for k, v in S.items()}
    def solve(p12, p13, p14):
        M = np.array([[p12[1], p12[2]], [p14[1], p14[2]]]); ab = np.linalg.solve(M, np.array([p12[0], p14[0]])); b13 = p13[0] / p13[2]
        return ab[0], ab[1], b13, (p12[0] - p12[2] * b13) / p12[1], (p14[0] - p14[2] * b13) / p14[1]
    point = solve(pts["r12"], pts["r13"], pts["r14"]); bs = []
    for _ in range(nb):
        rs = {k: means([v[i] for i in rng.integers(0, len(v), len(v))]) for k, v in S.items()}
        bs.append(solve(rs["r12"], rs["r13"], rs["r14"]))
    bs = np.array(bs); return point, bs.std(axis=0, ddof=1)
if FR["r12"] and FR["r13"] and FR["r14"]:
    L += ["\n**The two states cannot be parted by a fit over the slots or the seeds within the reads.** Within a read a failed slot's claim counts measure how long it lived after its failure as much as its conduct — a slot that made more claims stayed longer and earned more from the failure on — so with an intercept the slopes read negative (reads 12 and 14 by the slots: −14 a held claim, −5 a lost one, of record) and without one they read the blend of that selection and the reads' designs. What parts the states is the design: conduct G makes no claim with the seats held. So the costs are read from the reads' means, as the reviewer's (R) did, with their errors from a bootstrap over the seeds (2,000 draws):\n",
          "| lifetime | **a claim held, from reads 12 and 14** | **a claim lost, from reads 12 and 14** | a claim lost, read 13's own | a claim held, read 12 with read 13's lost | a claim held, read 14 with read 13's lost |", "|---|---|---|---|---|---|"]
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        pt, se = boot_costs(key)
        L.append(f"| {kn} | **{pt[0]:.1f} ± {se[0]:.1f}** | **{pt[1]:.1f} ± {se[1]:.1f}** | {pt[2]:.1f} ± {se[2]:.1f} | {pt[3]:.1f} ± {se[3]:.1f} | {pt[4]:.1f} ± {se[4]:.1f} |")
    L.append("\nThe means behind them: " + "; ".join(f"{kn} — read 12 {np.nanmean([r[key] for r in FR['r12']]):.0f} on {mF(FR['r12'], 'held'):.1f} held / {mF(FR['r12'], 'lost'):.1f} lost a failed slot, read 13 {np.nanmean([r[key] for r in FR['r13']]):.0f} on {mF(FR['r13'], 'lost'):.1f} lost, read 14 {np.nanmean([r[key] for r in FR['r14']]):.0f} on {mF(FR['r14'], 'held'):.1f} / {mF(FR['r14'], 'lost'):.1f}" for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like"))) + ".")
    for k, E in (("r12", R12), ("r13", R13), ("r14", R14)):
        cl, tk = [], []
        for e in E:
            for v in groups(e)["claim"]:
                if v.get("pfail_ticks") and "pf_ticks_lost" in v: cl.append(v.get("claims_member_held", 0) + v.get("claims_member_lost", 0)); tk.append(v["pf_ticks_lost"] + v["pf_ticks_after"])
        if len(cl) > 2: L.append(f"- {k.replace('r', 'read ')}: across its failed slots the claims after the failure and the ticks from the failure to the exit are correlated at {np.corrcoef(cl, tk)[0, 1]:+.2f} ({len(cl)} slots) — the survival the within-read fits read.")
# ---------------------------------------------------------------- W2: the identity and the level savings
SEATS = ("initial", "resumed", "audit", "third", "appeal", "dispute")
def counts(V):
    """W3's three counts for a group of slots (one episode): the mean a slot of its reviews by standing and, as a member, by seat with the planted cases among them by kind;
    the real-task reviews as a member before the first wrong planted verdict and before the first suspension, over every slot (censored at the exit) and over the slots that
    reach each, with the shares that reach; the wrong first approvals of real bad work and how many were paid, overturned or still open at the run's end; the care spent
    and the cost claimed as a member (real); read 16's hundredth."""
    n = len(V); g = lambda k: sum(v.get(k, 0) for v in V) / n
    d = {"n": n, "rv_member": g("rv_member"), "rv_probation": g("rv_probation"), "rv_down": g("rv_down"), "claims_m": g("claims_member")}
    for s_ in SEATS: d[s_] = g(f"rvm_{s_}"); d[f"pb_{s_}"] = g(f"rvm_plant_bad_{s_}"); d[f"pg_{s_}"] = g(f"rvm_plant_good_{s_}")
    d["plant_bad"] = sum(d[f"pb_{s_}"] for s_ in SEATS); d["plant_good"] = sum(d[f"pg_{s_}"] for s_ in SEATS); d["real"] = d["rv_member"] - d["plant_bad"] - d["plant_good"]
    d["pre_fail"] = g("rvm_real_pre_fail"); d["pre_susp"] = g("rvm_real_pre_susp"); d["m_pre_susp"] = g("rvm_pre_susp"); d["m_pre_fail"] = g("rvm_pre_fail")
    Vf = [v for v in V if v.get("pfail_ticks")]; Vs = [v for v in V if v["suspensions"] > 0]
    d["reach_fail"] = len(Vf) / n; d["reach_susp"] = len(Vs) / n
    d["pre_fail_r"] = np.mean([v.get("rvm_real_pre_fail", 0) for v in Vf]) if Vf else np.nan; d["pre_susp_r"] = np.mean([v.get("rvm_real_pre_susp", 0) for v in Vs]) if Vs else np.nan
    d["m_pre_susp_r"] = np.mean([v.get("rvm_pre_susp", 0) for v in Vs]) if Vs else np.nan
    d["fa"] = g("fa_init"); d["fa_paid"] = g("fa_init_paid"); d["fa_ov"] = g("fa_init_overturned"); d["fa_open"] = d["fa"] - d["fa_paid"] - d["fa_ov"]
    d["care_m"] = g("care_member"); d["claimed_m"] = g("claimed_member"); d["claimed_p"] = g("claimed_probation"); d["care_p"] = g("care_probation")
    H = [v for v in V if v.get("rv_member", 0) >= 100]; d["n100"] = len(H); d["hund"] = (sum(1 for v in H if v["suspensions"] > 0 and v.get("rvm_pre_susp", 0) < 100) / len(H)) if H else np.nan
    d["hund_any"] = (sum(1 for v in H if v["suspensions"] > 0) / len(H)) if H else np.nan
    return d
def count_rows(E, group):
    out = []
    for e in E:
        V = groups(e)[group]
        if V and "rv_member" in V[0] or any("rv_member" in v for v in V): out.append(dict(seed=int(e["seed"]), **counts(V)))
    return out
def count_rows_all(Cd):
    out = []
    for s_, c in sorted(Cd.items()):
        V = list(json.loads(c["learner_slots_json"]).values())
        if V and any("rv_member" in v for v in V): out.append(dict(seed=s_, **counts(V)))
    return out
def m(rows, k):
    x = np.array([r[k] for r in rows], float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def fmt(rows, k, d=1): a, b = m(rows, k); return f"{a:.{d}f} ± {b:.{d}f}"
def level_rows(E, C):
    """Per seed: the conduct's slots against the careful beside them (rows_of) with W2's level saving from the tallies — the share of the cost of care on all its reviews as a member
    the conduct's slot would have to be spared, in place of what its claims spared it, to end level — on the three lifetimes; and the realized claim share of its member reviews."""
    out = []
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"] or not any("rv_member" in v for v in g["claim"]): continue
        s_, c = counts(g["claim"]), counts(g["care"]); S_, Cc = stats_(g["claim"]), stats_(g["care"])
        call = s_["care_m"] + s_["claimed_m"]
        if not call or not S_["good"] or not Cc["good"]: continue
        spared = S_["ben"]   # a temptation of 1: the benefit is the cost the claims spared
        x_rec = (Cc["life"] - S_["life"] + spared) / call; x_res = (Cc["lres"] - S_["lres"] + spared) / call
        x_lfl = (Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"]) / call   # the careful's good-standing income scaled to the conduct's good ticks, less the conduct's own income in good standing, over its member care
        out.append(dict(seed=int(e["seed"]), x_rec=x_rec, x_res=x_res, x_lfl=x_lfl, good_c=Cc["good"], good_s=S_["good"], share=(s_["claims_m"] / s_["rv_member"] if s_["rv_member"] else np.nan), spared_share=spared / call,
                        loss_rec=Cc["life"] - S_["life"], loss_res=Cc["lres"] - S_["lres"], loss_lfl=Cc["ig"] - (S_["ig"] + S_["bg"]) / S_["good"] * Cc["good"], den_lfl=S_["bg"] / S_["good"] * Cc["good"], spared=spared, call=call, rvm=s_["rv_member"], cm=s_["claims_m"]))
    return out
def stats_(V):
    n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
    return dict(n=n, good=good, ig=ig, bg=bg, life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n, ben=sum(v["private_real"] for v in V) / n)
L += ["\n## W2. The level saving — the identity as the engine counts what a claim spares, and the level savings from the tallies\n",
      "**The identity holds as the engine counts.** A careful review's cost is drawn uniform on {2, 3} credits (times the calibration knob, 1 in every run of record) at every seat alike — `_care_cost` reads no seat — and the claim buys and is reimbursed exactly that draw, as the careful review would have been (an underfunded review pays what the wallet can buy, for both alike); the private benefit is the cost claimed times the temptation, real at the claim's tick; so at a temptation of 1 what a claim spares is the cost of care of that review and nothing else — not the fee, not the bond, not the verdict's consequence — and over a life the claims spare the conduct a share of the cost of care on all its reviews as a member equal to the share of those reviews it claimed, q in expectation (the coin is a review's own, independent of the cost's draw). The level saving is therefore x = q · T* up to the coin's noise, with T* the level temptation read as §112–§115 read it. What the identity does not carry: a claim on good work gives the right verdict where the careful's own review errs one time in twenty, so a conduct's claims improve its record a little relative to the careful's at that seat; that is in the loss, not in the saving. The tallies' figure below is the exact one: by seed, the careful slots' lifetime less the conduct's plus what the claims spared, over the care the conduct spent and claimed as a member (its member reviews' care, real); like for like the careful's income in good standing scaled to the conduct's good ticks less the conduct's own, over the same.\n",
      "| read | seeds | **level saving from the tallies, the mean of the seeds' ratios: of record** | **with the reservation** | **like for like** | the tallies as a ratio of the seeds' means: of record / with the reservation / like for like | the identity's q·T*: of record / with the reservation / like for like (the reviewer's) | claims as a member over member reviews (q) | the cost the claims spared over the member care (q) | member reviews a slot; claims as a member |", "|---|---|---|---|---|---|---|---|---|---|"]
REV_W2 = {"r9": (0.62, 0.52, 0.38), "r2": (0.76, 0.66, 0.52), "r1": (0.55, 0.51, 0.44), "r3": (0.03, 0.10, 0.20), "r11": (0.69, 0.68, 0.71), "r4": (2.67, 2.19, 1.65)}
LEVEL = {}; LEVEL_RM = {}
def identity(rows_rec, q):
    ta, tb, tc = temp(rows_rec, "rec", "ben"), temp(rows_rec, "res", "ben"), temp(rows_rec, "lfl", "den"); return q * ta[0], q * tb[0], q * tc[0], q * ta[1], q * tb[1], q * tc[1]
for rid in ("r9", "r2", "r1", "r3", "r11", "r4", "r15", "r16"):
    E_rec = {"r1": REC["r1"], "r2": REC["r2"], "r3": REC["r3"], "r4": REC["r4"], "r9": REC["r9"], "r11": REC["r11"], "r15": R15, "r16": R16}[rid]
    rows_rec = rows_of(E_rec, CW[WORLD[rid]]) if E_rec else []
    idn = identity(rows_rec, Q[rid]) if rows_rec else None
    E_t = {"r2": RR["r2"], "r4": RR["r4"], "r9": RR["r9"], "r11": RR["r11"], "r15": R15, "r16": R16}.get(rid, [])
    lv = level_rows(E_t, CW[WORLD[rid]]) if E_t else []; LEVEL[rid] = (lv, idn)
    rv = REV_W2.get(rid)
    idtxt = (f"{idn[0]:.2f} / {idn[1]:.2f} / {idn[2]:.2f}" + (f" ({rv[0]:.2f} / {rv[1]:.2f} / {rv[2]:.2f})" if rv else "")) if idn else "(pending)"
    if lv:
        rm_ = [ratio_se(col(lv, a_) + col(lv, "spared"), col(lv, "call")) for a_ in ("loss_rec", "loss_res")] + [ratio_se(col(lv, "loss_lfl") + col(lv, "den_lfl"), col(lv, "call") * np.array([r["good_c"] / r["good_s"] for r in lv]))]
        L.append(f"| {RN[rid]} | {len(lv)} | **{fmt(lv, 'x_rec', 2)}** | **{fmt(lv, 'x_res', 2)}** | **{fmt(lv, 'x_lfl', 2)}** | {rm_[0][0]:.2f} ± {rm_[0][1]:.2f} / {rm_[1][0]:.2f} ± {rm_[1][1]:.2f} / {rm_[2][0]:.2f} ± {rm_[2][1]:.2f} | {idtxt} | {fmt(lv, 'share', 3)} | {fmt(lv, 'spared_share', 3)} | {m(lv, 'rvm')[0]:.1f}; {m(lv, 'cm')[0]:.1f} |")
        LEVEL_RM[rid] = tuple(x[0] for x in rm_)
    else:
        L.append(f"| {RN[rid]} | {len(rows_rec)} | (the record carries no tallies) | | | | {idtxt} | | | |")
L.append("\nThe first three columns are what W2 asked — by seed, the share, as a mean with its error; the fourth is the same tallies as a ratio of the seeds' means, the form the level temptation has taken since §112, which the identity's q·T* must match (and does, to the coin: the claims' share of the member reviews reads q to three figures). The mean of the seeds' ratios runs a fifth to a third above it on every read because a seed's loss and its claims are negatively correlated — the conduct's slots that live longest claim most and lose least — so the seeds with few claims carry large ratios; it is the honest answer to the question as put, and the ratio of means the one to set against the identity.")
# ---------------------------------------------------------------- W3: the three counts
L += ["\n## W3. Three counts from the worlds on record (reads 2, 4, 9 and 11 run again whole at f16e1ffee; the conduct's slots, the careful slots beside them in the same world and seeds, and the all-careful population of the same world and seeds; the mean for a slot, ± the standard error over the seeds)\n",
      "### W3.1. The reviews made as a member in a life, by seat, and the planted cases among them by kind\n",
      "The engine's seat kinds: a first review of an unrevised submission (initial), the same reviewer resumed on a revision (resumed; none in these populations), the audit seat, the third seat (an audit-role challenge's), the appeal panel and the dispute panel. Reviews given on probation are beside; a review in neither standing (`down`: a seat completed by a slot whose standing had just changed) is counted apart.\n",
      "| read | group | **member reviews a slot** | initial | audit | third | appeal | dispute | resumed | planted among them: bad / good | … at the initial seat: bad / good | … at the audit seat: bad / good | … at the panels (third, appeal, dispute): bad / good | reviews on probation a slot | down |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
CNT = {}
def count_line(name, grp_name, rows):
    pb = lambda ks: sum(m(rows, f"pb_{k}")[0] for k in ks); pg = lambda ks: sum(m(rows, f"pg_{k}")[0] for k in ks)
    return (f"| {name} | {grp_name} | **{fmt(rows, 'rv_member')}** | {fmt(rows, 'initial')} | {fmt(rows, 'audit')} | {fmt(rows, 'third')} | {fmt(rows, 'appeal')} | {fmt(rows, 'dispute')} | {m(rows, 'resumed')[0]:.1f} | {fmt(rows, 'plant_bad')} / {fmt(rows, 'plant_good')} | "
            f"{pb(['initial']):.1f} / {pg(['initial']):.1f} | {pb(['audit']):.1f} / {pg(['audit']):.1f} | {pb(['third', 'appeal', 'dispute']):.1f} / {pg(['third', 'appeal', 'dispute']):.1f} | {fmt(rows, 'rv_probation')} | {m(rows, 'rv_down')[0]:.1f} |")
for rid in ("r9", "r2", "r4", "r11"):
    if not RR[rid]: L.append(f"| {RN[rid]} | (pending) | | | | | | | | | | | | | |"); continue
    CNT[rid] = {"claim": count_rows(RR[rid], "claim"), "care": count_rows(RR[rid], "care"), "all": count_rows_all({s_: c for s_, c in CWN[WORLD[rid]].items() if s_ in {int(e["seed"]) for e in RR[rid]}})}
    for gk, gn in (("claim", "the conduct's slots"), ("care", "the careful slots beside"), ("all", "the all-careful population")):
        if CNT[rid][gk]: L.append(count_line(RN[rid] if gk == "claim" else "", gn, CNT[rid][gk]))
L += ["\n### W3.2. From admission: the reviews of real tasks made as a member before the earned seats are first lost (the first wrong planted verdict on the record, by the driver's clock — the plant's closure) and before the first suspension; the shares of the slots that reach each\n",
      "Over every slot the count is censored at the exit (a slot that never fails counts all its real member reviews); over the slots that reach the event it is the count before it. A failure on probation (an arrival's, before admission) puts the record's mark on before any member review, so such a slot reaches the first with 0.\n",
      "| read | group | **real reviews as a member before the seats are first lost: every slot / the slots that reach it** | share that reach a failure | **real reviews as a member before the first suspension: every slot / the slots that reach it** | share that reach a suspension | member reviews of every kind before the first suspension, the slots that reach it |", "|---|---|---|---|---|---|---|"]
for rid in ("r9", "r2", "r4", "r11"):
    if rid not in CNT: L.append(f"| {RN[rid]} | (pending) | | | | | |"); continue
    for gk, gn in (("claim", "the conduct's slots"), ("care", "the careful slots beside"), ("all", "the all-careful population")):
        rows = CNT[rid][gk]
        if rows: L.append(f"| {RN[rid] if gk == 'claim' else ''} | {gn} | **{fmt(rows, 'pre_fail')} / {fmt(rows, 'pre_fail_r')}** | {fmt(rows, 'reach_fail', 2)} | **{fmt(rows, 'pre_susp')} / {fmt(rows, 'pre_susp_r')}** | {fmt(rows, 'reach_susp', 2)} | {fmt(rows, 'm_pre_susp_r')} |")
L += ["\n### W3.3. The wrong approvals of real bad work given in a life as a first reviewer, and how many were paid\n",
      "A first review's F on real work whose truth is unfulfilled; paid where the review vested and its fee reached the slot, overturned where its bond was forfeited (an audit's or a panel's overturn), open where the case had not settled by the run's end.\n",
      "| read | group | **wrong first approvals of real bad work a slot** | **paid** | overturned | open at the end | paid share of the settled | ratio to the careful slots beside (the conduct's) |", "|---|---|---|---|---|---|---|---|"]
for rid in ("r9", "r2", "r4", "r11"):
    if rid not in CNT: L.append(f"| {RN[rid]} | (pending) | | | | | | |"); continue
    for gk, gn in (("claim", "the conduct's slots"), ("care", "the careful slots beside"), ("all", "the all-careful population")):
        rows = CNT[rid][gk]
        if not rows: continue
        settled = m(rows, "fa_paid")[0] + m(rows, "fa_ov")[0]; ratio = ratio_se(col(rows, "fa"), col(CNT[rid]["care"], "fa")) if gk == "claim" and CNT[rid]["care"] else None
        L.append(f"| {RN[rid] if gk == 'claim' else ''} | {gn} | **{fmt(rows, 'fa', 2)}** | **{fmt(rows, 'fa_paid', 2)}** | {fmt(rows, 'fa_ov', 2)} | {fmt(rows, 'fa_open', 2)} | {(m(rows, 'fa_paid')[0] / settled if settled else np.nan):.2f} | {(f'{ratio[0]:.2f} ± {ratio[1]:.2f}' if ratio else '')} |")
# ---------------------------------------------------------------- W4: reads 15 and 16 (and read 9 beside) — the three lifetimes, both groups, the counts, the level saving
L += ["\n## W4. Reads 15 and 16 — conduct M at 0.5 and at 1.0 in world 3's cell on seeds 21–120 (read 9, conduct M at 0.1, beside): the three lifetimes with their level temptations (read as P4 and Q4 were)\n",
      "The conduct on 1 slot in 4; the gap is the careful slots beside less the conduct's (positive: the conduct behind), of record (the wallet's real wealth at the exit plus the benefit), with the reservation (0.8 real a tick from a departure to the run's end), like for like (the careful's good-standing income less the conduct's good-standing rate times the careful's good ticks); the level temptation 1 + gap / what the claims spared. Beside: the all-careful population of the same seeds.\n"] + HDR_L
ROWS = {"r9": rows_of(REC["r9"], CW["w3"]), "r15": rows_of(R15, CW["w3"]) if R15 else [], "r16": rows_of(R16, CW["w3"]) if R16 else []}
for rid in ("r9", "r15", "r16"): L.append(lifetimes_row(RN[rid], ROWS[rid]))
L += ["\n### Both groups a slot, the lifetime lost for each claim, and the honest side\n"] + HDR_G
for rid in ("r9", "r15", "r16"): L.append(groups_row(RN[rid], ROWS[rid]))
L += ["\n### W3's three counts for reads 15 and 16 (read 9's rerun beside)\n", "| read | group | **member reviews a slot** | initial | audit | third | appeal | dispute | resumed | planted among them: bad / good | … at the initial seat: bad / good | … at the audit seat: bad / good | … at the panels (third, appeal, dispute): bad / good | reviews on probation a slot | down |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for rid, E in (("r9", RR["r9"]), ("r15", R15), ("r16", R16)):
    if not E: L.append(f"| {RN[rid]} | (pending) | | | | | | | | | | | | | |"); continue
    CNT[rid] = {"claim": count_rows(E, "claim"), "care": count_rows(E, "care"), "all": count_rows_all({s_: c for s_, c in CWN["w3"].items() if s_ in {int(e["seed"]) for e in E}})}
    for gk, gn in (("claim", "the conduct's slots"), ("care", "the careful slots beside"), ("all", "the all-careful population")):
        if CNT[rid][gk]: L.append(count_line(RN[rid] if gk == "claim" else "", gn, CNT[rid][gk]))
L += ["\n| read | group | **real reviews as a member before the seats are first lost: every slot / the slots that reach it** | share that reach a failure | **real reviews as a member before the first suspension: every slot / the slots that reach it** | share that reach a suspension | member reviews of every kind before the first suspension, the slots that reach it | **wrong first approvals of real bad work a slot: given / paid / overturned** | ratio to the careful beside |", "|---|---|---|---|---|---|---|---|---|"]
for rid in ("r9", "r15", "r16"):
    if rid not in CNT: L.append(f"| {RN[rid]} | (pending) | | | | | | | |"); continue
    for gk, gn in (("claim", "the conduct's slots"), ("care", "the careful slots beside"), ("all", "the all-careful population")):
        rows = CNT[rid][gk]
        if not rows: continue
        ratio = ratio_se(col(rows, "fa"), col(CNT[rid]["care"], "fa")) if gk == "claim" and CNT[rid]["care"] else None
        L.append(f"| {RN[rid] if gk == 'claim' else ''} | {gn} | **{fmt(rows, 'pre_fail')} / {fmt(rows, 'pre_fail_r')}** | {fmt(rows, 'reach_fail', 2)} | **{fmt(rows, 'pre_susp')} / {fmt(rows, 'pre_susp_r')}** | {fmt(rows, 'reach_susp', 2)} | {fmt(rows, 'm_pre_susp_r')} | **{fmt(rows, 'fa', 2)} / {fmt(rows, 'fa_paid', 2)} / {fmt(rows, 'fa_ov', 2)}** | {(f'{ratio[0]:.2f} ± {ratio[1]:.2f}' if ratio else '')} |")
# read 16's hundredth
if "r16" in CNT and CNT["r16"]["claim"]:
    rows = CNT["r16"]["claim"]; H_all = []; S_all = []
    for e in R16:
        for v in groups(e)["claim"]:
            if v.get("rv_member", 0) >= 100: H_all.append((v["suspensions"] > 0 and v.get("rvm_pre_susp", 0) < 100, v["suspensions"] > 0, v.get("rvm_pre_susp", 0)))
            if v["suspensions"] > 0: S_all.append(v.get("rvm_pre_susp", 0))
    n100 = len(H_all); before = sum(1 for h in H_all if h[0]); ever = sum(1 for h in H_all if h[1])
    allv = [v for e in R16 for v in groups(e)["claim"]]; rvm = np.array([v.get("rv_member", 0) for v in allv]); rva = np.array([v.get("rv_member", 0) + v.get("rv_probation", 0) + v.get("rv_down", 0) for v in allv])
    nosusp = [v for v in allv if v["suspensions"] == 0]; ns_alive = sum(1 for v in nosusp if v["alive"]); ns_dep = len(nosusp) - ns_alive
    ns_m = np.array([v.get("rv_member", 0) for v in nosusp]); ns_fail = sum(1 for v in nosusp if v.get("pfail_ticks"))
    L += [f"\n**Read 16's hundredth.** Of the conduct's slots that make a hundred reviews as a member or more — **{n100} slots over the hundred seeds** ({m(rows, 'n100')[0]:.2f} a seed of {m(rows, 'n')[0]:.1f} conduct slots) — {before} were suspended before their hundredth member review, {ever} at some point. The set is empty because a claim at every member review stops a slot well short of a hundred: over the {len(allv)} conduct slots the member reviews in a life are {rvm.mean():.1f} a slot, the most {rvm.max()}, {100 * np.mean(rvm >= 50):.0f} in 100 reach fifty; counting the reviews on probation too {rva.mean():.1f} a slot, the most {rva.max()}, {100 * np.mean(rva >= 100):.0f} in 100 reach a hundred. Over the conduct's slots that reach a suspension ({len(S_all)} slots, {100 * len(S_all) / len(allv):.0f} in 100) the first comes after {np.mean(S_all):.1f} ± {np.std(S_all, ddof=1) / np.sqrt(len(S_all)):.1f} reviews as a member (median {np.median(S_all):.0f}; the real-task reviews among them in the table above). The {len(nosusp)} slots never suspended made {ns_m.mean():.1f} member reviews (the most {ns_m.max() if len(ns_m) else 0}): {ns_alive} alive at the run's end and {ns_dep} departed under the exit rule, {ns_fail} of them with a wrong planted verdict on the record (the seats lost, no suspension yet)."]
    # the same for read 15 and read 9, for the comparison
    for rid, E in (("r15", R15), ("r9", RR["r9"])):
        H_all = [(v["suspensions"] > 0 and v.get("rvm_pre_susp", 0) < 100, v["suspensions"] > 0) for e in E for v in groups(e)["claim"] if v.get("rv_member", 0) >= 100]; S_all = [v.get("rvm_pre_susp", 0) for e in E for v in groups(e)["claim"] if v["suspensions"] > 0]
        if H_all: L.append(f"- {RN[rid]}: {len(H_all)} conduct slots with a hundred member reviews or more, {sum(1 for h in H_all if h[0])} suspended before the hundredth ({100 * sum(1 for h in H_all if h[0]) / len(H_all):.0f} in 100), {sum(1 for h in H_all if h[1])} ever; the first suspension after {np.mean(S_all):.1f} member reviews over the {len(S_all)} slots that reach one.")
# ---------------------------------------------------------------- read 17: conduct G at 1.0 against read 14's conduct F at 1.0 and read 13's conduct G at 0.3
L += ["\n## Read 17. Conduct G at 1.0 in world 3's cell on seeds 21–140 — careful until its first wrong planted verdict, then a claim at every decision where its earned seats are lost, careful where they are held, on probation and after a suspension (read as read 13 was; reads 13 and 14 beside)\n",
      "### From the first failure on — among the slots that ever had a wrong planted verdict, the conduct's failed slots less the careful failed slots of the same world and seeds\n"] + HDR_F
FR["r17"] = failed_rows(R17, "G") if R17 else []
for rid, nm in (("r13", "read 13: conduct G at 0.3 (240 seeds)"), ("r14", "read 14: conduct F at 1.0 (120 seeds)"), ("r17", "**read 17: conduct G at 1.0 (120 seeds)**")): failed_table(L, nm, FR[rid])
L += ["\n### Over the life — the conduct's slots less the careful beside (every slot, failed or not)\n"] + HDR_L
ROWS["r13"] = rows_of(R13, CW["w3"]); ROWS["r14"] = rows_of(R14, CW["w3"]); ROWS["r17"] = rows_of(R17, CW["w3"]) if R17 else []
for rid, nm in (("r13", "read 13: conduct G at 0.3"), ("r14", "read 14: conduct F at 1.0"), ("r17", "**read 17: conduct G at 1.0**")): L.append(lifetimes_row(nm, ROWS[rid]))
L += ["\n### Paired on the shared seeds (second − first; a positive figure: the second further behind)\n"] + HDR_P
paired_rows(L, "read 17 (G at 1.0) against read 14 (F at 1.0), over the life", ROWS["r14"], ROWS["r17"])
paired_rows(L, "read 17 (G at 1.0) against read 14 (F at 1.0), from the first failure on", FR["r14"], FR["r17"])
paired_rows(L, "read 17 (G at 1.0) against read 13 (G at 0.3), from the first failure on", FR["r13"], FR["r17"])
if FR["r17"]:
    rows = FR["r17"]; pc = [ratio_se(col(rows, k), col(rows, "claims")) for k in ("rec", "res", "lfl")]; tt = [temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")]
    gF = lambda k: np.mean([r["F"][k] for r in rows]); gC = lambda k: np.mean([r["C"][k] for r in rows])
    sus = [r["F"]["susp"] for r in rows]
    L.append(f"\n**Read 17's figures for the expectations.** Claims a failed slot {gF('claims'):.1f} (held {gF('held'):.1f} / lost {gF('lost'):.1f}; read 13's 5.9); from the first failure on behind by {mse(col(rows, 'rec'))[0]:+.0f} ± {mse(col(rows, 'rec'))[1]:.0f} of record, {mse(col(rows, 'res'))[0]:+.0f} ± {mse(col(rows, 'res'))[1]:.0f} with the reservation, {mse(col(rows, 'lfl'))[0]:+.0f} ± {mse(col(rows, 'lfl'))[1]:.0f} like for like; for each claim {pc[0][0]:.1f} ± {pc[0][1]:.1f} / {pc[1][0]:.1f} ± {pc[1][1]:.1f} / {pc[2][0]:.1f} ± {pc[2][1]:.1f} real; level at {tt[0][0]:.1f} ± {tt[0][1]:.1f} / {tt[1][0]:.1f} ± {tt[1][1]:.1f} / {tt[2][0]:.1f} ± {tt[2][1]:.1f}; suspensions a failed slot {gF('susp'):.2f} (the careful failed slots' {gC('susp'):.2f}; read 13's 0.26, read 14's 0.51); further failures {gF('more'):.2f} against {gC('more'):.2f}; ticks without the seats {gF('tlost'):.0f} against {gC('tlost'):.0f}; departed {gF('dep'):.2f} against {gC('dep'):.2f}.")
# the level saving of reads 12–14 and 17 by the identity (Y3.3)
L += ["\n### Y3.3. The level saving on a marked record by the identity (q · the level temptation; the reviewer's figures in parentheses)\n", "| read | over the life: of record / with the reservation / like for like | from the first failure on: of record / with the reservation / like for like |", "|---|---|---|"]
for rid, q, nm, rv in (("r12", 0.3, "read 12: conduct F at 0.3", ("1.11 / 0.96 / 0.90", "1.05 / 0.84 / 0.81")), ("r13", 0.3, "read 13: conduct G at 0.3", (None, "0.57 / 0.36 / 0.51")), ("r14", 1.0, "read 14: conduct F at 1.0", (None, "2.9 / 2.1 / 1.5")), ("r17", 1.0, "read 17: conduct G at 1.0", (None, None))):
    rl = {"r12": rows_of(R12, CW["w3"]), "r13": ROWS["r13"], "r14": ROWS["r14"], "r17": ROWS["r17"]}[rid]; fr = FR[rid]
    a = identity(rl, q) if rl else None; b = identity(fr, q) if fr else None
    L.append(f"| {nm} | {(f'{a[0]:.2f} / {a[1]:.2f} / {a[2]:.2f}' if a else '(pending)')}{(f' ({rv[0]})' if rv[0] else '')} | {(f'{b[0]:.2f} / {b[1]:.2f} / {b[2]:.2f}' if b else '(pending)')}{(f' ({rv[1]})' if rv[1] else '')} |")
L.append("\nFor conduct G the identity's q is the dose while the seats are lost, not the share of all member reviews claimed — G claims none with the seats held — so its 'level saving' is the share of the care on its reviews with the seats lost, as the reviewer's 0.57 / 0.36 / 0.51 read it.")
# ---------------------------------------------------------------- the expectations and the refutations or showings
L += ["\n## Against the expectations stated before the run, and the refutations or showings\n"]
def chk(ok, text): L.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def ok_(x): return x is not None and not (isinstance(x, float) and np.isnan(x))
if "r9" in LEVEL and LEVEL["r9"][0]:
    lv, idn = LEVEL["r9"]; xr = m(lv, "x_rec")[0]
    rmv = LEVEL_RM["r9"]; chk(True, f"W2: the identity holds as the engine counts (one care draw at every seat, the claim sparing that draw and nothing else); the tallies' level savings of read 9 as a ratio of the seeds' means are {rmv[0]:.2f} / {rmv[1]:.2f} / {rmv[2]:.2f} against the identity's {idn[0]:.2f} / {idn[1]:.2f} / {idn[2]:.2f} ({'within' if max(abs(rmv[i] - idn[i]) for i in range(3)) < 0.1 else 'not within'} the 0.1 asked); the mean of the seeds' ratios {xr:.2f} / {m(lv, 'x_res')[0]:.2f} / {m(lv, 'x_lfl')[0]:.2f} is above both, for the reason given in W2.")
if "r9" in CNT and CNT["r9"]["claim"]:
    c9 = CNT["r9"]; rvm = m(c9["claim"], "rv_member")[0]; rs = m(c9["claim"], "reach_susp")[0]; rf = ratio_se(col(c9["claim"], "fa"), col(c9["care"], "fa"))[0]
    chk(60 <= rvm <= 90, f"W3: a conduct slot of read 9 makes {rvm:.1f} reviews as a member in a life (60 to 90 expected).")
    chk(0.10 <= rs <= 0.40, f"W3: {100 * rs:.0f} in 100 of read 9's conduct slots are suspended at least once (10 to 40 expected).")
    chk(1.5 <= rf <= 4, f"W3: a conduct slot of read 9 gives {rf:.2f} times a careful slot's wrong approvals of real bad work (1.5 to 4 expected).")
for rid, lo, hi, xs_lo, s_lo, s_hi in (("r15", 250, 700, 1.0, 0.30, 0.80), ("r16", 400, 900, 1.5, None, None)):
    if ROWS[rid] and LEVEL[rid][0]:
        rows = ROWS[rid]; lv = LEVEL[rid][0]; a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl"))
        chk(a[0] > 2 * a[1] and b[0] > 2 * b[1] and c[0] > 2 * c[1] and lo <= a[0] <= hi, f"{RN[rid]}: behind on every lifetime, {a[0]:+.0f} ± {a[1]:.0f} / {b[0]:+.0f} ± {b[1]:.0f} / {c[0]:+.0f} ± {c[1]:.0f} ({lo} to {hi} of record expected).")
        xs = (m(lv, "x_rec")[0], m(lv, "x_res")[0], m(lv, "x_lfl")[0]); chk(min(xs) > xs_lo, f"{RN[rid]}: the level saving from the tallies {xs[0]:.2f} / {xs[1]:.2f} / {xs[2]:.2f} (above {xs_lo} on every lifetime expected); by the identity {LEVEL[rid][1][0]:.2f} / {LEVEL[rid][1][1]:.2f} / {LEVEL[rid][1][2]:.2f}.")
        if s_lo is not None and rid in CNT: rs = m(CNT[rid]["claim"], "reach_susp")[0]; chk(s_lo <= rs <= s_hi, f"{RN[rid]}: {100 * rs:.0f} in 100 of the conduct's slots suspended at least once ({100 * s_lo:.0f} to {100 * s_hi:.0f} expected).")
if "r16" in CNT and CNT["r16"]["claim"]:
    S_all = [v.get("rvm_pre_susp", 0) for e in R16 for v in groups(e)["claim"] if v["suspensions"] > 0]; H_all = [(v["suspensions"] > 0 and v.get("rvm_pre_susp", 0) < 100) for e in R16 for v in groups(e)["claim"] if v.get("rv_member", 0) >= 100]
    chk(30 <= np.mean(S_all) <= 90, f"read 16: over the slots that reach a suspension the first comes after {np.mean(S_all):.1f} reviews as a member (30 to 90 expected).")
    if H_all: chk(np.mean(H_all) >= 0.9, f"read 16: of the slots that make a hundred reviews as a member, {100 * np.mean(H_all):.0f} in 100 were suspended before their hundredth (at least 9 in 10 expected).")
    else: L.append("- EMPTY — read 16: no conduct slot makes a hundred reviews as a member (the expectation's set is empty; every slot is stopped, departs or reaches the run's end before its hundredth).")
if FR["r17"]:
    rows = FR["r17"]; a = mse(col(rows, "rec")); pc = ratio_se(col(rows, "rec"), col(rows, "claims")); tt = temp(rows, "rec", "ben"); gF = lambda k: np.mean([r["F"][k] for r in rows])
    chk(15 <= gF("claims") <= 30, f"read 17: {gF('claims'):.1f} claims a failed slot (15 to 30 expected).")
    chk(20 <= a[0] <= 120, f"read 17: from the first failure on behind at the point value by {a[0]:+.0f} ± {a[1]:.0f} of record (20 to 120 expected).")
    chk(1 <= pc[0] <= 5, f"read 17: for each claim {pc[0]:.1f} ± {pc[1]:.1f} real of record lost (1 to 5 expected).")
    chk(1.3 <= tt[0] <= 2.7, f"read 17: level at a temptation of {tt[0]:.1f} ± {tt[1]:.1f} of record from the first failure on (1.3 to 2.7 expected).")
    chk(0.26 < gF("susp") <= 0.51, f"read 17: suspensions a failed slot {gF('susp'):.2f} (above read 13's 0.26 and no higher than read 14's 0.51 expected).")
    A_ = {r["seed"]: r for r in FR["r14"]}; B_ = {r["seed"]: r for r in rows}; sh = sorted(set(A_) & set(B_)); d = np.array([B_[s]["rec"] - A_[s]["rec"] for s in sh]); dm = mse(d)
    chk(dm[0] < 0, f"read 17: from the first failure on G at 1.0 loses less than F at 1.0 by seed — G less F {dm[0]:+.0f} ± {dm[1]:.0f} of record on {len(sh)} seeds (less expected).")
    b = mse(col(rows, "res")); L.append(f"- (the sign with the reservation, which the reviewer did not know: {b[0]:+.0f} ± {b[1]:.0f})")
L += ["\n### Refuted, or shown, each apart\n"]
if "r9" in LEVEL and LEVEL["r9"][0]:
    lv, idn = LEVEL["r9"]; L.append(f"- \"A cheaper model pays in the design as ruled when it misses one bad delivery in ten\": shown if the level saving of read 9 is under 0.9 at the point value on the lifetime of record — by the identity {idn[0]:.2f}, by the tallies {m(lv, 'x_rec')[0]:.2f} ± {m(lv, 'x_rec')[1]:.2f}: **{'SHOWN' if (idn[0] < 0.9 and m(lv, 'x_rec')[0] < 0.9) else 'NOT SHOWN'}**.")
if all(LEVEL.get(k, ([], None))[0] for k in ("r15", "r16")):
    xs = {k: (m(LEVEL[k][0], "x_rec")[0], m(LEVEL[k][0], "x_res")[0], m(LEVEL[k][0], "x_lfl")[0]) for k in ("r15", "r16")}
    L.append(f"- \"It does not pay when it misses half or more\": refuted if the level saving of read 15 or of read 16 is under 0.9 on any lifetime — read 15 {xs['r15'][0]:.2f} / {xs['r15'][1]:.2f} / {xs['r15'][2]:.2f}, read 16 {xs['r16'][0]:.2f} / {xs['r16'][1]:.2f} / {xs['r16'][2]:.2f} from the tallies (the identity {LEVEL['r15'][1][0]:.2f} / {LEVEL['r15'][1][1]:.2f} / {LEVEL['r15'][1][2]:.2f} and {LEVEL['r16'][1][0]:.2f} / {LEVEL['r16'][1][1]:.2f} / {LEVEL['r16'][1][2]:.2f}): **{'REFUTED' if min(xs['r15'] + xs['r16']) < 0.9 else 'NOT REFUTED'}**.")
if "r16" in CNT and CNT["r16"]["claim"]:
    H_all = [(v["suspensions"] > 0 and v.get("rvm_pre_susp", 0) < 100) for e in R16 for v in groups(e)["claim"] if v.get("rv_member", 0) >= 100]
    if H_all: L.append(f"- \"A member that misses everything is stopped within a hundred reviews\": refuted if in read 16, among the conduct's slots that make a hundred reviews as a member or more, fewer than 9 in 10 were suspended before their hundredth — {100 * np.mean(H_all):.0f} in 100 of {len(H_all)}: **{'REFUTED' if np.mean(H_all) < 0.9 else 'NOT REFUTED'}**.")
    else: L.append("- \"A member that misses everything is stopped within a hundred reviews\": refuted if in read 16, among the conduct's slots that make a hundred reviews as a member or more, fewer than 9 in 10 were suspended before their hundredth — no conduct slot makes a hundred reviews as a member, so the condition's set is empty: **NOT REFUTED** (and, read on the slots as they are, every one is stopped before a hundred: the member reviews in a life and the suspensions' timing above).")
if FR["r17"]:
    rows = FR["r17"]; a, b = mse(col(rows, "rec")), mse(col(rows, "res")); ta, tb = temp(rows, "rec", "ben"), temp(rows, "res", "ben")
    L.append(f"- \"A skip costs something while the earned seats are lost\": refuted if in read 17, from the first failure on, conduct G at 1.0 is within two standard errors of nothing on the lifetime of record — {a[0]:+.0f} ± {a[1]:.0f} ({a[0] / a[1]:.1f} SE): **{'REFUTED' if abs(a[0]) < 2 * a[1] else 'NOT REFUTED'}**.")
    L.append(f"- \"Skipping everything while the earned seats are lost pays\": shown if in read 17, from the first failure on, conduct G at 1.0 is ahead by two standard errors of record or with the reservation counted, or level at a temptation under 1 on both — of record {a[0]:+.0f} ± {a[1]:.0f} (level at {ta[0]:.1f}), with the reservation {b[0]:+.0f} ± {b[1]:.0f} (level at {tb[0]:.1f}): **{'SHOWN' if (a[0] < -2 * a[1] or b[0] < -2 * b[1] or (ta[0] < 1 and tb[0] < 1)) else 'NOT SHOWN'}**.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("written", sys.argv[1], len(L), "lines")
