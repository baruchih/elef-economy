"""The online iterations (the build plan's budget: up to ten rounds of plan-and-collect on the training seeds): each round collects
episodes with the current learned policy (ε-exploration) on seeds 1–20 into the same data directory (policy name online-<k>), retrains
the world model on everything collected so far, and every `--eval-every` rounds evaluates the learned reviewer against careful on the
evaluation seeds. Usage: python -m redteam.online --data <dir> --models <dir> --evals <dir> [--rounds 6] [--eps 0.1] -- <cell args>"""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam import train as T, run_q as Q
from redteam.env import ElefReviewerEnv
from redteam.collect import rollout
from redteam.plan import LearnedPolicy
from redteam.model import device


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--models", required=True); ap.add_argument("--evals", required=True)
    ap.add_argument("--rounds", type=int, default=6); ap.add_argument("--eps", type=float, default=0.1)
    ap.add_argument("--train-seeds", default="1-20"); ap.add_argument("--eval-seeds", default="21-40"); ap.add_argument("--eval-every", type=int, default=2)
    ap.add_argument("--epochs", type=int, default=40); ap.add_argument("--horizon", type=int, default=8); ap.add_argument("--start", default=None, help="the model to start from")
    ap.add_argument("--hide", default=""); ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    cell = [x for x in a.cell if x != "--"]
    hide = tuple(x for x in a.hide.split(",") if x)
    os.makedirs(a.models, exist_ok=True); os.makedirs(a.evals, exist_ok=True)
    model_path = a.start or os.path.join(a.models, "wm-online-0.pt")
    if not a.start:
        T.main(["--data", a.data, "--out", model_path, "--seeds", a.train_seeds, "--epochs", str(a.epochs), "--horizon", str(a.horizon)])
    env = ElefReviewerEnv(cell, ticks=a.ticks, hide=hide)
    log = []
    for k in range(1, a.rounds + 1):
        t0 = time.time()
        m, _ = T.load_model(model_path); m.to(device())
        pol = LearnedPolicy(m, horizon=a.horizon)
        lo, hi = (int(x) for x in a.train_seeds.split("-"))
        lifetimes = []
        for seed in range(lo, hi + 1):
            rng = np.random.default_rng(seed * 7919 + k)
            explore = lambda obs, r: int(r.integers(3)) if r.random() < a.eps else pol(obs, r)
            O, A, R, P, F, Tk, info = rollout(env, explore, seed, rng)
            np.savez_compressed(os.path.join(a.data, f"online{k}-seed{seed}.npz"), obs=O, action=A, reward=R, is_plant=P, fulfilled=F, t=Tk,
                                lifetime=info.get("lifetime_real_wealth", float("nan")), seed=seed, policy=f"online{k}")
            lifetimes.append(info.get("lifetime_real_wealth", float("nan")))
        model_path = os.path.join(a.models, f"wm-online-{k}.pt")
        T.main(["--data", a.data, "--out", model_path, "--seeds", a.train_seeds, "--epochs", str(a.epochs), "--horizon", str(a.horizon)])
        rec = {"round": k, "train_lifetime_mean": float(np.nanmean(lifetimes)), "seconds": round(time.time() - t0, 1)}
        if k % a.eval_every == 0 or k == a.rounds:
            out = os.path.join(a.evals, f"round-{k}")
            Q.main(["--model", model_path, "--out", out, "--seeds", a.eval_seeds, "--policies", "learned,careful", "--horizon", str(a.horizon),
                    "--hide", a.hide, "--ticks", str(a.ticks), "--"] + cell)
            s = json.load(open(os.path.join(out, "eval.json")))["summary"]
            rec["eval"] = {"learned": s["learned"]["lifetime_real_wealth"], "careful": s["careful"]["lifetime_real_wealth"],
                           "paired": s["learned"]["paired_minus_careful"], "care_share": s["learned"]["care_share"],
                           "plant_stamp_rate": s["learned"]["plant_stamp_rate"], "real_stamp_rate": s["learned"]["real_stamp_rate"]}
        log.append(rec)
        print(json.dumps(rec, default=float), flush=True)
        json.dump(log, open(os.path.join(a.evals, "online-log.json"), "w"), indent=1, default=float)
    env.close()


if __name__ == "__main__":
    main()
