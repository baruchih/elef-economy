#!/bin/zsh
# D2 (the reviewer's addendum 4, the word given): run 42's policies of record, frozen, in 2,000-tick runs on seeds 21–40 — the standard evaluation
# (the dial reader at 2,000 ticks runs beside it: dial_path_2000.sh); the quarter reader follows.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
C=results/redteam/stability/learned-rev-careful-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
$PY -m redteam.run_q --direct-model $C/direct/models/direct-online-10.pt --out $C/direct/eval/final-2000 --ticks 2000 --seeds 21-40 --policies direct,careful,hand --attrib own -- "${CELL[@]}" > $C/direct-final-2000.log 2>&1
$PY -m redteam.run_q --model $C/wm/models/wm-online-10.pt --out $C/wm/eval/final-2000 --ticks 2000 --seeds 21-40 --policies greedy,careful,hand --horizon 16 --attrib own -- "${CELL[@]}" > $C/wm-final-2000.log 2>&1
touch results/redteam/stability/2.9.0-s82/.frozen2000.done
