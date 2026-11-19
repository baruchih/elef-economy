"""Addendum 34 (November 19, 2026; notes §128): the readings asked from the record (point 6), the reviewer's arithmetic (point 5) confirmed or replaced, and eight reads without
training at 867998dfc — reads 57 to 64 (three options off by default: `--draw-wait on`, the wait kept under a minimum; `--standby-pay on`, the drawn seat's fee to the members that
stood; `--checker-rate 0.2`, the state's look on a sample of approved real work), each with (i) on, the four things of addendum 32 and the two rates of overturning for every read.
World 3's all-careful and read 35 run again whole at this commit and checked to the key against a28/rerun first. a28_read.py's helpers copied. Usage: a29_read.py OUT.md"""
import json, os, sys, hashlib, math, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D29, D28, D27, D26, D25, D22, D19 = f"{R}/a29", f"{R}/a28", f"{R}/a27", f"{R}/a26", f"{R}/a25", f"{R}/a22", f"{R}/a19"
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
def repro(new_eps, old_eps, label, skip_json_prefix=("dpanel", "statedrawn", "troop_drawn", "_free_0", "troopdrawn", "chk_", "seatstood", "_later")):
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
            a = {kk: vv for kk, vv in json.loads(o[k] or "{}").items() if not any(p in kk for p in skip_json_prefix)}; b = {kk: vv for kk, vv in json.loads(e.get(k) or "{}").items() if not any(p in kk for p in skip_json_prefix)}   # both sides filtered alike (a28 compared a record that lacked the sub-keys)
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
WK = WK + (("chk_looks", "chk_looks_after", "checkers' looks after an audit had confirmed", 1), ("chk_looks_no", "chk_looks_no", "checkers' looks with no audit", 1), ("chk_over_a", "chk_over_after", "checkers' overturns after an audit", 2), ("chk_over_n", "chk_over_no", "checkers' overturns with no audit", 2),
            ("chk_cost", "chk_cost", "the checkers' cost (nominal credits)", 0), ("chk_skip", "chk_skipped_court", "approvals the court had confirmed, not sampled", 1), ("chk_ref", "chk_refused", "looks refused for capacity or funds", 2),
            ("sb_tot", "standby_pay_total", "pay for standing by, nominal", 0), ("sb_seats", "standby_pay_seats", "seats whose fee went to members that stood", 1), ("sb_names", "standby_names", "members that stood at drawn seats, summed", 1), ("sb_dep", "standby_unpaid_departed", "shares of departed names, Ω's", 1),
            ("omfee", "omega_review_fee_income", "Ω's income from the troops' review fees", 0), ("drawn_a", "troop_drawn_audit", "troops drawn at the audit seat", 1), ("drawn_p", "troop_drawn_appeal", "troops drawn at the panels", 1), ("drawn_aw", "seated_audit_troop_drawn_wait", "of them at a later step (the wait)", 1),
            ("ta", "troop_audits", "the state's audit reviews a run", 1), ("ma", "seated_audit_member", "members' audit seats a run", 1), ("dfresh", "deciding_state_audit_fresh", "deciding verdicts afresh after the state's audit", 1))
# ------------------------------------------------------------------ the record and the reads
CW3o = load([f"{D28}/rerun/cw3-s21-70", f"{D28}/rerun/cw3-s71-120"], "careful")[1]; CW3 = load([f"{D29}/rerun/cw3-s21-70", f"{D29}/rerun/cw3-s71-120"], "careful")[1] or CW3o
R35o = load([f"{D28}/rerun/r35-s21-70", f"{D28}/rerun/r35-s71-120"], "careful")[1]; R35 = load([f"{D29}/rerun/r35-s21-70", f"{D29}/rerun/r35-s71-120"], "careful")[1] or R35o
R19 = load([f"{D28}/rerun/r19-s21-70", f"{D28}/rerun/r19-s71-120"], "mix:doseM0.2:0.25")[0]; R40 = load([f"{D27}/rerun/r40-s21-70", f"{D27}/rerun/r40-s71-120"], "mix:caseM0.2p0:1.0")[0]
R38 = load([f"{D27}/rerun/r38-s21-70", f"{D27}/rerun/r38-s71-120"], "mix:caseM0.2p0:0.25")[0]; R44 = load([f"{D27}/r44/s21-70", f"{D27}/r44/s71-120"], "mix:caseM0.2p0:0.25")[0]
R51 = load([f"{D28}/r51/s21-70", f"{D28}/r51/s71-120"], "careful")[1]; R52 = load([f"{D28}/r52/s21-70", f"{D28}/r52/s71-120"], "careful")[1]; R53 = load([f"{D28}/r53/s21-70", f"{D28}/r53/s71-120"], "careful")[1]
R55 = load([f"{D28}/r55/s21-70", f"{D28}/r55/s71-120"], "mix:caseM0.2p0:1.0")[0]; R56 = load([f"{D28}/r56/s21-70", f"{D28}/r56/s71-120"], "mix:doseM0.2:0.25")[0]
R57 = load([f"{D29}/r57/s21-70", f"{D29}/r57/s71-120"], "careful")[1]; R58 = load([f"{D29}/r58/s21-70", f"{D29}/r58/s71-120"], "careful")[1]
R59 = load([f"{D29}/r59/s21-70", f"{D29}/r59/s71-120"], "mix:doseM0.2:0.25")[0]; R60 = load([f"{D29}/r60/s21-70", f"{D29}/r60/s71-120"], "mix:doseM0.2:0.25")[0]
R61 = load([f"{D29}/r61/s21-70", f"{D29}/r61/s71-120"], "mix:caseM0.2p0:1.0")[0]; R62 = load([f"{D29}/r62/s21-70", f"{D29}/r62/s71-120"], "mix:caseM0.2p0:1.0")[0]
R63 = load([f"{D29}/r63/s21-70", f"{D29}/r63/s71-120"], "careful")[1]; R64 = load([f"{D29}/r64/s21-70", f"{D29}/r64/s71-120"], "mix:caseM0.2p0:1.0")[0]
CW3L, R35L = list(CW3.values()), list(R35.values()); LV = lambda Dd: list(Dd.values())
L = ["# Addendum 34 — the wait kept under a minimum, pay for standing by, and checkers: reads 57 to 64 (November 19, 2026; notes §128)\n"]
if CW3 is not CW3o and CW3o: L.append(repro(CW3L, list(CW3o.values()), "world 3's all-careful run again whole at 867998dfc (a28/rerun/cw3 at dc5b49896)"))
if R35 is not R35o and R35o: L.append(repro(R35L, list(R35o.values()), "read 35 (the seats drawn) run again whole at 867998dfc (a28/rerun/r35 at dc5b49896)"))
L.append(f"\nLoaded: cw3 {len(CW3)} (record {len(CW3o)}), r35 {len(R35)} (record {len(R35o)}), r19 {len(R19)}, r40 {len(R40)}, r38 {len(R38)}, r44 {len(R44)}, r51 {len(R51)}, r52 {len(R52)}, r53 {len(R53)}, r55 {len(R55)}, r56 {len(R56)}; "
         f"r57 {len(R57)}, r58 {len(R58)}, r59 {len(R59)}, r60 {len(R60)}, r61 {len(R61)}, r62 {len(R62)}, r63 {len(R63)}, r64 {len(R64)} episodes.\n")
def ra_rate(e, who): r = raj(e); return (r.get(f"{who}_over", 0) / r[f"{who}_n"]) if r.get(f"{who}_n") else np.nan
rng = np.random.default_rng(128)
def sub_rate(e, who, share, reps=200):
    """The rate of overturning on a random share of the looks: a hypergeometric draw of the overturned among the looks taken (the reader's draw, the record's counts)."""
    r = raj(e); n, k = int(r.get(f"{who}_n", 0)), int(r.get(f"{who}_over", 0)); m = int(round(share * n))
    if n == 0 or m == 0: return np.full(reps, np.nan)
    return rng.hypergeometric(k, n - k, m, size=reps) / m
def above_runs(E_test, E_ref, who, share=1.0, reps=200):
    """The runs of E_test whose rate stands above E_ref's highest run, on the same share of the looks (a draw for each replicate, both sides)."""
    if share >= 1.0:
        t = np.array([ra_rate(e, who) for e in E_test]); r_ = np.array([ra_rate(e, who) for e in E_ref]); return int((t > np.nanmax(r_)).sum()), len(t), np.nan
    T_ = np.array([sub_rate(e, who, share, reps) for e in E_test]); Rr = np.array([sub_rate(e, who, share, reps) for e in E_ref])
    cnt = [(T_[:, j] > np.nanmax(Rr[:, j])).sum() for j in range(reps)]; return float(np.mean(cnt)), T_.shape[0], float(np.std(cnt))
def chk_rate(e, by):
    n = f(e, f"chk_looks_{by}") if by != "all" else f(e, "chk_looks_after") + f(e, "chk_looks_no"); o = f(e, f"chk_over_{by}") if by != "all" else f(e, "chk_over_after") + f(e, "chk_over_no")
    return (o / n) if n else np.nan
def chk_sub(e, by, share, reps=200):
    n = f(e, f"chk_looks_{by}") if by != "all" else f(e, "chk_looks_after") + f(e, "chk_looks_no"); o = f(e, f"chk_over_{by}") if by != "all" else f(e, "chk_over_after") + f(e, "chk_over_no"); n, o = int(n), int(o); m = int(round(share * n))
    if n == 0 or m == 0: return np.full(reps, np.nan)
    return rng.hypergeometric(o, n - o, m, size=reps) / m
def chk_above(E_test, E_ref, by, share=1.0, reps=200):
    if share >= 1.0:
        t = np.array([chk_rate(e, by) for e in E_test]); r_ = np.array([chk_rate(e, by) for e in E_ref]); return int((t > np.nanmax(r_)).sum()), int((~np.isnan(t)).sum()), np.nan
    T_ = np.array([chk_sub(e, by, share, reps) for e in E_test]); Rr = np.array([chk_sub(e, by, share, reps) for e in E_ref])
    cnt = [(T_[:, j] > np.nanmax(Rr[:, j])).sum() for j in range(reps)]; return float(np.mean(cnt)), T_.shape[0], float(np.std(cnt))
# ------------------------------------------------------------------ the gap by term (6.4) and the pay by kind of slot
INC = ("fee", "emission", "uplift")
def _rf(v, seats): return sum(val for k, val in v.items() if k.startswith("rf_") and any(f"_{s}_" in k for s in seats) and k.split("_")[-1] in INC)
def _ev(v, classes): return sum(val for k, val in v.items() if k.startswith("ev_") and any(k.endswith("_" + c) for c in classes) and isinstance(val, (int, float)))
EV_NAMED = ("fee", "emission", "uplift", "bond", "courtfee", "care", "reimb", "standby", "delivery", "effort", "guarantee", "guarantee_in")
TERMS = (("audit", "the audit seats' income (fee, emission, uplift)", lambda v: _rf(v, ("audit",))),
         ("panel", "the panel seats' income (appeal, third, dispute)", lambda v: _rf(v, ("appeal", "third", "dispute"))),
         ("first", "the first reviews' income (the resumed seat with it)", lambda v: _rf(v, ("initial", "resumed"))),
         ("feeres", "review income on no seat of the slot's record (a residue)", lambda v: _ev(v, INC) - _rf(v, ("audit", "appeal", "third", "dispute", "initial", "resumed"))),
         ("bond", "bonds and court fees", lambda v: _ev(v, ("bond", "courtfee"))),
         ("care", "the care spent and reimbursed, net", lambda v: _ev(v, ("care", "reimb"))),
         ("ben", "the care spared (the private benefit)", lambda v: v.get("private_real", 0.0)),
         ("standby", "**pay for standing by**", lambda v: _ev(v, ("standby",))),
         ("work", "the work side (price, effort, guarantees)", lambda v: _ev(v, ("delivery", "effort", "guarantee", "guarantee_in"))),
         ("other", "every other wallet event (the float, the loan, a departure)", lambda v: sum(val for k, val in v.items() if k.startswith("ev_") and not any(k.endswith("_" + c) for c in EV_NAMED) and isinstance(val, (int, float)))),
         ("resid", "the residual (the starting wallet, the index's revaluation of what was held)", lambda v: life(v) - sum(val for k, val in v.items() if k.startswith("ev_") and isinstance(val, (int, float))) - v.get("private_real", 0.0)),
         ("life", "**the slot of record (the sum of the terms)**", life))
def gap_terms(E):
    """read 38's shape: the careful beside less the conduct, by seed and term."""
    out = {}
    for e in E:
        g = groups(e)
        if not g["claim"] or not g["care"]: continue
        out[int(e["seed"])] = {nm: np.mean([fn(v) for v in g["care"]]) - np.mean([fn(v) for v in g["claim"]]) for nm, _, fn in TERMS}
    return out
def terms_tab(title, pairs):
    """pairs: a list of (label, gaps_dict) — the first the base; the columns the gap by term and the difference from the base by seed."""
    base_lab, base = pairs[0]; rows = ["\n" + title + "\n", "| term | " + " | ".join(lab for lab, _ in pairs) + " | " + " | ".join(f"**{lab} − {base_lab}** (SE)" for lab, _ in pairs[1:]) + " |", "|---|" + "---|" * (2 * len(pairs) - 1)]
    for nm, lab, _ in TERMS:
        cells = [f"{np.mean([g[nm] for g in G.values()]):+.1f}" for _, G in pairs]
        dd = []
        for _, G in pairs[1:]:
            sd = sorted(set(G) & set(base)); d_ = mse([G[s][nm] - base[s][nm] for s in sd]); dd.append(f"**{d_[0]:+.1f} ± {d_[1]:.1f}**")
        rows.append(f"| {lab} | " + " | ".join(cells) + " | " + " | ".join(dd) + " |")
    return rows
def standby_by_kind(E, mixed):
    """The pay for standing by a slot, real, by kind of slot (the founders — in place from tick 0 — and the arrivals; the conduct and the careful beside where mixed)."""
    out = {}
    def sb(V): return np.mean([sum(val for k, val in v.items() if k.startswith("ev_") and k.endswith("_standby")) for v in V]) if V else np.nan
    for e in E:
        V = slots(e); g = groups(e) if mixed else None
        d = {"every slot": sb(V), "founders": sb([v for v in V if v["t_in"] == 0]), "arrivals": sb([v for v in V if v["t_in"] > 0]), "paid slots": np.mean([1 if sum(val for k, val in v.items() if k.startswith("ev_") and k.endswith("_standby")) > 0 else 0 for v in V])}
        if mixed: d.update({"the conduct": sb(g["claim"]), "the careful beside": sb(g["care"])})
        out[int(e["seed"])] = d
    return out
# ------------------------------------------------------------------ 1. asked from the record (point 6) and the arithmetic (point 5)
L += ["## 1. Asked from the record (point 6), and the reviewer's arithmetic (point 5)\n"]
V3 = [v for e in CW3L for v in slots(e)]; nrun = len(CW3L)
fee_a = sum(v.get("rf_member_audit_fee", 0) for v in V3); n_a = sum(v.get("rvs_member_audit", 0) for v in V3); em_a = sum(v.get("rf_member_audit_emission", 0) for v in V3); up_a = sum(v.get("rf_member_audit_uplift", 0) for v in V3); care_a = sum(v.get("care_member_audit", 0) for v in V3)
fee_i = sum(v.get("rf_member_initial_fee", 0) for v in V3); n_i = sum(v.get("rvs_member_initial", 0) for v in V3); fee_p = sum(v.get("rf_member_appeal_fee", 0) for v in V3); n_p = sum(v.get("rvs_member_appeal", 0) for v in V3)
tc3 = np.mean([f(e, "troop_review_cost") for e in CW3L]) / np.mean([f(e, "troop_reviews") for e in CW3L])
L.append(f"**6.1 — the audit seat's fee in real terms.** The fee is 1.5 f = **3.0 nominal at the index of the case's posting** (the fee pot φ^F is locked at the posting and every nominal of the case is frozen there, 2.0.0 §2.1), paid from the pot at the case's settlement. In the units of a member's 4.46 real beyond its care — the driver's real, every credit at P_0 / P_t of its own tick — "
         f"a member's audit seat in world 3's all-careful earned **{fee_a / n_a:.3f} real of fixed fee** ({n_a / nrun:.0f} member audit seats a run), {em_a / n_a:.3f} of emission share and {up_a / n_a:.3f} of uplift, {(fee_a + em_a + up_a) / n_a:.3f} beyond a care of {care_a / n_a:.3f} (§118's 4.46 over 2.82); the first review's fee {fee_i / n_i:.3f} real, a panel seat's {fee_p / n_p:.3f}. "
         f"So the reviewer's 3.3 real a seat is **2.83 real**, and the figures that take 3.3 are to be read at 0.86 of their size. Neither of 127d's two conversions is misread; they are two indices at two moments: a troop's cost c_T = 3.0 is purchased at the *published* index of the period before (`ledger.index()`, the mean price of the last closed period over P_0 — under 1 for most of the run), "
         f"{tc3:.2f} nominal credits a troop review on average, which is 3.0 real at that index; a member's care of 2 or 3 nominal (2.5 on average) is read real at the *live* P_t of its tick, 2.85 real on average (P_t about 17.5 over the run's reviews, 14.8 at its end). The fee is the third figure: 3.0 nominal frozen at the posting, 2.83 real when paid.\n")
# 6.2 the four rows of AL4.1
L += ["**6.2 — the four rows of table AL4.1 (6.9 of addendum 33), in the notes from here** (a slot's first approvals of real work in a life, by who looked at them again; the overturns after each; the marks a slot; the wrong planted verdicts as a member; a27/rerun/r38 and a27/r44 at 29cffb7c7):\n",
      "| read | slot kind | slots a seed | first approvals of real work a slot | **by a member: n (share)** | **by the state: n (share)** | by a dispute panel | never looked at | overturned: after a member's / the state's / a panel's | **marks a slot** | wrong planted verdicts as a member |", "|---|---|---|---|---|---|---|---|---|---|---|"]
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
L += al_rows("38 (cell B on 1 in 4)", R38, True) + al_rows("44 (the same with the mark)", R44, True)
# 6.4 read 56's gap by term
G19, G56 = gap_terms(R19), gap_terms(R56)
if G19 and G56:
    L += terms_tab("**6.4 — read 56's gap by term, beside read 19's** (the careful beside less the conduct, real a slot, by seed; every flow of the slot's wallet by class at the index of its tick, the private benefit beside, and the residual the events do not carry — the starting wallet and the index's revaluation of what was held):", [("read 19", G19), ("read 56", G56)])
    sd = sorted(set(G19) & set(G56)); d_a = mse([G56[s]["audit"] - G19[s]["audit"] for s in sd]); d_p = mse([G56[s]["panel"] - G19[s]["panel"] for s in sd]); d_l = mse([G56[s]["life"] - G19[s]["life"] for s in sd])
    L.append(f"\nOf the {-d_l[0]:.0f} ± {d_l[1]:.0f} real by which the gap fell, **{-d_a[0]:.0f} ± {d_a[1]:.0f} is the audit seats' income** (the careful beside lost more of it than the conduct, which held few) and {-d_p[0]:.0f} ± {d_p[1]:.0f} the panels'; the terms are read in the table with their errors. The planted record enters through the seats: it is what takes them, and under a minimum the state holds most of what it would take.\n")
# 6.5 planted cases at a member's seat
L += ["**6.5 — planted cases at a member's seat under a minimum** (a run; `plant_adj_<seat>` the plants adjudicated at a member's seat of the kind, `bad_met_<seat>` the bad among them on the harness's slots, the good the difference; the orchestrator's own verdict by the draw apart):\n",
      "| read | at a member's audit seat: bad / good | at a member's appeal panel seat: bad / good | at a member's third seat: bad / good | taken by the orchestrator's verdict by the draw: audit / panel | planted approvals posted |", "|---|---|---|---|---|---|"]
for nm, E in (("world 3's all-careful", CW3L), ("35 (the seats drawn)", R35L), ("53 (K = 3, (i))", LV(R53)), ("56 (conduct M on 1 in 4, K = 3, (i))", R56), ("57 (K = 3, (i), the wait kept)", LV(R57)), ("58 (K = 3, (i), the wait, the pay)", LV(R58))):
    if not E: continue
    m = lambda k: np.mean([f(e, k) for e in E])
    L.append(f"| {nm} | {m('bad_met_audit'):.1f} / {m('plant_adj_audit') - m('bad_met_audit'):.1f} | {m('bad_met_appeal'):.1f} / {m('plant_adj_appeal') - m('bad_met_appeal'):.1f} | {m('bad_met_third'):.1f} / {m('plant_adj_third') - m('bad_met_third'):.1f} | {m('troop_drawn_plant_audit'):.1f} / {m('troop_drawn_plant_appeal'):.1f} | {m('pa_posted'):.1f} |")
L.append("\nTo draw a planted case's seat among the members alone, as it is drawn with the option off: one condition in the harness's call — `pick_seat(..., troops=_draw and not task.plant)` — the driver knowing its own plants by its record (outside the convention, as `caseM<q>p<qP>` declares); the engine needs nothing, and the pass would still take a plant's seat past w_R by the orchestrator's verdict as today. Not built.\n")
# 6.7 read 55's measure on a random half and fifth of the looks
if R55 and R53:
    n_full = above_runs(R55, LV(R53), "statedrawn"); n_half = above_runs(R55, LV(R53), "statedrawn", 0.5); n_fifth = above_runs(R55, LV(R53), "statedrawn", 0.2)
    lk = np.mean([raj(e).get("statedrawn_n", 0) for e in R55])
    L.append(f"**6.7 — read 55's measure by the number of looks.** On every drawn look ({lk:.0f} a run) read 55's state rate stands above read 53's highest run in **{n_full[0]} of {n_full[1]}** runs; on a random half of each run's drawn looks (the reader's hypergeometric draw of the overturned among the looks taken, 200 draws, both reads on the same share, read 53's highest taken on its own halves) **{n_half[0]:.0f} ± {n_half[2]:.0f} of {n_half[1]}**; on a random fifth **{n_fifth[0]:.0f} ± {n_fifth[2]:.0f} of {n_fifth[1]}**.\n")
# 5.1 the audit odds
g3 = g_of([raj(e) for e in CW3L]); tot3 = g3("member_n") + g3("state_n") + g3("panel_n") + g3("never_n")
fo = [v for v in V3 if v["t_in"] == 0]; ar = [v for v in V3 if v["t_in"] > 0]
nv_ = lambda V: (sum(v.get("ra_never", 0) for v in V) / sum(v.get("ra_first", 0) for v in V)) if sum(v.get("ra_first", 0) for v in V) else np.nan
L.append(f"**5.1 — the audit odds.** Of every first approval of a member's real delivery in world 3's all-careful ({tot3:.0f} a run), **{g3('never_n') / tot3:.3f} are never looked at again** — {1 - g3('never_n') / tot3:.3f} get a look (a member's audit {g3('member_n') / tot3:.3f}, the state's {g3('state_n') / tot3:.3f}); the 0.07–0.085 the reviewer read were of the *wrong* first approvals in other cells. By the rule the roll is at the first reviewer's applied odds: 1 on probation (pinned) and p_eff ≥ 0.5 m_t as a member (the roll's floor of record), halving after every twenty reviews that stood. "
         f"The record carries the never-looked share by the slot, not by the standing at the approval: the founders' first approvals (members from tick 0) {nv_(fo):.3f} never looked at, the arrivals' (on probation at odds 1 for their first 488 ticks, then members) {nv_(ar):.3f}. A split by the standing at the roll would need a reading added at the roll; not run.\n")
# 5.2 the audit seats of a run
def audit_seats(E): return np.mean([f(e, "seated_audit_member") + f(e, "troop_audits") for e in E]), np.mean([f(e, "seated_audit_member") for e in E]), np.mean([f(e, "troop_audits") for e in E]), np.mean([f(e, "troop_drawn_plant_audit") for e in E])
a35, a52, a53 = audit_seats(R35L), audit_seats(LV(R52)), audit_seats(LV(R53))
L.append(f"**5.2 — the audit seats of a run: one base.** Every audit seat seated with a review, a member's or the state's, planted cases included: read 35 **{a35[0]:.0f}** ({a35[1]:.0f} members', {a35[2]:.0f} the state's: {a35[2] / a35[0]:.3f}), read 52 **{a52[0]:.0f}** ({a52[1]:.0f}; {a52[2]:.0f}: {a52[2] / a52[0]:.3f}), read 53 {a53[0]:.0f}. The reviewer's 1,242 / 0.618 = 2,010 is read 52's count; his 1,918 for read 35 is not a count of the record's — read 35 has {a35[0]:.0f}. "
         f"The {a35[0] - a52[0]:.0f} fewer seats under the draw are the planted cases' audit seats the orchestrator's own verdict took by the draw with no review ({a52[3]:.0f} a run) and the rest the run's own variation in the audits rolled.\n")
# 5.3 arithmetic
slope = (1.23 - 0.02) / 0.2
L.append(f"**5.3 — what a cheaper model spares, by the loop's prices.** Confirmed as arithmetic on the record's two points: the middle model spares 1 − 0.13/0.33 = {1 - 0.13 / 0.33:.2f} of the strongest's price and the cheapest 1 − 0.014/0.33 = {1 - 0.014 / 0.33:.3f}; on the line through read 38 (0.02 at none of the planted bad cases failed) and read 19 (1.23 at a dose of 0.2 on every case), the level saving is 0.02 + {slope:.2f} q, so the middle model is held once it fails q = {(0.606 - 0.02) / slope:.3f} of the planted bad cases, "
         f"{(0.606 - 0.02) / slope + 0.05 * (1 - (0.606 - 0.02) / slope):.3f} in all with the careful's own error; a model at a tenth {(0.9 - 0.02) / slope + 0.05 * (1 - (0.9 - 0.02) / slope):.3f}; the cheapest {(0.958 - 0.02) / slope + 0.05 * (1 - (0.958 - 0.02) / slope):.3f} — the reviewer's 0.142, 0.188 and 0.197. The line is two points and the points between them are not read.\n")
L.append("**5.4 to 5.10** are sketches for reads 57 to 64 and are confirmed or replaced by the reads in §2 and §3 below (5.4 by read 57; 5.5 is the variant of 127i, not ordered, left as arithmetic; 5.6 by reads 58 to 60; 5.7 by read 61; 5.8 by read 62; 5.9 and 5.10 by reads 63 and 64).\n")
# ------------------------------------------------------------------ shared tables (a28's)
HDR = ["| read | seeds | slots a seed: conduct / careful beside | **careful − conduct, of record** (SE) | temptation | with the reservation | like for like | **level saving: of record / with the reservation / like for like** | care a slot: conduct / careful | claims a slot | suspended at least once: conduct / careful | departed | member reviews: conduct / careful | **audit seats: conduct / careful** | panel seats: conduct / careful | pay for standing by: conduct / careful |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def sb_of(V): return np.mean([sum(val for k, val in v.items() if k.startswith("ev_") and k.endswith("_standby")) for v in V]) if V else np.nan
def qrow(nm, Q, E=None):
    a, b, c = mse(col(Q, "rec")), mse(col(Q, "res")), mse(col(Q, "lfl")); x = xs(Q); t_ = temp(Q, "rec", "ben")
    sbc = sbk_ = np.nan
    if E:
        sbc = np.mean([sb_of(groups(e)["claim"]) for e in E]); sbk_ = np.mean([sb_of(groups(e)["care"]) for e in E])
    return (f"| {nm} | {len(Q)} | {np.mean(col(Q, 'n')):.1f} / {np.mean(col(Q, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({se_(a)}) | {t_[0]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(Q, 'care_m') + col(Q, 'claimed_m')):.0f} / {np.mean(col(Q, 'care_mc')):.0f} | {np.mean(col(Q, 'claims')):.1f} | "
            f"{np.mean(col(Q, 'reach')):.3f} / {np.mean(col(Q, 'reachc')):.3f} | {np.mean(col(Q, 'dep')):.2f} / {np.mean(col(Q, 'depc')):.2f} | {np.mean(col(Q, 'rvm')):.1f} / {np.mean(col(Q, 'rvmc')):.1f} | **{np.mean(col(Q, 'aud')):.1f} / {np.mean(col(Q, 'audc')):.1f}** | {np.mean(col(Q, 'panel')):.1f} / {np.mean(col(Q, 'panelc')):.1f} | {sbc:.1f} / {sbk_:.1f} |")
def oh_row(nm, E):
    if not E or np.isnan(np.nanmean([f(e, "care_cost_real") for e in E])): return None
    nv = np.mean([f(e, "vested_real_roots") for e in E]); t = lambda k: np.mean([f(e, k) for e in E]) / nv
    return f"| {nm} | {nv:.0f} | {t('care_cost_real'):.2f} | {t('care_cost_plant'):.2f} | {t('troop_review_cost'):.2f} | {t('chk_cost'):.2f} | {t('cost_of_truth'):.2f} | {t('plant_price_sum'):.2f} | **{np.mean([f(e, 'sys_overhead_per_vested') for e in E]):.2f}** | {np.mean([f(e, 'P_t') for e in E]):.2f} |"
OH_HDR = ["| population | vested real roots | care on real cases | care on planted | troops' review cost (the checkers' included) | of it the checkers' | cost of truth | plants' price | **overhead a vested task** | P_t at the end |", "|---|---|---|---|---|---|---|---|---|---|"]
def three_row(nm, E):
    th = [three(e) for e in E]; m = lambda k: np.mean([t[k] for t in th])
    return f"| {nm} | {np.mean([f(e, 'bad_deliveries') for e in E]):.0f} | **{m('appr'):.1f}** | **{m('over'):.1f}** | **{m('paid'):.1f}** | {np.mean([1000 * f(e, 'leak_bad') for e in E]):.1f} | **{m('mirror'):.2f}** | {m('mirror_audit'):.2f} | {m('mirror_state'):.2f} |"
THREE_HDR = ["| read | bad deliveries a run | **approved at first** | **stopped before payment** | **paid in the end** | leak ‰ | **wrong rejections of good work standing** | by the audit road | after the state's audit |", "|---|---|---|---|---|---|---|---|---|"]
def ra_row(nm, E):
    Rr = [raj(e) for e in E]
    if not Rr or not any(Rr): return None
    g = g_of(Rr); tot = g("member_n") + g("state_n") + g("panel_n") + g("never_n")
    sh = lambda a, b: f"{g(a):.0f}; {g(b):.1f} ({g(b) / g(a):.3f})" if g(a) else "—"
    sd_ = (f" of them drawn {sh('statedrawn_n', 'statedrawn_over')}" if g("statedrawn_n") else "")
    ck = (f"{g('chk_good_n') + g('chk_bad_n'):.0f}; {g('chk_good_over') + g('chk_bad_over'):.1f} ({(g('chk_good_over') + g('chk_bad_over')) / (g('chk_good_n') + g('chk_bad_n')):.4f}); of them bad {g('chk_bad_n'):.1f}, overturned {g('chk_bad_over'):.1f}" if (g("chk_good_n") + g("chk_bad_n")) else "—")
    return f"| {nm} | {tot:.0f} | **{sh('member_n', 'member_over')}** | {sh('member_bad_n', 'member_bad_over')} | **{sh('state_n', 'state_over')}**{sd_} | {sh('state_bad_n', 'state_bad_over')} | {sh('panel_n', 'panel_over')} | {g('never_n'):.0f}; {g('never_bad_n'):.1f} bad | {ck} |"
RA_HDR = ["| population | first approvals of a member's real delivery a run | **looked at by a member's audit: n; overturned (share)** | of them bad: n; overturned | **by the state's audit: n; overturned (share)** | of them bad: n; overturned | by a dispute panel with no audit | never looked at; bad among them | **the checkers' looks on top: n; overturned (rate); bad among them** |", "|---|---|---|---|---|---|---|---|---|"]
def pair_row(nm, E):
    P = [p for p in (pairs_of(e) for e in E) if p]
    if not P: return None
    m = lambda k: np.mean([p[k] for p in P]); return f"| {nm} | {m('pairs'):.0f} | {m('meetings'):.0f} | **{pm(mse([p['mean'] for p in P]), 2)}** | {m('gt3'):.2f} | {m('mx'):.0f} |"
PAIR_HDR = ["| cell | pairs that meet a run (a first reviewer and the member at its audit seat) | meetings | **meetings a pair** | share of pairs meeting more than three times | the largest |", "|---|---|---|---|---|---|"]
def world_tab(nm_base, Pv, base_lab, rows):
    out = [f"\n**{nm_base}** — by seed:\n", f"| measure | {base_lab} | this | **this − {base_lab}** (SE) |", "|---|---|---|---|"]
    for k, k0, lab, d_ in rows:
        if not Pv or k not in Pv[0] or k0 not in Pv[0]: continue
        a0, a1 = col(Pv, k0), col(Pv, k)
        if np.all(np.isnan(a0)) and np.all(np.isnan(a1)): continue
        dd = mse(a1 - a0); out.append(f"| {lab} | {np.nanmean(a0):.{d_}f} | {np.nanmean(a1):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    return out
WROWS = (("life", "lifec", "the slot of record, real", 0), ("lres", "lresc", "with the reservation", 0), ("w_leak", "w0_leak", "**the leak, ‰**", 1), ("w_fa", "w0_fa", "standing false approvals a run", 1), ("w_oh", "w0_oh", "**the overhead a vested task**", 2), ("w_cot", "w0_cot", "the cost of truth a run", 0),
         ("aud", "audc", "**audit seats a slot**", 1), ("panel", "panelc", "panel seats a slot", 1), ("ss_audit", "ss0_audit", "**the state's share of the audit seats**", 3), ("ss_panel", "ss0_panel", "the state's share of the panel seats", 3), ("reach", "reachc", "slots suspended at least once", 3), ("dep", "depc", "slots departed", 3),
         ("t_appr", "t0_appr", "bad deliveries approved at first", 1), ("t_over", "t0_over", "stopped before payment", 1), ("t_paid", "t0_paid", "paid in the end", 1), ("t_mirror", "t0_mirror", "**the mirror: wrong rejections of good work standing**", 2), ("t_mirror_audit", "t0_mirror_audit", "by the audit road", 2), ("t_mirror_state", "t0_mirror_state", "after the state's audit", 2),
         ("w_dec", "w0_dec", "deciding verdicts opened", 1), ("w_dfresh", "w0_dfresh", "of them afresh after the state's audit", 1), ("w_Pt", "w0_Pt", "P_t at the end", 2), ("w_dep", "w0_dep", "departures a run", 1), ("w_susp", "w0_susp", "suspensions a run", 1), ("w_arr", "w0_arr", "arrivals a run", 1),
         ("w_ma", "w0_ma", "members' audit seats a run", 1), ("w_ta", "w0_ta", "the state's audit reviews a run", 1), ("w_drawn_a", "w0_drawn_a", "troops drawn at the audit seat", 1), ("w_drawn_aw", "w0_drawn_aw", "of them at a later step (the wait)", 1), ("w_drawn_p", "w0_drawn_p", "troops drawn at the panels", 1),
         ("w_sb_seats", "w0_sb_seats", "**seats whose fee went to the members that stood**", 1), ("w_sb_tot", "w0_sb_tot", "pay for standing by a run, nominal", 0), ("w_sb_names", "w0_sb_names", "members that stood at drawn seats, summed", 1), ("w_omfee", "w0_omfee", "**Ω's income from the troops' review fees, nominal**", 0),
         ("w_chk_looks", "w0_chk_looks", "**checkers' looks after an audit had confirmed**", 1), ("w_chk_looks_no", "w0_chk_looks_no", "checkers' looks with no audit", 1), ("w_chk_over_a", "w0_chk_over_a", "overturned after an audit", 2), ("w_chk_over_n", "w0_chk_over_n", "overturned with no audit", 2), ("w_chk_cost", "w0_chk_cost", "the checkers' cost a run, nominal", 0), ("w_chk_skip", "w0_chk_skip", "approvals the court had confirmed, not sampled", 1), ("w_chk_ref", "w0_chk_ref", "looks refused", 2))
def pool_tab(E, kind):
    g = g_of([sj(e) for e in E]); pool = [g(f"seatpool_{kind}_{i}") for i in range(6)]; tot = sum(pool)
    fill = {k: g(f"seatfill_{kind}_{k}") for k in ("member_step1", "member_later", "state", "troop_drawn", "troop_drawn_later")}; ft = fill["member_step1"] + fill["member_later"] + fill["state"] + fill["troop_drawn"]
    stood = {i: g(f"seatstood_{kind}_{i}") for i in range(1, 6)}
    return dict(tot=tot, shares=[p / tot if tot else np.nan for p in pool], fill=fill, ft=ft, fshares={k: v / ft if ft else np.nan for k, v in fill.items()}, back=(fill["member_later"] / pool[0]) if pool[0] else np.nan, stood=stood, stood_tot=sum(stood.values()))
# ------------------------------------------------------------------ 2. reads 57 to 61: the wait kept, the pay for standing by
L += ["\n## 2. Reads 57 to 61: the wait kept under a minimum (`--draw-wait on`), and pay for standing by (`--standby-pay on`); world 3's cell, K = 3, (i) on, seeds 21–120\n",
      "What was said before building (notes §128a): under the wait kept no troop is drawn where no member is free — the seat waits as with the option off, within w_R no demand of the pass's, at w_R the pass's summons as today, recorded as summoned; the draw is made at the first later step at which a member is free, among the free members and troop candidates up to K. "
      "The pay for standing by moves at the seat's settlement, the moment the troop's fee would have moved, in equal parts to the members that stood in the draw; a share owed to a name that has since departed is Ω's; a member that lost its standing is paid.\n"]
P57v53 = pop_rows(LV(R57), R53); P57v35 = pop_rows(LV(R57), R35); P58v57 = pop_rows(LV(R58), R57); P58v35 = pop_rows(LV(R58), R35); P58v53 = pop_rows(LV(R58), R53); P57c = pop_rows(LV(R57), CW3); P58c = pop_rows(LV(R58), CW3)
for nm, Pv, base in (("Read 57: the all-careful with the seats drawn, K = 3, (i) and the wait kept, against read 53 by seed", P57v53, "read 53"), ("Read 57 against read 35 (the seats drawn, no minimum)", P57v35, "read 35"),
                     ("Read 58: the same with pay for standing by, against read 57", P58v57, "read 57"), ("Read 58 against read 35", P58v35, "read 35"), ("Read 58 against read 53", P58v53, "read 53")):
    if Pv: L += world_tab(nm, Pv, base, WROWS)
L += ["\n**The pool at a seat's first seating step and how the seat was filled** (`seat_json`; a member's real roots' seats; the fill at a later step and the members that stood where a troop was drawn, new here):\n",
      "| read | seat | seats a run | **free at the first step: 0** | 1 | 2 | 3 | 4 | 5+ | filled by a member at the first step | by a member later | by the state's summons after the wait | **by a drawn troop** (of them at a later step) | of the seats with none free, a member came within the wait | **members stood and a troop was drawn: 1 / 2 / 3 / 4 stood** |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
for nm, E in (("35 (the seats drawn)", R35L), ("53 (K = 3, (i))", LV(R53)), ("**57** (the wait kept)", LV(R57)), ("**58** (the wait, the pay)", LV(R58)), ("**59** (M on 1 in 4, the pay, no wait)", R59), ("**60** (M on 1 in 4, the wait, the pay)", R60), ("**61** (cell B, the wait, the pay)", R61)):
    if not E or not any(sj(e) for e in E): continue
    for kind in ("audit", "panel"):
        p = pool_tab(E, kind); s = p["shares"]; fs = p["fshares"]; st = p["stood"]
        L.append(f"| {nm} | {kind} | {p['tot']:.0f} | **{s[0]:.3f}** | {s[1]:.3f} | {s[2]:.3f} | {s[3]:.3f} | {s[4]:.3f} | {s[5]:.3f} | {fs['member_step1']:.3f} | {fs['member_later']:.3f} | {fs['state']:.3f} | **{fs['troop_drawn']:.3f}** ({fs['troop_drawn_later']:.3f}) | {p['back']:.3f} | **{st[1] / p['tot']:.3f} / {st[2] / p['tot']:.3f} / {st[3] / p['tot']:.3f} / {st[4] / p['tot']:.3f}** |")
# the pay by kind of slot
L += ["\n**The pay for standing by a slot, real, by kind of slot** (the `standby` class of the slot's wallet events; the founders in place from tick 0, the arrivals after):\n", "| read | every slot | founders | arrivals | the conduct | the careful beside | slots paid at all |", "|---|---|---|---|---|---|---|"]
for nm, E, mixed in (("58 (the all-careful, the wait, the pay)", LV(R58), False), ("59 (M on 1 in 4, the pay, no wait)", R59, True), ("60 (M on 1 in 4, the wait, the pay)", R60, True), ("61 (cell B on every slot, the wait, the pay)", R61, False)):
    if not E: continue
    S = standby_by_kind(E, mixed); m = lambda k: np.nanmean([d.get(k, np.nan) for d in S.values()])
    L.append(f"| {nm} | **{m('every slot'):.1f}** | {m('founders'):.1f} | {m('arrivals'):.1f} | {m('the conduct'):.1f} | {m('the careful beside'):.1f} | {m('paid slots'):.3f} |")
# the pairs
L += ["\n**The pairs** (a first reviewer and the member at its audit seat):\n"] + PAIR_HDR
for nm, E in (("read 35", R35L), ("read 53 (K = 3, (i))", LV(R53)), ("**read 57** (the wait kept)", LV(R57)), ("**read 58**", LV(R58)), ("read 56", R56), ("**read 59**", R59), ("**read 60**", R60), ("read 55", R55), ("**read 61**", R61)):
    row = pair_row(nm, E) if E else None
    if row: L.append(row)
# reads 59 and 60: conduct M on 1 in 4
Q19, Q56, Q59, Q60 = rows_of(R19, CW3), rows_of(R56, CW3), rows_of(R59, CW3), rows_of(R60, CW3)
if Q59:
    L += ["\n**Reads 59 and 60: conduct M at a dose of 0.2 on 1 slot in 4 (read 19's population) with the seats drawn, K = 3, (i) and the pay — without the wait (59) and with it (60)** (read as read 19 was; against reads 56 and 19 by seed).\n"] + HDR
    L += [qrow("19: the cell of record", Q19), qrow("56: K = 3, (i)", Q56, R56), qrow("**59: the pay, no wait**", Q59, R59)] + ([qrow("**60: the pay, the wait kept**", Q60, R60)] if Q60 else [])
    L += ["\n| measure | read 56 | **read 59** | **59 − 56** (SE) | **read 60** | **60 − 56** (SE) | **60 − 59** (SE) |", "|---|---|---|---|---|---|---|"]
    for k, lab, d_ in (("rec", "careful − conduct, of record", 0), ("res", "with the reservation", 0), ("lfl", "like for like", 0), ("aud", "the conduct's audit seats", 1), ("audc", "the careful's audit seats", 1), ("panel", "the conduct's panel seats", 1), ("panelc", "the careful's panel seats", 1),
                       ("reach", "the conduct's slots suspended at least once", 3), ("reachc", "the careful's", 3), ("noseat", "the conduct's member ticks without the earned seats", 3), ("noseatc", "the careful's", 3), ("w_leak", "the leak ‰", 1), ("w_fa", "standing FA", 1), ("w_oh", "the overhead", 2), ("ss_audit", "the state's share of the audit seats", 3), ("w_sb_tot", "pay for standing by a run, nominal", 0), ("w_omfee", "Ω's income from the troops' fees", 0)):
        if k not in Q56[0] or k not in Q59[0]: continue
        d1, m56, m59, _ = paired(Q56, Q59, k); cells = f"| {lab} | {m56:.{d_}f} | {m59:.{d_}f} | **{d1[0]:+.{d_}f} ± {d1[1]:.{d_}f}** ({se_(d1)}) |"
        if Q60:
            d2, _, m60, _ = paired(Q56, Q60, k); d3 = paired(Q59, Q60, k)[0]; cells += f" {m60:.{d_}f} | **{d2[0]:+.{d_}f} ± {d2[1]:.{d_}f}** ({se_(d2)}) | {d3[0]:+.{d_}f} ± {d3[1]:.{d_}f} |"
        else: cells += " — | — | — |"
        L.append(cells)
    def ls_pair(QA, QB):
        A_, B_ = {r["seed"]: r for r in QA}, {r["seed"]: r for r in QB}; sd = sorted(set(A_) & set(B_)); return mse([(B_[s]["rec"] + B_[s]["ben"]) / B_[s]["call"] - (A_[s]["rec"] + A_[s]["ben"]) / A_[s]["call"] for s in sd])
    x56, x59 = xs(Q56)[0], xs(Q59)[0]; d59 = ls_pair(Q56, Q59); cells = f"| the level saving of record | {x56[0]:.2f} | {x59[0]:.2f} | **{d59[0]:+.2f} ± {d59[1]:.2f}** ({se_(d59)}) |"
    if Q60: x60 = xs(Q60)[0]; d60 = ls_pair(Q56, Q60); d60b = ls_pair(Q59, Q60); cells += f" {x60[0]:.2f} | **{d60[0]:+.2f} ± {d60[1]:.2f}** ({se_(d60)}) | {d60b[0]:+.2f} ± {d60b[1]:.2f} |"
    L.append(cells)
    L.append(f"\nThe level saving against 0.9: read 56 {x56[0]:.2f} ± {x56[1]:.2f} ({(x56[0] - 0.9) / x56[1]:+.1f} SE from it), read 59 **{x59[0]:.2f} ± {x59[1]:.2f}** ({(x59[0] - 0.9) / x59[1]:+.1f} SE)" + (f", read 60 **{x60[0]:.2f} ± {x60[1]:.2f}** ({(x60[0] - 0.9) / x60[1]:+.1f} SE)" if Q60 else "") + f"; read 19's 1.23 ± 0.11 stood +3.0 over it.\n")
    G59, G60 = gap_terms(R59), gap_terms(R60)
    pairs = [("read 19", G19), ("read 56", G56), ("read 59", G59)] + ([("read 60", G60)] if G60 else [])
    L += terms_tab("**The gap by term for reads 59 and 60** (as 6.4 asks for read 56: the careful beside less the conduct, real a slot, by seed; the difference from read 19 by seed):", pairs)
# read 61
P61v55 = pop_rows(R61, D(R55)); P61v40 = pop_rows(R61, D(R40)); P61 = pop_rows(R61, CW3)
if P61v55:
    L += world_tab("**Read 61: cell B at a dose of 0.2 on every slot with the seats drawn, K = 3, (i), the wait kept and the pay, against read 55 by seed**", P61v55, "read 55", WROWS)
    d61, d55 = fa_split(R61), fa_split(R55)
    L.append(f"\nOf the conduct's claims on real bad work at the first review ({d61['claims']:.1f} a run): stayed paid {d61['paid']:.3f} (read 55's {d55['paid']:.3f}; read 40's {fa_split(R40)['paid']:.3f}) — never audited {d61['none']:.3f}, confirmed by a member's audit {d61['mconf']:.3f}, by the state's {d61['sconf']:.3f}; overturned after a member's audit differed {d61['mdiff']:.3f}, after the state's {d61['sdiff']:.3f}. The claims overturned **{1 - d61['paid']:.3f}** (read 55's {1 - d55['paid']:.3f}).")
    st61 = np.array([ra_rate(e, "state") for e in R61]); st58 = np.array([ra_rate(e, "state") for e in LV(R58)]) if R58 else np.array([np.nan]); st57 = np.array([ra_rate(e, "state") for e in LV(R57)]) if R57 else np.array([np.nan])
    sd61 = np.array([ra_rate(e, "statedrawn") for e in R61]); sd58 = np.array([ra_rate(e, "statedrawn") for e in LV(R58)]) if R58 else np.array([np.nan])
    n61 = int((st61 > np.nanmax(st58)).sum()); n61d = int((sd61 > np.nanmax(sd58)).sum()); n61v57 = int((st61 > np.nanmax(st57)).sum())
    L.append(f"\n**The state's rate of overturning, run by run, with the wait kept.** Read 61: on every state look {st61.mean():.4f} with a spread of {st61.std(ddof=1):.4f} (the lowest run {st61.min():.4f}); read 58 (a careful population at the same options): {np.nanmean(st58):.4f} ± {np.nanstd(st58, ddof=1):.4f}, its highest run {np.nanmax(st58):.4f}. Read 61 stands above read 58's highest in **{n61} of {len(st61)}** runs (above read 57's highest in {n61v57}). "
             f"On the drawn looks alone: read 61 {sd61.mean():.4f}, read 58's highest {np.nanmax(sd58):.4f}, **{n61d} of {len(sd61)}** above.\n")
    RATE61 = (n61, len(st61))
# ------------------------------------------------------------------ 3. reads 62 to 64: the ruling alone on cell B, and the checkers
L += ["\n## 3. Reads 62 to 64: the ruling alone on cell B (read 62), and checkers at one approval in five (`--checker-rate 0.2`; reads 63 and 64)\n",
      "What was said before building (notes §128a): the coin runs over the approvals of a member's real root delivery whose window closes with the approval standing and the one challenge round unused — never looked at again, or audited and confirmed; an approval the court has already confirmed is not sampled and read apart. The look is seated at the window's close, after the audit where the roll took one and before the money is final — the 'on top' form; it holds the case open past its window until answered. "
      "The look that agrees lets the case vest at the next vesting step; one that differs opens the deciding verdict afresh and the case settles as after an audit that differed. The look's cost is the state's own (nothing from the allowance, no fee).\n"]
P62v40 = pop_rows(R62, D(R40)); P62 = pop_rows(R62, CW3)
if P62v40:
    L += world_tab("**Read 62: cell B at a dose of 0.2 on every slot with (i) and nothing else, against read 40 by seed**", P62v40, "read 40", WROWS)
    L.append(f"\nAgainst world 3's all-careful by seed the population's slot of record {pm(mse(col(P62, 'life') - col(P62, 'lifec')), 0)} (level saving {pm(xs(P62)[0], 2)}; read 40's {pm(xs(pop_rows(R40, CW3))[0], 2)}).\n")
P63v51 = pop_rows(LV(R63), R51); P63 = pop_rows(LV(R63), CW3)
if P63v51:
    L += world_tab("**Read 63: world 3's all-careful with (i) and checkers at one approval in five, against read 51 by seed**", P63v51, "read 51", WROWS)
    E63 = LV(R63); looks = np.mean([f(e, "chk_looks_after") + f(e, "chk_looks_no") for e in E63]); nv63 = np.mean([f(e, "vested_real_roots") for e in E63]); cost = np.mean([f(e, "chk_cost") for e in E63])
    real63 = np.mean([20.0 / f(e, "P_t") for e in E63])
    L.append(f"\nThe checkers' looks a run **{looks:.0f}** ({np.mean([f(e, 'chk_looks_after') for e in E63]):.0f} after an audit had confirmed the approval, {np.mean([f(e, 'chk_looks_no') for e in E63]):.0f} with no audit; {np.mean([f(e, 'chk_skipped_court') for e in E63]):.0f} approvals the court had already confirmed not sampled; {np.mean([f(e, 'chk_refused') for e in E63]):.2f} refused), their cost **{cost / nv63:.2f} a vested task** nominal ({cost:.0f} a run; c_T 3.0 real a look at the published index), "
             f"the overhead {np.mean([f(e, 'sys_overhead_per_vested') for e in E63]):.2f} against read 51's {np.mean(col(P63v51, 'w0_oh')):.2f}.")
    for by, lab in (("after", "after an audit had confirmed"), ("no", "with no audit"), ("all", "every look")):
        r63 = np.array([chk_rate(e, by) for e in E63]); r64 = np.array([chk_rate(e, by) for e in R64]) if R64 else np.array([np.nan])
        L.append(f"- The checkers' rate of overturning {lab}: read 63 run by run {np.nanmean(r63):.4f} with a spread of {np.nanstd(r63, ddof=1):.4f} (the highest run {np.nanmax(r63):.4f}); read 64 {np.nanmean(r64):.4f} ± {np.nanstd(r64, ddof=1):.4f} (the lowest {np.nanmin(r64):.4f}).")
    L.append("")
P64v62 = pop_rows(R64, D(R62)); P64v40 = pop_rows(R64, D(R40)); P64 = pop_rows(R64, CW3)
if P64v62:
    L += world_tab("**Read 64: cell B at a dose of 0.2 on every slot with (i) and checkers at one approval in five, against read 62 by seed**", P64v62, "read 62", WROWS)
    d64, d62 = fa_split(R64), fa_split(R62)
    L.append(f"\nOf the conduct's claims on real bad work at the first review ({d64['claims']:.1f} a run): stayed paid {d64['paid']:.3f} (read 62's {d62['paid']:.3f}); the checkers' catches are read in `ra_json` apart from the member's, the state's and nobody's.")
    E63 = LV(R63); rows = []
    for by, lab in (("after", "after an audit had confirmed"), ("no", "with no audit"), ("all", "every look")):
        full = chk_above(R64, E63, by); half = chk_above(R64, E63, by, 0.5)
        rows.append(f"- {lab}: read 64's rate stands above read 63's highest run in **{full[0]} of {full[1]}** runs on every look; on a random half of each run's looks (200 draws, both reads on the same share) **{half[0]:.0f} ± {half[2]:.0f} of {half[1]}**.")
        if by == "all": RATE64 = (full[0], full[1])
    L += ["\n**The checkers' rate of overturning as a measure of a shared miss** (run by run; the conditions take every look):\n"] + rows
    g64 = g_of([raj(e) for e in R64]); g63 = g_of([raj(e) for e in E63])
    L.append(f"\nThe looks by the truth: read 64's checkers looked at {g64('chk_good_n'):.0f} good and {g64('chk_bad_n'):.1f} bad approvals a run and overturned {g64('chk_bad_over'):.1f} of the bad and {g64('chk_good_over'):.2f} of the good; read 63's {g63('chk_good_n'):.0f} / {g63('chk_bad_n'):.1f}, {g63('chk_bad_over'):.1f} / {g63('chk_good_over'):.2f}.\n")
# ------------------------------------------------------------------ 4. the four things and the two rates for every read
L += ["\n## 4. The four things of addendum 32 and the two rates of overturning, for every read\n", "**How often a slot is looked at** (AL4.1):\n",
      "| read | slot kind | slots | first approvals of real work a slot | **by a member: n (share)** | **by the state: n (share)** | by a dispute panel | never looked at | overturned: after a member's / the state's / a panel's | **marks a slot** | wrong planted verdicts as a member |", "|---|---|---|---|---|---|---|---|---|---|---|"]
for nm, E, mixed in (("all-careful", CW3L, False), ("35", R35L, False), ("53", LV(R53), False), ("57", LV(R57), False), ("58", LV(R58), False), ("19", R19, True), ("56", R56, True), ("59", R59, True), ("60", R60, True), ("40", R40, False), ("55", R55, False), ("61", R61, False), ("62", R62, False), ("51", LV(R51), False), ("63", LV(R63), False), ("64", R64, False)):
    if E: L += al_rows(nm, E, mixed)
L += ["\n**The three counts in one row, and the mirror by road** (AL4.2, AL4.3):\n"] + THREE_HDR
for nm, E in (("all-careful", CW3L), ("35", R35L), ("53", LV(R53)), ("57", LV(R57)), ("58", LV(R58)), ("19", R19), ("56", R56), ("59", R59), ("60", R60), ("40", R40), ("55", R55), ("61", R61), ("62", R62), ("51", LV(R51)), ("63", LV(R63)), ("64", R64)):
    if E: L.append(three_row(nm, E))
L += ["\n**The overhead's terms** (AL4.4; the checkers' cost inside the troops' review cost, read apart):\n"] + OH_HDR
for nm, E in (("all-careful", CW3L), ("35", R35L), ("53", LV(R53)), ("57", LV(R57)), ("58", LV(R58)), ("19", R19), ("56", R56), ("59", R59), ("60", R60), ("40", R40), ("55", R55), ("61", R61), ("62", R62), ("51", LV(R51)), ("63", LV(R63)), ("64", R64)):
    row = oh_row(nm, E) if E else None
    if row: L.append(row)
L += ["\n**The two rates of overturning, and the checkers' on top** (every first approval of a member's real delivery by who looked again; the state's drawn looks apart; the checkers' looks and overturns apart from the three):\n"] + RA_HDR
for nm, E in (("world 3's all-careful", CW3L), ("read 35", R35L), ("read 53", LV(R53)), ("read 57", LV(R57)), ("read 58", LV(R58)), ("read 19", R19), ("read 56", R56), ("read 59", R59), ("read 60", R60), ("read 40", R40), ("read 55", R55), ("read 61", R61), ("read 62", R62), ("read 51", LV(R51)), ("read 63", LV(R63)), ("read 64", R64)):
    row = ra_row(nm, E) if E else None
    if row: L.append(row)
# ------------------------------------------------------------------ 5. the expectations and the conditions
L += ["\n## 5. Against the expectations stated before the run, and the conditions\n", "The reviewer's figures in real took 3.3 real a seat; the fee is 2.83 real (§1, 6.1), and his ranges that hang on it are read as he set them, the proportion noted beside.\n"]
VER = []
if P57v53 and P57v35:
    ss57, aud57 = np.mean(col(P57v53, "ss_audit")), np.mean(col(P57v53, "aud")); dl57 = mse(col(P57v35, "life") - col(P57v35, "lifec"))
    chk(in_band(ss57, 0.53, 0.60), f"read 57: the state on 0.53 to 0.60 of the audit seats (reads 52 and 53's 0.618) — {ss57:.3f}"); chk(in_band(aud57, 21, 25), f"read 57: a member holds 21 to 25 audit seats — {aud57:.1f}"); chk(in_band(-dl57[0], 20, 48), f"read 57: the slot 20 to 48 real under read 35's — {-dl57[0]:.0f} ± {dl57[1]:.0f} under")
if P58v57 and P58v35:
    p58 = pool_tab(LV(R58), "audit"); stood_share = p58["stood_tot"] / p58["tot"]; sbs = np.mean([standby_by_kind(LV(R58), False)[int(e["seed"])]["every slot"] for e in LV(R58)]); dl58 = mse(col(P58v35, "life") - col(P58v35, "lifec")); dss = mse(col(P58v57, "ss_audit") - col(P58v57, "ss0_audit"))
    chk(in_band(stood_share, 0.24, 0.32), f"read 58: members stood and a troop was drawn at 0.24 to 0.32 of the audit seats — {stood_share:.3f}"); chk(in_band(sbs, 40, 58), f"read 58: the pay for standing by 40 to 58 real a slot (at 3.3 a seat; at 2.83 the band is 34 to 50) — {sbs:.1f}")
    chk(in_band(-dl58[0], -35, 15), f"read 58: the slot between 15 real under read 35's and 35 over — {-dl58[0]:+.0f} ± {dl58[1]:.0f} under"); chk(not two_se(dss), f"read 58: the state's share read 57's within two SE — {dss[0]:+.3f} ± {dss[1]:.3f}")
if Q59:
    a59 = mse(col(Q59, "rec")); x59 = xs(Q59)[0]; d59 = paired(Q56, Q59, "rec")[0]
    chk(in_band(a59[0], 112, 160), f"read 59: the conduct's slot 112 to 160 real behind the careful beside it (read 56's 110 ± 23) — {a59[0]:+.0f} ± {a59[1]:.0f}"); chk(in_band(x59[0], 0.76, 1.02), f"read 59: level saving 0.76 to 1.02 — {x59[0]:.2f} ± {x59[1]:.2f}")
    VER.append(verdict(f"Pay for standing by gives back a part of what a minimum takes from what a member has to lose (shown if read 59's gap is over read 56's by two SE, by seed; refuted if at or under it at the point value) — read 59 less read 56 {d59[0]:+.0f} ± {d59[1]:.0f}", d59[0] - 2 * d59[1] > 0, d59[0] <= 0))
if Q60:
    a60 = mse(col(Q60, "rec")); x60 = xs(Q60)[0]
    chk(in_band(a60[0], 128, 190), f"read 60: the conduct's slot 128 to 190 real behind — {a60[0]:+.0f} ± {a60[1]:.0f}"); chk(in_band(x60[0], 0.85, 1.18), f"read 60: level saving 0.85 to 1.18 — {x60[0]:.2f} ± {x60[1]:.2f}")
    VER.append(verdict(f"With the wait kept and pay for standing by, the member of read 19 is held again under a minimum of three (shown if read 60's level saving is above 0.9 by two SE; refuted if under 0.9 at the point value) — {x60[0]:.2f} ± {x60[1]:.2f}, {(x60[0] - 0.9) / x60[1]:+.1f} SE from 0.9", x60[0] - 2 * x60[1] > 0.9, x60[0] < 0.9))
if P61v55:
    lk61 = np.mean(col(P61v55, "w_leak")); d61 = fa_split(R61)
    chk(in_band(lk61, 66, 78), f"read 61: leak 66 to 78 ‰ — {lk61:.1f}"); chk(in_band(1 - d61["paid"], 0.42, 0.50), f"read 61: of the conduct's claims 0.42 to 0.50 end overturned — {1 - d61['paid']:.3f}"); chk(RATE61[0] >= 93, f"read 61: the state's rate above read 58's highest run in 93 or more runs of 100 — {RATE61[0]} of {RATE61[1]}")
    VER.append(verdict(f"A minimum with the wait kept still tells a shared miss within one run (shown if read 61's state rate, run by run, is above read 58's highest run in at least 95 of 100; refuted if in fewer than 75) — {RATE61[0]} of {RATE61[1]}", RATE61[0] >= 95, RATE61[0] < 75))
if P62v40:
    lk62 = np.mean(col(P62v40, "w_leak")); m62 = np.mean(col(P62v40, "t_mirror"))
    chk(in_band(lk62, 89, 95), f"read 62: leak 89 to 95 ‰ (read 40's 92.3) — {lk62:.1f}"); chk(in_band(m62, 1.9, 2.7), f"read 62: 1.9 to 2.7 wrong rejections stand a run (4.85) — {m62:.2f}")
if P63v51:
    doh = mse(col(P63v51, "w_oh") - col(P63v51, "w0_oh")); lk63 = np.mean(col(P63v51, "w_leak")); dm = mse(col(P63v51, "t_mirror") - col(P63v51, "t0_mirror")); da = mse(col(P63v51, "aud") - col(P63v51, "audc"))
    chk(in_band(doh[0], 0.45, 0.75), f"read 63: the overhead 0.45 to 0.75 a task above read 51's — {doh[0]:+.2f} ± {doh[1]:.2f}"); chk(in_band(lk63, 3.4, 4.8), f"read 63: leak 3.4 to 4.8 ‰ — {lk63:.1f}"); chk(dm[0] <= 0.5, f"read 63: the mirror up to 0.5 a run above read 51's — {dm[0]:+.2f} ± {dm[1]:.2f}"); chk(not two_se(da), f"read 63: a member's audit seats read 51's within two SE — {da[0]:+.1f} ± {da[1]:.1f}")
    VER.append(verdict(f"Checkers leave the members their seats (shown if a member's audit seats in read 63 are within two SE of read 51's, by seed) — {da[0]:+.1f} ± {da[1]:.1f}", not two_se(da), two_se(da)))
if P64v62:
    lk64 = np.mean(col(P64v62, "w_leak"))
    chk(in_band(lk64, 70, 79), f"read 64: leak 70 to 79 ‰ — {lk64:.1f}"); chk(RATE64[0] >= 93, f"read 64: the checkers' rate above read 63's highest run in 93 or more runs of 100 (the look after the audit) — {RATE64[0]} of {RATE64[1]}")
    VER.append(verdict(f"Checkers at one approval in five tell a shared miss from a careful population within one run (shown if read 64's checkers' rate, run by run, is above read 63's highest run in at least 95 of 100; refuted if in fewer than 75) — {RATE64[0]} of {RATE64[1]}", RATE64[0] >= 95, RATE64[0] < 75))
L += CHK; n_met = sum(1 for c in CHK if c.startswith("- MET")); L.append(f"\n**{n_met} of {len(CHK)} expectations met.** (Reads 57 and 62 set no condition: a price and a base.)\n")
L += ["\n### The conditions\n"] + VER
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L[:8])); print(f"... written {sys.argv[1]} ({len(L)} lines)")
