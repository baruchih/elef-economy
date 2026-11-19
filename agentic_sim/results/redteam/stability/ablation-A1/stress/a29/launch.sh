#!/bin/zsh
# Addendum 34 (November 19, 2026; notes §128) — the harness at the commit this file names in a29-read.md: three options off by default — `--draw-wait on` ((v) the wait kept under a
# minimum: no troop drawn where no member is free, the draw at the first later step with one free, the pass's summons past w_R as today; the harness's alone), `--standby-pay on`
# (Params.standby_pay, (iv): a drawn seat's fixed fee to the members that stood in its draw at the seat's settlement, not to Ω), `--checker-rate q` (Params.checker_rate, (iii): the
# state's look on a coin over the approvals of a member's real root standing at the window's close with the challenge round unused; the look's cost the state's, no fee; differing,
# the deciding verdict afresh). With the three off nothing is drawn differently: world 3's all-careful and read 35 (the seats drawn) run again whole here and checked to the key
# against a28/rerun. Every read with (i) on (`--troop-no-vote on`).
#   rerun/cw3-*: world 3's all-careful (against a28/rerun/cw3).   rerun/r35-*: the seats drawn (against a28/rerun/r35).
#   r57/: the all-careful, seats drawn, K = 3, (v).   r58/: the same with (iv).   r59/: conduct M (doseM0.2) on 1 in 4, seats drawn, K = 3, (iv), no wait.   r60/: the same with (v).
#   r61/: cell B (caseM0.2p0) on every slot, seats drawn, K = 3, (v) and (iv).   r62/: cell B on every slot with (i) alone.   r63/: the all-careful with (iii) at 0.2.   r64/: cell B on every slot with (iii) at 0.2.
# Twenty processes at once (two seed halves a read). Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a29
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
NV="--troop-no-vote on"
K3="--seat-draw seats --draw-min 3"
JOBS=(
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"rerun/r35-s21-70 21-70 careful $W3 --seat-draw seats"
"rerun/r35-s71-120 71-120 careful $W3 --seat-draw seats"
"r57/s21-70 21-70 careful $W3 $NV $K3 --draw-wait on"
"r57/s71-120 71-120 careful $W3 $NV $K3 --draw-wait on"
"r58/s21-70 21-70 careful $W3 $NV $K3 --draw-wait on --standby-pay on"
"r58/s71-120 71-120 careful $W3 $NV $K3 --draw-wait on --standby-pay on"
"r59/s21-70 21-70 mix:doseM0.2:0.25 $W3 $NV $K3 --standby-pay on"
"r59/s71-120 71-120 mix:doseM0.2:0.25 $W3 $NV $K3 --standby-pay on"
"r60/s21-70 21-70 mix:doseM0.2:0.25 $W3 $NV $K3 --draw-wait on --standby-pay on"
"r60/s71-120 71-120 mix:doseM0.2:0.25 $W3 $NV $K3 --draw-wait on --standby-pay on"
"r61/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $NV $K3 --draw-wait on --standby-pay on"
"r61/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $NV $K3 --draw-wait on --standby-pay on"
"r62/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $NV"
"r62/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $NV"
"r63/s21-70 21-70 careful $W3 $NV --checker-rate 0.2"
"r63/s71-120 71-120 careful $W3 $NV --checker-rate 0.2"
"r64/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $NV --checker-rate 0.2"
"r64/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $NV --checker-rate 0.2"
)
run_one() {
  local out=$1 seeds=$2 pols=$3; shift 3
  mkdir -p $R/$(dirname $out)
  $PY -m redteam.run_q --out $R/$out --seeds $seeds --policies $pols --attrib own -- ${=CELL} "$@" > $R/$out.log 2>&1
}
for j in "${JOBS[@]}"; do
  set -- ${=j}; run_one "$@" &
done
wait
touch $R/.done
