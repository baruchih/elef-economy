"""The per-seat dial's path by period under a frozen policy of record (the economy reviewer's question after §88, November 10, 2026).

Usage, from agentic_sim/ with the conda env's python:
  $PY results/redteam/stability/2.9.0-s82/dial_path.py --out <dir> --label <name> --seeds 21-40 \
      [--direct-model <direct-online-10.pt>] [--model <wm-online-10.pt>] --policies direct,greedy,hand -- <cell args>

Each seed is one run of the frozen policy in the cell (run_q's episode, the population as in the finals of record); after the run the
period records are read from the public view (`dial()["periods"]`, the engine's own record) and the partial last period from
`dial()["period"]`. Written: <out>/dial-path-<label>.json (every seed's records, the dial's fields only) and <out>/dial-path-<label>.md —
per policy, by period: m^A before → after (mean over the seeds; the share of seeds whose multiplier stepped), π^A, the planted
approvals adjudicated at a member's audit seat in the period (pa_audit_adj) and confirmed there, the pool carried forward after the
close (seat_pool A: confirmed / adjudicated), F̂^A where a reading was taken (ten pooled adjudications, Appendix V), the members'
audits of real approvals (the planted approvals' base), the planted approvals posted; then every seed's own path. A run starts its
dial at the floor by construction (the engine's m^A 1, π^A = π^A_0 at genesis); nothing carries between runs.
"""
import sys, os, json, argparse, time
sys.path.insert(0, os.getcwd())
import numpy as np
from redteam.run_q import episode, load_model, load_direct, GreedyPolicy, DirectPolicy, policy_of, boundary_read_for, device, seeds_of
from redteam.env import ElefReviewerEnv

KEYS = ("t", "start", "m_A_before", "m_A", "pi_A", "F_hat_A", "pa_posted", "pa_verdicts", "pa_audit_adj", "pa_audit_confirmed", "pa_third",
        "pa_disputed_first", "pa_pass_would_audit", "pa_unseated", "real_member_audits", "real_approvals", "seat_pool", "m", "pi", "F_hat")


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", required=True); ap.add_argument("--label", required=True); ap.add_argument("--seeds", default="21-40")
    ap.add_argument("--model", default=None); ap.add_argument("--direct-model", default=None); ap.add_argument("--policies", default="direct")
    ap.add_argument("--ticks", type=int, default=1000); ap.add_argument("--attrib", default="own")
    ap.add_argument("--from-json", default=None, help="write the .md again from a saved .json (no runs)")
    ap.add_argument("cell", nargs=argparse.REMAINDER)
    a = ap.parse_args(argv)
    if a.from_json:
        out = json.load(open(a.from_json)); write_md(out, os.path.join(a.out, f"dial-path-{a.label}.md"), a.label); return
    cell = [x for x in a.cell if x != "--"]
    br = boundary_read_for(cell, "auto")
    m, ck = (load_model(a.model) if a.model else (None, {}))
    if m is not None:
        m.to(device())
    env = ElefReviewerEnv(cell, ticks=a.ticks, obs_dim=ck.get("config", {}).get("obs_dim"), role="reviewer", attrib=a.attrib)
    pols = {}
    for name in a.policies.split(","):
        if name == "greedy":
            pols[name] = GreedyPolicy(m, boundary_read=br)
        elif name == "direct":
            dm, _ = load_direct(a.direct_model); dm.to(device()); pols[name] = DirectPolicy(dm, boundary_read=br)
        else:
            pols[name] = policy_of(name, "reviewer")
    os.makedirs(a.out, exist_ok=True)
    out = {"cell": cell, "ticks": a.ticks, "seeds": a.seeds, "model": a.model, "direct_model": a.direct_model, "runs": {k: [] for k in pols}}
    t0 = time.time()
    for seed in sorted(seeds_of(a.seeds)):
        for name, pol in pols.items():
            r = episode(env, pol, seed, np.random.default_rng(seed))
            d = env.run.w.dial()
            periods = [{k: p.get(k) for k in KEYS} for p in d["periods"]]
            cur = d.get("period") or {}
            partial = {"t": env.run.w.t, "start": cur.get("start"), "pa_audit_adj": cur.get("pa_audit_adj"), "pa_audit_confirmed": cur.get("pa_audit_confirmed"),
                       "pa_posted": cur.get("pa_posted"), "real_member_audits": cur.get("real_member_audits"), "m_A": d.get("m_A"), "pi_A": d.get("pi_A"),
                       "seat_pool": (d["periods"][-1]["seat_pool"] if d["periods"] else {"A": [0, 0]})}   # the pool carried into the partial period (the live pool is not on the view)
            out["runs"][name].append({"seed": seed, "error": r.get("error"), "periods": periods, "partial": partial, "m_A_end": d.get("m_A"), "pi_A_end": d.get("pi_A"),
                                      "pa_posted": r.get("pa_posted"), "pa_audited": r.get("pa_audited"), "pa_confirmed": r.get("pa_confirmed"), "F_hat_A_row": r.get("F_hat_A"),
                                      "care_share": r.get("care_share"), "false_approvals_run": r.get("false_approvals_run")})
            path = " → ".join(f"{p['m_A']:.2f}" for p in periods) + f" → {d.get('m_A'):.2f} (partial)"
            adj = ", ".join(str(p["pa_audit_adj"]) for p in periods) + f", {cur.get('pa_audit_adj')} (partial)"
            print(f"seed {seed} {name}: m^A {path}; pa_audit_adj by period {adj}; F̂^A read at " + ", ".join(f"p{i}={p['F_hat_A']}" for i, p in enumerate(periods) if p["F_hat_A"] is not None) + f"  [{time.time() - t0:.0f}s]", flush=True)
    env.close()
    json.dump(out, open(os.path.join(a.out, f"dial-path-{a.label}.json"), "w"), indent=1)
    write_md(out, os.path.join(a.out, f"dial-path-{a.label}.md"), a.label)


def write_md(out, path, label):
    with open(path, "w") as f:
        f.write(f"# The per-seat dial's path by period — `{label}` (the economy reviewer's question after §88; `dial_path.py`)\n\n"
                f"Cell: `{' '.join(out['cell'])}`; seeds {out['seeds']}; {out['ticks']} ticks (a period 200 ticks: five closed periods and nothing closes the sixth). "
                "A run's dial starts at the floor (m^A 1, π^A = π^A_0 0.02 at genesis) and nothing carries between runs. m^A steps at a period's close on a reading of at least ten "
                "pooled adjudications of planted approvals at a member's audit seat (Appendix V, `seat_dial_min_adj` 10): `adj` is the period's own count, `pool` what the pool carries "
                "forward after the close (confirmed / adjudicated), `F̂^A` the reading where one was taken (mean over the seeds that read one; the count of seeds reading). The planted "
                "approvals posted in the period are at π^A per real approval audited by a member in the period (`base`); the partial sixth period's counts are shown for the record.\n\n")
        for name, runs in out["runs"].items():
            runs = [r for r in runs if not r.get("error")]
            if not runs:
                continue
            n_per = max(len(r["periods"]) for r in runs)
            f.write(f"## {name} ({len(runs)} seeds)\n\n| period | m^A before → after | seeds stepping (↑ / ↓) | π^A after | planted approvals posted | base (members' audits of real approvals) | adj at a member's audit seat | confirmed | pool carried | F̂^A read (n) |\n|---|---|---|---|---|---|---|---|---|---|\n")
            for i in range(n_per):
                ps = [r["periods"][i] for r in runs if len(r["periods"]) > i]
                mb = np.mean([p["m_A_before"] for p in ps]); ma = np.mean([p["m_A"] for p in ps])
                up = sum(1 for p in ps if p["m_A"] > p["m_A_before"] + 1e-9); dn = sum(1 for p in ps if p["m_A"] < p["m_A_before"] - 1e-9)
                fh = [p["F_hat_A"] for p in ps if p["F_hat_A"] is not None]
                pool = np.mean([p["seat_pool"]["A"][1] for p in ps]); poolc = np.mean([p["seat_pool"]["A"][0] for p in ps])
                f.write(f"| p{i} (t {ps[0]['start']}–{ps[0]['t']}) | {mb:.2f} → {ma:.2f} | {up} / {dn} of {len(ps)} | {np.mean([p['pi_A'] for p in ps]):.3f} | {np.mean([p['pa_posted'] for p in ps]):.1f} | {np.mean([p['real_member_audits'] for p in ps]):.0f} | {np.mean([p['pa_audit_adj'] for p in ps]):.1f} | {np.mean([p['pa_audit_confirmed'] for p in ps]):.1f} | {poolc:.1f} / {pool:.1f} | {(f'{np.mean(fh):.2f}' if fh else '—')} ({len(fh)}) |\n")
            parts = [r["partial"] for r in runs]
            f.write(f"| p{n_per} partial (t {parts[0]['start']}–{parts[0]['t']}) | {np.mean([r['periods'][-1]['m_A'] for r in runs]):.2f} (no close) | — | {np.mean([p['pi_A'] for p in parts]):.3f} | {np.mean([p['pa_posted'] or 0 for p in parts]):.1f} | {np.mean([p['real_member_audits'] or 0 for p in parts]):.0f} | {np.mean([p['pa_audit_adj'] or 0 for p in parts]):.1f} | {np.mean([p['pa_audit_confirmed'] or 0 for p in parts]):.1f} | {np.mean([(p['seat_pool'] or {'A': [0, 0]})['A'][0] for p in parts]):.1f} / {np.mean([(p['seat_pool'] or {'A': [0, 0]})['A'][1] for p in parts]):.1f} | — |\n\n")
            ends = [r["m_A_end"] for r in runs]
            first = [next((i for i, p in enumerate(r["periods"]) if p["m_A"] > 1 + 1e-9), None) for r in runs]
            stepped = [x for x in first if x is not None]
            f.write(f"m^A at the run's end: mean {np.mean(ends):.2f}, min {min(ends):.2f}, max {max(ends):.2f}; seeds whose m^A left 1 within the run: {len(stepped)} of {len(runs)}"
                    + (f" (first at period p{min(stepped)}–p{max(stepped)}, median p{int(np.median(stepped))})" if stepped else "") + "; adjudications a closed period, mean over the seeds and periods "
                    f"{np.mean([p['pa_audit_adj'] for r in runs for p in r['periods']]):.1f} against the ten a step needs; readings taken a run {np.mean([sum(1 for p in r['periods'] if p['F_hat_A'] is not None) for r in runs]):.1f} of {n_per} closes.\n\n"
                    "Every seed's path (m^A after each close; the adjudications at a member's audit seat by period in brackets; F̂^A where read):\n\n")
            for r in runs:
                f.write(f"- seed {r['seed']}: " + " → ".join(f"{p['m_A']:.2f}" for p in r["periods"]) + f" [{', '.join(str(p['pa_audit_adj']) for p in r['periods'])}] "
                        + ", ".join(f"p{i} F̂^A {p['F_hat_A']:.2f}" for i, p in enumerate(r["periods"]) if p["F_hat_A"] is not None) + f"; planted approvals a run {r['pa_posted']}, audited {r['pa_audited']}, confirmed {r['pa_confirmed']}\n")
            f.write("\n")


if __name__ == "__main__":
    main()
