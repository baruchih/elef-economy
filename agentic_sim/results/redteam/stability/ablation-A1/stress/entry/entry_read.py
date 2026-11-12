"""Addendum 8's entry test (H3.1; November 13, 2026; notes §109): the mixed world at the claiming slots' shares 0.1, 0.25, 0.75 (stress/entry/) beside
F4.1's halves (stress/f41/, the 0.5 row), read by group as §105 read the halves — the claiming group's lifetime a slot (wallet + benefit), alive, suspensions
and claims a slot, the first review claimed, the member audit seats held a slot and claimed, the panels; the careful group's lifetime a slot, alive,
suspensions a slot, audit seats a slot — against the all-careful population in the same cell (§102's finals' careful arm); the world's standing false
approvals, leak per thousand bad deliveries, overhead a vested task, P_t, the dials at the end (m^A, π^A). Means over seeds 21–40, the gap ± its SE.
The re-reads on the driver's corrected suspension log (4df18f1bc; `<eval>-at-4df18f1bc/`) are read where they exist — the evaluations of record counted
every arrival-born slot's arrival as a suspension (the fault stated in notes §109) — and every other group figure is checked identical to the record.
Usage: entry_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
ARMS = [("pa10", "the pin"), ("arm4", "arm 4")]; LEARN = [("direct", "direct", "mix:direct"), ("wm", "head alone", "mix:greedy")]
SHARES = [0.1, 0.25, 0.5, 0.75]
FIX = "-at-4df18f1bc"
def load(k, l, s, pol, fixed=True):
    d = f"{R}/f41/{k}-{l}" if s == 0.5 else f"{R}/entry/{k}-{l}-s{s}"
    if fixed and os.path.exists(f"{d}{FIX}/eval.json"): d += FIX
    p = f"{d}/eval.json"
    if not os.path.exists(p): return None
    j = json.load(open(p)); E = j["episodes"][pol if s == 0.5 else f"{pol}:{s}"]
    for e in E: e["_fixed"] = d.endswith(FIX)
    return E
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mean(E, k): return float(np.nanmean([f(e, k) for e in E]))
def mse(E, k): x = np.array([f(e, k) for e in E]); x = x[~np.isnan(x)]; return x.mean(), x.std(ddof=1) / np.sqrt(len(x))
def ratio(E, a, b): return float(np.nansum([f(e, a) for e in E]) / max(1e-9, np.nansum([f(e, b) for e in E])))
L = ["# The entry test: the claiming slots at 1 in 10, 1 in 4, 1 in 2 (F4.1) and 3 in 4 of the population — frozen policies, §102's cell (a temptation of 1, the bond ×1), seeds 21–40\n",
     "Each row one mixed world (an arm, a learner, a share): the claiming group answers the policy of record, the careful group cares; the groups drawn once per slot by the stable hash read against the share (arrivals included). "
     "`care − claim` the gap in real lifetime a slot (the live wallet net of its loan at the index, a departed slot's take-out, the private benefit counted for the claiming group), ± SE over seeds. "
     "The all-careful reference is §102's finals' careful arm in the same cell (20 seeds): its suspensions a slot and lifetime a slot. The leak per thousand bad deliveries; the overhead the system's a vested task.\n"]
L.append("| arm, learner | share | slots claim / care | **care − claim, real a slot** | claiming: lifetime a slot (wallet + benefit); alive; suspensions a slot; claims a slot | first review claimed; audit seats a slot (claimed); panels a slot | careful: lifetime a slot; alive; suspensions a slot; audit seats a slot; panels a slot | all-careful: lifetime a slot; suspensions a slot | world: FA; leak ‰; overhead; P_t; m^A; π^A |")
L.append("|---|---|---|---|---|---|---|---|---|")
checks = []
for k, kn in ARMS:
    ref = json.load(open(f"{R}/learned/{k}-t1-b1/direct/eval/final/eval.json"))["episodes"]["careful"]
    ref_susp = mean(ref, "suspensions") / mean(ref, "learner_pop_total"); ref_life = mean(ref, "learner_lifetime_real") / mean(ref, "learner_pop_total")   # the engine's count over every slot, arrivals included
    for l, ln, pol in LEARN:
        for s in SHARES:
            E = load(k, l, s, pol)
            if E is None: L.append(f"| {kn}, {ln} | {s} | (pending) | | | | | | |"); continue
            d = mse(E, "half_d_lifetime_per_slot")
            E0 = load(k, l, s, pol, fixed=False)                   # the evaluation of record: every group figure but the suspensions identical to the re-read
            same = all(abs(f(a, kk) - f(b, kk)) < 1e-6 or (f(a, kk) != f(a, kk) and f(b, kk) != f(b, kk)) for a, b in zip(E, E0) for kk in a if kk.startswith("half_") and "suspensions" not in kk and kk != "_fixed") if (E0 is not None and E[0]["_fixed"]) else None
            cl = dict(life=mean(E, "half_claim_lifetime_per_slot"), w=mean(E, "half_claim_wealth_per_slot"), b=mean(E, "half_claim_private_real") / max(1e-9, mean(E, "half_claim_slots")),
                      alive=mean(E, "half_claim_alive"), slots=mean(E, "half_claim_slots"), susp=mean(E, "half_claim_suspensions") / max(1e-9, mean(E, "half_claim_slots")), claims=mean(E, "half_claim_claims") / max(1e-9, mean(E, "half_claim_slots")),
                      fr=ratio(E, "half_claim_claimed_initial", "half_claim_seats_initial"), aud=mean(E, "half_claim_seats_audit") / max(1e-9, mean(E, "half_claim_slots")), audc=ratio(E, "half_claim_claimed_audit", "half_claim_seats_audit"), pan=mean(E, "half_claim_seats_panel") / max(1e-9, mean(E, "half_claim_slots")))
            ca = dict(life=mean(E, "half_care_lifetime_per_slot"), alive=mean(E, "half_care_alive"), slots=mean(E, "half_care_slots"), susp=mean(E, "half_care_suspensions") / max(1e-9, mean(E, "half_care_slots")),
                      aud=mean(E, "half_care_seats_audit") / max(1e-9, mean(E, "half_care_slots")), pan=mean(E, "half_care_seats_panel") / max(1e-9, mean(E, "half_care_slots")))
            w = dict(fa=mean(E, "false_approvals"), leak=1000 * mean(E, "leak_bad"), oh=mean(E, "sys_overhead_per_vested"), pt=mean(E, "P_t"), mA=mean(E, "m_A"), piA=mean(E, "pi_A"))
            L.append(f"| {kn}, {ln} | {s}{' (re-read' + (', identical' if same else ', DIFFERS') + ')' if same is not None else ''} | {cl['slots']:.1f} / {ca['slots']:.1f} | **{d[0]:+.0f} ± {d[1]:.0f}** | {cl['life']:.0f} ({cl['w']:.0f} + {cl['b']:.0f}); {cl['alive']:.1f}; {cl['susp']:.2f}; {cl['claims']:.1f} | {cl['fr']:.2f}; {cl['aud']:.1f} ({cl['audc']:.2f}); {cl['pan']:.1f} | "
                     f"{ca['life']:.0f}; {ca['alive']:.1f}; {ca['susp']:.2f}; {ca['aud']:.1f}; {ca['pan']:.1f} | {ref_life:.0f}; {ref_susp:.2f} | {w['fa']:.1f}; {w['leak']:.0f}; {w['oh']:.1f}; {w['pt']:.1f}; {w['mA']:.1f}; {w['piA']:.3f} |")
            checks.append((kn, ln, s, d[0], d[1], ca["susp"], w["leak"], cl["aud"], ca["aud"], k))
L.append("\n## Against addendum 8's expectations\n")
L.append("| arm, learner | share | careful ahead | at 1 in 10 by ≥ 200 | careful suspensions a slot (< 0.3 at 1 in 10) | leak (1 in 10 within 1.5× the unstressed: pin ≤ 16.5 / 12, arm 4 ≤ 15 / 9; 3 in 4 above half the all-claim: pin > 33, arm 4 > 9) | a claiming slot's audit seats under a tenth of a careful slot's |")
L.append("|---|---|---|---|---|---|---|")
for kn, ln, s, g, se, cs, leak, ca_, cc, k in checks:
    aud = "— (no member audit seat on a member's work under arm 4)" if k == "arm4" else f"{ca_:.1f} against {cc:.1f}: {'yes' if ca_ < 0.1 * cc else 'NO'}"
    L.append(f"| {kn}, {ln} | {s} | {'yes' if g > 2 * se else 'NO'} ({g:+.0f} ± {se:.0f}) | {('yes' if g >= 200 else 'NO') if s == 0.1 else '—'} | {cs:.2f} | {leak:.0f} | {aud} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
