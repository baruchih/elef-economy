# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-max 0.10`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-pifloor2-280/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 32391.8 ± 648.5 | -2757.9 ± 784.0 | 3057.9 | 0.646 | 0.353 | 0.000 | 0.287 | 0.292 | 0.119 | 0.831 | 38.20 | 168.85 | 0.05 |
| careful | 35149.6 ± 922.9 | nan ± nan | 4055.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.286 | 0.000 | 6.00 | 0.00 | 0.35 |
| stamper | 13906.7 ± 336.6 | -21242.9 ± 947.6 | 1918.1 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.011 | 1.000 | 24.20 | 342.95 | 0.80 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.287 (4854) / 0.292 (49036) | 0.963 (297) / 0.951 (5757) | 0.206 (160) / 0.234 (1055) | — / — |
| careful | 0.000 (5219) / 0.000 (52663) | 0.000 (629) / 0.000 (18737) | 0.000 (190) / 0.000 (3679) | — / — |
| stamper | 1.000 (3399) / 1.000 (34523) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.923 | 0.975 | 0.785 (311) | 0.860 (972) | 0.748 (922) | 0.504 (7393) | 0.315 (51561) | 44.950 | 568.950 | 1.739 | 3.756 |
| careful | — | 0.688 | 0.000 (25128) | 0.000 (5096) | 0.000 (4809) | 0.000 (1087) | 0.000 (44997) | 24.950 | 710.150 | 1.145 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (38362) | 88.500 | 343.900 | 2.262 | 3.875 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.800 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 22.900 / 39.650 | 38.200 ± 3.774 | +32.200 ± 3.937 | 59.550 | +48.650 ± 1.944 | 2.250 | 0.378 | 25.300 | +20.050 ± 1.006 | 1988.400 | 0.070 | +0.045 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 26733.335 ± 451.424 | +3362.053 ± 472.578 | 32391.8 ± 648.5 | -2757.9 ± 784.0 | 32.057 | -5.414 ± 0.452 | 17.718 ± 0.243 | +3.480 ± 0.437 | 19.223 | 0.001 | 2454.500 | 19.650 | 16.750 | +0.150 ± 0.472 | 57.131 | 134.350 |
| careful | 23.100 / 39.700 | 6.000 ± 0.598 | — | 10.900 | — | 2.750 | 0.068 | 5.250 | — | 1622.800 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23371.282 ± 330.427 | — | 35149.6 ± 922.9 | — | 37.471 | — | 14.238 ± 0.447 | — | 17.574 | 0.001 | 2637.300 | 19.700 | 16.600 | — | 930.099 | 213.600 |
| stamper | 10.700 / 39.950 | 24.200 ± 1.109 | +18.200 ± 1.500 | 127.100 | +116.200 ± 1.657 | 0.000 | 1.000 | 68.550 | +63.300 ± 1.131 | 1720.700 | 0.191 | +0.166 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 18619.481 ± 387.915 | -4751.801 ± 421.599 | 13906.7 ± 336.6 | -21242.9 ± 947.6 | 24.415 | -13.056 ± 0.474 | 30.020 ± 0.633 | +15.782 ± 0.792 | 24.655 | 0.407 | 1041.450 | 19.950 | 29.250 | +12.650 ± 0.716 | 710.090 | 138.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.827/0.173/0.000 (587); p1 0.604/0.395/0.001 (605); p2 0.611/0.389/0.000 (630); p3 0.574/0.426/0.000 (620); p4 0.615/0.385/0.000 (576); p5 0.607/0.393/0.000 (41)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (716); p2 1.000/0.000/0.000 (848); p3 1.000/0.000/0.000 (916); p4 1.000/0.000/0.000 (787); p5 1.000/0.000/0.000 (195)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (444); p2 0.000/1.000/0.000 (357); p3 0.000/1.000/0.000 (353); p4 0.000/1.000/0.000 (203)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2451.8 / 242.7 | 0.62 / 0.56 | -0.06 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.01 | -0.00 ± 0.00 | 0.409 / 0.343 | -0.067 ± 0.006 | 0.203 / 0.202 | 0.001 / 0.000 | 0.095 / 0.104 | +0.010 ± 0.006 | 2.04 / 1.86 | -0.18 ± 0.09 |
| careful | 2633.2 / 260.9 | 0.22 / 0.12 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.00 ± 0.00 | 0.162 / 0.129 | -0.033 ± 0.006 | 0.060 / 0.063 | 0.000 / 0.000 | 0.061 / 0.060 | -0.002 ± 0.004 | 1.48 / 1.24 | -0.24 ± 0.08 |
| stamper | 1726.2 / 169.9 | 1.76 / 1.26 | -0.49 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.01 | -0.01 ± 0.00 | 0.554 / 0.441 | -0.112 ± 0.006 | 0.403 / 0.328 | 0.398 / 0.361 | 0.106 / 0.084 | -0.022 ± 0.006 | 4.02 / 2.75 | -1.27 ± 0.20 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.06 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.067 ± 0.006 | -0.001 ± 0.006 | +0.010 ± 0.006 |
| careful | -0.10 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.034 ± 0.006 | +0.003 ± 0.003 | -0.002 ± 0.004 |
| stamper | -0.50 ± 0.04 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.113 ± 0.006 | -0.076 ± 0.007 | -0.023 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.117 / 0.061 | 0.63 / 0.66 | 0.027 / 0.009 | 0.00 / 0.00 | 0.55 / 0.75 | 0.809 / 0.595 |
| careful | 0.353 / 0.119 | 0.36 / 0.40 | 0.039 / 0.010 | 0.00 / 0.00 | 0.29 / 0.37 | 0.312 / 0.131 |
| stamper | 0.013 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.206 / 1.725 |
