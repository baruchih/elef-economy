"""The defaults read on run 42's population (the economy reviewer's third ruling, November 6, 2026): one table over the channel tables —
the record's defaults and the cells where one default moves — per policy the standing false approvals, the member-confirmed and never-audited
channels, the never-audited share, the odds at the verdict of the never-audited, and the audits bought a run by who sat.
Usage: summarize.py OUT.md (run from 2.9.0-s82/defaults-run42/)"""
import sys, os
cells = [("defaults (p_floor 0.2, halve every 5)", "fa-channels-defaults.md"), ("p_floor 0.35", "fa-channels-floor0.35.md"), ("p_floor 0.5", "fa-channels-floor0.5.md"),
         ("halve every 10", "fa-channels-halve10.md"), ("halve every 20", "fa-channels-halve20.md"), ("p_floor 0.5, halve every 20", "fa-channels-floor0.5-halve20.md")]
def table(lines, head):
    i = next(k for k, l in enumerate(lines) if l.startswith(head)); hdr = [h.strip() for h in lines[i].split("|")[1:-1]]; out = {}
    for l in lines[i + 2:]:
        if not l.startswith("| "): break
        c = [x.strip() for x in l.split("|")[1:-1]]
        if len(c) == len(hdr): out[c[0]] = dict(zip(hdr, c))
    return out
L = ["# The defaults read on run 42's population by channel (the third ruling's 3): run 42's trained policies (the direct's `direct-online-10.pt`, the head alone's `wm-online-10.pt`, trained at the defaults) and the hand on seeds 21–40, one default moved per cell, no retraining. Columns: the standing false approvals a run (mean ± SE over the seeds), the member-confirmed audit, the state-confirmed audit, the never-audited channel, its share, the mean odds at the verdict of the never-audited, and the audits bought a run on every real root by who sat. The full channel tables beside (fa-channels-<cell>.md).\n",
     "| cell | policy | standing false approvals | member confirmed | state confirmed | never audited | never-audited share | odds at verdict, never audited | audits a run, a member sat | audits a run, the state sat |", "|---|---|---|---|---|---|---|---|---|---|"]
for name, f in cells:
    if not os.path.exists(f): L.append(f"| {name} | — | (not run) | | | | | | | |"); continue
    lines = open(f).read().splitlines(); T = table(lines, "| policy | standing"); A = table(lines, "| policy | audits")
    for pol in ("direct", "head alone", "hand"):
        d = T[pol]; a = A.get(pol, {})
        L.append(f"| {name} | {pol} | {d['standing false approvals']} | {d['member confirmed']} | {d['state confirmed']} | {d['never audited']} | {d['never-audited share']} | {d['odds at verdict of the never-audited (mean)']} | {a.get('audits, a member sat', '—')} | {a.get('audits, the state sat', '—')} |")
L.append("\nPaired against the hand on the same seeds (policy − hand): the total, the member-confirmed audit, the never-audited channel.\n")
L.append("| cell | policy | total | member confirmed | never audited |"); L.append("|---|---|---|---|---|")
for name, f in cells:
    if not os.path.exists(f): continue
    lines = open(f).read().splitlines(); i = next(k for k, l in enumerate(lines) if l.startswith("Paired against the hand")); hdr = [h.strip() for h in lines[i + 2].split("|")[1:-1]]
    for l in lines[i + 4:i + 6]:
        c = [x.strip() for x in l.split("|")[1:-1]]; d = dict(zip(hdr, c))
        L.append(f"| {name} | {d['policy']} | {d['total']} | {d['member confirmed']} | {d['never audited']} |")
open(sys.argv[1], "w").write("\n".join(L) + "\n"); print("\n".join(L))
