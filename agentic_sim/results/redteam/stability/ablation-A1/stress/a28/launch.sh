#!/bin/zsh
# Addendum 33 (November 18, 2026, late night; notes §127) — the harness at dc5b49896: two options off by default (`--troop-no-vote on`, Params.troop_audit_no_vote —
# the state's audit that differed is no vote of the court, the deciding verdict given afresh by two troop seats; `--seat-draw seats --draw-min K`, Params.troop_draw — the state's troops as
# candidates in the draw of an audit or panel seat up to a minimum K, a troop drawn seated at once on the troop seat's road), the deciding seats' error declared apart (`--eps-deciding`,
# equal to ε_T here), and the readings asked: the pool at a seat's first seating step and how it was filled (`seat_json`), the filed challenges' panels by holder and end (`dpanel_*` in
# `seats_by_kind_json`), the state's look by the draw apart (`statedrawn_*` in `ra_json`), the troops drawn by role. Nothing drawn differently with the options off: world 3's all-careful,
# read 35 (the seats drawn), read 46 and read 19 run again whole here for the new readings and checked to the key against a27/, a26/ and a19/.
#   rerun/cw3-*: world 3's all-careful (against a27/rerun/cw3).   rerun/r35-*: the seats drawn (against a26/r35).   rerun/r46-*: cell B on every slot, disputes at 1, the second filing (against a27/r46).
#   rerun/r19-*: conduct M (doseM0.2) on 1 in 4 (against a19/r19).
#   r48/: cell B (caseM0.2p0) on 1 in 4 with the disputes at a detection of 1 and the second filing.   r49/: cell B on every slot, disputes at 0.5, the second filing.   r50/: at 0.2.
#   r51/: world 3's all-careful with (i).   r52/: the all-careful with the seats drawn and (ii) at K = 3, (i) off.   r53/: the same with (i).   r54/: (i) and (ii) at K = 5.
#   r55/: cell B on every slot with the seats drawn, (i) and (ii) at K = 3.   r56/: conduct M (doseM0.2) on 1 in 4 with the seats drawn, (i) and (ii) at K = 3.
# Twenty-six processes at once (two seed halves a read). Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a28
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
DISP="--dispute-policy truthful --second-filing on"
NV="--troop-no-vote on"
DRAW="--seat-draw seats"
JOBS=(
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"rerun/r35-s21-70 21-70 careful $W3 $DRAW"
"rerun/r35-s71-120 71-120 careful $W3 $DRAW"
"rerun/r46-s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $DISP --dispute-rate 1.0"
"rerun/r46-s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $DISP --dispute-rate 1.0"
"rerun/r19-s21-70 21-70 mix:doseM0.2:0.25 $W3"
"rerun/r19-s71-120 71-120 mix:doseM0.2:0.25 $W3"
"r48/s21-70 21-70 mix:caseM0.2p0:0.25 $W3 $DISP --dispute-rate 1.0"
"r48/s71-120 71-120 mix:caseM0.2p0:0.25 $W3 $DISP --dispute-rate 1.0"
"r49/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $DISP --dispute-rate 0.5"
"r49/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $DISP --dispute-rate 0.5"
"r50/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $DISP --dispute-rate 0.2"
"r50/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $DISP --dispute-rate 0.2"
"r51/s21-70 21-70 careful $W3 $NV"
"r51/s71-120 71-120 careful $W3 $NV"
"r52/s21-70 21-70 careful $W3 $DRAW --draw-min 3"
"r52/s71-120 71-120 careful $W3 $DRAW --draw-min 3"
"r53/s21-70 21-70 careful $W3 $DRAW --draw-min 3 $NV"
"r53/s71-120 71-120 careful $W3 $DRAW --draw-min 3 $NV"
"r54/s21-70 21-70 careful $W3 $DRAW --draw-min 5 $NV"
"r54/s71-120 71-120 careful $W3 $DRAW --draw-min 5 $NV"
"r55/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $DRAW --draw-min 3 $NV"
"r55/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $DRAW --draw-min 3 $NV"
"r56/s21-70 21-70 mix:doseM0.2:0.25 $W3 $DRAW --draw-min 3 $NV"
"r56/s71-120 71-120 mix:doseM0.2:0.25 $W3 $DRAW --draw-min 3 $NV"
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
