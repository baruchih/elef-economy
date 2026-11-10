#!/bin/zsh
# The third queue (November 10, 2026): 2.9.0 §8.7's m^A-at-1 cell (learned-rev-pafloor-290-own) after arm 2's chain — the last of the owed §8.7 cells,
# a different pin from the two launched first (π_t at its floor and at π_max). Run from agentic_sim/: queue3.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
A=$PWD/results/redteam/stability/ablation-A1
until [ -f $A/learned/arm2/chain.done ]; do sleep 600; done
zsh results/redteam/stability/learned-rev-pafloor-290-own/launch.sh all > results/redteam/stability/learned-rev-pafloor-290-own/chain.log 2>&1
