#!/bin/zsh
# The reviewer's four completing reads on §91 (November 10, 2026, night): the quarter reader at 1,000 ticks (the whole-run table: the leak over the tasks
# vested, the channel split, the seats by holder, the fees by seat kind, Ω's net) on run 42, the π^A-at-0.10 pin and arm 4 — the finals' models, seeds 21–40.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=results/redteam/stability/2.9.0-s82; A=results/redteam/stability/ablation-A1/learned; C=results/redteam/stability/learned-rev-careful-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
$PY $S/quarters.py --out $A --label arm4 --ticks 1000 --seeds 21-40 --direct-model $A/arm4/direct/models/direct-online-10.pt --model $A/arm4/wm/models/wm-online-10.pt --policies direct,greedy,hand,careful -- "${CELL[@]}" --arm 4 > $A/quarters-arm4.log 2>&1
$PY $S/quarters.py --out $A --label pa10 --ticks 1000 --seeds 21-40 --direct-model $A/pa10/direct/models/direct-online-10.pt --model $A/pa10/wm/models/wm-online-10.pt --policies direct,greedy,hand,careful -- "${CELL[@]}" --pi-a0 0.10 --pi-a-max 0.10 > $A/quarters-pa10.log 2>&1
$PY $S/quarters.py --out $S --label run42-1000 --ticks 1000 --seeds 21-40 --direct-model $C/direct/models/direct-online-10.pt --model $C/wm/models/wm-online-10.pt --policies direct,greedy,hand,careful -- "${CELL[@]}" > $S/quarters-run42-1000.log 2>&1
touch $S/.reads4.done
