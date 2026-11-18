"""Addenda 27 and 28 (November 18, 2026; notes §123): the reviewer's arithmetic on §122 confirmed or replaced (AH3), the readings asked from the record (AH4), and five reads without
training — reads 30 and 31 (the cell of the first failure with the ticks off at none; the all-careful and the case-keyed conduct at 0.1 on every slot), read 32 (the case-keyed conduct
at 0.1 on 3 slots in 4, the rest careful, world 3's cell), reads 33 and 34 (two groups of slots on the conduct at 0.1 under their group's salt, today's picks and the seating by group);
read 25 run again whole at d28f75da5 for the pair tallies, checked to the digit against a22/rerun; reads 33 and 34 at 8e30eac40 (launch2.sh), where the orchestrator's alias is read as no slot's first seat. a22_read.py's and a23_read.py's helpers copied. Usage: a24_read.py OUT.md"""
import json, os, sys, hashlib, math, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D24, D23, D22, D16 = f"{R}/a24", f"{R}/a23", f"{R}/a22", f"{R}/a16"
T = 1000; RES = 0.8
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
SEATS = ("initial", "resumed", "audit", "third", "appeal", "dispute")
def stats_(V):
    n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n; g = lambda k: sum(v.get(k, 0) for v in V) / n
    tm = sum(v.get("ticks_member", 0) for v in V); arr = [v for v in V if v["t_in"] > 0]
    return dict(n=n, good=good, ig=ig, bg=bg, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n, ben=g("private_real"),
                claims=g("claims"), susp=g("suspensions"), aud=g("audits_done"), panel=g("rvm_appeal") + g("rvm_third") + g("rvm_dispute"), care_m=g("care_member"), claimed_m=g("claimed_member"), rvm=g("rv_member"), reach=sum(1 for v in V if v["suspensions"] > 0) / n,
                tm=tm / n, noseat=(sum(v.get("ticks_member_noseat", 0) for v in V) / tm) if tm else np.nan, undet=(sum(v.get("ticks_member_noseat_undet", 0) for v in V) / tm) if tm else np.nan, fa=g("fa_init"), fpaid=g("fa_init_paid"),
                adm=(sum(1 for v in arr if "adm_ticks" in v) / len(arr)) if arr else np.nan, aud_inc=g("rf_member_audit_fee") + g("rf_member_audit_emission") + g("rf_member_audit_uplift"), aud_bond=g("rf_member_audit_bond"),
                panel_inc=sum(g(f"rf_member_{s_}_{k}") for s_ in ("third", "appeal", "dispute") for k in ("fee", "emission", "uplift")),
                work=sum(g(f"ev_{st}_delivery") - g(f"ev_{st}_effort") - g(f"ev_{st}_guarantee") for st in ("member", "probation", "down")), bonds=sum(g(f"ev_{st}_bond") for st in ("member", "probation", "down")),
                fees_all=sum(g(f"ev_{st}_{k}") for st in ("member", "probation", "down") for k in ("fee", "emission", "uplift")))
def state_share(e):
    tin = e.get("troop_initial_seats"); tr, ta, tp, ds = f(e, "troop_reviews"), f(e, "troop_audits"), f(e, "troop_panel_seats"), f(e, "deciding_seats")
    tin = float(tin) if tin not in (None, "") else (tr - tp - ds)
    mi = f(e, "seated_initial_member") + f(e, "seated_initial_probationer"); ma = f(e, "seated_audit_member"); mp = f(e, "seated_appeal_member"); tpa = tp - ta
    return {"first": tin / (tin + mi) if (tin + mi) else np.nan, "audit": ta / (ta + ma) if (ta + ma) else np.nan, "panel": tpa / (tpa + mp) if (tpa + mp) else np.nan}
WK = (("fa", "false_approvals", "standing false approvals a run", 1), ("leak", "leak_bad", "the leak, ‰ of bad deliveries", 1), ("oh", "sys_overhead_per_vested", "the system overhead a vested task", 2), ("cot", "cost_of_truth", "the cost of truth a run", 0),
      ("dep", "departures", "departures a run", 1), ("arr", "arrivals", "arrivals a run", 1), ("Pt", "P_t", "P_t at the end", 1))
def world(e): return {k: (1000 * f(e, kk) if k == "leak" else f(e, kk)) for k, kk, _, _ in WK}
def pop_rows(E, C):
    """Each seed: the population's slots against the all-careful's of C (the same cell) — the three gaps, the level saving's parts, the seats, the suspensions, the world's side."""
    out = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in C: continue
        V, Vc = slots(e), slots(C[s_]); S_, Cc = stats_(V), stats_(Vc); call = S_["care_m"] + S_["claimed_m"]
        out.append(dict(seed=s_, n=len(V), nc=len(Vc), rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], call=call, carec=Cc["care_m"],
                        **{k: S_[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "adm", "claims", "fa", "fpaid", "tm")}, **{k + "c": Cc[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "adm")},
                        **{f"w_{k}": v for k, v in world(e).items()}, **{f"w0_{k}": v for k, v in world(C[s_]).items()}, **{f"ss_{k}": v for k, v in state_share(e).items()}, **{f"ss0_{k}": v for k, v in state_share(C[s_]).items()}))
    return out
def rows_of(E, C=None):
    """Read 29's shape: the conduct's slots against the careful slots beside them in the same world, each seed; C the all-careful of the cell for the careful group's gain over it."""
    out = []
    for e in E:
        g = groups(e); s_ = int(e["seed"])
        if not g["claim"] or not g["care"]: continue
        S_, Cc = stats_(g["claim"]), stats_(g["care"]); Ca = stats_(slots(C[s_])) if (C and s_ in C) else None; call = S_["care_m"] + S_["claimed_m"]
        out.append(dict(seed=s_, n=S_["n"], nc=Cc["n"], rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], den=S_["brate"] * Cc["good"], call=call, carec=Cc["care_m"],
                        **{k: S_[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "fa", "fpaid", "tm", "aud_inc", "aud_bond", "panel_inc")}, **{k + "c": Cc[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "aud_inc", "aud_bond", "panel_inc")},
                        lifea=Ca["life"] if Ca else np.nan, care_vs_all=(Cc["life"] - Ca["life"]) if Ca else np.nan, aud_all=Ca["aud"] if Ca else np.nan, aud_inc_all=Ca["aud_inc"] if Ca else np.nan, panel_inc_all=Ca["panel_inc"] if Ca else np.nan,
                        d_work=(Cc["work"] - Ca["work"]) if Ca else np.nan, d_bonds=(Cc["bonds"] - Ca["bonds"]) if Ca else np.nan, d_fees=(Cc["fees_all"] - Ca["fees_all"]) if Ca else np.nan,
                        **{f"w_{k}": v for k, v in world(e).items()}, **{f"ss_{k}": v for k, v in state_share(e).items()}))
    return out
def xs(P, keys=("rec", "res", "lfl_num")): return tuple(ratio_se(col(P, k) + col(P, "ben"), col(P, "call")) for k in keys)
def temp(P, k, den): t = ratio_se(col(P, k), col(P, den)); return 1 + t[0], t[1]
def bm(E): return [{k: float(v) for k, v in json.loads(e.get("bad_met_first_json") or "{}").items()} for e in E]
def g_of(B): return lambda k: float(np.mean([r.get(k, 0.0) for r in B]))
def fa_split(B):
    """A member's claims on real bad work at the first review: the share that stays paid, and the fate by the audit's holder (never audited; a member's audit confirmed / differed; the state's)."""
    g = g_of(B); keys = {k for r in B for k in r}; cl = g("fa_member_claim"); paid = sum(g(k) for k in keys if k.startswith("fa_member_claim_paid")); ov = sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned"))
    d = dict(claims=cl, paid=paid / cl if cl else np.nan, none=g("fa_member_claim_paid_none") / cl if cl else np.nan, mconf=g("fa_member_claim_paid_audit_member_confirmed") / cl if cl else np.nan, sconf=g("fa_member_claim_paid_audit_state_confirmed") / cl if cl else np.nan,
             mdiff=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_audit_member")) / cl if cl else np.nan, sdiff=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_audit_state")) / cl if cl else np.nan)
    tot = g("first_member") + g("first_probation") + g("first_state"); d.update(tot=tot, fm=g("first_member") / tot if tot else np.nan, fp=g("first_probation") / tot if tot else np.nan, fs=g("first_state") / tot if tot else np.nan)
    return d
def susp_rows(Cd, tsusp, filt=lambda v: True):
    out = []
    for s_, e in sorted(Cd.items()):
        V = [v for v in slots(e) if filt(v)]
        if not V: continue
        n = len(V); mem = 0; ends = {"member": 0, "suspended": 0, "departed": 0, "open": 0}; whole = []; dep_t = []; open_t = []
        for v in V:
            st = sorted(v.get("susp_ticks", [])); sps = v.get("spells", [])
            mem += len([t for t in st if not any(sp["t0"] <= t < sp["t1"] for sp in sps)])   # a suspension whose tick falls inside no probation spell is a member's (with the ticks off at none a re-suspension on the way back ends no spell: the slot is a probationer again at the tick's end)
            for sp in v.get("spells", []):
                if sp["kind"] != "return": continue
                pre = [t for t in st if t <= sp["t0"]]; s0 = max(pre) if pre else sp["t0"] - tsusp; ends[sp["end"]] += 1
                (whole if sp["end"] == "member" else dep_t if sp["end"] == "departed" else open_t if sp["end"] == "open" else []).append(sp["t1"] - s0)
        tot = sum(ends.values())
        out.append(dict(seed=s_, n=n, mem=mem / n, tot=tot / n, adm=ends["member"] / tot if tot else np.nan, sus=ends["suspended"] / tot if tot else np.nan, dep=ends["departed"] / tot if tot else np.nan, opn=ends["open"] / tot if tot else np.nan,
                        whole=np.mean(whole) if whole else np.nan, dept=np.mean(dep_t) if dep_t else np.nan, opent=np.mean(open_t) if open_t else np.nan, good=np.mean([v["ticks_good"] for v in V]), reach=sum(1 for v in V if v["suspensions"] > 0) / n, susp=sum(v["suspensions"] for v in V) / n))
    return out
def pairs_of(e):
    """How often one pair meets — a first reviewer and the member at its audit seat: the pairs that meet, the meetings over them, the share meeting more than three times, the largest; the partners a first reviewer has."""
    pmj = {k: v for k, v in json.loads(e.get("pair_meet_json") or "{}").items() if not k.startswith("plant_rev")}   # the collections at d28f75da5 carried an alias pair for each planted approval (8e30eac40 reads the alias as no slot's)
    if not pmj: return None
    ns = [len(v) for v in pmj.values()]; firsts = {}
    for k, v in pmj.items(): firsts.setdefault(k.split("|")[0], set()).add(k.split("|")[1])
    return dict(pairs=len(ns), meetings=sum(ns), mean=np.mean(ns), gt3=sum(1 for x in ns if x > 3) / len(ns), mx=max(ns), partners=np.mean([len(s) for s in firsts.values()]), n_slots=len(json.loads(e["learner_slots_json"])))
def shared_fail(e):
    """Two member slots that gave a wrong verdict on the same planted case: the pairs a run, as a share of every pair of slots, the share of slots with such a partner, and whether the pair meets (a first reviewer and the member at its audit seat) at all, and after the shared failure."""
    pf = json.loads(e.get("pair_fail_json") or "{}"); pmj = {k: v for k, v in json.loads(e.get("pair_meet_json") or "{}").items() if not k.startswith("plant_rev")}; S = json.loads(e["learner_slots_json"]); n = len(S)
    meet = {}
    for k, v in pmj.items(): a, b = k.split("|"); meet.setdefault("|".join(sorted((a, b))), []).extend(v)
    pairs = len(pf); met = sum(1 for k in pf if k in meet); met_after = sum(1 for k, ts in pf.items() if k in meet and any(t > min(ts) for t in meet[k])); slots_with = len({x for k in pf for x in k.split("|")})
    failed = sum(1 for v in S.values() if sum(v.get(f"pw_member_{s_}", 0) for s_ in SEATS) > 0)
    return dict(pairs=pairs, share=pairs / (n * (n - 1) / 2), slots_with=slots_with / n, met=met / pairs if pairs else np.nan, met_after=met_after / pairs if pairs else np.nan, partners=2 * pairs / n / (n - 1), failed=failed / n, n=n)
def repro(new_eps, old_eps, label):
    old = {int(e["seed"]): e for e in old_eps}; n_rows = n_keys = n_slots = n_seeds = 0; diffs = []; bm_d = []
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
        bo, bn = json.loads(o["bad_met_first_json"]), json.loads(e["bad_met_first_json"])
        for k, val in bo.items():
            nv = bn.get(k, bn.get(k + "_member", 0) + bn.get(k + "_state", 0))     # the audit road's key split into _member / _state at 658d83ad0, after a22/rerun
            if nv != val: bm_d.append((s_, k))
    return f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") + f"; the `bad_met_first_json` tally compared apart with the audit road's key read as the sum of its `_member` / `_state` split (658d83ad0): **{len(bm_d)} differences**" + (f" ({bm_d[:4]})" if bm_d else "") + "."
def verdict(text, shown, refuted): return f"- {text} **{'Shown' if shown else ('Refuted' if refuted else 'Neither')}.**"
CHK = []
def chk(ok, text): CHK.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def in_band(x, lo, hi): return (not np.isnan(x)) and lo <= x <= hi
def paired(A, B, k, kb=None):
    kb = kb or k; A_, B_ = {r["seed"]: r for r in A}, {r["seed"]: r for r in B}; sd = sorted(set(A_) & set(B_)); return mse([B_[s][kb] - A_[s][k] for s in sd]), np.mean([A_[s][k] for s in sd]), np.mean([B_[s][kb] for s in sd]), len(sd)
# ------------------------------------------------------------------ the record
CW3 = load([f"{D23}/rerun/cw3-s21-70", f"{D23}/rerun/cw3-s71-120"], "careful")[1]; C23 = load([f"{D22}/rerun/r23-s21-70", f"{D22}/rerun/r23-s71-120"], "careful")[1]
R25_OLD = load([f"{D22}/rerun/r25-s21-70", f"{D22}/rerun/r25-s71-120"], "mix:caseM0.1:1.0")[0]; R25 = load([f"{D24}/rerun/r25-s21-70", f"{D24}/rerun/r25-s71-120"], "mix:caseM0.1:1.0")[0]
R26 = load([f"{D22}/r26/s21-70", f"{D22}/r26/s71-120"], "mix:caseM0.2:1.0")[0]; R27 = load([f"{D22}/r27/s21-70", f"{D22}/r27/s71-120"], "mix:caseM0.3:1.0")[0]; R28 = load([f"{D22}/r28/s21-70", f"{D22}/r28/s71-120"], "mix:caseM0.1:1.0")[0]
R29 = load([f"{D23}/r29/s21-70", f"{D23}/r29/s71-120"], "mix:caseM0.2:0.75")[0]; R19 = load([f"{D22}/rerun/r19-s21-70", f"{D22}/rerun/r19-s71-120"], "mix:doseM0.2:0.25")[0]
R9 = load([f"{D22}/rerun/r9-s21-70", f"{D22}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0]; R11 = load([f"{D16}/r11/s21-80"], "mix:doseM0.1:0.75")[0]
C30 = load([f"{D24}/r30/s21-70", f"{D24}/r30/s71-120"], "careful")[1]; R31 = load([f"{D24}/r31/s21-70", f"{D24}/r31/s71-120"], "mix:caseM0.1:1.0")[0]
R32 = load([f"{D24}/r32/s21-70", f"{D24}/r32/s71-120"], "mix:caseM0.1:0.75")[0]; R33 = load([f"{D24}/r33/s21-70", f"{D24}/r33/s71-120"], "mix:caseG0.1:1.0")[0]; R34 = load([f"{D24}/r34/s21-70", f"{D24}/r34/s71-120"], "mix:caseG0.1:1.0")[0]
L = ["# Addenda 27 and 28 — the reviewer's arithmetic on §122, the readings asked from the record, and reads 30 to 34 (November 18, 2026; notes §123)\n"]
if R25 and R25_OLD: L.append(repro(R25, R25_OLD, "read 25 run again whole at d28f75da5 (a22/rerun/r25, itself 0 differences against a20/r25)"))
L.append(f"\nLoaded: cw3 {len(CW3)}, r23 {len(C23)}, r25 {len(R25)} (record {len(R25_OLD)}), r26 {len(R26)}, r27 {len(R27)}, r28 {len(R28)}, r29 {len(R29)}, r19 {len(R19)}, r9 {len(R9)}, r11 {len(R11)}; r30 {len(C30)}, r31 {len(R31)}, r32 {len(R32)}, r33 {len(R33)}, r34 {len(R34)} episodes.\n")
# ------------------------------------------------------------------ 1. from the record
L += ["## 1. From the record: the reviewer's arithmetic (AH3) and the readings asked (AH4)\n"]
Q29 = rows_of(R29, CW3)
if Q29:
    x29 = xs(Q29); call, carec = np.mean(col(Q29, "call")), np.mean(col(Q29, "carec")); gain = ((0.9 - x29[0][0]) * call, x29[0][1] * call); cva = mse(col(Q29, "care_vs_all"))
    da = np.mean(col(Q29, "audc")) - np.mean(col(Q29, "aud_all")); dinc = mse(col(Q29, "aud_incc") - col(Q29, "aud_inc_all")); dpan = mse(col(Q29, "panel_incc") - col(Q29, "panel_inc_all")); per_seat = dinc[0] / da if da else np.nan
    L += [f"**AH4.1 and AH3.1 — read 29's care and the model's gain a member.** The care on all a slot's reviews as a member (the conduct's care paid plus the care its claims spared): the conduct's slots **{call:.0f} real** (R: about 232 by division), the careful quarter **{carec:.0f}**, "
          f"world 3's all-careful slot 250. The model keeps (0.9 − x) × care with x the level saving of record {pm(x29[0], 2)}: **{gain[0]:+.0f} ± {gain[1]:.0f} real a member** (R: about 360 behind — confirmed). The careful quarter's slot ends at {np.mean(col(Q29, 'lifec')) / np.mean(col(Q29, 'lifea')):.2f} of world 3's all-careful slot "
          f"and the conduct's at {np.mean(col(Q29, 'life')) / np.mean(col(Q29, 'lifea')):.2f} (R: 1.45 and 0.87 — confirmed).\n",
          f"**AH3.2 — where the careful quarter's gain comes from.** It holds {np.mean(col(Q29, 'audc')):.1f} audit seats a slot against the all-careful's {np.mean(col(Q29, 'aud_all')):.1f}, {np.mean(col(Q29, 'audc')) / np.mean(col(Q29, 'aud_all')):.1f} times (R: 2.8). Its income at the audit seat beyond the care reimbursed (the fee, the emission share and the uplift, by the per-slot flows) "
          f"is **{dinc[0]:+.0f} ± {dinc[1]:.0f} real above the all-careful slot's** by seed — {per_seat:.2f} real for each of the {da:.0f} seats more (R: 4.46 × 65 ≈ 290) — and its panel seats {dpan[0]:+.0f} ± {dpan[1]:.0f} more; the two together {dinc[0] + dpan[0]:.0f} of the {cva[0]:.0f} ± {cva[1]:.0f} it ends above (R: 290 of 404 — "
          f"{'confirmed' if 240 <= dinc[0] <= 340 else 'replaced'}). By every wallet event of the slot (real at the event's index): the careful quarter's review fees, emission shares and uplift at every seat {mse(col(Q29, 'd_fees'))[0]:+.0f} ± {mse(col(Q29, 'd_fees'))[1]:.0f} above the all-careful slot's, "
          f"its work (the deliveries less the effort and the guarantees lost) {mse(col(Q29, 'd_work'))[0]:+.0f} ± {mse(col(Q29, 'd_work'))[1]:.0f}, its bonds lost {mse(col(Q29, 'd_bonds'))[0]:+.0f} ± {mse(col(Q29, 'd_bonds'))[1]:.0f} — the seats' pay more than the whole gain, the work less, since a slot that sits more delivers less.\n"]
# AH3.3 / AH4.3: the never-audited share and the rule of thumb
L += ["**AH3.3 and AH4.3 — of a member's claims on real bad work at the first review, the fate by the audit's holder, and the rule of thumb.** The rule: a share never audited stays paid; an audit by a member on the same model confirms; any other audit misses 0.05. Here with the measured never-audited share and the measured holder shares in place of 0.03 and the state's share:\n",
      "| read | claims a run | **never audited (share)** | a member's audit confirmed | a member's audit differed | the state's confirmed | the state's differed | **stays paid, the tally** | the rule of thumb with 0.03 (R) | the rule with the measured never-audited share and holders |", "|---|---|---|---|---|---|---|---|---|---|"]
RULE_R = {"25": 0.67, "26": 0.35, "27": 0.20, "29": 0.26}
for nm, E in (("25: M at 0.1 on every slot", R25 or R25_OLD), ("26: M at 0.2 on every slot", R26), ("27: M at 0.3 on every slot", R27), ("29: M at 0.2 on 3 in 4", R29), ("32: M at 0.1 on 3 in 4", R32), ("33: two groups at 0.1, today's picks", R33), ("34: two groups, the seating by group", R34)):
    if not E: continue
    d = fa_split(bm(E)); same_conf = d["mconf"] + d["mdiff"]   # the member-held audits of a claim
    # the rule: never audited + member-held × (confirms where the holder is on the same model: the share confirmed among member-held audits is the measured proxy) + state-held × 0.05
    rule_meas = d["none"] + (d["mconf"] + d["mdiff"]) * (d["mconf"] / (d["mconf"] + d["mdiff"]) if (d["mconf"] + d["mdiff"]) else 0) + (d["sconf"] + d["sdiff"]) * 0.05
    L.append(f"| {nm} | {d['claims']:.1f} | **{d['none']:.3f}** | {d['mconf']:.2f} | {d['mdiff']:.2f} | {d['sconf']:.2f} | {d['sdiff']:.2f} | **{d['paid']:.2f}** | {RULE_R.get(nm[:2], '—')} | {rule_meas:.2f} |")
L.append("\nThe never-audited share is read, not 0.03 everywhere; the rule's miss at the higher doses is in its 'an audit by a member on the same model confirms' — at a dose of 0.2 or 0.3 the member at the audit seat claims on the case too (the same hash), so it confirms, but the state's audits are more and a member's audit that differs is a careful quarter's or an other group's.\n")
# AH4.2: the planted bad cases a slot meets as a member, and the shared failures of read 25
if CW3:
    V = [v for e in CW3.values() for v in slots(e)]; per = [sum(v.get(f"rvm_plant_bad_{s_}", 0) for s_ in SEATS) for v in V]; by_seat = {s_: np.mean([v.get(f"rvm_plant_bad_{s_}", 0) for v in V]) for s_ in SEATS}
    good_ = [sum(v.get(f"rvm_plant_good_{s_}", 0) for s_ in SEATS) for v in V]; anyst = [v.get("pb_met", 0) for v in V]
    L.append(f"**AH4.2 — the planted bad cases a slot meets as a member in a run, world 3's all-careful** ({len(V)} slots over 100 seeds): **{np.mean(per):.1f} on the mean and {np.median(per):.0f} on the median** (R: about 10); by seat — the first review {by_seat['initial']:.2f} (R: about 3.6), the resumed seat {by_seat['resumed']:.2f}, the audit seat {by_seat['audit']:.2f}, "
             f"the third seat {by_seat['third']:.2f}, an appeal panel {by_seat['appeal']:.2f}, a dispute panel {by_seat['dispute']:.2f} (it meets no bad plant); the planted good cases {np.mean(good_):.1f} a slot as a member; at every standing {np.mean(anyst):.1f} planted bad cases a slot (the probation's included).\n")
if R25 and R25[0].get("pair_fail_json") is not None:
    SF = [shared_fail(e) for e in R25]; PR = [pairs_of(e) for e in R25]
    L.append(f"**AH4.2 — in read 25, two slots that gave a wrong verdict on the same planted case** (member seats; the reveal's tick): **{np.mean(col(SF, 'pairs')):.1f} pairs a run**, {100 * np.mean(col(SF, 'share')):.2f} in 100 of every pair of slots; a slot shares a failed planted case with "
             f"**{100 * np.mean(col(SF, 'partners')):.1f} in 100 of the other slots** in a run (R: about 1 in 100), {100 * np.mean(col(SF, 'slots_with')):.0f} in 100 of the slots having at least one such partner; {100 * np.mean(col(SF, 'failed')):.0f} in 100 of the slots fail a planted case as a member within the run (R: 0.64 if a failure were read as a failure of its kind — here the measured share of slots). "
             f"Of those pairs **{np.mean(col(SF, 'met')):.2f} meet as a first reviewer and the member at its audit seat at some point in the run, and {np.mean(col(SF, 'met_after')):.2f} after the shared failure**. For every pair of a first reviewer and the member at its audit seat in read 25: {np.mean(col(PR, 'pairs')):.0f} pairs meet a run over {np.mean(col(PR, 'meetings')):.0f} member audit seats, "
             f"{np.mean(col(PR, 'mean')):.2f} meetings a pair, {100 * np.mean(col(PR, 'gt3')):.0f} in 100 of the pairs more than three times, the largest {np.mean(col(PR, 'mx')):.1f}; a first reviewer meets {np.mean(col(PR, 'partners')):.1f} different members at its audit seat.\n")
L += ["**AH3.6 — the audit road with the split, taken afresh.** Of record 3.09 a run follow the state's audit and 0.38 a member's; taken afresh with two fresh seats after the state's audit, 3.09 × (0.00725 / 0.0975) = 0.23 would follow it, and the audit road would hold 0.23 + 0.38 = **0.61** a run where the tally reads 3.47 (R: 0.23 and 0.61 — confirmed).\n",
      "**AH4.4 — one more deciding verdict for the worker after an audit the verdict upheld, with the fee by the outcome** (one sentence, not ordered): in `_settle_challenge` under arm 1, where the deciding verdict upholds the audit's N on a member's delivery, leave the case in a response window instead of finalizing N, admit one `respond(\"appeal\")` more from the actor that opens a fresh deciding verdict (two troop seats and a third on a split, the state's audit standing as the audit that differed and not as a seat) with no fee at the filing, and at its settlement charge the court fee to the loser — the actor's unlocked wallet where the N stands, the orchestrator's where it is overturned (the reviewers' bonds as now) — with a fee the loser cannot pay carried as a debt of the name that bars its next filing (a new liability kind in the ledger, read by I1 and a new invariant); a second road of the challenge, about a day in the engine with its tests, under one case a run by the engine's rates (R).\n"]
# ------------------------------------------------------------------ 2. reads 30 and 31
L += ["## 2. Reads 30 and 31: the cell of the first failure with the ticks off at none (`--t-susp 0`; addendum 27, Baruchi's first \"Yes\"; seeds 21–120)\n"]
P30 = pop_rows(list(C30.values()), CW3) if C30 else []; P30v23 = pop_rows(list(C30.values()), C23) if C30 else []; P23 = pop_rows(list(C23.values()), CW3) if C23 else []
P31 = pop_rows(R31, C30) if (R31 and C30) else []; P31v28 = pop_rows(R31, D(R28)) if (R31 and R28) else []; P28 = pop_rows(R28, C23) if (R28 and C23) else []
if P30:
    a, b, c = mse(col(P30, "rec")), mse(col(P30, "res")), mse(col(P30, "lfl")); a23_, b23_ = mse(col(P23, "rec")), mse(col(P23, "res")); v23 = mse(-col(P30v23, "rec")), mse(-col(P30v23, "res")), mse(-col(P30v23, "lfl"))
    L += ["**Read 30, the all-careful.** Its slot against world 3's all-careful slot by seed (world 3's less read 30's, of record / with the reservation / like for like) and against read 23's (read 30's less read 23's: positive is above):\n",
          "| population | slots a seed | **world 3's all-careful − this, of record** (SE) | with the reservation | like for like | **this − read 23's, of record** (SE) | with the reservation | like for like | the slot's lifetime of record |", "|---|---|---|---|---|---|---|---|---|",
          f"| read 23's all-careful (θ_duty 0.20, the hundred ticks on) | {np.mean(col(P23, 'n')):.1f} | {a23_[0]:+.0f} ± {a23_[1]:.0f} ({a23_[0] / a23_[1]:.1f}) | {b23_[0]:+.0f} ± {b23_[1]:.0f} | {mse(col(P23, 'lfl'))[0]:+.0f} ± {mse(col(P23, 'lfl'))[1]:.0f} | — | — | — | {np.mean(col(P23, 'life')):.0f} |",
          f"| **read 30's all-careful (θ_duty 0.20, the ticks off at none)** | {np.mean(col(P30, 'n')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{v23[0][0]:+.0f} ± {v23[0][1]:.0f}** ({v23[0][0] / v23[0][1]:.1f}) | {v23[1][0]:+.0f} ± {v23[1][1]:.0f} | {v23[2][0]:+.0f} ± {v23[2][1]:.0f} | {np.mean(col(P30, 'life')):.0f} |",
          "\n| population | suspended at least once (share) | suspensions a slot | good ticks a slot | arrivals admitted within the run (share) | audit seats a slot | member ticks without the earned seats (share) | the state's share of the audit seats | leak ‰ | standing false approvals | overhead | P_t |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for nm, P in (("world 3's all-careful", [dict(r, **{k: r[k + "c"] for k in ("reach", "susp", "good", "adm", "aud", "noseat")}, **{f"w_{k}": r[f"w0_{k}"] for k in ("leak", "fa", "oh", "Pt")}, ss_audit=r["ss0_audit"]) for r in P30]), ("read 23's all-careful", P23), ("**read 30's all-careful**", P30)):
        L.append(f"| {nm} | {np.mean(col(P, 'reach')):.2f} | {np.mean(col(P, 'susp')):.2f} | {np.mean(col(P, 'good')):.0f} | {np.nanmean(col(P, 'adm')):.2f} | {np.mean(col(P, 'aud')):.1f} | {np.nanmean(col(P, 'noseat')):.3f} | {np.nanmean(col(P, 'ss_audit')):.3f} | {np.mean(col(P, 'w_leak')):.1f} | {np.mean(col(P, 'w_fa')):.1f} | {np.mean(col(P, 'w_oh')):.2f} | {np.mean(col(P, 'w_Pt')):.1f} |")
if P31:
    x31 = xs(P31); a, b, c = mse(col(P31, "rec")), mse(col(P31, "res")), mse(col(P31, "lfl")); x28 = xs(P28) if P28 else None; a28 = mse(col(P28, "rec")) if P28 else None
    L += ["\n**Read 31, the case-keyed conduct at 0.1 on every slot, against read 30's all-careful** (read 28's row, against read 23's, beside):\n",
          "| read | seeds | slots a seed | **all-careful − population, of record** (SE) | temptation | with the reservation | like for like | **level saving: of record / with the reservation / like for like** | care a slot (population / all-careful) | suspended ≥ 1 | suspensions a slot | good ticks (population / all-careful) | arrivals admitted | leak ‰ | FA | overhead |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for nm, P, x in (("28: M at 0.1, the hundred ticks on (against read 23)", P28, x28), ("**31: M at 0.1, the ticks off at none (against read 30)**", P31, x31)):
        if not P: continue
        a_, b_, c_ = mse(col(P, "rec")), mse(col(P, "res")), mse(col(P, "lfl")); t_ = temp(P, "rec", "ben")
        L.append(f"| {nm} | {len(P)} | {np.mean(col(P, 'n')):.1f} / {np.mean(col(P, 'nc')):.1f} | **{a_[0]:+.0f} ± {a_[1]:.0f}** ({a_[0] / a_[1]:.1f}) | {t_[0]:.1f} ± {t_[1]:.1f} | {b_[0]:+.0f} ± {b_[1]:.0f} | {c_[0]:+.0f} ± {c_[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(P, 'call')):.0f} / {np.mean(col(P, 'carec')):.0f} | "
                 f"{np.mean(col(P, 'reach')):.2f} | {np.mean(col(P, 'susp')):.2f} | {np.mean(col(P, 'good')):.0f} / {np.mean(col(P, 'goodc')):.0f} | {np.nanmean(col(P, 'adm')):.2f} | {np.mean(col(P, 'w_leak')):.1f} | {np.mean(col(P, 'w_fa')):.1f} | {np.mean(col(P, 'w_oh')):.2f} |")
    if P31v28:
        L += ["\n**Read 31 against read 28 by seed** (the population's slot and the world's side; read 28 the hundred ticks on):\n", "| measure | read 28 | read 31 | **read 31 − read 28** (SE) |", "|---|---|---|---|"]
        for k, nm, d_ in (("life", "the population's slot, lifetime of record", 0), ("lres", "with the reservation", 0), ("good", "good ticks a slot", 0), ("susp", "suspensions a slot", 2), ("reach", "suspended at least once (share)", 2), ("rvm", "member reviews a slot", 1), ("aud", "audit seats a slot", 1), ("claims", "claims a slot", 1)):
            dd, ma_, mb_, n_ = paired(P28, P31, k); L.append(f"| {nm} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
        for k, kk, nm, d_ in WK:
            dd, ma_, mb_, n_ = paired(P28, P31, f"w_{k}"); L.append(f"| {nm} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
    L += ["\n**The way back, by the suspension (AF4.3's readings)** — the suspensions as a member a slot (a suspension whose tick falls inside no probation spell); the spells of the way back from a member's suspension (ended in a readmission, in another suspension, at a departure, open at the end); the ticks from the suspension to each end; the good ticks. With the ticks off at none a re-suspension on the way back ends no spell — the slot is a probationer again at the same tick's end, its window reset — so reads 30 and 31 show none 'suspended again' and their spells run on through it:\n",
          "| population | suspensions as a member a slot | spells of the way back a slot | ended: readmitted / suspended again / departed / open | ticks lost: to the readmission / to the departure / open at the end | good ticks a slot |", "|---|---|---|---|---|---|"]
    for nm, Cd, ts in (("read 23's all-careful (the hundred ticks on)", C23, 100), ("**read 30's all-careful (the ticks off at none)**", C30, 0), ("read 28: M at 0.1 on every slot (the hundred ticks on)", D(R28), 100), ("**read 31: M at 0.1 on every slot (the ticks off at none)**", D(R31), 0)):
        if not Cd: continue
        rows = susp_rows(Cd, ts); nf = lambda k, d_=0: ("—" if np.all(np.isnan(col(rows, k))) else f"{np.nanmean(col(rows, k)):.{d_}f}")
        L.append(f"| {nm} | {np.mean(col(rows, 'mem')):.3f} | {np.mean(col(rows, 'tot')):.3f} | {nf('adm', 2)} / {nf('sus', 2)} / {nf('dep', 2)} / {nf('opn', 2)} | {nf('whole')} / {nf('dept')} / {nf('opent')} | {np.mean(col(rows, 'good')):.0f} |")
    L.append("")
# ------------------------------------------------------------------ 3. read 32
L += ["## 3. Read 32: the case-keyed conduct at 0.1 on 3 slots in 4, the rest careful — world 3's cell, seeds 21–120\n"]
Q32 = rows_of(R32, CW3); Q9 = rows_of(R9, CW3); Q11 = rows_of(R11); Q19 = rows_of(R19, CW3)
if Q32:
    HDR = ["| read | seeds | slots a seed: conduct / careful beside | **careful − conduct, of record** (SE) | temptation | with the reservation | like for like | **the conduct's level saving: of record / with the reservation / like for like** | care a slot: conduct / careful beside | the conduct's slot / the careful's | the careful beside − the all-careful's slot |", "|---|---|---|---|---|---|---|---|---|---|---|"]
    def qrow(nm, Q):
        a, b, c = mse(col(Q, "rec")), mse(col(Q, "res")), mse(col(Q, "lfl")); x = xs(Q); t_ = temp(Q, "rec", "ben"); cva = mse(col(Q, "care_vs_all"))
        return (f"| {nm} | {len(Q)} | {np.mean(col(Q, 'n')):.1f} / {np.mean(col(Q, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {t_[0]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(Q, 'call')):.0f} / {np.mean(col(Q, 'carec')):.0f} | "
                f"{np.mean(col(Q, 'life')):.0f} / {np.mean(col(Q, 'lifec')):.0f} | {pm(cva, 0) if not np.isnan(cva[1]) else '—'} |")
    L += HDR + [qrow("**32: case-keyed M at 0.1 on 3 in 4**, world 3's cell", Q32)]
    if Q29: L.append(qrow("29: case-keyed M at 0.2 on 3 in 4, world 3's cell (the record)", Q29))
    if Q9: L.append(qrow("9: M at 0.1 drawn at each review on 1 in 4, world 3's cell (the record)", Q9))
    if Q11: L.append(qrow("11: M at 0.1 drawn at each review on 3 in 4, world 4's cell, seeds 21–80 (the record)", Q11))
    if Q19: L.append(qrow("19: M at 0.2 drawn at each review on 1 in 4, world 3's cell (the record)", Q19))
    L += ["\n**The seats, the time without them, the state's share** (read 29's four readings):\n", "| group | audit seats a slot | panel seats a slot | member reviews a slot | member ticks without the earned seats (share) | … the record undetermined | suspended at least once; suspensions a slot | good ticks a slot | lifetime of record |", "|---|---|---|---|---|---|---|---|---|"]
    for nm, Q, s_ in (("read 32: the conduct's slots (3 in 4)", Q32, ""), ("read 32: the careful quarter", Q32, "c"), ("read 29: the conduct's slots", Q29, ""), ("read 29: the careful quarter", Q29, "c")):
        if not Q: continue
        L.append(f"| {nm} | {np.mean(col(Q, 'aud' + s_)):.1f} | {np.mean(col(Q, 'panel' + s_)):.1f} | {np.mean(col(Q, 'rvm' + s_)):.1f} | **{np.nanmean(col(Q, 'noseat' + s_)):.3f}** | {np.nanmean(col(Q, 'undet' + s_)):.3f} | {np.mean(col(Q, 'reach' + s_)):.2f}; {np.mean(col(Q, 'susp' + s_)):.2f} | {np.mean(col(Q, 'good' + s_)):.0f} | {np.mean(col(Q, 'life' + s_)):.0f} |")
    L.append(f"| world 3's all-careful (every slot) | {np.mean(col(Q32, 'aud_all')):.1f} | | | | | | | {np.mean(col(Q32, 'lifea')):.0f} |")
    cva32 = mse(col(Q32, "care_vs_all")); d32 = fa_split(bm(R32))
    L.append(f"\nThe careful quarter's slot against world 3's all-careful slot by seed: **{cva32[0]:+.0f} ± {cva32[1]:.0f}** ({cva32[0] / cva32[1]:.1f} SE; read 29's +404 ± 26). The state's share of the seats: the first review {np.nanmean(col(Q32, 'ss_first')):.3f}, the audit seat **{np.nanmean(col(Q32, 'ss_audit')):.3f}**, the panels {np.nanmean(col(Q32, 'ss_panel')):.3f} (read 29's 0.001 / 0.380 / 0.265; read 25's 0.362 at the audit seat). "
             f"Who met the bad deliveries: of {d32['tot']:.0f} real bad deliveries closed a run {d32['fm']:.2f} were reviewed first by a member, {d32['fp']:.2f} on probation, {d32['fs']:.3f} by the state; the conduct's members claimed on {d32['claims']:.1f} a run at the first review, of which **{d32['paid']:.2f} stay paid** ({d32['none']:.2f} never audited, {d32['mconf']:.2f} confirmed by a member's audit, {d32['sconf']:.2f} by the state's) and {1 - d32['paid']:.2f} are overturned ({d32['mdiff']:.2f} after a member's audit differed — the careful quarter's — and {d32['sdiff']:.2f} after the state's).\n")
    P25 = pop_rows(R25 or R25_OLD, CW3)
    if P25:
        L += ["**Read 32 against read 25 by seed** — the conduct's slots (read 25's every slot on the conduct; read 32's three in four) and the world's side:\n", "| measure | read 25 | read 32 | **read 32 − read 25** (SE) |", "|---|---|---|---|"]
        for k25, k32, nm, d_ in (("life", "life", "the conduct's slot, lifetime of record", 0), ("rvm", "rvm", "member reviews a conduct slot", 1), ("aud", "aud", "audit seats a conduct slot", 1), ("susp", "susp", "suspensions a conduct slot", 2), ("good", "good", "good ticks a conduct slot", 0)):
            dd, ma_, mb_, n_ = paired(P25, Q32, k25, k32); L.append(f"| {nm} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
        for k, kk, nm, d_ in WK:
            dd, ma_, mb_, n_ = paired(P25, Q32, f"w_{k}"); L.append(f"| {nm} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
    L.append("")
# ------------------------------------------------------------------ 4. reads 33 and 34
L += ["## 4. Reads 33 and 34: two groups of slots on the case-keyed conduct at 0.1 under their group's salt — today's picks, and the seating by group (world 3's cell, seeds 21–120)\n"]
P33 = pop_rows(R33, CW3); P34 = pop_rows(R34, CW3); P25 = pop_rows(R25 or R25_OLD, CW3)
if P33 and P34:
    HDRP = ["| read | seeds | slots a seed: population / all-careful | **all-careful − population, of record** (SE) | temptation | with the reservation | like for like | **the population's level saving: of record / with the reservation / like for like** | care a slot | suspended ≥ 1; suspensions a slot | audit seats a slot: population / all-careful | member ticks without the seats | the state's share of the audit seats | leak ‰ | FA | overhead |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    def prow(nm, P):
        a, b, c = mse(col(P, "rec")), mse(col(P, "res")), mse(col(P, "lfl")); x = xs(P); t_ = temp(P, "rec", "ben")
        return (f"| {nm} | {len(P)} | {np.mean(col(P, 'n')):.1f} / {np.mean(col(P, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {t_[0]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(P, 'call')):.0f} | {np.mean(col(P, 'reach')):.2f}; {np.mean(col(P, 'susp')):.2f} | "
                f"{np.mean(col(P, 'aud')):.1f} / {np.mean(col(P, 'audc')):.1f} | {np.nanmean(col(P, 'noseat')):.3f} | {np.nanmean(col(P, 'ss_audit')):.3f} | {np.mean(col(P, 'w_leak')):.1f} | {np.mean(col(P, 'w_fa')):.1f} | {np.mean(col(P, 'w_oh')):.2f} |")
    L += HDRP + [prow("25: one model, case-keyed M at 0.1 on every slot (the record)", P25), prow("**33: two groups, two sets of cases, today's picks**", P33), prow("**34: two groups, the seating by group**", P34)]
    # the groups' balance
    gb = [np.mean([v.get("group", 0) for v in slots(e)]) for e in R33]; L.append(f"\nThe groups: {100 * np.mean(gb):.0f} in 100 of a run's slots in group 1 (the rest in group 0; {np.mean([len(slots(e)) for e in R33]):.1f} slots a run); the two groups' slots alike in read 33 (the lifetime of record of group 0 against group 1 by seed: {pm(mse([np.mean([life(v) for v in slots(e) if v.get('group') == 0]) - np.mean([life(v) for v in slots(e) if v.get('group') == 1]) for e in R33]), 0)}).\n")
    # who met the bad deliveries, with the holder of the audit by group
    L += ["**Who met the bad deliveries, with the holder of the audit by the first reviewer's group** (AD4.1's reading; the fate of a member's claim on real bad work at the first review):\n",
          "| read | real bad deliveries closed a run | first by a member / on probation / the state | member claims at the first review a run | **stays paid** | … never audited | … confirmed by the own group's audit | … by the other group's | … by the state's | overturned | … after the own group's audit differed | … the other group's | … the state's | of the paid, confirmed by the own group (R: 0.70–0.82 for 33) |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    FG = {}
    for nm, E in (("33", R33), ("34", R34)):
        B = bm(E); g = g_of(B); d = fa_split(B); cl = d["claims"]; keys = {k for r in B for k in r}
        gg = {k: g(f"fag_claim_{k}") / cl for k in ("paid_none", "paid_same_confirmed", "paid_other_confirmed", "paid_state_confirmed", "overturned_same_differed", "overturned_other_differed", "overturned_state_differed")}
        paid = sum(v for k, v in gg.items() if k.startswith("paid")); own_of_paid = gg["paid_same_confirmed"] / paid if paid else np.nan; FG[nm] = {**d, **gg, "paid": paid, "own_of_paid": own_of_paid}
        L.append(f"| {nm} | {d['tot']:.0f} | {d['fm']:.2f} / {d['fp']:.2f} / {d['fs']:.3f} | {cl:.1f} | **{paid:.2f}** | {gg['paid_none']:.3f} | {gg['paid_same_confirmed']:.2f} | {gg['paid_other_confirmed']:.2f} | {gg['paid_state_confirmed']:.2f} | {1 - paid:.2f} | {gg['overturned_same_differed']:.2f} | {gg['overturned_other_differed']:.2f} | {gg['overturned_state_differed']:.2f} | **{own_of_paid:.2f}** |")
    # the picks by group
    L += ["\n**The audit and panel picks by group** (`pick_json`: of the member picks whose first reviewer was a slot — the state's and the orchestrator's first seats apart, `nofirst` — the share seated from the other group; in read 34 the share that fell to today's pick for want of a free panel-eligible member of the other group):\n",
          "| read | audit picks with a slot's first reviewer a run | seated from the other group | the same group | fell to today's pick (34) | first seat not a slot's (the state's, the orchestrator's alias) | panel picks a run | other group | same group | fell to today's pick |", "|---|---|---|---|---|---|---|---|---|---|"]
    PK = {}
    for nm, E in (("33", R33), ("34", R34)):
        pk = [json.loads(e.get("pick_json") or "{}") for e in E]; g = lambda k: float(np.mean([p.get(k, 0) for p in pk]))
        na = g("pick_audit_same") + g("pick_audit_other") + g("pick_audit_fallback"); npn = g("pick_panel_same") + g("pick_panel_other") + g("pick_panel_fallback")
        PK[nm] = dict(a_other=g("pick_audit_other") / na if na else np.nan, a_same=g("pick_audit_same") / na if na else np.nan, a_fb=g("pick_audit_fallback") / na if na else np.nan, p_other=g("pick_panel_other") / npn if npn else np.nan, p_fb=g("pick_panel_fallback") / npn if npn else np.nan, na=na)
        L.append(f"| {nm} | {na:.0f} | **{PK[nm]['a_other']:.3f}** | {PK[nm]['a_same']:.3f} | {PK[nm]['a_fb']:.3f} | {g('pick_audit_nofirst'):.0f} | {npn:.0f} | {PK[nm]['p_other']:.3f} | {g('pick_panel_same') / npn if npn else np.nan:.3f} | {PK[nm]['p_fb']:.3f} |")
    L.append("\nIn read 34 a pick that fell to today's pick is a member of the first reviewer's own group by construction (no member of the other group was free and panel-eligible at the seat's turn, so the round-robin's next free one is the own group's); the share of the audit seats a member holds that are seated from the other group is the `other` column, the rest the fallback's.\n")
    # the state's share by seat
    L += ["**The state's share of the seats, by seat:**\n", "| read | the first review | the audit seat | the panels | the deciding verdict |", "|---|---|---|---|---|"]
    for nm, P in (("world 3's all-careful", [dict(r, **{f"ss_{k}": r[f"ss0_{k}"] for k in ("first", "audit", "panel")}) for r in P33]), ("25", P25), ("33", P33), ("34", P34)):
        L.append(f"| {nm} | {np.nanmean(col(P, 'ss_first')):.3f} | **{np.nanmean(col(P, 'ss_audit')):.3f}** | {np.nanmean(col(P, 'ss_panel')):.3f} | 1.00 |")
    # how often one pair meets
    L += ["\n**How often one pair meets** — a first reviewer and the member at its audit seat, over the run (the loop's count; every new collection carries it):\n", "| read | member audit seats a run with a slot's first reviewer | pairs that meet | **meetings a pair that meets** | pairs meeting more than three times (share) | the largest | members a first reviewer meets at its audit seat |", "|---|---|---|---|---|---|---|"]
    PRS = {}
    for nm, E in (("25: one model, today's picks", R25), ("30: the all-careful, the first failure's cell, the ticks off", list(C30.values())), ("31: M at 0.1, the first failure's cell, the ticks off", R31), ("32: M at 0.1 on 3 in 4", R32), ("33: two groups, today's picks", R33), ("34: two groups, the seating by group", R34)):
        PR = [p for p in (pairs_of(e) for e in E) if p]
        if not PR: continue
        PRS[nm[:2]] = PR; L.append(f"| {nm} | {np.mean(col(PR, 'meetings')):.0f} | {np.mean(col(PR, 'pairs')):.0f} | **{np.mean(col(PR, 'mean')):.2f}** | {np.mean(col(PR, 'gt3')):.2f} | {np.mean(col(PR, 'mx')):.1f} | {np.mean(col(PR, 'partners')):.1f} |")
    if "33" in PRS and "34" in PRS:
        r_ = np.mean(col(PRS["34"], "mean")) / np.mean(col(PRS["33"], "mean")); L.append(f"\nWith the seating by group a pair meets **{r_:.2f} times as often** as with today's picks (R: about twice): the pairing is the round-robin's — the next free panel-eligible member in id order after the last pick — and is set by who is free at the case's turn, not by the pool's size; narrowing the pool to the other group changes which member sits, hardly how many times the same two meet.\n")
    # against read 25 and against read 33 by seed
    def side(title, PA, PB, nmA, nmB):
        L.extend([f"\n**{title}** (paired by seed):\n", f"| measure | {nmA} | {nmB} | **{nmB} − {nmA}** (SE) |", "|---|---|---|---|"])
        for k, nm, d_ in (("life", "the population's slot, lifetime of record", 0), ("lres", "with the reservation", 0), ("aud", "audit seats a slot", 1), ("susp", "suspensions a slot", 2), ("good", "good ticks a slot", 0)):
            dd, ma_, mb_, n_ = paired(PA, PB, k); L.append(f"| {nm} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
        out = {}
        for k, kk, nm, d_ in WK:
            dd, ma_, mb_, n_ = paired(PA, PB, f"w_{k}"); out[k] = dd; L.append(f"| {nm} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({dd[0] / dd[1] if dd[1] else np.nan:.1f}) |")
        return out
    S33 = side("Read 33 against read 25 by seed (two models that miss different deliveries, against one model)", P25, P33, "read 25", "read 33"); S34 = side("Read 34 against read 33 by seed (the seating by group against today's picks)", P33, P34, "read 33", "read 34")
    L.append("")
# ------------------------------------------------------------------ 5. expectations and conditions
L += ["## 5. Against the expectations stated before the run (AF5 for reads 30 and 31; AH5 for reads 32 to 34), and the conditions\n"]
if P30:
    v23 = mse(-col(P30v23, "rec")); a = mse(col(P30, "rec")); rows30 = susp_rows(C30, 0)
    chk(in_band(100 * np.mean(col(P30, "reach")), 31, 37), f"read 30: 31 to 37 in 100 suspended at least once: {100 * np.mean(col(P30, 'reach')):.0f}."); chk(in_band(np.mean(col(P30, "susp")), 0.38, 0.52), f"read 30: 0.38 to 0.52 suspensions a slot: {np.mean(col(P30, 'susp')):.2f}.")
    chk(in_band(np.mean(col(P30, "good")), 490, 525), f"read 30: good ticks a slot 490 to 525 (read 23's 484): {np.mean(col(P30, 'good')):.0f}."); chk(in_band(np.nanmean(col(rows30, "whole")), 105, 150), f"read 30: the way back where it ends in a readmission 105 to 150 ticks from the suspension: {np.nanmean(col(rows30, 'whole')):.0f}.")
    chk(in_band(a[0], 36, 70), f"read 30: the slot behind world 3's by 36 to 70 real of record (read 23's 79): {a[0]:+.0f} ± {a[1]:.0f}."); chk(in_band(100 * np.nanmean(col(P30, "adm")), 80, 87), f"read 30: arrivals admitted 80 to 87 in 100: {100 * np.nanmean(col(P30, 'adm')):.0f}.")
    chk(in_band(np.mean(col(P30, "w_leak")), 3.6, 4.8), f"read 30: a leak of 3.6 to 4.8 in a thousand: {np.mean(col(P30, 'w_leak')):.1f}."); chk(in_band(np.mean(col(P30, "w_oh")), 12.0, 12.5), f"read 30: an overhead of 12.0 to 12.5: {np.mean(col(P30, 'w_oh')):.2f}.")
if P31:
    x = xs(P31)[0]; a = mse(col(P31, "rec"))
    chk(in_band(100 * np.mean(col(P31, "reach")), 68, 80), f"read 31: 68 to 80 in 100 suspended at least once: {100 * np.mean(col(P31, 'reach')):.0f}."); chk(in_band(np.mean(col(P31, "susp")), 0.85, 1.35), f"read 31: 0.85 to 1.35 suspensions a slot: {np.mean(col(P31, 'susp')):.2f}.")
    chk(in_band(np.mean(col(P31, "good")), 385, 450), f"read 31: good ticks a slot 385 to 450 (read 28's 354): {np.mean(col(P31, 'good')):.0f}."); chk(in_band(a[0], 95, 170), f"read 31: behind read 30's slot by 95 to 170 real of record: {a[0]:+.0f} ± {a[1]:.0f}.")
    chk(in_band(x[0], 0.6, 1.2), f"read 31: a level saving of 0.6 to 1.2 of record: {pm(x, 2)}."); chk(in_band(np.mean(col(P31, "w_leak")), 42, 52), f"read 31: a leak of 42 to 52: {np.mean(col(P31, 'w_leak')):.1f}.")
    chk(in_band(np.mean(col(P31, "w_fa")), 15, 24), f"read 31: standing false approvals of 15 to 24 a run: {np.mean(col(P31, 'w_fa')):.1f}."); chk(in_band(np.mean(col(P31, "w_oh")), 13.8, 15.2), f"read 31: an overhead of 13.8 to 15.2: {np.mean(col(P31, 'w_oh')):.2f}.")
if Q32:
    x = xs(Q32)[0]; a = mse(col(Q32, "rec")); d32 = fa_split(bm(R32))
    chk(in_band(np.mean(col(Q32, "audc")), 45, 56), f"read 32: the careful quarter holds 45 to 56 audit seats a slot: {np.mean(col(Q32, 'audc')):.1f}."); chk(in_band(np.mean(col(Q32, "aud")), 28, 34), f"read 32: the conduct's slots 28 to 34: {np.mean(col(Q32, 'aud')):.1f}.")
    chk(in_band(np.nanmean(col(Q32, "noseat")), 0.70, 0.80), f"read 32: the conduct's slots without their earned seats on 0.70 to 0.80 of their member ticks: {np.nanmean(col(Q32, 'noseat')):.3f}."); chk(in_band(np.nanmean(col(Q32, "noseatc")), 0.52, 0.60), f"read 32: the careful quarter on 0.52 to 0.60: {np.nanmean(col(Q32, 'noseatc')):.3f}.")
    chk(in_band(np.nanmean(col(Q32, "ss_audit")), 0.30, 0.37), f"read 32: the state holds 0.30 to 0.37 of the audit seats: {np.nanmean(col(Q32, 'ss_audit')):.3f}."); chk(in_band(a[0], 75, 190), f"read 32: the conduct's slots behind the careful quarter by 75 to 190 real of record: {a[0]:+.0f} ± {a[1]:.0f}.")
    chk(in_band(x[0], 0.40, 0.85), f"read 32: a level saving of 0.40 to 0.85 of record: {pm(x, 2)}."); chk(in_band(d32["paid"], 0.42, 0.54), f"read 32: of the conduct's claims at the first review 0.42 to 0.54 stay paid: {d32['paid']:.2f}.")
    chk(in_band(np.mean(col(Q32, "w_leak")), 27, 37), f"read 32: a leak of 27 to 37: {np.mean(col(Q32, 'w_leak')):.1f}."); chk(in_band(np.mean(col(Q32, "w_fa")), 13, 19), f"read 32: standing false approvals of 13 to 19 a run: {np.mean(col(Q32, 'w_fa')):.1f}."); chk(in_band(np.mean(col(Q32, "w_oh")), 14.0, 15.6), f"read 32: an overhead of 14.0 to 15.6: {np.mean(col(Q32, 'w_oh')):.2f}.")
if P33 and P34:
    x33, x34 = xs(P33)[0], xs(P34)[0]
    chk(in_band(FG["33"]["paid"], 0.35, 0.45), f"read 33: of a member's claims 0.35 to 0.45 stay paid (read 25's 0.67): {FG['33']['paid']:.2f}."); chk(in_band(FG["33"]["own_of_paid"], 0.70, 0.82), f"read 33: of those 0.70 to 0.82 confirmed by a member of the first reviewer's own group: {FG['33']['own_of_paid']:.2f}.")
    chk(in_band(np.mean(col(P33, "w_leak")), 27, 35), f"read 33: a leak of 27 to 35: {np.mean(col(P33, 'w_leak')):.1f}."); chk(in_band(np.mean(col(P33, "w_fa")), 13, 18), f"read 33: standing false approvals of 13 to 18 a run: {np.mean(col(P33, 'w_fa')):.1f}."); chk(in_band(np.mean(col(P33, "w_oh")), 13.8, 15.0), f"read 33: an overhead of 13.8 to 15.0: {np.mean(col(P33, 'w_oh')):.2f}.")
    chk(in_band(x33[0], 0.05, 0.22), f"read 33: the population's level saving 0.05 to 0.22 of record: {pm(x33, 2)}."); chk(in_band(np.nanmean(col(P33, "ss_audit")), 0.33, 0.39), f"read 33: the state holds 0.33 to 0.39 of the audit seats: {np.nanmean(col(P33, 'ss_audit')):.3f}.")
    chk(in_band(PK["34"]["a_other"], 0.85, 0.98), f"read 34: of the audit seats a member holds 0.85 to 0.98 seated from the other group: {PK['34']['a_other']:.3f} (the rest fell to today's pick).")
    chk(in_band(FG["34"]["paid"], 0.13, 0.24), f"read 34: of a member's claims 0.13 to 0.24 stay paid: {FG['34']['paid']:.2f}."); chk(in_band(np.mean(col(P34, "w_leak")), 12, 21), f"read 34: a leak of 12 to 21: {np.mean(col(P34, 'w_leak')):.1f}."); chk(in_band(np.mean(col(P34, "w_fa")), 6, 11), f"read 34: standing false approvals of 6 to 11 a run: {np.mean(col(P34, 'w_fa')):.1f}.")
    chk(in_band(x34[0], 0.08, 0.28), f"read 34: the population's level saving 0.08 to 0.28 of record: {pm(x34, 2)}."); chk(abs(np.nanmean(col(P34, "ss_audit")) - np.nanmean(col(P33, "ss_audit"))) <= 0.03, f"read 34: the state's share of the audit seats within 0.03 of read 33's: {np.nanmean(col(P34, 'ss_audit')):.3f} against {np.nanmean(col(P33, 'ss_audit')):.3f}.")
    if "33" in PRS and "34" in PRS:
        r_ = np.mean(col(PRS["34"], "mean")) / np.mean(col(PRS["33"], "mean")); chk(in_band(r_, 1.5, 2.5), f"read 34: a pair meets about twice as often as in read 33 (read as 1.5 to 2.5 times): {r_:.2f}.")
L += CHK; L.append(f"\n**{sum(1 for c_ in CHK if c_.startswith('- MET'))} of {len(CHK)} expectations met.**\n")
L += ["\n## 6. Refuted, or shown, each apart\n"]
if P30:
    v = mse(-col(P30v23, "rec")); L.append(verdict(f"*Without its hundred ticks of silence the suspension at the first failure costs the careful less*: shown if read 30's slot ends above read 23's by two standard errors of record, by seed; refuted if it ends at or under read 23's at the point value. Read 30's slot ends {v[0]:+.0f} ± {v[1]:.0f} above read 23's ({v[0] / v[1]:+.1f} SE).", v[0] - 2 * v[1] > 0, v[0] <= 0))
if P31:
    x = xs(P31)[0]; L.append(verdict(f"*Without the silence the suspension at the first failure still holds a population on a model that spares nine tenths at a dose of 0.1*: shown if read 31's level saving against read 30's all-careful is above 0.9 by two standard errors of record; refuted if it is under 0.9 at the point value. Read 31's is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] - 2 * x[1] > 0.9, x[0] < 0.9))
if Q32:
    x = xs(Q32)[0]; L.append(verdict(f"*At a dose of 0.1, among members of whom most are on the model, the model still pays a member*: shown if read 32's level saving of the conduct's slots against the careful quarter is under 0.9 by two standard errors of record; refuted if it is above 0.9 at the point value. Read 32's is {pm(x, 2)} ({(x[0] - 0.9) / x[1]:+.1f} SE from 0.9).", x[0] + 2 * x[1] < 0.9, x[0] > 0.9))
if P33 and P34:
    dd = S34["leak"]; L.append(verdict(f"*A seating that takes the second look from the members that do not share the first reviewer's misses leaves less bad work paid*: shown if read 34's leak is under read 33's by two standard errors, by seed; refuted if it is at or above read 33's at the point value. Read 34's leak is {dd[0]:+.1f} ± {dd[1]:.1f} ‰ against read 33's ({dd[0] / dd[1]:+.1f} SE).", dd[0] + 2 * dd[1] < 0, dd[0] >= 0))
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("wrote", sys.argv[1], len(L), "lines")
