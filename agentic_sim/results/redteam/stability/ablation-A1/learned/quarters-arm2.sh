#!/bin/zsh
# arm 2's quarter read at 1,000 ticks (the seats by holder, the fees by seat kind, Ω's net, the leak), as for arm 4 and the pin (notes §91's addendum)
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
S=results/redteam/stability/2.9.0-s82; A=results/redteam/stability/ablation-A1/learned
$PY $S/quarters.py --out $A --label arm2 --ticks 1000 --seeds 21-40 --model $A/arm2/wm/models/wm-online-10.pt --direct-model $A/arm2/direct/models/direct-online-10.pt --policies direct,greedy,hand,careful -- --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2 > $A/quarters-arm2.log 2>&1
touch $A/.qarm2.done
