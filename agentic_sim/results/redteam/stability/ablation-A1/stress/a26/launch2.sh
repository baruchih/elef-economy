#!/bin/zsh
# Addendum 30 (November 18, 2026; notes §125) — the harness at a4fc4f6c4: world 3's all-careful run again whole (seeds 21–120) for the row's new readings (the dial's level over the periods, the free
# panel-eligible members at the audit pick), beside reads 38–40 — checked to the digit against a25/rerun/cw3 before it is read (nothing drawn differently with the options off). Two processes.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a26
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
for seeds in 21-70 71-120; do
  $PY -m redteam.run_q --out $R/rerun/cw3-s$seeds --seeds $seeds --policies careful --attrib own -- ${=CELL} ${=W3} > $R/rerun/cw3-s$seeds.log 2>&1 &
done
wait
touch $R/.done2
