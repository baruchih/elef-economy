#!/bin/zsh
# §89's cause check (the reviewer's ask, November 10, 2026): Q4's line planner of record on the corrected engine at the OLD roll defaults
# (p_floor 0.2, the stood streak halving every 5 — Appendix A before November 6), under 2.8.0 and 2.7.0, seeds 21–40 paired —
# if the first seat's stamp and §58's loss return here, the consolidated roll defaults are what took them away.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
Q=results/redteam/Q4/line-v4b
for R in 2.8.0 2.7.0; do
  $PY -m redteam.run_q --model $Q/models/wm-online-10.pt --out $Q/eval-${R//./}cr-olddefaults --seeds 21-40 --policies greedy --role pair --boundary-read one-step --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --rules $R --p-floor 0.2 --p-halve-every 5 > $Q/eval-${R//./}cr-olddefaults.log 2>&1
done
touch results/redteam/stability/2.9.0-s85-own/.olddefaults.done
