# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1 --planted-approval off`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-liars-B-290/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 27608.8 ± 545.7 | -7269.9 ± 707.7 | 4245.7 | 0.662 | 0.324 | 0.014 | 0.193 | 0.211 | 0.336 | 0.595 | 9.90 | 102.60 | 0.05 |
| careful | 34878.7 ± 853.1 | nan ± nan | 4191.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 | 0.000 | 1.05 | 0.00 | 0.35 |
| stamper | 7124.2 ± 128.7 | -27754.4 ± 887.3 | 1076.4 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.029 | 1.000 | 9.25 | 187.75 | 1.00 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.193 (12273) / 0.211 (44085) | 0.962 (943) / 0.960 (15450) | 0.090 (5168) / 0.113 (6995) | — / — |
| careful | 0.000 (5154) / 0.000 (50746) | 0.000 (99) / 0.000 (16762) | 0.000 (2198) / 0.000 (8867) | — / — |
| stamper | 1.000 (3034) / 1.000 (17878) | — / 1.000 (343) | — / 1.000 (273) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.877 | 0.914 | 0.713 (498) | 0.589 (1382) | 0.517 (961) | 0.359 (31770) | 0.287 (50303) | 43.400 | 244.150 | 1.711 | 2.364 |
| careful | — | 0.680 | 0.000 (26476) | 0.000 (5834) | 0.000 (4561) | 0.000 (1325) | 0.000 (45630) | 25.100 | 723.900 | 1.240 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21528) | 74.200 | 176.100 | 2.207 | 2.530 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.100 / 39.750 | 9.900 ± 0.750 | +8.850 ± 0.799 | 100.900 | +91.250 ± 2.474 | 7.700 | 0.192 | 23.650 | +18.200 ± 0.810 | 1411.700 | 0.007 | -0.006 ± 0.001 | 258.050 / 104.200 (102.250 / 98.950) | 32015.643 ± 385.732 | +7914.514 ± 471.438 | 27608.8 ± 545.7 | -7269.9 ± 707.7 | 28.685 | -6.482 ± 0.558 | 24.904 ± 0.347 | +10.117 ± 0.479 | 22.782 | 0.057 | 2092.750 | 19.750 | 22.650 | +7.450 ± 0.573 | 71.974 | 137.200 |
| careful | 24.450 / 39.650 | 1.050 ± 0.198 | — | 9.650 | — | 3.450 | 0.043 | 5.450 | — | 1425.450 | 0.013 | — | 222.700 / 28.800 (25.850 / 25.250) | 24101.129 ± 438.620 | — | 34878.7 ± 853.1 | — | 35.167 | — | 14.787 ± 0.443 | — | 18.563 | 0.007 | 2527.400 | 19.650 | 15.200 | — | 647.046 | 229.350 |
| stamper | 4.200 / 40.000 | 9.250 ± 0.656 | +8.200 ± 0.635 | 111.700 | +102.050 ± 1.558 | 0.000 | 1.000 | 54.200 | +48.750 ± 1.908 | 651.100 | 0.018 | +0.005 ± 0.001 | 245.550 / 166.300 (174.200 / 165.300) | 8391.745 ± 172.653 | -15709.385 ± 525.555 | 7124.2 ± 128.7 | -27754.4 ± 887.3 | 26.711 | -8.456 ± 0.577 | 30.190 ± 0.801 | +15.404 ± 0.969 | 22.785 | 0.256 | 694.100 | 20.000 | 35.800 | +20.600 ± 0.913 | 5688.227 | 169.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.813/0.187/0.000 (594); p1 0.530/0.468/0.002 (476); p2 0.558/0.430/0.012 (339); p3 0.674/0.296/0.030 (299); p4 0.668/0.304/0.028 (306); p5 0.667/0.323/0.010 (310); p6 0.661/0.330/0.009 (304); p7 0.662/0.331/0.007 (305); p8 0.658/0.331/0.011 (310); p9 0.644/0.341/0.015 (314); p10 0.680/0.296/0.024 (275); p11 0.668/0.299/0.033 (237); p12 0.675/0.282/0.044 (154); p13 0.690/0.302/0.008 (24)
- **careful**: p0 1.000/0.000/0.000 (599); p1 1.000/0.000/0.000 (678); p2 1.000/0.000/0.000 (835); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (901); p5 1.000/0.000/0.000 (256); p6 1.000/0.000/0.000 (3)
- **stamper**: p0 0.000/1.000/0.000 (576); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (168); p3 0.000/1.000/0.000 (17); p4 0.000/1.000/0.000 (8); p5 0.000/1.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2204.2 / 613.6 | 1.83 / 2.29 | +0.46 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.01 ± 0.00 | 0.578 / 0.667 | +0.089 ± 0.004 | 0.346 / 0.414 | 0.056 / 0.000 | 0.210 / 0.257 | +0.047 ± 0.005 | 3.59 / 3.83 | +0.24 ± 0.05 |
| careful | 2537.3 / 257.7 | 0.56 / 0.39 | -0.17 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.257 / 0.212 | -0.045 ± 0.009 | 0.106 / 0.112 | 0.007 / 0.000 | 0.072 / 0.063 | -0.009 ± 0.005 | 2.25 / 1.94 | -0.31 ± 0.13 |
| stamper | 893.9 / 151.7 | 1.38 / 0.95 | -0.43 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.304 / 0.294 | -0.010 ± 0.008 | 0.173 / 0.172 | 0.223 / 0.000 | 0.114 / 0.080 | -0.034 ± 0.005 | 3.70 / 2.99 | -0.71 ± 0.41 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.02 ± 0.03 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.047 ± 0.003 | -0.035 ± 0.004 | +0.005 ± 0.006 |
| careful | -0.16 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.047 ± 0.009 | +0.005 ± 0.005 | -0.009 ± 0.005 |
| stamper | -0.93 ± 0.05 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.174 ± 0.012 | -0.123 ± 0.011 | -0.042 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.345 / 0.075 | 0.37 / 0.37 | 0.167 / 0.392 | 0.00 / 0.00 | 0.38 / 0.35 | 0.487 / 0.387 |
| careful | 0.328 / 0.019 | 0.38 / 0.53 | 0.145 / 0.412 | 0.00 / 0.00 | 0.31 / 0.32 | 0.382 / 0.428 |
| stamper | 0.019 / 0.000 | 0.01 / — | 0.271 / 0.999 | 0.00 / 0.00 | 0.00 / — | 1.279 / 1.999 |
