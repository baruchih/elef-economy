"""Train the world model on the offline episodes. Usage: python -m redteam.train --data results/redteam/Q2/offline-2.6.0 --out <ckpt.pt>
[--seeds 1-20] [--horizon 8] [--epochs 40] [--lam 0.05] [--d 64]. Records the losses per epoch beside the checkpoint."""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.model import WorldModel, device
from redteam.data import load_episodes, windows, obs_stats
from redteam.obs import OBS_DIM


def seeds_of(spec):
    lo, hi = (int(x) for x in spec.split("-")) if "-" in spec else (int(spec), int(spec))
    return set(range(lo, hi + 1))


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", default="1-20"); ap.add_argument("--policies", default=None)
    ap.add_argument("--horizon", type=int, default=8); ap.add_argument("--epochs", type=int, default=40)
    ap.add_argument("--batch", type=int, default=256); ap.add_argument("--lr", type=float, default=1e-3)
    ap.add_argument("--lam", type=float, default=0.05); ap.add_argument("--d", type=int, default=64)
    ap.add_argument("--torch-seed", type=int, default=0)
    a = ap.parse_args(argv)
    torch.manual_seed(a.torch_seed); np.random.seed(a.torch_seed)
    eps = load_episodes(a.data, seeds_of(a.seeds), a.policies.split(",") if a.policies else None)
    O, A, R = windows(eps, a.horizon)
    mean, std = obs_stats(eps)
    dev = device()
    m = WorldModel(OBS_DIM, 3, d=a.d, horizon=a.horizon).to(dev)
    m.obs_mean.copy_(mean.to(dev)); m.obs_std.copy_(std.to(dev))
    m.reward_scale.fill_(float(R.std().clamp(min=1e-3)))
    opt = torch.optim.AdamW(m.parameters(), lr=a.lr, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=a.epochs)
    n = O.shape[0]
    log = []
    t0 = time.time()
    for ep in range(a.epochs):
        m.train()
        perm = torch.randperm(n)
        tot, parts = 0.0, {"pred": 0.0, "sigreg": 0.0, "reward": 0.0}
        nb = 0
        for i in range(0, n, a.batch):
            idx = perm[i:i + a.batch]
            loss, p = m.loss(O[idx].to(dev), A[idx].to(dev), R[idx].to(dev), a.lam)
            opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(m.parameters(), 1.0); opt.step()
            tot += loss.item(); nb += 1
            for k in parts: parts[k] += p[k]
        sched.step()
        rec = {"epoch": ep + 1, "loss": tot / nb, **{k: v / nb for k, v in parts.items()}}
        log.append(rec)
        if (ep + 1) % 5 == 0 or ep == 0:
            print(f"epoch {ep+1}: loss {rec['loss']:.4f} pred {rec['pred']:.4f} sigreg {rec['sigreg']:.4f} reward {rec['reward']:.4f}", flush=True)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    torch.save({"state": m.state_dict(), "config": {"obs_dim": OBS_DIM, "n_actions": 3, "d": a.d, "horizon": a.horizon},
                "train": {"data": a.data, "seeds": a.seeds, "policies": a.policies, "episodes": len(eps), "windows": int(n), "epochs": a.epochs,
                          "lam": a.lam, "lr": a.lr, "batch": a.batch, "seconds": round(time.time() - t0, 1), "log": log}}, a.out)
    print(f"saved {a.out}: {len(eps)} episodes, {n} windows, {round(time.time()-t0,1)}s")


def load_model(path):
    ck = torch.load(path, map_location="cpu")
    m = WorldModel(**ck["config"])
    m.load_state_dict(ck["state"])
    return m.eval(), ck


if __name__ == "__main__":
    main()
