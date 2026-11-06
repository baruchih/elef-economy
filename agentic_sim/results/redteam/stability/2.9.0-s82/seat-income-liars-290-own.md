# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1; seeds 21–40; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-liars-290-own/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-liars-290-own/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 174 ± 10 | 168 ± 7 | 334 ± 12 | 58.1 | 56.0 | 111.5 |
| member | appeal | real | 1057 ± 28 | 1094 ± 27 | 1434 ± 26 | 475.4 | 499.8 | 621.9 |
| member | audit | plant | 14 ± 4 | 14 ± 3 | 139 ± 9 | 4.8 | 4.8 | 46.4 |
| member | audit | real | 2399 ± 54 | 2434 ± 48 | 2409 ± 43 | 847.5 | 867.8 | 861.5 |
| member | initial | plant | 125 ± 6 | 120 ± 3 | 290 ± 7 | 62.5 | 59.8 | 144.8 |
| member | initial | real | 4905 ± 19 | 4944 ± 17 | 4942 ± 25 | 2604.3 | 2631.2 | 2614.3 |
| state | appeal | real | 725 ± 17 | 668 ± 25 | 730 ± 15 | 334.8 | 309.2 | 314.9 |
| state | audit | real | 1654 ± 46 | 1504 ± 62 | 1445 ± 36 | 569.9 | 516.5 | 485.7 |
| state | initial | real | 2 ± 0 | 1 ± 0 | 7 ± 1 | 0.9 | 0.5 | 3.5 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 8674 ± 95 | 8774 ± 72 | 9548 ± 88 |
| state | 2381 ± 57 | 2173 ± 83 | 2182 ± 43 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 1231 ± 35 | 1262 ± 31 | 1769 ± 33 |
| members' audit-seat fees | 2413 ± 57 | 2449 ± 49 | 2548 ± 47 |
| state's audit-seat fees | 1654 ± 46 | 1504 ± 62 | 1445 ± 36 |
| state's panel fees | 725 ± 17 | 668 ± 25 | 730 ± 15 |
| state's initial-seat fees | 2 ± 0 | 1 ± 0 | 7 ± 1 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 691 ± 16 | 643 ± 15 | 1363 ± 23 |
| bond burned | state | 182 ± 8 | 189 ± 11 | 197 ± 9 |
| court fee won | member | 263 ± 6 | 259 ± 6 | 337 ± 7 |
| members' audits of real approvals (the base), a run | member | 817 ± 18 | 842 ± 18 | 869 ± 18 |
| service fee to Ω | state | 2399 ± 25 | 2381 ± 23 | 2422 ± 11 |
| uplift | member | 177 ± 138 | 98 ± 38 | 3725 ± 84 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 30 | 1.0 | 0.02 | [0, 0] | 0 | 0; 131 | 1.0 | 0.02 | [0, 0] | 0 | 0; 208 | 1.0 | 0.02 | [0, 0] | 0 | 0; 241 | 1.0 | 0.02 | [0, 0] | 0 | 0; 239 | 1.0 | 0.02 | [0, 0] | 0 | 0
- direct seed 22: 14 | 1.0 | 0.02 | [0, 0] | 0 | 0; 64 | 1.0 | 0.02 | [0, 0] | 0 | 0; 179 | 1.0 | 0.02 | [0, 0] | 0 | 0; 245 | 1.0 | 0.02 | [0, 0] | 0 | 0; 243 | 1.0 | 0.02 | [0, 0] | 0 | 0
- direct seed 23: 18 | 1.0 | 0.02 | [0, 0] | 0 | 0; 95 | 1.0 | 0.02 | [0, 0] | 0 | 0; 169 | 1.0 | 0.02 | [0, 0] | 0 | 0; 263 | 1.0 | 0.02 | [0, 0] | 0 | 0; 244 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 21: 54 | 1.0 | 0.02 | [0, 0] | 0 | 0; 105 | 1.0 | 0.02 | [0, 0] | 0 | 0; 249 | 1.0 | 0.02 | [0, 0] | 0 | 0; 241 | 1.0 | 0.02 | [0, 0] | 0 | 0; 125 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 22: 88 | 1.0 | 0.02 | [0, 0] | 0 | 0; 238 | 1.0 | 0.02 | [0, 0] | 0 | 0; 244 | 1.0 | 0.02 | [0, 0] | 0 | 0; 257 | 1.0 | 0.02 | [0, 0] | 0 | 0; 117 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 23: 53 | 1.0 | 0.02 | [0, 0] | 0 | 0; 238 | 1.0 | 0.02 | [0, 0] | 0 | 0; 208 | 1.0 | 0.02 | [0, 0] | 0 | 0; 166 | 1.0 | 0.02 | [0, 0] | 0 | 0; 108 | 1.0 | 0.02 | [0, 0] | 0 | 0; 103 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 21: 73 | 1.0 | 0.02 | [0, 0] | 0 | 0; 108 | 1.0 | 0.02 | [0, 0] | 0 | 0; 59 | 1.0 | 0.02 | [0, 0] | 0 | 0; 69 | 1.0 | 0.02 | [0, 0] | 0 | 0; 82 | 1.0 | 0.02 | [0, 0] | 0 | 0; 100 | 1.0 | 0.02 | [0, 0] | 0 | 0; 90 | 1.0 | 0.02 | [0, 0] | 0 | 0; 85 | 1.0 | 0.02 | [0, 0] | 0 | 0; 105 | 1.0 | 0.02 | [0, 0] | 0 | 0; 106 | 1.0 | 0.02 | [0, 0] | 0 | 0; 75 | 1.0 | 0.02 | [0, 0] | 0 | 0; 94 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 22: 11 | 1.0 | 0.02 | [0, 0] | 0 | 0; 91 | 1.0 | 0.02 | [0, 0] | 0 | 0; 62 | 1.0 | 0.02 | [0, 0] | 0 | 0; 74 | 1.0 | 0.02 | [0, 0] | 0 | 0; 83 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 97 | 1.0 | 0.02 | [0, 0] | 0 | 0; 83 | 1.0 | 0.02 | [0, 0] | 0 | 0; 80 | 1.0 | 0.02 | [0, 0] | 0 | 0; 91 | 1.0 | 0.02 | [0, 0] | 0 | 0; 92 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 23: 41 | 1.0 | 0.02 | [0, 0] | 0 | 0; 82 | 1.0 | 0.02 | [0, 0] | 0 | 0; 59 | 1.0 | 0.02 | [0, 0] | 0 | 0; 77 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 77 | 1.0 | 0.02 | [0, 0] | 0 | 0; 73 | 1.0 | 0.02 | [0, 0] | 0 | 0; 87 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 84 | 1.0 | 0.02 | [0, 0] | 0 | 0; 83 | 1.0 | 0.02 | [0, 0] | 0 | 0; 81 | 1.0 | 0.02 | [0, 0] | 0 | 0
