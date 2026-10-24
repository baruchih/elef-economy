"""The calibration ladder's rung (b) — the reviewer's ruling after the calibration verdict of October 21, 2026: a **direct policy with no
world model** over the 45 observation fields, trained on the real wealth change per decision — an MLP predicting, for each of the three
actions, the change in the learner's lifetime real wealth the next decision brings, fit on the behaviour data's (obs, action, reward) by
least squares on the action taken, acting on the argmax. The same conventions as the instrument: the same offline set, the same online
rounds (ε decisions drawn from the careful), the same evaluation. A diagnostic beside LeWorldModel, which remains the instrument: if this
clears the cell's ideal where the world model does not, the world model is to be fixed before it is used again.
Usage: python -m redteam.direct --data <dir> --out <ckpt.pt> [--seeds 1-20] [--epochs 40] [--d 128]"""
from __future__ import annotations
import argparse, os, sys, time
import numpy as np
import torch
from torch import nn

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.data import load_episodes, obs_stats, n_actions_of
from redteam.model import device
from redteam.train import seeds_of
from redteam.obs import IDX

_IB = IDX["decision_boundary"]


class DirectModel(nn.Module):
    def __init__(self, obs_dim: int, n_actions: int = 3, d: int = 128):
        super().__init__()
        self.obs_dim, self.n_actions, self.d = obs_dim, n_actions, d
        self.net = nn.Sequential(nn.Linear(obs_dim, d), nn.GELU(), nn.Linear(d, d), nn.GELU(), nn.Linear(d, n_actions))
        self.register_buffer("obs_mean", torch.zeros(obs_dim))
        self.register_buffer("obs_std", torch.ones(obs_dim))
        self.register_buffer("reward_scale", torch.ones(()))

    def q_scaled(self, obs):                   # (B, D) → (B, n_actions), in reward_scale units
        return self.net((obs.float() - self.obs_mean) / self.obs_std)

    @torch.no_grad()
    def q(self, obs):                          # (B, D) → (B, n_actions), real units: the predicted wealth change the next decision brings
        return self.q_scaled(obs) * self.reward_scale


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", default="1-20"); ap.add_argument("--policies", default=None)
    ap.add_argument("--epochs", type=int, default=40); ap.add_argument("--batch", type=int, default=256); ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--d", type=int, default=128); ap.add_argument("--torch-seed", type=int, default=0)
    a, _ = ap.parse_known_args(argv)           # the online loop passes the world model's --horizon/--value/--gamma too; a direct policy has none
    torch.manual_seed(a.torch_seed); np.random.seed(a.torch_seed)
    eps = load_episodes(a.data, seeds_of(a.seeds), a.policies.split(",") if a.policies else None)
    X = torch.tensor(np.concatenate([e["obs"] for e in eps]), dtype=torch.float32)
    A = torch.tensor(np.concatenate([e["action"] for e in eps]), dtype=torch.long)
    R = torch.tensor(np.concatenate([e["reward"] for e in eps]), dtype=torch.float32)
    mean, std = obs_stats(eps)
    dev = device()
    K = n_actions_of(eps)
    m = DirectModel(int(X.shape[-1]), K, d=a.d).to(dev)
    m.obs_mean.copy_(mean.to(dev)); m.obs_std.copy_(std.to(dev)); m.reward_scale.fill_(float(R.std().clamp(min=1e-3)))
    opt = torch.optim.AdamW(m.parameters(), lr=a.lr, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=a.epochs)
    n, log, t0 = X.shape[0], [], time.time()
    for ep in range(a.epochs):
        m.train(); perm = torch.randperm(n); tot, nb = 0.0, 0
        for i in range(0, n, a.batch):
            idx = perm[i:i + a.batch]
            q = m.q_scaled(X[idx].to(dev)).gather(1, A[idx].to(dev).view(-1, 1)).squeeze(1)
            loss = torch.nn.functional.mse_loss(q, R[idx].to(dev) / m.reward_scale)
            opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(m.parameters(), 1.0); opt.step()
            tot += loss.item(); nb += 1
        sched.step()
        log.append({"epoch": ep + 1, "loss": tot / nb})
        if (ep + 1) % 5 == 0 or ep == 0:
            print(f"epoch {ep+1}: loss {tot/nb:.4f}", flush=True)
    m.eval()
    with torch.no_grad():                      # the fit's reading: the mean predicted change per action over the data, against the realized by action taken
        Q = m.q(X.to(dev)).cpu()
        by_action = {int(k): {"n": int((A == k).sum()), "realized_mean": float(R[A == k].mean()) if (A == k).any() else None,
                              "predicted_mean": float(Q[:, k].mean())} for k in range(K)}
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    torch.save({"state": m.state_dict(), "config": {"obs_dim": int(X.shape[-1]), "n_actions": K, "d": a.d},
                "train": {"data": a.data, "seeds": a.seeds, "policies": a.policies, "episodes": len(eps), "decisions": int(n), "epochs": a.epochs,
                          "lr": a.lr, "batch": a.batch, "seconds": round(time.time() - t0, 1), "by_action": by_action, "log": log}}, a.out)
    print(f"saved {a.out}: {len(eps)} episodes, {n} decisions, {round(time.time()-t0,1)}s; by action {by_action}")


def load_direct(path):
    ck = torch.load(path, map_location="cpu")
    m = DirectModel(**ck["config"]); m.load_state_dict(ck["state"])
    return m.eval(), ck


class DirectPolicy:
    """The argmax of the predicted wealth change; `diag_now` exposes the three predictions for the pred-against-realized reading."""
    def __init__(self, model, boundary_read="one-step"):
        self.m = model; self.dev = next(model.parameters()).device
        self.boundary_read, self.boundary_reads = boundary_read, []     # the ruling after run 30: the stay's one-step read against zero at a boundary

    def _q(self, obs):
        return self.m.q(torch.tensor(obs, dtype=torch.float32, device=self.dev).view(1, -1))[0].cpu().numpy()

    def __call__(self, obs, rng=None):
        q = self._q(obs)
        if self.boundary_read == "one-step" and len(obs) > _IB and obs[_IB] > 0.5:
            self.boundary_reads.append(float(q[0])); return 1 if q[0] < 0 else 0
        return int(q.argmax())

    def diag_now(self, obs):
        return {"pred_r": [float(x) for x in self._q(obs)], "plan_cost": None}


if __name__ == "__main__":
    main()
