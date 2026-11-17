#!/bin/zsh
# Addendum 26 (November 17, 2026, late evening; notes §122) — the harness as at 72f341281 plus two readings (the audit road's standing rejections of good work by whose audit
# differed, a member's or the state's; a slot's first wrong planted verdict as a member — the planted bad cases its window held at that verdict, the seat, and whether it holds
# the earned seats at the reveal), nothing drawn differently (seed 21 of world 3's all-careful reproduces a22/rerun to the digit).
#   rerun/cw3-*: world 3's all-careful run again whole (seeds 21–120) for AF4.1 and AE3.3 — checked to the digit against a22/rerun before it is read.
#   r29/: conduct M at 0.2 with its claims set by the case (caseM0.2) on 3 slots in 4, the rest careful (the mix wrapper's share at 0.75), world 3's cell as it is, seeds 21–120.
# Reads 30 and 31 are not run (Baruchi's word not with the message). Four processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a23
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
JOBS=(
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"r29/s21-70 21-70 mix:caseM0.2:0.75 $W3"
"r29/s71-120 71-120 mix:caseM0.2:0.75 $W3"
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
