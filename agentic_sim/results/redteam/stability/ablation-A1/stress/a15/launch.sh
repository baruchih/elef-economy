#!/bin/zsh
# Addendum 15 (November 16, 2026; notes §114) at 726a25c76 — the harness as at 7bd5dd5fc plus the per-slot readers (the claims by standing and after a failure, the
# fees and bonds by seat, the failure phases), the seats by kind at closure and the two conducts; nothing drawn differently, so a world of record reproduces to the row.
# rerun/: N4's worlds 1, 2, 3, 4 and 6 run again whole for the new tallies (P3.1–P3.4; world 5 not needed) — w1 and w6 on seeds 21–120, w2/w3/w4 on 21–80 (w4 at the
#   dose of 0.1 alone); every figure of record checked to the digit by a15_read.py.
# p4/: the eight reads — conduct M (doseM<q>: careful on probation, a dose of q as a member) in world 1's, 4's and 6's cells at 0.1 on seeds 21–120 (world 4's
#   all-careful carried to 81–120) and in world 4's cell at 0.3 on 21–80; conduct F (doseF0.3: careful until a wrong planted verdict is on its record, then M at 0.3)
#   in world 4's and 6's cells on 21–80; the member's audit seat alone under arm 1 (dose0.3audit) at the fee of record and doubled on 21–80 — the all-careful of each
#   from rerun/ (the same cell on the same seeds). The cell: the stressed world at a temptation of 1, the later seats' bond ×1, the first review's bond of record,
#   the conduct on 1 slot in 4 (mix:<conduct>:0.25) and the rest careful. Ten processes. Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a15
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
PIN="--pi-a0 0.10 --pi-a-max 0.10"
W1="$PIN --w-audit 1.5"; W2="$PIN --w-audit 3"; W3="--arm 1 $PIN --w-audit 1.5"; W4="--arm 1 $PIN --w-audit 3"; W6="--arm 4"
JOBS=(
"rerun/w1-s21-70 21-70 mix:dose0.1:0.25,careful $W1"
"rerun/w1-s71-120 71-120 mix:dose0.1:0.25,careful $W1"
"rerun/w2 21-80 mix:dose0.1:0.25,careful $W2"
"rerun/w3 21-80 mix:dose0.1:0.25,careful $W3"
"rerun/w4 21-80 mix:dose0.1:0.25,careful $W4"
"rerun/w6-s21-70 21-70 mix:dose0.1:0.25,careful $W6"
"rerun/w6-s71-120 71-120 mix:dose0.1:0.25,careful $W6"
"p4/r1-s21-70 21-70 mix:doseM0.1:0.25 $W1"
"p4/r1-s71-120 71-120 mix:doseM0.1:0.25 $W1"
"p4/r2-s21-80 21-80 mix:doseM0.1:0.25 $W4"
"p4/r2-s81-120 81-120 mix:doseM0.1:0.25,careful $W4"
"p4/r3-s21-70 21-70 mix:doseM0.1:0.25 $W6"
"p4/r3-s71-120 71-120 mix:doseM0.1:0.25 $W6"
"p4/r4 21-80 mix:doseM0.3:0.25 $W4"
"p4/r5 21-80 mix:doseF0.3:0.25 $W4"
"p4/r6 21-80 mix:doseF0.3:0.25 $W6"
"p4/r7 21-80 mix:dose0.3audit:0.25 $W3"
"p4/r8 21-80 mix:dose0.3audit:0.25 $W4"
)
run_one() {
  local out=$1 seeds=$2 pols=$3; shift 3
  $PY -m redteam.run_q --out $R/$out --seeds $seeds --policies $pols --attrib own -- ${=CELL} "$@" > $R/$out.log 2>&1
}
n=0
for j in "${JOBS[@]}"; do
  set -- ${=j}; run_one "$@" &
  n=$((n+1)); if [ $((n % 10)) -eq 0 ]; then wait; fi
done
wait
touch $R/.done
