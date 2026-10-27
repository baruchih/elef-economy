# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-max 0.10`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-pifloor2-280/wm/models/wm-online-5.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 30271.8 ± 561.4 | -4877.8 ± 898.1 | 2905.6 | 0.632 | 0.367 | 0.001 | 0.328 | 0.331 | 0.072 | 0.851 | 30.35 | 178.85 | 0.05 |
| careful | 35149.6 ± 922.9 | nan ± nan | 4055.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.286 | 0.000 | 6.00 | 0.00 | 0.35 |
| stamper | 13906.7 ± 336.6 | -21242.9 ± 947.6 | 1918.1 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.011 | 1.000 | 24.20 | 342.95 | 0.80 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.328 (4857) / 0.331 (49069) | 0.971 (171) / 0.949 (3288) | 0.391 (92) / 0.380 (635) | — / — |
| careful | 0.000 (5219) / 0.000 (52663) | 0.000 (629) / 0.000 (18737) | 0.000 (190) / 0.000 (3679) | — / — |
| stamper | 1.000 (3399) / 1.000 (34523) | — / 1.000 (440) | — / — | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.952 | 0.988 | 0.910 (78) | 0.900 (409) | 0.926 (584) | 0.571 (4806) | 0.337 (52235) | 47.450 | 587.300 | 1.702 | 3.769 |
| careful | — | 0.688 | 0.000 (25128) | 0.000 (5096) | 0.000 (4809) | 0.000 (1087) | 0.000 (44997) | 24.950 | 710.150 | 1.145 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (38362) | 88.500 | 343.900 | 2.262 | 3.875 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.800 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 24.000 / 39.800 | 30.350 ± 1.860 | +24.350 ± 1.801 | 66.250 | +55.350 ± 1.866 | 2.150 | 0.380 | 27.650 | +22.400 ± 1.035 | 2017.600 | 0.082 | +0.057 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 25505.998 ± 323.604 | +2134.716 ± 400.732 | 30271.8 ± 561.4 | -4877.8 ± 898.1 | 31.977 | -5.494 ± 0.376 | 18.191 ± 0.393 | +3.953 ± 0.566 | 19.172 | 0.002 | 2453.850 | 19.800 | 15.800 | -0.800 ± 0.521 | 52.053 | 123.500 |
| careful | 23.100 / 39.700 | 6.000 ± 0.598 | — | 10.900 | — | 2.750 | 0.068 | 5.250 | — | 1622.800 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23371.282 ± 330.427 | — | 35149.6 ± 922.9 | — | 37.471 | — | 14.238 ± 0.447 | — | 17.574 | 0.001 | 2637.300 | 19.700 | 16.600 | — | 930.099 | 213.600 |
| stamper | 10.700 / 39.950 | 24.200 ± 1.109 | +18.200 ± 1.500 | 127.100 | +116.200 ± 1.657 | 0.000 | 1.000 | 68.550 | +63.300 ± 1.131 | 1720.700 | 0.191 | +0.166 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 18619.481 ± 387.915 | -4751.801 ± 421.599 | 13906.7 ± 336.6 | -21242.9 ± 947.6 | 24.415 | -13.056 ± 0.474 | 30.020 ± 0.633 | +15.782 ± 0.792 | 24.655 | 0.407 | 1041.450 | 19.950 | 29.250 | +12.650 ± 0.716 | 710.090 | 138.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.819/0.181/0.000 (585); p1 0.557/0.441/0.002 (602); p2 0.577/0.423/0.000 (573); p3 0.575/0.423/0.002 (557); p4 0.634/0.365/0.000 (547); p5 0.563/0.400/0.037 (42)
- **careful**: p0 1.000/0.000/0.000 (594); p1 1.000/0.000/0.000 (716); p2 1.000/0.000/0.000 (848); p3 1.000/0.000/0.000 (916); p4 1.000/0.000/0.000 (787); p5 1.000/0.000/0.000 (195)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (444); p2 0.000/1.000/0.000 (357); p3 0.000/1.000/0.000 (353); p4 0.000/1.000/0.000 (203)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2453.4 / 242.8 | 0.62 / 0.58 | -0.04 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.01 / 0.01 | -0.00 ± 0.00 | 0.425 / 0.345 | -0.079 ± 0.008 | 0.213 / 0.199 | 0.002 / 0.003 | 0.098 / 0.113 | +0.015 ± 0.005 | 1.97 / 1.80 | -0.17 ± 0.06 |
| careful | 2633.2 / 260.9 | 0.22 / 0.12 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.07 | +0.00 ± 0.00 | 0.162 / 0.129 | -0.033 ± 0.006 | 0.060 / 0.063 | 0.000 / 0.000 | 0.061 / 0.060 | -0.002 ± 0.004 | 1.48 / 1.24 | -0.24 ± 0.08 |
| stamper | 1726.2 / 169.9 | 1.76 / 1.26 | -0.49 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.01 | -0.01 ± 0.00 | 0.554 / 0.441 | -0.112 ± 0.006 | 0.403 / 0.328 | 0.398 / 0.361 | 0.106 / 0.084 | -0.022 ± 0.006 | 4.02 / 2.75 | -1.27 ± 0.20 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.04 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.080 ± 0.008 | -0.015 ± 0.009 | +0.015 ± 0.004 |
| careful | -0.10 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.034 ± 0.006 | +0.003 ± 0.003 | -0.002 ± 0.004 |
| stamper | -0.50 ± 0.04 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.113 ± 0.006 | -0.076 ± 0.007 | -0.023 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.066 / 0.035 | 0.60 / 0.76 | 0.026 / 0.009 | 0.00 / 0.00 | 0.59 / 0.50 | 0.891 / 0.711 |
| careful | 0.353 / 0.119 | 0.36 / 0.40 | 0.039 / 0.010 | 0.00 / 0.00 | 0.29 / 0.37 | 0.312 / 0.131 |
| stamper | 0.013 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.206 / 1.725 |
