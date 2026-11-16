# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 3`, seeds 51-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 34437.6 ± 588.8 | -46.4 ± 541.9 | 4588.1 | 0.978 | 0.000 | 0.000 | 0.026 | 0.027 | 0.371 | 0.014 | 3.80 | 14.43 | 0.40 |
| mix:dose0.3:0.25 | 35104.7 ± 621.0 | 620.6 ± 835.6 | 4935.6 | 0.957 | 0.000 | 0.000 | 0.063 | 0.066 | 0.385 | 0.006 | 4.37 | 35.27 | 0.47 |
| careful | 34484.0 ± 613.2 | nan ± nan | 4502.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.365 | 0.000 | 2.17 | 0.00 | 0.37 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.026 (8720) / 0.027 (77848) | 0.013 (5114) / 0.014 (37571) | 0.014 (4936) / 0.015 (3453) | — / — |
| mix:dose0.3:0.25 | 0.063 (14417) / 0.066 (76587) | 0.005 (7329) / 0.006 (39973) | 0.005 (6308) / 0.005 (3454) | — / — |
| careful | 0.000 (7999) / 0.000 (77757) | 0.000 (4636) / 0.000 (36248) | 0.000 (4846) / 0.000 (3591) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.026 (8720) / 0.027 (77848) | 0.013 (5114) / 0.014 (37571) | 0.014 (4936) / 0.015 (3453) | — / — |
| mix:dose0.3:0.25 | 0.063 (14417) / 0.066 (76587) | 0.005 (7329) / 0.006 (39973) | 0.005 (6308) / 0.005 (3454) | — / — |
| careful | 0.000 (7999) / 0.000 (77757) | 0.000 (4636) / 0.000 (36248) | 0.000 (4846) / 0.000 (3591) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (8720) [rej. blind 0.000] / 0.000 (77848) [rej. blind 0.000] | 0.000 (5114) / 0.000 (37571) | 0.000 (4936) / 0.000 (3453) | — / — | 3.6 ± 0.5 | -3028 |
| mix:dose0.3:0.25 | 0.000 (14417) [rej. blind 0.000] / 0.000 (76587) [rej. blind 0.000] | 0.000 (7329) / 0.000 (39973) | 0.000 (6308) / 0.000 (3454) | — / — | 4.0 ± 0.4 | -6314 |
| careful | 0.000 (7999) / 0.000 (77757) [rej. blind 0.000] | 0.000 (4636) / 0.000 (36248) | 0.000 (4846) / 0.000 (3591) | — / — | 3.1 ± 0.3 | +16 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.929 | — (0) | — (0) | 0.000 (18941) | 0.000 (4977) | 0.000 (113724) | 7.133 | 651.600 | 1.180 | 2.023 |
| mix:dose0.3:0.25 | — | 0.971 | — (0) | — (0) | 0.000 (7781) | 0.000 (4383) | 0.000 (135904) | 10.300 | 513.900 | 1.193 | 3.424 |
| careful | — | 0.917 | — (0) | — (0) | 0.000 (22801) | 0.000 (1322) | 0.000 (110954) | 5.200 | 654.767 | 1.203 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| mix:dose0.3:0.25 | 39.300 | 0.000 | 0.000 | 0.000 | 0.000 | 0.467 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.367 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 22.633 / 39.700 | 3.800 ± 0.402 | +1.633 ± 0.499 | 16.100 | +5.267 ± 1.273 | 4.833 | 0.081 | 7.133 | +1.933 ± 0.571 | 1923.133 | 0.021 | +0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24895.620 ± 270.968 | +274.459 ± 376.291 | 34437.6 ± 588.8 | -46.4 ± 541.9 | 35.765 | -0.263 ± 0.382 | 15.763 ± 0.294 | +0.225 ± 0.341 | 17.643 | 0.001 | 2599.333 | 19.700 | 17.067 | +0.233 ± 0.417 | 597.831 | 228.200 |
| mix:dose0.3:0.25 | 21.300 / 39.300 | 4.367 ± 0.397 | +2.200 ± 0.488 | 39.867 | +29.033 ± 3.976 | 5.867 | 0.091 | 10.300 | +5.100 ± 0.723 | 1962.367 | 0.030 | +0.015 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 28291.415 ± 579.765 | +3670.254 ± 545.767 | 35104.7 ± 621.0 | +620.6 ± 835.6 | 33.896 | -2.131 ± 0.452 | 17.899 ± 0.432 | +2.360 ± 0.618 | 18.078 | 0.002 | 2560.433 | 19.300 | 18.000 | +1.167 ± 0.521 | 215.833 | 248.867 |
| careful | 22.867 / 39.700 | 2.167 ± 0.296 | — | 10.833 | — | 3.500 | 0.053 | 5.200 | — | 1890.033 | 0.015 | — | 0.000 / 0.000 (0.000 / 0.000) | 24621.161 ± 342.554 | — | 34484.0 ± 613.2 | — | 36.027 | — | 15.539 ± 0.373 | — | 17.623 | 0.001 | 2597.067 | 19.700 | 16.833 | — | 656.388 | 187.033 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (582); p1 1.000/0.000/0.000 (674); p2 1.000/0.000/0.000 (809); p3 1.000/0.000/0.000 (899); p4 1.000/0.000/0.000 (892); p5 1.000/0.000/0.000 (448); p6 1.000/0.000/0.000 (116); p7 1.000/0.000/0.000 (62); p8 1.000/0.000/0.000 (6)
- **mix:dose0.3:0.25**: p0 1.000/0.000/0.000 (558); p1 1.000/0.000/0.000 (572); p2 1.000/0.000/0.000 (597); p3 1.000/0.000/0.000 (596); p4 1.000/0.000/0.000 (560); p5 1.000/0.000/0.000 (449); p6 1.000/0.000/0.000 (302); p7 1.000/0.000/0.000 (233); p8 1.000/0.000/0.000 (194); p9 1.000/0.000/0.000 (191); p10 1.000/0.000/0.000 (161); p11 1.000/0.000/0.000 (134); p12 1.000/0.000/0.000 (109); p13 1.000/0.000/0.000 (55); p14 1.000/0.000/0.000 (14)
- **careful**: p0 1.000/0.000/0.000 (587); p1 1.000/0.000/0.000 (734); p2 1.000/0.000/0.000 (874); p3 1.000/0.000/0.000 (955); p4 1.000/0.000/0.000 (980); p5 1.000/0.000/0.000 (344); p6 1.000/0.000/0.000 (29)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2594.9 / 290.7 | 0.26 / 0.18 | -0.08 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | -0.00 ± 0.00 | 0.174 / 0.141 | -0.034 ± 0.004 | 0.071 / 0.080 | 0.001 / 0.000 | 0.057 / 0.055 | -0.002 ± 0.002 | 1.63 / 1.36 | -0.26 ± 0.07 |
| mix:dose0.3:0.25 | 2552.9 / 480.6 | 0.37 / 0.33 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.14 | +0.01 ± 0.00 | 0.261 / 0.227 | -0.034 ± 0.007 | 0.107 / 0.114 | 0.002 / 0.000 | 0.068 / 0.072 | +0.004 ± 0.002 | 1.84 / 1.81 | -0.03 ± 0.06 |
| careful | 2591.9 / 266.6 | 0.26 / 0.16 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.00 ± 0.00 | 0.177 / 0.142 | -0.035 ± 0.005 | 0.074 / 0.083 | 0.001 / 0.000 | 0.057 / 0.060 | +0.003 ± 0.003 | 1.62 / 1.32 | -0.30 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.07 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.033 ± 0.003 | +0.009 ± 0.003 | -0.001 ± 0.002 |
| mix:dose0.3:0.25 | -0.04 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.041 ± 0.004 | +0.001 ± 0.002 | +0.004 ± 0.002 |
| careful | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.034 ± 0.005 | +0.009 ± 0.002 | +0.004 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.476 / 0.160 | 0.30 / 0.31 | 0.038 / 0.152 | 0.00 / 0.00 | 0.29 / 0.31 | 0.477 / 0.252 |
| mix:dose0.3:0.25 | 0.514 / 0.224 | 0.25 / 0.23 | 0.037 / 0.109 | 0.00 / 0.00 | 0.24 / 0.25 | 0.473 / 0.178 |
| careful | 0.459 / 0.135 | 0.27 / 0.30 | 0.040 / 0.168 | 0.00 / 0.00 | 0.27 / 0.30 | 0.479 / 0.261 |
