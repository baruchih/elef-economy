"""Addendum 9's I3.1 (November 12, 2026; notes §110): the entry test's worlds by group — the ticks a slot is in place, the lifetime for each tick in place,
and where a claiming slot's wallet comes from — read from the slots' own readings kept by the re-reads at b5961bf9f (`<cell>-at-b5961bf9f/`: the same
worlds, run again whole with the driver's per-slot readings; every group figure of record checked identical). The groups by the wrapper's hash (the first
two bytes of md5("<seed>:<name>") against share × 65536). Per group, the mean over seeds 21–40 of the per-seed per-slot figure: the ticks in place (from
the arrival tick, 0 for a genesis name, to the departure tick or the run's end), the lifetime a slot (the wallet net of its loan at the index or the
take-out, plus the private benefit), the lifetime a tick in place (the group's lifetime over its ticks), the wallet's sources from the public record in
nominal credits a slot — the deliveries' prices, the review fees (fixed + uplift + emission), the reimbursements, the costs bought (effort and care), the
bonds and guarantees forfeited — the awards and reviews a slot, the arrival loans (lent, repaid from income, recovered at departure, defaulted) a slot, and
the share of the group's slots that are arrival-born and alive at the end.  Usage: entry_slots_read.py OUT.md"""
import json, os, sys, hashlib, numpy as np
R = "results/redteam/stability/ablation-A1/stress"; C = "b5961bf9f"
ARMS = [("pa10", "the pin"), ("arm4", "arm 4")]; LEARN = [("direct", "direct", "mix:direct"), ("wm", "head alone", "mix:greedy")]; SHARES = [0.1, 0.25, 0.5, 0.75]
def group(seed, name, share):
    h = int.from_bytes(hashlib.md5(f"{seed}:{name}".encode()).digest()[:2], "big"); return "claim" if h < share * 65536 else "care"
def load(k, l, s, pol, suffix):
    d = f"{R}/f41/{k}-{l}{suffix}" if s == 0.5 else f"{R}/entry/{k}-{l}-s{s}{suffix}"
    p = f"{d}/eval.json"
    return json.load(open(p))["episodes"][pol if s == 0.5 else f"{pol}:{s}"] if os.path.exists(p) else None
def f(e, k): v = e.get(k); return float(v) if v not in (None, "") else np.nan
def mse(x): x = np.array(x, float); x = x[~np.isnan(x)]; return (x.mean(), x.std(ddof=1) / np.sqrt(len(x))) if len(x) > 1 else (x.mean() if len(x) else np.nan, np.nan)
L = ["# The entry test's worlds by group (I3.1): the ticks in place, the lifetime a tick, where the wallet comes from — the re-reads at b5961bf9f\n",
     "Each row one group of one mixed world; the figures the mean over seeds of the per-seed per-slot figure. The wallet's sources are nominal credits over the slot's life from the public record "
     "(a claiming slot's care cost is claimed and reimbursed as a careful review's, so `reimbursed` carries the claims too); the lifetime and the benefit are real. "
     "`loan` is the bank's arrival loan to the group's arrival-born names (lent = repaid + recovered + defaulted + outstanding).\n",
     "| arm, learner | share | group | slots; arrival-born; alive at end | ticks in place a slot | lifetime a slot (wallet + benefit) | **lifetime a tick in place** | deliveries; fees (fixed + uplift + emission); reimbursed; costs; bonds + guarantees forfeited (nominal, a slot) | awards; reviews a slot | loan lent; repaid; recovered; defaulted (nominal, a slot) | the record's group figures |",
     "|---|---|---|---|---|---|---|---|---|---|---|"]
for k, kn in ARMS:
    for l, ln, pol in LEARN:
        for s in SHARES:
            E = load(k, l, s, pol, f"-at-{C}"); E0 = load(k, l, s, pol, "-at-4df18f1bc")
            if E is None: L.append(f"| {kn}, {ln} | {s} | (pending) | | | | | | | | |"); continue
            same = all(abs(f(a, kk) - f(b, kk)) < 1e-6 or (np.isnan(f(a, kk)) and np.isnan(f(b, kk))) for a, b in zip(E, E0) for kk in a if kk.startswith("half_") and kk != "half_share") if E0 else None
            share = s
            for g in ("claim", "care"):
                acc = {x: [] for x in ("n", "born", "alive", "ticks", "life", "lpt", "deliv", "fees", "reimb", "costs", "forf", "awards", "reviews", "lent", "repaid", "recov", "defl")}
                for e in E:
                    slots = {x: v for x, v in json.loads(e["learner_slots_json"]).items() if group(int(e["seed"]), x, share) == g}
                    n = len(slots)
                    if not n: continue
                    V = list(slots.values())
                    life = sum(v["wealth_real"] + v["private_real"] for v in V); ticks = sum(v["ticks"] for v in V)
                    acc["n"].append(n); acc["born"].append(sum(1 for v in V if v["t_in"] > 0) / n); acc["alive"].append(sum(v["alive"] for v in V) / n)
                    acc["ticks"].append(ticks / n); acc["life"].append(life / n); acc["lpt"].append(life / ticks)
                    acc["deliv"].append(sum(v["delivery"] for v in V) / n); acc["fees"].append(sum(v["fee_fixed"] + v["fee_uplift"] + v["fee_emission"] for v in V) / n)
                    acc["reimb"].append(sum(v["reimbursed"] for v in V) / n); acc["costs"].append(sum(v["costs"] for v in V) / n)
                    acc["forf"].append(sum(v["bonds_forfeited"] + v["guarantees_forfeited"] for v in V) / n); acc["awards"].append(sum(v["awards"] for v in V) / n); acc["reviews"].append(sum(v["reviews"] for v in V) / n)
                    lent = sum(v["loan_repaid"] + v["loan_recovered"] + v["loan_defaulted"] + (v["loan_outstanding"] if v["alive"] else 0.0) for v in V)
                    acc["lent"].append(lent / n); acc["repaid"].append(sum(v["loan_repaid"] for v in V) / n); acc["recov"].append(sum(v["loan_recovered"] for v in V) / n); acc["defl"].append(sum(v["loan_defaulted"] for v in V) / n)
                m = {x: mse(v) for x, v in acc.items()}
                L.append(f"| {kn}, {ln} | {s} | {'claiming' if g == 'claim' else 'careful'} | {m['n'][0]:.1f}; {m['born'][0]:.2f}; {m['alive'][0]:.2f} | {m['ticks'][0]:.0f} ± {m['ticks'][1]:.0f} | {m['life'][0]:.0f} ± {m['life'][1]:.0f} | **{m['lpt'][0]:.3f} ± {m['lpt'][1]:.3f}** | "
                         f"{m['deliv'][0]:.0f}; {m['fees'][0]:.0f}; {m['reimb'][0]:.0f}; {m['costs'][0]:.0f}; {m['forf'][0]:.0f} | {m['awards'][0]:.1f}; {m['reviews'][0]:.1f} | {m['lent'][0]:.1f}; {m['repaid'][0]:.1f}; {m['recov'][0]:.1f}; {m['defl'][0]:.1f} | {'identical' if same else ('DIFFER' if same is not None else '—')} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
