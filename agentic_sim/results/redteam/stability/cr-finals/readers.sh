#!/bin/zsh
# The readers of record on the corrected episode (November 7, 2026; notes §77), after cr-finals/launch.sh: the channel split (fa_channels.py),
# the fee split (seat_income.py) and the liar chain's appeal-seat probe (appeal_tell.py) on the 2.9.0 chains (the current tree); the channel
# split on the 2.7.0 chains (the worktree at the provenance branch, the correction ported). Seeds 21–40, the models of record. Outputs here.
# Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
R=$PWD; S=$R/results/redteam/stability; T=$S/2.9.0-s82; O=$S/cr-finals
W=/private/tmp/claude-502/-Users-baruchi-admin-projects-elef-economy/eec13392-a9d7-4994-aec0-e91f71934505/scratchpad/wt-27/agentic_sim
SEEDS=$(seq 21 40 | paste -sd, -)
BASE="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule"
LIAR="$BASE --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1"
for c in careful stamper; do X=$S/learned-rev-$c-290-own
  $PY $T/fa_channels.py "$BASE" $SEEDS $X/direct/models/direct-online-10.pt $X/wm/models/wm-online-10.pt $O/fa-channels-$c-290-own-cr.md > $O/fa-channels-$c-290-own-cr.log 2>&1 &
  $PY $T/seat_income.py "$BASE" $SEEDS $X/direct/models/direct-online-10.pt $X/wm/models/wm-online-10.pt $O/seat-income-$c-290-own-cr.md > $O/seat-income-$c-290-own-cr.log 2>&1 &
done
Y=$S/learned-rev-liars-290-own
$PY $T/fa_channels.py "$LIAR" $SEEDS $Y/direct/models/direct-online-10.pt $Y/wm/models/wm-online-10.pt $O/fa-channels-liars-290-own-cr.md > $O/fa-channels-liars-290-own-cr.log 2>&1 &
$PY $T/seat_income.py "$LIAR" $SEEDS $Y/direct/models/direct-online-10.pt $Y/wm/models/wm-online-10.pt $O/seat-income-liars-290-own-cr.md > $O/seat-income-liars-290-own-cr.log 2>&1 &
$PY $T/appeal_tell.py "$LIAR" $SEEDS $Y/direct/models/direct-online-10.pt $O/appeal-tell-liars-290-own-cr-direct.npz > $O/appeal-tell-liars-290-own-cr-direct.txt 2>&1 &
( cd $W; for c in careful stamper; do Z=$S/learned-rev-$c-2-own; $PY $T/fa_channels.py "$BASE" $SEEDS $Z/direct/models/direct-online-10.pt $Z/wm/models/wm-online-10.pt $O/fa-channels-$c-2-own-cr.md > $O/fa-channels-$c-2-own-cr.log 2>&1 & done; wait ) &
wait
echo "readers done $(date)" > $O/readers.done
