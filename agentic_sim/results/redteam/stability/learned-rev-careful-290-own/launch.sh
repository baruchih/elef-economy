#!/bin/zsh
# The retrain of the careful basin at 2.9.0 on own-name credit (the economy reviewer's ruling of November 6, 2026, Q2's third step): the
# chain of record's recipe (learned-rev-careful-290b: the careful-weighted offline set — careful, ε, random on seeds 1–20, the stamper on
# 1–5 — ten rounds of ε 0.1 uniform exploration on the training seeds, the direct the carrier and the world model under the head alone
# beside, stride 4 on per-slot windows, the finals on seeds 21–40 with the careful, the stamper and the hand on the same slots), the one
# change `--attrib own` (the default from this commit; the chain of record trained on `pooled`). Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
X=results/redteam/stability/learned-rev-careful-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
step=${1:-collect}
case $step in
  collect)
    $PY -m redteam.collect --out $X/offline-main --seeds 1-20 --policies careful,eps,random --attrib own -- "${CELL[@]}" > $X/offline-main.log 2>&1 &
    $PY -m redteam.collect --out $X/offline-minor --seeds 1-5 --policies stamper --attrib own -- "${CELL[@]}" > $X/offline-minor.log 2>&1 &
    wait
    mkdir -p $X/direct-offline $X/wm-offline
    cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/direct-offline/; cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/wm-offline/ ;;
  online)
    $PY -m redteam.online --data $X/direct-offline --models $X/direct/models --evals $X/direct/eval --rounds 10 --eps 0.1 --explore uniform --learner direct --eval-every 5 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own -- "${CELL[@]}" > $X/direct-online.log 2>&1 &
    $PY -m redteam.online --data $X/wm-offline --models $X/wm/models --evals $X/wm/eval --rounds 10 --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own -- "${CELL[@]}" > $X/wm-online.log 2>&1 &
    wait ;;
  final)
    $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,hand --attrib own -- "${CELL[@]}" > $X/direct-final.log 2>&1 &
    $PY -m redteam.run_q --model $X/wm/models/wm-online-10.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,hand --horizon 16 --attrib own -- "${CELL[@]}" > $X/wm-final.log 2>&1 &
    wait ;;
esac
