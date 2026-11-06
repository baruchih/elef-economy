# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 35492.4 ± 759.8 | 561.3 ± 711.5 | 4371.1 | 0.811 | 0.186 | 0.004 | 0.011 | 0.011 | 0.340 | 0.537 | 2.10 | 6.35 | 0.20 |
| careful | 34931.1 ± 788.2 | nan ± nan | 4254.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.339 | 0.000 | 1.70 | 0.00 | 0.40 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.011 (5608) [rej. blind 0.001] / 0.011 (52109) [rej. blind 0.001] | 0.875 (88) / 0.880 (17566) [rej. blind 0.000] | 0.025 (3043) [rej. blind 0.018] / 0.039 (9008) [rej. blind 0.026] | — / — |
| careful | 0.000 (5190) / 0.000 (51027) | 0.000 (117) / 0.000 (17160) | 0.000 (2625) / 0.000 (8979) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.367 | 0.729 | 0.362 (28504) | 0.285 (8037) | 0.329 (4522) | 0.231 (1551) | 0.040 (44808) | 25.650 | 679.850 | 1.239 | 0.248 |
| careful | — | 0.684 | 0.000 (26258) | 0.000 (6098) | 0.000 (4898) | 0.000 (1223) | 0.000 (46621) | 24.800 | 736.000 | 1.222 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 23.350 / 39.800 | 2.100 ± 0.250 | +0.400 ± 0.419 | 14.200 | +4.900 ± 1.382 | 3.800 | 0.079 | 5.850 | +0.700 ± 0.805 | 1452.500 | 0.008 | -0.005 ± 0.001 | 226.450 / 36.600 (31.800 / 31.200) | 24803.166 ± 390.110 | +1358.652 ± 586.977 | 35492.4 ± 759.8 | +561.3 ± 711.5 | 36.735 | +1.331 ± 0.554 | 14.838 ± 0.361 | +0.486 ± 0.416 | 18.232 | 0.001 | 2608.800 | 19.800 | 16.450 | +1.000 ± 0.589 | 850.860 | 159.750 |
| careful | 24.200 / 39.650 | 1.700 ± 0.349 | — | 9.300 | — | 3.200 | 0.045 | 5.150 | — | 1454.650 | 0.013 | — | 224.050 / 31.500 (28.100 / 27.450) | 23444.514 ± 399.404 | — | 34931.1 ± 788.2 | — | 35.404 | — | 14.352 ± 0.339 | — | 18.284 | 0.006 | 2542.650 | 19.650 | 15.450 | — | 685.274 | 239.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.941/0.055/0.004 (606); p1 0.830/0.166/0.004 (716); p2 0.753/0.244/0.003 (858); p3 0.740/0.257/0.003 (905); p4 0.810/0.188/0.003 (842); p5 0.849/0.141/0.009 (307); p6 0.850/0.138/0.012 (93); p7 0.906/0.082/0.013 (44)
- **careful**: p0 1.000/0.000/0.000 (602); p1 1.000/0.000/0.000 (687); p2 1.000/0.000/0.000 (835); p3 1.000/0.000/0.000 (924); p4 1.000/0.000/0.000 (935); p5 1.000/0.000/0.000 (260); p6 1.000/0.000/0.000 (11)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2605.4 / 280.4 | 0.30 / 0.21 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | -0.00 ± 0.00 | 0.197 / 0.166 | -0.031 ± 0.004 | 0.073 / 0.081 | 0.001 / 0.000 | 0.064 / 0.064 | -0.001 ± 0.003 | 1.73 / 1.52 | -0.21 ± 0.10 |
| careful | 2551.3 / 259.5 | 0.50 / 0.36 | -0.14 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.254 / 0.218 | -0.036 ± 0.005 | 0.106 / 0.122 | 0.006 / 0.000 | 0.070 / 0.066 | -0.004 ± 0.003 | 2.13 / 1.85 | -0.28 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.004 | +0.008 ± 0.003 | -0.000 ± 0.003 |
| careful | -0.14 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.038 ± 0.005 | +0.014 ± 0.005 | -0.003 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.334 / 0.014 | 0.38 / 0.57 | 0.145 / 0.475 | 0.00 / 0.00 | 0.30 / 0.31 | 0.356 / 0.429 |
| careful | 0.334 / 0.022 | 0.39 / 0.36 | 0.146 / 0.471 | 0.00 / 0.00 | 0.33 / 0.34 | 0.385 / 0.464 |
