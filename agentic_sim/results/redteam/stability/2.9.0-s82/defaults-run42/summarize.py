"""The defaults read on run 42's population (the economy reviewer's third ruling, November 6, 2026): one table over the channel tables —
the record's cell (fa-channels-careful-290-own.md, the defaults) and the cells where one default moves — per policy the standing false
approvals, the member-confirmed and never-audited channels, the never-audited share and the odds at the verdict of the never-audited.
Usage: summarize.py OUT.md (run from 2.9.0-s82/defaults-run42/)"""
import re, sys, os
cells = [("defaults (p_floor 0.2, halve every 5)", "../fa-channels-careful-290-own.md"), ("p_floor 0.35", "fa-channels-floor0.35.md"), ("p_floor 0.5", "fa-channels-floor0.5.md"),
         ("halve every 10", "fa-channels-halve10.md"), ("halve every 20", "fa-channels-halve20.md"), ("p_floor 0.5, halve every 20", "fa-channels-floor0.5-halve20.md")]
L = ["# The defaults read on run 42's population by channel (the third ruling's 3): run 42's trained policies and the hand on seeds 21–40, one default moved per cell, no retraining. Columns: the standing false approvals a run (mean ± SE over the seeds), the member-confirmed audit, the never-audited channel, its share, the mean odds at the verdict of the never-audited. The full channel tables beside (fa-channels-<cell>.md).\n",
     "| cell | policy | standing false approvals | member confirmed | state confirmed | never audited | never-audited share | odds at verdict, never audited |", "|---|---|---|---|---|---|---|---|"]
for name, f in cells:
    if not os.path.exists(f): L.append(f"| {name} | — | (not run) | | | | | |"); continue
    rows = [l for l in open(f) if l.startswith("| ") and not l.startswith("| policy") and "−" not in l.split("|")[1]]
    hdr = [l for l in open(f) if l.startswith("| policy | standing")][0].split("|")[1:-1]; hdr = [h.strip() for h in hdr]
    for l in rows[:3]:
        c = [x.strip() for x in l.split("|")[1:-1]]
        if len(c) != len(hdr): continue
        d = dict(zip(hdr, c))
        L.append(f"| {name} | {d['policy']} | {d['standing false approvals']} | {d['member confirmed']} | {d['state confirmed']} | {d['never audited']} | {d['never-audited share']} | {d['odds at verdict of the never-audited (mean)']} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
