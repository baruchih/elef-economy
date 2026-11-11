# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29741.7 ± 691.5 | -416.1 ± 629.4 | 3058.6 | 0.978 | 0.021 | 0.000 | 0.019 | 0.017 | 0.044 | 0.121 | 4.95 | 9.10 | 0.50 |
| careful | 30157.8 ± 752.6 | nan ± nan | 3074.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.044 | 0.000 | 2.45 | 0.00 | 0.40 |
| stamper | 7643.8 ± 234.7 | -22514.0 ± 780.0 | 1013.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | — | 9.75 | 175.60 | 1.00 |
| hand | 30673.8 ± 608.7 | 516.0 ± 688.0 | 3365.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.064 | 0.000 | 3.75 | 0.00 | 0.60 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.019 (5433) [rej. blind 0.001] / 0.017 (53032) [rej. blind 0.000] | — / 0.750 (4) | 0.199 (795) [rej. blind 0.003] / 0.087 (1907) [rej. blind 0.003] | — / — |
| careful | 0.000 (5352) / 0.000 (53450) | — / — | 0.000 (763) / 0.000 (1927) | — / — |
| stamper | 1.000 (2788) / 1.000 (17482) | — / — | — / — | — / — |
| hand | 0.000 (12799) / 0.000 (50209) | — / 0.000 (155) | 0.000 (1616) / 0.000 (2540) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.019 (5433) [rej. blind 0.001] / 0.017 (53032) [rej. blind 0.000] | — / 0.750 (4) | 0.199 (795) [rej. blind 0.003] / 0.087 (1907) [rej. blind 0.003] | — / — | 2.6 ± 0.3 | +15 |
| careful | 0.000 (5352) [rej. blind 0.000] / 0.000 (53450) [rej. blind 0.000] | — / — | 0.000 (763) / 0.000 (1927) | — / — | 3.6 ± 0.4 | +18 |
| stamper | 1.000 (2788) / 1.000 (17482) | — / — | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.069 (12799) / 0.104 (50209) [rej. blind 0.000] | — / 0.000 (155) | 0.000 (1616) / 0.005 (2540) | — / — | 2.1 ± 0.3 | +6103 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.771 | 0.959 | — (0) | — (0) | 0.111 (5503) | 0.019 (422) | 0.013 (55246) | 24.100 | 634.250 | 1.168 | 0.378 |
| careful | — | 0.944 | — (0) | — (0) | 0.000 (7087) | — (0) | 0.000 (54405) | 24.400 | 670.250 | 1.139 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20270) | 75.650 | 232.800 | 1.495 | 2.321 |
| hand | — | 1.000 | — (0) | — (0) | 0.000 (2) | 0.000 (516) | 0.000 (66801) | 31.700 | 355.300 | 1.223 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.450 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 20.200 / 39.350 | 4.950 ± 0.663 | +2.500 ± 0.686 | 12.750 | +3.000 ± 0.921 | 3.900 | 0.080 | 4.750 | -0.050 ± 0.564 | 1951.900 | 0.020 | +0.003 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 19391.351 ± 372.217 | -67.281 ± 348.831 | 29741.7 ± 691.5 | -416.1 ± 629.4 | 38.225 | +0.020 ± 0.411 | 14.397 ± 0.406 | +0.220 ± 0.555 | 16.329 | 0.000 | 2657.100 | 19.350 | 19.150 | -0.050 ± 0.387 | 990.041 | 199.650 |
| careful | 20.400 / 39.600 | 2.450 ± 0.352 | — | 9.750 | — | 2.500 | 0.043 | 4.800 | — | 1933.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19458.632 ± 328.789 | — | 30157.8 ± 752.6 | — | 38.206 | — | 14.177 ± 0.384 | — | 16.393 | 0.000 | 2677.450 | 19.600 | 19.200 | — | 952.026 | 234.400 |
| stamper | 2.300 / 39.900 | 9.750 ± 0.714 | +7.300 ± 0.733 | 103.600 | +93.850 ± 2.084 | 0.000 | 1.000 | 55.750 | +50.950 ± 1.690 | 874.050 | 0.193 | +0.177 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 8377.115 ± 204.273 | -11081.517 ± 301.704 | 7643.8 ± 234.7 | -22514.0 ± 780.0 | 28.859 | -9.347 ± 0.317 | 28.765 ± 0.736 | +14.588 ± 0.883 | 21.371 | 0.176 | 751.400 | 19.900 | 37.600 | +18.400 ± 0.426 | 6130.142 | 415.850 |
| hand | 18.250 / 39.450 | 3.750 ± 0.441 | +1.300 ± 0.503 | 56.250 | +46.500 ± 1.894 | 6.900 | 0.051 | 12.250 | +7.450 ± 0.806 | 1981.550 | 0.043 | +0.026 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26358.487 ± 402.442 | +6899.855 ± 421.074 | 30673.8 ± 608.7 | +516.0 ± 688.0 | 32.862 | -5.344 ± 0.379 | 19.258 ± 0.492 | +5.081 ± 0.632 | 18.414 | 0.007 | 2499.700 | 19.450 | 21.200 | +2.000 ± 0.459 | 72.077 | 443.850 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.996/0.004/0.000 (559); p1 0.990/0.010/0.000 (555); p2 0.985/0.014/0.000 (560); p3 0.964/0.035/0.001 (576); p4 0.973/0.027/0.000 (577); p5 0.936/0.063/0.001 (215); p6 0.991/0.009/0.000 (17)
- **careful**: p0 1.000/0.000/0.000 (559); p1 1.000/0.000/0.000 (560); p2 1.000/0.000/0.000 (568); p3 1.000/0.000/0.000 (572); p4 1.000/0.000/0.000 (595); p5 1.000/0.000/0.000 (220)
- **stamper**: p0 0.000/1.000/0.000 (556); p1 0.000/1.000/0.000 (309); p2 0.000/1.000/0.000 (134); p3 0.000/1.000/0.000 (12); p4 0.000/1.000/0.000 (2); p5 0.000/1.000/0.000 (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2651.6 / 271.6 | 0.12 / 0.05 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.085 / 0.064 | -0.022 ± 0.005 | 0.024 / 0.028 | 0.000 / 0.000 | 0.058 / 0.062 | +0.004 ± 0.004 | 1.36 / 1.20 | -0.16 ± 0.06 |
| careful | 2672.5 / 267.6 | 0.08 / 0.03 | -0.05 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.071 | -0.011 ± 0.004 | 0.022 / 0.024 | 0.000 / 0.000 | 0.056 / 0.055 | -0.001 ± 0.002 | 1.30 / 1.20 | -0.10 ± 0.06 |
| stamper | 874.1 / 139.4 | 0.76 / 0.50 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.00 ± 0.01 | 0.193 / 0.158 | -0.035 ± 0.009 | 0.080 / 0.072 | 0.140 / 0.000 | 0.076 / 0.057 | -0.019 ± 0.005 | 3.81 / 2.59 | -1.22 ± 0.30 |
| hand | 2510.4 / 640.0 | 0.58 / 0.57 | -0.02 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.312 / 0.298 | -0.014 ± 0.007 | 0.133 / 0.142 | 0.007 / 0.000 | 0.112 / 0.122 | +0.009 ± 0.004 | 2.31 / 2.25 | -0.06 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.06 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.020 ± 0.004 | +0.004 ± 0.002 | +0.003 ± 0.004 |
| careful | -0.05 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.012 ± 0.004 | +0.002 ± 0.002 | -0.001 ± 0.002 |
| stamper | -0.70 ± 0.05 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.156 ± 0.012 | -0.081 ± 0.009 | -0.042 ± 0.005 |
| hand | -0.06 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.047 ± 0.005 | -0.009 ± 0.003 | -0.003 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.000 / 0.000 | 0.75 / — | 0.039 / 0.160 | 0.00 / 0.00 | 0.14 / 0.12 | 0.944 / 0.176 |
| careful | 0.000 / 0.000 | — / — | 0.039 / 0.157 | 0.00 / 0.00 | 0.14 / 0.13 | 0.924 / 0.174 |
| stamper | 0.000 / 0.000 | — / — | 0.000 / 0.032 | — / 0.00 | — / — | 1.267 / 0.064 |
| hand | 0.003 / 0.000 | 0.56 / — | 0.034 / 0.084 | 0.00 / 0.00 | 0.06 / 0.07 | 0.979 / 0.042 |
