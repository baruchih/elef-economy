#!/bin/zsh
# Addendum 17 (November 16, 2026; notes §116) at 59ce02e20 — the harness as at b1fa10d2c plus conduct G (doseG<q>: careful until its first wrong planted verdict, then a
# dose of q as a member at the decisions where its earned seats are lost — the engine's panel_eligible on its own record through the env's info — careful where
# held, on probation and after a suspension) and the members' wrong planted verdicts by seat and by the case's kind (plant_fail_{bad,good}_<seat>, a reading);
# nothing drawn differently, so a world of record reproduces to the digit. The three reads without training (V4), numbered through from Q4's, each in world 3's
# cell — the stressed world at a temptation of 1, arm 1 with π^A held at 0.10, the weights of record, the later seats' bond ×1 and the first review's bond of
# record — the conduct on 1 slot in 4, the all-careful of the same cell on the same seeds (of record on 21–120: a15/rerun/w3, a16/r9/careful-w3-s81-120; carried
# to 121–260 here beside read 12's seeds):
#   r12/: conduct F at 0.3 (doseF0.3) on seeds 21–260.
#   r13/: conduct G at 0.3 (doseG0.3) on seeds 21–260.
#   r14/: conduct F at 1.0 (doseF1.0) on seeds 21–140.
# Twelve processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a17
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
JOBS=(
"r12/s21-70 21-70 mix:doseF0.3:0.25 $W3"
"r12/s71-120 71-120 mix:doseF0.3:0.25 $W3"
"r12/s121-170 121-170 mix:doseF0.3:0.25,careful $W3"
"r12/s171-215 171-215 mix:doseF0.3:0.25,careful $W3"
"r12/s216-260 216-260 mix:doseF0.3:0.25,careful $W3"
"r13/s21-70 21-70 mix:doseG0.3:0.25 $W3"
"r13/s71-120 71-120 mix:doseG0.3:0.25 $W3"
"r13/s121-170 121-170 mix:doseG0.3:0.25 $W3"
"r13/s171-215 171-215 mix:doseG0.3:0.25 $W3"
"r13/s216-260 216-260 mix:doseG0.3:0.25 $W3"
"r14/s21-80 21-80 mix:doseF1.0:0.25 $W3"
"r14/s81-140 81-140 mix:doseF1.0:0.25 $W3"
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
