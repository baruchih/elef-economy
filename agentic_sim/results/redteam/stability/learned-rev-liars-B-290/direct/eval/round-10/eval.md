# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1 --planted-approval off`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29853.6 ± 854.3 | -5025.1 ± 992.0 | 4269.3 | 0.672 | 0.308 | 0.020 | 0.183 | 0.207 | 0.303 | 0.615 | 13.35 | 116.35 | 0.00 |
| careful | 34878.7 ± 853.1 | nan ± nan | 4191.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 | 0.000 | 1.05 | 0.00 | 0.35 |
| stamper | 7124.2 ± 128.7 | -27754.4 ± 887.3 | 1076.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.029 | 1.000 | 9.25 | 187.75 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.183 (12389) / 0.207 (47083) | 0.886 (894) / 0.885 (14311) | 0.203 (4188) / 0.250 (6521) | — / — |
| careful | 0.000 (5154) / 0.000 (50746) | 0.000 (99) / 0.000 (16762) | 0.000 (2198) / 0.000 (8867) | — / — |
| stamper | 1.000 (3034) / 1.000 (17878) | — / 1.000 (343) | — / 1.000 (273) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.871 | 0.933 | 0.585 (1260) | 0.677 (904) | 0.534 (1619) | 0.405 (25243) | 0.247 (56360) | 38.750 | 344.950 | 1.590 | 3.003 |
| careful | — | 0.680 | 0.000 (26476) | 0.000 (5834) | 0.000 (4561) | 0.000 (1325) | 0.000 (45630) | 25.100 | 723.900 | 1.240 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21528) | 74.200 | 176.100 | 2.207 | 2.530 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.350 / 39.700 | 13.350 ± 0.646 | +12.300 ± 0.715 | 95.250 | +85.600 ± 2.514 | 9.600 | 0.176 | 19.050 | +13.600 ± 0.838 | 1510.250 | 0.008 | -0.004 ± 0.001 | 274.200 / 98.500 (102.550 / 93.850) | 29865.420 ± 406.858 | +5764.291 ± 595.244 | 29853.6 ± 854.3 | -5025.1 ± 992.0 | 30.745 | -4.422 ± 0.618 | 21.914 ± 0.782 | +7.127 ± 0.886 | 20.986 | 0.026 | 2305.100 | 19.700 | 20.350 | +5.150 ± 0.693 | 66.576 | 126.950 |
| careful | 24.450 / 39.650 | 1.050 ± 0.198 | — | 9.650 | — | 3.450 | 0.043 | 5.450 | — | 1425.450 | 0.013 | — | 222.700 / 28.800 (25.850 / 25.250) | 24101.129 ± 438.620 | — | 34878.7 ± 853.1 | — | 35.167 | — | 14.787 ± 0.443 | — | 18.563 | 0.007 | 2527.400 | 19.650 | 15.200 | — | 647.046 | 229.350 |
| stamper | 4.200 / 40.000 | 9.250 ± 0.656 | +8.200 ± 0.635 | 111.700 | +102.050 ± 1.558 | 0.000 | 1.000 | 54.200 | +48.750 ± 1.908 | 651.100 | 0.018 | +0.005 ± 0.001 | 245.550 / 166.300 (174.200 / 165.300) | 8391.745 ± 172.653 | -15709.385 ± 525.555 | 7124.2 ± 128.7 | -27754.4 ± 887.3 | 26.711 | -8.456 ± 0.577 | 30.190 ± 0.801 | +15.404 ± 0.969 | 22.785 | 0.256 | 694.100 | 20.000 | 35.800 | +20.600 ± 0.913 | 5688.227 | 169.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.841/0.156/0.003 (610); p1 0.640/0.339/0.021 (533); p2 0.582/0.407/0.011 (357); p3 0.662/0.319/0.019 (274); p4 0.667/0.313/0.020 (284); p5 0.642/0.342/0.016 (303); p6 0.642/0.335/0.023 (302); p7 0.650/0.325/0.025 (297); p8 0.666/0.309/0.025 (292); p9 0.659/0.326/0.016 (297); p10 0.640/0.339/0.021 (300); p11 0.659/0.314/0.027 (239); p12 0.643/0.303/0.054 (124); p13 0.648/0.324/0.028 (45); p14 0.634/0.264/0.102 (13)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (678); p2 1.000/0.000/0.000 (835); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (901); p5 1.000/0.000/0.000 (256); p6 1.000/0.000/0.000 (3)
- **stamper**: p0 0.000/1.000/0.000 (576); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (168); p3 0.000/1.000/0.000 (17); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2354.2 / 619.5 | 1.12 / 1.26 | +0.14 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.05 | -0.00 ± 0.00 | 0.498 / 0.536 | +0.037 ± 0.008 | 0.254 / 0.289 | 0.025 / 0.000 | 0.134 / 0.148 | +0.014 ± 0.003 | 2.76 / 2.78 | +0.02 ± 0.03 |
| careful | 2537.3 / 257.7 | 0.56 / 0.39 | -0.17 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.257 / 0.212 | -0.045 ± 0.009 | 0.106 / 0.112 | 0.007 / 0.000 | 0.072 / 0.063 | -0.009 ± 0.005 | 2.25 / 1.94 | -0.31 ± 0.13 |
| stamper | 893.9 / 151.7 | 1.38 / 0.95 | -0.43 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.304 / 0.294 | -0.010 ± 0.008 | 0.173 / 0.172 | 0.223 / 0.000 | 0.114 / 0.080 | -0.034 ± 0.005 | 3.70 / 2.99 | -0.71 ± 0.41 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.02 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.056 ± 0.004 | -0.021 ± 0.004 | -0.001 ± 0.003 |
| careful | -0.16 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.047 ± 0.009 | +0.005 ± 0.005 | -0.009 ± 0.005 |
| stamper | -0.93 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.174 ± 0.012 | -0.123 ± 0.011 | -0.042 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.298 / 0.071 | 0.46 / 0.43 | 0.175 / 0.396 | 0.00 / 0.00 | 0.47 / 0.45 | 0.576 / 0.480 |
| careful | 0.328 / 0.019 | 0.38 / 0.53 | 0.145 / 0.412 | 0.00 / 0.00 | 0.31 / 0.32 | 0.382 / 0.428 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.271 / 0.999 | 0.00 / 0.00 | 0.00 / — | 1.279 / 1.999 |
