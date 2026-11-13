#!/bin/zsh
# Addendum 10's J4 (November 13, 2026; notes §111): the member's audit seat under the stakes, read by the dose without training — at f9c0dbb3e (the harness as at
# 848e1d22c / b5961bf9f: run_q's `dose<q>audit` policy, the driver's per-slot readings; nothing changed for this read). Arm 0 with π^A held; the dosing slots
# 1 in 4 (`mix:dose<q>audit:0.25`) with the dose at the member's audit seat alone and the rest careful; a temptation of 1; the first review's bond as in §110's
# dose worlds (G_V of record; `--bond-mult-later` the later seats' multiple); the all-careful population (`careful`) beside each world on the same seeds;
# seeds 21–80 (61–80 free of any other use: no evaluation of record carries a seed above 60; the 0.1 dose worlds used 41–60). Six worlds:
#   w1  π^A 0.10, the later seats' bond ×1, the fee of record (w_audit 1.5), a dose of 0.3   — §110's world on sixty seeds
#   w2  the same with a dose of 1
#   w3  π^A 0.10, ×1, the fee doubled (--w-audit 3), a dose of 0.3
#   w4  π^A 0.30, ×1, the fee of record, a dose of 0.3
#   w5  π^A 0.30, ×1, the fee doubled, a dose of 0.3   — the stake table's one cell closed with no added stake
#   w6  π^A 0.20, ×4, the fee of record, a dose of 0.3
# Read by audit_stakes_read.py → audit-stakes-read.md. Run from agentic_sim/ in the elef-redteam env: launch.sh [parallel]
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/audit-stakes
PAR=${1:-8}
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1)
declare -A W
W[w1]="--pi-a0 0.10 --pi-a-max 0.10 --bond-mult-later 1 --w-audit 1.5"
W[w2]="--pi-a0 0.10 --pi-a-max 0.10 --bond-mult-later 1 --w-audit 1.5"
W[w3]="--pi-a0 0.10 --pi-a-max 0.10 --bond-mult-later 1 --w-audit 3"
W[w4]="--pi-a0 0.30 --pi-a-max 0.30 --bond-mult-later 1 --w-audit 1.5"
W[w5]="--pi-a0 0.30 --pi-a-max 0.30 --bond-mult-later 1 --w-audit 3"
W[w6]="--pi-a0 0.20 --pi-a-max 0.20 --bond-mult-later 4 --w-audit 1.5"
declare -A Q
Q[w1]=0.3; Q[w2]=1; Q[w3]=0.3; Q[w4]=0.3; Q[w5]=0.3; Q[w6]=0.3
n=0
for k in w1 w2 w3 w4 w5 w6; do
  $PY -m redteam.run_q --out $R/$k --seeds 21-80 --policies mix:dose${Q[$k]}audit:0.25,careful --attrib own -- "${CELL[@]}" ${=W[$k]} > $R/$k.log 2>&1 &
  n=$((n+1)); if [ $((n % PAR)) -eq 0 ]; then wait; fi
done
wait
touch $R/.done
