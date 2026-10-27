# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 28092.3 ± 581.4 | -7436.8 ± 662.4 | 3407.7 | 0.708 | 0.288 | 0.005 | 0.212 | 0.243 | 0.128 | 0.681 | 30.10 | 137.35 | 0.15 |
| careful | 35529.1 ± 774.7 | nan ± nan | 4189.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.309 | 0.000 | 7.30 | 0.00 | 0.35 |
| stamper | 7349.8 ± 172.2 | -28179.3 ± 811.2 | 1057.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 16.30 | 179.80 | 1.00 |
| hand | 32865.8 ± 466.3 | -2663.3 ± 892.2 | 4571.6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.330 | 0.000 | 11.20 | 0.00 | 0.50 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.212 (12629) / 0.243 (46831) | 0.782 (1070) / 0.819 (5715) | 0.191 (831) / 0.224 (1078) | — / — |
| careful | 0.000 (5335) / 0.000 (52552) | 0.000 (1230) / 0.000 (19185) | 0.000 (1824) / 0.000 (3657) | — / — |
| stamper | 1.000 (3000) / 1.000 (17701) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (12308) / 0.000 (48984) | 0.000 (2682) / 0.000 (20164) | 0.000 (3227) / 0.000 (4067) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.917 | 0.960 | 0.697 (700) | 0.689 (425) | 0.642 (766) | 0.354 (12302) | 0.259 (53961) | 39.650 | 331.650 | 1.636 | 3.464 |
| careful | — | 0.675 | 0.000 (26530) | 0.000 (6574) | 0.000 (4265) | 0.000 (1116) | 0.000 (45298) | 24.600 | 720.300 | 1.174 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21141) | 72.450 | 179.000 | 2.197 | 2.482 |
| hand | — | 0.804 | 0.000 (125) | 0.000 (11846) | 0.000 (20429) | 0.000 (14484) | 0.000 (44548) | 36.000 | 353.450 | 1.366 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 19.250 / 39.800 | 30.100 ± 2.044 | +22.800 ± 2.331 | 115.250 | +106.050 ± 3.177 | 7.500 | 0.196 | 19.850 | +14.950 ± 0.887 | 1838.400 | 0.065 | +0.040 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 27919.708 ± 388.982 | +4809.813 ± 412.753 | 28092.3 ± 581.4 | -7436.8 ± 662.4 | 30.525 | -7.231 ± 0.480 | 21.609 ± 0.330 | +7.871 ± 0.342 | 20.643 | 0.025 | 2291.750 | 19.800 | 20.550 | +4.300 ± 0.581 | 60.866 | 129.650 |
| careful | 23.450 / 39.700 | 7.300 ± 0.508 | — | 9.200 | — | 2.650 | 0.042 | 4.900 | — | 1624.750 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23109.895 ± 390.187 | — | 35529.1 ± 774.7 | — | 37.756 | — | 13.739 ± 0.211 | — | 17.387 | 0.001 | 2632.400 | 19.700 | 16.250 | — | 999.731 | 185.000 |
| stamper | 3.950 / 40.000 | 16.300 ± 0.987 | +9.000 ± 1.326 | 111.250 | +102.050 ± 1.755 | 0.000 | 1.000 | 52.450 | +47.550 ± 1.370 | 885.100 | 0.189 | +0.164 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9235.727 ± 182.151 | -13874.168 ± 409.826 | 7349.8 ± 172.2 | -28179.3 ± 811.2 | 26.772 | -10.984 ± 0.470 | 31.455 ± 0.755 | +17.716 ± 0.875 | 22.777 | 0.201 | 737.650 | 20.000 | 36.050 | +19.800 ± 0.928 | 5739.536 | 113.600 |
| hand | 20.100 / 39.850 | 11.200 ± 0.702 | +3.900 ± 0.954 | 66.450 | +57.250 ± 1.612 | 5.450 | 0.051 | 16.150 | +11.250 ± 0.824 | 1655.650 | 0.063 | +0.038 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30073.813 ± 365.630 | +6963.918 ± 455.932 | 32865.8 ± 466.3 | -2663.3 ± 892.2 | 32.263 | -5.493 ± 0.383 | 19.545 ± 0.380 | +5.806 ± 0.477 | 19.813 | 0.031 | 2385.800 | 19.850 | 19.750 | +3.500 ± 0.478 | 121.124 | 169.150 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.814/0.186/0.000 (594); p1 0.513/0.480/0.007 (497); p2 0.668/0.328/0.004 (308); p3 0.700/0.295/0.004 (235); p4 0.709/0.284/0.008 (228); p5 0.705/0.283/0.012 (225); p6 0.718/0.279/0.004 (209); p7 0.736/0.258/0.006 (204); p8 0.731/0.266/0.003 (203); p9 0.729/0.268/0.002 (202); p10 0.774/0.222/0.004 (190); p11 0.779/0.214/0.006 (169); p12 0.748/0.240/0.012 (87); p13 0.738/0.258/0.005 (55); p14 0.613/0.387/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (591); p1 1.000/0.000/0.000 (732); p2 1.000/0.000/0.000 (856); p3 1.000/0.000/0.000 (918); p4 1.000/0.000/0.000 (805); p5 1.000/0.000/0.000 (280); p6 1.000/0.000/0.000 (6)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (168); p3 0.000/1.000/0.000 (18); p4 0.000/1.000/0.000 (3); p5 0.000/1.000/0.000 (1)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2341.6 / 631.5 | 1.16 / 1.52 | +0.37 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.475 / 0.550 | +0.075 ± 0.010 | 0.261 / 0.315 | 0.025 / 0.000 | 0.156 / 0.185 | +0.029 ± 0.004 | 2.76 / 2.95 | +0.19 ± 0.04 |
| careful | 2627.6 / 266.8 | 0.23 / 0.14 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.06 | -0.00 ± 0.00 | 0.155 / 0.126 | -0.029 ± 0.005 | 0.059 / 0.065 | 0.000 / 0.000 | 0.061 / 0.064 | +0.003 ± 0.004 | 1.52 / 1.27 | -0.25 ± 0.10 |
| stamper | 885.0 / 150.0 | 1.05 / 0.72 | -0.33 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.237 / 0.225 | -0.012 ± 0.009 | 0.133 / 0.129 | 0.167 / 0.000 | 0.103 / 0.078 | -0.025 ± 0.006 | 3.54 / 2.00 | -1.54 ± 0.19 |
| hand | 2449.2 / 615.4 | 0.73 / 0.73 | -0.00 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | -0.00 ± 0.00 | 0.345 / 0.361 | +0.016 ± 0.005 | 0.142 / 0.167 | 0.031 / 0.000 | 0.094 / 0.090 | -0.004 ± 0.004 | 2.61 / 2.38 | -0.23 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | +0.04 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.047 ± 0.004 | -0.018 ± 0.004 | +0.000 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.031 ± 0.005 | +0.006 ± 0.003 | +0.003 ± 0.004 |
| stamper | -0.86 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.174 ± 0.012 | -0.123 ± 0.010 | -0.037 ± 0.006 |
| hand | -0.12 ± 0.01 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.045 ± 0.004 | -0.007 ± 0.004 | -0.006 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.120 / 0.060 | 0.59 / 0.66 | 0.032 / 0.100 | 0.00 / 0.00 | 0.67 / 0.68 | 0.782 / 0.819 |
| careful | 0.363 / 0.103 | 0.40 / 0.40 | 0.040 / 0.162 | 0.00 / 0.00 | 0.30 / 0.28 | 0.304 / 0.324 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.045 | — / 0.00 | — / — | 1.195 / 1.993 |
| hand | 0.406 / 0.158 | 0.12 / 0.14 | 0.033 / 0.104 | 0.00 / 0.00 | 0.07 / 0.11 | 0.319 / 0.257 |
