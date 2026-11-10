#!/bin/zsh
# The per-seat dial's path by period under the frozen policies of record (the reviewer's question after §88, November 10, 2026):
# run 42 (learned-rev-careful-290-own) and the liar chain (learned-rev-liars-290-own), the direct, the head alone and the hand, seeds 21–40.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=results/redteam/stability/2.9.0-s82
C=results/redteam/stability/learned-rev-careful-290-own
L=results/redteam/stability/learned-rev-liars-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
LIARS=(--dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1)
$PY $S/dial_path.py --out $S --label run42-quick --seeds 21-23 --direct-model $C/direct/models/direct-online-10.pt --policies direct -- "${CELL[@]}"
touch $S/.dial-quick.done
$PY $S/dial_path.py --out $S --label run42 --seeds 21-40 --direct-model $C/direct/models/direct-online-10.pt --model $C/wm/models/wm-online-10.pt --policies direct,greedy,hand -- "${CELL[@]}"
$PY $S/dial_path.py --out $S --label liars --seeds 21-40 --direct-model $L/direct/models/direct-online-10.pt --model $L/wm/models/wm-online-10.pt --policies direct,greedy,hand -- "${CELL[@]}" "${LIARS[@]}"
touch $S/.dial.done
