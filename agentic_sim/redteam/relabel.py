"""The label recompute (the economy reviewer's ruling of November 6, 2026, Q2's second step): every stored episode of a chain — the offline
set and the online rounds — replayed by its own recorded actions (`chosen`) on the same seed, so the trajectory is the stored one, and
the attributed training reward computed on it under both name rules — the pooled construction the chain trained on (checked against the
stored `reward` to the decimal: the replay is the record) and own-name credit — written beside each other to a new data directory with the
seat of every decision from the environment's info, so a learner can be refit on the own-name labels and its argmax compared with the
stored model's on the same observations, by seat. Nothing stored is edited.
Usage: python -m redteam.relabel --data <chain data dir> --out <dir> [--seeds 1-20] [--policies careful,online10] [--ticks 1000] [--atol 1e-3] -- <cell args>"""
from __future__ import annotations
import argparse, glob, json, os, sys, time
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.env import ElefReviewerEnv
from redteam.attrib import attribute


def replay(env, seed, chosen):
    """Replay the episode by its recorded chosen actions; returns (obs (T, D), seats (T,), info) with info carrying both attributions."""
    obs, info = env.reset(seed=seed)
    O, S, K = [], [], []
    done = info.get("terminal", False); i = 0
    while not done:
        if i >= len(chosen):
            raise RuntimeError(f"the replay asked more decisions than the record holds ({len(chosen)})")
        O.append(obs); S.append(info.get("seat") or ("boundary" if info.get("boundary") else "?")); K.append(bool(info.get("is_plant", False)))
        obs, r, done, _, info = env.step(int(chosen[i])); i += 1
    if i != len(chosen):
        raise RuntimeError(f"the replay ended after {i} decisions; the record holds {len(chosen)}")
    return np.asarray(O, dtype=np.float32), np.asarray(S), np.asarray(K), info


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", default="1-20"); ap.add_argument("--policies", default=None, help="a subset of the stored policy names (careful, eps, …, online1 … online10)")
    ap.add_argument("--ticks", type=int, default=1000); ap.add_argument("--atol", type=float, default=1e-3, help="the tolerance on the stored (float32) pooled reward")
    ap.add_argument("--role", default="reviewer")
    ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    cell = [x for x in a.cell if x != "--"]
    lo, hi = (int(x) for x in a.seeds.split("-")) if "-" in a.seeds else (int(a.seeds), int(a.seeds))
    pols = set(a.policies.split(",")) if a.policies else None
    os.makedirs(a.out, exist_ok=True)
    try:
        env = ElefReviewerEnv(cell, ticks=a.ticks, role=a.role, attrib="pooled")
    except TypeError:                                                 # an earlier package (a worktree at the chain's own commit): the environment before the flag
        env = ElefReviewerEnv(cell, ticks=a.ticks, role=a.role)
    log = []; t0 = time.time()
    for f in sorted(glob.glob(os.path.join(a.data, "*-seed*.npz"))):
        z = np.load(f, allow_pickle=True)
        seed, policy = int(z["seed"]), str(z["policy"])
        if not (lo <= seed <= hi) or (pols is not None and policy not in pols):
            continue
        name = os.path.basename(f)
        if os.path.exists(os.path.join(a.out, name)):
            continue
        t1 = time.time()
        rec = {"file": name, "policy": policy, "seed": seed, "decisions": int(len(z["chosen"]))}
        try:
            O, S, K, info = replay(env, seed, z["chosen"])
        except Exception as ex:
            rec["error"] = repr(ex); log.append(rec); print(json.dumps(rec), flush=True); continue
        run = env.run
        lineages = [[x] for x in run.learner_chain] if getattr(run, "learner_pop", None) else None
        pooled, sp = attribute(run, env._marks, env._decisions, work_side=env.work_side, lineages=lineages, own_name=False)
        own, so = attribute(run, env._marks, env._decisions, work_side=env.work_side, lineages=lineages, own_name=True)
        stored = np.asarray(z["reward"], dtype=np.float64)
        d_obs = float(np.abs(O - z["obs"]).max()) if O.shape == z["obs"].shape else float("inf")
        d_rew = float(np.abs(pooled - stored).max()) if len(pooled) == len(stored) else float("inf")
        rec.update({"obs_max_abs_diff": d_obs, "pooled_max_abs_diff": d_rew, "reproduced": bool(d_obs == 0.0 and d_rew <= a.atol),
                    "pooled_sum": float(pooled.sum()), "own_sum": float(own.sum()), "pre_boundary_pooled": sp["pre_boundary_real"], "pre_boundary_own": so["pre_boundary_real"],
                    "changed": int((np.abs(pooled - own) > 1e-9).sum()), "seconds": round(time.time() - t1, 1)})
        np.savez_compressed(os.path.join(a.out, name), obs=O, action=z["action"], chosen=z["chosen"], reward=own.astype(np.float32), pooled=pooled.astype(np.float32),
                            stored_reward=z["reward"], is_plant=z["is_plant"], fulfilled=z["fulfilled"], t=z["t"], realized=z["realized"], lifetime=z["lifetime"], seed=seed,
                            policy=policy, role=z["role"] if "role" in z.files else a.role, n_actions=z["n_actions"] if "n_actions" in z.files else 3,
                            slot=z["slot"] if "slot" in z.files else np.zeros(len(own), dtype=np.int64), seat=S, is_plant_env=K)
        log.append(rec); print(json.dumps(rec), flush=True)
        json.dump({"cell": cell, "data": a.data, "ticks": a.ticks, "seconds": round(time.time() - t0, 1), "episodes": log}, open(os.path.join(a.out, "relabel.json"), "w"), indent=1)
    env.close()
    n = len(log); rep = sum(1 for r in log if r.get("reproduced"))
    print(f"{n} episodes, {rep} reproduced to the decimal (obs identical, pooled within {a.atol}); {round(time.time() - t0, 1)}s", flush=True)


if __name__ == "__main__":
    main()
