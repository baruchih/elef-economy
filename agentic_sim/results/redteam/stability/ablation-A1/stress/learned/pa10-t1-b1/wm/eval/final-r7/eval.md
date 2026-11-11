# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/stress/learned/pa10-t1-b1/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 29438.6 ± 503.2 | -6063.6 ± 869.2 | 3317.9 | 0.674 | 0.000 | 0.000 | 0.150 | 0.248 | 0.155 | 0.873 | 25.60 | 125.60 | 0.15 |
| careful | 35502.3 ± 852.9 | nan ± nan | 4637.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.384 | 0.000 | 2.55 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.150 (12683) / 0.248 (43371) | 0.905 (1653) / 0.987 (7282) | 0.287 (502) [rej. blind 0.004] / 0.202 (868) [rej. blind 0.003] | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.150 (12683) / 0.248 (43371) | 0.905 (1653) / 0.987 (7282) | 0.283 (502) / 0.198 (868) | — / — |
| careful | 0.000 (5284) / 0.000 (51900) | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.000 (12683) / 0.000 (43371) | 0.000 (1653) / 0.000 (7282) | 0.004 (502) [rej. blind 0.004] / 0.003 (868) [rej. blind 0.003] | — / — | 0.8 ± 0.2 | -21623 |
| careful | 0.000 (5284) [rej. blind 0.000] / 0.000 (51900) [rej. blind 0.000] | 0.000 (3178) / 0.000 (24974) | 0.000 (3248) / 0.000 (4174) | — / — | 2.2 ± 0.3 | +7 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | — | 1.000 | — (0) | — (0) | — (0) | — (0) | 0.000 (66359) | 45.250 | 191.900 | 1.824 | 2.776 |
| careful | — | 0.910 | — (0) | — (0) | 0.000 (16686) | 0.000 (779) | 0.000 (75293) | 24.350 | 668.700 | 1.190 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.150 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 16.850 / 39.700 | 25.600 ± 0.980 | +23.050 ± 1.139 | 93.250 | +83.150 ± 2.036 | 6.600 | 0.168 | 25.550 | +20.950 ± 0.893 | 1778.550 | 0.063 | +0.038 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 27883.513 ± 369.980 | +2948.863 ± 594.369 | 29438.6 ± 503.2 | -6063.6 ± 869.2 | 28.380 | -7.850 ± 0.448 | 22.398 ± 0.246 | +7.300 ± 0.569 | 21.104 | 0.076 | 2009.250 | 19.700 | 22.850 | +6.050 ± 0.591 | 67.148 | 84.650 |
| careful | 22.950 / 39.750 | 2.550 ± 0.438 | — | 10.100 | — | 3.250 | 0.053 | 4.600 | — | 1896.050 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 24934.650 ± 445.425 | — | 35502.3 ± 852.9 | — | 36.230 | — | 15.098 ± 0.513 | — | 17.953 | 0.001 | 2599.400 | 19.750 | 16.800 | — | 689.070 | 188.600 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 1.000/0.000/0.000 (306); p1 1.000/0.000/0.000 (151); p2 1.000/0.000/0.000 (162); p3 1.000/0.000/0.000 (178); p4 1.000/0.000/0.000 (170); p5 1.000/0.000/0.000 (171); p6 1.000/0.000/0.000 (170); p7 1.000/0.000/0.000 (169); p8 1.000/0.000/0.000 (166); p9 1.000/0.000/0.000 (166); p10 1.000/0.000/0.000 (161); p11 1.000/0.000/0.000 (156); p12 1.000/0.000/0.000 (106); p13 1.000/0.000/0.000 (5)
- **careful**: p0 1.000/0.000/0.000 (605); p1 1.000/0.000/0.000 (751); p2 1.000/0.000/0.000 (913); p3 1.000/0.000/0.000 (1021); p4 1.000/0.000/0.000 (1014); p5 1.000/0.000/0.000 (292); p6 1.000/0.000/0.000 (40); p7 1.000/0.000/0.000 (2)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2168.6 / 634.1 | 1.83 / 2.34 | +0.51 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.03 | -0.01 ± 0.00 | 0.583 / 0.678 | +0.095 ± 0.004 | 0.382 / 0.451 | 0.076 / 0.000 | 0.225 / 0.270 | +0.044 ± 0.004 | 3.54 / 3.80 | +0.26 ± 0.03 |
| careful | 2595.0 / 264.2 | 0.28 / 0.20 | -0.08 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.12 | -0.01 ± 0.00 | 0.170 / 0.144 | -0.025 ± 0.006 | 0.068 / 0.078 | 0.001 / 0.000 | 0.056 / 0.051 | -0.005 ± 0.004 | 1.75 / 1.49 | -0.26 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.06 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.044 ± 0.003 | -0.031 ± 0.004 | +0.004 ± 0.004 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.024 ± 0.005 | +0.011 ± 0.004 | -0.004 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.165 / 0.080 | 0.53 / 0.56 | 0.027 / 0.076 | 0.00 / 0.00 | 0.57 / 0.64 | 0.764 / 0.533 |
| careful | 0.474 / 0.137 | 0.30 / 0.31 | 0.040 / 0.162 | 0.00 / 0.00 | 0.28 / 0.31 | 0.302 / 0.280 |
