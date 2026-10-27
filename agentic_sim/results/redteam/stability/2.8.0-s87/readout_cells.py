"""2.8.0 §8.7 — the red team's three cells (the ruling after run 36; notes §55): (a) the dial pinned at its floor (`--dial off`, π 0.10), (b) pinned at
π_max 0.40 (`--dial off --pi0 0.40`), (c) untruthful real challengers (`--dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`). Each cell's
self-play finals (the direct, the head alone, the hand and the careful on seeds 21–40) against its base chain's on the same seeds — the careful basin
(`learned-rev-careful-280`) for (a) and (b), the disputes-on population (`learned-rev-disputes-280`) for (c) — paired by seed; the lies and their wins
in (c) (`true_rejections_appealed/overturned`, `true_approvals_disputed/overturned`, kept by run_q from this commit; the base finals predate it).
Usage: python3 readout_cells.py [out md]   (adapted from 2.8.0-s82/finals-paired.py)"""
import json, sys, math, os
import numpy as np
R = "results/redteam/stability"
CELLS = [("pifloor", "careful", "(a) the dial pinned at its floor — `--dial off`, π_t = 0.10"),
         ("picap", "careful", "(b) the dial pinned at π_max — `--dial off --pi0 0.40` (the mirror; a diagnostic, not a rule)"),
         ("liars", "disputes", "(c) untruthful real challengers — `--dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`"),
         ("pifloor2", "careful", "(a′) π_t pinned at its floor with the dial live — `--pi-max 0.10` (m_t answers the record on the odds, the reserve and ω)"),
         ("picap2", "careful", "(b′) π_t pinned at π_max with the dial live — `--pi0 0.40`")]
def load(chain, learner):
    p = f"{R}/learned-rev-{chain}-280/{learner}/eval/final/eval.json"
    try: return json.load(open(p))
    except FileNotFoundError: return None
def eps(d, pol): return {e["seed"]: e for e in d["episodes"][pol]}
def arr(E, key, seeds):
    out = []
    for s in seeds:
        v = E[s].get(key) if s in E else None
        out.append(float(v) if v not in (None, "") else np.nan)
    return np.array(out)
def mse(x):
    x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / math.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def fmt(m, s=None, d=1):
    if m is None or np.isnan(m): return "—"
    return f"{m:.{d}f}" if s is None else f"{m:+.{d}f} ± {s:.{d}f}"
def pooled_rate(E, seeds, seat, kind):
    st = sum(E[s].get(f"seat_{seat}_{kind}_stamped", 0) or 0 for s in seeds if s in E); n = sum(E[s].get(f"seat_{seat}_{kind}_seen", 0) or 0 for s in seeds if s in E)
    return (st / n if n else np.nan), n
KEYS = [("false_approvals_run", "false approvals (run)", 1), ("bad_plants_approved", "bad plants approved", 1), ("good_plants_rejected", "good plants rejected", 1),
        ("suspensions_run", "suspensions", 1), ("audit_overturn_rate", "audit overturn rate", 3), ("audits_held", "audits held", 1),
        ("disputes_filed", "disputes filed", 1), ("disputes_won", "disputes won", 1), ("false_approvals_disputed", "false approvals disputed", 1), ("false_approvals_overturned", "… overturned", 1),
        ("appeals_filed", "appeals filed", 1), ("appeals_won", "appeals won", 1), ("false_rejections_appealed", "false rejections appealed", 1), ("false_rejections_overturned", "… overturned", 1),
        ("true_rejections_appealed", "LIES: true rejections appealed", 1), ("true_rejections_overturned", "… won (bad work paid)", 1),
        ("true_approvals_disputed", "LIES: true approvals disputed", 1), ("true_approvals_overturned", "… won (good work unpaid)", 1), ("rulings", "rulings", 1),
        ("learner_pop_n", "slots alive", 1), ("pop_surplus_nominal", "nominal surplus", 0), ("lifetime_real_wealth", "real lifetime", 0), ("pop_tasks_per_1000", "tasks per 1,000", 1),
        ("P_t", "P_t", 1), ("requester_wallet_mean", "requesters' wallet", 0), ("state_share", "state share", 3), ("awarded", "awarded", 0), ("idle_for_bond_ticks", "idle for bond", 0),
        ("F_hat", "F̂", 3), ("departures", "departures", 1)]
SE_KEYS = {"false_approvals_run", "pop_surplus_nominal", "lifetime_real_wealth", "P_t", "pop_tasks_per_1000", "suspensions_run", "true_rejections_overturned", "true_approvals_overturned"}
out = []
def P(*a): out.append(" ".join(str(x) for x in a))
P("# §8.7 — the three cells' finals (seeds 21–40) against their base chain's, paired by seed\n")
P("The base chain: the careful basin of §54 (`learned-rev-careful-280`) for (a) and (b); the disputes-on population (`learned-rev-disputes-280`) for (c). The learners' columns are each chain's own final policy (the direct the carrier, the head alone beside); the hand and the careful references run on the cell's own flags.")
seeds = list(range(21, 41))
for cell, base, title in CELLS:
    P(f"\n## {title}\n")
    W = {}
    for chain, tag in ((cell, "cell"), (base, "base")):
        for L in ("direct", "wm"):
            d = load(chain, L)
            if d is None: P(f"missing learned-rev-{chain}-280/{L}/eval/final"); continue
            W[(tag, L)] = d
    cols = []
    for tag in ("cell", "base"):
        for pol, L in (("direct", "direct"), ("greedy", "wm"), ("hand", "direct"), ("careful", "direct")):
            d = W.get((tag, L))
            name = {"direct": "direct", "greedy": "head alone", "hand": "hand", "careful": "careful"}[pol]
            if d is None or pol not in d["episodes"]: cols.append((f"{tag} {name}", None)); continue
            cols.append((f"{tag} {name}", eps(d, pol)))
    P("| reading | " + " | ".join(c[0] for c in cols) + " |"); P("|---|" + "---|" * len(cols))
    r = []
    for n, E in cols:
        if E is None: r.append("—"); continue
        c = np.nanmean(arr(E, "care_share", seeds)); a = np.nanmean(arr(E, "approve_blind_share", seeds)); j = np.nanmean(arr(E, "reject_blind_share", seeds))
        r.append(f"{c:.3f} / {a:.3f} / {j:.3f}")
    P("| mix care / approve / reject | " + " | ".join(r) + " |")
    for seat in ("initial", "audit", "panel"):
        r = []
        for n, E in cols:
            if E is None: r.append("—"); continue
            pr, pn = pooled_rate(E, seeds, seat, "plant"); rr, rn = pooled_rate(E, seeds, seat, "real")
            r.append(f"{fmt(pr, d=3)} ({pn}) / {fmt(rr, d=3)} ({rn})")
        P(f"| {seat} seats stamped plant / real (n) | " + " | ".join(r) + " |")
    for key, label, dd in KEYS:
        r = []
        for n, E in cols:
            if E is None: r.append("—"); continue
            m, s = mse(arr(E, key, seeds)); r.append("—" if np.isnan(m) else (f"{m:.{dd}f} ± {s:.{dd}f}" if key in SE_KEYS else f"{m:.{dd}f}"))
        if all(x == "—" for x in r): continue
        P(f"| {label} | " + " | ".join(r) + " |")
    P("\nPaired cell − base by seed (the same policy class; for the learners the two chains' own policies):\n")
    P("| reading | direct | head alone | hand | careful |"); P("|---|---|---|---|---|")
    for key, label, dd in KEYS + [("care_share", "care share", 3), ("approve_blind_share", "approve blind", 3), ("reject_blind_share", "reject blind", 3)]:
        r = []
        for i in range(4):
            A = cols[i][1]; B = cols[i + 4][1]
            if A is None or B is None: r.append("—"); continue
            m, s = mse(arr(A, key, seeds) - arr(B, key, seeds)); r.append(fmt(m, s, dd))
        if all(x == "—" for x in r): continue
        P(f"| {label} | " + " | ".join(r) + " |")
    P("\nWithin the cell, paired against the hand on the same seeds:\n")
    P("| reading | direct − hand | head alone − hand | careful − hand |"); P("|---|---|---|---|")
    H = cols[2][1]
    for key, label, dd in KEYS:
        r = []
        for i in (0, 1, 3):
            A = cols[i][1]
            if A is None or H is None: r.append("—"); continue
            m, s = mse(arr(A, key, seeds) - arr(H, key, seeds)); r.append(fmt(m, s, dd))
        if all(x == "—" for x in r): continue
        P(f"| {label} | " + " | ".join(r) + " |")
    for i in (0, 1):
        A = cols[i][1]
        if A and H:
            fa = arr(A, "false_approvals_run", seeds); fh = arr(H, "false_approvals_run", seeds)
            P(f"- {cols[i][0]}: false approvals / the hand's = {np.nanmean(fa) / np.nanmean(fh):.2f}; seeds above the hand: {int((fa > fh).sum())}/20")
    P("\nMix by period (the cell's finals, pooled over seeds; care / approve / reject):")
    for i in (0, 1):
        n, E = cols[i]
        if E is None: continue
        agg = {}
        for s in seeds:
            if s not in E or not E[s].get("learner_mix_by_period"): continue
            m = json.loads(E[s]["learner_mix_by_period"]) if isinstance(E[s]["learner_mix_by_period"], str) else E[s]["learner_mix_by_period"]
            for p, row in enumerate(m):
                a = agg.setdefault(p, [0, 0, 0])
                for k in range(3): a[k] += row[k]
        P(f"- {n}: " + "; ".join(f"p{p} {a[0]/sum(a):.2f}/{a[1]/sum(a):.2f}/{a[2]/sum(a):.2f}" for p, a in sorted(agg.items()) if sum(a)))
    # the odds band at stamps
    for i in (0, 1):
        n, E = cols[i]
        if E is None: continue
        agg = {}
        for s in seeds:
            b = E[s].get("stamps_by_odds_band") if s in E else None
            if not b: continue
            b = json.loads(b) if isinstance(b, str) else b
            for band, v in (b.items() if isinstance(b, dict) else []):
                a = agg.setdefault(band, [0, 0]); a[0] += v.get("stamps", 0); a[1] += v.get("decisions", 0)
        if agg: P(f"- {n}, stamp rate by odds band (stamps / decisions): " + "; ".join(f"{band} {a[0]/a[1]:.2f} ({a[0]}/{a[1]})" for band, a in sorted(agg.items()) if a[1]))
o = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "cells.md")
open(o, "w").write("\n".join(out) + "\n"); print("wrote", o)
