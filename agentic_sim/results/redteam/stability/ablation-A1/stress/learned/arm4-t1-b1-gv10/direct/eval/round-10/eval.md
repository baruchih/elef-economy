# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --arm 4 --temptation 1 --gv 10 --bond-mult-later 1`, seeds 21-40, hide ``, model `None` (value off, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 29695.4 ± 688.6 | 10.8 ± 751.1 | 3161.0 | 0.884 | 0.017 | 0.001 | 0.091 | 0.120 | 0.002 | 0.982 | 4.35 | 62.95 | 0.20 |
| careful | 29684.6 ± 609.8 | nan ± nan | 2897.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.90 | 0.00 | 0.60 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.091 (12865) [rej. blind 0.001] / 0.120 (50242) [rej. blind 0.001] | — / 1.000 (106) [rej. blind 0.038] | — / 0.714 (7) [rej. blind 0.714] | — / — |
| careful | 0.000 (5277) / 0.000 (52668) | — / 0.000 (1) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| direct | 0.074 (12865) / 0.103 (50242) | — / 0.896 (106) | — / 0.000 (7) | — / — |
| careful | 0.000 (5277) / 0.000 (52668) | — / 0.000 (1) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| direct | 0.023 (12865) [rej. blind 0.006] / 0.032 (50242) [rej. blind 0.004] | — / 0.104 (106) [rej. blind 0.038] | — / 0.714 (7) [rej. blind 0.714] | — / — | 49.5 ± 1.5 | -5387 |
| careful | 0.011 (5277) [rej. blind 0.009] / 0.014 (52668) [rej. blind 0.003] | — / 0.000 (1) | — / — | — / — | 53.3 ± 1.5 | +787 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.998 | 0.999 | — (0) | — (0) | 0.015 (131) | 0.027 (37) | 0.017 (63052) | 32.000 | 384.900 | 1.279 | 1.967 |
| careful | — | 0.946 | — (0) | — (0) | 0.000 (6401) | — (0) | 0.000 (51545) | 24.450 | 653.600 | 1.191 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.500 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.600 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 17.550 / 39.500 | 4.350 ± 0.582 | +1.450 ± 0.829 | 65.350 | +56.450 ± 1.776 | 7.450 | 0.120 | 12.500 | +7.700 ± 0.719 | 1979.600 | 0.045 | +0.028 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24882.207 ± 260.669 | +5599.936 ± 504.815 | 29695.4 ± 688.6 | +10.8 ± 751.1 | 32.732 | -5.195 ± 0.551 | 19.504 ± 0.582 | +5.337 ± 0.670 | 18.566 | 0.006 | 2504.950 | 19.500 | 21.950 | +2.400 ± 0.483 | 54.752 | 843.050 |
| careful | 20.100 / 39.650 | 2.900 ± 0.390 | — | 8.900 | — | 3.350 | 0.046 | 4.800 | — | 1902.800 | 0.018 | — | 0.000 / 0.000 (0.000 / 0.000) | 19282.271 ± 424.603 | — | 29684.6 ± 609.8 | — | 37.927 | — | 14.167 ± 0.344 | — | 16.820 | 0.001 | 2638.000 | 19.650 | 19.550 | — | 1013.908 | 686.050 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.984/0.016/0.000 (499); p1 0.969/0.029/0.002 (331); p2 0.951/0.047/0.002 (246); p3 0.963/0.035/0.002 (203); p4 0.977/0.022/0.001 (179); p5 0.987/0.013/0.000 (176); p6 0.990/0.008/0.001 (172); p7 0.984/0.014/0.001 (177); p8 0.992/0.007/0.001 (177); p9 0.987/0.012/0.001 (175); p10 0.992/0.007/0.001 (171); p11 0.992/0.007/0.001 (154); p12 0.994/0.006/0.000 (108); p13 0.994/0.006/0.000 (65); p14 0.990/0.010/0.000 (19)
- **careful**: p0 1.000/0.000/0.000 (557); p1 1.000/0.000/0.000 (534); p2 1.000/0.000/0.000 (542); p3 1.000/0.000/0.000 (541); p4 1.000/0.000/0.000 (547); p5 1.000/0.000/0.000 (175); p6 1.000/0.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2512.1 / 643.2 | 0.51 / 0.48 | -0.04 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.16 / 0.12 | -0.04 ± 0.00 | 0.265 / 0.258 | -0.007 ± 0.009 | 0.124 / 0.138 | 0.006 / 0.000 | 0.098 / 0.115 | +0.017 ± 0.005 | 2.28 / 2.18 | -0.10 ± 0.08 |
| careful | 2633.4 / 263.9 | 0.18 / 0.10 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.12 | +0.01 ± 0.00 | 0.111 / 0.090 | -0.021 ± 0.005 | 0.041 / 0.044 | 0.001 / 0.000 | 0.060 / 0.067 | +0.007 ± 0.003 | 1.56 / 1.34 | -0.23 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| direct | -0.07 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.045 ± 0.004 | -0.013 ± 0.004 | -0.003 ± 0.004 |
| careful | -0.09 ± 0.02 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.023 ± 0.005 | +0.003 ± 0.003 | +0.007 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| direct | 0.002 / 0.000 | 0.39 / — | 0.035 / 0.000 | 0.00 / — | — / — | 0.966 / 0.000 |
| careful | 0.000 / 0.000 | 0.00 / — | 0.038 / 0.000 | 0.00 / — | — / — | 0.883 / 0.000 |
