# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful-290-own/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 34869.9 ± 719.5 | -740.1 ± 581.4 | 3929.9 | 0.862 | 0.138 | 0.000 | 0.005 | 0.004 | 0.268 | 0.507 | 13.65 | 9.35 | 0.30 |
| careful | 35610.0 ± 690.2 | nan ± nan | 4142.1 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 | 6.10 | 0.00 | 0.30 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.005 (5215) / 0.004 (52346) | 0.570 (875) / 0.605 (16683) | 0.062 (903) / 0.002 (2576) | — / — |
| careful | 0.000 (5358) / 0.000 (52610) | 0.000 (945) / 0.000 (18926) | 0.000 (1365) / 0.000 (3638) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.383 | 0.762 | 0.304 (23443) | 0.162 (3903) | 0.397 (3988) | 0.058 (690) | 0.033 (46574) | 24.600 | 750.650 | 1.195 | 0.380 |
| careful | — | 0.683 | 0.000 (25992) | 0.000 (5627) | 0.000 (4615) | 0.000 (1110) | 0.000 (45498) | 25.300 | 722.750 | 1.157 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 23.200 / 39.650 | 13.650 ± 1.001 | +7.550 ± 0.980 | 9.950 | -0.500 ± 0.829 | 3.500 | 0.060 | 4.950 | -0.700 ± 0.805 | 1660.450 | 0.016 | -0.008 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24105.275 ± 390.834 | +386.461 ± 475.304 | 34869.9 ± 719.5 | -740.1 ± 581.4 | 37.426 | +0.059 ± 0.561 | 14.790 ± 0.384 | +0.616 ± 0.374 | 17.977 | 0.002 | 2618.650 | 19.650 | 16.450 | -0.050 ± 0.380 | 932.410 | 172.100 |
| careful | 23.150 / 39.650 | 6.100 ± 0.355 | — | 10.450 | — | 3.400 | 0.055 | 5.650 | — | 1630.350 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 23718.813 ± 303.512 | — | 35610.0 ± 690.2 | — | 37.367 | — | 14.175 ± 0.294 | — | 17.614 | 0.001 | 2633.550 | 19.650 | 16.500 | — | 903.473 | 232.300 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.953/0.047/0.000 (591); p1 0.869/0.131/0.000 (677); p2 0.822/0.178/0.000 (796); p3 0.778/0.222/0.000 (853); p4 0.893/0.107/0.000 (810); p5 0.943/0.057/0.000 (203)
- **careful**: p0 1.000/0.000/0.000 (590); p1 1.000/0.000/0.000 (737); p2 1.000/0.000/0.000 (863); p3 1.000/0.000/0.000 (903); p4 1.000/0.000/0.000 (771); p5 1.000/0.000/0.000 (264); p6 1.000/0.000/0.000 (14)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2617.3 / 260.8 | 0.26 / 0.16 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.05 | -0.00 ± 0.00 | 0.160 / 0.133 | -0.028 ± 0.006 | 0.057 / 0.064 | 0.002 / 0.000 | 0.064 / 0.069 | +0.006 ± 0.005 | 1.68 / 1.31 | -0.37 ± 0.10 |
| careful | 2630.5 / 267.9 | 0.23 / 0.14 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.00 ± 0.00 | 0.156 / 0.127 | -0.029 ± 0.005 | 0.055 / 0.063 | 0.001 / 0.000 | 0.062 / 0.062 | +0.000 ± 0.003 | 1.51 / 1.17 | -0.34 ± 0.09 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.028 ± 0.006 | +0.007 ± 0.003 | +0.006 ± 0.005 |
| careful | -0.08 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.025 ± 0.005 | +0.009 ± 0.003 | +0.000 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.316 / 0.089 | 0.48 / 0.50 | 0.040 / 0.165 | 0.00 / 0.00 | 0.41 / 0.48 | 0.377 / 0.327 |
| careful | 0.357 / 0.106 | 0.38 / 0.42 | 0.038 / 0.158 | 0.00 / 0.00 | 0.29 / 0.31 | 0.308 / 0.256 |
