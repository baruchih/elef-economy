"""Addendum 13's M3.4 (November 16, 2026; notes §112): the known-answer fits of record were made on every slot's decisions of the dose worlds (known_read.py and
known_wm_direct.py fit `--data <world> --seeds 1-20`, the collector's whole file) and read on every slot's observations at the dosed seat. Here the same two fits —
the direct policy and the world model under the return head — on the dosing slots alone (the slots that ever claimed, as known_read.py classed them: the data of
record filtered to their decisions, each slot's own sequence intact, written to <world>-dosing/), at the first review (known/first) and at the member's audit seat
in J4's world 5 cell (known/audit-w5); each fit read at the dosed seat on the dosing slots' observations and on every slot's, against the known answer and the
data's own randomized difference.  Usage: known_dosing.py OUT.md  (from agentic_sim/ in the elef-redteam env)"""
import glob, json, os, sys, numpy as np, torch
sys.path.insert(0, os.getcwd())
from redteam.data import load_episodes, targets_in_episode_order
from redteam import direct as D, train as T
from redteam.plan import reward_now, horizon_read
from redteam.model import device
K = "results/redteam/stability/ablation-A1/stress/learned/horizon/known"
G = 0.98
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def known_audit(w):
    p = f"results/redteam/stability/ablation-A1/stress/audit-stakes/{w}/eval.json"; j = json.load(open(p)); E = [e for x in j["episodes"] if x.startswith("mix:") for e in j["episodes"][x]]
    f = lambda e, k: float(e[k]); r = ratio_se([f(e, "half_d_lifetime_per_slot") for e in E], [f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E]); return (r[0], r[1], len(E))
PER = ["obs", "action", "chosen", "reward", "is_plant", "fulfilled", "t", "realized", "slot", "seat", "unclaimed", "charge", "charge_t"]
def filter_world(world):
    src, dst = f"{K}/{world}", f"{K}/{world}-dosing"; os.makedirs(dst, exist_ok=True); kept = []
    for f in sorted(glob.glob(f"{src}/*.npz")):
        z = np.load(f); sl, act = z["slot"], z["action"]; dosing = {k for k in np.unique(sl) if (act[sl == k] == 3).any()}; m = np.isin(sl, list(dosing))
        out = {k: (z[k][m] if k in PER else z[k]) for k in z.files}
        np.savez_compressed(os.path.join(dst, os.path.basename(f)), **out); kept.append((int(m.sum()), int(len(m)), len(dosing), len(np.unique(sl))))
    return dst, kept
def verdict(dd, kn, name):
    k_val, k_se, k_n = kn
    if k_val < 2 * k_se: return f"{name}: the known answer ({-k_val:+.1f} ± {k_se:.1f}, {k_n} seeds) cannot be told from nothing — not tested"
    same = dd[0] < 0; within = (k_val / 3) <= -dd[0] <= (k_val * 3)
    return f"{name}: fitted {dd[0]:+.1f} ± {dd[1]:.1f} against the known {-k_val:+.1f} ± {k_se:.1f} ({k_n} seeds) — the sign {'the same' if same else 'OPPOSITE'}, {'within' if within else 'OUTSIDE'} a factor of three → **{'passed' if (same and within) else 'FAILED'}**"
L = ["# The known-answer fits on the dosing slots alone (addendum 13's M3.4) — the direct policy and the world model's return head, γ 0.98, to the slot's exit\n",
     "The fits of record (known-read.md, known-wm-direct.md) were made on every slot's decisions and read on every slot's observations at the dosed seat. Here the same fits on the dosing slots' decisions alone (the slots that ever claimed; each slot's own sequence intact), "
     "read at the dosed seat on the dosing slots' observations and on every slot's; the data's own randomized difference beside (the dose a coin within the dosing slot).\n"]
for world, seat_name, known in (("first", "initial", (23.1, 3.5, 20)), ("audit-w5", "audit", known_audit("w5"))):
    dst, kept = filter_world(world)
    eps_all = load_episodes(f"{K}/{world}", set(range(1, 21))); eps = load_episodes(dst, set(range(1, 21)))
    L.append(f"## {world}: the {'first review' if world == 'first' else 'member audit seat'} dosed at 0.3 on 1 slot in 4 — {sum(k[0] for k in kept)} of {sum(k[1] for k in kept)} decisions kept ({sum(k[2] for k in kept)} dosing slots of {sum(k[3] for k in kept)} over 20 episodes)\n")
    diffs = []
    for e in eps:
        rho, ret = targets_in_episode_order(e, None, G); seat = np.asarray(e["seat"]); act = np.asarray(e["action"])
        m0 = (seat == seat_name) & (act == 0); m3 = (seat == seat_name) & (act == 3)
        if m0.any() and m3.any(): diffs.append(ret[m3].mean() - ret[m0].mean())
    dm = mse(diffs); L.append(f"The data's own answer on the dosing slots (the return after a claim less after an inspection, per episode): **{dm[0]:+.1f} ± {dm[1]:.1f}** real over {len(diffs)} episodes.\n")
    ck = f"{dst}/direct-mc.pt"
    if not os.path.exists(ck): D.main(["--data", dst, "--out", ck, "--seeds", "1-20", "--epochs", "40", "--return-horizon", "mc", "--return-gamma", str(G)])
    m, _ = D.load_direct(ck); m.to(device())
    wk = f"{dst}/wm-mc-direct.pt"
    if not os.path.exists(wk): T.main(["--data", dst, "--out", wk, "--seeds", "1-20", "--epochs", "40", "--horizon", "16", "--value", "mc", "--heads", "two", "--stride", "4", "--return-horizon", "mc", "--return-gamma", str(G), "--return-read", "direct"])
    wm, _ = T.load_model(wk); wm.to(device()); assert not horizon_read(wm) and wm.return_read == "direct"
    for grp, E in (("the dosing slots' observations", eps), ("every slot's observations", eps_all)):
        pd, pw = [], []
        for e in E:
            seat = np.asarray(e["seat"]); O = e["obs"][seat == seat_name]
            if len(O):
                q = m.q(torch.tensor(O, dtype=torch.float32, device=device())).cpu().numpy(); pd.append(float((q[:, 3] - q[:, 0]).mean()))
                idx = np.linspace(0, len(O) - 1, min(len(O), 400)).astype(int); r = np.array([reward_now(wm, O[i]) for i in idx]); pw.append(float((r[:, 3] - r[:, 0]).mean()))
        dd, dw = mse(pd), mse(pw)
        L.append(f"**Read on {grp}** ({len(pd)} seeds): the direct policy fit on the dosing slots **{dd[0]:+.1f} ± {dd[1]:.1f}** — {verdict(dd, known, 'the direct')}; the return head fit on the dosing slots **{dw[0]:+.1f} ± {dw[1]:.1f}** — {verdict(dw, known, 'the return head')}.\n")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
