# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2 --dispute-policy truthful --dispute-rate 0.25`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29390.2 ± 781.6 | -649.9 ± 807.5 | 3103.8 | 0.973 | 0.027 | 0.000 | 0.019 | 0.018 | 0.049 | 0.203 | 6.15 | 17.05 | 0.30 |
| careful | 30040.1 ± 643.0 | nan ± nan | 3080.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 | 1.50 | 0.00 | 0.60 |
| hand | 30439.0 ± 642.3 | 399.0 ± 702.9 | 3392.6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.075 | 0.000 | 2.35 | 0.00 | 0.70 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.019 (5789) [rej. blind 0.001] / 0.018 (53230) [rej. blind 0.000] | — / 0.000 (3) | 0.306 (952) [rej. blind 0.007] / 0.156 (2103) [rej. blind 0.002] | — / — |
| careful | 0.000 (5348) / 0.000 (53180) | — / 0.000 (4) | 0.000 (899) / 0.000 (2187) | — / — |
| hand | 0.000 (12720) / 0.000 (50017) | — / 0.000 (165) | 0.000 (2242) / 0.000 (2708) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.020 (5789) [rej. blind 0.001] / 0.018 (53230) [rej. blind 0.000] | — / 0.000 (3) | 0.306 (952) [rej. blind 0.007] / 0.156 (2103) [rej. blind 0.002] | — / — | 3.0 ± 0.4 | +18 |
| careful | 0.000 (5348) [rej. blind 0.000] / 0.000 (53180) [rej. blind 0.000] | — / 0.000 (4) | 0.000 (899) / 0.000 (2187) | — / — | 3.2 ± 0.6 | +11 |
| hand | 0.069 (12720) [rej. blind 0.000] / 0.106 (50017) [rej. blind 0.000] | — / 0.000 (165) | 0.000 (2242) / 0.011 (2708) | — / — | 2.2 ± 0.3 | +6229 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.861 | 0.961 | — (0) | — (0) | 0.088 (5108) | 0.073 (545) | 0.021 (56424) | 25.300 | 619.850 | 1.201 | 0.674 |
| careful | — | 0.944 | — (0) | — (0) | 0.000 (7034) | — (0) | 0.000 (54584) | 24.800 | 667.550 | 1.184 | 0.000 |
| hand | — | 1.000 | — (0) | — (0) | — (0) | 0.000 (454) | 0.000 (67398) | 31.950 | 336.650 | 1.248 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |
| hand | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.700 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 20.200 / 39.550 | 6.150 ± 0.693 | +4.650 ± 0.786 | 15.050 | +6.000 ± 1.407 | 4.000 | 0.076 | 5.750 | +0.300 ± 0.629 | 1949.400 | 0.017 | +0.003 ± 0.001 | 8.700 / 5.950 (8.700 / 5.950) | 20160.235 ± 392.923 | +534.980 ± 422.083 | 29390.2 ± 781.6 | -649.9 ± 807.5 | 37.730 | -0.069 ± 0.391 | 15.362 ± 0.521 | +0.977 ± 0.538 | 16.583 | 0.000 | 2666.400 | 19.550 | 19.350 | +0.600 ± 0.461 | 873.175 | 224.000 |
| careful | 20.600 / 39.350 | 1.500 ± 0.256 | — | 9.050 | — | 4.000 | 0.046 | 5.450 | — | 1909.650 | 0.014 | — | 8.200 / 8.100 (8.200 / 8.100) | 19625.255 ± 284.439 | — | 30040.1 ± 643.0 | — | 37.798 | — | 14.385 ± 0.260 | — | 16.632 | 0.000 | 2663.200 | 19.350 | 18.750 | — | 924.074 | 243.750 |
| hand | 18.000 / 39.650 | 2.350 ± 0.310 | +0.850 ± 0.372 | 55.750 | +46.700 ± 1.793 | 7.000 | 0.057 | 12.300 | +6.850 ± 0.995 | 1954.350 | 0.033 | +0.019 ± 0.001 | 19.100 / 18.800 (19.100 / 18.800) | 26234.151 ± 352.503 | +6608.896 ± 397.884 | 30439.0 ± 642.3 | +399.0 ± 702.9 | 32.687 | -5.111 ± 0.340 | 19.387 ± 0.445 | +5.001 ± 0.504 | 18.506 | 0.005 | 2494.600 | 19.650 | 21.650 | +2.900 ± 0.492 | 61.639 | 408.500 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.994/0.006/0.000 (559); p1 0.985/0.015/0.000 (542); p2 0.980/0.020/0.000 (562); p3 0.961/0.038/0.001 (556); p4 0.963/0.037/0.000 (553); p5 0.942/0.058/0.000 (239); p6 0.930/0.067/0.003 (47); p7 0.965/0.033/0.002 (27); p8 0.976/0.024/0.000 (13); p9 1.000/0.000/0.000 (7)
- **careful**: p0 1.000/0.000/0.000 (558); p1 1.000/0.000/0.000 (547); p2 1.000/0.000/0.000 (564); p3 1.000/0.000/0.000 (580); p4 1.000/0.000/0.000 (606); p5 1.000/0.000/0.000 (225)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2661.5 / 289.4 | 0.11 / 0.05 | -0.05 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.067 | -0.015 ± 0.005 | 0.024 / 0.024 | 0.000 / 0.000 | 0.060 / 0.068 | +0.008 ± 0.004 | 1.33 / 1.22 | -0.11 ± 0.06 |
| careful | 2659.0 / 267.4 | 0.13 / 0.06 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.103 / 0.087 | -0.016 ± 0.003 | 0.035 / 0.037 | 0.000 / 0.000 | 0.058 / 0.067 | +0.009 ± 0.003 | 1.47 / 1.25 | -0.22 ± 0.10 |
| hand | 2500.8 / 636.0 | 0.60 / 0.66 | +0.06 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.337 / 0.328 | -0.008 ± 0.008 | 0.157 / 0.172 | 0.005 / 0.000 | 0.118 / 0.129 | +0.011 ± 0.003 | 2.32 / 2.38 | +0.06 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.05 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.011 ± 0.004 | +0.001 ± 0.002 | +0.006 ± 0.003 |
| careful | -0.07 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.016 ± 0.003 | +0.003 ± 0.003 | +0.009 ± 0.004 |
| hand | -0.00 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.041 ± 0.004 | -0.004 ± 0.004 | -0.002 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.000 / 0.000 | 0.67 / — | 0.043 / 0.180 | 0.00 / 0.00 | 0.16 / 0.13 | 0.949 / 0.199 |
| careful | 0.000 / 0.000 | 0.50 / — | 0.042 / 0.180 | 0.00 / 0.00 | 0.15 / 0.12 | 0.926 / 0.193 |
| hand | 0.003 / 0.000 | 0.16 / — | 0.041 / 0.128 | 0.00 / 0.00 | 0.06 / 0.08 | 0.990 / 0.080 |
