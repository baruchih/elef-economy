#!/bin/zsh
# Addendum 7's cells on the payoff table (November 12, 2026; notes §104), the scripted ε population of §99 (ε 0.2 uniform over the four actions, seeds 1–20,
# own-name credit), into the same payoff/ directory as §99's cells; read by payoff_stress.py → payoff-addendum7.md.
#   f42: F4.2's stake at every member seat — G_V ×2 and ×4 (--gv 10, 20; the first review's bond with it, the later seats' multiple at 1) × the temptation {1, 2}
#        on the three finalists (12 cells; cell names -gv10 / -gv20).
#   g2:  G2's premium seat's stake on arm 0 with π^A pinned — the bond at the audit and panel seats {×6, ×8} × π^A {0.10, 0.20} × the audit seat's role weight
#        {1.5 (of record), 3 (--w-audit 3, a harness option on a parameter of record)} × the temptation {1, 2} (16 cells; -w3 names the weight at 3), and beside
#        them π^A 0.20 at ×1 and ×4 at the weight of record, at both temptations (4 cells), for the slope.
# Run from agentic_sim/ in the elef-redteam env: payoff2-launch.sh f42|g2 [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/stress/payoff
PAR=${2:-4}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[pa20]="--pi-a0 0.20 --pi-a-max 0.20"
ARM[arm2]="--arm 2"
ARM[arm4]="--arm 4"
n=0
run() {   # name, extra args
  mkdir -p $D/$1
  $PY -m redteam.collect --out $D/$1 --seeds 1-20 --policies eps4 --attrib own -- "${CELL[@]}" ${=2} > $D/$1.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
}
case ${1:-f42} in
  f42)
    for k in pa10 arm2 arm4; do for t in 1 2; do for g in 10 20; do
      run $k-t$t-b1-gv$g "${ARM[$k]} --temptation $t --bond-mult-later 1 --gv $g"
    done; done; done
    wait; touch $D/.f42.done ;;
  g2)
    for t in 1 2; do for k in pa10 pa20; do for b in 6 8; do
      run $k-t$t-b$b "${ARM[$k]} --temptation $t --bond-mult-later $b"
      run $k-t$t-b$b-w3 "${ARM[$k]} --temptation $t --bond-mult-later $b --w-audit 3"
    done; done; done
    for t in 1 2; do for b in 1 4; do
      run pa20-t$t-b$b "${ARM[pa20]} --temptation $t --bond-mult-later $b"
    done; done
    wait; touch $D/.g2.done ;;
esac
