#!/bin/zsh
# Addendum 7's F4.1 — trap or equilibrium (November 12, 2026; notes §104): frozen policies, no training. On each finalist at a temptation of 1 and the bond ×1,
# the stressed policy of record (§102's finals: the direct's and the head alone's round-10 models) on half the slots and the careful on the other half, in one
# world — run_q's `mix:<policy>` (the half drawn once per slot by a stable hash of the seed and the name, arrivals included), read by half: the slots' real
# lifetime with the private benefit counted, the suspensions, the seats held. Seeds 21–40. Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm2]="--arm 2"
ARM[arm4]="--arm 4"
for k in pa10 arm2 arm4; do
  L=$R/learned/$k-t1-b1
  $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $R/f41/$k-direct --seeds 21-40 --policies mix:direct --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/f41/$k-direct.log 2>&1 &
  $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $R/f41/$k-wm --seeds 21-40 --policies mix:greedy --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/f41/$k-wm.log 2>&1 &
done
wait
touch $R/f41/.done
