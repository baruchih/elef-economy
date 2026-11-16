# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 4`, seeds 71-120, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 30461.0 ± 554.9 | -608.3 ± 473.3 | 2949.6 | 0.977 | 0.000 | 0.000 | 0.023 | 0.023 | 0.000 | 0.130 | 3.08 | 12.12 | 0.30 |
| careful | 31069.3 ± 435.7 | nan ± nan | 2908.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 2.36 | 0.00 | 0.36 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.023 (14829) / 0.023 (132627) | — / 0.130 (23) | — / — | — / — |
| careful | 0.000 (13354) / 0.000 (132033) | — / 0.000 (20) | — / — | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.023 (14829) / 0.023 (132627) | — / 0.130 (23) | — / — | — / — |
| careful | 0.000 (13354) / 0.000 (132033) | — / 0.000 (20) | — / — | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.001 (14829) [rej. blind 0.000] / 0.000 (132627) [rej. blind 0.000] | — / 0.000 (23) | — / — | — / — | 5.8 ± 0.4 | -3326 |
| careful | 0.001 (13354) [rej. blind 0.001] / 0.000 (132033) [rej. blind 0.000] | — / 0.000 (20) | — / — | — / — | 5.7 ± 0.4 | +63 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | — | 0.959 | — (0) | — (0) | 0.000 (12089) | 0.000 (2184) | 0.000 (133206) | 6.720 | 614.180 | 1.197 | 1.804 |
| careful | — | 0.952 | — (0) | — (0) | 0.000 (14219) | 0.000 (294) | 0.000 (130894) | 4.940 | 684.760 | 1.179 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 39.440 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.480 | 0.000 | 0.000 | 0.000 | 0.000 | 0.360 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 19.620 / 39.440 | 3.080 ± 0.244 | +0.720 ± 0.308 | 15.560 | +5.700 ± 0.975 | 3.940 | 0.058 | 6.720 | +1.780 ± 0.395 | 1955.040 | 0.023 | +0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 19768.427 ± 290.476 | -413.703 ± 319.253 | 30461.0 ± 554.9 | -608.3 ± 473.3 | 38.154 | +0.372 ± 0.323 | 14.516 ± 0.341 | +0.417 ± 0.360 | 16.550 | 0.001 | 2655.840 | 19.440 | 19.820 | +1.060 ± 0.317 | 980.587 | 284.920 |
| careful | 20.720 / 39.480 | 2.360 ± 0.189 | — | 9.860 | — | 3.300 | 0.045 | 4.940 | — | 1913.740 | 0.017 | — | 0.000 / 0.000 (0.000 / 0.000) | 20182.130 ± 237.462 | — | 31069.3 ± 435.7 | — | 37.782 | — | 14.099 ± 0.173 | — | 16.830 | 0.001 | 2642.520 | 19.480 | 18.760 | — | 942.867 | 308.120 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.1:0.25**: p0 1.000/0.000/0.000 (543); p1 1.000/0.000/0.000 (518); p2 1.000/0.000/0.000 (488); p3 1.000/0.000/0.000 (485); p4 1.000/0.000/0.000 (473); p5 1.000/0.000/0.000 (281); p6 1.000/0.000/0.000 (59); p7 1.000/0.000/0.000 (17); p8 1.000/0.000/0.000 (9); p9 1.000/0.000/0.000 (8)
- **careful**: p0 1.000/0.000/0.000 (557); p1 1.000/0.000/0.000 (536); p2 1.000/0.000/0.000 (538); p3 1.000/0.000/0.000 (542); p4 1.000/0.000/0.000 (536); p5 1.000/0.000/0.000 (194); p6 1.000/0.000/0.000 (5)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 2652.5 / 296.6 | 0.13 / 0.07 | -0.06 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.093 / 0.073 | -0.020 ± 0.003 | 0.031 / 0.033 | 0.001 / 0.000 | 0.061 / 0.068 | +0.007 ± 0.002 | 1.38 / 1.21 | -0.17 ± 0.04 |
| careful | 2640.7 / 267.1 | 0.19 / 0.11 | -0.08 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.01 ± 0.00 | 0.125 / 0.106 | -0.019 ± 0.003 | 0.045 / 0.049 | 0.001 / 0.000 | 0.059 / 0.065 | +0.006 ± 0.002 | 1.54 / 1.27 | -0.26 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | -0.06 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.019 ± 0.004 | +0.001 ± 0.002 | +0.006 ± 0.002 |
| careful | -0.08 ± 0.01 | +0.00 ± 0.00 | +0.01 ± 0.00 | -0.020 ± 0.003 | +0.004 ± 0.002 | +0.006 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.1:0.25 | 0.000 / 0.000 | 0.61 / — | 0.039 / 0.000 | 0.00 / — | — / — | 0.902 / 0.000 |
| careful | 0.000 / 0.000 | 0.54 / — | 0.041 / 0.000 | 0.00 / — | — / — | 0.889 / 0.000 |
