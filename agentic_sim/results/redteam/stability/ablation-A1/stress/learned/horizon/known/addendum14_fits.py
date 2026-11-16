"""Addendum 14's N3.3–N3.5 (November 16, 2026; notes §113), from the collections on record — nothing collected again. (3) What one claim costs by the slot's record:
in the known-answer set at the first review (known/first, every slot's data of record), the data's own difference within the dosing slots — the return after a
claim less after an inspection, at γ 0.98 and undiscounted, both to the slot's exit — split by the slot's record at the decision (the driver's tally in the
observation: `own_plant_failures` the wrong plant verdicts of its life so far, `own_member` the tier). (4) The chains' own fits: on which data each horizon final was fit
(the offline sets and the rounds, their shares and what a claim marks in each) and, on the rounds' exploration steps at the first review — reconstructed exactly from
the rounds' seeding (`seed × 7919 + round`, the ε coin then the uniform draw; the policies draw nothing) — the data's own difference beside the final fit's read on the
same observations. (5) H4's read (reward + γ V at the predicted next latent) fit on the dosing slots alone, as known_dosing.py fit the other two.
Usage: addendum14_fits.py OUT.md  (from agentic_sim/ in the elef-redteam env)"""
import glob, os, sys, time, numpy as np, torch
sys.path.insert(0, os.getcwd())
from redteam.data import targets_in_episode_order
from redteam.obs import IDX
from redteam import direct as D, train as T
from redteam.plan import reward_now, value_read, horizon_read
from redteam.model import device
K = "results/redteam/stability/ablation-A1/stress/learned/horizon/known"; X = "results/redteam/stability/ablation-A1/stress/learned/horizon"
G = 0.98
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (np.nan, np.nan)
def load(f):
    z = np.load(f, allow_pickle=True); n = len(z["action"])
    return {k: z[k] for k in z.files if k in ("obs", "action", "chosen", "reward", "is_plant", "fulfilled", "t", "slot", "seat", "unclaimed", "charge", "charge_t")} | {"seed": int(z["seed"]), "policy": str(z["policy"])}
def pooled(x, y):                                               # the difference of two samples' means with its error (Welch)
    x, y = np.array(x, float), np.array(y, float)
    if len(x) < 2 or len(y) < 2: return (np.nan, np.nan, len(x), len(y))
    return (x.mean() - y.mean(), np.sqrt(x.var(ddof=1) / len(x) + y.var(ddof=1) / len(y)), len(x), len(y))
L = ["# Addendum 14's N3.3–N3.5 from the collections on record (November 16, 2026)\n"]
# ---- 3. what one claim costs by the slot's record (known/first: the first review dosed at 0.3 on 1 slot in 4; seeds 1–20) ----
L += ["## 3. What one claim costs, by the slot's record — the data's own difference within the dosing slots at the first review (known/first, seeds 1–20)\n",
      "The dosing slots' first-review decisions, classed by the slot's record in the observation at the decision: **clean, the tier held** (no wrong plant verdict in its life so far, a member), **clean, on probation** (none, a probationer), **a failure on it** (one or more). The return after a claim less after an inspection, by the same slot's decisions, at γ 0.98 and undiscounted, both to the slot's exit — per episode (mean ± SE over the episodes where both actions occur in the class) and pooled over the decisions (Welch's error).\n",
      "| class | decisions: claims / inspections | **γ 0.98: per episode** (episodes) | pooled | **undiscounted: per episode** | pooled |", "|---|---|---|---|---|---|"]
CL = {"clean, the tier held": lambda fl, mem: (fl == 0) & mem, "clean, on probation": lambda fl, mem: (fl == 0) & ~mem, "a failure on it": lambda fl, mem: fl > 0, "every record": lambda fl, mem: np.ones_like(mem)}
per = {c: {"d98": [], "d1": []} for c in CL}; pool = {c: {"c98": [], "i98": [], "c1": [], "i1": []} for c in CL}
for f in sorted(glob.glob(f"{K}/first/*-seed*.npz")):
    e = load(f); seat, act, sl, O = e["seat"], e["action"], e["slot"], e["obs"]
    dosing = {k for k in np.unique(sl) if (act[sl == k] == 3).any()}; m = np.isin(sl, list(dosing)) & (seat == "initial")
    _, r98 = targets_in_episode_order(e, None, G); _, r1 = targets_in_episode_order(e, None, 1.0)
    fl = np.rint(O[:, IDX["own_plant_failures"]] * 10).astype(int); mem = O[:, IDX["own_member"]] > 0.5
    for c, fn in CL.items():
        mc = m & fn(fl, mem); i3, i0 = mc & (act == 3), mc & (act == 0)
        pool[c]["c98"] += list(r98[i3]); pool[c]["i98"] += list(r98[i0]); pool[c]["c1"] += list(r1[i3]); pool[c]["i1"] += list(r1[i0])
        if i3.any() and i0.any(): per[c]["d98"].append(r98[i3].mean() - r98[i0].mean()); per[c]["d1"].append(r1[i3].mean() - r1[i0].mean())
for c in CL:
    p98 = pooled(pool[c]["c98"], pool[c]["i98"]); p1 = pooled(pool[c]["c1"], pool[c]["i1"]); a, b = mse(per[c]["d98"]), mse(per[c]["d1"])
    L.append(f"| {c} | {p98[2]} / {p98[3]} | **{a[0]:+.1f} ± {a[1]:.1f}** ({len(per[c]['d98'])}) | {p98[0]:+.1f} ± {p98[1]:.1f} | **{b[0]:+.1f} ± {b[1]:.1f}** | {p1[0]:+.1f} ± {p1[1]:.1f} |")
# ---- 4. the chains' own fits ----
L += ["", "## 4. The chains' own fits — the data each horizon final was fit on, and the rounds' exploration steps at the first review\n",
      "Each final (round 10's model) was fit on everything in its data directory: the offline sets (`careful`, `eps4`, `random4` on seeds 1–20; `claimer`, `stamper` on seeds 1–5) and the ten rounds' collections (`online1`–`online10`, seeds 1–20, the round's policy with ε 0.1 uniform over the four actions). Decisions and the claims among them by set; what a claim marks there in a word.\n",
      "| chain | set | episodes | decisions | share of the fit | claims (share) | first-review decisions | claims there (share) | what a claim marks |", "|---|---|---|---|---|---|---|---|---|"]
MARK = {"careful": "nothing (no claim)", "eps4": "a coin on a careful slot (ε 0.1, one action in four)", "random4": "a coin at every decision", "claimer": "the slot (every decision of the policy's slots)", "stamper": "nothing (a stamp, no claim)", "online": "the policy's own state (self-play, every slot the same policy) and the ε coin"}
CH = [("pa10", "direct", "direct-offline", "the pin, the direct"), ("pa10", "wm-ret", "wm-ret-offline", "the pin, the return head"), ("arm4", "direct", "direct-offline", "arm 4, the direct"), ("arm4", "wm-ret", "wm-ret-offline", "arm 4, the return head")]
comp = {}
for k, sub, dd, nm in CH:
    files = sorted(glob.glob(f"{X}/{k}-t1-b1-mc/{dd}/*-seed*.npz")); rows = {}
    for f in files:
        z = np.load(f, allow_pickle=True); pol = str(z["policy"]); key = "online" if pol.startswith("online") else pol; a = z["action"]; s = z["seat"]
        r = rows.setdefault(key, [0, 0, 0, 0, 0]); r[0] += 1; r[1] += len(a); r[2] += int((a == 3).sum()); r[3] += int((s == "initial").sum()); r[4] += int(((s == "initial") & (a == 3)).sum())
    tot = sum(r[1] for r in rows.values()); comp[nm] = rows
    for key in ("careful", "eps4", "random4", "claimer", "stamper", "online"):
        if key in rows:
            r = rows[key]; L.append(f"| {nm} | {key}{' (rounds 1–10)' if key == 'online' else ''} | {r[0]} | {r[1]:,} | {100 * r[1] / tot:.0f} in 100 | {r[2]:,} ({r[2] / r[1]:.3f}) | {r[3]:,} | {r[4]:,} ({r[4] / max(1, r[3]):.3f}) | {MARK[key]} |")
L += ["", "**The rounds' exploration steps at the first review.** The ε steps reconstructed from the rounds' seeding (checked: at every reconstructed step the stored choice equals the uniform draw). The data's own difference on them — the return at γ 0.98 to the slot's exit, by the same slot's decisions, after an ε claim less after an ε inspection — per episode (mean ± SE over the episodes with both) and pooled; beside it the final fit's read on the same observations (the direct: the return predicted for a claim less for an inspection; the return head: the same). The policy's own (non-ε) claim share at the first review by round beside, since in self-play a claim there marks the state the policy claims at.\n",
      "| chain | seat | ε steps: claims / inspections | **the data's own difference, per episode** (episodes) | pooled | **the final fit's read on the same observations** | the policy's own claim share there, rounds 1 → 10 |", "|---|---|---|---|---|---|---|"]
for k, sub, dd, nm in CH:
    if sub == "direct":
        m, _ = D.load_direct(f"{X}/{k}-t1-b1-mc/direct/models/direct-online-10.pt"); m.to(device()); readf = lambda O: (lambda q: q[:, 3] - q[:, 0])(m.q(torch.tensor(O, dtype=torch.float32, device=device())).cpu().numpy())
    else:
        wm, _ = T.load_model(f"{X}/{k}-t1-b1-mc/wm-ret/models/wm-online-10.pt"); wm.to(device()); assert not horizon_read(wm) and wm.return_read == "direct"
        readf = lambda O: np.array([(lambda r: r[3] - r[0])(reward_now(wm, O[i])) for i in np.linspace(0, len(O) - 1, min(len(O), 120)).astype(int)])
    for seat_name in (("initial", "audit") if k == "pa10" else ("initial",)):
        per_d, per_f, pc, pi, own = [], [], [], [], {}
        for rk in range(1, 11):
            for seed in range(1, 21):
                f = f"{X}/{k}-t1-b1-mc/{dd}/online{rk}-seed{seed}.npz"
                if not os.path.exists(f): continue
                e = load(f); ch = e["chosen"]; n = len(ch); r = np.random.default_rng(seed * 7919 + rk); eps = np.zeros(n, bool); draw = np.full(n, -1)
                for i in range(n):
                    if r.random() < 0.1: eps[i] = True; draw[i] = int(r.integers(4))
                assert (ch[eps] == draw[eps]).all(), f
                _, r98 = targets_in_episode_order(e, None, G); s = e["seat"] == seat_name
                i3, i0 = eps & s & (ch == 3), eps & s & (ch == 0); pc += list(r98[i3]); pi += list(r98[i0])
                if i3.any() and i0.any(): per_d.append(r98[i3].mean() - r98[i0].mean())
                Oe = e["obs"][eps & s]
                if len(Oe): per_f.append(float(readf(Oe).mean()))
                o = own.setdefault(rk, [0, 0]); ns = (~eps) & s; o[0] += int(ns.sum()); o[1] += int((ns & (ch == 3)).sum())
        p = pooled(pc, pi); a, b = mse(per_d), mse(per_f)
        L.append(f"| {nm} | {'the first review' if seat_name == 'initial' else 'the member audit seat'} | {p[2]} / {p[3]} | **{a[0]:+.1f} ± {a[1]:.1f}** ({len(per_d)}) | {p[0]:+.1f} ± {p[1]:.1f} | **{b[0]:+.1f} ± {b[1]:.1f}** ({len(per_f)} episodes) | {' → '.join(f'{own[rk][1] / max(1, own[rk][0]):.2f}' for rk in (1, 3, 5, 7, 10) if rk in own)} |")
# ---- 5. H4's read fit on the dosing slots alone ----
L += ["", "## 5. H4's read (reward + γ V at the predicted next latent) fit on the dosing slots alone, read at the dosed seat on the dosing slots' observations\n",
      "| world | the data's own difference (§112) | **H4's read, fit on the dosing slots** (per seed ± SE) | the H4 fit of record (every slot), read on the dosing slots' observations | the H4 fit of record as read in §111 (every slot's observations) | fit time |", "|---|---|---|---|---|---|"]
for world, seat_name, own_d, rec in (("first", "initial", "−5.5 ± 2.3", "−4.8 ± 0.4"), ("audit-w5", "audit", "−5.2 ± 4.5", "−3.8 ± 0.5")):
    dst = f"{K}/{world}-dosing"; wk = f"{dst}/wm-mc.pt"; t0 = time.time()
    if not os.path.exists(wk): T.main(["--data", dst, "--out", wk, "--seeds", "1-20", "--epochs", "40", "--horizon", "16", "--value", "mc", "--heads", "two", "--stride", "4", "--return-horizon", "mc", "--return-gamma", str(G)])
    secs = time.time() - t0
    wm, _ = T.load_model(wk); wm.to(device()); assert horizon_read(wm)
    wr, _ = T.load_model(f"{K}/{world}/wm-mc.pt"); wr.to(device()); assert horizon_read(wr)
    pv, pr = [], []
    for f in sorted(glob.glob(f"{dst}/*-seed*.npz")):
        e = load(f); O = e["obs"][e["seat"] == seat_name]
        if len(O):
            idx = np.linspace(0, len(O) - 1, min(len(O), 300)).astype(int)
            pv.append(float(np.mean([(lambda v: v[3] - v[0])(value_read(wm, O[i])) for i in idx]))); pr.append(float(np.mean([(lambda v: v[3] - v[0])(value_read(wr, O[i])) for i in idx])))
    a, b = mse(pv), mse(pr)
    L.append(f"| {'the first review' if world == 'first' else 'world 5, the member audit seat'} | {own_d} | **{a[0]:+.1f} ± {a[1]:.1f}** ({len(pv)} seeds) | {b[0]:+.1f} ± {b[1]:.1f} | {rec} | {secs / 60:.1f} min |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
