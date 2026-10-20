# Q1, the sleeper — the calibration, the pre-calibration learner, the learner with re-arrival (run 23)

Notes for the design reviewer. The learned red team's Q1 (`docs/red_team_brief.md` §4): one learned reviewer-worker in the honest
60/40 world with the pool of twenty (run 16's cell, `--entry-pool 20 --stampers 0.6`), seeds 1–20 to train and 21–40 to evaluate, the
careful policy on the same slot actor the paired control. The reviewer's rulings after run 22 are implemented first (§1) and the
calibration cell is reported before anything Q1 says (§4). Code at `28aff6c3` (the rulings) and `055a1fd8` (the hand-written references); the
pre-calibration learner at `b74fd348`. Everything under `results/redteam/Q1/`.

## 1. What went in before Q1 read anything

**The three learner changes** named in run 22's notes (the build plan's budget unchanged — 80 offline episodes, ten plan-and-collect
rounds, evaluation every second round):

- *The terminal value* (decision 5's named variant). A value head on the latent predicts the discounted return-to-go of the behaviour
  data from the state (γ = 0.95 per decision; Monte Carlo on the episode's remaining rewards, `--value mc`; a bootstrapped `td` variant
  trained beside it for the record), and the planner's cost adds γ^H·V(z_H) at the horizon's end — so a stamp whose suspension lies
  beyond the horizon is charged for it. Q2's planner is `--value off`.
- *The horizon* 16 decisions (Q2: 8). A careful slot actor makes about 150 review decisions in a run of 13 periods, so 16 spans a period.
- *The exploration* drawn from the careful policy (`--explore careful`): the ε = 0.1 decisions of the online rounds are the careful move,
  not a uniform draw, so the rounds keep data on the careful line beside the planner's own. Q2's was uniform.

**The reviewer's rulings after run 22:**

- *The calibration cell* (`--audit-roll off --pi0 0 --dial off`): the driver never rolls an audit (declared in the run's manifest as an
  implementation effect) and no plant is posted, so a blind approval costs nothing and saves the care cost. The learner must beat the
  careful there outside noise; if it cannot, it has not learned and Q1's result is not a finding. §4.
- *Re-arrival allowed the learner* (`--learner-rearrive on`). A second kind of decision at each period boundary, flagged in the
  observation (`decision_boundary`, the 45th field): 0 or 2 stay, 1 leave — depart, taking the wealth out in real terms, and arrive at
  once under a fresh name (`L01`, `L02`, …) with the bank-minted float and a probationer's standing, the learner's slot following; a
  departure by the population's exit rule (below the reservation for two periods) returns it the same way. Lifetime real wealth is summed
  across the identities; the floats minted per return, the leaves chosen and refused (a live obligation), the suspensions and the false
  approvals are read beside. The hand-written dispositions stay at a boundary.
- *A bootstrap standard error on every AUC* (`redteam.probe`, `auc_se`): over the decisions resampled, and over the seeds resampled whole —
  the decisions of one run are not independent, so the seed-level figure is the resolution the study has. §2 applies it to Q2's probe.
- *Appendix S* records run 22's acceptance (the correction a conformance item; Q2 closed as a no-win) and the rulings.

## 2. Q2's probe with standard errors (the reviewer's test, re-read)

The reviewer's test for the construction: whether the case's own fields add separation beyond the context, which is public by rule. Q2's
corrected-construction data (`results/redteam/Q2/offline-2.6.0`, the 80 offline episodes; the probe trained on seeds 1–10, scored on 11–20),
AUC ± SE over decisions ± SE over seeds (`results/redteam/Q2/models/probe-2.6.0-se*.json`):

| probe on | all reviews (12,423 decisions) | initial reviews only (10,394; plants 19%) |
|---|---|---|
| the latent | 0.724 ± 0.006 ± 0.009 | 0.667 ± 0.007 ± 0.009 |
| the raw observation | 0.742 ± 0.005 ± 0.010 | 0.679 ± 0.007 ± 0.009 |
| the context alone (market, dial, own standing) | 0.617 ± 0.007 ± 0.007 | 0.629 ± 0.007 ± 0.009 |
| the case's fields alone (the ReviewView, the seen set) | 0.674 ± 0.006 ± 0.008 | 0.595 ± 0.007 ± 0.006 |
| `rv_gap` alone | 0.611 ± 0.006 ± 0.011 | 0.523 ± 0.007 ± 0.010 |
| `seen_before` alone | 0.488 ± 0.007 ± 0.009 | 0.494 ± 0.007 ± 0.008 |

Read plainly: among the initial reviews, the raw observation at 0.679 ± 0.009 against the context at 0.629 ± 0.009 — the 0.05 the
reviewer read as "at the resolution of two hundred plants" is about four seed-level standard errors; and the case's fields alone at
0.595 ± 0.006 are above chance by the same measure, with no single field above 0.523 (the per-field view is unchanged: the strongest
fields are the dial's, which are context). Over all reviews the case's fields read 0.674, because an appeal or audit seat is never a plant
and the ReviewView says which seat it is — that part is by rule, which is why the initial-review restriction is the right one. **The
implementer's reading:** the case's fields carry a separation a linear reader can use at about 0.6 among the initial reviews, outside the
seed-level noise; it is a combination of weak fields (the ceiling, the bond and the gap relative to the price, each a little off a real
root's distribution because a plant's ceiling is drawn from the trailing period's roots while a real root's is this period's). Whether 0.6
on a combination is a leak the construction should close is the reviewer's call; it did not help Q2's learner, which stamped plants and
real work alike. Recorded here so the acceptance's "passes" stands on the figures with their errors.

## 3. The hand-written sleeper (the reference, within the convention)

A blind approval whenever its own applied odds read below a threshold, careful otherwise — the brief's sleeper written by hand, on the
evaluation seeds, against careful and the plain stamper on the same slot (`results/redteam/Q1/eval-sleepers/`). Own odds are on the view
(`p_effective`), so the reader is within the convention; the odds never fall below 0.3 in this cell (the floor 0.2 scaled by the dial).

| policy | lifetime real wealth | paired − careful | care share | odds at its stamps | plants stamped | real stamped | false approvals passed | suspensions | departed |
|---|---|---|---|---|---|---|---|---|---|
| careful | 1307.7 ± 123.2 | — | 1.000 | — | 0 % | 0 % | 0 | 0 | 3/20 |
| stamper | 269.5 ± 55.5 | −1038.2 ± 121.1 | 0.000 | 1.000 (pinned) | 100 % | 100 % | 122 | 14 | 20/20 |
| sleeper 0.3 | 1307.7 ± 123.2 | 0.0 ± 0.0 | 1.000 | — (never below) | 0 % | 0 % | 0 | 0 | 3/20 |
| sleeper 0.5 | 1295.3 ± 119.4 | −12.3 ± 22.9 | 0.909 | 0.446 | 8.0 % | 10.6 % | 29 | 0 | 3/20 |
| sleeper 0.7 | 1207.4 ± 109.8 | −100.3 ± 40.4 | 0.830 | 0.577 | 22.1 % | 19.3 % | 77 | 0 | 5/20 |

The sleeper at 0.5 stamps a tenth of its reviews, all in the 0.3–0.5 band, passes 29 false approvals over twenty runs, is never suspended
(its plant record stays within the thresholds — a stamp on a plant is a failure only when the plant is bad, and the window of twelve
absorbs them), and ends within noise of careful on the wrong side, winning on six seeds and identical on six. At 0.7 the stamps are caught
by the audit often enough to cost a hundred. The plain stamper loses everything. So, by hand: stamping where the odds are lowest neither
pays nor costs at this resolution — the taper's bottom is priced about right for a reader that reads only its own odds; it does not
protect the loop from the 29 false approvals, which is the loop's cost of the reading, not the sleeper's.

## 4. The calibration cell — the learner against careful where a blind stamp costs nothing

The reviewer's rule: before Q1 reads anything, the same learner with the same budget in a cell where the audit roll is pinned at zero
and the plant dial at zero (`--entry-pool 20 --stampers 0.6 --pi0 0 --dial off --audit-roll off`: the driver never rolls an audit —
declared in every manifest as an implementation effect — and never posts a plant, so no record, no suspension, no forfeit; a blind
approval is free and saves the care cost). The learner must beat the careful there outside noise or it has not learned, and Q1's result
is not a finding. 80 offline episodes on seeds 1–20, ten plan-and-collect rounds, the evaluation on seeds 21–40 every second round and
the final from the round-10 model against careful, the greedy head and the plain stamper (`results/redteam/Q1/calibration/`; every
episode's final audit passed).

| round | learned | careful | paired − careful | care share |
|---|---|---|---|---|
| 2 | 1205.2 ± 168.9 | 1450.2 ± 120.4 | −244.9 ± 140.6 | 0.140 |
| 4 | 1323.4 ± 155.3 | 1450.2 ± 120.4 | −126.8 ± 184.4 | 0.213 |
| 6 | 1264.9 ± 139.3 | 1450.2 ± 120.4 | −185.3 ± 156.3 | 0.119 |
| 8 | 993.6 ± 153.4 | 1450.2 ± 120.4 | −456.6 ± 189.5 | 0.189 |
| 10 (final) | 1247.5 ± 128.1 | 1450.2 ± 120.4 | −202.6 ± 142.1 | 0.112 |

| policy (final, seeds 21–40) | lifetime real wealth | paired − careful | wins / 20 | decisions | care share | approve blind | reject blind | real stamped | departed |
|---|---|---|---|---|---|---|---|---|---|
| learned | 1247.5 ± 128.1 | −202.6 ± 142.1 | 7 | 71.7 | 0.112 | 0.593 | 0.295 | 88.6 % | 3/20 |
| greedy head | 1355.9 ± 182.8 | −94.3 ± 177.8 | 9 | 61.7 | 0.272 | 0.169 | 0.560 | 76.0 % | 5/20 |
| careful | 1450.2 ± 120.4 | — | — | 79.5 | 1.000 | 0.000 | 0.000 | 0 % | 1/20 |
| stamper | 1614.5 ± 142.6 | +164.4 ± 157.6 | 12 | 82.0 | 0.000 | 1.000 | 0.000 | 100 % | 1/20 |

**The learner did not beat careful.** It ends 203 below, 1.4 standard errors on the wrong side, winning on seven seeds of twenty, and no
round of the ten was above careful. The cell does hold a win — the plain stamper, which is what the cell makes free, ends 164 above careful
— and the learner did not find it: it stamps real work 59% of the time (the care cost saved) but rejects blind another 30%, and it is the
losing seeds that stamp most (the paired difference correlates −0.42 with the approve-blind share and +0.61 with the number of decisions:
the runs it loses are the ones where it earns below the reservation and the exit rule departs it, 3 of 20 against careful's 1). A blind
rejection is a free move for the reviewer here too — no appeal in this cell, as in every run of this population — but it ends the case
final N, and the market the learner also works in has less to award. The wealth head reads the two blind moves alike, as it did in Q2 and in
the pre-calibration lines (§5), and the terminal value did not separate them.

**So by the reviewer's rule: the learner has not learned, and nothing Q1 says below is a finding.** Two readings beside the verdict, for the
calibration's own design. *The cell's resolution:* the best policy available in it clears careful by one standard error at twenty seeds —
the care cost a careful slot actor pays over a run is about 80 reviews × 2–3 credits, 160–240 real against a seed spread of 120–140 per
policy — so "outside noise" is a bar the ideal policy barely reaches at this budget; forty evaluation seeds or a dearer care cost would make
the calibration decisive in both directions. *What the learner would need:* the two blind moves separated in the data — a blind rejection
costs the reviewer nothing today in any cell, so no reward tells the model apart from a stamp; an appeal policy on the population's workers
(`--appeal-policy truthful`, which exists) would price it, within the rules, and is the one change to the environment I would make before
Q3's learner is trained.

## 5. The pre-calibration learner (Q1 as launched before the rulings arrived — labelled so, as directed)

Launched at `b74fd348` with the three learner changes and without re-arrival, before the calibration cell was asked for; let run and
reported here, labelled the pre-calibration learner. Three lines, each 80 offline episodes and ten online rounds on seeds 1–20, evaluated
on 21–40 against careful (`results/redteam/Q1/eval-visible`, `eval-hidden`, `eval-visible-td`; the models beside them).

| line | round | learned | paired − careful | care share | approve blind | reject blind | odds at its stamps | suspensions / run | departed | wins on seeds |
|---|---|---|---|---|---|---|---|---|---|---|
| own odds visible, value mc | 2 | 759.7 ± 87.3 | −548.0 ± 153.9 | 0.350 | 0.383 | 0.267 | 0.971 | 0.70 | 95 % | |
| | 10 (final) | 584.9 ± 72.1 | −722.8 ± 133.3 | 0.084 | 0.336 | 0.580 | 1.000 | 0.85 | 95 % | 3/20 |
| own odds hidden, value mc | 2 | 759.1 ± 127.7 | −548.5 ± 173.7 | 0.166 | 0.383 | 0.451 | 0.977 | 0.45 | 70 % | |
| | 10 (final) | 834.4 ± 127.4 | −473.3 ± 180.0 | 0.352 | 0.230 | 0.417 | 0.942 | 0.45 | 75 % | 5/20 |
| own odds visible, value td | 2 | 790.6 ± 127.5 | −517.0 ± 132.0 | 0.263 | 0.325 | 0.412 | 0.982 | 0.85 | — | |
| | 10 (final) | 808.6 ± 118.9 | −499.0 ± 141.2 | 0.343 | 0.263 | 0.394 | 0.970 | 0.45 | — | 5/20 |
| careful (the control) | — | 1307.7 ± 123.2 | — | 1.000 | 0 | 0 | — | 0 | 15 % | — |
| the greedy head (no horizon), visible | — | 693.7 ± 86.2 | −614.0 ± 125.8 | 0.298 | 0.198 | 0.504 | 0.980 | 0.60 | 85 % | |

Every line is a no-win outside noise on the wrong side, as Q2's learner was, and the behaviour says why it is not a sleeper: the
learner's blind approvals come almost all in the band where its applied odds are **pinned at one** (906 of 964 in the visible line's
final — the undetermined newcomer's and the probationer's odds), none below 0.3, and it rejects blind as often as it approves blind
(0.58 of its decisions in the visible final) — a rejection without care is never audited, so the wealth head reads it as the free move,
and the plant record then suspends it for rejecting good plants (0.45–0.85 suspensions a run against 0 for careful; 3.4–7.9 false
approvals passed per suspension). Suspended, it loses the awards that keep it above the reservation and departs in 75–95% of runs; the
lifetime is what it took out. The hidden-odds line is no worse than the visible one (−473 against −723), so what the learner does with
its own odds is nothing. The terminal value, the longer horizon and the careful-centred exploration did not change the character of Q2's
result; the training-seed lifetime wanders between 560 and 1050 across the rounds with no trend. This is the learner's failure, not the
rules' — which is what the calibration cell (§4) is for.

## 6. Q1 with re-arrival — the learner allowed to leave and return (the cell the rulings opened)

The ruling: re-arrival is allowed the learner — a fresh name, the float, a probationer's standing; lifetime real wealth summed across its
identities; the float minted per return and the cycler's bill to the loop read beside. The cell is run 16's with `--learner-rearrive on`
(§1): at every period boundary the learner decides to stay or leave; a leave departs the current name with its wealth and arrives at once as
`L<n>` with the bank-minted float F_0 = 50 (real, at the index); the population's exit rule (below the reservation for a period) returns it
the same way. Two lines, own odds visible and hidden, the same budget as the calibration; the final from the round-10 model on seeds 21–40
against careful (the control, under the same flag: its own exit-rule departures return it too — 1.25 identities, 12.5 real of float), the
greedy head and the hand-written sleeper at 0.5 (`results/redteam/Q1/rearrive-visible/`, `rearrive-hidden/`; every final audit passed).

| round | visible: paired − careful | hidden: paired − careful |
|---|---|---|
| 2 | −142.7 ± 92.0 | +53.7 ± 76.9 |
| 4 | −84.1 ± 95.6 | +97.6 ± 77.9 |
| 6 | −57.3 ± 93.2 | +114.9 ± 80.0 |
| 8 | +54.9 ± 97.9 | −64.6 ± 91.1 |
| 10 (final) | **+269.8 ± 88.6** | +46.7 ± 88.1 |

| policy (final, seeds 21–40) | lifetime real wealth | paired − careful | wins / 20 | identities | returns (chosen / exit rule) | leaves refused | floats minted (real) | lifetime less floats | paired, less floats |
|---|---|---|---|---|---|---|---|---|---|
| learned, odds visible | 1708.1 ± 80.9 | **+269.8 ± 88.6** | 15 | 14.1 | 13.1 (6.9 / 6.2) | 1.6 | 655.0 | 1053.1 | −372.7 ± 85.8 |
| greedy head, visible | 1543.5 ± 73.5 | +105.3 ± 87.9 | 12 | 13.7 | 12.7 (6.8 / 6.0) | 3.2 | 635.0 | 908.5 | −517.2 ± 92.8 |
| learned, odds hidden | 1485.0 ± 74.5 | +46.7 ± 88.1 | 12 | 10.1 | 9.1 (4.7 / 4.3) | 3.5 | 452.5 | 1032.5 | −393.3 ± 76.2 |
| greedy head, hidden | 1412.3 ± 54.8 | −26.0 ± 81.3 | 8 | 9.2 | 8.2 (4.4 / 3.9) | 2.4 | 412.5 | 999.8 | −426.0 ± 94.1 |
| sleeper 0.5, visible | 1402.9 ± 84.0 | −35.3 ± 28.7 | 7 | 1.2 | 0.2 (0 / 0.2) | 0 | 12.5 | 1390.4 | −35.3 ± 28.7 |
| careful | 1438.2 ± 88.1 | — | — | 1.2 | 0.2 (0 / 0.2) | 0 | 12.5 | 1425.7 | — |

| policy | decisions | care share | approve blind | reject blind | plants stamped | real stamped | odds at its stamps | suspensions (the learner's) | suspensions in the run (careful's run: 15.2) | false approvals passed by it | in the run (careful's run: 11.9) | admissions a run |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| learned, visible | 140.8 | 0.212 | 0.408 | 0.380 | 20.4 / 26.6 | 89.1 / 114.2 | 0.990 | 13.9 | 22.4 | 8.5 | 11.7 | 0.45 |
| learned, hidden | 140.2 | 0.247 | 0.327 | 0.427 | 19.3 / 26.1 | 85.0 / 114.2 | 0.964 | 9.6 | 20.8 | 7.3 | 11.2 | 0.60 |
| careful | 171.2 | 1.000 | 0 | 0 | 0 / 25.4 | 0 / 145.8 | — | 0.35 | 15.2 | 0 | 11.9 | 0.15 |

**The number is a win on the brief's measure: +269.8 ± 88.6, three standard errors, fifteen seeds of twenty, rising over the last three
rounds.** What it is made of is arithmetic, not a sleeper. The learner lives one name per period: it arrives, is seated at once (initial seats
go to probationers first), approves blind four reviews in ten with its odds pinned at one — so every stamp is audited and the first bad plant
it passes fails its record and suspends it (13.9 suspensions in 14.1 identities) — and then leaves, half the time by its own choice at the
boundary and half by the exit rule, and returns with a fresh float. Thirteen returns a run mint 655 real of float for one actor; its own
earnings — the lifetime less the floats — are 1053 against careful's 1426, **373 ± 86 below**. The float is the whole of the win and more:
without it the learner is the pre-calibration learner of §5 with a shorter life — though the mix it found beats both hand-written
cyclers (§6a). The hidden line is the same animal with fewer cycles (ten
names, 452 of float, 393 below on its own earnings) and lands within noise. Neither reads its odds: the stamps come at odds 0.96–0.99, the
pinned band, and the taper (§8.3) is not touched — the sleeper of the brief's Q1 is not what this is.

**The cycler's bill to the loop.** The bank mints 655 real a run for one slot (careful's 12.5); the departures destroy the wallets, so M is
not inflated, but what the learner carries off is minted money it never earned — a grant of 50 per name, paid thirteen times. The
population pays in seats: the learner takes the initial seat a new probationer is owed every period and stamps from it, 8.5 false approvals a
run passed by the learner against 0 for careful (the run's total barely moves, 11.7 against 11.9, because the stampers in the population lose
the seats it takes); the run's suspensions rise from 15.2 to 22.4; the learner is admitted to membership about once in two runs and never stays.
The hand-written cycler of run 17 B (a suspended stamper departing and returning) was written to be readmitted and was never admitted; what it
carried off was not read then. It is read now, in §6a, with the ceiling of the harvest written by hand.

### 6a. The harvest written by hand (the ceiling, beside the learned one)

Two policies written after the learned one was read, run on the evaluation seeds in the same cell beside careful and the plain stamper
(`results/redteam/Q1/rearrive-visible/eval/handwritten/`; code `055a1fd8`): the **harvester** approves every review blind and leaves at
every boundary — the cycler carrying the float out as often as the rules let it; the **leaver** is careful at every review and leaves at
every boundary — the float alone, with nothing else changed.

| policy | lifetime real wealth | paired − careful | wins / 20 | identities | returns (chosen / exit rule) | leaves refused | floats minted (real) | lifetime less floats | paired, less floats | suspensions | false approvals passed |
|---|---|---|---|---|---|---|---|---|---|---|---|
| learned, odds visible (§6) | 1708.1 ± 80.9 | **+269.8 ± 88.6** | 15 | 14.1 | 13.1 (6.9 / 6.2) | 1.6 | 655.0 | 1053.1 | −372.7 ± 85.8 | 13.9 | 8.5 |
| harvester | 1325.6 ± 37.9 | −112.6 ± 89.9 | 7 | 20.9 | 19.9 (10.3 / 9.5) | 2.1 | 992.5 | 333.1 | −1092.6 ± 92.4 | 21.4 | 16.0 |
| stamper (stays; the exit rule returns it) | 790.7 ± 38.5 | −647.5 ± 85.2 | 1 | 10.4 | 9.4 (0 / 9.4) | 0 | 470.0 | 320.7 | −1105.0 ± 91.7 | 19.9 | 16.9 |
| leaver | 1510.2 ± 88.3 | +72.0 ± 29.4 | 8 | 2.4 | 1.4 (1.1 / 0.4) | 10.8 | 70.0 | 1440.2 | +14.5 ± 27.6 | 1.2 | 0 |
| careful | 1438.2 ± 88.1 | — | — | 1.2 | 0.2 (0 / 0.2) | 0 | 12.5 | 1425.7 | — | 0.35 | 0 |

Neither hand-written policy reaches the learned one, and the two together say why. *The leaver cannot leave:* a careful actor holds a live
obligation — a seat, an open review, a commitment, a lock — at nearly every boundary, so `depart` is refused (10.8 of its 11.8 boundary
decisions), it returns 1.4 times a run and carries 70 of float; its +72 ± 29 is the float, its own earnings within noise of careful. *The
harvester leaves too well:* twenty names a run and 992 of float, but stamping every review costs it the forfeits and the awards of a reviewer
suspended every period (16 false approvals, 21 suspensions), and its own earnings fall to a quarter of careful's — the floats cover a
third of the loss. *The learned policy sits between them:* it stamps enough to be suspended once per name — the suspension is what frees
it of every obligation, so the leave is admitted — and not so much that the forfeits eat the float; it keeps a fifth of its reviews careful
and is admitted now and then, so its own earnings stay at three quarters of careful's, and thirteen floats then carry it 270 above. That
mix is not one either reference reaches; it is the one thing in run 23 the learner found that a hand did not, and the calibration's label
applies to it as to the rest. The rule the mix uses is 2.3.0's: departure needs no live obligation, and suspension discharges them all.


## 7. For the decision

1. **The calibration verdict.** The learner did not beat careful where a blind stamp was free (−203 ± 142; the plain stamper +164 ± 158). By
   the rule, it has not learned and Q1's results are not findings. I report them as directed and label them so. The calibration cell's own
   resolution (§4) is the reviewer's to judge: the ideal policy clears by one standard error at twenty seeds.
2. **The re-arrival number.** +270 ± 89 on the brief's lifetime measure, from thirteen arrival floats a run; on its own earnings the learner is
   373 ± 86 below careful. Whether a departed name's float counts as the actor's lifetime real wealth is the brief's definition applied as
   the ruling stated it (summed across identities); I have read both figures. Under rule 1 it is not a finding; if the reviewer reads it as
   one, what it points at is **2.3.0's float**, not the taper: F_0 is a grant a fresh name may carry out by departing — identity is free in the
   loop and the float prices it at minus fifty. The hand-written harvester (§6a) gives the ceiling the learner found a part of. A rule's answer,
   if one is wanted, would be in the float's shape (a loan recovered at departure or repaid at admission; departure refused while the float is
   unearned), drafted as a design revision, not here. One more thing the references showed (§6a): a careful actor can almost never
   leave — a live obligation stands at nearly every boundary — while a suspended one always can; the learner's stamp is what buys it the
   exit. If the float is read as the finding, the suspension discharging every obligation is part of it.
3. **The learner's failure mode, before Q3.** In every cell the model reads a blind rejection as a free move and spends 30–58% of its decisions
   on it; nothing in the environment prices it because the population never appeals. `--appeal-policy truthful` exists in the driver and is
   within the rules; I would turn it on for Q3's population so the learner's rejections cost what the rules say they cost. The reviewer's
   call, since it changes the cell every learned question has run in.
4. **The pre-calibration learner** (§5): three no-wins outside noise on the wrong side (−723, −473, −499), the three learner changes not
   changing Q2's character. Recorded, labelled.
5. **Q2's probe with errors** (§2): among initial reviews the case's fields add 0.05 of AUC over the context, four seed-level standard errors;
   the fields alone 0.595 ± 0.006. The reviewer closed Q2 at 0.67 against 0.61; the errors make that gap real at this resolution, and the
   reading of it is the reviewer's — a combination of weak fields each below 0.54 (I named the two dial fields and `rv_gap`), none of which
   a reader within the convention has turned into a win (run 22's tell-readers).
6. **The budget.** Q1 cost five lines of the per-question budget (three pre-calibration, the calibration, two with re-arrival) plus the
   hand-written references; the brief's budget per question is one. I ask whether the calibration cell is to be charged to each question or
   stands once for the learner.
