# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --arm 1 --pi-a0 0.10 --pi-a-max 0.10 --w-audit 1.5`, seeds 121-170, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | 35996.3 ± 492.3 | -268.2 ± 421.2 | 4653.3 | 0.984 | 0.000 | 0.000 | 0.022 | 0.018 | 0.380 | 0.011 | 2.86 | 9.78 | 0.40 |
| careful | 36264.5 ± 503.9 | nan ± nan | 4617.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.377 | 0.000 | 2.30 | 0.00 | 0.32 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseF0.3:0.25 | 0.022 (14184) / 0.018 (130038) | 0.013 (8721) / 0.011 (64958) | 0.014 (8792) / 0.010 (5972) | — / — |
| careful | 0.000 (13428) / 0.000 (130292) | 0.000 (8353) / 0.000 (64302) | 0.000 (8415) / 0.000 (6078) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:doseF0.3:0.25 | 0.022 (14184) / 0.018 (130038) | 0.013 (8721) / 0.011 (64958) | 0.014 (8792) / 0.010 (5972) | — / — |
| careful | 0.000 (13428) / 0.000 (130292) | 0.000 (8353) / 0.000 (64302) | 0.000 (8415) / 0.000 (6078) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | 0.000 (14184) [rej. blind 0.000] / 0.000 (130038) | 0.000 (8721) / 0.000 (64958) | 0.000 (8792) / 0.000 (5972) | — / — | 2.6 ± 0.3 | -3635 |
| careful | 0.000 (13428) [rej. blind 0.000] / 0.000 (130292) [rej. blind 0.000] | 0.000 (8353) / 0.000 (64302) | 0.000 (8415) / 0.000 (6078) | — / — | 2.4 ± 0.3 | +18 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | — | 0.923 | — (0) | — (0) | 0.000 (35490) | 0.000 (4175) | 0.000 (193000) | 5.720 | 658.240 | 1.197 | 1.710 |
| careful | — | 0.912 | — (0) | — (0) | 0.000 (41551) | 0.000 (2058) | 0.000 (187259) | 5.580 | 674.040 | 1.162 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | 39.600 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.580 | 0.000 | 0.000 | 0.000 | 0.000 | 0.320 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | 22.760 / 39.600 | 2.860 ± 0.241 | +0.560 ± 0.251 | 15.540 | +4.740 ± 1.166 | 3.140 | 0.097 | 5.720 | +0.140 ± 0.319 | 1922.260 | 0.019 | +0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25038.169 ± 207.392 | -26.715 ± 206.604 | 35996.3 ± 492.3 | -268.2 ± 421.2 | 36.279 | -0.160 ± 0.200 | 15.101 ± 0.259 | +0.354 ± 0.279 | 17.424 | 0.000 | 2606.880 | 19.600 | 16.840 | +0.400 ± 0.232 | 691.178 | 198.640 |
| careful | 23.140 / 39.580 | 2.300 ± 0.229 | — | 10.800 | — | 3.060 | 0.051 | 5.580 | — | 1897.220 | 0.014 | — | 0.000 / 0.000 (0.000 / 0.000) | 25064.885 ± 213.608 | — | 36264.5 ± 503.9 | — | 36.439 | — | 14.747 ± 0.219 | — | 17.435 | 0.001 | 2611.040 | 19.580 | 16.440 | — | 716.635 | 235.280 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:doseF0.3:0.25**: p0 1.000/0.000/0.000 (591); p1 1.000/0.000/0.000 (753); p2 1.000/0.000/0.000 (899); p3 1.000/0.000/0.000 (945); p4 1.000/0.000/0.000 (918); p5 1.000/0.000/0.000 (351); p6 1.000/0.000/0.000 (66); p7 1.000/0.000/0.000 (36); p8 1.000/0.000/0.000 (14); p9 1.000/0.000/0.000 (6)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (778); p2 1.000/0.000/0.000 (902); p3 1.000/0.000/0.000 (981); p4 1.000/0.000/0.000 (977); p5 1.000/0.000/0.000 (330); p6 1.000/0.000/0.000 (51); p7 1.000/0.000/0.000 (4)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | 2600.8 / 283.7 | 0.23 / 0.15 | -0.08 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.00 ± 0.00 | 0.156 / 0.124 | -0.032 ± 0.003 | 0.060 / 0.062 | 0.000 / 0.000 | 0.054 / 0.051 | -0.003 ± 0.002 | 1.54 / 1.32 | -0.22 ± 0.05 |
| careful | 2605.8 / 268.6 | 0.22 / 0.13 | -0.09 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | +0.00 ± 0.00 | 0.159 / 0.125 | -0.033 ± 0.003 | 0.061 / 0.068 | 0.001 / 0.000 | 0.053 / 0.051 | -0.002 ± 0.002 | 1.56 / 1.33 | -0.23 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | -0.08 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.030 ± 0.003 | +0.003 ± 0.002 | -0.003 ± 0.002 |
| careful | -0.09 ± 0.01 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.035 ± 0.003 | +0.006 ± 0.002 | -0.002 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:doseF0.3:0.25 | 0.493 / 0.162 | 0.29 / 0.30 | 0.039 / 0.161 | 0.00 / 0.00 | 0.30 / 0.32 | 0.456 / 0.239 |
| careful | 0.488 / 0.152 | 0.29 / 0.32 | 0.039 / 0.159 | 0.00 / 0.00 | 0.26 / 0.30 | 0.440 / 0.237 |
