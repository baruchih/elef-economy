#!/bin/zsh
# Ablation brief A1 r2 §7.2 — the scripted populations at seeds 21–40 paired against arm 0: five cells (all-careful with arrivals, the 60/40
# entry cell, fixed 60/40, entry with truthful disputes, entry with liars at 0.1) under nine configurations — arm 0, arm 0 pinned at π^A 0.10
# and 0.20, arms 1, 1b (r 0.25), 1c, 2, 3, 4. 1,000 ticks; run from agentic_sim/ with the project's python3:
#   results/redteam/stability/ablation-A1/scripted/launch.sh [workers]        (one run: launch.sh one <cell> <arm> <seed>)
D=$PWD/results/redteam/stability/ablation-A1/scripted
declare -A CELL ARM
CELL[careful]="--entry-pool 20 --stampers 0"
CELL[entry60]="--entry-pool 20 --stampers 0.6"
CELL[fixed60]="--stampers 0.6"
CELL[disputes]="--entry-pool 20 --stampers 0.6 --dispute-policy truthful"
CELL[liars]="--entry-pool 20 --stampers 0.6 --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1"
ARM[arm0]=""
ARM[arm0-pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm0-pa20]="--pi-a0 0.20 --pi-a-max 0.20"
ARM[arm1]="--arm 1"
ARM[arm1b]="--arm 1b --sample-rate 0.25"
ARM[arm1c]="--arm 1c"
ARM[arm2]="--arm 2"
ARM[arm3]="--arm 3"
ARM[arm4]="--arm 4"
if [[ "$1" == one ]]; then
  cell=$2; arm=$3; seed=$4
  python3 -m drivers.stamping ${=CELL[$cell]} ${=ARM[$arm]} --seed $seed --name $cell-$arm-s$seed --results-root $D > $D/logs/$cell-$arm-s$seed.log 2>&1
  exit
fi
W=${1:-6}; mkdir -p $D/logs; SELF=$D/launch.sh
for cell in careful entry60 fixed60 disputes liars; do for arm in arm0 arm0-pa10 arm0-pa20 arm1 arm1b arm1c arm2 arm3 arm4; do for seed in {21..40}; do echo "$cell $arm $seed"; done; done; done \
  | xargs -P $W -n 3 $SELF one
echo done > $D/logs/.done
