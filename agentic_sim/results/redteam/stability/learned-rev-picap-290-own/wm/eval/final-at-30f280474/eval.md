# Evaluation — cell `--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --pi0 0.40`, seeds 21-40, hide ``, model `/Users/baruchi-admin/projects/elef-economy/agentic_sim/results/redteam/stability/learned-rev-picap-290-own/wm/models/wm-online-10.pt` (value mc, horizon 16)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the non-initial seats — the audits and the panels, 2.7.0's plant-blind seats, which a plant reaches under 2.8.0 — are read apart: their share of the review decisions and the stamp rate on them, and below by seat kind. A `stamp rate` here is the rate of verdicts given without inspecting, approve blind or reject blind (the label corrected November 6, 2026; the two signs are the `approve blind` / `reject blind` columns on the whole decision set, and the reject-blind part by seat is in the seat table).

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant blind-verdict rate (initial) | real blind-verdict rate (initial) | non-initial share | non-initial blind-verdict rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 29594.8 ± 638.6 | -232.4 ± 795.5 | 5745.5 | 0.942 | 0.058 | 0.000 | 0.004 | 0.003 | 0.397 | 0.141 | 8.95 | 5.10 | 0.50 |
| careful | 29827.2 ± 564.0 | nan ± nan | 5661.4 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.394 | 0.000 | 4.45 | 0.00 | 0.50 |
| stamper | 2866.6 ± 84.1 | -26960.6 ± 580.6 | 485.8 | 0.000 | 1.000 | 0.000 | 1.000 | 1.000 | 0.026 | 1.000 | 6.15 | 71.20 | 1.00 |
| hand | 31090.3 ± 521.7 | 1263.0 ± 575.7 | 5542.2 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.414 | 0.000 | 3.95 | 0.00 | 0.55 |

The rate of verdicts given without inspecting by seat kind (2.8.0 §5) — `stamped` in the readers counts a blind verdict of either sign, approve blind or reject blind; the reject-blind part is shown in brackets where it is not zero (the label corrected November 6, 2026) — plant / real, with the decisions pooled over the seeds in parentheses; under 2.7.0 a plant reached the initial review alone, under 2.8.0 it reaches every seat.

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real |
|---|---|---|---|---|
| greedy | 0.004 (19375) / 0.003 (49885) | 0.162 (5410) / 0.178 (30428) | 0.026 (4711) [rej. blind 0.003] / 0.007 (5101) [rej. blind 0.004] | — / — |
| careful | 0.000 (19185) / 0.000 (49430) | 0.000 (4675) / 0.000 (30455) | 0.000 (4059) / 0.000 (5423) | — / — |
| stamper | 1.000 (2615) / 1.000 (6847) | — / 1.000 (253) | — / — | — / — |
| hand | 0.000 (18107) / 0.000 (46810) | 0.000 (4956) / 0.000 (31503) | 0.000 (4030) / 0.000 (5439) | — / — |

The same rates measured from the engine's reviews rather than from the actions (November 7, 2026): a review that spent care inspected, one that spent none gave a blind verdict of the sign it gave — the reading the record's exporter uses for the 60/40 mix (`hand`, action 3, which the action counters cannot see: they read 0 for it). For a learned policy the two readings agree except where a careful review could not afford a cent of its care — `underfunded careful reviews` is the run's count over every careful review (mean ± SE over the seeds), an upper bound on the blind readings that were a careful review paying nothing; `≠ actions` is the blind verdicts counted here less the actions' count, pooled over the seeds and the seats (for `hand` it is the whole count, the actions reading 0).

| policy | initial plant / real | audit plant / real | panel plant / real | resumed plant / real | underfunded careful reviews | ≠ actions |
|---|---|---|---|---|---|---|
| greedy | 0.004 (19375) / 0.003 (49885) | 0.162 (5410) / 0.178 (30428) | 0.026 (4711) [rej. blind 0.003] / 0.007 (5101) [rej. blind 0.004] | — / — | 3.4 ± 0.4 | +6 |
| careful | 0.000 (19185) [rej. blind 0.000] / 0.000 (49430) [rej. blind 0.000] | 0.000 (4675) / 0.000 (30455) | 0.000 (4059) / 0.000 (5423) | — / — | 4.3 ± 0.5 | +12 |
| stamper | 1.000 (2615) / 1.000 (6847) | — / 1.000 (253) | — / — | — / — | 0.0 ± 0.0 | +0 |
| hand | 0.065 (18107) [rej. blind 0.000] / 0.065 (46810) | 0.000 (4956) / 0.004 (31503) | 0.000 (4030) / 0.002 (5439) | — / — | 3.8 ± 0.4 | +4367 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 0.908 | 0.852 | — (0) | — (0) | 0.036 (33326) | 0.103 (2566) | 0.066 (79018) | 6.300 | 199.350 | 1.253 | 0.810 |
| careful | — | 0.859 | — (0) | — (0) | 0.000 (32333) | 0.000 (1537) | 0.000 (79357) | 5.100 | 201.750 | 1.098 | 0.000 |
| stamper | 1.000 | — | — (0) | — (0) | — (0) | — (0) | 1.000 (9715) | 39.800 | 73.300 | 1.884 | 1.789 |
| hand | — | 0.979 | — (0) | — (0) | 0.000 (3644) | 0.000 (7663) | 0.000 (99538) | 15.600 | 224.350 | 1.116 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| greedy | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| careful | 39.850 | 0.000 | 0.000 | 0.000 | 0.000 | 0.500 | 0.000 |
| stamper | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 1.000 | 0.000 |
| hand | 39.950 | 0.000 | 0.000 | 0.000 | 0.000 | 0.550 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 19.600 / 39.950 | 8.950 ± 0.835 | +4.500 ± 0.694 | 37.900 | +0.500 ± 1.825 | 13.550 | 0.058 | 6.300 | +1.200 ± 0.588 | 1660.800 | 0.022 | -0.002 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 33742.464 ± 469.210 | +614.442 ± 486.389 | 29594.8 ± 638.6 | -232.4 ± 795.5 | 32.706 | -0.093 ± 0.426 | 24.739 ± 0.492 | +0.572 ± 0.582 | 21.691 | 0.002 | 2506.500 | 19.950 | 20.350 | +0.050 ± 0.303 | 74.512 | 101.250 |
| careful | 19.550 / 39.850 | 4.450 ± 0.591 | — | 37.400 | — | 12.900 | 0.055 | 5.100 | — | 1658.700 | 0.024 | — | 0.000 / 0.000 (0.000 / 0.000) | 33128.022 ± 486.531 | — | 29827.2 ± 564.0 | — | 32.799 | — | 24.167 ± 0.431 | — | 21.255 | 0.003 | 2486.750 | 19.850 | 20.300 | — | 126.087 | 109.200 |
| stamper | 7.850 / 39.950 | 6.150 ± 0.549 | +1.700 ± 0.788 | 98.950 | +61.550 ± 1.350 | 0.000 | — | 39.800 | +34.700 ± 0.543 | 342.550 | 0.193 | +0.170 ± 0.005 | 0.000 / 0.000 (0.000 / 0.000) | 1911.095 ± 117.846 | -31216.928 ± 481.161 | 2866.6 ± 84.1 | -26960.6 ± 580.6 | 29.067 | -3.731 ± 0.567 | 28.018 ± 0.978 | +3.851 ± 1.068 | 17.708 | 0.374 | 239.150 | 19.950 | 32.100 | +11.800 ± 0.713 | 8584.835 | 96.250 |
| hand | 19.350 / 39.950 | 3.950 ± 0.420 | -0.500 ± 0.734 | 74.800 | +37.400 ± 1.510 | 10.750 | 0.053 | 15.600 | +10.500 ± 0.484 | 1799.550 | 0.039 | +0.015 ± 0.001 | 0.000 / 0.000 (0.000 / 0.000) | 33231.166 ± 300.258 | +103.144 ± 484.565 | 31090.3 ± 521.7 | +1263.0 ± 575.7 | 30.790 | -2.009 ± 0.471 | 23.068 ± 0.414 | -1.099 ± 0.476 | 20.700 | 0.024 | 2317.600 | 19.950 | 20.600 | +0.300 ± 0.356 | 66.368 | 158.200 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **greedy**: p0 0.917/0.083/0.000 (195); p1 0.836/0.162/0.002 (258); p2 0.808/0.191/0.001 (296); p3 0.845/0.155/0.000 (300); p4 0.878/0.122/0.001 (298); p5 0.903/0.097/0.000 (302); p6 0.896/0.103/0.001 (298); p7 0.917/0.083/0.000 (300); p8 0.937/0.063/0.000 (303); p9 0.951/0.049/0.000 (305); p10 0.981/0.018/0.000 (305); p11 0.992/0.008/0.000 (310); p12 0.991/0.009/0.000 (314); p13 0.989/0.011/0.000 (310); p14 0.995/0.005/0.000 (313); p15 1.000/0.000/0.000 (312); p16 0.999/0.000/0.000 (309); p17 0.997/0.003/0.000 (309); p18 1.000/0.000/0.000 (277); p19 1.000/0.000/0.000 (118); p20 1.000/0.000/0.000 (15)
- **careful**: p0 1.000/0.000/0.000 (198); p1 1.000/0.000/0.000 (255); p2 1.000/0.000/0.000 (299); p3 1.000/0.000/0.000 (307); p4 1.000/0.000/0.000 (309); p5 1.000/0.000/0.000 (304); p6 1.000/0.000/0.000 (307); p7 1.000/0.000/0.000 (299); p8 1.000/0.000/0.000 (300); p9 1.000/0.000/0.000 (306); p10 1.000/0.000/0.000 (306); p11 1.000/0.000/0.000 (302); p12 1.000/0.000/0.000 (299); p13 1.000/0.000/0.000 (310); p14 1.000/0.000/0.000 (302); p15 1.000/0.000/0.000 (304); p16 1.000/0.000/0.000 (313); p17 1.000/0.000/0.000 (308); p18 1.000/0.000/0.000 (228); p19 1.000/0.000/0.000 (92); p20 1.000/0.000/0.000 (13)
- **stamper**: p0 0.000/1.000/0.000 (194); p1 0.000/1.000/0.000 (179); p2 0.000/1.000/0.000 (111); p3 0.000/1.000/0.000 (1); p4 0.000/1.000/0.000 (0)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0); p14 —/—/— (0); p15 —/—/— (0); p16 —/—/— (0); p17 —/—/— (0); p18 —/—/— (0); p19 —/—/— (0)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling's raise was refused at least once (a real root's by the requester's wallet; a plant's drawn at the trailing real roots' rate and held at their delay — the conformance correction after run 35; before it never a plant's, §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| greedy | 2494.2 / 968.8 | 0.50 / 0.52 | +0.02 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.18 / 0.16 | -0.02 ± 0.00 | 0.279 / 0.254 | -0.025 ± 0.002 | 0.145 / 0.138 | 0.002 / 0.000 | 0.093 / 0.095 | +0.002 ± 0.002 | 2.29 / 2.31 | +0.02 ± 0.06 |
| careful | 2471.5 / 959.2 | 0.56 / 0.58 | +0.02 ± 0.01 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.18 | -0.02 ± 0.00 | 0.309 / 0.281 | -0.028 ± 0.003 | 0.159 / 0.151 | 0.002 / 0.000 | 0.098 / 0.099 | +0.001 ± 0.002 | 2.38 / 2.39 | +0.01 ± 0.04 |
| stamper | 342.4 / 130.8 | 0.85 / 0.81 | -0.03 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.08 / 0.04 | -0.04 ± 0.00 | 0.018 / 0.006 | -0.011 ± 0.006 | 0.011 / 0.004 | 0.303 / 0.000 | 0.052 / 0.051 | -0.001 ± 0.005 | 1.81 / 1.64 | -0.16 ± 0.14 |
| hand | 2340.5 / 905.4 | 1.20 / 1.22 | +0.02 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.20 / 0.17 | -0.03 ± 0.00 | 0.513 / 0.483 | -0.029 ± 0.004 | 0.251 / 0.243 | 0.024 / 0.000 | 0.130 / 0.132 | +0.002 ± 0.003 | 3.01 / 3.05 | +0.04 ± 0.03 |

The same differences **period-matched** (§52): the real roots' stage means by period, reweighted by the plants' count in each period, so a plant rate that rises with the dial while the market drifts is not read as a difference in the plant's path. Plant − real, paired by seed.

| policy | posted → awarded | awarded → submitted | submitted → seated | raised share | raise refused (wallet) | seen share |
|---|---|---|---|---|---|---|
| greedy | +0.02 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.024 ± 0.002 | -0.006 ± 0.002 | +0.002 ± 0.002 |
| careful | +0.02 ± 0.01 | +0.00 ± 0.00 | -0.02 ± 0.00 | -0.026 ± 0.003 | -0.007 ± 0.002 | +0.001 ± 0.002 |
| stamper | -0.03 ± 0.02 | +0.00 ± 0.00 | -0.04 ± 0.00 | -0.011 ± 0.006 | -0.006 ± 0.004 | -0.001 ± 0.005 |
| hand | +0.03 ± 0.02 | +0.00 ± 0.00 | -0.03 ± 0.00 | -0.029 ± 0.004 | -0.008 ± 0.003 | +0.002 ± 0.003 |

The stages after the first verdict (2.8.0 §2.3), real / plant: the share of roots whose pending F was audited and the audit seat's wait from the roll; the share with an appeal or a dispute filed and the filing's delay from the verdict; the first panel seat's wait from the filing; the seats the state took per root (a real root's by a troop, a plant's by the orchestrator's own verdict).

| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats |
|---|---|---|---|---|---|---|
| greedy | 0.603 / 0.206 | 0.08 / 0.09 | 0.038 / 0.082 | 0.00 / 0.00 | 0.08 / 0.07 | 0.072 / 0.042 |
| careful | 0.608 / 0.207 | 0.08 / 0.08 | 0.039 / 0.079 | 0.00 / 0.00 | 0.07 / 0.09 | 0.072 / 0.045 |
| stamper | 0.037 / 0.000 | 0.00 / — | 0.000 / 0.014 | — / 0.00 | — / — | 1.187 / 1.748 |
| hand | 0.659 / 0.233 | 0.10 / 0.12 | 0.036 / 0.076 | 0.00 / 0.00 | 0.07 / 0.11 | 0.120 / 0.125 |
