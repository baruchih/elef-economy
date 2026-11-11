# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 2`, seeds 21-40, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct | 30919.4 ± 518.6 | nan ± nan | 3448.3 | 0.895 | 0.006 | 0.000 | 0.079 | 0.117 | 0.064 | 0.055 | 4.05 | 61.00 | 0.35 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:direct | 0.079 (14109) [rej. blind 0.000] / 0.117 (50459) [rej. blind 0.000] | — / 0.091 (110) | 0.053 (1865) / 0.056 (2424) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:direct | 0.073 (14109) / 0.111 (50459) | — / 0.082 (110) | 0.052 (1865) / 0.052 (2424) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:direct | 0.007 (14109) [rej. blind 0.001] / 0.008 (50459) [rej. blind 0.000] | — / 0.009 (110) | 0.001 (1865) / 0.003 (2424) | — / — | 5.2 ± 0.6 | -6758 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct | 1.000 | 1.000 | — (0) | — (0) | 0.000 (9) | — (0) | 0.006 (68958) | 35.000 | 301.400 | 1.428 | 1.743 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:direct | 39.350 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct | 17.750 / 39.350 | 4.050 ± 0.413 | — | 65.350 | — | 7.650 | 0.107 | 15.650 | — | 1995.100 | 0.044 | — | 0.000 / 0.000 (0.000 / 0.000) | 25635.631 ± 281.916 | — | 30919.4 ± 518.6 | — | 32.959 | — | 18.799 ± 0.353 | — | 17.815 | 0.003 | 2522.150 | 19.350 | 21.600 | — | 57.051 | 176.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:direct**: p0 0.998/0.002/0.000 (417); p1 0.978/0.021/0.001 (261); p2 0.988/0.012/0.000 (198); p3 0.989/0.011/0.000 (197); p4 0.991/0.009/0.000 (202); p5 0.989/0.011/0.000 (203); p6 0.994/0.006/0.000 (204); p7 0.997/0.003/0.000 (207); p8 0.998/0.002/0.000 (206); p9 0.999/0.001/0.000 (204); p10 1.000/0.000/0.000 (202); p11 0.997/0.002/0.001 (204); p12 0.999/0.001/0.000 (192); p13 0.996/0.003/0.001 (136); p14 0.984/0.016/0.000 (57); p15 1.000/0.000/0.000 (16)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:direct | 2522.9 / 705.5 | 0.50 / 0.63 | +0.14 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | -0.01 ± 0.00 | 0.307 / 0.327 | +0.020 ± 0.008 | 0.146 / 0.170 | 0.003 / 0.000 | 0.119 / 0.141 | +0.022 ± 0.004 | 2.18 / 2.32 | +0.14 ± 0.04 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:direct | +0.02 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.043 ± 0.004 | -0.013 ± 0.004 | +0.001 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:direct | 0.002 / 0.000 | 0.27 / — | 0.035 / 0.089 | 0.00 / 0.00 | 0.07 / 0.10 | 0.989 / 0.047 |
