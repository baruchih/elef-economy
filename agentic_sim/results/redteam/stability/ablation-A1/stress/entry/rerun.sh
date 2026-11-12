#!/bin/zsh
# The halves (f41/) and the entry test (entry/) re-read on the driver's corrected suspension log (4df18f1bc; November 13, 2026): the same commands as launch.sh,
# into <eval>-at-4df18f1bc/ beside the evaluations of record (every column but the per-slot suspensions reproduces to the decimal: the check in entry_read.py).
# Waits for addendum 8's queue. Run from agentic_sim/ in the elef-redteam env: rerun.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
until [ -f $R/.queue8.done ]; do sleep 60; done
PAR=${1:-6}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm2]="--arm 2"
ARM[arm4]="--arm 4"
n=0
go() { $@ & n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi; }
for k in pa10 arm2 arm4; do
  L=$R/learned/$k-t1-b1
  go $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $R/f41/$k-direct-at-4df18f1bc --seeds 21-40 --policies mix:direct --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/f41/$k-direct-at-4df18f1bc.log 2>&1
  go $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $R/f41/$k-wm-at-4df18f1bc --seeds 21-40 --policies mix:greedy --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/f41/$k-wm-at-4df18f1bc.log 2>&1
done
for s in 0.1 0.25 0.75; do for k in pa10 arm4; do
  L=$R/learned/$k-t1-b1
  go $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $R/entry/$k-direct-s$s-at-4df18f1bc --seeds 21-40 --policies mix:direct:$s --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/entry/$k-direct-s$s-at-4df18f1bc.log 2>&1
  go $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $R/entry/$k-wm-s$s-at-4df18f1bc --seeds 21-40 --policies mix:greedy:$s --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/entry/$k-wm-s$s-at-4df18f1bc.log 2>&1
done; done
wait; touch $R/entry/.rerun.done
