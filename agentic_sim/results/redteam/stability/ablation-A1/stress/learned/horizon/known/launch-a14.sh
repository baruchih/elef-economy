#!/bin/zsh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
K=$PWD/results/redteam/stability/ablation-A1/stress/learned/horizon/known
/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python $K/addendum14_fits.py $K/addendum14-fits.md > $K/addendum14_fits.log 2>&1
touch $K/a14.done
