#!/bin/zsh
# Addendum 11's K3 (November 13, 2026; notes §111) at 1a02e69ec: the entry test's four worlds at 1 in 10 (the pin and arm 4, the direct and the head alone of
# §102's chains on the claiming slots, 'mix:<policy>:0.1'; stress/entry/launch.sh's cells) and §110's eight dose worlds (stress/dose/launch.sh's cells) run again
# whole with the slot's standing by tick kept (the driver's per-slot export: ticks, the wallet's change and the benefit in good standing and while suspended or on
# probation) — the same worlds (the policies frozen, the episode by seed), every group figure of record identical; read by standing_read.py → standing-read.md.
# Run from agentic_sim/ in the elef-redteam env: launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
S=$R/standing
PAR=${1:-6}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
n=0
run() { "$@" & n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi }
for k in pa10 arm4; do
  L=$R/learned/$k-t1-b1
  run $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $S/entry-$k-direct-s0.1 --seeds 21-40 --policies mix:direct:0.1 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $S/entry-$k-direct-s0.1.log 2>&1
  run $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $S/entry-$k-wm-s0.1 --seeds 21-40 --policies mix:greedy:0.1 --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $S/entry-$k-wm-s0.1.log 2>&1
  for q in 0.1 0.3 1; do
    SEEDS=21-40; if [ "$q" = "0.1" ]; then SEEDS=21-60; fi
    run $PY -m redteam.run_q --out $S/dose-$k-dose$q --seeds $SEEDS --policies mix:dose$q:0.25,careful --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $S/dose-$k-dose$q.log 2>&1
  done
done
for sp in audit first; do
  run $PY -m redteam.run_q --out $S/dose-pa10-dose0.3$sp --seeds 21-40 --policies mix:dose0.3$sp:0.25,careful --attrib own -- "${CELL[@]}" ${=ARM[pa10]} > $S/dose-pa10-dose0.3$sp.log 2>&1
done
wait
touch $S/.done
