#!/bin/zsh
# The provenance re-read of the plant kind's state-seat stage (November 13, 2026; restage.py emits the commands, one evaluation of record each, into
# <eval>-at-30f280474/). Waits for addendum 8's queue, then six at a time. Run from agentic_sim/ in the elef-redteam env: restage.sh [parallel]
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=$PWD/results/redteam/stability
until [ -f $S/ablation-A1/stress/.queue8.done ]; do sleep 60; done
python3 $S/2.9.0-s82/restage.py emit > $S/2.9.0-s82/restage-cmds.txt
xargs -P ${1:-6} -I CMD zsh -c CMD < $S/2.9.0-s82/restage-cmds.txt
touch $S/2.9.0-s82/.restage.done
