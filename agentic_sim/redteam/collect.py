"""Offline trajectories for the world model (the build plan: careful, stamper, careful with ε = 0.2 random actions, uniform random, on
seeds 1–20 by default). One file per (policy, seed) under <out>/<policy>-seed<N>.npz: obs (T, D), action (T,), reward (T,) — the attributed training reward since the
ruling after the ladder, the realized change beside it as realized (T,) — is_plant (T,), fulfilled (T,), t (T,) and the episode's lifetime
real wealth. Usage: python -m redteam.collect --out results/redteam/Q2/offline
[--seeds 1-20] [--policies careful,stamper,eps,random,leaver] [--rules 2.6.0] -- <cell args>"""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.env import ElefReviewerEnv, policy_of, default_policies


def rollout(env, policy, seed, rng):
    obs, info = env.reset(seed=seed)
    O, A, C, R, P, F, T, ID = [], [], [], [], [], [], [], []
    done = info.get("terminal", False)
    while not done:
        a = policy(obs, rng)
        O.append(obs); C.append(a); P.append(info.get("is_plant", False)); F.append(info.get("fulfilled", True)); T.append(info.get("t", 0)); ID.append(str(info.get("identity")))
        obs, r, done, _, info = env.step(a)
        A.append(info.get("action_effected", a))        # version 4: the action effected (a refused leave is a stay); the choice kept in C
        R.append(r)
    # the ruling after the ladder: the training reward is the attributed one (the realized kept beside it as `realized`)
    R_real = np.array(R, dtype=np.float32)
    attr = info.get("attributed")
    R_use = np.array(attr, dtype=np.float32) if attr is not None and len(attr) == len(R) else R_real
    names = sorted(set(ID))
    info = dict(info, realized_rewards=R_real, action_chosen=np.array(C, dtype=np.int64), slot=np.array([names.index(x) for x in ID], dtype=np.int64))   # the population: the slot of each decision
    return (np.array(O, dtype=np.float32).reshape(-1, obs.shape[-1]), np.array(A, dtype=np.int64), R_use,
            np.array(P, dtype=bool), np.array(F, dtype=bool), np.array(T, dtype=np.int64), info)


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", default="1-20")
    ap.add_argument("--policies", default=None, help="by role: careful,stamper,eps,random,leaver (the reviewer; version 3 added the leaver) / careful,zero,eps,random,leaver (Q3's deliverer)")
    ap.add_argument("--role", choices=["reviewer", "deliverer", "pair", "child", "parent", "bidder", "requester"], default="reviewer", help="Q3: `deliverer` — the slot's quality decisions (0 well, 1 badly at zero effort)")
    ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("--hide", default="", help="observation fields zeroed (comma-separated), e.g. own_p_eff for Q1's hidden-odds cell")
    ap.add_argument("--attrib", choices=["own", "pooled"], default="own", help="the attribution's name rule (November 6, 2026): own-name credit, or run 32's pooled construction (the shared-purse cell)")
    ap.add_argument("cell", nargs=argparse.REMAINDER, help="the stamping driver's cell arguments after --")
    a = ap.parse_args(argv)
    cell = [x for x in a.cell if x != "--"]
    lo, hi = (int(x) for x in a.seeds.split("-")) if "-" in a.seeds else (int(a.seeds), int(a.seeds))
    os.makedirs(a.out, exist_ok=True)
    env = ElefReviewerEnv(cell, ticks=a.ticks, hide=tuple(x for x in a.hide.split(",") if x), role=a.role, attrib=a.attrib)
    summary = []
    t0 = time.time()
    for name in (a.policies or default_policies(a.role)).split(","):
        pol = policy_of(name, a.role)
        for seed in range(lo, hi + 1):
            rng = np.random.default_rng(seed * 1000 + hash(name) % 997)
            O, A, R, P, F, T, info = rollout(env, pol, seed, rng)
            np.savez_compressed(os.path.join(a.out, f"{name}-seed{seed}.npz"), obs=O, action=A, chosen=info["action_chosen"], reward=R, is_plant=P, fulfilled=F, t=T,
                                realized=info.get("realized_rewards", R), lifetime=info.get("lifetime_real_wealth", float("nan")), seed=seed, policy=name,
                                role=a.role, n_actions=env.n_actions, slot=info["slot"])
            summary.append({"policy": name, "seed": seed, "decisions": int(len(A)), "lifetime_real_wealth": info.get("lifetime_real_wealth"),
                            "plants": int(P.sum()), "error": info.get("error")})
            print(f"{name} seed {seed}: {len(A)} decisions, lifetime {info.get('lifetime_real_wealth', float('nan')):.1f}, plants {int(P.sum())}" + (f" ERROR {info['error']}" if info.get("error") else ""), flush=True)
    env.close()
    json.dump({"cell": cell, "ticks": a.ticks, "hide": a.hide, "role": a.role, "attrib": a.attrib, "n_actions": env.n_actions, "seconds": round(time.time() - t0, 1), "episodes": summary},
              open(os.path.join(a.out, "summary.json"), "w"), indent=1)


if __name__ == "__main__":
    main()
