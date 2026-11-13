#!/bin/zsh
# The learner with a horizon's known-answer data (addendum 10's J5, the second test of I5; November 13, 2026; notes §111) at 336aaf301 (the collector's factory fix; the export ffd23d851's): two dose worlds of §110
# collected with the horizon's export — the pin at a temptation of 1 and the bond ×1, the dosing slots 1 in 4 at a dose of 0.3 at the first review alone
# (`mix:dose0.3first:0.25`; the known answer there 23.1 ± 3.5 real lost a claim) and at the member's audit seat alone (`mix:dose0.3audit:0.25`; the known
# answer there J4's), seeds 1–20 (the training seeds; the dose read was on 21–40 and is the known answer's source). The direct policy and the world model are
# fit on each at a return horizon of `mc` and γ 0.98 by known_read.py, which reads the fitted difference in return between a claim and an inspection at the
# seat against the known answer, and the return's spread with the decisions behind each action at each seat (the third test).
# Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
R=$PWD/results/redteam/stability/ablation-A1/stress/learned/horizon/known
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10)
if [ "$1" = "" ]; then          # the two worlds of the first launch; the later blocks by their own argument
$PY -m redteam.collect --out $R/first --seeds 1-20 --policies mix:dose0.3first:0.25 --attrib own -- "${CELL[@]}" > $R/first.log 2>&1 &
$PY -m redteam.collect --out $R/audit --seeds 1-20 --policies mix:dose0.3audit:0.25 --attrib own -- "${CELL[@]}" > $R/audit.log 2>&1 &
wait
touch $R/.done
fi
# Added after J4's read (November 13, 2026): the member's audit seat at a dose of 1 in the same cell (J4's world 2, where the known answer — 15.0 ± 2.9 real lost a
# claim on sixty seeds — can be told from nothing where world 1's 4.0 ± 4.8 cannot), seeds 1–20: launch.sh audit1
if [ "$1" = "audit1" ]; then
  $PY -m redteam.collect --out $R/audit1 --seeds 1-20 --policies mix:dose1audit:0.25 --attrib own -- "${CELL[@]}" > $R/audit1.log 2>&1
  touch $R/.audit1.done
fi
# Added after the known-answer reads (November 13, 2026): the member's audit seat at a dose of 0.3 in J4's world 5 cell (π^A 0.30, the fee doubled: the known
# answer 45.1 ± 7.7 real lost a claim on sixty seeds, and the dose randomized within the slot — world 2's dose of 1 confounds the action with the group), seeds 1–20:
# launch.sh audit-w5
if [ "$1" = "audit-w5" ]; then
  $PY -m redteam.collect --out $R/audit-w5 --seeds 1-20 --policies mix:dose0.3audit:0.25 --attrib own -- --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.30 --pi-a-max 0.30 --w-audit 3 > $R/audit-w5.log 2>&1
  touch $R/.audit-w5.done
fi
