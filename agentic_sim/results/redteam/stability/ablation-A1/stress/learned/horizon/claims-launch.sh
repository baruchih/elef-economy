#!/bin/zsh
# The horizon learners' claims by seat/standing/life (addendum 10's J5; November 13, 2026; notes §111); run again on November 16, 2026 for addendum 13's M3.5 (the claim by
# quarter of the run's tick, the slots in place from tick 0 and the arrivals apart; the decisions kept) — the same rollouts (the policies of record carry no ε, the
# environment's draws are the seed's), written to horizon-claims-2.md with horizon-claims.md kept as the record of November 13. Run from agentic_sim/.
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
H=results/redteam/stability/ablation-A1/stress/learned/horizon
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
OUT=${1:-$H/horizon-claims-2.md}
$PY $H/horizon_claims.py $OUT > $H/claims-2.log 2>&1
touch $H/claims-2.done
