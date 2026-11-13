"""The learner with a horizon's known-answer test and the return's spread (addendum 10's J5, I5's second and third tests; November 13, 2026; notes §111) at
ffd23d851. On a dose world's data (known/first: the pin, the dosing slots 1 in 4 at a dose of 0.3 at the first review alone; known/audit: the same at the member's
audit seat alone; known/audit1: a dose of 1 there — J4's world 2, whose known answer can be told from nothing where world 1's cannot; seeds 1–20, collected with the horizon's export): (i) the return target to the slot's exit at γ 0.98 by seat and action — n, mean, SD — for
the dosing slots (the slots that ever claimed) and for all, and the randomized difference at the dosed seat on the dosing slots (a claim there is the policy's
coin, so the mean return after a claim less after an inspection is the data's own answer); (ii) the direct policy fit on it at the horizon (40 epochs) and read
on the dosed seat's observations — the fitted return of a claim less an inspection, per seed, mean ± SE; (iii) the world model fit the same way (the value head
at the return, two heads, horizon 16, stride 4) and read by the head alone as reward + γ V(next). The known answer at the first review is §110's 23.1 ± 3.5
real lost a claim (the lifetime lost for each claim; the same sign, within a factor of three, passes); at the audit seat J4's world 1 (read from its eval.json),
tested when it can be told from nothing.  Usage: known_read.py OUT.md [--skip-wm]"""
import glob, json, os, sys, time
import numpy as np, torch
sys.path.insert(0, os.getcwd())
from redteam.data import load_episodes, targets_in_episode_order, by_slot
from redteam import direct as D, train as T
from redteam.plan import value_read, reward_now
from redteam.model import device
K = "results/redteam/stability/ablation-A1/stress/learned/horizon/known"
G = 0.98
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def known_audit(w="w1"):                                                   # J4's world: the lifetime lost for each claim on sixty seeds (w1 a dose of 0.3, w2 a dose of 1)
    p = f"results/redteam/stability/ablation-A1/stress/audit-stakes/{w}/eval.json"
    if not os.path.exists(p): return None
    j = json.load(open(p)); E = [e for x in j["episodes"] if x.startswith("mix:") for e in j["episodes"][x]]
    f = lambda e, k: float(e[k]); return ratio_se([f(e, "half_d_lifetime_per_slot") for e in E], [f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E]) + (len(E),)
L = ["# The known-answer test and the return's spread (I5's second and third tests) — the direct policy and the world model at a horizon to the slot's exit, γ 0.98\n"]
skip_wm = "--skip-wm" in sys.argv
for world, seat_name, known, dose in (("first", "initial", (23.1, 3.5, 20), 0.3), ("audit", "audit", known_audit("w1"), 0.3), ("audit1", "audit", known_audit("w2"), 1.0), ("audit-w5", "audit", known_audit("w5"), 0.3)):
    d = f"{K}/{world}"
    eps = load_episodes(d, set(range(1, 21)))
    if not eps: L.append(f"## {world}: (pending)\n"); continue
    seat_title = "first review" if world == "first" else "member's audit seat"
    cell_name = "J4's world 5 cell: π^A 0.30, the fee doubled" if world == "audit-w5" else "the pin"
    L.append(f"## The {seat_title} dosed at {dose} on 1 slot in 4 ({cell_name}; {len(eps)} episodes, {sum(len(e['action']) for e in eps)} decisions)\n")
    # (i) the spread
    rows = {}; diffs = []
    for e in eps:
        rho, ret = targets_in_episode_order(e, None, G)
        seat = np.asarray(e["seat"]); act = np.asarray(e["action"]); sl = np.asarray(e["slot"])
        dosing = {k for k in np.unique(sl) if (act[sl == k] == 3).any()}
        is_d = np.isin(sl, list(dosing))
        for grp, mask in (("dosing", is_d), ("all", np.ones(len(act), bool))):
            for s in ("initial", "audit", "panel", "resumed"):
                for a in (0, 3):
                    m = mask & (seat == s) & (act == a)
                    if m.any(): rows.setdefault((grp, s, a), []).append(ret[m])
        m0 = is_d & (seat == seat_name) & (act == 0); m3 = is_d & (seat == seat_name) & (act == 3)
        if m0.any() and m3.any(): diffs.append(ret[m3].mean() - ret[m0].mean())
    L.append("**(i) The return's spread, with the decisions behind each action at each seat** (the return to the slot's exit at γ 0.98, real; pooled over the 20 episodes):\n")
    L.append("| slots | seat | action | n | mean | SD | SE |"); L.append("|---|---|---|---|---|---|---|")
    for (grp, s, a), v in sorted(rows.items()):
        x = np.concatenate(v); L.append(f"| {grp} | {s} | {'inspect' if a == 0 else 'claim'} | {len(x)} | {x.mean():.1f} | {x.std(ddof=1):.1f} | {x.std(ddof=1) / np.sqrt(len(x)):.1f} |")
    dm = mse(diffs)
    L.append(f"\n**The data's own answer at the {seat_name} seat on the dosing slots** (a claim there the policy's coin): the return after a claim less after an inspection, per episode, **{dm[0]:+.1f} ± {dm[1]:.1f}** real over {len(diffs)} episodes.\n")
    # (ii) the direct
    ck = f"{d}/direct-mc.pt"
    if not os.path.exists(ck):
        D.main(["--data", d, "--out", ck, "--seeds", "1-20", "--epochs", "40", "--return-horizon", "mc", "--return-gamma", str(G)])
    m, _ = D.load_direct(ck); m.to(device())
    per_seed = []
    for e in eps:
        seat = np.asarray(e["seat"]); X = torch.tensor(e["obs"][seat == seat_name], dtype=torch.float32, device=device())
        if len(X): q = m.q(X).cpu().numpy(); per_seed.append(float((q[:, 3] - q[:, 0]).mean()))
    dd = mse(per_seed)
    kn = known
    def verdict(dd, kn, name):
        if kn is None: return f"{name}: the known answer is not yet on record (J4's world 1 pending)"
        k_val, k_se, k_n = kn
        if k_val < 2 * k_se: return f"{name}: the known answer ({-k_val:+.1f} ± {k_se:.1f}, {k_n} seeds) cannot be told from nothing — not tested here"
        same = dd[0] < 0; within = (k_val / 3) <= -dd[0] <= (k_val * 3)
        return f"{name}: fitted {dd[0]:+.1f} ± {dd[1]:.1f} against the known {-k_val:+.1f} ± {k_se:.1f} — the sign {'the same' if same else 'OPPOSITE'}, {'within' if within else 'OUTSIDE'} a factor of three → **{'passed' if (same and within) else 'FAILED'}**"
    L.append(f"**(ii) The direct policy** fit at the horizon (40 epochs; `direct-mc.pt`), read on every {seat_name}-seat observation: the fitted return of a claim less an inspection, per seed, **{dd[0]:+.1f} ± {dd[1]:.1f}** real. {verdict(dd, kn, 'the direct')}.\n")
    # (iii) the world model
    if not skip_wm:
        wk = f"{d}/wm-mc.pt"
        if not os.path.exists(wk):
            T.main(["--data", d, "--out", wk, "--seeds", "1-20", "--epochs", "40", "--horizon", "16", "--value", "mc", "--heads", "two", "--stride", "4", "--return-horizon", "mc", "--return-gamma", str(G)])
        wm, _ = T.load_model(wk); wm.to(device())
        per_seed_w, per_seed_r = [], []
        for e in eps:
            seat = np.asarray(e["seat"]); O = e["obs"][seat == seat_name]
            if len(O):
                idx = np.linspace(0, len(O) - 1, min(len(O), 400)).astype(int)        # a sample of the seat's observations (the read is one forward pass each)
                v = np.array([value_read(wm, O[i]) for i in idx]); r = np.array([reward_now(wm, O[i]) for i in idx])
                per_seed_w.append(float((v[:, 3] - v[:, 0]).mean())); per_seed_r.append(float((r[:, 3] - r[:, 0]).mean()))
        dw = mse(per_seed_w); dr = mse(per_seed_r)
        L.append(f"**(iii) The world model** fit the same way (`wm-mc.pt`), read by the head alone as reward + γ V(next) on the {seat_name}-seat observations (up to 400 a seed): a claim less an inspection **{dw[0]:+.1f} ± {dw[1]:.1f}** real (the reward head's one decision alone {dr[0]:+.1f} ± {dr[1]:.1f}). {verdict(dw, kn, 'the world model')}.\n")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
