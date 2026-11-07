# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1; seeds 21–40; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-liars-290-own/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-liars-290-own/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 172 ± 8 | 179 ± 8 | 308 ± 10 | 57.2 | 59.8 | 102.5 |
| member | appeal | real | 1137 ± 27 | 1120 ± 20 | 1436 ± 17 | 503.4 | 501.6 | 615.5 |
| member | audit | plant | 20 ± 5 | 21 ± 5 | 172 ± 9 | 6.5 | 7.0 | 57.4 |
| member | audit | real | 2986 ± 68 | 3063 ± 57 | 3004 ± 39 | 1074.7 | 1103.3 | 1076.5 |
| member | initial | plant | 125 ± 4 | 128 ± 3 | 285 ± 7 | 62.5 | 64.1 | 142.6 |
| member | initial | real | 4817 ± 27 | 4848 ± 24 | 4796 ± 21 | 2588.4 | 2607.1 | 2555.3 |
| state | appeal | real | 693 ± 21 | 661 ± 18 | 745 ± 13 | 318.5 | 305.9 | 321.4 |
| state | audit | real | 1630 ± 53 | 1523 ± 41 | 1497 ± 35 | 561.0 | 523.1 | 503.8 |
| state | initial | real | 2 ± 0 | 1 ± 0 | 16 ± 2 | 0.8 | 0.7 | 8.6 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 9256 ± 118 | 9359 ± 89 | 10001 ± 68 |
| state | 2325 ± 71 | 2185 ± 56 | 2258 ± 40 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 1308 ± 33 | 1299 ± 25 | 1744 ± 23 |
| members' audit-seat fees | 3005 ± 69 | 3084 ± 58 | 3177 ± 39 |
| state's audit-seat fees | 1630 ± 53 | 1523 ± 41 | 1497 ± 35 |
| state's panel fees | 693 ± 21 | 661 ± 18 | 745 ± 13 |
| state's initial-seat fees | 2 ± 0 | 1 ± 0 | 16 ± 2 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 736 ± 13 | 656 ± 15 | 1407 ± 16 |
| bond burned | state | 181 ± 11 | 184 ± 10 | 196 ± 8 |
| court fee won | member | 263 ± 4 | 256 ± 6 | 330 ± 5 |
| members' audits of real approvals (the base), a run | member | 1027 ± 29 | 1045 ± 26 | 1057 ± 16 |
| service fee to Ω | state | 2419 ± 32 | 2406 ± 21 | 2375 ± 11 |
| uplift | member | 201 ± 59 | 167 ± 78 | 3686 ± 76 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 33 | 1.0 | 0.02 | [0, 0] | 0 | 0; 93 | 1.0 | 0.02 | [0, 0] | 0 | 0; 240 | 1.0 | 0.02 | [0, 0] | 0 | 0; 325 | 1.0 | 0.02 | [0, 0] | 0 | 0; 213 | 1.0 | 0.02 | [0, 0] | 0 | 0
- direct seed 22: 14 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 171 | 1.0 | 0.02 | [0, 0] | 0 | 0; 244 | 1.0 | 0.02 | [0, 0] | 0 | 0; 229 | 1.0 | 0.02 | [0, 0] | 0 | 0
- direct seed 23: 39 | 1.0 | 0.02 | [0, 0] | 0 | 0; 172 | 1.0 | 0.02 | [0, 0] | 0 | 0; 251 | 1.0 | 0.02 | [0, 0] | 0 | 0; 237 | 1.0 | 0.02 | [0, 0] | 0 | 0; 306 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 21: 42 | 1.0 | 0.02 | [0, 0] | 0 | 0; 188 | 1.0 | 0.02 | [0, 0] | 0 | 0; 307 | 1.0 | 0.02 | [0, 0] | 0 | 0; 302 | 1.0 | 0.02 | [0, 0] | 0 | 0; 295 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 22: 80 | 1.0 | 0.02 | [1, 1] | 1 | 1; 137 | 1.0 | 0.02 | [2, 2] | 1 | 1; 222 | 1.0 | 0.02 | [2, 2] | 0 | 0; 319 | 1.0 | 0.02 | [2, 2] | 0 | 0; 287 | 1.0 | 0.02 | [2, 2] | 0 | 0
- head alone seed 23: 36 | 1.0 | 0.02 | [0, 0] | 0 | 0; 221 | 1.0 | 0.02 | [0, 0] | 0 | 0; 281 | 1.0 | 0.02 | [0, 0] | 0 | 0; 263 | 1.0 | 0.02 | [0, 0] | 0 | 0; 298 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 21: 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 67 | 1.0 | 0.02 | [0, 0] | 0 | 0; 63 | 1.0 | 0.02 | [0, 0] | 0 | 0; 80 | 1.0 | 0.02 | [0, 0] | 0 | 0; 80 | 1.0 | 0.02 | [0, 0] | 0 | 0; 99 | 1.0 | 0.02 | [0, 0] | 0 | 0; 112 | 1.0 | 0.02 | [0, 0] | 0 | 0; 127 | 1.0 | 0.02 | [0, 0] | 0 | 0; 143 | 1.0 | 0.02 | [0, 0] | 0 | 0; 145 | 1.0 | 0.02 | [0, 0] | 0 | 0; 161 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 22: 11 | 1.0 | 0.02 | [0, 0] | 0 | 0; 70 | 1.0 | 0.02 | [0, 0] | 0 | 0; 3 | 1.0 | 0.02 | [0, 0] | 0 | 0; 59 | 1.0 | 0.02 | [0, 0] | 0 | 0; 87 | 1.0 | 0.02 | [0, 0] | 0 | 0; 107 | 1.0 | 0.02 | [0, 0] | 0 | 0; 122 | 1.0 | 0.02 | [0, 0] | 0 | 0; 128 | 1.0 | 0.02 | [0, 0] | 0 | 0; 145 | 1.0 | 0.02 | [0, 0] | 0 | 0; 178 | 1.0 | 0.02 | [0, 0] | 0 | 0; 179 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 23: 30 | 1.0 | 0.02 | [0, 0] | 0 | 0; 68 | 1.0 | 0.02 | [0, 0] | 0 | 0; 53 | 1.0 | 0.02 | [0, 0] | 0 | 0; 81 | 1.0 | 0.02 | [0, 0] | 0 | 0; 92 | 1.0 | 0.02 | [0, 0] | 0 | 0; 95 | 1.0 | 0.02 | [0, 0] | 0 | 0; 105 | 1.0 | 0.02 | [0, 0] | 0 | 0; 102 | 1.0 | 0.02 | [0, 0] | 0 | 0; 124 | 1.0 | 0.02 | [0, 0] | 0 | 0; 134 | 1.0 | 0.02 | [0, 0] | 0 | 0; 144 | 1.0 | 0.02 | [0, 0] | 0 | 0
