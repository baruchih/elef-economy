# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi-a0 0.20 --pi-a-max 0.20`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/ablation-A1/learned/pa20/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 35410.7 ± 971.5 | 207.0 ± 1113.7 | 4866.9 | 0.981 | 0.009 | 0.010 | 0.005 | 0.004 | 0.414 | 0.039 | 3.10 | 2.50 | 0.50 |
| careful | 35203.7 ± 703.1 | nan ± nan | 4876.6 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.412 | 0.000 | 2.40 | 0.00 | 0.30 |
| stamper | 6821.6 ± 137.4 | -28382.1 ± 665.0 | 1067.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.55 | 184.05 | 1.00 |
| hand | 33287.2 ± 519.4 | -1916.5 ± 704.9 | 5122.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.422 | 0.000 | 8.05 | 0.00 | 0.50 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.005 (5430) [rej. blind 0.000] / 0.004 (51627) [rej. blind 0.000] | 0.014 (5714) [rej. blind 0.005] / 0.021 (25005) [rej. blind 0.000] | 0.122 (5490) [rej. blind 0.121] / 0.073 (4072) [rej. blind 0.071] | — / — |
| careful | 0.000 (5235) / 0.000 (52115) | 0.000 (5650) / 0.000 (25027) | 0.000 (5371) / 0.000 (4134) | — / — |
| stamper | 1.000 (3054) / 1.000 (17863) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (11779) / 0.000 (47422) | 0.000 (7390) / 0.000 (25036) | 0.000 (6665) / 0.000 (4152) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.005 (5430) [rej. blind 0.000] / 0.004 (51627) [rej. blind 0.000] | 0.014 (5714) [rej. blind 0.005] / 0.021 (25005) [rej. blind 0.000] | 0.122 (5490) [rej. blind 0.121] / 0.073 (4072) [rej. blind 0.071] | — / — | 2.5 ± 0.4 | +8 |
| careful | 0.000 (5235) [rej. blind 0.000] / 0.000 (52115) [rej. blind 0.000] | 0.000 (5650) / 0.000 (25027) | 0.000 (5371) / 0.000 (4134) | — / — | 2.6 ± 0.5 | +5 |
| stamper | 1.000 (3054) / 1.000 (17863) | — / 1.000 (440) | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.103 (11779) / 0.157 (47422) | 0.000 (7390) / 0.010 (25036) | 0.000 (6665) / 0.005 (4152) | — / — | 0.8 ± 0.2 | +8941 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.930 | 0.905 | — (0) | — (0) | 0.005 (18921) | — (0) | 0.009 (78417) | 26.200 | 656.700 | 1.191 | 0.095 |
| careful | — | 0.908 | — (0) | — (0) | 0.000 (18247) | 0.000 (249) | 0.000 (79036) | 24.900 | 675.700 | 1.182 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21357) | 77.350 | 178.300 | 2.151 | 2.379 |
| hand | — | 0.999 | — (0) | — (0) | — (0) | 0.000 (1298) | 0.000 (101146) | 36.700 | 338.600 | 1.421 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.700 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.550 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 22.800 / 39.700 | 3.100 ± 0.435 | +0.700 ± 0.585 | 11.500 | +1.350 ± 1.661 | 2.750 | 0.047 | 6.500 | +1.150 ± 1.184 | 1888.600 | 0.029 | +0.005 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 26487.799 ± 486.959 | +885.001 ± 626.080 | 35410.7 ± 971.5 | +207.0 ± 1113.7 | 35.627 | -0.638 ± 0.651 | 16.275 ± 0.693 | +0.718 ± 0.769 | 18.525 | 0.004 | 2581.350 | 19.700 | 16.900 | +1.350 ± 0.812 | 578.368 | 221.450 |
| careful | 24.000 / 39.550 | 2.400 ± 0.294 | — | 10.150 | — | 3.150 | 0.043 | 5.350 | — | 1905.300 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 25602.799 ± 389.383 | — | 35203.7 ± 703.1 | — | 36.265 | — | 15.556 ± 0.334 | — | 17.880 | 0.001 | 2612.750 | 19.550 | 15.550 | — | 650.960 | 198.600 |
| stamper | 3.300 / 40.000 | 14.550 ± 0.860 | +12.150 ± 0.877 | 115.150 | +105.000 ± 2.256 | 0.000 | 1.000 | 57.350 | +52.000 ± 2.215 | 893.050 | 0.194 | +0.170 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 8733.724 ± 169.657 | -16869.074 ± 422.761 | 6821.6 ± 137.4 | -28382.1 ± 665.0 | 26.576 | -9.689 ± 0.553 | 32.718 ± 0.787 | +17.162 ± 0.893 | 22.599 | 0.243 | 704.800 | 20.000 | 36.700 | +21.150 ± 0.921 | 5677.134 | 167.800 |
| hand | 20.900 / 39.900 | 8.050 ± 0.734 | +5.650 ± 0.859 | 65.200 | +55.050 ± 1.519 | 6.800 | 0.056 | 16.800 | +11.450 ± 0.916 | 1900.900 | 0.059 | +0.035 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 31212.911 ± 406.304 | +5610.112 ± 471.482 | 33287.2 ± 519.4 | -1916.5 ± 704.9 | 31.044 | -5.221 ± 0.499 | 19.899 ± 0.318 | +4.342 ± 0.458 | 20.229 | 0.035 | 2313.050 | 19.900 | 19.000 | +3.450 ± 0.515 | 64.368 | 196.150 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.971/0.028/0.001 (594); p1 0.965/0.017/0.018 (811); p2 0.983/0.006/0.011 (976); p3 0.988/0.002/0.010 (1053); p4 0.987/0.002/0.011 (1042); p5 0.994/0.001/0.005 (315); p6 0.986/0.012/0.002 (21); p7 0.996/0.002/0.002 (24); p8 1.000/0.000/0.000 (25); p9 0.993/0.000/0.007 (7)
- **careful**: p0 1.000/0.000/0.000 (596); p1 1.000/0.000/0.000 (796); p2 1.000/0.000/0.000 (1019); p3 1.000/0.000/0.000 (1083); p4 1.000/0.000/0.000 (1070); p5 1.000/0.000/0.000 (313)
- **stamper**: p0 0.000/1.000/0.000 (562); p1 0.000/1.000/0.000 (303); p2 0.000/1.000/0.000 (168); p3 0.000/1.000/0.000 (23); p4 0.000/1.000/0.000 (10); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2581.3 / 271.5 | 0.36 / 0.27 | -0.09 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.14 | +0.00 ± 0.00 | 0.189 / 0.158 | -0.031 ± 0.007 | 0.078 / 0.087 | 0.004 / 0.000 | 0.061 / 0.062 | +0.001 ± 0.003 | 1.75 / 1.52 | -0.23 ± 0.07 |
| careful | 2605.8 / 261.8 | 0.24 / 0.15 | -0.10 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.12 / 0.12 | -0.01 ± 0.01 | 0.178 / 0.149 | -0.029 ± 0.005 | 0.069 / 0.074 | 0.001 / 0.000 | 0.053 / 0.054 | +0.000 ± 0.003 | 1.61 / 1.23 | -0.37 ± 0.08 |
| stamper | 893.1 / 152.7 | 1.03 / 0.77 | -0.26 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.04 / 0.02 | -0.01 ± 0.00 | 0.223 / 0.219 | -0.004 ± 0.009 | 0.126 / 0.130 | 0.210 / 0.000 | 0.093 / 0.076 | -0.017 ± 0.004 | 3.35 / 1.95 | -1.40 ± 0.22 |
| hand | 2371.1 / 589.0 | 1.00 / 1.01 | +0.01 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.17 / 0.17 | +0.00 ± 0.00 | 0.430 / 0.442 | +0.013 ± 0.008 | 0.203 / 0.232 | 0.036 / 0.000 | 0.103 / 0.099 | -0.005 ± 0.004 | 3.04 / 2.79 | -0.25 ± 0.10 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | -0.10 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.01 | -0.037 ± 0.004 | +0.004 ± 0.005 | +0.000 ± 0.003 |
| careful | -0.10 ± 0.02 | +0.00 ± 0.00 | -0.01 ± 0.01 | -0.027 ± 0.004 | +0.006 ± 0.005 | +0.001 ± 0.003 |
| stamper | -0.76 ± 0.03 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.147 ± 0.014 | -0.098 ± 0.011 | -0.023 ± 0.004 |
| hand | -0.11 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.055 ± 0.006 | -0.013 ± 0.003 | -0.006 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.478 / 0.147 | 0.30 / 0.31 | 0.038 / 0.154 | 0.00 / 0.00 | 0.29 / 0.31 | 0.300 / 0.283 |
| careful | 0.474 / 0.143 | 0.34 / 0.36 | 0.041 / 0.158 | 0.00 / 0.00 | 0.32 / 0.35 | 0.305 / 0.315 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.032 | — / 0.00 | — / — | 1.201 / 1.757 |
| hand | 0.514 / 0.208 | 0.11 / 0.14 | 0.032 / 0.087 | 0.00 / 0.00 | 0.10 / 0.10 | 0.335 / 0.238 |
