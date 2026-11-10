"""The frozen head-alone policy at the audit seat, by the dial's level — what it reads when it turns to inspecting (the economy reviewer's
second read after notes §92, November 10, 2026; nothing built in the engine or the harness). The policy of record (`wm-online-10.pt`, the head
alone over the latent) is run frozen for 2,000 ticks in run 42's cell; every decision's observation (the 45 named fields), action, seat, case
kind and the dial's level at that tick are kept. Then, on the audit-seat decisions on real cases:
  - by band of m^A: the decisions, the blind rate (a verdict with no care), the head's predicted margin of care over the better blind verdict,
    and the mean of each field;
  - the attribution by clamping: the high-dial decisions (where the policy inspects) with one field — or one group of fields — replaced by
    draws of that field from the low-dial decisions (where it stamped), the policy asked again: the rise in its blind rate is what that field
    carries of the turn; the reverse clamp (low-dial decisions given the high-dial field) beside;
  - a rank AUC per field, care against blind, pooled and within the high band.
Usage: $PY results/redteam/stability/2.9.0-s82/audit_attrib.py --out <dir> --model <wm.pt> [--seeds 21-40] [--ticks 2000] -- <cell>
       … --analyze <dir>   (the tables again from the saved decisions)"""
import sys, os, json, argparse, time, glob
sys.path.insert(0, os.getcwd())
import numpy as np, torch
from redteam.env import ElefReviewerEnv
from redteam.train import load_model, seeds_of
from redteam.plan import GreedyPolicy, boundary_read_for
from redteam.run_q import device
from redteam.obs import OBS_FIELDS, IDX

GROUPS = {"the market (public)": OBS_FIELDS[:IDX["dial_m"]], "the dial and the period's position (public)": OBS_FIELDS[IDX["dial_m"]:IDX["own_wealth_real"]],
          "own standing and record": OBS_FIELDS[IDX["own_wealth_real"]:IDX["rv_gap"]], "the assignment": OBS_FIELDS[IDX["rv_gap"]:IDX["seen_before"]],
          "the seen set": OBS_FIELDS[IDX["seen_before"]:IDX["decision_boundary"]],
          "own penalties (overturned, plant failures)": ["own_overturned", "own_plant_failures"], "own odds alone": ["own_p_eff"],
          "own plant record (bad, good met)": ["own_plant_bad_n", "own_plant_good_n"]}
BANDS = [(1.0, 1.5, "m^A 1–1.5"), (1.5, 4.0, "1.5–4"), (4.0, 8.0, "4–8"), (8.0, 14.0, "8–14"), (14.0, 1e9, "14–20")]


def reward_batch(model, O):
    """The review-side head's predicted change per action for a batch of observations: (N, D) → (N, K)."""
    dev = next(model.parameters()).device
    with torch.no_grad():
        o = torch.tensor(np.asarray(O, np.float32), device=dev).unsqueeze(0)
        z = model.encode(o); K = model.n_actions; outs = []
        for k in range(K):
            oh = torch.nn.functional.one_hot(torch.full((1, o.shape[1]), k, dtype=torch.long), K).float().to(dev)
            outs.append(model.reward(z, model.act_now(oh, o))[0] * model.reward_scale)
        return torch.stack(outs, -1).cpu().numpy()


def collect(a, cell):
    br = boundary_read_for(cell, "auto"); m, ck = load_model(a.model); m.to(device())
    env = ElefReviewerEnv(cell, ticks=a.ticks, obs_dim=ck.get("config", {}).get("obs_dim"), role="reviewer", attrib="own")
    pol = GreedyPolicy(m, boundary_read=br); os.makedirs(a.out, exist_ok=True); t0 = time.time()
    for seed in sorted(seeds_of(a.seeds)):
        rng = np.random.default_rng(seed); obs, info = env.reset(seed=seed); done = info.get("terminal", False)
        O, A, S, P, T, MA, PA, MT = [], [], [], [], [], [], [], []
        while not done:
            W = env.run.w._w
            act = pol(obs, rng)
            O.append(np.array(obs, np.float32)); A.append(act); S.append(str(info.get("seat") or "boundary")); P.append(bool(info.get("is_plant", False)))
            T.append(int(info.get("t", W.t))); MA.append(float(W.m_A)); PA.append(float(W.pi_A)); MT.append(float(W.m_t))
            obs, r, done, _, info = env.step(act)
        np.savez_compressed(os.path.join(a.out, f"decisions-seed{seed}.npz"), obs=np.stack(O), action=np.array(A), seat=np.array(S), is_plant=np.array(P), t=np.array(T), m_A=np.array(MA), pi_A=np.array(PA), m_t=np.array(MT), seed=seed)
        au = [(s, p, x) for s, p, x in zip(S, P, A) if s == "audit" and not p]
        print(f"seed {seed}: {len(A)} decisions, {len(au)} audit seats on real cases, blind there {np.mean([x != 0 for _, _, x in au]) if au else float('nan'):.3f}, m^A at the end {MA[-1]:.2f} [{time.time() - t0:.0f}s]", flush=True)
    env.close(); return m


def rank_auc(x, y):
    """AUC of x for y (bool): P(x_pos > x_neg) by ranks, ties at a half."""
    x = np.asarray(x, float); y = np.asarray(y, bool)
    if y.sum() == 0 or (~y).sum() == 0: return float("nan")
    order = np.argsort(x, kind="mergesort"); ranks = np.empty(len(x)); ranks[order] = np.arange(1, len(x) + 1)
    xs = x[order]; i = 0
    while i < len(xs):                                           # tie ranks
        j = i
        while j + 1 < len(xs) and xs[j + 1] == xs[i]: j += 1
        if j > i: ranks[order[i:j + 1]] = (i + 1 + j + 1) / 2
        i = j + 1
    return float((ranks[y].sum() - y.sum() * (y.sum() + 1) / 2) / (y.sum() * (~y).sum()))


def analyze(a, m):
    files = sorted(glob.glob(os.path.join(a.out, "decisions-seed*.npz")))
    D = [np.load(f) for f in files]
    obs = np.concatenate([d["obs"] for d in D]); act = np.concatenate([d["action"] for d in D]); seat = np.concatenate([d["seat"] for d in D])
    plant = np.concatenate([d["is_plant"] for d in D]); mA = np.concatenate([d["m_A"] for d in D]); seedv = np.concatenate([np.full(len(d["action"]), int(d["seed"])) for d in D])
    sel = (seat == "audit") & (~plant); selp = (seat == "audit") & plant
    O, A, M, SD = obs[sel], act[sel], mA[sel], seedv[sel]
    blind = A != 0
    pred = reward_batch(m, O); margin = pred[:, 0] - np.maximum(pred[:, 1], pred[:, 2])
    agree = float(np.mean((np.argmax(pred, 1) != 0) == blind))
    rng = np.random.default_rng(0)
    lines = [f"# The frozen head-alone policy at the audit seat, by the dial's level — what it reads when it turns to inspecting (`audit_attrib.py`; the reviewer's second read after §92)\n",
             f"Cell `{' '.join(json.load(open(os.path.join(a.out, 'meta.json')))['cell']) if os.path.exists(os.path.join(a.out, 'meta.json')) else ''}`, the policy of record `{a.model}` frozen, {len(D)} seeds, {a.ticks:,} ticks; {len(A):,} audit-seat decisions on real cases ({int(selp.sum()):,} on plants beside), the blind rate {blind.mean():.3f} pooled. "
             f"The head's argmax recomputed from the saved observations agrees with the action taken on {agree:.4f} of them (the rest the boundary read's or the tie's). A blind verdict is a verdict of either sign with no care spent; the band is m^A at the decision's tick.\n"]
    # 1. by band
    lines.append("## By the dial's level\n\n| band | decisions (seeds) | blind rate | on plants | the head's margin for care over the better blind verdict (real, mean) | seeds' blind rate min–max |\n|---|---|---|---|---|---|")
    band_of = np.full(len(A), -1)
    for i, (lo, hi, name) in enumerate(BANDS):
        k = (M >= lo) & (M < hi); band_of[k] = i
        kp = (mA[selp] >= lo) & (mA[selp] < hi)
        per_seed = [blind[k & (SD == s)].mean() for s in np.unique(SD) if (k & (SD == s)).sum() >= 20]
        lines.append(f"| {name} | {int(k.sum()):,} ({len(np.unique(SD[k]))}) | **{blind[k].mean() if k.sum() else float('nan'):.3f}** | {(act[selp][kp] != 0).mean() if kp.sum() else float('nan'):.3f} | {margin[k].mean() if k.sum() else float('nan'):+.2f} | {min(per_seed) if per_seed else float('nan'):.2f}–{max(per_seed) if per_seed else float('nan'):.2f} |")
    # 2. the fields by band: the mean per band, the fields sorted by the standardized move from the lowest to the highest populated band
    pop = [i for i in range(len(BANDS)) if (band_of == i).sum() >= 50]
    lo_b, hi_b = pop[0], pop[-1]
    sd = O.std(0) + 1e-9
    moves = [(j, (O[band_of == hi_b, j].mean() - O[band_of == lo_b, j].mean()) / sd[j]) for j in range(O.shape[1])]
    lines.append("\n## The fields by band (the mean of each field over the band's audit-seat decisions; the 16 that move most from the lowest band to the highest, in standard deviations of the field over all audit decisions)\n\n| field | " + " | ".join(BANDS[i][2] for i in pop) + " | move (SD) |\n|---|" + "---|" * (len(pop) + 1))
    for j, mv in sorted(moves, key=lambda x: -abs(x[1]))[:16]:
        lines.append(f"| `{OBS_FIELDS[j]}` | " + " | ".join(f"{O[band_of == i, j].mean():.3f}" for i in pop) + f" | {mv:+.2f} |")
    # 3. the clamp attribution
    hi = np.where(M >= 8.0)[0]; lo = np.where(M < 1.5)[0]
    if len(hi) < 50 or len(lo) < 50:
        hi = np.where(band_of == hi_b)[0]; lo = np.where(band_of == lo_b)[0]
    cap = 4000
    hi = rng.choice(hi, min(cap, len(hi)), replace=False); lo = rng.choice(lo, min(cap, len(lo)), replace=False)
    Oh, Ol = O[hi], O[lo]; base_h = float(np.mean(np.argmax(reward_batch(m, Oh), 1) != 0)); base_l = float(np.mean(np.argmax(reward_batch(m, Ol), 1) != 0))
    def clamp(src, dst, cols, reps=3):
        out = []
        for _ in range(reps):
            X = dst.copy(); draw = rng.integers(0, len(src), len(dst))
            for j in cols: X[:, j] = src[draw, j]
            out.append(float(np.mean(np.argmax(reward_batch(m, X), 1) != 0)))
        return float(np.mean(out))
    lines.append(f"\n## The attribution by clamping\n\nThe high-dial audit decisions (m^A {M[hi].min():.1f}–{M[hi].max():.1f}, {len(hi):,} drawn; the policy blind on {base_h:.3f} of them as saved, {base_h:.3f} recomputed) with one field replaced by draws of it from the low-dial decisions (m^A {M[lo].min():.1f}–{M[lo].max():.1f}, {len(lo):,} drawn; blind {base_l:.3f}), the head asked again — the rise in the blind rate is what the field carries of the turn to inspecting; the reverse clamp beside (the low-dial decisions given the field's high-dial draws — the fall in their blind rate). Three draws averaged. Fields sorted by the first clamp's rise; the groups below the fields.\n\n| field | high-dial blind rate with the field's low-dial values | rise | low-dial blind rate with the field's high-dial values | fall | rank AUC care vs blind, pooled | within the high band |\n|---|---|---|---|---|---|---|")
    rows = []
    for j in range(O.shape[1]):
        if OBS_FIELDS[j] == "decision_boundary": continue
        h = clamp(Ol, Oh, [j]); l = clamp(Oh, Ol, [j])
        rows.append((OBS_FIELDS[j], h, h - base_h, l, base_l - l, rank_auc(O[:, j], ~blind), rank_auc(O[hi, j], ~blind[hi])))
    for nm, h, dh, l, dl, auc, auch in sorted(rows, key=lambda x: -x[2]):
        lines.append(f"| `{nm}` | {h:.3f} | **{dh:+.3f}** | {l:.3f} | {dl:+.3f} | {auc:.3f} | {auch:.3f} |")
    lines.append("\n| group | high-dial blind rate with the group's low-dial values | rise | low-dial blind rate with the group's high-dial values | fall |\n|---|---|---|---|---|")
    for g, names in GROUPS.items():
        cols = [IDX[n] for n in names]; h = clamp(Ol, Oh, cols); l = clamp(Oh, Ol, cols)
        lines.append(f"| {g} | {h:.3f} | **{h - base_h:+.3f}** | {l:.3f} | {base_l - l:+.3f} |")
    lines.append(f"| every field (the whole observation) | {clamp(Ol, Oh, list(range(O.shape[1] - 1))):.3f} | — | {clamp(Oh, Ol, list(range(O.shape[1] - 1))):.3f} | — |")
    open(os.path.join(a.out, "audit-attrib.md"), "w").write("\n".join(lines) + "\n"); print("\n".join(lines))


def main(argv=None):
    ap = argparse.ArgumentParser(); ap.add_argument("--out", required=True); ap.add_argument("--model", required=True); ap.add_argument("--seeds", default="21-40")
    ap.add_argument("--ticks", type=int, default=2000); ap.add_argument("--analyze", action="store_true"); ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv); cell = [x for x in a.cell if x != "--"]
    if a.analyze:
        m, _ = load_model(a.model); m.to(device()); analyze(a, m); return
    os.makedirs(a.out, exist_ok=True); json.dump({"cell": cell, "ticks": a.ticks, "seeds": a.seeds, "model": a.model}, open(os.path.join(a.out, "meta.json"), "w"))
    m = collect(a, cell); analyze(a, m)


if __name__ == "__main__":
    main()
