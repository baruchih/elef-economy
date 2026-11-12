#!/bin/zsh
# Addendum 9's dose (I4.1; November 12, 2026; notes §110) and the entry test's worlds re-read with the slots' readings (I3.1) — at b5961bf9f (the harness:
# run_q's dose policy, the driver's per-slot readings). The dose: a scripted policy — careful, and at each review decision a claim with probability q
# (`dose<q>` at every review seat; `dose<q>audit` at the member's audit seat alone; `dose<q>first` at the first review alone; the seat kind from the env's
# info, the seat table's source) — a reader-side wrapper, as the share was, declared before running; on 1 in 4 of the slots (`mix:dose<q>:0.25`), the rest
# careful; the pin and arm 4 at a temptation of 1 and the bond ×1; doses 0.1, 0.3 and 1 at every seat, and on the pin 0.3 at the audit seat alone and at the
# first review alone; the all-careful population (`careful`) in the same worlds; seeds 21–40, the two worlds at 0.1 on seeds 21–60 (41–60 free of any other use).
# The entry test's twelve worlds and F4.1's four halves worlds run again whole at this commit beside the evaluations of record (`<cell>-at-b5961bf9f/`): the
# same worlds (the policies frozen, the episode by seed), every group figure of record identical, the slots' ticks in place and wallet sources now kept.
# Run from agentic_sim/ in the elef-redteam env: launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
C=b5961bf9f
PAR=${1:-8}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
n=0
run() { "$@" & n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi }
for k in pa10 arm4; do
  for q in 0.1 0.3 1; do
    SEEDS=21-40; if [ "$q" = "0.1" ]; then SEEDS=21-60; fi
    run $PY -m redteam.run_q --out $R/dose/$k-dose$q --seeds $SEEDS --policies mix:dose$q:0.25,careful --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/dose/$k-dose$q.log 2>&1
  done
done
for sp in audit first; do
  run $PY -m redteam.run_q --out $R/dose/pa10-dose0.3$sp --seeds 21-40 --policies mix:dose0.3$sp:0.25,careful --attrib own -- "${CELL[@]}" ${=ARM[pa10]} > $R/dose/pa10-dose0.3$sp.log 2>&1
done
for k in pa10 arm4; do
  L=$R/learned/$k-t1-b1
  for s in 0.1 0.25 0.75; do
    run $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $R/entry/$k-direct-s$s-at-$C --seeds 21-40 --policies mix:direct:$s --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/entry/$k-direct-s$s-at-$C.log 2>&1
    run $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $R/entry/$k-wm-s$s-at-$C --seeds 21-40 --policies mix:greedy:$s --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/entry/$k-wm-s$s-at-$C.log 2>&1
  done
  run $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $R/f41/$k-direct-at-$C --seeds 21-40 --policies mix:direct --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/f41/$k-direct-at-$C.log 2>&1
  run $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $R/f41/$k-wm-at-$C --seeds 21-40 --policies mix:greedy --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/f41/$k-wm-at-$C.log 2>&1
done
wait
touch $R/dose/.done
