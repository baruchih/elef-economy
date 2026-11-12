#!/bin/zsh
# The provenance re-read's pairings (November 13, 2026): every pairing of record on the corrected engine that prints the plant kind's state-seat stage
# ("state seats per plant", the period-matched stage table's state seats) is produced again by finals-paired.py over the re-read evaluations
# (<eval>-at-30f280474/), into <pairing>-at-30f280474.md beside the pairing of record; restage_read.py diffs the two. Where one side of a pairing is
# an evaluation made before the corrected emission (the macOS episode, §77), that side stays the evaluation of record and the listing says so.
# Run from agentic_sim/ after restage.sh: restage_pair.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
S=$PWD/results/redteam/stability
A=-at-30f280474
P="python3 $S/2.9.0-s82/finals-paired.py"
L=$S/ablation-A1/learned; T=$S/ablation-A1/stress/learned; D=$S/ablation-A1/detection
pair() {   # out, cell(s) ... with the env set by the caller
  "$@"
}
# A. the ablation chains against run 42 (base learned-rev-careful-290-own, final-cr)
for c in pa10:"pa10" arm1c:"arm1c" arm2:"arm2" arm4:"arm4" arm0-carried:"arm 0 carried" pa10-stamper-run42:"pin stamper start" arm2-stamper-run42:"arm 2, the stamper start" arm4-stamper-run42:"arm 4 stamper start" pa20-run42:"π^A pinned at 0.20"; do
  f=${c%%:*}; tag=${c#*:}; cell=${f%-run42}
  SUF290="" BASESUF="-290-own" FINAL=final$A BASEFINAL=final-cr$A TAG290="$tag" TAGBASE="run 42 (arm 0)" BASECELL="ablation-A1/learned/${cell}:careful" ${=P} $L/finals-paired-$f$A.md ablation-A1/learned/$cell > $L/finals-paired-$f$A.log 2>&1
done
# B. cell against cell under ablation-A1/learned
for c in pa20:pa10:"π^A pinned at 0.20":"π^A pinned at 0.10" pa10-stamper:pa10:"pin stamper start":"pin careful start" arm2-stamper:arm2:"arm 2, the stamper start":"arm 2, the careful start" arm4-stamper:arm4:"arm 4 stamper start":"arm 4 careful start"; do
  IFS=: read f b tag tagb <<< "$c"
  SUF290="" BASESUF="" FINAL=final$A BASEFINAL=final$A TAG290="$tag" TAGBASE="$tagb" BASECELL="ablation-A1/learned/${f}:ablation-A1/learned/${b}" ${=P} $L/finals-paired-$f$A.md ablation-A1/learned/$f > $L/finals-paired-$f$A.log 2>&1
done
# C. the stressed chains
st() { f=$1; cell=$2; base=$3; tag=$4; tagb=$5
  SUF290="" BASESUF="" FINAL=final$A BASEFINAL=final$A TAG290="$tag" TAGBASE="$tagb" BASECELL="${cell}:${base}" ${=P} $T/finals-paired-$f$A.md $cell > $T/finals-paired-$f$A.log 2>&1; }
st pa10-t1-b1 ablation-A1/stress/learned/pa10-t1-b1 ablation-A1/learned/pa10 "the 0.10 pin, stressed (x 1, bond x1)" "the 0.10 pin, unstressed"
st arm2-t1-b1 ablation-A1/stress/learned/arm2-t1-b1 ablation-A1/learned/arm2 "arm 2, stressed (x 1, bond x1)" "arm 2, unstressed"
st arm4-t1-b1 ablation-A1/stress/learned/arm4-t1-b1 ablation-A1/learned/arm4 "arm 4, stressed (x 1, bond x1)" "arm 4, unstressed"
st arm4-t1-b1-gv10 ablation-A1/stress/learned/arm4-t1-b1-gv10 ablation-A1/stress/learned/arm4-t1-b1 "arm 4, G_V ×2 (t 1)" "arm 4, stressed G_V ×1 (t 1)"
st arm4-t1-b1-gv10-unstressed ablation-A1/stress/learned/arm4-t1-b1-gv10 ablation-A1/learned/arm4 "arm 4, G_V ×2 (t 1)" "arm 4, unstressed"
st pa20-t1-b6-gv20 ablation-A1/stress/learned/pa20-t1-b6-gv20 ablation-A1/learned/pa20 "G3: pa 0.20, G_V 20, bond x1.5 (x6 of 5), t1" "unstressed 0.20 pin"
st pa20-t1-b6-gv20-stressed ablation-A1/stress/learned/pa20-t1-b6-gv20 ablation-A1/stress/learned/pa10-t1-b1 "G3: pa 0.20, G_V 20, bond x1.5 (x6 of 5), t1" "stressed 0.10 pin, bond x1, t1"
# D. the detection cells: the retrained chains against run 42's policies frozen in the same cell, through a mirror of the frozen cell's layout
M=/private/tmp/claude-502/-Users-baruchi-admin-projects-elef-economy/eec13392-a9d7-4994-aec0-e91f71934505/scratchpad/restage-mirror
for d in 0.25 0.1; do
  for l in direct wm; do
    src=$D/frozen$( [ $l = wm ] && echo -wm )-d$d
    mkdir -p $M/frozen-d$d/$l/eval; ln -sfn $src $M/frozen-d$d/$l/eval/final; ln -sfn $src$A $M/frozen-d$d/$l/eval/final$A
  done
  mkdir -p $S/ablation-A1/detection/mirror-tmp; ln -sfn $M/frozen-d$d $S/ablation-A1/detection/mirror-tmp/frozen-d$d
  SUF290="" BASESUF="" FINAL=final$A BASEFINAL=final$A TAG290="C5 retrained at $d" TAGBASE="run 42's policies frozen at $d" BASECELL="ablation-A1/detection/retrain-d${d}:ablation-A1/detection/mirror-tmp/frozen-d${d}" ${=P} $D/retrain-d$d/finals-paired-vs-frozen$A.md ablation-A1/detection/retrain-d$d > $D/retrain-d$d/finals-paired-vs-frozen$A.log 2>&1
done
rm -rf $S/ablation-A1/detection/mirror-tmp
# E. 2.9.0-s87-own: the pins and the half against run 42 (both sides on the corrected engine)
O=$S/2.9.0-s87-own
SUF290="-290-own" BASESUF="-290-own" FINAL=final$A BASEFINAL=final-cr$A TAG290="pinned" TAGBASE="run 42" BASECELL="pifloor:careful,picap:careful" ${=P} $O/finals-paired-pins$A.md pifloor picap > $O/finals-paired-pins$A.log 2>&1
SUF290="-290-own" BASESUF="-290-own" FINAL=final$A BASEFINAL=final-cr$A TAG290="the half" TAGBASE="run 42 (all)" BASECELL="half:careful" ${=P} $O/finals-paired-half-vs-run42$A.md half > $O/finals-paired-half-vs-run42$A.log 2>&1
# the half against run 41 (-290, the old engine: the base side stays the evaluation of record)
SUF290="-290-own" BASESUF="-290" FINAL=final$A BASEFINAL=final TAG290="own money" TAGBASE="run 41" ${=P} $O/finals-paired-half$A.md half > $O/finals-paired-half$A.log 2>&1
# F. cr-finals: 2.9.0 (final-cr, re-read) against 2.7.0 (unaffected, as of record); the seam pairings' corrected side re-read against the macOS side of record
C=$S/cr-finals
SUF290="-290-own" BASESUF="-2-own" FINAL=final-cr$A BASEFINAL=final-cr TAG290="2.9.0" TAGBASE="2.7.0" ${=P} $C/paired-290-vs-270-own-cr$A.md careful stamper > $C/paired-290-vs-270-own-cr$A.log 2>&1
SUF290="-290-own" BASESUF="-290-own" FINAL=final-cr$A BASEFINAL=final TAG290="corrected" TAGBASE="macOS" ${=P} $C/seam-290-own$A.md careful liars stamper > $C/seam-290-own$A.log 2>&1
touch $S/2.9.0-s82/.restage-pair.done
