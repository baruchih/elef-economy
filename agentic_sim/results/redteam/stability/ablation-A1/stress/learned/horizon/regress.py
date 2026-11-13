"""The learner with a horizon's regression test (addendum 10's J5, the first of I5's three tests; November 13, 2026; notes §111) at ffd23d851: a horizon of 1
reproduces the chains of record to the decimal. Three readings on the pin's chain of record (stress/learned/pa10-t1-b1, the one-decision learners):
(a) the return target at a horizon of 1 equals the stored `reward` of every episode of the chain's data (the direct's set and the online rounds), exactly;
(b) stored episodes replayed by their recorded actions on the environment as built (the export in) give the attributed reward within float32 of the stored
    `reward` — the attribution is unchanged — and the export's three arrays of the episode's length;
(c) the direct policy refit at a horizon of 1 by the code as built, and by the code of record (f9c0dbb3e's data.py and direct.py in a temporary package), on the
    same data, the same torch seed, on the CPU: identical weights; the world model's trainer the same on two epochs.
Usage: regress.py OUT.md  (from agentic_sim/ in the elef-redteam env)"""
import glob, importlib, json, os, subprocess, sys, tempfile, time
import numpy as np, torch
sys.path.insert(0, os.getcwd())
from redteam.data import load_episodes, targets_in_episode_order
X = "results/redteam/stability/ablation-A1/stress/learned/pa10-t1-b1"
CELL = "--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.10 --pi-a-max 0.10 --temptation 1 --bond-mult-later 1".split()
L = ["# The regression at a horizon of 1 (I5's first test) — the pin's chain of record at ffd23d851\n"]
# (a)
n_files = n_dec = 0; worst = 0.0
for f in sorted(glob.glob(f"{X}/direct-offline/*-seed*.npz")):
    z = np.load(f, allow_pickle=True)
    e = {"reward": z["reward"], "action": z["action"], "t": z["t"], "slot": z["slot"] if "slot" in z.files else None,
         "unclaimed": np.zeros(len(z["action"]), np.float32), "charge": np.zeros(len(z["action"]), np.float32), "charge_t": np.full(len(z["action"]), -1)}
    rho, ret = targets_in_episode_order(e, 1, 0.98)
    worst = max(worst, float(np.abs(ret - z["reward"].astype(np.float64)).max()) if len(ret) else 0.0); n_files += 1; n_dec += len(ret)
L.append(f"**(a) The target at a horizon of 1 is the stored reward.** {n_files} files, {n_dec} decisions of the chain's data (the offline set and the ten rounds): the largest difference {worst:.3g} — {'identical' if worst == 0 else 'NOT identical'}.\n")
# (b)
from redteam.env import ElefReviewerEnv
env = ElefReviewerEnv(CELL, ticks=1000, role="reviewer", attrib="own")
rows = []
for f in [f"{X}/direct-offline/careful-seed1.npz", f"{X}/direct-offline/eps4-seed2.npz", f"{X}/direct-offline/online10-seed3.npz"]:
    z = np.load(f, allow_pickle=True); chosen = z["chosen"]; seed = int(z["seed"])
    obs, info = env.reset(seed=seed); done = info.get("terminal", False); i = 0
    while not done:
        obs, r, done, _, info = env.step(int(chosen[i])); i += 1
    att = np.asarray(info["attributed"], np.float64); st = z["reward"].astype(np.float64)
    d = float(np.abs(att - st).max()); u = np.asarray(info["unclaimed"]); ch = np.asarray(info["charge"])
    rows.append((os.path.basename(f), i, len(chosen), d, float(u.sum()), float(info["attribution"]["pre_boundary_real"]), float(ch.sum()), int((ch != 0).sum())))
env.close()
L.append("**(b) Stored episodes replayed by their recorded actions on the environment as built:** the attributed reward against the stored `reward` (float32), the export beside.\n")
L.append("| episode | decisions replayed / stored | max |attributed − stored| | unclaimed (sum, real) | pre-boundary (real) | suspension charges (sum) | decisions charged |"); L.append("|---|---|---|---|---|---|---|")
for r in rows: L.append(f"| {r[0]} | {r[1]} / {r[2]} | {r[3]:.2e} | {r[4]:.1f} | {r[5]:.1f} | {r[6]:.1f} | {r[7]} |")
L.append(f"\nThe attribution is {'unchanged within float32 (every difference under 1e-3)' if all(r[3] < 1e-3 for r in rows) else 'CHANGED'}.\n")
# (c)
tmp = tempfile.mkdtemp(); pkg = os.path.join(tmp, "redteam_old"); os.makedirs(pkg)
open(os.path.join(pkg, "__init__.py"), "w").close()
for m in ("data", "direct", "train", "model"):
    src = subprocess.run(["git", "show", f"f9c0dbb3e:agentic_sim/redteam/{m}.py"], capture_output=True, text=True, check=True).stdout
    src = src.replace("from redteam.data import", "from redteam_old.data import").replace("from redteam.model import", "from redteam_old.model import").replace("from redteam.train import", "from redteam_old.train import")
    src = src.replace("from .lewm.module import", "from redteam.lewm.module import")
    open(os.path.join(pkg, f"{m}.py"), "w").write(src)
sys.path.insert(0, tmp)
import redteam.model as NM, redteam.direct as ND, redteam.train as NT
import redteam_old.model as OM, redteam_old.direct as OD, redteam_old.train as OT
cpu = lambda: torch.device("cpu")
NM.device = OM.device = ND.device = OD.device = NT.device = OT.device = cpu
def fit_direct(mod, out, extra):
    t0 = time.time(); mod.main(["--data", f"{X}/direct-offline", "--out", out, "--seeds", "1-20", "--epochs", "6", "--torch-seed", "0"] + extra); return time.time() - t0
d_new = os.path.join(tmp, "direct-new.pt"); d_old = os.path.join(tmp, "direct-old.pt")
t_new = fit_direct(ND, d_new, ["--return-horizon", "1"]); t_old = fit_direct(OD, d_old, [])
sn, so = torch.load(d_new, map_location="cpu")["state"], torch.load(d_old, map_location="cpu")["state"]
same_d = all(torch.equal(sn[k], so[k]) for k in sn) and set(sn) == set(so)
L.append(f"**(c) The direct policy refit at a horizon of 1, the code as built against the code of record (f9c0dbb3e), on the chain's data, torch seed 0, six epochs, on the CPU:** the weights {'identical, tensor for tensor' if same_d else 'DIFFER'} ({len(sn)} tensors; {t_new:.0f} s / {t_old:.0f} s).\n")
def fit_wm(mod, out, extra):
    mod.main(["--data", f"{X}/wm-offline", "--out", out, "--seeds", "1-3", "--epochs", "2", "--horizon", "16", "--value", "mc", "--heads", "two", "--stride", "8", "--torch-seed", "0"] + extra)
w_new = os.path.join(tmp, "wm-new.pt"); w_old = os.path.join(tmp, "wm-old.pt")
fit_wm(NT, w_new, ["--return-horizon", "1"]); fit_wm(OT, w_old, [])
sn, so = torch.load(w_new, map_location="cpu")["state"], torch.load(w_old, map_location="cpu")["state"]
same_w = all(torch.equal(sn[k], so[k]) for k in sn) and set(sn) == set(so)
L.append(f"**The world model's trainer the same** (seeds 1–3, two epochs, horizon 16, the value head, two heads, stride 8, on the CPU): the weights {'identical, tensor for tensor' if same_w else 'DIFFER'} ({len(sn)} tensors).\n")
L.append(f"**Verdict:** {'passed' if (worst == 0 and all(r[3] < 1e-3 for r in rows) and same_d and same_w) else 'FAILED'} — a horizon of 1 reproduces the chain of record: the same targets, the same attribution, the same fit.")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
