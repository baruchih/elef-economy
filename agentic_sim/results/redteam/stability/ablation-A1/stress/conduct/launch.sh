#!/bin/zsh
# Addendum 13's M4 (November 16, 2026; notes §112): the horizon learners' conduct among careful members — the four finals of the horizon chains (stress/learned/horizon/
# {pa10,arm4}-t1-b1-mc/, the direct at ffd23d851 and the world model under the return head at 04f1c5565), frozen, no exploration, each in its own cell (the pin at
# π^A 0.10 and arm 4; a temptation of 1, the bond ×1, the fee of record), (a) the policy on 1 in 4 of the learner slots and the careful on the rest (`mix:<policy>:0.25`,
# the wrapper of record), (b) the reverse (`mix:<policy>:0.75`), the all-careful population beside on the same seeds; seeds 21–60; run_q at 25aab307e (the mix wrapper's
# seats and claims by standing added as a reading). Read by conduct_read.py. Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
H=$R/learned/horizon
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
for k in pa10 arm4; do
  X=$H/$k-t1-b1-mc
  $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $R/conduct/$k-direct --seeds 21-60 --policies mix:direct:0.25,mix:direct:0.75,careful --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/conduct/$k-direct.log 2>&1 &
  $PY -m redteam.run_q --model $X/wm-ret/models/wm-online-10.pt --out $R/conduct/$k-wm --seeds 21-60 --policies mix:greedy:0.25,mix:greedy:0.75,careful --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/conduct/$k-wm.log 2>&1 &
done
wait
touch $R/conduct/.done
