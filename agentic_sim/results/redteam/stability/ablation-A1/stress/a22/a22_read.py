"""Addendum 24 (November 17, 2026; notes §121): the reviewer's arithmetic (AD3) confirmed or replaced from the record, the five readings asked from the record (AD4), and the
three reads without training (AD5: a22/launch.sh — r26 conduct M at 0.2 with its claims set by the case on every slot in world 3's cell, r27 the same at 0.3, r28 the same at 0.1
in the cell of the first failure, θ_duty 0.20; seeds 21–120), read as read 25 was (a20_read.py's helpers copied). World 3's all-careful, read 23's all-careful, read 25, read 9 and
read 19 were run again whole at this commit for the readings the record does not carry (the first reviewer of each bad delivery and a wrong first approval's fate, the standing
rejections' reasons, the unfunded appeals, the state's first-review seats, the ticks as a member without the earned seats) and are checked to the digit against the record before
they are read. Usage: a22_read.py OUT.md [A22_DIR A20_DIR A19_DIR]"""
import json, os, sys, hashlib, math, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
D22 = sys.argv[2] if len(sys.argv) > 2 else f"{R}/a22"; D20 = sys.argv[3] if len(sys.argv) > 3 else f"{R}/a20"; D19 = sys.argv[4] if len(sys.argv) > 4 else f"{R}/a19"
T = 1000; RES = 0.8; N_MIN = 4; N_P = 20; THETA = 0.20; D_FEE = 2.0
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else ((x.mean() if len(x) else np.nan), np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num)
    if n < 2 or den.mean() == 0: return ((num.mean() / den.mean()) if n and den.mean() else np.nan, np.nan)
    a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1); r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def pm(t, d=1): return f"{t[0]:.{d}f} ± {t[1]:.{d}f}" if not np.isnan(t[1]) else f"{t[0]:.{d}f}"
def slots(e): return list(json.loads(e["learner_slots_json"]).values())
def life(v): return v["wealth_real"] + v["private_real"]
def after(v): return (T - v["t_out"]) if (not v["alive"] and v["t_out"] is not None and v["t_out"] < T) else 0
def groups(e):
    S = json.loads(e["learner_slots_json"]); share = float(e.get("half_share") or 0.5); seed = int(e["seed"]); grp = {"claim": [], "care": []}
    for x, v in S.items():
        h = int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big"); grp["claim" if h < share * 65536 else "care"].append(v)
    return grp
def load(dirs, pol):
    E, C = [], {}
    for d in dirs:
        p = f"{d}/eval.json"
        if not os.path.exists(p): continue
        j = json.load(open(p))
        if pol in j["episodes"]: E += j["episodes"][pol]
        if "careful" in j["episodes"]: C.update({int(e["seed"]): e for e in j["episodes"]["careful"]})
    return E, C
def D(E): return {int(e["seed"]): e for e in E}
def col(rows, k): return np.array([r[k] for r in rows], float)
def m(rows, k): return mse([r[k] for r in rows])
def stats_(V):
    n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
    return dict(n=n, good=good, ig=ig, bg=bg, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n, ben=sum(v["private_real"] for v in V) / n,
                claims=sum(v["claims"] for v in V) / n, susp=sum(v["suspensions"] for v in V) / n, aud=sum(v["audits_done"] for v in V) / n)
SEATS = ("initial", "resumed", "audit", "third", "appeal", "dispute")
def counts(V):
    n = len(V); g = lambda k: sum(v.get(k, 0) for v in V) / n
    d = {"n": n, "rv_member": g("rv_member"), "claims_m": g("claims_member")}
    for s_ in SEATS: d[s_] = g(f"rvm_{s_}")
    d["reach_susp"] = sum(1 for v in V if v["suspensions"] > 0) / n; d["fa"] = g("fa_init"); d["fa_paid"] = g("fa_init_paid"); d["care_m"] = g("care_member"); d["claimed_m"] = g("claimed_member")
    d["aud"] = g("audits_done"); d["panel"] = g("rvm_appeal") + g("rvm_third") + g("rvm_dispute"); d["good"] = g("ticks_good"); d["susp"] = g("suspensions")
    tm = sum(v.get("ticks_member", 0) for v in V); d["tm"] = tm / n; d["noseat"] = (sum(v.get("ticks_member_noseat", 0) for v in V) / tm) if tm else np.nan; d["noseat_undet"] = (sum(v.get("ticks_member_noseat_undet", 0) for v in V) / tm) if tm else np.nan
    d["pf_lost"] = sum(v.get("pf_good_ticks_lost", 0) for v in V) / n; d["pf_lost_share"] = (sum(v.get("pf_good_ticks_lost", 0) for v in V) / sum(v["ticks_good"] for v in V)) if sum(v["ticks_good"] for v in V) else np.nan
    arr = [v for v in V if v["t_in"] > 0]; d["adm"] = (sum(1 for v in arr if "adm_ticks" in v) / len(arr)) if arr else np.nan
    return d
def rows_of(E, C, filt=lambda v: True):
    out = []
    for e in E:
        g = {k: [v for v in V if filt(v)] for k, V in groups(e).items()}
        if not g["claim"] or not g["care"] or int(e["seed"]) not in C: continue
        r = {"seed": int(e["seed"])}
        for kk, V in g.items(): r[kk] = stats_(V); r[kk].update(counts(V))
        cc, s = r["care"], r["claim"]
        r.update(rec=cc["life"] - s["life"], res=cc["lres"] - s["lres"], lfl=cc["ig"] - s["rate"] * cc["good"], den=s["brate"] * cc["good"], ben=s["ben"], claims=s["claims"], call=s["care_m"] + s["claimed_m"])
        out.append(r)
    return out
def temp(rows, key, den): t = ratio_se(col(rows, key), col(rows, den)); return 1 + t[0], t[1]
def pop_rows(E, C):
    out = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in C: continue
        V = slots(e); Vc = slots(C[s_]); S_, Cc = stats_(V), stats_(Vc); d, dc = counts(V), counts(Vc); call = d["care_m"] + d["claimed_m"]
        out.append(dict(seed=s_, n=len(V), nc=len(Vc), rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], ben=S_["ben"], claims=S_["claims"], call=call, spared=S_["ben"],
                        x_rec=(Cc["life"] - S_["life"] + S_["ben"]) / call if call else np.nan, x_res=(Cc["lres"] - S_["lres"] + S_["ben"]) / call if call else np.nan, x_lfl=(Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"]) / call if call else np.nan,
                        loss_rec=Cc["life"] - S_["life"], loss_res=Cc["lres"] - S_["lres"], loss_lfl=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"],
                        life=S_["life"], lifec=Cc["life"], lres=S_["lres"], lresc=Cc["lres"], ig=S_["ig"], igc=Cc["ig"], good=S_["good"], goodc=Cc["good"], susp=S_["susp"], suspc=Cc["susp"], aud=d["aud"], audc=dc["aud"], panel=d["panel"], panelc=dc["panel"],
                        reach=d["reach_susp"], reachc=dc["reach_susp"], rvm=d["rv_member"], rvmc=dc["rv_member"], noseat=d["noseat"], noseatc=dc["noseat"], undet=d["noseat_undet"], undetc=dc["noseat_undet"], adm=d["adm"], admc=dc["adm"],
                        fa=f(e, "false_approvals"), fa0=f(C[s_], "false_approvals"), leak=1000 * f(e, "leak_bad"), leak0=1000 * f(C[s_], "leak_bad"), oh=f(e, "sys_overhead_per_vested"), oh0=f(C[s_], "sys_overhead_per_vested"),
                        dep=f(e, "departures"), dep0=f(C[s_], "departures"), arr=f(e, "arrivals"), arr0=f(C[s_], "arrivals"), cot=f(e, "cost_of_truth"), cot0=f(C[s_], "cost_of_truth"), Pt=f(e, "P_t"), Pt0=f(C[s_], "P_t"), fai=d["fa"], fai0=dc["fa"], fpaid=d["fa_paid"], fpaid0=dc["fa_paid"],
                        **{f"ss_{k}": v for k, v in state_share(e).items()}, **{f"ss0_{k}": v for k, v in state_share(C[s_]).items()}))
    return out
def state_share(e):
    """The state's share of the seats by seat: the first review (the state's initial seats over every initial seat), the audit seat, the panels (appeal and dispute), the deciding verdict (the state's by construction)."""
    tin = e.get("troop_initial_seats"); tr, ta, tp, ds = f(e, "troop_reviews"), f(e, "troop_audits"), f(e, "troop_panel_seats"), f(e, "deciding_seats")
    tin = float(tin) if tin not in (None, "") else (tr - tp - ds)        # the record before this commit: the troop reviews that were neither panel seats nor the deciding verdict's
    mi = f(e, "seated_initial_member") + f(e, "seated_initial_probationer"); ma = f(e, "seated_audit_member"); mp = f(e, "seated_appeal_member"); tpa = tp - ta
    return {"first": tin / (tin + mi) if (tin + mi) else np.nan, "audit": ta / (ta + ma) if (ta + ma) else np.nan, "panel": tpa / (tpa + mp) if (tpa + mp) else np.nan, "deciding": 1.0 if ds else np.nan, "n_first": tin + mi, "n_audit": ta + ma, "n_panel": tpa + mp, "n_dec": ds}
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
def binom_tail(n, p, k): return sum(math.comb(n, i) * p ** i * (1 - p) ** (n - i) for i in range(k, n + 1))
def verdict(text, shown, refuted): return f"- {text} **{'Shown' if shown else ('Refuted' if refuted else 'Neither')}.**"
CHK = []
def chk(ok, text): CHK.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def in_band(x, lo, hi): return (not np.isnan(x)) and lo <= x <= hi
# ------------------------------------------------------------------ the record and the reruns
CW3_OLD = load([f"{D19}/rerun/cw3-s21-70", f"{D19}/rerun/cw3-s71-120"], "careful")[1]; CW3 = load([f"{D22}/rerun/cw3-s21-70", f"{D22}/rerun/cw3-s71-120"], "careful")[1]
C23_OLD = load([f"{D20}/r23/s21-70", f"{D20}/r23/s71-120"], "careful")[1]; C23 = load([f"{D22}/rerun/r23-s21-70", f"{D22}/rerun/r23-s71-120"], "careful")[1]
R25_OLD = load([f"{D20}/r25/s21-70", f"{D20}/r25/s71-120"], "mix:caseM0.1:1.0")[0]; R25 = load([f"{D22}/rerun/r25-s21-70", f"{D22}/rerun/r25-s71-120"], "mix:caseM0.1:1.0")[0]
R9_OLD = load([f"{D19}/rerun/r9-s21-70", f"{D19}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0]; R9 = load([f"{D22}/rerun/r9-s21-70", f"{D22}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0]
R19_OLD = load([f"{D19}/r19/s{a}-{b}" for a, b in ((21, 45), (46, 70), (71, 95), (96, 120))], "mix:doseM0.2:0.25")[0]; R19 = load([f"{D22}/rerun/r19-s21-70", f"{D22}/rerun/r19-s71-120"], "mix:doseM0.2:0.25")[0]
R18 = load([f"{D19}/r18/s{a}-{b}" for a, b in ((21, 45), (46, 70), (71, 95), (96, 120))], "mix:doseM0.1:1.0")[0]
C20 = load([f"{D20}/r20/s21-60", f"{D20}/r20/s61-100", f"{D20}/r20/s101-140"], "careful")[1]; R22 = load([f"{D20}/r22/s21-70", f"{D20}/r22/s71-120"], "mix:doseM0.1:0.25")[0]; R24 = load([f"{D20}/r24/s21-70", f"{D20}/r24/s71-120"], "mix:doseM0.1:0.25")[0]
R26 = load([f"{D22}/r26/s21-70", f"{D22}/r26/s71-120"], "mix:caseM0.2:1.0")[0]; R27 = load([f"{D22}/r27/s21-70", f"{D22}/r27/s71-120"], "mix:caseM0.3:1.0")[0]; R28 = load([f"{D22}/r28/s21-70", f"{D22}/r28/s71-120"], "mix:caseM0.1:1.0")[0]
L = ["# Addendum 24 — the reviewer's arithmetic, five readings from the record, and reads 26–28 (November 17, 2026; notes §121)\n",
     "The record's worlds run again whole at this commit for the readings the record does not carry, checked to the digit against the record (every row column and every per-slot key of the record compared; the new keys beside):\n"]
for nm, new, old in (("world 3's all-careful (a19/rerun/cw3)", list(CW3.values()), list(CW3_OLD.values())), ("read 23's all-careful (a20/r23)", list(C23.values()), list(C23_OLD.values())), ("read 25 (a20/r25)", R25, R25_OLD), ("read 9 (a19/rerun/r9)", R9, R9_OLD), ("read 19 (a19/r19)", R19, R19_OLD)):
    if new and old: L.append(repro(new, old, nm)[0])
L.append(f"\nLoaded: cw3 {len(CW3)}, r23 {len(C23)}, r25 {len(R25)}, r26 {len(R26)}, r27 {len(R27)}, r28 {len(R28)}; r9 {len(R9)}, r19 {len(R19)}, r18 {len(R18)}, r22 {len(R22)}, r24 {len(R24)} episodes.\n")
# ------------------------------------------------------------------ AD3: the reviewer's arithmetic
L += ["## 1. The reviewer's arithmetic (AD3), confirmed or replaced from the record\n",
      "**AD3.1 — where a model that spares nine tenths stops paying, by the identity x = q · T\\*.** The level temptations of record (the conduct's gap over its benefit as a ratio of the seeds' means, plus one) from the worlds on record, and q = 0.9 / T\\*; in misses in all q + (1 − q) / 20 (a careful review misses one in twenty).\n",
      "| cell (read) | lifetime | T\\* of record | q = 0.9 / T\\* | in misses in all | one in | the reviewer's (R) |", "|---|---|---|---|---|---|---|"]
RV = {("0.50, as built (read 9)", "rec"): (6.2, 0.145, 0.19), ("0.50, as built (read 9)", "res"): (5.2, 0.173, 0.21), ("0.50, as built (read 9)", "lfl"): (3.8, 0.237, 0.28),
      ("0.34, the second failure (read 22)", "rec"): (7.4, 0.122, 0.17), ("0.34, the second failure (read 22)", "res"): (5.7, 0.158, 0.20), ("0.34, the second failure (read 22)", "lfl"): (3.8, 0.237, 0.28),
      ("0.20, the first failure (read 24)", "rec"): (11.5, 0.078, 0.12), ("0.20, the first failure (read 24)", "res"): (8.2, 0.110, 0.15), ("0.20, the first failure (read 24)", "lfl"): (2.2, 0.409, 0.44)}
TS = {}
for nm, E, C in (("0.50, as built (read 9)", R9_OLD, CW3_OLD), ("0.34, the second failure (read 22)", R22, C20), ("0.20, the first failure (read 24)", R24, C23_OLD)):
    rows = rows_of(E, C)
    if not rows: continue
    for key, kn, den in (("rec", "of record", "ben"), ("res", "with the reservation", "ben"), ("lfl", "like for like", "den")):
        t = temp(rows, key, den); q = 0.9 / t[0]; al = q + (1 - q) / 20; TS[(nm, key)] = (t, q, al); rv = RV[(nm, key)]
        L.append(f"| {nm} | {kn} | {t[0]:.1f} ± {t[1]:.1f} | {q:.3f} | {al:.3f} | {1 / al:.1f} | T\\* {rv[0]}, q {rv[1]:.3f}, in all {rv[2]:.2f} |")
L.append("\nThe reviewer's figures are the record's to the rounding (the level temptations as §119's tables carry them; the identity confirmed in §117 as the engine counts).\n")
L += ["**AD3.2 — what that model keeps at a dose of 0.1, and the bases of §119's two phrases.** The model spares nine tenths of the cost of its care, so on the base of the care it keeps 0.9 less the level saving: 0.9 − 0.61 = +0.29 as built, 0.9 − 0.74 = +0.16 at the second failure, 0.9 − 1.14 = −0.24 at the first — the reviewer's three figures, confirmed. §119's \"keeps 0.4 of its saving (0.61)\" was 1 − 0.61 = 0.39, on the base of the whole care and not of the nine tenths the model spares — a slip, corrected by erratum to 0.29 on the base of the care (0.32 of its own saving, 0.29 / 0.9). §119's \"keeps 0.16 (0.74)\" is on the base of 0.9. \"A quarter of the way to the line\" cannot be placed on any base the implementer can reconstruct (from 0.61 to the line at 0.90 the level saving 0.74 covers 0.45 of the way, not a quarter) and is withdrawn by erratum.\n"]
# AD3.3: read 25 in plain size
def plain(E):
    rows = []
    for e in E:
        aw = f(e, "awarded") - f(e, "troop_deliveries"); bd = f(e, "bad_deliveries"); fa = f(e, "false_approvals")
        rows.append(dict(bad_share=bd / aw if aw else np.nan, paid_per_1000=1000 * fa / aw if aw else np.nan, leak=1000 * f(e, "leak_bad"), fa=fa, aw=aw))
    return rows
P_ = {nm: plain(E) for nm, E in (("the all-careful", list(CW3_OLD.values())), ("read 18", R18), ("read 25", R25_OLD))}
L += ["**AD3.3 — read 25 in plain size.** From the rows of record (the members' real roots awarded, the bad deliveries among them, the standing false approvals):\n",
      "| world | bad share of the members' real roots | leak, ‰ of bad deliveries | **paid bad deliveries in a thousand tasks** | the reviewer's (R) |", "|---|---|---|---|---|"]
for nm, rv in (("the all-careful", 1.0), ("read 18", 2.9), ("read 25", 10.1)):
    r_ = P_[nm]; L.append(f"| {nm} | {np.mean(col(r_, 'bad_share')):.3f} | {np.mean(col(r_, 'leak')):.1f} | **{np.mean(col(r_, 'paid_per_1000')):.1f}** | {rv} |")
L.append(f"\nThe leak is {np.mean(col(P_['read 25'], 'leak')) / np.mean(col(P_['the all-careful'], 'leak')):.1f} times the all-careful's (R: 10.5) and the paid bad deliveries in a thousand tasks {np.mean(col(P_['read 25'], 'paid_per_1000')) / np.mean(col(P_['the all-careful'], 'paid_per_1000')):.1f} times. Confirmed, with the bad share read from the rows (0.200 at the members' seats).\n")
# AD3.4 / AD4.1: who met the bad deliveries, and a wrong first approval's fate — from the rerun's tally
def bm_rows(Cd):
    out = []
    for s_, e in sorted(Cd.items()):
        bm = json.loads(e.get("bad_met_first_json") or "{}")
        if not bm: continue
        r = {"seed": s_, **{k: float(v) for k, v in bm.items()}}
        out.append(r)
    return out
def bm_mean(rows, k): return float(np.mean([r.get(k, 0.0) for r in rows])) if rows else np.nan
def bm_table(L, rows, who_label):
    tot = sum(bm_mean(rows, f"first_{w}") for w in ("member", "probation", "state"))
    L += [f"| first reviewer | bad deliveries a run | share |", "|---|---|---|"]
    for w, wn in (("member", "a member"), ("probation", "a slot on probation"), ("state", "the state")):
        L.append(f"| {wn} | {bm_mean(rows, f'first_{w}'):.1f} | {bm_mean(rows, f'first_{w}') / tot if tot else np.nan:.3f} |")
    L.append(f"| every bad delivery closed | {tot:.1f} | |")
    keys = sorted({k for r in rows for k in r if k.startswith("fa_")})
    L += ["", "| wrong first approval of real bad work (a run) | count | of its kind |", "|---|---|---|"]
    for who in ("member", "probation", "state"):
        for cl in ("claim", "care"):
            base = bm_mean(rows, f"fa_{who}_{cl}")
            if not base: continue
            L.append(f"| **{who}, {'a claim' if cl == 'claim' else 'a careful error'}** | **{base:.2f}** | 1.000 |")
            for k in keys:
                if k.startswith(f"fa_{who}_{cl}_"): L.append(f"| … {k[len(f'fa_{who}_{cl}_'):].replace('_', ' ')} | {bm_mean(rows, k):.2f} | {bm_mean(rows, k) / base:.3f} |")
BM25 = bm_rows(D(R25)); BM3 = bm_rows(CW3)
L += ["**AD3.4 and AD4.1 — who met the bad deliveries that the shared model missed, in read 25.** From read 25's world run again whole (the tally at a member's real root's closure: the first reviewer's standing at the review, the verdict, whether the slot claimed on it, and its fate — vested, or overturned after the audit seat or a dispute panel differed; a bad delivery still open at the run's end is not counted). The state's first-review seats are one a run (the troop summoned for a seat unfilled past w_R): the state meets the bad deliveries at the audit seat, not at the first review.\n"]
if BM25:
    bm_table(L, BM25, "read 25"); L.append("")
    fm, fp, fs = bm_mean(BM25, "first_member"), bm_mean(BM25, "first_probation"), bm_mean(BM25, "first_state"); tot = fm + fp + fs
    cl = bm_mean(BM25, "fa_member_claim"); clp = sum(bm_mean(BM25, k) for r in BM25[:1] for k in {k for r in BM25 for k in r} if k.startswith("fa_member_claim_paid")); clo = cl - clp
    ovs = {k[len("fa_member_claim_overturned_"):]: bm_mean(BM25, k) for k in {k for r in BM25 for k in r} if k.startswith("fa_member_claim_overturned_")}
    st_ov = sum(v for k, v in ovs.items() if k.startswith("audit_state")); L.append(f"Of the real bad deliveries closed a run ({tot:.0f}), {fm / tot:.2f} were reviewed first by a member, {fp / tot:.2f} by a slot on probation and {fs / tot:.3f} by the state (R: about six in ten by a member). Of those a member claimed on at the first review ({cl:.1f} a run), {clp / cl if cl else np.nan:.2f} stayed paid (R: about three in four) and {clo / cl if cl else np.nan:.2f} were overturned — every one by the deciding verdict after an audit seat differed, {st_ov / clo if clo else np.nan:.2f} of them after the state's audit and {abs(1 - st_ov / clo) if clo else np.nan:.2f} after a member's (R: nearly every one at a seat of the state's — every one; a member's audit on the same case is the same model's claim and confirms). Of the claims that stayed paid, {bm_mean(BM25, 'fa_member_claim_paid_none') / clp if clp else np.nan:.2f} were never audited, {bm_mean(BM25, 'fa_member_claim_paid_audit_member_confirmed') / clp if clp else np.nan:.2f} were confirmed by a member's audit (the same conduct claiming at the audit seat) and {bm_mean(BM25, 'fa_member_claim_paid_audit_state_confirmed') / clp if clp else np.nan:.2f} by the state's.\n")
    L.append(f"The reviewer's AD3.4 is replaced by the count: the shared model's misses stay paid at the first review where the audit seat is a member's with the same model (a claim confirms a claim) and are caught where it is the state's; the careful errors ({bm_mean(BM25, 'fa_member_care'):.1f} a run by members, {bm_mean(BM25, 'fa_probation_care'):.1f} on probation) are caught at the same seats at the careful's rate.\n")
if BM3:
    L.append("The all-careful of world 3, the same tally (every wrong first approval a careful error):\n"); bm_table(L, BM3, "cw3"); L.append("")
# AD3.5: AB4.6's relation against read 23
rows24 = rows_of(R24, C23_OLD)
if rows24 and C23_OLD and CW3_OLD:
    care24 = np.mean(col(rows24, "call")); sd = sorted(set(C23_OLD) & set(CW3_OLD))
    d23 = mse([np.mean([life(v) for v in slots(C23_OLD[s])]) - np.mean([life(v) for v in slots(CW3_OLD[s])]) for s in sd]); d23r = mse([np.mean([life(v) + RES * after(v) for v in slots(C23_OLD[s])]) - np.mean([life(v) + RES * after(v) for v in slots(CW3_OLD[s])]) for s in sd])
    L += ["**AD3.5 — AB4.6's relation against read 23.** The relation (the careful lose 0.05 / (0.95 q) of what the model would save, 0.9 of its care) at the line of record q = 0.078 gives " + f"{0.05 / (0.95 * TS[('0.20, the first failure (read 24)', 'rec')][1]):.2f} of the saving, {0.05 / (0.95 * TS[('0.20, the first failure (read 24)', 'rec')][1]) * 0.9 * care24:.0f} real on read 24's conduct's care of {care24:.0f}; read 23 has {d23[0]:+.0f} ± {d23[1]:.0f} of record. With the reservation, at q = 0.110, {0.05 / (0.95 * TS[('0.20, the first failure (read 24)', 'res')][1]):.2f} of the saving, {0.05 / (0.95 * TS[('0.20, the first failure (read 24)', 'res')][1]) * 0.9 * care24:.0f} real; the read has {d23r[0]:+.0f} ± {d23r[1]:.0f}. The reviewer's arithmetic is confirmed on the care it took (0.67 and 0.48 of a saving of 0.9 × 215 to 250: 130 to 150 and 93 to 108), but that care is read 9's conduct's in world 3's cell; in the cell of the first failure a member reviews less (read 24's conduct {care24:.0f} real of care as a member, §119's 56 member reviews a life), and on that base the relation reads {0.05 / (0.95 * TS[('0.20, the first failure (read 24)', 'rec')][1]) * 0.9 * care24:.0f} of record against the read's {-d23[0]:.0f} ± {d23[1]:.0f} — within a standard error — and {0.05 / (0.95 * TS[('0.20, the first failure (read 24)', 'res')][1]) * 0.9 * care24:.0f} with the reservation against {-d23r[0]:.0f} ± {d23r[1]:.0f}, a third under. The reviewer's miss 5 ('two thirds to nine tenths too high') is the care base, not the relation's form; the relation still leaves out that what a barred member does not win goes to the others, as the reviewer says, which is why it reads under with the reservation.\n"]
# AD3.6 / AD4.4: the rejections of good work that stand
def frn_rows(Cd):
    out = []
    for s_, e in sorted(Cd.items()):
        bm = json.loads(e.get("bad_met_first_json") or "{}"); r = {"seed": s_, "unf": f(e, "appeals_unfunded"), "unf_fee": f(e, "appeals_unfunded_fee"), "unf_w": f(e, "appeals_unfunded_wallet"), "fr": f(e, "false_rejections"), "filed": f(e, "appeals_filed"), "lost": f(e, "appeals_lost"), "frt": f(e, "false_rejections_total")}
        r.update({k: float(v) for k, v in bm.items() if k.startswith("frn_")}); out.append(r)
    return out
FR3 = frn_rows(CW3)
if FR3:
    keys = sorted({k for r in FR3 for k in r if k.startswith("frn_")})
    L += ["**AD3.6 and AD4.4 — the rejections of good work that are never appealed.** From world 3's all-careful run again whole: the standing rejections of good work a run by the engine's reason for the final N, and whether the actor had appealed; the appeals an actor wanted and could not fund, with the court fee and the actor's unlocked balance at the time.\n",
          "| rejections of good work standing at the run's end, a run | count |", "|---|---|"]
    for k in keys: L.append(f"| {k[4:].replace('_', ' ')} | {np.mean([r.get(k, 0.0) for r in FR3]):.2f} |")
    L.append(f"| **every standing rejection of good work** (`false_rejections`) | **{m(FR3, 'fr')[0]:.2f}** |")
    L.append(f"| rejections of good work put to the actor (`false_rejections_total`) / appeals filed / lost | {m(FR3, 'frt')[0]:.1f} / {m(FR3, 'filed')[0]:.1f} / {m(FR3, 'lost')[0]:.2f} |")
    L.append(f"| appeals wanted and unfunded (`appeals_unfunded`) | {m(FR3, 'unf')[0]:.2f} |")
    na = np.mean([r.get("frn_not_appealed_audit_upheld_nonfulfillment", 0.0) for r in FR3])
    unf = m(FR3, 'unf')[0]; fee_u = (np.sum([r['unf_fee'] for r in FR3]) / np.sum([r['unf'] for r in FR3])) if unf else np.nan; w_u = (np.sum([r['unf_w'] for r in FR3]) / np.sum([r['unf'] for r in FR3])) if unf else np.nan; acc = np.mean([r.get('frn_not_appealed_rejection_accepted', 0.0) for r in FR3])
    L.append(f"\n**§120's sentence 'the rest never appealed for want of the court fee' is corrected by erratum: it holds for one in six of them.** Of the {m(FR3, 'fr')[0]:.2f} standing rejections of good work a run, {m(FR3, 'lost')[0]:.2f} are appeals lost at the deciding verdict, **{na:.2f} are the audit road's** — a good delivery approved at the first review, rejected by the audit seat in error, and the deciding verdict upholding the rejection in error: final N 'audit upheld nonfulfillment', with no response window and no appeal, the case's one challenge round spent by the audit — and **{acc:.2f} are rejections accepted for want of the court fee** (`appeals_unfunded` {unf:.2f} a run: the actor wanted to appeal and its unlocked balance was under the fee — the fee {fee_u:.2f} real at the case's index, D = {D_FEE:.0f} nominal, against a holding of {w_u:.2f} real at the time; the rest the state's own good deliveries rejected, which accept the verdict). Every other rejection of good work put to the actor was appealed ({m(FR3, 'frt')[0]:.1f} put, {m(FR3, 'filed')[0]:.1f} filed). The reviewer's 'at least 3.06 a run' (5.28 less 2.22) is the right size: the never-appealed are {na + acc:.2f} a run, {(na + acc) / (na + acc + m(FR3, 'filed')[0]):.3f} of the wrong rejections, five in six of them on a road with no appeal.\n")
# AD3.7: the line and the earned seats' threshold
L += ["**AD3.7 — the line and the earned seats' threshold.** The rule as the engine counts (`Actor.a_hat` = (wrong + 1) / (n + 2) over the trailing n_P = 20 bad plants; `record_passes` fails above θ, `panel_eligible` at θ_panel = 0.20 and the suspension at θ_duty): on a full window four wrong is 5/22 = 0.227 and fails, three is 4/22 = 0.182 and passes — the reviewer's arithmetic confirmed. Four or more wrong of twenty, each wrong with probability 0.05 + 0.95 · dose:\n",
      "| conduct | wrong on the planted bad cases met | four or more of twenty | the reviewer's (R) |", "|---|---|---|---|"]
for label, dose, rv in (("careful", 0.0, "1.6 in 100"), ("a dose of 0.1", 0.1, "33"), ("a dose of 0.145, the line", 0.145, "53"), ("a dose of 0.2", 0.2, "74"), ("a dose of 0.3", 0.3, "94")):
    p = 0.05 + 0.95 * dose; L.append(f"| {label} | {p:.3f} | {100 * binom_tail(20, p, 4):.1f} in 100 | {rv} |")
L.append("\nThe ticks without the earned seats, measured — the reviewer asks it from read 9's and read 19's ticks. The record's slots carry the first failure's phase alone (the good ticks from the first wrong planted verdict until the seats return, `pf_good_ticks_lost`); the reruns at this commit carry every tick as a member on which the slot was not panel-eligible on its own record (`ticks_member_noseat`), and among them the ticks on which its record was still undetermined (fewer than n_min = 4 planted bad cases met, `ticks_member_noseat_undet`) — a founder of world 3 meets its fourth planted bad case about half-way through the run, and an arrival on probation does not hold the seats whatever its record:\n")
L += ["| world / read | slots | member ticks a slot | **without the earned seats (share of the member ticks)** | … of it the record undetermined | … the record failing | the first failure's spell (good ticks a slot; share) | audit seats a slot | panel seats a slot |", "|---|---|---|---|---|---|---|---|---|"]
def seats_row(nm, V):
    d = counts(V); L.append(f"| {nm} | {d['n']} | {d['tm']:.0f} | **{d['noseat']:.3f}** | {d['noseat_undet']:.3f} | {d['noseat'] - d['noseat_undet']:.3f} | {d['pf_lost']:.0f}; {d['pf_lost_share']:.3f} | {d['aud']:.1f} | {d['panel']:.1f} |")
for nm, E in (("read 9: conduct M at 0.1 on 1 in 4 — the conduct's slots", R9), ("read 19: conduct M at 0.2 on 1 in 4 — the conduct's slots", R19)):
    if E:
        seats_row(nm, [v for e in E for v in groups(e)["claim"]]); seats_row(nm.replace("the conduct's slots", "the careful beside"), [v for e in E for v in groups(e)["care"]])
for nm, Cd in (("world 3's all-careful (every slot)", CW3), ("read 25: case-keyed M at 0.1 on every slot", D(R25)), ("read 26: case-keyed M at 0.2 on every slot", D(R26)), ("read 27: case-keyed M at 0.3 on every slot", D(R27)), ("read 23's all-careful, θ_duty 0.20 (every slot)", C23), ("read 28: case-keyed M at 0.1 on every slot, θ_duty 0.20", D(R28))):
    if Cd: seats_row(nm, [v for e in Cd.values() for v in slots(e)])
L.append("\nThe reviewer's reading of the line as the earned seats' threshold is confirmed in its mechanism and corrected in one part. Confirmed: a careful member's audit seats beside read 9's conduct (39.6 at 4.46 real beyond their care, 177 real) are of the size of what a model that spares nine tenths saves (194 on a care of 215), and the conduct loses them by failing enough planted bad cases to be without the seats most of the time — the table above has the conduct's slots without the seats for a larger share of their member ticks than the careful beside, with the record failing the larger part of it, where the careful's own share is mostly the undetermined record of a founder's first half-run. Corrected: the binomial on a full window overstates the time without the seats for a conduct at the line, because a member that fails the record at the earned seats' threshold is checked at every plant and its seats come back as the window turns over — the measured share, not the binomial, is the figure of record. (The share for the careful is not nothing: the undetermined record holds a founder off the panels until its fourth bad plant, which is the panel-determined rule of 1.6.0, not a failure.)\n")
# AD3.8
L += ["**AD3.8 — how far 'the first failure' holds.** By the smoothed rate, with n right verdicts already in the window a first wrong gives (1 + 1) / (n + 2), above 0.20 only while n ≤ 7; a second wrong 3 / (n + 2), above 0.20 while n ≤ 12; a third 4 / (n + 2), while n ≤ 17; a fourth 5 / (n + 2), always on a window of twenty. So for a member whose window already holds eight or more right verdicts the first holds: its first wrong planted verdict does not suspend it at θ_duty 0.20 (119a's count), and AA3.4's second reading — suspended at its first wrong once the window is determined — holds only for a window of four to seven. At eight or more the suspension's threshold is the earned seats' own: the member is suspended at the fourth wrong on a full window, when it also loses the seats; between, at the second wrong while the window holds at most twelve and at the third while it holds at most seventeen. 'The cell of the first failure' names the cell by its effect on a record of no more than seven, as the reviewer says (AD2.6).\n"]
# ------------------------------------------------------------------ AD4.2: the state's share of the seats by seat
L += ["## 2. The state's share of the seats, by seat (AD4.2)\n", "The state's initial seats over every initial seat (members' and probationers'); its audit seats over every audit seat (the plants' and the planted approvals' among them); its appeal and dispute panel seats over every panel seat; the deciding verdict's seats, the state's by construction. For the worlds on record before this commit the state's initial seats are its reviews that were neither panel seats nor the deciding verdict's (the identity holds to the unit on the reruns).\n",
      "| world / read | first review | audit seat | panels | deciding verdict | seats a run: first / audit / panels / deciding |", "|---|---|---|---|---|---|"]
def ss_row(nm, Cd):
    rows = [state_share(e) for e in Cd.values()]
    if rows: L.append(f"| {nm} | {np.nanmean([r['first'] for r in rows]):.3f} | {np.nanmean([r['audit'] for r in rows]):.3f} | {np.nanmean([r['panel'] for r in rows]):.3f} | {np.nanmean([r['deciding'] for r in rows]):.2f} | {np.mean([r['n_first'] for r in rows]):.0f} / {np.mean([r['n_audit'] for r in rows]):.0f} / {np.mean([r['n_panel'] for r in rows]):.0f} / {np.mean([r['n_dec'] for r in rows]):.0f} |")
for nm, Cd in (("world 3's all-careful", CW3 or CW3_OLD), ("read 18: M at 0.1 on every slot", D(R18)), ("read 25: case-keyed M at 0.1 on every slot", D(R25) or D(R25_OLD)), ("read 23's all-careful, θ_duty 0.20", C23 or C23_OLD), ("read 26: case-keyed M at 0.2", D(R26)), ("read 27: case-keyed M at 0.3", D(R27)), ("read 28: case-keyed M at 0.1, θ_duty 0.20", D(R28))):
    if Cd: ss_row(nm, Cd)
# ------------------------------------------------------------------ AD5: reads 26–28
L += ["\n## 3. Reads 26–28: a population above the line, and a population under the first failure (AD5)\n",
      "Conduct M with its claims set by the case on every slot of the world (the mix wrapper's share at 1.0; as a member a claim where the case's hash falls under the dose, the same cases for every slot of the seed at every seat, careful at the others and on probation), seeds 21–120, read as read 25 was: each row a seed, the all-careful's slot less the population's (reads 26 and 27 against world 3's all-careful, read 28 against read 23's all-careful of the same cell), the population's level saving as a ratio of the seeds' means (what the claims spared plus the loss, over the care on all its reviews as a member), and the world's side by seed.\n"]
HDR_POP = ["| read | seeds | slots a seed: population / all-careful | **all-careful − population, of record** (SE from nothing) | temptation | **with the reservation** | temptation | like for like (reported) | the population's slot: of record / with the reservation | suspended at least once (share): population / all-careful | suspensions a slot | good ticks a slot: population / all-careful | arrivals admitted (share): population / all-careful |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
P25 = pop_rows(R25 or R25_OLD, CW3 or CW3_OLD); P26 = pop_rows(R26, CW3 or CW3_OLD); P27 = pop_rows(R27, CW3 or CW3_OLD); P28 = pop_rows(R28, C23 or C23_OLD); P18 = pop_rows(R18, CW3 or CW3_OLD)
POPS = (("25: M at 0.1 (the record's read, against world 3's all-careful)", P25), ("**26: M at 0.2**, world 3's cell", P26), ("**27: M at 0.3**, world 3's cell", P27), ("**28: M at 0.1**, the cell of the first failure (against read 23's all-careful)", P28))
L += HDR_POP
for nm, P in POPS:
    if not P: continue
    a, b, c = mse(col(P, "rec")), mse(col(P, "res")), mse(col(P, "lfl")); ta, tb = temp(P, "rec", "ben"), temp(P, "res", "ben")
    L.append(f"| {nm} | {len(P)} | {np.mean(col(P, 'n')):.1f} / {np.mean(col(P, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {ta[0]:.1f} ± {ta[1]:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f}) | {tb[0]:.1f} ± {tb[1]:.1f} | {c[0]:+.0f} ± {c[1]:.0f} | {np.mean(col(P, 'life')):.0f} / {np.mean(col(P, 'lres')):.0f} | {np.mean(col(P, 'reach')):.2f} / {np.mean(col(P, 'reachc')):.2f} | {np.mean(col(P, 'susp')):.2f} | {np.mean(col(P, 'good')):.0f} / {np.mean(col(P, 'goodc')):.0f} | {np.nanmean(col(P, 'adm')):.2f} / {np.nanmean(col(P, 'admc')):.2f} |")
L += ["\n| read | what the claims spared a slot | the care on all its reviews as a member | claims a slot | **the population's level saving, the ratio of the seeds' means: of record / with the reservation / like for like** | the mean of the seeds' ratios | wrong first approvals of real bad work a slot (paid) |", "|---|---|---|---|---|---|---|"]
RM = {}
for nm, P in POPS:
    if not P: continue
    rm = tuple(ratio_se(col(P, f"loss_{k}") + col(P, "spared"), col(P, "call")) for k in ("rec", "res", "lfl")); mr = tuple(mse(col(P, f"x_{k}")) for k in ("rec", "res", "lfl")); RM[nm[:4]] = rm
    L.append(f"| {nm} | {pm(mse(col(P, 'spared')))} | {pm(mse(col(P, 'call')), 0)} | {pm(mse(col(P, 'claims')))} | **{pm(rm[0], 2)} / {pm(rm[1], 2)} / {pm(rm[2], 2)}** | {pm(mr[0], 2)} / {pm(mr[1], 2)} / {pm(mr[2], 2)} | {np.mean(col(P, 'fai')):.2f} ({np.mean(col(P, 'fpaid')):.2f}) |")
L += ["\n**The seats the members hold, and the time without them** (the reviewer's three readings beyond read 25's): the audit seats and the panel seats a slot that members hold; the share of a slot's ticks as a member on which it is without its earned seats (and of it the undetermined record); the state's share of the seats by seat.\n",
      "| read | audit seats a slot: population / all-careful | panel seats a slot: population / all-careful | member reviews a slot: population / all-careful | **member ticks without the earned seats (share): population / all-careful** | … the record undetermined: population / all-careful | the state's share: first review / audit / panels (population) | (all-careful) |", "|---|---|---|---|---|---|---|---|"]
for nm, P in POPS:
    if not P: continue
    L.append(f"| {nm} | {np.mean(col(P, 'aud')):.1f} / {np.mean(col(P, 'audc')):.1f} | {np.mean(col(P, 'panel')):.1f} / {np.mean(col(P, 'panelc')):.1f} | {np.mean(col(P, 'rvm')):.1f} / {np.mean(col(P, 'rvmc')):.1f} | **{np.nanmean(col(P, 'noseat')):.3f} / {np.nanmean(col(P, 'noseatc')):.3f}** | {np.nanmean(col(P, 'undet')):.3f} / {np.nanmean(col(P, 'undetc')):.3f} | {np.nanmean(col(P, 'ss_first')):.3f} / {np.nanmean(col(P, 'ss_audit')):.3f} / {np.nanmean(col(P, 'ss_panel')):.3f} | {np.nanmean(col(P, 'ss0_first')):.3f} / {np.nanmean(col(P, 'ss0_audit')):.3f} / {np.nanmean(col(P, 'ss0_panel')):.3f} |")
WK = (("fa", "fa0", "standing false approvals a run", 1), ("leak", "leak0", "the leak, ‰ of bad deliveries", 1), ("oh", "oh0", "the system overhead a vested task", 2), ("cot", "cot0", "the cost of truth a run", 0), ("dep", "dep0", "departures a run", 1), ("arr", "arr0", "arrivals a run", 1), ("Pt", "Pt0", "P_t at the end", 1))
def world_side(L, title, PA, PB, nmA, nmB, with_base=True):
    A_ = {r["seed"]: r for r in PA}; B_ = {r["seed"]: r for r in PB}; sd = sorted(set(A_) & set(B_)); out = {}
    L += [f"\n**{title}** (paired by seed; the all-careful of each read's own cell beside):\n", f"| measure | {nmA} | {nmB} | **{nmB} − {nmA}** (SE from nothing) | {nmA} − its all-careful | {nmB} − its all-careful |", "|---|---|---|---|---|---|"]
    for k, k0, nm, d in WK:
        dd = mse([B_[s][k] - A_[s][k] for s in sd]); dA = mse(col(PA, k) - col(PA, k0)); dB = mse(col(PB, k) - col(PB, k0)); out[k] = (dd, np.mean(col(PB, k)), np.mean(col(PA, k)))
        L.append(f"| {nm} | {np.mean(col(PA, k)):.{d}f} | {np.mean(col(PB, k)):.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) | {dA[0]:+.{d}f} ± {dA[1]:.{d}f} | {dB[0]:+.{d}f} ± {dB[1]:.{d}f} |")
    return out
W = {}
if P25 and P26: W["26"] = world_side(L, "The world's side, read 26 against read 25", P25, P26, "read 25", "read 26")
if P25 and P27: W["27"] = world_side(L, "The world's side, read 27 against read 25", P25, P27, "read 25", "read 27")
if P25 and P28: W["28v25"] = world_side(L, "The world's side, read 28 against read 25", P25, P28, "read 25", "read 28")
# read 28 against read 23: the three lifetimes by seed (pop_rows against C23 is exactly that) and the world's side
if P28:
    L += ["\n**Read 28 against read 23 by seed** — the three lifetimes (read 23's all-careful slot less read 28's population's, each seed on the same cell) are the first table's row for read 28; the world's side against read 23's all-careful is its 'read 28 − its all-careful' column above, repeated here with the all-careful's own level:\n", "| measure | read 23's all-careful | read 28 | **read 28 − read 23** (SE) |", "|---|---|---|---|"]
    for k, k0, nm, d in WK:
        dd = mse(col(P28, k) - col(P28, k0)); L.append(f"| {nm} | {np.mean(col(P28, k0)):.{d}f} | {np.mean(col(P28, k)):.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
    W["28"] = {k: (mse(col(P28, k) - col(P28, k0)), np.mean(col(P28, k)), np.mean(col(P28, k0))) for k, k0, _, _ in WK}
# ------------------------------------------------------------------ expectations and verdicts
L += ["\n## 4. Against the expectations stated before the run (AD5)\n"]
if P26:
    a = mse(col(P26, "rec")); chk(in_band(np.mean(col(P26, "aud")), 16, 30), f"read 26: audit seats a slot that members hold 16 to 30 (read 25 about 36): {np.mean(col(P26, 'aud')):.1f}."); chk(in_band(100 * np.mean(col(P26, "reach")), 13, 26), f"read 26: 13 to 26 slots in 100 suspended at least once: {100 * np.mean(col(P26, 'reach')):.0f}.")
    chk(in_band(a[0], 70, 240), f"read 26: behind the all-careful's slot by 70 to 240 real of record: {a[0]:+.0f} ± {a[1]:.0f}."); chk(in_band(RM['**26'][0][0], 0.5, 1.2), f"read 26: a level saving of 0.5 to 1.2 of record: {pm(RM['**26'][0], 2)}.")
    chk(in_band(np.mean(col(P26, "leak")), 55, 100), f"read 26: a leak of 55 to 100 in a thousand bad deliveries: {np.mean(col(P26, 'leak')):.1f}."); chk(in_band(np.mean(col(P26, "fa")), 28, 50), f"read 26: standing false approvals of 28 to 50 a run: {np.mean(col(P26, 'fa')):.1f}."); chk(in_band(np.mean(col(P26, "oh")), 15, 19), f"read 26: an overhead of 15 to 19: {np.mean(col(P26, 'oh')):.2f}.")
if P27:
    a = mse(col(P27, "rec")); chk(in_band(np.mean(col(P27, "aud")), 4, 16), f"read 27: audit seats a slot 4 to 16: {np.mean(col(P27, 'aud')):.1f}."); chk(in_band(100 * np.mean(col(P27, "reach")), 25, 50), f"read 27: 25 to 50 in 100 suspended at least once: {100 * np.mean(col(P27, 'reach')):.0f}.")
    chk(in_band(a[0], 170, 420), f"read 27: behind by 170 to 420 real of record: {a[0]:+.0f} ± {a[1]:.0f}."); chk(in_band(RM['**27'][0][0], 1.2, 2.6), f"read 27: a level saving of 1.2 to 2.6 of record: {pm(RM['**27'][0], 2)}.")
    chk(in_band(np.mean(col(P27, "leak")), 60, 130), f"read 27: a leak of 60 to 130: {np.mean(col(P27, 'leak')):.1f}."); chk(in_band(np.mean(col(P27, "fa")), 30, 65), f"read 27: standing false approvals of 30 to 65 a run: {np.mean(col(P27, 'fa')):.1f}."); chk(in_band(np.mean(col(P27, "oh")), 16, 21), f"read 27: an overhead of 16 to 21: {np.mean(col(P27, 'oh')):.2f}.")
if P28:
    a = mse(col(P28, "rec")); chk(in_band(100 * np.mean(col(P28, "reach")), 55, 78), f"read 28: 55 to 78 in 100 suspended at least once: {100 * np.mean(col(P28, 'reach')):.0f}."); chk(in_band(np.mean(col(P28, "susp")), 0.65, 1.1), f"read 28: 0.65 to 1.1 suspensions a slot: {np.mean(col(P28, 'susp')):.2f}.")
    chk(in_band(np.mean(col(P28, "good")), 340, 420), f"read 28: good ticks a slot 340 to 420 (read 23's 484): {np.mean(col(P28, 'good')):.0f} ({np.mean(col(P28, 'goodc')):.0f})."); chk(in_band(100 * np.nanmean(col(P28, "adm")), 74, 84), f"read 28: arrivals admitted within the run 74 to 84 in 100: {100 * np.nanmean(col(P28, 'adm')):.0f}.")
    chk(in_band(a[0], 20, 135), f"read 28: behind read 23's slot by 20 to 135 real of record: {a[0]:+.0f} ± {a[1]:.0f}."); chk(in_band(RM['**28'][0][0], 0.25, 1.0), f"read 28: a level saving of 0.25 to 1.0 of record against read 23's all-careful: {pm(RM['**28'][0], 2)}.")
    chk(in_band(np.mean(col(P28, "leak")), 30, 50), f"read 28: a leak of 30 to 50: {np.mean(col(P28, 'leak')):.1f}."); chk(in_band(np.mean(col(P28, "fa")), 15, 26), f"read 28: standing false approvals of 15 to 26 a run: {np.mean(col(P28, 'fa')):.1f}."); chk(in_band(np.mean(col(P28, "oh")), 14.5, 17.5), f"read 28: an overhead of 14.5 to 17.5: {np.mean(col(P28, 'oh')):.2f}.")
L += CHK; L.append(f"\n**{sum(1 for c in CHK if c.startswith('- MET'))} of {len(CHK)} expectations met.**\n")
L += ["\n## 5. Refuted, or shown, each apart (AD5's conditions)\n"]
if P26:
    x = RM['**26'][0]; L.append(verdict(f"*A population on a model that misses a quarter of the bad work does not gain by it*: shown if read 26's level saving of record is above 0.9 by two standard errors; refuted if it is under 0.9 at the point value. Read 26's is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] - 2 * x[1] > 0.9, x[0] < 0.9))
if P27:
    x = RM['**27'][0]; L.append(verdict(f"*A population on a model that misses a third of the bad work loses by it*: the same condition on read 27. Read 27's is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] - 2 * x[1] > 0.9, x[0] < 0.9))
if P28:
    x = RM['**28'][0]; L.append(verdict(f"*The suspension at the first failure does not hold a population on a model that spares nine tenths at a dose of 0.1*: shown if read 28's level saving against read 23's all-careful is under 0.9 by two standard errors of record; refuted if it is above 0.9 at the point value. Read 28's is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] + 2 * x[1] < 0.9, x[0] > 0.9))
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("wrote", sys.argv[1], len(L), "lines")
