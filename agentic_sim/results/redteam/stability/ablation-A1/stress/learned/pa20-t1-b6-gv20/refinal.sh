#!/bin/zsh
# The finals again on the corrected reader (November 12, 2026; 30f280474). The resumed chain's finals and the world model's round-5 evaluation each carried
# an episode that ended in the driver's error — the stage table's row for the first period (a planted approval's stages filed there with no seated count;
# the stamper reference at seed 26 in both finals, the greedy at seeds 26, 36, 40 in the round-5 evaluation). The driver's stage table now skips the
# planted approval at closure; the policies, the models and the worlds are unchanged, so every other episode reproduces the first pass to the decimal.
# The errored evaluations are kept beside as final-at-7394be48b/ and round-5-at-7394be48b/. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa20-t1-b6-gv20
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20 --temptation 1 --gv 20 --bond-mult-later 1.5)
$PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,claimer,hand --attrib own -- "${CELL[@]}" > $X/direct-final-2.log 2>&1 &
$PY -m redteam.run_q --model $X/wm/models/wm-online-10.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,claimer,hand --horizon 16 --attrib own -- "${CELL[@]}" > $X/wm-final-2.log 2>&1 &
$PY -m redteam.run_q --model $X/wm/models/wm-online-5.pt --out $X/wm/eval/round-5 --seeds 21-40 --policies greedy,careful --horizon 16 --hide "" --ticks 1000 --role reviewer --boundary-read auto -- "${CELL[@]}" > $X/wm-round5-2.log 2>&1 &
wait; touch $X/refinal.done
