"""The label recompute's reading (the economy reviewer's ruling of November 6, 2026, Q2's second step): on a chain's relabelled set
(redteam.relabel — every stored episode replayed by its actions, the pooled label the chain trained on and the own-name label beside it,
the seat of every decision), (1) the labels by seat and action under both rules — what a decision was credited with, and the pooled purse's
part of it; (2) the learners refit on each label set with the chain's own settings — the direct policy, and the world model read by the head
alone — and their argmax compared decision by decision on the same observations, by seat: the share that changes between the two label rules,
beside the share that changes between two refits on the same (pooled) labels, the refit's own noise; the stored model of the chain beside.
Usage: python -m redteam.relabel_read --data <relabel dir> --out <dir> [--stored-direct <pt>] [--stored-wm <pt>] [--wm on|off] [--epochs 40] [--stride 4] [--seeds 1-20]"""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.data import load_episodes
from redteam.direct import main as D_main, load_direct
from redteam.train import main as T_main, load_model, seeds_of
from redteam.model import device

SEATS = ("initial", "audit", "panel", "resumed")
ACTS = ("care", "approve blind", "reject blind")


def seat_from_obs(X):
    """The seat kind from the observation's own fields (the view's question, the responses available, the resumed flag) — what the 2.9.0
    environment's info names; the 2.7.0 chain's environment (the worktree at its commit) carried no `seat`, so its replay reads it here."""
    from redteam.obs import IDX
    init = X[:, IDX["rv_responses_available"]] > 0.5; ful = X[:, IDX["rv_q_fulfillment"]] > 0.5; res = X[:, IDX["rv_resumed"]] > 0.5; bnd = X[:, IDX["decision_boundary"]] > 0.5
    out = np.where(bnd, "boundary", np.where(init, "initial", np.where(~ful, "panel", np.where(res, "resumed", "audit"))))
    return out.astype(object)


def load_relabelled(root, seeds):
    import glob
    O, A, R_own, R_pool, S, K = [], [], [], [], [], []
    for f in sorted(glob.glob(os.path.join(root, "*-seed*.npz"))):
        z = np.load(f, allow_pickle=True)
        if int(z["seed"]) not in seeds:
            continue
        O.append(z["obs"]); A.append(z["action"]); R_own.append(z["reward"]); R_pool.append(z["pooled"]); S.append(z["seat"].astype(object)); K.append(z["is_plant"])
    X, S = np.concatenate(O), np.concatenate(S)
    derived = seat_from_obs(X); known = S != "?"
    agree = float((derived[known] == S[known]).mean()) if known.any() else None
    S = np.where(known, S, derived).astype(str)
    print(f"seats: {int(known.sum())} from the environment's info, {int((~known).sum())} derived from the observation; agreement where both {agree}", flush=True)
    return X, np.concatenate(A), np.concatenate(R_own).astype(np.float64), np.concatenate(R_pool).astype(np.float64), S, np.concatenate(K), agree


@torch.no_grad()
def direct_q(m, X, bs=8192):
    m.to(device()); out = []
    for i in range(0, len(X), bs):
        out.append(m.q(torch.tensor(X[i:i + bs], dtype=torch.float32, device=device())).cpu().numpy())
    return np.concatenate(out)


@torch.no_grad()
def wm_head_q(m, X, bs=2048):
    """The head alone over the latent at a review decision: the review-side head's predicted change per action (the planner's no-horizon read)."""
    m.to(device()); dev = device(); out = []
    for i in range(0, len(X), bs):
        o = torch.tensor(X[i:i + bs], dtype=torch.float32, device=dev).unsqueeze(1)          # (B, 1, D)
        z = m.encode(o)
        qs = []
        for k in range(m.n_actions):
            oh = torch.nn.functional.one_hot(torch.full((o.shape[0], 1), k, dtype=torch.long, device=dev), m.n_actions).float()
            qs.append(m.reward(z, m.act_now(oh, o))[:, 0] * m.reward_scale)
        out.append(torch.stack(qs, -1).cpu().numpy())
    return np.concatenate(out)


def mix(arg, sel):
    n = int(sel.sum())
    return [float((arg[sel] == k).mean()) if n else None for k in range(3)]


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--stored-direct", default=None); ap.add_argument("--stored-wm", default=None)
    ap.add_argument("--wm", choices=["on", "off"], default="on"); ap.add_argument("--seeds", default="1-20")
    ap.add_argument("--epochs", type=int, default=40); ap.add_argument("--stride", type=int, default=4); ap.add_argument("--horizon", type=int, default=16)
    ap.add_argument("--torch-seed", type=int, default=0)
    a = ap.parse_args(argv)
    os.makedirs(a.out, exist_ok=True); t0 = time.time()
    seeds = seeds_of(a.seeds)
    X, A, R_own, R_pool, S, K, agree = load_relabelled(a.data, seeds)
    review = S != "boundary"
    rep = {"data": a.data, "decisions": int(len(A)), "review_decisions": int(review.sum()), "seeds": a.seeds, "seat_agreement_info_vs_obs": agree}
    # (1) the labels by seat and action
    lab = {}
    for seat in SEATS + ("boundary",):
        sel = S == seat
        if not sel.any():
            continue
        row = {"n": int(sel.sum()), "changed_share": float((np.abs(R_own[sel] - R_pool[sel]) > 1e-6).mean()),
               "pooled_mean": float(R_pool[sel].mean()), "own_mean": float(R_own[sel].mean())}
        for k, an in enumerate(ACTS):
            s2 = sel & (A == k)
            row[an] = {"n": int(s2.sum()), "pooled_mean": float(R_pool[s2].mean()) if s2.any() else None, "own_mean": float(R_own[s2].mean()) if s2.any() else None,
                       "pooled_minus_own_mean": float((R_pool[s2] - R_own[s2]).mean()) if s2.any() else None}
        for kind, kk in (("plant", K), ("real", ~K)):
            s3 = sel & kk
            row[kind] = {"n": int(s3.sum()), "pooled_mean": float(R_pool[s3].mean()) if s3.any() else None, "own_mean": float(R_own[s3].mean()) if s3.any() else None}
        lab[seat] = row
    rep["labels"] = lab
    # (2) the refits: the direct on own and on pooled (the refit control), the stored beside
    train = ["--data", a.data, "--seeds", a.seeds, "--epochs", str(a.epochs), "--torch-seed", str(a.torch_seed)]
    paths = {"direct own": os.path.join(a.out, "direct-own.pt"), "direct pooled refit": os.path.join(a.out, "direct-pooled-refit.pt"), "direct pooled refit (seed 1)": os.path.join(a.out, "direct-pooled-refit-s1.pt")}
    if not os.path.exists(paths["direct own"]):
        D_main(train + ["--out", paths["direct own"], "--label", "reward"])
    if not os.path.exists(paths["direct pooled refit"]):
        D_main(train + ["--out", paths["direct pooled refit"], "--label", "pooled"])
    if not os.path.exists(paths["direct pooled refit (seed 1)"]):          # the refit's own noise: the same labels on another torch seed (seed 0 reproduces the stored fit exactly)
        D_main(train[:-1] + ["1", "--out", paths["direct pooled refit (seed 1)"], "--label", "pooled"])
    Q = {}
    for name, pth in paths.items():
        m, _ = load_direct(pth); Q[name] = direct_q(m, X)
    if a.stored_direct:
        m, _ = load_direct(a.stored_direct); Q["direct stored"] = direct_q(m, X)
    if a.wm == "on":
        wtrain = ["--data", a.data, "--seeds", a.seeds, "--epochs", str(a.epochs), "--horizon", str(a.horizon), "--value", "mc", "--gamma", "0.95", "--heads", "two", "--stride", str(a.stride), "--torch-seed", str(a.torch_seed)]
        wpaths = {"wm own": os.path.join(a.out, "wm-own.pt"), "wm pooled refit": os.path.join(a.out, "wm-pooled-refit.pt"), "wm pooled refit (seed 1)": os.path.join(a.out, "wm-pooled-refit-s1.pt")}
        if not os.path.exists(wpaths["wm own"]):
            T_main(wtrain + ["--out", wpaths["wm own"], "--label", "reward"])
        if not os.path.exists(wpaths["wm pooled refit"]):
            T_main(wtrain + ["--out", wpaths["wm pooled refit"], "--label", "pooled"])
        if not os.path.exists(wpaths["wm pooled refit (seed 1)"]):
            T_main(wtrain[:-1] + ["1", "--out", wpaths["wm pooled refit (seed 1)"], "--label", "pooled"])
        for name, pth in wpaths.items():
            m, _ = load_model(pth); Q[name] = wm_head_q(m, X)
        if a.stored_wm:
            m, _ = load_model(a.stored_wm); Q["wm stored"] = wm_head_q(m, X)
    arg = {n: q.argmax(1) for n, q in Q.items()}
    pairs = [("direct own", "direct pooled refit"), ("direct own", "direct stored"), ("direct pooled refit", "direct stored"), ("direct pooled refit (seed 1)", "direct pooled refit"),
             ("wm own", "wm pooled refit"), ("wm own", "wm stored"), ("wm pooled refit", "wm stored"), ("wm pooled refit (seed 1)", "wm pooled refit")]
    cmp = {}
    for seat in SEATS:
        sel = review & (S == seat)
        if not sel.any():
            continue
        row = {"n": int(sel.sum()), "mix": {n: mix(arg[n], sel) for n in arg}, "mix_plant": {n: mix(arg[n], sel & K) for n in arg}, "mix_real": {n: mix(arg[n], sel & ~K) for n in arg}}
        for x, y in pairs:
            if x in arg and y in arg:
                row[f"changed {x} vs {y}"] = float((arg[x][sel] != arg[y][sel]).mean())
                row[f"changed {x} vs {y} (plant)"] = float((arg[x][sel & K] != arg[y][sel & K]).mean()) if (sel & K).any() else None
        cmp[seat] = row
    sel = review
    cmp["all review"] = {"n": int(sel.sum()), "mix": {n: mix(arg[n], sel) for n in arg}, **{f"changed {x} vs {y}": float((arg[x][sel] != arg[y][sel]).mean()) for x, y in pairs if x in arg and y in arg}}
    rep["argmax"] = cmp; rep["seconds"] = round(time.time() - t0, 1)
    json.dump(rep, open(os.path.join(a.out, "relabel-read.json"), "w"), indent=1)
    # the tables
    L = [f"# The label recompute on `{a.data}` (seeds {a.seeds}; {rep['decisions']} decisions, {rep['review_decisions']} at review seats)\n",
         "The pooled label (the construction the chain trained on) and the own-name label on the same decisions, by seat and by the action taken: the mean credit, and the pooled purse's part — pooled minus own — per decision.\n",
         "| seat | decisions | label changed (share) | mean pooled | mean own | " + " | ".join(f"{an}: n / pooled / own / pooled − own" for an in ACTS) + " | plant: n / pooled / own | real: n / pooled / own |", "|---|---|---|---|---|" + "---|" * (len(ACTS) + 2)]
    f3 = lambda v: "—" if v is None else f"{v:.2f}"
    for seat, row in lab.items():
        L.append(f"| {seat} | {row['n']} | {row['changed_share']:.3f} | {row['pooled_mean']:.2f} | {row['own_mean']:.2f} | " + " | ".join(f"{row[an]['n']} / {f3(row[an]['pooled_mean'])} / {f3(row[an]['own_mean'])} / {f3(row[an]['pooled_minus_own_mean'])}" for an in ACTS)
                 + f" | {row['plant']['n']} / {f3(row['plant']['pooled_mean'])} / {f3(row['plant']['own_mean'])} | {row['real']['n']} / {f3(row['real']['pooled_mean'])} / {f3(row['real']['own_mean'])} |")
    L.append("\nThe argmax by seat on the same observations: the action mix (care / approve blind / reject blind) each model chooses over every decision at the seat, and the share of decisions whose argmax differs between two models — own-name against the pooled refit (the label rule's effect), own-name against the stored model, the pooled refit against the stored model (the same labels and torch seed: zero where the fit is deterministic, or the data differ from the stored model's), and a second pooled refit on another torch seed against the first (two fits of the same labels: the refit's own noise, the floor any difference must clear).\n")
    names = list(arg.keys())
    L.append("| seat | decisions | " + " | ".join(f"{n}: mix" for n in names) + " | " + " | ".join(f"{x} vs {y}" for x, y in pairs if x in arg and y in arg) + " |"); L.append("|---|---|" + "---|" * (len(names) + sum(1 for x, y in pairs if x in arg and y in arg)))
    fm = lambda m: "—" if m[0] is None else " / ".join(f"{v:.3f}" for v in m)
    for seat, row in cmp.items():
        L.append(f"| {seat} | {row['n']} | " + " | ".join(fm(row['mix'][n]) for n in names) + " | " + " | ".join(f"{row[f'changed {x} vs {y}']:.3f}" for x, y in pairs if f"changed {x} vs {y}" in row) + " |")
    L.append("\nThe same mix on the plants alone and on the real cases alone at each seat:\n")
    L.append("| seat | " + " | ".join(f"{n}: plant / real" for n in names) + " |"); L.append("|---|" + "---|" * len(names))
    for seat in SEATS:
        if seat in cmp:
            L.append(f"| {seat} | " + " | ".join(f"{fm(cmp[seat]['mix_plant'][n])} — {fm(cmp[seat]['mix_real'][n])}" for n in names) + " |")
    open(os.path.join(a.out, "relabel-read.md"), "w").write("\n".join(L) + "\n"); print("\n".join(L))


if __name__ == "__main__":
    main()
