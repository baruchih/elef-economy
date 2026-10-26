# Evaluation — cell `--entry-pool 20 --stampers 0.6 --dispute-policy truthful --learner-pop all --learner-role reviewer --learner-exit rule`, seeds 21-30, hide ``, model `None` (value off, horizon 8)

The plant and real stamp rates are read on the initial reviews alone (the ruling after run 26); the plant-blind seats — a revised submission or a panel, where no plant is received — are read apart: their share of the review decisions and the stamp rate on them.

| policy | lifetime real wealth | paired − careful | decisions | care share | approve blind | reject blind | plant stamp rate (initial) | real stamp rate (initial) | blind-seat share | blind-seat stamp rate | run false approvals | learner's | departed |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 31747.4 ± 1538.1 | -1168.6 ± 2162.8 | 4341.6 | 0.530 | 0.456 | 0.015 | 0.275 | 0.302 | 0.288 | 0.904 | 46.40 | 267.20 | 0.10 |
| hand | 31365.9 ± 723.0 | -1550.1 ± 1262.4 | 4203.6 | 0.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.276 | 0.000 | 3.30 | 0.00 | 0.40 |
| careful | 32916.0 ± 1207.6 | nan ± nan | 4085.7 | 1.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.280 | 0.000 | 0.30 | 0.00 | 0.30 |

Q1's readings — the applied odds at the policy's blind approvals (its stamps) and at its other decisions, its stamp rate by odds band (decisions in the band pooled over the seeds), the slot's suspensions, the ticks between its admissions, the false approvals it passed per suspension:

| policy | odds at stamps | odds at cares | stamp rate 0.0-0.3 | stamp rate 0.3-0.5 | stamp rate 0.5-0.7 | stamp rate 0.7-1.0 | stamp rate pinned | suspensions | admissions seen | ticks between admissions | false approvals / suspension |
|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 0.892 | 0.958 | 0.879 (519) | 0.747 (561) | 0.706 (669) | 0.634 (10780) | 0.377 (30887) | 38.500 | 347.800 | 1.326 | 6.940 |
| hand | — | 0.808 | 0.000 (7) | 0.000 (6145) | 0.000 (7544) | 0.000 (7468) | 0.000 (20872) | 36.500 | 350.400 | 1.389 | 0.000 |
| careful | — | 0.700 | 0.000 (11135) | 0.000 (3600) | 0.000 (2351) | 0.000 (771) | 0.000 (23000) | 24.700 | 702.300 | 1.122 | 0.000 |

Re-arrival (allowed after run 22; the driver's `--learner-rearrive on`): identities per episode, returns, leaves chosen at a boundary and refused, the floats minted per episode in real terms (the loop's bill), the share of episodes whose last identity had departed:

| policy | identities | returns | leaves chosen | leaves refused | floats minted (real) | departed at the end | boundary decisions |
|---|---|---|---|---|---|---|---|
| direct | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.100 | 0.000 |
| hand | 40.000 | 0.000 | 0.000 | 0.000 | 0.000 | 0.400 | 0.000 |
| careful | 39.900 | 0.000 | 0.000 | 0.000 | 0.000 | 0.300 | 0.000 |

The reviewers in self-play — every member a learner slot sharing one policy (`--learner-pop all --learner-role reviewer`); the references on the same slots: `careful` (all-careful), `stamper` (all-stamper), `hand` (each slot's disposition by hand — run 24's 60/40). Honesty first: the run's standing false approvals, the bad plants approved and the good rejected (the plant record), the dial's F̂, the suspensions, the audit layer's overturn rate (settled roots with an audit seat whose initial approval it overturned, over those with a seat); then the members' nominal surplus and the customers' tasks per 1,000 nominal credits, P_t and the members' price, the state's share, arrivals and departures. Paired columns are against `careful`.

| policy | slots (alive / total) | false approvals (run) | paired | bad plants approved | paired | good plants rejected | F̂ | suspensions | paired | audits held | overturn rate | paired | disputes filed / won (false approvals disputed / overturned) | nominal surplus | paired | real (the slots' lifetime) | paired | tasks per 1,000 (customers) | paired | P_t close | paired | members' price | state share | awarded | arrivals | departures | paired | requesters' wallet | idle for bond |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 18.800 / 39.900 | 46.400 ± 3.569 | +46.100 ± 3.576 | 152.600 | +142.500 ± 4.559 | 9.900 | 0.309 | 18.600 | +13.800 ± 2.210 | 1773.100 | 0.007 | -0.006 ± 0.001 | 152.500 / 109.900 (152.500 / 109.900) | 31431.219 ± 742.244 | +9437.292 ± 679.065 | 31747.4 ± 1538.1 | -1168.6 ± 2162.8 | 31.512 | -6.546 ± 0.281 | 21.536 ± 0.800 | +7.191 ± 1.095 | 20.502 | 0.010 | 2399.600 | 19.900 | 21.100 | +4.100 ± 1.048 | 58.838 | 130.400 |
| hand | 19.700 / 40.000 | 3.300 ± 0.396 | +3.000 ± 0.394 | 66.000 | +55.900 ± 2.137 | 7.600 | 0.058 | 16.500 | +11.700 ± 1.184 | 1544.300 | 0.012 | -0.001 ± 0.001 | 91.000 / 88.000 (91.000 / 88.000) | 29188.431 ± 482.990 | +7194.504 ± 410.465 | 31365.9 ± 723.0 | -1550.1 ± 1262.4 | 32.159 | -5.898 ± 0.467 | 20.006 ± 0.653 | +5.661 ± 0.762 | 19.968 | 0.028 | 2378.900 | 20.000 | 20.300 | +3.300 ± 0.870 | 140.973 | 259.900 |
| careful | 22.900 / 39.900 | 0.300 ± 0.153 | — | 10.100 | — | 3.500 | 0.038 | 4.800 | — | 1627.800 | 0.014 | — | 27.100 / 26.500 (27.100 / 26.500) | 21993.927 ± 509.522 | — | 32916.0 ± 1207.6 | — | 38.057 | — | 14.345 ± 0.478 | — | 17.160 | 0.001 | 2671.500 | 19.900 | 17.000 | — | 963.400 | 146.400 |

The action mix by period (care / approve blind / reject blind, pooled over the seeds; the decisions a period, mean over the seeds):

- **direct**: p0 0.841/0.158/0.000 (594); p1 0.482/0.498/0.020 (564); p2 0.539/0.444/0.016 (354); p3 0.561/0.429/0.010 (286); p4 0.472/0.510/0.019 (290); p5 0.447/0.525/0.028 (282); p6 0.452/0.535/0.013 (277); p7 0.427/0.558/0.015 (272); p8 0.442/0.542/0.016 (271); p9 0.421/0.562/0.017 (270); p10 0.431/0.543/0.027 (256); p11 0.492/0.494/0.014 (205); p12 0.511/0.480/0.009 (176); p13 0.552/0.439/0.009 (149); p14 0.515/0.471/0.014 (78); p15 0.686/0.314/0.000 (15)
- **hand**: p0 —/—/— (0); p1 —/—/— (0); p2 —/—/— (0); p3 —/—/— (0); p4 —/—/— (0); p5 —/—/— (0); p6 —/—/— (0); p7 —/—/— (0); p8 —/—/— (0); p9 —/—/— (0); p10 —/—/— (0); p11 —/—/— (0); p12 —/—/— (0); p13 —/—/— (0)
- **careful**: p0 1.000/0.000/0.000 (584); p1 1.000/0.000/0.000 (702); p2 1.000/0.000/0.000 (828); p3 1.000/0.000/0.000 (860); p4 1.000/0.000/0.000 (747); p5 1.000/0.000/0.000 (300); p6 1.000/0.000/0.000 (64)

The plant's life by stage beside a real root's (the ruling after run 34; a conformance diagnostic on the instrument — a plant takes every step in the pass a real root would): per root that reached its first initial seat, by case kind, the ticks posted → awarded, awarded → submitted, submitted → seated (the review's assignment), the share raised, the share whose ceiling the requester's wallet refused to raise at least once (never a plant's: its raise is minted — §52), the share at the floor (a plant unbid for w_A) or delivered by a troop (a real root unbid for w_A), the share whose reviewer had the case in its seen set and the ticks from the sighting to the seat. Each stage as real / plant, then plant − real paired by seed (mean ± SE).

| policy | roots seated (real / plant) | posted → awarded | Δ | awarded → submitted | Δ | submitted → seated | Δ | raised share | Δ | raise refused (wallet) | troop (real) / floor (plant) | seen share | Δ | ticks since sighting | Δ |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| direct | 2416.1 / 673.3 | 0.78 / 0.88 | +0.10 ± 0.09 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.07 | +0.00 ± 0.00 | 0.363 / 0.427 | +0.064 ± 0.020 | 0.191 / 0.000 | 0.010 / 0.020 | 0.110 / 0.117 | +0.008 ± 0.007 | 2.43 / 2.66 | +0.23 ± 0.12 |
| hand | 2436.5 / 607.8 | 0.86 / 0.74 | -0.12 ± 0.04 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.13 / 0.15 | +0.02 ± 0.00 | 0.378 / 0.405 | +0.027 ± 0.009 | 0.157 / 0.000 | 0.028 / 0.043 | 0.107 / 0.095 | -0.011 ± 0.004 | 2.78 / 2.55 | -0.23 ± 0.09 |
| careful | 2666.9 / 276.6 | 0.13 / 0.06 | -0.07 ± 0.02 | 1.00 / 1.00 | +0.00 ± 0.00 | 0.07 / 0.08 | +0.01 ± 0.00 | 0.143 / 0.135 | -0.007 ± 0.005 | 0.047 / 0.000 | 0.000 / 0.000 | 0.059 / 0.067 | +0.007 ± 0.004 | 1.25 / 1.10 | -0.15 ± 0.07 |
