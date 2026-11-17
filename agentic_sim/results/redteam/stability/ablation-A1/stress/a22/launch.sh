#!/bin/zsh
# Addendum 24 (November 17, 2026; notes §121) — the harness as at eca3d5ee3 plus the readings of this commit (the driver's `bad_met_first_json`: the bad deliveries by their first
# reviewer's kind and a wrong first approval's fate, a claim's or a careful error's, paid or overturned and at whose seat; the rejections of good work that stand, by the engine's
# reason; `appeals_unfunded` with the fee and the holding at the time; the state's first-review seats; per slot the ticks as a member without the earned seats, split by an
# undetermined record; the planted bad cases met) — readings at the closure and in the standing tally, nothing drawn differently (seed 21 of world 3's all-careful and of read 25
# reproduce a19/rerun and a20/r25 to the digit: 0 row and 0 per-slot differences).
#   rerun/cw3-*: world 3's all-careful (seeds 21–120) run again whole for AD4.2 and AD4.4.   rerun/r23-*: read 23's all-careful (θ_duty 0.20) run again whole, read 28's baseline.
#   rerun/r25-*: read 25 run again whole for AD4.1 — checked to the digit against a20/r25 before it is read.
#   r26/: conduct M at 0.2 with its claims set by the case (caseM0.2) on every slot, world 3's cell as it is, seeds 21–120.   r27/: the same at 0.3 (caseM0.3).
#   r28/: caseM0.1 on every slot in the cell of the first failure (world 3's cell with --theta-duty 0.20), seeds 21–120.
# Twelve processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a22
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
PIN="--pi-a0 0.10 --pi-a-max 0.10"
W3="--arm 1 $PIN --w-audit 1.5"
T20="$W3 --theta-duty 0.20"
JOBS=(
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"rerun/r23-s21-70 21-70 careful $T20"
"rerun/r23-s71-120 71-120 careful $T20"
"rerun/r25-s21-70 21-70 mix:caseM0.1:1.0 $W3"
"rerun/r25-s71-120 71-120 mix:caseM0.1:1.0 $W3"
"r26/s21-70 21-70 mix:caseM0.2:1.0 $W3"
"r26/s71-120 71-120 mix:caseM0.2:1.0 $W3"
"r27/s21-70 21-70 mix:caseM0.3:1.0 $W3"
"r27/s71-120 71-120 mix:caseM0.3:1.0 $W3"
"r28/s21-70 21-70 mix:caseM0.1:1.0 $T20"
"r28/s71-120 71-120 mix:caseM0.1:1.0 $T20"
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
