#!/bin/zsh
# Addendum 14's N4 (November 16, 2026; notes §113): a light skipper in the ruled design's nearest cell, read as the dose without training — at 7bd5dd5fc (the
# harness as at 25aab307e plus run_q's tallies by action; nothing drawn differently). The stressed world at a temptation of 1, the later seats' bond ×1, the first
# review's bond as in §110's dose worlds (G_V of record), the dosing slots 1 in 4 with the dose at every seat (`mix:dose<q>:0.25`) and the rest careful, the
# all-careful population (`careful`) beside each world on the same seeds. Six worlds:
#   w1  the pin (arm 0, π^A held at 0.10), the fee of record (w_audit 1.5), a dose of 0.1 — of record on seeds 21–60 (stress/dose/pa10-dose0.1); here seeds 61–120 added
#   w2  the pin, the audit seat's fee doubled (--w-audit 3), 0.1 — seeds 21–80
#   w3  arm 1 (the trusted ruling) with π^A held at 0.10, the fee of record, 0.1 — seeds 21–80
#   w4  arm 1 with π^A held at 0.10, the fee doubled, 0.1 — the ruled design's nearest cell — seeds 21–80
#   w5  world 4 with a dose of 0.3 — seeds 21–80 (run in the same calls as w4, its all-careful shared)
#   w6  arm 4, 0.1 — of record on seeds 21–60 (stress/dose/arm4-dose0.1); here seeds 61–120 added
# Seeds 81–120 are free of any other use (no evaluation of record carries a seed above 80). Read by n4_read.py → n4-read.md.
# Run from agentic_sim/ in the elef-redteam env: launch.sh
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/n4
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
PIN="--pi-a0 0.10 --pi-a-max 0.10"
$PY -m redteam.run_q --out $R/w1-s61-120 --seeds 61-120 --policies mix:dose0.1:0.25,careful --attrib own -- "${CELL[@]}" ${=PIN} --w-audit 1.5 > $R/w1-s61-120.log 2>&1 &
$PY -m redteam.run_q --out $R/w2 --seeds 21-80 --policies mix:dose0.1:0.25,careful --attrib own -- "${CELL[@]}" ${=PIN} --w-audit 3 > $R/w2.log 2>&1 &
$PY -m redteam.run_q --out $R/w3 --seeds 21-80 --policies mix:dose0.1:0.25,careful --attrib own -- "${CELL[@]}" --arm 1 ${=PIN} --w-audit 1.5 > $R/w3.log 2>&1 &
$PY -m redteam.run_q --out $R/w45-s21-50 --seeds 21-50 --policies mix:dose0.1:0.25,mix:dose0.3:0.25,careful --attrib own -- "${CELL[@]}" --arm 1 ${=PIN} --w-audit 3 > $R/w45-s21-50.log 2>&1 &
$PY -m redteam.run_q --out $R/w45-s51-80 --seeds 51-80 --policies mix:dose0.1:0.25,mix:dose0.3:0.25,careful --attrib own -- "${CELL[@]}" --arm 1 ${=PIN} --w-audit 3 > $R/w45-s51-80.log 2>&1 &
$PY -m redteam.run_q --out $R/w6-s61-120 --seeds 61-120 --policies mix:dose0.1:0.25,careful --attrib own -- "${CELL[@]}" --arm 4 > $R/w6-s61-120.log 2>&1 &
wait
touch $R/.done
