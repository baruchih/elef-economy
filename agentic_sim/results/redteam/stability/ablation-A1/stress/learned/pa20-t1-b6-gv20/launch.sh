#!/bin/zsh
# Addendum 7's G3 — one learned chain on the pin at the cheapest cell of G2's table the audit seat's claim edge reads closed by more than 1 real (November 12, 2026; notes §106):
# π^A pinned at 0.20, the bond at the audit and panel seats 30 (×6 of the record's G_V 5, the cell's: −2.49 ± 0.44), the audit seat's weight of record 1.5, a temptation of 1,
# with the first review's bond at the multiple F4.2's table names as closing the first review by more than 1 real on the pin — ×4 (G_V 20: −3.77 ± 0.50; ×2 reads −0.99 ± 0.19,
# on the line) — so --gv 20 --bond-mult-later 1.5 (the later seats at 30, as the cell read them). The recipe of §102: the careful start on a four-action offline set
# (careful, eps4, random4 on seeds 1–20; the claimer and the stamper on 1–5), ten rounds of ε 0.1 uniform, the direct the carrier and the world model under the head
# alone beside, stride 4, the finals on seeds 21–40 with the careful, the stamper, the claimer and the hand on the same slots.
# Engine: main at 8555fe991 and after. Run from agentic_sim/ in the elef-redteam env: launch.sh all
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa20-t1-b6-gv20/launch.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa20-t1-b6-gv20
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20 --temptation 1 --gv 20 --bond-mult-later 1.5)
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
