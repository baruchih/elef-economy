"""The learned reviewer: model-predictive control over the learner's decisions — the Cross-Entropy Method over categorical action
sequences (LeWM's planner, on one-hot actions), the cost minus the predicted sum of wealth changes over the horizon, the first action
executed and the plan redone at the next decision (receding horizon). Written to the stable-worldmodel cost contract so its solvers can
stand in; the solver here is the package's own so the loop has no dependency the study cannot read."""
from __future__ import annotations
import numpy as np
import torch


class CategoricalCEM:
    def __init__(self, model, horizon=8, n_actions=3, samples=256, iters=6, topk=32, smoothing=0.3, seed=0, device=None):
        self.m, self.H, self.K, self.S, self.iters, self.topk, self.smooth = model, horizon, n_actions, samples, iters, topk, smoothing
        self.rng = np.random.default_rng(seed)
        self.dev = device or next(model.parameters()).device

    def plan(self, obs_now):
        probs = np.full((self.H, self.K), 1.0 / self.K)
        obs_t = torch.tensor(obs_now, dtype=torch.float32, device=self.dev).unsqueeze(0)
        best_a, best_c = None, np.inf
        for _ in range(self.iters):
            seqs = np.empty((self.S, self.H), dtype=np.int64)
            for h in range(self.H):
                seqs[:, h] = self.rng.choice(self.K, size=self.S, p=probs[h])
            onehot = torch.nn.functional.one_hot(torch.tensor(seqs), self.K).float().unsqueeze(0).to(self.dev)   # (1, S, H, K)
            cost = self.m.get_cost({"obs": obs_t}, onehot)[0].cpu().numpy()                                    # (S,)
            elite = seqs[np.argsort(cost)[: self.topk]]
            if cost.min() < best_c:
                best_c, best_a = float(cost.min()), seqs[int(np.argmin(cost))].copy()
            freq = np.stack([np.bincount(elite[:, h], minlength=self.K) / len(elite) for h in range(self.H)])
            probs = (1 - self.smooth) * freq + self.smooth * probs
        # the planner's cost by first action (the diagnostic ladder's reading): the best plan with its first action swapped for each
        alt = np.stack([best_a] * self.K); alt[np.arange(self.K), 0] = np.arange(self.K)
        onehot = torch.nn.functional.one_hot(torch.tensor(alt), self.K).float().unsqueeze(0).to(self.dev)
        self.last_first_costs = [float(x) for x in self.m.get_cost({"obs": obs_t}, onehot)[0].cpu().numpy()]
        return int(best_a[0]), best_a, best_c


def reward_now(model, obs):
    """The wealth head's predicted change in real wealth for each action from this observation (real units). Version 4 (two heads): the head
    of the decision's kind — the review-side head at a review, the boundary head at a boundary."""
    dev = next(model.parameters()).device
    with torch.no_grad():
        o = torch.tensor(obs, dtype=torch.float32, device=dev).view(1, 1, -1)
        z = model.encode(o)
        head, scale = model.reward, model.reward_scale
        if getattr(model, "side_heads", "one") == "two" and bool(model.is_boundary(o[0, 0])):
            head, scale = model.reward_b, model.reward_scale_b
        r = torch.stack([head(z, model.act(torch.nn.functional.one_hot(torch.tensor([[k]]), model.n_actions).float().to(dev)))[0, 0]
                         for k in range(model.n_actions)]) * scale
    return [float(x) for x in r.cpu().numpy()]


class LearnedPolicy:
    """The planner as a policy for the environment and the collector: one decision at a time. `diag_now` (after a decision) gives the
    wealth head's predicted change per action and the planner's cost per first action — the ladder's pred-against-realized reading."""
    def __init__(self, model, horizon=8, **kw):
        self.m = model
        self.cem = CategoricalCEM(model, horizon=horizon, **kw)
        self.trace = []

    def __call__(self, obs, rng=None):
        a, seq, c = self.cem.plan(obs)
        self.trace.append((a, c))
        return a

    def diag_now(self, obs):
        return {"pred_r": reward_now(self.m, obs), "plan_cost": list(getattr(self.cem, "last_first_costs", []) or [])}


class GreedyPolicy:
    """One step of the wealth head: the action with the highest predicted change now (the no-horizon control; under version 4's stopping
    rule, the head alone over the latent — the review-side head at a review, the boundary head at a boundary — is the planner if the CEM does not clear)."""
    def __init__(self, model):
        self.m = model; self.dev = next(model.parameters()).device

    def __call__(self, obs, rng=None):
        return int(np.argmax(reward_now(self.m, obs)))

    def diag_now(self, obs):
        return {"pred_r": reward_now(self.m, obs), "plan_cost": None}
