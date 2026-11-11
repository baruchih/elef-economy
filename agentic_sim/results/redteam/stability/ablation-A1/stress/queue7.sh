#!/bin/zsh
# Addendum 7's queue (November 12, 2026; notes §104): F4.1 first (six run_q evaluations in parallel), F4.2's twelve payoff cells beside it; G2's twenty cells
# after F4.1 has finished (so the note that states the weight option reaches Baruchi before they run); then the table over every cell in payoff/.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=$PWD/results/redteam/stability/ablation-A1/stress
( $X/f41/launch.sh ) &
( $X/payoff2-launch.sh f42 4; until [ -f $X/f41/.done ]; do sleep 120; done; $X/payoff2-launch.sh g2 6 ) &
wait
python3 $X/payoff_stress.py $X/payoff $X/payoff/payoff-addendum7.md > $X/payoff/payoff-addendum7.log 2>&1
touch $X/.queue7.done
