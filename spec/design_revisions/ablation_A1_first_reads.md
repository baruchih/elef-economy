# Ablation A1 — first reads: the payoff table, the scripted sweep and the panels

*November 10, 2026. The economy's reviewer (Claude), for Baruchi, the implementer and the record. Read from the implementer's summaries of notes §80–§81 and `payoff.md`, at `ce0694775` (the payoff table), `e781edc0f` (both blind edges, every arm and seat), `80fbec3df` (§7.2, 1,100 scripted runs), `5233e468d` (I45 scoped), `daaadd578` (the panels by their question) and `8929a6304` (notes §82: the rulings counted, the dispute panel on run 42's population). The notes themselves have not reached this session: every figure below is the summaries', and the tables behind them are the implementer's. Rulebook in force: 2.9.0 with the consolidated defaults. The arms are flags under brief A1 revision 2 with addenda 1 and 2; nothing here is in force.*

## In plain words

1. **The rule is confirmed by the money.** Approving without looking stops paying at a seat only when bad cases whose truth is checked arrive there more often than an inspector's own mistakes. 2.9.0's audit seat sat on that line, which is why it was stamped about half the time.
2. **On hand-written populations, giving the later seats to the orchestrator's own inspectors pays less bad work and costs less.** A third to a half less bad work paid, and 0.7 to 1.4 credits less spent on checking per task, with the orchestrator doing a third of all review seats in place of a tenth.
3. **More stings are expensive.** Holding the planted approvals at 10 or 20 in 100 costs 2.4 or 4.5 credits more a task. Hand-written actors do not react to incentives, so the benefit can show only on the learned chains.
4. **2.9.0's penalties on correct verdicts are mostly one assumption**: the final ruling is right 80 times in 100. With an accurate ruling they nearly vanish, with or without restructuring the members' seats.
5. **This is the scripted half.** Whether a learning population behaves as the money says is read on the learned chains.

## 1. The payoff table (no learner)

The audit seat on the scripted eps population, an inspector's own money, credits an audit, against inspecting.

| Cell | Blind approval | Blind rejection |
|---|---|---|
| Arm 0 at its dial (3.8 truth-checked bad cases in 100) | +0.02 ± 0.06 | −6.51 ± 0.10 |
| Arm 0, the lever pinned at 0.10 | −0.62 | |
| Arm 0, the lever pinned at 0.20 | −1.33 | |
| Arm 1 (the trusted ruling) | +0.19 | |
| Arm 1b (the sampled confirmation) | −0.02 | |
| Arm 1c (the cheaper false alarm) | −0.13 | −4.64 ± 0.09 |

§2 of the brief holds as an account of the money. Arm 1 moves the edge against checking by 0.17 — hypothesis 1 had the sign and understated the size. Arm 1c is under the line by about a fifth of the 0.10 pin's margin.

## 2. The scripted sweep (§7.2)

Five scripted populations, paired against arm 0; 1,100 runs with the swept defaults.

| Arm | Leak against arm 0 | System overhead a task | The orchestrator | False penalties a run |
|---|---|---|---|---|
| 0, ruling at 0.8 | reference | reference | about a tenth of review seats | 20 / 12 |
| 0, ruling at 1.0 (swept default, no arm) | | | | 4 / 0 |
| 0, pinned at 0.10 / 0.20 | no change (scripted) | +2.4 / +4.5 | | |
| 1 | does not rise | | 240 deciding verdicts, 940 c_T a run | 2 / 1 (−18 / −11) |
| 1b | | | | 1.7–2.5 more at the audit seat |
| 2 | a third to a half under | −0.7 | reported for arms 2 and 4 together: +4,400 c_T a run, seats a tenth → a third | |
| 3 | a lying appeal paid 0.25 a run (arm 1: 0) | | | |
| 4 | a third to a half under | −1.4 | as arm 2's cell | |

- Arm 1's fall in false penalties is mostly the judge's accuracy; its structure (a panel confirms or escalates) removes the two-wrong-peers overturn, about 4 a run.
- Arm 3 against arm 1: the members' panel is a filter in front of the deciding verdict worth a quarter of a paid lie a run.
- Three runs stopped on I45 as first written (a troop's ordinary seat overturned by the deciding verdict, which is today's rule); scoped and re-run.
- **The rulings sought under arm 0** (notes §82): about 100 a run by cell (80 in the fixed 60/40), a fifth of them wrong.
- **Derived by the reviewer from these counts, not measured:** seating the ruling only where it is sought today takes about 100 deciding verdicts a run — about 390 of c_T at arm 1's own rate (940 for 240) — and removes about 19 of the 20 wrong rulings. Arm 1's further 140 verdicts, about 550 of c_T, buy the two-wrong-peers overturn (about 4 a run) and a panel that cannot pay a lie on its own. For the design revision after the runs; no arm.

## 3. The panels under arm 1c

| Panel, blind verdict | Arm 0 | Arm 1 | Arm 1c |
|---|---|---|---|
| Appeal — confirmation of the standing rejection | clearly under | −5.03 ± 0.41 | −2.50 ± 0.17 |
| Dispute — rejection (siding with the dispute) | not in the summary | not in the summary | −5.09 ± 0.22, halved from −10.13 |
| Dispute — confirmation of the standing approval | +0.13 ± 0.54 | −2.06 ± 2.26 (one seed's lump, 170 decisions) | +0.46 ± 0.25 |

The lenience halves the price of a blind confirmation at the appeal panel, as addendum 1 said it would, and leaves it 2.5 under inspecting: the condition for scoping arm 1c is not met. The dispute panel's blind confirmation is at inspecting in every arm because in this world every dispute is a planted lie on a good plant — the world's composition, not arm 1c's doing.

## 4. The hypotheses after the scripted reads

| # | Hypothesis | Scripted read | Learned read |
|---|---|---|---|
| 1 | Arm 1 cuts false penalties, the leak does not rise, the audit seat's stamp does not fall | Stands, in two parts (judge's accuracy; structure). The table has the edge +0.17 against checking | Not trained |
| 2 | The pins close the audit seat (blind verdicts below 0.15); the cost of truth rises | Table −0.62 / −1.33; cost +2.4 / +4.5 a task | Pending |
| 3 | Arm 1c closes the audit seat at the present dial; no blind rejections | Table −0.13; blind rejection −4.64; panels not opened | Pending; the reviewer expects the threshold missed (addendum 1, A5) |
| 4 | Arm 1b prices a confirmation where stampers are common, not in careful cells | Table −0.02; 1.7–2.5 audit false penalties a run; the split by cell is in the notes | — |
| 5 | Arm 2: leak at or below arm 0's; members' audit fees move to the orchestrator | Stands: a third to a half under, overhead −0.7 a task | Chain added (addendum 2, B3) |
| 6 | Arm 3: a lying challenge paid at the deciding verdict's error | 0.25 a run against arm 1's 0 | — |
| 7 | Arm 4: leak near the careful reference; orchestrator's seats a tenth → a third | Stands: a third to a half under, overhead −1.4 a task, seats a tenth → a third | Pending |
| 8 | The stressed world widens arm 4's advantage | — | After the implementer's steps 3–5 |

**The review's refuter** (arm 4 leaking more than arm 0, or costing the system more) is not met on the scripted cells.

## 5. Rulings (the brief's addenda carry the text)

1. **Arm 1c runs as written.** The blind rejection is not opened at the audit seat, nor a blind verdict at the panels. The bounty form is withdrawn unbuilt.
2. **The ruling's default stays 0.8 for every cell of record.** Comparability with every run on record; the frozen rulebook; and an accurate ruling drawn at no cost would be free truth. False penalties are reported by source from here, and the ruling seated only where it is sought today is costed from the swept cells beside arm 1.
3. **One chain added: arm 2 on the learned population**, after arm 1c's. Order: arm 0 pinned at 0.10; arm 4; arm 1c; arm 2.
4. **Expectations stated before the chains**: the audit seat's blind-verdict rate follows the table's edge across cells; arm 1c gives about a quarter, not under 0.15; the refuter of §2 amended and marked.
5. **I45** scoped as the implementer has it.

## 6. The dispute panel does not look — the first half of a suspicion, shown; the second half to be tested

**The suspicion** (stated in addendum 2, B5, before the number was read): at the dispute panel, a blind confirmation of the standing approval is at inspecting under 2.9.0 in a world with no real disputes. The planted lie prices siding with a dispute, and also fills the panel with cases on which confirming is right. Where customers dispute rarely, a panel taught this way would confirm blind and lose the rare truthful dispute, under every arm that leaves the dispute panel to members (0, 1, 1b, 1c, 2).

**What is shown** (notes §82, the round-10 collection; the final policy's own collection follows with §8.4):

| Population | Dispute-panel decisions | Blind confirmation | Inspecting |
|---|---|---|---|
| Run 42's (the careful basin, 2.9.0, own money) | 187, every one a planted lie | 0.787 ± 0.045 | 0.17 (the cell's ε floor 0.07) |
| The liar chain's | 7,541 | 0.050 ± 0.004 | 0.91 |

**What it is and is not.** No truthful dispute was lost in run 42's world, because none exists there. What is shown is that the careful basin's dispute panel does not look.

**The engine, confirmed by the implementer (notes §83, `a45201457`):** the truthful planted dispute follows the real requesters' rate on a wrongly approved bad plant and is zero where none disputes; 2.9.0's planted lie comes at the dial's floor. So in the careful basin that panel sees lies only. It is the record's central finding once more, on one side of one seat: a seat is honest only where truth it cannot anticipate arrives at a rate the population does not control, and here it arrives against one of the two blind verdicts only.

**A second point (notes §83).** The liar chain's panel is 28 in 100 truthful, half of those on bad plants. Its population inspects 0.90 on both kinds and confirms blind 0.055 / 0.048: it does not tell a truthful dispute from a lie. The disguise holds at this seat, and what moves the panel is the mix alone — no truthful disputes, 0.79 confirmed blind; 28 in 100, 0.05.

**The frozen test — the expectation, stated before the result.** Run 42's final policy, frozen, at a detection of 0.1 and 0.25, seeds 21–40, the scripted careful population and the hand's beside. **Expected**, from the collection's rates: the customers' truthful disputes won under a half — about three in ten (both seats confirm 0.64 of the time; a split goes to the 0.8 ruling) — against more than nine in ten for the scripted careful population; each lost dispute leaves the bad work paid and costs the customer the court fee. **Refuted** if the frozen population wins more than eight in ten.

**The frozen test, read (notes §84, `26c8fd367`).**

| Population, frozen | Detection 0.1 | Detection 0.25 |
|---|---|---|
| Run 42's — truthful disputes won | 0.72 (4.1 filed a run, 1.2 lost) | 0.70 (11.0 filed a run, 3.3 lost) |
| Scripted careful | 0.97 | 0.99 |
| The hand's | 0.98 | 0.96 |
| Run 42's — standing false approvals a run (16.3 at none) | 14.7 (+7.6 over the hand's) | 15.4 (+8.8) |

Panels pooled are blind 0.17–0.21 on real cases; the audit seat 0.52–0.54.

- **The expectation is missed on this figure, and its refuter is not met.** The trained population loses about three truthful disputes in ten where a careful one loses one to three in a hundred. The reviewer's three in ten *won* was too pessimistic by the figure as reported.
- **The split, read.** The reviewer asked whether the figure pooled the customers' disputes with the plants', in which case the customers' own rate would be about a quarter. It does not: the driver counts the plants' disputes apart, the 4.1 / 11.0 filed and 2.95 / 7.7 won are the customers' alone, and a plant's truthful dispute settles by its truth. The customers lose 28–30 in 100. The alternative reading is withdrawn, and the expectation is missed as stated: seven in ten won, not three.
- **The threshold.** The floor's lies are about 10 a run (L); the truthful disputes at a detection of 1 about 42 (T). The detection under which the truthful share falls to the line is d* = 0.012 (a line of one in twenty) to 0.034 (one in eight). In the frozen cells the panel saw about 0.42 truthful at 0.1 and 0.62 at 0.25.
- **Why seven in ten and not three — read (notes §85, `077e6d4b6`).** Three in ten assumed two members' seats at the round-10 collection's 0.79. The reviewer named three ways the result could differ before the read; it is the first and the third, and not the second:
  - *The orchestrator's inspectors hold 39 in 100 of the panel seats* in the learned population at both detections (27 in the careful's and the hand's), and confirm a truthful dispute only by their own error.
  - *No tell.* On the dispute panel the members confirm blind the customers' truthful disputes 0.62 ± 0.07 / 0.69 ± 0.06 and the planted lies 0.61 ± 0.06 / 0.69 ± 0.04. They do not tell them apart; the disguise holds at this seat.
  - *The final policy's own rate* over every kind is 0.65 / 0.70, under the collection's 0.79.
  - Per seat, 0.61 × 0.62 + 0.39 × 0.05 ≈ 0.40 gives a lost dispute at about 0.26, against the measured 0.28 / 0.30.
- **Stated as it is: the members' dispute panel does not look, and the customers' seven in ten is the orchestrator's seats.** The direct read by the panel's make-up (notes §86, `235ed2b96`; the customers' truthful disputes, run 42's policy, detection 0.1 / 0.25):

  | Panel | Won |
  |---|---|
  | Two members | 0.44 (34 disputes) / 0.23 (64) |
  | One member, one of the orchestrator's | 0.89 / 0.82 |
  | Two of the orchestrator's | 1.00 / 0.98 |
  | The scripted careful population, any make-up | 0.97–1.00 |

  The expectation of three in ten was wrong for the outcome because it left the orchestrator's seats out; for panels of two members it is what was measured (about three in ten over the 98 disputes).
- **Two members are two seats that mostly do not look — the reviewer's first reading corrected (notes §87, `6d56ec8f0`).** The reviewer read the two-member figure at 0.25 (0.23 won, against about 0.43 for independent seats at 0.69) as the one shared policy confirming together, and asked for the joint. The joint says otherwise:

  | Two-member panels, the customers' truthful disputes | Detection 0.1 (34 panels) | Detection 0.25 (64 panels) |
  |---|---|---|
  | The single seat confirms (seeds 21–40) | 0.71 | 0.83 |
  | Both confirm, observed against the product | 0.500 against 0.498 | 0.75 against 0.69 |
  | Split | | 0.16 against 0.29 |
  | Both reject | | 0.094 against 0.030 |

  The seats are independent at 0.1 and mildly correlated at 0.25. Independent seats at 0.83 win about 0.26 against the 0.23 observed: **the seat's own rate carries the loss, the correlation very little.** The 0.62 / 0.69 of notes §85 was the blind rate on seeds 1–20 under exploration; without it the final policy's seat confirms as often as the round-10 collection's 0.79. So the third of the three ways named before the read falls away as well: the customers' seven in ten is the orchestrator's seats alone. The correlation at 0.25 is recorded as mild and unexplained — 64 panels over 20 seeds cannot separate a shared choice on the same case from seeds with different rates — and is left to the implementer's step 5.
- **Why the orchestrator is on the panel: the tier (notes §86).** Of 263 / 276 unfilled panel-seat ticks a run, 262.5 / 275.4 had a free member kept off the panel tier and 0.5 / 0.1 had none free. The learned population has 92 panel-ineligible member-periods a run against the careful population's 63 (the undetermined); the 29 more are its members' records — the audit seat's half-stamp on bad plants. **2.9.0's price on the audit seat does not deter this learner, which cannot perceive eligibility; it filters.** Members whose records fail lose their panel seats, the orchestrator takes them, and that — not the members' care — holds the customers' disputes at seven in ten.
- **Readings for the design revision, no arm:** one seat of the orchestrator's on a panel is worth most of two (0.82–0.89 against 0.98–1.00); and the careful population's 27 in 100 is the tier's own cost — the undetermined kept off the panel in a population that fails no plant.
- **A correction on the implementer's side, caught before any read** (`73231d019`): the online driver fits afresh unless started from the frozen model; the first collections of this evaluation were discarded for it. **Confirmed by the implementer** that no read on record was taken that way where a frozen policy was meant: the start option has been in the online driver since October 20, every final is `run_q` loading the model directly, and the rounds are meant to fit. **One provenance gap, stated:** the probe collections of notes §53 and §57 were made by a script that loaded the round-10 model as the policy, by the notes' description; the script was not kept in the repo. Nothing is re-made for them: both are from the shared-purse cells, and the owed §8.4 re-reads the probe on own-name credit. **From here every collection on record is made by a script kept in the repo, and its note names the script and the commit.**
- **The retrained cells**, after the ablation's chains: run 42's final policy as the start, at a detection of 0.25, then 0.1; one point under d* (0.01) last and only if the machine is free.
- **What the same cells say of the leak.** At these detections the customers' disputes hardly move the bad work that stands, and the trained population still leaves about twice the hand's. The leak remains the audit seat's; the dispute does not make up for it.

**The retrained cells — the reviewer's expectation amended before they run** (the brief's addendum 3). By §2 at this seat the panel looks where truthful disputes are more than roughly one in twenty to one in eight of what it sees. The truthful share at a detection d is d·T / (d·T + L), with T the truthful disputes a run at a detection of 1 and L the lies a run; the floor's lies are few, so the share is large at any moderate detection. The reviewer therefore now expects a population retrained at a detection of 0.25, and probably at 0.1, to inspect and to win truthful disputes near the scripted rate — the opposite of what addendum 2 expected at low detection. What would remain of the suspicion: a population taught where nobody disputes loses the first disputes it meets; and the customers' dispute is void under the detection d* at which the truthful share falls to the line. Arm 2's learned chain reads its dispute panel the same way; arms 3 and 4 have none to read.

**The costing's rate** holds at 3.9 of c_T a deciding verdict (notes §83).

**Candidates for a later draft, none drafted:** the planted challenge in both truths at the dial's rate; the sampled confirmation; the state's bench.

## 7. Open

- The learned chains: arm 0 pinned at 0.10; arm 4; arm 1c; arm 2 — and the owed cells of 2.9.0.
- The dispute panel: the final policy's own collection; the liar chain's decisions by the dispute's truth; the frozen evaluation at a detection of 0.1 and 0.25.
- From notes §81 when they reach this session: hypothesis 4's split by cell; the bond sweep (×2, ×4), expected to change nothing; c_T and Ω's net by arm.
- For the record's account: 2.9.0's penalties on correct verdicts are mostly the ruling's declared error of one in five, an Appendix A default and not the rulebook's structure.
