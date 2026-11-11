# The customers' truthful disputes by the panel's make-up, and the state's panel seats by cause — detection 0.1, the direct's policy /Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/detection/retrain-d0.1/direct/models/direct-online-20.pt and the careful, cell --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --dispute-rate 0.1, seeds 21–40

| policy | make-up | disputes a run | won a run | **won share (pooled)** |
|---|---|---|---|---|
| direct | two members | 1.05 ± 0.22 | 1.00 ± 0.21 | 0.952 (21) |
| direct | one member, one of the state's | 0.75 ± 0.16 | 0.70 ± 0.15 | 0.933 (15) |
| direct | two of the state's | 1.15 ± 0.23 | 1.10 ± 0.23 | 0.957 (23) |
| careful | two members | 1.90 ± 0.38 | 1.85 ± 0.39 | 0.974 (38) |
| careful | one member, one of the state's | 0.65 ± 0.15 | 0.65 ± 0.15 | 1.000 (13) |
| careful | two of the state's | 1.00 ± 0.24 | 1.00 ± 0.24 | 1.000 (20) |

| policy | member panel seats | state panel seats (audit + appeal) | state audits | panel seats unfilled at the driver's seating (ticks) | … a free member kept off the tier | … no member free | member-periods panel-ineligible |
|---|---|---|---|---|---|---|---|
| direct | 228.10 ± 8.21 | 902.85 ± 32.53 | 767.60 ± 26.79 | 227.60 ± 9.44 | 227.30 ± 9.43 | 0.30 ± 0.15 | 80.40 ± 1.88 |
| careful | 301.30 ± 9.98 | 721.55 ± 22.25 | 608.95 ± 18.89 | 192.45 ± 6.77 | 192.25 ± 6.75 | 0.20 ± 0.09 | 63.30 ± 1.23 |

The joint of the two verdicts on the customers' truthful disputes, by make-up (pooled): both confirm the standing F / split / both reject, against the product of the single-seat F rate p on the same panels (p², 2p(1−p), (1−p)²):

| policy | make-up | panels | single-seat F rate p | both confirm (observed / p²) | split (observed / 2p(1−p)) | both reject (observed / (1−p)²) |
|---|---|---|---|---|---|---|
| direct | two members | 21 | 0.048 | 0.000 / 0.002 | 0.095 / 0.091 | 0.905 / 0.907 |
| direct | one member, one of the state's | 15 | 0.067 | 0.000 / 0.004 | 0.133 / 0.124 | 0.867 / 0.871 |
| direct | two of the state's | 23 | 0.065 | 0.000 / 0.004 | 0.130 / 0.122 | 0.870 / 0.874 |
| careful | two members | 38 | 0.039 | 0.000 / 0.002 | 0.079 / 0.076 | 0.921 / 0.923 |
| careful | one member, one of the state's | 13 | 0.038 | 0.000 / 0.001 | 0.077 / 0.074 | 0.923 / 0.925 |
| careful | two of the state's | 20 | 0.050 | 0.000 / 0.003 | 0.100 / 0.095 | 0.900 / 0.902 |
