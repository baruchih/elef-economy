#!/bin/zsh
# Addendum 20 (November 17, 2026; notes §118) at 906fc5ac4 — the harness as at f16e1ffee plus addendum 20's readings (each review's flows by the standing and seat of
# the review they belong to; every wallet event by the slot's standing and class; the first reviews by standing and the work's kind; the wrong planted verdicts by
# standing and seat; the probation spells); nothing drawn differently, so a world of record reproduces to the digit (checked: world 3's all-careful of seed 21 against a18/rerun).
#   r18/: conduct M at 0.1 on every slot (mix:doseM0.1:1.0 — the mix wrapper's share at 1: every slot's hash is under it) in world 3's cell (arm 1, π^A held at 0.10, the
#         weights of record, the later seats' bond ×1), seeds 21–120 — read against the all-careful population of the same seeds by seed.
#   r19/: conduct M at 0.2 (doseM0.2: careful on probation and after a suspension, a claim at one review in five as a member) on 1 slot in 4 in world 3's cell, seeds 21–120.
#   rerun/: Z4.1, Z4.2 and Z3's confirmations need per-slot readings the record does not carry, so the all-careful of world 3 and read 9 (conduct M at 0.1 on 1 slot in 4) on
#         seeds 21–120 are run again whole here — checked to the digit against a18/rerun/cw3-* and a18/rerun/r9-* (nothing collected anew).
# Twelve processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a19
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
PIN="--pi-a0 0.10 --pi-a-max 0.10"
W3="--arm 1 $PIN --w-audit 1.5"
JOBS=(
"r18/s21-45 21-45 mix:doseM0.1:1.0 $W3"
"r18/s46-70 46-70 mix:doseM0.1:1.0 $W3"
"r18/s71-95 71-95 mix:doseM0.1:1.0 $W3"
"r18/s96-120 96-120 mix:doseM0.1:1.0 $W3"
"r19/s21-45 21-45 mix:doseM0.2:0.25 $W3"
"r19/s46-70 46-70 mix:doseM0.2:0.25 $W3"
"r19/s71-95 71-95 mix:doseM0.2:0.25 $W3"
"r19/s96-120 96-120 mix:doseM0.2:0.25 $W3"
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"rerun/r9-s21-70 21-70 mix:doseM0.1:0.25 $W3"
"rerun/r9-s71-120 71-120 mix:doseM0.1:0.25 $W3"
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
