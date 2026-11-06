#!/bin/zsh
# 2.9.0 §8.3 / §8.6 on the corrected engine at the roll's new defaults (the economy reviewer's fourth ruling, November 6, 2026; notes §74–§75):
# the four honest populations by hand (§56's cells) at seeds 21–40, four arms each on the identical seeds —
#   new    2.9.0 (both flags on) at the new defaults   (p_floor 0.5, the halving window 20 — Appendix A from faf968aa4)
#   old    2.9.0 at the old defaults                   (--p-floor 0.2 --p-halve-every 5)
#   280    --rules 2.8.0 at the new defaults
#   280old --rules 2.8.0 at the old defaults           (§56's 2.8.0 arm, re-run on the corrected engine)
# so new − old is the defaults' cost under 2.9.0 (the ruling's condition), 280 − 280old the same under 2.8.0, new − 280 is 2.9.0 against
# 2.8.0 at the new defaults and old − 280old at the old (the rc's §8.3 as written). 1,000 ticks; run from agentic_sim/ with the project's python3:
#   results/redteam/stability/2.9.0-s83/launch.sh [workers]        (one run: launch.sh one <cell> <arm> <seed>)
D=$PWD/results/redteam/stability/2.9.0-s83
declare -A CELL ARM
CELL[entry60]="--entry-pool 20 --stampers 0.6"
CELL[fixed60]="--stampers 0.6"
CELL[careful]="--entry-pool 20 --stampers 0"
CELL[disputes]="--entry-pool 20 --stampers 0.6 --dispute-policy truthful"
ARM[new]="--p-floor 0.5 --p-halve-every 20"
ARM[old]="--p-floor 0.2 --p-halve-every 5"
ARM[280]="--rules 2.8.0 --p-floor 0.5 --p-halve-every 20"
ARM[280old]="--rules 2.8.0 --p-floor 0.2 --p-halve-every 5"
if [[ "$1" == one ]]; then
  cell=$2; arm=$3; seed=$4
  python3 -m drivers.stamping ${=CELL[$cell]} ${=ARM[$arm]} --seed $seed --name $cell-$arm-s$seed --results-root $D > $D/logs/$cell-$arm-s$seed.log 2>&1
  exit
fi
W=${1:-6}; mkdir -p $D/logs; SELF=$D/launch.sh
for cell in entry60 fixed60 careful disputes; do for arm in new old 280 280old; do for seed in {21..40}; do echo "$cell $arm $seed"; done; done; done \
  | xargs -P $W -n 3 $SELF one
echo done > $D/logs/.done
