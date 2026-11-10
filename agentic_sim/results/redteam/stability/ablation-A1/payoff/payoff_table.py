"""Ablation brief A1 r2 §6 / §7.1 — the payoff table first, with no learner: own money by action and seat on the scripted ε population
(run 24's entry cell, every member a slot; ε 0.2 uniform around the careful, so action 0 is the policy's choice whatever the state and
actions 1 and 2 are the uniform draws — each action's mean reward at a seat is read without selection), collected on own-name credit per arm
(payoff/<arm>/eps-seed*.npz: the attributed reward of each decision, the seat, the plant flag and the truth). Beside each seat: the share of
truth-checked bad cases at it (a bad plant — under 2.9.0 at the audit seat a planted approval — that a stamp there is caught on), §2's
left-hand side measured instead of assumed. Means ± SE across seeds (the per-seed mean first). Usage: payoff_table.py [payoff dir] [out md]"""
import glob, os, sys
import numpy as np
root = sys.argv[1] if len(sys.argv) > 1 else os.path.dirname(os.path.abspath(__file__))
out = sys.argv[2] if len(sys.argv) > 2 else os.path.join(root, "payoff.md")
ARMS = [("arm0", "arm 0 — 2.9.0 as in force (π^A at its floor)"), ("arm0-pa10", "arm 0, π^A pinned at 0.10"), ("arm0-pa20", "arm 0, π^A pinned at 0.20"),
        ("arm1", "arm 1 — the trusted ruling"), ("arm1b", "arm 1b — the sampled confirmation (r 0.25)"), ("arm1c", "arm 1c — the cheaper false alarm")]
SEATS = ["initial", "audit", "panel", "resumed"]
ACTS = {0: "inspect", 1: "approve blind", 2: "reject blind"}
def ms(v):
    v = np.asarray(v, float); v = v[~np.isnan(v)]
    return (float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else float("nan"), len(v))
L = [f"# The payoff table (A1 r2 §6): own money by action and seat on the scripted ε population, per arm\n",
     "Each cell: the mean attributed own-money reward of a decision (credits, real) ± the SE across seeds, and the decisions behind it. "
     "`truth-checked bad` is the share of the seat's cases that are bad plants (at the audit seat under 2.9.0: planted approvals) — a stamp "
     "there is caught on these and on nothing else; `plant share` every plant. The careful's own error is the driver's 5 in 100.\n"]
for key, label in ARMS:
    files = sorted(glob.glob(os.path.join(root, key, "eps-seed*.npz")))
    if not files:
        L.append(f"\n## {label}\n\n(no collection)\n"); continue
    per = {s: {a: [] for a in ACTS} for s in SEATS}; share = {s: [] for s in SEATS}; plant = {s: [] for s in SEATS}; n_dec = {s: 0 for s in SEATS}
    for f in files:
        z = np.load(f, allow_pickle=True)
        seat = z["seat"].astype(str); act = z["action"]; rew = z["reward"].astype(float); isp = z["is_plant"].astype(bool); ful = z["fulfilled"].astype(bool)
        for s in SEATS:
            m = seat == s
            if not m.any():
                for a in ACTS: per[s][a].append(np.nan)
                share[s].append(np.nan); plant[s].append(np.nan); continue
            n_dec[s] += int(m.sum())
            share[s].append(float((isp[m] & ~ful[m]).mean())); plant[s].append(float(isp[m].mean()))
            for a in ACTS:
                ma = m & (act == a)
                per[s][a].append(float(rew[ma].mean()) if ma.any() else np.nan)
    L.append(f"\n## {label} ({len(files)} seeds)\n")
    L.append("| seat | decisions | truth-checked bad | plant share | inspect | approve blind | reject blind | approve blind − inspect |")
    L.append("|---|---|---|---|---|---|---|---|")
    for s in SEATS:
        if n_dec[s] == 0: continue
        sh = ms(share[s]); pl = ms(plant[s]); cells = []
        for a in ACTS:
            mm = ms(per[s][a]); cells.append(f"{mm[0]:+.3f} ± {mm[1]:.3f}" if mm[2] else "—")
        d = np.asarray(per[s][1], float) - np.asarray(per[s][0], float); dm = ms(d)
        L.append(f"| {s} | {n_dec[s]} | {sh[0]:.3f} ± {sh[1]:.3f} | {pl[0]:.3f} | " + " | ".join(cells) + f" | {dm[0]:+.3f} ± {dm[1]:.3f} |")
open(out, "w").write("\n".join(L) + "\n"); print("\n".join(L))
