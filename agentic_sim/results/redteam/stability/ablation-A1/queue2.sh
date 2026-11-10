#!/bin/zsh
# The second queue (November 10, 2026): arm 2's chain after the three ablation chains (the reviewer's order: the owed chains; arm 0 pinned at 0.10;
# arm 4; 1c; arm 2). Run from agentic_sim/: queue2.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
A=$PWD/results/redteam/stability/ablation-A1
until [ -f $A/learned/pa10/chain.done ] && [ -f $A/learned/arm1c/chain.done ] && [ -f $A/learned/arm4/chain.done ]; do sleep 600; done
zsh $A/learned/arm2/launch.sh all > $A/learned/arm2/chain.log 2>&1
