"""Addendum 15 (November 16, 2026; notes §114): P3's readings from N4's worlds run again whole at 726a25c76 for the per-slot tallies (a15/rerun/; every figure of
record checked to the digit against stress/n4/ and stress/standing/), and P4's eight reads (a15/p4/) — read as N4 was, with the claims split by standing, the slots in
place from tick 0 alone for conduct M, the failure's share, tick and claims after it for conduct F, the expectations stated before the run and the refutations.
Usage: a15_read.py OUT.md"""
import json, os, sys, glob, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; A = f"{R}/a15"
T = 1000; RES = 0.8
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def f0(e, k): v = e.get(k); return float(v) if v not in (None, "") else 0.0
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); ok = ~(np.isnan(num) | np.isnan(den)); num, den = num[ok], den[ok]; n = len(num)
    if n < 2 or den.mean() == 0: return (np.nan, np.nan)
    a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1); r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
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
def rows_of(E, C, filt=lambda v: True):
    """Per seed: the gap on the three lifetimes between the careful and the claiming slots the filter keeps, and both groups' readings a slot."""
    out = []
    for e in E:
        g = {k: [v for v in V if filt(v)] for k, V in groups(e).items()}
        if not g["claim"] or not g["care"] or int(e["seed"]) not in C: continue
        c0 = C[int(e["seed"])]; Sc = [v for v in json.loads(c0["learner_slots_json"]).values() if filt(v)]
        r = {"seed": int(e["seed"]), "all_care": (sum(life(v) for v in Sc) / len(Sc)) if Sc else np.nan}
        for kk, V in g.items():
            n = len(V); good = sum(v["ticks_good"] for v in V) / n; ig = sum(v["income_good"] for v in V) / n; bg = sum(v["benefit_good"] for v in V) / n
            r[kk] = dict(n=n, good=good, ig=ig, rate=((ig + bg) / good if good else np.nan), brate=(bg / good if good else np.nan), life=sum(life(v) for v in V) / n, lres=sum(life(v) + RES * after(v) for v in V) / n,
                         ben=sum(v["private_real"] for v in V) / n, claims=sum(v["claims"] for v in V) / n, cm=sum(v.get("claims_member", 0) for v in V) / n, cp=sum(v.get("claims_probation", 0) for v in V) / n,
                         caf=sum(v.get("claims_after_fail", 0) for v in V) / n, susp=sum(v["suspensions"] for v in V) / n, aud=sum(v["audits_done"] for v in V) / n,
                         failed=sum(1 for v in V if v.get("pfail_ticks")) / n, first_t=np.mean([v["pfail_ticks"][0] for v in V if v.get("pfail_ticks")]) if any(v.get("pfail_ticks") for v in V) else np.nan,
                         **{f"src_{k}": sum(v.get(k, 0.0) for v in V) / n for k in ("fee_initial", "fee_audit", "fee_panel", "fee_other", "delivery", "reimbursed", "fee_uplift", "fee_emission", "bond_initial", "bond_audit", "bond_panel", "bond_other", "bonds_forfeited")})
        cc, s = r["care"], r["claim"]
        r.update(rec=cc["life"] - s["life"], res=cc["lres"] - s["lres"], lfl=cc["ig"] - s["rate"] * cc["good"], den=s["brate"] * cc["good"], ben=s["ben"], claims=s["claims"], care_minus_all=cc["life"] - r["all_care"],
                 fa=f(e, "false_approvals"), leak=1000 * f(e, "leak_bad"), oh=f(e, "sys_overhead_per_vested"), fa0=f(c0, "false_approvals"), leak0=1000 * f(c0, "leak_bad"), oh0=f(c0, "sys_overhead_per_vested"))
        out.append(r)
    return out
def col(rows, k): return np.array([r[k] for r in rows], float)
def grp(rows, kk, k): return np.mean([r[kk][k] for r in rows])
def temp(rows, key, den): t = ratio_se(col(rows, key), col(rows, den)); return 1 + t[0], t[1]
def lifetimes_row(name, rows, extra=""):
    if not rows: return f"| {name} | (pending) | | | | | | |{extra}"
    a, b, c = mse(col(rows, "rec")), mse(col(rows, "res")), mse(col(rows, "lfl")); ta, tb, tc = temp(rows, "rec", "ben"), temp(rows, "res", "ben"), temp(rows, "lfl", "den")
    return f"| {name} | {len(rows)} | **{a[0]:+.0f} ± {a[1]:.0f}** ({a[0] / a[1]:.1f}) | {ta[0]:.1f} ± {ta[1]:.1f} | **{b[0]:+.0f} ± {b[1]:.0f}** ({b[0] / b[1]:.1f}) | {tb[0]:.1f} ± {tb[1]:.1f} | **{c[0]:+.0f} ± {c[1]:.0f}** ({c[0] / c[1]:.1f}) | {tc[0]:.1f} ± {tc[1]:.1f} |{extra}"
def groups_row(name, rows):
    if not rows: return f"| {name} | (pending) | | | |"
    l1, l2, l3 = ratio_se(col(rows, "rec"), col(rows, "claims")), ratio_se(col(rows, "res"), col(rows, "claims")), ratio_se(col(rows, "lfl"), col(rows, "claims"))
    return (f"| {name} | {grp(rows, 'claim', 'claims'):.1f} ({grp(rows, 'claim', 'cm'):.1f} / {grp(rows, 'claim', 'cp'):.1f}); {grp(rows, 'claim', 'ben'):.1f}; {grp(rows, 'claim', 'susp'):.2f}; {grp(rows, 'claim', 'aud'):.1f}; {grp(rows, 'claim', 'good'):.0f} | "
            f"{grp(rows, 'care', 'susp'):.2f}; {grp(rows, 'care', 'aud'):.1f}; {grp(rows, 'care', 'good'):.0f} | **{l1[0]:.1f} ± {l1[1]:.1f} / {l2[0]:.1f} ± {l2[1]:.1f} / {l3[0]:.1f} ± {l3[1]:.1f}** | "
            f"{mse(col(rows, 'care_minus_all'))[0]:+.0f} ± {mse(col(rows, 'care_minus_all'))[1]:.0f}; {np.mean(col(rows, 'fa')):.1f}; {np.mean(col(rows, 'leak')):.0f}; {np.mean(col(rows, 'oh')):.1f} ({np.mean(col(rows, 'fa0')):.1f}; {np.mean(col(rows, 'leak0')):.0f}; {np.mean(col(rows, 'oh0')):.1f}) |")
HDR_L = ["| world / read | seeds | **of record** | temptation | **with the reservation** | temptation | **like for like** | temptation |", "|---|---|---|---|---|---|---|---|"]
HDR_G = ["| world / read | dosing slots: claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** | careful group − all-careful; FA; leak ‰; overhead (all-careful) |", "|---|---|---|---|---|"]
# ---------------------------------------------------------------- the worlds run again: reproduction check
RERUN = {"w1": [f"{A}/rerun/w1-s21-70", f"{A}/rerun/w1-s71-120"], "w2": [f"{A}/rerun/w2"], "w3": [f"{A}/rerun/w3"], "w4": [f"{A}/rerun/w4"], "w6": [f"{A}/rerun/w6-s21-70", f"{A}/rerun/w6-s71-120"]}
REC = {"w1": [f"{R}/standing/dose-pa10-dose0.1", f"{R}/n4/w1-s61-120"], "w2": [f"{R}/n4/w2"], "w3": [f"{R}/n4/w3"], "w4": [f"{R}/n4/w45-s21-50", f"{R}/n4/w45-s51-80"], "w6": [f"{R}/standing/dose-arm4-dose0.1", f"{R}/n4/w6-s61-120"]}
WN = {"w1": "world 1: the pin, the fee of record", "w2": "world 2: the pin, the fee doubled", "w3": "world 3: arm 1, the fee of record", "w4": "world 4: arm 1, the fee doubled", "w6": "world 6: arm 4"}
L = ["# Addendum 15's P3 from N4's worlds run again whole, and P4's eight reads (November 16, 2026; a15/launch.sh at 726a25c76)\n", "## The worlds run again: every figure of record reproduced?\n"]
D = {}
for k in RERUN:
    E, C = load(RERUN[k], "mix:dose0.1:0.25"); E0, C0 = load(REC[k], "mix:dose0.1:0.25"); D[k] = (E, C)
    a = {int(e["seed"]): (f(e, "half_d_lifetime_per_slot"), f(e, "half_claim_claims"), f(e, "false_approvals")) for e in E}; b = {int(e["seed"]): (f(e, "half_d_lifetime_per_slot"), f(e, "half_claim_claims"), f(e, "false_approvals")) for e in E0}
    common = sorted(set(a) & set(b)); same = all(all(abs(x - y) < 1e-9 for x, y in zip(a[s], b[s])) for s in common)
    ca = {s: f(c, "learner_lifetime_real") for s, c in C.items()}; cb = {s: f(c, "learner_lifetime_real") for s, c in C0.items()}; cs = sorted(set(ca) & set(cb)); same_c = all(abs(ca[s] - cb[s]) < 1e-6 for s in cs)
    L.append(f"- {WN[k]}: the dosing world on {len(common)} shared seeds {'**to the digit**' if same else '**DIFFERS**'} (the gap, the claims, the false approvals), the all-careful on {len(cs)} seeds {'to the digit' if same_c else '**DIFFERS**'}; {len(E)} dosing and {len(C)} careful episodes here.")
# ---------------------------------------------------------------- P3.1 by the slot's kind
L += ["", "## P3.1. The dose by the slot's kind — worlds 1, 4 and 6 (the dosing slots against the careful slots of the same kind)\n", "The slots in place from tick 0 (`t_in` 0, the founding members) and the arrivals apart; within each kind the gap on the three lifetimes, the claims as a member and on probation, the lifetime lost for each claim.\n"] + HDR_L
P31 = {}
for k in ("w1", "w4", "w6"):
    E, C = D[k]
    for kind, filt in (("in place from tick 0", lambda v: v["t_in"] == 0), ("arrivals", lambda v: v["t_in"] > 0), ("every slot", lambda v: True)):
        rows = rows_of(E, C, filt); P31[(k, kind)] = rows; L.append(lifetimes_row(f"{WN[k]} — {kind}", rows))
L += ["", "| world — kind | dosing slots a slot: n; claims (as a member / on probation); benefit; suspensions; audit seats; good ticks | careful slots: n; suspensions; audit seats; good ticks | **lost for each claim: of record / with the reservation / like for like** |", "|---|---|---|---|"]
for k in ("w1", "w4", "w6"):
    for kind in ("in place from tick 0", "arrivals", "every slot"):
        rows = P31[(k, kind)]
        if not rows: continue
        l1, l2, l3 = ratio_se(col(rows, "rec"), col(rows, "claims")), ratio_se(col(rows, "res"), col(rows, "claims")), ratio_se(col(rows, "lfl"), col(rows, "claims"))
        L.append(f"| {WN[k]} — {kind} | {grp(rows, 'claim', 'n'):.1f}; {grp(rows, 'claim', 'claims'):.1f} ({grp(rows, 'claim', 'cm'):.1f} / {grp(rows, 'claim', 'cp'):.1f}); {grp(rows, 'claim', 'ben'):.1f}; {grp(rows, 'claim', 'susp'):.2f}; {grp(rows, 'claim', 'aud'):.1f}; {grp(rows, 'claim', 'good'):.0f} | {grp(rows, 'care', 'n'):.1f}; {grp(rows, 'care', 'susp'):.2f}; {grp(rows, 'care', 'aud'):.1f}; {grp(rows, 'care', 'good'):.0f} | **{l1[0]:.1f} ± {l1[1]:.1f} / {l2[0]:.1f} ± {l2[1]:.1f} / {l3[0]:.1f} ± {l3[1]:.1f}** |")
# ---------------------------------------------------------------- P3.2 where the doubled fee goes
L += ["", "## P3.2. Where the doubled fee goes under arm 1 — worlds 1 to 4, each group's income a slot by source and the bonds forfeited by seat\n",
      "Real a slot over the slot's life (the public record's tally at the index of each event): the review fees by the seat's role (first reviews / the member's audit seats / panels and appeals / other), the awards (the delivery price), the reimbursements, the uplift and the emission; the bonds forfeited by seat (first review / audit / panel).\n",
      "| world | group | **fees: first reviews / audit seats / panels / other** | awards | reimbursed | uplift; emission | **bonds forfeited: first review / audit / panel** (all) |", "|---|---|---|---|---|---|---|"]
for k in ("w1", "w2", "w3", "w4"):
    rows = rows_of(*D[k])
    if not rows: continue
    for kk, kn in (("claim", "dosing"), ("care", "careful")):
        g = lambda key: grp(rows, kk, "src_" + key)
        L.append(f"| {WN[k]} | {kn} | **{g('fee_initial'):.1f} / {g('fee_audit'):.1f} / {g('fee_panel'):.1f} / {g('fee_other'):.1f}** | {g('delivery'):.0f} | {g('reimbursed'):.0f} | {g('fee_uplift'):.1f}; {g('fee_emission'):.1f} | **{g('bond_initial'):.1f} / {g('bond_audit'):.1f} / {g('bond_panel'):.1f}** ({g('bonds_forfeited'):.1f}) |")
L += ["", "**World 4 less world 3, paired by seed (arm 1: the fee doubled less the fee of record), and world 2 less world 1 (the pin):**\n", "| pair | seeds | lifetime | the fee of record | the fee doubled | **doubled − record, paired** |", "|---|---|---|---|---|---|"]
for a, b, nm in (("w3", "w4", "arm 1 (world 4 less 3)"), ("w1", "w2", "the pin (world 2 less 1)")):
    ra = {r["seed"]: r for r in rows_of(*D[a])}; rb = {r["seed"]: r for r in rows_of(*D[b])}; seeds = sorted(set(ra) & set(rb))
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        if seeds:
            x = np.array([ra[s][key] for s in seeds]); y = np.array([rb[s][key] for s in seeds]); ok = ~(np.isnan(x) | np.isnan(y)); m = mse(y[ok] - x[ok])
            L.append(f"| {nm} | {int(ok.sum())} | {kn} | {x[ok].mean():+.0f} | {y[ok].mean():+.0f} | **{m[0]:+.0f} ± {m[1]:.0f}** |")
# ---------------------------------------------------------------- P3.3 a wrong planted verdict in the all-careful
L += ["", "## P3.3. A wrong planted verdict in the all-careful populations of worlds 1, 4 and 6\n",
      "Per slot: whether a wrong planted verdict ever lands on its record, the tick of the first; the slot's income a tick (real) before the first, from it until its panel seats return (a member and panel-eligible again), and after; how many return and how long the seats are lost; the suspensions.\n",
      "| world | slots | **share with a wrong planted verdict** | tick of the first (mean; median) | **income a tick: before / seats lost / after** | seats returned: share of the failed; ticks lost (mean) | never returned: alive at the end / departed | suspended (share of the failed) |", "|---|---|---|---|---|---|---|---|"]
for k in ("w1", "w4", "w6"):
    E, C = D[k]; V = [v for c in C.values() for v in json.loads(c["learner_slots_json"]).values()]
    F = [v for v in V if v.get("pfail_ticks")]
    if not V: continue
    inc = lambda ph: sum(v[f"pf_income_{ph}"] for v in F) / max(1, sum(v[f"pf_ticks_{ph}"] for v in F))
    back = [v for v in F if v.get("pf_back_t") is not None]; nb = [v for v in F if v.get("pf_back_t") is None]
    L.append(f"| {WN[k]} | {len(V)} | **{len(F) / len(V):.3f}** | {np.mean([v['pfail_ticks'][0] for v in F]):.0f}; {np.median([v['pfail_ticks'][0] for v in F]):.0f} | **{inc('before'):.2f} / {inc('lost'):.2f} / {inc('after'):.2f}** | {len(back) / max(1, len(F)):.2f}; {np.mean([v['pf_ticks_lost'] for v in back]) if back else float('nan'):.0f} | {sum(1 for v in nb if v['alive'])} / {sum(1 for v in nb if not v['alive'])} | {sum(1 for v in F if v['suspensions']) / max(1, len(F)):.2f} |")
# ---------------------------------------------------------------- P3.4 the orchestrator's seats by kind
L += ["", "## P3.4. The orchestrator's seats under arm 1, by kind, for each vested task — the all-careful of worlds 3 and 4, beside the same seats' holders in world 1\n",
      "Under arm 1 the deciding verdict opens after a difference at the audit (`audit`: a member's audit disagreed with the first verdict; `state_audit`: the state's audit seat disagreed, its verdict the first seat) or where a member panel escalates (`panel`, on an appeal or in a dispute). Per real root awarded (run_q's row carries the awards, not the vested count; nearly every awarded root vests): the deciding verdicts by reason and the challenge's kind, their seats, and the panel seats sat by members and by the state by the challenge's kind (`audit` the third seat after an audit's difference, `appeal`, `dispute`); under arm 0 (world 1) the same panel seats and the rulings.\n",
      "| world | real roots awarded a run (the denominator) | **deciding verdicts per vested task: after an audit's difference (member's / state's) / on an appeal / in a dispute** | their seats per vested task | **panel seats per vested task — members: third / appeal / dispute; the state: third / appeal / dispute** | rulings per vested task |", "|---|---|---|---|---|---|"]
for k in ("w1", "w3", "w4"):
    E, C = D[k]; cs = list(C.values())
    if not cs: continue
    tot = {}; vest = 0.0; rul = 0.0
    for c in cs:
        d = json.loads(c.get("seats_by_kind_json") or "{}")
        for kk, v in d.items(): tot[kk] = tot.get(kk, 0) + v
        vest += f0(c, "awarded"); rul += f0(c, "rulings")   # the roots awarded a run (the vested real roots are not in run_q's row; nearly every awarded root vests)
    g = lambda kk: tot.get(kk, 0) / max(1, vest)
    L.append(f"| {WN[k]} | {vest / len(cs):.0f} | **{g('dec_audit_audit'):.3f} / {g('dec_state_audit_audit'):.3f} / {g('dec_panel_appeal'):.3f} / {g('dec_panel_dispute'):.3f}** | {sum(v for kk, v in tot.items() if kk.startswith('decseats_')) / max(1, vest):.3f} | **{g('panelseat_member_audit'):.3f} / {g('panelseat_member_appeal'):.3f} / {g('panelseat_member_dispute'):.3f}; {g('panelseat_troop_audit'):.3f} / {g('panelseat_troop_appeal'):.3f} / {g('panelseat_troop_dispute'):.3f}** | {rul / max(1, vest):.3f} |")
# ---------------------------------------------------------------- P4
READS = [("r1", "1. conduct M at 0.1, world 1's cell (the pin)", [f"{A}/p4/r1-s21-70", f"{A}/p4/r1-s71-120"], "mix:doseM0.1:0.25", "w1", []),
         ("r2", "2. conduct M at 0.1, world 4's cell (arm 1, the fee doubled)", [f"{A}/p4/r2-s21-80", f"{A}/p4/r2-s81-120"], "mix:doseM0.1:0.25", "w4", [f"{A}/p4/r2-s81-120"]),
         ("r3", "3. conduct M at 0.1, world 6's cell (arm 4)", [f"{A}/p4/r3-s21-70", f"{A}/p4/r3-s71-120"], "mix:doseM0.1:0.25", "w6", []),
         ("r4", "4. conduct M at 0.3, world 4's cell", [f"{A}/p4/r4"], "mix:doseM0.3:0.25", "w4", []),
         ("r5", "5. conduct F (M at 0.3 from the first failure), world 4's cell", [f"{A}/p4/r5"], "mix:doseF0.3:0.25", "w4", []),
         ("r6", "6. conduct F, world 6's cell", [f"{A}/p4/r6"], "mix:doseF0.3:0.25", "w6", []),
         ("r7", "7. the audit seat alone under arm 1, the fee of record, dose 0.3", [f"{A}/p4/r7"], "mix:dose0.3audit:0.25", "w3", []),
         ("r8", "8. the audit seat alone under arm 1, the fee doubled, dose 0.3", [f"{A}/p4/r8"], "mix:dose0.3audit:0.25", "w4", [])]
L += ["", "## P4. The eight reads — the three lifetimes with their level temptations\n"] + HDR_L
P4 = {}
for rid, nm, dirs, pol, cw, extra_c in READS:
    E, Cx = load(dirs, pol); C = dict(D[cw][1]); C.update(Cx)
    rows = rows_of(E, C); P4[rid] = (rows, E, C); L.append(lifetimes_row(nm, rows))
    if rid in ("r1", "r2", "r3", "r4"):
        rows0 = rows_of(E, C, lambda v: v["t_in"] == 0); P4[rid + "g"] = rows0; L.append(lifetimes_row(nm + " — the slots in place from tick 0 alone", rows0))
L += ["", "## P4. Both groups a slot, the lifetime lost for each claim, and the honest side\n"] + HDR_G
for rid, nm, *_ in READS:
    L.append(groups_row(nm, P4[rid][0]))
    if rid + "g" in P4: L.append(groups_row(nm + " — in place from tick 0", P4[rid + "g"]))
L += ["", "**Conduct F — the failure's share, the tick of the first and the claims after it (the conduct's slots):**\n", "| read | slots with a wrong planted verdict (share) | tick of the first (mean) | claims a slot: all / after the first failure / as a member / on probation |", "|---|---|---|---|"]
for rid in ("r5", "r6"):
    rows = P4[rid][0]
    if rows: L.append(f"| {dict((r[0], r[1]) for r in READS)[rid]} | {grp(rows, 'claim', 'failed'):.3f} | {np.nanmean(col([r['claim'] for r in rows], 'first_t')) if rows else float('nan'):.0f} | {grp(rows, 'claim', 'claims'):.1f} / {grp(rows, 'claim', 'caf'):.1f} / {grp(rows, 'claim', 'cm'):.1f} / {grp(rows, 'claim', 'cp'):.1f} |")
# ---------------------------------------------------------------- paired contrasts
L += ["", "## Paired contrasts on the shared seeds\n", "| contrast | seeds | lifetime | first | second | **second − first, paired** | SE from nothing |", "|---|---|---|---|---|---|---|"]
def paired(nm, ra, rb):
    A = {r["seed"]: r for r in ra}; B = {r["seed"]: r for r in rb}; seeds = sorted(set(A) & set(B))
    for key, kn in (("rec", "of record"), ("res", "with the reservation"), ("lfl", "like for like")):
        if seeds:
            x = np.array([A[s][key] for s in seeds]); y = np.array([B[s][key] for s in seeds]); ok = ~(np.isnan(x) | np.isnan(y)); m = mse(y[ok] - x[ok])
            L.append(f"| {nm} | {int(ok.sum())} | {kn} | {x[ok].mean():+.0f} | {y[ok].mean():+.0f} | **{m[0]:+.0f} ± {m[1]:.0f}** | {m[0] / m[1]:.1f} |")
paired("read 8 less read 7 (the audit seat alone under arm 1: the fee doubled less the fee of record)", P4["r7"][0], P4["r8"][0])
for rid, w in (("r1", "w1"), ("r2", "w4"), ("r3", "w6")):
    paired(f"conduct M at 0.1 less the plain dose at 0.1, {WN[w]}", rows_of(*D[w]), P4[rid][0])
E5, C5 = load([f"{R}/n4/w45-s21-50", f"{R}/n4/w45-s51-80"], "mix:dose0.3:0.25"); W5 = rows_of(E5, dict(D["w4"][1]))
paired("conduct M at 0.3 less the plain dose at 0.3 (world 5), world 4's cell", W5, P4["r4"][0])
paired("conduct F less the plain dose at 0.3 (world 5), world 4's cell", W5, P4["r5"][0])
paired("conduct F less conduct M at 0.3, world 4's cell", P4["r4"][0], P4["r5"][0])
# ---------------------------------------------------------------- expectations
L += ["", "## Against the expectations stated before the run\n", "| statement | read | |", "|---|---|---|"]
def chk(name, cond, read): L.append(f"| {name} | {read} | {'met' if cond else 'MISSED'} |")
def g(rid, key): rows = P4[rid][0]; return mse(col(rows, key)) if rows else (np.nan, np.nan)
def lost(rid, key, rows=None): rows = P4[rid][0] if rows is None else rows; return ratio_se(col(rows, key), col(rows, "claims")) if rows else (np.nan, np.nan)
PLAIN = {"r1": (16.7, 12.7, 11.9), "r2": (20.4, 16.1, 12.9), "r3": (15.0, 8.2, 5.8)}
for rid in ("r1", "r2", "r3"):
    a = g(rid, "rec"); ag = mse(col(P4[rid + "g"], "rec")) if P4[rid + "g"] else (np.nan, np.nan)
    chk(f"M at 0.1, {rid}: behind of record, all slots and the slots in place from tick 0 (≥ 2 SE)", a[0] > 2 * a[1] and ag[0] > 2 * ag[1], f"{a[0]:+.0f} ± {a[1]:.0f}; from tick 0 {ag[0]:+.0f} ± {ag[1]:.0f}")
    ls = [lost(rid, k)[0] for k in ("rec", "res", "lfl")]
    chk(f"M at 0.1, {rid}: for each claim less than the plain dose ({' / '.join(str(x) for x in PLAIN[rid])})", all(x < p for x, p in zip(ls, PLAIN[rid])), " / ".join(f"{x:.1f}" for x in ls))
a, c = g("r2", "rec"), g("r2", "lfl"); tc = temp(P4["r2"][0], "lfl", "den") if P4["r2"][0] else (np.nan, np.nan)
chk("M at 0.1 in world 4's cell: behind by 40 to 150 of record", 40 <= a[0] <= 150, f"{a[0]:+.0f} ± {a[1]:.0f}"); chk("… by 20 to 110 like for like", 20 <= c[0] <= 110, f"{c[0]:+.0f} ± {c[1]:.0f}"); chk("… level at a temptation of 2.5 to 6 like for like", 2.5 <= tc[0] <= 6, f"{tc[0]:.1f} ± {tc[1]:.1f}")
c = g("r3", "lfl"); chk("M at 0.1 in world 6's cell: within two standard errors of nothing like for like", abs(c[0]) <= 2 * c[1], f"{c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE)")
a = g("r4", "rec"); l4 = lost("r4", "rec"); chk("M at 0.3 in world 4's cell: behind by 150 to 450 of record", 150 <= a[0] <= 450, f"{a[0]:+.0f} ± {a[1]:.0f}"); chk("… losing less for each claim than world 5's 26.8", l4[0] < 26.8, f"{l4[0]:.1f} ± {l4[1]:.1f}")
for rid, w5 in (("r5", 26.8), ("r6", None)):
    rows = P4[rid][0]
    if not rows: continue
    a = g(rid, "rec"); chk(f"F, {rid}: under 8 claims a slot", grp(rows, "claim", "claims") < 8, f"{grp(rows, 'claim', 'claims'):.1f}"); chk(f"F, {rid}: behind by under 120 of record", a[0] < 120, f"{a[0]:+.0f} ± {a[1]:.0f}")
    chk(f"F, {rid}: not ahead by two standard errors", not (a[0] < -2 * a[1]), f"{a[0] / a[1]:.1f} SE")
    l = lost(rid, "rec"); chk(f"F, {rid}: losing less for each claim than the plain dose at 0.3 ({'world 5: 26.8' if rid == 'r5' else 'arm 4 at 0.3 of record: 15.3 on twenty seeds'})", l[0] < (26.8 if rid == "r5" else 15.3), f"{l[0]:.1f} ± {l[1]:.1f}")
a = g("r7", "rec"); chk("the audit seat alone under arm 1 at the fee of record: within two standard errors of nothing (J4's world 1: 30 ± 35)", abs(a[0]) <= 2 * a[1], f"{a[0]:+.0f} ± {a[1]:.0f} ({a[0] / a[1]:.1f} SE)")
a = g("r8", "rec"); l8 = lost("r8", "rec"); chk("… at twice the fee: behind by 60 to 200 of record, ≥ 3 SE (J4's world 3: 129 ± 34)", 60 <= a[0] <= 200 and a[0] >= 3 * a[1], f"{a[0]:+.0f} ± {a[1]:.0f} ({a[0] / a[1]:.1f} SE)"); chk("… losing 10 to 30 for each claim (18.9 ± 5.8)", 10 <= l8[0] <= 30, f"{l8[0]:.1f} ± {l8[1]:.1f}")
b, c = g("r2", "res"), g("r2", "lfl")
L.append(f"\n**Refuted, each apart.** *The combination as ruled holds the conduct the learners found* — refuted if M at 0.1 in world 4's cell is within two standard errors of nothing with the reservation counted or like for like: {b[0]:+.0f} ± {b[1]:.0f} ({b[0] / b[1]:.1f} SE) and {c[0]:+.0f} ± {c[1]:.0f} ({c[0] / c[1]:.1f} SE) — **{'REFUTED' if (b[0] <= 2 * b[1] or c[0] <= 2 * c[1]) else 'not refuted'}**.")
a = g("r8", "rec"); L.append(f"*The seat's pay is a stake beside the court* — refuted if in read 8 the dosing slot is within two standard errors of nothing of record: {a[0]:+.0f} ± {a[1]:.0f} ({a[0] / a[1]:.1f} SE) — **{'REFUTED' if a[0] <= 2 * a[1] else 'not refuted'}**.")
rr = [g("r5", k) for k in ("rec", "res", "lfl")]; L.append(f"*A failed record still has something to lose* — no refutation stated; F in world 4's cell on the three lifetimes: {', '.join(f'{x[0]:+.0f} ± {x[1]:.0f} ({x[0] / x[1]:.1f} SE)' for x in rr)} — {'within two standard errors of nothing on all three' if all(abs(x[0]) <= 2 * x[1] for x in rr) else 'not within two standard errors of nothing on all three'}.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
