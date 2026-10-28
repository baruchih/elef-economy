# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --planted-lie off`, seeds 21-40, hide ``, model `results/redteam/stability/learned-rev-careful-A-290/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | non-initial share | non-initial stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 27513.8 ± 603.3 | -8141.8 ± 845.0 | 3406.3 | 0.715 | 0.285 | 0.000 | 0.175 | 0.197 | 0.159 | 0.778 | 28.35 | 106.60 | 0.05 |
| careful | 35655.6 ± 875.6 | nan ± nan | 4083.8 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.294 | 0.000 | 6.20 | 0.00 | 0.35 |
| stamper | 6948.3 ± 161.7 | -28707.4 ± 911.8 | 1062.7 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.021 | 1.000 | 14.50 | 181.25 | 1.00 |
| hand | 32126.9 ± 601.9 | -3528.7 ± 754.3 | 4458.3 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.311 | 0.000 | 12.25 | 0.00 | 0.45 |

The stamp rate by seat kind (2.8.0 §5), plant / real, with the decisions pooled over the seeds in parentheses — under 2.7.0 a plant reached the initial review alone; under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.175 (12566) / 0.197 (44742) | 0.912 (1431) / 0.871 (7906) | 0.130 (324) / 0.161 (1158) | — / — |
| careful | 0.000 (5298) / 0.000 (52363) | 0.000 (986) / 0.000 (18823) | 0.000 (503) / 0.000 (3704) | — / — |
| stamper | 1.000 (3022) / 1.000 (17791) | — / 1.000 (440) | — / — | — / — |
| hand | 0.000 (12283) / 0.000 (49127) | 0.000 (2646) / 0.000 (19963) | 0.000 (1142) / 0.000 (4005) | — / — |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.893 | 0.941 | 0.571 (198) | 0.724 (257) | 0.651 (441) | 0.389 (21128) | 0.231 (46103) | 43.600 | 259.850 | 1.651 | 2.445 |
| careful | — | 0.679 | 0.000 (25847) | 0.000 (5628) | 0.000 (4397) | 0.000 (1163) | 0.000 (44642) | 24.900 | 717.400 | 1.164 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (21253) | 74.200 | 177.300 | 2.196 | 2.443 |
| hand | — | 0.809 | 0.000 (32) | 0.000 (11708) | 0.000 (18035) | 0.000 (14932) | 0.000 (44459) | 35.100 | 348.150 | 1.383 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.050 | 0.000 |
| careful | 39.750 | 0.000 | 0.000 | 0.000 | 0.000 | 0.350 | 0.000 |
| stamper | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.450 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 17.200 / 39.850 | 28.350 ± 1.164 | +22.150 ± 1.227 | 100.900 | +92.150 ± 4.154 | 6.350 | 0.178 | 23.750 | +18.600 ± 0.825 | 1713.800 | 0.053 | +0.028 ± 0.003 | 0.000 / 0.000 (0.000 / 0.000) | 29551.807 ± 456.842 | +6074.771 ± 469.690 | 27513.8 ± 603.3 | -8141.8 ± 845.0 | 29.350 | -8.103 ± 0.417 | 23.225 ± 0.428 | +9.224 ± 0.506 | 21.522 | 0.049 | 2136.650 | 19.850 | 22.650 | +6.350 ± 0.425 | 70.951 | 148.800 |
| careful | 23.450 / 39.750 | 6.200 ± 0.601 | — | 8.750 | — | 3.650 | 0.058 | 5.150 | — | 1607.500 | 0.025 | — | 0.000 / 0.000 (0.000 / 0.000) | 23477.036 ± 308.524 | — | 35655.6 ± 875.6 | — | 37.453 | — | 14.001 ± 0.333 | — | 17.610 | 0.001 | 2622.400 | 19.750 | 16.300 | — | 952.910 | 207.250 |
| stamper | 3.550 / 40.000 | 14.500 ± 0.734 | +8.300 ± 1.024 | 113.050 | +104.300 ± 2.129 | 0.000 | 1.000 | 54.200 | +49.050 ± 2.195 | 889.500 | 0.190 | +0.165 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 9098.454 ± 180.421 | -14378.582 ± 341.474 | 6948.3 ± 161.7 | -28707.4 ± 911.8 | 26.554 | -10.899 ± 0.403 | 32.917 ± 0.747 | +18.916 ± 0.863 | 22.723 | 0.223 | 720.950 | 20.000 | 36.450 | +20.150 ± 0.952 | 5679.194 | 120.700 |
| hand | 20.100 / 39.900 | 12.250 ± 0.984 | +6.050 ± 1.299 | 64.750 | +56.000 ± 1.903 | 6.400 | 0.042 | 15.200 | +10.050 ± 0.766 | 1646.850 | 0.063 | +0.037 ± 0.002 | 0.000 / 0.000 (0.000 / 0.000) | 29459.043 ± 399.511 | +5982.007 ± 358.873 | 32126.9 ± 601.9 | -3528.7 ± 754.3 | 32.367 | -5.086 ± 0.424 | 19.806 ± 0.505 | +5.805 ± 0.486 | 19.797 | 0.025 | 2407.000 | 19.900 | 19.800 | +3.500 ± 0.473 | 175.040 | 196.350 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.869/0.131/0.000 (590); p1 0.497/0.502/0.001 (403); p2 0.640/0.360/0.000 (259); p3 0.726/0.274/0.000 (220); p4 0.719/0.281/0.000 (220); p5 0.732/0.268/0.000 (226); p6 0.717/0.283/0.000 (220); p7 0.737/0.263/0.000 (224); p8 0.714/0.286/0.000 (231); p9 0.763/0.237/0.000 (226); p10 0.709/0.291/0.000 (227); p11 0.711/0.289/0.000 (190); p12 0.691/0.309/0.000 (127); p13 0.649/0.351/0.000 (36); p14 0.700/0.300/0.000 (6)
- **careful**: p0 1.000/0.000/0.000 (596); p1 1.000/0.000/0.000 (715); p2 1.000/0.000/0.000 (866); p3 1.000/0.000/0.000 (898); p4 1.000/0.000/0.000 (770); p5 1.000/0.000/0.000 (230); p6 1.000/0.000/0.000 (10)
- **stamper**: p0 0.000/1.000/0.000 (561); p1 0.000/1.000/0.000 (305); p2 0.000/1.000/0.000 (170); p3 0.000/1.000/0.000 (19); p4 0.000/1.000/0.000 (5); p5 0.000/1.000/0.000 (2)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2237.1 / 628.3 | 1.62 / 2.16 | +0.54 ± 0.03 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.05 / 0.05 | -0.01 ± 0.00 | 0.541 / 0.639 | +0.098 ± 0.006 | 0.323 / 0.399 | 0.049 / 0.000 | 0.199 / 0.254 | +0.055 ± 0.005 | 3.36 / 3.72 | +0.36 ± 0.03 |
| careful | 2618.2 / 264.9 | 0.26 / 0.15 | -0.11 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.170 / 0.129 | -0.040 ± 0.004 | 0.064 / 0.069 | 0.001 / 0.000 | 0.063 / 0.062 | -0.001 ± 0.003 | 1.56 / 1.27 | -0.29 ± 0.06 |
| stamper | 889.5 / 151.1 | 1.08 / 0.71 | -0.37 ± 0.05 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.03 / 0.03 | -0.01 ± 0.00 | 0.231 / 0.207 | -0.024 ± 0.009 | 0.136 / 0.124 | 0.189 / 0.000 | 0.097 / 0.076 | -0.022 ± 0.005 | 3.40 / 2.19 | -1.21 ± 0.17 |
| hand | 2456.3 / 614.1 | 0.71 / 0.69 | -0.02 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.14 / 0.14 | +0.00 ± 0.00 | 0.291 / 0.297 | +0.006 ± 0.005 | 0.128 / 0.149 | 0.025 / 0.000 | 0.096 / 0.091 | -0.004 ± 0.004 | 2.56 / 2.32 | -0.24 ± 0.06 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.09 ± 0.02 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.042 ± 0.004 | -0.021 ± 0.004 | +0.015 ± 0.005 |
| careful | -0.10 ± 0.02 | +0.00 ± 0.00 | +0.00 ± 0.00 | -0.039 ± 0.005 | +0.005 ± 0.003 | -0.001 ± 0.003 |
| stamper | -0.89 ± 0.07 | +0.00 ± 0.00 | -0.01 ± 0.00 | -0.177 ± 0.014 | -0.123 ± 0.012 | -0.032 ± 0.006 |
| hand | -0.12 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.046 ± 0.004 | -0.010 ± 0.003 | -0.004 ± 0.004 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.175 / 0.102 | 0.51 / 0.54 | 0.031 / 0.010 | 0.00 / 0.00 | 0.52 / 0.53 | 0.690 / 0.375 |
| careful | 0.357 / 0.117 | 0.36 / 0.39 | 0.040 / 0.014 | 0.00 / 0.00 | 0.28 / 0.22 | 0.306 / 0.137 |
| stamper | 0.025 / 0.000 | 0.00 / — | 0.000 / 0.000 | — / — | — / — | 1.196 / 1.721 |
| hand | 0.401 / 0.181 | 0.11 / 0.13 | 0.034 / 0.010 | 0.00 / 0.00 | 0.08 / 0.06 | 0.322 / 0.177 |
