#!/bin/zsh
# Addendum 12's L3.2 (November 13, 2026; notes §111) at 2d74cf21d: what an admission costs and pays — the all-careful population (the 'careful' policy on every slot) in the
# stressed world's two cells (the pin and arm 4, a temptation of 1, the bond ×1), seeds 21–40, with the driver's snapshot of each arrival-born slot's Tally at its
# admission (adm_* in the per-slot export); read by admission_read.py → admission-read.md. The same worlds as §110's dose worlds' all-careful population (every
# figure of record identical). Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
A=$PWD/results/redteam/stability/ablation-A1/stress/admission
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
$PY -m redteam.run_q --out $A/pa10-careful --seeds 21-40 --policies careful --attrib own -- "${CELL[@]}" --pi-a0 0.10 --pi-a-max 0.10 > $A/pa10-careful.log 2>&1 &
$PY -m redteam.run_q --out $A/arm4-careful --seeds 21-40 --policies careful --attrib own -- "${CELL[@]}" --arm 4 > $A/arm4-careful.log 2>&1 &
wait
touch $A/.done
