#!/bin/zsh
# Addendum 5's reads in the reviewer's order (November 11, 2026): the 0.20 pin's chain, arm 2's stamper start and arm 2's frozen detection reads
# in parallel; the retrained dispute cells of C5 at 0.25 then 0.1 behind them in sequence.
Q=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1
$Q/learned/pa20/launch.sh all > $Q/learned/pa20/chain.log 2>&1 &
$Q/learned/arm2-stamper/launch.sh all > $Q/learned/arm2-stamper/chain.log 2>&1 &
$Q/detection/arm2/launch.sh > $Q/detection/arm2/launch.log 2>&1 &
( $Q/detection/retrain-d0.25/launch.sh all > $Q/detection/retrain-d0.25/chain.log 2>&1; $Q/detection/retrain-d0.1/launch.sh all > $Q/detection/retrain-d0.1/chain.log 2>&1 ) &
wait
touch $Q/.queue5.done
