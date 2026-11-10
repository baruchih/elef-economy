# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-max 0.10`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-pifloor-290-own/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 33949.3 ± 821.3 | -678.3 ± 748.1 | 4057.8 | 0.853 | 0.147 | 0.000 | 0.001 | 0.001 | 0.298 | 0.497 | 9.15 | 7.80 | 0.50 |
| careful | 34627.6 ± 839.5 | nan ± nan | 4376.9 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.354 | 0.000 | 2.80 | 0.00 | 0.30 |
| stamper | 13617.6 ± 304.4 | -21010.0 ± 860.0 | 1925.0 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.011 | 1.000 | 25.75 | 359.50 | 0.75 |
| hand | 30796.8 ± 1463.2 | -3830.8 ± 1386.9 | 3413.4 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.298 | 0.000 | 10.10 | 0.00 | 0.40 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.001 (5135) / 0.001 (51866) | 0.517 (1061) / 0.565 (19673) | 0.162 (942) / 0.073 (2479) | — / — |
| careful | 0.000 (5097) / 0.000 (51495) | 0.000 (1163) / 0.000 (24391) | 0.000 (1465) / 0.000 (3927) | — / — |
| stamper | 1.000 (3417) / 1.000 (34644) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (4313) / 0.000 (43641) | 0.000 (944) / 0.000 (15871) | 0.000 (952) / 0.000 (2548) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.001 (5135) / 0.001 (51866) | 0.517 (1061) / 0.565 (19673) | 0.162 (942) / 0.073 (2479) | — / — | 2.2 ± 0.4 | +5 |
| careful | 0.000 (5097) [rej. blind 0.000] / 0.000 (51495) | 0.000 (1163) / 0.000 (24391) | 0.000 (1465) / 0.000 (3927) | — / — | 2.9 ± 0.3 | +8 |
| stamper | 1.000 (3417) / 1.000 (34644) | — / 1.000 (440) | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.284 (4313) / 0.278 (43641) | 0.000 (944) / 0.016 (15871) | 0.000 (952) / 0.008 (2548) | — / — | 1.1 ± 0.5 | +13654 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.784 | 0.945 | — (0) | — (0) | 0.408 (13195) | 0.330 (528) | 0.096 (67433) | 25.150 | 727.600 | 1.241 | 0.310 |
| careful | — | 0.917 | — (0) | — (0) | 0.000 (14626) | 0.000 (730) | 0.000 (72182) | 24.850 | 709.950 | 1.174 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (38501) | 88.150 | 342.700 | 2.349 | 4.078 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (143) | — (0) | 0.000 (68126) | 39.250 | 722.600 | 1.381 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.750 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 22.700 / 39.850 | 9.150 ± 0.871 | +6.350 ± 0.895 | 11.200 | +1.300 ± 0.737 | 3.150 | 0.068 | 5.300 | +0.150 ± 0.563 | 1917.200 | 0.018 | -0.007 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 24709.649 ± 433.377 | -439.409 ± 545.598 | 33949.3 ± 821.3 | -678.3 ± 748.1 | 35.917 | +0.424 ± 0.442 | 15.799 ± 0.421 | +0.119 ± 0.645 | 18.497 | 0.008 | 2579.750 | 19.850 | 17.150 | +0.000 ± 0.688 | 650.910 | 200.750 |
| careful | 22.550 / 39.700 | 2.800 ± 0.367 | — | 9.900 | — | 3.150 | 0.038 | 5.150 | — | 1881.650 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 25149.058 ± 420.211 | — | 34627.6 ± 839.5 | — | 35.493 | — | 15.680 ± 0.563 | — | 18.444 | 0.008 | 2564.150 | 19.700 | 17.150 | — | 592.071 | 260.250 |
| stamper | 10.800 / 39.950 | 25.750 ± 1.051 | +22.950 ± 0.942 | 126.200 | +116.300 ± 1.475 | 0.000 | 1.000 | 68.200 | +63.050 ± 1.243 | 1726.400 | 0.199 | +0.175 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 18749.521 ± 383.205 | -6399.538 ± 450.734 | 13617.6 ± 304.4 | -21010.0 ± 860.0 | 24.021 | -11.472 ± 0.602 | 30.862 ± 0.514 | +15.182 ± 0.912 | 24.979 | 0.398 | 1059.350 | 19.950 | 29.150 | +12.000 ± 0.743 | 642.531 | 150.650 |
| hand | 25.100 / 39.900 | 10.100 ± 0.804 | +7.300 ± 0.874 | 53.750 | +43.850 ± 1.326 | 2.050 | 0.131 | 19.350 | +14.200 ± 0.869 | 1801.800 | 0.079 | +0.054 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 28884.182 ± 359.342 | +3735.124 ± 547.750 | 30796.8 ± 1463.2 | -3830.8 ± 1386.9 | 28.687 | -6.805 ± 0.569 | 20.371 ± 0.870 | +4.692 ± 1.026 | 22.059 | 0.096 | 1987.950 | 19.900 | 14.800 | -2.350 ± 0.544 | 84.866 | 214.350 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.983/0.017/0.000 (590); p1 0.881/0.119/0.000 (642); p2 0.783/0.217/0.000 (768); p3 0.776/0.224/0.000 (881); p4 0.850/0.150/0.000 (947); p5 0.957/0.043/0.000 (230)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (727); p2 1.000/0.000/0.000 (872); p3 1.000/0.000/0.000 (981); p4 1.000/0.000/0.000 (995); p5 1.000/0.000/0.000 (205)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (447); p2 0.000/1.000/0.000 (354); p3 0.000/1.000/0.000 (344); p4 0.000/1.000/0.000 (217)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2593.3 / 256.8 | 0.35 / 0.25 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.06 / 0.06 | -0.00 ± 0.00 | 0.177 / 0.153 | -0.024 ± 0.004 | 0.068 / 0.074 | 0.008 / 0.000 | 0.064 / 0.060 | -0.003 ± 0.004 | 1.81 / 1.59 | -0.21 ± 0.08 |
| careful | 2574.8 / 254.8 | 0.41 / 0.29 | -0.12 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.10 | -0.00 ± 0.00 | 0.191 / 0.161 | -0.030 ± 0.006 | 0.076 / 0.079 | 0.008 / 0.000 | 0.061 / 0.059 | -0.003 ± 0.003 | 2.04 / 1.50 | -0.54 ± 0.15 |
| stamper | 1732.2 / 170.8 | 1.73 / 1.18 | -0.55 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.02 / 0.01 | -0.01 ± 0.00 | 0.545 / 0.440 | -0.104 ± 0.005 | 0.395 / 0.328 | 0.389 / 0.000 | 0.110 / 0.082 | -0.028 ± 0.006 | 4.18 / 2.73 | -1.45 ± 0.18 |
| hand | 2182.1 / 215.7 | 1.79 / 1.56 | -0.23 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.07 | -0.01 ± 0.00 | 0.516 / 0.440 | -0.075 ± 0.006 | 0.320 / 0.299 | 0.096 / 0.000 | 0.111 / 0.099 | -0.012 ± 0.006 | 3.86 / 3.51 | -0.35 ± 0.17 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.025 ± 0.004 | +0.005 ± 0.004 | -0.003 ± 0.004 |
| careful | -0.12 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.031 ± 0.006 | +0.002 ± 0.004 | -0.002 ± 0.003 |
| stamper | -0.56 ± 0.04 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.108 ± 0.005 | -0.070 ± 0.006 | -0.029 ± 0.006 |
| hand | -0.23 ± 0.03 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.076 ± 0.006 | -0.021 ± 0.008 | -0.012 ± 0.006 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.374 / 0.099 | 0.47 / 0.49 | 0.038 / 0.162 | 0.00 / 0.00 | 0.47 / 0.50 | 0.428 / 0.354 |
| careful | 0.467 / 0.128 | 0.30 / 0.31 | 0.038 / 0.165 | 0.00 / 0.00 | 0.29 / 0.33 | 0.311 / 0.272 |
| stamper | 0.013 / 0.000 | 0.00 / — | 0.000 / 0.050 | — / 0.00 | — / — | 1.215 / 1.762 |
| hand | 0.351 / 0.141 | 0.40 / 0.38 | 0.027 / 0.144 | 0.00 / 0.00 | 0.39 / 0.42 | 0.566 / 0.688 |
