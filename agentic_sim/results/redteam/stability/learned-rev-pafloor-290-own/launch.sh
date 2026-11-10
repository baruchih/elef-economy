#!/bin/zsh
# 2.9.0 §8.7's pinned cell — the self-play population with m^A pinned at 1: the planted approvals held at π^A's floor 0.02 per member-audited real
# approval (`--pi-a-max 0.02` = π^A_0, so the per-seat multiplier cannot step; the dial's π_t, m_t and the lie multipliers live) — the lever shown from
# below, read against the rc's prediction (the seat unpriced, the capture of run 36 returns). On own-name credit at 2.9.0 on the corrected engine; the
# recipe learned-rev-careful-290-own's (the careful-weighted offline set — careful, ε, random on seeds 1–20, the stamper on 1–5 — ten rounds of ε 0.1
# uniform exploration, the direct the carrier and the world model under the head alone beside, stride 4, the finals on seeds 21–40 with careful,
# stamper and hand on the same slots), paired against run 42. Queued behind arm 2's chain (ablation-A1/queue3.sh; November 10, 2026, notes §88).
# Run from agentic_sim/ in the elef-redteam env: launch.sh all (collect, online, final).
# with the cell's own flag. Run from agentic_sim/ in the elef-redteam env: launch.sh all (collect, online, final).
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-pafloor-290-own/launch.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
X=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-pafloor-290-own
CELL=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a-max 0.02)
step=${1:-collect}
case $step in
  collect)
    $PY -m redteam.collect --out $X/offline-main --seeds 1-20 --policies careful,eps,random --attrib own -- "${CELL[@]}" > $X/offline-main.log 2>&1 &
    $PY -m redteam.collect --out $X/offline-minor --seeds 1-5 --policies stamper --attrib own -- "${CELL[@]}" > $X/offline-minor.log 2>&1 &
    wait
    mkdir -p $X/direct-offline $X/wm-offline
    cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/direct-offline/; cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/wm-offline/ ;;
  online)
    $PY -m redteam.online --data $X/direct-offline --models $X/direct/models --evals $X/direct/eval --rounds 10 --eps 0.1 --explore uniform --learner direct --eval-every 5 --eval-policies direct,careful --stride 4 --horizon 16 --attrib own -- "${CELL[@]}" > $X/direct-online.log 2>&1 &
    $PY -m redteam.online --data $X/wm-offline --models $X/wm/models --evals $X/wm/eval --rounds 10 --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own -- "${CELL[@]}" > $X/wm-online.log 2>&1 &
    wait ;;
  final)
    $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $X/direct/eval/final --seeds 21-40 --policies direct,careful,stamper,hand --attrib own -- "${CELL[@]}" > $X/direct-final.log 2>&1 &
    $PY -m redteam.run_q --model $X/wm/models/wm-online-10.pt --out $X/wm/eval/final --seeds 21-40 --policies greedy,careful,stamper,hand --horizon 16 --attrib own -- "${CELL[@]}" > $X/wm-final.log 2>&1 &
    wait ;;
  all) $SELF collect && $SELF online && $SELF final && touch $X/chain.done ;;
esac
