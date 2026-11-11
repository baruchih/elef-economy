#!/bin/zsh
# The stressed world (the plan's steps 3–5; the reviewer's addendum 5: "then the stressed world ... on the finalists: arm 0 with the planted
# approval's floor at 0.10, arm 2, arm 4"), the payoff table first as the brief orders (§6/§7.1): the scripted ε population of run 24's entry
# cell on own-name credit, seeds 1–20, four actions where the temptation is on (ε 0.2 uniform over inspect / approve blind / reject blind /
# claim the allowance and stamp), per finalist × temptation {1, 2, 4} × the bond at the audit and panel seats {×1, ×2, ×4}; and the shared
# difficulty at ρ 0.5 (the members', the troops' and the ruling's alike) at temptation 1, bond ×1 — the correlated-errors axis read apart.
# Run from agentic_sim/ in the elef-redteam env: payoff-launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy-stress/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/stress/payoff
PAR=${1:-6}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm2]="--arm 2"
ARM[arm4]="--arm 4"
n=0
run() {   # name, extra args
  mkdir -p $D/$1
  $PY -m redteam.collect --out $D/$1 --seeds 1-20 --policies eps4 --attrib own -- "${CELL[@]}" ${=2} > $D/$1.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
}
for k in pa10 arm2 arm4; do
  for t in 1 2 4; do
    for b in 1 2 4; do
      run $k-t$t-b$b "${ARM[$k]} --temptation $t --bond-mult-later $b"
    done
  done
  run $k-t1-b1-rho0.5 "${ARM[$k]} --temptation 1 --shared-difficulty 0.5 --shared-difficulty-troops 0.5 --shared-difficulty-ruling 0.5"
done
wait
touch $D/.done
