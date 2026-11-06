# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --dispute-policy truthful --appeal-lie 0.1 --dispute-lie 0.1`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-liars-290-own/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 36114.0 ± 616.0 | 1182.9 ± 850.6 | 4340.2 | 0.805 | 0.195 | 0.000 | 0.001 | 0.001 | 0.339 | 0.574 | 1.70 | 0.95 | 0.30 |
| careful | 34931.1 ± 788.2 | nan ± nan | 4254.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.339 | 0.000 | 1.70 | 0.00 | 0.40 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.001 (5376) / 0.001 (51973) | 0.990 (97) / 0.959 (17494) | 0.004 (2815) / 0.003 (9049) | — / — |
| careful | 0.000 (5190) / 0.000 (51027) | 0.000 (117) / 0.000 (17160) | 0.000 (2625) / 0.000 (8979) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.347 | 0.714 | 0.361 (31988) | 0.309 (5996) | 0.358 (4528) | 0.233 (876) | 0.039 (43416) | 25.000 | 691.800 | 1.209 | 0.038 |
| careful | — | 0.684 | 0.000 (26258) | 0.000 (6098) | 0.000 (4898) | 0.000 (1223) | 0.000 (46621) | 24.800 | 736.000 | 1.222 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.800 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| careful | 39.650 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 23.450 / 39.800 | 1.700 ± 0.263 | +0.000 ± 0.497 | 10.600 | +1.300 ± 1.312 | 3.200 | 0.050 | 5.200 | +0.050 ± 0.854 | 1406.850 | 0.005 | -0.008 ± 0.001 | 219.850 / 30.400 (27.200 / 26.700) | 24802.867 ± 303.382 | +1358.354 ± 535.767 | 36114.0 ± 616.0 | +1182.9 ± 850.6 | 36.842 | +1.438 ± 0.628 | 14.472 ± 0.299 | +0.120 ± 0.446 | 18.294 | 0.002 | 2600.750 | 19.800 | 16.350 | +0.900 ± 0.714 | 911.461 | 255.900 |
| careful | 24.200 / 39.650 | 1.700 ± 0.349 | — | 9.300 | — | 3.200 | 0.045 | 5.150 | — | 1454.650 | 0.013 | — | 224.050 / 31.500 (28.100 / 27.450) | 23444.514 ± 399.404 | — | 34931.1 ± 788.2 | — | 35.404 | — | 14.352 ± 0.339 | — | 18.284 | 0.006 | 2542.650 | 19.650 | 15.450 | — | 685.274 | 239.800 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.922/0.078/0.000 (633); p1 0.800/0.200/0.000 (733); p2 0.742/0.258/0.000 (848); p3 0.738/0.262/0.000 (914); p4 0.826/0.174/0.000 (859); p5 0.882/0.118/0.000 (322); p6 0.851/0.149/0.000 (30)
- **careful**: p0 1.000/0.000/0.000 (602); p1 1.000/0.000/0.000 (687); p2 1.000/0.000/0.000 (835); p3 1.000/0.000/0.000 (924); p4 1.000/0.000/0.000 (935); p5 1.000/0.000/0.000 (260); p6 1.000/0.000/0.000 (11)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2598.7 / 268.8 | 0.34 / 0.21 | -0.14 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.06 | -0.01 ± 0.00 | 0.209 / 0.171 | -0.038 ± 0.004 | 0.073 / 0.082 | 0.001 / 0.000 | 0.066 / 0.066 | -0.000 ± 0.003 | 1.85 / 1.34 | -0.51 ± 0.09 |
| careful | 2551.3 / 259.5 | 0.50 / 0.36 | -0.14 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.254 / 0.218 | -0.036 ± 0.005 | 0.106 / 0.122 | 0.006 / 0.000 | 0.070 / 0.066 | -0.004 ± 0.003 | 2.13 / 1.85 | -0.28 ± 0.07 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.13 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.038 ± 0.004 | +0.009 ± 0.004 | +0.000 ± 0.003 |
| careful | -0.14 ± 0.03 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.038 ± 0.005 | +0.014 ± 0.005 | -0.003 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.334 / 0.017 | 0.39 / 0.39 | 0.143 / 0.453 | 0.00 / 0.00 | 0.30 / 0.32 | 0.333 / 0.404 |
| careful | 0.334 / 0.022 | 0.39 / 0.36 | 0.146 / 0.471 | 0.00 / 0.00 | 0.33 / 0.34 | 0.385 / 0.464 |
