# Addendum 29 — how often one pair meets where care is scarce, and two counts of a careful slot's failed tests (November 18, 2026; notes §124)

- **world 3's all-careful run again whole at 8e30eac40 (a23/rerun, itself 0 differences against a22/rerun)**: 100 seeds, 32300 row columns and 512102 per-slot keys over 3947 slots compared with the record's — **0 differences**; the `bad_met_first_json` tally **0 differences**.
- **read 29 run again whole at 8e30eac40 (a23/r29)**: 100 seeds, 40800 row columns and 543121 per-slot keys over 3958 slots compared with the record's — **0 differences**; the `bad_met_first_json` tally **0 differences**.

Loaded: cw3 100 (record 100), r29 100 (record 100), r32 100, r25 100, r33 100, r34 100 episodes.

## 1. How often one pair meets — a first reviewer and the member at its audit seat (AI3)

Over a run, every member audit seat whose first seat was a slot's (the state's and the orchestrator's first seats apart): the pairs that meet, the mean over them, the share of them meeting more than three times, the largest; by the holder of the audit seat where the world has two conducts. The reviewer's even spread (R) is the side's audit seats over the first reviewers, λ = the side's member audit seats a run / (slots − 1) / the side's slots; by chance alone a Poisson count at λ gives the mean over the pairs that meet and the share over three.

| population | audit seat's holder | member audit seats a run (a slot's first seat) | pairs that meet | **meetings a pair that meets** | **more than three times (share)** | the largest | members a first reviewer meets | λ, the even spread (R: his) | by chance alone: mean / share > 3 | the reviewer's range |
|---|---|---|---|---|---|---|---|---|---|---|
| world 3's all-careful | any member | 1290 | 351 | **3.68** | **0.36** | 27.7 | 9.4 | 0.85 (0.93) | 1.5 / 0.02 | 1.5–2.4 / 0.02–0.12 |
| read 29: case-keyed M at 0.2 on 3 in 4 | any member | 1288 | 303 | **4.28** | **0.39** | 33.3 | 8.4 | 0.84 (—) | 1.5 / 0.02 | — |
| read 29: case-keyed M at 0.2 on 3 in 4 | careful | 869 | 143 | **6.30** | **0.59** | 33.2 | 4.2 | 2.41 (2.56) | 2.6 / 0.25 | 2.8–4.5 / 0.28–0.55 |
| read 29: case-keyed M at 0.2 on 3 in 4 | conduct | 418 | 160 | **2.57** | **0.22** | 14.6 | 4.7 | 0.37 (0.39) | 1.2 / 0.00 | 1.2–1.8 / — |
| read 32: case-keyed M at 0.1 on 3 in 4 | any member | 1307 | 342 | **3.84** | **0.38** | 29.8 | 9.2 | 0.86 (—) | 1.5 / 0.02 | — |
| read 32: case-keyed M at 0.1 on 3 in 4 | careful | 507 | 114 | **4.38** | **0.44** | 25.1 | 3.3 | 1.38 (1.26) | 1.8 / 0.07 | 1.8–3.0 / 0.06–0.25 |
| read 32: case-keyed M at 0.1 on 3 in 4 | conduct | 799 | 227 | **3.50** | **0.34** | 23.0 | 6.3 | 0.70 (0.78) | 1.4 / 0.01 | 1.4–2.2 / — |
| read 25: M at 0.1 on every slot | any member | 1290 | 345 | **3.75** | **0.38** | 27.1 | 9.5 | 0.85 (—) | 1.5 / 0.02 | — |
| read 33: two groups, today's picks | any member | 1290 | 343 | **3.76** | **0.37** | 29.1 | 9.3 | 0.84 (—) | 1.5 / 0.02 | — |
| read 34: the seating by group | any member | 1318 | 335 | **3.93** | **0.38** | 29.7 | 9.2 | 0.87 (—) | 1.5 / 0.02 | — |

The pairs are the round-robin's: the audit seat goes to the next free panel-eligible member in id order after the last pick, so a first reviewer's audits fall to the few members free at its cases' turns and the same two meet many times where an even draw would give one or two.

## 2. Two counts of a careful slot's failed tests (AI4) — world 3's all-careful, from the record

Of 3947 slots on 100 seeds, **0.520 carry a wrong planted verdict in the run at any standing** — this is §118's '52 in 100 reach the first loss of their earned seats': the driver's phase from the first wrong verdict on (`pf_phase` 'lost' begins at `pfail_ticks[0]`, whatever the standing and whether or not the seats go, and ends at the next tick as a member with the seats, of zero length where the first failure takes nothing) — of which **0.414 as a member** (§122's 0.41) and 0.119 on probation (an arrival's, or the way back's; the two overlap). The seats are lost by the record — a member's ticks with a determined record and no earned seats — for **0.251 of the slots**, 253 ticks each on the mean. By the road, in 100 of all slots:

| how the earned seats come to be lost | slots (in 100 of all) | of the slots that lose them |
|---|---|---|
| the first wrong verdict as a member with the bad window at 4 to 7 — the seats held and taken at once | 10.9 | 0.44 |
| the first wrong verdict as a member with the bad window at 3 or under — the record undetermined, the seats never yet held, withheld when it is determined until the window holds eight | 4.8 | 0.19 |
| a later wrong verdict as a member: the first with the window at eight or more took nothing, a second within it did | 3.2 | 0.13 |
| a wrong verdict carried from probation alone (an arrival admitted with it in the window, no wrong verdict as a member) | 4.2 | 0.17 |
| one wrong verdict as a member with the window at eight or more, and a wrong one on probation before it | 0.4 | 0.02 |
| otherwise — one wrong verdict as a member with the bad window at eight or more and nothing on probation: by the rule the only road left is a rejected *good* plant with the good record determined (four to seven good plants met; the tally carries the verdict, not the kind) | 1.4 | 0.06 |
| no wrong verdict recorded (a tick or so at the record's determination) | 0.1 | 0.00 |

The first wrong verdict as a member by its window: at 3 or under 0.20 of them (the seats not yet held; 188 of 326 later carry lost ticks), at 4 to 7 0.27 (432 of 446 lose the seats), at 8 or more 0.53 (201 of 862 ever lose them in the run, 661 never) — §122's 0.47 'take the seats at once' is the first two together, and 0.27 of the first failures take seats a member held. Of the 470 slots with a wrong verdict on probation 235 are admitted within the run and 213 of those are members without the seats on a determined record, 165 with no wrong verdict of their own as a member. The rule as the engine has it: `record_passes(θ)` fails a kind whose window holds n_min or more with (wrong + 1) / (n + 2) above θ — one wrong bad plant fails θ_panel 0.20 at n ≤ 7, two at n ≤ 12; one rejected good plant at 4 ≤ n_good ≤ 7 (a careful slot meets 2.3 good plants as a member in a run, so that record is seldom determined).

