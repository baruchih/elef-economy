"""The online iterations (the build plan's budget: up to ten rounds of plan-and-collect on the training seeds): each round collects
episodes with the current learned policy (ε-exploration) on seeds 1–20 into the same data directory (policy name online-<k>), retrains
the world model on everything collected so far, and every `--eval-every` rounds evaluates the learned reviewer against careful on the
evaluation seeds. `--explore careful` (Q1 onward) draws the ε decisions from the careful policy instead of uniformly, so the rounds keep
data on the careful line beside the planner's own; `uniform` is Q2's. `--value`/`--gamma` go to the trainer (the terminal value, decision 5).
Usage: python -m redteam.online --data <dir> --models <dir> --evals <dir> [--rounds 6] [--eps 0.1] [--explore careful] [--value mc] -- <cell args>"""
from __future__ import annotations
import argparse, json, os, sys, time
import numpy as np
import torch

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
from redteam import train as T, run_q as Q
from redteam.env import ElefReviewerEnv, _boundary
from redteam.collect import rollout
from redteam.plan import LearnedPolicy, GreedyPolicy
from redteam.model import device


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--data", required=True); ap.add_argument("--models", required=True); ap.add_argument("--evals", required=True)
    ap.add_argument("--rounds", type=int, default=6); ap.add_argument("--eps", type=float, default=0.1); ap.add_argument("--first-round", type=int, default=1)
    ap.add_argument("--train-seeds", default="1-20"); ap.add_argument("--eval-seeds", default="21-40"); ap.add_argument("--eval-every", type=int, default=2)
    ap.add_argument("--epochs", type=int, default=40); ap.add_argument("--horizon", type=int, default=8); ap.add_argument("--start", default=None, help="the model to start from")
    ap.add_argument("--hide", default=""); ap.add_argument("--ticks", type=int, default=1000)
    ap.add_argument("--explore", choices=["careful", "uniform"], default="careful", help="what the ε decisions are drawn from")
    ap.add_argument("--value", choices=["off", "mc", "td"], default="off"); ap.add_argument("--gamma", type=float, default=0.95)
    ap.add_argument("--heads", choices=["one", "two"], default="two", help="version 4: the review-side head and the boundary head (the trainer's); `one` is version 3's")
    ap.add_argument("--eval-policies", default="learned,careful")
    ap.add_argument("--learner", choices=["wm", "direct"], default="wm", help="the ladder's rung (b): `direct` trains redteam.direct in place of the world model and plans nothing")
    ap.add_argument("--role", choices=["reviewer", "deliverer"], default="reviewer", help="Q3: the learned deliverer")
    ap.add_argument("--plan", choices=["cem", "greedy"], default="cem", help="the collecting policy on the world model: the CEM planner, or the head alone over the latent (version 4's stopping rule)")
    ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    direct = a.learner == "direct"
    if direct:
        from redteam.direct import main as D_main, load_direct, DirectPolicy
    lead = a.eval_policies.split(",")[0]       # the policy the round's record reads (learned, or direct)
    stem = "direct-online" if direct else "wm-online"
    def fit(data, out):
        (D_main if direct else T.main)(["--data", data, "--out", out] + train_args)
    cell = [x for x in a.cell if x != "--"]
    hide = tuple(x for x in a.hide.split(",") if x)
    os.makedirs(a.models, exist_ok=True); os.makedirs(a.evals, exist_ok=True)
    train_args = ["--seeds", a.train_seeds, "--epochs", str(a.epochs), "--horizon", str(a.horizon), "--value", a.value, "--gamma", str(a.gamma), "--heads", a.heads]
    model_path = a.start or os.path.join(a.models, f"{stem}-0.pt")
    if not a.start:
        fit(a.data, model_path)
    env = ElefReviewerEnv(cell, ticks=a.ticks, hide=hide, role=a.role)
    log = []
    for k in range(a.first_round, a.first_round + a.rounds):
        t0 = time.time()
        if direct:
            m, _ = load_direct(model_path); m.to(device()); pol = DirectPolicy(m)
        else:
            m, _ = T.load_model(model_path); m.to(device()); pol = GreedyPolicy(m) if a.plan == "greedy" else LearnedPolicy(m, horizon=a.horizon)
        lo, hi = (int(x) for x in a.train_seeds.split("-"))
        lifetimes = []
        for seed in range(lo, hi + 1):
            rng = np.random.default_rng(seed * 7919 + k)
            if a.explore == "uniform":
                explore = lambda obs, r: int(r.integers(env.n_actions)) if r.random() < a.eps else pol(obs, r)
            else:
                explore = lambda obs, r: ((int(r.integers(2)) if _boundary(obs) else 0) if r.random() < a.eps else pol(obs, r))   # version 3: an ε decision at a boundary leaves or stays equally
            O, A, R, P, F, Tk, info = rollout(env, explore, seed, rng)
            np.savez_compressed(os.path.join(a.data, f"online{k}-seed{seed}.npz"), obs=O, action=A, chosen=info["action_chosen"], reward=R, is_plant=P, fulfilled=F, t=Tk,
                                realized=info.get("realized_rewards", R), lifetime=info.get("lifetime_real_wealth", float("nan")), seed=seed, policy=f"online{k}",
                                role=a.role, n_actions=env.n_actions)
            lifetimes.append(info.get("lifetime_real_wealth", float("nan")))
        model_path = os.path.join(a.models, f"{stem}-{k}.pt")
        fit(a.data, model_path)
        rec = {"round": k, "train_lifetime_mean": float(np.nanmean(lifetimes)), "seconds": round(time.time() - t0, 1), "explore": a.explore, "value": a.value, "heads": a.heads, "role": a.role, "plan": a.plan}
        if k % a.eval_every == 0 or k == a.first_round + a.rounds - 1:
            out = os.path.join(a.evals, f"round-{k}")
            Q.main((["--direct-model", model_path] if direct else ["--model", model_path]) + ["--out", out, "--seeds", a.eval_seeds, "--policies", a.eval_policies, "--horizon", str(a.horizon),
                    "--hide", a.hide, "--ticks", str(a.ticks), "--role", a.role, "--"] + cell)
            s = json.load(open(os.path.join(out, "eval.json")))["summary"]
            rec["eval"] = {lead: s[lead]["lifetime_real_wealth"], "careful": s["careful"]["lifetime_real_wealth"],
                           "paired": s[lead]["paired_minus_careful"], "care_share": s[lead].get("care_share"), "bad_share": s[lead].get("bad_share"),
                           "plant_stamp_rate": s[lead].get("plant_stamp_rate"), "real_stamp_rate": s[lead].get("real_stamp_rate"),
                           "odds_at_stamps": s[lead].get("odds_at_stamps_mean"), "slot_suspensions": s[lead].get("slot_suspensions"),
                           "pred_vs_realized": s[lead].get("pred_vs_realized")}
        log.append(rec)
        print(json.dumps(rec, default=float), flush=True)
        json.dump(log, open(os.path.join(a.evals, f"online-log-{a.first_round}.json" if a.first_round > 1 else "online-log.json"), "w"), indent=1, default=float)
    env.close()


if __name__ == "__main__":
    main()
