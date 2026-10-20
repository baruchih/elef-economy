# Review of "The learned red team — a brief"

**Date:** October 20, 2026 · **Text reviewed:** `red-team-brief.md` (October 20), kept verbatim as `docs/red_team_brief.md` · **Against:** the 2.5.0 text in force (§8.3, §14, §18.2), the engine at `44ef6e47` (`sim/engine.py`, `drivers/view.py`, `drivers/stamping.py`), LeWorldModel (arXiv 2603.19312, `lucas-maes/le-wm`, MIT) and stable-worldmodel 0.1.1 (`galilai-group`), this machine · **Reviewer:** the implementer.

**Classification under §19.** A study brief: evaluations under the fixed rules. Nothing in it moves a rule; a win is a finding for a design revision drafted afterwards, as the brief itself says (§2.2). It is reviewed for implementability — can the learners be built as drivers under the conventions, with what, at what cost — and for its facts.

**Verdict. Implementable as it stands, with one correction of fact, four readings and a build plan that needs five decisions before anything is installed.** The brief's order (Q2 alone first; a win on Q2 halts) is right and is kept.

## The correction

- **The account's filename.** The brief cites `economy-2x-consolidated-account.md`; in this repository it is `docs/economy_2x_account.md` (the revised version adopted the same day), with its review beside it.

## Readings

1. **"LeWorldModel agents" is a world model and a planner, not a policy learner.** LeWM learns the dynamics of a latent state from offline trajectories (next-embedding prediction plus SIGReg) and acts by model-predictive control: the Cross-Entropy Method samples action sequences, rolls them through the predictor, and picks the cheapest under a cost. In the paper the cost is distance to a goal embedding. The brief's reward — own real wealth — has no goal embedding, so the cost must be learned: **a wealth head on the latent** (the change in the actor's real wealth over a step), trained with the world model, and the planner's cost is minus the predicted sum over the horizon. The brief leaves the architecture to the implementer and this is the adaptation; it is named in every report. The platform supports it directly: a model is anything with `get_cost(info, candidates) → cost`, state-only environments are supported (`add_pixels=False`), discrete actions have their own solver (`CategoricalCEMSolver`), and le-wm's `Embedder` already embeds low-dimensional vectors — no vision transformer anywhere.

2. **The decision step is not the tick.** LeWM plans five steps ahead; the sleeper's payoff (Q1) runs over periods of 75 ticks. One environment step is therefore **one decision event** — a review assignment to answer, a free tick with a request to bid on, a delivery due, a period boundary for a customer — with the engine's tick loop and the hand-written population running between events; the observation carries the slow state the plan needs (own audit odds, standing, ticks since admission, the period's position), so a stamping decision is a function of state, not of a long horizon. Horizons of 8–16 decisions span hundreds of ticks. Variants (a tick step with frameskip) are allowed and named.

3. **The truth channel is the driver's convention, and the learner gets it only by paying.** The engine has no notion of work quality: a task's truth is the driver's (`Task.fulfilled`, drawn at the fail rate), a careful reviewer learns it with accuracy *a* for a care cost of 2–3 (`Stamping.verdict`), a stamper answers F for nothing. The learner **never reads `Task.fulfilled`**; its *care* action buys the noisy signal at the cost, as the careful disposition does, and its verdict is then its own. The deliverer's quality dial (Q3) is likewise the driver's: *good* work spends the effort cost c_D at submission (`spend`) and sets the truth true; *bad* work sets it false and spends — **a decision below** — nothing (the strongest adversary; a lowballer that never worked) or a fraction. The learner also never drops the audit roll (the roll stays in the driver's hands, not the learner's) and reads only its own `p_effective`.

4. **Q2's leak surface, as the record shows it.** The reviewer's view (`ReviewView`, §14) is a function of case fields that exclude the actor and the plant marker: review and case ids, `t_submit`, the review's deadline, the bond, the cap K, `resumed`, `is_nested`, the question and the responses available. A plant's view carries nothing a case's does not — *by field*. What a driver also knows is the clock and its own history, and three candidates for a separation exist in the construction, not the fields: (i) a plant is created in the submitted state and assigned the same tick (`plants_due` → `create_plant` before the tick's assignments), so `t_assign − t_submit = 0` for every plant, while a real case waits in the queue when seats are short; (ii) a plant is priced at the published P_t exactly, a real case at a bid — the view carries no price, but the bond and cap are indexed at the case's lock and may differ in the second decimal; (iii) the plant rate's rhythm (π_t × the period's initial rate) against the arrival of real work. The learner is free to find these or anything else; the ablation (§4 Q2) removes `t_submit`, then the bond and cap, then randomises the plants' seating delay, until the separation vanishes. If (i) is the leak, the fix is in the plants' seating or the view's `t_submit` — a revision, drafted before anything else runs, as §8 says.

## Facts checked

- The identity persists through suspension and probation; departure archives the name forever and re-arrival is a fresh name with the float (2.3.0) — the brief's §3 is right.
- Every observation the brief lists is in the public view (`market`, `troops`, `bank`, `service`, `dial`, `membership`, `p_effective`, the actor's own wallet through `wealth`); nothing per other actor is needed or read.
- Every action is a public operation: bids through the driver's selection (`award` is the orchestrator's), `submit`/`spend`, `complete_review` with its cost, `respond` (accept/appeal), `post_nested`/`judge_nested`/`cancel_nested`, `arrive`/`depart`, `post_root`/`raise_ceiling`/`withdraw_unawarded`.
- Seeds: runs 12–19 used seeds 1–20; the control on 21–40 is twenty runs a cell, cheap. Seed noise in the notes has been read as two standard errors over the twenty; the stop rule uses that.
- The suite stays dependency-free: `python3 -S run_tests.py` must keep passing, so the learner is a separate package that the engine, the drivers and the runner never import.

## The build plan (the implementer's, for acceptance)

**Where.** `agentic_sim/redteam/` — `env.py` (the decision-event Gymnasium environment around the stamping driver, one actor's slot delegated to a policy; registered as `swm/Elef<Role>-v0`), `obs.py` (the observation vector from the public view and the actor's own history, with a named field list for the ablations), `collect.py` (offline trajectories from the hand-written dispositions plus ε-exploration on seeds 1–20), `model.py` (le-wm's `Embedder` + `ARPredictor` + SIGReg, vendored under MIT with attribution, plus the wealth head), `train.py`, `plan.py` (`get_cost`, `CategoricalCEMSolver`, `WorldModelPolicy`), `run_q.py` (a question's cells on seeds 21–40 with the control, writing runs in the established form). Results under `results/studies/rt-Q2/…` with notes as before.

**Environment on this machine.** Apple M4 Max, 14 cores, 36 GB; Python 3.13 system with miniconda, no torch, no gymnasium. A conda environment `elef-redteam` at Python 3.11 with torch (MPS), gymnasium and `stable-worldmodel==0.1.1`; nothing installed into the project's Python. LeWM's own training is hours on one GPU for 10,000–20,000 episodes of 200 steps; our offline sets are 20 seeds × a few behaviour policies × ~1,000 decisions, two orders smaller — minutes on MPS, so the budget is in rollouts, not epochs.

**Budget and stop rule, recorded per question.** Offline: 20 seeds × 4 behaviour policies (careful, stamper, careful with ε = 0.2 random actions, uniform random) = 80 runs. Online: up to 10 iterations of plan-and-collect on seeds 1–20 (the platform's online-learning path). Evaluation: seeds 21–40 against the careful control at the same cost and split. No-win: the learner's lifetime real wealth within two standard errors of the careful's over the twenty. Win: above it, reported at once.

**The five decisions before anything is installed.**
1. The conda environment at Python 3.11 beside the project's Python (torch with MPS; stable-worldmodel 0.1.1).
2. Vendoring le-wm's `module.py`/`jepa.py` (MIT) into `redteam/lewm/` with attribution, rather than depending on the repository.
3. The decision-event step as the environment's step (reading 2), a tick step with frameskip as the named variant.
4. Bad work costs the deliverer nothing (reading 3) — the strongest adversary; a fraction of c_D as the named variant.
5. The wealth head as the planner's cost (reading 1), with a bootstrapped terminal value as the named variant if the horizon proves short.

**Recommendation.** Accept the brief as the red team's charter; decide the five; then Q2 alone, as §8 orders.
