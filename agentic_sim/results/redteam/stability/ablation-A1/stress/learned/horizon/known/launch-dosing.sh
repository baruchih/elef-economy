#!/bin/zsh
# Addendum 13's M3.4 (November 16, 2026): the known-answer fits on the dosing slots alone (known_dosing.py → known-dosing.md). Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/learned/horizon/known
$PY $R/known_dosing.py $R/known-dosing.md > $R/known_dosing.log 2>&1
touch $R/.dosing.done
