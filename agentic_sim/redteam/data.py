"""The offline episodes (redteam.collect's npz files) as windows for the world model: obs (T+1), actions (T) one-hot, rewards (T).

The learner with a horizon (Baruchi's ruling of November 13, 2026; brief A1 addendum 10, J5; the design notes §109 H4): a decision's training target is its
slot's own-name return — the discounted sum, along the slot's own sequence of decisions, of every later decision's attributed reward and of the slot's
unclaimed work-side events in the ticks between them (`unclaimed`, the attribution's export), over a horizon H of the slot's decisions (`mc`: to the slot's
exit — the run's end or its departure; nothing after). The suspension charge (the counterfactual on the plant failures) is dropped where the horizon
reaches the suspension itself — the income forgone is then read as it happens — and kept where it does not; at H = 1 the target is the stored reward,
so a horizon of 1 reproduces every chain of record to the decimal (`horizon_targets`, the regression test)."""
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
        n = len(z["action"])
        eps.append({"obs": z["obs"], "action": z["action"], "reward": z[label], "is_plant": z["is_plant"], "fulfilled": z["fulfilled"],
                    "t": z["t"], "seed": seed, "policy": policy, "lifetime": float(z["lifetime"]), "slot": z["slot"] if "slot" in z.files else None,
                    "n_actions": int(z["n_actions"]) if "n_actions" in z.files else 3, "role": str(z["role"]) if "role" in z.files else "reviewer",
                    "seat": z["seat"] if "seat" in z.files else None,
                    # the horizon's export (November 13, 2026); a record before it carries none — zeros, and the charge's tick −1
                    "unclaimed": z["unclaimed"] if "unclaimed" in z.files else np.zeros(n, dtype=np.float32),
                    "charge": z["charge"] if "charge" in z.files else np.zeros(n, dtype=np.float32),
                    "charge_t": z["charge_t"] if "charge_t" in z.files else np.full(n, -1, dtype=np.int64),
                    "has_export": bool("unclaimed" in z.files)})
    return eps


def parse_horizon(spec):
    """`1`, an integer H, or `mc` (None: to the slot's exit)."""
    s = str(spec).strip().lower()
    return None if s in ("mc", "inf", "life") else int(s)


def horizon_targets(e, horizon, gamma):
    """Along one slot's own sequence (an episode after `by_slot`): the per-decision reward label and the targets under the return horizon.
    Returns (rho, ret, value): `rho[i]` the one-decision reward the horizon learner reads — the attributed reward without the suspension charge, plus the
    slot's unclaimed events in the window after decision i, plus the charge where it is kept; `ret[i]` the H-step discounted return of rho from i (the
    direct policy's target); `value[i]` the (H − 1)-step return from i (the world model's value target at position i, so that rho[i] + γ value[i + 1] is
    ret[i]), with value[T] = 0 after the last decision. A charge on decision i is kept when the window of H decisions from i is whole and ends before the
    suspension's tick — the horizon does not reach it — and dropped otherwise (the income forgone then stands in the return as the awards that do not come).
    At horizon 1: rho = ret = the stored reward exactly, value = 0 (the chains of record; the world model's own value head is built by the caller then)."""
    r = np.asarray(e["reward"], dtype=np.float64); T = len(r)
    if horizon == 1:
        return r.copy(), r.copy(), np.zeros(T + 1, dtype=np.float64)
    ch = np.asarray(e["charge"], dtype=np.float64); ct = np.asarray(e["charge_t"]); u = np.asarray(e["unclaimed"], dtype=np.float64); t = np.asarray(e["t"])
    H = horizon
    base = r - ch + u
    keep = np.zeros(T, dtype=np.float64)
    if H is not None:
        for i in range(T):
            if ct[i] >= 0 and i + H - 1 <= T - 1 and t[i + H - 1] < ct[i]:
                keep[i] = ch[i]
    rho = base + keep
    def disc_sum(x, n_steps):                                   # Σ_{j < n_steps} γ^j x[i + j], truncated at the end; n_steps None = all
        G = np.zeros(len(x) + 1, dtype=np.float64)
        if n_steps is None:
            for i in range(len(x) - 1, -1, -1):
                G[i] = x[i] + gamma * G[i + 1]
            return G
        if n_steps <= 0:
            return G
        for i in range(len(x) - 1, -1, -1):
            G[i] = x[i] + gamma * G[i + 1] - (gamma ** n_steps) * (x[i + n_steps] if i + n_steps < len(x) else 0.0)
        return G
    ret = disc_sum(rho, H)[:T]
    value = disc_sum(rho, None if H is None else H - 1)
    return rho, ret, value


def targets_in_episode_order(e, horizon, gamma):
    """`horizon_targets` over each slot of an episode, scattered back into the episode's own decision order (so that at horizon 1 the direct policy's data
    is the chains of record's, decision for decision). Returns (rho, ret) of the episode's length."""
    T = len(e["action"]); rho = np.zeros(T, dtype=np.float64); ret = np.zeros(T, dtype=np.float64)
    sl = e.get("slot")
    groups = [np.arange(T)] if (sl is None or len(sl) == 0) else [np.where(sl == k)[0] for k in np.unique(sl)]
    for idx in groups:
        sub = {k: (np.asarray(e[k])[idx] if k in ("reward", "charge", "charge_t", "unclaimed", "t") else e[k]) for k in ("reward", "charge", "charge_t", "unclaimed", "t")}
        a, b, _ = horizon_targets(sub, horizon, gamma)
        rho[idx] = a; ret[idx] = b
    return rho, ret


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
            out.append({**e, "obs": e["obs"][idx], "action": e["action"][idx], "reward": e["reward"][idx], "is_plant": e["is_plant"][idx], "fulfilled": e["fulfilled"][idx], "t": e["t"][idx], "slot": None,
                        **{k2: e[k2][idx] for k2 in ("unclaimed", "charge", "charge_t", "seat") if e.get(k2) is not None}})
    return out


def windows(eps, horizon, n_actions=3, gamma=0.95, stride=1, return_horizon=1, return_gamma=0.98, return_read="value"):
    """Every window of horizon+1 observations with the horizon actions and rewards between them (stride 1); beside them the discounted
    return-to-go at each of the horizon+1 positions — by side since version 4, (…, 2) = [review, boundary]; a one-head model sums them —
    and the episode's-end flag (1 at the last observation, which has no successor — the terminal value's targets). An episode shorter than
    the horizon contributes nothing. Under a return horizon other than 1 (the learner with a horizon, November 13, 2026) the per-step reward is
    `horizon_targets`' rho and the value target its (H − 1)-step return at return_gamma, by side; at 1 the path of record, untouched."""
    O, A, R, G, D = [], [], [], [], []
    for e in by_slot(eps):
        T = len(e["action"])
        if return_horizon != 1:
            rho, ret, val = horizon_targets(e, return_horizon, return_gamma)
            e = {**e, "reward": (ret if return_read == "direct" else rho).astype(np.float32)}   # `direct`: the reward head fit to the H-step return itself (the known-answer test's second read, November 13, 2026)
            b = (e["obs"][:T, 44] > 0.5).astype(np.float64) if e["obs"].shape[-1] > 44 else np.zeros(T)
            side_b = np.append(b, 0.0)                                                   # the value target by side: the review side's where the decision is a review
            g = np.stack([val * (1 - side_b), val * side_b], axis=-1).astype(np.float32)   # (T+1, 2)
        else:
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
