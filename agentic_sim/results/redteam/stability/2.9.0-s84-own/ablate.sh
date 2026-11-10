#!/bin/zsh
# the carriers of the panel's and the appeal seat's gap (§8.4 on own money): the probe's per-field ablation at the panel kinds and the initial seat
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=results/redteam/stability
for chain in careful liars; do X=$S/learned-rev-$chain-290-own; P=$X/probe-seats
  for set in online11 eps; do for seat in initial audit panel appeal dispute; do
    $PY -m redteam.probe --data $P/data --model $X/wm/models/wm-online-10.pt --policies $set --seat $seat --ablate-case --out $P/probe-$set-$seat-abl.json > $P/probe-$set-$seat-abl.log 2>&1
  done; done
done
python3 $S/2.9.0-s84-own/readout.py > $S/2.9.0-s84-own/readout.log 2>&1
touch $S/2.9.0-s84-own/.abl.done
