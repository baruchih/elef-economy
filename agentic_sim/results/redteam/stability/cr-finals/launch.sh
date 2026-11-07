#!/bin/zsh
# The finals of record re-evaluated once on the corrected engine (the economy reviewer's and Baruchi's ruling of November 7, 2026; notes §77):
# the emission's power correctly rounded (`Params.emission`), so a seed's episode no longer depends on the platform and the record's replay and
# any later pairing on seeds 21–40 read the same episode. The chains' models are the ones of record (round 10 of each chain, trained on the
# macOS episode); only the evaluation is re-run — seeds 21–40, the same policies (the direct or the head alone, the careful, the stamper and the
# 60/40 mix `hand` on the same slots), the measured seat table in every eval.md. Outputs beside the finals of record: <chain>/{direct,wm}/eval/final-cr/
# (the finals of record stay at eval/final/ as the macOS episode's, the seam stated). The 2.9.0 chains run on the current tree; the 2.7.0 pairing's
# chains on the provenance branch own-name-at-8b26ebf6 in its worktree, the correction ported there. Run from agentic_sim/ in the elef-redteam env.
PY=/opt/homebrew/Caskroom/miniconda/base/envs/elef-redteam/bin/python
R=/Users/baruchi-admin/projects/elef-economy/agentic_sim; S=$R/results/redteam/stability
W=/private/tmp/claude-502/-Users-baruchi-admin-projects-elef-economy/eec13392-a9d7-4994-aec0-e91f71934505/scratchpad/wt-27/agentic_sim
BASE=(--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule)
LIAR=("${BASE[@]}" --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1)
final() {   # final <tree> <chain> <cell args...>
  local T=$1 X=$S/$2; shift 2
  ( cd $T && $PY -m redteam.run_q --direct-model $X/direct/models/direct-online-10.pt --out $X/direct/eval/final-cr --seeds 21-40 --policies direct,careful,stamper,hand --attrib own -- "$@" > $X/direct-final-cr.log 2>&1 ) &
  ( cd $T && $PY -m redteam.run_q --model $X/wm/models/wm-online-10.pt --out $X/wm/eval/final-cr --seeds 21-40 --policies greedy,careful,stamper,hand --horizon 16 --attrib own -- "$@" > $X/wm-final-cr.log 2>&1 ) &
}
cd $R
final $R learned-rev-careful-290-own "${BASE[@]}"      # run 42
final $R learned-rev-stamper-290-own "${BASE[@]}"      # the basin test's stamper start
final $R learned-rev-liars-290-own   "${LIAR[@]}"      # the liar chain
final $W learned-rev-careful-2-own   "${BASE[@]}"      # the 2.7.0 pairing, careful start
final $W learned-rev-stamper-2-own   "${BASE[@]}"      # the 2.7.0 pairing, stamper start
wait
echo "finals done $(date)" > $S/cr-finals/finals.done
