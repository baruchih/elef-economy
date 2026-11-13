"""The learned reviewer: model-predictive control over the learner's decisions — the Cross-Entropy Method over categorical action
sequences (LeWM's planner, on one-hot actions), the cost minus the predicted sum of wealth changes over the horizon, the first action
executed and the plan redone at the next decision (receding horizon). Written to the stable-worldmodel cost contract so its solvers can
stand in; the solver here is the package's own so the loop has no dependency the study cannot read."""
from __future__ import annotations
import numpy as np
import torch


# -- the boundary read (the ruling after run 30, a construction correction, not planner work): without re-arrival a leave's value is zero by
# rule — the name's lifetime ends and nothing follows — so the boundary decision is the stay head's one-step read against zero: leave if the
# head predicts the stay's period negative, stay otherwise; the heads' own read of the leave code (trained by the few leaves effected) is not
# consulted. Under re-arrival (`--learner-rearrive on`) the fresh name's period is learned and the heads decide as before.
def at_boundary(model, obs):
    i = int(getattr(model, "boundary_idx", 44))
    return len(obs) > i and obs[i] > 0.5


def boundary_read_for(cell, flag="auto"):
    """`one-step` or `learned`: the flag as given, or by the cell (`auto`): learned when the cell allows re-arrival, one-step otherwise."""
    if flag in ("one-step", "learned"):
        return flag
    rearrive = any(x == "--learner-rearrive" and i + 1 < len(cell) and cell[i + 1] == "on" for i, x in enumerate(cell))
    return "learned" if rearrive else "one-step"


def boundary_one_step(model, obs, reads):
    stay = reward_now(model, obs)[0]                 # the boundary head's read of the stay (the period's reviewing income, real), against zero for the leave
    reads.append(float(stay))
    return 1 if stay < 0 else 0


class CategoricalCEM:
    def __init__(self, model, horizon=8, n_actions=None, samples=256, iters=6, topk=32, smoothing=0.3, seed=0, device=None):
        K = n_actions or getattr(model, "n_actions", 3)                 # the model's action count (3 the reviewer's, 2 Q3's deliverer)
        self.m, self.H, self.K, self.S, self.iters, self.topk, self.smooth = model, horizon, K, samples, iters, topk, smoothing
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
    of the decision's kind — the review-side head at a review, the boundary head at a boundary. The kind-conditioned action (the parent) reads
    the decision's kind from the observation."""
    dev = next(model.parameters()).device
    with torch.no_grad():
        o = torch.tensor(obs, dtype=torch.float32, device=dev).view(1, 1, -1)
        z = model.encode(o)
        head, scale = model.reward, model.reward_scale
        if getattr(model, "side_heads", "one") == "two" and bool(model.is_boundary(o[0, 0])):
            head, scale = model.reward_b, model.reward_scale_b
        r = torch.stack([head(z, model.act_now(torch.nn.functional.one_hot(torch.tensor([[k]]), model.n_actions).float().to(dev), o))[0, 0]
                         for k in range(model.n_actions)]) * scale                    # the kind-conditioned action reads the decision's kind from the observation
    return [float(x) for x in r.cpu().numpy()]


def value_read(model, obs):
    """The learner with a horizon (November 13, 2026): for each action, the reward head's one-decision read plus γ times the value head at the predicted
    next latent — the H-step return the heads were fit to; the review side's heads (a population cell has no boundary decision)."""
    dev = next(model.parameters()).device
    with torch.no_grad():
        o = torch.tensor(obs, dtype=torch.float32, device=dev).view(1, 1, -1)
        z = model.encode(o)
        out = []
        for k in range(model.n_actions):
            a = model.act_now(torch.nn.functional.one_hot(torch.tensor([[k]]), model.n_actions).float().to(dev), o)
            r = model.reward(z, a)[0, 0] * model.reward_scale
            z1 = model.predict(z, a)[:, -1:]
            v = model.value(z1)[0, 0] * model.reward_scale
            out.append(float((r + model.gamma * v).cpu()))
    return out


def horizon_read(model):
    """True where the head alone reads reward + γ V(next): a model fit to a return under the `value` read. Under the `direct` read the reward head is the return itself and is read alone."""
    return int(getattr(model, "return_horizon", 1)) != 1 and getattr(model, "value_mode", "off") != "off" and getattr(model, "return_read", "value") == "value"


class LearnedPolicy:
    """The planner as a policy for the environment and the collector: one decision at a time. `diag_now` (after a decision) gives the
    wealth head's predicted change per action and the planner's cost per first action — the ladder's pred-against-realized reading."""
    def __init__(self, model, horizon=8, boundary_read="one-step", **kw):
        self.m = model
        self.cem = CategoricalCEM(model, horizon=horizon, **kw)
        self.trace = []
        self.boundary_read, self.boundary_reads = boundary_read, []   # the ruling after run 30: the stay head's one-step read against zero at a boundary (the reads kept)

    def __call__(self, obs, rng=None):
        if self.boundary_read == "one-step" and at_boundary(self.m, obs):
            a = boundary_one_step(self.m, obs, self.boundary_reads); self.trace.append((a, None)); return a
        a, seq, c = self.cem.plan(obs)
        self.trace.append((a, c))
        return a

    def diag_now(self, obs):
        return {"pred_r": reward_now(self.m, obs), "plan_cost": list(getattr(self.cem, "last_first_costs", []) or [])}


class GreedyPolicy:
    """One step of the wealth head: the action with the highest predicted change now (the no-horizon control; under version 4's stopping
    rule, the head alone over the latent — the review-side head at a review, the boundary head at a boundary — is the planner if the CEM does not clear)."""
    def __init__(self, model, boundary_read="one-step"):
        self.m = model; self.dev = next(model.parameters()).device
        self.boundary_read, self.boundary_reads = boundary_read, []

    def __call__(self, obs, rng=None):
        if self.boundary_read == "one-step" and at_boundary(self.m, obs):
            return boundary_one_step(self.m, obs, self.boundary_reads)
        return int(np.argmax(self._read(obs)))

    def _read(self, obs):                      # the learner with a horizon: reward + γ V(next) where the model was fit to a return; the head alone otherwise
        return value_read(self.m, obs) if horizon_read(self.m) else reward_now(self.m, obs)

    def diag_now(self, obs):
        return {"pred_r": self._read(obs), "plan_cost": None}
