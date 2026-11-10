#!/bin/zsh
# Ablation brief A1 r2 §6/§7.1 — the payoff table first, with no learner: the scripted ε population (run 24's entry cell, every member a slot,
# ε 0.2 uniform around the careful) collected on own-name credit for arms 0 (the floor), 0 pinned at π^A 0.10 and 0.20, 1, 1b and 1c, seeds 1–20;
# the reader (payoff_table.py) gives own money by action and seat with the share of truth-checked bad cases at each seat beside. Run from
# agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/payoff
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
declare -A ARM
ARM[arm0]=""
ARM[arm0-pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm0-pa20]="--pi-a0 0.20 --pi-a-max 0.20"
ARM[arm1]="--arm 1"
ARM[arm1b]="--arm 1b --sample-rate 0.25"
ARM[arm1c]="--arm 1c"
for k in arm0 arm0-pa10 arm0-pa20 arm1 arm1b arm1c; do
  $PY -m redteam.collect --out $D/$k --seeds 1-20 --policies eps --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $D/$k.log 2>&1 &
done
wait
echo done > $D/.done
