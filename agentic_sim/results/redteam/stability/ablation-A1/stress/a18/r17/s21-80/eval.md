# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | 34708.4 ± 495.8 | nan ± nan | 4676.1 | 0.980 | 0.000 | 0.000 | 0.038 | 0.031 | 0.381 | 0.000 | 2.98 | 16.32 | 0.33 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseG1.0:0.25 | 0.038 (18317) / 0.031 (155309) | 0.000 (11063) / 0.000 (78051) | 0.000 (10829) / 0.000 (6995) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseG1.0:0.25 | 0.038 (18317) / 0.031 (155309) | 0.000 (11063) / 0.000 (78051) | 0.000 (10829) / 0.000 (6995) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | 0.000 (18317) [rej. blind 0.000] / 0.000 (155309) [rej. blind 0.000] | 0.000 (11063) / 0.000 (78051) | 0.000 (10829) / 0.000 (6995) | — / — | 2.2 ± 0.2 | -5531 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | — | 0.930 | — (0) | — (0) | 0.000 (39096) | 0.000 (4841) | 0.000 (236627) | 6.183 | 647.983 | 1.189 | 2.639 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | 39.450 | 0.000 | 0.000 | 0.000 | 0.000 | 0.333 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | 22.000 / 39.450 | 2.983 ± 0.227 | — | 19.350 | — | 3.700 | 0.112 | 6.183 | — | 1926.633 | 0.022 | — | 0.000 / 0.000 (0.000 / 0.000) | 25697.063 ± 263.748 | — | 34708.4 ± 495.8 | — | 35.561 | — | 16.502 ± 0.438 | — | 17.796 | 0.001 | 2593.433 | 19.450 | 17.450 | — | 546.904 | 197.050 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:doseG1.0:0.25**: p0 1.000/0.000/0.000 (592); p1 1.000/0.000/0.000 (711); p2 1.000/0.000/0.000 (893); p3 1.000/0.000/0.000 (935); p4 1.000/0.000/0.000 (855); p5 1.000/0.000/0.000 (360); p6 1.000/0.000/0.000 (108); p7 1.000/0.000/0.000 (53); p8 1.000/0.000/0.000 (35); p9 1.000/0.000/0.000 (11); p10 1.000/0.000/0.000 (12); p11 1.000/0.000/0.000 (13); p12 1.000/0.000/0.000 (5)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | 2588.5 / 305.3 | 0.27 / 0.16 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.14 | +0.01 ± 0.00 | 0.170 / 0.131 | -0.039 ± 0.004 | 0.067 / 0.069 | 0.001 / 0.000 | 0.055 / 0.055 | +0.001 ± 0.002 | 1.70 / 1.44 | -0.26 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.037 ± 0.003 | +0.002 ± 0.002 | +0.000 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:doseG1.0:0.25 | 0.496 / 0.178 | 0.27 / 0.25 | 0.038 / 0.149 | 0.00 / 0.00 | 0.26 / 0.29 | 0.465 / 0.222 |
