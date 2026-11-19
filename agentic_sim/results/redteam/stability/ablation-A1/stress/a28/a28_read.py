"""Addendum 33 (November 18, 2026, late night → read November 19; notes §127): the readings asked from the record (point 6), the reviewer's arithmetic (point 5) confirmed or replaced,
and nine reads without training at dc5b49896 — reads 48 to 50 (nothing built: cell B on 1 slot in 4 with the complaint at a detection of 1 and the second filing; cell B on every
slot with the detection at 0.5 and at 0.2), reads 51 to 56 (two options off by default: `--troop-no-vote on`, the state's audit that differed as no vote of the court; `--seat-draw
seats --draw-min K`, the state's troops as candidates in the draw up to a minimum), the four things of addendum 32 and the two rates of overturning for every read. World 3's
all-careful, read 35, read 46 and read 19 run again whole at this commit for the readings the record does not carry (the pool at a seat's first seating step and how it was filled;
the filed challenges' panels by holder and end; the state's look by the draw) and checked to the key against a27/, a26/ and a19/ first. a27_read.py's helpers copied. Usage: a28_read.py OUT.md"""
import json, os, sys, hashlib, math, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D28, D27, D26, D25, D22, D19 = f"{R}/a28", f"{R}/a27", f"{R}/a26", f"{R}/a25", f"{R}/a22", f"{R}/a19"
T = 1000; RES = 0.8; EPS = 0.05; D_FEE = 2.0
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
        if pol in j["episodes"]: E += [e for e in j["episodes"][pol] if not e.get("error") or e.get("error") == "None"]
        if "careful" in j["episodes"]: C.update({int(e["seed"]): e for e in j["episodes"]["careful"] if not e.get("error") or e.get("error") == "None"})
    return E, C
def D(E): return {int(e["seed"]): e for e in E}
def col(rows, k): return np.array([r[k] for r in rows], float)
SEATS = ("initial", "resumed", "audit", "third", "appeal", "dispute")
def ev_delivery(v): return sum(val for k, val in v.items() if k.startswith("ev_") and k.endswith("_delivery") and isinstance(val, (int, float)))
def stats_(V):
    n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n; g = lambda k: sum((v.get(k, 0) or 0) for v in V) / n
    tm = sum(v.get("ticks_member", 0) for v in V); arr = [v for v in V if v["t_in"] > 0]; sus = [v for v in V if v["suspensions"] > 0]
    pb = sum(v.get(f"rvm_plant_bad_{s}", 0) for v in V for s in SEATS); pwb = sum(v.get(f"pwb_member_{s}", 0) for v in V for s in SEATS); pg = sum(v.get(f"rvm_plant_good_{s}", 0) for v in V for s in SEATS); pwg = sum(v.get(f"pwg_member_{s}", 0) for v in V for s in SEATS)
    rb = sum(v.get("rvi_member_real_bad", 0) for v in V); fai = sum(v.get("fai_member", 0) for v in V); has_kind = any(k.startswith(("pwb_", "pwg_")) for v in V for k in v)
    rho_s = sum(v.get("rho_member_sum", 0) or 0 for v in V); rho_e = [v["rho_end"] for v in V if v.get("rho_end") not in (None, "")]
    noseat_rec = sum(1 for v in V if v.get("ticks_member_noseat", 0) > v.get("ticks_member_noseat_undet", 0)) / n
    return dict(n=n, good=good, ig=ig, bg=bg, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n, ben=g("private_real"),
                claims=g("claims"), claims_m=g("claims_member"), susp=g("suspensions"), aud=g("audits_done"), panel=g("rvm_appeal") + g("rvm_third") + g("rvm_dispute"), care_m=g("care_member"), claimed_m=g("claimed_member"), rvm=g("rv_member"), reach=len(sus) / n,
                pre_susp=(np.mean([v.get("rvm_pre_susp", 0) for v in sus]) if sus else np.nan), dep=sum(1 for v in V if not v["alive"]) / n,
                tm=tm / n, noseat=(sum(v.get("ticks_member_noseat", 0) for v in V) / tm) if tm else np.nan, undet=(sum(v.get("ticks_member_noseat_undet", 0) for v in V) / tm) if tm else np.nan, noseat_rec=noseat_rec,
                lost_phase=sum(1 for v in V if v.get("pf_ticks_lost", 0) > 0) / n, fa=g("fa_init"), fpaid=g("fa_init") - g("fa_init_overturned"), fover=g("fa_init_overturned"),
                pw=sum(g(f"pw_member_{s}") for s in SEATS), pb_met=pb / n, pwb=pwb / n, pwb_share=(pwb / pb if (pb and has_kind) else np.nan), pwg_share=(pwg / pg if (pg and has_kind) else np.nan), pg_met=pg / n, rb_first=rb / n, fai_share=(fai / rb if rb else np.nan),
                marks=g("marks_real"), rho_m=(rho_s / tm if tm else np.nan), rho_end=(np.mean(rho_e) if rho_e else np.nan), awards=g("awards"), work=sum(ev_delivery(v) for v in V) / n,
                ra_first=g("ra_first"), ra_member=g("ra_member"), ra_state=g("ra_state"), ra_never=g("ra_never"), ra_panel=g("ra_panel"), ra_over=g("ra_over"), ra_over_member=g("ra_over_member"), ra_over_state=g("ra_over_state"), ra_over_panel=g("ra_over_panel"),
                adm=(sum(1 for v in arr if "adm_ticks" in v) / len(arr)) if arr else np.nan, aud_inc=g("rf_member_audit_fee") + g("rf_member_audit_emission") + g("rf_member_audit_uplift"),
                bonds=g("bonds_forfeited"), fee_init=g("fee_initial"))
def state_share(e):
    tin = e.get("troop_initial_seats"); tr, ta, tp, ds = f(e, "troop_reviews"), f(e, "troop_audits"), f(e, "troop_panel_seats"), f(e, "deciding_seats")
    tin = float(tin) if tin not in (None, "") else (tr - tp - ds)
    mi = f(e, "seated_initial_member") + f(e, "seated_initial_probationer"); ma = f(e, "seated_audit_member"); mp = f(e, "seated_appeal_member"); tpa = tp - ta
    return {"first": tin / (tin + mi) if (tin + mi) else np.nan, "audit": ta / (ta + ma) if (ta + ma) else np.nan, "panel": tpa / (tpa + mp) if (tpa + mp) else np.nan}
WK = (("fa", "false_approvals", "standing false approvals a run", 1), ("leak", "leak_bad", "the leak, ‰ of bad deliveries", 1), ("oh", "sys_overhead_per_vested", "the system overhead a vested task", 2), ("cot", "cost_of_truth", "the cost of truth a run", 0),
      ("dep", "departures", "departures a run", 1), ("arr", "arrivals", "arrivals a run", 1), ("Pt", "P_t", "P_t at the end", 1), ("m", "m_mean", "the dial's m_t, the mean over the periods", 3), ("susp", "suspensions", "suspensions a run", 1), ("bd", "bad_deliveries", "bad deliveries a run", 0),
      ("marks", "real_miss_marks", "marks for a miss on real work a run", 1), ("disp", "disputes_filed", "disputes filed a run", 1), ("dwon", "disputes_won", "disputes won", 1), ("sf", "second_filings", "second filings", 1), ("sfw", "second_filings_won", "second filings won", 1), ("sfl", "second_filings_lost", "second filings lost", 1),
      ("lapsed", "second_windows_lapsed", "confirmations final at the window's close", 1), ("declined", "second_declined", "the party declined to go on", 1), ("unf", "second_unfunded", "second filings unfunded", 1), ("paidf", "req_court_paid_real", "court fees the requesters put down, real", 1), ("backf", "req_court_back_real", "court fees back to the requesters, real", 1),
      ("care_r", "care_cost_real", "care on real cases (nominal)", 0), ("care_p", "care_cost_plant", "care on planted cases", 0), ("troopc", "troop_review_cost", "the troops' review cost", 0), ("pprice", "plant_price_sum", "the plants' price", 0), ("nv", "vested_real_roots", "vested real roots", 0), ("dec", "deciding_opened", "deciding verdicts opened", 1), ("pa_disp", "pa_disputed", "planted approvals disputed", 1), ("pdisp", "plant_disputes_filed", "the plant requester's disputes", 1))
def world(e): return {k: (1000 * f(e, kk) if k == "leak" else f(e, kk)) for k, kk, _, _ in WK}
def bmj(e): return {k: float(v) for k, v in json.loads(e.get("bad_met_first_json") or "{}").items()}
def raj(e): return {k: float(v) for k, v in json.loads(e.get("ra_json") or "{}").items()}
def three(e):
    """AL4.2: of a member's real bad deliveries, approved at first (any first reviewer), stopped before payment (overturned), paid in the end — from the closure tally; the mirror (wrong rejections of good work standing) beside."""
    b = bmj(e); appr = sum(v for k, v in b.items() if k.startswith("fa_") and k.count("_") == 2); over = sum(v for k, v in b.items() if "_overturned_" in k); paid = sum(v for k, v in b.items() if "_paid_" in k)
    mirror = sum(v for k, v in b.items() if k.startswith("frn_")); mirror_audit = sum(v for k, v in b.items() if k.startswith("frn_") and "audit_upheld" in k); mirror_state = sum(v for k, v in b.items() if k.startswith("frn_") and "audit_upheld" in k and k.endswith("_state"))
    return dict(appr=appr, over=over, paid=paid, mirror=mirror, mirror_audit=mirror_audit, mirror_state=mirror_state)
def pop_rows(E, C):
    out = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in C: continue
        V, Vc = slots(e), slots(C[s_]); S_, Cc = stats_(V), stats_(Vc); call = S_["care_m"] + S_["claimed_m"]
        out.append(dict(seed=s_, n=len(V), nc=len(Vc), rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], call=call, carec=Cc["care_m"],
                        **{k: S_[k] for k in S_ if k not in ("n", "ben")}, **{k + "c": Cc[k] for k in Cc if k not in ("n",)},
                        **{f"w_{k}": v for k, v in world(e).items()}, **{f"w0_{k}": v for k, v in world(C[s_]).items()}, **{f"ss_{k}": v for k, v in state_share(e).items()}, **{f"ss0_{k}": v for k, v in state_share(C[s_]).items()}, **{f"t_{k}": v for k, v in three(e).items()}, **{f"t0_{k}": v for k, v in three(C[s_]).items()}))
    return out
def rows_of(E, C=None):
    """Read 38's shape: the conduct's slots against the careful slots beside them in the same world, each seed; C the all-careful of the cell for the careful group's gain over it."""
    out = []
    for e in E:
        g = groups(e); s_ = int(e["seed"])
        if not g["claim"] or not g["care"]: continue
        S_, Cc = stats_(g["claim"]), stats_(g["care"]); Ca = stats_(slots(C[s_])) if (C and s_ in C) else None; call = S_["care_m"] + S_["claimed_m"]
        out.append(dict(seed=s_, n=S_["n"], nc=Cc["n"], rec=Cc["life"] - S_["life"], res=Cc["lres"] - S_["lres"], lfl=Cc["ig"] - S_["rate"] * Cc["good"], lfl_num=Cc["ig"] * S_["good"] / Cc["good"] - S_["ig"] - S_["ben"], ben=S_["ben"], call=call, carec=Cc["care_m"],
                        **{k: S_[k] for k in S_ if k not in ("n", "ben")}, **{k + "c": Cc[k] for k in Cc if k not in ("n",)},
                        lifea=Ca["life"] if Ca else np.nan, care_vs_all=(Cc["life"] - Ca["life"]) if Ca else np.nan, aud_all=Ca["aud"] if Ca else np.nan,
                        **{f"w_{k}": v for k, v in world(e).items()}, **{f"ss_{k}": v for k, v in state_share(e).items()}, **{f"t_{k}": v for k, v in three(e).items()}))
    return out
def xs(P, keys=("rec", "res", "lfl_num")): return tuple(ratio_se(col(P, k) + col(P, "ben"), col(P, "call")) for k in keys)
def temp(P, k, den): t = ratio_se(col(P, k), col(P, den)); return 1 + t[0], t[1]
def g_of(B): return lambda k: float(np.mean([r.get(k, 0.0) for r in B]))
def fa_split(E):
    B = [bmj(e) for e in E]; g = g_of(B); keys = {k for r in B for k in r}; cl = g("fa_member_claim"); paid = sum(g(k) for k in keys if k.startswith("fa_member_claim_paid")); ov = sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned"))
    d = dict(claims=cl, paid=paid / cl if cl else np.nan, none=g("fa_member_claim_paid_none") / cl if cl else np.nan, mconf=g("fa_member_claim_paid_audit_member_confirmed") / cl if cl else np.nan, sconf=g("fa_member_claim_paid_audit_state_confirmed") / cl if cl else np.nan,
             pconf=g("fa_member_claim_paid_panel") / cl if cl else np.nan,
             mdiff=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_audit_member")) / cl if cl else np.nan, sdiff=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_audit_state")) / cl if cl else np.nan,
             pan=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_panel")) / cl if cl else np.nan, pan2=sum(g(k) for k in keys if k.startswith("fa_member_claim_overturned_panel") and k.endswith("_second")) / cl if cl else np.nan)
    tot = g("first_member") + g("first_probation") + g("first_state"); d.update(tot=tot, fm=g("first_member") / tot if tot else np.nan, fp=g("first_probation") / tot if tot else np.nan, fs=g("first_state") / tot if tot else np.nan)
    care = g("fa_member_care"); d.update(care=care, care_over=(sum(g(k) for k in keys if k.startswith("fa_member_care_overturned")) / care) if care else np.nan)
    return d
def paid_by_seed(E):
    out = {}
    for e in E:
        b = bmj(e); cl = b.get("fa_member_claim", 0); paid = sum(v for k, v in b.items() if k.startswith("fa_member_claim_paid")); out[int(e["seed"])] = (paid / cl) if cl else np.nan
    return out
NEW_ROW = {"ra_json", "real_miss_marks", "second_filings", "second_filings_won", "second_filings_lost", "second_windows_lapsed", "second_filed_dispute", "second_filed_appeal", "second_unfunded", "second_refused", "second_declined", "req_court_paid_real", "req_court_back_real", "care_cost_real", "care_cost_plant", "plant_price_sum", "vested_real_roots"}
NEW_SLOT = {"rho_member_mean", "rho_end", "marks_real", "rho_member_sum"}

def pairs_of(e, side=None):
    pmj = {k: v for k, v in json.loads(e.get("pair_meet_json") or "{}").items() if not k.startswith("plant_rev")}
    if side is not None:
        c = careful_of(e); pmj = {k: v for k, v in pmj.items() if c(k.split("|")[1]) == (side == "careful")}
    if not pmj: return None
    ns = [len(v) for v in pmj.values()]
    return dict(seed=int(e["seed"]), pairs=len(ns), meetings=sum(ns), mean=np.mean(ns), gt3=sum(1 for x in ns if x > 3) / len(ns), mx=max(ns))
def repro(new_eps, old_eps, label, skip_json_prefix=("dpanel", "statedrawn", "troop_drawn", "_free_0", "troopdrawn")):
    """The record's keys compared one by one (a column or a per-slot key the record lacks is not compared; the json tallies parsed, the new sub-keys left out)."""
    old = {int(e["seed"]): e for e in old_eps}; n_rows = n_keys = n_slots = n_seeds = 0; diffs = []; js_d = []
    for e in new_eps:
        s_ = int(e["seed"])
        if s_ not in old: continue
        o = old[s_]; n_seeds += 1
        for k in o:
            if k.endswith("_json") or k not in e: continue
            n_rows += 1
            if o[k] != e[k]: diffs.append((s_, k))
        So, Sn = json.loads(o["learner_slots_json"]), json.loads(e["learner_slots_json"])
        for x, v in So.items():
            n_slots += 1
            for k, val in v.items():
                n_keys += 1
                if Sn.get(x, {}).get(k) != val: diffs.append((s_, x, k))
        for k in ("bad_met_first_json", "pair_meet_json", "pair_fail_json", "pick_json", "ra_json", "seats_by_kind_json"):
            if k not in o or o.get(k) in (None, ""): continue
            a = json.loads(o[k] or "{}"); b = {kk: vv for kk, vv in json.loads(e.get(k) or "{}").items() if not any(p in kk for p in skip_json_prefix)}
            if a != b: js_d.append((s_, k))
    return (f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") +
            f"; the json tallies (the closure, the pairs, the picks, the second looks, the seats by kind) **{len(js_d)} differences**" + (f" ({js_d[:5]})" if js_d else "") + "; the columns and sub-keys the record lacks are compared apart.")
CHK = []
def chk(ok, text): CHK.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def in_band(x, lo, hi): return (not np.isnan(x)) and lo <= x <= hi
def paired(A, B, k, kb=None):
    kb = kb or k; A_, B_ = {r["seed"]: r for r in A}, {r["seed"]: r for r in B}; sd = sorted(set(A_) & set(B_)); return mse([B_[s][kb] - A_[s][k] for s in sd]), np.mean([A_[s][k] for s in sd]), np.mean([B_[s][kb] for s in sd]), len(sd)
def two_se(dd): return (not np.isnan(dd[1])) and dd[1] > 0 and abs(dd[0]) > 2 * dd[1]
def verdict(text, shown, refuted): return f"- {text} **{'Shown' if shown else ('Refuted' if refuted else 'Neither')}.**"
def sj(e): return {k: float(v) for k, v in json.loads(e.get("seat_json") or "{}").items()}
def sbk(e): return {k: float(v) for k, v in json.loads(e.get("seats_by_kind_json") or "{}").items()}
def frn(e):
    b = bmj(e); return {k[4:]: v for k, v in b.items() if k.startswith("frn_")}
# ------------------------------------------------------------------ the record and the reads
CW3o = load([f"{D27}/rerun/cw3-s21-70", f"{D27}/rerun/cw3-s71-120"], "careful")[1]; CW3 = load([f"{D28}/rerun/cw3-s21-70", f"{D28}/rerun/cw3-s71-120"], "careful")[1] or CW3o
R35o = load([f"{D26}/r35/s21-70", f"{D26}/r35/s71-120"], "careful")[1]; R35 = load([f"{D28}/rerun/r35-s21-70", f"{D28}/rerun/r35-s71-120"], "careful")[1] or R35o
R46o = load([f"{D27}/r46/s21-70", f"{D27}/r46/s71-120"], "mix:caseM0.2p0:1.0")[0]; R46 = load([f"{D28}/rerun/r46-s21-70", f"{D28}/rerun/r46-s71-120"], "mix:caseM0.2p0:1.0")[0] or R46o
R19o = load([f"{D19}/r19/s21-45", f"{D19}/r19/s46-70", f"{D19}/r19/s71-95", f"{D19}/r19/s96-120"], "mix:doseM0.2:0.25")[0]; R19 = load([f"{D28}/rerun/r19-s21-70", f"{D28}/rerun/r19-s71-120"], "mix:doseM0.2:0.25")[0] or R19o
R38 = load([f"{D27}/rerun/r38-s21-70", f"{D27}/rerun/r38-s71-120"], "mix:caseM0.2p0:0.25")[0]; R40 = load([f"{D27}/rerun/r40-s21-70", f"{D27}/rerun/r40-s71-120"], "mix:caseM0.2p0:1.0")[0]
R42 = load([f"{D27}/r42/s21-70", f"{D27}/r42/s71-120"], "mix:caseM1.0p0:0.25")[0]; R43 = load([f"{D27}/r43/s21-70", f"{D27}/r43/s71-120"], "careful")[1]; R44 = load([f"{D27}/r44/s21-70", f"{D27}/r44/s71-120"], "mix:caseM0.2p0:0.25")[0]
R45 = load([f"{D27}/r45/s21-70", f"{D27}/r45/s71-120"], "mix:caseM0.2p0:1.0")[0]; R46a = load([f"{D27}/r46a/s21-70", f"{D27}/r46a/s71-120"], "mix:caseM0.2p0:1.0")[0]; R47 = load([f"{D27}/r47/s21-70", f"{D27}/r47/s71-120"], "careful")[1]
R29 = load([f"{D25}/rerun/r29-s21-70", f"{D25}/rerun/r29-s71-120"], "mix:caseM0.2:0.75")[0]; CW3_25 = load([f"{D25}/rerun/cw3-s21-70", f"{D25}/rerun/cw3-s71-120"], "careful")[1]
R48 = load([f"{D28}/r48/s21-70", f"{D28}/r48/s71-120"], "mix:caseM0.2p0:0.25")[0]; R49 = load([f"{D28}/r49/s21-70", f"{D28}/r49/s71-120"], "mix:caseM0.2p0:1.0")[0]; R50 = load([f"{D28}/r50/s21-70", f"{D28}/r50/s71-120"], "mix:caseM0.2p0:1.0")[0]
R51 = load([f"{D28}/r51/s21-70", f"{D28}/r51/s71-120"], "careful")[1]; R52 = load([f"{D28}/r52/s21-70", f"{D28}/r52/s71-120"], "careful")[1]; R53 = load([f"{D28}/r53/s21-70", f"{D28}/r53/s71-120"], "careful")[1]; R54 = load([f"{D28}/r54/s21-70", f"{D28}/r54/s71-120"], "careful")[1]
R55 = load([f"{D28}/r55/s21-70", f"{D28}/r55/s71-120"], "mix:caseM0.2p0:1.0")[0]; R56 = load([f"{D28}/r56/s21-70", f"{D28}/r56/s71-120"], "mix:doseM0.2:0.25")[0]
CW3L, R35L = list(CW3.values()), list(R35.values())
L = ["# Addendum 33 — the state's audit as no vote, the troops in the draw, and the buyer's complaint on one member and at a lower detection: reads 48 to 56 (November 19, 2026; notes §127)\n"]
if CW3 is not CW3o and CW3o: L.append(repro(CW3L, list(CW3o.values()), "world 3's all-careful run again whole at dc5b49896 (a27/rerun/cw3 at 29cffb7c7)"))
if R35 is not R35o and R35o: L.append(repro(R35L, list(R35o.values()), "read 35 (the seats drawn) run again whole at dc5b49896 (a26/r35 at a4fc4f6c4)"))
if R46 is not R46o and R46o: L.append(repro(R46, R46o, "read 46 run again whole at dc5b49896 (a27/r46 at 29cffb7c7)"))
if R19 is not R19o and R19o: L.append(repro(R19, R19o, "read 19 (conduct M at 0.2 on 1 in 4) run again whole at dc5b49896 (a19/r19 at 906fc5ac4)"))
L.append(f"\nLoaded: cw3 {len(CW3)} (record {len(CW3o)}), r35 {len(R35)} (record {len(R35o)}), r46 {len(R46)} (record {len(R46o)}), r19 {len(R19)} (record {len(R19o)}), r38 {len(R38)}, r40 {len(R40)}, r42 {len(R42)}, r43 {len(R43)}, r44 {len(R44)}, r45 {len(R45)}, r46a {len(R46a)}, r47 {len(R47)}, r29 {len(R29)}; "
         f"r48 {len(R48)}, r49 {len(R49)}, r50 {len(R50)}, r51 {len(R51)}, r52 {len(R52)}, r53 {len(R53)}, r54 {len(R54)}, r55 {len(R55)}, r56 {len(R56)} episodes.\n")
Q38 = rows_of(R38, CW3); Q19 = rows_of(R19, CW3); Q48 = rows_of(R48, CW3); Q56 = rows_of(R56, CW3); Q44 = rows_of(R44, CW3)
P40 = pop_rows(R40, CW3); P46 = pop_rows(R46, CW3); P46v40 = pop_rows(R46, D(R40)); P45 = pop_rows(R45, CW3)
P49v40 = pop_rows(R49, D(R40)); P50v40 = pop_rows(R50, D(R40)); P49v46 = pop_rows(R49, D(R46)); P50v46 = pop_rows(R50, D(R46)); P49 = pop_rows(R49, CW3); P50 = pop_rows(R50, CW3)
P51 = pop_rows(list(R51.values()), CW3); P52 = pop_rows(list(R52.values()), R35); P53 = pop_rows(list(R53.values()), R35); P54 = pop_rows(list(R54.values()), R35); P53v52 = pop_rows(list(R53.values()), R52)
P52c = pop_rows(list(R52.values()), CW3); P53c = pop_rows(list(R53.values()), CW3); P54c = pop_rows(list(R54.values()), CW3); P35 = pop_rows(R35L, CW3)
P55v40 = pop_rows(R55, D(R40)); P55 = pop_rows(R55, CW3)
def ra_rate(e, who): r = raj(e); return (r.get(f"{who}_over", 0) / r[f"{who}_n"]) if r.get(f"{who}_n") else np.nan
# ------------------------------------------------------------------ 1. asked from the record (point 6) and the arithmetic (point 5)
L += ["## 1. Asked from the record (point 6), and the reviewer's arithmetic (point 5)\n"]
# 6.3 the mirror's base
fr_all = [f(e, "false_rejections") for e in CW3L]; fr_frn = [sum(frn(e).values()) for e in CW3L]; tg = [f(e, "troop_delivered_final_n") - f(e, "troop_bad_final_n") for e in CW3L]
L.append(f"**6.3 — the mirror's base: 5.28 against 5.17.** `false_rejections` counts every standing rejection of good work at a closure, the orchestrator's own deliveries included: {np.mean(fr_all):.2f} a run in world 3's all-careful. The `frn_*` tally behind the mirror of §126 counts a member's real roots alone: {np.mean(fr_frn):.2f}. The difference, {np.mean(np.array(fr_all) - np.array(fr_frn)):.2f} a run, is the state's own good deliveries rejected and standing ({np.mean(tg):.2f} = `troop_delivered_final_n` {np.mean([f(e, 'troop_delivered_final_n') for e in CW3L]):.2f} less `troop_bad_final_n` {np.mean([f(e, 'troop_bad_final_n') for e in CW3L]):.2f}). Both figures stand, each on its base; the mirror as AL4 reads it is the members' roots' 5.17.\n")
# 6.4 read 29's residual with every class
if R29 and CW3_25:
    rows = []
    for e in R29:
        s_ = int(e["seed"])
        if s_ not in CW3_25: continue
        Q = groups(e)["care"]; Vc = slots(CW3_25[s_])
        ev = lambda V: np.mean([sum(val for k, val in v.items() if k.startswith("ev_") and isinstance(val, (int, float))) for v in V])
        rows.append((np.mean([life(v) for v in Q]) - np.mean([life(v) for v in Vc]), ev(Q) - ev(Vc), f(e, "P_t") - f(CW3_25[s_], "P_t")))
    rows = np.array(rows); L.append(f"**6.4 — read 29's residual with every class of the wallet's events.** The careful quarter's slot against world 3's all-careful slot by seed: the gap of record {pm(mse(rows[:, 0]), 0)}, the sum of every `ev_*` class (the care and its reimbursement, the bonds and court fees, the fees, emission and uplift, the delivery, effort and guarantees, the loan and the float, a departure, other) {pm(mse(rows[:, 1]), 0)}, **the rest {pm(mse(rows[:, 0] - rows[:, 1]), 0)}** — §125's −246 ± 22 stands. It is not the decomposition's missing classes this time: the two slots live in different worlds, and the index at the end differs (read 29's P_t less world 3's {pm(mse(rows[:, 2]), 2)}), so the revaluation of the wealth held and the starting wallets, in no event, carry it. Reads 38 and 40's residuals were within one world, where the index cancels.\n")
# 6.5 read 42's suspensions by standing
if R42:
    def susp_split(V):
        pro = mem = 0
        for v in V:
            sp = v.get("spells", [])
            for t in v.get("susp_ticks", []):
                if any(s["t0"] <= t <= s.get("t1", 10**9) for s in sp): pro += 1
                else: mem += 1
        return pro / len(V), mem / len(V)
    a = [susp_split(groups(e)["claim"]) for e in R42]; c = [susp_split(groups(e)["care"]) for e in R42]
    dpro = mse([x[0] - y[0] for x, y in zip(a, c)]); dmem = mse([x[1] - y[1] for x, y in zip(a, c)])
    arr = lambda V, k: [v for v in V if (v.get("t_in", 0) > 0) == k]
    ra_ = np.nanmean([np.mean([v["suspensions"] > 0 for v in arr(groups(e)["claim"], True)]) if arr(groups(e)["claim"], True) else np.nan for e in R42]); rc_ = np.nanmean([np.mean([v["suspensions"] > 0 for v in arr(groups(e)["care"], True)]) if arr(groups(e)["care"], True) else np.nan for e in R42])
    fa_ = np.nanmean([np.mean([v["suspensions"] > 0 for v in arr(groups(e)["claim"], False)]) if arr(groups(e)["claim"], False) else np.nan for e in R42]); fc_ = np.nanmean([np.mean([v["suspensions"] > 0 for v in arr(groups(e)["care"], False)]) if arr(groups(e)["care"], False) else np.nan for e in R42])
    L.append(f"**6.5 — read 42: why the slots that read no real case are suspended less often (0.103 against 0.129).** The suspensions a slot by the standing at the time: on probation (inside a probation spell — an arrival's, or the way back after a suspension) the conduct's slots {np.mean([x[0] for x in a]):.3f} against the careful's {np.mean([x[0] for x in c]):.3f} ({dpro[0]:+.3f} ± {dpro[1]:.3f}); as a member {np.mean([x[1] for x in a]):.4f} against {np.mean([x[1] for x in c]):.4f} ({dmem[0]:+.4f} ± {dmem[1]:.4f}). By the slot's kind, suspended at least once: the founders {fa_:.3f} against {fc_:.3f}, the arrivals {ra_:.3f} against {rc_:.3f}. In one sentence: the whole difference sits in the arrival-born slots' probation, where the conduct is careful by construction and identical to the careful beside it, so no rule separates the two and the gap reads as the seeds' chance on a few hundred arrival slots (about 1.7 SE on the slots' own count), not as something the claims buy — as a member, where it claims, it is suspended as rarely as a careful member and only by its planted record.\n")
# 6.6 read 46's dispute panels (the rerun's dpanel tally)
def dpanel(E, kind):
    g = g_of([sbk(e) for e in E]); keys = {k for e in E for k in sbk(e) if k.startswith(f"dpanel_{kind}_")}
    tot = sum(g(k) for k in keys); byend = {}
    for k in keys:
        parts = k.split("_"); nt, end = parts[3], parts[4]; byend[(nt, end)] = byend.get((nt, end), 0) + g(k)
    st, sm, sd = g(f"dpanelseat_{kind}_troop"), g(f"dpanelseat_{kind}_member"), g(f"dpanelseat_{kind}_troopdrawn")
    return dict(tot=tot, byend=byend, troop=st, member=sm, drawn=sd, share=(st / (st + sm)) if (st + sm) else np.nan)
if R46 and any("dpanelseat_dispute_troop" in sbk(e) for e in R46):
    d = dpanel(R46, "dispute"); be = d["byend"]; e_ = lambda nt, end: be.get((nt, end), 0.0)
    conf = sum(v for (nt, end), v in be.items() if end == "confirmed"); esc = sum(v for (nt, end), v in be.items() if end == "escalated"); sec = sum(v for (nt, end), v in be.items() if end == "second")
    L.append(f"**6.6 — read 46's dispute panels** (the rerun at dc5b49896, the panel read at the closure of every disputed root; the record reproduced to the key). The state's share of the dispute panels' seats **{d['share']:.3f}** ({d['troop']:.1f} troop seats against {d['member']:.1f} members' a run; the appeal panels' {dpanel(R46, 'appeal')['share']:.3f}). Of the **{d['tot']:.1f}** disputes closed a run: the panel confirmed **{conf:.2f}** and the approval stayed (a second filing lost, declined, unfunded or lapsed, or none in the window), **{sec:.1f}** went on by a second filing after a confirmation, and the panel itself sent **{esc:.1f}** on by its own split — of those **{e_('t1', 'escalated') + e_('t2', 'escalated'):.1f}** with a troop among the two seats ({e_('t1', 'escalated'):.1f} with one, {e_('t2', 'escalated'):.1f} with two) and **{e_('t0', 'escalated'):.1f}** with two members (a careful member reading the truth on a case the model did not claim on: the careful errors' disputes). The panel never overturns under arm 1. Of the confirmations {e_('t0', 'confirmed'):.2f} had two members, {e_('t1', 'confirmed'):.2f} one troop, {e_('t2', 'confirmed'):.2f} two. "
             f"The reviewer's 5.2: with the state on {d['share']:.3f} of these seats a panel of two has a troop in it at {1 - (1 - d['share'])**2:.3f} and one that differs at {0.95 * (1 - (1 - d['share'])**2):.3f}; the read's 0.440 of the claims overturned at the panel's own escalation fits a share of 0.267 (R) — the share measured on the dispute panels is {d['share']:.3f}, {'inside' if abs(d['share'] - 0.267) < 0.03 else 'not'} his figure; the 0.235 of record is the share over every panel seat a review sat, the plants' panels included, where the state's own verdicts are not reviews.\n")
# 6.7 bad cases at a member's audit seat
L += ["**6.7 — what reaches a member's audit seat in a run**: the planted bad cases met at the audit seat (`bad_met_audit`, the harness's slots) and the real bad approvals a member's audit looked at (`ra_json`):\n", "| population | planted bad cases at a member's audit seat | real bad approvals looked at by a member's audit | by the state's audit | by a dispute panel | planted bad at the third seat / the appeal panels / the dispute panels |", "|---|---|---|---|---|---|"]
for nm, E in (("world 3's all-careful", CW3L), ("read 46 (disputes at 1, the second filing)", R46), ("read 47 (the all-careful with them)", list(R47.values())), ("read 40", R40)):
    if not E: continue
    g = g_of([raj(e) for e in E]); L.append(f"| {nm} | {np.mean([f(e, 'bad_met_audit') for e in E]):.1f} | {g('member_bad_n'):.1f} | {g('state_bad_n'):.1f} | {g('panel_bad_n'):.1f} | {np.mean([f(e, 'bad_met_third') for e in E]):.1f} / {np.mean([f(e, 'bad_met_appeal') for e in E]):.1f} / {np.mean([f(e, 'bad_met_dispute') for e in E]):.1f} |")
L.append("\nWith every planted approval and every bad plant approved disputed first at a detection of 1, the audit seat meets no planted bad case and about one real bad approval a run; the planted bad cases go to the dispute panels (about 210 a run) instead.\n")
# 6.8 read 46's population level saving
if P46:
    x46, x40, x45 = xs(P46)[0], xs(P40)[0], xs(P45)[0]; dl = mse(col(P46, "life") - col(P46, "lifec"))
    L.append(f"**6.8 — read 46's level saving for the population**, in read 40's form (the population's slot against world 3's all-careful slot by seed, the saving a ratio of the seeds' means): **{pm(x46, 2)}** (the slot {pm(dl, 0)} of record; read 40's {pm(x40, 2)}, read 45's {pm(x45, 2)}).\n")
# 6.9 by kind of slot (a27-read.md §5 AL4.1)
L.append("**6.9 — by kind of slot, the first approvals of real work that got an audit by who sat it, with read 44's marks.** It is in `a27-read.md` §5, table AL4.1 (the rows '38 the conduct', '38 the careful beside', '44 the conduct', '44 the careful beside'): a slot's first approvals of real work in a life, by a member's audit (n, share), the state's, a dispute panel, nobody, the overturns by each, the marks a slot and the wrong planted verdicts. The four rows again:\n")
L += ["| read | slot kind | slots | first approvals of real work a slot | **by a member: n (share)** | **by the state: n (share)** | by a dispute panel | never looked at | overturned: after a member's / the state's / a panel's | **marks a slot** | wrong planted verdicts as a member |", "|---|---|---|---|---|---|---|---|---|---|---|"]
def al_row(nm, kind, S_):
    fr = S_["ra_first"] or np.nan
    return f"| {nm} | {kind} | {S_['n']} | {S_['ra_first']:.1f} | **{S_['ra_member']:.1f} ({S_['ra_member'] / fr:.3f})** | **{S_['ra_state']:.1f} ({S_['ra_state'] / fr:.3f})** | {S_['ra_panel']:.1f} | {S_['ra_never']:.1f} | {S_['ra_over_member']:.2f} / {S_['ra_over_state']:.2f} / {S_['ra_over_panel']:.2f} | **{S_['marks']:.2f}** | {S_['pw']:.2f} |"
def al_rows(nm, E, mixed):
    out = []
    if not E or not any(raj(e) for e in E): return out
    if mixed:
        V = [v for e in E for v in groups(e)["claim"]]; Vc = [v for e in E for v in groups(e)["care"]]; S1, S2 = stats_(V), stats_(Vc); S1["n"], S2["n"] = round(len(V) / len(E), 1), round(len(Vc) / len(E), 1)
        out += [al_row(nm, "the conduct", S1), al_row(nm, "the careful beside", S2)]
    else:
        V = [v for e in E for v in slots(e)]; S1 = stats_(V); S1["n"] = round(len(V) / len(E), 1); out.append(al_row(nm, "every slot", S1))
    return out
L += al_rows("38", R38, True) + al_rows("44 (the mark)", R44, True)
# 6.10 the pool at a seat's first seating step (read 35's rerun; world 3's beside)
def pool_tab(E, kind):
    g = g_of([sj(e) for e in E]); pool = [g(f"seatpool_{kind}_{i}") for i in range(6)]; tot = sum(pool)
    fill = {k: g(f"seatfill_{kind}_{k}") for k in ("member_step1", "member_later", "state", "troop_drawn")}; ft = sum(fill.values())
    return dict(tot=tot, shares=[p / tot if tot else np.nan for p in pool], fill=fill, ft=ft, fshares={k: v / ft if ft else np.nan for k, v in fill.items()}, back=(fill["member_later"] / pool[0]) if pool[0] else np.nan)
if R35L and any(sj(e) for e in R35L):
    L += ["\n**6.10 — the draw's pool, from read 35's record run again whole** (the seats drawn, world 3's cell; the all-careful with today's picks beside): at an audit or panel seat's first seating step (the roll's tick; the filing's), the free panel-eligible members, as shares of the seats at 0, 1, 2, 3, 4 and 5 or more; how the seat was then filled — a member at the first step, a member at a later step (what the wait of two steps brings back), the state's troop after the wait; the troop's cost beside a member's care and pay.\n",
          "| cell | seat | seats a run | **free at the first step: 0** | 1 | 2 | 3 | 4 | 5 or more | filled by a member at the first step | by a member later | by the state | **of the seats with none free, a member came within the wait** |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
    for nm, E in (("read 35 (the seats drawn)", R35L), ("world 3's all-careful (today's picks)", CW3L), ("read 52 (K = 3)", list(R52.values())), ("read 53 (K = 3, (i))", list(R53.values())), ("read 54 (K = 5, (i))", list(R54.values()))):
        if not E or not any(sj(e) for e in E): continue
        for kind in ("audit", "panel"):
            p = pool_tab(E, kind); s = p["shares"]; fs = p["fshares"]
            L.append(f"| {nm} | {kind} | {p['tot']:.0f} | **{s[0]:.3f}** | {s[1]:.3f} | {s[2]:.3f} | {s[3]:.3f} | {s[4]:.3f} | {s[5]:.3f} | {fs['member_step1']:.3f} | {fs['member_later']:.3f} | {fs['state']:.3f}{(' (drawn ' + format(fs['troop_drawn'], '.3f') + ')') if fs['troop_drawn'] else ''} | **{p['back']:.3f}** |")
    tc = np.mean([f(e, "troop_review_cost") for e in CW3L]) / np.mean([f(e, "troop_reviews") for e in CW3L])
    L.append(f"\nThe pool of record (a26, 2.29 free at a member's pick) was read at the picks that were made; the first-step pool above includes the turns with none free, which is what the draw of a minimum sees. A troop's review costs the state c_T = 3.0 real purchased at the index ({tc:.2f} nominal a troop review on average in world 3's run), reimbursed from the request's allowance within K = 5 as a member's care is (the care drawn 2 or 3 nominal, 2.5 on average — 2.85 real at the cell's P_t); the seat's fee, 1.5 f = 3.0 nominal at the audit seat, is Ω's as the troops' wallet, with no emission share and no uplift (a member's 4.46 real beyond its care there, §118). Under the draw a troop sits at the seat's first step: the wait is gone, and the seats a member would have taken at the second step go to the draw.\n")
# 6.11 read 45's mirror by road
L += ["**6.11 — the mirror by road** (the wrong rejections of good work standing a run, by the engine's reason): appealed and lost at the deciding verdict; the audit road after the state's audit differed; after a member's; never appealed for want of the fee (accepted).\n", "| read | **standing** | appeal lost | audit road, the state's audit | audit road, a member's audit | accepted (unfunded) |", "|---|---|---|---|---|---|"]
def mir_row(nm, E):
    g = g_of([frn(e) for e in E]); return f"| {nm} | **{sum(g(k) for k in {kk for e in E for kk in frn(e)}):.2f}** | {g('appealed_appeal_upheld_nonfulfillment'):.2f} | {g('not_appealed_audit_upheld_nonfulfillment_state'):.2f} | {g('not_appealed_audit_upheld_nonfulfillment_member'):.2f} | {g('not_appealed_rejection_accepted'):.2f} |"
for nm, E in (("world 3's all-careful", CW3L), ("read 40", R40), ("read 43 (the all-careful, the mark)", list(R43.values())), ("**read 45** (every slot, the mark)", R45), ("read 46", R46), ("read 47", list(R47.values())), ("**read 51** ((i): the state's audit no vote)", list(R51.values())), ("read 35 (the seats drawn)", R35L), ("**read 52** (K = 3)", list(R52.values())), ("**read 53** (K = 3, (i))", list(R53.values())), ("**read 54** (K = 5, (i))", list(R54.values())), ("read 55", R55), ("read 56", R56)):
    if E: L.append(mir_row(nm, E))
# 5.1 and 5.5 from the record
if R43:
    mk = np.mean([f(e, "real_miss_marks") for e in R43.values()]); fo = np.mean([sum(v.get("fa_init_overturned", 0) for v in slots(e)) for e in R43.values()])
    L.append(f"\n**5.1 — one mark in eight follows a mistake of the court on good work.** Read 43: {mk:.1f} marks a run; the wrong first approvals of real bad work overturned {fo:.1f} a run (the slots' tally); the rest, {mk - fo:.1f}, are approvals of good work the deciding verdict overturned in error — {(mk - fo) / mk:.3f} of the marks, one in {mk / (mk - fo):.0f}. §126's 'about one mark in ten' is replaced by the reviewer's one in eight.")
st3, st40 = np.array([ra_rate(e, "state") for e in CW3L]), np.array([ra_rate(e, "state") for e in R40]); mb3, mb40 = np.array([ra_rate(e, "member") for e in CW3L]), np.array([ra_rate(e, "member") for e in R40])
L.append(f"\n**5.5 — the state's rate of overturning within one run.** The reviewer's arithmetic confirmed (2.7 SE from the two counts): run by run, the state's rate in world 3's all-careful is {st3.mean():.4f} with a spread of {st3.std(ddof=1):.4f} over the seeds (the highest run {st3.max():.4f}); in read 40 {st40.mean():.4f} ± {st40.std(ddof=1):.4f} (the lowest run {st40.min():.4f}); **{(st40 > st3.max()).sum()} of {len(st40)} of read 40's runs stand above the all-careful's highest run**, and {(st40 > np.percentile(st3, 95)).sum()} above its 95th percentile. The members' rate: {mb3.mean():.4f} ± {mb3.std(ddof=1):.4f} against {mb40.mean():.4f} ± {mb40.std(ddof=1):.4f}; {(mb40 > mb3.max()).sum()} of read 40's runs above the all-careful's highest — one run tells the state's rate apart and not the members', as he had it.\n")
# ------------------------------------------------------------------ shared tables
HDR = ["| read | seeds | slots a seed: conduct / careful beside | **careful − conduct, of record** (SE) | temptation | with the reservation | like for like | **level saving: of record / with the reservation / like for like** | care a slot: conduct / careful | claims a slot (as a member; share of its member reviews) | suspended ≥ once: conduct / careful | departed: conduct / careful | member reviews: conduct / careful | audit seats: conduct / careful | wrong planted verdicts as a member: conduct / careful |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def qrow(nm, Q):
    a, b, c = mse(col(Q, "rec")), mse(col(Q, "res")), mse(col(Q, "lfl")); x = xs(Q); t_ = temp(Q, "rec", "ben")
    return (f"| {nm} | {len(Q)} | {np.mean(col(Q, 'n')):.1f} / {np.mean(col(Q, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({se_(a)}) | {t_[0]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(Q, 'call')):.0f} / {np.mean(col(Q, 'carec')):.0f} | {np.mean(col(Q, 'claims_m')):.1f} ({np.mean(col(Q, 'claims_m')) / np.mean(col(Q, 'rvm')):.3f}) | "
            f"{np.mean(col(Q, 'reach')):.3f} / {np.mean(col(Q, 'reachc')):.3f} | {np.mean(col(Q, 'dep')):.2f} / {np.mean(col(Q, 'depc')):.2f} | {np.mean(col(Q, 'rvm')):.1f} / {np.mean(col(Q, 'rvmc')):.1f} | {np.mean(col(Q, 'aud')):.1f} / {np.mean(col(Q, 'audc')):.1f} | {np.mean(col(Q, 'pw')):.2f} / {np.mean(col(Q, 'pwc')):.2f} |")
WHO = ["| read | first approvals of bad work a run (claims; careful errors) | **stayed paid**: never looked at / a member's audit confirmed / the state's confirmed / a dispute panel confirmed | **overturned**: after a member's audit / the state's / the panel's own escalation / a second filing | of the claims alone: paid / overturned at the panel's escalation / after a second filing / after the state's audit / after a member's |", "|---|---|---|---|---|"]
def who_row(nm, E):
    B = [bmj(e) for e in E]; g = g_of(B); keys = {k for r in B for k in r if k.startswith("fa_")}
    base = {k: g(k) for k in keys if k.count("_") == 2}; tot = sum(base.values()); cl = g("fa_member_claim"); ce = tot - cl
    s = lambda *pats: sum(g(k) for k in keys if k.count("_") > 2 and all(p in k for p in pats))
    sx = lambda *pats: sum(g(k) for k in keys if k.count("_") > 2 and all(p in k for p in pats) and not k.endswith("_second"))
    pn, pm_, ps, pp = s("_paid_none"), s("_paid_audit_member"), s("_paid_audit_state"), s("_paid_panel")
    om, os_, op, o2 = sx("_overturned_audit_member"), sx("_overturned_audit_state"), sx("_overturned_panel"), s("_overturned_", "_second")
    d = fa_split(E)
    return (f"| {nm} | {tot:.1f} ({cl:.1f}; {ce:.1f}) | {pn:.2f} / {pm_:.2f} / {ps:.2f} / {pp:.2f} | {om:.2f} / {os_:.2f} / {op:.2f} / {o2:.2f} | "
            f"{d['paid']:.3f} / {d['pan'] - d['pan2']:.3f} / {d['pan2']:.3f} / {d['sdiff']:.3f} / {d['mdiff']:.3f} |") if cl else f"| {nm} | {tot:.1f} (—; {ce:.1f}) | {pn:.2f} / {pm_:.2f} / {ps:.2f} / {pp:.2f} | {om:.2f} / {os_:.2f} / {op:.2f} / {o2:.2f} | — |"
def ra_row(nm, E):
    Rr = [raj(e) for e in E]
    if not Rr or not any(Rr): return None
    g = g_of(Rr); tot = g("member_n") + g("state_n") + g("panel_n") + g("never_n")
    sh = lambda a, b: f"{g(a):.0f}; {g(b):.1f} ({g(b) / g(a):.3f})" if g(a) else "—"
    sd_ = (f" of them drawn {sh('statedrawn_n', 'statedrawn_over')}" if g("statedrawn_n") else "")
    return f"| {nm} | {tot:.0f} | **{sh('member_n', 'member_over')}** | {sh('member_bad_n', 'member_bad_over')} | **{sh('state_n', 'state_over')}**{sd_} | {sh('state_bad_n', 'state_bad_over')} | {sh('panel_n', 'panel_over')} | {g('never_n'):.0f}; {g('never_bad_n'):.1f} |"
RA_HDR = ["| population | first approvals of a member's real delivery a run | **looked at by a member's audit: n; overturned (share)** | of them bad: n; overturned | **by the state's audit: n; overturned (share)** | of them bad: n; overturned | by a dispute panel: n; overturned | never looked at: n; bad among them |", "|---|---|---|---|---|---|---|---|"]
def oh_row(nm, E):
    if not E or np.isnan(np.nanmean([f(e, "care_cost_real") for e in E])): return None
    nv = np.mean([f(e, "vested_real_roots") for e in E]); t = lambda k: np.mean([f(e, k) for e in E]) / nv
    return f"| {nm} | {nv:.0f} | {t('care_cost_real'):.2f} | {t('care_cost_plant'):.2f} | {t('troop_review_cost'):.2f} | {t('cost_of_truth'):.2f} | {t('plant_price_sum'):.2f} | **{np.mean([f(e, 'sys_overhead_per_vested') for e in E]):.2f}** | {np.mean([f(e, 'P_t') for e in E]):.2f} |"
OH_HDR = ["| population | vested real roots | care on real cases | care on planted | troops' review cost | cost of truth | plants' price | **overhead a vested task** | P_t at the end |", "|---|---|---|---|---|---|---|---|---|"]
def three_row(nm, E):
    th = [three(e) for e in E]; m = lambda k: np.mean([t[k] for t in th])
    return f"| {nm} | {np.mean([f(e, 'bad_deliveries') for e in E]):.0f} | **{m('appr'):.1f}** | **{m('over'):.1f}** | **{m('paid'):.1f}** | {np.mean([1000 * f(e, 'leak_bad') for e in E]):.1f} | **{m('mirror'):.2f}** | {m('mirror_audit'):.2f} | {m('mirror_state'):.2f} |"
THREE_HDR = ["| read | bad deliveries a run | **approved at first** | **stopped before payment** | **paid in the end** | leak ‰ | **wrong rejections of good work standing** | by the audit road | after the state's audit |", "|---|---|---|---|---|---|---|---|---|"]
def pair_row(nm, E):
    P = [p for p in (pairs_of(e) for e in E) if p]
    if not P: return None
    m = lambda k: np.mean([p[k] for p in P]); return f"| {nm} | {m('pairs'):.0f} | {m('meetings'):.0f} | **{pm(mse([p['mean'] for p in P]), 2)}** | {m('gt3'):.2f} | {m('mx'):.0f} |"
PAIR_HDR = ["| cell | pairs that meet a run (a first reviewer and the member at its audit seat) | meetings | **meetings a pair** | share of pairs meeting more than three times | the largest |", "|---|---|---|---|---|---|"]
def world_tab(nm_base, Pv, base_lab, rows):
    out = [f"\n**{nm_base}** — by seed:\n", f"| measure | {base_lab} | this | **this − {base_lab}** (SE) |", "|---|---|---|---|"]
    for k, k0, lab, d_ in rows:
        if not Pv or k not in Pv[0] or k0 not in Pv[0]: continue
        dd = mse(col(Pv, k) - col(Pv, k0)); out.append(f"| {lab} | {np.nanmean(col(Pv, k0)):.{d_}f} | {np.nanmean(col(Pv, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    return out
WROWS = (("life", "lifec", "the slot of record, real", 0), ("lres", "lresc", "with the reservation", 0), ("w_leak", "w0_leak", "**the leak, ‰**", 1), ("w_fa", "w0_fa", "standing false approvals a run", 1), ("w_oh", "w0_oh", "the overhead a vested task", 2), ("w_cot", "w0_cot", "the cost of truth", 0),
         ("aud", "audc", "**audit seats a slot**", 1), ("panel", "panelc", "panel seats a slot", 1), ("ss_audit", "ss0_audit", "**the state's share of the audit seats**", 3), ("ss_panel", "ss0_panel", "the state's share of the panel seats", 3), ("reach", "reachc", "slots suspended at least once", 3), ("susp", "suspc", "suspensions a slot", 3), ("dep", "depc", "departed", 3), ("good", "goodc", "good ticks a slot", 0), ("rho_m", "rho_mc", "ρ over the member ticks", 3),
         ("t_appr", "t0_appr", "bad deliveries approved at first", 1), ("t_over", "t0_over", "stopped before payment", 1), ("t_paid", "t0_paid", "paid in the end", 1), ("t_mirror", "t0_mirror", "**the mirror: wrong rejections of good work standing**", 2), ("t_mirror_audit", "t0_mirror_audit", "of them by the audit road", 2), ("t_mirror_state", "t0_mirror_state", "of them after the state's audit", 2),
         ("w_disp", "w0_disp", "disputes filed a run", 1), ("w_sf", "w0_sf", "second filings a run", 1), ("w_dec", "w0_dec", "deciding verdicts opened", 1), ("w_Pt", "w0_Pt", "P_t at the end", 2), ("w_dep", "w0_dep", "departures a run", 1), ("w_susp", "w0_susp", "suspensions a run", 1))
# ------------------------------------------------------------------ 2. reads 48 to 50: the complaint on one member, and at a lower detection
L += ["\n## 2. Reads 48 to 50: the buyer's complaint on one member, and where buyers notice one time in two and one in five (`--dispute-policy truthful --second-filing on`, `--dispute-rate` 1.0 / 0.5 / 0.2; world 3's cell, seeds 21–120; nothing built)\n",
      "The requester acts once, the tick after the approval and before any audit roll: it reads the truth and, where the work truly failed, disputes with probability `--dispute-rate` (a coin on the driver's stream); a disputed approval is never rolled for an audit, an undisputed one is rolled as today. So at a detection under 1 the bad approvals the buyer did not notice go to the audit seat as in read 40, and the ones it noticed to the panel and the court.\n"]
if Q48:
    L += ["**Read 48: cell B at a dose of 0.2 on 1 slot in 4 with the complaint at a detection of 1 and the second filing** (read as read 38 was; against read 38 by seed).\n"] + HDR + [qrow("**48: cell B on 1 in 4, the complaint**", Q48), qrow("38: the same without the complaint (the record)", Q38)]
    L += ["\n| measure | read 38 | **read 48** | **48 − 38** (SE) |", "|---|---|---|---|"]
    for k, lab, d_ in (("rec", "careful − conduct, of record", 0), ("res", "with the reservation", 0), ("lfl", "like for like", 0), ("fover", "the conduct's wrong first approvals overturned a slot", 2), ("fpaid", "the conduct's wrong first approvals that stayed paid a slot", 2), ("bonds", "the conduct's bonds forfeited (nominal)", 1), ("aud", "the conduct's audit seats", 1), ("audc", "the careful's audit seats", 1), ("rvm", "the conduct's member reviews", 1), ("claims", "the conduct's claims a slot", 1), ("reach", "the conduct's slots suspended at least once", 3), ("reachc", "the careful's", 3), ("awards", "the conduct's awards", 1), ("work", "the conduct's income from work, real", 0),
                       ("w_leak", "the leak ‰", 1), ("w_fa", "standing FA", 1), ("w_oh", "the overhead", 2), ("w_disp", "disputes a run", 1), ("w_sf", "second filings a run", 1), ("ss_audit", "the state's share of the audit seats", 3)):
        dd, ma_, mb_, n_ = paired(Q38, Q48, k); L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    x38, x48 = xs(Q38)[0], xs(Q48)[0]; A_, B_ = {r["seed"]: r for r in Q38}, {r["seed"]: r for r in Q48}; sd = sorted(set(A_) & set(B_))
    dl48 = mse([(B_[s]["rec"] + B_[s]["ben"]) / B_[s]["call"] - (A_[s]["rec"] + A_[s]["ben"]) / A_[s]["call"] for s in sd]); L.append(f"| the level saving of record | {x38[0]:.2f} | {x48[0]:.2f} | **{dl48[0]:+.2f} ± {dl48[1]:.2f}** ({se_(dl48)}) |")
    rows = []
    for e in R48:
        g = groups(e); a, c = g["claim"], g["care"]
        sp = np.mean([v.get("claimed_member", 0) + v.get("claimed_probation", 0) + v.get("claimed_down", 0) for v in a])
        ev_ = lambda V, *cls: sum(sum(val for v in V for k, val in v.items() if k.startswith("ev_") and k.endswith("_" + x) and isinstance(val, (int, float))) / len(V) for x in cls)
        bd = ev_(a, "bond", "courtfee") - ev_(c, "bond", "courtfee"); fe = ev_(a, "fee", "emission", "uplift") - ev_(c, "fee", "emission", "uplift"); wk = ev_(a, "delivery", "effort", "guarantee") - ev_(c, "delivery", "effort", "guarantee"); rec = np.mean([life(v) for v in a]) - np.mean([life(v) for v in c])
        rows.append((sp, bd, fe, wk, rec))
    rows = np.array(rows); L.append(f"\nWhere read 48's gap comes from (the conduct's slots less the careful beside them, real, by seed): the care spared {pm(mse(rows[:, 0]), 1)}, the bonds and court fees {pm(mse(rows[:, 1]), 1)}, the fees with emission and uplift {pm(mse(rows[:, 2]), 1)}, the work's side {pm(mse(rows[:, 3]), 1)}; of record {pm(mse(rows[:, 4]), 1)}.\n")
L += ["\n**Every first approval of bad work by who looked at it again, and whether it ended overturned** (the closure tally of a member's real bad deliveries; the claims and the careful errors together, then the claims alone):\n"] + WHO
for nm, E in (("38 (the record)", R38), ("**48**", R48), ("40 (the record)", R40), ("46 (detection 1, the second filing)", R46), ("**49** (detection 0.5)", R49), ("**50** (detection 0.2)", R50), ("47 (the all-careful, detection 1)", list(R47.values())), ("world 3's all-careful", CW3L), ("**55** (K = 3 and (i))", R55)):
    if E: L.append(who_row(nm, E))
for nm, Pv, base in (("Read 49 (detection 0.5) against read 40", P49v40, "read 40"), ("Read 49 against read 46 (detection 1)", P49v46, "read 46"), ("Read 50 (detection 0.2) against read 40", P50v40, "read 40"), ("Read 50 against read 46", P50v46, "read 46")):
    if Pv: L += world_tab(nm, Pv, base, WROWS)
if P49 and P50:
    L.append(f"\nAgainst world 3's all-careful by seed, the population's slot of record: read 49 {pm(mse(col(P49, 'life') - col(P49, 'lifec')), 0)} (level saving {pm(xs(P49)[0], 2)}), read 50 {pm(mse(col(P50, 'life') - col(P50, 'lifec')), 0)} ({pm(xs(P50)[0], 2)}); read 46's {pm(mse(col(P46, 'life') - col(P46, 'lifec')), 0)} ({pm(xs(P46)[0], 2)}), read 40's {pm(mse(col(P40, 'life') - col(P40, 'lifec')), 0)} ({pm(xs(P40)[0], 2)}).\n")
    for nm, E in (("49", R49), ("50", R50)):
        w_ = lambda k: np.nanmean([world(e)[k] for e in E])
        L.append(f"Read {nm}: {w_('disp'):.1f} disputes a run ({w_('dwon'):.1f} won), {w_('sf'):.1f} second filings ({w_('sfw'):.1f} won, {w_('sfl'):.1f} lost, {w_('lapsed'):.1f} lapsed, {w_('declined'):.1f} declined, {w_('unf'):.1f} unfunded), the requesters' court fees {w_('paidf'):.0f} real put down and {w_('backf'):.0f} back; the leak {w_('leak'):.1f} ‰; the reviewer's sketch d × 2.5 + (1 − d) × 92.3 gives {(0.5 if nm == '49' else 0.2) * 2.5 + (1 - (0.5 if nm == '49' else 0.2)) * 92.3:.1f}.")
# ------------------------------------------------------------------ 3. reads 51 to 56: the state's audit as no vote, the troops in the draw
L += ["\n## 3. Reads 51 to 56: the state's audit as no vote of the court (`--troop-no-vote on`), and the troops as candidates in the draw up to a minimum (`--seat-draw seats --draw-min K`; world 3's cell, seeds 21–120)\n",
      "What was said before building (notes §127a): the draw is made at the seat's first seating step — the roll's tick for the audit, the filing's for a panel seat — among the free panel-eligible members with troop candidates added up to K, one drawn over all on the seat stream; so the wait of two steps is gone for a drawn seat, and where no member is free a troop is drawn with certainty and sits at once. A dispute's panel and an appeal's are drawn alike, each seat at its own turn. Two fresh deciding seats that differ seat a third, and the majority decides, as after a member's audit differed. The record tells a drawn troop from a summoned one (`msg: drawn`; the counters by role; the state's drawn looks apart in the second-look tally). With both options off, world 3's all-careful and read 35 reproduce (the head of this file).\n"]
if P51:
    L += ["**Read 51: world 3's all-careful with (i), against world 3's all-careful by seed.**\n", "| measure | the all-careful | **read 51** | **51 − all-careful** (SE) |", "|---|---|---|---|"]
    for k, k0, lab, d_ in WROWS:
        if k not in P51[0]: continue
        dd = mse(col(P51, k) - col(P51, k0)); L.append(f"| {lab} | {np.nanmean(col(P51, k0)):.{d_}f} | {np.nanmean(col(P51, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    fr51 = np.mean([f(e, "deciding_state_audit_fresh") for e in R51.values()]); sp51 = np.mean([f(e, "deciding_splits") for e in R51.values()]); sp3 = np.mean([f(e, "deciding_splits") for e in CW3L]); dseats51 = np.mean([f(e, "deciding_seats") for e in R51.values()]); dseats3 = np.mean([f(e, "deciding_seats") for e in CW3L]); cu51 = np.mean([f(e, "state_cost_unreimbursed") for e in R51.values()]); cu3 = np.mean([f(e, "state_cost_unreimbursed") for e in CW3L])
    L.append(f"\nThe deciding verdicts opened afresh after the state's audit differed: {fr51:.1f} a run (every one of the `state_audit` reason); the deciding seats a run {dseats51:.0f} against {dseats3:.0f}, the splits {sp51:.1f} against {sp3:.1f}; the orchestrator's unreimbursed cost {cu51:.0f} against {cu3:.0f}.\n")
for nm, Pv, E, base in (("Read 52: the all-careful with the seats drawn and (ii) at K = 3, (i) off, against read 35 by seed", P52, list(R52.values()), "read 35"), ("Read 53: the same with (i), against read 35", P53, list(R53.values()), "read 35"), ("Read 53 against read 52 (what (i) adds at K = 3)", P53v52, list(R53.values()), "read 52"), ("Read 54: (i) and (ii) at K = 5, against read 35", P54, list(R54.values()), "read 35")):
    if not Pv: continue
    L += [f"\n**{nm}.**\n", f"| measure | {base} | this | **this − {base}** (SE) |", "|---|---|---|---|"]
    for k, k0, lab, d_ in WROWS:
        if k not in Pv[0]: continue
        dd = mse(col(Pv, k) - col(Pv, k0)); L.append(f"| {lab} | {np.nanmean(col(Pv, k0)):.{d_}f} | {np.nanmean(col(Pv, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    da, dp = np.mean([f(e, "troop_drawn_audit") for e in E]), np.mean([f(e, "troop_drawn_appeal") for e in E]); dpa, dpp = np.mean([f(e, "troop_drawn_plant_audit") for e in E]), np.mean([f(e, "troop_drawn_plant_appeal") for e in E]); rf = np.mean([f(e, "draw_troop_refused") for e in E]); ta = np.mean([f(e, "troop_audits") for e in E]); tp = np.mean([f(e, "troop_panel_seats") - f(e, "troop_audits") for e in E])
    L.append(f"\nTroops drawn a run: {da:.0f} at the audit seat (of the state's {ta:.0f} audit reviews; the rest the pass's after a refused draw), {dp:.0f} at the panels (of {tp:.0f}); the orchestrator's own verdict by the draw on a plant's seat {dpa:.0f} / {dpp:.0f}; draws refused for capacity or funds {rf:.1f} (the seat then waits as today). The pick asked with no member free (`pick_*_free_0`): " + ", ".join(f"{k} {np.mean([json.loads(e.get('pick_json') or '{}').get(k, 0) for e in E]):.0f}" for k in ("pick_audit_free_0", "pick_panel_free_0")) + ".\n")
if P52c:
    L.append("Against world 3's all-careful by seed (the seats drawn is itself a construction beside the record's order): the slot of record " + "; ".join(f"read {nm} {pm(mse(col(P, 'life') - col(P, 'lifec')), 0)}" for nm, P in (("35", P35), ("52", P52c), ("53", P53c), ("54", P54c)) if P) + ".\n")
L += ["\n**The pairs, as read 35 has them** (a first reviewer and the member at its audit seat; the troops' seats are no pair):\n"] + PAIR_HDR
for nm, E in (("world 3's all-careful", CW3L), ("read 35 (the seats drawn)", R35L), ("**read 52** (K = 3)", list(R52.values())), ("**read 53** (K = 3, (i))", list(R53.values())), ("**read 54** (K = 5, (i))", list(R54.values())), ("read 55", R55), ("read 56", R56)):
    row = pair_row(nm, E) if E else None
    if row: L.append(row)
if P55v40:
    L += ["\n**Read 55: cell B on every slot with the seats drawn, (i) and (ii) at K = 3, against read 40 by seed.**\n", "| measure | read 40 | **read 55** | **55 − 40** (SE) |", "|---|---|---|---|"]
    for k, k0, lab, d_ in WROWS:
        if k not in P55v40[0]: continue
        dd = mse(col(P55v40, k) - col(P55v40, k0)); L.append(f"| {lab} | {np.nanmean(col(P55v40, k0)):.{d_}f} | {np.nanmean(col(P55v40, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    d55 = fa_split(R55); d40 = fa_split(R40)
    L.append(f"\nOf the conduct's claims on real bad work at the first review ({d55['claims']:.1f} a run): stayed paid {d55['paid']:.3f} (read 40's {d40['paid']:.3f}) — never audited {d55['none']:.3f}, confirmed by a member's audit {d55['mconf']:.3f}, by the state's {d55['sconf']:.3f}; overturned after the state's audit {d55['sdiff']:.3f} (read 40's {d40['sdiff']:.3f}), after a member's {d55['mdiff']:.3f}. The claims overturned in all **{1 - d55['paid']:.3f}** where read 40 has {1 - d40['paid']:.3f}. Against world 3's all-careful by seed the population's slot {pm(mse(col(P55, 'life') - col(P55, 'lifec')), 0)}, the level saving {pm(xs(P55)[0], 2)} (read 40's {pm(xs(P40)[0], 2)}).\n")
    st55 = np.array([ra_rate(e, "state") for e in R55]); st53 = np.array([ra_rate(e, "state") for e in R53.values()]); st52 = np.array([ra_rate(e, "state") for e in R52.values()]); mb55 = np.array([ra_rate(e, "member") for e in R55]); mb53 = np.array([ra_rate(e, "member") for e in R53.values()])
    n_above = int((st55 > st53.max()).sum()); n55 = len(st55)
    L.append(f"**The state's rate of overturning, run by run, once its looks are drawn.** Read 55: {st55.mean():.4f} with a spread of {st55.std(ddof=1):.4f} over the seeds (the lowest run {st55.min():.4f}); read 53 (a careful population at the same K and (i)): {st53.mean():.4f} ± {st53.std(ddof=1):.4f} (the highest run {st53.max():.4f}); read 52's {st52.mean():.4f} ± {st52.std(ddof=1):.4f}. **{n_above} of {n55} of read 55's runs stand above read 53's highest run.** The members' rate: read 55 {mb55.mean():.4f} ± {mb55.std(ddof=1):.4f} against read 53's {mb53.mean():.4f} ± {mb53.std(ddof=1):.4f}.\n")
    RATE55 = (n_above, n55)
if Q56:
    L += ["\n**Read 56: conduct M at a dose of 0.2 on 1 slot in 4 (read 19's population) with the seats drawn, (i) and (ii) at K = 3** (read as read 19 was; against read 19 by seed).\n"] + HDR + [qrow("**56: M at 0.2 on 1 in 4, K = 3 and (i)**", Q56), qrow("19: the same in the cell of record (run again whole)", Q19)]
    L += ["\n| measure | read 19 | **read 56** | **56 − 19** (SE) |", "|---|---|---|---|"]
    for k, lab, d_ in (("rec", "careful − conduct, of record", 0), ("res", "with the reservation", 0), ("lfl", "like for like", 0), ("aud", "the conduct's audit seats", 1), ("audc", "the careful's audit seats", 1), ("panel", "the conduct's panel seats", 1), ("panelc", "the careful's panel seats", 1), ("aud_inc", "the conduct's audit-seat income (fee, emission, uplift), real", 0), ("aud_incc", "the careful's", 0), ("rvm", "the conduct's member reviews", 1), ("rvmc", "the careful's", 1), ("claims", "the conduct's claims a slot", 1), ("fover", "the conduct's wrong first approvals overturned", 2), ("fpaid", "… that stayed paid", 2), ("bonds", "the conduct's bonds forfeited (nominal)", 1), ("bondsc", "the careful's", 1),
                       ("pw", "the conduct's wrong planted verdicts as a member", 2), ("reach", "the conduct's slots suspended at least once", 3), ("reachc", "the careful's", 3), ("noseat", "the conduct's member ticks without the earned seats", 3), ("noseatc", "the careful's", 3), ("good", "the conduct's good ticks", 0), ("goodc", "the careful's", 0), ("w_leak", "the leak ‰", 1), ("w_fa", "standing FA", 1), ("w_oh", "the overhead", 2), ("ss_audit", "the state's share of the audit seats", 3), ("ss_panel", "the state's share of the panel seats", 3)):
        if k not in Q56[0] or k not in Q19[0]: continue
        dd, ma_, mb_, n_ = paired(Q19, Q56, k); L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    x19, x56 = xs(Q19)[0], xs(Q56)[0]; A_, B_ = {r["seed"]: r for r in Q19}, {r["seed"]: r for r in Q56}; sd = sorted(set(A_) & set(B_))
    dl56 = mse([(B_[s]["rec"] + B_[s]["ben"]) / B_[s]["call"] - (A_[s]["rec"] + A_[s]["ben"]) / A_[s]["call"] for s in sd]); L.append(f"| the level saving of record | {x19[0]:.2f} | {x56[0]:.2f} | **{dl56[0]:+.2f} ± {dl56[1]:.2f}** ({se_(dl56)}) |")
    dg56 = paired(Q19, Q56, "rec")[0]
# ------------------------------------------------------------------ 4. the four things and the two rates for every read
L += ["\n## 4. The four things of addendum 32 and the two rates of overturning, for every read\n", "**How often a slot is looked at** (AL4.1; the marks are off in every read here):\n",
      "| read | slot kind | slots | first approvals of real work a slot | **by a member: n (share)** | **by the state: n (share)** | by a dispute panel | never looked at | overturned: after a member's / the state's / a panel's | **marks a slot** | wrong planted verdicts as a member |", "|---|---|---|---|---|---|---|---|---|---|---|"]
for nm, E, mixed in (("all-careful", CW3L, False), ("35", R35L, False), ("48", R48, True), ("49", R49, False), ("50", R50, False), ("51", list(R51.values()), False), ("52", list(R52.values()), False), ("53", list(R53.values()), False), ("54", list(R54.values()), False), ("55", R55, False), ("56", R56, True), ("19 (run again)", R19, True)):
    L += al_rows(nm, E, mixed)
L += ["\n**The three counts in one row, and the mirror by road** (AL4.2, AL4.3):\n"] + THREE_HDR
for nm, E in (("all-careful", CW3L), ("35", R35L), ("38", R38), ("48", R48), ("40", R40), ("46", R46), ("49", R49), ("50", R50), ("51", list(R51.values())), ("52", list(R52.values())), ("53", list(R53.values())), ("54", list(R54.values())), ("55", R55), ("19 (run again)", R19), ("56", R56)):
    if E: L.append(three_row(nm, E))
L += ["\n**The overhead's five terms** (AL4.4):\n"] + OH_HDR
for nm, E in (("all-careful", CW3L), ("35", R35L), ("38", R38), ("48", R48), ("40", R40), ("46", R46), ("49", R49), ("50", R50), ("51", list(R51.values())), ("52", list(R52.values())), ("53", list(R53.values())), ("54", list(R54.values())), ("55", R55), ("19 (run again)", R19), ("56", R56)):
    row = oh_row(nm, E) if E else None
    if row: L.append(row)
L += ["\n**The two rates of overturning** (every first approval of a member's real delivery by who looked again; the state's drawn looks apart where the draw is on):\n"] + RA_HDR
for nm, E in (("world 3's all-careful", CW3L), ("read 35", R35L), ("read 38", R38), ("read 48", R48), ("read 40", R40), ("read 46", R46), ("read 49", R49), ("read 50", R50), ("read 51", list(R51.values())), ("read 52", list(R52.values())), ("read 53", list(R53.values())), ("read 54", list(R54.values())), ("read 55", R55), ("read 19 (run again)", R19), ("read 56", R56)):
    row = ra_row(nm, E) if E else None
    if row: L.append(row)
# ------------------------------------------------------------------ 5. the expectations and the conditions
L += ["\n## 5. Against the expectations stated before the run, and the conditions\n"]
VER = []
if Q48:
    a = mse(col(Q48, "rec")); x = xs(Q48)[0]; d = fa_split(R48); lk = np.mean(col(Q48, "w_leak"))
    chk(in_band(-a[0], -20, 95), f"read 48: the conduct's slot between 20 behind and 95 ahead of the careful beside it, of record — {-a[0]:+.0f} ± {a[1]:.0f} (ahead positive)"); chk(in_band(x[0], -0.25, 0.30), f"read 48: level saving −0.25 to 0.30 — {x[0]:.2f} ± {x[1]:.2f}")
    chk(in_band(1 - d["paid"], 0.97, 0.99), f"read 48: of the conduct's claims on real bad work at the first review 0.97 to 0.99 end overturned (read 38's 0.75) — {1 - d['paid']:.3f}"); chk(in_band(lk, 0.5, 2.0), f"read 48: leak 0.5 to 2.0 ‰ — {lk:.2f}")
    VER.append(verdict("A buyer's complaint that can reach the court holds one member that the planted cases do not see, among careful ones (read 48's level saving above 0.9 by two SE: shown; under 0.9 at the point value: refuted)", x[0] - 2 * x[1] > 0.9, x[0] < 0.9))
if P49v40 and P50v40:
    lk49, lk50 = np.mean(col(P49v40, "w_leak")), np.mean(col(P50v40, "w_leak")); sf49, sf50 = np.mean(col(P49v40, "w_sf")), np.mean(col(P50v40, "w_sf")); doh49, doh50 = mse(col(P49v40, "w_oh") - col(P49v40, "w0_oh")), mse(col(P50v40, "w_oh") - col(P50v40, "w0_oh"))
    chk(in_band(lk49, 42, 52), f"read 49: leak 42 to 52 ‰ — {lk49:.1f}"); chk(in_band(sf49, 15, 21), f"read 49: 15 to 21 second filings a run — {sf49:.1f}"); chk(in_band(doh49[0], 0.20, 0.36), f"read 49: the overhead 0.20 to 0.36 above read 40's — {doh49[0]:+.2f} ± {doh49[1]:.2f}")
    chk(in_band(lk50, 69, 79), f"read 50: leak 69 to 79 ‰ — {lk50:.1f}"); chk(in_band(sf50, 5, 9), f"read 50: 5 to 9 second filings a run — {sf50:.1f}"); chk(in_band(doh50[0], 0.05, 0.18), f"read 50: the overhead 0.05 to 0.18 above read 40's — {doh50[0]:+.2f} ± {doh50[1]:.2f}")
    VER.append(verdict("What the complaint finds goes with how often buyers notice, and with nothing else (refuted if read 49's leak is outside 42 to 52 or read 50's outside 69 to 79; shown where both are inside)", in_band(lk49, 42, 52) and in_band(lk50, 69, 79), not (in_band(lk49, 42, 52) and in_band(lk50, 69, 79))))
if P51:
    m51, ms51 = np.mean(col(P51, "t_mirror")), np.mean(col(P51, "t_mirror_state")); dlk = mse(col(P51, "w_leak") - col(P51, "w0_leak")); dl = mse(col(P51, "life") - col(P51, "lifec")); dms = mse(col(P51, "t_mirror_state") - col(P51, "t0_mirror_state")); ms3 = np.mean(col(P51, "t0_mirror_state"))
    chk(in_band(m51, 2.0, 2.8), f"read 51: 2.0 to 2.8 wrong rejections stand a run (5.17) — {m51:.2f}"); chk(in_band(ms51, 0.1, 0.5), f"read 51: 0.1 to 0.5 after the state's audit (3.09) — {ms51:.2f}"); chk(dlk[0] <= 1.5, f"read 51: the leak rises by up to 1.5 ‰ — {dlk[0]:+.2f} ± {dlk[1]:.2f}"); chk(not two_se(dl), f"read 51: the slot of record within two SE of the all-careful's — {dl[0]:+.0f} ± {dl[1]:.0f}")
    VER.append(verdict("Taking the state's differing audit out of the court's seats takes away most of the wrong rejections that reach a worker with no appeal (shown if read 51's wrong rejections after the state's audit are under a third of the all-careful's by two SE, by seed; refuted if at or over a half at the point value)", dms[0] + 2 * dms[1] < -(2.0 / 3.0) * ms3, ms51 >= 0.5 * ms3))
if P52:
    ss52, aud52 = np.mean(col(P52, "ss_audit")), np.mean(col(P52, "aud")); dl52 = mse(col(P52, "life") - col(P52, "lifec")); m52 = np.mean(col(P52, "t_mirror"))
    chk(in_band(ss52, 0.45, 0.58), f"read 52: the state on 0.45 to 0.58 of the audit seats (0.317) — {ss52:.3f}"); chk(in_band(aud52, 22, 29), f"read 52: a member holds 22 to 29 audit seats (35.8) — {aud52:.1f}"); chk(in_band(-dl52[0], 10, 60), f"read 52: the slot 10 to 60 real under read 35's — {-dl52[0]:+.0f} ± {dl52[1]:.0f} under"); chk(in_band(m52, 6.2, 7.6), f"read 52: 6.2 to 7.6 wrong rejections stand a run — {m52:.2f}")
    VER.append(verdict("A minimum of three puts the state on about half of the second looks (refuted if read 52's share of the audit seats is outside 0.45 to 0.58)", in_band(ss52, 0.45, 0.58), not in_band(ss52, 0.45, 0.58)))
if P53 and P53v52:
    dss, daud = mse(col(P53v52, "ss_audit") - col(P53v52, "ss0_audit")), mse(col(P53v52, "aud") - col(P53v52, "audc")); m53 = np.mean(col(P53, "t_mirror")); dl53 = mse(col(P53, "life") - col(P53, "lifec"))
    chk(not two_se(dss) and not two_se(daud), f"read 53: the state's share and a member's audit seats as read 52's within two SE by seed — {dss[0]:+.3f} ± {dss[1]:.3f}; {daud[0]:+.1f} ± {daud[1]:.1f}"); chk(in_band(m53, 2.0, 3.2), f"read 53: 2.0 to 3.2 wrong rejections stand a run — {m53:.2f}"); chk(in_band(-dl53[0], 10, 60), f"read 53: the slot 10 to 60 real under read 35's — {-dl53[0]:+.0f} ± {dl53[1]:.0f} under")
if P54:
    ss54, aud54 = np.mean(col(P54, "ss_audit")), np.mean(col(P54, "aud")); dl54 = mse(col(P54, "life") - col(P54, "lifec"))
    chk(in_band(ss54, 0.56, 0.72), f"read 54: the state on 0.56 to 0.72 of the audit seats — {ss54:.3f}"); chk(in_band(aud54, 15, 23), f"read 54: a member holds 15 to 23 audit seats — {aud54:.1f}"); chk(in_band(-dl54[0], 30, 100), f"read 54: the slot 30 to 100 real under read 35's — {-dl54[0]:+.0f} ± {dl54[1]:.0f} under")
if P55v40:
    lk55 = np.mean(col(P55v40, "w_leak")); d55 = fa_split(R55); st = np.mean([ra_rate(e, "state") for e in R55])
    chk(in_band(lk55, 70, 85), f"read 55: leak 70 to 85 ‰ (92.3) — {lk55:.1f}"); chk(in_band(1 - d55["paid"], 0.36, 0.47), f"read 55: of the conduct's claims 0.36 to 0.47 end overturned (0.30) — {1 - d55['paid']:.3f}"); chk(in_band(st, 0.035, 0.045), f"read 55: of the first approvals the state looks at again 0.035 to 0.045 end overturned — {st:.4f}")
    VER.append(verdict(f"Once its looks are drawn, the state's rate of overturning tells a shared miss from a careful population within one run (shown if read 55's rate, run by run, is above the highest run of read 53 in at least 95 runs of 100; refuted if in fewer than 75) — {RATE55[0]} of {RATE55[1]}", RATE55[0] >= 95, RATE55[0] < 75))
if Q56:
    a = mse(col(Q56, "rec")); x = xs(Q56)[0]
    chk(in_band(a[0], 120, 195), f"read 56: the conduct's slot 120 to 195 real behind the careful beside it (read 19's 200 ± 18) — {a[0]:+.0f} ± {a[1]:.0f}"); chk(in_band(x[0], 0.85, 1.15), f"read 56: level saving 0.85 to 1.15 (1.23) — {x[0]:.2f} ± {x[1]:.2f}")
    VER.append(verdict(f"A minimum takes from what a member has to lose (shown if read 56's gap is under read 19's by two SE, by seed; refuted if at or over it at the point value) — read 56 less read 19 {dg56[0]:+.0f} ± {dg56[1]:.0f}", dg56[0] + 2 * dg56[1] < 0, dg56[0] >= 0))
L += CHK; n_met = sum(1 for c in CHK if c.startswith("- MET")); L.append(f"\n**{n_met} of {len(CHK)} expectations met.** (Reads 53 and 54 set no condition: they are the prices.)\n")
L += ["\n### The conditions\n"] + VER
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L[:10])); print(f"... written {sys.argv[1]} ({len(L)} lines)")
