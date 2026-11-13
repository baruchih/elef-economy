#!/bin/zsh
# The learner with a horizon's first chains (Baruchi's ruling of November 13, 2026; brief A1 addendum 10, J5; notes §111) at ffd23d851: §102's two cells — the pin
# (arm 0, π^A held at 0.10) and arm 4 (the small core), a temptation of 1 and the bond ×1 — with the decision's training target its slot's own return to the
# slot's exit at γ 0.98 (`--return-horizon mc --return-gamma 0.98`; the chains of record's shape otherwise: the four-action offline set — careful, eps4, random4 on
# seeds 1–20, the claimer and the stamper on 1–5 — collected again with the horizon's export, ten rounds of ε 0.1 uniform over the four actions, the direct the
# carrier and the world model under the head alone (reading reward + γ V(next)) beside, stride 4, the finals on seeds 21–40 with the careful, the stamper, the
# claimer and the hand on the same slots). Paired against the finals of record at stress/learned/{pa10,arm4}-t1-b1/ (the one-decision learners) by horizon_read.py.
# Run from agentic_sim/ in the elef-redteam env: launch.sh all
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/horizon/launch.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
H=$PWD/results/redteam/stability/ablation-A1/stress/learned/horizon
BASE=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
RET=(--return-horizon mc --return-gamma 0.98)
step=${1:-collect}
case $step in
  collect)
    for k in pa10 arm4; do X=$H/$k-t1-b1-mc; mkdir -p $X
      $PY -m redteam.collect --out $X/offline-main --seeds 1-20 --policies careful,eps4,random4 --attrib own -- "${BASE[@]}" ${=ARM[$k]} > $X/offline-main.log 2>&1 &
      $PY -m redteam.collect --out $X/offline-minor --seeds 1-5 --policies claimer,stamper --attrib own -- "${BASE[@]}" ${=ARM[$k]} > $X/offline-minor.log 2>&1 &
    done; wait
    for k in pa10 arm4; do X=$H/$k-t1-b1-mc; mkdir -p $X/direct-offline $X/wm-offline
      cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/direct-offline/; cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/wm-offline/; done ;;
  online)
    for k in pa10 arm4; do X=$H/$k-t1-b1-mc
      $PY -m redteam.online --data $X/direct-offline --models $X/direct/models --evals $X/direct/eval --rounds 10 --eps 0.1 --explore uniform --learner direct --eval-every 5 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own "${RET[@]}" -- "${BASE[@]}" ${=ARM[$k]} > $X/direct-online.log 2>&1 &
      $PY -m redteam.online --data $X/wm-offline --models $X/wm/models --evals $X/wm/eval --rounds 10 --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own "${RET[@]}" -- "${BASE[@]}" ${=ARM[$k]} > $X/wm-online.log 2>&1 &
    done; wait ;;
  final)
    for k in pa10 arm4; do X=$H/$k-t1-b1-mc
      $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,claimer,hand --attrib own -- "${BASE[@]}" ${=ARM[$k]} > $X/direct-final.log 2>&1 &
      $PY -m redteam.run_q --model $X/wm/models/wm-online-10.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,claimer,hand --horizon 16 --attrib own -- "${BASE[@]}" ${=ARM[$k]} > $X/wm-final.log 2>&1 &
    done; wait ;;
  all) $SELF collect && $SELF online && $SELF final && touch $H/chain.done ;;
esac
