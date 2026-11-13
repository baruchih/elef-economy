# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --pi-a0 0.30 --pi-a-max 0.30 --bond-mult-later 1 --w-audit 3`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 36663.2 ± 428.4 | -682.8 ± 519.0 | 4992.4 | 0.989 | 0.000 | 0.000 | 0.000 | 0.000 | 0.429 | 0.026 | 3.03 | 0.68 | 0.35 |
| careful | 37346.0 ± 514.2 | nan ± nan | 5078.2 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.440 | 0.000 | 2.55 | 0.00 | 0.38 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15712) / 0.000 (155311) | 0.033 (23219) / 0.036 (72123) | 0.000 (21474) / 0.000 (11703) | — / — |
| careful | 0.000 (15854) / 0.000 (154792) | 0.000 (24025) / 0.000 (74515) | 0.000 (23099) / 0.000 (12406) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15712) / 0.000 (155311) | 0.033 (23219) / 0.036 (72123) | 0.000 (21474) / 0.000 (11703) | — / — |
| careful | 0.000 (15854) / 0.000 (154792) | 0.000 (24025) / 0.000 (74515) | 0.000 (23099) / 0.000 (12406) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15712) [rej. blind 0.000] / 0.000 (155311) [rej. blind 0.000] | 0.000 (23219) / 0.000 (72123) | 0.000 (21474) / 0.000 (11703) | — / — | 3.7 ± 0.3 | -3317 |
| careful | 0.000 (15854) [rej. blind 0.000] / 0.000 (154792) [rej. blind 0.000] | 0.000 (24025) / 0.000 (74515) | 0.000 (23099) / 0.000 (12406) | — / — | 4.1 ± 0.3 | +29 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | — | 0.909 | — (0) | — (0) | 0.000 (55544) | 0.000 (1302) | 0.000 (242696) | 5.050 | 683.583 | 1.173 | 0.135 |
| careful | — | 0.901 | — (0) | — (0) | 0.000 (60616) | 0.000 (2367) | 0.000 (241708) | 5.150 | 663.317 | 1.172 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 39.733 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.683 | 0.000 | 0.000 | 0.000 | 0.000 | 0.383 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 23.883 / 39.733 | 3.033 ± 0.219 | +0.483 ± 0.291 | 9.867 | -0.117 ± 0.611 | 3.200 | 0.047 | 5.050 | -0.100 ± 0.398 | 1900.283 | 0.024 | -0.001 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 27021.095 ± 215.952 | -627.827 ± 236.951 | 36663.2 ± 428.4 | -682.8 ± 519.0 | 35.598 | +0.075 ± 0.208 | 15.919 ± 0.220 | -0.032 ± 0.351 | 18.161 | 0.001 | 2595.150 | 19.733 | 15.850 | -0.150 ± 0.287 | 554.614 | 226.733 |
| careful | 23.683 / 39.683 | 2.550 ± 0.205 | — | 9.983 | — | 3.600 | 0.048 | 5.150 | — | 1885.183 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 27648.922 ± 209.911 | — | 37346.0 ± 514.2 | — | 35.524 | — | 15.951 ± 0.281 | — | 18.228 | 0.001 | 2586.017 | 19.683 | 16.000 | — | 553.844 | 273.317 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.3audit:0.25**: p0 1.000/0.000/0.000 (596); p1 1.000/0.000/0.000 (772); p2 1.000/0.000/0.000 (1002); p3 1.000/0.000/0.000 (1116); p4 1.000/0.000/0.000 (1119); p5 1.000/0.000/0.000 (329); p6 1.000/0.000/0.000 (3)
- **careful**: p0 1.000/0.000/0.000 (604); p1 1.000/0.000/0.000 (801); p2 1.000/0.000/0.000 (1033); p3 1.000/0.000/0.000 (1133); p4 1.000/0.000/0.000 (1138); p5 1.000/0.000/0.000 (312); p6 1.000/0.000/0.000 (40); p7 1.000/0.000/0.000 (18)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 2588.5 / 261.9 | 0.30 / 0.19 | -0.11 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.13 | -0.00 ± 0.00 | 0.192 / 0.153 | -0.039 ± 0.003 | 0.080 / 0.085 | 0.001 / 0.000 | 0.055 / 0.056 | +0.001 ± 0.002 | 1.66 / 1.38 | -0.28 ± 0.05 |
| careful | 2579.9 / 264.2 | 0.32 / 0.21 | -0.11 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | -0.00 ± 0.00 | 0.194 / 0.159 | -0.034 ± 0.003 | 0.077 / 0.087 | 0.001 / 0.000 | 0.054 / 0.052 | -0.001 ± 0.002 | 1.74 / 1.37 | -0.37 ± 0.05 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.039 ± 0.003 | +0.005 ± 0.002 | +0.001 ± 0.002 |
| careful | -0.11 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.036 ± 0.003 | +0.009 ± 0.002 | -0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.457 / 0.131 | 0.34 / 0.35 | 0.039 / 0.161 | 0.00 / 0.00 | 0.34 / 0.35 | 0.325 / 0.268 |
| careful | 0.474 / 0.134 | 0.30 / 0.31 | 0.040 / 0.163 | 0.00 / 0.00 | 0.30 / 0.32 | 0.301 / 0.254 |
