#!/bin/zsh
# A1 r2 §4 — a default swept under the implementer's step 3, not an arm: the ruling's accuracy on arm 0 (0.95 and 1.0 against the 0.8 of
# the scripted sweep's arm 0), the five cells, seeds 21–40. Run from agentic_sim/: launch-ruling.sh [workers]
D=$PWD/results/redteam/stability/ablation-A1/scripted
declare -A CELL ARM
CELL[careful]="--entry-pool 20 --stampers 0"
CELL[entry60]="--entry-pool 20 --stampers 0.6"
CELL[fixed60]="--stampers 0.6"
CELL[disputes]="--entry-pool 20 --stampers 0.6 --dispute-policy truthful"
CELL[liars]="--entry-pool 20 --stampers 0.6 --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1"
ARM[arm0-r95]="--ruling-accuracy 0.95"
ARM[arm0-r100]="--ruling-accuracy 1.0"
if [[ "$1" == one ]]; then
  cell=$2; arm=$3; seed=$4
  python3 -m drivers.stamping ${=CELL[$cell]} ${=ARM[$arm]} --seed $seed --name $cell-$arm-s$seed --results-root $D > $D/logs/$cell-$arm-s$seed.log 2>&1
  exit
fi
W=${1:-6}; SELF=$D/launch-ruling.sh
for cell in careful entry60 fixed60 disputes liars; do for arm in arm0-r95 arm0-r100; do for seed in {21..40}; do echo "$cell $arm $seed"; done; done; done \
  | xargs -P $W -n 3 $SELF one
echo done > $D/logs/.done-ruling
