#!/bin/zsh
# The split of the orchestrator's own bad work (November 12, 2026; notes §105's addendum): final-r7 read the bad work standing (vested) and left the rest unsplit between caught
# (final N) and still pending with its audit held at the run's end; the driver now exports troop_bad_final_n / troop_bad_pending, read here on the policies of record alone
# (the direct and the head alone), the same seeds, → eval/final-r7b/.
# Run from agentic_sim/ in the elef-redteam env: readings7-launch.sh
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
  $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $L/direct/eval/final-r7b --seeds 21-40 --policies direct --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $L/direct-final-r7b.log 2>&1 &
  $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $L/wm/eval/final-r7b --seeds 21-40 --policies greedy --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $L/wm-final-r7b.log 2>&1 &
done
wait
touch $R/.readings7b.done
