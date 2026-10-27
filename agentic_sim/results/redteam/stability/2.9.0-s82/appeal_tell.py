"""§8.2's liar cell: is the planted lie told apart at the appeal seat? The 45-field observation at every panel decision of the learned
population (or the hand's), grouped by seat / case kind / truth; per field the standardized mean difference and the single-field AUC
between the planted lie's appeals (plant, bad) and the real appeals; a logistic probe on the whole vector with leave-one-seed-out
folds; the same for the controls (the truthful plant appeal of 2.8.0's class, the dispute seat, the initial seat).
Usage: appeal_tell.py "<cell>" seeds direct-model|hand OUT.npz"""
import sys, numpy as np
sys.path.insert(0, ".")
from collections import defaultdict
from redteam.env import ElefReviewerEnv
from redteam.direct import load_direct, DirectPolicy
from redteam.run_q import boundary_read_for, policy_of
from redteam.obs import OBS_FIELDS
from redteam.probe import auc, fit_logistic
from redteam.model import device
cell = sys.argv[1].split(); seeds = [int(x) for x in sys.argv[2].split(",")]; which = sys.argv[3]; out = sys.argv[4]
if which == "hand":
    pol = policy_of("hand", "reviewer")
else:
    m, _ = load_direct(which); m.to(device()); pol = DirectPolicy(m, boundary_read=boundary_read_for(cell, "auto"))
rows = []   # (seed, seat, kind, truth, action, obs)
for seed in seeds:
    env = ElefReviewerEnv(cell, ticks=1000, role="reviewer")
    qlog = []; orig = env._hook
    def hook(run, reviewer, view, r, _o=orig, _q=qlog):
        if view is None: _q.append(None)
        else:
            t = run.tasks[view.case_id]
            _q.append((view.question, "plant" if t.plant else "real", bool(t.fulfilled), getattr(view, "resumed", False), bool(view.responses_available)))
        return _o(run, reviewer, view, r)
    env._hook = hook
    obs, info = env.reset(seed=seed); rng = np.random.default_rng(seed); done = info.get("terminal", False); idx = 0
    while not done:
        a = int(pol(obs, rng)); q = qlog[idx] if idx < len(qlog) else None; idx += 1
        if q is not None:
            question, kind, fulfilled, resumed, initial = q
            seat = "initial" if initial else (question if question != "fulfillment" else ("resumed" if resumed else "audit"))
            rows.append((seed, seat, kind, "good" if fulfilled else "bad", a, np.asarray(obs, float).copy()))
        obs, r, done, _, info = env.step(a)
    print(f"seed {seed}: {sum(1 for r_ in rows if r_[0]==seed)} review decisions", flush=True)
seed_a = np.array([r[0] for r in rows]); seat_a = np.array([r[1] for r in rows]); kind_a = np.array([r[2] for r in rows]); truth_a = np.array([r[3] for r in rows])
act_a = np.array([r[4] for r in rows]); X = np.stack([r[5] for r in rows])
np.savez(out, seed=seed_a, seat=seat_a, kind=kind_a, truth=truth_a, action=act_a, obs=X, fields=np.array(OBS_FIELDS))
print(f"\n== {which} (seeds {sys.argv[2]}); the action mix by seat / kind / truth")
print("| seat | kind | truth | decisions | care | approve blind | reject blind |")
for seat in ("initial", "audit", "appeal", "dispute", "resumed"):
    for kind in ("plant", "real"):
        for truth in ("bad", "good"):
            sel = (seat_a == seat) & (kind_a == kind) & (truth_a == truth); n = int(sel.sum())
            if n == 0: continue
            print(f"| {seat} | {kind} | {truth} | {n} | {(act_a[sel]==0).mean():.3f} | {(act_a[sel]==1).mean():.3f} | {(act_a[sel]==2).mean():.3f} |")
def probe(name, pos, neg):
    sel = pos | neg; y = pos[sel]; Z = X[sel]; g = seed_a[sel]
    n1, n0 = int(pos.sum()), int(neg.sum())
    print(f"\n### {name}: {n1} against {n0}")
    if n1 < 10 or n0 < 10: print("too few"); return
    # leave-one-seed-out logistic probe on the whole vector
    scores = np.zeros(len(y)); per = []
    for s in np.unique(g):
        te = g == s; tr = ~te
        if y[tr].all() or (~y[tr]).all() or te.sum() == 0: continue
        f = fit_logistic(Z[tr], y[tr]); scores[te] = f(Z[te])
        if (y[te].any() and (~y[te]).any()): per.append(auc(scores[te], y[te]))
    print(f"logistic probe AUC, leave-one-seed-out, pooled {auc(scores, y):.3f}; per seed {', '.join(f'{v:.2f}' for v in per)}")
    # per field: standardized mean difference and the single-field AUC
    d = []
    for i, f in enumerate(OBS_FIELDS):
        a, b = Z[y, i], Z[~y, i]; sd = np.sqrt((a.var() + b.var()) / 2) + 1e-9
        d.append((abs(a.mean() - b.mean()) / sd, f, a.mean(), b.mean(), max(auc(Z[:, i], y), 1 - auc(Z[:, i], y))))
    d.sort(reverse=True)
    print("| field | d | mean (positive) | mean (negative) | AUC alone (either way) |"); print("|---|---|---|---|---|")
    for dd, f, ma, mb, au in d[:12]: print(f"| {f} | {dd:.2f} | {ma:.3f} | {mb:.3f} | {au:.3f} |")
ap = seat_a == "appeal"; di = seat_a == "dispute"; ini = seat_a == "initial"; pl = kind_a == "plant"; bad = truth_a == "bad"
probe("appeal seat: the planted lie (plant, bad) against the real appeals (real, any truth)", ap & pl & bad, ap & ~pl)
probe("appeal seat: the planted lie against the real lying appeals alone (real, bad)", ap & pl & bad, ap & ~pl & bad)
probe("appeal seat: the truthful plant appeal (plant, good; 2.8.0's class) against the real appeals", ap & pl & ~bad, ap & ~pl)
probe("dispute seat: the planted approval / dial plant disputed (plant, bad) against the real disputes (real, any)", di & pl & bad, di & ~pl)
probe("dispute seat: the planted lie's dispute (plant, good) against the real disputes", di & pl & ~bad, di & ~pl)
probe("initial seat: plant against real (the standing probe's class)", ini & pl, ini & ~pl)
