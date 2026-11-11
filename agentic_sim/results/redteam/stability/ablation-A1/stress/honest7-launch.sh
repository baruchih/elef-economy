#!/bin/zsh
# Addendum 7's "read beside, because the honest pay the stake too" (G2, F4.2; November 12, 2026; notes §106): the careful population in each added cell —
# its false penalties by seat, its surplus, its idle-for-bond time, the underfunded reviews, the slots alive, the orchestrator's share of the audit seats —
# run_q --policies careful on seeds 21–30 (ten seeds; a reading beside the table, not a pairing), → payoff/honest/<cell>/eval.json. Parallel 3.
# Run from agentic_sim/ in the elef-redteam env: honest7-launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/stress/payoff/honest
PAR=${1:-3}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[pa20]="--pi-a0 0.20 --pi-a-max 0.20"
ARM[arm2]="--arm 2"
ARM[arm4]="--arm 4"
n=0
run() {
  mkdir -p $D/$1
  $PY -m redteam.run_q --out $D/$1 --seeds 21-30 --policies careful --attrib own -- "${CELL[@]}" ${=2} > $D/$1.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
}
for t in 1 2; do for k in pa10 pa20; do for b in 6 8; do
  run $k-t$t-b$b "${ARM[$k]} --temptation $t --bond-mult-later $b"
  run $k-t$t-b$b-w3 "${ARM[$k]} --temptation $t --bond-mult-later $b --w-audit 3"
done; done; done
for t in 1 2; do for b in 1 4; do run pa20-t$t-b$b "${ARM[pa20]} --temptation $t --bond-mult-later $b"; done; done
for k in pa10 arm2 arm4; do for t in 1 2; do for g in 10 20; do run $k-t$t-b1-gv$g "${ARM[$k]} --temptation $t --bond-mult-later 1 --gv $g"; done; done; done
run pa10-t1-b1 "${ARM[pa10]} --temptation 1 --bond-mult-later 1"
wait; touch $D/.done
