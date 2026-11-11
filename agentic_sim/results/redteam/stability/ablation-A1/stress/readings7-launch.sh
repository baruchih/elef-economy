#!/bin/zsh
# Addendum 7's two readings asked (F4.4; November 12, 2026; notes §105): the orchestrator's own bad work standing a run under the temptation, and the private
# benefit a slot by policy — the stressed finals of record (§102: the three finalists at a temptation of 1 and the bond ×1, the direct's and the head alone's
# round-10 models) re-evaluated on the same seeds with the driver's new readings exported (troop_bad_delivered, troop_bad_standing, learner_private_real,
# allowance_claimed, learner_slots_json), the policy of record with the careful and the claimer beside; the finals of record at eval/final/ untouched.
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
  $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $L/direct/eval/final-r7 --seeds 21-40 --policies direct,careful,claimer --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $L/direct-final-r7.log 2>&1 &
  $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $L/wm/eval/final-r7 --seeds 21-40 --policies greedy,careful --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $L/wm-final-r7.log 2>&1 &
done
wait
touch $R/.readings7.done
