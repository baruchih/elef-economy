#!/bin/zsh
# The horizon learners' claims by seat/standing/life (addendum 10's J5; November 13, 2026; notes §111). Run from agentic_sim/.
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
H=results/redteam/stability/ablation-A1/stress/learned/horizon
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
$PY $H/horizon_claims.py $H/horizon-claims.md > $H/claims.log 2>&1
touch $H/claims.done
