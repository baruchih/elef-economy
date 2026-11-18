#!/bin/zsh
# Addendum 28 (November 18, 2026; notes §123) — reads 33 and 34 run again whole at 8e30eac40: the first reviewer read for the picks by group is a slot's name alone (at d28f75da5 the
# orchestrator's plant_rev: alias on a planted approval was read as a slot with a group drawn from its name — about 130 audit picks a run seated by a pseudo-group under prefer;
# those runs discarded uncommitted). Everything else as launch.sh. Four processes at once. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a24
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
JOBS=(
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
touch $R/.done2
