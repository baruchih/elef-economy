"""The offline episodes (redteam.collect's npz files) as windows for the world model: obs (T+1), actions (T) one-hot, rewards (T)."""
from __future__ import annotations
import glob, os
import numpy as np
import torch


def load_episodes(root, seeds=None, policies=None):
    eps = []
    for f in sorted(glob.glob(os.path.join(root, "*-seed*.npz"))):
        z = np.load(f, allow_pickle=True)
        seed, policy = int(z["seed"]), str(z["policy"])
        if seeds is not None and seed not in seeds:
            continue
        if policies is not None and policy not in policies:
            continue
        eps.append({"obs": z["obs"], "action": z["action"], "reward": z["reward"], "is_plant": z["is_plant"], "fulfilled": z["fulfilled"],
                    "t": z["t"], "seed": seed, "policy": policy, "lifetime": float(z["lifetime"])})
    return eps


def windows(eps, horizon, n_actions=3):
    """Every window of horizon+1 observations with the horizon actions and rewards between them (stride 1)."""
    O, A, R = [], [], []
    for e in eps:
        T = len(e["action"])
        for s in range(0, T - horizon):
            O.append(e["obs"][s:s + horizon + 1]); A.append(e["action"][s:s + horizon]); R.append(e["reward"][s:s + horizon])
    if not O:
        return None
    O = torch.tensor(np.stack(O), dtype=torch.float32)
    A = torch.nn.functional.one_hot(torch.tensor(np.stack(A), dtype=torch.long), n_actions).float()
    R = torch.tensor(np.stack(R), dtype=torch.float32)
    return O, A, R


def obs_stats(eps):
    X = np.concatenate([e["obs"] for e in eps], axis=0)
    return torch.tensor(X.mean(0), dtype=torch.float32), torch.tensor(X.std(0) + 1e-6, dtype=torch.float32)
