"""2.9.0 §8.4 on own-name credit at the corrected engine (the owed cells, November 10, 2026; run 42's careful basin and the liar chain) — adapted from 2.8.0-s84:  — the probe at every seat: Q2's probe (redteam.probe --seat) on the careful basin's and the disputes-on population's collections under the
direct's final policy (online11) and on the ε set (the floor), per seat kind. Reads <chain>/probe-seats/probe-<set>-<seat>.json and writes seats.md.
Usage: python3 readout.py [out md]"""
import json, os, sys
root = "results/redteam/stability"
out = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(os.path.abspath(__file__)), "seats.md")
def f3(v): return f"{v[0]:.3f} ± {v[2]:.3f}" if isinstance(v, list) else (f"{v:.3f}" if isinstance(v, float) else str(v))
L = ["# §8.4 — the probe at every seat (AUC, chance 0.5; ± the bootstrap SE over seeds)\n"]
for chain in ("careful", "liars"):
    L.append(f"\n## `learned-rev-{chain}-290-own` (the population under the direct's final policy, `online11`; the ε set the floor)\n")
    L.append("| set | seat | test decisions | plant share | raw obs | context only | case fields only | latent | **gap raw − context** | top case fields (added to context) |\n|---|---|---|---|---|---|---|---|---|---|")
    for s in ("online11", "eps"):
        for seat in ("all", "initial", "audit", "panel", "appeal", "dispute", "resumed"):   # appeal / dispute: the panel by its question (the disputes-on chain)
            f = os.path.join(root, f"learned-rev-{chain}-290-own", "probe-seats", f"probe-{s}-{seat}.json")
            if not os.path.exists(f):
                continue                      # the careful basin has no dispute seat (disputes off) and its appeal question is its panel
            e = json.load(open(f))
            abl = e.get("case_field_ablation") or {}
            top = sorted(((v["added_to_context"][0], k) for k, v in abl.items()), reverse=True)[:3]
            L.append(f"| {s} | {seat} | {e['test_decisions']:,} | {e['plant_share_test']:.3f} | {f3(e['auc_raw_obs'])} | {f3(e['auc_context_only'])} | {f3(e['auc_case_fields_only'])} | {f3(e['auc_latent'])} | **{e['auc_gap_raw_minus_context'][0]:+.4f} ± {e['auc_gap_raw_minus_context'][2]:.4f}** | " + ", ".join(f"{k} {v:+.4f}" for v, k in top) + " |")
open(out, "w").write("\n".join(L) + "\n"); print("wrote", out)
