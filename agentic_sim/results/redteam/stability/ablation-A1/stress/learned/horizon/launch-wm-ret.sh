#!/bin/zsh
# The world model's chains under the return-head read (November 13, 2026; notes §111) at 04f1c5565: H4's read (the head alone as reward + γ V at the predicted next
# latent) failed the known-answer test at the first review (−0.7 ± 0.2 against −23.1 ± 3.5) and its chains were stopped in their first round (the partial record
# kept under wm/ as the failed read's); the return head (`--return-read direct`: the reward head fit to the slot's return to its exit at γ 0.98, read alone) passed
# (−27.8 ± 1.5), so the world model's chains run on it — the same offline set (copied to wm-ret-offline/, free of the stopped chain's round files), ten rounds of
# ε 0.1 uniform under the head alone, stride 4, the final on seeds 21–40 with the careful, the stamper, the claimer and the hand. Run from agentic_sim/: launch-wm-ret.sh all
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
SELF=/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/horizon/launch-wm-ret.sh
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
H=$PWD/results/redteam/stability/ablation-A1/stress/learned/horizon
BASE=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1)
declare -A ARM
ARM[pa10]="--pi-a0 0.10 --pi-a-max 0.10"
ARM[arm4]="--arm 4"
RET=(--return-horizon mc --return-gamma 0.98 --return-read direct)
step=${1:-online}
case $step in
  online)
    for k in pa10 arm4; do X=$H/$k-t1-b1-mc; mkdir -p $X/wm-ret-offline; cp $X/offline-main/*.npz $X/offline-minor/*.npz $X/wm-ret-offline/
      $PY -m redteam.online --data $X/wm-ret-offline --models $X/wm-ret/models --evals $X/wm-ret/eval --rounds 10 --eps 0.1 --explore uniform --plan greedy --value mc --heads two --horizon 16 --stride 4 --eval-every 5 --eval-policies greedy,careful --attrib own "${RET[@]}" -- "${BASE[@]}" ${=ARM[$k]} > $X/wm-ret-online.log 2>&1 &
    done; wait ;;
  final)
    for k in pa10 arm4; do X=$H/$k-t1-b1-mc
      $PY -m redteam.run_q --model $X/wm-ret/models/wm-online-10.pt --out $X/wm-ret/eval/final --seeds 21-40 --policies greedy,careful,stamper,claimer,hand --horizon 16 --attrib own -- "${BASE[@]}" ${=ARM[$k]} > $X/wm-ret-final.log 2>&1 &
    done; wait ;;
  all) $SELF online && $SELF final && touch $H/chain-wm-ret.done ;;
esac
