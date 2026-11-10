#!/bin/zsh
# The basin test owed (the brief's §7.3; the reviewer's note of November 10, night): the stamper start for the π^A-at-0.10 pin and for arm 4, after arm 2's chain.
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
A=$PWD/results/redteam/stability/ablation-A1/learned
until [ -f $A/arm2/chain.done ]; do sleep 600; done
zsh $A/pa10-stamper/launch.sh all > $A/pa10-stamper/chain.log 2>&1 &
zsh $A/arm4-stamper/launch.sh all > $A/arm4-stamper/chain.log 2>&1 &
wait
