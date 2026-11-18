"""Addendum 30 (November 18, 2026, midday; notes §125): the reviewer's arithmetic on §123–§124 confirmed or replaced (AJ3), the readings asked from the record (AJ4), and six reads without
training at a4fc4f6c4 — reads 35 and 36 (world 3's all-careful and read 29's population with the audit and panel seats drawn: `--seat-draw seats`, a construction with its own stream; beside them
the option of record `--assignment seeded` as it is, every pick drawn on the world's stream), reads 37 to 40 (the conduct with two doses on Baruchi's word: cell A caseM0.1p0.98 on 1 slot in 4;
cell B caseM0.2p0 on 1 in 4, 3 in 4 and every slot). The conduct with the doses equal (caseM0.1p0.1) run on every slot first and checked to the digit against read 25 (a24/rerun/r25); world 3's
all-careful run again whole for the row's new readings and checked against a25/rerun/cw3. a24_read.py's and a25_read.py's helpers copied. Usage: a26_read.py OUT.md"""
import json, os, sys, hashlib, math, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D26, D25, D24, D22, D19, D18 = f"{R}/a26", f"{R}/a25", f"{R}/a24", f"{R}/a22", f"{R}/a19", f"{R}/a18"
T = 1000; RES = 0.8; EPS = 0.05
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else ((x.mean() if len(x) else np.nan), np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num)
    if n < 2 or den.mean() == 0: return ((num.mean() / den.mean()) if n and den.mean() else np.nan, np.nan)
    a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1); r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def pm(t, d=1): return f"{t[0]:.{d}f} ± {t[1]:.{d}f}" if not np.isnan(t[1]) else f"{t[0]:.{d}f}"
def se_(t): return f"{t[0] / t[1]:.1f}" if (t[1] and not np.isnan(t[1])) else "—"
def slots(e): return list(json.loads(e["learner_slots_json"]).values())
def life(v): return v["wealth_real"] + v["private_real"]
def after(v): return (T - v["t_out"]) if (not v["alive"] and v["t_out"] is not None and v["t_out"] < T) else 0
def careful_of(e):
    share = float(e.get("half_share") or 0.5); seed = int(e["seed"])
    return lambda x: int.from_bytes(hashlib.md5(f"{seed}:{x}".encode()).digest()[:2], "big") >= share * 65536
def groups(e):
    S = json.loads(e["learner_slots_json"]); c = careful_of(e); grp = {"claim": [], "care": []}
    for x, v in S.items(): grp["care" if c(x) else "claim"].append(v)
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
    tm = sum(v.get("ticks_member", 0) for v in V); arr = [v for v in V if v["t_in"] > 0]; sus = [v for v in V if v["suspensions"] > 0]
    pb = sum(v.get(f"rvm_plant_bad_{s}", 0) for v in V for s in SEATS); pwb = sum(v.get(f"pwb_member_{s}", 0) for v in V for s in SEATS); pg = sum(v.get(f"rvm_plant_good_{s}", 0) for v in V for s in SEATS); pwg = sum(v.get(f"pwg_member_{s}", 0) for v in V for s in SEATS)
    rb = sum(v.get("rvi_member_real_bad", 0) for v in V); fai = sum(v.get("fai_member", 0) for v in V); has_kind = any(k.startswith(("pwb_", "pwg_")) for v in V for k in v); pw_any = sum(v.get(f"pw_member_{s}", 0) for v in V for s in SEATS)
    return dict(n=n, good=good, ig=ig, bg=bg, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n, ben=g("private_real"),
                claims=g("claims"), susp=g("suspensions"), aud=g("audits_done"), panel=g("rvm_appeal") + g("rvm_third") + g("rvm_dispute"), care_m=g("care_member"), claimed_m=g("claimed_member"), rvm=g("rv_member"), reach=len(sus) / n,
                pre_susp=(np.mean([v.get("rvm_pre_susp", 0) for v in sus]) if sus else np.nan),
                tm=tm / n, noseat=(sum(v.get("ticks_member_noseat", 0) for v in V) / tm) if tm else np.nan, undet=(sum(v.get("ticks_member_noseat_undet", 0) for v in V) / tm) if tm else np.nan, fa=g("fa_init"), fpaid=g("fa_init") - g("fa_init_overturned"),
                pw=sum(g(f"pw_member_{s}") for s in SEATS), pb_met=pb / n, pwb_share=(pwb / pb if (pb and has_kind) else np.nan), pwg_share=(pwg / pg if (pg and has_kind) else np.nan), pg_met=pg / n, rb_first=rb / n, fai_share=(fai / rb if rb else np.nan), pw_any_share=(pw_any / (pb + pg) if ((pb + pg) and any(k.startswith("pw_") for v in V for k in v)) else np.nan),
                adm=(sum(1 for v in arr if "adm_ticks" in v) / len(arr)) if arr else np.nan, aud_inc=g("rf_member_audit_fee") + g("rf_member_audit_emission") + g("rf_member_audit_uplift"),
                panel_inc=sum(g(f"rf_member_{s_}_{k}") for s_ in ("third", "appeal", "dispute") for k in ("fee", "emission", "uplift")))
def state_share(e):
    tin = e.get("troop_initial_seats"); tr, ta, tp, ds = f(e, "troop_reviews"), f(e, "troop_audits"), f(e, "troop_panel_seats"), f(e, "deciding_seats")
    tin = float(tin) if tin not in (None, "") else (tr - tp - ds)
    mi = f(e, "seated_initial_member") + f(e, "seated_initial_probationer"); ma = f(e, "seated_audit_member"); mp = f(e, "seated_appeal_member"); tpa = tp - ta
    return {"first": tin / (tin + mi) if (tin + mi) else np.nan, "audit": ta / (ta + ma) if (ta + ma) else np.nan, "panel": tpa / (tpa + mp) if (tpa + mp) else np.nan}
WK = (("fa", "false_approvals", "standing false approvals a run", 1), ("leak", "leak_bad", "the leak, ‰ of bad deliveries", 1), ("oh", "sys_overhead_per_vested", "the system overhead a vested task", 2), ("cot", "cost_of_truth", "the cost of truth a run", 0),
      ("dep", "departures", "departures a run", 1), ("arr", "arrivals", "arrivals a run", 1), ("Pt", "P_t", "P_t at the end", 1), ("m", "m_mean", "the dial's m_t, the mean over the periods", 3), ("mend", "m", "m_t at the end", 3), ("pi", "pi_mean", "π_t, the mean over the periods", 3))
def world(e): return {k: (1000 * f(e, kk) if k == "leak" else f(e, kk)) for k, kk, _, _ in WK}
def frees(e, kind="audit"):
    pk = json.loads(e.get("pick_json") or "{}"); n = pk.get(f"pick_{kind}_free_n", 0)
    return dict(mean=(pk.get(f"pick_{kind}_free_sum", 0) / n) if n else np.nan, one=(pk.get(f"pick_{kind}_free_1", 0) / n) if n else np.nan, two=(pk.get(f"pick_{kind}_free_2", 0) / n) if n else np.nan, three=(pk.get(f"pick_{kind}_free_3p", 0) / n) if n else np.nan, n=n, drawn=pk.get(f"pick_{kind}_drawn", 0))
def pop_rows(E, C):
    out = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in C: continue
        V, Vc = slots(e), slots(C[s_]); S_, Cc = stats_(V), stats_(Vc); call = S_["care_m"] + S_["claimed_m"]
        out.append(dict(seed=s_, n=len(V), nc=len(Vc), rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], call=call, carec=Cc["care_m"],
                        **{k: S_[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "adm", "claims", "fa", "fpaid", "tm", "pw", "pb_met", "pg_met", "pwb_share", "pwg_share", "pw_any_share", "rb_first", "fai_share", "pre_susp")}, **{k + "c": Cc[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "adm", "pw", "pb_met", "pg_met", "pwb_share", "pwg_share", "pw_any_share", "rb_first", "fai_share")},
                        **{f"w_{k}": v for k, v in world(e).items()}, **{f"w0_{k}": v for k, v in world(C[s_]).items()}, **{f"ss_{k}": v for k, v in state_share(e).items()}, **{f"ss0_{k}": v for k, v in state_share(C[s_]).items()}, fr=frees(e)["mean"], fr0=frees(C[s_])["mean"]))
    return out
def rows_of(E, C=None):
    """Read 29's shape: the conduct's slots against the careful slots beside them in the same world, each seed; C the all-careful of the cell for the careful group's gain over it."""
    out = []
    for e in E:
        g = groups(e); s_ = int(e["seed"])
        if not g["claim"] or not g["care"]: continue
        S_, Cc = stats_(g["claim"]), stats_(g["care"]); Ca = stats_(slots(C[s_])) if (C and s_ in C) else None; call = S_["care_m"] + S_["claimed_m"]
        out.append(dict(seed=s_, n=S_["n"], nc=Cc["n"], rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], call=call, carec=Cc["care_m"],
                        **{k: S_[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "fa", "fpaid", "tm", "pw", "pb_met", "pg_met", "pwb_share", "pwg_share", "pw_any_share", "rb_first", "fai_share", "pre_susp", "claims")}, **{k + "c": Cc[k] for k in ("life", "lres", "good", "susp", "aud", "panel", "reach", "rvm", "noseat", "undet", "pw", "pb_met", "pg_met", "pwb_share", "pwg_share", "pw_any_share", "rb_first", "fai_share", "pre_susp")},
                        lifea=Ca["life"] if Ca else np.nan, care_vs_all=(Cc["life"] - Ca["life"]) if Ca else np.nan, aud_all=Ca["aud"] if Ca else np.nan,
                        **{f"w_{k}": v for k, v in world(e).items()}, **{f"ss_{k}": v for k, v in state_share(e).items()}, fr=frees(e)["mean"]))
    return out
def xs(P, keys=("rec", "res", "lfl_num")): return tuple(ratio_se(col(P, k) + col(P, "ben"), col(P, "call")) for k in keys)
def temp(P, k, den): t = ratio_se(col(P, k), col(P, den)); return 1 + t[0], t[1]
def bm(E): return [{k: float(v) for k, v in json.loads(e.get("bad_met_first_json") or "{}").items()} for e in E]
def g_of(B): return lambda k: float(np.mean([r.get(k, 0.0) for r in B]))
def fa_split(B):
    g = g_of(B); keys = {k for r in B for k in r}; cl = g("fa_member_claim"); paid = sum(g(k) for k in keys if k.startswith("fa_member_claim_paid")); ov = sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned"))
    d = dict(claims=cl, paid=paid / cl if cl else np.nan, none=g("fa_member_claim_paid_none") / cl if cl else np.nan, mconf=g("fa_member_claim_paid_audit_member_confirmed") / cl if cl else np.nan, sconf=g("fa_member_claim_paid_audit_state_confirmed") / cl if cl else np.nan,
             mdiff=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_audit_member")) / cl if cl else np.nan, sdiff=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_audit_state")) / cl if cl else np.nan)
    tot = g("first_member") + g("first_probation") + g("first_state"); d.update(tot=tot, fm=g("first_member") / tot if tot else np.nan, fp=g("first_probation") / tot if tot else np.nan, fs=g("first_state") / tot if tot else np.nan)
    return d
def paid_by_seed(E):
    out = {}
    for e in E:
        b = {k: float(v) for k, v in json.loads(e.get("bad_met_first_json") or "{}").items()}; cl = b.get("fa_member_claim", 0); paid = sum(v for k, v in b.items() if k.startswith("fa_member_claim_paid"))
        out[int(e["seed"])] = (paid / cl) if cl else np.nan
    return out
def pairs_of(e, side=None):
    pmj = {k: v for k, v in json.loads(e.get("pair_meet_json") or "{}").items() if not k.startswith("plant_rev")}
    if side is not None:
        c = careful_of(e); pmj = {k: v for k, v in pmj.items() if c(k.split("|")[1]) == (side == "careful")}
    if not pmj: return None
    ns = [len(v) for v in pmj.values()]; firsts = {}
    for k, v in pmj.items(): firsts.setdefault(k.split("|")[0], set()).add(k.split("|")[1])
    S = json.loads(e["learner_slots_json"]); n = len(S); n_side = (sum(1 for x in S if careful_of(e)(x) == (side == "careful")) if side else n)
    return dict(seed=int(e["seed"]), pairs=len(ns), meetings=sum(ns), mean=np.mean(ns), gt3=sum(1 for x in ns if x > 3) / len(ns), mx=max(ns), partners=np.mean([len(s) for s in firsts.values()]), n=n, n_side=n_side, lam=sum(ns) / (n - 1) / n_side if n_side else np.nan)
def pois(lam):
    p = [math.exp(-lam) * lam ** k / math.factorial(k) for k in range(4)]; return lam / (1 - p[0]), (1 - sum(p)) / (1 - p[0])
def repro(new_eps, old_eps, label, skip=("pick_json",)):
    old = {int(e["seed"]): e for e in old_eps}; n_rows = n_keys = n_slots = n_seeds = 0; diffs = []; bm_d = []; pm_d = []
    for e in new_eps:
        s_ = int(e["seed"])
        if s_ not in old: continue
        o = old[s_]; n_seeds += 1
        for k in o:
            if k in ("learner_slots_json", "bad_met_first_json", "pair_meet_json") or k in skip: continue
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
            if bn.get(k, bn.get(k + "_member", 0) + bn.get(k + "_state", 0)) != val: bm_d.append((s_, k))
        po = {k: v for k, v in json.loads(o.get("pair_meet_json") or "{}").items() if not k.startswith("plant_rev")}; pn = {k: v for k, v in json.loads(e.get("pair_meet_json") or "{}").items() if not k.startswith("plant_rev")}
        if po != pn: pm_d.append(s_)
    return (f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") +
            f"; the `bad_met_first_json` tally **{len(bm_d)} differences**" + (f" ({bm_d[:4]})" if bm_d else "") + f"; the pair tally with d28f75da5's alias pairs dropped **{len(pm_d)} differences**" + (f" (seeds {pm_d[:5]})" if pm_d else "") +
            "; `pick_json` compared apart — it carries the new counters (the free members at the picks) and is the one column that differs by construction.")
def verdict(text, shown, refuted): return f"- {text} **{'Shown' if shown else ('Refuted' if refuted else 'Neither')}.**"
CHK = []
def chk(ok, text): CHK.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def in_band(x, lo, hi): return (not np.isnan(x)) and lo <= x <= hi
def paired(A, B, k, kb=None):
    kb = kb or k; A_, B_ = {r["seed"]: r for r in A}, {r["seed"]: r for r in B}; sd = sorted(set(A_) & set(B_)); return mse([B_[s][kb] - A_[s][k] for s in sd]), np.mean([A_[s][k] for s in sd]), np.mean([B_[s][kb] for s in sd]), len(sd)
def two_se(dd): return (not np.isnan(dd[1])) and dd[1] > 0 and abs(dd[0]) > 2 * dd[1]
# ------------------------------------------------------------------ the record
CW3_25 = load([f"{D25}/rerun/cw3-s21-70", f"{D25}/rerun/cw3-s71-120"], "careful")[1]; CW3 = load([f"{D26}/rerun/cw3-s21-70", f"{D26}/rerun/cw3-s71-120"], "careful")[1] or CW3_25
R29 = load([f"{D25}/rerun/r29-s21-70", f"{D25}/rerun/r29-s71-120"], "mix:caseM0.2:0.75")[0]; R26 = load([f"{D22}/r26/s21-70", f"{D22}/r26/s71-120"], "mix:caseM0.2:1.0")[0]
R25 = load([f"{D24}/rerun/r25-s21-70", f"{D24}/rerun/r25-s71-120"], "mix:caseM0.1:1.0")[0]; R9 = load([f"{D19}/rerun/r9-s21-70", f"{D19}/rerun/r9-s71-120"], "mix:doseM0.1:0.25")[0]
R16 = load([f"{D18}/r16/s21-70", f"{D18}/r16/s71-120"], "mix:doseM1.0:0.25")[0]; R19 = load([f"{D22}/rerun/r19-s21-70", f"{D22}/rerun/r19-s71-120"], "mix:doseM0.2:0.25")[0]
P11 = load([f"{D26}/rerun/p11-s21-70", f"{D26}/rerun/p11-s71-120"], "mix:caseM0.1p0.1:1.0")[0]
C35 = load([f"{D26}/r35/s21-70", f"{D26}/r35/s71-120"], "careful")[1]; C35a = load([f"{D26}/r35a/s21-70", f"{D26}/r35a/s71-120"], "careful")[1]
R36 = load([f"{D26}/r36/s21-70", f"{D26}/r36/s71-120"], "mix:caseM0.2:0.75")[0]; R36a = load([f"{D26}/r36a/s21-70", f"{D26}/r36a/s71-120"], "mix:caseM0.2:0.75")[0]
R37 = load([f"{D26}/r37/s21-70", f"{D26}/r37/s71-120"], "mix:caseM0.1p0.98:0.25")[0]; R38 = load([f"{D26}/r38/s21-70", f"{D26}/r38/s71-120"], "mix:caseM0.2p0:0.25")[0]
R39 = load([f"{D26}/r39/s21-70", f"{D26}/r39/s71-120"], "mix:caseM0.2p0:0.75")[0]; R40 = load([f"{D26}/r40/s21-70", f"{D26}/r40/s71-120"], "mix:caseM0.2p0:1.0")[0]
L = ["# Addendum 30 — the seats drawn, and the conduct with two doses: reads 35 to 40 (November 18, 2026; notes §125)\n"]
if P11 and R25: L.append(repro(P11, R25, "caseM0.1p0.1 on every slot (the conduct with its two doses equal) against read 25 (a24/rerun/r25 at d28f75da5, itself 0 differences against a22/rerun)"))
if CW3 is not CW3_25 and CW3_25: L.append(repro(list(CW3.values()), list(CW3_25.values()), "world 3's all-careful run again whole at a4fc4f6c4 (a25/rerun/cw3 at 8e30eac40)"))
L.append(f"\nLoaded: cw3 {len(CW3)} (record {len(CW3_25)}), r29 {len(R29)}, r26 {len(R26)}, r25 {len(R25)}, r9 {len(R9)}, r16 {len(R16)}, r19 {len(R19)}; p11 {len(P11)}, r35 {len(C35)}, r35a {len(C35a)}, r36 {len(R36)}, r36a {len(R36a)}, r37 {len(R37)}, r38 {len(R38)}, r39 {len(R39)}, r40 {len(R40)} episodes.\n")
# ------------------------------------------------------------------ 1. reads 35 and 36
L += ["## 1. Reads 35 and 36: the audit and panel seats drawn (world 3's cell, seeds 21–120)\n",
      "Two seatings beside the record's round-robin: **`--seat-draw seats`** (read 35 / 36 of record here — the audit and panel seats drawn among the free panel-eligible members at the seat's turn, on a stream of their own salted on the seed; the first review the round-robin's as today, whose pointer a drawn seat does not move), and **`--assignment seeded`** as the option stands (35a / 36a — every pick drawn, the first review among them, from the world's own stream, which also draws the tasks' truths, the care, the careful error and the audit roll: another world at the seed, so its figures against the record are not paired). The pair tally as §124 gave it; the free panel-eligible members at the audit pick (a reading in every mode).\n",
      "| population | seating | audit seat's holder | member audit seats a run | pairs that meet | **meetings a pair that meets** | **more than three (share)** | the largest | members a first reviewer meets | λ, the even spread | by chance (Poisson): mean / share > 3 | the reviewer's range |", "|---|---|---|---|---|---|---|---|---|---|---|---|"]
PR = {}
for key, nm, st, E, sides in (("cw3", "world 3's all-careful", "round-robin (the record)", list(CW3.values()), (None,)), ("r35", "read 35", "**the seats drawn**", list(C35.values()), (None,)), ("r35a", "read 35a", "`--assignment seeded`", list(C35a.values()), (None,)),
                              ("r29", "read 29: case-keyed M at 0.2 on 3 in 4", "round-robin (the record)", R29, (None, "careful", "conduct")), ("r36", "read 36", "**the seats drawn**", R36, (None, "careful", "conduct")), ("r36a", "read 36a", "`--assignment seeded`", R36a, (None, "careful", "conduct"))):
    for side in sides:
        P = [p for p in (pairs_of(e, side) for e in E) if p]
        if not P: continue
        lam = np.mean(col(P, "lam")); ch = pois(lam); PR[(key, side)] = dict(mean=mse(col(P, "mean")), gt3=mse(col(P, "gt3")), mx=np.mean(col(P, "mx")), partners=mse(col(P, "partners")), lam=lam, ch=ch, rows=P)
        ex = {("r35", None): "1.5–2.6 / 0.02–0.22; partners 14–22", ("r36", "careful"): "2.6–3.8 / 0.24–0.45; partners 7–9", ("r36", "conduct"): "1.2–1.9"}.get((key, side), "—")
        L.append(f"| {nm} | {st} | {side or 'any member'} | {np.mean(col(P, 'meetings')):.0f} | {np.mean(col(P, 'pairs')):.0f} | **{pm(mse(col(P, 'mean')), 2)}** | **{pm(mse(col(P, 'gt3')), 2)}** | {np.mean(col(P, 'mx')):.1f} | {pm(mse(col(P, 'partners')), 1)} | {lam:.2f} | {ch[0]:.2f} / {ch[1]:.2f} | {ex} |")
L += ["\n**The free panel-eligible members at the audit pick** (every mode; the picks where a member takes the seat):\n", "| population | seating | audit picks a run | free on the mean | one alone | two | three or more | panel picks a run: free on the mean; one alone |", "|---|---|---|---|---|---|---|---|"]
FR = {}
for key, nm, st, E in (("cw3", "world 3's all-careful", "round-robin", list(CW3.values())), ("r35", "read 35", "the seats drawn", list(C35.values())), ("r35a", "read 35a", "seeded", list(C35a.values())), ("r29", "read 29", "round-robin", R29), ("r36", "read 36", "the seats drawn", R36), ("r36a", "read 36a", "seeded", R36a),
                       ("r38", "read 38", "round-robin", R38), ("r39", "read 39", "round-robin", R39), ("r40", "read 40", "round-robin", R40)):
    F_ = [frees(e) for e in E if frees(e)["n"]]; Fp = [frees(e, "panel") for e in E if frees(e, "panel")["n"]]
    if not F_: continue
    FR[key] = dict(mean=mse(col(F_, "mean")), one=mse(col(F_, "one")), two=mse(col(F_, "two")), three=mse(col(F_, "three")))
    L.append(f"| {nm} | {st} | {np.mean(col(F_, 'n')):.0f} | **{pm(FR[key]['mean'], 2)}** | **{pm(FR[key]['one'], 2)}** | {pm(FR[key]['two'], 2)} | {pm(FR[key]['three'], 2)} | {np.mean(col(Fp, 'mean')):.2f}; {np.mean(col(Fp, 'one')):.2f} |")
if "cw3" in FR: L.append(f"\nThe reviewer's Poisson sketch from read 34's fallback share (R): 2.0 free on the mean where a member takes the seat, one alone 0.42, two 0.32, three or more 0.26. The count in world 3's all-careful: {FR['cw3']['mean'][0]:.2f} on the mean, one alone {FR['cw3']['one'][0]:.2f}, two {FR['cw3']['two'][0]:.2f}, three or more {FR['cw3']['three'][0]:.2f}.\n")
# read 35 against cw3 by seed: six figures
P35 = pop_rows(list(C35.values()), CW3) if C35 else []; P35a = pop_rows(list(C35a.values()), CW3) if C35a else []
SIX = (("life", "the slot of record", 0), ("w_leak", "the leak, ‰", 1), ("w_fa", "standing false approvals a run", 1), ("w_oh", "the overhead a vested task", 2), ("aud", "audit seats a slot", 1), ("ss_audit", "the state's share of the audit seats", 3))
for nm, P in (("**Read 35 (the seats drawn) against world 3's all-careful by seed**", P35), ("Read 35a (`--assignment seeded`, another world at the seed) against world 3's all-careful, by seed as a form", P35a)):
    if not P: continue
    L += [f"\n{nm} — the six figures of the reviewer's condition (no more than one beyond two standard errors):\n", "| measure | world 3's all-careful | this | **this − all-careful** (SE) | beyond 2 SE |", "|---|---|---|---|---|"]
    n_out = 0
    for k, lab, d_ in SIX:
        k0 = {"life": "lifec", "aud": "audc", "ss_audit": "ss0_audit"}.get(k, k.replace("w_", "w0_")); dd = mse(col(P, k) - col(P, k0)); out = two_se(dd); n_out += out
        L.append(f"| {lab} | {np.mean(col(P, k0)):.{d_}f} | {np.mean(col(P, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) | {'yes' if out else 'no'} |")
    for k, lab, d_ in (("good", "good ticks a slot", 0), ("susp", "suspensions a slot", 2), ("reach", "suspended at least once", 2), ("noseat", "member ticks without the earned seats", 3), ("w_cot", "the cost of truth", 0), ("w_m", "m_t over the periods", 3), ("w_Pt", "P_t at the end", 1)):
        k0 = {"good": "goodc", "susp": "suspc", "reach": "reachc", "noseat": "noseatc"}.get(k, k.replace("w_", "w0_")); dd = mse(col(P, k) - col(P, k0))
        L.append(f"| {lab} | {np.nanmean(col(P, k0)):.{d_}f} | {np.nanmean(col(P, k)):.{d_}f} | {dd[0]:+.{d_}f} ± {dd[1]:.{d_}f} ({se_(dd)}) | |")
    if P is P35: SIX35 = n_out
    L.append(f"\nFigures of the six beyond two standard errors: **{n_out}**.\n")
# read 36 against r29 by seed
Q29 = rows_of(R29, CW3); Q36 = rows_of(R36, CW3); Q36a = rows_of(R36a, CW3); PD29 = paid_by_seed(R29); PD36 = paid_by_seed(R36); PD36a = paid_by_seed(R36a)
SIX36 = None
for nm, Q, PD in (("**Read 36 (the seats drawn) against read 29 by seed**", Q36, PD36), ("Read 36a (`--assignment seeded`) against read 29, by seed as a form", Q36a, PD36a)):
    if not Q: continue
    L += [f"\n{nm} — the six figures of the condition:\n", "| measure | read 29 | this | **this − read 29** (SE) | beyond 2 SE |", "|---|---|---|---|---|"]
    n_out = 0
    for k, lab, d_ in (("rec", "the conduct's gap of record (careful quarter − conduct)", 0), ("lvl", "the conduct's level saving of record", 2), ("audc", "the careful quarter's audit seats a slot", 1), ("ss_audit", "the state's share of the audit seats", 3), ("w_leak", "the leak, ‰", 1), ("paid", "the share of the conduct's claims that stays paid", 3)):
        A_ = {r["seed"]: r for r in Q29}; B_ = {r["seed"]: r for r in Q}; sd = sorted(set(A_) & set(B_))
        if k == "lvl":
            a_ = [(A_[s]["rec"] + A_[s]["ben"]) / A_[s]["call"] for s in sd]; b_ = [(B_[s]["rec"] + B_[s]["ben"]) / B_[s]["call"] for s in sd]; xa, xb = xs(Q29)[0], xs(Q)[0]
        elif k == "paid": a_ = [PD29[s] for s in sd]; b_ = [PD[s] for s in sd]; xa, xb = (np.nanmean(a_), np.nan), (np.nanmean(b_), np.nan)
        else: a_ = [A_[s][k] for s in sd]; b_ = [B_[s][k] for s in sd]; xa, xb = (np.mean(a_), np.nan), (np.mean(b_), np.nan)
        dd = mse(np.array(b_) - np.array(a_)); out = two_se(dd); n_out += out
        L.append(f"| {lab} | {xa[0]:.{d_}f} | {xb[0]:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) | {'yes' if out else 'no'} |")
    for k, lab, d_ in (("care_vs_all", "the careful quarter − the all-careful's slot", 0), ("aud", "the conduct's audit seats a slot", 1), ("w_fa", "standing false approvals a run", 1), ("w_oh", "the overhead a vested task", 2), ("w_m", "m_t over the periods", 3)):
        dd, ma_, mb_, n_ = paired(Q29, Q, k)
        if np.isnan(dd[0]): L.append(f"| {lab} | — (the record has no dial column) | {mb_:.{d_}f} | — | |"); continue
        L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | {dd[0]:+.{d_}f} ± {dd[1]:.{d_}f} ({se_(dd)}) | |")
    if Q is Q36: SIX36 = n_out
    L.append(f"\nFigures of the six beyond two standard errors: **{n_out}**.\n")
# ------------------------------------------------------------------ 2. reads 37 to 40
L += ["## 2. Reads 37 to 40: the conduct with two doses (`caseM<q>p<qP>`; Baruchi's word of November 18) in world 3's cell, seeds 21–120\n",
      "Cell A (`caseM0.1p0.98`): a dose of 0.1 on real cases and of 0.98 on planted bad cases — tests that see the model. Cell B (`caseM0.2p0`): 0.2 on real cases and none on planted bad cases — tests that do not. A planted good case goes as a real one, at the dose on real cases; careful on probation. The conduct reads the case's kind from the driver's own record (the env's `is_plant` and the plant's truth), outside the convention and declared so.\n",
      "**The three shares as the engine counts them** — of the planted bad cases a slot meets as a member, the share it gives a wrong verdict on (the conduct's slots; the careful slots beside them); of the real bad work it reviews first as a member, the share it approves; beside them a planted good case rejected:\n",
      "| read | conduct | slots: conduct / careful | planted bad cases met as a member (conduct / careful) | **wrong on them: conduct / careful** | planted good met (conduct / careful) | rejected: conduct / careful | real bad work reviewed first as a member (conduct / careful) | **approved: conduct / careful** | the cell's three shares (R) |", "|---|---|---|---|---|---|---|---|---|---|"]
Q37 = rows_of(R37, CW3); Q38 = rows_of(R38, CW3); Q39 = rows_of(R39, CW3); Q9 = rows_of(R9, CW3); Q16 = rows_of(R16, CW3); Q19 = rows_of(R19, CW3); P40 = pop_rows(R40, CW3); P26 = pop_rows(R26, CW3); P25 = pop_rows(R25, CW3)
def share_row(nm, cd, Q, pop=False, exp="—"):
    if not Q: return None
    a = ratio_se([r["pwb_share"] * r["pb_met"] for r in Q], [r["pb_met"] for r in Q]); ac = ratio_se([r["pwb_sharec"] * r["pb_metc"] for r in Q], [r["pb_metc"] for r in Q])
    g_ = ratio_se([r["pwg_share"] * r["pg_met"] for r in Q], [r["pg_met"] for r in Q]); gc = ratio_se([r["pwg_sharec"] * r["pg_metc"] for r in Q], [r["pg_metc"] for r in Q])
    b = ratio_se([r["fai_share"] * r["rb_first"] for r in Q], [r["rb_first"] for r in Q]); bc = ratio_se([r["fai_sharec"] * r["rb_firstc"] for r in Q], [r["rb_firstc"] for r in Q])
    def alt(t, key):   # the record before a4fc4f6c4 has no shares by kind: the wrong planted verdicts of either kind over the planted cases met, marked
        if not np.isnan(t[0]): return pm(t, 3)
        kb, kg = key.replace("pw_any_share", "pb_met"), key.replace("pw_any_share", "pg_met")
        x = ratio_se([r[key] * (r[kb] + r[kg]) for r in Q], [r[kb] + r[kg] for r in Q])
        return f"({pm(x, 3)} either kind)" if not np.isnan(x[0]) else "—"
    fb = lambda t: pm(t, 3) if not np.isnan(t[0]) else "—"
    return f"| {nm} | {cd} | {np.mean(col(Q, 'n')):.1f} / {np.mean(col(Q, 'nc')):.1f} | {np.mean(col(Q, 'pb_met')):.1f} / {np.mean(col(Q, 'pb_metc')):.1f} | **{alt(a, 'pw_any_share')} / {alt(ac, 'pw_any_sharec')}** | {np.mean(col(Q, 'pg_met')):.1f} / {np.mean(col(Q, 'pg_metc')):.1f} | {fb(g_)} / {fb(gc)} | {np.mean(col(Q, 'rb_first')):.1f} / {np.mean(col(Q, 'rb_firstc')):.1f} | **{fb(b)} / {fb(bc)}** | {exp} |"
for row in (share_row("**37: cell A on 1 in 4**", "caseM0.1p0.98", Q37, exp="0.981, 0.05, 0.145"), share_row("**38: cell B on 1 in 4**", "caseM0.2p0", Q38, exp="0.05, 0.05, 0.24"), share_row("**39: cell B on 3 in 4**", "caseM0.2p0", Q39, exp="0.05, 0.05, 0.24"),
            share_row("**40: cell B on every slot** (the careful column: world 3's all-careful)", "caseM0.2p0", P40, exp="0.05, 0.05, 0.24"), share_row("9: M at 0.1 drawn at each review on 1 in 4 (the record)", "doseM0.1", Q9), share_row("16: M at 1.0 on 1 in 4 (the record)", "doseM1.0", Q16), share_row("19: M at 0.2 on 1 in 4 (the record)", "doseM0.2", Q19),
            share_row("29: case-keyed M at 0.2 on 3 in 4 (the record)", "caseM0.2", Q29), share_row("26: case-keyed M at 0.2 on every slot (the record)", "caseM0.2", P26)):
    if row: L.append(row)
L.append("\nThe shares by kind are the per-slot export's `pwb_` / `pwg_` keys (a wrong verdict on a planted case by the plant's kind — new at a4fc4f6c4); the reads of record predate them, so their columns carry in parentheses the wrong planted verdicts of either kind over the planted cases of both kinds met as a member (the all-careful's column of read 40 is the a26 rerun's, by kind). Read 16's record predates the first reviews by the work's kind too (906fc5ac4).\n")
# read 37
HDR = ["| read | seeds | slots a seed: conduct / careful beside | **careful − conduct, of record** (SE) | temptation | with the reservation | like for like | **the conduct's level saving: of record / with the reservation / like for like** | care a slot: conduct / careful beside | suspended ≥ 1: conduct / careful | member reviews before the first suspension (conduct) | member reviews in a life: conduct / careful | audit seats a slot: conduct / careful | wrong planted verdicts as a member: conduct / careful | leak ‰ | FA | overhead |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def qrow(nm, Q):
    a, b, c = mse(col(Q, "rec")), mse(col(Q, "res")), mse(col(Q, "lfl")); x = xs(Q); t_ = temp(Q, "rec", "ben")
    return (f"| {nm} | {len(Q)} | {np.mean(col(Q, 'n')):.1f} / {np.mean(col(Q, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({se_(a)}) | {t_[0]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(Q, 'call')):.0f} / {np.mean(col(Q, 'carec')):.0f} | "
            f"{np.mean(col(Q, 'reach')):.2f} / {np.mean(col(Q, 'reachc')):.2f} | {np.nanmean(col(Q, 'pre_susp')):.1f} | {np.mean(col(Q, 'rvm')):.1f} / {np.mean(col(Q, 'rvmc')):.1f} | {np.mean(col(Q, 'aud')):.1f} / {np.mean(col(Q, 'audc')):.1f} | {np.mean(col(Q, 'pw')):.2f} / {np.mean(col(Q, 'pwc')):.2f} | {np.mean(col(Q, 'w_leak')):.1f} | {np.mean(col(Q, 'w_fa')):.1f} | {np.mean(col(Q, 'w_oh')):.2f} |")
L += ["\n### Read 37: cell A on 1 slot in 4, the rest careful (read as reads 9 and 16 were)\n"] + HDR
for nm, Q in (("**37: cell A (0.1 real / 0.98 planted bad) on 1 in 4**", Q37), ("16: M at 1.0 on 1 in 4 (the record)", Q16), ("9: M at 0.1 on 1 in 4 (the record)", Q9)):
    if Q: L.append(qrow(nm, Q))
if Q37:
    d37 = fa_split(bm(R37)); L.append(f"\nThe closure tally of the conduct's claims on real bad work at the first review (by whose audit): {d37['claims']:.1f} claims a run, **{d37['paid']:.2f} stay paid** ({d37['none']:.2f} never audited, {d37['mconf']:.2f} confirmed by a member's audit, {d37['sconf']:.2f} by the state's), {1 - d37['paid']:.2f} overturned ({d37['mdiff']:.2f} after a member's audit differed, {d37['sdiff']:.2f} after the state's); of {d37['tot']:.0f} real bad deliveries a run {d37['fm']:.2f} reviewed first by a member, {d37['fp']:.2f} on probation, {d37['fs']:.3f} by the state.\n")
# read 38
L += ["\n### Read 38: cell B on 1 slot in 4, the rest careful (read as read 19 was)\n"] + HDR
for nm, Q in (("**38: cell B (0.2 real / 0 planted bad) on 1 in 4**", Q38), ("19: M at 0.2 on 1 in 4 (the record)", Q19)):
    if Q: L.append(qrow(nm, Q))
if Q38:
    d38 = fa_split(bm(R38)); L += [f"\nClaims a run {d38['claims']:.1f} (R: 16–21), of which **{d38['paid']:.2f} stay paid** (R: 0.16–0.28; {d38['none']:.2f} never audited, {d38['mconf']:.2f} a member's audit confirmed, {d38['sconf']:.2f} the state's), {1 - d38['paid']:.2f} overturned ({d38['mdiff']:.2f} a member's audit differed, {d38['sdiff']:.2f} the state's).\n",
                 "**The conduct's slots against the careful beside them by seed** — the four figures of the reviewer's condition (none beyond two standard errors):\n", "| measure | the careful beside | the conduct | **conduct − careful** (SE) | beyond 2 SE |", "|---|---|---|---|---|"]
    n_out = 0
    for k, lab, d_ in (("reach", "suspended at least once (share)", 3), ("aud", "audit seats a slot", 1), ("rvm", "member reviews in a life", 1), ("pw", "wrong planted verdicts as a member", 3)):
        dd = mse(col(Q38, k) - col(Q38, k + "c")); out = two_se(dd); n_out += out
        L.append(f"| {lab} | {np.mean(col(Q38, k + 'c')):.{d_}f} | {np.mean(col(Q38, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) | {'yes' if out else 'no'} |")
    for k, lab, d_ in (("noseat", "member ticks without the earned seats (share)", 3), ("good", "good ticks a slot", 0), ("susp", "suspensions a slot", 3), ("panel", "panel seats a slot", 1)):
        dd = mse(col(Q38, k) - col(Q38, k + "c")); L.append(f"| {lab} | {np.nanmean(col(Q38, k + 'c')):.{d_}f} | {np.nanmean(col(Q38, k)):.{d_}f} | {dd[0]:+.{d_}f} ± {dd[1]:.{d_}f} ({se_(dd)}) | |")
    FOUR38 = n_out; L.append(f"\nFigures of the four beyond two standard errors: **{n_out}**.\n")
# read 39
L += ["\n### Read 39: cell B on 3 slots in 4, the rest careful (read as read 29 was, and against read 29 by seed)\n"] + HDR
for nm, Q in (("**39: cell B on 3 in 4**", Q39), ("29: case-keyed M at 0.2 on 3 in 4 (the record)", Q29)):
    if Q: L.append(qrow(nm, Q))
if Q39:
    d39 = fa_split(bm(R39)); cva = mse(col(Q39, "care_vs_all")); cva29 = mse(col(Q29, "care_vs_all"))
    L += [f"\nThe careful quarter's slot against world 3's all-careful slot by seed **{cva[0]:+.0f} ± {cva[1]:.0f}** (R: within 30; read 29's {cva29[0]:+.0f} ± {cva29[1]:.0f}); the careful quarter holds {np.mean(col(Q39, 'audc')):.1f} audit seats a slot (R: 32–44; read 29's {np.mean(col(Q29, 'audc')):.1f}). Claims a run {d39['claims']:.1f} (R: 54–64; read 29's 59.4), **{d39['paid']:.2f} stay paid** (R: 0.46–0.60; read 29's 0.23 — {d39['none']:.2f} never audited, {d39['mconf']:.2f} a member's audit confirmed, {d39['sconf']:.2f} the state's; {d39['mdiff']:.2f} / {d39['sdiff']:.2f} overturned after a member's / the state's audit). "
          f"The state's share of the seats: the first review {np.nanmean(col(Q39, 'ss_first')):.3f}, the audit seat **{np.nanmean(col(Q39, 'ss_audit')):.3f}** (R: 0.30–0.36; read 29's 0.380), the panels {np.nanmean(col(Q39, 'ss_panel')):.3f}.\n",
          "**Read 39 against read 29 by seed:**\n", "| measure | read 29 | read 39 | **read 39 − read 29** (SE) |", "|---|---|---|---|"]
    for k, lab, d_ in (("rec", "the conduct's gap of record", 0), ("res", "with the reservation", 0), ("lfl", "like for like", 0), ("life", "the conduct's slot of record", 0), ("lifec", "the careful quarter's slot", 0), ("care_vs_all", "the careful quarter − the all-careful", 0), ("aud", "the conduct's audit seats a slot", 1), ("audc", "the careful quarter's audit seats", 1), ("reach", "the conduct suspended at least once", 3), ("noseat", "the conduct's member ticks without the earned seats", 3), ("rvm", "the conduct's member reviews", 1), ("ss_audit", "the state's share of the audit seats", 3)):
        dd, ma_, mb_, n_ = paired(Q29, Q39, k); L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    for k, kk, lab, d_ in WK:
        if k in ("m", "mend", "pi"): continue
        dd, ma_, mb_, n_ = paired(Q29, Q39, f"w_{k}"); L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
# read 40
L += ["\n### Read 40: cell B on every slot (read as read 26 was: against world 3's all-careful, and against read 26 by seed)\n",
      "| read | seeds | slots a seed | **all-careful − population, of record** (SE) | temptation | with the reservation | like for like | **the population's level saving: of record / with the reservation / like for like** | care a slot (population / all-careful) | audit seats a slot (population / all-careful) | member ticks without the earned seats (population / all-careful) | the state's share of the audit seats (population / all-careful) | suspended ≥ 1 | good ticks | leak ‰ | FA | overhead | m_t over the periods (population / all-careful) |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def prow(nm, P):
    a, b, c = mse(col(P, "rec")), mse(col(P, "res")), mse(col(P, "lfl")); x = xs(P); t_ = temp(P, "rec", "ben")
    return (f"| {nm} | {len(P)} | {np.mean(col(P, 'n')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({se_(a)}) | {t_[0]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(P, 'call')):.0f} / {np.mean(col(P, 'carec')):.0f} | {np.mean(col(P, 'aud')):.1f} / {np.mean(col(P, 'audc')):.1f} | "
            f"{np.nanmean(col(P, 'noseat')):.3f} / {np.nanmean(col(P, 'noseatc')):.3f} | {np.nanmean(col(P, 'ss_audit')):.3f} / {np.nanmean(col(P, 'ss0_audit')):.3f} | {np.mean(col(P, 'reach')):.2f} | {np.mean(col(P, 'good')):.0f} | {np.mean(col(P, 'w_leak')):.1f} | {np.mean(col(P, 'w_fa')):.1f} | {np.mean(col(P, 'w_oh')):.2f} | {('—' if np.all(np.isnan(col(P, 'w_m'))) else f"{np.nanmean(col(P, 'w_m')):.3f}")} / {np.nanmean(col(P, 'w0_m')):.3f} |")
for nm, P in (("**40: cell B on every slot**", P40), ("26: case-keyed M at 0.2 on every slot (the record)", P26), ("25: case-keyed M at 0.1 on every slot (the record)", P25)):
    if P: L.append(prow(nm, P))
if P40:
    d40 = fa_split(bm(R40)); d26 = fa_split(bm(R26))
    L += [f"\nClaims a run {d40['claims']:.1f} (R: 70–82; read 26's {d26['claims']:.1f}), **{d40['paid']:.2f} stay paid** (R: 0.63–0.76; read 26's {d26['paid']:.2f} — {d40['none']:.2f} never audited, {d40['mconf']:.2f} a member's audit confirmed, {d40['sconf']:.2f} the state's; {d40['mdiff']:.2f} / {d40['sdiff']:.2f} overturned after a member's / the state's audit). The dial: m_t over the periods {np.nanmean(col(P40, 'w_m')):.3f} against the all-careful's {np.nanmean(col(P40, 'w0_m')):.3f} (π_t {np.nanmean(col(P40, 'w_pi')):.3f} / {np.nanmean(col(P40, 'w0_pi')):.3f}; at the end {np.nanmean(col(P40, 'w_mend')):.3f} / {np.nanmean(col(P40, 'w0_mend')):.3f}) — the overhead's dial reads the planted record, which in cell B is a careful population's.\n",
          "**Read 40 against read 26 by seed** (the population's slot and the world's side):\n", "| measure | read 26 | read 40 | **read 40 − read 26** (SE) |", "|---|---|---|---|"]
    for k, lab, d_ in (("life", "the population's slot, lifetime of record", 0), ("lres", "with the reservation", 0), ("rec", "all-careful − population, of record", 0), ("good", "good ticks a slot", 0), ("susp", "suspensions a slot", 2), ("reach", "suspended at least once", 2), ("rvm", "member reviews a slot", 1), ("aud", "audit seats a slot", 1), ("noseat", "member ticks without the earned seats", 3), ("ss_audit", "the state's share of the audit seats", 3), ("claims", "claims a slot", 1)):
        dd, ma_, mb_, n_ = paired(P26, P40, k); L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    for k, kk, lab, d_ in WK:
        if k in ("m", "mend", "pi"): continue
        dd, ma_, mb_, n_ = paired(P26, P40, f"w_{k}"); L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    LEAK40 = paired(P26, P40, "w_leak")[0]
# ------------------------------------------------------------------ 3. expectations and conditions
L += ["\n## 3. Against the expectations stated before the run (AJ6), and the five conditions\n"]
if ("r35", None) in PR:
    p = PR[("r35", None)]; chk(in_band(p["mean"][0], 1.5, 2.6), f"read 35: a pair that meets meets 1.5–2.6 times ({p['mean'][0]:.2f})"); chk(in_band(p["gt3"][0], 0.02, 0.22), f"read 35: 0.02–0.22 of them more than three times ({p['gt3'][0]:.2f})"); chk(in_band(p["partners"][0], 14, 22), f"read 35: a first reviewer meets 14–22 members ({p['partners'][0]:.1f})")
if "r35" in FR: chk(in_band(FR["r35"]["mean"][0], 1.6, 2.6), f"read 35: 1.6–2.6 members free on the mean where a member takes the audit seat ({FR['r35']['mean'][0]:.2f})"); chk(in_band(FR["r35"]["one"][0], 0.30, 0.50), f"read 35: one alone at 0.30–0.50 of the turns ({FR['r35']['one'][0]:.2f})")
if P35: chk(SIX35 <= 1, f"read 35: no more than one of six figures beyond two standard errors against world 3's all-careful ({SIX35})")
if ("r36", "careful") in PR:
    p = PR[("r36", "careful")]; chk(in_band(p["mean"][0], 2.6, 3.8), f"read 36, a careful slot at the audit seat: 2.6–3.8 meetings a pair ({p['mean'][0]:.2f})"); chk(in_band(p["gt3"][0], 0.24, 0.45), f"read 36: 0.24–0.45 more than three times ({p['gt3'][0]:.2f})"); chk(in_band(p["partners"][0], 7, 9), f"read 36: a first reviewer meets 7–9 careful slots ({p['partners'][0]:.1f})")
if ("r36", "conduct") in PR: p = PR[("r36", "conduct")]; chk(in_band(p["mean"][0], 1.2, 1.9), f"read 36, the conduct's slot at the audit seat: 1.2–1.9 meetings a pair ({p['mean'][0]:.2f})")
if Q36: chk(SIX36 <= 1, f"read 36: no more than one of six figures beyond two standard errors against read 29 ({SIX36})")
if Q37:
    x37 = xs(Q37); a37 = mse(col(Q37, "rec"))
    chk(in_band(100 * np.mean(col(Q37, "reach")), 66, 82), f"read 37: 66–82 in 100 of the conduct's slots suspended at least once ({100 * np.mean(col(Q37, 'reach')):.0f})"); chk(in_band(np.nanmean(col(Q37, "pre_susp")), 24, 31), f"read 37: the first suspension after 24–31 member reviews ({np.nanmean(col(Q37, 'pre_susp')):.1f})")
    chk(in_band(np.mean(col(Q37, "rvm")), 24, 33), f"read 37: 24–33 member reviews in a life ({np.mean(col(Q37, 'rvm')):.1f})"); chk(in_band(a37[0], 620, 760), f"read 37: behind the careful beside by 620–760 of record ({a37[0]:.0f})"); chk(in_band(x37[0][0], 7.5, 11), f"read 37: a level saving of 7.5–11 ({x37[0][0]:.2f})"); chk(in_band(np.mean(col(Q37, "w_leak")), 4, 8), f"read 37: a leak of 4–8 ‰ ({np.mean(col(Q37, 'w_leak')):.1f})")
if Q38:
    x38 = xs(Q38); a38 = mse(col(Q38, "rec"))
    chk(in_band(-a38[0], 10, 55), f"read 38: the conduct ahead of the careful beside by 10–55 of record ({-a38[0]:+.0f})"); chk(in_band(x38[0][0], -0.05, 0.15), f"read 38: a level saving of −0.05–0.15 ({x38[0][0]:.2f})"); chk(FOUR38 == 0, f"read 38: none of four figures beyond two standard errors ({FOUR38})")
    chk(in_band(d38["claims"], 16, 21), f"read 38: 16–21 claims a run ({d38['claims']:.1f})"); chk(in_band(d38["paid"], 0.16, 0.28), f"read 38: 0.16–0.28 of them stay paid ({d38['paid']:.2f})"); chk(in_band(np.mean(col(Q38, "w_leak")), 10, 16), f"read 38: a leak of 10–16 ‰ ({np.mean(col(Q38, 'w_leak')):.1f})")
if Q39:
    x39 = xs(Q39); a39 = mse(col(Q39, "rec"))
    chk(in_band(-a39[0], 15, 60), f"read 39: the conduct ahead of the careful quarter by 15–60 of record ({-a39[0]:+.0f})"); chk(in_band(x39[0][0], -0.05, 0.12), f"read 39: a level saving of −0.05–0.12 ({x39[0][0]:.2f})"); chk(in_band(np.mean(col(Q39, "audc")), 32, 44), f"read 39: the careful quarter holds 32–44 audit seats a slot ({np.mean(col(Q39, 'audc')):.1f})")
    chk(abs(cva[0]) <= 30, f"read 39: the careful quarter within 30 real of the all-careful slot ({cva[0]:+.0f})"); chk(in_band(d39["claims"], 54, 64), f"read 39: 54–64 claims a run ({d39['claims']:.1f})"); chk(in_band(d39["paid"], 0.46, 0.60), f"read 39: 0.46–0.60 stay paid ({d39['paid']:.2f})")
    chk(in_band(np.mean(col(Q39, "w_leak")), 53, 75), f"read 39: a leak of 53–75 ‰ ({np.mean(col(Q39, 'w_leak')):.1f})"); chk(in_band(np.mean(col(Q39, "w_fa")), 27, 38), f"read 39: 27–38 standing false approvals ({np.mean(col(Q39, 'w_fa')):.1f})"); chk(in_band(np.mean(col(Q39, "w_oh")), 11.6, 13.2), f"read 39: an overhead of 11.6–13.2 ({np.mean(col(Q39, 'w_oh')):.2f})"); chk(in_band(np.nanmean(col(Q39, "ss_audit")), 0.30, 0.36), f"read 39: the state's share of the audit seats 0.30–0.36 ({np.nanmean(col(Q39, 'ss_audit')):.3f})")
if P40:
    x40 = xs(P40); a40 = mse(col(P40, "rec"))
    chk(in_band(-a40[0], 15, 60), f"read 40: the population's slot ahead of the all-careful's by 15–60 of record ({-a40[0]:+.0f})"); chk(in_band(x40[0][0], -0.05, 0.10), f"read 40: a level saving of −0.05–0.10 ({x40[0][0]:.2f})"); chk(in_band(np.mean(col(P40, "aud")), 32, 40), f"read 40: 32–40 audit seats a slot ({np.mean(col(P40, 'aud')):.1f})")
    chk(in_band(np.nanmean(col(P40, "noseat")), 0.57, 0.66), f"read 40: without the earned seats on 0.57–0.66 of the member ticks ({np.nanmean(col(P40, 'noseat')):.3f})"); chk(in_band(np.nanmean(col(P40, "ss_audit")), 0.30, 0.37), f"read 40: the state's share of the audit seats 0.30–0.37 ({np.nanmean(col(P40, 'ss_audit')):.3f})")
    chk(in_band(d40["claims"], 70, 82), f"read 40: 70–82 claims a run ({d40['claims']:.1f})"); chk(in_band(d40["paid"], 0.63, 0.76), f"read 40: 0.63–0.76 stay paid ({d40['paid']:.2f})"); chk(in_band(np.mean(col(P40, "w_leak")), 94, 122), f"read 40: a leak of 94–122 ‰ ({np.mean(col(P40, 'w_leak')):.1f})")
    chk(in_band(np.mean(col(P40, "w_fa")), 48, 62), f"read 40: 48–62 standing false approvals ({np.mean(col(P40, 'w_fa')):.1f})"); chk(in_band(np.mean(col(P40, "w_oh")), 11.6, 13.0), f"read 40: an overhead of 11.6–13.0 ({np.mean(col(P40, 'w_oh')):.2f})")
L += CHK + [f"\n**{sum(1 for c in CHK if c.startswith('- MET'))} of {len(CHK)} expectations met.**\n", "\n**The five conditions, each apart:**\n"]
if ("r35", None) in PR: m35 = PR[("r35", None)]["mean"]; L.append(verdict(f"A draw among the members that are free spreads the pairs (read 35's pair that meets meets {pm(m35, 2)} times; shown if under 2.6 by two SE, refuted if 2.6 or more at the point).", m35[0] + 2 * m35[1] < 2.6, m35[0] >= 2.6))
if Q37: L.append(verdict(f"Tests that a model fails as the cheapest model failed the previews hold it in the design as ruled, where it misses real work only as at a dose of 0.1 (read 37's level saving {pm(x37[0], 2)} of record; shown if above 0.9 by two SE, refuted if under 0.9 at the point).", x37[0][0] - 2 * x37[0][1] > 0.9, x37[0][0] < 0.9))
if Q38: L.append(verdict(f"Nothing in the design as ruled holds a member on a model that passes the tests as a careful review does and misses real bad work one time in four (read 38's level saving {pm(x38[0], 2)}; shown if under 0.9 by two SE, refuted if 0.9 or more at the point).", x38[0][0] + 2 * x38[0][1] < 0.9, x38[0][0] >= 0.9))
if Q39: L.append(verdict(f"Among members of whom most are on such a model, care pays a member no better than the model (read 39's level saving {pm(x39[0], 2)} for the conduct against the careful quarter; shown if under 0.9 by two SE, refuted if 0.9 or more at the point).", x39[0][0] + 2 * x39[0][1] < 0.9, x39[0][0] >= 0.9))
if P40 and P26: L.append(verdict(f"The buyers get more bad work paid than where the record sees the same model (read 40's leak against read 26's by seed {LEAK40[0]:+.1f} ± {LEAK40[1]:.1f} ‰; shown if above by two SE, refuted if at or under at the point).", LEAK40[0] > 2 * LEAK40[1], LEAK40[0] <= 0))
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("wrote", sys.argv[1], len(L), "lines")
