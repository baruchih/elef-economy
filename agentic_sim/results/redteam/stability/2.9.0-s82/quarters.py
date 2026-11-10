"""D2 (the economy reviewer's addendum 4 to ablation brief A1, November 10, 2026): the frozen policy of record in a long run, read by quarter.

Usage, from agentic_sim/ with the conda env's python:
  $PY results/redteam/stability/2.9.0-s82/quarters.py --out <dir> --label <name> --ticks 2000 --seeds 21-40 \
      [--direct-model …] [--model …] --policies direct,greedy,hand -- <cell args>

Each seed is one run of the frozen policy in the cell (run_q's episode; the population as in the finals of record), read from the world
after the run and at the quarter boundaries (a snapshot at the first decision at or after each boundary, within a tick or two of it):
  - each dial's path — the period records' m_t, m^A, m^La, m^Ld and π^A with the planted approvals adjudicated and F̂^A at each close;
  - the audit seats by holder — the audit reviews on members' real deliveries by the quarter of the seat's assignment, a member's or the
    state's (a troop), the member's inspected or blind (care spent or none; a blind verdict of either sign), the audit seats on plants beside;
  - the panel seats the same way;
  - the member-periods by tier — at each boundary the members alive (is_member), of them duty-ineligible and panel-ineligible (the record's
    tests), the probationers and the suspended beside;
  - the channel split — fa_channels' classification of every standing false approval (a real root vested unfulfilled, the state's own
    deliveries excluded) by the quarter of its vesting;
  - the cost of truth — the bank's mint_plant − retire_plant at each boundary (cumulative; the quarter's share by difference);
  - the members' review-fee income — every `feepot_out` "… review fee" event to a member by the quarter of its tick, the state's beside;
  - the members alive at each boundary.
Written: <out>/quarters-<label>.json (every seed) and <out>/quarters-<label>.md (means over the seeds, per policy, by quarter)."""
import sys, os, json, argparse, time
sys.path.insert(0, os.getcwd())
import numpy as np
from redteam.run_q import episode, load_model, load_direct, GreedyPolicy, DirectPolicy, policy_of, boundary_read_for, device, seeds_of
from redteam.env import ElefReviewerEnv
from sim.invariants import public_id

CH = ["member confirmed", "state confirmed", "audited, rejected, vested", "disputed, panel confirmed (a member sat)", "disputed, panel confirmed (the state's alone)",
      "appealed, panel sided with the appellant (a member sat)", "appealed, panel sided with the appellant (the state's alone)", "never audited"]


class Snapshotting:
    """Wraps a policy: at the first decision at or after each quarter boundary, reads the world's state (the driver's thread is blocked at the decision)."""
    def __init__(self, pol, env, ticks, nq=4):
        self.pol, self.env, self.bounds, self.snaps = pol, env, [int(round(ticks * k / nq)) for k in range(1, nq + 1)], []
        self.boundary_reads = getattr(pol, "boundary_reads", [])
    def __call__(self, obs, rng):
        run = getattr(self.env, "run", None)
        if run is not None and self.snaps.__len__() < len(self.bounds) and run.w.t >= self.bounds[len(self.snaps)]:
            self.snaps.append(snapshot(run, self.bounds[len(self.snaps)]))
        return self.pol(obs, rng)
    def diag_now(self, obs):
        return self.pol.diag_now(obs) if hasattr(self.pol, "diag_now") else None


def snapshot(run, bound):
    W = run.w._w
    A = [a for a in W.actors.values() if not W.is_troop(a.id)] if hasattr(W, "actors") else []
    members = [a for a in A if a.is_member]
    return {"bound": bound, "t": W.t, "members_alive": len(members), "duty_ineligible": sum(1 for a in members if not a.duty_eligible),
            "panel_ineligible": sum(1 for a in members if not a.panel_eligible), "probationers": sum(1 for a in A if a.probation),
            "suspended": sum(1 for a in A if a.suspended_until is not None), "actors": len(A),
            "cost_of_truth": float(W.bank_minted.get("mint_plant", 0.0) - W.bank_destroyed.get("retire_plant", 0.0)),
            "m_t": W.m_t, "m_A": W.m_A, "m_La": W.m_La, "m_Ld": W.m_Ld, "pi_A": W.pi_A, "pi_t": W.pi_t}


def read_world(run, ticks, nq=4):
    W = run.w._w
    q_of = lambda t: min(nq - 1, int(t * nq // ticks)) if t is not None else None
    seats = {q: {"audit member inspected": 0, "audit member blind": 0, "audit state": 0, "audit plant member": 0, "audit plant member blind": 0, "audit plant state": 0,
                 "panel member inspected": 0, "panel member blind": 0, "panel state": 0, "panel plant member": 0, "panel plant state": 0} for q in range(nq)}
    chan = {q: dict.fromkeys(CH, 0) for q in range(nq)}
    fees = {q: {"member": 0.0, "state": 0.0, "member_n": 0, "state_n": 0} for q in range(nq)}
    roots = {q: 0 for q in range(nq)}
    # the quarter's price (the reviewer's read after §92): the care spent by case kind and the state's seats' cost by the quarter of the review's
    # completion, a plant's awarded price by the quarter of its closure, the bad deliveries vested — the system's overhead a vested task by quarter
    price = {q: {"care_real": 0.0, "care_plant": 0.0, "troop_cost": 0.0, "plant_price": 0.0, "bad_vested": 0, "fa_vested": 0, "bad_settled": 0, "fa_settled": 0} for q in range(nq)}
    for rv in W.reviews.values():
        tq = rv.t_done if rv.t_done is not None else rv.t_assign
        if tq is None or rv.cost is None or rv.cost <= 0: continue
        q = q_of(tq); cc = W.cases.get(rv.case) if hasattr(rv, "case") else None
        tk = run.tasks.get(public_id(rv.case)) if hasattr(rv, "case") else None
        if W.is_troop(rv.reviewer): price[q]["troop_cost"] += rv.cost
        elif str(rv.reviewer).startswith("plant_rev:") or rv.reviewer == "PLANT_REV": pass
        else: price[q]["care_plant" if (tk is not None and tk.plant) else "care_real"] += rv.cost
    for cid, c in W.cases.items():
        t = run.tasks.get(public_id(cid))
        if t is None or not c.is_root or W.is_troop(c.actor):
            continue
        plant = bool(t.plant)
        if plant and c.tree_closed and c.t_closed is not None:
            price[q_of(c.t_closed)]["plant_price"] += float(c.B or 0.0)
        if not plant and c.tree_closed and not t.fulfilled:      # the driver's `bad_deliveries` by the quarter of the settlement (every outcome), the false approvals among them
            qs = q_of(c.t_closed if c.t_closed is not None else W.t); price[qs]["bad_settled"] += 1
            if c.state == "VESTED": price[qs]["fa_settled"] += 1
        for x in c.reviews:
            rv = W.reviews[x]
            if rv.role not in ("audit", "appeal") or rv.t_assign is None:
                continue
            q = q_of(rv.t_assign); k = "audit" if rv.role == "audit" else "panel"
            if W.is_troop(rv.reviewer):
                seats[q][f"{k} plant state" if plant else f"{k} state"] += 1
            elif plant:
                seats[q][f"{k} plant member"] += 1
                if k == "audit" and rv.cost <= 0: seats[q]["audit plant member blind"] += 1
            else:
                seats[q][f"{k} member inspected" if rv.cost > 0 else f"{k} member blind"] += 1
        if plant or c.state != "VESTED":
            continue
        q = q_of(c.t_vest if c.t_vest is not None else W.t); roots[q] += 1
        if t.fulfilled:
            continue
        price[q]["bad_vested"] += 1; price[q]["fa_vested"] += 1
        audits = [W.reviews[x] for x in c.reviews if W.reviews[x].role == "audit"]
        if not audits:
            ch = c.challenge
            if ch is not None:
                panel = [W.reviews[x] for x in ch["reviews"]]
                who = "a member sat" if any(not W.is_troop(p_.reviewer) for p_ in panel) else "the state's alone"
                if ch["kind"] == "dispute": chan[q][f"disputed, panel confirmed ({who})"] += 1
                elif ch["kind"] == "appeal": chan[q][f"appealed, panel sided with the appellant ({who})"] += 1
                continue
            chan[q]["never audited"] += 1
            continue
        conf = [a for a in audits if a.verdict == "F" and a.status in ("done", "vested")]
        if conf: chan[q]["state confirmed" if W.is_troop(conf[-1].reviewer) else "member confirmed"] += 1
        else: chan[q]["audited, rejected, vested"] += 1
    for e in W.ledger.events:
        if e.kind == "feepot_out" and (e.note or "").endswith("review fee") and e.t is not None:
            q = q_of(e.t)
            if W.is_troop(e.dst): fees[q]["state"] += e.amount; fees[q]["state_n"] += 1
            elif not (str(e.dst).startswith("plant_rev:") or e.dst == "PLANT_REV"): fees[q]["member"] += e.amount; fees[q]["member_n"] += 1
    periods = [{k: p.get(k) for k in ("t", "start", "m", "pi", "m_A", "pi_A", "m_La", "m_Ld", "pa_audit_adj", "pa_audit_confirmed", "F_hat_A", "real_member_audits", "pa_posted", "F_hat")} for p in run.w.dial()["periods"]]
    # the whole run: every review seat by who sat and its role (plants included), and the review fees by who sat and the seat's role
    seats_all = {}; fees_role = {}
    for rv in W.reviews.values():
        who = "state" if W.is_troop(rv.reviewer) else ("plant alias" if (str(rv.reviewer).startswith("plant_rev:") or rv.reviewer == "PLANT_REV") else "member")
        role = {"initial": "resumed" if getattr(rv, "resumed", False) else "initial", "audit": "audit", "appeal": "panel"}.get(rv.role, rv.role)
        seats_all[f"{who} {role}"] = seats_all.get(f"{who} {role}", 0) + 1
    for e in W.ledger.events:
        if e.kind == "feepot_out" and (e.note or "").endswith("review fee"):
            who = "state" if W.is_troop(e.dst) else ("plant alias" if (str(e.dst).startswith("plant_rev:") or e.dst == "PLANT_REV") else "member")
            c = W.cases.get(e.case) if e.case is not None else None; role = "?"
            if c is not None:
                for rid in c.reviews:
                    rv = W.reviews[rid]
                    if rv.reviewer == e.dst: role = {"initial": "initial", "audit": "audit", "appeal": "panel"}.get(rv.role, rv.role)
            fees_role[f"{who} {role}"] = fees_role.get(f"{who} {role}", 0.0) + e.amount
    return {"seats": seats, "channels": chan, "fees": fees, "roots_vested": roots, "periods": periods, "seats_all": seats_all, "fees_role": fees_role, "price": price}


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--label", required=True); ap.add_argument("--seeds", default="21-40")
    ap.add_argument("--model", default=None); ap.add_argument("--direct-model", default=None); ap.add_argument("--policies", default="direct")
    ap.add_argument("--ticks", type=int, default=2000); ap.add_argument("--attrib", default="own")
    ap.add_argument("--from-json", default=None, help="write the .md again from a saved .json (no runs)")
    ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    if a.from_json:
        write_md(json.load(open(a.from_json)), os.path.join(a.out, f"quarters-{a.label}.md"), a.label); return
    cell = [x for x in a.cell if x != "--"]
    br = boundary_read_for(cell, "auto")
    m, ck = (load_model(a.model) if a.model else (None, {}))
    if m is not None: m.to(device())
    env = ElefReviewerEnv(cell, ticks=a.ticks, obs_dim=ck.get("config", {}).get("obs_dim"), role="reviewer", attrib=a.attrib)
    pols = {}
    for name in a.policies.split(","):
        if name == "greedy": pols[name] = GreedyPolicy(m, boundary_read=br)
        elif name == "direct":
            dm, _ = load_direct(a.direct_model); dm.to(device()); pols[name] = DirectPolicy(dm, boundary_read=br)
        else: pols[name] = policy_of(name, "reviewer")
    os.makedirs(a.out, exist_ok=True)
    out = {"cell": cell, "ticks": a.ticks, "seeds": a.seeds, "model": a.model, "direct_model": a.direct_model, "runs": {k: [] for k in pols}}
    t0 = time.time()
    for seed in sorted(seeds_of(a.seeds)):
        for name, pol in pols.items():
            sp = Snapshotting(pol, env, a.ticks)
            r = episode(env, sp, seed, np.random.default_rng(seed))
            if r.get("error"):
                print(f"seed {seed} {name}: ERROR {r['error']}", flush=True); out["runs"][name].append({"seed": seed, "error": r["error"]}); continue
            while len(sp.snaps) < len(sp.bounds):                   # the run ended before a boundary's first decision: the end state stands for it
                sp.snaps.append(snapshot(env.run, sp.bounds[len(sp.snaps)]))
            rec = read_world(env.run, a.ticks)
            row = env.run.row(a.ticks)                                 # the driver's full row at the end (the leak, the overhead, Ω's net, the tasks vested)
            rec.update({"seed": seed, "snaps": sp.snaps, "false_approvals_run": r.get("false_approvals_run"), "care_share": r.get("care_share"),
                        "lifetime_real_wealth": r.get("lifetime_real_wealth"), "suspensions_run": r.get("suspensions_run"), "m_A_end": env.run.w._w.m_A,
                        "row": {k: row.get(k) for k in ("vested", "false_approvals", "bad_deliveries", "leak_paid", "leak_bad", "sys_overhead_per_vested", "cust_overhead_per_vested",
                                                         "omega_net", "omega_unlocked", "cost_of_truth", "state_share", "troop_review_cost", "state_cost_unreimbursed", "awarded", "final_n")}})
            out["runs"][name].append(rec)
            print(f"seed {seed} {name}: m^A by close " + " → ".join(f"{p['m_A']:.2f}" for p in rec["periods"]) + f"; members alive at the quarters {[s['members_alive'] for s in sp.snaps]}; "
                  f"audit seats member/state by quarter {[(v['audit member inspected'] + v['audit member blind'], v['audit state']) for v in rec['seats'].values()]}; FA {r.get('false_approvals_run')} [{time.time() - t0:.0f}s]", flush=True)
    env.close()
    json.dump(out, open(os.path.join(a.out, f"quarters-{a.label}.json"), "w"), indent=1, default=float)
    write_md(out, os.path.join(a.out, f"quarters-{a.label}.md"), a.label)


def ms(v):
    v = np.asarray(v, float); return f"{v.mean():.1f} ± {v.std(ddof=1) / np.sqrt(len(v)):.1f}" if len(v) > 1 else f"{v.mean():.1f}"


def write_md(out, path, label):
    nq = 4; T = out["ticks"]
    with open(path, "w") as f:
        f.write(f"# The frozen policy in a {T:,}-tick run, read by quarter — `{label}` (D2, the economy reviewer's addendum 4; `quarters.py`)\n\n"
                f"Cell: `{' '.join(out['cell'])}`; seeds {out['seeds']}. Means over the seeds (± SE where shown). A quarter is {T // nq} ticks; the seats by the quarter of the seat's "
                "assignment, the standing false approvals by the quarter of their vesting, the fees by the quarter of their payment, the snapshots at the first decision at or after the "
                "boundary (the members alive and the tiers at that moment; the cost of truth cumulative there). The audit and panel seats are on members' real deliveries (the plants' beside); "
                "a member's seat inspected (care spent) or blind (none spent, a verdict of either sign).\n\n")
        for name, runs in out["runs"].items():
            runs = [r for r in runs if not r.get("error")]
            if not runs: continue
            f.write(f"## {name} ({len(runs)} seeds; the standing false approvals a run {ms([r['false_approvals_run'] for r in runs])}, care {np.mean([r['care_share'] or 0 for r in runs]):.3f}, m^A at the end {np.mean([r['m_A_end'] for r in runs]):.2f})\n\n")
            # the dials by close
            n_per = max(len(r["periods"]) for r in runs)
            f.write("**The dials by close** (mean over the seeds that reached the close): \n\n| close | t | m_t | π_t | m^A | π^A | m^La | m^Ld | planted approvals adjudicated at a member's audit seat | F̂^A read (n) |\n|---|---|---|---|---|---|---|---|---|---|\n")
            for i in range(n_per):
                ps = [r["periods"][i] for r in runs if len(r["periods"]) > i]
                fh = [p["F_hat_A"] for p in ps if p["F_hat_A"] is not None]
                f.write(f"| {i} | {np.mean([p['t'] for p in ps]):.0f} | {np.mean([p['m'] for p in ps]):.2f} | {np.mean([p['pi'] for p in ps]):.3f} | {np.mean([p['m_A'] for p in ps]):.2f} | {np.mean([p['pi_A'] for p in ps]):.3f} | {np.mean([p['m_La'] for p in ps]):.2f} | {np.mean([p['m_Ld'] for p in ps]):.2f} | {np.mean([p['pa_audit_adj'] for p in ps]):.1f} | {(f'{np.mean(fh):.2f}' if fh else '—')} ({len(fh)}) |\n")
            f.write("\n**By quarter**:\n\n| quarter | members alive | duty-ineligible / panel-ineligible of them | probationers / suspended | audit seats on members' work: member inspected / member blind / state | the member's share of them | member blind rate | audit seats on plants: member (blind) / state | panel seats: member inspected / blind / state | standing false approvals vested: member-confirmed / state-confirmed / never audited / other | roots vested | review fees: members / the state | cost of truth (cumulative at the boundary; the quarter's) | m^A / π^A at the boundary |\n|---|---|---|---|---|---|---|---|---|---|---|---|---|---|\n")
            for q in range(nq):
                S = [r["seats"][str(q)] if str(q) in r["seats"] else r["seats"][q] for r in runs]
                C = [r["channels"][str(q)] if str(q) in r["channels"] else r["channels"][q] for r in runs]
                F = [r["fees"][str(q)] if str(q) in r["fees"] else r["fees"][q] for r in runs]
                R = [r["roots_vested"][str(q)] if str(q) in r["roots_vested"] else r["roots_vested"][q] for r in runs]
                sn = [r["snaps"][q] for r in runs]
                mi, mb, st_ = (np.mean([s["audit member inspected"] for s in S]), np.mean([s["audit member blind"] for s in S]), np.mean([s["audit state"] for s in S]))
                share = (mi + mb) / max(1e-9, mi + mb + st_); blind = mb / max(1e-9, mi + mb)
                other = np.mean([sum(c[k] for k in CH if k not in ("member confirmed", "state confirmed", "never audited")) for c in C])
                cot_prev = np.mean([r["snaps"][q - 1]["cost_of_truth"] for r in runs]) if q > 0 else 0.0
                f.write(f"| Q{q + 1} (t {q * T // nq}–{(q + 1) * T // nq}) | {np.mean([s['members_alive'] for s in sn]):.1f} | {np.mean([s['duty_ineligible'] for s in sn]):.1f} / {np.mean([s['panel_ineligible'] for s in sn]):.1f} | {np.mean([s['probationers'] for s in sn]):.1f} / {np.mean([s['suspended'] for s in sn]):.1f} | {mi:.0f} / {mb:.0f} / {st_:.0f} | **{share:.2f}** | **{blind:.3f}** | {np.mean([s['audit plant member'] for s in S]):.0f} ({np.mean([s['audit plant member blind'] for s in S]):.0f}) / {np.mean([s['audit plant state'] for s in S]):.0f} | {np.mean([s['panel member inspected'] for s in S]):.0f} / {np.mean([s['panel member blind'] for s in S]):.0f} / {np.mean([s['panel state'] for s in S]):.0f} | **{ms([c['member confirmed'] for c in C])}** / {ms([c['state confirmed'] for c in C])} / {ms([c['never audited'] for c in C])} / {other:.1f} | {np.mean(R):.0f} | {np.mean([x['member'] for x in F]):.0f} / {np.mean([x['state'] for x in F]):.0f} | {np.mean([s['cost_of_truth'] for s in sn]):.0f} ({np.mean([s['cost_of_truth'] for s in sn]) - cot_prev:.0f}) | {np.mean([s['m_A'] for s in sn]):.2f} / {np.mean([s['pi_A'] for s in sn]):.3f} |\n")
            if all("price" in r for r in runs):
                f.write("\n**The quarter's price** (the system's overhead per task vested in the quarter: the care spent on real and planted cases, the state's seats' cost, the cost of truth and the plants' awarded price, by the quarter of each; the standing false approvals vested in the quarter over the bad deliveries vested in it, per thousand; the bad deliveries here are a member's real roots vested unfulfilled, the false approvals among them those vested approved — every unfulfilled root that vests is a false approval, so the two counts coincide; the leak per thousand bad deliveries is read on the bad deliveries settled in the quarter at every outcome — the driver's `bad_deliveries` by the quarter of the settlement — and the false approvals among them):\n\n| quarter | roots vested | care on real / on plants | the state's seats' cost | the cost of truth (the quarter's) | the plants' price | system overhead a vested task | standing false approvals vested | per thousand tasks vested | bad deliveries settled / false approvals among them | leak per thousand bad deliveries |\n|---|---|---|---|---|---|---|---|---|---|---|\n")
                tot = {"care_real": 0.0, "care_plant": 0.0, "troop_cost": 0.0, "cot": 0.0, "plant_price": 0.0, "roots": 0.0, "fa": 0.0, "bad_s": 0.0, "fa_s": 0.0}
                for q in range(nq):
                    P = [r["price"][str(q)] if str(q) in r["price"] else r["price"][q] for r in runs]
                    R = [r["roots_vested"][str(q)] if str(q) in r["roots_vested"] else r["roots_vested"][q] for r in runs]
                    cot_q = np.mean([r["snaps"][q]["cost_of_truth"] - (r["snaps"][q - 1]["cost_of_truth"] if q > 0 else 0.0) for r in runs])
                    cr, cp, tc, pp = (np.mean([x["care_real"] for x in P]), np.mean([x["care_plant"] for x in P]), np.mean([x["troop_cost"] for x in P]), np.mean([x["plant_price"] for x in P]))
                    nv = max(1e-9, np.mean(R)); fa = np.mean([x["fa_vested"] for x in P])
                    bs = np.mean([x.get("bad_settled", 0) for x in P]); fs = np.mean([x.get("fa_settled", 0) for x in P])
                    for k, v in (("care_real", cr), ("care_plant", cp), ("troop_cost", tc), ("cot", cot_q), ("plant_price", pp), ("roots", nv), ("fa", fa), ("bad_s", bs), ("fa_s", fs)): tot[k] += v
                    f.write(f"| Q{q + 1} | {nv:.0f} | {cr:.0f} / {cp:.0f} | {tc:.0f} | {cot_q:.0f} | {pp:.0f} | **{(cr + cp + tc + cot_q + pp) / nv:.2f}** | {ms([x['fa_vested'] for x in P])} | {fa / nv * 1000:.1f} | {bs:.0f} / {fs:.1f} | **{fs / max(1e-9, bs) * 1000:.1f}** |\n")
                f.write(f"| the run (the quarters summed) | {tot['roots']:.0f} | {tot['care_real']:.0f} / {tot['care_plant']:.0f} | {tot['troop_cost']:.0f} | {tot['cot']:.0f} | {tot['plant_price']:.0f} | **{(tot['care_real'] + tot['care_plant'] + tot['troop_cost'] + tot['cot'] + tot['plant_price']) / max(1e-9, tot['roots']):.2f}** | {tot['fa']:.1f} | {tot['fa'] / max(1e-9, tot['roots']) * 1000:.1f} | {tot['bad_s']:.0f} / {tot['fa_s']:.1f} | **{tot['fa_s'] / max(1e-9, tot['bad_s']) * 1000:.1f}** |\n")
            # the whole run: the seats by holder and role, the fees by holder and seat kind, Ω's net, the leak
            SA = {}; FR = {}
            for r in runs:
                for k, v in r.get("seats_all", {}).items(): SA[k] = SA.get(k, 0) + v / len(runs)
                for k, v in r.get("fees_role", {}).items(): FR[k] = FR.get(k, 0.0) + v / len(runs)
            tot_seats = sum(v for k, v in SA.items() if not k.startswith("plant alias")); st_seats = sum(v for k, v in SA.items() if k.startswith("state"))
            rows = [r.get("row") or {} for r in runs]
            g = lambda k: [x.get(k) for x in rows if x.get(k) is not None]
            f.write(f"\n**The whole run.** Review seats a run by who sat and the seat (plants included): " + ", ".join(f"{k} {v:.0f}" for k, v in sorted(SA.items())) +
                    f" — the state's share of the review seats **{st_seats / max(1e-9, tot_seats):.3f}** ({st_seats:.0f} of {tot_seats:.0f}). The review fees a run by who sat and the seat kind: " + ", ".join(f"{k} {v:.0f}" for k, v in sorted(FR.items())) +
                    f" — the members' {sum(v for k, v in FR.items() if k.startswith('member')):.0f} in all, the state's {sum(v for k, v in FR.items() if k.startswith('state')):.0f}. "
                    + (f"Ω's net {ms(g('omega_net'))}; the tasks vested {ms(g('vested'))} a run, bad deliveries {ms(g('bad_deliveries'))}, the standing false approvals {ms(g('false_approvals'))} — the leak {np.mean(g('leak_paid')):.4f} per vested task (the row's), {np.mean(g('leak_bad')):.3f} per bad delivery; the system's overhead a vested task {np.mean(g('sys_overhead_per_vested')):.2f}, the customers' {np.mean(g('cust_overhead_per_vested')):.2f}; the state's review cost {np.mean(g('troop_review_cost')):.0f}, unreimbursed {np.mean(g('state_cost_unreimbursed') or [0]):.0f}; the cost of truth {np.mean(g('cost_of_truth')):.0f}." if g("vested") else "") + "\n\n")


if __name__ == "__main__":
    main()
