#!/bin/zsh
# The queue behind the owed chains (November 10, 2026): when learned-rev-{pifloor,picap,half}-290-own have finished, the ablation's three learned
# chains (arm 0 pinned at 0.10, arm 1c, arm 4; careful starts) start together, and §8.5's lone learners are re-read on the corrected engine
# beside them — Q3's and Q4's trained policies of record under 2.9.0 (eval-290cr) and under --rules 2.7.0 (eval-270cr), seeds 21–40, one
# process at a time. When the scripted sweep has finished, the ruling's accuracy sweep follows it. Run from agentic_sim/: queue.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
A=$PWD/results/redteam/stability/ablation-A1
( until [ -f $A/scripted/logs/.done ]; do sleep 60; done
  zsh $A/scripted/launch-ruling.sh 6 > $A/scripted/launch-ruling.log 2>&1 ) &
( until [ -f results/redteam/stability/learned-rev-pifloor-290-own/chain.done ] && [ -f results/redteam/stability/learned-rev-picap-290-own/chain.done ] \
        && [ -f results/redteam/stability/learned-rev-half-290-own/chain.done ]; do sleep 120; done
  for k in pa10 arm1c arm4; do (zsh $A/learned/$k/launch.sh all > $A/learned/$k/chain.log 2>&1 &); done
  Q=results/redteam
  $PY -m redteam.run_q --model $Q/Q3/line-v4/models/wm-online-10.pt --out $Q/Q3/line-v4/eval-290cr --seeds 21-40 --policies greedy,learned,careful,zero --role deliverer --boundary-read one-step --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 > $Q/Q3/line-v4/eval-290cr.log 2>&1
  $PY -m redteam.run_q --model $Q/Q3/line-v4/models/wm-online-10.pt --out $Q/Q3/line-v4/eval-270cr --seeds 21-40 --policies greedy,learned,careful,zero --role deliverer --boundary-read one-step --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --rules 2.7.0 > $Q/Q3/line-v4/eval-270cr.log 2>&1
  $PY -m redteam.run_q --model $Q/Q4/line-v4b/models/wm-online-10.pt --out $Q/Q4/line-v4b/eval-290cr --seeds 21-40 --policies greedy,learned,careful,collude --role pair --boundary-read one-step --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 > $Q/Q4/line-v4b/eval-290cr.log 2>&1
  $PY -m redteam.run_q --model $Q/Q4/line-v4b/models/wm-online-10.pt --out $Q/Q4/line-v4b/eval-270cr --seeds 21-40 --policies greedy,learned,careful,collude --role pair --boundary-read one-step --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --rules 2.7.0 > $Q/Q4/line-v4b/eval-270cr.log 2>&1
  touch $A/s85.done ) &
wait
