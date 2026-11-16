#!/bin/zsh
# Addendum 16 (November 16, 2026; notes §115) at b1fa10d2c — the harness as at 726a25c76 plus the per-slot readers of item 6 (a member's claims split by whether its
# earned seats were held at the claim; each failure phase's good-standing ticks and income and its benefit); nothing drawn differently, so a world of record reproduces
# to the row. The three reads without training (Q4), numbered through from P4's eight, each the stressed world at a temptation of 1, the later seats' bond ×1, the
# first review's bond of record, the all-careful of the same cell on the same seeds:
#   r9/: conduct M at 0.1 (doseM0.1) on 1 slot in 4 in world 3's cell (arm 1, π^A held at 0.10, the weight of record) on seeds 21–120; world 3's all-careful of
#        record on 21–80 (a15/rerun/w3) carried to 81–120 here (careful-w3-s81-120).
#   r10/: conduct F (doseF0.3: careful until a wrong planted verdict is on its record, then M at 0.3) on 1 slot in 4 in world 4's cell (arm 1, the pin, the weight
#        doubled) on seeds 81–260; with P4's read 5 (21–80) 240 seeds; world 4's all-careful of record on 21–120 (a15/rerun/w4, a15/p4/r2-s81-120) carried to 121–260.
#   r11/: conduct M at 0.1 on 3 slots in 4 (mix:doseM0.1:0.75) in world 4's cell on seeds 21–80.
#   r5b/, r6b/: P4's reads 5 and 6 (conduct F in world 4's and 6's cells, 21–80) run again whole for item 6's split — checked to the digit against a15/p4/r5, r6.
# Seeds beyond 120 are free: the driver seeds every stream by the integer's arithmetic as it does 21–120. Ten processes. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a16
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
PIN="--pi-a0 0.10 --pi-a-max 0.10"
W3="--arm 1 $PIN --w-audit 1.5"; W4="--arm 1 $PIN --w-audit 3"; W6="--arm 4"
JOBS=(
"r9/s21-70 21-70 mix:doseM0.1:0.25 $W3"
"r9/s71-120 71-120 mix:doseM0.1:0.25 $W3"
"r9/careful-w3-s81-120 81-120 careful $W3"
"r10/s81-125 81-125 mix:doseF0.3:0.25 $W4"
"r10/s126-170 126-170 mix:doseF0.3:0.25,careful $W4"
"r10/s171-215 171-215 mix:doseF0.3:0.25,careful $W4"
"r10/s216-260 216-260 mix:doseF0.3:0.25,careful $W4"
"r10/careful-w4-s121-125 121-125 careful $W4"
"r11/s21-80 21-80 mix:doseM0.1:0.75 $W4"
"r5b 21-80 mix:doseF0.3:0.25 $W4"
"r6b 21-80 mix:doseF0.3:0.25 $W6"
)
run_one() {
  local out=$1 seeds=$2 pols=$3; shift 3
  mkdir -p $R/$(dirname $out)
  $PY -m redteam.run_q --out $R/$out --seeds $seeds --policies $pols --attrib own -- ${=CELL} "$@" > $R/$out.log 2>&1
}
n=0
for j in "${JOBS[@]}"; do
  set -- ${=j}; run_one "$@" &
  n=$((n+1)); if [ $((n % 10)) -eq 0 ]; then wait; fi
done
wait
touch $R/.done
