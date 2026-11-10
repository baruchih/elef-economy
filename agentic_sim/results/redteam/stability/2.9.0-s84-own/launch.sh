#!/bin/zsh
# 2.9.0 §8.4 on own-name credit at the corrected engine (the owed cells, November 10, 2026): Q2's probe at every seat on the learned populations'
# collections — run 42's careful basin (learned-rev-careful-290-own) and the liar chain (learned-rev-liars-290-own): one round of the population
# under the direct's round-10 policy (online11: redteam.online's round 11 without its use — the collection is the point; ε 0.1 uniform as the
# rounds were), the same cell's hand-written ε set as the floor, the probe (redteam.probe --seat) on the world model's latent of record per
# seat kind. Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=results/redteam/stability
declare -A CELL
CELL[careful]="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule"
CELL[liars]="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1"
for chain in careful liars; do
  X=$S/learned-rev-$chain-290-own; P=$X/probe-seats
  mkdir -p $P/data $P/models $P/evals
  cp $X/direct-offline/*.npz $P/data/; cp $X/direct/models/direct-online-10.pt $P/models/
  $PY -m redteam.online --data $P/data --models $P/models --evals $P/evals --first-round 11 --rounds 1 --eps 0.1 --explore uniform --learner direct --eval-every 100 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own -- ${=CELL[$chain]} > $P/online11.log 2>&1
  for set in online11 eps; do for seat in all initial audit panel appeal dispute resumed; do
    $PY -m redteam.probe --data $P/data --model $X/wm/models/wm-online-10.pt --policies $set --seat $seat --out $P/probe-$set-$seat.json > $P/probe-$set-$seat.log 2>&1
  done; done
done
python3 $S/2.9.0-s84-own/readout.py > $S/2.9.0-s84-own/readout.log 2>&1
touch $S/2.9.0-s84-own/.done
