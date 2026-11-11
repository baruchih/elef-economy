#!/bin/zsh
# The carried chain's quarter read (notes §94; November 11, 2026): the frozen policies of record of arm0-carried (round 20's direct and head alone) in a
# 1,000-tick run starting the four dials where round 20's runs ended (final-starts.txt — the finals' own starts), the careful and the hand at the same
# starts; the quarter's price, the leak by channel, the dials by close. Two calls, one per learner, each at its own start.
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
S=results/redteam/stability/2.9.0-s82; A=results/redteam/stability/ablation-A1/learned; X=$A/arm0-carried
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule"
DS=3.009180,13.600128,6.192114,1.037742
WS=2.598085,14.111864,6.329700,1.732815
( $PY $S/quarters.py --out $A --label arm0-carried-direct --ticks 1000 --seeds 21-40 --direct-model $X/direct/models/direct-online-20.pt --policies direct,careful,hand -- ${=CELL} --dial-start $DS > $A/quarters-arm0-carried-direct.log 2>&1; touch $A/.qcd.done ) &
( $PY $S/quarters.py --out $A --label arm0-carried-wm --ticks 1000 --seeds 21-40 --model $X/wm/models/wm-online-20.pt --policies greedy,careful -- ${=CELL} --dial-start $WS > $A/quarters-arm0-carried-wm.log 2>&1; touch $A/.qcw.done ) &
wait; touch $A/.qcarried.done
