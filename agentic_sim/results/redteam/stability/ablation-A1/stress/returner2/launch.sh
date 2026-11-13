#!/bin/zsh
# Addendum 10's J3.3 (November 13, 2026; notes §111) at ffd23d851: §110's four returner worlds (stress/returner/launch.sh at 848e1d22c — the claimreturner, the
# claimer and the careful on the learner's slot in Q1's re-arrival cell, a careful population and Q1's 60/40, the pin and arm 4, a temptation of 1, the bond ×1,
# seeds 21–40) run again whole with run_q's `--trace on` (the learner's lifetime by tick from the environment's marks) and the driver's `susp_ticks` in the
# per-slot export — so that the first name's wallet and benefit at its first suspension, and the careful slot's wallet at the same tick on the same seed, can be
# read (returner_trace_read.py). The same worlds: the policies scripted, the episode by seed; every figure of record identical.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/returner2
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
for k in pa10 arm4; do for pop in careful hand; do
  ST=0; if [ "$pop" = "hand" ]; then ST=0.6; fi
  $PY -m redteam.run_q --out $R/$k-$pop --seeds 21-40 --policies claimreturner,claimer,careful --attrib own --trace on -- --entry-pool 20 --stampers $ST --learner-slot on --learner-rearrive on --temptation 1 --bond-mult-later 1 ${=ARM[$k]} > $R/$k-$pop.log 2>&1 &
done; done
wait
touch $R/.done
