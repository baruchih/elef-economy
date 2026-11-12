#!/bin/zsh
# Addendum 8's entry test (H3.1; November 13, 2026; notes §109): F4.1's construction with the claiming slots at 1 in 10, 1 in 4 and 3 in 4 of the population
# (F4.1 read 1 in 2) — frozen policies, no training. On the pin and on arm 4 at a temptation of 1 and the bond ×1, §102's policies of record (the stressed
# chains' round-10 models, direct and head alone), seeds 21–40, run_q's `mix:<policy>:<share>` — the share a reader-side option (the wrapper of record drew
# halves; the same stable hash of the seed and the slot's name read against the share, arrivals included, so at 0.5 the halves are F4.1's to the name).
# Read by group as in §105 (the `half_claim_*` / `half_care_*` keys). Run from agentic_sim/ in the elef-redteam env: launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress
PAR=${1:-6}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
n=0
for s in 0.1 0.25 0.75; do for k in pa10 arm4; do
  L=$R/learned/$k-t1-b1
  $PY -m redteam.run_q --direct-model $L/direct/models/direct-online-10.pt --out $R/entry/$k-direct-s$s --seeds 21-40 --policies mix:direct:$s --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/entry/$k-direct-s$s.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
  $PY -m redteam.run_q --model $L/wm/models/wm-online-10.pt --out $R/entry/$k-wm-s$s --seeds 21-40 --policies mix:greedy:$s --horizon 16 --attrib own -- "${CELL[@]}" ${=ARM[$k]} > $R/entry/$k-wm-s$s.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
done; done
wait
touch $R/entry/.done
