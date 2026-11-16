# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 34878.5 ± 481.6 | -446.2 ± 498.3 | 4625.1 | 0.979 | 0.000 | 0.000 | 0.028 | 0.025 | 0.373 | 0.013 | 3.72 | 14.12 | 0.35 |
| careful | 35324.6 ± 425.4 | nan ± nan | 4585.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.374 | 0.000 | 2.48 | 0.00 | 0.23 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.028 (17723) / 0.025 (156242) | 0.014 (10393) / 0.013 (75924) | 0.014 (10168) / 0.015 (7059) | — / — |
| careful | 0.000 (15755) / 0.000 (156559) | 0.000 (9676) / 0.000 (75771) | 0.000 (10004) / 0.000 (7382) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.028 (17723) / 0.025 (156242) | 0.014 (10393) / 0.013 (75924) | 0.014 (10168) / 0.015 (7059) | — / — |
| careful | 0.000 (15755) / 0.000 (156559) | 0.000 (9676) / 0.000 (75771) | 0.000 (10004) / 0.000 (7382) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (17723) [rej. blind 0.000] / 0.000 (156242) [rej. blind 0.000] | 0.000 (10393) / 0.000 (75924) | 0.000 (10168) / 0.000 (7059) | — / — | 2.1 ± 0.3 | -5794 |
| careful | 0.000 (15755) [rej. blind 0.000] / 0.000 (156559) [rej. blind 0.000] | 0.000 (9676) / 0.000 (75771) | 0.000 (10004) / 0.000 (7382) | — / — | 2.1 ± 0.2 | +30 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.933 | — (0) | — (0) | 0.000 (36866) | 0.000 (8365) | 0.000 (232278) | 6.500 | 628.233 | 1.189 | 2.172 |
| careful | — | 0.911 | — (0) | — (0) | 0.000 (49661) | 0.000 (640) | 0.000 (224846) | 5.233 | 665.283 | 1.172 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.400 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.450 | 0.000 | 0.000 | 0.000 | 0.000 | 0.233 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 22.400 / 39.400 | 3.717 ± 0.275 | +1.233 ± 0.364 | 17.117 | +7.483 ± 1.063 | 3.433 | 0.079 | 6.500 | +1.267 ± 0.391 | 1929.283 | 0.020 | +0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25108.954 ± 206.628 | +528.742 ± 242.623 | 34878.5 ± 481.6 | -446.2 ± 498.3 | 35.931 | -0.537 ± 0.193 | 15.841 ± 0.301 | +0.921 ± 0.350 | 17.602 | 0.001 | 2608.683 | 19.400 | 17.000 | +0.083 ± 0.225 | 597.388 | 202.200 |
| careful | 22.533 / 39.450 | 2.483 ± 0.192 | — | 9.633 | — | 3.567 | 0.048 | 5.233 | — | 1892.283 | 0.014 | — | 0.000 / 0.000 (0.000 / 0.000) | 24580.212 ± 170.256 | — | 35324.6 ± 425.4 | — | 36.468 | — | 14.919 ± 0.208 | — | 17.445 | 0.001 | 2614.650 | 19.450 | 16.917 | — | 730.616 | 199.833 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (585); p1 1.000/0.000/0.000 (688); p2 1.000/0.000/0.000 (834); p3 1.000/0.000/0.000 (890); p4 1.000/0.000/0.000 (866); p5 1.000/0.000/0.000 (474); p6 1.000/0.000/0.000 (130); p7 1.000/0.000/0.000 (38); p8 1.000/0.000/0.000 (12); p9 1.000/0.000/0.000 (7); p10 1.000/0.000/0.000 (5)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (744); p2 1.000/0.000/0.000 (940); p3 1.000/0.000/0.000 (1011); p4 1.000/0.000/0.000 (999); p5 1.000/0.000/0.000 (285); p6 1.000/0.000/0.000 (13)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2604.0 / 295.4 | 0.22 / 0.13 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | +0.00 ± 0.00 | 0.152 / 0.121 | -0.031 ± 0.004 | 0.054 / 0.059 | 0.001 / 0.000 | 0.056 / 0.056 | +0.000 ± 0.002 | 1.57 / 1.28 | -0.29 ± 0.04 |
| careful | 2609.3 / 262.6 | 0.23 / 0.14 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | +0.00 ± 0.00 | 0.155 / 0.127 | -0.028 ± 0.003 | 0.058 / 0.061 | 0.001 / 0.000 | 0.054 / 0.056 | +0.002 ± 0.002 | 1.56 / 1.28 | -0.28 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.030 ± 0.004 | +0.004 ± 0.002 | +0.001 ± 0.002 |
| careful | -0.09 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.029 ± 0.003 | +0.003 ± 0.002 | +0.002 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.479 / 0.162 | 0.30 / 0.30 | 0.039 / 0.152 | 0.00 / 0.00 | 0.29 / 0.31 | 0.476 / 0.240 |
| careful | 0.478 / 0.141 | 0.29 / 0.31 | 0.039 / 0.166 | 0.00 / 0.00 | 0.26 / 0.31 | 0.452 / 0.243 |
