#!/bin/zsh
# The resume (November 12, 2026). The chain's first pass crashed in run_q's reader, not in the engine or the driver: one episode in each learner's evaluation ended
# without an attribution (the world model's round-5 evaluation at seed 26, the direct's final at seed 25) and `pred_vs_realized` summed the missing values and
# raised; the reader now records such an episode (its `error` field) and reads the mean over the rest. The direct's ten rounds completed (direct-online-10.pt);
# its final re-runs whole. The world model's rounds 1–5 completed (wm-online-5.pt; the round-5 evaluation is re-run by run_q as online.py would have run it,
# the first pass's online log kept as online-log-rounds1-5.json), rounds 6–10 continue from wm-online-5.pt on the same collection (--first-round 6), then the final.
# Run from agentic_sim/ in the elef-redteam env: resume.sh all
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa20-t1-b6-gv20/resume.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa20-t1-b6-gv20
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20 --temptation 1 --gv 20 --bond-mult-later 1.5)
step=${1:-all}
case $step in
  direct-final)
    $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,claimer,hand --attrib own -- "${CELL[@]}" > $X/direct-final.log 2>&1 ;;
  wm-round5)
    $PY -m redteam.run_q --model $X/wm/models/wm-online-5.pt --out $X/wm/eval/round-5 --seeds 21-40 --policies greedy,careful --horizon 16 --hide "" --ticks 1000 --role reviewer --boundary-read auto -- "${CELL[@]}" > $X/wm-round5.log 2>&1 ;;
  wm-online)
    $PY -m redteam.online --data $X/wm-offline --models $X/wm/models --evals $X/wm/eval --first-round 6 --rounds 5 --start $X/wm/models/wm-online-5.pt --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own -- "${CELL[@]}" > $X/wm-online-resume.log 2>&1 ;;
  wm-final)
    $PY -m redteam.run_q --model $X/wm/models/wm-online-10.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,claimer,hand --horizon 16 --attrib own -- "${CELL[@]}" > $X/wm-final.log 2>&1 ;;
  all)
    $SELF direct-final &
    ( $SELF wm-round5; $SELF wm-online && $SELF wm-final ) &
    wait; touch $X/chain.done ;;
esac
