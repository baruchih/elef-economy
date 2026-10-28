# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29255.1 ± 496.9 | -5676.0 ± 546.4 | 4153.7 | 0.679 | 0.305 | 0.016 | 0.196 | 0.216 | 0.287 | 0.597 | 10.45 | 115.05 | 0.20 |
| careful | 34931.1 ± 788.2 | nan ± nan | 4254.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.339 | 0.000 | 1.70 | 0.00 | 0.40 |
| stamper | 7124.2 ± 128.7 | -27806.9 ± 837.7 | 1076.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.029 | 1.000 | 9.25 | 187.75 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.196 (12823) / 0.216 (46390) | 0.850 (760) / 0.853 (13156) | 0.220 (4135) / 0.254 (5810) | — / — |
| careful | 0.000 (5190) / 0.000 (51027) | 0.000 (117) / 0.000 (17160) | 0.000 (2625) / 0.000 (8979) | — / — |
| stamper | 1.000 (3034) / 1.000 (17878) | — / 1.000 (343) | — / 1.000 (273) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.900 | 0.937 | 0.569 (677) | 0.497 (702) | 0.438 (1209) | 0.389 (23208) | 0.264 (57278) | 37.500 | 318.800 | 1.661 | 3.068 |
| careful | — | 0.684 | 0.000 (26258) | 0.000 (6098) | 0.000 (4898) | 0.000 (1223) | 0.000 (46621) | 24.800 | 736.000 | 1.222 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21528) | 74.200 | 176.100 | 2.207 | 2.530 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.700 / 39.900 | 10.450 ± 0.857 | +8.750 ± 0.994 | 103.250 | +93.950 ± 2.420 | 10.100 | 0.166 | 17.600 | +12.450 ± 0.783 | 1505.800 | 0.009 | -0.004 ± 0.001 | 277.650 / 104.550 (107.200 / 100.500) | 29950.171 ± 329.410 | +6505.658 ± 429.704 | 29255.1 ± 496.9 | -5676.0 ± 546.4 | 30.388 | -5.016 ± 0.566 | 22.249 ± 0.336 | +7.897 ± 0.394 | 21.004 | 0.020 | 2281.000 | 19.900 | 21.200 | +5.750 ± 0.512 | 72.379 | 119.550 |
| careful | 24.200 / 39.650 | 1.700 ± 0.349 | — | 9.300 | — | 3.200 | 0.045 | 5.150 | — | 1454.650 | 0.013 | — | 224.050 / 31.500 (28.100 / 27.450) | 23444.514 ± 399.404 | — | 34931.1 ± 788.2 | — | 35.404 | — | 14.352 ± 0.339 | — | 18.284 | 0.006 | 2542.650 | 19.650 | 15.450 | — | 685.274 | 239.800 |
| stamper | 4.200 / 40.000 | 9.250 ± 0.656 | +7.550 ± 0.573 | 111.700 | +102.400 ± 1.338 | 0.000 | 1.000 | 54.200 | +49.050 ± 1.737 | 651.100 | 0.018 | +0.006 ± 0.001 | 245.550 / 166.300 (174.200 / 165.300) | 8391.745 ± 172.653 | -15052.769 ± 460.866 | 7124.2 ± 128.7 | -27806.9 ± 837.7 | 26.711 | -8.693 ± 0.521 | 30.190 ± 0.801 | +15.838 ± 0.898 | 22.785 | 0.256 | 694.100 | 20.000 | 35.800 | +20.350 ± 0.865 | 5688.227 | 169.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.816/0.181/0.002 (600); p1 0.579/0.404/0.016 (474); p2 0.693/0.292/0.015 (322); p3 0.686/0.277/0.037 (282); p4 0.620/0.360/0.021 (292); p5 0.621/0.360/0.018 (292); p6 0.641/0.345/0.014 (286); p7 0.651/0.332/0.018 (283); p8 0.677/0.305/0.018 (271); p9 0.691/0.298/0.010 (272); p10 0.703/0.287/0.010 (276); p11 0.658/0.325/0.016 (234); p12 0.698/0.267/0.035 (163); p13 0.662/0.307/0.031 (92); p14 0.639/0.349/0.011 (13)
- **careful**: p0 1.000/0.000/0.000 (602); p1 1.000/0.000/0.000 (687); p2 1.000/0.000/0.000 (835); p3 1.000/0.000/0.000 (924); p4 1.000/0.000/0.000 (935); p5 1.000/0.000/0.000 (260); p6 1.000/0.000/0.000 (11)
- **stamper**: p0 0.000/1.000/0.000 (576); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (168); p3 0.000/1.000/0.000 (17); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2319.5 / 641.1 | 1.21 / 1.46 | +0.24 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.04 | -0.01 ± 0.00 | 0.481 / 0.528 | +0.046 ± 0.006 | 0.255 / 0.298 | 0.019 / 0.000 | 0.143 / 0.158 | +0.016 ± 0.004 | 2.96 / 3.12 | +0.16 ± 0.05 |
| careful | 2551.3 / 259.5 | 0.50 / 0.36 | -0.14 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.254 / 0.218 | -0.036 ± 0.005 | 0.106 / 0.122 | 0.006 / 0.000 | 0.070 / 0.066 | -0.004 ± 0.003 | 2.13 / 1.85 | -0.28 ± 0.07 |
| stamper | 893.9 / 151.7 | 1.38 / 0.95 | -0.43 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.304 / 0.294 | -0.010 ± 0.008 | 0.173 / 0.172 | 0.223 / 0.000 | 0.114 / 0.080 | -0.034 ± 0.005 | 3.70 / 2.99 | -0.71 ± 0.41 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.01 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.055 ± 0.003 | -0.022 ± 0.003 | -0.004 ± 0.004 |
| careful | -0.14 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.038 ± 0.005 | +0.014 ± 0.005 | -0.003 ± 0.004 |
| stamper | -0.93 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.174 ± 0.012 | -0.123 ± 0.011 | -0.042 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.279 / 0.058 | 0.51 / 0.50 | 0.177 / 0.421 | 0.00 / 0.00 | 0.51 / 0.53 | 0.622 / 0.562 |
| careful | 0.334 / 0.022 | 0.39 / 0.36 | 0.146 / 0.471 | 0.00 / 0.00 | 0.33 / 0.34 | 0.385 / 0.464 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.271 / 0.999 | 0.00 / 0.00 | 0.00 / — | 1.279 / 1.999 |
