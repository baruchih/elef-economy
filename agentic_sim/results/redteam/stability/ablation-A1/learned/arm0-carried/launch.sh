#!/bin/zsh
# Arm 0 with the dials carried (the economy reviewer's addendum 4 to ablation brief A1, D3; November 10, 2026) — a harness option, no rule:
# 2.9.0 as written in an economy that does not restart. From run 42's final policies (learned-rev-careful-290-own, direct-online-10 / wm-online-10),
# ten further rounds (11–20) on run 42's offline set plus the chain's own collections; each round's runs start their four dials (m_t, m^A, m^La, m^Ld)
# at the MEAN over the round before's runs of the dials at their end (the carry rule, the implementer's: a single economy would carry one state and the
# twenty seeds are its samples; the mean is the pooled reading, the per-run ends kept in the online log's `dials` block), the round's evaluation at
# the mean of its own round's ends; the first round where run 42's final evaluation (seeds 21–40, final-cr) ended — the direct 1.186 / 4.767 / 1.507 / 1.000,
# the head alone 1.162 / 3.812 / 1.117 / 1.000 (2.9.0-s82/dial-path-run42.json for m_t and m^A, the finals' rows for m^La, m^Ld). The final evaluation
# on seeds 21–40 starts where round 20's runs ended (read from the online log).
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/learned/arm0-carried/launch.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/learned/arm0-carried
R=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-careful-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
step=${1:-online}
case $step in
  online)
    mkdir -p $X/direct-offline $X/wm-offline $X/direct/models $X/wm/models
    cp $R/direct-offline/*.npz $X/direct-offline/; cp $R/wm-offline/*.npz $X/wm-offline/
    $PY -m redteam.online --data $X/direct-offline --models $X/direct/models --evals $X/direct/eval --start $R/direct/models/direct-online-10.pt --first-round 11 --rounds 10 --eps 0.1 --explore uniform --learner direct --eval-every 5 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own --carry-dials mean --dial-start 1.186,4.767,1.507,1.000 -- "${CELL[@]}" > $X/direct-online.log 2>&1 &
    $PY -m redteam.online --data $X/wm-offline --models $X/wm/models --evals $X/wm/eval --start $R/wm/models/wm-online-10.pt --first-round 11 --rounds 10 --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own --carry-dials mean --dial-start 1.162,3.812,1.117,1.000 -- "${CELL[@]}" > $X/wm-online.log 2>&1 &
    wait ;;
  final)
    DS=$(python3 -c "import json; L=json.load(open('$X/direct/eval/online-log-11.json')); print(','.join('%.6f'%x for x in L[-1]['dials']['ends_mean']))")
    WS=$(python3 -c "import json; L=json.load(open('$X/wm/eval/online-log-11.json')); print(','.join('%.6f'%x for x in L[-1]['dials']['ends_mean']))")
    echo "final starts: direct $DS, wm $WS" > $X/final-starts.txt
    $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-20.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,hand --attrib own -- "${CELL[@]}" --dial-start $DS > $X/direct-final.log 2>&1 &
    $PY -m redteam.run_q --model $X/wm/models/wm-online-20.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,hand --horizon 16 --attrib own -- "${CELL[@]}" --dial-start $WS > $X/wm-final.log 2>&1 &
    wait ;;
  all) $SELF online && $SELF final && touch $X/chain.done ;;
esac
