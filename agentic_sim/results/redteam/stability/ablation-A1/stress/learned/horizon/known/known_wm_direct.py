"""The world model's second read under a horizon on the known-answer data (November 13, 2026; notes §111; at 04f1c5565): the reward head fit to the H-step return
itself on the latent (`--return-read direct`; mc, γ 0.98, 40 epochs, horizon 16, two heads, stride 4) and read alone at the dosed seat — a claim less an inspection,
per seed, mean ± SE — against the known answer (the first review 23.1 ± 3.5; the audit seat J4's world 1, 4.0 ± 4.8, untestable; J4's world 2 at a dose of 1,
15.0 ± 2.9).  Usage: known_wm_direct.py OUT.md"""
import json, os, sys, numpy as np, torch
sys.path.insert(0, os.getcwd())
from redteam.data import load_episodes
from redteam import train as T
from redteam.plan import reward_now, horizon_read
from redteam.model import device
K = "results/redteam/stability/ablation-A1/stress/learned/horizon/known"
def mse(x): x = np.array(x, float); return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def ratio_se(num, den):
    num, den = np.array(num, float), np.array(den, float); n = len(num); a, b = num.mean(), den.mean(); cov = np.cov(num, den, ddof=1)
    r = a / b; return r, abs(r) * np.sqrt(cov[0, 0] / a**2 + cov[1, 1] / b**2 - 2 * cov[0, 1] / (a * b)) / np.sqrt(n)
def known_audit(w):
    p = f"results/redteam/stability/ablation-A1/stress/audit-stakes/{w}/eval.json"; j = json.load(open(p)); E = [e for x in j["episodes"] if x.startswith("mix:") for e in j["episodes"][x]]
    f = lambda e, k: float(e[k]); r = ratio_se([f(e, "half_d_lifetime_per_slot") for e in E], [f(e, "half_claim_claims") / f(e, "half_claim_slots") for e in E]); return (r[0], r[1], len(E))
L = ["# The world model under the return-head read (`--return-read direct`): the known-answer test at each dosed seat\n"]
for world, seat_name, known in (("first", "initial", (23.1, 3.5, 20)), ("audit", "audit", known_audit("w1")), ("audit1", "audit", known_audit("w2")), ("audit-w5", "audit", known_audit("w5"))):
    d = f"{K}/{world}"; eps = load_episodes(d, set(range(1, 21)))
    if not eps: L.append(f"## {world}: (pending)\n"); continue
    wk = f"{d}/wm-mc-direct.pt"
    if not os.path.exists(wk):
        T.main(["--data", d, "--out", wk, "--seeds", "1-20", "--epochs", "40", "--horizon", "16", "--value", "mc", "--heads", "two", "--stride", "4", "--return-horizon", "mc", "--return-gamma", "0.98", "--return-read", "direct"])
    wm, _ = T.load_model(wk); wm.to(device()); assert not horizon_read(wm) and wm.return_read == "direct"
    per_seed = []
    for e in eps:
        seat = np.asarray(e["seat"]); O = e["obs"][seat == seat_name]
        if len(O):
            idx = np.linspace(0, len(O) - 1, min(len(O), 400)).astype(int); r = np.array([reward_now(wm, O[i]) for i in idx]); per_seed.append(float((r[:, 3] - r[:, 0]).mean()))
    dd = mse(per_seed); k_val, k_se, k_n = known
    if k_val < 2 * k_se: v = f"the known answer ({-k_val:+.1f} ± {k_se:.1f}, {k_n} seeds) cannot be told from nothing — not tested"
    else:
        same = dd[0] < 0; within = (k_val / 3) <= -dd[0] <= (k_val * 3)
        v = f"against the known {-k_val:+.1f} ± {k_se:.1f} ({k_n} seeds): the sign {'the same' if same else 'OPPOSITE'}, {'within' if within else 'OUTSIDE'} a factor of three → **{'passed' if (same and within) else 'FAILED'}**"
    L.append(f"**{world} ({seat_name} seat, {len(eps)} episodes):** the return head's read, a claim less an inspection, per seed **{dd[0]:+.1f} ± {dd[1]:.1f}** real — {v}.\n")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
