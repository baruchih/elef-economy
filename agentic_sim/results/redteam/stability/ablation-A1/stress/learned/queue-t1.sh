#!/bin/zsh
L=/Users/baruchi-admin/projects/elef-economy-stress/agentic_sim/results/redteam/stability/ablation-A1/stress/learned
$L/pa10-t1-b1/launch.sh all > $L/pa10-t1-b1/chain.log 2>&1 &
$L/arm2-t1-b1/launch.sh all > $L/arm2-t1-b1/chain.log 2>&1 &
$L/arm4-t1-b1/launch.sh all > $L/arm4-t1-b1/chain.log 2>&1 &
wait; touch $L/.queue-t1.done
