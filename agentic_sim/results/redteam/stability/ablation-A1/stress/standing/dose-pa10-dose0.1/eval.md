# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-60, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 35058.0 ± 581.1 | -636.5 ± 595.6 | 4725.6 | 0.979 | 0.000 | 0.000 | 0.024 | 0.025 | 0.387 | 0.015 | 3.88 | 14.20 | 0.30 |
| careful | 35694.5 ± 562.1 | nan ± nan | 4595.5 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.381 | 0.000 | 2.55 | 0.00 | 0.20 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (11986) / 0.025 (103806) | 0.015 (6989) / 0.014 (51126) | 0.016 (6876) / 0.016 (8242) | — / — |
| careful | 0.000 (10503) / 0.000 (103317) | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.024 (11986) / 0.025 (103806) | 0.015 (6989) / 0.014 (51126) | 0.016 (6876) / 0.016 (8242) | — / — |
| careful | 0.000 (10503) / 0.000 (103317) | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (11986) [rej. blind 0.000] / 0.000 (103806) [rej. blind 0.000] | 0.000 (6989) / 0.000 (51126) | 0.000 (6876) / 0.000 (8242) | — / — | 2.5 ± 0.3 | -3953 |
| careful | 0.000 (10503) [rej. blind 0.000] / 0.000 (103317) [rej. blind 0.000] | 0.000 (6289) / 0.000 (49205) | 0.000 (6363) / 0.000 (8143) | — / — | 2.6 ± 0.3 | +13 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.925 | — (0) | — (0) | 0.000 (27375) | 0.000 (7514) | 0.000 (154136) | 6.425 | 626.200 | 1.203 | 2.210 |
| careful | — | 0.911 | — (0) | — (0) | 0.000 (33138) | 0.000 (1109) | 0.000 (149573) | 4.725 | 678.650 | 1.183 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.675 | 0.000 | 0.000 | 0.000 | 0.000 | 0.200 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 22.875 / 39.700 | 3.875 ± 0.338 | +1.325 ± 0.432 | 16.400 | +6.075 ± 1.274 | 3.975 | 0.072 | 6.425 | +1.700 ± 0.467 | 1927.050 | 0.030 | +0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25706.112 ± 408.010 | +515.467 ± 429.912 | 35058.0 ± 581.1 | -636.5 ± 595.6 | 35.828 | -0.151 ± 0.340 | 16.112 ± 0.442 | +1.001 ± 0.442 | 17.961 | 0.001 | 2600.550 | 19.700 | 16.825 | +0.450 ± 0.370 | 571.152 | 232.225 |
| careful | 23.300 / 39.675 | 2.550 ± 0.277 | — | 10.325 | — | 3.150 | 0.057 | 4.725 | — | 1887.250 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 25190.644 ± 294.399 | — | 35694.5 ± 562.1 | — | 35.979 | — | 15.111 ± 0.293 | — | 18.104 | 0.002 | 2585.700 | 19.675 | 16.375 | — | 660.690 | 211.575 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (580); p1 1.000/0.000/0.000 (696); p2 1.000/0.000/0.000 (828); p3 1.000/0.000/0.000 (899); p4 1.000/0.000/0.000 (885); p5 1.000/0.000/0.000 (491); p6 1.000/0.000/0.000 (180); p7 1.000/0.000/0.000 (47); p8 1.000/0.000/0.000 (15); p9 1.000/0.000/0.000 (5)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (731); p2 1.000/0.000/0.000 (903); p3 1.000/0.000/0.000 (1015); p4 1.000/0.000/0.000 (1021); p5 1.000/0.000/0.000 (293); p6 1.000/0.000/0.000 (27); p7 1.000/0.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2595.2 / 299.6 | 0.26 / 0.13 | -0.13 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | +0.01 ± 0.00 | 0.168 / 0.129 | -0.039 ± 0.004 | 0.067 / 0.070 | 0.001 / 0.000 | 0.056 / 0.047 | -0.009 ± 0.002 | 1.65 / 1.30 | -0.35 ± 0.06 |
| careful | 2582.9 / 262.6 | 0.33 / 0.23 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.181 / 0.155 | -0.026 ± 0.004 | 0.075 / 0.086 | 0.002 / 0.000 | 0.058 / 0.052 | -0.005 ± 0.002 | 1.88 / 1.54 | -0.34 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.11 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.038 ± 0.005 | +0.003 ± 0.003 | -0.008 ± 0.002 |
| careful | -0.09 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.027 ± 0.004 | +0.010 ± 0.002 | -0.005 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.486 / 0.161 | 0.29 / 0.28 | 0.038 / 0.152 | 0.00 / 0.00 | 0.27 / 0.30 | 0.303 / 0.238 |
| careful | 0.470 / 0.139 | 0.30 / 0.31 | 0.040 / 0.164 | 0.00 / 0.00 | 0.29 / 0.32 | 0.309 / 0.259 |
