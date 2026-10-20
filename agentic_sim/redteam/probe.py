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


def auc_se(scores, labels, groups=None, n_boot=1000, seed=0):
    """The AUC with a bootstrap standard error (the reviewer's instruction after run 22): over the decisions resampled with replacement,
    and, when `groups` (the decision's seed) is given, over the seeds resampled whole — the decisions of one run are not independent, so
    the seed-level figure is the resolution the study has. Returns [auc, se_decisions, se_seeds]."""
    s, y = np.asarray(scores, float), np.asarray(labels, bool)
    a0 = auc(s, y)
    rng = np.random.default_rng(seed)
    bs = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(s), len(s))
        v = auc(s[idx], y[idx])
        if v == v:
            bs.append(v)
    out = [a0, float(np.std(bs, ddof=1)) if len(bs) > 1 else float("nan")]
    if groups is not None:
        g = np.asarray(groups)
        uniq = np.unique(g)
        members = {u: np.flatnonzero(g == u) for u in uniq}
        cs = []
        for _ in range(n_boot):
            pick = rng.choice(uniq, size=len(uniq), replace=True)
            idx = np.concatenate([members[u] for u in pick])
            v = auc(s[idx], y[idx])
            if v == v:
                cs.append(v)
        out.append(float(np.std(cs, ddof=1)) if len(cs) > 1 else float("nan"))
    return out


def auc_gap_se(scores_a, scores_b, labels, groups, n_boot=1000, seed=0):
    """The difference AUC(a) − AUC(b) with paired bootstrap standard errors: the same resample of decisions, then of seeds, scores both."""
    sa, sb, y = np.asarray(scores_a, float), np.asarray(scores_b, float), np.asarray(labels, bool)
    g0 = auc(sa, y) - auc(sb, y)
    rng = np.random.default_rng(seed)
    bs = []
    for _ in range(n_boot):
        idx = rng.integers(0, len(y), len(y))
        v = auc(sa[idx], y[idx]) - auc(sb[idx], y[idx])
        if v == v:
            bs.append(v)
    g = np.asarray(groups); uniq = np.unique(g); members = {u: np.flatnonzero(g == u) for u in uniq}
    cs = []
    for _ in range(n_boot):
        pick = rng.choice(uniq, size=len(uniq), replace=True)
        idx = np.concatenate([members[u] for u in pick])
        v = auc(sa[idx], y[idx]) - auc(sb[idx], y[idx])
        if v == v:
            cs.append(v)
    return [g0, float(np.std(bs, ddof=1)) if len(bs) > 1 else float("nan"), float(np.std(cs, ddof=1)) if len(cs) > 1 else float("nan")]


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
    ap.add_argument("--initial-only", action="store_true", help="restrict to the initial reviews (rv_responses_available), where plants are received")
    ap.add_argument("--policies", default="careful,stamper,eps,random",
                    help="the behaviour policies' episodes to read (comma-separated; the four offline policies by default — an online run writes "
                         "its rounds' episodes beside the offline ones, and the probe names its episodes from run 24; 'all' reads every file)")
    ap.add_argument("--ablate-case", action="store_true", help="the per-field ablation of the case's fields (alone, added to the context, removed from the raw)")
    a = ap.parse_args(argv)
    m, ck = load_model(a.model)
    pols = None if a.policies in (None, "", "all") else a.policies.split(",")
    tr, te = load_episodes(a.data, seeds_of(a.train_seeds), pols), load_episodes(a.data, seeds_of(a.test_seeds), pols)
    if a.initial_only:
        for e in tr + te:
            keep = e["obs"][:, IDX["rv_responses_available"]] > 0.5
            e["obs"], e["is_plant"] = e["obs"][keep], e["is_plant"][keep]
    def stack(eps, f):
        return np.concatenate([f(e) for e in eps], 0)
    Ztr, Zte = stack(tr, lambda e: latents(m, e["obs"])), stack(te, lambda e: latents(m, e["obs"]))
    Otr, Ote = stack(tr, lambda e: e["obs"]), stack(te, lambda e: e["obs"])
    ytr, yte = stack(tr, lambda e: e["is_plant"]), stack(te, lambda e: e["is_plant"])
    gte = stack(te, lambda e: np.full(len(e["is_plant"]), e["seed"]))      # the decision's seed, for the seed-level bootstrap
    out = {"data": a.data, "model": a.model, "policies": pols or "all", "train_seeds": a.train_seeds, "test_seeds": a.test_seeds,
           "episodes_train": len(tr), "episodes_test": len(te),
           "initial_only": a.initial_only, "train_decisions": int(len(ytr)), "test_decisions": int(len(yte)),
           "plant_share_test": float(yte.mean())}
    out["auc_latent"] = auc_se(fit_logistic(Ztr, ytr)(Zte), yte, gte)       # every AUC as [value, SE over decisions, SE over seeds]
    out["auc_raw_obs"] = auc_se(fit_logistic(Otr, ytr)(Ote), yte, gte)
    # the base-rate check: a probe on the context alone (the market, the dial, own standing — fields that move the plant RATE, not the case)
    # against a probe on the case's own fields (the ReviewView and the seen set); a leak is a separation the case's fields carry
    from redteam.obs import OBS_FIELDS
    width = Otr.shape[1]                                                   # the data's width (44 before the boundary field)
    fields = list(enumerate(OBS_FIELDS[:width]))
    ctx = [i for i, f in fields if not (f.startswith("rv_") or f.startswith("seen_") or f == "my_bid_lost")]
    case = [i for i, f in fields if f.startswith("rv_") or f.startswith("seen_") or f == "my_bid_lost"]
    s_ctx = fit_logistic(Otr[:, ctx], ytr)(Ote[:, ctx])
    out["auc_context_only"] = auc_se(s_ctx, yte, gte)
    out["auc_case_fields_only"] = auc_se(fit_logistic(Otr[:, case], ytr)(Ote[:, case]), yte, gte)
    # the reviewer's criterion after run 23: what the case adds beyond the context — the gap raw − context, paired (the same resamples
    # score both probes), as [gap, SE over decisions, SE over seeds]; the case adds nothing when the gap is within two seed-level SE of zero
    out["auc_gap_raw_minus_context"] = auc_gap_se(fit_logistic(Otr, ytr)(Ote), s_ctx, yte, gte)
    if a.ablate_case:
        # the build plan's ablation, by field (§6): for each of the case's fields, its own AUC, what it adds to the context alone
        # (AUC(context + f) − AUC(context), paired), and what the whole observation loses without it (AUC(raw − f) − AUC(raw), paired);
        # the field that closes the gap is the finding
        s_raw = fit_logistic(Otr, ytr)(Ote)
        abl = {}
        for i, f in fields:
            if i not in case:
                continue
            s_plus = fit_logistic(Otr[:, ctx + [i]], ytr)(Ote[:, ctx + [i]])
            keep = [j for j in range(width) if j != i]
            s_minus = fit_logistic(Otr[:, keep], ytr)(Ote[:, keep])
            abl[f] = {"alone": auc_se(Ote[:, i], yte, gte), "added_to_context": auc_gap_se(s_plus, s_ctx, yte, gte),
                      "removed_from_raw": auc_gap_se(s_minus, s_raw, yte, gte)}
        out["case_field_ablation"] = abl
    # the per-field view, the strongest first (|AUC − 0.5|)
    per = {f: auc(Ote[:, i], yte) for i, f in fields}
    out["fields_top"] = sorted(((round(max(v, 1 - v), 3), f, round(v, 3)) for f, v in per.items() if v == v), reverse=True)[:8]
    sb = IDX["seen_before"]
    out["auc_seen_before"] = auc_se(-Ote[:, sb], yte, gte)                    # unseen → more likely a plant, if the leak were there
    out["auc_rv_gap"] = auc_se(-Ote[:, IDX["rv_gap"]], yte, gte)
    print(json.dumps(out, indent=1))
    if a.out:
        json.dump(out, open(a.out, "w"), indent=1)
    return out


if __name__ == "__main__":
    main()
