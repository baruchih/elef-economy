#!/bin/zsh
# Addenda 18–19 (November 17, 2026; notes §117) at f16e1ffee — the harness as at 575e405b1 plus the per-slot readings (first run at bb0ada7af, whose tally read the standing after the verdict; run again whole here at f16e1ffee, the standing read before it) (a slot's reviews by standing and by the
# engine's seat kind with the planted cases among them by kind; its real-task reviews as a member before its first wrong planted verdict and before its first
# suspension; the care spent and the cost claimed, real; its wrong first approvals of real bad work, paid or overturned); nothing drawn differently, so a world of
# record reproduces to the digit (checked: world 3's all-careful of seed 81 and conduct M of seed 21).
#   r15/: conduct M at 0.5 (doseM0.5) on 1 slot in 4 in world 3's cell (arm 1, π^A held at 0.10, the weights of record, the later seats' bond ×1), seeds 21–120.
#   r16/: conduct M at 1.0 (doseM1.0: careful on probation and after a suspension, a claim at every review as a member) in world 3's cell, seeds 21–120.
#   r17/: conduct G at 1.0 (doseG1.0: careful until its first wrong planted verdict, then a claim at every decision where its earned seats are lost) in world 3's
#         cell, seeds 21–140 — read against read 14's conduct F at 1.0 (a17/r14b) by seed.
#   rerun/: W3's three counts and W2's level savings need per-slot tallies the record does not carry, so the worlds of reads 2, 4, 9 and 11 and the all-careful of
#         worlds 3 and 4 on seeds 21–120 are run again whole here (r2: conduct M at 0.1 in world 4's cell, 21–120; r4: M at 0.3 in world 4's cell, 21–80; r9: M at
#         0.1 in world 3's cell, 21–120; r11: M at 0.1 on 3 slots in 4 in world 4's cell, 21–80; cw3, cw4: the all-careful, 21–120) — checked to the digit against
#         a15/p4/r2-*, a15/p4/r4, a16/r9/*, a16/r11/s21-80, a15/rerun/w3, a16/r9/careful-w3-s81-120, a15/rerun/w4, a15/p4/r2-s81-120 (nothing collected anew).
# Sixteen processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a18
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
PIN="--pi-a0 0.10 --pi-a-max 0.10"
W3="--arm 1 $PIN --w-audit 1.5"; W4="--arm 1 $PIN --w-audit 3"
JOBS=(
"r15/s21-70 21-70 mix:doseM0.5:0.25 $W3"
"r15/s71-120 71-120 mix:doseM0.5:0.25 $W3"
"r16/s21-70 21-70 mix:doseM1.0:0.25 $W3"
"r16/s71-120 71-120 mix:doseM1.0:0.25 $W3"
"r17/s21-80 21-80 mix:doseG1.0:0.25 $W3"
"r17/s81-140 81-140 mix:doseG1.0:0.25 $W3"
"rerun/r9-s21-70 21-70 mix:doseM0.1:0.25 $W3"
"rerun/r9-s71-120 71-120 mix:doseM0.1:0.25 $W3"
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"rerun/r2-s21-70 21-70 mix:doseM0.1:0.25 $W4"
"rerun/r2-s71-120 71-120 mix:doseM0.1:0.25 $W4"
"rerun/r4-s21-80 21-80 mix:doseM0.3:0.25 $W4"
"rerun/r11-s21-80 21-80 mix:doseM0.1:0.75 $W4"
"rerun/cw4-s21-70 21-70 careful $W4"
"rerun/cw4-s71-120 71-120 careful $W4"
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
