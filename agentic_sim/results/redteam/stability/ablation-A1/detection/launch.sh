#!/bin/zsh
# The reviewer's read (3) of November 10 (the watch item's second half, an evaluation ahead of the chains): run 42's final policy — the direct's
# round-10 model of learned-rev-careful-290-own — frozen, in a world where a requester notices bad work with probability 0.1 or 0.25
# (--dispute-policy truthful --dispute-rate r: the driver's per-case chance, 1.0 in the truthful-dispute cells of record), seeds 21–40, the
# scripted careful and the 60/40 hand on the same slots in the same worlds; the readings disputes filed / won by the dispute's truth, the
# standing false approvals, the leak, the court fees. Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/detection
M=results/redteam/stability/learned-rev-careful-290-own/direct/models/direct-online-10.pt
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful)
for r in 0.1 0.25; do
  $PY -m redteam.run_q --direct-model $M --out $D/frozen-d$r --seeds 21-40 --policies direct,careful,hand --attrib own -- "${CELL[@]}" --dispute-rate $r > $D/frozen-d$r.log 2>&1 &
done
wait
touch $D/.done
