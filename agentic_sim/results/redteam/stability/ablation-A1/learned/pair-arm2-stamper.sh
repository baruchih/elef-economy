#!/bin/zsh
# arm 2's stamper start paired against its careful start (the basin test, addendum 5 E3.2) and against run 42
cd /Users/baruchi-admin/projects/elef-economy/agentic_sim
A=results/redteam/stability/ablation-A1/learned
SUF290="" BASESUF="" BASEFINAL=final FINAL=final TAG290="arm 2, the stamper start" TAGBASE="arm 2, the careful start" BASECELL="ablation-A1/learned/arm2-stamper:ablation-A1/learned/arm2" python3 results/redteam/stability/2.9.0-s82/finals-paired.py $A/finals-paired-arm2-stamper.md ablation-A1/learned/arm2-stamper > $A/finals-paired-arm2-stamper.log 2>&1
SUF290="" BASESUF=-290-own BASEFINAL=final-cr FINAL=final TAG290="arm 2, the stamper start" TAGBASE="run 42 (arm 0)" BASECELL="ablation-A1/learned/arm2-stamper:careful" python3 results/redteam/stability/2.9.0-s82/finals-paired.py $A/finals-paired-arm2-stamper-run42.md ablation-A1/learned/arm2-stamper > $A/finals-paired-arm2-stamper-run42.log 2>&1
