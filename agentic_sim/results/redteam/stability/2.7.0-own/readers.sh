#!/bin/zsh
# The readers on the four own-name chains' finals (notes §73): the channel split, the fee split and the appeal-seat probe on the 2.9.0 chains
# (the current tree), the channel split on the 2.7.0 chains (the worktree at 8b26ebf6 — the readers run there against the 2.7.0 engine and the
# models trained on it). Seeds 21–40, the finals' models. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
R=$PWD; S=$R/results/redteam/stability; T=$S/2.9.0-s82; O=$S/2.7.0-own
W=/private/tmp/claude-502/-Users-baruchi-admin-projects-elef-economy/eec13392-a9d7-4994-aec0-e91f71934505/scratchpad/wt-27/agentic_sim
SEEDS=$(seq 21 40 | paste -sd, -)
BASE="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule"
LIAR="$BASE --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1"
X=$S/learned-rev-stamper-290-own; Y=$S/learned-rev-liars-290-own
$PY $T/fa_channels.py "$BASE" $SEEDS $X/direct/models/direct-online-10.pt $X/wm/models/wm-online-10.pt $T/fa-channels-stamper-290-own.md > $T/fa-channels-stamper-290-own.log 2>&1 &
$PY $T/fa_channels.py "$LIAR" $SEEDS $Y/direct/models/direct-online-10.pt $Y/wm/models/wm-online-10.pt $T/fa-channels-liars-290-own.md > $T/fa-channels-liars-290-own.log 2>&1 &
$PY $T/seat_income.py "$BASE" $SEEDS $X/direct/models/direct-online-10.pt $X/wm/models/wm-online-10.pt $T/seat-income-stamper-290-own.md > $T/seat-income-stamper-290-own.log 2>&1 &
$PY $T/seat_income.py "$LIAR" $SEEDS $Y/direct/models/direct-online-10.pt $Y/wm/models/wm-online-10.pt $T/seat-income-liars-290-own.md > $T/seat-income-liars-290-own.log 2>&1 &
$PY $T/appeal_tell.py "$LIAR" $SEEDS $Y/direct/models/direct-online-10.pt $T/appeal-tell-liars-290-own-direct.npz > $T/appeal-tell-liars-290-own-direct.txt 2>&1 &
( cd $W; for c in careful stamper; do Z=$S/learned-rev-$c-2-own; $PY $T/fa_channels.py "$BASE" $SEEDS $Z/direct/models/direct-online-10.pt $Z/wm/models/wm-online-10.pt $O/fa-channels-$c-2-own.md > $O/fa-channels-$c-2-own.log 2>&1 & done; wait ) &
wait
