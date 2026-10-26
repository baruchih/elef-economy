# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-stamper-280/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 27124.5 ± 419.0 | -8044.6 ± 858.5 | 3219.6 | 0.699 | 0.300 | 0.001 | 0.199 | 0.231 | 0.118 | 0.873 | 29.70 | 121.70 | 0.10 |
| careful | 35169.1 ± 847.0 | nan ± nan | 4052.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.285 | 0.000 | 6.65 | 0.00 | 0.30 |
| stamper | 7002.0 ± 181.5 | -28167.1 ± 878.4 | 1063.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.20 | 182.10 | 1.00 |
| hand | 31529.1 ± 741.8 | -3640.0 ± 1009.0 | 4380.8 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.310 | 0.000 | 11.40 | 0.00 | 0.45 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.199 (12131) / 0.231 (44651) | 0.981 (856) / 0.986 (5666) | 0.194 (248) / 0.202 (840) | — / — |
| careful | 0.000 (5287) / 0.000 (52624) | 0.000 (642) / 0.000 (18617) | 0.000 (212) / 0.000 (3663) | — / — |
| stamper | 1.000 (3039) / 1.000 (17796) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (12204) / 0.000 (48258) | 0.000 (2418) / 0.000 (19945) | 0.000 (846) / 0.000 (3945) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.911 | 0.948 | 0.745 (372) | 0.770 (549) | 0.757 (432) | 0.342 (15815) | 0.273 (47224) | 43.850 | 276.000 | 1.661 | 2.775 |
| careful | — | 0.683 | 0.000 (25595) | 0.000 (5019) | 0.000 (4705) | 0.000 (979) | 0.000 (44747) | 24.950 | 697.400 | 1.149 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21275) | 74.950 | 179.350 | 2.172 | 2.430 |
| hand | — | 0.815 | 0.000 (32) | 0.000 (9872) | 0.000 (18254) | 0.000 (15267) | 0.000 (44191) | 36.400 | 350.600 | 1.364 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.300 / 39.700 | 29.700 ± 1.982 | +23.050 ± 2.222 | 105.250 | +95.050 ± 1.924 | 6.450 | 0.143 | 24.150 | +18.900 ± 0.695 | 1749.050 | 0.061 | +0.036 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 28977.087 ± 422.543 | +5660.550 ± 397.360 | 27124.5 ± 419.0 | -8044.6 ± 858.5 | 29.280 | -8.247 ± 0.375 | 22.967 ± 0.243 | +8.898 ± 0.455 | 21.619 | 0.043 | 2142.800 | 19.700 | 22.400 | +6.200 ± 0.468 | 73.784 | 132.500 |
| careful | 23.500 / 39.700 | 6.650 ± 0.568 | — | 10.200 | — | 3.300 | 0.054 | 5.250 | — | 1616.850 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23316.537 ± 373.976 | — | 35169.1 ± 847.0 | — | 37.527 | — | 14.069 ± 0.359 | — | 17.542 | 0.001 | 2634.850 | 19.700 | 16.200 | — | 949.449 | 211.850 |
| stamper | 3.850 / 40.000 | 14.200 ± 0.647 | +7.550 ± 0.872 | 113.550 | +103.350 ± 2.769 | 0.000 | 1.000 | 54.950 | +49.700 ± 2.549 | 889.800 | 0.192 | +0.166 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9049.254 ± 151.120 | -14267.283 ± 352.384 | 7002.0 ± 181.5 | -28167.1 ± 878.4 | 26.601 | -10.926 ± 0.434 | 32.597 ± 0.855 | +18.528 ± 0.935 | 22.720 | 0.223 | 721.000 | 20.000 | 36.150 | +19.950 ± 0.972 | 5688.290 | 130.000 |
| hand | 19.750 / 39.900 | 11.400 ± 0.741 | +4.750 ± 0.867 | 65.950 | +55.750 ± 1.686 | 7.250 | 0.055 | 16.500 | +11.250 ± 0.912 | 1638.350 | 0.062 | +0.036 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30504.185 ± 388.945 | +7187.648 ± 366.959 | 31529.1 ± 741.8 | -3640.0 ± 1009.0 | 31.511 | -6.016 ± 0.408 | 21.146 ± 0.555 | +7.077 ± 0.653 | 20.493 | 0.025 | 2365.950 | 19.900 | 20.150 | +3.950 ± 0.587 | 64.918 | 193.700 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.828/0.169/0.003 (590); p1 0.493/0.505/0.003 (456); p2 0.472/0.527/0.000 (290); p3 0.676/0.324/0.000 (216); p4 0.705/0.295/0.000 (202); p5 0.739/0.261/0.000 (196); p6 0.794/0.206/0.000 (194); p7 0.802/0.198/0.000 (194); p8 0.784/0.216/0.000 (198); p9 0.761/0.239/0.000 (209); p10 0.730/0.270/0.000 (218); p11 0.725/0.275/0.000 (164); p12 0.715/0.285/0.000 (77); p13 0.719/0.281/0.000 (14)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (705); p2 1.000/0.000/0.000 (830); p3 1.000/0.000/0.000 (911); p4 1.000/0.000/0.000 (773); p5 1.000/0.000/0.000 (239)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (170); p3 0.000/1.000/0.000 (24); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2232.6 / 606.5 | 1.56 / 2.11 | +0.55 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.03 | -0.01 ± 0.00 | 0.532 / 0.635 | +0.102 ± 0.006 | 0.326 / 0.404 | 0.043 / 0.068 | 0.198 / 0.251 | +0.052 ± 0.003 | 3.31 / 3.61 | +0.30 ± 0.04 |
| careful | 2631.2 / 264.4 | 0.23 / 0.12 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.162 / 0.128 | -0.034 ± 0.005 | 0.061 / 0.066 | 0.000 / 0.000 | 0.062 / 0.060 | -0.002 ± 0.004 | 1.48 / 1.24 | -0.24 ± 0.08 |
| stamper | 889.8 / 151.9 | 1.07 / 0.79 | -0.28 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.229 / 0.217 | -0.012 ± 0.008 | 0.128 / 0.128 | 0.189 / 0.270 | 0.098 / 0.068 | -0.030 ± 0.006 | 3.38 / 2.26 | -1.13 ± 0.27 |
| hand | 2412.9 / 610.2 | 0.91 / 0.91 | +0.00 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | -0.00 ± 0.00 | 0.375 / 0.380 | +0.005 ± 0.005 | 0.167 / 0.186 | 0.025 / 0.028 | 0.109 / 0.104 | -0.005 ± 0.003 | 2.78 / 2.59 | -0.20 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.06 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.050 ± 0.003 | -0.031 ± 0.004 | +0.008 ± 0.003 |
| careful | -0.11 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.037 ± 0.005 | +0.004 ± 0.003 | -0.002 ± 0.004 |
| stamper | -0.80 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.163 ± 0.012 | -0.110 ± 0.009 | -0.041 ± 0.007 |
| hand | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.052 ± 0.004 | -0.013 ± 0.003 | -0.007 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.125 / 0.068 | 0.57 / 0.56 | 0.027 / 0.011 | 0.00 / 0.00 | 0.52 / 0.70 | 0.767 / 0.454 |
| careful | 0.351 / 0.120 | 0.36 / 0.42 | 0.040 / 0.012 | 0.00 / 0.00 | 0.29 / 0.39 | 0.313 / 0.130 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.196 / 1.717 |
| hand | 0.407 / 0.196 | 0.11 / 0.14 | 0.033 / 0.012 | 0.00 / 0.00 | 0.07 / 0.10 | 0.323 / 0.174 |
