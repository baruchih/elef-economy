"""Addendum 22 (November 17, 2026; notes §119): from the record — AB5.1 (three figures that differ between the notes: the like-for-like base), AB5.2 (the way back from a
member's suspension, from read 15's world run again whole at eca3d5ee3), AB4.5 and AB4.7 (the planted cases in read 16's 27.5 reviews; the split of read 9's loss from the flows
by seat) — and the six reads without training (a20/launch.sh at eca3d5ee3: r20–r22 in the cell of the second failure, θ_duty 0.34; r23–r24 in the cell of the first failure,
θ_duty 0.20; r25 conduct M at 0.1 with its claims set by the case on every slot in world 3's cell), read as reads 9, 17, 18 and 19 were (a18_read.py's and a19_read.py's helpers
copied), with the reviewer's expectations stated before the run and the refutations or showings. Usage: a20_read.py OUT.md [A20_DIR A19_DIR A18_DIR]"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
D20 = sys.argv[2] if len(sys.argv) > 2 else f"{R}/a20"; D19 = sys.argv[3] if len(sys.argv) > 3 else f"{R}/a19"; D18 = sys.argv[4] if len(sys.argv) > 4 else f"{R}/a18"
T = 1000; RES = 0.8; T_SUSP = 100; G_V = 5.0
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else ((x.mean() if len(x) else np.nan), np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num)
    if n < 2 or den.mean() == 0: return ((num.mean() / den.mean()) if n and den.mean() else np.nan, np.nan)
    a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1); r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def pm(t, d=1): return f"{t[0]:.{d}f} ± {t[1]:.{d}f}" if not np.isnan(t[1]) else f"{t[0]:.{d}f}"
def groups(e):
    S = json.loads(e["learner_slots_json"]); share = float(e.get("half_share") or 0.5); seed = int(e["seed"]); grp = {"claim": [], "care": []}
    for x, v in S.items():
        h = int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big"); grp["claim" if h < share * 65536 else "care"].append(v)
    return grp
def slots(e): return list(json.loads(e["learner_slots_json"]).values())
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
def stats_(V):
    n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
    return dict(n=n, good=good, ig=ig, bg=bg, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n, ben=sum(v["private_real"] for v in V) / n,
                claims=sum(v["claims"] for v in V) / n, cm=sum(v.get("claims_member", 0) for v in V) / n, cp=sum(v.get("claims_probation", 0) for v in V) / n, susp=sum(v["suspensions"] for v in V) / n, aud=sum(v["audits_done"] for v in V) / n)
def rows_of(E, C, filt=lambda v: True):
    out = []
    for e in E:
        g = {k: [v for v in V if filt(v)] for k, V in groups(e).items()}
        if not g["claim"] or not g["care"] or int(e["seed"]) not in C: continue
        c0 = C[int(e["seed"])]; Sc = [v for v in slots(c0) if filt(v)]
        r = {"seed": int(e["seed"]), "all_care": (sum(life(v) for v in Sc) / len(Sc)) if Sc else np.nan}
        for kk, V in g.items(): r[kk] = stats_(V)
        cc, s = r["care"], r["claim"]
        r.update(rec=cc["life"] - s["life"], res=cc["lres"] - s["lres"], lfl=cc["ig"] - s["rate"] * cc["good"], den=s["brate"] * cc["good"], ben=s["ben"], claims=s["claims"], care_minus_all=cc["life"] - r["all_care"],
                 fa=f(e, "false_approvals"), leak=1000 * f(e, "leak_bad"), oh=f(e, "sys_overhead_per_vested"), fa0=f(c0, "false_approvals"), leak0=1000 * f(c0, "leak_bad"), oh0=f(c0, "sys_overhead_per_vested"))
        out.append(r)
    return out
def col(rows, k): return np.array([r[k] for r in rows], float)
def grp(rows, kk, k): return np.mean([r[kk][k] for r in rows])
def temp(rows, key, den): t = ratio_se(col(rows, key), col(rows, den)); return 1 + t[0], t[1]
def lifetimes_row(name, rows, extra=""):
    a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl")); ta, tb, tc = temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")
    return f"| {name} | {len(rows)} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {ta[0]:.1f} ± {ta[1]:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f}) | {tb[0]:.1f} ± {tb[1]:.1f} | **{c[0]:+.0f} ± {c[1]:.0f}** ({c[0] / c[1]:.1f}) | {tc[0]:.1f} ± {tc[1]:.1f} |{extra}"
def groups_row(name, rows):
    l1, l2, l3 = ratio_se(col(rows, "rec"), col(rows, "claims")), ratio_se(col(rows, "res"), col(rows, "claims")), ratio_se(col(rows, "lfl"), col(rows, "claims"))
    return (f"| {name} | {grp(rows, 'claim', 'claims'):.1f} ({grp(rows, 'claim', 'cm'):.1f} / {grp(rows, 'claim', 'cp'):.1f}); {grp(rows, 'claim', 'ben'):.1f}; {grp(rows, 'claim', 'susp'):.2f}; {grp(rows, 'claim', 'aud'):.1f}; {grp(rows, 'claim', 'good'):.0f} | "
            f"{grp(rows, 'care', 'susp'):.2f}; {grp(rows, 'care', 'aud'):.1f}; {grp(rows, 'care', 'good'):.0f} | **{l1[0]:.1f} ± {l1[1]:.1f} / {l2[0]:.1f} ± {l2[1]:.1f} / {l3[0]:.1f} ± {l3[1]:.1f}** | "
            f"{mse(col(rows, 'care_minus_all'))[0]:+.0f} ± {mse(col(rows, 'care_minus_all'))[1]:.0f}; {np.mean(col(rows, 'fa')):.1f}; {np.mean(col(rows, 'leak')):.0f}; {np.mean(col(rows, 'oh')):.1f} ({np.mean(col(rows, 'fa0')):.1f}; {np.mean(col(rows, 'leak0')):.0f}; {np.mean(col(rows, 'oh0')):.1f}) |")
HDR_L = ["| world / read | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |", "|---|---|---|---|---|---|---|---|"]
HDR_G = ["| world / read | conduct's slots: claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** | careful group − all-careful of the cell; FA; leak ‰; overhead (all-careful of the cell) |", "|---|---|---|---|---|"]
HDR_P = ["| contrast | seeds | lifetime | first | second | **second − first, paired** | SE from nothing |", "|---|---|---|---|---|---|---|"]
def paired_rows(L, nm, ra, rb):
    A_ = {r["seed"]: r for r in ra}; B_ = {r["seed"]: r for r in rb}; seeds = sorted(set(A_) & set(B_)); out = {}
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        if seeds:
            x = np.array([A_[s][key] for s in seeds]); y = np.array([B_[s][key] for s in seeds]); ok = ~(np.isnan(x) | np.isnan(y)); m_ = mse(y[ok] - x[ok]); out[key] = m_
            L.append(f"| {nm} | {int(ok.sum())} | {kn} | {x[ok].mean():+.0f} | {y[ok].mean():+.0f} | **{m_[0]:+.0f} ± {m_[1]:.0f}** | {m_[0] / m_[1]:.1f} |")
    return out
SEATS = ("initial", "resumed", "audit", "third", "appeal", "dispute"); SEAT_N = {"initial": "the first review", "resumed": "the resumed seat", "audit": "the audit seat", "third": "the third seat", "appeal": "an appeal panel", "dispute": "a dispute panel"}
CLS = ("fee", "emission", "uplift", "reimb", "bond", "courtfee")
def counts(V):
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
    d["susp"] = g("suspensions"); d["aud"] = g("audits_done"); d["pfails"] = sum(len(v.get("pfail_ticks", [])) for v in V) / n; d["good"] = g("ticks_good")
    d["pw_member"] = sum(sum(n_ for k, n_ in v.items() if k.startswith("pw_member_")) for v in V) / n; d["pw_probation"] = sum(sum(n_ for k, n_ in v.items() if k.startswith("pw_probation_")) for v in V) / n
    d["reach_fail_m"] = sum(1 for v in V if any(k.startswith("pw_member_") for k in v)) / n
    return d
def count_rows(E, group):
    out = []
    for e in E:
        V = groups(e)[group]
        if V and any("rv_member" in v for v in V): out.append(dict(seed=int(e["seed"]), **counts(V)))
    return out
def count_rows_all(Cd):
    out = []
    for s_, c in sorted(Cd.items()):
        V = slots(c)
        if V and any("rv_member" in v for v in V): out.append(dict(seed=s_, **counts(V)))
    return out
def m(rows, k): return mse([r[k] for r in rows])
def fmt(rows, k, d=1): a, b = m(rows, k); return f"{a:.{d}f} ± {b:.{d}f}"
def level_rows(E):
    out = []
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"] or not any("rv_member" in v for v in g["claim"]): continue
        s_, c = counts(g["claim"]), counts(g["care"]); S_, Cc = stats_(g["claim"]), stats_(g["care"])
        call = s_["care_m"] + s_["claimed_m"]
        if not call or not S_["good"] or not Cc["good"]: continue
        spared = S_["ben"]
        out.append(dict(seed=int(e["seed"]), x_rec=(Cc["life"] - S_["life"] + spared) / call, x_res=(Cc["lres"] - S_["lres"] + spared) / call, x_lfl=(Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"]) / call,
                        loss_rec=Cc["life"] - S_["life"], loss_res=Cc["lres"] - S_["lres"], loss_lfl=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - spared, spared=spared, call=call, rvm=s_["rv_member"], cm=s_["claims_m"], share=(s_["claims_m"] / s_["rv_member"] if s_["rv_member"] else np.nan),
                        good_c=Cc["good"], good_s=S_["good"], loss_lfl_k3=Cc["ig"] - S_["rate"] * Cc["good"], den_k3=S_["brate"] * Cc["good"]))
    return out
def level_line(rows):
    rm = tuple(ratio_se(col(rows, f"loss_{k}") + col(rows, "spared"), col(rows, "call")) for k in ("rec", "res", "lfl")); mr = tuple(mse(col(rows, f"x_{k}")) for k in ("rec", "res", "lfl"))
    return rm, mr
def repro(new_eps, old_eps, label):
    old = {int(e["seed"]): e for e in old_eps}; n_rows = n_keys = n_slots = n_seeds = 0; diffs = []
    for e in new_eps:
        s_ = int(e["seed"])
        if s_ not in old: continue
        o = old[s_]; n_seeds += 1
        for k in o:
            if k == "learner_slots_json": continue
            n_rows += 1
            if o[k] != e.get(k): diffs.append((s_, k))
        So, Sn = json.loads(o["learner_slots_json"]), json.loads(e["learner_slots_json"])
        for x, v in So.items():
            n_slots += 1
            for k, val in v.items():
                n_keys += 1
                if Sn.get(x, {}).get(k) != val: diffs.append((s_, x, k))
    return f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") + ".", len(diffs), n_seeds
def failed_rows(E):
    """a18's: per seed, the conduct's failed slots less the careful failed slots of the same world and seed, from the first failure on."""
    out = []
    for e in E:
        g = groups(e); Fs = [v for v in g["claim"] if v.get("pfail_ticks")]; Cs = [v for v in g["care"] if v.get("pfail_ticks")]
        if not Fs or not Cs or "pf_good_ticks_lost" not in Fs[0]: continue
        a, c = agg_fail(Fs), agg_fail(Cs)
        out.append(dict(seed=int(e["seed"]), F=a, C=c, rec=c["rec"] - a["rec"], res=c["res"] - a["res"], lfl=c["gi"] - a["rate"] * c["gt"], den=a["brate"] * c["gt"], ben=a["ben"], claims=a["claims"]))
    return out
def agg_fail(V):
    n = len(V); inc = sum(v["pf_income_lost"] + v["pf_income_after"] for v in V) / n; ben = sum(v["pf_benefit_lost"] + v["pf_benefit_after"] for v in V) / n
    gt = sum(v["pf_good_ticks_lost"] + v["pf_good_ticks_after"] for v in V) / n; gi = sum(v["pf_good_income_lost"] + v["pf_good_income_after"] for v in V) / n; gb = sum(v["pf_benefit_lost"] + v["pf_benefit_after"] for v in V) / n
    return dict(n=n, rec=inc + ben, res=inc + ben + RES * sum(after(v) for v in V) / n, gt=gt, gi=gi, rate=((gi + gb) / gt if gt else np.nan), brate=(gb / gt if gt else np.nan),
                claims=sum(v.get("claims_after_fail", 0) for v in V) / n, held=sum(v.get("claims_member_held", 0) for v in V) / n, lost=sum(v.get("claims_member_lost", 0) for v in V) / n,
                more=sum(len(v["pfail_ticks"]) - 1 for v in V) / n, tlost=sum(v["pf_ticks_lost"] for v in V) / n, susp=sum(v["suspensions"] for v in V) / n, dep=sum(1 for v in V if not v["alive"]) / n,
                ticks=sum(v["pf_ticks_lost"] + v["pf_ticks_after"] for v in V) / n, back=sum(1 for v in V if v.get("pf_back_t") is not None) / n, ben=ben,
                susp_after=sum(sum(1 for t in v.get("susp_ticks", []) if t >= v["pfail_ticks"][0]) for v in V) / n)
def failed_table(L, name, rows):
    if not rows: L.append(f"| {name} | (pending) | | | | | | | | | |"); return
    a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl")); ta, tb, tc = temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")
    gF = lambda k: np.mean([r["F"][k] for r in rows]); gC = lambda k: np.mean([r["C"][k] for r in rows])
    L.append(f"| {name} | {len(rows)} | {gF('n'):.1f} / {gC('n'):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({ta[0]:.1f}) | **{b[0]:+.0f} ± {b[1]:.0f}** ({tb[0]:.1f}) | **{c[0]:+.0f} ± {c[1]:.0f}** ({tc[0]:.1f}) | {gF('claims'):.1f} ({gF('held'):.1f} / {gF('lost'):.1f}) | {gF('more'):.2f} / {gC('more'):.2f} | {gF('tlost'):.0f} / {gC('tlost'):.0f} ({gF('back'):.2f} / {gC('back'):.2f}) | {gF('susp_after'):.2f} / {gC('susp_after'):.2f}; {gF('dep'):.2f} / {gC('dep'):.2f} | {gF('ticks'):.0f} / {gC('ticks'):.0f} |")
HDR_F = ["| read | seeds | failed slots a seed: conduct / careful | **from the first failure: of record** (level at) | **with the reservation** (level at) | **like for like** (level at) | the conduct's claims after the first failure a slot (seats held / lost at the claim) | further wrong planted verdicts a slot: conduct / careful | ticks without the earned seats: conduct / careful (share whose seats returned) | suspensions from the failure on a failed slot: conduct / careful; departed share: conduct / careful | ticks from the first failure to the exit: conduct / careful |", "|---|---|---|---|---|---|---|---|---|---|---|"]
def to_susp(E):
    tk, cl, ns, nf, cs = [], [], 0, 0, []
    for e in E:
        for v in groups(e)["claim"]:
            if not v.get("pfail_ticks"): continue
            nf += 1; f0_ = v["pfail_ticks"][0]; ss = [t for t in v["susp_ticks"] if t >= f0_]
            if ss: ns += 1; tk.append(ss[0] - f0_); cl.append(v.get("claims_pre_susp", np.nan))
            else: cs.append(v.get("claims_pre_susp", np.nan))
    return nf, ns, tk, cl, cs
# ---- spells: an arrival's probation, and the way back from a suspension (with the suspension's tick attached)
def spells(Cd, kind):
    rows = []
    for c in Cd.values():
        for v in slots(c):
            st = sorted(v.get("susp_ticks", []))
            for sp in v.get("spells", []):
                if sp["kind"] != kind: continue
                r = dict(sp, slot_alive=v["alive"], t_in=v["t_in"])
                if kind == "return":
                    pre = [t for t in st if t <= sp["t0"]]; r["susp_t"] = max(pre) if pre else sp["t0"] - T_SUSP; r["whole"] = sp["t1"] - r["susp_t"]
                rows.append(r)
    return rows
def spell_table(label, S, kind):
    n = len(S)
    if not n: return [f"| {label} | 0 | | | | | |"]
    ends = {k: sum(1 for s in S if s["end"] == k) for k in ("member", "suspended", "departed", "open")}
    adm = [s for s in S if s["end"] == "member"]; sus = [s for s in S if s["end"] == "suspended"]
    whole = (f"**{pm(mse([s['whole'] for s in adm]), 0)}** (median {np.median([s['whole'] for s in adm]) if adm else np.nan:.0f})" if kind == "return" else "")
    return [f"| {label} | {n} | {ends['member'] / n:.2f} / {ends['suspended'] / n:.2f} / {ends['departed'] / n:.2f} / {ends['open'] / n:.2f} | **{pm(mse([s['ticks'] for s in adm]), 0)} ticks, {pm(mse([s['reviews'] for s in adm]))} reviews** (medians {np.median([s['ticks'] for s in adm]) if adm else np.nan:.0f}, {np.median([s['reviews'] for s in adm]) if adm else np.nan:.0f}) | {whole} | {pm(mse([s['ticks'] for s in sus]), 0)} ticks, {pm(mse([s['reviews'] for s in sus]))} reviews | {pm(mse([s['ticks'] for s in S]), 0)} ticks, {pm(mse([s['reviews'] for s in S]))} reviews |"]
HDR_S = ["| spells | n | ended: member / suspended / departed / open | **to membership (from the probation's start): ticks, reviews** | the whole way from the suspension to the readmission: ticks | to a suspension: ticks, reviews | every spell: ticks, reviews |", "|---|---|---|---|---|---|---|"]
def susp_split(Cd, filt=lambda v: True):
    """Per seed: the slots suspended at least once in 100 — any; as a member (a suspension that no probation spell ends); on probation — and the suspensions a slot; the arrivals admitted in the run; the good ticks."""
    rows = []
    for s_, c in sorted(Cd.items()):
        V = [v for v in slots(c) if filt(v)]
        if not V: continue
        n = len(V); anyS = memS = proS = 0; nsusp = 0; mism = 0
        for v in V:
            pro_t = {sp["t1"] - 1 for sp in v.get("spells", []) if sp["end"] == "suspended"}; st = v.get("susp_ticks", [])   # a spell closes at the standing step of the tick after the suspension is logged
            nsusp += len(st); mism += len(pro_t - set(st))
            if st: anyS += 1
            if any(t not in pro_t for t in st): memS += 1
            if any(t in pro_t for t in st): proS += 1
        arr = [v for v in V if v["t_in"] > 0]; adm = [v for v in arr if "adm_ticks" in v]
        rows.append(dict(seed=s_, n=n, any=anyS / n, mem=memS / n, pro=proS / n, susp=nsusp / n, mism=mism, adm=(len(adm) / len(arr) if arr else np.nan), good=np.mean([v["ticks_good"] for v in V]),
                         life=np.mean([life(v) for v in V]), lres=np.mean([life(v) + RES * after(v) for v in V]), ig=np.mean([v["income_good"] for v in V]),
                         fa=f(c, "false_approvals"), leak=1000 * f(c, "leak_bad"), oh=f(c, "sys_overhead_per_vested"), cot=f(c, "cost_of_truth"), dep=f(c, "departures"), arrivals=f(c, "arrivals"), Pt=f(c, "P_t")))
    return rows
def failed_members(Cd, filt=lambda v: True):
    """Per seed: the careful slots that took a wrong planted verdict as a member, from their first failure on (a18's aggregate)."""
    rows = []
    for s_, c in sorted(Cd.items()):
        V = [v for v in slots(c) if filt(v) and v.get("pfail_ticks") and any(k.startswith("pw_member_") for k in v) and "pf_good_ticks_lost" in v]
        if not V: continue
        rows.append(dict(seed=s_, **agg_fail(V)))
    return rows
def paired_cells(L, nm, ra, rb, keys, d=0):
    """second − first by seed on each key (name, label, digits)."""
    A_ = {r["seed"]: r for r in ra}; B_ = {r["seed"]: r for r in rb}; seeds = sorted(set(A_) & set(B_)); out = {}
    for key, kn, dd in keys:
        x = np.array([A_[s][key] for s in seeds], float); y = np.array([B_[s][key] for s in seeds], float); ok = ~(np.isnan(x) | np.isnan(y)); m_ = mse(y[ok] - x[ok]); out[key] = m_
        L.append(f"| {nm} | {kn} | {int(ok.sum())} | {x[ok].mean():.{dd}f} | {y[ok].mean():.{dd}f} | **{m_[0]:+.{dd}f} ± {m_[1]:.{dd}f}** | {(m_[0] / m_[1]) if m_[1] else np.nan:.1f} |")
    return out
HDR_C = ["| contrast | measure | seeds | world 3's cell | the cell | **cell − world 3, paired** | SE from nothing |", "|---|---|---|---|---|---|---|"]
def pop_rows(E, C):
    out = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in C: continue
        V = slots(e); Vc = slots(C[s_]); S_, Cc = stats_(V), stats_(Vc); d, dc = counts(V), counts(Vc); call = d["care_m"] + d["claimed_m"]
        out.append(dict(seed=s_, n=len(V), nc=len(Vc), rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], ben=S_["ben"], den=S_["brate"] * Cc["good"], claims=S_["claims"], call=call, spared=S_["ben"],
                        x_rec=(Cc["life"] - S_["life"] + S_["ben"]) / call if call else np.nan, x_res=(Cc["lres"] - S_["lres"] + S_["ben"]) / call if call else np.nan, x_lfl=(Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"]) / call if call else np.nan,
                        loss_rec=Cc["life"] - S_["life"], loss_res=Cc["lres"] - S_["lres"], loss_lfl=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"],
                        life=S_["life"], lifec=Cc["life"], lres=S_["lres"], lresc=Cc["lres"], ig=S_["ig"], igc=Cc["ig"], good=S_["good"], goodc=Cc["good"], susp=S_["susp"], suspc=Cc["susp"], aud=S_["aud"], audc=Cc["aud"], reach=d["reach_susp"], reachc=dc["reach_susp"], rvm=d["rv_member"], rvmc=dc["rv_member"],
                        fa=f(e, "false_approvals"), fa0=f(C[s_], "false_approvals"), leak=1000 * f(e, "leak_bad"), leak0=1000 * f(C[s_], "leak_bad"), oh=f(e, "sys_overhead_per_vested"), oh0=f(C[s_], "sys_overhead_per_vested"),
                        dep=f(e, "departures"), dep0=f(C[s_], "departures"), arr=f(e, "arrivals"), arr0=f(C[s_], "arrivals"), cot=f(e, "cost_of_truth"), cot0=f(C[s_], "cost_of_truth"), Pt=f(e, "P_t"), Pt0=f(C[s_], "P_t"), fai=d["fa"], fai0=dc["fa"], fpaid=d["fa_paid"], fpaid0=dc["fa_paid"]))
    return out
# ------------------------------------------------------------------ the record
CW3 = load([f"{D19}/rerun/cw3-s21-70", f"{D19}/rerun/cw3-s71-120"], "careful")[1]
R9 = load([f"{D19}/rerun/r9-s21-70", f"{D19}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0]
R15_OLD = load([f"{D18}/r15/s21-70", f"{D18}/r15/s71-120"], "mix:doseM0.5:0.25")[0]
R15 = load([f"{D20}/rerun/r15-s21-70", f"{D20}/rerun/r15-s71-120"], "mix:doseM0.5:0.25")[0]
R17 = load([f"{D18}/r17/s21-80", f"{D18}/r17/s81-140"], "mix:doseG1.0:0.25")[0]
R18 = load([f"{D19}/r18/s{a}-{b}" for a, b in ((21, 45), (46, 70), (71, 95), (96, 120))], "mix:doseM0.1:1.0")[0]
R19 = load([f"{D19}/r19/s{a}-{b}" for a, b in ((21, 45), (46, 70), (71, 95), (96, 120))], "mix:doseM0.2:0.25")[0]
C20 = load([f"{D20}/r20/s21-60", f"{D20}/r20/s61-100", f"{D20}/r20/s101-140"], "careful")[1]
R21 = load([f"{D20}/r21/s21-60", f"{D20}/r21/s61-100", f"{D20}/r21/s101-140"], "mix:doseG1.0:0.25")[0]
R22 = load([f"{D20}/r22/s21-70", f"{D20}/r22/s71-120"], "mix:doseM0.1:0.25")[0]
C23 = load([f"{D20}/r23/s21-70", f"{D20}/r23/s71-120"], "careful")[1]
R24 = load([f"{D20}/r24/s21-70", f"{D20}/r24/s71-120"], "mix:doseM0.1:0.25")[0]
R25 = load([f"{D20}/r25/s21-70", f"{D20}/r25/s71-120"], "mix:caseM0.1:1.0")[0]
D = lambda E: {int(e["seed"]): e for e in E}
L = ["# Addendum 22: the record's readings and the six reads without training (November 17, 2026; a20/launch.sh at eca3d5ee3)\n",
     f"Loaded: cw3 {len(CW3)}, r9 {len(R9)}, r15 (a18) {len(R15_OLD)}, r15 (rerun) {len(R15)}, r17 {len(R17)}, r18 {len(R18)}, r19 {len(R19)}; r20 {len(C20)}, r21 {len(R21)}, r22 {len(R22)}, r23 {len(C23)}, r24 {len(R24)}, r25 {len(R25)} episodes.\n"]
CHK = []
def chk(ok, text): CHK.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def in_band(x, lo, hi): return (not np.isnan(x)) and lo <= x <= hi
# ------------------------------------------------------------------ 0. the rerun against the record
L += ["\n## 0. The rerun against the record\n", "Read 15's world (conduct M at 0.5 on 1 slot in 4, world 3's cell, seeds 21–120) run again whole at eca3d5ee3 — the harness of 906fc5ac4 plus the `--theta-duty` passthrough at its default — for the probation spells, which a18/r15 (f16e1ffee) did not export; checked against a18/r15 on every row column and every per-slot key the record carries, before it is read:\n"]
rp = repro(R15, R15_OLD, "read 15 (conduct M at 0.5 on 1 slot in 4)"); L.append(rp[0]); REPRO_OK = (rp[1] == 0 and rp[2] == 100)
# ------------------------------------------------------------------ AB5.1
L += ["\n## AB5.1. Three figures that differ between the notes — the like-for-like base\n"]
def lfl_both(E, C):
    rows = rows_of(E, C); lv = level_rows(E)
    g_k3 = mse(col(rows, "lfl")); g_ct = mse(col(lv, "loss_lfl"))   # K3's base (the careful's good ticks) / the conduct's good ticks
    rm_ct = ratio_se(col(lv, "loss_lfl") + col(lv, "spared"), col(lv, "call"))
    rm_k3 = ratio_se(col(lv, "loss_lfl_k3") + col(lv, "den_k3"), col(lv, "call") * col(lv, "good_c") / col(lv, "good_s"))
    rm_k3b = ratio_se(col(lv, "loss_lfl_k3") + col(lv, "den_k3"), col(lv, "call"))
    return g_k3, g_ct, rm_k3, rm_ct, rm_k3b, mse(col(lv, "x_lfl"))
for nm, E, C in (("read 9", R9, CW3), ("read 15", R15_OLD, CW3)):
    if not E: continue
    g_k3, g_ct, rm_k3, rm_ct, rm_k3b, mr = lfl_both(E, C)
    L.append(f"- **{nm}**: the gap like for like on K3's base (the careful's income in good standing less the conduct's rate over the careful's good ticks, the ruling of November 16) {pm(g_k3, 0)}; the same difference on the conduct's good ticks (the careful's rate over the conduct's good ticks, less the conduct's income) {pm(g_ct, 0)}. The level saving like for like as a ratio of the seeds' means: with each seed's numerator and denominator on the careful's good ticks (§117's form) {pm(rm_k3, 2)}; on the conduct's own good ticks (§118's form) {pm(rm_ct, 2)}; the mean of the seeds' ratios {pm(mr, 2)} (the same per seed either way).")
L.append("\nWhat moved is the base of the like-for-like comparison, not the data. Per seed the two forms are the same ratio (the K3 gap plus the benefit's denominator, scaled by the conduct's good ticks over the careful's, is the careful's rate on the conduct's good ticks less the conduct's income); as a ratio of the seeds' means they weight the seeds differently — §117 by the care scaled to the careful's ticks, §118 by the care as measured — and the figures differ by a hundredth or two, a third of the error. **The figures of record from here**: for the gap like for like, K3's base as ruled (read 9's 63 ± 14); for the level saving like for like, §118's form (0.40 ± 0.07 for read 9, 1.79 ± 0.07 for read 15), the numerator and the denominator both on the conduct's own good ticks, which is the quantity the identity x = q · T* was confirmed on. §118's Z3.3 column headed 'the gap like for like' (65 ± 14) is the gap on the conduct's good ticks — the numerator of the level saving — and is relabelled so by erratum; the gain like for like there, 108 ± 15, is 0.9 of the care less what the claims spared less that gap, and with K3's gap in its place it reads " + (f"{pm(mse(0.9 * col(level_rows(R9), 'call') - col(level_rows(R9), 'spared') - col(rows_of(R9, CW3), 'lfl')), 0)} (the same quantity on the careful's good ticks; both stand, each on its base)." if R9 else "(pending)."))
# ------------------------------------------------------------------ AB5.2 the way back
L += ["\n## AB5.2. The way back from a member's suspension, as built\n",
      "A spell on the way back begins when the hundred ticks off duty end (the probation's start) and ends in a readmission (`since_susp ≥ 4` outcomes of either kind with the record passing θ_duty), in another suspension (a wrong planted verdict on probation), at the slot's departure, or open at the run's end. The whole way is counted from the tick of the suspension that began it (the slot's suspension log) to the readmission. Read 15's world holds the most; the others beside.\n"] + HDR_S
SPELL_SETS = [("read 15's world (M at 0.5 on 1 in 4; the rerun)", D(R15) if R15 else {}), ("world 3's all-careful (cw3)", CW3), ("read 9's world (M at 0.1 on 1 in 4)", D(R9)), ("read 18's world (M at 0.1 on every slot)", D(R18)), ("read 19's world (M at 0.2 on 1 in 4)", D(R19)),
              ("read 20's world (all-careful, θ_duty 0.34)", C20), ("read 21's world (G at 1.0, θ_duty 0.34)", D(R21)), ("read 22's world (M at 0.1, θ_duty 0.34)", D(R22)), ("read 23's world (all-careful, θ_duty 0.20)", C23), ("read 24's world (M at 0.1, θ_duty 0.20)", D(R24)), ("read 25's world (case-keyed M at 0.1 on every slot)", D(R25))]
RET = {}
for nm, Cd in SPELL_SETS:
    if not Cd: continue
    SR = spells(Cd, "return"); RET[nm] = SR; L += spell_table(nm, SR, "return")
if R15:
    SRc = [s for s in spells(D(R15), "return")]
    Sg = {"claim": [], "care": []}
    for e in R15:
        for kk, V in groups(e).items():
            for v in V:
                st = sorted(v.get("susp_ticks", []))
                for sp in v.get("spells", []):
                    if sp["kind"] == "return": pre = [t for t in st if t <= sp["t0"]]; Sg[kk].append(dict(sp, whole=sp["t1"] - (max(pre) if pre else sp["t0"] - T_SUSP)))
    L += ["\nRead 15's world by group:\n"] + HDR_S + spell_table("the conduct's slots (M at 0.5)", Sg["claim"], "return") + spell_table("the careful slots beside", Sg["care"], "return")
L += ["\nAn arrival's probation in the same worlds, for the comparison Z3.6 made:\n"] + HDR_S
for nm, Cd in SPELL_SETS:
    if not Cd: continue
    L += spell_table(nm, spells(Cd, "arrival"), "arrival")
# ------------------------------------------------------------------ AB4.5 and AB4.7
L += ["\n## AB4.5 and AB4.7 from the record\n"]
CC = count_rows_all(CW3)
pl_share = ratio_se(col(CC, "plant_bad") + col(CC, "plant_good"), col(CC, "rv_member")); pb_share = ratio_se(col(CC, "plant_bad"), col(CC, "rv_member"))
L.append(f"- **AB4.5.** The planted cases are {pm(pl_share, 3)} of a careful member's reviews as a member over every seat in world 3's all-careful ({pm(pb_share, 3)} the bad ones), so 27.5 reviews as a member hold {27.5 * pl_share[0]:.1f} planted cases of both kinds and {27.5 * pb_share[0]:.1f} bad ones. By the rule the first suspension of a member that claims at every review falls at its fourth planted bad case where its window starts empty (the record is read from n_min = 4 bad plants on; four wrong of four is 5/6), and at the fifth wrong one where the window holds the four right verdicts of a probation (five wrong beside four right is 6/11, the fourth 5/10 is not above 0.5).")
def split_rows(E):
    out = []
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"]: continue
        r = {"seed": int(e["seed"])}; Pt = f(e, "P_t"); gv = G_V * 20.0 / Pt if Pt else np.nan
        for kk, V in g.items():
            n = len(V); s = lambda k: sum(v.get(k, 0.0) for v in V) / n
            d = {"n": n, "good": s("ticks_good"), "ig": s("income_good"), "life": sum(life(v) for v in V) / n, "ben": s("private_real"), "pw": sum(sum(x for k, x in v.items() if k.startswith("pw_member_")) for v in V) / n}
            for st in SEATS: d[f"n_{st}"] = s(f"rvm_{st}"); d[f"beyond_{st}"] = s(f"rf_member_{st}_fee") + s(f"rf_member_{st}_emission") + s(f"rf_member_{st}_uplift"); d[f"bond_{st}"] = -s(f"rf_member_{st}_bond"); d[f"pw_{st}"] = s(f"pw_member_{st}")
            d["beyond"] = sum(d[f"beyond_{st}"] for st in SEATS); d["bond"] = sum(d[f"bond_{st}"] for st in SEATS); d["bond_planted"] = d["pw"] * gv; d["bond_real"] = d["bond"] - d["bond_planted"]
            d["care"] = s("care_member") + s("claimed_member"); d["reimb"] = sum(s(f"rf_member_{st}_reimb") for st in SEATS); d["courtfee"] = sum(s(f"rf_member_{st}_courtfee") for st in SEATS)
            d["fa_ov"] = s("fa_init_overturned"); d["fa"] = s("fa_init"); d["nseats"] = sum(d[f"n_{st}"] for st in SEATS); d["gv"] = gv
            r[kk] = d
        out.append(r)
    return out
SP9 = split_rows(R9) if R9 else []
if SP9:
    L += ["\n**AB4.7 — the split of read 9's loss from the flows by seat** (a19/rerun/r9 at 906fc5ac4: the conduct's slots and the careful beside them, a mean a slot by seed, the difference careful − conduct ± its SE over the seeds; every flow real at its tick and tallied to the seat of the review it belongs to; the bond on the planted cases is the wrong planted verdicts as a member times the bond G^V = 5 at the run's closing index, the bond on real work the rest of the bonds lost at member seats).\n",
          "| | the conduct's slot | the careful beside | **careful − conduct** |", "|---|---|---|---|"]
    def dline(nm, k, d=1, sign=1):
        a = np.array([r["claim"][k] for r in SP9]); b = np.array([r["care"][k] for r in SP9]); dd = mse(sign * (b - a)); L.append(f"| {nm} | {a.mean():.{d}f} | {b.mean():.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** |")
    dline("the lifetime of record (wallet + benefit)", "life", 0); dline("the benefit (what the claims spared)", "ben", 1); dline("ticks in good standing", "good", 0); dline("income in good standing (K3)", "ig", 0)
    dline("reviews as a member (every seat)", "nseats", 1)
    for st in SEATS:
        if np.mean([r["care"][f"n_{st}"] for r in SP9]) > 0.05: dline(f"… at {SEAT_N[st]}", f"n_{st}", 1)
    dline("**income beyond the care at member seats (fee + emission + uplift), real**", "beyond", 0)
    for st in SEATS:
        if np.mean([r["care"][f"beyond_{st}"] for r in SP9]) > 0.5: dline(f"… at {SEAT_N[st]}", f"beyond_{st}", 1)
    dline("the care spent and claimed at member seats", "care", 0); dline("the care reimbursed at member seats", "reimb", 0)
    dline("**bonds lost at member seats, real (all)**", "bond", 1)
    for st in SEATS:
        if np.mean([r["care"][f"bond_{st}"] for r in SP9]) > 0.05: dline(f"… at {SEAT_N[st]}", f"bond_{st}", 1)
    dline("… on the planted cases (wrong planted verdicts × G^V at the closing index; an upper estimate, the bond is 5 real at P_0 and more as P_t falls)", "bond_planted", 1); dline("… on real work (the rest; a lower estimate)", "bond_real", 1)
    dline("wrong planted verdicts as a member", "pw", 2); dline("wrong first approvals of real bad work / of which overturned", "fa", 2); dline("… overturned", "fa_ov", 2)
    dline("court fees at member seats (net)", "courtfee", 1)
    a_ = lambda k: np.mean([r["care"][k] - r["claim"][k] for r in SP9])
    L.append(f"\nSo of the {a_('life'):.0f} real a careful slot ends ahead of the conduct's of record (the 109 of §116; with the {np.mean([r['claim']['ben'] for r in SP9]):.1f} the claims spared, {a_('life') + np.mean([r['claim']['ben'] for r in SP9]):.0f} before the saving), the seats carry {a_('beyond'):.0f} real of income beyond the care that the conduct does not earn ({a_('beyond_audit'):.0f} of it at the audit seat, {a_('beyond_third') + a_('beyond_appeal') + a_('beyond_dispute'):.0f} at the panels, {a_('beyond_initial'):+.0f} at the first review), the bonds {a_('bond'):+.1f} real in all — the conduct loses {-a_('bond_planted'):.1f} more on its planted cases (an upper estimate at the closing index; at least {-(np.mean([r['claim']['pw'] - r['care']['pw'] for r in SP9]) * 5):.1f} at P_0) and {-a_('bond_initial'):.1f} more at the first review, where its 0.74 more overturned approvals of real bad work sit, while the careful loses {a_('bond_audit') + a_('bond_third') + a_('bond_appeal') + a_('bond_dispute'):.1f} more at the audit seat and the panels it holds and the conduct does not (a careful auditor's own one error in twenty on a real case, overturned when challenged) — and the rest is the work side and the ticks out of good standing ({a_('good'):.0f} fewer good ticks). The reviewer's 75 real in seats, under 4 in bonds on real work and 'more than half of what the conduct loses is what its failed planted cases cost it' are read against these figures in the notes.")
# ------------------------------------------------------------------ the two cells: reads 20 and 23 against world 3's all-careful
L += ["\n## Reads 20 and 23. The all-careful population with the suspension's threshold moved — against world 3's all-careful by seed (seeds 21–120, the seeds the record holds)\n",
      "The row V3.1 gave for an all-careful population (a slot's lifetime of record, with the reservation, and its income in good standing — the like-for-like figure for a population with no conduct beside it), for all slots, the founders and the arrivals; then the suspensions, the spells, the admissions and the world's side, each cell − world 3 paired by seed.\n"]
CELLS = [("read 20: θ_duty 0.34 (the second failure)", C20), ("read 23: θ_duty 0.20 (the first failure)", C23)]
SS = {}
for nm, Cd in CELLS:
    if not Cd: continue
    L += [f"\n**{nm}** ({len(Cd)} seeds; paired on the {len(set(Cd) & set(CW3))} the record holds)\n", "| slots | measure | seeds | world 3's cell | the cell | **cell − world 3, paired** | SE from nothing |", "|---|---|---|---|---|---|---|"]
    for gl, filt in (("every slot", lambda v: True), ("the founders", lambda v: v["t_in"] == 0), ("the arrivals", lambda v: v["t_in"] > 0)):
        a = susp_split(CW3, filt); b = susp_split(Cd, filt); SS[(nm, gl)] = (a, b)
        paired_cells(L, gl, a, b, (("life", "lifetime of record", 0), ("lres", "with the reservation", 0), ("ig", "income in good standing", 0), ("good", "good ticks a slot", 0), ("susp", "suspensions a slot", 2), ("any", "slots suspended at least once (share)", 3), ("mem", "… as a member", 3), ("pro", "… on probation", 3)) + ((("adm", "arrivals admitted within the run (share)", 3),) if gl != "the founders" else ()))
    a, b = SS[(nm, "every slot")]
    L.append(f"| the world | | | | | | |")
    paired_cells(L, "the world", a, b, (("fa", "standing false approvals a run", 1), ("leak", "the leak, ‰ of bad deliveries", 1), ("oh", "the system overhead a vested task", 2), ("cot", "the cost of truth a run", 0), ("dep", "departures a run", 1), ("arrivals", "arrivals a run", 1), ("Pt", "P_t at the end", 1)))
    mm = sum(r["mism"] for r in b); L.append(f"\n(The suspension log and the spells are matched a tick apart — a spell closes at the standing step of the tick after the suspension is logged; {mm} probation spells end at a tick the log does not hold.)")
    # the failed careful members from the failure on
    fa_, fb_ = failed_members(CW3), failed_members(Cd)
    L += [f"\n**The careful slots that take a wrong planted verdict as a member, from that failure on** — {nm} against world 3's cell by seed (the slots' first failure to the exit: the income of record with the benefit, with the reservation, and like for like as the cell's failed slots' good-standing income less world 3's failed slots' rate over the cell's good ticks from the failure; a mean over a seed's failed slots, then over the seeds):\n",
          "| | world 3's cell | the cell | **cell − world 3, paired** | SE |", "|---|---|---|---|---|"]
    A_ = {r["seed"]: r for r in fa_}; B_ = {r["seed"]: r for r in fb_}; seeds = sorted(set(A_) & set(B_))
    def fl(nm_, fn, d=0):
        x = np.array([fn(A_[s]) for s in seeds]); y = np.array([fn(B_[s]) for s in seeds]); dd = mse(y - x); L.append(f"| {nm_} | {x.mean():.{d}f} | {y.mean():.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** | {dd[0] / dd[1] if dd[1] else np.nan:.1f} |"); return dd
    fl("failed slots a seed (as members)", lambda r: r["n"], 1)
    FM = {}
    FM["rec"] = fl("from the first failure: of record", lambda r: r["rec"]); FM["res"] = fl("… with the reservation", lambda r: r["res"])
    x = np.array([A_[s]["gi"] for s in seeds]); y = np.array([B_[s]["gi"] - A_[s]["rate"] * B_[s]["gt"] + A_[s]["gi"] - A_[s]["gi"] for s in seeds])
    # like for like: the cell's failed slots' good income less world 3's rate over the cell's good ticks (positive = the cell's slot ahead); as cell − world 3 it is the cell's gi less (world 3's rate × the cell's gt)
    lfl = np.array([B_[s]["gi"] - A_[s]["rate"] * B_[s]["gt"] for s in seeds]); dd = mse(lfl); FM["lfl"] = dd; L.append(f"| … like for like (the cell's good income less world 3's rate over the cell's good ticks) | | | **{dd[0]:+.0f} ± {dd[1]:.0f}** | {dd[0] / dd[1]:.1f} |")
    fl("good ticks from the failure", lambda r: r["gt"]); fl("ticks from the failure to the exit", lambda r: r["ticks"]); fl("ticks without the earned seats", lambda r: r["tlost"]); fl("share whose seats returned", lambda r: r["back"], 2)
    fl("further wrong planted verdicts", lambda r: r["more"], 2); fl("suspensions from the failure on", lambda r: r["susp_after"], 2); fl("departed share", lambda r: r["dep"], 2)
    SS[(nm, "failed")] = FM
# ------------------------------------------------------------------ read 21 against read 17
L += ["\n## Read 21. Conduct G at 1.0 on 1 slot in 4 in the cell of the second failure (θ_duty 0.34), seeds 21–140 — read as read 17 was, and against read 17 by seed\n"] + HDR_F
FR = {"r17": failed_rows(R17), "r21": failed_rows(R21) if R21 else []}
failed_table(L, "read 17: conduct G at 1.0, world 3's cell (120 seeds)", FR["r17"]); failed_table(L, "**read 21: conduct G at 1.0, θ_duty 0.34 (120 seeds)**", FR["r21"])
L += ["\nOver the whole life (the careful slots beside, of the same world and seed; the cell's all-careful for the careful group's contrast):\n"] + HDR_L
ROWS = {"r17": rows_of(R17, CW3), "r21": rows_of(R21, C20) if R21 else []}
for nm, rows in (("read 17: G at 1.0, world 3's cell", ROWS["r17"]), ("**read 21: G at 1.0, θ_duty 0.34**", ROWS["r21"])):
    if rows: L.append(lifetimes_row(nm, rows))
L += ["\n"] + HDR_G
for nm, rows in (("read 17", ROWS["r17"]), ("**read 21**", ROWS["r21"])):
    if rows: L.append(groups_row(nm, rows))
L += ["\n"] + HDR_P
P21 = {}
if FR["r21"]:
    P21["life"] = paired_rows(L, "read 21 against read 17 (G at 1.0: θ_duty 0.34 less world 3's cell), over the life", ROWS["r17"], ROWS["r21"])
    P21["fail"] = paired_rows(L, "… from the first failure on (the failed slots)", FR["r17"], FR["r21"])
    L += ["\n| read | failed slots | suspended after the failure (share) | ticks from the first failure to the first suspension: mean / median | claims in them a suspended slot: mean / median | claims a never-suspended failed slot |", "|---|---|---|---|---|---|"]
    for nm, E in (("17: G at 1.0, world 3's cell", R17), ("**21: G at 1.0, θ_duty 0.34**", R21)):
        nf, ns, tk, cl, cs = to_susp(E)
        if nf: L.append(f"| {nm} | {nf} | {ns} ({ns / nf:.2f}) | {np.mean(tk) if tk else np.nan:.0f} / {np.median(tk) if tk else np.nan:.0f} | {np.nanmean(cl) if cl else np.nan:.1f} / {np.nanmedian(cl) if cl else np.nan:.0f} | {np.nanmean(cs) if cs else np.nan:.1f} |")
# ------------------------------------------------------------------ reads 22 and 24 against read 9
L += ["\n## Reads 22 and 24. Conduct M at 0.1 on 1 slot in 4 in the two cells — read as reads 9 and 19 were, and against read 9 by seed\n"] + HDR_L
ROWS["r9"] = rows_of(R9, CW3); ROWS["r22"] = rows_of(R22, C20) if R22 else []; ROWS["r24"] = rows_of(R24, C23) if R24 else []; ROWS["r19"] = rows_of(R19, CW3) if R19 else []
for nm, rows in (("read 9: M at 0.1, world 3's cell (θ_duty 0.50)", ROWS["r9"]), ("**read 22: M at 0.1, θ_duty 0.34**", ROWS["r22"]), ("**read 24: M at 0.1, θ_duty 0.20**", ROWS["r24"]), ("read 19: M at 0.2, world 3's cell", ROWS["r19"])):
    if rows: L.append(lifetimes_row(nm, rows))
L += ["\n"] + HDR_G
for nm, rows in (("read 9", ROWS["r9"]), ("**read 22**", ROWS["r22"]), ("**read 24**", ROWS["r24"]), ("read 19", ROWS["r19"])):
    if rows: L.append(groups_row(nm, rows))
L += ["\n| read | seeds | **the level saving, the ratio of the seeds' means: of record / with the reservation / like for like** | the mean of the seeds' ratios | the identity's q · T* | claims as a member over member reviews | member reviews a slot; claims as a member |", "|---|---|---|---|---|---|---|"]
LV = {}
for nm, E, q in (("read 9", R9, 0.1), ("**read 22**", R22, 0.1), ("**read 24**", R24, 0.1), ("read 19", R19, 0.2)):
    rows = level_rows(E) if E else []
    if not rows: continue
    rm, mr = level_line(rows); Tt = tuple(temp(ROWS[{"read 9": "r9", "**read 22**": "r22", "**read 24**": "r24", "read 19": "r19"}[nm]], k, d)[0] for k, d in (("rec", "ben"), ("res", "ben"), ("lfl", "den"))); LV[nm] = (rm, mr, Tt)
    L.append(f"| {nm} | {len(rows)} | **{pm(rm[0], 2)} / {pm(rm[1], 2)} / {pm(rm[2], 2)}** | {pm(mr[0], 2)} / {pm(mr[1], 2)} / {pm(mr[2], 2)} | {q * Tt[0]:.2f} / {q * Tt[1]:.2f} / {q * Tt[2]:.2f} | {np.mean(col(rows, 'share')):.3f} | {np.mean(col(rows, 'rvm')):.1f}; {np.mean(col(rows, 'cm')):.1f} |")
CN = {k: (count_rows(E, "claim"), count_rows(E, "care")) for k, E in (("r9", R9), ("r22", R22), ("r24", R24), ("r19", R19)) if E}
L += ["\n**W3's three counts and the suspensions** (a mean a slot):\n", "| count | read 9: conduct / careful beside | **read 22: conduct / careful** | **read 24: conduct / careful** | read 19: conduct / careful |", "|---|---|---|---|---|"]
def cc_(k, d=1, fn=None):
    cells = []
    for key in ("r9", "r22", "r24", "r19"):
        if key not in CN: cells.append("(pending)"); continue
        a, b = CN[key]; cells.append(f"{(fn(a) if fn else m(a, k)[0]):.{d}f} / {(fn(b) if fn else m(b, k)[0]):.{d}f}")
    return " | ".join(cells)
for nm, k, d in (("reviews as a member in a life", "rv_member", 1), ("… at the first review", "initial", 1), ("… at the audit seat", "audit", 1), ("reviews on probation", "rv_probation", 1), ("good ticks a slot", "good", 0), ("planted bad cases met as a member", "plant_bad", 1), ("wrong planted verdicts as a member", "pw_member", 2), ("… on probation", "pw_probation", 2),
                 ("slots reaching a wrong planted verdict as a member (share)", "reach_fail_m", 2), ("**slots suspended at least once (share)**", "reach_susp", 2), ("suspensions a slot", "susp", 2), ("reviews of real tasks as a member before the first suspension, over the slots suspended", "pre_susp_r", 1),
                 ("wrong first approvals of real bad work in a life", "fa", 2), ("… of which stay paid", "fa_paid", 2)):
    L.append(f"| {nm} | {cc_(k, d)} |")
FAR = {}
for key in CN:
    a, b = CN[key]; FAR[key] = ratio_se(col(a, "fa"), col(b, "fa"))
L.append("| the conduct's wrong first approvals over the careful beside's | " + " | ".join(pm(FAR[k], 2) if k in FAR else "(pending)" for k in ("r9", "r22", "r24", "r19")) + " |")
L += ["\n"] + HDR_P
P22 = P24 = {}
if ROWS["r22"]: P22 = paired_rows(L, "read 22 against read 9 (M at 0.1: θ_duty 0.34 less world 3's cell), the gap careful − conduct over the life", ROWS["r9"], ROWS["r22"])
if ROWS["r24"]: P24 = paired_rows(L, "read 24 against read 9 (M at 0.1: θ_duty 0.20 less world 3's cell)", ROWS["r9"], ROWS["r24"])
if ROWS["r22"] and ROWS["r24"]: paired_rows(L, "read 24 against read 22 (θ_duty 0.20 less 0.34)", ROWS["r22"], ROWS["r24"])
# the careful beside against the cell's all-careful, and the conduct against the cell's all-careful (V3.2's form)
# ------------------------------------------------------------------ AB4.6 the relation across thresholds
L += ["\n## AB4.6. Across the three thresholds: what the careful lose, and where the level saving stands\n",
      "| θ_duty | the careful population's slot: cell − world 3 of record (paired by seed) | … with the reservation | … income in good standing | the careful failed member from its failure on: cell − world 3 | conduct M at 0.1 on 1 in 4: behind the careful beside, of record | its level saving of record (ratio of means) | its slots suspended at least once |", "|---|---|---|---|---|---|---|---|"]
for th, nm, rk, lk in (("0.50 (of record)", None, "r9", "read 9"), ("0.34", "read 20: θ_duty 0.34 (the second failure)", "r22", "**read 22**"), ("0.20", "read 23: θ_duty 0.20 (the first failure)", "r24", "**read 24**")):
    if nm is None: cell = "0 (the record) | 0 | 0 | 0"
    elif (nm, "every slot") in SS:
        a, b = SS[(nm, "every slot")]; A_ = {r["seed"]: r for r in a}; B_ = {r["seed"]: r for r in b}; sd = sorted(set(A_) & set(B_))
        dl = mse([B_[s]["life"] - A_[s]["life"] for s in sd]); dr = mse([B_[s]["lres"] - A_[s]["lres"] for s in sd]); di = mse([B_[s]["ig"] - A_[s]["ig"] for s in sd]); fm = SS.get((nm, "failed"), {}).get("rec", (np.nan, np.nan))
        cell = f"{dl[0]:+.0f} ± {dl[1]:.0f} | {dr[0]:+.0f} ± {dr[1]:.0f} | {di[0]:+.0f} ± {di[1]:.0f} | {fm[0]:+.0f} ± {fm[1]:.0f}"
    else: cell = "(pending) | | |"
    rows = ROWS.get(rk, []); lv = LV.get(lk)
    L.append(f"| {th} | {cell} | {pm(mse(col(rows, 'rec')), 0) if rows else '(pending)'} | {pm(lv[0][0], 2) if lv else '(pending)'} | {m(CN[rk][0], 'reach_susp')[0]:.2f} / careful {m(CN[rk][1], 'reach_susp')[0]:.2f} |" if rk in CN else f"| {th} | {cell} | (pending) | | |")
L.append("\nThe reviewer's relation (AB4.6): a cheaper model stops paying where its extra failures (0.95 q a test beyond the careful's 0.05) cost what it saves, so at the line the careful lose, by their own failures, 0.05 ÷ (0.95 q) of what the model would save. It is a relation between the cost of a failure and the line, not a read; the rows above are the measured pairs it is set against.")
# ------------------------------------------------------------------ read 25 against read 18 and the all-careful
L += ["\n## Read 25. Conduct M at 0.1 with its claims set by the case, on every slot — world 3's cell, seeds 21–120, read as read 18 was, and against read 18 by seed\n",
      "Every slot of the world follows the conduct: as a member a claim where the case's hash falls under the dose (the same cases for every slot of the seed, at every seat), careful at the others and on probation. Each row a seed: the all-careful's slot less the population's; then the population against read 18's by seed.\n"]
P25 = pop_rows(R25, CW3) if R25 else []; P18 = pop_rows(R18, CW3) if R18 else []
HDR_POP = ["| read | seeds | slots a seed: population / all-careful | **all-careful − population, of record** (SE from nothing) | temptation | **with the reservation** | temptation | like for like (reported) | the population's slot: of record / with the reservation | suspended at least once (share): population / all-careful | member reviews a slot: population / all-careful | audit seats a slot: population / all-careful |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
L += HDR_POP
for nm, P in (("18: M at 0.1 on every slot (claims drawn at each review)", P18), ("**25: M at 0.1 on every slot, the claims set by the case**", P25)):
    if not P: continue
    a, b, c = mse(col(P, "rec")), mse(col(P, "res")), mse(col(P, "lfl")); ta, tb = temp(P, "rec", "ben"), temp(P, "res", "ben")
    L.append(f"| {nm} | {len(P)} | {np.mean(col(P, 'n')):.1f} / {np.mean(col(P, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {ta[0]:.1f} ± {ta[1]:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f}) | {tb[0]:.1f} ± {tb[1]:.1f} | {c[0]:+.0f} ± {c[1]:.0f} | {np.mean(col(P, 'life')):.0f} / {np.mean(col(P, 'lres')):.0f} | {np.mean(col(P, 'reach')):.2f} / {np.mean(col(P, 'reachc')):.2f} | {np.mean(col(P, 'rvm')):.1f} / {np.mean(col(P, 'rvmc')):.1f} | {np.mean(col(P, 'aud')):.1f} / {np.mean(col(P, 'audc')):.1f} |")
L += ["\n| read | what the claims spared a slot | the care on all its reviews as a member | claims a slot | **the population's level saving, the ratio of the seeds' means: of record / with the reservation / like for like** | the mean of the seeds' ratios | wrong first approvals of real bad work a slot (paid) |", "|---|---|---|---|---|---|---|"]
RM = {}
for nm, P in (("18", P18), ("**25**", P25)):
    if not P: continue
    rm = tuple(ratio_se(col(P, f"loss_{k}") + col(P, "spared"), col(P, "call")) for k in ("rec", "res", "lfl")); mr = tuple(mse(col(P, f"x_{k}")) for k in ("rec", "res", "lfl")); RM[nm] = rm
    L.append(f"| {nm} | {pm(mse(col(P, 'spared')))} | {pm(mse(col(P, 'call')), 0)} | {pm(mse(col(P, 'claims')))} | **{pm(rm[0], 2)} / {pm(rm[1], 2)} / {pm(rm[2], 2)}** | {pm(mr[0], 2)} / {pm(mr[1], 2)} / {pm(mr[2], 2)} | {np.mean(col(P, 'fai')):.2f} ({np.mean(col(P, 'fpaid')):.2f}) |")
WK = (("fa", "fa0", "standing false approvals a run", 1), ("leak", "leak0", "the leak, ‰ of bad deliveries", 1), ("oh", "oh0", "the system overhead a vested task", 2), ("cot", "cot0", "the cost of truth a run", 0), ("dep", "dep0", "departures a run", 1), ("arr", "arr0", "arrivals a run", 1), ("Pt", "Pt0", "P_t at the end", 1))
L += ["\n**The world's side, paired by seed** (the population's less the all-careful's):\n", "| measure | read 18 | read 25 | the all-careful | **read 18 − all-careful** | **read 25 − all-careful** | **read 25 − read 18** (SE from nothing) |", "|---|---|---|---|---|---|---|"]
W25 = {}
if P25 and P18:
    A_ = {r["seed"]: r for r in P18}; B_ = {r["seed"]: r for r in P25}; sd = sorted(set(A_) & set(B_))
    for k, k0, nm, d in WK:
        d18 = mse(col(P18, k) - col(P18, k0)); d25 = mse(col(P25, k) - col(P25, k0)); dd = mse([B_[s][k] - A_[s][k] for s in sd]); W25[k] = (dd, np.mean(col(P25, k)), np.mean(col(P18, k)))
        L.append(f"| {nm} | {np.mean(col(P18, k)):.{d}f} | {np.mean(col(P25, k)):.{d}f} | {np.mean(col(P25, k0)):.{d}f} | {d18[0]:+.{d}f} ± {d18[1]:.{d}f} | {d25[0]:+.{d}f} ± {d25[1]:.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** ({dd[0] / dd[1]:.1f}) |")
    L += ["\n**The members' side, read 25 against read 18 by seed** (the population's slot):\n", "| measure | read 18 | read 25 | **read 25 − read 18** (SE) |", "|---|---|---|---|"]
    for k, nm, d in (("life", "the slot's lifetime of record", 0), ("lres", "… with the reservation", 0), ("ig", "… income in good standing", 0), ("good", "good ticks a slot", 0), ("reach", "slots suspended at least once (share)", 3), ("susp", "suspensions a slot", 3), ("rvm", "member reviews a slot", 1), ("aud", "audit seats a slot", 1), ("claims", "claims a slot", 1), ("spared", "what the claims spared", 1), ("fai", "wrong first approvals of real bad work a slot", 2), ("fpaid", "… that stay paid", 2)):
        dd = mse([B_[s][k] - A_[s][k] for s in sd]); W25[k] = (dd, np.mean(col(P25, k)), np.mean(col(P18, k))); L.append(f"| {nm} | {np.mean(col(P18, k)):.{d}f} | {np.mean(col(P25, k)):.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
    # the claims by kind at the first review (Z4.2's rows) for read 25
    def kind_rows(Cd, st):
        rows = []
        for key, c in sorted(Cd.items()):
            V = slots(c); g = lambda k: sum(v.get(k, 0) for v in V)
            rb, rg, pb, pg, fai = g(f"rvi_{st}_real_bad"), g(f"rvi_{st}_real_good"), g(f"rvi_{st}_plant_bad"), g(f"rvi_{st}_plant_good"), g(f"fai_{st}"); tot = rb + rg + pb + pg
            if tot: rows.append(dict(seed=int(c["seed"]), n=len(V), rb=rb, rg=rg, pb=pb, pg=pg, fai=fai, tot=tot))
        return rows
    L += ["\n| population, as a member | wrong first approvals of real bad work over the real bad work reviewed first | planted bad share of the first reviews |", "|---|---|---|"]
    for nm, Cd in (("read 18", D(R18)), ("read 25", D(R25)), ("the all-careful", CW3)):
        kr = kind_rows(Cd, "member"); L.append(f"| {nm} | {pm(ratio_se(col(kr, 'fai'), col(kr, 'rb')), 3)} | {pm(ratio_se(col(kr, 'pb'), col(kr, 'tot')), 3)} |")
# ------------------------------------------------------------------ expectations
L += ["\n## Against the expectations stated before the run (AB6, AB7)\n"]
def gget(key, k, which=0): a, b = CN[key]; return m(a if which == 0 else b, k)[0]
if C20 and ("read 20: θ_duty 0.34 (the second failure)", "every slot") in SS:
    a, b = SS[("read 20: θ_duty 0.34 (the second failure)", "every slot")]; A_ = {r["seed"]: r for r in a}; B_ = {r["seed"]: r for r in b}; sd = sorted(set(A_) & set(B_))
    s20 = np.mean(col(b, "susp")); r20 = np.mean(col(b, "any")); adm20 = np.nanmean(col(b, "adm")); dl20 = mse([B_[s]["life"] - A_[s]["life"] for s in sd]); lk20 = np.mean(col(b, "leak"))
    chk(in_band(s20, 0.13, 0.19), f"read 20: suspensions a slot 0.13 to 0.19: {s20:.2f}."); chk(in_band(100 * r20, 12, 17), f"read 20: 12 to 17 slots in 100 suspended at least once: {100 * r20:.0f}.")
    chk(in_band(100 * adm20, 86, 89), f"read 20: arrivals admitted within the run 86 to 89 in 100: {100 * adm20:.0f}."); chk(in_band(dl20[0], -25, 10), f"read 20: a slot's lifetime of record between 25 under world 3's and 10 over at the point value: {dl20[0]:+.0f} ± {dl20[1]:.0f} by seed."); chk(in_band(lk20, 4.0, 5.6), f"read 20: a leak of 4.0 to 5.6 in a thousand: {lk20:.1f}.")
if FR["r21"]:
    gF = lambda k: np.mean([r["F"][k] for r in FR["r21"]]); gC = lambda k: np.mean([r["C"][k] for r in FR["r21"]]); a21 = mse(col(FR["r21"], "rec")); b21 = mse(col(FR["r21"], "res"))
    chk(in_band(gF("claims"), 7, 12), f"read 21: between 7 and 12 claims a failed slot (read 17's 15.6): {gF('claims'):.1f}."); chk(in_band(gF("susp_after"), 0.60, 0.90), f"read 21: suspensions a failed slot from the failure on 0.60 to 0.90 for the conduct: {gF('susp_after'):.2f}."); chk(in_band(gC("susp_after"), 0.22, 0.32), f"read 21: … 0.22 to 0.32 for the careful failed slots: {gC('susp_after'):.2f}.")
    chk(in_band(a21[0], 40, 160), f"read 21: the conduct behind the careful failed slots by 40 to 160 real of record from the first failure on: {a21[0]:+.0f} ± {a21[1]:.0f}."); chk(in_band(b21[0], -20, 90), f"read 21: with the reservation between 20 ahead and 90 behind (the sign not called): {b21[0]:+.0f} ± {b21[1]:.0f}.")
    if P21.get("fail"): dd = P21["fail"]["rec"]; chk(in_band(dd[0], 20, 140), f"read 21: by seed worse off than read 17's conduct by 20 to 140 real of record (the gap from the failure on, read 21 less read 17): {dd[0]:+.0f} ± {dd[1]:.0f}.")
if "r22" in CN:
    a22 = mse(col(ROWS["r22"], "rec")); chk(in_band(100 * gget("r22", "reach_susp"), 18, 28), f"read 22: 18 to 28 of the conduct's slots in 100 suspended at least once: {100 * gget('r22', 'reach_susp'):.0f}."); chk(in_band(100 * gget("r22", "reach_susp", 1), 12, 17), f"read 22: 12 to 17 of the careful beside: {100 * gget('r22', 'reach_susp', 1):.0f}.")
    chk(in_band(a22[0], 110, 180), f"read 22: behind by 110 to 180 real of record: {a22[0]:+.0f} ± {a22[1]:.0f}."); chk(in_band(LV["**read 22**"][0][0][0], 0.65, 0.95), f"read 22: a level saving of 0.65 to 0.95 of record: {pm(LV['**read 22**'][0][0], 2)}.")
if C23 and ("read 23: θ_duty 0.20 (the first failure)", "every slot") in SS:
    a, b = SS[("read 23: θ_duty 0.20 (the first failure)", "every slot")]; A_ = {r["seed"]: r for r in a}; B_ = {r["seed"]: r for r in b}; sd = sorted(set(A_) & set(B_))
    s23 = np.mean(col(b, "susp")); r23 = np.mean(col(b, "any")); g23 = np.mean(col(b, "good")); adm23 = np.nanmean(col(b, "adm")); dl23 = mse([B_[s]["life"] - A_[s]["life"] for s in sd]); lk = mse([B_[s]["leak"] - A_[s]["leak"] for s in sd]); oh23 = np.mean(col(b, "oh"))
    back = [s["whole"] for s in RET.get("read 23's world (all-careful, θ_duty 0.20)", []) if s["end"] == "member"]; wb = np.mean(back) if back else np.nan; fm = SS.get(("read 23: θ_duty 0.20 (the first failure)", "failed"), {}).get("rec", (np.nan, np.nan))
    chk(in_band(s23, 0.36, 0.56), f"read 23: suspensions a slot 0.36 to 0.56: {s23:.2f}."); chk(in_band(100 * r23, 30, 45), f"read 23: 30 to 45 slots in 100 suspended at least once: {100 * r23:.0f}."); chk(in_band(g23, 410, 480), f"read 23: good ticks a slot 410 to 480 (world 3's 550): {g23:.0f} ({np.mean(col(a, 'good')):.0f}).")
    chk(in_band(100 * adm23, 74, 85), f"read 23: arrivals admitted within the run 74 to 85 in 100: {100 * adm23:.0f}."); chk(in_band(wb, 350, 520), f"read 23: the way back from a member's suspension to a readmission 350 to 520 ticks from the suspension: {wb:.0f} (n = {len(back)}).")
    chk(in_band(dl23[0], -80, 0), f"read 23: a slot's lifetime of record between level with world 3's and 80 under it: {dl23[0]:+.0f} ± {dl23[1]:.0f} by seed."); chk(in_band(-fm[0], 80, 250), f"read 23: a careful member that fails ends 80 to 250 real lower from the failure on than in world 3's cell: {fm[0]:+.0f} ± {fm[1]:.0f} (cell − world 3).")
    chk(lk[0] <= 1.0, f"read 23: a leak no more than 1 in a thousand above world 3's: {lk[0]:+.1f} ± {lk[1]:.1f}."); chk(in_band(oh23, 11.9, 13.6), f"read 23: an overhead of 11.9 to 13.6: {oh23:.2f}.")
if "r24" in CN:
    a24 = mse(col(ROWS["r24"], "rec")); chk(in_band(100 * gget("r24", "reach_susp"), 50, 70), f"read 24: 50 to 70 of the conduct's slots in 100 suspended at least once: {100 * gget('r24', 'reach_susp'):.0f}."); chk(in_band(100 * gget("r24", "reach_susp", 1), 30, 45), f"read 24: 30 to 45 of the careful beside: {100 * gget('r24', 'reach_susp', 1):.0f}.")
    chk(in_band(gget("r24", "rv_member"), 38, 56), f"read 24: between 38 and 56 reviews as a member in a life (read 9's 75.4): {gget('r24', 'rv_member'):.1f}."); chk(in_band(a24[0], 80, 220), f"read 24: behind by 80 to 220 real of record: {a24[0]:+.0f} ± {a24[1]:.0f}."); chk(in_band(LV["**read 24**"][0][0][0], 0.8, 1.6), f"read 24: a level saving of 0.8 to 1.6 of record (the side of 0.9 not called): {pm(LV['**read 24**'][0][0], 2)}.")
if P25 and W25:
    lk25, fa25 = W25["leak"][1], W25["fa"][1]; chk(in_band(lk25, 40, 120), f"read 25: the leak 40 to 120 in a thousand bad deliveries (read 18's {W25['leak'][2]:.1f}): {lk25:.1f}."); chk(in_band(fa25, 20, 60), f"read 25: the standing false approvals 20 to 60 a run (read 18's {W25['fa'][2]:.1f}): {fa25:.1f}.")
    chk(abs(W25["life"][0][0]) <= 30, f"read 25: a slot within 30 real of read 18's of record: {W25['life'][0][0]:+.0f} ± {W25['life'][0][1]:.0f} by seed."); chk(abs(100 * W25["reach"][0][0]) <= 4, f"read 25: as many slots suspended as read 18, within 4 in 100: {100 * W25['reach'][0][0]:+.1f} ± {100 * W25['reach'][0][1]:.1f}.")
L += CHK; n_met = sum(1 for c in CHK if c.startswith("- MET")); L.append(f"\n**{n_met} of {len(CHK)} met.**")
# ------------------------------------------------------------------ refuted or shown
L += ["\n## Refuted, or shown, each apart\n"]
def verdict(text, shown, refuted): return f"- {text} **{'Shown' if shown else ('Refuted' if refuted else 'Neither')}.**"
if FR["r21"]:
    a = mse(col(FR["r21"], "rec")); L.append(verdict(f"*With the suspension at the second failure, a claim costs something while the earned seats are lost*: shown if read 21's conduct is behind the careful failed slots by two standard errors of record, from the first failure on; refuted if it is within one standard error of nothing, or ahead. It is {a[0]:+.0f} ± {a[1]:.0f} ({a[0] / a[1]:.1f} SE).", a[0] >= 2 * a[1], a[0] <= a[1]))
if C20 and ("read 20: θ_duty 0.34 (the second failure)", "every slot") in SS:
    L.append(verdict(f"*The suspension at the second failure costs the careful nothing that a read can see*: refuted if read 20's slot ends below world 3's by two standard errors of record, by seed; shown if it is within one standard error of it, or above. Cell − world 3 is {dl20[0]:+.0f} ± {dl20[1]:.0f} ({dl20[0] / dl20[1]:.1f} SE).", dl20[0] >= -dl20[1], dl20[0] <= -2 * dl20[1]))
if "**read 22**" in LV:
    x = LV["**read 22**"][0][0]; L.append(verdict(f"*The suspension at the second failure holds a model that spares nine tenths at a dose of 0.1*: shown if read 22's level saving is above 0.9 by two standard errors of record; refuted if it is under 0.9 at the point value. It is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] - 0.9 >= 2 * x[1], x[0] < 0.9))
if "**read 24**" in LV:
    x = LV["**read 24**"][0][0]; L.append(verdict(f"*The suspension at the first failure, with the way back as built, holds that model at that dose*: the same condition on read 24. It is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] - 0.9 >= 2 * x[1], x[0] < 0.9))
if C23 and ("read 23: θ_duty 0.20 (the first failure)", "every slot") in SS:
    L.append(verdict(f"*The suspension at the first failure, with the way back as built, costs the careful population a part of its lifetime*: shown if read 23's slot ends below world 3's by two standard errors of record, by seed; refuted if it is within one standard error of it, or above. Cell − world 3 is {dl23[0]:+.0f} ± {dl23[1]:.0f} ({dl23[0] / dl23[1]:.1f} SE).", dl23[0] <= -2 * dl23[1], dl23[0] >= -dl23[1]))
if P25 and W25:
    dd, l25, l18 = W25["leak"]; L.append(verdict(f"*When every member misses the same deliveries, the buyers get several times what read 18 has*: shown if the leak is at least twice read 18's at the point value and above it by two standard errors, by seed; refuted if it is within two standard errors of read 18's. The leak is {l25:.1f} against read 18's {l18:.1f} ({l25 / l18:.2f} times), above it by {dd[0]:+.1f} ± {dd[1]:.1f} by seed ({dd[0] / dd[1]:.1f} SE).", l25 >= 2 * l18 and dd[0] >= 2 * dd[1], abs(dd[0]) < 2 * dd[1]))
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("wrote", sys.argv[1], len(L), "lines;", n_met, "of", len(CHK), "met")
