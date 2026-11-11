# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dial-start 3.168375,16.258218,5.676270,1.069438`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 36600.4 ± 600.6 | 2024.6 ± 754.0 | 6425.8 | 0.967 | 0.013 | 0.020 | 0.017 | 0.016 | 0.502 | 0.050 | 2.70 | 6.15 | 0.30 |
| careful | 34575.8 ± 773.7 | nan ± nan | 6243.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.497 | 0.000 | 2.05 | 0.00 | 0.35 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.017 (12591) [rej. blind 0.004] / 0.016 (51379) [rej. blind 0.003] | 0.020 (11185) [rej. blind 0.012] / 0.015 (34944) [rej. blind 0.002] | 0.154 (12477) [rej. blind 0.128] / 0.098 (5939) [rej. blind 0.097] | — / — |
| careful | 0.000 (10876) / 0.000 (51925) | 0.000 (10087) / 0.000 (34386) | 0.000 (11757) / 0.000 (5836) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.017 (12591) [rej. blind 0.004] / 0.016 (51379) [rej. blind 0.003] | 0.020 (11185) [rej. blind 0.012] / 0.015 (34944) [rej. blind 0.002] | 0.154 (12477) [rej. blind 0.128] / 0.098 (5939) [rej. blind 0.097] | — / — | 2.8 ± 0.4 | +5 |
| careful | 0.000 (10876) [rej. blind 0.000] / 0.000 (51925) [rej. blind 0.000] | 0.000 (10087) / 0.000 (34386) | 0.000 (11757) / 0.000 (5836) | — / — | 3.0 ± 0.5 | +2 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.981 | 0.988 | — (0) | — (0) | 0.042 (591) | 0.013 (11156) | 0.013 (116768) | 25.200 | 256.950 | 1.243 | 0.244 |
| careful | — | 0.965 | — (0) | — (0) | 0.000 (5803) | 0.000 (15824) | 0.000 (103240) | 24.000 | 296.250 | 1.075 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 21.700 / 39.950 | 2.700 ± 0.356 | +0.650 ± 0.483 | 28.950 | +8.650 ± 1.834 | 8.300 | 0.059 | 5.250 | +1.150 ± 0.612 | 1952.000 | 0.034 | +0.009 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 33029.459 ± 424.019 | +1072.225 ± 518.403 | 36600.4 ± 600.6 | +2024.6 ± 754.0 | 34.132 | -0.467 ± 0.442 | 19.540 ± 0.382 | -1.011 ± 0.604 | 18.304 | 0.002 | 2586.100 | 19.950 | 18.250 | -0.150 ± 0.264 | 158.022 | 85.800 |
| careful | 21.500 / 39.900 | 2.050 ± 0.294 | — | 20.300 | — | 6.450 | 0.049 | 4.100 | — | 1912.850 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 31957.234 ± 478.880 | — | 34575.8 ± 773.7 | — | 34.600 | — | 20.551 ± 0.668 | — | 18.265 | 0.002 | 2608.300 | 19.900 | 18.400 | — | 249.186 | 108.350 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.947/0.047/0.006 (231); p1 0.939/0.017/0.044 (298); p2 0.925/0.024/0.051 (442); p3 0.953/0.011/0.036 (502); p4 0.956/0.021/0.023 (542); p5 0.977/0.010/0.013 (510); p6 0.977/0.011/0.012 (543); p7 0.983/0.009/0.008 (557); p8 0.978/0.011/0.011 (574); p9 0.976/0.010/0.014 (606); p10 0.974/0.009/0.017 (562); p11 0.978/0.006/0.016 (460); p12 0.975/0.009/0.016 (301); p13 0.970/0.005/0.025 (208); p14 0.956/0.007/0.037 (86); p15 0.939/0.061/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (230); p1 1.000/0.000/0.000 (350); p2 1.000/0.000/0.000 (496); p3 1.000/0.000/0.000 (537); p4 1.000/0.000/0.000 (598); p5 1.000/0.000/0.000 (629); p6 1.000/0.000/0.000 (663); p7 1.000/0.000/0.000 (702); p8 1.000/0.000/0.000 (741); p9 1.000/0.000/0.000 (698); p10 1.000/0.000/0.000 (299); p11 1.000/0.000/0.000 (130); p12 1.000/0.000/0.000 (56); p13 1.000/0.000/0.000 (61); p14 1.000/0.000/0.000 (43); p15 1.000/0.000/0.000 (9)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2568.9 / 629.5 | 0.31 / 0.27 | -0.04 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.21 / 0.18 | -0.02 ± 0.00 | 0.255 / 0.196 | -0.059 ± 0.009 | 0.102 / 0.093 | 0.002 / 0.000 | 0.061 / 0.059 | -0.002 ± 0.003 | 1.76 / 1.67 | -0.09 ± 0.05 |
| careful | 2596.2 / 543.8 | 0.22 / 0.19 | -0.03 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.18 | -0.02 ± 0.00 | 0.163 / 0.124 | -0.038 ± 0.009 | 0.066 / 0.063 | 0.002 / 0.000 | 0.056 / 0.051 | -0.005 ± 0.002 | 1.65 / 1.47 | -0.18 ± 0.04 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.03 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.038 ± 0.005 | -0.000 ± 0.003 | -0.000 ± 0.003 |
| careful | -0.04 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.030 ± 0.004 | +0.001 ± 0.003 | -0.003 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.670 / 0.220 | 0.11 / 0.14 | 0.041 / 0.200 | 0.00 / 0.00 | 0.11 / 0.14 | 0.104 / 0.137 |
| careful | 0.654 / 0.205 | 0.11 / 0.14 | 0.040 / 0.224 | 0.00 / 0.00 | 0.11 / 0.13 | 0.096 / 0.138 |
