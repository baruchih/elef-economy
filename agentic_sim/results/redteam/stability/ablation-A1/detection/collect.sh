#!/bin/zsh
# The dispute panel's own actions in the two detection cells (the reviewer's note of November 10, after read (3)): one round of run 42's final
# policy (the direct's round-10 model, ε 0.1 uniform as the rounds were — the online driver's round 11 with its fit and eval unused) in each
# detection cell, seeds 1–20, so the panel's decisions can be split by the dispute's truth and owner; read by panel_by_truth.py.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/detection
X=results/redteam/stability/learned-rev-careful-290-own
for r in 0.1 0.25; do
  P=$D/collect-d$r; mkdir -p $P/data $P/models $P/evals
  cp $X/direct-offline/*.npz $P/data/; cp $X/direct/models/direct-online-10.pt $P/models/
  $PY -m redteam.online --data $P/data --models $P/models --evals $P/evals --start $P/models/direct-online-10.pt --first-round 11 --rounds 1 --eps 0.1 --explore uniform --learner direct --eval-every 100 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own -- --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate $r > $P/online11.log 2>&1 &
done
wait
touch $D/.collect-done
