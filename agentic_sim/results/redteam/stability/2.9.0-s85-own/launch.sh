#!/bin/zsh
# 2.9.0 §8.5 on the corrected engine, the rest (November 10, 2026; notes §89): the rc's own control — Q3's and Q4's policies of record under
# --rules 2.8.0 (eval-280cr) — and Q1's line of record (Q1/rearrive-280/models/wm-online-10.pt, the chain of §60) under 2.9.0 (eval-290cr) and
# under --rules 2.8.0 (eval-280cr), seeds 21–40, one process at a time, on the committed engine (763a7d5be). The first four evals (Q3's and
# Q4's policies under 2.9.0 and under --rules 2.7.0, eval-290cr / eval-270cr) were made by ablation-A1/queue.sh at the same commit; the
# pairing by pair_evals.py here. Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
Q=results/redteam
$PY -m redteam.run_q --model $Q/Q4/line-v4b/models/wm-online-10.pt --out $Q/Q4/line-v4b/eval-280cr --seeds 21-40 --policies greedy,learned,careful,collude --role pair --boundary-read one-step --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --rules 2.8.0 > $Q/Q4/line-v4b/eval-280cr.log 2>&1
$PY -m redteam.run_q --model $Q/Q3/line-v4/models/wm-online-10.pt --out $Q/Q3/line-v4/eval-280cr --seeds 21-40 --policies greedy,learned,careful,zero --role deliverer --boundary-read one-step --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --rules 2.8.0 > $Q/Q3/line-v4/eval-280cr.log 2>&1
$PY -m redteam.run_q --model $Q/Q1/rearrive-280/models/wm-online-10.pt --out $Q/Q1/rearrive-280/eval-290cr --seeds 21-40 --policies learned,greedy,careful,harvester,leaver --boundary-read learned --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --learner-rearrive on > $Q/Q1/rearrive-280/eval-290cr.log 2>&1
$PY -m redteam.run_q --model $Q/Q1/rearrive-280/models/wm-online-10.pt --out $Q/Q1/rearrive-280/eval-280cr --seeds 21-40 --policies learned,greedy,careful,harvester,leaver --boundary-read learned --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --learner-rearrive on --rules 2.8.0 > $Q/Q1/rearrive-280/eval-280cr.log 2>&1
touch results/redteam/stability/2.9.0-s85-own/.done
