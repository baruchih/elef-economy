#!/bin/zsh
# Addendum 24's AD3.7 (notes §121): read 9 (conduct M at 0.1 on 1 slot in 4) and read 19 (M at 0.2 on 1 in 4) run again whole at this commit for the ticks without the earned
# seats the record does not carry (a19/rerun/r9 and a19/r19 are at 906fc5ac4, before the standing tally split them) — checked to the digit against the record before they are read.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a22
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
JOBS=(
"rerun/r9-s21-70 21-70 mix:doseM0.1:0.25 $W3"
"rerun/r9-s71-120 71-120 mix:doseM0.1:0.25 $W3"
"rerun/r19-s21-70 21-70 mix:doseM0.2:0.25 $W3"
"rerun/r19-s71-120 71-120 mix:doseM0.2:0.25 $W3"
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
touch $R/.done2
