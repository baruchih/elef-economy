# The customers' truthful disputes by the panel's make-up, and the state's panel seats by cause — detection 0.25, the direct's policy /Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/detection/retrain-d0.25/direct/models/direct-online-20.pt and the careful, cell --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.25, seeds 21–40

| policy | make-up | disputes a run | won a run | **won share (pooled)** |
|---|---|---|---|---|
| direct | two members | 3.05 ± 0.51 | 2.95 ± 0.49 | 0.967 (61) |
| direct | one member, one of the state's | 2.30 ± 0.29 | 2.25 ± 0.31 | 0.978 (46) |
| direct | two of the state's | 2.35 ± 0.44 | 2.30 ± 0.45 | 0.979 (47) |
| careful | two members | 3.35 ± 0.32 | 3.30 ± 0.32 | 0.985 (67) |
| careful | one member, one of the state's | 1.85 ± 0.26 | 1.80 ± 0.27 | 0.973 (37) |
| careful | two of the state's | 1.90 ± 0.27 | 1.90 ± 0.27 | 1.000 (38) |

| policy | member panel seats | state panel seats (audit + appeal) | state audits | panel seats unfilled at the driver's seating (ticks) | … a free member kept off the tier | … no member free | member-periods panel-ineligible |
|---|---|---|---|---|---|---|---|
| direct | 226.90 ± 7.32 | 916.55 ± 25.06 | 776.85 ± 21.82 | 233.60 ± 7.41 | 233.35 ± 7.39 | 0.25 ± 0.16 | 82.30 ± 2.20 |
| careful | 293.65 ± 7.21 | 773.60 ± 21.57 | 650.10 ± 19.56 | 210.90 ± 6.00 | 210.45 ± 5.99 | 0.45 ± 0.11 | 63.50 ± 1.37 |

The joint of the two verdicts on the customers' truthful disputes, by make-up (pooled): both confirm the standing F / split / both reject, against the product of the single-seat F rate p on the same panels (p², 2p(1−p), (1−p)²):

| policy | make-up | panels | single-seat F rate p | both confirm (observed / p²) | split (observed / 2p(1−p)) | both reject (observed / (1−p)²) |
|---|---|---|---|---|---|---|
| direct | two members | 61 | 0.074 | 0.016 / 0.005 | 0.115 / 0.137 | 0.869 / 0.858 |
| direct | one member, one of the state's | 46 | 0.054 | 0.000 / 0.003 | 0.109 / 0.103 | 0.891 / 0.894 |
| direct | two of the state's | 47 | 0.043 | 0.000 / 0.002 | 0.085 / 0.081 | 0.915 / 0.917 |
| careful | two members | 67 | 0.067 | 0.000 / 0.005 | 0.134 / 0.125 | 0.866 / 0.870 |
| careful | one member, one of the state's | 37 | 0.068 | 0.000 / 0.005 | 0.135 / 0.126 | 0.865 / 0.869 |
| careful | two of the state's | 38 | 0.053 | 0.000 / 0.003 | 0.105 / 0.100 | 0.895 / 0.898 |
