#!/bin/zsh
# Addendum 29 (November 18, 2026, later that morning; notes §124) — the harness at 8e30eac40 (nothing built): world 3's all-careful and read 29 run again whole for the pair tally
# (a first reviewer and the member at its audit seat; every run carries it from d28f75da5), seeds 21–120 — checked to the digit against a23/rerun and a23/r29 before they are read.
# Four processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a25
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
JOBS=(
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"rerun/r29-s21-70 21-70 mix:caseM0.2:0.75 $W3"
"rerun/r29-s71-120 71-120 mix:caseM0.2:0.75 $W3"
)
run_one() {
  local out=$1 seeds=$2 pols=$3; shift 3
  mkdir -p $R/$(dirname $out)
  $PY -m redteam.run_q --out $R/$out --seeds $seeds --policies $pols --attrib own -- ${=CELL} "$@" > $R/$out.log 2>&1
}
for j in "${JOBS[@]}"; do
  set -- ${=j}; run_one "$@" &
done
wait
touch $R/.done
