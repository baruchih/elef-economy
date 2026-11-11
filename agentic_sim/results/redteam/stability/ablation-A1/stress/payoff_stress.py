"""The stressed world's payoff table (the plan's step 3, November 11, 2026): own money by action and seat on the scripted ε population with the
fourth action — claim the allowance and stamp — per cell (finalist × temptation × the bond at the audit and panel seats; the shared-difficulty
cell apart), read as ablation-A1/payoff/payoff_table.py reads the arms: the attributed own-money reward of each decision by seat and action
(ε 0.2 uniform over the four actions, so each action's mean at a seat is read without selection), the share of truth-checked bad cases at the
seat beside; the two edges against inspecting — approve blind and the claim (the claim's edge is the stamp's plus the private benefit, the
temptation × the cost claimed, less nothing: the ledger sees a careful review). Means ± SE across seeds. Usage: payoff_stress.py <payoff dir> <out md>"""
import glob, os, sys, re
import numpy as np
root = sys.argv[1]; out = sys.argv[2]
SEATS = ["initial", "audit", "panel", "resumed"]
ACTS = {0: "inspect", 1: "approve blind", 2: "reject blind", 3: "claim + stamp"}
def ms(v):
    v = np.asarray(v, float); v = v[~np.isnan(v)]
    return (float(v.mean()), float(v.std(ddof=1) / np.sqrt(len(v))) if len(v) > 1 else float("nan"), len(v))
cells = sorted(d for d in os.listdir(root) if os.path.isdir(os.path.join(root, d)) and glob.glob(os.path.join(root, d, "*-seed*.npz")))
def key(c):
    m = re.match(r"(pa10|arm2|arm4)-t([\d.]+)-b([\d.]+)(-rho([\d.]+))?", c)
    return ({"pa10": 0, "arm2": 1, "arm4": 2}[m.group(1)], float(m.group(5) or 0), float(m.group(2)), float(m.group(3))) if m else (9, 0, 0, 0)
cells.sort(key=key)
L = [f"# The stressed world's payoff table: own money by action and seat on the scripted ε population, per cell\n",
     "Each cell: the mean attributed own-money reward of a decision (credits, real) ± the SE across seeds, and the decisions behind it; `truth-checked bad` the share of the seat's cases "
     "that are bad plants (at the audit seat under 2.9.0: planted approvals). The claim's reward carries the private benefit (--temptation × the cost claimed, real) the ledger never sees; "
     "`approve blind − inspect` and `claim − inspect` are the two edges against inspecting. The bond's multiple is the audit and panel seats' (the first review's bond G_V).\n"]
summ = []
for c in cells:
    files = sorted(glob.glob(os.path.join(root, c, "*-seed*.npz")))
    per = {s: {a: [] for a in ACTS} for s in SEATS}; share = {s: [] for s in SEATS}; n_dec = {s: 0 for s in SEATS}; has3 = False
    for f in files:
        z = np.load(f, allow_pickle=True)
        seat = z["seat"].astype(str); act = z["action"]; rew = z["reward"].astype(float); isp = z["is_plant"].astype(bool); ful = z["fulfilled"].astype(bool)
        has3 = has3 or bool((act == 3).any())
        for s in SEATS:
            m = seat == s
            if not m.any():
                for a in ACTS: per[s][a].append(np.nan)
                share[s].append(np.nan); continue
            n_dec[s] += int(m.sum()); share[s].append(float((isp[m] & ~ful[m]).mean()))
            for a in ACTS:
                ma = m & (act == a); per[s][a].append(float(rew[ma].mean()) if ma.any() else np.nan)
    L.append(f"\n## {c} ({len(files)} seeds)\n")
    L.append("| seat | decisions | truth-checked bad | inspect | approve blind | reject blind | claim + stamp | approve blind − inspect | claim − inspect |")
    L.append("|---|---|---|---|---|---|---|---|---|")
    row = {"cell": c}
    for s in SEATS:
        if n_dec[s] == 0: continue
        sh = ms(share[s]); cells_ = []
        for a in ACTS:
            mm = ms(per[s][a]); cells_.append(f"{mm[0]:+.3f} ± {mm[1]:.3f}" if mm[2] else "—")
        d1 = ms(np.asarray(per[s][1], float) - np.asarray(per[s][0], float)); d3 = ms(np.asarray(per[s][3], float) - np.asarray(per[s][0], float))
        L.append(f"| {s} | {n_dec[s]} | {sh[0]:.3f} ± {sh[1]:.3f} | " + " | ".join(cells_) + f" | {d1[0]:+.3f} ± {d1[1]:.3f} | {d3[0]:+.3f} ± {d3[1]:.3f} |")
        row[s] = (d1, d3, sh)
    summ.append(row)
L.append("\n## The two edges at the first review and the audit seat, every cell\n")
L.append("| cell | initial: approve blind − inspect | initial: claim − inspect | audit: truth-checked bad | audit: approve blind − inspect | audit: claim − inspect | panel: claim − inspect |")
L.append("|---|---|---|---|---|---|---|")
def e(x): return f"{x[0]:+.3f} ± {x[1]:.3f}" if x and x[2] else "—"
for r in summ:
    i, a, p = r.get("initial"), r.get("audit"), r.get("panel")
    L.append(f"| {r['cell']} | {e(i[0]) if i else '—'} | {e(i[1]) if i else '—'} | {f'{a[2][0]:.3f}' if a else '—'} | {e(a[0]) if a else '—'} | {e(a[1]) if a else '—'} | {e(p[1]) if p else '—'} |")
open(out, "w").write("\n".join(L) + "\n"); print("\n".join(L))
