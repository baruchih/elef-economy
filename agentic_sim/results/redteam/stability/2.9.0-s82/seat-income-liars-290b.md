# §8.6: the review fees by seat and by who sat — --entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1; seeds 21–30; the finals' direct (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-liars-290b/direct/models/direct-online-10.pt) and head alone (/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-liars-290b/wm/models/wm-online-10.pt), the hand beside. Nominal credits a run, means ± SE over the seeds. A seat's fee is the fixed fee paid from the fee pot at settlement (`feepot_out … review fee`); who sat: a member, the state (a troop), the plant alias (never paid — a check). Beside: the duty uplift paid, the court fees the state won, the bonds burned.

| who sat | seat | case kind | direct | head alone | hand | direct (seats) | head alone (seats) | hand (seats) |
|---|---|---|---|---|---|---|---|---|
| member | appeal | plant | 209 ± 18 | 166 ± 16 | 361 ± 19 | 69.8 | 55.3 | 120.2 |
| member | appeal | real | 950 ± 54 | 798 ± 59 | 1453 ± 41 | 378.7 | 301.1 | 632.0 |
| member | audit | plant | 70 ± 11 | 94 ± 14 | 125 ± 11 | 23.5 | 31.2 | 41.7 |
| member | audit | real | 1922 ± 81 | 1761 ± 68 | 2409 ± 68 | 673.6 | 593.4 | 859.9 |
| member | initial | plant | 283 ± 7 | 266 ± 7 | 288 ± 9 | 141.6 | 133.1 | 144.1 |
| member | initial | real | 4751 ± 30 | 4538 ± 44 | 4930 ± 24 | 2506.9 | 2351.5 | 2606.6 |
| state | appeal | real | 1255 ± 29 | 1211 ± 41 | 724 ± 16 | 562.4 | 519.9 | 311.2 |
| state | audit | real | 2498 ± 90 | 2498 ± 79 | 1431 ± 53 | 859.6 | 851.4 | 479.7 |
| state | initial | real | 5 ± 2 | 6 ± 2 | 5 ± 1 | 2.4 | 3.0 | 2.7 |

Totals by who sat (review fees a run):

| who sat | direct | head alone | hand |
|---|---|---|---|
| member | 8185 ± 131 | 7624 ± 141 | 9566 ± 129 |
| state | 3758 ± 115 | 3714 ± 110 | 2160 ± 52 |
| plant alias | 0 ± 0 | 0 ± 0 | 0 ± 0 |

The members' panel income (appeal + dispute seats, real and plant) and the state's audit-seat income:

| reading | direct | head alone | hand |
|---|---|---|---|
| members' panel fees | 1159 ± 68 | 964 ± 72 | 1813 ± 51 |
| members' audit-seat fees | 1992 ± 82 | 1855 ± 70 | 2534 ± 72 |
| state's audit-seat fees | 2498 ± 90 | 2498 ± 79 | 1431 ± 53 |
| state's panel fees | 1255 ± 29 | 1211 ± 41 | 724 ± 16 |
| state's initial-seat fees | 5 ± 2 | 6 ± 2 | 5 ± 1 |

Beside:

| flow | to / from | direct | head alone | hand |
|---|---|---|---|---|
| bond burned | member | 1632 ± 46 | 1461 ± 44 | 1356 ± 41 |
| bond burned | state | 345 ± 18 | 361 ± 17 | 189 ± 13 |
| court fee won | member | 413 ± 11 | 373 ± 10 | 339 ± 12 |
| members' audits of real approvals (the base), a run | member | 652 ± 23 | 573 ± 25 | 860 ± 27 |
| service fee to Ω | state | 2446 ± 11 | 2488 ± 13 | 2424 ± 16 |
| uplift | member | 3920 ± 145 | 3887 ± 152 | 3684 ± 110 |

The dial per seat's path by period (seed: real member audits of real approvals | m^A | π^A | pool A [hit, adj] | pa adjudicated | confirmed):

- direct seed 21: 59 | 1.0 | 0.02 | [0, 0] | 0 | 0; 87 | 1.0 | 0.02 | [0, 0] | 0 | 0; 115 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 65 | 1.0 | 0.02 | [0, 0] | 0 | 0; 44 | 1.0 | 0.02 | [0, 0] | 0 | 0; 27 | 1.0 | 0.02 | [0, 0] | 0 | 0; 45 | 1.0 | 0.02 | [0, 0] | 0 | 0; 40 | 1.0 | 0.02 | [0, 0] | 0 | 0; 57 | 1.0 | 0.02 | [0, 0] | 0 | 0; 82 | 1.0 | 0.02 | [0, 0] | 0 | 0
- direct seed 22: 29 | 1.0 | 0.02 | [0, 0] | 0 | 0; 38 | 1.0 | 0.02 | [0, 0] | 0 | 0; 105 | 1.0 | 0.02 | [0, 0] | 0 | 0; 38 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 0] | 0 | 0; 67 | 1.0 | 0.02 | [0, 0] | 0 | 0; 75 | 1.0 | 0.02 | [0, 0] | 0 | 0; 68 | 1.0 | 0.02 | [0, 0] | 0 | 0; 69 | 1.0 | 0.02 | [0, 0] | 0 | 0; 74 | 1.0 | 0.02 | [0, 0] | 0 | 0; 16 | 1.0 | 0.02 | [0, 0] | 0 | 0
- direct seed 23: 16 | 1.0 | 0.02 | [0, 0] | 0 | 0; 19 | 1.0 | 0.02 | [0, 0] | 0 | 0; 71 | 1.0 | 0.02 | [0, 0] | 0 | 0; 71 | 1.0 | 0.02 | [0, 0] | 0 | 0; 76 | 1.0 | 0.02 | [0, 0] | 0 | 0; 69 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 0] | 0 | 0; 54 | 1.0 | 0.02 | [0, 0] | 0 | 0; 49 | 1.0 | 0.02 | [0, 0] | 0 | 0; 57 | 1.0 | 0.02 | [0, 0] | 0 | 0; 57 | 1.0 | 0.02 | [0, 0] | 0 | 0; 46 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 21: 44 | 1.0 | 0.02 | [0, 0] | 0 | 0; 100 | 1.0 | 0.02 | [0, 0] | 0 | 0; 13 | 1.0 | 0.02 | [0, 0] | 0 | 0; 25 | 1.0 | 0.02 | [0, 0] | 0 | 0; 12 | 1.0 | 0.02 | [0, 0] | 0 | 0; 34 | 1.0 | 0.02 | [0, 0] | 0 | 0; 32 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 0] | 0 | 0; 38 | 1.0 | 0.02 | [0, 0] | 0 | 0; 58 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 22: 14 | 1.0 | 0.02 | [0, 0] | 0 | 0; 0 | 1.0 | 0.02 | [0, 0] | 0 | 0; 2 | 1.0 | 0.02 | [0, 0] | 0 | 0; 42 | 1.0 | 0.02 | [0, 0] | 0 | 0; 58 | 1.0 | 0.02 | [0, 0] | 0 | 0; 58 | 1.0 | 0.02 | [0, 0] | 0 | 0; 56 | 1.0 | 0.02 | [0, 0] | 0 | 0; 72 | 1.0 | 0.02 | [0, 0] | 0 | 0; 87 | 1.0 | 0.02 | [0, 0] | 0 | 0; 53 | 1.0 | 0.02 | [0, 0] | 0 | 0; 50 | 1.0 | 0.02 | [0, 0] | 0 | 0; 30 | 1.0 | 0.02 | [0, 0] | 0 | 0
- head alone seed 23: 17 | 1.0 | 0.02 | [0, 0] | 0 | 0; 110 | 1.0 | 0.02 | [0, 0] | 0 | 0; 117 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 0] | 0 | 0; 52 | 1.0 | 0.02 | [0, 0] | 0 | 0; 69 | 1.0 | 0.02 | [0, 0] | 0 | 0; 60 | 1.0 | 0.02 | [0, 0] | 0 | 0; 38 | 1.0 | 0.02 | [0, 0] | 0 | 0; 38 | 1.0 | 0.02 | [0, 0] | 0 | 0; 47 | 1.0 | 0.02 | [0, 0] | 0 | 0; 38 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 21: 73 | 1.0 | 0.02 | [0, 0] | 0 | 0; 108 | 1.0 | 0.02 | [0, 0] | 0 | 0; 59 | 1.0 | 0.02 | [0, 0] | 0 | 0; 69 | 1.0 | 0.02 | [0, 0] | 0 | 0; 82 | 1.0 | 0.02 | [0, 0] | 0 | 0; 100 | 1.0 | 0.02 | [0, 0] | 0 | 0; 90 | 1.0 | 0.02 | [0, 0] | 0 | 0; 85 | 1.0 | 0.02 | [0, 0] | 0 | 0; 105 | 1.0 | 0.02 | [0, 0] | 0 | 0; 106 | 1.0 | 0.02 | [0, 0] | 0 | 0; 75 | 1.0 | 0.02 | [0, 0] | 0 | 0; 94 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 22: 11 | 1.0 | 0.02 | [0, 0] | 0 | 0; 91 | 1.0 | 0.02 | [0, 0] | 0 | 0; 62 | 1.0 | 0.02 | [0, 0] | 0 | 0; 74 | 1.0 | 0.02 | [0, 0] | 0 | 0; 83 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 97 | 1.0 | 0.02 | [0, 0] | 0 | 0; 83 | 1.0 | 0.02 | [0, 0] | 0 | 0; 80 | 1.0 | 0.02 | [0, 0] | 0 | 0; 91 | 1.0 | 0.02 | [0, 0] | 0 | 0; 92 | 1.0 | 0.02 | [0, 0] | 0 | 0
- hand seed 23: 41 | 1.0 | 0.02 | [0, 0] | 0 | 0; 82 | 1.0 | 0.02 | [0, 0] | 0 | 0; 59 | 1.0 | 0.02 | [0, 0] | 0 | 0; 77 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 77 | 1.0 | 0.02 | [0, 0] | 0 | 0; 73 | 1.0 | 0.02 | [0, 0] | 0 | 0; 87 | 1.0 | 0.02 | [0, 0] | 0 | 0; 79 | 1.0 | 0.02 | [0, 0] | 0 | 0; 84 | 1.0 | 0.02 | [0, 0] | 0 | 0; 83 | 1.0 | 0.02 | [0, 0] | 0 | 0; 81 | 1.0 | 0.02 | [0, 0] | 0 | 0
