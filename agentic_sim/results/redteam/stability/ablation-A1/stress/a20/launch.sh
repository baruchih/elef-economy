#!/bin/zsh
# Addendum 22 (November 17, 2026; notes §119) at eca3d5ee3 — the harness as at 906fc5ac4 plus the driver's `--theta-duty` (a passthrough on Params.theta_duty, 0.50 in every
# run of record) and the scripted conduct `caseM<q>` (conduct M with its claims set by the case); nothing drawn differently at the defaults (world 3's all-careful of seed 21
# reproduces a19/rerun to the digit with the option at 0.50).
#   rerun/r15-*: AB5.2 — read 15 (conduct M at 0.5 on 1 slot in 4, world 3's cell, seeds 21–120) run again whole for the spells the record does not carry (a18/r15 was at
#         f16e1ffee, before the spells were exported) — checked to the digit against a18/r15 before it is read.
#   The cell of the second failure: world 3's cell (arm 1, π^A held at 0.10, the weights of record, the later seats' bond ×1) with --theta-duty 0.34 and nothing else.
#   r20/: the all-careful population, seeds 21–140.   r21/: conduct G at 1.0 (doseG1.0) on 1 slot in 4, seeds 21–140.   r22/: conduct M at 0.1 (doseM0.1) on 1 slot in 4, seeds 21–120.
#   The cell of the first failure: world 3's cell with --theta-duty 0.20 (the earned seats' own threshold) and nothing else.
#   r23/: the all-careful population, seeds 21–120.   r24/: conduct M at 0.1 on 1 slot in 4, seeds 21–120.
#   r25/: AB7 — conduct M at 0.1 with its claims set by the case (caseM0.1) on every slot (the mix wrapper's share at 1.0) in world 3's cell as it is, seeds 21–120.
# Sixteen processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a20
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
PIN="--pi-a0 0.10 --pi-a-max 0.10"
W3="--arm 1 $PIN --w-audit 1.5"
T34="$W3 --theta-duty 0.34"; T20="$W3 --theta-duty 0.20"
JOBS=(
"rerun/r15-s21-70 21-70 mix:doseM0.5:0.25 $W3"
"rerun/r15-s71-120 71-120 mix:doseM0.5:0.25 $W3"
"r20/s21-60 21-60 careful $T34"
"r20/s61-100 61-100 careful $T34"
"r20/s101-140 101-140 careful $T34"
"r21/s21-60 21-60 mix:doseG1.0:0.25 $T34"
"r21/s61-100 61-100 mix:doseG1.0:0.25 $T34"
"r21/s101-140 101-140 mix:doseG1.0:0.25 $T34"
"r22/s21-70 21-70 mix:doseM0.1:0.25 $T34"
"r22/s71-120 71-120 mix:doseM0.1:0.25 $T34"
"r23/s21-70 21-70 careful $T20"
"r23/s71-120 71-120 careful $T20"
"r24/s21-70 21-70 mix:doseM0.1:0.25 $T20"
"r24/s71-120 71-120 mix:doseM0.1:0.25 $T20"
"r25/s21-70 21-70 mix:caseM0.1:1.0 $W3"
"r25/s71-120 71-120 mix:caseM0.1:1.0 $W3"
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
