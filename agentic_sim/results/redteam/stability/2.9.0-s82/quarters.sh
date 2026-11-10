#!/bin/zsh
# D2: run 42's policies of record (the direct, the head alone) and the hand, frozen, in 2,000-tick runs on seeds 21–40, read by quarter (quarters.py).
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=results/redteam/stability/2.9.0-s82; C=results/redteam/stability/learned-rev-careful-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
$PY $S/quarters.py --out $S --label run42-2000 --ticks 2000 --seeds 21-40 --direct-model $C/direct/models/direct-online-10.pt --model $C/wm/models/wm-online-10.pt --policies direct,greedy,hand -- "${CELL[@]}"
touch $S/.quarters.done
