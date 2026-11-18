"""Addendum 31 (November 18, 2026, evening; notes §126): the reviewer's arithmetic on §125 confirmed or replaced (AK3), the eight readings asked from the record (AK4, AL7), and nine
reads without training at 29cffb7c7 — reads 41 and 42 (cell B at a dose of 0.5 and of 1 on real cases, on 1 slot in 4), reads 43 to 45 (the mark for a miss on real work:
`--real-miss-mark on`; world 3's all-careful, cell B on 1 in 4 and on every slot), reads 46, 46a and 47 (the buyer's complaint on the ruled road: `--dispute-policy truthful
--dispute-rate 1.0`, with and without `--second-filing on`; cell B on every slot and world 3's all-careful), and AL4's four things for every read. World 3's all-careful and
reads 38, 39 and 40 run again whole at this commit for the readings the record does not carry (ρ, every first approval by who looked again) and checked to the key against
a26/ first. a26_read.py's helpers copied. Usage: a27_read.py OUT.md"""
import json, os, sys, hashlib, math, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; D27, D26, D25, D24, D22, D19, D18 = f"{R}/a27", f"{R}/a26", f"{R}/a25", f"{R}/a24", f"{R}/a22", f"{R}/a19", f"{R}/a18"
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
def repro(new_eps, old_eps, label):
    old = {int(e["seed"]): e for e in old_eps}; n_rows = n_keys = n_slots = n_seeds = 0; diffs = []; bm_d = []; pm_d = []
    for e in new_eps:
        s_ = int(e["seed"])
        if s_ not in old: continue
        o = old[s_]; n_seeds += 1
        for k in o:
            if k in ("learner_slots_json", "bad_met_first_json", "pair_meet_json") or k in NEW_ROW: continue
            n_rows += 1
            if o[k] != e.get(k): diffs.append((s_, k))
        So, Sn = json.loads(o["learner_slots_json"]), json.loads(e["learner_slots_json"])
        for x, v in Sn.items():
            n_slots += 1
            for k, val in v.items():
                if k in NEW_SLOT or k.startswith("ra_"): continue
                n_keys += 1
                if So.get(x, {}).get(k) != val: diffs.append((s_, x, k))
        if json.loads(o["bad_met_first_json"]) != json.loads(e["bad_met_first_json"]): bm_d.append(s_)
        if json.loads(o.get("pair_meet_json") or "{}") != json.loads(e.get("pair_meet_json") or "{}"): pm_d.append(s_)
    return (f"- **{label}**: {n_seeds} seeds, {n_rows} row columns and {n_keys} per-slot keys over {n_slots} slots compared with the record's — **{len(diffs)} differences**" + (f" ({diffs[:5]})" if diffs else "") +
            f"; the closure tally **{len(bm_d)} differences**" + (f" (seeds {bm_d[:4]})" if bm_d else "") + f"; the pair tally **{len(pm_d)} differences**" + (f" (seeds {pm_d[:5]})" if pm_d else "") +
            "; the new columns (`ra_json`, ρ, the marks, the overhead's terms, the second filing's counters) are not in the record and are compared apart.")
CHK = []
def chk(ok, text): CHK.append(f"- {'MET' if ok else 'MISSED'} — {text}")
def in_band(x, lo, hi): return (not np.isnan(x)) and lo <= x <= hi
def paired(A, B, k, kb=None):
    kb = kb or k; A_, B_ = {r["seed"]: r for r in A}, {r["seed"]: r for r in B}; sd = sorted(set(A_) & set(B_)); return mse([B_[s][kb] - A_[s][k] for s in sd]), np.mean([A_[s][k] for s in sd]), np.mean([B_[s][kb] for s in sd]), len(sd)
def two_se(dd): return (not np.isnan(dd[1])) and dd[1] > 0 and abs(dd[0]) > 2 * dd[1]
def verdict(text, shown, refuted): return f"- {text} **{'Shown' if shown else ('Refuted' if refuted else 'Neither')}.**"
# ------------------------------------------------------------------ the record
CW3o = load([f"{D26}/rerun/cw3-s21-70", f"{D26}/rerun/cw3-s71-120"], "careful")[1]; CW3 = load([f"{D27}/rerun/cw3-s21-70", f"{D27}/rerun/cw3-s71-120"], "careful")[1] or CW3o
R38o = load([f"{D26}/r38/s21-70", f"{D26}/r38/s71-120"], "mix:caseM0.2p0:0.25")[0]; R39o = load([f"{D26}/r39/s21-70", f"{D26}/r39/s71-120"], "mix:caseM0.2p0:0.75")[0]; R40o = load([f"{D26}/r40/s21-70", f"{D26}/r40/s71-120"], "mix:caseM0.2p0:1.0")[0]
R38 = load([f"{D27}/rerun/r38-s21-70", f"{D27}/rerun/r38-s71-120"], "mix:caseM0.2p0:0.25")[0] or R38o; R39 = load([f"{D27}/rerun/r39-s21-70", f"{D27}/rerun/r39-s71-120"], "mix:caseM0.2p0:0.75")[0] or R39o; R40 = load([f"{D27}/rerun/r40-s21-70", f"{D27}/rerun/r40-s71-120"], "mix:caseM0.2p0:1.0")[0] or R40o
R26 = load([f"{D22}/r26/s21-70", f"{D22}/r26/s71-120"], "mix:caseM0.2:1.0")[0]; R29 = load([f"{D25}/rerun/r29-s21-70", f"{D25}/rerun/r29-s71-120"], "mix:caseM0.2:0.75")[0]; R19 = load([f"{D22}/rerun/r19-s21-70", f"{D22}/rerun/r19-s71-120"], "mix:doseM0.2:0.25")[0]
R16 = load([f"{D18}/r16/s21-70", f"{D18}/r16/s71-120"], "mix:doseM1.0:0.25")[0]; R15 = load([f"{D18}/r15/s21-70", f"{D18}/r15/s71-120"], "mix:doseM0.5:0.25")[0]; R37 = load([f"{D26}/r37/s21-70", f"{D26}/r37/s71-120"], "mix:caseM0.1p0.98:0.25")[0]
R41 = load([f"{D27}/r41/s21-70", f"{D27}/r41/s71-120"], "mix:caseM0.5p0:0.25")[0]; R42 = load([f"{D27}/r42/s21-70", f"{D27}/r42/s71-120"], "mix:caseM1.0p0:0.25")[0]
R43 = load([f"{D27}/r43/s21-70", f"{D27}/r43/s71-120"], "careful")[1]; R44 = load([f"{D27}/r44/s21-70", f"{D27}/r44/s71-120"], "mix:caseM0.2p0:0.25")[0]; R45 = load([f"{D27}/r45/s21-70", f"{D27}/r45/s71-120"], "mix:caseM0.2p0:1.0")[0]
R46 = load([f"{D27}/r46/s21-70", f"{D27}/r46/s71-120"], "mix:caseM0.2p0:1.0")[0]; R46a = load([f"{D27}/r46a/s21-70", f"{D27}/r46a/s71-120"], "mix:caseM0.2p0:1.0")[0]; R47 = load([f"{D27}/r47/s21-70", f"{D27}/r47/s71-120"], "careful")[1]
L = ["# Addendum 31 — a second look alone, the mark for a miss on real work, and the buyer's complaint on the ruled road: reads 41 to 47 (November 18, 2026; notes §126)\n"]
if CW3 is not CW3o and CW3o: L.append(repro(list(CW3.values()), list(CW3o.values()), "world 3's all-careful run again whole at 29cffb7c7 (a26/rerun/cw3 at a4fc4f6c4)"))
for nm, N_, O_ in (("read 38", R38, R38o), ("read 39", R39, R39o), ("read 40", R40, R40o)):
    if N_ is not O_ and O_: L.append(repro(N_, O_, f"{nm} run again whole at 29cffb7c7 (a26 at a4fc4f6c4)"))
L.append(f"\nLoaded: cw3 {len(CW3)} (record {len(CW3o)}), r38 {len(R38)}, r39 {len(R39)}, r40 {len(R40)}, r26 {len(R26)}, r29 {len(R29)}, r19 {len(R19)}, r16 {len(R16)}, r15 {len(R15)}, r37 {len(R37)}; r41 {len(R41)}, r42 {len(R42)}, r43 {len(R43)}, r44 {len(R44)}, r45 {len(R45)}, r46 {len(R46)}, r46a {len(R46a)}, r47 {len(R47)} episodes.\n")
Q38 = rows_of(R38, CW3); Q39 = rows_of(R39, CW3); P40 = pop_rows(R40, CW3); Q41 = rows_of(R41, CW3); Q42 = rows_of(R42, CW3); Q19 = rows_of(R19, CW3); Q16 = rows_of(R16, CW3); Q15 = rows_of(R15, CW3); Q37 = rows_of(R37, CW3)
P43 = pop_rows(list(R43.values()), CW3); Q44 = rows_of(R44, CW3); P45 = pop_rows(R45, CW3); P45v40 = pop_rows(R45, D(R40)); P45v43 = pop_rows(R45, R43); P46 = pop_rows(R46, CW3); P46v40 = pop_rows(R46, D(R40)); P46a = pop_rows(R46a, CW3); P46av40 = pop_rows(R46a, D(R40)); P47 = pop_rows(list(R47.values()), CW3)
P26 = pop_rows(R26, CW3); P40o = pop_rows(R40o, CW3)
# ------------------------------------------------------------------ 1. AK4 / AL7: asked from the record
L += ["## 1. Asked from the record (AK4, AL7)\n"]
# 1.1 the window the award reads in read 38
if Q38:
    L += ["**AK4.1 — the window that the award reads, in read 38** (the rerun at 29cffb7c7: ρ over a slot's member ticks and at the end — the exit's for a departed slot; the awards won in a life; the income from work, real, every event of the `delivery` class at the slot's standing). The conduct's slots against the careful beside them, by seed:\n",
          "| measure | conduct | careful beside | **conduct − careful** (SE) |", "|---|---|---|---|"]
    for k, lab, d_ in (("rho_m", "ρ over the member ticks", 3), ("rho_end", "ρ at the end", 3), ("awards", "awards won in a life", 1), ("work", "income from work in a life, real", 0), ("rvm", "reviews as a member", 1), ("fover", "wrong first approvals overturned a slot", 2), ("bonds", "bonds forfeited in a life (nominal)", 1), ("susp", "suspensions a slot", 2), ("dep", "departed within the run", 2), ("good", "good ticks", 0)):
        dd = mse(col(Q38, k) - col(Q38, k + "c")); L.append(f"| {lab} | {np.nanmean(col(Q38, k)):.{d_}f} | {np.nanmean(col(Q38, k + 'c')):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    for nm, Q in (("read 41", Q41), ("read 42", Q42), ("read 44", Q44)):
        if Q:
            L.append(f"| *{nm}: ρ over the member ticks* | {np.nanmean(col(Q, 'rho_m')):.3f} | {np.nanmean(col(Q, 'rho_mc')):.3f} | {pm(mse(col(Q, 'rho_m') - col(Q, 'rho_mc')), 3)} |")
            L.append(f"| *{nm}: awards won* | {np.nanmean(col(Q, 'awards')):.1f} | {np.nanmean(col(Q, 'awardsc')):.1f} | {pm(mse(col(Q, 'awards') - col(Q, 'awardsc')), 1)} |")
            L.append(f"| *{nm}: income from work, real* | {np.nanmean(col(Q, 'work')):.0f} | {np.nanmean(col(Q, 'workc')):.0f} | {pm(mse(col(Q, 'work') - col(Q, 'workc')), 0)} |")
# 1.3 whose second look overturns
L += ["\n**AK4.3 — whose second look overturns.** Every first approval of a member's real delivery at its closure, by who looked at it again (a member's audit seat; the state's; a dispute panel with no audit; nobody) and whether the approval ended overturned — the truth beside (`ra_json`; the two counts ELEF can keep with no knowledge of any model: of the first approvals a member's audit looked at, the share overturned, and the same for the state's). The cell's buyers do not dispute, so the panel column is empty before read 46.\n",
      "| population | first approvals a run | **looked at by a member: n; overturned (share)** | of them bad: n; overturned | good: n; overturned | **by the state: n; overturned (share)** | bad: n; overturned | good: n; overturned | by a dispute panel: n; overturned | never looked at: n; bad among them |", "|---|---|---|---|---|---|---|---|---|---|"]
def ra_row(nm, E):
    Rr = [raj(e) for e in E]
    if not Rr or not any(Rr): return None
    g = g_of(Rr); tot = g("member_n") + g("state_n") + g("panel_n") + g("never_n")
    sh = lambda a, b: f"{g(a):.0f}; {g(b):.1f} ({g(b) / g(a):.3f})" if g(a) else "—"
    return f"| {nm} | {tot:.0f} | **{sh('member_n', 'member_over')}** | {sh('member_bad_n', 'member_bad_over')} | {sh('member_good_n', 'member_good_over')} | **{sh('state_n', 'state_over')}** | {sh('state_bad_n', 'state_bad_over')} | {sh('state_good_n', 'state_good_over')} | {sh('panel_n', 'panel_over')} | {g('never_n'):.0f}; {g('never_bad_n'):.1f} |"
for nm, E in (("world 3's all-careful", list(CW3.values())), ("read 38 (cell B on 1 in 4)", R38), ("read 39 (3 in 4)", R39), ("read 40 (every slot)", R40), ("read 41 (0.5 on 1 in 4)", R41), ("read 42 (1.0 on 1 in 4)", R42), ("read 43 (all-careful, the mark)", list(R43.values())), ("read 44 (cell B 1 in 4, the mark)", R44), ("read 45 (every slot, the mark)", R45),
               ("read 46 (every slot, disputes, second filing)", R46), ("read 46a (disputes, no second filing)", R46a), ("read 47 (all-careful, disputes, second filing)", list(R47.values()))):
    row = ra_row(nm, E)
    if row: L.append(row)
# 1.4 who gives the first review
L += ["\n**AK4.4 — who gives the first review of a bad delivery**, and what moves it. The share of a member's real bad deliveries first reviewed by a member, a probationer or the state (the closure tally), beside the members' ticks without their earned seats, the probationers' share of all reviews and the audit seats a slot:\n",
      "| population | bad deliveries a run | **first by a member** | by a probationer | by the state | member ticks without the earned seats | probationers' share of all reviews | audit seats a slot | the state's share of the audit seats |", "|---|---|---|---|---|---|---|---|---|"]
for nm, E in (("world 3's all-careful", list(CW3.values())), ("read 26 (caseM0.2 on every slot)", R26), ("read 29 (caseM0.2 on 3 in 4)", R29), ("read 39", R39), ("read 40", R40), ("read 45 (the mark)", R45), ("read 43 (all-careful, the mark)", list(R43.values()))):
    if not E: continue
    d = fa_split(E); S_ = [stats_(slots(e)) for e in E]; ss = np.nanmean([state_share(e)["audit"] for e in E])
    rv_p = np.mean([sum(v.get("rv_probation", 0) for v in slots(e)) / max(1, sum(v.get("rv_probation", 0) + v.get("rv_member", 0) for v in slots(e))) for e in E])
    L.append(f"| {nm} | {d['tot']:.0f} | **{d['fm']:.3f}** | {d['fp']:.3f} | {d['fs']:.3f} | {np.mean([s['noseat'] for s in S_]):.3f} | {rv_p:.3f} | {np.mean([s['aud'] for s in S_]):.1f} | {ss:.3f} |")
# 1.5 the overhead's terms
L += ["\n**AK4.5 — the overhead's terms.** The system overhead a vested task is five terms over the vested real roots (`sys_overhead_per_vested`): the care bought on real cases, the care on planted cases, the troops' review cost, the cost of truth (the plants' pots minted less what returned) and the plants' own awarded price (their shadow cost) — nominal credits a vested task. Read 40 against world 3's all-careful, by seed; the other reads beside:\n",
      "| population | vested real roots | care on real cases | care on planted | troops' review cost | cost of truth | plants' price | **overhead a vested task** | P_t at the end | awards a run | the members' mean price |", "|---|---|---|---|---|---|---|---|---|---|---|"]
def oh_row(nm, E):
    if not E or np.isnan(np.nanmean([f(e, "care_cost_real") for e in E])): return None
    nv = np.mean([f(e, "vested_real_roots") for e in E]); t = lambda k: np.mean([f(e, k) for e in E]) / nv
    return f"| {nm} | {nv:.0f} | {t('care_cost_real'):.2f} | {t('care_cost_plant'):.2f} | {t('troop_review_cost'):.2f} | {t('cost_of_truth'):.2f} | {t('plant_price_sum'):.2f} | **{np.mean([f(e, 'sys_overhead_per_vested') for e in E]):.2f}** | {np.mean([f(e, 'P_t') for e in E]):.2f} | {np.mean([f(e, 'awarded') for e in E]):.0f} | {np.mean([f(e, 'member_price_mean') for e in E]):.2f} |"
for nm, E in (("world 3's all-careful", list(CW3.values())), ("read 38", R38), ("read 39", R39), ("read 40", R40), ("read 41", R41), ("read 42", R42), ("read 43", list(R43.values())), ("read 44", R44), ("read 45", R45), ("read 46", R46), ("read 46a", R46a), ("read 47", list(R47.values()))):
    row = oh_row(nm, E)
    if row: L.append(row)
if P40 and not np.isnan(np.nanmean(col(P40, "w_care_r"))):
    L.append("\nRead 40 less world 3's all-careful by seed, a vested task: " + "; ".join(f"{lab} {pm(mse((col(P40, 'w_' + k) - col(P40, 'w0_' + k)) / col(P40, 'w0_nv')), 3)}" for k, lab in (("care_r", "care on real"), ("care_p", "care on planted"), ("troopc", "troops' cost"), ("cot", "cost of truth"), ("pprice", "plants' price"))) +
             f"; the overhead {pm(mse(col(P40, 'w_oh') - col(P40, 'w0_oh')), 3)}; vested roots {pm(mse(col(P40, 'w_nv') - col(P40, 'w0_nv')), 1)}; P_t {pm(mse(col(P40, 'w_Pt') - col(P40, 'w0_Pt')), 2)}.\n")
# 1.6 / 1.7 / AL7
if R37:
    num = [sum(v.get(f"pwg_member_{s}", 0) for v in groups(e)["claim"] for s in SEATS) for e in R37]; den = [sum(v.get(f"rvm_plant_good_{s}", 0) for v in groups(e)["claim"] for s in SEATS) for e in R37]
    numc = [sum(v.get(f"pwg_member_{s}", 0) for v in groups(e)["care"] for s in SEATS) for e in R37]; denc = [sum(v.get(f"rvm_plant_good_{s}", 0) for v in groups(e)["care"] for s in SEATS) for e in R37]
    byseat = {s: (sum(v.get(f"pwg_member_{s}", 0) for e in R37 for v in groups(e)["claim"]), sum(v.get(f"rvm_plant_good_{s}", 0) for e in R37 for v in groups(e)["claim"])) for s in SEATS}
    L.append(f"**AK4.7 — read 37's planted good cases rejected.** The conduct's slots reject {pm(ratio_se(num, den), 4)} of the planted good cases they meet as a member ({np.mean(den):.1f} a run on 1 slot in 4), the careful beside them {pm(ratio_se(numc, denc), 4)} ({np.mean(denc):.0f} a run); by seat the conduct's: " +
             ", ".join(f"{s} {a}/{b} = {a / b:.3f}" for s, (a, b) in byseat.items() if b) + f". The identity's figure for a conduct at a dose of 0.1 on planted good cases (0.9 × a careful review's 0.05) is 0.045: the read is {(ratio_se(num, den)[0] - 0.045) / ratio_se(num, den)[1]:.1f} SE above it and {(ratio_se(num, den)[0] - ratio_se(numc, denc)[0]) / math.hypot(ratio_se(num, den)[1], ratio_se(numc, denc)[1]):.1f} SE above the careful's. Read 38's conduct, at a dose of 0.2, rejects " +
             (f"{pm(ratio_se([sum(v.get(f'pwg_member_{s}', 0) for v in groups(e)['claim'] for s in SEATS) for e in R38], [sum(v.get(f'rvm_plant_good_{s}', 0) for v in groups(e)['claim'] for s in SEATS) for e in R38]), 4)}" if R38 else "—") + " (the identity's 0.040).\n")
if P40:
    dd = mse(col(P40, "reach") - col(P40, "reachc")); L.append(f"**AL7 — read 40's slots suspended at least once, against world 3's all-careful by seed**: {np.mean(col(P40, 'reach')):.3f} against {np.mean(col(P40, 'reachc')):.3f}, **{dd[0]:+.3f} ± {dd[1]:.3f}** ({se_(dd)} SE); suspensions a slot {np.mean(col(P40, 'susp')):.3f} against {np.mean(col(P40, 'suspc')):.3f}; the world's suspensions a run {np.mean(col(P40, 'w_susp')):.1f} against {np.mean(col(P40, 'w0_susp')):.1f} ({pm(mse(col(P40, 'w_susp') - col(P40, 'w0_susp')), 2)}).\n")
# ------------------------------------------------------------------ 2. reads 41 and 42
HDR = ["| read | seeds | slots a seed: conduct / careful beside | **careful − conduct, of record** (SE) | temptation | with the reservation | like for like | **level saving: of record / with the reservation / like for like** | care a slot: conduct / careful | claims a slot (as a member; share of its member reviews) | suspended ≥ 1: conduct / careful | departed: conduct / careful | member reviews in a life: conduct / careful | audit seats: conduct / careful | wrong planted verdicts as a member: conduct / careful | leak ‰ | FA | overhead |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def qrow(nm, Q):
    a, b, c = mse(col(Q, "rec")), mse(col(Q, "res")), mse(col(Q, "lfl")); x = xs(Q); t_ = temp(Q, "rec", "ben")
    return (f"| {nm} | {len(Q)} | {np.mean(col(Q, 'n')):.1f} / {np.mean(col(Q, 'nc')):.1f} | **{a[0]:+.0f} ± {a[1]:.0f}** ({se_(a)}) | {t_[0]:.1f} | {b[0]:+.0f} ± {b[1]:.0f} | {c[0]:+.0f} ± {c[1]:.0f} | **{pm(x[0], 2)} / {pm(x[1], 2)} / {pm(x[2], 2)}** | {np.mean(col(Q, 'call')):.0f} / {np.mean(col(Q, 'carec')):.0f} | {np.mean(col(Q, 'claims')):.1f} ({np.mean(col(Q, 'claims_m')) / max(1e-9, np.mean(col(Q, 'rvm'))):.3f}) | "
            f"{np.mean(col(Q, 'reach')):.3f} / {np.mean(col(Q, 'reachc')):.3f} | {np.mean(col(Q, 'dep')):.2f} / {np.mean(col(Q, 'depc')):.2f} | {np.mean(col(Q, 'rvm')):.1f} / {np.mean(col(Q, 'rvmc')):.1f} | {np.mean(col(Q, 'aud')):.1f} / {np.mean(col(Q, 'audc')):.1f} | {np.mean(col(Q, 'pw')):.2f} / {np.mean(col(Q, 'pwc')):.2f} | {np.mean(col(Q, 'w_leak')):.1f} | {np.mean(col(Q, 'w_fa')):.1f} | {np.mean(col(Q, 'w_oh')):.2f} |")
L += ["## 2. Reads 41 and 42: a second look alone, on 1 slot in 4 (cell B at a dose of 0.5 and of 1 on real cases; world 3's cell, seeds 21–120)\n",
      "`caseM0.5p0` and `caseM1.0p0`: the conduct passes ELEF's tests as a careful review does (no claim on a planted bad case; a planted good case as a real one) and claims on real cases at the dose — read 42's member reads no real case. Read as read 38 was; beside them read 38 (0.2) and the reads of record with the tests seeing the model (15 at 0.5, 16 at 1.0, 19 at 0.2).\n"] + HDR
for nm, Q in (("**41: cell B at 0.5 on 1 in 4**", Q41), ("**42: cell B at 1.0 on 1 in 4**", Q42), ("38: cell B at 0.2 on 1 in 4 (the record)", Q38), ("15: M at 0.5 on 1 in 4 (the record)", Q15), ("16: M at 1.0 on 1 in 4 (the record)", Q16), ("19: M at 0.2 on 1 in 4 (the record)", Q19)):
    if Q: L.append(qrow(nm, Q))
L += ["\n**The planted record beside the careful's, by seed** (the reviewer's expectation: within two standard errors on the wrong planted verdicts as a member and on the slots suspended at least once):\n",
      "| read | wrong planted verdicts as a member: conduct / careful; **difference** | planted bad met: conduct / careful | wrong on planted bad (share): conduct / careful | suspended at least once: conduct / careful; **difference** | member ticks without the earned seats: conduct / careful | audit seats: **difference** |", "|---|---|---|---|---|---|---|"]
for nm, Q in (("41", Q41), ("42", Q42), ("38", Q38), ("44", Q44)):
    if not Q: continue
    dpw = mse(col(Q, "pw") - col(Q, "pwc")); drh = mse(col(Q, "reach") - col(Q, "reachc")); da = mse(col(Q, "aud") - col(Q, "audc"))
    L.append(f"| {nm} | {np.mean(col(Q, 'pw')):.2f} / {np.mean(col(Q, 'pwc')):.2f}; **{dpw[0]:+.3f} ± {dpw[1]:.3f}** | {np.mean(col(Q, 'pb_met')):.1f} / {np.mean(col(Q, 'pb_metc')):.1f} | {np.nanmean(col(Q, 'pwb_share')):.3f} / {np.nanmean(col(Q, 'pwb_sharec')):.3f} | {np.mean(col(Q, 'reach')):.3f} / {np.mean(col(Q, 'reachc')):.3f}; **{drh[0]:+.3f} ± {drh[1]:.3f}** | {np.nanmean(col(Q, 'noseat')):.3f} / {np.nanmean(col(Q, 'noseatc')):.3f} | {da[0]:+.1f} ± {da[1]:.1f} |")
L += ["\n**The claims on real bad work at the first review, and what became of them** (the closure tally; the conduct's slots):\n",
      "| read | claims a run | stay paid | never audited | confirmed by a member's audit | by the state's audit | by a dispute panel | overturned after a member's audit | after the state's | after a dispute panel (of them after a second filing) | the careful's own wrong first approvals a run; overturned | leak ‰ | standing FA |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def fa_row(nm, E):
    if not E: return None
    d = fa_split(E); return f"| {nm} | {d['claims']:.1f} | **{d['paid']:.3f}** | {d['none']:.3f} | {d['mconf']:.3f} | {d['sconf']:.3f} | {d['pconf']:.3f} | {d['mdiff']:.3f} | {d['sdiff']:.3f} | {d['pan']:.3f} ({d['pan2']:.3f}) | {d['care']:.1f}; {d['care_over']:.3f} | {np.mean([1000 * f(e, 'leak_bad') for e in E]):.1f} | {np.mean([f(e, 'false_approvals') for e in E]):.1f} |"
for nm, E in (("**41**", R41), ("**42**", R42), ("38", R38), ("39", R39), ("40", R40), ("**44** (the mark)", R44), ("**45** (the mark)", R45), ("**46** (disputes, second filing)", R46), ("**46a** (disputes alone)", R46a), ("15 (record)", R15), ("16 (record)", R16)):
    row = fa_row(nm, E)
    if row: L.append(row)
# the gain's decomposition (as a26 §2 did): care spared, bonds, fees, work
L += ["\n**Where the gain or loss comes from** (the conduct's slots less the careful beside them, real, by seed; the wallet's events by class at every standing, signed as the wallet sees them): the care the claims spare (the private benefit, `claimed_*`), the bonds and court fees, the fees of reviews with the emission and the uplift, the work's side (the delivery price, the effort, the guarantees), the other classes (the care bought and reimbursed, the loan, the float, a departure), the sum of those, the gap of record and the rest (the index's revaluation of the wealth held, in no event):\n",
      "| read | care spared | bonds and court fees | fees, emission, uplift | work | other | sum of the events | **of record (conduct − careful)** | the rest |", "|---|---|---|---|---|---|---|---|---|"]
def evsum(V, cls): return sum(val for v in V for k, val in v.items() if k.startswith("ev_") and k.endswith("_" + cls) and isinstance(val, (int, float))) / len(V)
def evd(a, c, *classes): return sum(evsum(a, k) - evsum(c, k) for k in classes)   # the conduct's wallet events less the careful's, real, signed as the wallet sees them (an outflow negative)
for nm, E in (("41", R41), ("42", R42), ("38", R38), ("44", R44)):
    if not E: continue
    rows = []
    for e in E:
        g = groups(e); a, c = g["claim"], g["care"]
        sp = np.mean([v.get("claimed_member", 0) + v.get("claimed_probation", 0) + v.get("claimed_down", 0) for v in a])
        bd = evd(a, c, "bond", "courtfee"); fe = evd(a, c, "fee", "emission", "uplift"); wk = evd(a, c, "delivery", "effort", "guarantee"); ot = evd(a, c, "care", "reimb", "loan", "float", "departure", "other_in"); rec = np.mean([life(v) for v in a]) - np.mean([life(v) for v in c])
        rows.append((sp, bd, fe, wk, ot, sp + bd + fe + wk + ot, rec))
    rows = np.array(rows); m = lambda i: pm(mse(rows[:, i]), 1)
    L.append(f"| {nm} | {m(0)} | {m(1)} | {m(2)} | {m(3)} | {m(4)} | {m(5)} | **{m(6)}** | {pm(mse(rows[:, 6] - rows[:, 5]), 1)} |")
for nm, E, Cref in (("40 (every slot, against the all-careful by seed)", R40, CW3), ("45 (every slot, the mark; against the all-careful)", R45, CW3), ("46 (every slot, disputes and the second filing; against the all-careful)", R46, CW3)):
    if not E or not Cref: continue
    rows = []
    for e in E:
        s_ = int(e["seed"])
        if s_ not in Cref: continue
        a, c = slots(e), slots(Cref[s_])
        sp = np.mean([v.get("claimed_member", 0) + v.get("claimed_probation", 0) + v.get("claimed_down", 0) for v in a])
        bd = evd(a, c, "bond", "courtfee"); fe = evd(a, c, "fee", "emission", "uplift"); wk = evd(a, c, "delivery", "effort", "guarantee"); ot = evd(a, c, "care", "reimb", "loan", "float", "departure", "other_in"); rec = np.mean([life(v) for v in a]) - np.mean([life(v) for v in c])
        rows.append((sp, bd, fe, wk, ot, sp + bd + fe + wk + ot, rec))
    rows = np.array(rows); m = lambda i: pm(mse(rows[:, i]), 1)
    L.append(f"| {nm} | {m(0)} | {m(1)} | {m(2)} | {m(3)} | {m(4)} | {m(5)} | **{m(6)}** | {pm(mse(rows[:, 6] - rows[:, 5]), 1)} |")
L.append("\n(An outflow is negative: the conduct's extra bonds read negative. The population rows set the population's slot against the all-careful's slot of another world at the same seed, as read 40's 86 of record is. §125's decomposition took the work's side as everything but the care, the bonds and the fees; here it is the three work classes, the rest in `other`.)\n")
# ------------------------------------------------------------------ 3. reads 43 to 45: the mark
L += ["## 3. Reads 43 to 45: the mark for a miss on real work (`--real-miss-mark on`; world 3's cell, seeds 21–120)\n",
      "An approval of a real root that the deciding verdict overturns is entered on its first reviewer's planted record as a wrong verdict on a planted bad case, at any standing, and the record is re-checked as after a plant; nothing else of real work enters. A slot's entries on the record by where they come from: the wrong planted verdicts as a member (`pw_member_*`) and the marks (`marks_real`, the engine's count on the actor). The slots that are at some time without their earned seats by the record: a member tick not panel-eligible beyond the undetermined ones (`ticks_member_noseat − ticks_member_noseat_undet > 0`; the driver's undetermined test counts planted bad cases met, so a young slot barred by marks alone is counted undetermined — an undercount of a few in a hundred at most); beside it the share in the phase after a first wrong planted verdict (`pf_ticks_lost`, which the marks do not move).\n"]
if P43:
    L += ["**Read 43: world 3's all-careful with the mark, against world 3's all-careful by seed.**\n", "| measure | all-careful | **read 43** | **read 43 − all-careful** (SE) |", "|---|---|---|---|"]
    for k, lab, d_ in (("life", "the slot of record, real", 0), ("lres", "with the reservation", 0), ("marks", "marks a slot in a life", 2), ("pw", "wrong planted verdicts as a member a slot", 2), ("fover", "wrong first approvals of real bad work overturned a slot", 2), ("noseat_rec", "slots at some time without the earned seats by the record (share)", 3), ("lost_phase", "slots in the phase after a first wrong planted verdict (share)", 3),
                       ("noseat", "member ticks without the earned seats", 3), ("reach", "slots suspended at least once", 3), ("susp", "suspensions a slot", 3), ("dep", "departed within the run", 3), ("aud", "audit seats a slot", 1), ("good", "good ticks a slot", 0), ("rho_m", "ρ over the member ticks", 3)):
        dd = mse(col(P43, k) - col(P43, k + "c")); L.append(f"| {lab} | {np.nanmean(col(P43, k + 'c')):.{d_}f} | {np.nanmean(col(P43, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    for k, lab, d_ in (("marks", "marks a run", 1), ("leak", "the leak, ‰", 1), ("fa", "standing false approvals a run", 1), ("oh", "the overhead a vested task", 2), ("cot", "the cost of truth", 0), ("susp", "suspensions a run", 1), ("dep", "departures a run", 1), ("Pt", "P_t at the end", 2), ("dec", "deciding verdicts opened", 1)):
        dd = mse(col(P43, "w_" + k) - col(P43, "w0_" + k)); L.append(f"| {lab} | {np.nanmean(col(P43, 'w0_' + k)):.{d_}f} | {np.nanmean(col(P43, 'w_' + k)):.{d_}f} | {dd[0]:+.{d_}f} ± {dd[1]:.{d_}f} ({se_(dd)}) |")
    dd = mse(col(P43, "ss_audit") - col(P43, "ss0_audit")); L.append(f"| the state's share of the audit seats | {np.nanmean(col(P43, 'ss0_audit')):.3f} | {np.nanmean(col(P43, 'ss_audit')):.3f} | **{dd[0]:+.3f} ± {dd[1]:.3f}** ({se_(dd)}) |")
    dd = mse(col(P43, "ss_panel") - col(P43, "ss0_panel")); L.append(f"| the state's share of the panel seats | {np.nanmean(col(P43, 'ss0_panel')):.3f} | {np.nanmean(col(P43, 'ss_panel')):.3f} | {dd[0]:+.3f} ± {dd[1]:.3f} ({se_(dd)}) |")
    for k, lab in (("mirror", "**the mirror: wrong rejections of good work standing a run**"), ("mirror_audit", "of them by the audit road"), ("mirror_state", "of them after the state's audit"), ("appr", "bad deliveries approved at first"), ("over", "stopped before payment"), ("paid", "paid in the end")):
        dd = mse(col(P43, "t_" + k) - col(P43, "t0_" + k)); L.append(f"| {lab} | {np.mean(col(P43, 't0_' + k)):.2f} | {np.mean(col(P43, 't_' + k)):.2f} | **{dd[0]:+.2f} ± {dd[1]:.2f}** ({se_(dd)}) |")
    e43 = mse(col(P43, "marks") + col(P43, "pw")); L.append(f"\nA slot carries **{e43[0]:.2f} ± {e43[1]:.2f}** wrong entries on its record in a life under the mark ({np.mean(col(P43, 'pw')):.2f} planted, {np.mean(col(P43, 'marks')):.2f} marks), where the all-careful's slot carries {np.mean(col(P43, 'pwc')):.2f}.\n")
if Q44:
    L += ["**Read 44: cell B on 1 slot in 4 with the mark** (read as read 38 was; against read 38 by seed).\n"] + HDR + [qrow("**44: cell B at 0.2 on 1 in 4, the mark**", Q44), qrow("38: the same without the mark (the record)", Q38)]
    L += ["\n| measure | read 38 | **read 44** | **44 − 38** (SE) |", "|---|---|---|---|"]
    for k, lab, d_ in (("rec", "careful − conduct, of record", 0), ("res", "with the reservation", 0), ("lfl", "like for like", 0), ("marks", "the conduct's marks a slot", 2), ("marksc", "the careful's marks a slot", 2), ("pw", "the conduct's wrong planted verdicts as a member", 2), ("noseat_rec", "the conduct's slots at some time without the earned seats", 3), ("noseat_recc", "the careful's", 3), ("noseat", "the conduct's member ticks without the earned seats", 3), ("noseatc", "the careful's", 3),
                       ("reach", "the conduct's slots suspended at least once", 3), ("reachc", "the careful's", 3), ("aud", "the conduct's audit seats", 1), ("audc", "the careful's audit seats", 1), ("rvm", "the conduct's member reviews", 1), ("claims", "the conduct's claims a slot", 1), ("w_leak", "the leak ‰", 1), ("w_fa", "standing FA", 1), ("w_oh", "the overhead", 2), ("ss_audit", "the state's share of the audit seats", 3)):
        dd, ma_, mb_, n_ = paired(Q38, Q44, k); L.append(f"| {lab} | {ma_:.{d_}f} | {mb_:.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) |")
    x38, x44 = xs(Q38)[0], xs(Q44)[0]; A_, B_ = {r["seed"]: r for r in Q38}, {r["seed"]: r for r in Q44}; sd = sorted(set(A_) & set(B_))
    dl = mse([(B_[s]["rec"] + B_[s]["ben"]) / B_[s]["call"] - (A_[s]["rec"] + A_[s]["ben"]) / A_[s]["call"] for s in sd]); L.append(f"| the level saving of record | {x38[0]:.2f} | {x44[0]:.2f} | **{dl[0]:+.2f} ± {dl[1]:.2f}** ({se_(dl)}) |")
if P45:
    L += ["\n**Read 45: cell B on every slot with the mark** (read as read 40 was; against read 40 and against read 43 by seed).\n", "| measure | read 40 | read 43 | **read 45** | **45 − 40** (SE) | **45 − 43** (SE) |", "|---|---|---|---|---|---|"]
    for k, lab, d_, kind in (("life", "the slot of record, real", 0, "s"), ("lres", "with the reservation", 0, "s"), ("marks", "marks a slot", 2, "s"), ("pw", "wrong planted verdicts as a member a slot", 2, "s"), ("noseat_rec", "slots at some time without the earned seats by the record", 3, "s"), ("noseat", "member ticks without the earned seats", 3, "s"), ("reach", "slots suspended at least once", 3, "s"), ("aud", "audit seats a slot", 1, "s"), ("claims", "claims a slot", 1, "s"), ("rvm", "member reviews a slot", 1, "s"), ("dep", "departed", 3, "s"),
                             ("w_leak", "**the leak, ‰**", 1, "w"), ("w_fa", "standing false approvals a run", 1, "w"), ("w_oh", "the overhead a vested task", 2, "w"), ("w_cot", "the cost of truth", 0, "w"), ("w_marks", "marks a run", 1, "w"), ("w_susp", "suspensions a run", 1, "w"), ("ss_audit", "**the state's share of the audit seats**", 3, "w"), ("t_appr", "bad deliveries approved at first", 1, "w"), ("t_over", "stopped before payment", 1, "w"), ("t_paid", "paid in the end", 1, "w"), ("t_mirror", "the mirror: wrong rejections standing", 2, "w")):
        d40, m40, m45, _ = paired(P40o if kind == "w" else P40o, P45v40 if True else P45, k if kind == "w" else k, k); d43, m43, _, _ = paired(P43, P45v43, k, k)
        L.append(f"| {lab} | {m40:.{d_}f} | {m43:.{d_}f} | **{m45:.{d_}f}** | **{d40[0]:+.{d_}f} ± {d40[1]:.{d_}f}** ({se_(d40)}) | {d43[0]:+.{d_}f} ± {d43[1]:.{d_}f} ({se_(d43)}) |")
    L.append(f"\nRead 45's population against world 3's all-careful by seed: the slot of record {pm(mse(col(P45, 'life') - col(P45, 'lifec')), 0)}, the level saving {pm(xs(P45)[0], 2)}; read 40's was {pm(mse(col(P40, 'life') - col(P40, 'lifec')), 0)} and {pm(xs(P40)[0], 2)}.\n")
# ------------------------------------------------------------------ 4. reads 46, 46a, 47: the buyer's complaint
L += ["## 4. Reads 46, 46a and 47: the buyer's complaint on the ruled road (`--dispute-policy truthful --dispute-rate 1.0`, with and without `--second-filing on`; world 3's cell, seeds 21–120)\n",
      "How a requester comes to dispute (as the harness has exercised it since run 30): in the tick's challenge pass, the first time it sees its root pending on an approval (the tick after the verdict), before any audit roll, it reads the delivery's truth outside the convention and declared, and disputes where the work truly failed with probability `--dispute-rate` — 1.0 here, every one: the detection is 1. A disputed approval is never rolled for an audit (the dispute's panel takes the challenge round), so in these cells the audit seat audits approvals of good work alone. The plant requester disputes a bad plant's F at the trailing real requesters' rate after their delay (2.8.0), so with the detection at 1 every planted approval is disputed first (§68's fact (iii)) and the planted approvals' audit seat is never reached. The second filing: the party whose filing a panel of two confirmed is asked once, the tick after, and goes on where the truth is on its side, the fee D put down again; a plant's challenge resolves by its truth at the panel and has no second filing.\n",
      "| read | disputes filed a run | won | lost | **second filings** | won (the deciding verdict overturned) | lost (confirmed) | confirmations final at the window's close (no filing) | the party declined | unfunded | deciding verdicts opened | the requesters' court fees put down, real | got back | **the leak ‰** | standing FA | the mirror (wrong rejections standing) | planted approvals disputed | the plant requester's disputes | overhead |", "|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|"]
def disp_row(nm, E):
    if not E: return None
    w = lambda k: np.nanmean([world(e)[k] for e in E]); th = [three(e) for e in E]
    return (f"| {nm} | {w('disp'):.1f} | {w('dwon'):.1f} | {np.nanmean([f(e, 'disputes_lost') for e in E]):.1f} | **{w('sf'):.1f}** | {w('sfw'):.1f} | {w('sfl'):.1f} | {w('lapsed'):.1f} | {w('declined'):.1f} | {w('unf'):.1f} | {w('dec'):.1f} | {w('paidf'):.0f} | {w('backf'):.0f} | **{w('leak'):.1f}** | {w('fa'):.1f} | {np.mean([t['mirror'] for t in th]):.2f} | {w('pa_disp'):.1f} | {w('pdisp'):.1f} | {w('oh'):.2f} |")
for nm, E in (("**46: cell B on every slot, disputes and the second filing**", R46), ("**46a: the same without the second filing**", R46a), ("40: cell B on every slot, no disputes (the record)", R40), ("**47: world 3's all-careful, disputes and the second filing**", list(R47.values())), ("world 3's all-careful (the record)", list(CW3.values()))):
    row = disp_row(nm, E)
    if row: L.append(row)
for nm, Pv, base in (("Read 46 against read 40 by seed", P46v40, "read 40"), ("Read 46a against read 40 by seed", P46av40, "read 40"), ("Read 47 against world 3's all-careful by seed", P47, "the all-careful")):
    if not Pv: continue
    L += [f"\n**{nm}** — the six figures of the reviewer's condition for read 47 (no more than one beyond two standard errors) and the rest:\n", f"| measure | {base} | this | **this − {base}** (SE) | beyond 2 SE |", "|---|---|---|---|---|"]
    n_out = 0
    for k, k0, lab, d_, six in (("life", "lifec", "the slot of record", 0, True), ("w_fa", "w0_fa", "standing false approvals a run", 1, True), ("w_oh", "w0_oh", "the overhead a vested task", 2, True), ("aud", "audc", "audit seats a slot", 1, True), ("ss_audit", "ss0_audit", "the state's share of the audit seats", 3, True), ("reach", "reachc", "slots suspended at least once", 3, True),
                                 ("w_leak", "w0_leak", "**the leak, ‰**", 1, False), ("t_appr", "t0_appr", "bad deliveries approved at first", 1, False), ("t_over", "t0_over", "stopped before payment", 1, False), ("t_paid", "t0_paid", "paid in the end", 1, False), ("t_mirror", "t0_mirror", "the mirror: wrong rejections of good work standing", 2, False), ("w_cot", "w0_cot", "the cost of truth", 0, False), ("good", "goodc", "good ticks a slot", 0, False), ("w_dep", "w0_dep", "departures a run", 1, False), ("w_Pt", "w0_Pt", "P_t at the end", 2, False), ("ss_panel", "ss0_panel", "the state's share of the panel seats", 3, False)):
        dd = mse(col(Pv, k) - col(Pv, k0)); out = two_se(dd); n_out += out if six else 0
        L.append(f"| {lab} | {np.nanmean(col(Pv, k0)):.{d_}f} | {np.nanmean(col(Pv, k)):.{d_}f} | **{dd[0]:+.{d_}f} ± {dd[1]:.{d_}f}** ({se_(dd)}) | {('yes' if out else 'no') if six else ''} |")
    L.append(f"\nFigures of the six beyond two standard errors: **{n_out}**.\n")
    if Pv is P47: SIX47 = n_out
# ------------------------------------------------------------------ 5. AL4 for every read: how often a slot is looked at
L += ["## 5. AL4 for every read\n", "**AL4.1 — how often a slot is looked at.** For each kind of slot: of its first approvals of real work (as a member or a probationer), the number that got an audit by a member and by the state, a dispute panel, or nobody; the entries the mark writes beside (reads 43–45). A slot's figures in a life, the conduct's slots and the careful beside them where the cell has both:\n",
      "| read | slot kind | slots | first approvals of real work a slot | **by a member: n (share)** | **by the state: n (share)** | by a dispute panel | never looked at | overturned: after a member's / the state's / a panel's | **marks a slot** | wrong planted verdicts as a member |", "|---|---|---|---|---|---|---|---|---|---|---|"]
def al_row(nm, kind, S_):
    fr = S_["ra_first"] or np.nan
    return f"| {nm} | {kind} | {S_['n']} | {S_['ra_first']:.1f} | **{S_['ra_member']:.1f} ({S_['ra_member'] / fr:.3f})** | **{S_['ra_state']:.1f} ({S_['ra_state'] / fr:.3f})** | {S_['ra_panel']:.1f} | {S_['ra_never']:.1f} | {S_['ra_over_member']:.2f} / {S_['ra_over_state']:.2f} / {S_['ra_over_panel']:.2f} | **{S_['marks']:.2f}** | {S_['pw']:.2f} |"
for nm, E, mixed in (("all-careful", list(CW3.values()), False), ("38", R38, True), ("39", R39, True), ("40", R40, False), ("41", R41, True), ("42", R42, True), ("43", list(R43.values()), False), ("44", R44, True), ("45", R45, False), ("46", R46, False), ("46a", R46a, False), ("47", list(R47.values()), False)):
    if not E or not any(raj(e) for e in E): continue
    if mixed:
        V = [v for e in E for v in groups(e)["claim"]]; Vc = [v for e in E for v in groups(e)["care"]]; S1, S2 = stats_(V), stats_(Vc); S1["n"], S2["n"] = round(len(V) / len(E), 1), round(len(Vc) / len(E), 1)
        L.append(al_row(nm, "the conduct", S1)); L.append(al_row(nm, "the careful beside", S2))
    else:
        V = [v for e in E for v in slots(e)]; S1 = stats_(V); S1["n"] = round(len(V) / len(E), 1); L.append(al_row(nm, "every slot", S1))
L += ["\n**AL4.2 and AL4.3 — the three counts in one row, and the mirror.** Of a member's real bad deliveries: approved at first (any first reviewer), stopped before payment, paid in the end; the leak is the last over all bad deliveries. The mirror: of the good deliveries, the wrong rejections that stand (the final-N tally of good work by the engine's reason), of them by the audit road and after the state's audit.\n",
      "| read | bad deliveries a run | **approved at first** | **stopped before payment** | **paid in the end** | leak ‰ | **wrong rejections of good work standing** | by the audit road | after the state's audit |", "|---|---|---|---|---|---|---|---|---|"]
for nm, E in (("all-careful", list(CW3.values())), ("38", R38), ("39", R39), ("40", R40), ("41", R41), ("42", R42), ("43 (the mark)", list(R43.values())), ("44", R44), ("45", R45), ("46 (disputes, second filing)", R46), ("46a", R46a), ("47", list(R47.values()))):
    if not E: continue
    th = [three(e) for e in E]; m = lambda k: np.mean([t[k] for t in th])
    L.append(f"| {nm} | {np.mean([f(e, 'bad_deliveries') for e in E]):.0f} | **{m('appr'):.1f}** | **{m('over'):.1f}** | **{m('paid'):.1f}** | {np.mean([1000 * f(e, 'leak_bad') for e in E]):.1f} | **{m('mirror'):.2f}** | {m('mirror_audit'):.2f} | {m('mirror_state'):.2f} |")
L.append("\n(AL4.4, the overhead's terms for every read, is the table of §1 above.)\n")
# ------------------------------------------------------------------ 6. the expectations and the conditions
L += ["## 6. Against the expectations stated before the run, and the conditions\n"]
if Q41:
    x = xs(Q41)[0]; a = mse(col(Q41, "rec")); d = fa_split(R41); cm = np.mean(col(Q41, "claims_m")) / np.mean(col(Q41, "rvm"))
    chk(in_band(cm, 0.40, 0.48), f"read 41: the conduct claims at 0.44 of its reviews as a member — read {cm:.3f}"); chk(in_band(d["claims"], 36, 46), f"read 41: 36 to 46 claims a run on real bad work at the first review — {d['claims']:.1f}"); chk(in_band(d["paid"], 0.20, 0.32), f"read 41: 0.20 to 0.32 of them stay paid — {d['paid']:.3f}")
    chk(in_band(-a[0], -200, 100), f"read 41: the conduct's slot between 100 ahead and 200 behind of record — {-a[0]:+.0f} (ahead positive)"); chk(in_band(x[0], 0.05, 1.25), f"read 41: level saving 0.05 to 1.25 — {x[0]:.2f}"); chk(in_band(np.mean(col(Q41, "w_leak")), 20, 32), f"read 41: leak 20 to 32 ‰ — {np.mean(col(Q41, 'w_leak')):.1f}")
    dpw = mse(col(Q41, "pw") - col(Q41, "pwc")); drh = mse(col(Q41, "reach") - col(Q41, "reachc")); chk(not two_se(dpw) and not two_se(drh), f"read 41: the planted record a careful slot's (wrong planted verdicts {dpw[0]:+.3f} ± {dpw[1]:.3f}; suspended at least once {drh[0]:+.3f} ± {drh[1]:.3f}, neither beyond 2 SE)")
    V41 = verdict("A second look alone holds a member that passes every test and skips at every second real case (read 41's level saving above 0.9 by two standard errors: shown; under 0.9 at the point value: refuted)", x[0] - 2 * x[1] > 0.9, x[0] < 0.9)
if Q42:
    x = xs(Q42)[0]; a = mse(col(Q42, "rec")); d = fa_split(R42); cm = np.mean(col(Q42, "claims_m")) / np.mean(col(Q42, "rvm"))
    chk(in_band(cm, 0.88, 0.89), f"read 42: the conduct claims at 0.88 to 0.89 of its reviews as a member — {cm:.3f}"); chk(in_band(d["claims"], 72, 92), f"read 42: 72 to 92 claims a run — {d['claims']:.1f}"); chk(in_band(d["paid"], 0.20, 0.32), f"read 42: 0.20 to 0.32 stay paid — {d['paid']:.3f}")
    chk(in_band(-a[0], -500, 200), f"read 42: between 200 ahead and 500 behind — {-a[0]:+.0f}"); chk(in_band(x[0], 0.1, 2.9), f"read 42: level saving 0.1 to 2.9 — {x[0]:.2f}"); chk(in_band(np.mean(col(Q42, "w_leak")), 36, 56), f"read 42: leak 36 to 56 ‰ — {np.mean(col(Q42, 'w_leak')):.1f}")
    dpw = mse(col(Q42, "pw") - col(Q42, "pwc")); drh = mse(col(Q42, "reach") - col(Q42, "reachc")); chk(not two_se(dpw) and not two_se(drh), f"read 42: the planted record a careful slot's ({dpw[0]:+.3f} ± {dpw[1]:.3f}; {drh[0]:+.3f} ± {drh[1]:.3f})")
    V42 = verdict("A second look alone holds a member that passes every test and reads no real case (read 42's level saving)", x[0] - 2 * x[1] > 0.9, x[0] < 0.9)
if P43:
    e43 = np.mean(col(P43, "marks") + col(P43, "pw")); ns = np.mean(col(P43, "noseat_rec")); ss = np.mean(col(P43, "ss_audit")); dl = mse(col(P43, "life") - col(P43, "lifec")); dm = mse(col(P43, "t_mirror") - col(P43, "t0_mirror"))
    chk(in_band(round(e43, 1), 1.0, 1.3), f"read 43: a slot carries 1.0 to 1.3 wrong entries on its record in a life — {e43:.2f} (planted {np.mean(col(P43, 'pw')):.2f} + marks {np.mean(col(P43, 'marks')):.2f})"); chk(in_band(100 * ns, 36, 52), f"read 43: 36 to 52 slots in 100 at some time without their earned seats by the record — {100 * ns:.0f} (the phase after a planted failure {100 * np.mean(col(P43, 'lost_phase')):.0f})")
    chk(in_band(ss, 0.36, 0.46), f"read 43: the state holds 0.36 to 0.46 of the audit seats — {ss:.3f}"); chk(in_band(-dl[0], 25, 90), f"read 43: the slot ends 25 to 90 real under the all-careful's — {-dl[0]:+.0f} ± {dl[1]:.0f} under")
    chk(in_band(np.mean(col(P43, "t_mirror")), 5.7, 6.6), f"read 43 (AL4's mirror): 5.7 to 6.6 wrong rejections of good work stand a run — {np.mean(col(P43, 't_mirror')):.2f} (the all-careful {np.mean(col(P43, 't0_mirror')):.2f}; {dm[0]:+.2f} ± {dm[1]:.2f} by seed)")
    V43m = verdict("The mark costs good work as well as careful reviewers (AL4: refuted if read 43 has no more wrong rejections of good work standing than the all-careful by two standard errors, by seed)", dm[0] - 2 * dm[1] > 0, dm[0] + 2 * dm[1] <= 0 or (dm[0] <= 0))
if Q44:
    x = xs(Q44)[0]; a = mse(col(Q44, "rec"))
    chk(in_band(a[0], 30, 230), f"read 44: the conduct's slot 30 to 230 real behind the careful beside it — {a[0]:+.0f} ± {a[1]:.0f} behind"); chk(in_band(x[0], 0.3, 1.1), f"read 44: level saving 0.3 to 1.1 (the point value 0.6) — {x[0]:.2f}")
    V44 = verdict("A mark for a miss on real work holds one member that the planted cases do not see, among careful ones (read 44's level saving above 0.9 by two SE: shown; under 0.9 at the point value: refuted)", x[0] - 2 * x[1] > 0.9, x[0] < 0.9)
if P45v40:
    lk = np.mean(col(P45v40, "w_leak")); ss = np.mean(col(P45v40, "ss_audit")); dl43 = paired(P43, P45v43, "life")[0]; dlk = mse(col(P45v40, "w_leak") - col(P45v40, "w0_leak"))
    chk(in_band(lk, 60, 85), f"read 45: leak 60 to 85 ‰ — {lk:.1f} (read 40's {np.mean(col(P45v40, 'w0_leak')):.1f}; {dlk[0]:+.1f} ± {dlk[1]:.1f} by seed)"); chk(in_band(ss, 0.40, 0.55), f"read 45: the state holds 0.40 to 0.55 of the audit seats — {ss:.3f}"); chk(in_band(abs(dl43[0]), 0, 60), f"read 45: the population's slot within 60 real of read 43's — {dl43[0]:+.0f} ± {dl43[1]:.0f}")
    V45 = verdict("With the mark the buyers get less bad work paid where every member is such a member (read 45's leak under read 40's by two SE, by seed: shown; at or over it at the point value: refuted)", dlk[0] + 2 * dlk[1] < 0, dlk[0] >= 0)
if P46v40:
    lk = np.mean(col(P46v40, "w_leak")); d46 = fa_split(R46); dlk = mse(col(P46v40, "w_leak") - col(P46v40, "w0_leak")); sf = np.mean([world(e)["sf"] for e in R46]); sfw = np.mean([world(e)["sfw"] for e in R46])
    ov_disputed = (1 - d46["paid"]) if not np.isnan(d46["paid"]) else np.nan
    chk(in_band(lk, 4, 14), f"read 46: leak 4 to 14 ‰ — {lk:.1f}"); chk(in_band(ov_disputed, 0.90, 0.97), f"read 46: of the claims a requester disputes, 0.90 to 0.97 end overturned — {ov_disputed:.3f} of the conduct's claims on real bad work at the first review (every one disputed at a detection of 1); overturned after a second filing {d46['pan2']:.3f} of the claims, at the panel's escalation {d46['pan'] - d46['pan2']:.3f}")
    chk(in_band(sf, 40, 50), f"read 46: the deciding verdict rules on 40 to 50 second filings a run — {sf:.1f} ({sfw:.1f} won)")
    V46 = verdict("On the ruled road a buyer's complaint brings a miss that every member shares to the deciding verdict (read 46's leak under read 40's by two SE, by seed: shown; at or over it: refuted)", dlk[0] + 2 * dlk[1] < 0, dlk[0] >= 0)
if P46av40:
    dlk = mse(col(P46av40, "w_leak") - col(P46av40, "w0_leak")); chk(not two_se(dlk), f"read 46a: the leak within two SE of read 40's by seed — {dlk[0]:+.1f} ± {dlk[1]:.1f} ({np.mean(col(P46av40, 'w_leak')):.1f} against {np.mean(col(P46av40, 'w0_leak')):.1f})")
if P47:
    nd = np.mean([world(e)["disp"] for e in R47.values()]); lk = np.mean(col(P47, "w_leak"))
    chk(in_band(nd, 2, 3.49), f"read 47: two or three disputes a run — {nd:.2f}"); chk(in_band(round(lk, 1), 0.5, 2.5), f"read 47: leak 0.5 to 2.5 ‰ — {lk:.2f} (the all-careful's {np.mean(col(P47, 'w0_leak')):.1f})"); chk(SIX47 <= 1, f"read 47: of six figures of the world no more than one beyond two SE against the all-careful by seed — {SIX47}")
L += CHK; n_met = sum(1 for c in CHK if c.startswith("- MET")); L.append(f"\n**{n_met} of {len(CHK)} expectations met.**\n")
L += ["\n### The conditions\n"] + [v for v in (globals().get(k) for k in ("V41", "V42", "V44", "V45", "V46", "V43m")) if v]
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L[:12])); print(f"... written {sys.argv[1]} ({len(L)} lines)")
