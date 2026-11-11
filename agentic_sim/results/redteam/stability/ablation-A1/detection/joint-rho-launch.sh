#!/bin/zsh
# Addendum 6's F4.3 — the joint-verdict read at ρ 0.5 on the scripted populations (November 12, 2026; notes §107): §87's reader (the two panel seats' verdicts on
# the customers' truthful disputes against the product of the single seat's rate) with the shared difficulty at ρ 0.5 for the members, the troops and the
# ruling, on the careful and the hand (no model; "none"), at detections 0.25 and 0.1, seeds 21–40; the ρ 0 reads of record (§87, disputes-by-panel-d*.md) beside.
# Run from agentic_sim/ in the elef-redteam env: joint-rho-launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
D=$PWD/results/redteam/stability/ablation-A1/detection
RHO="--shared-difficulty 0.5 --shared-difficulty-troops 0.5 --shared-difficulty-ruling 0.5"
for r in 0.25 0.1; do
  nice $PY $D/disputes_by_panel.py $r none $D/joint-rho0.5-d$r.md 21-40 "$RHO" > $D/joint-rho0.5-d$r.log 2>&1 &
done
wait; touch $D/.joint-rho.done
