"""A question's evaluation: the learned reviewer (the planner on a trained world model) against the careful policy on the evaluation
seeds, paired by seed — the same slot actor, cost and seed — with the honesty readings beside; the greedy wealth-head policy as the
no-horizon control. Writes <out>/eval.json and <out>/eval.md. Usage: python -m redteam.run_q --model <ckpt> --out <dir> [--seeds 21-40]
[--policies learned,greedy,careful] [--horizon 8] [--hide own_p_eff] -- <cell args>"""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam.env import ElefReviewerEnv, POLICIES
from redteam.train import load_model, seeds_of
from redteam.plan import LearnedPolicy, GreedyPolicy
from redteam.model import device


def episode(env, policy, seed, rng):
    obs, info = env.reset(seed=seed)
    done = info.get("terminal", False)
    acts, plants_stamped, real_stamped, plants_seen, real_seen = [], 0, 0, 0, 0
    while not done:
        a = policy(obs, rng)
        acts.append(a)
        if info.get("is_plant"):
            plants_seen += 1; plants_stamped += int(a != 0)
        else:
            real_seen += 1; real_stamped += int(a != 0)
        obs, r, done, _, info = env.step(a)
    row = info.get("row", {})
    return {"seed": seed, "decisions": len(acts), "lifetime_real_wealth": info.get("lifetime_real_wealth"),
            "care_share": float(np.mean([x == 0 for x in acts])) if acts else None, "approve_blind_share": float(np.mean([x == 1 for x in acts])) if acts else None,
            "reject_blind_share": float(np.mean([x == 2 for x in acts])) if acts else None,
            "plants_seen": plants_seen, "plants_stamped": plants_stamped, "real_seen": real_seen, "real_stamped": real_stamped,
            "false_approvals_run": row.get("false_approvals"), "learner_false_approvals": row.get("learner_false_approvals"),
            "slot_departed": row.get("slot_departed"), "slot_rho": row.get("slot_rho"), "slot_plant_failures": row.get("learner_plant_failures"),
            "suspensions_run": row.get("suspensions"), "error": info.get("error")}


def mse(xs):
    xs = [x for x in xs if x is not None and not (isinstance(x, float) and np.isnan(x))]
    if not xs:
        return (float("nan"), float("nan"))
    return float(np.mean(xs)), float(np.std(xs, ddof=1) / np.sqrt(len(xs))) if len(xs) > 1 else 0.0


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--model", required=True); ap.add_argument("--out", required=True)
    ap.add_argument("--seeds", default="21-40"); ap.add_argument("--policies", default="learned,greedy,careful")
    ap.add_argument("--horizon", type=int, default=8); ap.add_argument("--samples", type=int, default=256); ap.add_argument("--iters", type=int, default=6)
    ap.add_argument("--hide", default=""); ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    cell = [x for x in a.cell if x != "--"]
    hide = tuple(x for x in a.hide.split(",") if x)
    m, ck = load_model(a.model); m.to(device())
    env = ElefReviewerEnv(cell, ticks=a.ticks, hide=hide)
    pols = {}
    for name in a.policies.split(","):
        if name == "learned":
            pols[name] = LearnedPolicy(m, horizon=a.horizon, samples=a.samples, iters=a.iters)
        elif name == "greedy":
            pols[name] = GreedyPolicy(m)
        else:
            pols[name] = POLICIES[name]
    os.makedirs(a.out, exist_ok=True)
    results = {k: [] for k in pols}
    t0 = time.time()
    for seed in sorted(seeds_of(a.seeds)):
        for name, pol in pols.items():
            rng = np.random.default_rng(seed)
            r = episode(env, pol, seed, rng)
            results[name].append(r)
            print(f"seed {seed} {name}: {r['decisions']} decisions, lifetime {r['lifetime_real_wealth']:.1f}, care {r['care_share']}, plants stamped {r['plants_stamped']}/{r['plants_seen']}, real stamped {r['real_stamped']}/{r['real_seen']}", flush=True)
    env.close()
    summary = {}
    for name, rows in results.items():
        summary[name] = {k: mse([r[k] for r in rows]) for k in ("lifetime_real_wealth", "decisions", "care_share", "approve_blind_share", "reject_blind_share",
                                                                 "false_approvals_run", "learner_false_approvals", "suspensions_run", "slot_departed")}
        ps, pn, rs, rn = (sum(r[k] for r in rows) for k in ("plants_stamped", "plants_seen", "real_stamped", "real_seen"))
        summary[name]["plant_stamp_rate"] = ps / max(1, pn); summary[name]["real_stamp_rate"] = rs / max(1, rn)
    if "careful" in results:
        base = {r["seed"]: r["lifetime_real_wealth"] for r in results["careful"]}
        for name in results:
            if name == "careful":
                continue
            d = [r["lifetime_real_wealth"] - base[r["seed"]] for r in results[name] if r["seed"] in base]
            summary[name]["paired_minus_careful"] = mse(d)
    out = {"cell": cell, "seeds": a.seeds, "hide": a.hide, "model": a.model, "model_train": ck.get("train", {}), "horizon": a.horizon,
           "samples": a.samples, "iters": a.iters, "seconds": round(time.time() - t0, 1), "summary": summary, "episodes": results}
    json.dump(out, open(os.path.join(a.out, "eval.json"), "w"), indent=1, default=float)
    with open(os.path.join(a.out, "eval.md"), "w") as f:
        f.write(f"# Evaluation — cell `{' '.join(cell)}`, seeds {a.seeds}, hide `{a.hide}`\n\n| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate | real stamp rate | run false approvals | learner's | departed |\n|---|---|---|---|---|---|---|---|---|---|---|---|\n")
        for name, s in summary.items():
            pm = s.get("paired_minus_careful", (float("nan"), float("nan")))
            f.write(f"| {name} | {s['lifetime_real_wealth'][0]:.1f} ± {s['lifetime_real_wealth'][1]:.1f} | {pm[0]:.1f} ± {pm[1]:.1f} | {s['decisions'][0]:.1f} | {s['care_share'][0]:.3f} | {s['approve_blind_share'][0]:.3f} | {s['reject_blind_share'][0]:.3f} | {s['plant_stamp_rate']:.3f} | {s['real_stamp_rate']:.3f} | {s['false_approvals_run'][0]:.2f} | {s['learner_false_approvals'][0]:.2f} | {s['slot_departed'][0]:.2f} |\n")
    print(json.dumps(summary, indent=1, default=float))


if __name__ == "__main__":
    main()
