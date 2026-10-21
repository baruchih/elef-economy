"""The environment's reward timing — the examination the reviewer's ruling after the calibration ladder calls for when nothing clears
the ideal. ElefReviewerEnv's per-decision reward is the change in the learner's lifetime real wealth between consecutive decisions.
This decomposes that reward, for a policy in a cell, by **source** — every ledger event touching the learner's names, classified by
kind and note into the reviewing side (the care cost, its reimbursement, the review fee, the bond lost or the court fee paid) and the
working side (a delivery price, a guarantee forfeited, the emission share, the duty uplift) — and by **timing**: for every review
decision, the decision window in which each of its own case's consequences landed (lag in decisions and in ticks). The reading beside
the ladder: how much of a window's reward the decision caused, when its consequences arrive, and how large the uncaused part is.

  python -m redteam.timing --out results/redteam/Q1/reward-timing --seeds 21-40 --policies careful,stamper -- <cell args>
  (--model <wm.pt> --horizon 16 adds the learned policy; --direct-model <direct.pt> the direct one)

The decomposition's check: the classified deltas (nominal, times the run's closing real factor) summed over a window against the
reward the environment paid — the residual is the index moving within the run and nothing else, and it is reported."""
from __future__ import annotations

import argparse
import json
import os
import time
from collections import defaultdict

import numpy as np

from redteam.env import ElefReviewerEnv
from redteam.run_q import policy_of, seeds_of

SOURCES = ("care_cost", "reimbursement", "review_fee", "bond_lost", "delivery_price", "effort_cost", "guarantee_lost", "court_fee", "emission", "uplift",
           "revaluation", "other")
REVIEW_SIDE = ("care_cost", "reimbursement", "review_fee", "bond_lost")                         # what the review decision causes
WORK_SIDE = ("delivery_price", "effort_cost", "guarantee_lost", "court_fee", "emission", "uplift")   # the slot actor's other life, uncaused by the decision
EXCLUDED = ("lock", "release", "departure", "arrival", "arrival_repayment")   # W unchanged, or the lifetime measure carries it another way


def classify(e, names) -> tuple[str, float] | None:
    """(source, signed nominal change to the names' wealth W) for a ledger event, or None when it does not touch W."""
    if e.kind in EXCLUDED:
        return None
    src_in, dst_in = e.src in names, e.dst in names
    if not (src_in or dst_in) or (src_in and dst_in):
        return None
    sign = 1.0 if dst_in else -1.0
    n = e.note or ""
    k = e.kind
    if k == "purchase" and n.startswith("review"):
        s = "care_cost"
    elif k == "purchase":
        s = "effort_cost"                                      # the slot actor's own work: "execution"
    elif (k == "deposit_out" and ("reimburse" in n or "deferred" in n)) or (k == "transfer" and "advance" in n and dst_in):
        s = "reimbursement"                                    # from the allowance, deferred, or Ω's advance
    elif k == "feepot_out" and n.endswith("review fee"):
        s = "review_fee"
    elif k == "burn_bond" and "bond:" in n:
        s = "bond_lost"
    elif k == "forfeit_to" and "court fee" in n:
        s = "bond_lost" if src_in else "court_fee"             # the reviewer's bond paying the appellant's fee; the slot's own fee coming back
    elif k == "transfer" and "court fee" in n:
        s = "court_fee"                                        # the slot appealing a verdict on its own work
    elif k == "escrow_out" and "delivery price" in n:
        s = "delivery_price"
    elif k == "forfeit_to" and "forfeit:" in n:
        s = "guarantee_lost"
    elif k == "burn_bond" and "rej:" in n:
        s = "court_fee"
    elif k == "fee_out" and "emission share" in n:
        s = "emission"
    elif k == "transfer" and "duty uplift" in n:
        s = "uplift"
    else:
        s = "other"
    return s, sign * float(e.amount)


def episode(env, policy, seed, rng):
    """One run: the decisions (tick, ledger position, case, action, reward) and the learner's events, classified and windowed."""
    obs, info = env.reset(seed=seed)
    done = info.get("terminal", False)
    mark = lambda info, prev: (info.get("t", 0), info.get("n_events", prev[1] if prev else 0), info.get("case"), bool(info.get("boundary", False)),
                               info.get("real_factor", prev[4] if prev else 1.0), info.get("wealth_real", prev[5] if prev else 0.0))
    marks = [mark(info, None)]
    acts, rewards = [], []
    while not done:
        a = policy(obs, rng)
        acts.append(int(a))
        obs, r, done, _, info = env.step(a)
        rewards.append(float(r))
        marks.append(mark(info, marks[-1]))
    run = env.run
    names = set(run.learner_chain)
    real = marks[-1][4]
    events = run.w.events_since(0)
    n_dec = len(acts)
    # window i = ledger positions [marks[i].n, marks[i+1].n); the last window runs to the end
    bounds = [m[1] for m in marks]
    by_window = [defaultdict(float) for _ in range(n_dec)]
    other_notes = defaultdict(float)
    # the review decisions' own cases: which window their consequences landed in
    case_of = {i: marks[i][2] for i in range(n_dec) if marks[i][2] is not None and not marks[i][3]}
    first_window_of_case = {}
    for i, c in case_of.items():
        first_window_of_case.setdefault(c, i)
    lags = defaultdict(list)         # source -> [(lag in decisions, lag in ticks)]
    for pos, e in enumerate(events):
        cl = classify(e, names)
        if cl is None:
            continue
        s, d = cl
        i = int(np.searchsorted(bounds, pos, side="right")) - 1
        if i < 0:
            continue
        i = min(i, n_dec - 1)
        by_window[i][s] += d
        if s == "other":
            other_notes[f"{e.kind}:{e.note[:40]}"] += d
        if s in REVIEW_SIDE and e.case in first_window_of_case:
            j = first_window_of_case[e.case]
            lags[s].append((i - j, e.t - marks[j][0]))
    rows = []
    for i in range(n_dec):
        w = by_window[i]
        r0, r1 = marks[i][4], marks[i + 1][4]                   # the index at the decision and at the next: the window's deltas count at r1,
        w_nom = (marks[i][5] / r0) if r0 else 0.0                # the wealth held revalued by the index's move (a boundary's published P_t)
        w["revaluation"] = w_nom * (r1 - r0) / r1 if r1 else 0.0
        tot = sum(w.values()) * r1
        rows.append({"i": i, "t": marks[i][0], "ticks": marks[i + 1][0] - marks[i][0], "boundary": marks[i][3], "action": acts[i], "reward": rewards[i],
                     "classified_real": tot, "review_side": sum(w[s] for s in REVIEW_SIDE) * r1, "work_side": sum(w[s] for s in WORK_SIDE) * r1,
                     "other": w["other"] * r1, **{s: w[s] * r1 for s in SOURCES}})
    return {"seed": seed, "decisions": n_dec, "lifetime_real_wealth": info.get("lifetime_real_wealth"), "real_factor": real, "ticks": run.w.t,
            "windows": rows, "lags": {s: v for s, v in lags.items()}, "other_notes": dict(other_notes)}


def mse(xs):
    xs = [x for x in xs if x is not None and np.isfinite(x)]
    return (float(np.mean(xs)), float(np.std(xs, ddof=1) / np.sqrt(len(xs))) if len(xs) > 1 else 0.0, len(xs)) if xs else (float("nan"), float("nan"), 0)


def summarize(eps):
    """Pooled over the seeds: per source the mean per window, the SD across windows, the share of windows it appears in; the reward's
    SD against the review side's; the residual; the lags."""
    W = [w for e in eps for w in e["windows"] if not w["boundary"]]
    if not W:
        return {}
    tk = np.array([w["ticks"] for w in W])
    out = {"windows": len(W), "runs": len(eps), "ticks_per_window_mean": float(tk.mean()), "ticks_per_window_median": float(np.median(tk)),
           "ticks_per_window_p90": float(np.percentile(tk, 90)), "windows_of_one_tick": float((tk <= 1).mean())}
    rew = np.array([w["reward"] for w in W]); cls = np.array([w["classified_real"] for w in W])
    out["reward"] = {"mean": float(rew.mean()), "sd": float(rew.std(ddof=1))}
    # the uncaused part's weight: the share of the reward's variance carried by the windows longer than five ticks (where the work lands)
    long = tk > 5
    out["long_windows"] = {"share": float(long.mean()), "reward_mean": float(rew[long].mean()) if long.any() else None, "reward_sd": float(rew[long].std(ddof=1)) if long.sum() > 1 else None,
                           "short_reward_mean": float(rew[~long].mean()) if (~long).any() else None, "short_reward_sd": float(rew[~long].std(ddof=1)) if (~long).sum() > 1 else None,
                           "share_of_variance": float(((rew[long] - rew.mean()) ** 2).sum() / max(1e-9, ((rew - rew.mean()) ** 2).sum()))}
    out["residual"] = {"mean_abs": float(np.abs(rew - cls).mean()), "corr": float(np.corrcoef(rew, cls)[0, 1]) if rew.std() > 0 and cls.std() > 0 else None}
    for part in ("review_side", "work_side", "other"):
        x = np.array([w[part] for w in W]); out[part] = {"mean": float(x.mean()), "sd": float(x.std(ddof=1))}
    out["sources"] = {}
    for s in SOURCES:
        x = np.array([w[s] for w in W])
        out["sources"][s] = {"mean": float(x.mean()), "sd": float(x.std(ddof=1)), "share_of_windows": float((np.abs(x) > 1e-9).mean())}
    # by the action taken in the window
    out["by_action"] = {}
    for k, name in ((0, "care"), (1, "approve_blind"), (2, "reject_blind")):
        Wk = [w for w in W if w["action"] == k]
        if not Wk:
            continue
        out["by_action"][name] = {"n": len(Wk), "reward_mean": float(np.mean([w["reward"] for w in Wk])), "review_side_mean": float(np.mean([w["review_side"] for w in Wk])),
                                  "work_side_mean": float(np.mean([w["work_side"] for w in Wk])),
                                  **{s: float(np.mean([w[s] for w in Wk])) for s in REVIEW_SIDE}}
    # the lags of a decision's own consequences
    out["lags"] = {}
    for s in REVIEW_SIDE:
        L = [x for e in eps for x in e["lags"].get(s, [])]
        if not L:
            continue
        d = np.array([x[0] for x in L]); t = np.array([x[1] for x in L])
        out["lags"][s] = {"n": len(L), "lag_decisions_mean": float(d.mean()), "lag_ticks_mean": float(t.mean()),
                          "in_own_window": float((d == 0).mean()), "lag_1": float((d == 1).mean()), "lag_2_plus": float((d >= 2).mean())}
    notes = defaultdict(float)
    for e in eps:
        for k, v in e["other_notes"].items():
            notes[k] += v
    out["other_notes"] = dict(sorted(notes.items(), key=lambda kv: -abs(kv[1]))[:12])
    return out


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--seeds", default="21-40"); ap.add_argument("--policies", default="careful,stamper")
    ap.add_argument("--model", default=None); ap.add_argument("--direct-model", default=None); ap.add_argument("--horizon", type=int, default=16)
    ap.add_argument("--samples", type=int, default=256); ap.add_argument("--iters", type=int, default=6)
    ap.add_argument("--hide", default=""); ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    cell = [x for x in a.cell if x != "--"]
    hide = tuple(x for x in a.hide.split(",") if x)
    pols, ck = {}, {}
    for name in a.policies.split(","):
        if name == "learned":
            from redteam.plan import LearnedPolicy
            from redteam.train import load_model, device
            m, ck = load_model(a.model); m.to(device())
            pols[name] = LearnedPolicy(m, horizon=a.horizon, samples=a.samples, iters=a.iters)
        elif name == "direct":
            from redteam.direct import load_direct, DirectPolicy
            from redteam.train import device
            dm, _ = load_direct(a.direct_model); dm.to(device())
            pols[name] = DirectPolicy(dm)
        else:
            pols[name] = policy_of(name)
    env = ElefReviewerEnv(cell, ticks=a.ticks, hide=hide, obs_dim=ck.get("config", {}).get("obs_dim"))
    os.makedirs(a.out, exist_ok=True)
    results = {k: [] for k in pols}
    t0 = time.time()
    for seed in sorted(seeds_of(a.seeds)):
        for name, pol in pols.items():
            rng = np.random.default_rng(seed)
            r = episode(env, pol, seed, rng)
            results[name].append(r)
            print(f"seed {seed} {name}: {r['decisions']} decisions, lifetime {r['lifetime_real_wealth']:.1f}, "
                  f"review side {sum(w['review_side'] for w in r['windows']):.1f}, work side {sum(w['work_side'] for w in r['windows']):.1f}", flush=True)
    env.close()
    summary = {name: summarize(rows) for name, rows in results.items()}
    out = {"cell": cell, "seeds": a.seeds, "model": a.model, "direct_model": a.direct_model, "horizon": a.horizon, "seconds": round(time.time() - t0, 1),
           "summary": summary, "episodes": results}
    json.dump(out, open(os.path.join(a.out, "timing.json"), "w"), indent=1, default=float)
    with open(os.path.join(a.out, "timing.md"), "w") as f:
        f.write(f"# The reward's timing — cell `{' '.join(cell)}`, seeds {a.seeds}\n\nPer decision window (real at the window's closing index): the reward the "
                f"environment paid, its reviewing side (what the decision caused: the care cost, its reimbursement, the review fee, the bond lost), its working "
                f"side (the slot actor's other life: the delivery price, the effort cost, a guarantee lost, its own court fee, the emission share, the uplift) "
                f"and the revaluation of the wealth held by the index's move, mean and SD across windows; the decomposition is exact (the residual is the "
                f"check); the lag from a review decision to its own case's consequences.\n\n| policy | windows | ticks/window mean / median / p90 | one-tick windows | reward mean | reward SD | review side mean | SD | work side mean | SD | revaluation mean | SD | other | residual |abs| | corr |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for name, s in summary.items():
            if not s:
                continue
            f.write(f"| {name} | {s['windows']} | {s['ticks_per_window_mean']:.1f} / {s['ticks_per_window_median']:.0f} / {s['ticks_per_window_p90']:.0f} | {s['windows_of_one_tick']:.2f} | {s['reward']['mean']:.2f} | {s['reward']['sd']:.2f} | {s['review_side']['mean']:.2f} | "
                    f"{s['review_side']['sd']:.2f} | {s['work_side']['mean']:.2f} | {s['work_side']['sd']:.2f} | {s['sources']['revaluation']['mean']:.2f} | {s['sources']['revaluation']['sd']:.2f} | {s['other']['mean']:.2f} | {s['residual']['mean_abs']:.2f} | "
                    f"{s['residual']['corr'] if s['residual']['corr'] is None else round(s['residual']['corr'], 3)} |\n")
        f.write("\n## The long windows (more than five ticks between decisions: the slot off duty, its work landing)\n\n| policy | share of windows | reward mean (long) | SD | reward mean (short) | SD | share of the reward's variance |\n|---|---|---|---|---|---|---|\n")
        for name, s in summary.items():
            if s:
                lw = s["long_windows"]
                f.write(f"| {name} | {lw['share']:.2f} | {lw['reward_mean']:.2f} | {lw['reward_sd']:.2f} | {lw['short_reward_mean']:.2f} | {lw['short_reward_sd']:.2f} | {lw['share_of_variance']:.2f} |\n")
        f.write("\n## By source (mean per window, SD, share of windows carrying it)\n\n| policy | " + " | ".join(SOURCES) + " |\n|---|" + "---|" * len(SOURCES) + "\n")
        for name, s in summary.items():
            if s:
                f.write(f"| {name} | " + " | ".join(f"{s['sources'][k]['mean']:.2f} ± {s['sources'][k]['sd']:.1f} ({s['sources'][k]['share_of_windows']:.2f})" for k in SOURCES) + " |\n")
        f.write("\n## By the action taken in the window\n\n| policy | action | n | reward | review side | work side | care cost | reimbursement | review fee | bond lost |\n|---|---|---|---|---|---|---|---|---|---|\n")
        for name, s in summary.items():
            for act, v in (s.get("by_action") or {}).items():
                f.write(f"| {name} | {act} | {v['n']} | {v['reward_mean']:.2f} | {v['review_side_mean']:.2f} | {v['work_side_mean']:.2f} | {v['care_cost']:.2f} | {v['reimbursement']:.2f} | {v['review_fee']:.2f} | {v['bond_lost']:.2f} |\n")
        f.write("\n## The lag from a review decision to its own case's consequences\n\n| policy | source | n | lag (decisions) | lag (ticks) | in own window | one later | two or more later |\n|---|---|---|---|---|---|---|---|\n")
        for name, s in summary.items():
            for src, v in (s.get("lags") or {}).items():
                f.write(f"| {name} | {src} | {v['n']} | {v['lag_decisions_mean']:.2f} | {v['lag_ticks_mean']:.1f} | {v['in_own_window']:.2f} | {v['lag_1']:.2f} | {v['lag_2_plus']:.2f} |\n")
        f.write("\n## Unclassified events (kind:note, summed real)\n\n")
        for name, s in summary.items():
            f.write(f"- {name}: " + (", ".join(f"`{k}` {v:.1f}" for k, v in (s.get('other_notes') or {}).items()) or "none") + "\n")
    print(json.dumps({k: {kk: vv for kk, vv in v.items() if kk in ("windows", "reward", "review_side", "work_side", "residual", "lags")} for k, v in summary.items()}, indent=1, default=float))


if __name__ == "__main__":
    main()
