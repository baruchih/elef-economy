"""What the learner with a horizon does that no scripted read tried (addendum 10's J5; November 13, 2026; notes §111): the final policies of the horizon chains rolled
out on the evaluation seeds (21–40) without exploration, every decision kept with its seat, its slot's standing from the observation (a member in good standing;
on probation or undetermined — the odds pinned; the own-standing fields), the slot's record (bad plants met, suspensions) and the decision's position in the slot's
life (the tick over the slot's ticks in place) — and the claims tallied by seat, by standing, by the slot's suspensions so far, by the life's quarter, and by the
standing false approvals' odds band. Usage: horizon_claims.py OUT.md  (from agentic_sim/ in the elef-redteam env)"""
import json, os, sys, numpy as np, torch
sys.path.insert(0, os.getcwd())
from redteam.env import ElefReviewerEnv
from redteam.obs import IDX
from redteam.train import load_model
from redteam.direct import load_direct, DirectPolicy
from redteam.plan import GreedyPolicy
from redteam.model import device
H = "results/redteam/stability/ablation-A1/stress/learned/horizon"
BASE = "--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1".split()
ARM = {"pa10": "--pi-a0 0.10 --pi-a-max 0.10".split(), "arm4": ["--arm", "4"]}
FIELDS = [k for k in ("own_member", "own_probationer", "own_suspended", "own_p_eff", "own_plant_bad_n", "own_plant_failures", "own_ticks_since_admission", "own_reviews", "own_awards") if k in IDX]
L = ["# The horizon learners' claims: when, at which seat, at what standing, how late in a slot's life (the finals' policies rolled out on seeds 21–40, no exploration)\n",
     f"Standing fields read from the observation: {', '.join(FIELDS)}.\n"]
for k in ("pa10", "arm4"):
    for lrn, sub, mk in (("direct", "direct", "direct-online-10.pt"), ("wm (return head)", "wm-ret", "wm-online-10.pt")):
        mp = f"{H}/{k}-t1-b1-mc/{sub}/models/{mk}"
        if not os.path.exists(mp): L.append(f"## {k}, {lrn}: (pending)\n"); continue
        if sub == "direct":
            m, _ = load_direct(mp); m.to(device()); pol = DirectPolicy(m, boundary_read="one-step")
        else:
            m, _ = load_model(mp); m.to(device()); pol = GreedyPolicy(m, boundary_read="one-step")
        env = ElefReviewerEnv(BASE + ARM[k], ticks=1000, role="reviewer", attrib="own")
        rec = []                                                  # (seat, action, member, probation, p_eff, bad_plants, suspensions, life_pos)
        slots_life = {}
        for seed in range(21, 41):
            obs, info = env.reset(seed=seed); rng = np.random.default_rng(seed); done = info.get("terminal", False); buf = []
            while not done:
                a = int(pol(obs, rng)); seat = info.get("seat") or "boundary"; ident = str(info.get("identity")); t = int(info.get("t", 0))
                buf.append((seed, ident, t, seat, a, *[float(obs[IDX[f]]) for f in FIELDS]))
                obs, r, done, _, info = env.step(a)
            S = json.loads(info["row"]["learner_slots_json"])
            for row in buf:
                v = S.get(row[1]); t_in = (v["t_in"] if v else 0); t_out = (v["t_out"] if v and v["t_out"] is not None else 1000)
                rec.append(row + (((row[2] - t_in) / max(1, t_out - t_in)),))
        env.close()
        R = np.array([r[4:] for r in rec], dtype=float); seats = np.array([r[3] for r in rec]); act = R[:, 0]; F = {f: R[:, 1 + i] for i, f in enumerate(FIELDS)}; life = R[:, -1]
        claim = act == 3; n = len(act)
        L.append(f"## {k}, {lrn} — {n} decisions on 20 seeds, claims {claim.mean():.3f}\n")
        L.append("| by | class | decisions | claim rate | care | approve blind | reject blind |"); L.append("|---|---|---|---|---|---|---|")
        def row(name, cls, m):
            if m.sum(): L.append(f"| {name} | {cls} | {int(m.sum())} | **{(act[m] == 3).mean():.3f}** | {(act[m] == 0).mean():.3f} | {(act[m] == 1).mean():.3f} | {(act[m] == 2).mean():.3f} |")
        for s in ("initial", "audit", "panel", "resumed"): row("seat", s, seats == s)
        if "own_member" in F and "own_probationer" in F:
            row("standing", "a member in good standing", (F["own_member"] > 0.5)); row("standing", "a probationer", (F["own_probationer"] > 0.5))
            for s in ("initial", "audit"):
                row(f"standing at the {s} seat", "member", (F["own_member"] > 0.5) & (seats == s)); row(f"standing at the {s} seat", "probationer", (F["own_probationer"] > 0.5) & (seats == s))
        if "own_p_eff" in F:
            for lo, hi in ((0, 0.5), (0.5, 0.99), (0.99, 1.01)): row("own audit odds", f"[{lo}, {hi})", (F["own_p_eff"] >= lo) & (F["own_p_eff"] < hi))
        if "own_plant_failures" in F:
            for v in (0, 1, 2): row("plant failures in the record", f"{v}" if v < 2 else "2 or more", (F["own_plant_failures"] == v) if v < 2 else (F["own_plant_failures"] >= 2))
        if "own_plant_bad_n" in F:
            for lo, hi in ((0, 1), (1, 3), (3, 99)): row("bad plants in the window", f"[{lo}, {hi})", (F["own_plant_bad_n"] >= lo) & (F["own_plant_bad_n"] < hi))
        if "own_ticks_since_admission" in F:
            for lo, hi in ((0, 100), (100, 300), (300, 1e9)): row("ticks since admission", f"[{lo:.0f}, {hi:.0f})", (F["own_ticks_since_admission"] >= lo) & (F["own_ticks_since_admission"] < hi))
        for q in range(4): row("quarter of the slot's life", f"{q + 1}", (life >= q / 4) & (life < (q + 1) / 4 + (1e-9 if q == 3 else 0)))
        for s in ("initial", "audit"):
            for q in range(4): row(f"quarter at the {s} seat", f"{q + 1}", (seats == s) & (life >= q / 4) & (life < (q + 1) / 4 + (1e-9 if q == 3 else 0)))
        L.append("")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
