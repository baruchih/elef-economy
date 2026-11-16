# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 3`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 34587.4 ± 449.2 | -467.3 ± 535.7 | 4690.6 | 0.980 | 0.000 | 0.000 | 0.026 | 0.025 | 0.384 | 0.013 | 3.62 | 13.05 | 0.32 |
| careful | 35054.7 ± 506.2 | nan ± nan | 4613.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.382 | 0.000 | 2.58 | 0.00 | 0.38 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.026 (17890) / 0.025 (155356) | 0.014 (10461) / 0.013 (75510) | 0.011 (9940) / 0.013 (12278) | — / — |
| careful | 0.000 (15843) / 0.000 (155294) | 0.000 (9494) / 0.000 (74217) | 0.000 (9707) / 0.000 (12279) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.026 (17890) / 0.025 (155356) | 0.014 (10461) / 0.013 (75510) | 0.011 (9940) / 0.013 (12278) | — / — |
| careful | 0.000 (15843) / 0.000 (155294) | 0.000 (9494) / 0.000 (74217) | 0.000 (9707) / 0.000 (12279) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 (17890) [rej. blind 0.000] / 0.000 (155356) [rej. blind 0.000] | 0.000 (10461) / 0.000 (75510) | 0.000 (9940) / 0.000 (12278) | — / — | 4.0 ± 0.4 | -5635 |
| careful | 0.000 (15843) [rej. blind 0.000] / 0.000 (155294) [rej. blind 0.000] | 0.000 (9494) / 0.000 (74217) | 0.000 (9707) / 0.000 (12279) | — / — | 4.1 ± 0.4 | +43 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.927 | — (0) | — (0) | 0.000 (40096) | 0.000 (7864) | 0.000 (233475) | 6.817 | 638.617 | 1.183 | 1.914 |
| careful | — | 0.912 | — (0) | — (0) | 0.000 (49652) | 0.000 (1451) | 0.000 (225731) | 5.200 | 685.967 | 1.160 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.717 | 0.000 | 0.000 | 0.000 | 0.000 | 0.317 | 0.000 |
| careful | 39.783 | 0.000 | 0.000 | 0.000 | 0.000 | 0.383 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 22.250 / 39.717 | 3.617 ± 0.232 | +1.033 ± 0.332 | 16.317 | +5.833 ± 1.084 | 3.500 | 0.078 | 6.817 | +1.617 ± 0.396 | 1922.483 | 0.029 | +0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25900.633 ± 284.379 | +511.949 ± 311.135 | 34587.4 ± 449.2 | -467.3 ± 535.7 | 35.392 | -0.265 ± 0.247 | 16.471 ± 0.306 | +0.842 ± 0.387 | 18.166 | 0.001 | 2594.550 | 19.717 | 17.467 | +0.717 ± 0.279 | 490.211 | 268.833 |
| careful | 23.033 / 39.783 | 2.583 ± 0.243 | — | 10.483 | — | 3.350 | 0.055 | 5.200 | — | 1885.033 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 25388.684 ± 224.203 | — | 35054.7 ± 506.2 | — | 35.657 | — | 15.629 ± 0.261 | — | 18.156 | 0.001 | 2592.217 | 19.783 | 16.750 | — | 590.517 | 226.567 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (584); p1 1.000/0.000/0.000 (698); p2 1.000/0.000/0.000 (848); p3 1.000/0.000/0.000 (898); p4 1.000/0.000/0.000 (886); p5 1.000/0.000/0.000 (416); p6 1.000/0.000/0.000 (138); p7 1.000/0.000/0.000 (67); p8 1.000/0.000/0.000 (29); p9 1.000/0.000/0.000 (23); p10 1.000/0.000/0.000 (8); p11 1.000/0.000/0.000 (2)
- **careful**: p0 1.000/0.000/0.000 (602); p1 1.000/0.000/0.000 (733); p2 1.000/0.000/0.000 (928); p3 1.000/0.000/0.000 (995); p4 1.000/0.000/0.000 (1002); p5 1.000/0.000/0.000 (342); p6 1.000/0.000/0.000 (12)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2589.3 / 298.2 | 0.29 / 0.18 | -0.11 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.13 | +0.00 ± 0.00 | 0.197 / 0.157 | -0.040 ± 0.003 | 0.082 / 0.089 | 0.001 / 0.000 | 0.057 / 0.055 | -0.003 ± 0.002 | 1.69 / 1.42 | -0.27 ± 0.04 |
| careful | 2588.2 / 264.1 | 0.30 / 0.20 | -0.11 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | +0.00 ± 0.00 | 0.198 / 0.161 | -0.037 ± 0.003 | 0.083 / 0.091 | 0.001 / 0.000 | 0.055 / 0.050 | -0.005 ± 0.002 | 1.77 / 1.40 | -0.37 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.040 ± 0.003 | +0.006 ± 0.002 | -0.002 ± 0.002 |
| careful | -0.11 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.038 ± 0.003 | +0.007 ± 0.002 | -0.004 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.479 / 0.165 | 0.29 / 0.30 | 0.038 / 0.142 | 0.00 / 0.00 | 0.27 / 0.29 | 0.310 / 0.236 |
| careful | 0.471 / 0.140 | 0.30 / 0.33 | 0.040 / 0.164 | 0.00 / 0.00 | 0.29 / 0.32 | 0.304 / 0.252 |
