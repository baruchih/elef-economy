"""Addendum 20 (November 17, 2026; notes §118): from the record — Z4.1 (what a review earns beside what its care costs, by seat, and the share of a slot's income in good
standing its reviews bring), Z4.2 (how much of the work in front of a member is bad; the planted share of its first reviews by kind; Z3.1's relation as the engine counts),
Z3.1–Z3.6 confirmed or replaced — and the two reads without training in world 3's cell (a19/launch.sh at 906fc5ac4: r18 conduct M at 0.1 on every slot, r19 conduct M at 0.2
on 1 slot in 4), read as reads 9 and 15 were (a18_read.py's helpers copied), with the expectations stated before the run and the refutations or showings.
Usage: a19_read.py OUT.md [A19_DIR A18_DIR]"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D18 = sys.argv[3] if len(sys.argv) > 3 else f"{R}/a18"; D19 = sys.argv[2] if len(sys.argv) > 2 else f"{R}/a19"
T = 1000; RES = 0.8; E_CARE = 0.05
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
        c0 = C[int(e["seed"])]; Sc = [v for v in json.loads(c0["learner_slots_json"]).values() if filt(v)]
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
HDR_G = ["| world / read | conduct's slots: claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** | careful group − all-careful; FA; leak ‰; overhead (all-careful) |", "|---|---|---|---|---|"]
SEATS = ("initial", "resumed", "audit", "third", "appeal", "dispute")
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
    d["susp"] = g("suspensions"); d["aud"] = g("audits_done"); d["pfails"] = sum(len(v.get("pfail_ticks", [])) for v in V) / n
    d["pw_member"] = sum(sum(n_ for k, n_ in v.items() if k.startswith("pw_member_")) for v in V) / n; d["pw_probation"] = sum(sum(n_ for k, n_ in v.items() if k.startswith("pw_probation_")) for v in V) / n
    for st in ("member", "probation"):
        for kd in ("real_bad", "real_good", "plant_bad", "plant_good"): d[f"rvi_{st}_{kd}"] = g(f"rvi_{st}_{kd}")
        d[f"fai_{st}"] = g(f"fai_{st}")
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
        V = list(json.loads(c["learner_slots_json"]).values())
        if V and any("rv_member" in v for v in V): out.append(dict(seed=s_, **counts(V)))
    return out
def m(rows, k): return mse([r[k] for r in rows])
def fmt(rows, k, d=1): a, b = m(rows, k); return f"{a:.{d}f} ± {b:.{d}f}"
def level_rows(E, C):
    out = []
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"] or not any("rv_member" in v for v in g["claim"]): continue
        s_, c = counts(g["claim"]), counts(g["care"]); S_, Cc = stats_(g["claim"]), stats_(g["care"])
        call = s_["care_m"] + s_["claimed_m"]
        if not call or not S_["good"] or not Cc["good"]: continue
        spared = S_["ben"]
        out.append(dict(seed=int(e["seed"]), x_rec=(Cc["life"] - S_["life"] + spared) / call, x_res=(Cc["lres"] - S_["lres"] + spared) / call, x_lfl=(Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"]) / call,
                        loss_rec=Cc["life"] - S_["life"], loss_res=Cc["lres"] - S_["lres"], loss_lfl=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - spared, spared=spared, call=call, rvm=s_["rv_member"], cm=s_["claims_m"], share=(s_["claims_m"] / s_["rv_member"] if s_["rv_member"] else np.nan)))
    return out
def level_line(rows, q=None, ident=None):
    rm = tuple(ratio_se(col(rows, f"loss_{k}") + col(rows, "spared"), col(rows, "call")) for k in ("rec", "res", "lfl")); mr = tuple(mse(col(rows, f"x_{k}")) for k in ("rec", "res", "lfl"))
    return rm, mr
# ------------------------------------------------------------------ the record
CW3 = load([f"{D19}/rerun/cw3-s21-70", f"{D19}/rerun/cw3-s71-120"], "careful")[1]
CW3_OLD = load([f"{D18}/rerun/cw3-s21-70", f"{D18}/rerun/cw3-s71-120"], "careful")[1]
R9 = load([f"{D19}/rerun/r9-s21-70", f"{D19}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0]
R9_OLD = load([f"{D18}/rerun/r9-s21-70", f"{D18}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0]
R15 = load([f"{D18}/r15/s21-70", f"{D18}/r15/s71-120"], "mix:doseM0.5:0.25")[0]
R18 = load([f"{D19}/r18/s{a}-{b}" for a, b in ((21, 45), (46, 70), (71, 95), (96, 120))], "mix:doseM0.1:1.0")[0]
R19 = load([f"{D19}/r19/s{a}-{b}" for a, b in ((21, 45), (46, 70), (71, 95), (96, 120))], "mix:doseM0.2:0.25")[0]
L = ["# Addendum 20: the record's readings and the two reads without training (November 17, 2026; a19/launch.sh at 906fc5ac4)\n"]
# reproduction
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
    return f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") + "."
L += ["\n## 0. The reruns against the record\n", "The all-careful of world 3 and read 9 on seeds 21–120 run again whole at 906fc5ac4 for the readings the record does not carry, checked against a18/rerun (f16e1ffee) on every row column and every per-slot key the record carries:\n",
      repro(list(CW3.values()), list(CW3_OLD.values()), "world 3's all-careful (cw3)"), repro(R9, R9_OLD, "read 9 (conduct M at 0.1 on 1 slot in 4)")]
# ------------------------------------------------------------------ Z4.1
SEAT_N = {"initial": "the first review", "resumed": "the resumed seat", "audit": "the audit seat", "third": "the third seat", "appeal": "an appeal panel", "dispute": "a dispute panel"}
CLS = ("fee", "emission", "uplift", "reimb", "bond", "courtfee")
def seat_table(Cd, st, title):
    rows = []
    for s_ in SEATS:
        per = {k: [] for k in ("n",) + CLS + ("care",)}
        for c in Cd.values():
            V = list(json.loads(c["learner_slots_json"]).values()); n = sum(v.get(f"rvs_{st}_{s_}", 0) for v in V)
            if n == 0: continue
            per["n"].append(n / len(V))
            for k in CLS: per[k].append(sum(v.get(f"rf_{st}_{s_}_{k}", 0.0) for v in V) / n)
            per["care"].append(sum(v.get(f"care_{st}_{s_}", 0.0) + v.get(f"claimed_{st}_{s_}", 0.0) for v in V) / n)
        if not per["n"]: continue
        fee, em, up, re_, bo, cf, ca = (mse(per[k]) for k in ("fee", "emission", "uplift", "reimb", "bond", "courtfee", "care"))
        net = mse(np.array(per["fee"]) + np.array(per["emission"]) + np.array(per["uplift"]) + np.array(per["reimb"]) + np.array(per["bond"]) + np.array(per["courtfee"]) - np.array(per["care"]))
        beyond = mse(np.array(per["fee"]) + np.array(per["emission"]) + np.array(per["uplift"]))
        rows.append(f"| {SEAT_N[s_]} | {pm(mse(per['n']))} | **{pm(fee, 2)}** | {pm(em, 2)} | {pm(up, 3)} | {pm(re_, 2)} | **{pm(ca, 2)}** | {pm((-bo[0], bo[1]), 2)} | {pm(cf, 3)} | **{pm(beyond, 2)}** | **{pm(net, 2)}** |")
    return [f"\n**{title}**\n", "| seat | reviews a slot in a life | **the fee that vests** | the emission share | the uplift | the care reimbursed | **the care spent** | the bond forfeited (lost) | a court fee | **the review's income beyond its care (fee + emission + uplift)** | **net of everything (fee + emission + uplift + reimbursed + court fee − care − bond)** |", "|---|---|---|---|---|---|---|---|---|---|---|"] + rows
L += ["\n## Z4.1. What a review earns beside what its care costs — the all-careful population of world 3's cell, seeds 21–120\n",
      "Every figure real at the tick of the event (the index then), a mean over the seeds of the seed's figure (the seed's slots' flows over their reviews) with its standard error over the seeds. The flows are tallied by the standing and seat of the review they belong to (a fee vests at the case's settlement, often ticks after the review; it is credited to that review). The care is the cost the review bought (uniform on {2, 3} nominal at every seat alike); it is reimbursed from the case's allowance within the cap in the same call, so a review's *net* cost of care is the difference between the two columns (an underfunded review, or one past the cap, pays the rest). The bond is what the slot lost at that seat when its verdict was overturned. The emission share is the dial's emission paid to the case's reviewers by fee weight at settlement; the uplift the duty fund's payout (next to nothing in this cell).\n"]
L += seat_table(CW3, "member", "As a member, by seat") + seat_table(CW3, "probation", "On probation (the first review alone, by the rule)")
# income in good standing split
def income_split(Cd, filt=lambda v: True, label=""):
    keys = ("delivery", "effort", "guarantee", "guarantee_in", "fee", "emission", "uplift", "reimb", "care", "bond", "courtfee", "float", "loan", "departure", "pots", "other_in", "other_out")
    acc = {k: [] for k in keys + ("income_good", "ticks_good", "n")}
    for c in Cd.values():
        V = [v for v in json.loads(c["learner_slots_json"]).values() if filt(v)]
        if not V: continue
        n = len(V); acc["n"].append(n)
        for k in keys: acc[k].append(sum(v.get(f"ev_member_{k}", 0.0) for v in V) / n)
        acc["income_good"].append(sum(v["income_good"] for v in V) / n); acc["ticks_good"].append(sum(v["ticks_good"] for v in V) / n)
    A = {k: np.array(v, float) for k, v in acc.items()}
    reviews = A["fee"] + A["emission"] + A["uplift"] + A["reimb"] + A["care"] + A["bond"] + A["courtfee"]
    work = A["delivery"] + A["effort"] + A["guarantee"] + A["guarantee_in"]
    other = A["float"] + A["loan"] + A["pots"] + A["other_in"] + A["other_out"]
    flows = reviews + work + other; resid = A["income_good"] - flows
    return [f"| {label} | {np.mean(A['n']):.1f} | {pm(mse(A['ticks_good']), 0)} | **{pm(mse(A['income_good']), 0)}** | **{pm(mse(reviews), 0)}** ({pm(ratio_se(reviews, A['income_good']), 2)}) | {pm(mse(A['fee']), 0)} + {pm(mse(A['emission']), 0)} + {pm(mse(A['uplift']), 1)} + {pm(mse(A['reimb']), 0)} − {pm(mse(-A['care']), 0)} − {pm(mse(-A['bond']), 0)} + {pm(mse(A['courtfee']), 1)} | **{pm(mse(work), 0)}** ({pm(ratio_se(work, A['income_good']), 2)}) | {pm(mse(A['delivery']), 0)} − {pm(mse(-A['effort']), 0)} − {pm(mse(-A['guarantee']), 0)} | {pm(mse(other), 0)} (the genesis payout and the rest {pm(mse(A['other_in'] + A['other_out'] + A['pots']), 0)}, the arrival float {pm(mse(A['float']), 0)}, its loan's repayments {pm(mse(A['loan']), 0)}) | {pm(mse(-A['departure']), 0)} | {pm(mse(resid), 0)} |"]
L += ["\n**The share of a slot's income in good standing that its reviews bring.** A slot's income in good standing is K3's measure: the change in its real wealth over the ticks it was a member. Here it is split by the events on its wallet in those ticks, each real at its tick: the reviews' part (the fees, the emission share, the uplift, the care reimbursed, a court fee returned, less the care bought and the bonds forfeited), the work's part (the delivery price vesting, less the effort burned and the guarantees forfeited), and the rest (the genesis payout of 50 a founder, the arrival float and its loan's repayments, the wallet out at a departure — a departed slot's wallet leaves as `departure` — K3's measure stops at the tick before, so the wallet out is shown apart and is not among the flows; the residual column is K3 less the flows: the revaluation of what the slot held by the index's step).\n",
      "| slots | slots a seed | good ticks a slot | **income in good standing a slot (K3)** | **the reviews' part** (share) | fee + emission + uplift + reimbursed − care − bonds + court fees | **the work's part** (share) | delivery − effort − guarantees | the rest | the wallet out at a departure (apart) | residual (K3 − the flows: the revaluation of wealth held) |", "|---|---|---|---|---|---|---|---|---|---|---|"]
L += income_split(CW3, label="every slot") + income_split(CW3, lambda v: v["t_in"] == 0, "the founders") + income_split(CW3, lambda v: v["t_in"] > 0, "the arrivals") + income_split(CW3, lambda v: v["alive"] == 1, "the slots alive at the end (no wallet out)")
# ------------------------------------------------------------------ Z4.2
def kind_rows(Cd, st, group=None):
    rows = []
    for key, c in sorted(Cd.items()):
        V = list(json.loads(c["learner_slots_json"]).values()) if group is None else groups(c)[group]
        g = lambda k: sum(v.get(k, 0) for v in V)
        rb, rg, pb, pg, fai = g(f"rvi_{st}_real_bad"), g(f"rvi_{st}_real_good"), g(f"rvi_{st}_plant_bad"), g(f"rvi_{st}_plant_good"), g(f"fai_{st}")
        tot = rb + rg + pb + pg
        if tot == 0: continue
        rows.append(dict(seed=int(c["seed"]), n=len(V), rb=rb, rg=rg, pb=pb, pg=pg, fai=fai, tot=tot))
    return rows
def kind_line(label, rows):
    bad = ratio_se(col(rows, "rb"), col(rows, "rb") + col(rows, "rg")); pb = ratio_se(col(rows, "pb"), col(rows, "tot")); pg = ratio_se(col(rows, "pg"), col(rows, "tot")); pl = ratio_se(col(rows, "pb") + col(rows, "pg"), col(rows, "tot"))
    rate = ratio_se(col(rows, "fai"), col(rows, "rb")); per = mse(col(rows, "tot") / col(rows, "n")); pbs = mse(col(rows, "pb") / col(rows, "n")); rbs = mse(col(rows, "rb") / col(rows, "n"))
    return f"| {label} | {len(rows)} | {pm(per)} | {pm(rbs, 2)} | **{pm(bad, 3)}** | **{pm(pb, 3)}** ({pm(pbs, 2)} a slot) | {pm(pg, 3)} | {pm(pl, 3)} | **{pm(rate, 3)}** |", rate, bad, pb, pl
L += ["\n## Z4.2. How much of the work is bad — and Z3.1's relation as the engine counts\n",
      "Among a slot's first reviews (the initial seat; the resumed seat, a resubmission's, is apart), by standing: the share of the real tasks whose work is bad (the population's draw b = 0.2 at every root, the state's deliveries among them); the share of the first reviews that are planted, by kind (the dial's plants and the planted approvals: a planted approval's first seat is nobody's and is not among them); and the slot's wrong first approvals of real bad work over the real bad work it reviewed first — the careful's own error there (the coin at 1 − 0.95), and conduct M's, against Z3.1's q + (1 − q) ÷ 20. Ratios of the seeds' sums; errors by the delta method over the seeds.\n",
      "| population, standing | seeds | first reviews a slot | real bad first reviews a slot | **bad share of the real tasks reviewed first** | **planted bad share of the first reviews** | planted good share | planted share, both kinds | **wrong first approvals of real bad work over the real bad work reviewed first** |", "|---|---|---|---|---|---|---|---|---|"]
Z31 = {}
for label, Cd, st, g_ in (("all-careful, as a member", CW3, "member", None), ("all-careful, on probation", CW3, "probation", None), ("read 9's conduct M at 0.1, as a member", {int(e["seed"]): e for e in R9}, "member", "claim"), ("read 9's conduct, on probation (careful there)", {int(e["seed"]): e for e in R9}, "probation", "claim"), ("read 9's careful beside, as a member", {int(e["seed"]): e for e in R9}, "member", "care"),
                        ("read 19's conduct M at 0.2, as a member", {int(e["seed"]): e for e in R19}, "member", "claim"), ("read 15's conduct M at 0.5, as a member", {int(e["seed"]): e for e in R15}, "member", "claim"), ("read 18's population (M at 0.1 on every slot), as a member", {int(e["seed"]): e for e in R18}, "member", None)):
    rows = kind_rows(Cd, st, g_)
    if not rows: L.append(f"| {label} | (the record carries no first reviews by kind) | | | | | | | |"); continue
    line, rate, bad, pb, pl = kind_line(label, rows); L.append(line); Z31[label] = (rate, bad, pb, pl)
def z(label, i=0): return Z31.get(label, ((np.nan, np.nan),) * 4)[i]
K9, K19, K15, KC, KP = "read 9's conduct M at 0.1, as a member", "read 19's conduct M at 0.2, as a member", "read 15's conduct M at 0.5, as a member", "all-careful, as a member", "all-careful, on probation"
L += [f"\n- **The careful's error on real bad work at the first review** reads {pm(z(KC), 3)} in the all-careful (the coin's 0.050); conduct M at 0.1 reads {pm(z(K9), 3)} against Z3.1's 0.145, at 0.2 {pm(z(K19), 3)} against 0.24, at 0.5 {pm(z(K15), 3)} against 0.525. (A claim is an approval; so on real bad work a conduct at a dose of q approves q of what it claims and 0.05 of what it looks at — the relation as the engine counts, up to the coin.)",
      f"- **The work in front of a member at the first review**: {pm(z(KC, 1), 3)} of the real tasks are bad; the planted bad cases are {pm(z(KC, 2), 3)} of its first reviews and the planted cases of both kinds {pm(z(KC, 3), 3)}; on probation {pm(z(KP, 2), 3)} and {pm(z(KP, 3), 3)}."]
# ------------------------------------------------------------------ Z3
L += ["\n## Z3. The reviewer's arithmetic, confirmed or replaced\n"]
# Z3.2
def tstar(rows): return tuple(temp(rows, k, d)[0] for k, d in (("rec", "ben"), ("res", "ben"), ("lfl", "den")))
ROWS9, ROWS15, ROWS19 = rows_of(R9, CW3), rows_of(R15, CW3_OLD), (rows_of(R19, CW3) if R19 else [])
T9, T15 = tstar(ROWS9), tstar(ROWS15); T19 = tstar(ROWS19) if ROWS19 else (np.nan,) * 3
L += ["**Z3.2 — where a model that spares nine tenths stops paying.** By the identity x = q · T*, level where q = 0.9 / T*. The level temptations T* (1 + the gap over the benefit, a ratio of the seeds' means):\n",
      "| read | T*: of record / with the reservation / like for like | q at which x = 0.9 | in misses in all, q + (1 − q) ÷ 20 |", "|---|---|---|---|"]
for nm, Tt in (("read 9 (M at 0.1)", T9), ("read 15 (M at 0.5)", T15), ("read 19 (M at 0.2)", T19)):
    if np.isnan(Tt[0]): continue
    q = tuple(0.9 / t for t in Tt); L.append(f"| {nm} | {Tt[0]:.2f} / {Tt[1]:.2f} / {Tt[2]:.2f} | {q[0]:.3f} / {q[1]:.3f} / {q[2]:.3f} | {q[0] + (1 - q[0]) * E_CARE:.3f} / {q[1] + (1 - q[1]) * E_CARE:.3f} / {q[2] + (1 - q[2]) * E_CARE:.3f} |")
L.append("\nThe reviewer's 0.14 / 0.17 / 0.24 (0.18 / 0.22 / 0.28 in misses in all) are these to the hundredth from reads 9 and 15. T* is not one number across doses (6.2 at 0.1, 6.6 at 0.5 of record), so the line is drawn between reads; read 19 at 0.2 sits on it — section 6.\n")
# Z3.3
def gain_rows(E, C, spare=0.9):
    out = []
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"] or int(e["seed"]) not in C: continue
        s_, c = counts(g["claim"]), counts(g["care"]); S_, Cc = stats_(g["claim"]), stats_(g["care"]); call = s_["care_m"] + s_["claimed_m"]
        out.append(dict(seed=int(e["seed"]), call=call, spared=S_["ben"], gap_rec=Cc["life"] - S_["life"], gap_res=Cc["lres"] - S_["lres"], gap_lfl=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"],
                        gain_rec=spare * call - (Cc["life"] - S_["life"]) - S_["ben"], gain_res=spare * call - (Cc["lres"] - S_["lres"]) - S_["ben"], gain_lfl=spare * call - (Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"]),
                        rvm=s_["rv_member"], cpr=call / s_["rv_member"] if s_["rv_member"] else np.nan, share=s_["claims_m"] / s_["rv_member"] if s_["rv_member"] else np.nan))
    return out
G9 = gain_rows(R9, CW3)
L += ["**Z3.3 — what the cheaper model gains at a dose of 0.1.** Measured on read 9's conduct slots (the care on all their reviews as a member is tallied: the care spent plus the cost claimed, real), by seed, mean ± SE over the seeds; the gain is 0.9 of that care, less the conduct's gap against the careful beside it, less what its claims already spared it (the benefit).\n",
      "| | the care on a life's reviews as a member | … a review | the claims' share of the member reviews | what the claims spared | **the gap of record / with the reservation / like for like** | **the cheaper model's gain: of record / with the reservation / like for like** |", "|---|---|---|---|---|---|---|",
      f"| read 9, measured | {pm(mse(col(G9, 'call')), 0)} | {pm(mse(col(G9, 'cpr')), 2)} | {pm(mse(col(G9, 'share')), 3)} | {pm(mse(col(G9, 'spared')))} | {pm(mse(col(G9, 'gap_rec')), 0)} / {pm(mse(col(G9, 'gap_res')), 0)} / {pm(mse(col(G9, 'gap_lfl')), 0)} | **{pm(mse(col(G9, 'gain_rec')), 0)} / {pm(mse(col(G9, 'gain_res')), 0)} / {pm(mse(col(G9, 'gain_lfl')), 0)}** |",
      "| the reviewer (R) | 214 | 2.8 | 0.099 | 21.2 | 109 / 90 / 63 | 62 ± 24 / about 80 / about 110 |"]
# Z3.4
def fail_stats(Cd, group=None):
    rows = []
    for key, c in sorted(Cd.items()):
        V = list(json.loads(c["learner_slots_json"]).values()) if group is None else groups(c)[group]
        if not V: continue
        d = counts(V); n = len(V)
        pl_m = d["plant_bad"] + d["plant_good"]; pl_p = d["rvi_probation_plant_bad"] + d["rvi_probation_plant_good"]
        rows.append(dict(seed=int(c["seed"]), pl_m=pl_m, pl_p=pl_p, plb_m=d["plant_bad"], plg_m=d["plant_good"], pw_m=d["pw_member"], pw_p=d["pw_probation"], pfails=d["pfails"], reach=d["reach_fail"], reach_m=sum(1 for v in V if any(k.startswith("pw_member_") for k in v)) / n))
    return rows
L += ["\n**Z3.4 — why the record does not stop that member.** Measured: the planted cases a slot meets in a life (as a member, every seat; on probation, the first review), its wrong planted verdicts (by the standing of the review), and the share of slots that reach one; the Poisson share 1 − e^(−λ) beside, λ the measured mean.\n",
      "| slots | planted cases a slot as a member (bad / good) | … on probation | **wrong planted verdicts a slot: as a member / on probation / in all** | **share reaching a wrong verdict (any standing) / as a member** | 1 − e^(−λ) on the member count |", "|---|---|---|---|---|---|"]
for label, rows in (("all-careful (world 3)", fail_stats(CW3)), ("read 9's conduct M at 0.1", fail_stats({int(e["seed"]): e for e in R9}, "claim")), ("read 9's careful beside", fail_stats({int(e["seed"]): e for e in R9}, "care")), ("read 19's conduct M at 0.2", fail_stats({int(e["seed"]): e for e in R19}, "claim") if R19 else []), ("read 18's population", fail_stats({int(e["seed"]): e for e in R18}) if R18 else [])):
    if not rows: continue
    lam = m(rows, "pw_m")[0]
    L.append(f"| {label} | {fmt(rows, 'pl_m')} ({m(rows, 'plb_m')[0]:.1f} / {m(rows, 'plg_m')[0]:.1f}) | {fmt(rows, 'pl_p')} | **{fmt(rows, 'pw_m', 2)} / {fmt(rows, 'pw_p', 2)} / {fmt(rows, 'pfails', 2)}** | **{m(rows, 'reach')[0]:.2f} / {m(rows, 'reach_m')[0]:.2f}** | {1 - np.exp(-lam):.2f} |")
L.append("\nThe reviewer's 1.3 and 0.7 wrong planted verdicts in a life and 72 and 49 in 100 reaching one are the arithmetic of section 4's counts; the measured figures are the row above (the conduct's wrong verdicts come at every seat it holds as a member — the audit seat's and the panels' included — and a careful slot's at its own one in twenty on each kind; the shares reaching one count the probation's wrong verdicts too, which is why they run above the Poisson figure on the member count).\n")
# Z3.5
L += ["**Z3.5 — between the two thresholds a further failure costs about nothing.** The reviewer's figures are quotients of the read's means: read 17's gap of record from the first failure on, 26 ± 21, over its further failures beyond the careful's, 1.68 − 0.49 = 1.19, is 22 ± 18 a failure; read 13's 15 ± 15 over 0.87 − 0.45 = 0.42 is 36 ± 36. Confirmed as arithmetic. What they are not: a measured cost of one further failure. Within a read the failed slots' further failures and their time in place go together as their claims do (§117's Y3.2: a slot that stays longer fails more and earns more), so a fit of the gap on the further failures within a read reads survival, as the fit on the claims did; and the quotient divides a gap that carries the suspensions and the departures too. The 102 ± 14 where the seats are held (§115's item 6) was read the same way, from F at 0.3's gap over its further failures, and stands as that.\n"]
# Z3.6
def spells(Cd, kind):
    rows = []
    for c in Cd.values():
        for v in json.loads(c["learner_slots_json"]).values():
            for sp in v.get("spells", []):
                if sp["kind"] == kind: rows.append(dict(sp, slot_alive=v["alive"], t_in=v["t_in"]))
    return rows
def spell_table(label, S):
    n = len(S)
    if not n: return [f"| {label} | 0 | | | | | |"]
    ends = {k: sum(1 for s in S if s["end"] == k) for k in ("member", "suspended", "departed", "open")}
    adm = [s for s in S if s["end"] == "member"]; sus = [s for s in S if s["end"] == "suspended"]
    return [f"| {label} | {n} | {ends['member'] / n:.2f} / {ends['suspended'] / n:.2f} / {ends['departed'] / n:.2f} / {ends['open'] / n:.2f} | **{pm(mse([s['ticks'] for s in adm]), 0)} ticks, {pm(mse([s['reviews'] for s in adm]))} reviews** (medians {np.median([s['ticks'] for s in adm]) if adm else np.nan:.0f}, {np.median([s['reviews'] for s in adm]) if adm else np.nan:.0f}) | {pm(mse([s['ticks'] for s in sus]), 0)} ticks, {pm(mse([s['reviews'] for s in sus]))} reviews | {pm(mse([s['ticks'] for s in S]), 0)} ticks, {pm(mse([s['reviews'] for s in S]))} reviews | {pm(mse([s['t0'] for s in S]), 0)} |"]
SA, SR = spells(CW3, "arrival"), spells(CW3, "return")
n_arr = sum(1 for c in CW3.values() for v in json.loads(c["learner_slots_json"]).values() if v["t_in"] > 0)
n_slots = sum(len(json.loads(c["learner_slots_json"])) for c in CW3.values())
adm_first = [s for s in SA if s["end"] == "member"]
# the probation's planted rate
PR = kind_rows(CW3, "probation"); pb_rate = ratio_se(col(PR, "pb"), col(PR, "tot")); pl_rate = ratio_se(col(PR, "pb") + col(PR, "pg"), col(PR, "tot"))
rv_p = mse([np.mean([v.get("rv_probation", 0) for v in json.loads(c["learner_slots_json"]).values() if v["t_in"] > 0]) for c in CW3.values()])
L += ["**Z3.6 — the door as built is slow.** Measured on the all-careful of world 3's cell, seeds 21–120: every spell on probation (an arrival's, from its arrival; the way back, from the end of a suspension's hundred ticks), how it ended (admitted or readmitted as a member; suspended — a wrong planted verdict on probation; the slot departed on it; open at the run's end), and the ticks and reviews it took. A slot that is suspended on probation serves the hundred ticks again and begins a new spell.\n",
      "| spells | n | ended: member / suspended / departed / open | **to membership: ticks, reviews** | to a suspension: ticks, reviews | every spell: ticks, reviews | began at tick |", "|---|---|---|---|---|---|---|"]
L += spell_table("an arrival's probation", SA) + spell_table("the way back from a suspension", SR)
ARR = [v for c in CW3.values() for v in json.loads(c["learner_slots_json"]).values() if v["t_in"] > 0]; ADM = [v for v in ARR if "adm_ticks" in v]
L += [f"\n- **{n_arr} arrivals in {len(CW3)} seeds ({n_arr / len(CW3):.1f} a seed, {n_slots / len(CW3):.1f} slots a seed)**: {len(ADM) / max(1, n_arr):.2f} are admitted in the run, {sum(1 for v in ARR if any(sp['end'] == 'suspended' for sp in v.get('spells', []))) / max(1, n_arr):.2f} are suspended on probation at least once; **from the arrival to the admission, the whole road (the record's snapshot at admission, suspensions included): {pm(mse([v['adm_ticks'] for v in ADM]), 0)} ticks and {pm(mse([v['adm_reviews'] for v in ADM]))} reviews** (medians {np.median([v['adm_ticks'] for v in ADM]) if ADM else np.nan:.0f}, {np.median([v['adm_reviews'] for v in ADM]) if ADM else np.nan:.0f}); the reviews on probation {pm(rv_p)} an arrival in a life (the reviewer's 55).",
      f"- **The planted cases on probation come at {pm(pl_rate, 3)} of a probationer's first reviews, the bad ones at {pm(pb_rate, 3)}** — the door admits an arrival on four *bad* planted cases adjudicated with no failure among them (the engine's `_check_record`: `len(plant_bad) ≥ n_min` and the record passing θ_duty; a good plant counts for the readmission after a suspension, `since_susp ≥ n_min` of either kind, not for the admission), so an arrival's probation is about 4 ÷ {pb_rate[0]:.3f} ≈ {4 / pb_rate[0]:.0f} first reviews long where no failure restarts it. The reviewer's 'about one first review in ten' is the planted share of both kinds on a member's first reviews; on probation it is the bad plants' share alone that opens the door.",
      "- The reviewer's 520 ticks and 55 reviews are replaced by the measured spells above."]
# ------------------------------------------------------------------ read 18
L += ["\n## Read 18. Conduct M at 0.1 on every slot — world 3's cell, seeds 21–120, against the all-careful population of the same seeds\n",
      "Every slot of the world follows the conduct (the mix wrapper's share at 1.0; the arrivals included — careful on probation, a claim at one review in ten as a member). Each row a seed: the all-careful's slot (the mean over its slots) less the population's slot; the three lifetimes, with the population's benefit as the temptation's denominator; the level saving as the ratio of the seeds' means (the all-careful's lifetime less the population's plus what the claims spared, over the care on the population's reviews as a member) with the mean of the seeds' ratios beside; like for like is the all-careful's income in good standing less the population's rate over the all-careful's good ticks — against another world's slots, reported and not read, as before.\n"]
def pop_rows(E, C):
    out = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in C: continue
        V = list(json.loads(e["learner_slots_json"]).values()); Vc = list(json.loads(C[s_]["learner_slots_json"]).values())
        S_, Cc = stats_(V), stats_(Vc); d, dc = counts(V), counts(Vc); call = d["care_m"] + d["claimed_m"]
        out.append(dict(seed=s_, n=len(V), nc=len(Vc), rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], ben=S_["ben"], den=S_["brate"] * Cc["good"], claims=S_["claims"], call=call, spared=S_["ben"],
                        x_rec=(Cc["life"] - S_["life"] + S_["ben"]) / call if call else np.nan, x_res=(Cc["lres"] - S_["lres"] + S_["ben"]) / call if call else np.nan, x_lfl=(Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"]) / call if call else np.nan,
                        loss_rec=Cc["life"] - S_["life"], loss_res=Cc["lres"] - S_["lres"], loss_lfl=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"],
                        life=S_["life"], lifec=Cc["life"], lres=S_["lres"], lresc=Cc["lres"], ig=S_["ig"], igc=Cc["ig"], good=S_["good"], goodc=Cc["good"], susp=S_["susp"], suspc=Cc["susp"], aud=S_["aud"], audc=Cc["aud"],
                        fa=f(e, "false_approvals"), fa0=f(C[s_], "false_approvals"), leak=1000 * f(e, "leak_bad"), leak0=1000 * f(C[s_], "leak_bad"), oh=f(e, "sys_overhead_per_vested"), oh0=f(C[s_], "sys_overhead_per_vested"),
                        dep=f(e, "departures"), dep0=f(C[s_], "departures"), arr=f(e, "arrivals"), arr0=f(C[s_], "arrivals"), cot=f(e, "cost_of_truth"), cot0=f(C[s_], "cost_of_truth"), Pt=f(e, "P_t"), Pt0=f(C[s_], "P_t")))
    return out
P18 = pop_rows(R18, CW3) if R18 else []
if P18:
    a, b, c = mse(col(P18, "rec")), mse(col(P18, "res")), mse(col(P18, "lfl")); ta, tb, tc = temp(P18, "rec", "ben"), temp(P18, "res", "ben"), temp(P18, "lfl", "den")
    RM18 = tuple(ratio_se(col(P18, f"loss_{k}") + col(P18, "spared"), col(P18, "call")) for k in ("rec", "res", "lfl")); MR18 = tuple(mse(col(P18, f"x_{k}")) for k in ("rec", "res", "lfl")); rm, mr = RM18, MR18
    L += ["| read | seeds | slots a seed: population / all-careful | **all-careful − population, of record** (SE from nothing) | temptation | **with the reservation** | temptation | like for like (reported) | temptation | the population's slot: of record / with the reservation / in good standing (the all-careful's) |", "|---|---|---|---|---|---|---|---|---|---|",
          f"| 18: M at 0.1 on every slot | {len(P18)} | {np.mean(col(P18, 'n')):.1f} / {np.mean(col(P18, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {ta[0]:.1f} ± {ta[1]:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f}) | {tb[0]:.1f} ± {tb[1]:.1f} | {c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f}) | {tc[0]:.1f} ± {tc[1]:.1f} | {np.mean(col(P18, 'life')):.0f} / {np.mean(col(P18, 'lres')):.0f} / {np.mean(col(P18, 'ig')):.0f} ({np.mean(col(P18, 'lifec')):.0f} / {np.mean(col(P18, 'lresc')):.0f} / {np.mean(col(P18, 'igc')):.0f}) |",
          "\n| | what the claims spared a slot | the care on all its reviews as a member (spent + claimed) | claims a slot | **the population's level saving, the ratio of the seeds' means: of record / with the reservation / like for like** | the mean of the seeds' ratios | suspensions a slot (the all-careful's) | audit seats a slot (the all-careful's) | good ticks a slot (the all-careful's) |", "|---|---|---|---|---|---|---|---|---|",
          f"| read 18 | {pm(mse(col(P18, 'spared')))} | {pm(mse(col(P18, 'call')), 0)} | {pm(mse(col(P18, 'claims')))} | **{pm(rm[0], 2)} / {pm(rm[1], 2)} / {pm(rm[2], 2)}** | {pm(mr[0], 2)} / {pm(mr[1], 2)} / {pm(mr[2], 2)} | {np.mean(col(P18, 'susp')):.2f} ({np.mean(col(P18, 'suspc')):.2f}) | {np.mean(col(P18, 'aud')):.1f} ({np.mean(col(P18, 'audc')):.1f}) | {np.mean(col(P18, 'good')):.0f} ({np.mean(col(P18, 'goodc')):.0f}) |"]
    L += ["\n**The world's side, paired by seed** (the population's less the all-careful's; the standing false approvals a run, the leak per thousand bad deliveries, the system overhead a vested task; with the departures, the arrivals, the cost of truth and P_t):\n",
          "| measure | the population | the all-careful | **population − all-careful** (SE from nothing) |", "|---|---|---|---|"]
    for k, k0, nm, d in (("fa", "fa0", "standing false approvals a run", 1), ("leak", "leak0", "the leak, ‰ of bad deliveries", 1), ("oh", "oh0", "the system overhead a vested task", 2), ("dep", "dep0", "departures a run", 1), ("arr", "arr0", "arrivals a run", 1), ("cot", "cot0", "the cost of truth a run", 0), ("Pt", "Pt0", "P_t at the end", 2)):
        dd = mse(col(P18, k) - col(P18, k0)); L.append(f"| {nm} | {np.mean(col(P18, k)):.{d}f} | {np.mean(col(P18, k0)):.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** ({dd[0] / dd[1]:.1f}) |")
    C18 = count_rows_all({int(e["seed"]): e for e in R18}); CC = count_rows_all(CW3)
    L += ["\n**W3's three counts for the population, with the all-careful's beside** (a mean a slot):\n",
          "| count | read 18's population | the all-careful |", "|---|---|---|"]
    for nm, k, d in (("reviews as a member in a life", "rv_member", 1), ("… at the first review", "initial", 1), ("… at the audit seat", "audit", 1), ("… at the third seat / an appeal panel / a dispute panel", None, 1), ("planted cases among them, bad / good", None, 1), ("reviews on probation", "rv_probation", 1), ("claims as a member", "claims_m", 1),
                     ("reviews of real tasks as a member before the earned seats are first lost (every slot, censored)", "pre_fail", 1), ("… over the slots that reach a failure", "pre_fail_r", 1), ("slots that reach a wrong planted verdict, share", "reach_fail", 2), ("slots suspended at least once, share", "reach_susp", 2), ("reviews as a member before the first suspension, over the slots suspended (of real tasks)", None, 1),
                     ("wrong first approvals of real bad work in a life", "fa", 2), ("… of which stay paid / are overturned / still open", None, 2), ("wrong planted verdicts a slot, in all", "pfails", 2)):
        if k is not None: L.append(f"| {nm} | {fmt(C18, k, d)} | {fmt(CC, k, d)} |")
        elif nm.startswith("… at the third"): L.append(f"| {nm} | {m(C18, 'third')[0]:.1f} / {m(C18, 'appeal')[0]:.1f} / {m(C18, 'dispute')[0]:.1f} | {m(CC, 'third')[0]:.1f} / {m(CC, 'appeal')[0]:.1f} / {m(CC, 'dispute')[0]:.1f} |")
        elif nm.startswith("planted"): L.append(f"| {nm} | {m(C18, 'plant_bad')[0]:.1f} / {m(C18, 'plant_good')[0]:.1f} | {m(CC, 'plant_bad')[0]:.1f} / {m(CC, 'plant_good')[0]:.1f} |")
        elif nm.startswith("reviews as a member before"): L.append(f"| {nm} | {m(C18, 'm_pre_susp_r')[0]:.1f} ({m(C18, 'pre_susp_r')[0]:.1f}) | {m(CC, 'm_pre_susp_r')[0]:.1f} ({m(CC, 'pre_susp_r')[0]:.1f}) |")
        else: L.append(f"| {nm} | {m(C18, 'fa_paid')[0]:.2f} / {m(C18, 'fa_ov')[0]:.2f} / {m(C18, 'fa_open')[0]:.2f} | {m(CC, 'fa_paid')[0]:.2f} / {m(CC, 'fa_ov')[0]:.2f} / {m(CC, 'fa_open')[0]:.2f} |")
    _cc = {r["seed"]: r for r in CC}; _p = [(r, _cc[r["seed"]]) for r in C18 if r["seed"] in _cc]
    fa_ratio = ratio_se([a["fa"] for a, b in _p], [b["fa"] for a, b in _p]); paid_ratio = ratio_se([a["fa_paid"] for a, b in _p], [b["fa_paid"] for a, b in _p])
    L.append(f"\nThe population's slot gives {fa_ratio[0]:.2f} ± {fa_ratio[1]:.2f} times the all-careful slot's wrong first approvals of real bad work, and {paid_ratio[0]:.2f} ± {paid_ratio[1]:.2f} times the ones that stay paid.")
# ------------------------------------------------------------------ read 19
L += ["\n## Read 19. Conduct M at 0.2 on 1 slot in 4 — world 3's cell, seeds 21–120, read as reads 9 and 15 were\n"] + HDR_L
LR = {}
for nm, rows in (("9: M at 0.1 (a18/rerun at 906fc5ac4)", ROWS9), ("**19: M at 0.2**", ROWS19), ("15: M at 0.5 (a18)", ROWS15)):
    if rows: L.append(lifetimes_row(nm, rows)); LR[nm] = rows
L += ["\n"] + HDR_G
for nm, rows in LR.items(): L.append(groups_row(nm, rows))
L += ["\n| read | seeds | **the level saving, the ratio of the seeds' means: of record / with the reservation / like for like** | the mean of the seeds' ratios | the identity's q · T* | claims as a member over member reviews | member reviews a slot; claims as a member |", "|---|---|---|---|---|---|---|"]
LV = {}
for nm, E, q in (("9: M at 0.1", R9, 0.1), ("**19: M at 0.2**", R19, 0.2), ("15: M at 0.5", R15, 0.5)):
    rows = level_rows(E, CW3 if E is not R15 else CW3_OLD)
    if not rows: continue
    rm, mr = level_line(rows); Tt = tstar(rows_of(E, CW3 if E is not R15 else CW3_OLD)); LV[nm] = (rm, mr, Tt)
    L.append(f"| {nm} | {len(rows)} | **{pm(rm[0], 2)} / {pm(rm[1], 2)} / {pm(rm[2], 2)}** | {pm(mr[0], 2)} / {pm(mr[1], 2)} / {pm(mr[2], 2)} | {q * Tt[0]:.2f} / {q * Tt[1]:.2f} / {q * Tt[2]:.2f} | {np.mean(col(rows, 'share')):.3f} | {np.mean(col(rows, 'rvm')):.1f}; {np.mean(col(rows, 'cm')):.1f} |")
C19 = count_rows(R19, "claim") if R19 else []; C19c = count_rows(R19, "care") if R19 else []; C9 = count_rows(R9, "claim"); C9c = count_rows(R9, "care")
if C19:
    L += ["\n**W3's three counts** (a mean a slot; read 9's beside):\n", "| count | read 19's conduct | the careful beside (read 19) | read 9's conduct | the careful beside (read 9) |", "|---|---|---|---|---|"]
    for nm, k, d in (("reviews as a member in a life", "rv_member", 1), ("… at the first review / the audit seat", None, 1), ("planted cases among them, bad / good", None, 1), ("reviews of real tasks as a member before the earned seats are first lost (every slot)", "pre_fail", 1), ("… over the slots that reach a failure", "pre_fail_r", 1), ("slots that reach a wrong planted verdict, share", "reach_fail", 2), ("slots suspended at least once, share", "reach_susp", 2),
                     ("reviews as a member before the first suspension, over the slots suspended (of real tasks)", None, 1), ("wrong first approvals of real bad work in a life", "fa", 2), ("… of which stay paid", "fa_paid", 2), ("wrong planted verdicts a slot, in all", "pfails", 2)):
        cells = []
        for rows in (C19, C19c, C9, C9c):
            if k is not None: cells.append(fmt(rows, k, d))
            elif nm.startswith("… at the first"): cells.append(f"{m(rows, 'initial')[0]:.1f} / {m(rows, 'audit')[0]:.1f}")
            elif nm.startswith("planted"): cells.append(f"{m(rows, 'plant_bad')[0]:.1f} / {m(rows, 'plant_good')[0]:.1f}")
            else: cells.append(f"{m(rows, 'm_pre_susp_r')[0]:.1f} ({m(rows, 'pre_susp_r')[0]:.1f})")
        L.append(f"| {nm} | " + " | ".join(cells) + " |")
    r19_fa = ratio_se(col(C19, "fa"), col(C19c, "fa")); L.append(f"\nRead 19's conduct slot gives {r19_fa[0]:.2f} ± {r19_fa[1]:.2f} times the careful beside's wrong first approvals of real bad work (read 9's 2.27 ± 0.11).")
# ------------------------------------------------------------------ expectations
L += ["\n## Against what was stated before the run\n"]
def chk(ok, text): L.append(f"- {'MET' if ok else 'MISSED'} — {text}")
if P18:
    gap = mse(col(P18, "rec")); chk(-10 <= gap[0] <= 55, f"read 18: at the point value the population's slot ends between 10 real ahead of the all-careful's and 55 behind, of record: the all-careful's less the population's {gap[0]:+.0f} ± {gap[1]:.0f}.")
    chk(RM18[0][0] < 0.4, f"read 18: its level saving under 0.4 on the lifetime of record: {RM18[0][0]:.2f} ± {RM18[0][1]:.2f} (the ratio of the seeds' means).")
    lk, lk0 = np.mean(col(P18, "leak")), np.mean(col(P18, "leak0")); chk(11 <= lk <= 18, f"read 18: the leak 11 to 18 in a thousand bad deliveries (the all-careful's 5): {lk:.1f} ({lk0:.1f}).")
    fa_, fa0_ = np.mean(col(P18, "fa")), np.mean(col(P18, "fa0")); chk(6.5 <= fa_ <= 9.5, f"read 18: the standing false approvals 6.5 to 9.5 a run (the all-careful's 2.5): {fa_:.1f} ({fa0_:.1f}).")
    oh_, oh0_ = np.mean(col(P18, "oh")), np.mean(col(P18, "oh0")); chk(12.2 <= oh_ <= 13.8, f"read 18: the overhead 12.2 to 13.8 a vested task (the all-careful's 11.9): {oh_:.2f} ({oh0_:.2f}).")
    fa18, paid18 = m(C18, "fa")[0], m(C18, "fa_paid")[0]; chk(1.3 <= fa18 <= 1.7, f"read 18: a slot gives 1.3 to 1.7 wrong first approvals of real bad work in a life: {fa18:.2f}."); chk(0.18 <= paid18 <= 0.35, f"read 18: 0.18 to 0.35 of them stay paid: {paid18:.2f}.")
    s18 = m(C18, "reach_susp")[0]; chk(0.12 <= s18 <= 0.20, f"read 18: between 12 and 20 in 100 of the slots suspended at least once: {100 * s18:.0f}.")
if ROWS19:
    a19 = mse(col(ROWS19, "rec")); b19 = mse(col(ROWS19, "res")); c19 = mse(col(ROWS19, "lfl"))
    chk(a19[0] > 0 and b19[0] > 0 and c19[0] > 0 and 150 <= a19[0] <= 300, f"read 19: behind on every lifetime, by 150 to 300 real of record: {a19[0]:+.0f} ± {a19[1]:.0f} / {b19[0]:+.0f} ± {b19[1]:.0f} / {c19[0]:+.0f} ± {c19[1]:.0f}.")
    rm19 = LV["**19: M at 0.2**"][0]; chk(1.0 <= rm19[0][0] <= 1.7, f"read 19: the level saving 1.0 to 1.7 of record: {rm19[0][0]:.2f} ± {rm19[0][1]:.2f}."); chk(0.85 <= rm19[1][0] <= 1.35, f"read 19: 0.85 to 1.35 with the reservation: {rm19[1][0]:.2f} ± {rm19[1][1]:.2f}."); chk(0.6 <= rm19[2][0] <= 0.95, f"read 19: 0.6 to 0.95 like for like: {rm19[2][0]:.2f} ± {rm19[2][1]:.2f}.")
    rv19 = m(C19, "rv_member")[0]; chk(63 <= rv19 <= 73, f"read 19: a conduct slot makes 63 to 73 reviews as a member in a life: {rv19:.1f}.")
    s19 = m(C19, "reach_susp")[0]; chk(0.14 <= s19 <= 0.24, f"read 19: between 14 and 24 in 100 of the conduct's slots suspended at least once: {100 * s19:.0f}.")
    chk(3.2 <= r19_fa[0] <= 4.3, f"read 19: a conduct slot gives 3.2 to 4.3 times a careful slot's wrong first approvals of real bad work: {r19_fa[0]:.2f} ± {r19_fa[1]:.2f}.")
L += ["\n**Refuted, or shown, each apart.**\n"]
if P18:
    x = RM18[0]; L.append(f"- *When every member takes the cheaper model at a dose of 0.1, the members gain*: shown if read 18's level saving for the population is under 0.9 at the point value on the lifetime of record; refuted if it is 0.9 or more. It is {x[0]:.2f} ± {x[1]:.2f}: **{'SHOWN' if x[0] < 0.9 else 'REFUTED'}**.")
    dl = mse(col(P18, "leak") - col(P18, "leak0")); L.append(f"- *And the buyers pay*: shown if read 18's leak is above the all-careful's by two standard errors, by seed; refuted if it is not above it at the point value. The leak less the all-careful's by seed is {dl[0]:+.1f} ± {dl[1]:.1f} ‰ ({dl[0] / dl[1]:.1f} SE): **{'SHOWN' if dl[0] > 2 * dl[1] else ('REFUTED' if dl[0] <= 0 else 'NEITHER')}**.")
if ROWS19:
    x = LV["**19: M at 0.2**"][0][0]; L.append(f"- *A model that spares nine tenths does not pay at a dose of 0.2*: refuted if read 19's level saving is under 0.9 at the point value on the lifetime of record; shown if it is above 0.9 by two standard errors. It is {x[0]:.2f} ± {x[1]:.2f} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9): **{'REFUTED' if x[0] < 0.9 else ('SHOWN' if x[0] - 0.9 > 2 * x[1] else 'NEITHER')}**.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("wrote", sys.argv[1], len(L), "lines")
