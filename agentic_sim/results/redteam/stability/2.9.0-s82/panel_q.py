"""§54: the learned reviewer's action by the panel's question (appeal | dispute) and by case kind — is the panel stamp rate one number or two?
Usage: panel_q.py "<cell>" seeds direct-model"""
import sys, numpy as np
from collections import defaultdict
from redteam.env import ElefReviewerEnv
from redteam.direct import load_direct, DirectPolicy
from redteam.model import device
cell = sys.argv[1].split(); seeds = [int(x) for x in sys.argv[2].split(",")]; dm = sys.argv[3]
m, _ = load_direct(dm); m.to(device())
agg = defaultdict(lambda: [0, 0, 0, 0])   # (question, kind) -> counts of actions 0/1/2, n
won = defaultdict(int)
for seed in seeds:
    env = ElefReviewerEnv(cell, ticks=1000, role="reviewer")
    qlog = []
    orig = env._hook
    def hook(run, reviewer, view, r, _o=orig, _q=qlog):
        _q.append(None if view is None else (view.question, "plant" if run.tasks[view.case_id].plant else "real", bool(run.tasks[view.case_id].fulfilled), getattr(view, "resumed", False), bool(view.responses_available)))
        return _o(run, reviewer, view, r)
    env._hook = hook
    obs, info = env.reset(seed=seed); rng = np.random.default_rng(seed); p = DirectPolicy(m)
    done = info.get("terminal", False); idx = 0
    while not done:
        a = int(p(obs, rng))
        q = qlog[idx] if idx < len(qlog) else None; idx += 1
        if q is not None:
            question, kind, fulfilled, resumed, initial = q
            seat = "initial" if initial else (question if question != "fulfillment" else ("resumed" if resumed else "audit"))
            key = (seat, kind, "good" if fulfilled else "bad")
            if 0 <= a < 3: agg[key][a] += 1
            agg[key][3] += 1
        obs, r, done, _, info = env.step(a)
    row = env.run.row(1000)
    for k in ("disputes_filed", "disputes_won", "appeals_filed", "appeals_won", "plant_disputes_filed", "plant_appeals_filed", "false_approvals", "plant_fail_dispute", "plant_fail_appeal", "plant_adj_dispute", "plant_adj_appeal", "plant_fail_audit", "plant_adj_audit", "plant_fail_third", "plant_adj_third", "rulings"):
        won[k] += float(row.get(k, 0) or 0)
print(f"== {dm} (seeds {sys.argv[2]})")
print("| seat | kind | truth | decisions | care | approve blind (stamp) | reject blind |")
for key in sorted(agg):
    c0, c1, c2, n = agg[key]
    print(f"| {key[0]} | {key[1]} | {key[2]} | {n} | {c0/n:.3f} | {c1/n:.3f} | {c2/n:.3f} |")
print({k: round(v / len(seeds), 2) for k, v in won.items()})
