# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 2`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 31026.9 ± 602.4 | 869.1 ± 548.1 | 3033.2 | 0.975 | 0.024 | 0.001 | 0.022 | 0.019 | 0.045 | 0.141 | 4.55 | 9.45 | 0.40 |
| careful | 30157.8 ± 752.6 | nan ± nan | 3074.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.044 | 0.000 | 2.45 | 0.00 | 0.40 |
| stamper | 7643.8 ± 234.7 | -22514.0 ± 780.0 | 1013.5 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.000 | — | 9.75 | 175.60 | 1.00 |
| hand | 30673.8 ± 608.7 | 516.0 ± 688.0 | 3365.9 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.064 | 0.000 | 3.75 | 0.00 | 0.60 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.022 (5545) [rej. blind 0.001] / 0.019 (52411) [rej. blind 0.000] | — / 0.000 (4) | 0.237 (800) [rej. blind 0.011] / 0.101 (1903) [rej. blind 0.004] | — / — |
| careful | 0.000 (5352) / 0.000 (53450) | — / — | 0.000 (763) / 0.000 (1927) | — / — |
| stamper | 1.000 (2788) / 1.000 (17482) | — / — | — / — | — / — |
| hand | 0.000 (12799) / 0.000 (50209) | — / 0.000 (155) | 0.000 (1616) / 0.000 (2540) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.022 (5545) [rej. blind 0.001] / 0.020 (52411) [rej. blind 0.000] | — / 0.000 (4) | 0.237 (800) [rej. blind 0.011] / 0.101 (1903) [rej. blind 0.004] | — / — | 4.1 ± 0.6 | +18 |
| careful | 0.000 (5352) [rej. blind 0.000] / 0.000 (53450) [rej. blind 0.000] | — / — | 0.000 (763) / 0.000 (1927) | — / — | 3.6 ± 0.4 | +18 |
| stamper | 1.000 (2788) / 1.000 (17482) | — / — | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.069 (12799) / 0.104 (50209) [rej. blind 0.000] | — / 0.000 (155) | 0.000 (1616) / 0.005 (2540) | — / — | 2.1 ± 0.3 | +6103 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.841 | 0.962 | — (0) | — (0) | 0.096 (5049) | 0.046 (325) | 0.018 (55289) | 5.550 | 649.500 | 1.212 | 1.703 |
| careful | — | 0.944 | — (0) | — (0) | 0.000 (7087) | — (0) | 0.000 (54405) | 4.800 | 670.250 | 1.139 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (20270) | 55.750 | 232.800 | 1.495 | 3.150 |
| hand | — | 1.000 | — (0) | — (0) | 0.000 (2) | 0.000 (516) | 0.000 (66801) | 12.250 | 355.300 | 1.223 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.400 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| stamper | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.450 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 20.500 / 39.400 | 4.550 ± 0.591 | +2.100 ± 0.692 | 14.500 | +4.750 ± 1.908 | 3.800 | 0.082 | 5.550 | +0.750 ± 0.507 | 1928.550 | 0.021 | +0.004 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 20697.248 ± 546.251 | +1238.616 ± 600.066 | 31026.9 ± 602.4 | +869.1 ± 548.1 | 37.057 | -1.149 ± 0.618 | 14.574 ± 0.471 | +0.397 ± 0.588 | 17.003 | 0.001 | 2623.500 | 19.400 | 18.900 | -0.300 ± 0.424 | 813.950 | 301.150 |
| careful | 20.400 / 39.600 | 2.450 ± 0.352 | — | 9.750 | — | 2.500 | 0.043 | 4.800 | — | 1933.250 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 19458.632 ± 328.789 | — | 30157.8 ± 752.6 | — | 38.206 | — | 14.177 ± 0.384 | — | 16.393 | 0.000 | 2677.450 | 19.600 | 19.200 | — | 952.026 | 234.400 |
| stamper | 2.300 / 39.900 | 9.750 ± 0.714 | +7.300 ± 0.733 | 103.600 | +93.850 ± 2.084 | 0.000 | 1.000 | 55.750 | +50.950 ± 1.690 | 874.050 | 0.193 | +0.177 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 8377.115 ± 204.273 | -11081.517 ± 301.704 | 7643.8 ± 234.7 | -22514.0 ± 780.0 | 28.859 | -9.347 ± 0.317 | 28.765 ± 0.736 | +14.588 ± 0.883 | 21.371 | 0.176 | 751.400 | 19.900 | 37.600 | +18.400 ± 0.426 | 6130.142 | 415.850 |
| hand | 18.250 / 39.450 | 3.750 ± 0.441 | +1.300 ± 0.503 | 56.250 | +46.500 ± 1.894 | 6.900 | 0.051 | 12.250 | +7.450 ± 0.806 | 1981.550 | 0.043 | +0.026 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26358.487 ± 402.442 | +6899.855 ± 421.074 | 30673.8 ± 608.7 | +516.0 ± 688.0 | 32.862 | -5.344 ± 0.379 | 19.258 ± 0.492 | +5.081 ± 0.632 | 18.414 | 0.007 | 2499.700 | 19.450 | 21.200 | +2.000 ± 0.459 | 72.077 | 443.850 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.995/0.005/0.000 (559); p1 0.987/0.013/0.000 (545); p2 0.976/0.023/0.001 (555); p3 0.967/0.032/0.001 (575); p4 0.965/0.035/0.000 (569); p5 0.934/0.062/0.004 (199); p6 0.981/0.019/0.000 (11); p7 0.987/0.013/0.000 (11); p8 0.995/0.005/0.000 (10); p9 1.000/0.000/0.000 (0)
- **careful**: p0 1.000/0.000/0.000 (559); p1 1.000/0.000/0.000 (560); p2 1.000/0.000/0.000 (568); p3 1.000/0.000/0.000 (572); p4 1.000/0.000/0.000 (595); p5 1.000/0.000/0.000 (220)
- **stamper**: p0 0.000/1.000/0.000 (556); p1 0.000/1.000/0.000 (309); p2 0.000/1.000/0.000 (134); p3 0.000/1.000/0.000 (12); p4 0.000/1.000/0.000 (2); p5 0.000/1.000/0.000 (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2620.6 / 277.2 | 0.24 / 0.13 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.145 / 0.111 | -0.034 ± 0.005 | 0.051 / 0.054 | 0.001 / 0.000 | 0.062 / 0.065 | +0.003 ± 0.003 | 1.69 / 1.38 | -0.31 ± 0.08 |
| careful | 2672.5 / 267.6 | 0.08 / 0.03 | -0.05 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.082 / 0.071 | -0.011 ± 0.004 | 0.022 / 0.024 | 0.000 / 0.000 | 0.056 / 0.055 | -0.001 ± 0.002 | 1.30 / 1.20 | -0.10 ± 0.06 |
| stamper | 874.1 / 139.4 | 0.76 / 0.50 | -0.26 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.00 ± 0.01 | 0.193 / 0.158 | -0.035 ± 0.009 | 0.080 / 0.072 | 0.140 / 0.000 | 0.076 / 0.057 | -0.019 ± 0.005 | 3.81 / 2.59 | -1.22 ± 0.30 |
| hand | 2510.4 / 640.0 | 0.58 / 0.57 | -0.02 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.312 / 0.298 | -0.014 ± 0.007 | 0.133 / 0.142 | 0.007 / 0.000 | 0.112 / 0.122 | +0.009 ± 0.004 | 2.31 / 2.25 | -0.06 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.10 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.033 ± 0.007 | +0.002 ± 0.006 | +0.001 ± 0.003 |
| careful | -0.05 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.012 ± 0.004 | +0.002 ± 0.002 | -0.001 ± 0.002 |
| stamper | -0.70 ± 0.05 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.156 ± 0.012 | -0.081 ± 0.009 | -0.042 ± 0.005 |
| hand | -0.06 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.047 ± 0.005 | -0.009 ± 0.003 | -0.003 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.000 / 0.000 | 0.67 / — | 0.041 / 0.170 | 0.00 / 0.00 | 0.17 / 0.13 | 0.949 / 0.195 |
| careful | 0.000 / 0.000 | — / — | 0.039 / 0.157 | 0.00 / 0.00 | 0.14 / 0.13 | 0.924 / 0.174 |
| stamper | 0.000 / 0.000 | — / — | 0.000 / 0.032 | — / 0.00 | — / — | 1.267 / 0.064 |
| hand | 0.003 / 0.000 | 0.56 / — | 0.034 / 0.084 | 0.00 / 0.00 | 0.06 / 0.07 | 0.979 / 0.042 |
