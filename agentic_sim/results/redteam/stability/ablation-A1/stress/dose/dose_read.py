"""Addendum 9's dose (I4.1; November 12, 2026; notes §110): the dosing slots (1 in 4, `mix:dose<q>[audit|first]:0.25`) against the careful slots of the same
world and the all-careful population in the same world (`careful`, paired by seed), on the pin and arm 4 at a temptation of 1 and the bond ×1; read as the
entry test and beside it the claims a slot and the lifetime lost for each claim — (the careful group's lifetime a slot − the dosing group's) over the dosing
slots' claims a slot, ± SE by the ratio's delta method over seeds — and the mechanism at 0.1: the suspensions a slot against the careful group's and the member
audit seats a slot.  Usage: dose_read.py OUT.md"""
import json, os, sys, numpy as np
R = "results/redteam/stability/ablation-A1/stress"
WORLDS = [("pa10", "the pin", "dose0.1", "0.1, every seat"), ("pa10", "the pin", "dose0.3", "0.3, every seat"), ("pa10", "the pin", "dose1", "1, every seat"),
          ("pa10", "the pin", "dose0.3audit", "0.3, the member's audit seat only"), ("pa10", "the pin", "dose0.3first", "0.3, the first review only"),
          ("arm4", "arm 4", "dose0.1", "0.1, every seat"), ("arm4", "arm 4", "dose0.3", "0.3, every seat"), ("arm4", "arm 4", "dose1", "1, every seat")]
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
L = ["# The dose (I4.1): a careful member that claims with probability q — 1 slot in 4, the pin and arm 4, a temptation of 1, the bond ×1\n",
     "Each row one world (seeds 21–40; the two at 0.1 on 21–60). `care − dose` the careful group's lifetime a slot less the dosing group's (± SE over seeds); the all-careful population's lifetime a slot "
     "in the same world beside (the `careful` policy, the same seeds). The lifetime lost for each claim is the gap over the dosing slots' claims a slot. The world's standing false approvals, leak per thousand bad deliveries and overhead a vested task, with the all-careful world's beside.\n",
     "| arm | dose | slots dose / care | **care − dose, real a slot** | dosing: lifetime a slot (wallet + benefit); alive; suspensions a slot; claims a slot | claimed at the first review; at the audit seat; audit seats a slot | careful group: lifetime a slot; suspensions a slot; audit seats a slot | all-careful: lifetime a slot; suspensions a slot | **lost for each claim (real)** | world: FA; leak ‰; overhead (all-careful: FA; leak; overhead) |",
     "|---|---|---|---|---|---|---|---|---|---|"]
checks = []
for k, kn, d, dn in WORLDS:
    p = f"{R}/dose/{k}-{d}/eval.json"
    if not os.path.exists(p): L.append(f"| {kn} | {dn} | (pending) | | | | | | | |"); continue
    j = json.load(open(p)); pol = [x for x in j["episodes"] if x.startswith("mix:")][0]; E = j["episodes"][pol]; C = {int(e["seed"]): e for e in j["episodes"]["careful"]}
    g = mse([f(e, "half_d_lifetime_per_slot") for e in E])
    cl = dict(life=mse([f(e, "half_claim_lifetime_per_slot") for e in E])[0], alive=mse([f(e, "half_claim_alive") for e in E])[0], n=mse([f(e, "half_claim_slots") for e in E])[0],
              susp=mse([f(e, "half_claim_suspensions") / f(e, "half_claim_slots") for e in E]), claims=mse([f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E]),
              fr=sum(f(e, "half_claim_claimed_initial") for e in E) / max(1, sum(f(e, "half_claim_seats_initial") for e in E)), ac=sum(f(e, "half_claim_claimed_audit") for e in E) / max(1, sum(f(e, "half_claim_seats_audit") for e in E)),
              aud=mse([f(e, "half_claim_seats_audit") / f(e, "half_claim_slots") for e in E]))
    ca = dict(life=mse([f(e, "half_care_lifetime_per_slot") for e in E])[0], n=mse([f(e, "half_care_slots") for e in E])[0], susp=mse([f(e, "half_care_suspensions") / f(e, "half_care_slots") for e in E]),
              aud=mse([f(e, "half_care_seats_audit") / f(e, "half_care_slots") for e in E]))
    ref = dict(life=mse([f(C[int(e["seed"])], "learner_lifetime_real") / f(C[int(e["seed"])], "learner_pop_total") for e in E])[0], susp=mse([f(C[int(e["seed"])], "suspensions") / f(C[int(e["seed"])], "learner_pop_total") for e in E])[0])
    lost = ratio_se([f(e, "half_d_lifetime_per_slot") for e in E], [f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E])
    w = dict(fa=mse([f(e, "false_approvals") for e in E])[0], leak=1000 * mse([f(e, "leak_bad") for e in E])[0], oh=mse([f(e, "sys_overhead_per_vested") for e in E])[0],
             fa0=mse([f(C[int(e["seed"])], "false_approvals") for e in E])[0], leak0=1000 * mse([f(C[int(e["seed"])], "leak_bad") for e in E])[0], oh0=mse([f(C[int(e["seed"])], "sys_overhead_per_vested") for e in E])[0])
    def nn(x, fmt): return "—" if (x != x) else format(x, fmt)
    L.append(f"| {kn} | {dn} ({len(E)} seeds) | {cl['n']:.1f} / {ca['n']:.1f} | **{g[0]:+.0f} ± {g[1]:.0f}** | {cl['life']:.0f}; {cl['alive']:.1f}; {cl['susp'][0]:.2f} ± {cl['susp'][1]:.2f}; {cl['claims'][0]:.1f} | {cl['fr']:.3f}; {nn(cl['ac'], '.3f')}; {nn(cl['aud'][0], '.1f')} | "
             f"{ca['life']:.0f}; {ca['susp'][0]:.2f} ± {ca['susp'][1]:.2f}; {ca['aud'][0]:.1f} | {ref['life']:.0f}; {ref['susp']:.2f} | **{lost[0]:.1f} ± {lost[1]:.1f}** | {w['fa']:.1f}; {w['leak']:.0f}; {w['oh']:.1f} ({w['fa0']:.1f}; {w['leak0']:.0f}; {w['oh0']:.1f}) |")
    checks.append((kn, dn, d, g, cl, ca, lost))
L.append("\n## Against addendum 9's expectations\n")
L.append("| arm | dose | behind (≥ 350 at 1; ≥ 150 at 0.3; 30–250 at 0.1) | at 0.1 the mechanism: suspensions a slot ≥ 1.5× the careful's; fewer audit seats a slot | lost for each claim ≥ 5 at 0.3 and 1 | refuted (level or ahead at 0.3)? |")
L.append("|---|---|---|---|---|---|")
for kn, dn, d, g, cl, ca, lost in checks:
    q = 0.1 if d.startswith("dose0.1") else (0.3 if d.startswith("dose0.3") else 1.0)
    need = 350 if q == 1 else (150 if q == 0.3 else None)
    beh = (f"{'yes' if g[0] >= need else 'NO'} ({g[0]:+.0f} ± {g[1]:.0f} against ≥ {need})" if need else f"{'yes' if 30 <= g[0] <= 250 else 'NO'} ({g[0]:+.0f} ± {g[1]:.0f} against 30–250)")
    mech = (f"suspensions {cl['susp'][0]:.2f} against {ca['susp'][0]:.2f} ({'yes' if cl['susp'][0] >= 1.5 * ca['susp'][0] else 'NO'}); audit seats " + ("— (no member audit seat on a member's work under arm 4)" if cl['aud'][0] != cl['aud'][0] else f"{cl['aud'][0]:.1f} against {ca['aud'][0]:.1f} ({'yes' if cl['aud'][0] < ca['aud'][0] else 'NO'})")) if q == 0.1 else "—"
    lc = (f"{'yes' if lost[0] >= 5 else 'NO'} ({lost[0]:.1f} ± {lost[1]:.1f})") if q >= 0.3 else "—"
    ref = (f"{'LEVEL OR AHEAD' if g[0] <= 2 * g[1] else 'behind'}{'' if d == 'dose0.3' else ' (a seat-restricted dose; the condition names the dose at every seat)'}") if q == 0.3 else "—"
    L.append(f"| {kn} | {dn} | {beh} | {mech} | {lc} | {ref} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
