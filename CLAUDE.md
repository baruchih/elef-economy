# Agentic-OS — the economic loop

A rulebook for a task → verification → dispute → settlement loop among autonomous actors, and a
reference implementation of it with no strategies. Ten external reviews. The rulebook is at **1.7.1**:
the frozen 1.0.1 baseline plus seven design revisions made under §19 — the verification deposit is two
pots (1.1.0, §4.3; after the first scoped run showed careful review paid for its own care), the loop's
own clock (1.2.0, §7.6, §11.2, §12.2: planted work, the plant record, the effort dial; after runs 2–3
showed the loop fair only with both challengers present and blind under capture), and inspection is
membership (1.3.0, §5.2, §11.2, §12.1: a suspended actor wins no award, probation is the way back, a
cap on members' duty, the dial's raised tax paid to the reviewers; after run 4 showed suspension from
duty was a reward), and the orchestrator's troops (1.4.0, §7.7, §8.3, §12.3: a rolled audit is an obligation
of the case; a seat unfilled for w_R ticks or a request unawarded for w_A with no free member is taken by a
troop the engine summons and the duty fund pays, used last, used once, counted in public; after run 5 showed
a captured market honest and short of hands), and the reserve is sized to the need (1.5.0, §12.3, I23: the fund's
troop reserve is the current period's peak troop *demand* — capital held plus the cost of the summonses it
refused for funds — starting at the standing demand, so the fund grows into the need and pays out the rest at the
period's end; after run 6 showed the 1.4.0 reserve, the peak capital once carried, drained to by every batch's
uplift and so never able to rise), and auto-scale (1.6.0, §3.1, §6.1, §7.1, §10.4, §12.1, §12.3, I26: every root
request carries a service clock and the orchestrator owes the requester for lateness past T_s, from Ω or as Ω's
liability; Ω backs the fund above a plant reserve with no advance cap, inspection seats before deliveries, a delivery
summoned only when its inspection can be carried too; the reserve is sized on the reviews waiting; a panel seat needs
a determined record once the world's first plant is adjudicated; R_T over two periods — five rules, one flag each;
after run 7 showed the reviewing seat, not the treasury, capping the market, the demand stock counting a never-expiring
queue, and the probation leak as the plant record's lag on the auditor), and the state's earnings (1.7.0, §4.1, §10.4, §12.1,
§12.2, §12.3, I23: the duty fund is 1.3.0's uplift fund again — the raised tax in, its whole balance out — and the troops' wallet
is a separate troop account whose unlocked balance above R_T, now the two-period peak of the capital troops hold, flows to Ω at
each batch; 1.4.0's "nothing a troop earns reaches Ω" withdrawn, the guards named, Ω's income by source a reading; the members'
duty cap two thirds; ω₀ swept with the rebate pinned; after run 8 showed the troops' earnings paying the reviewers' uplift while Ω
carried the clock's rebates on 2 a tick and went broke at 50–60%) — and one patch, **1.7.1**: §12.3's summons for an award is
read per request, not per tick — the root requests past w_A beyond the free fundable members are the state's, oldest first,
after the members have taken theirs — a conformance correction ruled after run 9's addendum traced the 50/50 collapse to
one free member blocking every award summons that tick; no rule moved. Read `HANDOFF.md` first for where things stand
and what is proposed next.

## Layout

```
spec/agentic_economics_loop_spec_v1_7_1.md   the text in force (standalone; Appendix A defaults, E errata, F–L design revisions 1–7 and the 1.7.1 ruling)
spec/design_revisions/                       accepted design revisions, verbatim (dr1: two pots; dr2: the loop's own clock; dr3:
                                             inspection is membership; dr4: the orchestrator's troops; dr5: the reserve is sized to
                                             the need; dr6: auto-scale; dr7: the state's earnings), and the implementer's reviews of dr2–dr7's candidates
spec/history/                                v0.1 … v1.7.0 — superseded, kept for provenance only
reviews/                                     R01–R10, one external review per version, with the reviewer's notes
agentic_sim/                                 the engine, 26 invariants, 25 test files, runner, drivers, results
docs/line_map_economic_loop_v1_0_1.txt       text export of the _line map of the loop (the live map is the source)
HANDOFF.md                                   status, history table, open questions, proposed next step
```

## Commands

```
cd agentic_sim
python3 run_tests.py        # expected: 248 passed, 0 failed, 26 expected failures
python3 -S run_tests.py     # same, with no site-packages
python3 run_tests.py --record   # same, every World in record mode
python3 -m pytest tests -q  # expected: 248 passed, 26 xfailed, 0 xpassed (conftest mirrors the runner; pytest is not installed here)
python3 -m drivers.load_run --actors 200 --ticks 10000 --on-duty 40 --tasks 30 --record-dir /path  # throughput run
python3 -m drivers.stamping --actors 20 --ticks 1000 --stampers 0.6 --seed 1 --appeal-policy truthful   # §18.1 q1 under 1.7.0
python3 -m drivers.stamping --rules 1.6.0 --seed 1   # the 1.6.0 control: the merged fund (uplift from troop earnings), the half cap, the demand reserve
python3 -m drivers.stamping --accounts off --seed 1   # the troop account off alone (the cap stays two thirds); --duty-cap half alone is the other OFAT cell
python3 -m drivers.stamping --omega-rate 0.10 --r-s 1 --seed 1   # the 1.7.0 §8 take sweep: ω₀ 5/10/15% with the rebate pinned at 1 a tick
python3 -m drivers.stamping --rules 1.5.0 --seed 1   # the 1.5.0 control: also the five 1.6.0 flags off, A_T binds, one-period reset
python3 -m drivers.stamping --seat-queue off --seed 1   # one 1.6.0 rule off alone (also --clock, --backing, --panel-determined, --reserve-periods 1)
python3 -m drivers.stamping --duty-cap all --omega0 1000 --t-s 5 --seed 1   # the 1.6.0 §8 sweeps' knobs; --plant-reserve period is the text's literal horizon
python3 -m drivers.stamping --rules 1.4.0 --seed 1   # the 1.4.0 control: the reserve is the peak capital carried (two periods)
python3 -m drivers.stamping --rules 1.3.0 --seed 1   # the 1.3.0 control: troops off (the audit obligation holds in every mode)
python3 -m drivers.stamping --rules 1.2.0 --seed 1   # the 1.2.0 control: also membership, the fund and netted plant capital off
python3 -m drivers.stamping --rules 1.1.0 --seed 1   # the 1.1.0 control: also no plants, dial off, p 0.5/0.5, Ω float 20
python3 -m drivers.stamping --stamper-mode reformer --stampers 0.6 --seed 1   # the red team of 1.3.0 §8
python3 -m drivers.stamping --decline-awards 0.25 --stampers 0.6 --seed 1    # the red team of 1.5.0 §8: careful actors that offer for nothing
```

Drivers hold a `drivers.view.Public`, not the `World`: that class lists the operations a driver may
call. A driver that needs something not on it has found a conformance bug or a design question.

Results are kept (`drivers/results.py`): the runner writes what it printed to `results/tests/<commit>.txt`
(one file per commit, `-dirty` when the tree differs from it); every run writes
`results/runs/<run-id>/` with `manifest.json` (engine commit, params, declared operations, outcome),
`metrics.csv` and `fingerprint.json`. A sweep (`drivers/sweep.py`) puts every run and its summary under one
study folder, `results/studies/<study>/<sweep>/runs/`, so a study is one directory. Commit the ones that matter. Results are written by the code and
read by people; the suite and the engine stay the authority — never edit a result to match.

Any other result is a regression — including an XPASS. The 26 expected failures each have a stated
reason in `run_tests.py` (`EXPECTED_FAIL`, with `EXPECTED_FAIL_PARAMS` naming the parameter runs inside a
mixed test): one original (a single-answer ⊥ appeal), four superseded by the reviewer-view contract,
nineteen on the withdrawn audit-reopening path, one superseded by design revision 1 (it pinned the
1.0.1 deposit through the human's budget; its principle is re-asserted in `test_v11`), one superseded by
design revision 2 (it pinned Ω's cold-start float at 20; Appendix A now says 300). They are strict in both entry points: an expected
failure that passes means a withdrawn path is admitted again, and the run fails.

## Change discipline — spec §19, and the one rule that matters most

Classify a finding before acting on it:

| Finding | What it warrants |
|---|---|
| The engine misapplies a rule, or a refused action has effects | Fix the engine, add a regression test. **The rules do not move.** |
| Two active rules demand contradictory outcomes | The smallest explicit rule decision, versioned and labelled as a design revision |
| A workflow that would be useful but is not offered | A proposal for a later design revision — not an obligation to support it now |
| A strategy performs badly, or an incentive looks wrong | An evaluation under the fixed rules — not a rule change |
| The consolidated wording says more or less than the decisions | Errata (as in v1.0.1 Appendix E) |

A conformance pass may change *how* a rule is applied; a change to *what participants may do* is a
design revision and is read on its own before it is implemented. v0.9 broke this once (an interface
finding answered with a state-machine expansion); the next review found sixteen consequences and the
change was withdrawn, not repaired. Do not repeat it.

While building strategy runs, the baseline stays frozen between revisions. Drivers live in
`agentic_sim/drivers/`, use only the public operations of `World`, and never reach into engine internals.
A design revision is a release candidate (`-rc.N`, not in force) until accepted; then the engine is
changed to it, the goldens are re-pinned once at the implementing commit, reviewer tests that pinned the
old figures become expected failures with that reason and their principle re-asserted, and the text is
consolidated into one standalone spec with the accepted revision kept verbatim in `spec/design_revisions/`.

## Conventions in `agentic_sim`

- Every action is validated whole before anything is recorded or moved. A refused action changes
  nothing — tests assert this against full world snapshots. Keep it that way for any new operation.
- Twenty-five invariants run after every tick (`sim/invariants.py`). A failing invariant is an engine
  bug or a spec contradiction, never a property of a strategy. Two entry points, one set of
  predicates: `check_all` is the full audit from genesis (what tests call; scheduled in a run by
  `Params.full_check_every`); `check_tick` is what `advance` runs, the same predicates over the
  working set — cases and reviews that can still change, plus anything touched since the last tick.
  `tests/test_perf_equivalence.py` holds the proof that they agree and pins the engine's History head
  (re-pinned once for 1.1.0, since settlement changed; once for 1.2.0, since the reserve and the
  scenario — which now plants work — changed; once for 1.3.0, since membership and the fund changed; once
  for 1.4.0, since the roll became an obligation and troops are summoned; once for 1.5.0, since the reserve counts refused
  demand and the uplift paid changed; once for 1.6.0, since the clock pays rebates, Ω backs the fund, the reserve
  seats the queue and panels need a determined record). Keep new invariants in that shape: a predicate
  over an explicit scope.
  The per-tick check is not configurable: `advance` always runs it. `full_check_every` only adds
  the full audit on a cadence (0 = not scheduled; runs call `check_all` at the end), and
  `record_dir` only moves where the record is stored. `python3 run_tests.py --record` runs the
  whole suite in record mode as the storage layer's conformance check. The per-tick check is the
  incremental audit; the full audit is from genesis by definition, so scheduling it makes a run
  quadratic — strategy runs use the per-tick check plus one final `check_all`.
- The engine keeps every case and review ever created in `cases` and `reviews`, and a working set
  (`_live_cases`, `_live_reviews`) that the tick loop and `check_tick` read. A settled case leaves
  the working set and comes back through `_dirty_cases` when touched again. New engine code that
  mutates a case must do so through an operation that logs to the case or moves money on its
  account; that is what marks it dirty.
- With `Params.record_dir` set, the record lives on disk (`sim/record.py`): the History and the
  event copy are journals written through to files, and settled cases and reviews are paged out
  to archives, so RAM holds the working set. `w.cases[k]` makes an object resident (for code that
  may change it); `peek` and iteration give a read-only copy without pulling the archive in — the
  invariants use `_peek`, and new audit code must too. `check_all` streams the record in chunks.
  `tests/test_record_mode.py` proves the fingerprint is identical to the in-memory run and that
  the chain re-hashes from the file alone. Without `record_dir` nothing in `record.py` is used.
- Reviewer test files (`tests/test_review*.py`) are kept **verbatim**. Never edit one to make it
  pass; if a reviewer test must fail, add it to `EXPECTED_FAIL` with the reason, and mirror it in
  `tests/conftest.py`.
- No strategies in the engine. Every bid, verdict, appeal, audit roll, ruling and human action is
  injected by the caller; `sim/strategies.py` holds Protocols only.
- Defaults are in `sim/params.py` and spec Appendix A. Moving a default is not a design change;
  changing a rule is.
- The engine has no bid registry, no selection and no audit roll: `award` takes the chosen actor,
  and `p_audit` per reviewer is maintained but never rolled. Offers, S_θ with λ and the κ tie band,
  and the audit roll are the driver's — by design. A driver that skips the roll or reads `p_audit`
  dishonestly produces an implementation effect, not an economic one (spec §18.2).
- There is no enforced read-only facade on `World`; "public operations only" is a convention. Put a
  thin read-only view in `drivers/` so the rule is checkable.
- The `History` hash chain in `sim/ledger.py` is the authoritative record; wallet events and case
  logs are copies that invariant I16 checks for membership and order.
- The deposit is two pots (1.1.0 §4.3): the case pool's `deposit` field is the expense allowance φ^E
  (the 1.0.1 name is kept, reviewer tests read it) and `fee_pot` is φ^F. Expenses come from the
  allowance only; fixed fees `w_r · f_fee` from the pot; a nested case's reviews draw on its root's
  pool; the cross-pot step and the refund happen only at tree closure (`_maybe_close_tree`), and I10
  admits exactly those post-vesting movements by the event's note (`"nested …"`, `"tree closure…"`).
  I19 checks the pots per tick. A root with open pots stays in the working set until its tree closes.
- The loop's own clock (1.2.0 §7.6, §11.2, §12.2): `create_plant(truth, B)` builds a case in the submitted
  state from two system wallets (`PLANT_REQ`, `PLANT_ACT`) funded by Ω and swept back to Ω at closure, with
  the sealed marker in the History; a plant's initial verdict is adjudicated against its truth at once
  (`_adjudicate_plant`), every challenge operation refuses a plant, and its grade is `plant`. An actor's
  plant record is two trailing windows (`plant_bad`, `plant_good`); `duty_eligible` / `panel_eligible` are
  checked in `_eligible` for every assignment and in `_rotate`, which also readmits, removes the
  ineligible when their review completes, fills to `X_t` or shrinks to it, and counts the eligibility
  shortfall. The dial is read once per period in `_maybe_end_period` (before rotation) and sizes `pi_t`,
  the applied audit odds (`Actor.p_eff`, what a driver rolls), `X_t` and ω; `plants_due()` is what the
  rate calls for and the driver supplies. I20 and I21 are per tick; I9 is `min(X_t, eligible)`. The
  reviewer's view carries no actor. A still-failing record at the end of a suspension readmits on
  probation until the next plant (`_rotate`, §11.2) — the implementer's reading, confirmed as the rule by
  patch 1.2.1 and restated by 1.3.0.
- Inspection is membership (1.3.0 §5.2, §11.2, §12.1, §12.2): `award` refuses an actor that is suspended
  or on probation (`Actor.is_member`) and records `Case.member_at_award`; after `T_susp` a suspended actor
  is a probationer (`probation`) — initial reviews only, `p_eff` pinned at 1 (`Actor.pinned`, also for an
  undetermined newcomer; the §8.3 update does not run while pinned), re-checked at every plant
  (`_check_record`: any failure re-suspends; readmission on the trailing record with `since_susp ≥ n_min`).
  `_rotate_membership` holds two kinds of seat: member seats (`World.member_seats`, sized each period on
  applied audit odds plus the challenge rate) and initial seats, probationers first (an idle member in an
  initial seat makes room), members up to the cap `_member_cap(E_t)`, the panel floor min(V_max − 1, E_t)
  bounded by availability, turns refilled by kind. The duty fund is the wallet `DUTY_FUND`: `award` sends
  (m − 1) ω₀ B there, the settlement batch pays it out by role weight as `Review.uplift`. A plant funds its
  pots only (`net_plant_capital`): no escrow, no guarantee lock; I15 exempts it. I22, I23 per tick.
  `Params(membership=False, duty_fund=False, net_plant_capital=False)` is the 1.2.1 engine
  (`drivers.stamping --rules 1.2.0`); `test_v12` asserts it. Two implementer's readings, confirmed as rules
  by patch 1.3.1 (§12.1): the members' cap never falls below the reserve floor V_max + 1 (`_member_cap`;
  the literal ⌈E_t/2⌉ breaks every six-actor world at tick 0), and an outgoing probationer with no free
  probationer stays rather than hand its seat to a member who would yield it back.
- The orchestrator's troops (1.4.0 §7.7, §8.3, §12.3): `roll_audit(cid)` records a rolled audit as an
  obligation (the shape of the vacated-audit hold: `audit_obligation`, `open_items`); the driver rolls on
  `audit_odds(cid)` and never drops a roll; a human ruling ends the obligation. `_summon_troops` runs at
  step 5 after the seating: a required seat unfilled for `w_R` seating steps with no free eligible on-duty
  reviewer (`_free_eligible_reviewer`), or a root request unawarded for `w_A` with no free fundable member (since 1.7.1: the root requests past `w_A`
  beyond the free fundable members, oldest first — the bullet below)
  and β ≥ B̄ (`mean_awarded_price`), gets a troop when the fund can carry cost plus bond (`_fund_can_carry`,
  with Ω's advance up to `A_T`); the audit of a troop reviewer's approval of a troop's delivery
  (`market_audit_only`, odds 1, recorded by the engine at the verdict) is never summoned for and is counted
  as held. A troop is a single-use id `T<n>` whose ledger operations resolve to `DUTY_FUND` through
  `Ledger.aliases`; it is not an `Actor` (every reviewer lookup is guarded), claims no emission or uplift
  (excluded from the batch's weights), accepts every verdict on its delivery at the verdict (final N at
  once), resumes its seat on a resubmission, and is recorded in `World.troops` and the History. The fund
  repays the advance before and after each batch and pays uplift only from above `R_T` (the trailing peak
  troop capital). I24, I25 per tick; I9, I22, I23 amended (the fund reconciles against `fund_flow`, every
  recorded flow into and out of its wallet). `Params.troops=False` is the 1.3.0 engine with the obligation
  held (`--rules 1.3.0`). A troop reviewer's approval of a member's work carries `min(1, m p_floor)` — a
  default chosen at implementation, Appendix I. `Params.dial=False, pi0=0, p_start=p_cap=0.5, Omega0=20` is the 1.1.0 engine's behaviour
  (`drivers.stamping --rules 1.1.0`).
- The reserve is sized to the need (1.5.0 §12.3, I23): `_summon_troops` accumulates, inside one pass, the `need` of every
  summons the fund refused for funds (`_pass_refused`; a panel short of both seats counts both; a request priced below B̄,
  a requester that cannot pay in, or a full path adds nothing) and reads it with the capital live troops hold at the
  pass's end — `troop_demand_held`, `troop_demand_refused`, `troop_demand_now` = D_s. `R_T` is `troop_demand_peak`, the
  running maximum of D_s over the current period, reset at the period's end (before the same tick's seating) to the
  capital still held — the standing demand; `troop_demand_peak_refused` is the refused part of the peak. The uplift
  check is unchanged (unlocked balance above `R_T`). The period record carries `demand_peak`, `demand_peak_refused`,
  `demand_last`. I23 checks `R_T` ≥ capital held and ≥ D_s. `Params.reserve_demand=False` is the 1.4.0 reading (the
  larger of this and the previous period's peak capital carried) — `drivers.stamping --rules 1.4.0`. The driver
  attributes each probationer's false approval by route (audit upheld / audit rejected and ruling overturned) and, on
  the upheld route, by the auditor's kind at the time (troop / member never suspended / suspended later / readmitted
  before), classified after the run from its own suspension log; `--decline-awards` is the 1.5.0 red team.
- Auto-scale (1.6.0; `Params.service_clock, omega_backs_fund, seat_the_queue, panel_determined, reserve_periods`, all on;
  `--rules 1.5.0` turns them off together). The clocks run in the summons pass (`_clock_runs`: a live root, not a plant,
  β ≥ B̄ while unawarded) and stop once, in `_initial_verdict`, `_finalize_N` or `_vest` (`_stop_clock`: lateness past
  `T_s`, rebate `min(r_s·late, B)` paid Ω → requester from above the plant reserve or appended to `omega_liabilities`;
  `_service_omega_liabilities(min_age)` runs before the pass with a period's age and after it with none; the serviced
  note is I10-exempt). `_omega_available()` is Ω's unlocked balance above `_plant_reserve()` (π_t × the period's initial
  rate × (φ^E+φ^F) × `plant_reserve_life`, 15 — the implementer's reading; 0 = the text's ticks remaining) and replaces
  A_T's room in `_fund_can_carry`. `_summon_troops` runs the review seats first, then the awards, oldest case first, with
  `_priority_violation` for I26; `_summon_delivery` checks fund + Ω available ≥ cost + G + 2(c_T + G^V) and draws the
  delivery's own shortfall. `_reserve_target()` = max(X_t, waiting initial + waiting panel + the period's initial rate),
  taken at every rotation (`_x_target`; `_waiting_reviews()` by kind); `_rotate` and `_rotate_membership` fill to it,
  member seats at least the panel seats waiting within the cap (`duty_cap_frac`). `Actor.panel_eligible` requires
  `len(plant_bad) ≥ n_min` once `first_plant_adjudicated_at` is set (`_adjudicate_plant`). `R_T` over two periods
  (`troop_demand_peak_prev`). The period record carries on-time, late, lateness, rebates, liabilities, Ω's minimum, the
  plant reserve, troop panel summonses. I26 per tick; I9, I22, I23, I24 amended. The driver writes the rating, Ω and
  seat columns and offers `--duty-cap`, `--t-s`, `--plant-reserve`, `--beta-low/--beta-low-share`.
- The state's earnings (1.7.0; `Params.troop_account`, on; `duty_cap_frac` 2/3; `--rules 1.6.0` turns the flag off and the cap
  to half). The troops' wallet is `TROOP_ACCT` (`World.troop_wallet`; troop ids alias to it; the carry check, the advance, its
  repayment, the delivery check, I23's lock reconciliation and `fund_flow` follow it); `DUTY_FUND` is the uplift fund — the
  raised tax in and nothing else, its whole unlocked balance paid as uplift at the batch (I23: it equals `fund_in − fund_out`
  and holds no lock). After the batch's second `_repay_advance`, `_pay_troop_surplus` sends the troop account's unlocked balance
  above `R_T` to Ω (`troop_surplus_paid`, period `troop_surplus`); under the flag `R_T` is the 1.4.0 reading — the two-period
  peak of `_troop_capital_now()` — and I23 keeps `R_T ≥ held`, retiring `R_T ≥ D_s` (the demand readings stay in the record).
  Ω's record by source: `omega_fee_income` (`_fee_income` at every base-fee transfer), `advances_made/repaid`, the period's
  `omega_income`, `omega_advances`, `omega_out` (rebates paid, liabilities paid, plant capital out and swept back),
  `uplift_fund`. A troop reviewer's cost is reimbursed from the allowance like any reviewer's, so a review seat nets its fee
  (the accepted text's "nets nothing" is corrected in Appendix L). `test_v13`–`test_v16` are pinned to the merged fund and
  the half cap. Driver: `--accounts`, `--omega-rate`, `--r-s`, `--duty-cap` defaulting by the rules; the account, surplus and
  income columns.
- The award summons is per request (patch 1.7.1, §12.3; a conformance correction, no flag). `_summon_troops`'s award pass gathers
  the root requests past `w_A` in creation order, counts the free fundable members at the market price (`_free_fundable_members`),
  leaves that many of the oldest to the market and summons for the rest, oldest first, each through the unchanged delivery
  check; readings `awards_left_to_members` (summed; in the period record and `view.troops()`), `awards_waiting_now`,
  `members_free_now`; driver columns `awards_waiting_w_a`, `members_free_at_seating`, `awards_left_to_members`. 1.4.0–1.7.0
  read the rule per tick (one free member blocked every award summons that tick — run 9's 50/50 collapse). `test_v171` pins
  it; goldens re-pinned once at the correcting commit; the `--rules` controls carry the correction too (as the 1.4.0 audit
  obligation did), so run 8's and run 9's controls are no longer reproduced to the unit.
- Money is checked by invariant I1 (conservation) — never silently create or lose credits.

## Vocabulary (spec Appendix C has the full notation)

F / N / P / ⊥ — fulfilled / not fulfilled / partially fulfilled / cannot assess. P and ⊥ are
responses to a submission, available only on the first review of an unrevised submission.
Pending — approved or appeal admitted, window open, actor's capacity released. Suspended — a challenge
or audit holds the case. Vested — financial finality. Ω — the orchestrator's operating account, a
revolving float. ρ reliability, κ duty credit. G guarantee, G^V reviewer bond, D court fee,
K reasonable-cost cap, φ = φ^E + φ^F verification deposit (expense allowance + fee pot), f the ordinary-review
fee (appeal and audit 1.5 f), β price ceiling, v_t credit value = Res_t / M_t. Plant — a case whose
fulfillment the orchestrator knows by construction (bad / good); π_t plant rate, β_P bad share, F̂_t the
reserve's bad-plant approval rate against F*, m_t the effort multiplier, X_t the sized reserve, â / r̂ an
actor's bad-plant approval and good-plant rejection rates against θ_panel / θ_duty, T_susp the suspension. Member / suspended / probationer — an actor's standing in the market (1.3.0); E_t the
members eligible for duty; duty fund and uplift — the dial's raised tax and its payout to settling reviews.
Troop — the orchestrator's own reviewer or deliverer, summoned for one seat (1.4.0); ε_T its declared error
rate; w_R, w_A the seat and award windows; c_T, c^D_T its costs; B̄ the trailing market price; R_T the fund's
troop reserve; A_T Ω's advance cap; troop-ticks, troop shortfall, held for the market's audit — the readings. D_s the troop demand at a seating (held plus
refused for funds); since 1.5.0 R_T is its peak over the period, since 1.6.0 over the current and the previous one.
Service clock, T_s, r_s — a root request's ticks from posting to its first verdict, the target, the rebate a tick late;
the network rating (on-time share, lateness, rebates, Ω's liability); the plant reserve; the reserve target; a
determined record (≥ n_min bad plants adjudicated) — 1.6.0.
Uplift fund and troop account — the duty fund restored to 1.3.0's shape, and the troops' separate wallet whose surplus above
R_T (since 1.7.0 the two-period peak of capital held) is Ω's; Ω's income by source — base fee, troop surplus, beside its own
money's flows and its outflows — 1.7.0.
"Ruling" has two senses: the orchestrator rules on splits inside the procedure; only a human
*overrides* it (spec §15.2).
