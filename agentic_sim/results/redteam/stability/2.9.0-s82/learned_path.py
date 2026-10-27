"""The learned population's (and the run_q hand's) dial-per-seat path per period under 2.9.0 on seeds 21–23: the direct final model on the
careful basin's cell, the hand beside — the engine's period records read at the episode's end."""
import sys, numpy as np
sys.path.insert(0, ".")
from redteam.env import ElefReviewerEnv
from redteam.direct import load_direct, DirectPolicy
from redteam.run_q import boundary_read_for, policy_of
from redteam.model import device
cell = ["--entry-pool", "20", "--stampers", "0.6", "--learner-pop", "all", "--learner-role", "reviewer", "--learner-exit", "rule"]
model = sys.argv[1]; seeds = [int(x) for x in sys.argv[2].split(",")]
br = boundary_read_for(cell, "auto")
env = ElefReviewerEnv(cell, ticks=1000, role="reviewer")
dm, _ = load_direct(model); dm.to(device())
pols = {"direct": DirectPolicy(dm, boundary_read=br), "hand": policy_of("hand", "reviewer")}
rng = np.random.default_rng(0)
def f(x, d=3): return "—" if x in (None, "—") else (f"{x:.{d}f}" if isinstance(x, float) else str(x))
for name, pol in pols.items():
    for s in seeds:
        obs, info = env.reset(seed=s); done = info.get("terminal", False)
        while not done:
            a = pol(obs, rng); obs, r, done, _, info = env.step(a)
        per = env.run.w.dial()["periods"]
        print(f"\n== {name} seed {s}  periods {len(per)}  (model {model})")
        print("| p | t | real approvals | pa posted / verdicts | pa audit adj / confirmed | F̂^A | m^A before → after | π^A | real appeals | lie quota a / d | lies filed a / d | lie adj a / d | lie sided a / d | F̂^La | F̂^Ld | m^La | m^Ld | F̂ | m_t |")
        print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
        for i, p in enumerate(per):
            g = lambda k, d="—": p.get(k, d)
            lq = g("lie_quota", {}) or {}; lf = g("lies_filed", {}) or {}; la = g("lie_adj", {}) or {}; ls = g("lie_sided", {}) or {}
            print(f"| {i} | {g('t')} | {g('real_approvals')} | {g('pa_posted')} / {g('pa_verdicts')} | {g('pa_audit_adj')} / {g('pa_audit_confirmed')} | {f(g('F_hat_A'))} | {f(g('m_A_before'),2)} → {f(g('m_A'),2)} | {f(g('pi_A'))} | {g('real_appeals')} | {f(lq.get('appeal'),1)} / {f(lq.get('dispute'),1)} | {lf.get('appeal','—')} / {lf.get('dispute','—')} | {la.get('appeal','—')} / {la.get('dispute','—')} | {ls.get('appeal','—')} / {ls.get('dispute','—')} | {f(g('F_hat_La'))} | {f(g('F_hat_Ld'))} | {f(g('m_La'),2)} | {f(g('m_Ld'),2)} | {f(g('F_hat'))} | {f(g('m'),2) if 'm' in p else f(g('m_t'),2)} |")
        sys.stdout.flush()
