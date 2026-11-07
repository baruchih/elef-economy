# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-stamper-290-own/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 34870.8 ± 779.3 | -505.8 ± 1020.1 | 4269.3 | 0.835 | 0.165 | 0.000 | 0.020 | 0.019 | 0.322 | 0.473 | 13.60 | 20.55 | 0.35 |
| careful | 35376.6 ± 1021.8 | nan ± nan | 4380.3 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.354 | 0.000 | 2.65 | 0.00 | 0.40 |
| stamper | 7015.0 ± 148.4 | -28361.6 ± 1006.5 | 1067.7 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.40 | 187.55 | 1.00 |
| hand | 32930.4 ± 520.4 | -2446.2 ± 925.5 | 4809.1 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.375 | 0.000 | 7.20 | 0.00 | 0.45 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.020 (5880) / 0.019 (52040) | 0.531 (1504) / 0.555 (21938) | 0.015 (1220) / 0.007 (2804) | — / — |
| careful | 0.000 (5215) / 0.000 (51338) | 0.000 (1198) / 0.000 (24402) | 0.000 (1502) / 0.000 (3951) | — / — |
| stamper | 1.000 (3047) / 1.000 (17867) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (11866) / 0.000 (48226) | 0.000 (3106) / 0.000 (25884) | 0.000 (2637) / 0.000 (4462) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.020 (5880) / 0.019 (52040) [rej. blind 0.000] | 0.531 (1504) / 0.555 (21938) | 0.015 (1220) / 0.007 (2804) | — / — | 2.6 ± 0.5 | +3 |
| careful | 0.000 (5215) [rej. blind 0.000] / 0.000 (51338) | 0.000 (1198) / 0.000 (24402) | 0.000 (1502) / 0.000 (3951) | — / — | 2.6 ± 0.4 | +8 |
| stamper | 1.000 (3047) / 1.000 (17867) | — / 1.000 (440) | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.100 (11866) [rej. blind 0.000] / 0.151 (48226) | 0.000 (3106) / 0.010 (25884) | 0.000 (2637) / 0.004 (4462) | — / — | 1.1 ± 0.4 | +8763 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.816 | 0.955 | — (0) | — (0) | 0.449 (11340) | 0.328 (3846) | 0.110 (70200) | 24.850 | 698.200 | 1.257 | 0.827 |
| careful | — | 0.919 | — (0) | — (0) | 0.000 (14115) | 0.000 (862) | 0.000 (72629) | 25.150 | 714.900 | 1.186 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21354) | 74.950 | 176.650 | 2.186 | 2.502 |
| hand | — | 0.999 | — (0) | — (0) | 0.000 (143) | 0.000 (1013) | 0.000 (95025) | 35.700 | 363.700 | 1.342 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| careful | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 22.750 / 39.700 | 13.600 ± 1.352 | +10.950 ± 1.381 | 15.450 | +4.750 ± 0.940 | 3.300 | 0.067 | 5.150 | -0.300 ± 0.567 | 1943.400 | 0.019 | -0.006 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 25448.718 ± 321.953 | +366.955 ± 466.158 | 34870.8 ± 779.3 | -505.8 ± 1020.1 | 36.012 | +0.531 ± 0.490 | 15.987 ± 0.495 | +0.719 ± 0.613 | 18.367 | 0.001 | 2605.600 | 19.700 | 16.950 | +0.650 ± 0.499 | 640.419 | 208.450 |
| careful | 23.400 / 39.700 | 2.650 ± 0.412 | — | 10.700 | — | 3.500 | 0.046 | 5.450 | — | 1882.600 | 0.026 | — | 0.000 / 0.000 (0.000 / 0.000) | 25081.763 ± 393.915 | — | 35376.6 ± 1021.8 | — | 35.481 | — | 15.269 ± 0.468 | — | 18.472 | 0.010 | 2551.650 | 19.700 | 16.300 | — | 610.512 | 256.100 |
| stamper | 3.600 / 40.000 | 14.400 ± 1.094 | +11.750 ± 1.135 | 113.550 | +102.850 ± 1.700 | 0.000 | 1.000 | 54.950 | +49.500 ± 1.816 | 893.400 | 0.197 | +0.171 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 9097.061 ± 193.375 | -15984.703 ± 437.547 | 7015.0 ± 148.4 | -28361.6 ± 1006.5 | 26.613 | -8.868 ± 0.606 | 32.549 ± 0.650 | +17.281 ± 0.917 | 22.826 | 0.209 | 736.550 | 20.000 | 36.400 | +20.100 ± 1.061 | 5708.059 | 118.200 |
| hand | 20.650 / 39.850 | 7.200 ± 0.735 | +4.550 ± 0.838 | 62.400 | +51.700 ± 1.455 | 6.050 | 0.039 | 15.850 | +10.400 ± 0.682 | 1925.900 | 0.054 | +0.029 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 30042.259 ± 276.423 | +4960.496 ± 418.283 | 32930.4 ± 520.4 | -2446.2 ± 925.5 | 31.698 | -3.783 ± 0.454 | 19.417 ± 0.270 | +4.149 ± 0.480 | 19.674 | 0.027 | 2365.800 | 19.850 | 19.200 | +2.900 ± 0.464 | 59.930 | 165.350 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.947/0.053/0.000 (603); p1 0.888/0.112/0.000 (652); p2 0.810/0.190/0.000 (795); p3 0.725/0.275/0.000 (801); p4 0.806/0.194/0.000 (751); p5 0.862/0.138/0.000 (486); p6 0.921/0.079/0.000 (168); p7 0.865/0.135/0.000 (12)
- **careful**: p0 1.000/0.000/0.000 (597); p1 1.000/0.000/0.000 (719); p2 1.000/0.000/0.000 (854); p3 1.000/0.000/0.000 (954); p4 1.000/0.000/0.000 (961); p5 1.000/0.000/0.000 (294); p6 1.000/0.000/0.000 (1)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (306); p2 0.000/1.000/0.000 (173); p3 0.000/1.000/0.000 (24); p4 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2602.0 / 294.0 | 0.27 / 0.16 | -0.12 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.08 | +0.01 ± 0.00 | 0.176 / 0.137 | -0.039 ± 0.006 | 0.072 / 0.073 | 0.001 / 0.000 | 0.062 / 0.059 | -0.002 ± 0.003 | 1.68 / 1.31 | -0.37 ± 0.10 |
| careful | 2566.9 / 260.8 | 0.43 / 0.30 | -0.13 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.11 / 0.11 | -0.00 ± 0.00 | 0.196 / 0.164 | -0.032 ± 0.006 | 0.082 / 0.085 | 0.010 / 0.000 | 0.058 / 0.060 | +0.002 ± 0.003 | 2.07 / 1.63 | -0.45 ± 0.16 |
| stamper | 893.4 / 152.3 | 1.02 / 0.71 | -0.31 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.02 | -0.01 ± 0.00 | 0.221 / 0.213 | -0.008 ± 0.010 | 0.125 / 0.131 | 0.175 / 0.000 | 0.095 / 0.076 | -0.019 ± 0.005 | 3.50 / 2.11 | -1.39 ± 0.16 |
| hand | 2411.3 / 593.3 | 0.86 / 0.91 | +0.05 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.15 / 0.15 | -0.01 ± 0.00 | 0.403 / 0.411 | +0.009 ± 0.004 | 0.176 / 0.199 | 0.027 / 0.000 | 0.097 / 0.093 | -0.004 ± 0.003 | 2.69 / 2.71 | +0.02 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.09 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.025 ± 0.005 | +0.006 ± 0.003 | -0.001 ± 0.003 |
| careful | -0.13 ± 0.02 | +0.00 ± 0.00 | -0.00 ± 0.00 | -0.032 ± 0.006 | +0.002 ± 0.003 | +0.002 ± 0.003 |
| stamper | -0.83 ± 0.04 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.163 ± 0.014 | -0.105 ± 0.008 | -0.028 ± 0.006 |
| hand | -0.08 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.052 ± 0.004 | -0.009 ± 0.003 | -0.006 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.416 / 0.139 | 0.43 / 0.43 | 0.038 / 0.152 | 0.00 / 0.00 | 0.42 / 0.42 | 0.389 / 0.307 |
| careful | 0.468 / 0.130 | 0.31 / 0.33 | 0.039 / 0.164 | 0.00 / 0.00 | 0.29 / 0.31 | 0.313 / 0.268 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.028 | — / 0.00 | — / — | 1.203 / 1.746 |
| hand | 0.525 / 0.214 | 0.11 / 0.14 | 0.035 / 0.085 | 0.00 / 0.00 | 0.09 / 0.11 | 0.321 / 0.216 |
