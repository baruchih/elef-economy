"""The offline episodes (redteam.collect's npz files) as windows for the world model: obs (T+1), actions (T) one-hot, rewards (T)."""
from __future__ import annotations
import glob, os
import numpy as np
import torch


def load_episodes(root, seeds=None, policies=None, label="reward"):
    """`label` names the npz key read as the training reward: `reward` (the file's own — the attributed reward of its collection), or, in a
    relabelled set (redteam.relabel), `pooled` for the construction the chain trained on beside the own-name labels in `reward`."""
    eps = []
    for f in sorted(glob.glob(os.path.join(root, "*-seed*.npz"))):
        z = np.load(f, allow_pickle=True)
        seed, policy = int(z["seed"]), str(z["policy"])
        if seeds is not None and seed not in seeds:
            continue
        if policies is not None and policy not in policies:
            continue
        eps.append({"obs": z["obs"], "action": z["action"], "reward": z[label], "is_plant": z["is_plant"], "fulfilled": z["fulfilled"],
                    "t": z["t"], "seed": seed, "policy": policy, "lifetime": float(z["lifetime"]), "slot": z["slot"] if "slot" in z.files else None,
                    "n_actions": int(z["n_actions"]) if "n_actions" in z.files else 3, "role": str(z["role"]) if "role" in z.files else "reviewer"})
    return eps


def n_actions_of(eps):
    """The action count the episodes were collected under (3 for the reviewer, 2 for Q3's deliverer; one value across the set)."""
    ks = {e.get("n_actions", 3) for e in eps}
    assert len(ks) == 1, ks
    return ks.pop()


def returns_to_go(rewards, gamma):
    """G_t = Σ_{k ≥ t} γ^{k−t} r_k over the episode, with G_T = 0 after the last reward (an episode ends when the run ends or the
    learner departs; nothing is earned after)."""
    G = np.zeros(len(rewards) + 1, dtype=np.float32)
    for t in range(len(rewards) - 1, -1, -1):
        G[t] = rewards[t] + gamma * G[t + 1]
    return G


def split_by_side(e, boundary_idx=44):
    """Version 4: an episode's rewards by the decision's kind — (review side, boundary side), each zero on the other kind's decisions. Data
    without the boundary field (Q2's) is all review side."""
    r = np.asarray(e["reward"], dtype=np.float32)
    if e["obs"].shape[-1] <= boundary_idx:
        return r, np.zeros_like(r)
    b = (e["obs"][:len(r), boundary_idx] > 0.5).astype(np.float32)
    return r * (1 - b), r * b


def by_slot(eps):
    """The learned population (the ruling after run 32): an episode's decisions interleave the slots; the world model's windows run along one slot's
    own sequence, so an episode with a `slot` array is split into one sub-episode per slot. Episodes without it pass through."""
    out = []
    for e in eps:
        sl = e.get("slot")
        if sl is None or len(sl) == 0:
            out.append(e); continue
        for k in np.unique(sl):
            idx = np.where(sl == k)[0]
            out.append({**e, "obs": e["obs"][idx], "action": e["action"][idx], "reward": e["reward"][idx], "is_plant": e["is_plant"][idx], "fulfilled": e["fulfilled"][idx], "t": e["t"][idx], "slot": None})
    return out


def windows(eps, horizon, n_actions=3, gamma=0.95, stride=1):
    """Every window of horizon+1 observations with the horizon actions and rewards between them (stride 1); beside them the discounted
    return-to-go at each of the horizon+1 positions — by side since version 4, (…, 2) = [review, boundary]; a one-head model sums them —
    and the episode's-end flag (1 at the last observation, which has no successor — the terminal value's targets). An episode shorter than
    the horizon contributes nothing."""
    O, A, R, G, D = [], [], [], [], []
    for e in by_slot(eps):
        T = len(e["action"])
        rr, rb = split_by_side(e)
        g = np.stack([returns_to_go(rr, gamma), returns_to_go(rb, gamma)], axis=-1)      # (T+1, 2)
        for s in range(0, T - horizon, max(1, int(stride))):
            O.append(e["obs"][s:s + horizon + 1]); A.append(e["action"][s:s + horizon]); R.append(e["reward"][s:s + horizon])
            G.append(g[s:s + horizon + 1])
            d = np.zeros(horizon + 1, dtype=np.float32); d[-1] = 1.0 if s + horizon == T - 1 else 0.0   # the last obs of the episode sits at the window's end
            D.append(d)
    if not O:
        return None
    O = torch.tensor(np.stack(O), dtype=torch.float32)
    A = torch.nn.functional.one_hot(torch.tensor(np.stack(A), dtype=torch.long), n_actions).float()
    R = torch.tensor(np.stack(R), dtype=torch.float32)
    return O, A, R, torch.tensor(np.stack(G), dtype=torch.float32), torch.tensor(np.stack(D), dtype=torch.float32)


def obs_stats(eps):
    X = np.concatenate([e["obs"] for e in eps], axis=0)
    return torch.tensor(X.mean(0), dtype=torch.float32), torch.tensor(X.std(0) + 1e-6, dtype=torch.float32)
