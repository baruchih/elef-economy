# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 2 — specification 1.2.0-rc.3: the loop's own clock

**Project:** ELEF / Agentic Economics  
**Version:** 1.2.0-rc.3 — a release candidate, not yet in force. rc.1 (October 17) was the proposal as first sent; rc.2 settled the eight points of the first implementation review [I3]; rc.3 settles the three the settlements raised [I4] — the plant record persists through suspension, one rule for a newcomer's audit odds, eligibility checked at assignment with a suspended actor leaving duty whether or not a replacement exists — and five smaller points. rc.2 settled, from [I3]: the actor leaves the reviewer's view, the reserve may run short rather than seat the negligent, the plant record is defined on the quantity the clock measures, newcomer plant-doubling is dropped, Ω's working capital and the audit cap are stated, and the hypothesis names its channels. On acceptance it becomes **1.2.0**, consolidated into one standalone text, and 1.1.0 moves to history. Semver as before: patch = wording, minor = design revision under §19, major = change of approach.  
**Prepared:** October 17, 2026 (rc.1–rc.3)  
**Supersedes:** 1.1.0 where this document speaks; everywhere else 1.1.0 stands unchanged.  
**Nature of this revision:** A **design revision** under §19 — the second since the freeze. It adds one mechanism with three parts (planted work, a plant record, an effort dial); makes two quantities endogenous that were fixed — the reserve size $X$ (§12) and the service fee $\omega$ (§4.1), both now scaled by the dial; changes the information contract of §14 by removing the actor's identity from the reviewer's view; changes two defaults (how newcomers are audited, and the audit-odds cap); labels one unlabelled sentence (§7.5); and states one design assumption that the baseline left implicit. It is read on its own before it is implemented.  
**Design assumption, stated:** **Humans do not intervene.** The loop cannot control whether or when a human complains, overrides, or even looks. Every mechanism in this revision works with no human action at all; human attention, where it comes, is a bonus the loop accepts and never relies on.  
**Status:** Proposed. Accompanied by the evidence that required it (§1) and the runs that test it (§8).

> **Money enters with requests. Truth enters with requesters — and, from this revision, with the orchestrator's own planted work.**
>
> **Care is paid for, not charged for.**
>
> **Verification effort is a living thing: it rises when the record says the economy is in danger and eases when it is not.** *(new)*

---

## 1. Why: what runs 2 and 3 found

Runs 2 and 3 — 1,295 runs under 1.1.0, every final audit passed — established four facts about the loop as it stands [S2]:

1. **Each direction of reviewer error has a natural challenger, and the loop is fair only when both are present.** The actor polices rejections (appeals, a ≈ 0.98); the requester polices approvals (disputes). With appeals alone, a careful reviewer's 5% false rejections are punished almost every time while a stamper's negligence is caught about 3% of the time, and stampers end richer (+200 per actor at 50/50, X = 8). With the requester disputing one bad result in four, careful ends richer by 489; break-even is a dispute rate of about **0.07**.
2. **Careful review pays only above an accuracy of about 92%** at that dispute rate. The evaluator's required accuracy, bracketed in the baseline, has a number.
3. **A stamper-majority reserve captures the loop, and nothing inside the loop recovers it.** At 10/90 every panel is stamper-majority: disputes fail (23 of 135 won), appeals against the careful minority succeed, only the minority's errors are ever adjudicated, their reliability ends *below* the stampers', and selection hands the stampers the awards (159 to 66). No dispute rate in the sweep recovers it. **Under capture, reliability ρ is itself corrupted**, because the panels that produce it are captured; any remedy that leans on ρ — a ρ floor for duty, panels chosen by ρ — entrenches capture rather than curing it.
4. **Bond size cannot carry deterrence.** At G^V = 20, about 7% of duty slot-ticks — a quarter of one slot on average — are held by actors who cannot fund the bond; reviews wait 4,500–4,700 review-ticks, awards go unfilled in some 600 ticks, vesting falls 4%. The reserve starves.

Two further facts shape the remedy. Every signal the loop produces — verdicts, overturns, dispute outcomes, reliability — is produced by the panel, so under capture the loop is blind to its own state. And the design assumption above removes the one external oracle the baseline implicitly leaned on: the human. **If neither the panel nor the human can be trusted to supply truth, the orchestrator must own some truth itself.** The October 14 proposal map asked exactly this: "for which claims do we genuinely know an audit answer?" The answer this revision gives: for the ones the orchestrator wrote.

**Classification.** A design revision motivated by strategy findings (runs 2–3), labelled and read on its own. It adds a mechanism; it does not alter any settlement, verdict, or challenge rule of 1.1.0.

---

## 2. The rules

### 2.1 Planted work — the orchestrator's own clock

**Rule.** The orchestrator may introduce into the review stream a **plant**: a case whose submission's fulfillment is **known to the orchestrator by construction**. A *bad plant* is known not fulfilled; a *good plant* is known fulfilled. A plant is created directly in the submitted state, attributed to a **plant requester** and a **plant actor** that belong to the orchestrator and whose wallets are the operating account's; it carries an ordinary award, allowance and fee pot, all funded by $\Omega$. It is assigned an initial reviewer exactly as any case is (§7.5).

**Rule — indistinguishability, and a change to §14.** A plant is indistinguishable from an ordinary case in the reviewer's view: same `question`, same `responses_available`, a submission drawn to look like the population's — and **no actor identity**. Under 1.1.0 the view carried the submission's actor; a plant actor named there would be known to every reviewer after the first revealed plant. This revision **removes the actor from the reviewer's view** (§14's table becomes: the request's terms; the submission's result, evidence, time of submission, and whether resubmitted; the question; the responses available; for an appeal or dispute, the assessment under challenge and its grounds). The reviewer judges the work, not the worker; a reviewer never needed the actor's name to decide whether the request was met, and not having it also closes a collusion channel — a reviewer can no longer recognise a friend's work — which the baseline brackets but does not have to invite. The orchestrator still knows the actor; so does the record. The plant marker is committed to the History at creation, sealed, and revealed at the plant's adjudication — its initial verdict — when the reviewer's bond moves or does not. Nothing a reviewer can observe before answering distinguishes a plant from real work: the view is a function of case fields that exclude the actor and the marker, and §7 makes that a test.

**Rule — adjudication by truth.** A plant has no challenge round: no audit is rolled on it, no appeal or dispute is admitted, no ruling is sought. At its initial verdict:

| Plant | Verdict | Outcome for the reviewer |
|---|---|---|
| bad | $\mathsf N$ | **stood**: fee and emission share at settlement; plant record +1 |
| bad | $\mathsf F$ | **plant failure**: bond forfeited whole and burned; no fee; expenses reimbursed as for any overturned review; reliability down; audit odds doubled; plant record −1 |
| good | $\mathsf F$ | **stood**: paid; plant record +1 |
| good | $\mathsf N$ | **plant failure**, as above — the mirror that catches false rejecters without anyone having to appeal |
| either | $\mathsf P$ or $\bot$ | **spent**: the plant ends with no plant outcome for the reviewer; the plant tests the verdict, not the response path |

A plant's verdict is adjudicated by its known truth the moment it is given; the plant then runs out its window and settles like any case — the reviewer is paid or not by the ordinary rule, the pots refund to $\Omega$. The reviewer learns that a case was a plant only after it has answered.

**Rule — the plant rate.** In each period a fraction $\pi_t$ of initial reviews are plants, with bad plants a fraction $\beta_P$ of them. $\pi_t$ is set by the effort dial (§2.3) and is **public**; which cases are plants is not.

**Consequence.** The **bad-plant approval rate** $\hat F_t$ — the share of bad plants approved in period $t$ — is a measurement of the reserve's negligence that no panel produces and no majority can paint. It is the clock the rest of this revision runs on.

**Limit.** A plant must be constructible: a submission whose fulfillment the orchestrator knows and a reviewer cannot tell from real work. That is easy where fulfillment is mechanical (tests, hashes, reproducible outputs) and hard where it is semantic. The mechanism's reach is therefore domain-dependent; this is a limit on where the loop can be deployed first, not on the loop.

### 2.2 The plant record — negligence measured where it cannot be hidden

**Rule.** Every actor carries a **plant record**: over its trailing $n_P$ bad plants and trailing $n_P$ good plants, its smoothed **bad-plant approval rate** and **good-plant rejection rate**,

$$\hat a_i=\frac{o^{\text{bad}}_i+1}{n^{\text{bad}}_i+2},\qquad \hat r_i=\frac{o^{\text{good}}_i+1}{n^{\text{good}}_i+2},$$

where $o^{\text{bad}}_i$ is the number of bad plants actor $i$ approved and $o^{\text{good}}_i$ the number of good plants it rejected. These are the individual counterparts of the clock $\hat F_t$ — the same quantity the dial measures for the reserve, measured per actor. A record is *undetermined* until the actor has judged $n_{\min}$ plants of the kind in question. A plant outcome also counts in $\rho$ as any stood or overturned outcome does.

**Rule — two tiers of eligibility.**
- **Panel eligibility** (appeal, dispute and audit reviews): $\hat a_i\le\theta_{\text{panel}}$ and $\hat r_i\le\theta_{\text{panel}}$. An actor whose record exceeds either may still take initial reviews but may not sit in judgment on a challenge.
- **Duty eligibility** (any review): $\hat a_i\le\theta_{\text{duty}}$ and $\hat r_i\le\theta_{\text{duty}}$. An actor whose record exceeds either is **suspended from duty** for $T_{\text{susp}}$ ticks. **Its plant record persists.** At the end of the suspension it is readmitted only if its record passes, and otherwise remains suspended for a further $T_{\text{susp}}$; on readmission its audit odds restart at $p_{\text{start}}$. Suspension affects duty only — the actor may still offer and execute work; its $\rho$ carries the plant failures into selection as it would any overturn.
- An actor with an undetermined record is eligible for both tiers.

**Consequence.** A suspended actor cannot wait its way back in: a full stamper at $\hat a=0.83$ passes nothing until it rejects bad plants — five rejections after four approvals give $(4+1)/(9+2)=0.45$ — so it is out until it changes behaviour. That change of behaviour is the actuator Hypothesis 2 needs; a cleared record would have readmitted every stamper with a clean slate for the ~50 reviews a record takes to re-form, leaving panels stamper-majority at about 70% strength indefinitely [I4].

**Rule — when eligibility is checked.** Eligibility is a property at **assignment and at rotation**. A record moves whenever one of the actor's plants is adjudicated, so an actor holding an assignment may cross a threshold mid-review: it completes its active review, whose verdict is adjudicated as usual, and **leaves duty when that review completes, whether or not a replacement is available** — this overrides §12's "the outgoing actor stays until replaced", which would otherwise keep the negligent to make the number.

**Rule — the reserve may run short.** When fewer actors are eligible than the reserve size $X_t$ calls for, the reserve holds the eligible ones and the gap is recorded as an **eligibility shortfall**, a third kind beside the occupancy and solvency shortfalls of §12; reviews wait, as §7.5 says. The loop does not seat a negligent reviewer to make a number. A market with two honest reviewers in twenty lacks reviewers, and the record says so.

**Consequence.** This is the panel-composition rule the runs asked for, and it is safe where a $\rho$ floor was not: the plant record is adjudicated by truth, not by the panel, so a captured majority cannot protect its members' records. A full stamper approves every bad plant and reaches $\hat a=(4+1)/(4+2)=0.83>\theta_{\text{duty}}$ on its fourth bad plant — out of the reserve. A reviewer that approves half the bad plants sits near $\hat a\approx0.5$: out of every panel, and on the edge of duty. A careful reviewer at 95% accuracy sits near $\hat a\approx0.09$ once its window fills; early on, one careful reviewer in five has a single failure in its first four bad plants ($\hat a=0.33$) and is kept off panels — not off duty — until the window grows. With a full window of 20 it is off panels about 2% of the time at $\varepsilon=0.05$ and about 13% at $\varepsilon=0.10$: a cost of the mechanism on the honest side, which the §8 runs report. That price is paid in panel seats, not in money. The good-plant record $\hat r$ forms slowly — at $\beta_P=0.75$, four good plants take about 160 reviews, roughly 800 ticks at the defaults — which is acceptable because appeals already expose false rejecters at $a\approx0.98$; $\hat r$ is the backstop for a market where actors do not appeal.

**Recorded and rejected.** rc.1 defined a single plant reliability $\rho^P$ over good and bad plants together and set its floor at 0.5. Because good plants are free passes for an approver, a reviewer approving half the bad plants scored $\rho^P\approx0.63$ — eligible forever while contributing five times the target negligence. Eligibility is therefore defined on the quantity the clock measures [I3].

### 2.3 The effort dial — verification effort as a living thing

**Rule.** The orchestrator maintains a global **effort multiplier** $m_t\ge1$, public, updated once per period from the clock:

$$m_{t+1}=\operatorname{clamp}\!\Big(m_t\cdot\big(\hat F_t/F^*\big)^{\gamma},\ \ 0.9\,m_t,\ \ 2\,m_t\Big)\ \ \text{and then into}\ [1,\ m_{\max}],$$

where $\hat F_t$ is the bad-plant approval rate measured over the period, $F^*$ the target rate, $\gamma$ the gain. In words: when measured negligence exceeds the target, effort rises — at most doubling per period; when it is below, effort eases — at most 10% per period. Up fast, down slow, because capture is expensive and recovery is hard; bounded steps, because the dial must be predictable and not oscillate. This is the block-difficulty adjustment with negligence in place of block time and planted work in place of timestamps.

**Rule — what the dial moves.** Four things scale with $m_t$, together:

1. **The plant rate**: $\pi_t = \pi_0\, m_t$ (capped at $\pi_{\max}$).
2. **Audit odds**: each reviewer's adaptive $p_j$ is applied as $\min(1,\ m_t\,p_j)$.
3. **The reserve**: $X_t$ is sized to the expected review demand of the period, with a floor of $V_{\max}+1$; replacement before release as in §12. *Default sizing:* $X_t=\max\big(V_{\max}+1,\ \lceil r_t\,\bar d\,\rceil\big)$, where $r_t$ is the expected number of reviews per tick — initial reviews times $(1+\pi_t)$, plus audits at $m_t\bar p$, plus the trailing rate of challenge reviews — and $\bar d$ the mean review duration in ticks. At 3 tasks a tick, $\bar p\approx0.25$ and $\bar d=1$ this gives $X=5$ at rest — one more than run 1's reserve of four, which was saturated in over 90% of ticks — and $X=6$ at $m=2$. The reserve is held at $\min(X_t,\ \text{eligible actors})$ (§2.2).
4. **The service fee**: $\omega_t=\omega_0\,m_t$. Verification effort is funded by the economy's security tax, and the tax rises with the threat. $\Omega$ funds plants from it.

**Rule — the alarm.** If $m_t=m_{\max}$ and $\hat F_t>F^*$ for two consecutive periods, the orchestrator commits a **capture alarm** to the History and re-seats the duty reserve from the actors with the lowest $\hat a_i$ (ties by lowest $\hat r_i$, then duty credit) — the one place a record may choose the panel, because this record cannot be captured. The alarm is also the signal to a human, if any is listening; the loop does not wait for one.

**Rule — working capital.** A plant ties up its award, allowance, fee pot and the plant actor's guarantee — $B+\varphi^E+\varphi^F+\lceil0.5B\rceil$, 45 credits at the defaults — from creation until its tree closes. The plant count the dial calls for in a period is **capped by what $\Omega$ can fund from its unlocked balance**, and the gap is recorded as a **plant shortfall**. $\Omega$'s cold-start float is raised to carry one period of plants at $m=1$ (§2.7).

**Consequence.** Under this rule the reserve's honesty is a controlled variable with an uncapturable sensor and an actuator that removes negligent reviewers through a channel they cannot vote on. The honest regime gains margin; the captured regime is detected and acted on from inside the loop. What the dial does not do is make negligence impossible: it makes it unprofitable and short-lived.

### 2.4 Newcomers — fully checked until they have a record

**Default (changed).** $p_{\text{start}}=1.0$: a new actor's approvals are audited every time until five in a row have stood; thereafter the adaptive rule of §8.3 applies. **The audit-odds cap $p_{\text{cap}}$ becomes 1.0** (it was 0.5), so the doubling on an overturn or a plant failure can return an established reviewer to full audit. An actor readmitted from suspension is a newcomer for this purpose; an actor whose plant record is merely undetermined is not — its audit odds follow §8.3 from $p_{\text{start}}$ like anyone's, and this is the only rule for a newcomer's odds. Plants reach newcomers at the ordinary rate: under §7.5 the orchestrator does not choose the reviewer, so it cannot aim a plant, and a newcomer that received plants out of proportion would have a signal §2.1 says does not exist. The §8.3 rule from $p_{\text{start}}=1.0$ covers a newcomer's first approvals in full and tapers as they stand — odds of 1 until five in a row have stood, then 0.5, 0.25 and the floor, about fifteen reviews in all.

**Consequence.** Entry at $\rho=0.5$ with half the approvals unchecked was the cheapest route into the reserve for a stamper. It is closed at the cost of a few extra audits per new actor.

**Recorded and rejected.** rc.1 doubled the plant rate for newcomers; it cannot coexist with round-robin assignment and would itself be a signal [I3].

### 2.5 §7.5 labelled

**Rule.** A reviewer assigned to a case is fresh (not on the case's path), on duty, and **eligible by plant record** (§2.2).

**Default.** Among eligible duty actors: volunteers first; otherwise round-robin in id order from the last assigned; otherwise wait. Refusing to volunteer does not exempt an actor from mandatory duty.

**Recorded and rejected.** Panels chosen by $\rho$: under capture it excludes the careful minority (run 3, 10/90 — their $\rho$ ended below the stampers'). Goes to Appendix B of the consolidation with that reason.

### 2.6 What this does to the bond asymmetry

**Consequence (replaces the open question of run 2).** The two error directions had exposures of ≈0.98 (false rejections, via appeals) and ≈0.027 (false approvals, via audits). Plants expose both at the same rate $\pi_t\beta_P$ and $\pi_t(1-\beta_P)$ respectively, by construction, without an appeal or a dispute. The bond stays one bond; the asymmetry is addressed through exposure, which the solvency run (run 3) showed is the only affordable route.

### 2.7 Defaults

| Default | Value | Note |
|---|---|---|
| $\pi_0$ base plant rate | 0.10 of initial reviews | at 3 tasks/tick, 0.3 plants/tick |
| $\pi_{\max}$ | 0.40 | |
| $\beta_P$ bad-plant share | 0.75 | negligence is the probe's purpose; good plants keep rejecters honest |
| $F^*$ target bad-plant approval rate | 0.10 | a careful reserve at 95% accuracy sits near 0.05 |
| $\gamma$ gain | 1 | |
| period | 50 adjudicated plants, or 200 ticks, whichever first | adjudication is at the verdict; settlement is a window later and would read the reserve of a window ago |
| $m_{\max}$ | 4 | |
| $n_{\min}$ plants of a kind before a record is determined | 4 | |
| $n_P$ trailing window per kind | 20 plants | |
| $\theta_{\text{panel}}$ | 0.20 ($=2F^*$) | above it, no seat on appeal, dispute or audit panels |
| $\theta_{\text{duty}}$ | 0.50 | above it, suspended from duty |
| $T_{\text{susp}}$ | 100 ticks | |
| $p_{\text{start}}$ / $p_{\text{cap}}$ | 1.0 / 1.0 (were 0.5 / 0.5) | |
| $\omega_0$ | 5% of $B$ (unchanged); $\omega_t=\omega_0 m_t$ | |
| $\Omega_0$ cold-start float | 300 credits (was 20) | one period of plants at $m=1$: ≈ 0.3 plants a tick × 45 tied up × 15–20 ticks to closure |

All are defaults: expected to move under simulation; moving them is not a design change.

---

## 3. Consequences and hypotheses

**Compensation under plants.** Write $\bar f=f+\bar e$ for the surviving fee with its emission share: $f=2$, and $\bar e\approx2$ at the start of a run (10 credits a tick shared among three to four settling reviews by weight), halving every 1,000 ticks. A stamper facing plant rate $\pi$ with bad share $\beta_P$ expects, per review, an additional loss of $\pi\beta_P(\bar f+G^V)$ before any reputation effect — at the defaults $0.1\times0.75\times(4+5)\approx0.68$ per review. A careful reviewer at error rate $\varepsilon$ expects $\pi\varepsilon(\bar f+G^V)\approx0.045$.

**Hypothesis 1 — the contest, by channel.** Under 1.2.0 careless review loses to careful review through three channels, and which dominates depends on the split [I3]:
- *Money*: about $0.6$ per review, roughly **120 per actor** over 1,000 ticks at ≈200 reviews each. This is the scale of the 50/50 gap (+200 under appeals alone) and reverses it; it is far from the 10/90 gaps (+1,336 to +1,794), which were selection effects — 66 awards to 159.
- *Reliability*: plant failures enter $\rho$. A stamper adds about 7.5 overturns per 100 outcomes at $\pi=0.1$, a careful reviewer about 0.5, so $\rho\approx0.90$ against $\approx0.95$ — reversing run 3's 0.973 against 0.953 and, with it, the award shares. **This is the channel that flips 10/90.**
- *The seat*: a stamper leaves the reserve within about $n_{\min}/(\pi\beta_P)\approx50$ reviews; from then on it neither earns review fees nor sits on panels.

The dependence on the requester's dispute rate and on the actor's appeal rate, which decided the contest under 1.1.0, is removed as a *necessary* condition; both remain welcome. The §8 runs measure the three channels separately.

**Hypothesis 2 — capture.** A stamper majority cannot persist in the reserve: each stamper leaves it within about 50 reviews of plant exposure, panels are held by actors whose plant records pass, and the honest regime is restored without any human action. What capture becomes instead is a **shortage**: at 10/90 the reserve runs short by up to eighteen eligible actors, reviews wait, and the eligibility shortfall is on the record — the loop stays honest and slow rather than captured and fast, and says which. The tipping point of run 3 (somewhere between 50/50 and 10/90) moves to "nowhere" for honesty, and reappears as a capacity cliff that the market must answer by recruiting reviewers.

**Hypothesis 3 — cost.** At $m=1$ plants cost $\Omega$ about one careful inspection's fee and expenses per plant (a stamper's failed plant costs $\Omega$ nothing but the refunded pots), about 2 credits per tick at 3 tasks/tick, against a service-fee income of 3 per tick; at $m_{\max}=4$ the floating fee covers four times the plants. Whether this holds under the full challenge load is §18.1 question 3 restated.

**Hypothesis 4 — camouflage.** A stamper that rejects a random fraction of work to look careful still approves bad plants at its approval rate and is caught in proportion; camouflage buys time, not safety. The red-team run (§8) tests this and the harder case: a reviewer that tries to *detect* plants from the view, which by §2.1 carries nothing to detect.

**Limit, restated.** Plants exist where fulfillment is constructible. In a domain where it is not, the loop falls back to 1.1.0's position: fair with both challengers present, blind under capture. That is a deployment boundary and is to be stated as such in the product.

---

## 4. What does not change

Verdicts and their availability; the two pots and the settlement rule of 1.1.0, including tree closure; emission; the credit and the halt state; denomination; offers, selection and the guarantee; the lifecycle and tick order; the cap, the bond and its forfeiture rule, timeouts, replacement; appeals, disputes, audits (now scaled by $m_t$), rulings, the two-question appeal; delegation; reliability $\rho$ (which now also counts plant outcomes) and duty credit; rotation by lowest duty credit among eligibles; the record; the human, overrides, corrections, label grades — plants carry a fifth grade, **plant**, truth known by construction, never promoted; permitted, forbidden and not-offered operations, except that *create plant* is added to the orchestrator's permitted operations.

**What does change besides the mechanism, listed so it is not missed:** the reserve size $X$ is no longer a fixed default but sized each period (§2.3, amending §12); the service fee $\omega$ scales with the dial (§2.3, amending §4.1); the reviewer's view no longer carries the actor (§2.1, amending §14); the audit cap is 1.0 (§2.4, amending §8.3's default). Emission is unchanged in rule but plants settle in the same batches as real reviews, so they take emission shares by weight: each real review's share is diluted by about $\pi_t$; nothing extra is minted.

---

## 5. Invariants, notation, questions (amendments)

**I20 (new) — plants are self-adjudicated.** A plant's outcome is set only by its known truth; no audit, appeal, dispute or ruling is ever opened on a plant; the plant marker is in the History at creation and revealed only at adjudication. (That a plant's view is indistinguishable is not a per-tick predicate; it is a property of the view function — it reads no actor and no marker — and is asserted by a test, §7.)
**I21 (new) — the dial is bounded and the reserve is sized.** $1\le m_t\le m_{\max}$; each step within $[0.9,2]$; $\pi_t\le\pi_{\max}$; $X_t\ge V_{\max}+1$; the reserve holds $\min(X_t,\ \text{eligible})$ actors; no assignment is made to an actor ineligible for that tier at the time of assignment; no actor remains on duty past the completion of its active review once duty-ineligible; the eligibility and plant shortfalls are counted. **I9** is amended accordingly (the reserve holds $\min(X_t,\text{eligible})$, not $X$).
**I1** (conservation) covers $\Omega$-funded plants. **I13** (grade provenance) admits the *plant* grade. **I17** accounts plant pots to $\Omega$.

**Appendix A (amended).** $\Omega_0=300$; the initialization condition $|A_0|\cdot50+\Omega_0\le M_0$ reads with 300. The plant requester and plant actor are two system wallets funded by transfer from $\Omega$ at a plant's creation and swept back to $\Omega$ at its tree's closure; "$\Omega$'s unlocked balance" in §2.3 is $\Omega$'s wallet before that transfer; `create_plant` builds the case in the submitted state without the award path; I1 and I17 hold as written.

**Notation (Appendix C additions).** $\pi_t$ plant rate; $\beta_P$ bad-plant share; $\hat F_t$ bad-plant approval rate of the reserve; $F^*$ its target; $m_t$ effort multiplier; $\gamma$ gain; $\hat a_i$, $\hat r_i$ an actor's smoothed bad-plant approval and good-plant rejection rates; $n_{\min}$, $n_P$, $\theta_{\text{panel}}$, $\theta_{\text{duty}}$, $T_{\text{susp}}$ as in §2.7.

**§18.1 (amended questions).** *Q1* becomes: under 1.2.0, how fast does stamping lose, and in how many reviews does a stamper leave the reserve? *Q3*: does $\omega_t$ fund plants and audits at each $m$; how large does $\Omega$'s outstanding exposure get? *Q6*: does $X_t$ track demand without starving the market of actors? *New Q9*: how far does the tipping point move, and does the alarm ever fire in a run that began honest? *New Q10*: what fraction of real work in a target domain admits plants?

---

## 6. Worked example

Six actors; C, D, E, F on duty; $m=1$, $\pi=0.1$, $\beta_P=0.75$. C is a stamper; D is careful (cost 3). $\Omega$ holds 100.

**A bad plant to C.** $\Omega$ funds a plant: award 20, allowance 10, fee pot 5 — 35 moves from $\Omega$ to the plant's escrow and pots. C is assigned, sets aside its bond 5, answers $\mathsf F$ at cost 0. Adjudication by truth: plant failure. C's bond is burned; C gets no fee; C's $\rho$ records an overturn; C's $p$ doubles; C's plant record is 0 stood, 1 failed. The plant runs out its window and settles: award, allowance and fee pot return to $\Omega$ in full. $\Omega$'s net cost: 0. The economy's supply fell by 5 (the burned bond).

**A bad plant to D.** D sets aside 5, spends 3, answers $\mathsf N$. Stood. At settlement D is reimbursed 3 from the allowance and paid the fee 2 plus its emission share; 7 of the allowance and 3 of the fee pot return to $\Omega$. $\Omega$'s net cost: 5. D's plant record: 1 stood.

**Four bad plants later.** C has approved all four: $\hat a_C=(4+1)/(4+2)=0.83>\theta_{\text{duty}}=0.5$ with $n_{\min}=4$ reached — C is suspended from duty for 100 ticks, and the next eligible actor with the lowest duty credit is seated before C is released; if none is eligible, the reserve runs one short and the eligibility shortfall is counted. D rejected all four: $\hat a_D=(0+1)/(4+2)=0.17\le\theta_{\text{panel}}=0.2$ — eligible for duty and for panels. Had D slipped once, $\hat a_D=0.33$: still on duty, off panels until its window grows.

**The dial.** Over a period of 50 plants (37 bad), 15 bad plants were approved: $\hat F=15/37=0.41$ against $F^*=0.10$; ratio 4.1, clamped to ×2: $m\colon1\to2$. Next period: plant rate 0.2, audit odds doubled, $\omega$ 10% of $B$, $X$ re-sized to cover the added demand (from 5 to 6 at 3 tasks a tick), the plant count capped by what $\Omega$ can fund. If the reserve was honest all along, $\hat F$ sits near 0.05 and $m$ eases 10% a period back to 1.

---

## 7. Implementation note (what the engine must do; no code here)

- A **plant requester** and **plant actor** owned by the orchestrator, wallets backed by $\Omega$; `create_plant(truth)` is an orchestrator operation that produces a case in the submitted state with the plant marker sealed in its History entry, refused when $\Omega$'s unlocked balance cannot fund it (and the shortfall counted). The reviewer view **drops the actor field** (§2.1); a test asserts that the view of a plant and of a matched ordinary case are equal field for field.
- **Adjudication at verdict**: on a plant's initial $\mathsf F$/$\mathsf N$ the engine applies the §2.1 table; $\mathsf P$/$\bot$ marks the plant spent. No challenge operation accepts a plant case. Settlement is the ordinary 1.1.0 rule; pots refund to $\Omega$ at closure.
- **Plant record** per actor: trailing windows per kind, $\hat a_i$ and $\hat r_i$; the two-tier eligibility check at rotation (duty) and at every assignment (panel for challenge reviews); suspension with its clock, overriding §12's stay-until-replaced rule at the completion of the active review; readmission only by a passing record, else a further suspension; audit odds restarting at $p_{\text{start}}$ on readmission; the eligibility shortfall counter beside occupancy and solvency.
- **The dial**: period accounting of $\hat F_t$ on adjudications; the update rule with its clamps; $\pi_t$, the audit scaling with $p_{\text{cap}}=1$, $X_t$ sizing held at $\min(X_t,\text{eligible})$, $\omega_t$. The engine computes the *required* plant count per tick and caps it by $\Omega$'s unlocked balance; the driver supplies plants of the declared truth at that rate — a run that supplies fewer declares it under §18.2. The alarm commits a History event and re-seats the reserve by plant record.
- **Defaults** in params, including $\Omega_0=300$ and $p_{\text{cap}}=1$; **I20, I21** in the per-tick checks; I1, I9, I13, I17 amended.
- **Drivers**: the stamping driver gains a plant supplier (the task world already knows truth), the camouflage disposition, and columns for $\hat F_t$, $m_t$, $\pi_t$, suspensions, $\Omega$ plant spend, and per-population plant failures.
- **Tests**: `test_v12.py` with the §6 figures, the two eligibility tiers and the suspension, the eligibility shortfall, the capital cap, the clamp bounds, the alarm and re-seating, and the view-equality test. Existing tests that fix $p_{\text{start}}=0.5$ or $p_{\text{cap}}=0.5$, or read `ReviewView.actor`, are revised; reviewer-authored tests that do are superseded with the reason, as before.

---

## 8. After acceptance — the runs

1. **Reproduce §6.**
2. **Controller on vs off under a drifting stamper share**: dispositions re-drawn each 100 ticks toward stampers until 90%, with appeals truthful and **no disputes** (the design assumption); X free to track. Does the honest regime hold, does the alarm fire, how large does the eligibility shortfall get, and how long does it last once suspended stampers return as newcomers? Measure the three channels of Hypothesis 1 separately.
3. **Adaptive dispositions**: actors switch between careful and stamping on observed wealth of each type. The equilibrium question, under 1.2.0 and, as control, under 1.1.0.
4. **Tipping point**: 40/60, 30/70, 20/80 under 1.1.0 (the baseline for Q9) and 1.2.0.
5. **Red team**: camouflaged stampers (approve 90%, reject 10% at random); a reviewer that attempts to detect plants from the view (I20 says it cannot; the run checks that the engine agrees).
6. **Cost**: $\Omega$'s plant spend and $\omega_t$ across $m$; the reserve's size trajectory (Q3, Q6).

---

## 9. Provenance

**[S2] Runs 2 and 3 (October 17, 2026)** — `agentic_sim/results/studies/1.1.0-stamping/` and `1.1.0-combined/`, 1,295 runs, engines `a1e726a` (1.1.0) to `f3aede2`; hand-off sections "Design revision 1" through "Run 3". **[C-rev2] Design discussion (October 17, 2026).** Baruchi: "surprise inspection is a living thing — we can increase it if we see that we are in danger and release a bit otherwise, like the effort in bitcoin"; "I am going out of an assumption that humans will not intervene; we cannot control if and when they will complain." Claude: without a human, every signal is panel-produced; the orchestrator must own truth — mechanically checkable work, or planted work; Baruchi chose planted work as "a real dial". **[P-oct14]** The October 14 proposal map's open question on known-answer audits — "for which claims do we genuinely know an audit answer?" — answered here for the plants the orchestrator writes. **[I2]** The implementer's §7.5 reading, adopted in §2.5. **[I3] Implementation review of rc.1 (October 17, 2026)** — the actor in the reviewer's view; I9 against I21 when eligible actors are fewer than the reserve; $\rho^P$ mixing good and bad plants; newcomer plant-doubling against round-robin; the solvency figure; $\Omega$'s working capital; the audit cap; the channels of Hypothesis 1; and the smaller points on $X$ at rest, the list of rule changes, emission dilution and the engine commits — all adopted in rc.2. **[I4] Implementation review of rc.2 (October 17, 2026)** — a cleared record on return would have readmitted stampers with clean slates and kept panels stamper-majority at about 70% strength; two rules for a newcomer's audit odds; eligibility as a property at assignment, with a suspended actor leaving duty regardless of replacement; the period on adjudications; $\hat r$'s slow formation; the panel cost on honest reviewers; the Appendix A condition; the two-system-wallet reading — all adopted in rc.3. **[I5] Review of rc.3 (October 17, 2026)** — implementable as it stands; one leftover sentence in §2.4 (the ~50-review figure from the struck rule) corrected here as the review directed, for the consolidation.

---

## Closing statement

> The loop no longer needs anyone to complain. It writes some of the work itself, knows the answer, and watches who gets it wrong. The watching costs effort; the effort rises when the watching finds trouble and eases when it does not; the effort is paid for by the fee every request pays for its security. A reviewer that will not look loses its bond, its standing and its seat, through a door no majority can hold shut. Humans may still pull the plug. They do not have to.
