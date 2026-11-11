#!/bin/zsh
# The retrained dispute cells of C5 (addendum 5 E3.4; November 11, 2026): run 42's final policies — learned-rev-careful-290-own's direct-online-10 /
# wm-online-10, the captured dispute panel the start — retrained in the world where a requester notices bad work with probability 0.1
# (--dispute-policy truthful --dispute-rate 0.1), ten further rounds 11–20 on run 42's offline set plus the chain's own collections (the carried
# chain's recipe without the dials carried), ε 0.1 uniform, stride 4, own-name credit; the final on seeds 21–40 with the careful, the stamper and the
# hand on the same slots. Read by the panel's make-up with the state's share of the panel seats beside the members' own rate (disputes_by_panel.py).
# Run from agentic_sim/ in the elef-redteam env: launch.sh all
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/detection/retrain-d0.1/launch.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/detection/retrain-d0.1
R=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.1)
step=${1:-online}
case $step in
  online)
    mkdir -p $X/direct-offline $X/wm-offline $X/direct/models $X/wm/models
    cp $R/direct-offline/*.npz $X/direct-offline/; cp $R/wm-offline/*.npz $X/wm-offline/
    $PY -m redteam.online --data $X/direct-offline --models $X/direct/models --evals $X/direct/eval --start $R/direct/models/direct-online-10.pt --first-round 11 --rounds 10 --eps 0.1 --explore uniform --learner direct --eval-every 5 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own -- "${CELL[@]}" > $X/direct-online.log 2>&1 &
    $PY -m redteam.online --data $X/wm-offline --models $X/wm/models --evals $X/wm/eval --start $R/wm/models/wm-online-10.pt --first-round 11 --rounds 10 --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own -- "${CELL[@]}" > $X/wm-online.log 2>&1 &
    wait ;;
  final)
    $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-20.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,hand --attrib own -- "${CELL[@]}" > $X/direct-final.log 2>&1 &
    $PY -m redteam.run_q --model $X/wm/models/wm-online-20.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,hand --horizon 16 --attrib own -- "${CELL[@]}" > $X/wm-final.log 2>&1 &
    wait
    $PY results/redteam/stability/ablation-A1/detection/disputes_by_panel.py 0.1 $X/direct/models/direct-online-20.pt $X/disputes-by-panel.md 21-40 > $X/disputes-by-panel.log 2>&1 ;;
  all) $SELF online && $SELF final && touch $X/chain.done ;;
esac
