"""The Q2 probe: can a linear reader of the world model's latent tell a plant from real work? Train a logistic probe on the latents of
the training seeds' decisions, score it on held-out seeds; the same on the raw observation (the baseline) and on the single field
`seen_before`. Reported as AUC (chance 0.5). Usage: python -m redteam.probe --data <offline dir> --model <ckpt> [--train-seeds 1-10] [--test-seeds 11-20]"""
from __future__ import annotations
import argparse, json, os, sys
import numpy as np
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.data import load_episodes
from redteam.train import load_model, seeds_of
from redteam.obs import IDX


def auc(scores, labels):
    s, y = np.asarray(scores, float), np.asarray(labels, bool)
    if y.all() or (~y).all():
        return float("nan")
    order = np.argsort(s)
    ranks = np.empty(len(s)); ranks[order] = np.arange(1, len(s) + 1)
    n1, n0 = y.sum(), (~y).sum()
    return float((ranks[y].sum() - n1 * (n1 + 1) / 2) / (n1 * n0))


def fit_logistic(X, y, epochs=300, lr=0.05, l2=1e-3):
    X = torch.tensor(X, dtype=torch.float32); y = torch.tensor(y, dtype=torch.float32)
    mu, sd = X.mean(0), X.std(0) + 1e-6
    Xn = (X - mu) / sd
    w = torch.zeros(X.shape[1], requires_grad=True); b = torch.zeros(1, requires_grad=True)
    opt = torch.optim.Adam([w, b], lr=lr)
    pos = y.mean().clamp(1e-3, 1 - 1e-3)
    weight = torch.where(y > 0.5, 1.0 / pos, 1.0 / (1 - pos))          # class-balanced
    for _ in range(epochs):
        logit = Xn @ w + b
        loss = (torch.nn.functional.binary_cross_entropy_with_logits(logit, y, reduction="none") * weight).mean() + l2 * (w * w).sum()
        opt.zero_grad(); loss.backward(); opt.step()
    return lambda Z: ((torch.tensor(Z, dtype=torch.float32) - mu) / sd @ w + b).detach().numpy()


def latents(m, obs):
    with torch.no_grad():
        return m.encode(torch.tensor(obs, dtype=torch.float32).unsqueeze(0))[0].numpy()


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--model", required=True)
    ap.add_argument("--train-seeds", default="1-10"); ap.add_argument("--test-seeds", default="11-20")
    ap.add_argument("--out", default=None)
    a = ap.parse_args(argv)
    m, ck = load_model(a.model)
    tr, te = load_episodes(a.data, seeds_of(a.train_seeds)), load_episodes(a.data, seeds_of(a.test_seeds))
    def stack(eps, f):
        return np.concatenate([f(e) for e in eps], 0)
    Ztr, Zte = stack(tr, lambda e: latents(m, e["obs"])), stack(te, lambda e: latents(m, e["obs"]))
    Otr, Ote = stack(tr, lambda e: e["obs"]), stack(te, lambda e: e["obs"])
    ytr, yte = stack(tr, lambda e: e["is_plant"]), stack(te, lambda e: e["is_plant"])
    out = {"data": a.data, "model": a.model, "train_decisions": int(len(ytr)), "test_decisions": int(len(yte)),
           "plant_share_test": float(yte.mean())}
    out["auc_latent"] = auc(fit_logistic(Ztr, ytr)(Zte), yte)
    out["auc_raw_obs"] = auc(fit_logistic(Otr, ytr)(Ote), yte)
    # the base-rate check: a probe on the context alone (the market, the dial, own standing — fields that move the plant RATE, not the case)
    # against a probe on the case's own fields (the ReviewView and the seen set); a leak is a separation the case's fields carry
    from redteam.obs import OBS_FIELDS
    ctx = [i for i, f in enumerate(OBS_FIELDS) if not (f.startswith("rv_") or f.startswith("seen_") or f == "my_bid_lost")]
    case = [i for i, f in enumerate(OBS_FIELDS) if f.startswith("rv_") or f.startswith("seen_") or f == "my_bid_lost"]
    out["auc_context_only"] = auc(fit_logistic(Otr[:, ctx], ytr)(Ote[:, ctx]), yte)
    out["auc_case_fields_only"] = auc(fit_logistic(Otr[:, case], ytr)(Ote[:, case]), yte)
    # the per-field view, the strongest first (|AUC − 0.5|)
    per = {f: auc(Ote[:, i], yte) for i, f in enumerate(OBS_FIELDS)}
    out["fields_top"] = sorted(((round(max(v, 1 - v), 3), f, round(v, 3)) for f, v in per.items() if v == v), reverse=True)[:8]
    sb = IDX["seen_before"]
    out["auc_seen_before"] = auc(-Ote[:, sb], yte)                       # unseen → more likely a plant, if the leak were there
    out["auc_rv_gap"] = auc(-Ote[:, IDX["rv_gap"]], yte)
    print(json.dumps(out, indent=1))
    if a.out:
        json.dump(out, open(a.out, "w"), indent=1)
    return out


if __name__ == "__main__":
    main()
