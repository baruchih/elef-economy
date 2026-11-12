#!/bin/zsh
# Addendum 8's honest side of the missing cells (H3.2; November 13, 2026; notes §109), as §106's addendum: the careful population in each added stake —
# run_q --policies careful on seeds 21–30 → payoff/honest/<cell>/eval.json. Nine stakes at a temptation of 1: the temptation is the claimer's alone and a
# careful population never claims (§106's honest cells at t1 and t2 are identical to the decimal but for the cell's label and the seconds). Parallel 3.
# Run from agentic_sim/ in the elef-redteam env: honest8-launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/stress/payoff/honest
PAR=${1:-3}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
declare -A ARM
ARM[pa20]="--pi-a0 0.20 --pi-a-max 0.20"
ARM[pa30]="--pi-a0 0.30 --pi-a-max 0.30"
n=0
run() {
  mkdir -p $D/$1
  $PY -m redteam.run_q --out $D/$1 --seeds 21-30 --policies careful --attrib own -- "${CELL[@]}" ${=2} > $D/$1.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
}
run pa20-t1-b2    "${ARM[pa20]} --temptation 1 --bond-mult-later 2"
run pa20-t1-b2-w3 "${ARM[pa20]} --temptation 1 --bond-mult-later 2 --w-audit 3"
run pa20-t1-b4-w3 "${ARM[pa20]} --temptation 1 --bond-mult-later 4 --w-audit 3"
for b in 1 2 4; do
  run pa30-t1-b$b    "${ARM[pa30]} --temptation 1 --bond-mult-later $b"
  run pa30-t1-b$b-w3 "${ARM[pa30]} --temptation 1 --bond-mult-later $b --w-audit 3"
done
wait; touch $D/.honest8.done
