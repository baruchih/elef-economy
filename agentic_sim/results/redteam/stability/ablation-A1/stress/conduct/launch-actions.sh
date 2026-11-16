#!/bin/zsh
# Addendum 14's N3.1 (November 16, 2026; notes §113): M4's four cells at 1 in 4 run again at 7bd5dd5fc — the same rollouts (the finals of record frozen with no
# exploration, the environment's draws the seed's), with run_q's new tallies of the mixed world's verdicts by action, the planted cases failed and the bonds lost
# by action kind (`half_<group>_act<a>_<seat>`, `_pfail<a>_`, `_bondlost<a>_`); every figure of record reproduced to the digit (checked by conduct_actions_read.py).
# Run from agentic_sim/ in the elef-redteam env: launch-actions.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
X=$R/learned/horizon
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
for k in pa10 arm4; do
  $PY -m redteam.run_q --direct-model $X/$k-t1-b1-mc/direct/models/direct-online-10.pt --out $R/conduct/$k-direct-actions --seeds 21-60 --policies mix:direct:0.25 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/conduct/$k-direct-actions.log 2>&1 &
  $PY -m redteam.run_q --model $X/$k-t1-b1-mc/wm-ret/models/wm-online-10.pt --out $R/conduct/$k-wm-actions --seeds 21-60 --policies mix:greedy:0.25 --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/conduct/$k-wm-actions.log 2>&1 &
done
wait
touch $R/conduct/actions.done
