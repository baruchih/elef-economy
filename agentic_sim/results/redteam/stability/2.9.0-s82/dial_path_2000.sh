#!/bin/zsh
# The cheapest direct read of the dial's climb (named in §88's addendum 2): run 42's frozen policies of record in a 2,000-tick run — ten closes — the dial read per period.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=results/redteam/stability/2.9.0-s82; C=results/redteam/stability/learned-rev-careful-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
$PY $S/dial_path.py --out $S --label run42-2000 --ticks 2000 --seeds 21-40 --direct-model $C/direct/models/direct-online-10.pt --model $C/wm/models/wm-online-10.pt --policies direct,greedy,hand -- "${CELL[@]}"
touch $S/.dial2000.done
