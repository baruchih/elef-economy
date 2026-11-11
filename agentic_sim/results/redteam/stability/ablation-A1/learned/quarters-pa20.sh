#!/bin/zsh
# the 0.20 pin's quarter read at 1,000 ticks (the seats by holder, the fees by seat kind, Ω's net, the leak per bad delivery), as for the 0.10 pin, arm 4 and arm 2 (notes §91's addendum, §93); addendum 5 E3.1
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
S=results/redteam/stability/2.9.0-s82; A=results/redteam/stability/ablation-A1/learned
$PY $S/quarters.py --out $A --label pa20 --ticks 1000 --seeds 21-40 --model $A/pa20/wm/models/wm-online-10.pt --direct-model $A/pa20/direct/models/direct-online-10.pt --policies direct,greedy,hand,careful -- --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20 > $A/quarters-pa20.log 2>&1
touch $A/.qpa20.done
