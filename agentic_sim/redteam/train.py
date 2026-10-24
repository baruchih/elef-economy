"""Train the world model on the offline episodes. Usage: python -m redteam.train --data results/redteam/Q2/offline-2.6.0 --out <ckpt.pt>
[--seeds 1-20] [--horizon 8] [--epochs 40] [--lam 0.05] [--d 64] [--value off|mc|td --gamma 0.95]. Records the losses per epoch beside the
checkpoint. `--value` trains the terminal value head (decision 5's named variant; Q1 onward) and the planner reads it at the horizon's end."""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.model import WorldModel, device
from redteam.data import load_episodes, windows, obs_stats, n_actions_of
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
    ap.add_argument("--value", choices=["off", "mc", "td"], default="off", help="the terminal value head: off (Q2's planner), mc (the discounted return-to-go), td (bootstrapped)")
    ap.add_argument("--gamma", type=float, default=0.95, help="the discount per decision for the value head and the planner's sum")
    ap.add_argument("--heads", choices=["one", "two"], default="two", help="version 4: `two` — a review-side head and a boundary head on the latent; `one` is version 3's single head")
    ap.add_argument("--kind-actions", choices=["on", "off"], default="off", help="the kind-conditioned action (the ruling after run 29; Q5's parent): the action one-hot over kind × action")
    a = ap.parse_args(argv)
    torch.manual_seed(a.torch_seed); np.random.seed(a.torch_seed)
    eps = load_episodes(a.data, seeds_of(a.seeds), a.policies.split(",") if a.policies else None)
    K = n_actions_of(eps)                                            # 3 for the reviewer, 2 for Q3's deliverer
    O, A, R, G, D = windows(eps, a.horizon, n_actions=K, gamma=a.gamma)
    mean, std = obs_stats(eps)
    dev = device()
    obs_dim = int(O.shape[-1])                                       # the data's width (44 before the boundary field, 45 after)
    heads = a.heads if obs_dim > 44 else "one"                      # data without the boundary field has one kind of decision
    kind_actions = a.kind_actions == "on"
    m = WorldModel(obs_dim, K, d=a.d, horizon=a.horizon, value_mode=a.value, gamma=a.gamma, side_heads=heads, kind_actions=kind_actions).to(dev)
    m.obs_mean.copy_(mean.to(dev)); m.obs_std.copy_(std.to(dev))
    if heads == "two":                                               # each head in its own units: the review side's and the boundary side's scale
        b = (O[:, :-1, 44] > 0.5).float()
        rr, rb = R * (1 - b), R * b
        m.reward_scale.fill_(float(rr.std().clamp(min=1e-3))); m.reward_scale_b.fill_(float(rb.std().clamp(min=1e-3)))
    else:
        m.reward_scale.fill_(float(R.std().clamp(min=1e-3)))
    opt = torch.optim.AdamW(m.parameters(), lr=a.lr, weight_decay=1e-4)
    sched = torch.optim.lr_scheduler.CosineAnnealingLR(opt, T_max=a.epochs)
    n = O.shape[0]
    log = []
    t0 = time.time()
    for ep in range(a.epochs):
        m.train()
        perm = torch.randperm(n)
        tot, parts = 0.0, {"pred": 0.0, "sigreg": 0.0, "reward": 0.0, "value": 0.0, "reward_b": 0.0, "value_b": 0.0}
        nb = 0
        for i in range(0, n, a.batch):
            idx = perm[i:i + a.batch]
            loss, p = m.loss(O[idx].to(dev), A[idx].to(dev), R[idx].to(dev), a.lam, ret=G[idx].to(dev), done=D[idx].to(dev))
            opt.zero_grad(); loss.backward(); torch.nn.utils.clip_grad_norm_(m.parameters(), 1.0); opt.step()
            tot += loss.item(); nb += 1
            for k in parts: parts[k] += p.get(k, 0.0)
        sched.step()
        rec = {"epoch": ep + 1, "loss": tot / nb, **{k: v / nb for k, v in parts.items()}}
        log.append(rec)
        if (ep + 1) % 5 == 0 or ep == 0:
            print(f"epoch {ep+1}: loss {rec['loss']:.4f} pred {rec['pred']:.4f} sigreg {rec['sigreg']:.4f} reward {rec['reward']:.4f} value {rec['value']:.4f}"
                  + (f" reward_b {rec.get('reward_b', 0):.4f} value_b {rec.get('value_b', 0):.4f}" if heads == "two" else ""), flush=True)
    os.makedirs(os.path.dirname(a.out) or ".", exist_ok=True)
    torch.save({"state": m.state_dict(), "config": {"obs_dim": obs_dim, "n_actions": K, "d": a.d, "horizon": a.horizon, "value_mode": a.value, "gamma": a.gamma, "side_heads": heads,
                                                   "kind_actions": kind_actions},
                "train": {"data": a.data, "seeds": a.seeds, "policies": a.policies, "episodes": len(eps), "windows": int(n), "epochs": a.epochs, "role": eps[0].get("role", "reviewer"),
                          "lam": a.lam, "lr": a.lr, "batch": a.batch, "value": a.value, "gamma": a.gamma, "heads": heads, "kind_actions": kind_actions,
                          "reward_scale": float(m.reward_scale), "reward_scale_b": float(m.reward_scale_b), "seconds": round(time.time() - t0, 1), "log": log}}, a.out)
    print(f"saved {a.out}: {len(eps)} episodes, {n} windows, {round(time.time()-t0,1)}s")


def load_model(path):
    ck = torch.load(path, map_location="cpu")
    m = WorldModel(**ck["config"])
    missing, unexpected = m.load_state_dict(ck["state"], strict=False)
    assert not unexpected and all(k.startswith("value_head.") or k == "reward_scale_b" for k in missing), (missing, unexpected)   # Q2's checkpoints predate the value head (off); version 3's the boundary scale
    return m.eval(), ck


if __name__ == "__main__":
    main()
