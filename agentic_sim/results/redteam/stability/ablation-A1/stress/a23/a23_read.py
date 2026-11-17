"""Addendum 26 (November 17, 2026, late evening; notes §122): the reviewer's arithmetic on §121 confirmed or replaced (AF3), the five readings from the record (AF4), addendum 25's
questions from the record (AE3), and read 29 — conduct M at 0.2 with its claims set by the case on 3 slots in 4, the rest careful, in world 3's cell (a23/launch.sh at 658d83ad0,
seeds 21–120), read as read 19 was and against read 26 by seed. World 3's all-careful run again whole at 658d83ad0 for the audit road by whose audit differed and the first wrong
planted verdict as a member, checked to the digit against a22/rerun. a22_read.py's helpers copied. Usage: a23_read.py OUT.md"""
import json, os, sys, hashlib, math, glob, csv, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D23, D22, D20, D19 = f"{R}/a23", f"{R}/a22", f"{R}/a20", f"{R}/a19"
T = 1000; RES = 0.8; D_FEE = 2.0; T_SUSP = 100
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
                claims=sum(v["claims"] for v in V) / n, susp=sum(v["suspensions"] for v in V) / n, aud=sum(v["audits_done"] for v in V) / n, panel=sum(v.get("rvm_appeal", 0) + v.get("rvm_third", 0) + v.get("rvm_dispute", 0) for v in V) / n,
                care_m=sum(v.get("care_member", 0) for v in V) / n, claimed_m=sum(v.get("claimed_member", 0) for v in V) / n, rvm=sum(v.get("rv_member", 0) for v in V) / n, reach=sum(1 for v in V if v["suspensions"] > 0) / n,
                tm=sum(v.get("ticks_member", 0) for v in V) / n, noseat=(sum(v.get("ticks_member_noseat", 0) for v in V) / sum(v.get("ticks_member", 0) for v in V)) if sum(v.get("ticks_member", 0) for v in V) else np.nan,
                undet=(sum(v.get("ticks_member_noseat_undet", 0) for v in V) / sum(v.get("ticks_member", 0) for v in V)) if sum(v.get("ticks_member", 0) for v in V) else np.nan, fa=sum(v.get("fa_init", 0) for v in V) / n, fpaid=sum(v.get("fa_init_paid", 0) for v in V) / n)
def state_share(e):
    tin = e.get("troop_initial_seats"); tr, ta, tp, ds = f(e, "troop_reviews"), f(e, "troop_audits"), f(e, "troop_panel_seats"), f(e, "deciding_seats")
    tin = float(tin) if tin not in (None, "") else (tr - tp - ds)
    mi = f(e, "seated_initial_member") + f(e, "seated_initial_probationer"); ma = f(e, "seated_audit_member"); mp = f(e, "seated_appeal_member"); tpa = tp - ta
    return {"first": tin / (tin + mi) if (tin + mi) else np.nan, "audit": ta / (ta + ma) if (ta + ma) else np.nan, "panel": tpa / (tpa + mp) if (tpa + mp) else np.nan}
WK = (("fa", "false_approvals", "standing false approvals a run", 1), ("leak", "leak_bad", "the leak, ‰ of bad deliveries", 1), ("oh", "sys_overhead_per_vested", "the system overhead a vested task", 2), ("cot", "cost_of_truth", "the cost of truth a run", 0), ("dep", "departures", "departures a run", 1), ("arr", "arrivals", "arrivals a run", 1), ("Pt", "P_t", "P_t at the end", 1))
def world(e): return {k: (1000 * f(e, kk) if k == "leak" else f(e, kk)) for k, kk, _, _ in WK}
def repro(new_eps, old_eps, label):
    old = {int(e["seed"]): e for e in old_eps}; n_rows = n_keys = n_slots = n_seeds = 0; diffs = []
    for e in new_eps:
        s_ = int(e["seed"])
        if s_ not in old: continue
        o = old[s_]; n_seeds += 1
        for k in o:
            if k in ("learner_slots_json", "bad_met_first_json"): continue
            n_rows += 1
            if o[k] != e.get(k): diffs.append((s_, k))
        So, Sn = json.loads(o["learner_slots_json"]), json.loads(e["learner_slots_json"])
        for x, v in So.items():
            n_slots += 1
            for k, val in v.items():
                n_keys += 1
                if Sn.get(x, {}).get(k) != val: diffs.append((s_, x, k))
    return f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") + " (the `bad_met_first_json` tally, extended at this commit, compared apart: its keys of record unchanged)."
def verdict(text, shown, refuted): return f"- {text} **{'Shown' if shown else ('Refuted' if refuted else 'Neither')}.**"
CHK = []
def chk(ok, text): CHK.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def in_band(x, lo, hi): return (not np.isnan(x)) and lo <= x <= hi
# ------------------------------------------------------------------ the record
CW3_22 = load([f"{D22}/rerun/cw3-s21-70", f"{D22}/rerun/cw3-s71-120"], "careful")[1]; CW3 = load([f"{D23}/rerun/cw3-s21-70", f"{D23}/rerun/cw3-s71-120"], "careful")[1]
C23 = load([f"{D22}/rerun/r23-s21-70", f"{D22}/rerun/r23-s71-120"], "careful")[1]
R25 = load([f"{D22}/rerun/r25-s21-70", f"{D22}/rerun/r25-s71-120"], "mix:caseM0.1:1.0")[0]; R26 = load([f"{D22}/r26/s21-70", f"{D22}/r26/s71-120"], "mix:caseM0.2:1.0")[0]
R27 = load([f"{D22}/r27/s21-70", f"{D22}/r27/s71-120"], "mix:caseM0.3:1.0")[0]; R28 = load([f"{D22}/r28/s21-70", f"{D22}/r28/s71-120"], "mix:caseM0.1:1.0")[0]
R29 = load([f"{D23}/r29/s21-70", f"{D23}/r29/s71-120"], "mix:caseM0.2:0.75")[0]
R19 = load([f"{D22}/rerun/r19-s21-70", f"{D22}/rerun/r19-s71-120"], "mix:doseM0.2:0.25")[0]
L = ["# Addendum 26 — the reviewer's arithmetic on §121, the readings asked from the record, addendum 25's questions, and read 29 (November 17, 2026; notes §122)\n"]
if CW3 and CW3_22: L.append(repro(list(CW3.values()), list(CW3_22.values()), "world 3's all-careful (a22/rerun/cw3, itself 0 differences against a19/rerun)"))
L.append(f"\nLoaded: cw3 {len(CW3)}, r23 {len(C23)}, r25 {len(R25)}, r26 {len(R26)}, r27 {len(R27)}, r28 {len(R28)}, r29 {len(R29)}, r19 {len(R19)} episodes.\n")
# ------------------------------------------------------------------ AF4.1 / AF3.1: the audit road by whose audit differed
L += ["## 1. The reviewer's arithmetic (AF3) and the readings asked (AF4)\n"]
def frn(Cd):
    rows = []
    for s_, e in sorted(Cd.items()):
        bm = json.loads(e.get("bad_met_first_json") or "{}"); rows.append({"seed": s_, **{k: float(v) for k, v in bm.items() if k.startswith("frn_")}, "fr": f(e, "false_rejections"), "lost": f(e, "appeals_lost"), "na": f(e, "troop_audits"), "ma": f(e, "seated_audit_member")})
    return rows
FR = frn(CW3)
if FR:
    g = lambda k: float(np.mean([r.get(k, 0.0) for r in FR])); st_, me_ = g("frn_not_appealed_audit_upheld_nonfulfillment_state"), g("frn_not_appealed_audit_upheld_nonfulfillment_member"); ta, ma = g("na"), g("ma")
    L += ["**AF4.1 and AF3.1 — the audit road, by whose audit differed.** From the engine's text first: in world 3's cell the state's audit that differs is the deciding verdict's first seat wherever the state holds an audit seat — `_audit_result` under arm 1 opens the deciding verdict with `first=(r.id, r.verdict)` for a troop's audit (`_open_deciding(c, \"state_audit\", first=…)`, the reason `state_audit`), one more seat of the orchestrator's is summoned and a third on a split; after a member's audit two fresh seats (`\"audit\"`). So a wrong N at the state's audit on good work is upheld if one more seat is wrong or the third after a split, 0.05 + 0.95 × 0.05 = 0.0975; after a member's wrong N it takes two wrong of three, 0.00725 — the reviewer's arithmetic confirmed from the engine. The count, from world 3's all-careful run again whole:\n",
          "| the audit road's standing rejections of good work, a run | count | the reviewer's (R) |", "|---|---|---|", f"| after the state's audit differed | **{st_:.2f}** | 3.2 |", f"| after a member's audit differed | **{me_:.2f}** | 0.5 |", f"| together | {st_ + me_:.2f} | 3.7 (the tally's 3.47) |",
          f"\nThe state's audit seats a run {ta:.0f} of {ta + ma:.0f} ({ta / (ta + ma):.3f}); the audits of good work wrong at 0.05 give {0.05 * ta * 0.8 * 0.0975:.2f} after the state's (0.8 of the audit seats on good work) and {0.05 * ma * 0.8 * 0.00725:.2f} after a member's by the rates. **{st_ / (st_ + me_):.2f} of the audit road's wrong rejections follow an audit the state sat** (R: about nine in ten). Taken afresh with two new seats after the state's audit the first figure would be {st_ * 0.00725 / 0.0975:.2f} a run and the standing rejections of good work about {m(FR, 'fr')[0] - st_ + st_ * 0.00725 / 0.0975:.1f} where they are {m(FR, 'fr')[0]:.2f} (R: 0.2 and 2.5) — arithmetic, no read.\n"]
# ------------------------------------------------------------------ AF3.2 / AF4.2: the care a slot, the gain a member
def pop_stats(E, C):
    rows = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in C: continue
        V, Vc = slots(e), slots(C[s_]); S_, Cc = stats_(V), stats_(Vc); call = S_["care_m"] + S_["claimed_m"]
        rows.append(dict(seed=s_, rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], call=call, carec=Cc["care_m"], rvm=S_["rvm"], rvmc=Cc["rvm"], susp=S_["susp"], suspc=Cc["susp"], reach=S_["reach"], reachc=Cc["reach"], good=S_["good"], goodc=Cc["good"], life=S_["life"], lifec=Cc["life"], **{f"w_{k}": v for k, v in world(e).items()}, **{f"w0_{k}": v for k, v in world(C[s_]).items()}))
    return rows
P25, P26, P27, P28 = pop_stats(R25, CW3 or CW3_22), pop_stats(R26, CW3 or CW3_22), pop_stats(R27, CW3 or CW3_22), pop_stats(R28, C23)
L += ["**AF3.2 and AF4.2 — the care on a slot's reviews as a member, and what the model gains a member.** The care on all a slot's reviews as a member (the conduct's care paid plus the care its claims spared; the all-careful's care beside), the level saving of record x as a ratio of the seeds' means, and the gain a member (0.9 − x) × the care:\n",
      "| read | care a slot, the population | care a slot, the all-careful beside | the reviewer's care (R) | level saving of record | **the model keeps (0.9 − x) × care, real a member** | the reviewer's (R) |", "|---|---|---|---|---|---|---|"]
X = {}
for nm, P, rv, rg in (("25: M at 0.1, world 3's cell", P25, "—", "—"), ("26: M at 0.2", P26, 224, "about 110 ahead"), ("27: M at 0.3", P27, 210, "about 40 ahead"), ("28: M at 0.1, the first failure", P28, 154, "about 70 behind")):
    if not P: continue
    x = ratio_se(col(P, "rec") + col(P, "ben"), col(P, "call")); xr = ratio_se(col(P, "res") + col(P, "ben"), col(P, "call")); xl = ratio_se(col(P, "lfl_num") + col(P, "ben"), col(P, "call")); X[nm[:2]] = (x, xr, xl); care = np.mean(col(P, "call"))
    L.append(f"| {nm} | {care:.0f} | {np.mean(col(P, 'carec')):.0f} | {rv} | {pm(x, 2)} | **{(0.9 - x[0]) * care:+.0f} ± {x[1] * care:.0f}** | {rg} |")
L.append("\nThe reviewer's care (the gap over the level saving less the dose) is the measured care to within a few real, since the claims spare the dose's share of the care; the gains confirmed.\n")
if P26:
    xr = X["26"][1]; L.append(f"**AF3.3 — read 26's level saving with the reservation, and its gap.** The figure that stands is the level saving, {pm(xr, 2)}: read 26's gap with the reservation is **{mse(col(P26, 'res'))[0]:+.0f} ± {mse(col(P26, 'res'))[1]:.0f} — the population is ahead of the all-careful with the reservation, not behind** (the table of record has it with its sign, all-careful − population −13 ± 8, as read 25's −33 ± 10 and read 18's −13 ± 11 before it: the conduct's slots that depart leave later than the careful's or hold more at the exit). §121's sentence \"by 13 ± 8 with the reservation\" dropped the sign and is corrected by erratum: ahead by 13 ± 8. (−13 + 50.5) / 239 = 0.16 as the table has it; the reviewer's 0.26 took the gap as behind.\n")
# AF3.4: what the shared model misses that stays paid
def bm(E):
    rows = []
    for e in E:
        b = json.loads(e.get("bad_met_first_json") or "{}"); rows.append({k: float(v) for k, v in b.items()})
    return rows
L += ["**AF3.4 — how much of what the shared model misses stays paid**, by the leak's arithmetic (the rest of the leak a careful population's 4.8 ‰) and by the tally of the member claims at the first review:\n", "| read | dose | by the leak: (leak − (1 − q) × 4.8) / (1000 q) | the reviewer's (R) | by the tally: of the member claims on real bad work, the share that stays paid | confirmed by a member's audit / the state's / never audited |", "|---|---|---|---|---|---|"]
for nm, E, q, rv in (("25", R25, 0.1, "46 in 100"), ("26", R26, 0.2, "22"), ("27", R27, 0.3, "11")):
    if not E: continue
    B = bm(E); g = lambda k: float(np.mean([r.get(k, 0.0) for r in B])); cl = g("fa_member_claim"); paid = sum(g(k) for k in {k for r in B for k in r} if k.startswith("fa_member_claim_paid")); leak = np.mean([1000 * f(e, "leak_bad") for e in E])
    L.append(f"| {nm} | {q} | {(leak - (1 - q) * 4.8) / (1000 * q):.2f} | {rv} | **{paid / cl if cl else np.nan:.2f}** ({cl:.1f} claims a run, {paid:.1f} paid) | {g('fa_member_claim_paid_audit_member_confirmed') / paid if paid else np.nan:.2f} / {g('fa_member_claim_paid_audit_state_confirmed') / paid if paid else np.nan:.2f} / {g('fa_member_claim_paid_none') / paid if paid else np.nan:.2f} |")
L.append("\nThe leak's arithmetic confirmed; by the tally the share of a member's claims that stay paid falls with the dose as the audit seats go to the state, which is the same thing seen from the seat.\n")
if P28:
    _r1, _r2 = ratio_se(col(P28, "rec"), col(P28, "ben")), ratio_se(col(P28, "res"), col(P28, "ben")); t_rec, t_res = (1 + _r1[0], _r1[1]), (1 + _r2[0], _r2[1])
    L.append(f"**AF3.5 — where the model stops paying a population under the first failure.** By the identity, q = 0.9 / T\\* with read 28's level temptation {t_rec[0]:.1f} ± {t_rec[1]:.1f} of record: **{0.9 / t_rec[0]:.3f}** (R: 0.07; in misses in all {0.9 / t_rec[0] + (1 - 0.9 / t_rec[0]) / 20:.3f}, one bad delivery in {1 / (0.9 / t_rec[0] + (1 - 0.9 / t_rec[0]) / 20):.1f}); with the reservation {t_res[0]:.1f} ± {t_res[1]:.1f}, q = **{0.9 / t_res[0]:.3f}** (R: 0.11, one in six and a half: {1 / (0.9 / t_res[0] + (1 - 0.9 / t_res[0]) / 20):.1f}). As built the reads do not reach it: at 0.3 the model keeps a fifth of its care (AF3.2). Confirmed.\n")
    L.append(f"**AF3.6 — the relation on the care of the first failure's cell, 143 real.** 0.05 / (0.95 q) × 0.9 × 143 at q = 0.078 is {0.05 / (0.95 * 0.078) * 0.9 * 143:.0f} (R: 87), at q = {0.9 / t_rec[0]:.3f} (read 28's line for a population) {0.05 / (0.95 * 0.9 / t_rec[0]) * 0.9 * 143:.0f} (R: 101; {(0.05 / (0.95 * 0.9 / t_rec[0]) * 0.9 * 143 - 79) / 12:.1f} SE above read 23's 79 ± 12), at q = 0.1 {0.05 / (0.95 * 0.1) * 0.9 * 143:.0f} (R: 68). Confirmed to within the rounding of q.\n")
    L.append(f"**AF3.7 — how well the tests tell the two apart.** Read 28's slots are suspended {np.mean(col(P28, 'susp')):.2f} a slot against read 23's {np.mean(col(P28, 'suspc')):.2f}, **{np.mean(col(P28, 'susp')) / np.mean(col(P28, 'suspc')):.1f} times** (R: 2.2), and the population's loss of record {mse(col(P28, 'rec'))[0]:.0f} is {mse(col(P28, 'rec'))[0] / 79:.1f} times the careful's 79 (R: 2.4). Confirmed.\n")
L.append("**AF3.8 — if the tests told them apart better** (no read): by the relation the careful lose 0.05 / (0.95 q) of what the model saves — 0.53 at q = 0.1 today; with planted bad cases the model fails one time in two, 0.05 / (0.50 − 0.05) = 0.11, a fifth of it. Confirmed as arithmetic; what the relation leaves out stands (121b).\n")
# AF4.3: read 28 beside read 23, by the suspension
def susp_rows(Cd, filt=lambda v: True):
    out = []
    for s_, e in sorted(Cd.items()):
        V = [v for v in slots(e) if filt(v)]
        if not V: continue
        n = len(V); mem = 0; ends = {"member": 0, "suspended": 0, "departed": 0, "open": 0}; whole = []; dep_t = []; open_t = []
        for v in V:
            st = sorted(v.get("susp_ticks", [])); pro_t = {sp["t1"] - 1 for sp in v.get("spells", []) if sp["end"] == "suspended"}
            mem_ticks = [t for t in st if t not in pro_t]; mem += len(mem_ticks)
            for sp in v.get("spells", []):
                if sp["kind"] != "return": continue
                pre = [t for t in st if t <= sp["t0"]]; s0 = max(pre) if pre else sp["t0"] - T_SUSP
                ends[sp["end"]] += 1
                if sp["end"] == "member": whole.append(sp["t1"] - s0)
                elif sp["end"] == "departed": dep_t.append(sp["t1"] - s0)
                elif sp["end"] == "open": open_t.append(sp["t1"] - s0)
            # a suspension with no return spell yet (the slot still in its hundred ticks, or departed inside them)
        tot = sum(ends.values())
        out.append(dict(seed=s_, n=n, mem=mem / n, tot=tot / n, adm=ends["member"] / tot if tot else np.nan, sus=ends["suspended"] / tot if tot else np.nan, dep=ends["departed"] / tot if tot else np.nan, opn=ends["open"] / tot if tot else np.nan,
                        whole=np.mean(whole) if whole else np.nan, dept=np.mean(dep_t) if dep_t else np.nan, opent=np.mean(open_t) if open_t else np.nan, good=np.mean([v["ticks_good"] for v in V])))
    return out
L += ["**AF4.3 — read 28 beside read 23, by the suspension** (the suspensions as a member a slot — a suspension no probation spell ends; the way back's spells from a member's suspension: ended in a readmission, in another suspension, at a departure, or open at the run's end; the ticks from the suspension to its end, which are the good ticks lost for each, the hundred ticks off inside them):\n",
      "| population | suspensions as a member a slot | spells of the way back a slot | ended: readmitted / suspended again / departed / open | ticks lost: to the readmission / to the departure / open at the end | good ticks a slot |", "|---|---|---|---|---|---|"]
for nm, Cd in (("read 23's all-careful (θ_duty 0.20)", C23), ("read 28: case-keyed M at 0.1 on every slot (θ_duty 0.20)", D(R28)), ("world 3's all-careful", CW3 or CW3_22), ("read 25: case-keyed M at 0.1 on every slot", D(R25))):
    if not Cd: continue
    rows = susp_rows(Cd); nf = lambda k, d=0: ("—" if np.all(np.isnan(col(rows, k))) else f"{np.nanmean(col(rows, k)):.{d}f}")
    L.append(f"| {nm} | {np.mean(col(rows, 'mem')):.3f} | {np.mean(col(rows, 'tot')):.3f} | {nf('adm', 2)} / {nf('sus', 2)} / {nf('dep', 2)} / {nf('opn', 2)} | {nf('whole')} / {nf('dept')} / {nf('opent')} | {np.mean(col(rows, 'good')):.0f} |")
L.append("")
# AE3.3: the first wrong planted verdict as a member
if CW3:
    V = [v for e in CW3.values() for v in slots(e) if "pf_first_member_n" in v]; N = [min(v["pf_first_member_n"], 20) for v in V]; took = [v for v in V if v["pf_first_member_n"] <= 7]; elig0 = [v for v in V if v["pf_first_member_elig"] == 0]; by_seat = {}
    for v in V: by_seat[v["pf_first_member_seat"]] = by_seat.get(v["pf_first_member_seat"], 0) + 1
    ns = sum(len(slots(e)) for e in CW3.values())
    L += [f"**AE3.3 — how often a first failed test takes the earned seats, in world 3's all-careful.** {len(V)} of {ns} slots give a wrong planted verdict as a member within the run ({len(V) / ns:.2f}); at that verdict the window holds {np.mean(N):.1f} planted bad cases on the mean and {np.median(N):.0f} on the median (this one included; the trailing window of twenty); by the rule a first wrong takes the seats while the window holds at most seven — **{len(took) / len(V):.2f} of the first failures as a member take the earned seats at once** ({len(took)} of {len(V)}), and when the driver learns of the failure at the plant's reveal the slot is without its seats on {len(elig0) / len(V):.2f} (the record checked at every plant since; the two agree to within the plants adjudicated between the verdict and the reveal). By the seat of the first failure: " + ", ".join(f"{k} {n_}" for k, n_ in sorted(by_seat.items())) + ". So a first failed test takes the seats for about half of the careful members that ever fail one — those that fail while the window holds at most seven, the median window at the first failure being eight — and not \"usually\".\n"]
# AE3.1: the liar sweep
root = "results/redteam/stability/ablation-A1/scripted/runs"
def finals(cell, arm):
    out = {}
    for fn in glob.glob(os.path.join(root, f"*{cell}-{arm}-s*", "metrics.csv")):
        rows = list(csv.DictReader(open(fn)))
        if rows: out[int(fn.split("-s")[-1].split("/")[0])] = rows[-1]
    return out
L += ["## 2. Addendum 25's questions from the record (AE3)\n",
      "**AE3.1 — parties that appeal right rulings.** Yes: `--appeal-lie p` is the rate at which an actor appeals a rejection of its *bad* work (the driver's response step: a rejection of unfulfilled work is appealed with probability p where the truthful policy would accept; `--dispute-lie` the requester's mirror on good work's approval; 2.8.0 §8.7 (c)), 0 in every cell of record from world 3 on. From the first sweep's liar cell (§81; `scripted/runs/*liars-arm{0,1,3}-s*`: run 24's entry population with truthful disputes and both lies at 0.1, seeds 21–40, 1,000 ticks; the rows of November 10 carry the appeals by the work's truth but not the panel's road by the appeal's truth, so the panel-ended share is bounded, not split):\n",
      "| arm | lying appeals a run (`true_rejections_appealed`) | paid (`true_rejections_overturned`) | appeals lost, all | truthful appeals / paid | deciding verdicts from a panel (appeals and disputes together) | fees the lying appellants lost, nominal (D = 2 each) |", "|---|---|---|---|---|---|---|"]
for arm in ("arm0", "arm1", "arm3"):
    Fd = finals("liars", arm)
    if not Fd: continue
    g = lambda k: float(np.mean([float(Fd[s][k] or 0) for s in Fd])); se = lambda k: float(np.std([float(Fd[s][k] or 0) for s in Fd], ddof=1) / np.sqrt(len(Fd)))
    L.append(f"| {arm} ({len(Fd)} seeds) | {g('true_rejections_appealed'):.1f} ± {se('true_rejections_appealed'):.1f} | **{g('true_rejections_overturned'):.2f} ± {se('true_rejections_overturned'):.2f}** | {g('appeals_lost'):.1f} | {g('false_rejections_appealed'):.1f} / {g('false_rejections_overturned'):.1f} | {g('deciding_panel'):.1f} | {2 * (g('true_rejections_appealed') - g('true_rejections_overturned')):.0f} |")
L.append("\nUnder arm 1 none of the 33.8 lying appeals a run was paid on twenty seeds (R: under 1 in a thousand — not refuted; 0 of 676), the appellants losing 68 nominal a run in fees, 2 each; under arm 0 0.85 a run (2.1 in 100) by two wrong peers or the ruling, under arm 3 0.25 by the state's bench. How many ended at the panel with both confirming cannot be split from the record (the deciding verdicts from a panel count the disputes' too, 259 disputes a run beside 103 appeals), and that population is run 24's 60/40 with its stampers at the panels, not two careful seats; a cell in world 3's cell with `--appeal-lie 0.1` would carry the split at closure (`seats_by_kind_json`'s `dec_panel_appeal`, from November 16) — not ordered.\n")
L.append("**AE3.2 — a second filing after a confirmation** (one sentence): in `_settle_challenge` under `trusted_ruling`, where the panel settles by \"appeal reviewers\" on an appeal, leave the case in a second response window instead of PENDING, admit one `respond(\"appeal\")` more that pays a second court fee and opens the deciding verdict (`_open_deciding(c, \"second filing\")`), the fee returned from the overturned reviewer's bond where the verdict is overturned and kept by Ω where it stands — a new road of the challenge in the engine, an arm of the brief behind a flag, about a day with its invariant and tests; not built.\n")
L.append("**AE3.4 — a seating by group** (one sentence): the engine takes the reviewer the driver chooses (`assign_audit` / `assign_appeal` with the name), so a seating by group is the driver's — the wrapper of read 25 with a second salt gives every slot a group, the driver's audit and panel picks take a free panel-eligible member of the other group from the first reviewer's where one is free and fall to today's pick where none is, with the pick's group read beside — a harness construction of about an hour, no rule; not built, and the draw Baruchi's.\n")
L.append("**AF4.4 — the deciding verdict taken afresh after the state's audit** (one sentence): in `_audit_result` under arm 1, where the audit that differed is a troop's, open the deciding verdict without `first=(r.id, r.verdict)` — two fresh seats of the orchestrator's and a third on a split, the state's audit standing as the audit that differed and not as a seat — one line behind a flag of the arm, I45–I48 unchanged, a test; not built.\n")
L.append("**AF4.5 — a conduct with one dose on real cases and another on planted bad cases** (one sentence): the wrappers read the slot's own observation, which carries nothing of a case's kind, so `caseM<q>:<q_P>` would read the plant flag from the driver's own record through the env's info (`plant_record(cid)`, the orchestrator's road — outside the convention, as the `oracle` tell-reader was, and declared so), about an hour; it stands for a model that misses the kind of delivery ELEF plants, which is Baruchi's to order.\n")
L.append("**Reads 30 and 31, not run** (Baruchi's word not with the message): the ticks off at none is already an option of the harness — `--t-susp` (the driver's passthrough on `Params.T_susp`, 100 of record; §118's Z5 named it) — and the engine reads `T_susp` in one place, `_check_record`'s suspension (`suspended_until = t + T_susp`); nothing else reads it, the probation that follows the silence unchanged.\n")
# ------------------------------------------------------------------ read 29
L += ["## 3. Read 29: conduct M at 0.2 with its claims set by the case on 3 slots in 4, the rest careful — world 3's cell, seeds 21–120\n",
      "Read as read 19 was (the conduct's slots against the careful quarter beside them, each seed; the gaps of record, with the reservation and like for like; the level saving as a ratio of the seeds' means, the conduct's loss plus what its claims spared over the care on all its reviews as a member) and against read 26 by seed.\n"]
def rows_of(E, C):
    out = []
    for e in E:
        g = groups(e); s_ = int(e["seed"])
        if not g["claim"] or not g["care"] or s_ not in C: continue
        S_, Cc = stats_(g["claim"]), stats_(g["care"]); Ca = stats_(slots(C[s_])); call = S_["care_m"] + S_["claimed_m"]
        out.append(dict(seed=s_, n=S_["n"], nc=Cc["n"], rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], den=S_["brate"] * Cc["good"], call=call, claims=S_["claims"],
                        aud=S_["aud"], audc=Cc["aud"], panel=S_["panel"], panelc=Cc["panel"], rvm=S_["rvm"], rvmc=Cc["rvm"], noseat=S_["noseat"], noseatc=Cc["noseat"], undet=S_["undet"], undetc=Cc["undet"], susp=S_["susp"], suspc=Cc["susp"], reach=S_["reach"], reachc=Cc["reach"], good=S_["good"], goodc=Cc["good"],
                        life=S_["life"], lifec=Cc["life"], lifea=Ca["life"], care_vs_all=Cc["life"] - Ca["life"], aud_all=Ca["aud"], tm=S_["tm"], tmc=Cc["tm"], fai=S_["fa"], fpaid=S_["fpaid"], **{f"ss_{k}": v for k, v in state_share(e).items()}, **{f"w_{k}": v for k, v in world(e).items()}))
    return out
Q29 = rows_of(R29, CW3 or CW3_22); Q19 = rows_of(R19, CW3 or CW3_22)
if Q29:
    a, b, c = mse(col(Q29, "rec")), mse(col(Q29, "res")), mse(col(Q29, "lfl")); ta, tb, tc = 1 + ratio_se(col(Q29, "rec"), col(Q29, "ben"))[0], 1 + ratio_se(col(Q29, "res"), col(Q29, "ben"))[0], 1 + ratio_se(col(Q29, "lfl"), col(Q29, "den"))[0]
    x29 = tuple(ratio_se(col(Q29, k) + col(Q29, "ben"), col(Q29, "call")) for k in ("rec", "res", "lfl_num"))
    L += ["| read | seeds | slots a seed: conduct / careful quarter | **careful quarter − conduct, of record** (SE) | temptation | **with the reservation** | temptation | like for like | temptation | **the conduct's level saving: of record / with the reservation / like for like** | claims a slot; what they spared; the care as a member |", "|---|---|---|---|---|---|---|---|---|---|---|",
          f"| **29: M at 0.2 case-keyed on 3 in 4** | {len(Q29)} | {np.mean(col(Q29, 'n')):.1f} / {np.mean(col(Q29, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {ta:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f}) | {tb:.1f} | {c[0]:+.0f} ± {c[1]:.0f} | {tc:.1f} | **{pm(x29[0], 2)} / {pm(x29[1], 2)} / {pm(x29[2], 2)}** | {np.mean(col(Q29, 'claims')):.1f}; {np.mean(col(Q29, 'ben')):.1f}; {np.mean(col(Q29, 'call')):.0f} |"]
    if Q19:
        a19, b19, c19 = mse(col(Q19, "rec")), mse(col(Q19, "res")), mse(col(Q19, "lfl")); x19 = tuple(ratio_se(col(Q19, k) + col(Q19, "ben"), col(Q19, "call")) for k in ("rec", "res", "lfl_num"))
        L.append(f"| 19: M at 0.2 drawn at each review on 1 in 4 (the mirror, the record) | {len(Q19)} | {np.mean(col(Q19, 'n')):.1f} / {np.mean(col(Q19, 'nc')):.1f} | {a19[0]:+.0f} ± {a19[1]:.0f} | {1 + ratio_se(col(Q19, 'rec'), col(Q19, 'ben'))[0]:.1f} | {b19[0]:+.0f} ± {b19[1]:.0f} | {1 + ratio_se(col(Q19, 'res'), col(Q19, 'ben'))[0]:.1f} | {c19[0]:+.0f} ± {c19[1]:.0f} | {1 + ratio_se(col(Q19, 'lfl'), col(Q19, 'den'))[0]:.1f} | {pm(x19[0], 2)} / {pm(x19[1], 2)} / {pm(x19[2], 2)} | {np.mean(col(Q19, 'claims')):.1f}; {np.mean(col(Q19, 'ben')):.1f}; {np.mean(col(Q19, 'call')):.0f} |")
    cva = mse(col(Q29, "care_vs_all"))
    L += ["\n**The seats, the time without them, the careful quarter against world 3's all-careful, and the state's share** (the reviewer's four readings):\n",
          "| group | audit seats a slot | panel seats a slot | member reviews a slot | member ticks without the earned seats (share) | … the record undetermined | suspended at least once (share); suspensions a slot | good ticks a slot | the slot's lifetime of record |", "|---|---|---|---|---|---|---|---|---|",
          f"| the conduct's slots (3 in 4) | {np.mean(col(Q29, 'aud')):.1f} | {np.mean(col(Q29, 'panel')):.1f} | {np.mean(col(Q29, 'rvm')):.1f} | **{np.nanmean(col(Q29, 'noseat')):.3f}** | {np.nanmean(col(Q29, 'undet')):.3f} | {np.mean(col(Q29, 'reach')):.2f}; {np.mean(col(Q29, 'susp')):.2f} | {np.mean(col(Q29, 'good')):.0f} | {np.mean(col(Q29, 'life')):.0f} |",
          f"| the careful quarter | **{np.mean(col(Q29, 'audc')):.1f}** | {np.mean(col(Q29, 'panelc')):.1f} | {np.mean(col(Q29, 'rvmc')):.1f} | {np.nanmean(col(Q29, 'noseatc')):.3f} | {np.nanmean(col(Q29, 'undetc')):.3f} | {np.mean(col(Q29, 'reachc')):.2f}; {np.mean(col(Q29, 'suspc')):.2f} | {np.mean(col(Q29, 'goodc')):.0f} | {np.mean(col(Q29, 'lifec')):.0f} |",
          f"| world 3's all-careful (every slot) | {np.mean(col(Q29, 'aud_all')):.1f} | | | | | | | {np.mean(col(Q29, 'lifea')):.0f} |",
          f"\nThe careful quarter's slot against world 3's all-careful slot of record, by seed: **{cva[0]:+.0f} ± {cva[1]:.0f}** ({cva[0] / cva[1]:.1f} SE). The state's share of the seats: the first review {np.nanmean(col(Q29, 'ss_first')):.3f}, the audit seat **{np.nanmean(col(Q29, 'ss_audit')):.3f}**, the panels {np.nanmean(col(Q29, 'ss_panel')):.3f} (world 3's all-careful 0.000 / 0.317 / 0.235; read 26's 0.000 / 0.702 / 0.589).\n"]
    # who met the bad deliveries
    B29 = bm(R29)
    if B29:
        g = lambda k: float(np.mean([r.get(k, 0.0) for r in B29])); tot = g("first_member") + g("first_probation") + g("first_state"); cl = g("fa_member_claim"); paid = sum(g(k) for k in {k for r in B29 for k in r} if k.startswith("fa_member_claim_paid")); ovt = cl - paid
        ovs = {k[len("fa_member_claim_overturned_"):]: g(k) for k in {k for r in B29 for k in r} if k.startswith("fa_member_claim_overturned_")}; st_ov = sum(v for k, v in ovs.items() if k.startswith("audit_state")); me_ov = sum(v for k, v in ovs.items() if k.startswith("audit_member"))
        L.append(f"**Who met the bad deliveries, as read 25 gave it.** Of {tot:.0f} real bad deliveries closed a run, {g('first_member') / tot:.2f} reviewed first by a member, {g('first_probation') / tot:.2f} on probation, {g('first_state') / tot:.3f} the state. Of the {cl:.1f} a run a member of the conduct claimed on at the first review, **{paid / cl if cl else np.nan:.2f} stayed paid** ({g('fa_member_claim_paid_audit_member_confirmed') / paid if paid else np.nan:.2f} of them confirmed by a member's audit, {g('fa_member_claim_paid_audit_state_confirmed') / paid if paid else np.nan:.2f} by the state's, {g('fa_member_claim_paid_none') / paid if paid else np.nan:.2f} never audited) and {ovt / cl if cl else np.nan:.2f} were overturned — **{me_ov / ovt if ovt else np.nan:.2f} of them after a member's audit differed** (the careful quarter's seats, which read 26 did not have: read 25's 0.00) and {st_ov / ovt if ovt else np.nan:.2f} after the state's. The careful errors beside: {g('fa_member_care'):.1f} a run by members, {g('fa_probation_care'):.1f} on probation.\n")
    # against read 26 by seed
    if P26:
        A_ = {r["seed"]: r for r in P26}; sd = sorted(set(A_) & {r["seed"] for r in Q29}); B_ = {r["seed"]: r for r in Q29}
        L += ["\n**Read 29 against read 26 by seed** — the conduct's slots (read 26's every slot on the conduct; read 29's three in four) and the world's side:\n", "| measure | read 26 | read 29 | **read 29 − read 26** (SE from nothing) |", "|---|---|---|---|"]
        for k26, k29, nm, d in (("life", "life", "the conduct's slot, lifetime of record", 0), ("rvm", "rvm", "member reviews a conduct slot", 1), ("susp", "susp", "suspensions a conduct slot", 2), ("good", "good", "good ticks a conduct slot", 0)):
            dd = mse([B_[s][k29] - A_[s][k26] for s in sd]); L.append(f"| {nm} | {np.mean([A_[s][k26] for s in sd]):.{d}f} | {np.mean([B_[s][k29] for s in sd]):.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
        for k, kk, nm, d in WK:
            dd = mse([B_[s][f"w_{k}"] - A_[s][f"w_{k}"] for s in sd]); L.append(f"| {nm} | {np.mean([A_[s][f'w_{k}'] for s in sd]):.{d}f} | {np.mean([B_[s][f'w_{k}'] for s in sd]):.{d}f} | **{dd[0]:+.{d}f} ± {dd[1]:.{d}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
    # expectations
    L += ["\n## 4. Against the expectations stated before the run (AF5), and the condition\n"]
    chk(in_band(np.mean(col(Q29, "audc")), 50, 95), f"read 29: the careful quarter holds 50 to 95 audit seats a slot (the all-careful's 35.8): {np.mean(col(Q29, 'audc')):.1f}."); chk(in_band(cva[0], 45, 265), f"read 29: the careful quarter's slot 45 to 265 real above world 3's all-careful slot of record: {cva[0]:+.0f} ± {cva[1]:.0f}.")
    chk(in_band(np.nanmean(col(Q29, "noseat")), 0.85, 0.95), f"read 29: the conduct's slots without their earned seats on 0.85 to 0.95 of their member ticks: {np.nanmean(col(Q29, 'noseat')):.3f}."); chk(in_band(np.nanmean(col(Q29, "ss_audit")), 0.33, 0.60), f"read 29: the state holds 0.33 to 0.60 of the audit seats: {np.nanmean(col(Q29, 'ss_audit')):.3f}.")
    chk(in_band(a[0], 170, 460), f"read 29: the conduct's slots behind the careful quarter by 170 to 460 real of record: {a[0]:+.0f} ± {a[1]:.0f}."); chk(in_band(x29[0][0], 0.95, 2.6), f"read 29: a level saving of 0.95 to 2.6 of record: {pm(x29[0], 2)}.")
    chk(in_band(np.mean(col(Q29, "w_leak")), 20, 38), f"read 29: a leak of 20 to 38 in a thousand bad deliveries: {np.mean(col(Q29, 'w_leak')):.1f}."); chk(in_band(np.mean(col(Q29, "w_fa")), 10, 19), f"read 29: standing false approvals of 10 to 19 a run: {np.mean(col(Q29, 'w_fa')):.1f}."); chk(in_band(np.mean(col(Q29, "w_oh")), 13.5, 15.6), f"read 29: an overhead of 13.5 to 15.6: {np.mean(col(Q29, 'w_oh')):.2f}.")
    L += CHK; L.append(f"\n**{sum(1 for c_ in CHK if c_.startswith('- MET'))} of {len(CHK)} expectations met.**\n")
    x = x29[0]; L.append(verdict(f"*Among members of whom most are on a model that misses a quarter of the bad work, a member does better careful than on the model*: shown if read 29's level saving of the conduct's slots against the careful quarter is above 0.9 by two standard errors of record; refuted if it is under 0.9 at the point value. Read 29's is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] - 2 * x[1] > 0.9, x[0] < 0.9))
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("wrote", sys.argv[1], len(L), "lines")
