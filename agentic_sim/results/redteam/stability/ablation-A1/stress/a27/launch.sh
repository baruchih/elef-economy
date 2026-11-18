#!/bin/zsh
# Addendum 31 (November 18, 2026, evening; notes §126) — the harness at 29cffb7c7: two options off by default on Baruchi's agreed reads (`--real-miss-mark`, the mark for a miss on real
# work; `--second-filing`, the buyer's complaint on the ruled road), the per-slot ρ and marks, every first approval of a member's real delivery by who looked again (`ra_json`), the
# overhead's terms. Nothing drawn differently with the options off: world 3's all-careful and reads 38, 39 and 40 run again whole here for the new readings and checked to the key
# against a26/.
#   rerun/cw3-*: world 3's all-careful, seeds 21–120 (against a26/rerun/cw3).
#   rerun/r38-*, r39-*, r40-*: cell B (caseM0.2p0) on 1 in 4, 3 in 4 and every slot (against a26/r38, r39, r40).
#   r41/: cell B at a dose of 0.5 on real cases on 1 slot in 4 (caseM0.5p0), the rest careful.   r42/: at a dose of 1 (caseM1.0p0) on 1 slot in 4.
#   r43/: world 3's all-careful with the mark.   r44/: cell B on 1 in 4 with the mark.   r45/: cell B on every slot with the mark.
#   r46/: cell B on every slot with the requesters' truthful disputes at a detection of 1 and the second filing.   r46a/: the same without the second filing.
#   r47/: world 3's all-careful with the disputes and the second filing.
# Twenty-four processes at once (two seed halves a read). Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/a27
CELL="--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1"
W3="--arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5"
DISP="--dispute-policy truthful --dispute-rate 1.0"
JOBS=(
"rerun/cw3-s21-70 21-70 careful $W3"
"rerun/cw3-s71-120 71-120 careful $W3"
"rerun/r38-s21-70 21-70 mix:caseM0.2p0:0.25 $W3"
"rerun/r38-s71-120 71-120 mix:caseM0.2p0:0.25 $W3"
"rerun/r39-s21-70 21-70 mix:caseM0.2p0:0.75 $W3"
"rerun/r39-s71-120 71-120 mix:caseM0.2p0:0.75 $W3"
"rerun/r40-s21-70 21-70 mix:caseM0.2p0:1.0 $W3"
"rerun/r40-s71-120 71-120 mix:caseM0.2p0:1.0 $W3"
"r41/s21-70 21-70 mix:caseM0.5p0:0.25 $W3"
"r41/s71-120 71-120 mix:caseM0.5p0:0.25 $W3"
"r42/s21-70 21-70 mix:caseM1.0p0:0.25 $W3"
"r42/s71-120 71-120 mix:caseM1.0p0:0.25 $W3"
"r43/s21-70 21-70 careful $W3 --real-miss-mark on"
"r43/s71-120 71-120 careful $W3 --real-miss-mark on"
"r44/s21-70 21-70 mix:caseM0.2p0:0.25 $W3 --real-miss-mark on"
"r44/s71-120 71-120 mix:caseM0.2p0:0.25 $W3 --real-miss-mark on"
"r45/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 --real-miss-mark on"
"r45/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 --real-miss-mark on"
"r46/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $DISP --second-filing on"
"r46/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $DISP --second-filing on"
"r46a/s21-70 21-70 mix:caseM0.2p0:1.0 $W3 $DISP"
"r46a/s71-120 71-120 mix:caseM0.2p0:1.0 $W3 $DISP"
"r47/s21-70 21-70 careful $W3 $DISP --second-filing on"
"r47/s71-120 71-120 careful $W3 $DISP --second-filing on"
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
