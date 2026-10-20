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
        return int(best_a[0]), best_a, best_c


class LearnedPolicy:
    """The planner as a policy for the environment and the collector: one decision at a time."""
    def __init__(self, model, horizon=8, **kw):
        self.cem = CategoricalCEM(model, horizon=horizon, **kw)
        self.trace = []

    def __call__(self, obs, rng=None):
        a, seq, c = self.cem.plan(obs)
        self.trace.append((a, c))
        return a


class GreedyPolicy:
    """One step of the wealth head: the action with the highest predicted change now (the no-horizon control)."""
    def __init__(self, model):
        self.m = model; self.dev = next(model.parameters()).device

    def __call__(self, obs, rng=None):
        with torch.no_grad():
            o = torch.tensor(obs, dtype=torch.float32, device=self.dev).view(1, 1, -1)
            z = self.m.encode(o)
            r = torch.stack([self.m.reward(z, self.m.act(torch.nn.functional.one_hot(torch.tensor([[k]]), 3).float().to(self.dev)))[0, 0] for k in range(3)])   # scale-free: the argmax
            return int(r.argmax())
