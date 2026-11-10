# The customers' truthful disputes by the panel's make-up, and the state's panel seats by cause — detection 0.25, run 42's final policy (results/redteam/stability/learned-rev-careful-290-own/direct/models/direct-online-10.pt) and the careful, seeds 21–40

| policy | make-up | disputes a run | won a run | **won share (pooled)** |
|---|---|---|---|---|
| direct | two members | 3.20 ± 0.33 | 0.75 ± 0.16 | 0.234 (64) |
| direct | one member, one of the state's | 3.80 ± 0.30 | 3.10 ± 0.27 | 0.816 (76) |
| direct | two of the state's | 3.95 ± 0.32 | 3.85 ± 0.32 | 0.975 (79) |
| careful | two members | 3.35 ± 0.32 | 3.30 ± 0.32 | 0.985 (67) |
| careful | one member, one of the state's | 1.85 ± 0.26 | 1.80 ± 0.27 | 0.973 (37) |
| careful | two of the state's | 1.90 ± 0.27 | 1.90 ± 0.27 | 1.000 (38) |

| policy | member panel seats | state panel seats (audit + appeal) | state audits | panel seats unfilled at the driver's seating (ticks) | … a free member kept off the tier | … no member free | member-periods panel-ineligible |
|---|---|---|---|---|---|---|---|
| direct | 214.90 ± 6.81 | 1058.70 ± 32.89 | 895.70 ± 28.21 | 275.50 ± 8.72 | 275.40 ± 8.72 | 0.10 ± 0.07 | 92.05 ± 3.08 |
| careful | 293.65 ± 7.21 | 773.60 ± 21.57 | 650.10 ± 19.56 | 210.90 ± 6.00 | 210.45 ± 5.99 | 0.45 ± 0.11 | 63.50 ± 1.37 |
