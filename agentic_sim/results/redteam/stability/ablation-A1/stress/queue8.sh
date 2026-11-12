#!/bin/zsh
# Addendum 8's two reads in sequence (November 13, 2026): the entry test, the stake table's eighteen cells, their honest side. Run from agentic_sim/: queue8.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=$PWD/results/redteam/stability/ablation-A1/stress
zsh $S/entry/launch.sh 6 > $S/entry/launch.log 2>&1
zsh $S/payoff3-launch.sh 6 > $S/payoff3-launch.log 2>&1
zsh $S/honest8-launch.sh 3 > $S/honest8-launch.log 2>&1
touch $S/.queue8.done
