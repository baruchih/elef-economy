# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5 --troop-no-vote on --seat-draw seats --draw-min 3 --draw-wait on --standby-pay on`, seeds 71-120, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | 35712.2 ± 645.6 | nan ± nan | 3966.4 | 0.967 | 0.000 | 0.000 | 0.037 | 0.035 | 0.258 | 0.029 | 4.02 | 18.16 | 0.18 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.2:0.25 | 0.037 (16231) / 0.035 (130917) | 0.029 (5467) / 0.029 (37672) | 0.028 (4346) / 0.028 (3689) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseM0.2:0.25 | 0.037 (16231) / 0.035 (130917) | 0.029 (5467) / 0.029 (37672) | 0.028 (4346) / 0.028 (3689) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | 0.000 (16231) [rej. blind 0.000] / 0.000 (130917) | 0.000 (5467) / 0.000 (37672) | 0.000 (4346) / 0.000 (3689) | — / — | 1.3 ± 0.2 | -6599 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | — | 0.953 | — (0) | — (0) | 0.000 (18387) | 0.000 (4653) | 0.000 (175282) | 5.800 | 665.380 | 1.194 | 3.131 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | 39.560 | 0.000 | 0.000 | 0.000 | 0.000 | 0.180 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | 23.520 / 39.560 | 4.020 ± 0.278 | — | 21.120 | — | 4.400 | 0.087 | 5.800 | — | 1964.220 | 0.020 | — | 0.000 / 0.000 (0.000 / 0.000) | 23951.038 ± 314.107 | — | 35712.2 ± 645.6 | — | 36.668 | — | 14.897 ± 0.366 | — | 16.894 | 0.001 | 2622.260 | 19.560 | 16.040 | — | 717.159 | 146.220 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:doseM0.2:0.25**: p0 1.000/0.000/0.000 (563); p1 1.000/0.000/0.000 (533); p2 1.000/0.000/0.000 (582); p3 1.000/0.000/0.000 (647); p4 1.000/0.000/0.000 (716); p5 1.000/0.000/0.000 (426); p6 1.000/0.000/0.000 (147); p7 1.000/0.000/0.000 (82); p8 1.000/0.000/0.000 (58); p9 1.000/0.000/0.000 (34); p10 1.000/0.000/0.000 (23); p11 1.000/0.000/0.000 (12); p12 1.000/0.000/0.000 (6); p13 1.000/0.000/0.000 (6); p14 1.000/0.000/0.000 (1)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | 2618.3 / 324.6 | 0.22 / 0.13 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | +0.00 ± 0.00 | 0.156 / 0.122 | -0.034 ± 0.004 | 0.060 / 0.063 | 0.001 / 0.000 | 0.074 / 0.072 | -0.003 ± 0.002 | 1.49 / 1.25 | -0.24 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | -0.07 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.029 ± 0.003 | +0.005 ± 0.002 | -0.002 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:doseM0.2:0.25 | 0.463 / 0.163 | 0.21 / 0.21 | 0.038 / 0.147 | 0.00 / 0.00 | 0.22 / 0.24 | 0.703 / 0.386 |
