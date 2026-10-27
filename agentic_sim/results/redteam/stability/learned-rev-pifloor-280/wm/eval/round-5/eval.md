# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial off`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-pifloor-280/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 25746.8 ± 423.4 | -9062.4 ± 752.5 | 2866.3 | 0.509 | 0.491 | 0.000 | 0.440 | 0.456 | 0.095 | 0.845 | 94.50 | 240.80 | 0.05 |
| careful | 34809.2 ± 647.5 | nan ± nan | 4039.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.289 | 0.000 | 5.70 | 0.00 | 0.35 |
| stamper | 10017.9 ± 321.2 | -24791.4 ± 621.0 | 1874.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.012 | 1.000 | 23.05 | 345.40 | 0.85 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.440 (4667) / 0.456 (47212) | 0.945 (220) / 0.950 (4337) | 0.284 (109) / 0.307 (782) | — / — |
| careful | 0.000 (5180) / 0.000 (52256) | 0.000 (575) / 0.000 (18957) | 0.000 (192) / 0.000 (3631) | — / — |
| stamper | 1.000 (3324) / 1.000 (33716) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.660 | 0.955 | 0.914 (9005) | 0.857 (2547) | 0.818 (4402) | 0.431 (859) | 0.340 (40514) | 57.650 | 530.500 | 1.919 | 4.177 |
| careful | — | 0.665 | 0.000 (26978) | 0.000 (5546) | 0.000 (4306) | 0.000 (1030) | 0.000 (42931) | 24.850 | 661.650 | 1.211 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (37480) | 86.350 | 352.150 | 2.152 | 4.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.850 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 18.700 / 39.750 | 94.500 ± 5.165 | +88.800 ± 5.140 | 81.550 | +71.300 ± 1.982 | 1.450 | 0.647 | 37.900 | +32.650 ± 0.918 | 1683.950 | 0.087 | +0.061 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 28530.927 ± 381.135 | +5300.214 ± 388.129 | 25746.8 ± 423.4 | -9062.4 ± 752.5 | 30.878 | -6.894 ± 0.383 | 23.984 ± 0.406 | +9.987 ± 0.468 | 22.190 | 0.008 | 2345.550 | 19.750 | 21.050 | +3.600 ± 0.432 | 82.967 | 190.650 |
| careful | 22.150 / 39.600 | 5.700 ± 0.607 | — | 10.250 | — | 2.850 | 0.046 | 5.250 | — | 1578.650 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23230.713 ± 394.109 | — | 34809.2 ± 647.5 | — | 37.772 | — | 13.997 ± 0.283 | — | 17.491 | 0.001 | 2618.250 | 19.600 | 17.450 | — | 1033.546 | 228.900 |
| stamper | 7.750 / 40.000 | 23.050 ± 1.258 | +17.350 ± 1.346 | 124.900 | +114.650 ± 1.667 | 0.000 | 1.000 | 66.350 | +61.100 ± 1.347 | 1683.550 | 0.198 | +0.172 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 14114.807 ± 394.301 | -9115.907 ± 566.436 | 10017.9 ± 321.2 | -24791.4 ± 621.0 | 25.385 | -12.387 ± 0.282 | 32.823 ± 0.595 | +18.826 ± 0.567 | 25.271 | 0.406 | 1023.150 | 20.000 | 32.250 | +14.800 ± 0.854 | 1348.683 | 145.950 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.805/0.195/0.000 (583); p1 0.514/0.486/0.000 (581); p2 0.461/0.539/0.000 (580); p3 0.422/0.578/0.000 (576); p4 0.320/0.680/0.000 (517); p5 0.450/0.550/0.000 (28)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (748); p2 1.000/0.000/0.000 (870); p3 1.000/0.000/0.000 (896); p4 1.000/0.000/0.000 (772); p5 1.000/0.000/0.000 (158)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (454); p2 0.000/1.000/0.000 (388); p3 0.000/1.000/0.000 (356); p4 0.000/1.000/0.000 (117)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2360.6 / 233.3 | 0.94 / 0.90 | -0.04 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.412 / 0.354 | -0.058 ± 0.007 | 0.152 / 0.146 | 0.008 / 0.010 | 0.125 / 0.129 | +0.004 ± 0.005 | 2.73 / 2.59 | -0.13 ± 0.11 |
| careful | 2612.8 / 259.0 | 0.18 / 0.10 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.01 ± 0.00 | 0.130 / 0.101 | -0.029 ± 0.006 | 0.045 / 0.052 | 0.000 / 0.000 | 0.064 / 0.071 | +0.007 ± 0.004 | 1.53 / 1.27 | -0.25 ± 0.07 |
| stamper | 1685.8 / 166.2 | 1.67 / 1.21 | -0.46 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.502 / 0.400 | -0.103 ± 0.005 | 0.324 / 0.273 | 0.393 / 0.354 | 0.110 / 0.093 | -0.017 ± 0.004 | 4.12 / 2.92 | -1.20 ± 0.26 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.04 ± 0.03 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.058 ± 0.007 | -0.006 ± 0.006 | +0.004 ± 0.005 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.029 ± 0.006 | +0.007 ± 0.003 | +0.007 ± 0.004 |
| stamper | -0.46 ± 0.03 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.103 ± 0.005 | -0.052 ± 0.008 | -0.017 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.092 / 0.047 | 0.59 / 0.68 | 0.022 / 0.006 | 0.00 / 0.00 | 0.51 / 0.50 | 0.734 / 0.599 |
| careful | 0.361 / 0.110 | 0.36 / 0.38 | 0.038 / 0.011 | 0.00 / 0.00 | 0.26 / 0.16 | 0.288 / 0.123 |
| stamper | 0.013 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.213 / 1.725 |
