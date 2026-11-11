#!/bin/zsh
# Addendum 5 E3.3 (November 11, 2026): arm 2's policies of record — the direct's and the head alone's round-10 models of ablation-A1/learned/arm2 —
# frozen in a world where a requester notices bad work with probability 0.1 or 0.25 (--dispute-policy truthful --dispute-rate r, §84's cells with
# --arm 2), seeds 21–40, the scripted careful and the 60/40 hand on the same slots; then the customers' truthful disputes won by the panel's make-up
# and the state's share of the panel seats by cause (disputes_by_panel.py with the cell's extra args) on the direct, as §86 read run 42's.
# Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/detection/arm2
A=results/redteam/stability/ablation-A1/learned/arm2
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2 --dispute-policy truthful)
for r in 0.1 0.25; do
  $PY -m redteam.run_q --direct-model $A/direct/models/direct-online-10.pt --out $D/frozen-d$r --seeds 21-40 --policies direct,careful,hand --attrib own -- "${CELL[@]}" --dispute-rate $r > $D/frozen-d$r.log 2>&1 &
  $PY -m redteam.run_q --model $A/wm/models/wm-online-10.pt --out $D/frozen-wm-d$r --seeds 21-40 --policies greedy,careful --horizon 16 --attrib own -- "${CELL[@]}" --dispute-rate $r > $D/frozen-wm-d$r.log 2>&1 &
done
wait
for r in 0.1 0.25; do
  $PY results/redteam/stability/ablation-A1/detection/disputes_by_panel.py $r $A/direct/models/direct-online-10.pt $D/disputes-by-panel-d$r.md 21-40 "--arm 2" > $D/disputes-by-panel-d$r.log 2>&1 &
done
wait
touch $D/.done
