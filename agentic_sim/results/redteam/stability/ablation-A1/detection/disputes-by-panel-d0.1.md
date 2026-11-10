# The customers' truthful disputes by the panel's make-up, and the state's panel seats by cause — detection 0.1, run 42's final policy (results/redteam/stability/learned-rev-careful-290-own/direct/models/direct-online-10.pt) and the careful, seeds 21–40

| policy | make-up | disputes a run | won a run | **won share (pooled)** |
|---|---|---|---|---|
| direct | two members | 1.70 ± 0.29 | 0.75 ± 0.14 | 0.441 (34) |
| direct | one member, one of the state's | 1.35 ± 0.25 | 1.20 ± 0.19 | 0.889 (27) |
| direct | two of the state's | 1.00 ± 0.23 | 1.00 ± 0.23 | 1.000 (20) |
| careful | two members | 1.90 ± 0.38 | 1.85 ± 0.39 | 0.974 (38) |
| careful | one member, one of the state's | 0.65 ± 0.15 | 0.65 ± 0.15 | 1.000 (13) |
| careful | two of the state's | 1.00 ± 0.24 | 1.00 ± 0.24 | 1.000 (20) |

| policy | member panel seats | state panel seats (audit + appeal) | state audits | panel seats unfilled at the driver's seating (ticks) | … a free member kept off the tier | … no member free | member-periods panel-ineligible |
|---|---|---|---|---|---|---|---|
| direct | 240.75 ± 8.62 | 965.90 ± 31.70 | 810.60 ± 24.83 | 262.95 ± 15.43 | 262.50 ± 15.17 | 0.45 ± 0.30 | 92.55 ± 4.65 |
| careful | 301.30 ± 9.98 | 721.55 ± 22.25 | 608.95 ± 18.89 | 192.45 ± 6.77 | 192.25 ± 6.75 | 0.20 ± 0.09 | 63.30 ± 1.23 |

The joint of the two verdicts on the customers' truthful disputes, by make-up (pooled): both confirm the standing F / split / both reject, against the product of the single-seat F rate p on the same panels (p², 2p(1−p), (1−p)²):

| policy | make-up | panels | single-seat F rate p | both confirm (observed / p²) | split (observed / 2p(1−p)) | both reject (observed / (1−p)²) |
|---|---|---|---|---|---|---|
| direct | two members | 34 | 0.706 | 0.500 / 0.498 | 0.412 / 0.415 | 0.088 / 0.087 |
| direct | one member, one of the state's | 27 | 0.389 | 0.000 / 0.151 | 0.778 / 0.475 | 0.222 / 0.373 |
| direct | two of the state's | 20 | 0.050 | 0.000 / 0.003 | 0.100 / 0.095 | 0.900 / 0.902 |
| careful | two members | 38 | 0.039 | 0.000 / 0.002 | 0.079 / 0.076 | 0.921 / 0.923 |
| careful | one member, one of the state's | 13 | 0.038 | 0.000 / 0.001 | 0.077 / 0.074 | 0.923 / 0.925 |
| careful | two of the state's | 20 | 0.050 | 0.000 / 0.003 | 0.100 / 0.095 | 0.900 / 0.902 |
