"""§8.6 (the ruling after §69): the review fees by seat and by who sat — the state's review-fee income and the members' panel income —
on a chain's finals: the learned population (direct, head alone) and the hand on the same seeds. From the ledger's events: every
`feepot_out` "… review fee" (the seat's fixed fee at settlement) credited to a member, a troop (the state) or a plant alias, keyed by the
review's role (initial / audit / appeal / dispute …) and the case's kind (real / plant); beside them the duty uplift paid, the court fees
won by the state, Ω's service fees, and the bonds burned by kind of sitter (the price of a wrong seat). Means over the seeds, real at P_0
(nominal / index at the event's tick is not kept in the event, so the figures are nominal — stated).
Usage: seat_income.py "<cell>" seeds direct-model wm-model OUT.md"""
import sys, numpy as np
sys.path.insert(0, ".")
from collections import defaultdict
from redteam.env import ElefReviewerEnv, policy_of
from redteam.train import load_model
from redteam.plan import GreedyPolicy, boundary_read_for
from redteam.direct import load_direct, DirectPolicy
from redteam.model import device
cell = sys.argv[1].split(); seeds = [int(x) for x in sys.argv[2].split(",")]; dmp, wmp, out = sys.argv[3], sys.argv[4], sys.argv[5]
br = boundary_read_for(cell, "auto")
dm, _ = load_direct(dmp); dm.to(device()); wm, ck = load_model(wmp); wm.to(device())
pols = {"direct": DirectPolicy(dm, boundary_read=br), "head alone": GreedyPolicy(wm, boundary_read=br), "hand": policy_of("hand", "reviewer")}
res = {n: [] for n in pols}; paths = {}
def who(W, wid):
    if wid is None: return "none"
    if W.is_troop(wid): return "state"
    if str(wid).startswith("plant_rev:") or wid == "PLANT_REV": return "plant alias"
    return "member"
for seed in seeds:
    for name, pol in pols.items():
        env = ElefReviewerEnv(cell, ticks=1000, role="reviewer")
        obs, info = env.reset(seed=seed); rng = np.random.default_rng(seed); done = info.get("terminal", False)
        while not done:
            obs, r, done, _, info = env.step(int(pol(obs, rng)))
        run = env.run; W = run.w._w
        ev = W.ledger.events          # the ledger's own copy (the view's events_since carries public ids)
        fees = defaultdict(float); fees_n = defaultdict(int); other = defaultdict(float)
        for e in ev:
            k, n = e.kind, e.note or ""
            if k == "feepot_out" and n.endswith("review fee"):
                c = W.cases.get(e.case) if e.case is not None else None
                role = "?"
                if c is not None:
                    for rid in c.reviews:
                        rv = W.reviews[rid]
                        if rv.reviewer == e.dst: role = rv.role
                kind = "plant" if (c is not None and getattr(c, "plant", None)) else "real"
                key = (who(W, e.dst), role, kind); fees[key] += e.amount; fees_n[key] += 1
            elif k == "transfer" and n == "duty uplift": other[("uplift", who(W, e.dst))] += e.amount
            elif k == "forfeit_to" and "court fee" in n: other[("court fee won", who(W, e.dst))] += e.amount
            elif k == "transfer" and n == "service fee": other[("service fee to Ω", "state")] += e.amount
            elif k == "burn_bond": other[("bond burned", who(W, e.src))] += e.amount
        # the dial per seat's path: the base (members' audits of real approvals) a period, m^A, π^A and the pool at each close
        path = [(per.get("real_member_audits"), per.get("m_A"), per.get("pi_A"), (per.get("seat_pool") or {}).get("A"), per.get("pa_audit_adj"), per.get("pa_audit_confirmed")) for per in W.periods]
        other[("members' audits of real approvals (the base), a run", "member")] += float(sum((per.get("real_member_audits") or 0) for per in W.periods))
        paths.setdefault(name, []).append((seed, path))
        res[name].append((dict(fees), dict(fees_n), dict(other)))
        tot = defaultdict(float)
        for (w, role, kind), v in fees.items(): tot[w] += v
        print(f"seed {seed} {name}: review fees — " + ", ".join(f"{w} {v:.0f}" for w, v in sorted(tot.items())) + "; " + ", ".join(f"{a} to {b} {v:.0f}" for (a, b), v in sorted(other.items())), flush=True)
L = [f"# §8.6: the review fees by seat and by who sat — {' '.join(cell)}; seeds {seeds[0]}–{seeds[-1]}; the finals' direct ({dmp}) and head alone ({wmp}), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.\n"]
def ms(v): v = np.asarray(v, float); return f"{v.mean():.0f} ± {v.std(ddof=1)/np.sqrt(len(v)):.0f}" if len(v) > 1 else f"{v.mean():.0f}"
keys = sorted({k for n in pols for f, _, _ in res[n] for k in f})
L.append("| who sat | seat | case kind | " + " | ".join(pols) + " | " + " | ".join(f"{p} (seats)" for p in pols) + " |"); L.append("|---|---|---|" + "---|" * (2 * len(pols)))
for key in keys:
    L.append(f"| {key[0]} | {key[1]} | {key[2]} | " + " | ".join(ms([f.get(key, 0.0) for f, _, _ in res[n]]) for n in pols) + " | " + " | ".join(f"{np.mean([c.get(key, 0) for _, c, _ in res[n]]):.1f}" for n in pols) + " |")
L.append("\nTotals by who sat (review fees a run):\n"); L.append("| who sat | " + " | ".join(pols) + " |"); L.append("|---|" + "---|" * len(pols))
for w in ("member", "state", "plant alias"):
    L.append(f"| {w} | " + " | ".join(ms([sum(v for (ww, _, _), v in f.items() if ww == w) for f, _, _ in res[n]]) for n in pols) + " |")
L.append("\nThe members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:\n"); L.append("| reading | " + " | ".join(pols) + " |"); L.append("|---|" + "---|" * len(pols))
L.append("| members' panel fees | " + " | ".join(ms([sum(v for (ww, r, _), v in f.items() if ww == "member" and r in ("appeal", "dispute")) for f, _, _ in res[n]]) for n in pols) + " |")
L.append("| members' audit-seat fees | " + " | ".join(ms([sum(v for (ww, r, _), v in f.items() if ww == "member" and r == "audit") for f, _, _ in res[n]]) for n in pols) + " |")
L.append("| state's audit-seat fees | " + " | ".join(ms([sum(v for (ww, r, _), v in f.items() if ww == "state" and r == "audit") for f, _, _ in res[n]]) for n in pols) + " |")
L.append("| state's panel fees | " + " | ".join(ms([sum(v for (ww, r, _), v in f.items() if ww == "state" and r in ("appeal", "dispute")) for f, _, _ in res[n]]) for n in pols) + " |")
L.append("| state's initial-seat fees | " + " | ".join(ms([sum(v for (ww, r, _), v in f.items() if ww == "state" and r == "initial") for f, _, _ in res[n]]) for n in pols) + " |")
okeys = sorted({k for n in pols for _, _, o in res[n] for k in o})
L.append("\nBeside:\n"); L.append("| flow | to / from | " + " | ".join(pols) + " |"); L.append("|---|---|" + "---|" * len(pols))
for key in okeys:
    L.append(f"| {key[0]} | {key[1]} | " + " | ".join(ms([o.get(key, 0.0) for _, _, o in res[n]]) for n in pols) + " |")
L.append("\nThe dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):\n")
for n in pols:
    for seed, path in paths.get(n, [])[:3]:
        L.append(f"- {n} seed {seed}: " + "; ".join(f"{a} | {m} | {pi} | {pool} | {adj} | {conf}" for a, m, pi, pool, adj, conf in path))
open(out, "w").write("\n".join(L) + "\n"); print("\n".join(L))
