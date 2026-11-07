"""The 60/40 mix's seat rates on seeds 21–40, measured from the engine's reviews (November 7, 2026; notes §77): the `hand` arm of each
re-evaluated final on the corrected engine (eval/final-cr/eval.json; the direct's and the head alone's runs of the same cell give the identical
hand episode — the first found is read), per cell. Pooled over the seeds (the record's aggregate) and the per-seed rates' mean ± SE, with the
per-seed counts written beside as CSV so the record can carry them. Usage: mix-seats-20.py OUT.md OUT.csv"""
import json, sys, os, math
import numpy as np
R = "results/redteam/stability"
CELLS = [("2.9.0, run 24's world (run 42 / the basin test)", ["learned-rev-careful-290-own", "learned-rev-stamper-290-own"]),
         ("2.9.0, the liar cell (disputes on, lying real challengers at 0.1)", ["learned-rev-liars-290-own"]),
         ("2.7.0, run 24's world (the pairing; the provenance branch)", ["learned-rev-careful-2-own", "learned-rev-stamper-2-own"])]
SEATS = ("initial", "audit", "panel", "resumed"); KINDS = ("plant", "real")
out, csv = [], ["cell,chain,seed,seat,kind,seen,approve_blind,reject_blind,underfunded_careful_reviews"]
out.append("# The 60/40 mix's seat rates on seeds 21–40, measured from the engine's reviews (the corrected engine; the `hand` arm of the re-evaluated finals)\n")
out.append("A review that spent care inspected; one that spent none gave a blind verdict of the sign it gave (the exporter's reading, §76). `blind` is approve-blind + reject-blind over the seat's reviews by the learner slots (every member and arrival); the reject-blind part beside. Pooled: the counts summed over the 20 seeds. Per seed: the rate's mean ± SE over the seeds that have the seat. `underfunded` is the run's count of careful reviews that could not afford a cent of their care (an upper bound on blind readings that were a careful review paying nothing).\n")
for label, chains in CELLS:
    found = None
    for ch in chains:
        for L in ("direct", "wm"):
            p = f"{R}/{ch}/{L}/eval/final-cr/eval.json"
            if os.path.exists(p):
                d = json.load(open(p))
                if "hand" in d["episodes"]: found = (ch, L, d); break
        if found: break
    out.append(f"\n## {label}\n")
    if not found: out.append("missing"); continue
    ch, L, d = found; E = {e["seed"]: e for e in d["episodes"]["hand"]}; seeds = sorted(E)
    if not any(f"measured_initial_real_seen" in E[s] for s in seeds): out.append(f"no measured keys in {ch}/{L}"); continue
    out.append(f"From `{ch}/{L}/eval/final-cr/` (the hand episodes are the cell's, whichever chain's final ran them), seeds {seeds[0]}–{seeds[-1]}, {len(seeds)} seeds.\n")
    out.append("| seat | kind | reviews (pooled) | blind (pooled) | reject-blind (pooled) | blind rate, per seed mean ± SE | seeds with the seat |"); out.append("|---|---|---|---|---|---|---|")
    for seat in SEATS:
        for kind in KINDS:
            n = [E[s].get(f"measured_{seat}_{kind}_seen", 0) for s in seeds]; a = [E[s].get(f"measured_{seat}_{kind}_approve_blind", 0) for s in seeds]; r = [E[s].get(f"measured_{seat}_{kind}_reject_blind", 0) for s in seeds]
            for s, nn, aa, rr in zip(seeds, n, a, r): csv.append(f"{label.split(',')[0]},{ch},{s},{seat},{kind},{nn},{aa},{rr},{E[s].get('underfunded_careful_reviews', 0)}")
            N = sum(n); B = sum(a) + sum(r)
            rates = np.array([(aa + rr) / nn for nn, aa, rr in zip(n, a, r) if nn]); 
            ms = f"{rates.mean():.3f} ± {rates.std(ddof=1) / math.sqrt(len(rates)):.3f}" if len(rates) > 1 else "—"
            out.append(f"| {seat} | {kind} | {N} | {B} ({B / N:.3f}) | {sum(r)} ({sum(r) / N:.3f}) | {ms} | {len(rates)} |" if N else f"| {seat} | {kind} | 0 | — | — | — | 0 |")
    uf = np.array([E[s].get("underfunded_careful_reviews", 0) or 0 for s in seeds], float)
    fa = np.array([float(E[s].get("false_approvals_run") or 0) for s in seeds])
    out.append(f"\nUnderfunded careful reviews a run {uf.mean():.1f} ± {uf.std(ddof=1) / math.sqrt(len(uf)):.1f}; the run's standing false approvals {fa.mean():.1f} ± {fa.std(ddof=1) / math.sqrt(len(fa)):.1f}.")
open(sys.argv[1], "w").write("\n".join(out) + "\n"); open(sys.argv[2], "w").write("\n".join(csv) + "\n"); print("\n".join(out))
