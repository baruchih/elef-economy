#!/bin/zsh
# Addendum 9's name that returns (I4.2; November 12, 2026; notes §110) at 848e1d22c. The return cannot be put on the mixed world's claiming slots without a
# build (the population cell's exit is the rule and has no re-arrival; a slot returning under a fresh name joined to its group is a driver change), so the
# operator runs as Q1's re-arrival cell: one learner slot (`--learner-slot on --learner-rearrive on`), the hand-written `claimreturner` — claim at every
# review seat, leave at the first period boundary at which it is suspended (the boundary is the only exit decision the cell has; the driver's exit rule is
# off for the slot), return at once under a fresh name L<n> with the bank's arrival loan (F0 50 nominal at the index) and a probationer's standing (no record,
# the odds pinned at 1, initial reviews only, admitted on n_min bad plants with a passing record) — beside the careful on the same slot and the `claimer`
# that never leaves; in a careful population (`--stampers 0`, the entry pool's candidates careful too) and in Q1's own 60/40 population (`--stampers 0.6`);
# the pin and arm 4 at a temptation of 1 and the bond ×1; seeds 21–40. A temptation of 2 is read from the same worlds (the benefit is off the ledger and
# unread by the scripted policies). Run from agentic_sim/ in the elef-redteam env: launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
PAR=${1:-4}
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
n=0
for k in pa10 arm4; do for pop in careful hand; do
  ST=0; if [ "$pop" = "hand" ]; then ST=0.6; fi
  $PY -m redteam.run_q --out $R/returner/$k-$pop --seeds 21-40 --policies claimreturner,claimer,careful --attrib own -- --entry-pool 20 --stampers $ST --learner-slot on --learner-rearrive on --temptation 1 --bond-mult-later 1 ${=ARM[$k]} > $R/returner/$k-$pop.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
done; done
wait
touch $R/returner/.done
