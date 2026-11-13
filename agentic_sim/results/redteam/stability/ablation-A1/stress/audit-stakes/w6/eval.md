# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --pi-a0 0.20 --pi-a-max 0.20 --bond-mult-later 4 --w-audit 1.5`, seeds 21-80, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 33739.8 ± 422.5 | 283.4 ± 341.3 | 4739.3 | 0.988 | 0.000 | 0.000 | 0.000 | 0.000 | 0.396 | 0.030 | 2.97 | 0.62 | 0.28 |
| careful | 33456.4 ± 399.3 | nan ± nan | 4791.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.404 | 0.000 | 2.62 | 0.00 | 0.28 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15784) / 0.000 (155836) | 0.040 (15934) / 0.038 (70559) | 0.000 (14838) / 0.000 (11406) | — / — |
| careful | 0.000 (15719) / 0.000 (155643) | 0.000 (16212) / 0.000 (72027) | 0.000 (15891) / 0.000 (11988) | — / — |

The stressed world's fourth action by seat kind — the allowance claimed and the verdict F without inspecting (counted above among the blind verdicts; the ledger sees a careful review, so the measured reading below cannot see it):

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.000 (15784) / 0.000 (155836) | 0.040 (15934) / 0.038 (70559) | 0.000 (14838) / 0.000 (11406) | — / — |
| careful | 0.000 (15719) / 0.000 (155643) | 0.000 (16212) / 0.000 (72027) | 0.000 (15891) / 0.000 (11988) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.001 (15784) [rej. blind 0.000] / 0.001 (155836) [rej. blind 0.000] | 0.000 (15934) / 0.001 (70559) [rej. blind 0.000] | 0.000 (14838) / 0.001 (11406) | — / — | 8.3 ± 0.3 | -3173 |
| careful | 0.001 (15719) [rej. blind 0.000] / 0.001 (155643) [rej. blind 0.000] | 0.000 (16212) / 0.001 (72027) [rej. blind 0.000] | 0.000 (15891) / 0.001 (11988) | — / — | 8.4 ± 0.4 | +178 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | — | 0.913 | — (0) | — (0) | 0.000 (49639) | 0.000 (1664) | 0.000 (233054) | 5.183 | 695.717 | 1.191 | 0.119 |
| careful | — | 0.907 | — (0) | — (0) | 0.000 (54654) | 0.000 (898) | 0.000 (231928) | 4.700 | 693.567 | 1.153 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.283 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.283 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 23.250 / 39.700 | 2.967 ± 0.204 | +0.350 ± 0.260 | 10.117 | +0.700 ± 0.552 | 3.100 | 0.055 | 5.183 | +0.483 ± 0.343 | 1908.083 | 0.024 | -0.000 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24492.466 ± 199.673 | -316.349 ± 199.651 | 33739.8 ± 422.5 | +283.4 ± 341.3 | 35.588 | +0.047 ± 0.179 | 15.727 ± 0.248 | -0.273 ± 0.271 | 18.293 | 0.002 | 2598.767 | 19.700 | 16.450 | +0.000 ± 0.265 | 542.075 | 316.900 |
| careful | 23.250 / 39.700 | 2.617 ± 0.199 | — | 9.417 | — | 3.300 | 0.052 | 4.700 | — | 1889.067 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 24808.815 ± 186.235 | — | 33456.4 ± 399.3 | — | 35.540 | — | 16.000 ± 0.235 | — | 18.390 | 0.002 | 2597.300 | 19.700 | 16.450 | — | 536.301 | 328.383 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **mix:dose0.3audit:0.25**: p0 1.000/0.000/0.000 (575); p1 1.000/0.000/0.000 (733); p2 1.000/0.000/0.000 (942); p3 1.000/0.000/0.000 (1036); p4 1.000/0.000/0.000 (1066); p5 1.000/0.000/0.000 (311); p6 1.000/0.000/0.000 (20)
- **careful**: p0 1.000/0.000/0.000 (578); p1 1.000/0.000/0.000 (752); p2 1.000/0.000/0.000 (976); p3 1.000/0.000/0.000 (1074); p4 1.000/0.000/0.000 (1084); p5 1.000/0.000/0.000 (321); p6 1.000/0.000/0.000 (6)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 2597.3 / 263.1 | 0.31 / 0.20 | -0.11 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.11 | -0.01 ± 0.00 | 0.186 / 0.151 | -0.036 ± 0.003 | 0.075 / 0.081 | 0.002 / 0.000 | 0.058 / 0.057 | -0.001 ± 0.002 | 1.79 / 1.52 | -0.26 ± 0.06 |
| careful | 2594.1 / 262.0 | 0.33 / 0.22 | -0.10 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | -0.00 ± 0.00 | 0.187 / 0.159 | -0.028 ± 0.003 | 0.073 / 0.080 | 0.002 / 0.000 | 0.057 / 0.055 | -0.001 ± 0.002 | 1.81 / 1.54 | -0.27 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.036 ± 0.003 | +0.006 ± 0.002 | -0.001 ± 0.002 |
| careful | -0.10 ± 0.01 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.029 ± 0.003 | +0.007 ± 0.002 | -0.001 ± 0.002 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| mix:dose0.3audit:0.25 | 0.446 / 0.131 | 0.35 / 0.36 | 0.040 / 0.163 | 0.00 / 0.00 | 0.34 / 0.37 | 0.339 / 0.279 |
| careful | 0.456 / 0.131 | 0.31 / 0.32 | 0.040 / 0.165 | 0.00 / 0.00 | 0.30 / 0.33 | 0.320 / 0.269 |
