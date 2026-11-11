#!/bin/zsh
# Addendum 6's F4.2 — arm 4's learned chain at a temptation of 1 and the multiple the table says closes the first review by more than 1 real (November 12, 2026; notes §106):
# G_V ×2 (--gv 10; the later seats' multiple at 1), where the first review's claim edge reads −1.61 ± 0.31 under arm 4 (×4 −3.47). The recipe of §102 (as pa10-t1-b1/launch.sh).
# Engine: main at 8555fe991 and after. Run from agentic_sim/ in the elef-redteam env: launch.sh all
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/arm4-t1-b1-gv10/launch.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/arm4-t1-b1-gv10
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 4 --temptation 1 --gv 10 --bond-mult-later 1)
step=${1:-collect}
case $step in
  collect)
    $PY -m redteam.collect --out $X/offline-main --seeds 1-20 --policies careful,eps4,random4 --attrib own -- "${CELL[@]}" > $X/offline-main.log 2>&1 &
    $PY -m redteam.collect --out $X/offline-minor --seeds 1-5 --policies claimer,stamper --attrib own -- "${CELL[@]}" > $X/offline-minor.log 2>&1 &
    wait
    mkdir -p $X/direct-offline $X/wm-offline
    cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/direct-offline/; cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/wm-offline/ ;;
  online)
    $PY -m redteam.online --data $X/direct-offline --models $X/direct/models --evals $X/direct/eval --rounds 10 --eps 0.1 --explore uniform --learner direct --eval-every 5 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own -- "${CELL[@]}" > $X/direct-online.log 2>&1 &
    $PY -m redteam.online --data $X/wm-offline --models $X/wm/models --evals $X/wm/eval --rounds 10 --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own -- "${CELL[@]}" > $X/wm-online.log 2>&1 &
    wait ;;
  final)
    $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,claimer,hand --attrib own -- "${CELL[@]}" > $X/direct-final.log 2>&1 &
    $PY -m redteam.run_q --model $X/wm/models/wm-online-10.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,claimer,hand --horizon 16 --attrib own -- "${CELL[@]}" > $X/wm-final.log 2>&1 &
    wait ;;
  all) $SELF collect && $SELF online && $SELF final && touch $X/chain.done ;;
esac
