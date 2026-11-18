#!/bin/zsh
# Addendum 30 (November 18, 2026, midday; notes §125) — the harness at a4fc4f6c4: the conduct with two doses (`caseM<q>p<qP>`, Baruchi's
# word of November 18), the drawn audit and panel seats on their own stream (`--seat-draw seats`, a construction), the free-count reading at the audit and panel picks, the wrong planted verdicts by
# kind per slot, the dial's level in the row — nothing drawn differently with the options off (read 25 reproduced whole first, rerun/p11).
#   rerun/p11-*: caseM0.1p0.1 on every slot in world 3's cell, seeds 21–120 — the ordered check that the conduct with the two doses equal is caseM0.1 to the digit (against a24/rerun/r25).
#   r35/:  world 3's all-careful with the seats drawn (--seat-draw seats; the audit and panel seats among the free panel-eligible members at the seat's turn, the first review the round-robin's), seeds 21–120.
#   r35a/: the same under --assignment seeded, the option of record as it is (every pick drawn, the first review among them, on the world's own stream — another world at the seed), seeds 21–120.
#   r36/:  caseM0.2 on 3 slots in 4, the rest careful, with the seats drawn (--seat-draw seats), seeds 21–120 (read 29 with the seats drawn).
#   r36a/: the same under --assignment seeded as it is.
#   r37/:  cell A — caseM0.1p0.98 on 1 slot in 4, the rest careful, seeds 21–120.
#   r38/:  cell B — caseM0.2p0 on 1 slot in 4, the rest careful, seeds 21–120.
#   r39/:  cell B on 3 slots in 4, seeds 21–120.
#   r40/:  cell B on every slot, seeds 21–120.
# Fourteen processes at once (two seed halves a read, the reproduction included). Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a26
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
JOBS=(
"rerun/p11-s21-70 21-70 mix:caseM0.1p0.1:1.0 $W3"
"rerun/p11-s71-120 71-120 mix:caseM0.1p0.1:1.0 $W3"
"r35/s21-70 21-70 careful $W3 --seat-draw seats"
"r35/s71-120 71-120 careful $W3 --seat-draw seats"
"r35a/s21-70 21-70 careful $W3 --assignment seeded"
"r35a/s71-120 71-120 careful $W3 --assignment seeded"
"r36/s21-70 21-70 mix:caseM0.2:0.75 $W3 --seat-draw seats"
"r36/s71-120 71-120 mix:caseM0.2:0.75 $W3 --seat-draw seats"
"r36a/s21-70 21-70 mix:caseM0.2:0.75 $W3 --assignment seeded"
"r36a/s71-120 71-120 mix:caseM0.2:0.75 $W3 --assignment seeded"
"r37/s21-70 21-70 mix:caseM0.1p0.98:0.25 $W3"
"r37/s71-120 71-120 mix:caseM0.1p0.98:0.25 $W3"
"r38/s21-70 21-70 mix:caseM0.2p0:0.25 $W3"
"r38/s71-120 71-120 mix:caseM0.2p0:0.25 $W3"
"r39/s21-70 21-70 mix:caseM0.2p0:0.75 $W3"
"r39/s71-120 71-120 mix:caseM0.2p0:0.75 $W3"
"r40/s21-70 21-70 mix:caseM0.2p0:1.0 $W3"
"r40/s71-120 71-120 mix:caseM0.2p0:1.0 $W3"
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
