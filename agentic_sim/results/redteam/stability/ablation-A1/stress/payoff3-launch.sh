#!/bin/zsh
# Addendum 8's missing cells of the stake's table (H3.2; November 13, 2026; notes §109): §106's instrument — the scripted ε population of §99 (ε 0.2 uniform
# over the four actions, seeds 1–20, own-name credit) on arm 0 with π^A pinned, the member's audit seat — at π^A 0.20 the bond ×2 at the weights 1.5 and 3
# and ×4 at the weight 3, at π^A 0.30 the bond ×1, ×2, ×4 at both weights; the temptation 1 and 2; the first review's bond as §99 had it (G_V 5). Eighteen
# cells into the same payoff/ directory, read with the rest by payoff_stress.py → payoff-addendum8.md. Run from agentic_sim/ in the elef-redteam env: payoff3-launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/stress/payoff
PAR=${1:-6}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
declare -A ARM
ARM[pa20]="--pi-a0 0.20 --pi-a-max 0.20"
ARM[pa30]="--pi-a0 0.30 --pi-a-max 0.30"
n=0
run() {   # name, extra args
  mkdir -p $D/$1
  $PY -m redteam.collect --out $D/$1 --seeds 1-20 --policies eps4 --attrib own -- "${CELL[@]}" ${=2} > $D/$1.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
}
for t in 1 2; do
  run pa20-t$t-b2    "${ARM[pa20]} --temptation $t --bond-mult-later 2"
  run pa20-t$t-b2-w3 "${ARM[pa20]} --temptation $t --bond-mult-later 2 --w-audit 3"
  run pa20-t$t-b4-w3 "${ARM[pa20]} --temptation $t --bond-mult-later 4 --w-audit 3"
  for b in 1 2 4; do
    run pa30-t$t-b$b    "${ARM[pa30]} --temptation $t --bond-mult-later $b"
    run pa30-t$t-b$b-w3 "${ARM[pa30]} --temptation $t --bond-mult-later $b --w-audit 3"
  done
done
wait; touch $D/.payoff3.done
