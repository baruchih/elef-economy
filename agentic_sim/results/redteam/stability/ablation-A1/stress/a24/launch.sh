#!/bin/zsh
# Addenda 27 and 28 (November 18, 2026; notes §123) — the harness at d28f75da5: the seating by group (`--seat-group`, `caseG<q>`, the picks by group, the holder of the audit by group) and two
# readings in every run (how often one pair meets — a first reviewer and the member at its audit seat; two member slots failing the same planted case), nothing drawn differently with the
# option off (seed 21 of world 3's all-careful and of read 25 reproduce a23/rerun and a22/rerun to the digit).
#   rerun/r25-*: read 25 run again whole (seeds 21–120) for AH4.2's pairs — checked to the digit against a22/rerun before it is read.
#   r30/: the all-careful in the cell of the first failure (world 3's cell with --theta-duty 0.20) with the ticks off at none (--t-susp 0), seeds 21–120 (addendum 27, Baruchi's first "Yes").
#   r31/: conduct M at 0.1 with its claims set by the case (caseM0.1) on every slot, the same cell, seeds 21–120.
#   r32/: caseM0.1 on 3 slots in 4, the rest careful (the mix wrapper's share at 0.75), world 3's cell as it is, seeds 21–120.
#   r33/: two groups of slots, every slot on caseG0.1 (its group's salt), world 3's cell, today's picks with the groups read (--seat-group read), seeds 21–120.
#   r34/: the same with the seating by group (--seat-group prefer), seeds 21–120.
# Twelve processes at once. Run from agentic_sim/ in the elef-redteam env.
#   r33/ and r34/ of record are launch2.sh's, run again at 8e30eac40 (the first reviewer read for the picks by group a slot's name alone; this launcher's r33/r34 at d28f75da5 discarded uncommitted).
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a24
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
T20="$W3 --theta-duty 0.20"
JOBS=(
"rerun/r25-s21-70 21-70 mix:caseM0.1:1.0 $W3"
"rerun/r25-s71-120 71-120 mix:caseM0.1:1.0 $W3"
"r30/s21-70 21-70 careful $T20 --t-susp 0"
"r30/s71-120 71-120 careful $T20 --t-susp 0"
"r31/s21-70 21-70 mix:caseM0.1:1.0 $T20 --t-susp 0"
"r31/s71-120 71-120 mix:caseM0.1:1.0 $T20 --t-susp 0"
"r32/s21-70 21-70 mix:caseM0.1:0.75 $W3"
"r32/s71-120 71-120 mix:caseM0.1:0.75 $W3"
"r33/s21-70 21-70 mix:caseG0.1:1.0 $W3 --seat-group read"
"r33/s71-120 71-120 mix:caseG0.1:1.0 $W3 --seat-group read"
"r34/s21-70 21-70 mix:caseG0.1:1.0 $W3 --seat-group prefer"
"r34/s71-120 71-120 mix:caseG0.1:1.0 $W3 --seat-group prefer"
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
