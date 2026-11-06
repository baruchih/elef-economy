# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule; seeds 21–40; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-stamper-290-own/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-stamper-290-own/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 38 ± 2 | 36 ± 2 | 83 ± 4 | 12.5 | 12.1 | 27.6 |
| member | appeal | real | 408 ± 22 | 398 ± 15 | 733 ± 23 | 159.6 | 156.0 | 271.9 |
| member | audit | plant | 67 ± 5 | 69 ± 4 | 249 ± 10 | 22.4 | 22.9 | 83.0 |
| member | audit | real | 2370 ± 75 | 2280 ± 39 | 2880 ± 59 | 859.5 | 834.2 | 1017.5 |
| member | initial | plant | 127 ± 4 | 138 ± 3 | 286 ± 7 | 63.4 | 69.2 | 142.9 |
| member | initial | real | 5106 ± 16 | 5111 ± 22 | 5112 ± 37 | 2654.2 | 2664.3 | 2618.5 |
| state | appeal | real | 337 ± 12 | 345 ± 10 | 294 ± 11 | 132.7 | 136.5 | 112.7 |
| state | audit | real | 2159 ± 70 | 2256 ± 56 | 1806 ± 42 | 754.4 | 787.5 | 617.9 |
| state | initial | real | 0 ± 0 | 1 ± 0 | 12 ± 2 | 0.2 | 0.3 | 6.2 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 8116 ± 111 | 8031 ± 60 | 9342 ± 119 |
| state | 2496 ± 78 | 2602 ± 62 | 2112 ± 50 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 446 ± 23 | 434 ± 15 | 816 ± 22 |
| members' audit-seat fees | 2438 ± 79 | 2348 ± 42 | 3129 ± 68 |
| state's audit-seat fees | 2159 ± 70 | 2256 ± 56 | 1806 ± 42 |
| state's panel fees | 337 ± 12 | 345 ± 10 | 294 ± 11 |
| state's initial-seat fees | 0 ± 0 | 1 ± 0 | 12 ± 2 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 756 ± 21 | 733 ± 11 | 1469 ± 25 |
| bond burned | state | 169 ± 9 | 202 ± 9 | 165 ± 9 |
| court fee won | member | 189 ± 5 | 186 ± 4 | 156 ± 5 |
| members' audits of real approvals (the base), a run | member | 813 ± 25 | 794 ± 18 | 979 ± 24 |
| service fee to Ω | state | 2347 ± 23 | 2360 ± 30 | 2453 ± 12 |
| uplift | member | 153 ± 67 | 377 ± 53 | 3933 ± 82 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 51 | 1.0 | 0.02 | [0, 0] | 0 | 0; 153 | 1.0 | 0.02 | [2, 4] | 4 | 2; 290 | 1.0 | 0.02 | [4, 9] | 5 | 2; 249 | 2.0 | 0.04 | [0, 0] | 5 | 3; 154 | 2.0 | 0.04 | [3, 6] | 6 | 3
- direct seed 22: 33 | 1.0 | 0.02 | [0, 0] | 0 | 0; 166 | 1.0 | 0.02 | [2, 3] | 3 | 2; 256 | 1.0 | 0.02 | [3, 8] | 5 | 1; 192 | 2.0 | 0.04 | [0, 0] | 4 | 1; 130 | 2.0 | 0.04 | [1, 5] | 5 | 1; 158 | 4.0 | 0.08 | [0, 0] | 7 | 4
- direct seed 23: 91 | 1.0 | 0.02 | [1, 1] | 1 | 1; 99 | 1.0 | 0.02 | [2, 3] | 2 | 1; 224 | 1.0 | 0.02 | [3, 8] | 5 | 1; 242 | 2.0 | 0.04 | [0, 0] | 5 | 3; 146 | 2.0 | 0.04 | [2, 5] | 5 | 2
- head alone seed 21: 40 | 1.0 | 0.02 | [0, 0] | 0 | 0; 193 | 1.0 | 0.02 | [3, 4] | 4 | 3; 176 | 1.0 | 0.02 | [6, 8] | 4 | 3; 188 | 2.0 | 0.04 | [0, 0] | 3 | 3; 142 | 2.0 | 0.04 | [3, 6] | 6 | 3
- head alone seed 22: 26 | 1.0 | 0.02 | [0, 0] | 0 | 0; 189 | 1.0 | 0.02 | [4, 4] | 4 | 4; 161 | 1.0 | 0.02 | [7, 7] | 3 | 3; 168 | 2.0 | 0.04 | [0, 0] | 3 | 2; 155 | 2.0 | 0.04 | [4, 6] | 6 | 4; 109 | 4.0 | 0.08 | [0, 0] | 5 | 2; 94 | 4.0 | 0.08 | [3, 7] | 7 | 3
- head alone seed 23: 17 | 1.0 | 0.02 | [0, 0] | 0 | 0; 37 | 1.0 | 0.02 | [1, 1] | 1 | 1; 149 | 1.0 | 0.02 | [2, 3] | 2 | 1; 318 | 2.0 | 0.04 | [0, 0] | 7 | 2; 245 | 4.0 | 0.08 | [0, 0] | 10 | 4
- hand seed 21: 20 | 1.0 | 0.02 | [0, 0] | 0 | 0; 6 | 1.0 | 0.02 | [0, 0] | 0 | 0; 52 | 1.0 | 0.02 | [0, 1] | 1 | 0; 71 | 1.0 | 0.02 | [0, 2] | 1 | 0; 81 | 1.0 | 0.02 | [1, 4] | 2 | 1; 90 | 1.0 | 0.02 | [1, 6] | 2 | 0; 92 | 1.0 | 0.02 | [1, 8] | 2 | 0; 106 | 1.0 | 0.02 | [0, 0] | 2 | 0; 93 | 1.0 | 0.02 | [1, 2] | 2 | 1; 107 | 1.0 | 0.02 | [1, 4] | 2 | 0; 105 | 1.0 | 0.02 | [1, 6] | 2 | 0
- hand seed 22: 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 10 | 1.0 | 0.02 | [0, 0] | 0 | 0; 70 | 1.0 | 0.02 | [0, 1] | 1 | 0; 88 | 1.0 | 0.02 | [0, 3] | 2 | 0; 84 | 1.0 | 0.02 | [0, 5] | 2 | 0; 99 | 1.0 | 0.02 | [0, 7] | 2 | 0; 97 | 1.0 | 0.02 | [0, 9] | 2 | 0; 109 | 1.0 | 0.02 | [0, 0] | 2 | 0; 98 | 1.0 | 0.02 | [0, 2] | 2 | 0; 99 | 1.0 | 0.02 | [1, 4] | 2 | 1; 98 | 1.0 | 0.02 | [1, 6] | 2 | 0
- hand seed 23: 19 | 1.0 | 0.02 | [0, 0] | 0 | 0; 34 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 1] | 1 | 0; 76 | 1.0 | 0.02 | [0, 2] | 1 | 0; 95 | 1.0 | 0.02 | [0, 4] | 2 | 0; 90 | 1.0 | 0.02 | [0, 6] | 2 | 0; 82 | 1.0 | 0.02 | [0, 7] | 1 | 0; 90 | 1.0 | 0.02 | [0, 9] | 2 | 0; 89 | 1.0 | 0.02 | [0, 0] | 2 | 0; 105 | 1.0 | 0.02 | [0, 2] | 2 | 0; 100 | 1.0 | 0.02 | [0, 4] | 2 | 0; 101 | 1.0 | 0.02 | [0, 6] | 2 | 0; 92 | 1.0 | 0.02 | [0, 8] | 2 | 0
