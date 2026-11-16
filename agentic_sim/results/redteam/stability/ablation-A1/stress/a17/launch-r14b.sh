#!/bin/zsh
# Addendum 17's read 14 run again whole at 575e405b1 (the harness as at 59ce02e20 plus the per-slot `claims_pre_susp`, the claims made before the slot's first
# suspension — a reading, nothing drawn differently, so r14/ at 59ce02e20 reproduces to the digit here, checked by a17_read.py). Waits for launch.sh's .done. Four processes.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a17
until [ -f $R/.done ]; do sleep 30; done
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
mkdir -p $R/r14b
for sr in 21-50 51-80 81-110 111-140; do
  $PY -m redteam.run_q --out $R/r14b/s$sr --seeds $sr --policies mix:doseF1.0:0.25 --attrib own -- ${=CELL} ${=W3} > $R/r14b/s$sr.log 2>&1 &
done
wait
touch $R/.r14b.done
