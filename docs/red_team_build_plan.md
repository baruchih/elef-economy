# The learned red team — build plan and decisions

**Prepared:** October 20, 2026 · **From:** the implementer · **For:** the design reviewer · **Status:** the brief (`docs/red_team_brief.md`) is accepted as the red team's charter; the five build decisions below were taken by Baruchi on October 20; nothing is installed yet — the build starts on this plan.

---

## 1. What is being built

A learned actor that lives inside the 2.5.0 engine as a driver, under the drivers' conventions, and tries to end richer than a careful actor of the same cost at the same split by being unfaithful. Its tool is **LeWorldModel** (Maes, Le Lidec, Scieur, LeCun, Balestriero, arXiv 2603.19312): a joint-embedding world model trained from offline trajectories with two losses — next-embedding prediction and SIGReg — and planned by model-predictive control with the Cross-Entropy Method. It runs on **stable-worldmodel 0.1.1**, which supplies the environment wrapper, dataset collection, the solvers and the evaluation loop.

Three adaptations, all the implementer's and named in every report:

- **The cost is a learned wealth head.** LeWM's planner minimises distance to a goal embedding. The red team's reward — the actor's own lifetime real wealth, $W \cdot P_0/P_t$ — has no goal, so a head on the latent predicts the change in the actor's real wealth over a step, and the planner's cost is minus the predicted sum over the horizon.
- **The step is a decision event, not the tick.** LeWM plans five steps ahead; the sleeper's payoff runs over 75-tick periods. One environment step is one decision — a review assignment to answer, a free tick with a request to bid on, a delivery due, a period boundary for a customer — with the engine and the hand-written population running between decisions. The observation carries the slow state a plan needs (own audit odds, standing, ticks since admission, the period's position). Horizons of 8–16 decisions span hundreds of ticks.
- **Truth is bought through care only.** The engine has no notion of work quality; a task's truth is the driver's hidden flag. The learner never reads it. Its *care* action pays the care cost (2–3 credits) and receives the careful disposition's signal at accuracy *a*; stamping is free and blind. The deliverer's quality dial sets the flag: good work spends the effort cost c_D; bad work spends nothing.

## 2. The five decisions, as taken

| # | Decision | Taken |
|---|---|---|
| 1 | A conda environment at Python 3.11 beside the project's Python (3.13), with torch on Apple MPS, gymnasium and stable-worldmodel 0.1.1. The engine, the drivers and the test runner never import any of it; `python3 -S run_tests.py` keeps passing unchanged. | ok |
| 2 | le-wm's two model files (`module.py`, `jepa.py`; MIT) vendored into `agentic_sim/redteam/lewm/` with attribution, rather than a dependency on the repository. | ok |
| 3 | The decision event as the environment's step; a tick step with frameskip is the named variant. | ok |
| 4 | Bad work costs the deliverer nothing — the strongest adversary; a fraction of c_D is the named variant. | ok |
| 5 | The wealth head as the planner's cost; a bootstrapped terminal value is the named variant if the horizon proves short. | ok |

## 3. The learner's contract (the brief's §2, made concrete)

- **Reads:** `drivers.view.Public` only — `market`, `troops`, `bank`, `service`, `dial`, `membership`, its own `p_effective`, its own wallet through `wealth`, and the `ReviewView` of its own assignments. Nothing about any other actor by name; no engine field.
- **Acts:** through the public operations only — offers into the driver's selection, `submit`/`spend`, `complete_review` with its cost, `respond`, `post_nested`/`judge_nested`/`cancel_nested`, `arrive`/`depart`, `post_root`/`raise_ceiling`/`withdraw_unawarded`.
- **Never:** drops the audit roll (the roll stays in the driver's hands, outside the learner's action space) or reads any `p_audit` but its own.
- **Identity:** one actor through suspension and probation; departure archives the name; re-arrival is a fresh name with the float (2.3.0).
- A learner that reaches past the view produces an implementation effect; its result is discarded (brief §2.1).

## 4. Layout

```
agentic_sim/redteam/            a separate package; the suite never imports it
  env.py        the decision-event Gymnasium environment around the stamping driver, one actor's slot delegated to a policy;
                registered as swm/Elef<Role>-v0 (Reviewer, Worker, Child, Parent, Customer)
  obs.py        the observation vector from the public view and the actor's own history — a named field list, so an ablation
                is "drop these names"
  collect.py    offline trajectories on seeds 1–20 from behaviour policies: careful, stamper, careful with ε = 0.2 random
                actions, uniform random
  lewm/         module.py, jepa.py (MIT, lucas-maes/le-wm), with attribution
  model.py      Embedder → ARPredictor (actions one-hot through AdaLN) → SIGReg; the wealth head on the latent
  train.py      the training loop (stable-worldmodel's loader; windows of history_size decisions)
  plan.py       get_cost over candidate action sequences; CategoricalCEMSolver; WorldModelPolicy with PlanConfig
  run_q.py      a question's cells on seeds 21–40 with the careful control, each run a folder in the established form
results/studies/rt-Q2/ … rt-Q7/, rt-stability/   runs, summaries, notes-for-reviewer as before
```

The machine: Apple M4 Max, 14 cores, 36 GB. LeWM trains in hours on one GPU for 10,000–20,000 episodes of 200 steps; the red team's offline sets are 20 seeds × 4 policies × about 1,000 decisions — two orders smaller — so training is minutes on MPS and the budget is in rollouts, not epochs.

## 5. Budget and stop rules, per question

- **Offline:** 80 runs (20 seeds × 4 behaviour policies), 1,000 ticks each, in the honest 60/40 world with the pool of twenty (run 16's cell) unless the question says otherwise.
- **Online:** up to 10 iterations of plan-and-collect on seeds 1–20.
- **Evaluation:** seeds 21–40, the learner against the careful control at the same cost and split; the control is run on the same seeds.
- **No-win:** the learner's lifetime real wealth within two standard errors of the careful's over the twenty evaluation seeds after the budget — reported as such.
- **Win:** above it — reported at once; a win on Q2 halts the study.
- Every run: manifest (engine and driver commits, params, declared operations), metrics, fingerprint; every per-tick check and the final audit passed, or the run is not reported.

## 6. Q2 first, alone — can plants be told apart?

**Setup.** One learned reviewer on duty in the honest population, scored on reviews only (review income less forfeits), receiving plants at the ordinary rate. Its actions per assignment: care or not; the verdict.

**The surface it may find.** The reviewer's view is a function of case fields that exclude the actor and the plant marker — by field, a plant's view carries nothing a case's does not. The construction is where a separation could live:

1. A plant is created in the submitted state and assigned the same tick, so its gap from submission to assignment is always zero, while a real case queues when seats are short.
2. A plant is priced at the published P_t exactly, a real case at a bid; the bond and the cap are indexed at the case's lock and may differ in the second decimal.
3. The plant rate's rhythm against the arrival of real work.

**The ablation order** if a separation appears: drop `t_submit` from the observation; then the bond and cap; then randomise the plants' seating delay in the driver; until the separation vanishes. The field that closes it is the finding.

**What a win means.** The gate is blind; the fix is in what the plants' construction or the view leaks, drafted as a revision before anything else runs.

## 7. Then, in order

Q1 the sleeper · Q3 the selective cheat · Q4 collusion through the blind view (two learners, a shared reward) · Q5 the delegation chain (a learned child at σ 0.8, then a learned parent) · Q6 money games · Q7 the customer · the stability track last (a learned population bidding; the price as the reading; not a red-team win).

## 8. What comes back to the reviewer

For each question, notes in the established form, answering in this order: did it win (the numbers of brief §1); what it does, in words, read from behaviour; what it cost the loop (false approvals, suspensions and readmissions, the lagging auditor, the state's share); what rule it points at, if any. The reviewer records each as run 2N and drafts a revision only on a win.

## 9. Risks named now

- **Horizon.** Five planning steps is the paper's; decision events stretch it, but a strategy whose payoff is a whole period away may still be beyond the planner — the terminal-value variant (decision 5) is the fallback.
- **Low-diversity data.** The paper notes SIGReg weakens on simple, low-dimensional environments with little diversity; the ε-random and uniform behaviour policies are there to widen the data, and the regulariser's weight will be swept and recorded.
- **Describability.** A planner's behaviour is read from its rollouts, not its weights (brief §2.6); every report carries the decision traces the description rests on.
