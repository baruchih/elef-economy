#!/bin/zsh
# waits for the 0.20 pin's chain, then runs its quarter read
A=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/learned
until [ -f $A/pa20/chain.done ]; do sleep 300; done
zsh $A/quarters-pa20.sh
