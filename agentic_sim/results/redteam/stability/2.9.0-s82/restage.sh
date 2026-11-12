#!/bin/zsh
# The provenance re-read of the plant kind's state-seat stage (November 13, 2026; restage.py emits the commands, one evaluation of record each, into
# <eval>-at-30f280474/), six at a time through a small pool (macOS's xargs cannot carry a command this long). Run from agentic_sim/ in the elef-redteam env: restage.sh [parallel]
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=$PWD/results/redteam/stability
python3 $S/2.9.0-s82/restage.py emit > $S/2.9.0-s82/restage-cmds.txt
python3 - "$S/2.9.0-s82/restage-cmds.txt" "${1:-6}" <<'PY'
import subprocess, sys, time
cmds = [l.strip() for l in open(sys.argv[1]) if l.strip()]; par = int(sys.argv[2]); live = []
for c in cmds:
    while len(live) >= par:
        live = [p for p in live if p.poll() is None]; time.sleep(5)
    live.append(subprocess.Popen(["zsh", "-c", c]))
for p in live: p.wait()
PY
touch $S/2.9.0-s82/.restage.done
