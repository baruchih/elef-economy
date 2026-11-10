#!/bin/zsh
# The reviewer's reads after §92 (November 10, 2026): (1) the quarter's price in the 2,000-tick run (quarters.py extended) under the head alone,
# the hand and the careful; (2) the frozen head-alone policy's attribution at the audit seat by the dial's level (audit_attrib.py).
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
S=results/redteam/stability/2.9.0-s82; C=results/redteam/stability/learned-rev-careful-290-own
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule"
rm -f $S/.reads92.done
( $PY $S/quarters.py --out $S --label run42-2000-price --ticks 2000 --seeds 21-40 --model $C/wm/models/wm-online-10.pt --policies greedy,hand,careful -- ${=CELL} > $S/quarters-run42-2000-price.log 2>&1; touch $S/.q92.done ) &
( $PY $S/audit_attrib.py --out $S/audit-attrib-run42-2000 --model $C/wm/models/wm-online-10.pt --seeds 21-40 --ticks 2000 -- ${=CELL} > $S/audit-attrib-run42-2000.log 2>&1; touch $S/.a92.done ) &
wait; touch $S/.reads92.done
