# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 3 — specification 1.3.0-rc.2: inspection is membership

**Project:** ELEF / Agentic Economics  
**Version:** 1.3.0-rc.2 — a release candidate, not yet in force. rc.1 (October 17) was the proposal as first sent; rc.2 settles the five points of the implementation review [I7] — one record for readmission and panel seats, the duty cap as a seating rule with the panel floor yielding over it, reserve sizing on applied audit odds, the refill order for turns, and the invariant consequences of netted plant capital — and its six smaller points. On acceptance it becomes **1.3.0**, consolidated into one standalone text, and 1.2.1 moves to history. Semver as before.  
**Prepared:** October 17, 2026 (rc.1 and rc.2)  
**Supersedes:** 1.2.1 where this document speaks; everywhere else 1.2.1 stands unchanged. (1.2.1 is 1.2.0 with the probation sentence of Appendix A applied — a patch, in force since October 17; this revision restates probation in full in §2.2.)  
**Nature of this revision:** A **design revision** under §19 — the third since the freeze. It changes what a suspension from duty means (it now suspends market membership), what probation is (a supervised way back), who carries the reviewing load (a cap on members' duty, with probationers filling the first-review slots), where the dial's raised tax goes (to the reviewers, not to Ω), and how plant capital is counted (the pots only). It adds no participant, no verdict, no challenge.  
**Design assumption, unchanged:** humans do not intervene.  
**Status:** Proposed. Accompanied by the evidence that required it (§1) and the runs that test it (§8). A remedy for the slowness §3 describes is deliberately **not** in this revision; it is reserved for a later one.

> **Money enters with requests. Truth enters with requesters — and with the orchestrator's own planted work.**
>
> **Verification effort is a living thing.**
>
> **Inspection is membership: an actor that will not inspect honestly does not work, until it does.** *(new)*

---

## 1. Why: what run 4 found

Run 4 — 300 runs under 1.2.0, every final audit passed, truthful appeals and no disputes throughout — established that the clock works and exposed what it costs [S4]:

1. **Honesty holds everywhere, with nobody watching.** False approvals four- to five-fold below 1.1.0 at every split from 50/50 to 80/20; under a stamper share drifting to 90% they stop growing once the dial saturates (83 against a control of 650); stampers are suspended within their first handful of plants; a population that adapts its disposition to what pays drifts toward honesty (stamper share 0.29 against 0.43). Hypothesis 2 of revision 2 holds as stated.
2. **It is slow.** When most of the reserve is suspended there are few eligible reviewers: a case waits for a reviewer 47 times longer than in the control, vesting ends 40% lower, and Ω cannot fund a third of the plants the dial calls for at $m_{\max}$.
3. **Suspension from duty is a reward.** At 60/40 the eight careful actors are the only eligible reviewers; the dial sizes the reserve to 7–8; they are on duty almost always — 500 to 800 reviews each at a fee of 2 — while the twelve suspended stampers, freed from duty, take the awards at 20: delivery income 3,311 against 1,063 per actor, stampers richer in 19 of 20 seeds. Selection cannot help, because it runs among *free* actors and the honest are not free. Honesty was defended by the honest minority at pocket-money rates while the excluded majority worked.
4. **Ω banks the raised tax** (+5,898 at 60/40) that the dial levied for exactly the effort the honest were supplying.
5. **Working capital, not income, caps the clock**: a plant ties up 45 credits of Ω's own money — of which 30 is Ω paying itself.
6. **One wording defect of rc.3 §2.2**, found at implementation: with the record persisting, a suspended actor judges no plants and could never pass; the implementer's probation reading gave $T_{\text{susp}}$ its meaning and is confirmed here.

The contest is therefore no longer about detection. It is about **who carries the reviewing load and what membership of the market requires**. Baruchi's answer [C-rev3]: *if you get thrown out of inspection you are banned from receiving a new task; to get tasks back you have to prove you are doing good inspection for a while.*

**Classification.** A design revision motivated by a strategy finding, labelled and read on its own. It changes the meaning of an existing state (suspension) and adds a cap and a fund; it alters no settlement, verdict or challenge rule.

---

## 2. The rules

### 2.1 Membership is gated by the plant record

**Rule.** An actor **suspended from duty** (1.2.0 §2.2: its bad-plant approval rate $\hat a$ or good-plant rejection rate $\hat r$ above $\theta_{\text{duty}}$) is **suspended from the market**: it wins no new award while suspended. It may finish the commitment it holds, including by delegating within it, and its open cases settle by the ordinary rules. Its wallet, reputation and record are untouched by the suspension itself; its $\rho$ carries its plant failures into selection as any overturns, for when it returns.

**Consequence.** Exclusion from duty no longer frees an actor to earn. An actor that will not inspect honestly is not a member of the market until it does; the duty that was a burden the honest carried for the negligent is now the gate the negligent must pass to work again.

**Recorded and rejected.** A *duty levy* — letting a suspended actor keep winning awards against a cash levy paid to the reviewers — was considered. It is softer and preserves throughput, but it prices negligence as an option, keeps the negligent inside the market as competitors of the honest, and under an adapting population converges more slowly than exclusion. It may return as a later softening; it is not in this revision.

### 2.2 Probation: the way back

**Rule.** After $T_{\text{susp}}$ ticks a suspended actor becomes a **probationer**. A probationer:

- serves **initial reviews only** — no appeal, dispute or audit seat;
- is assigned exactly as any duty actor is (1.2.0 §2.5, round-robin among those on duty), and receives plants at the ordinary rate, mixed with real work it cannot tell apart;
- has its **audit odds pinned at $p=1$**: every approval it gives is audited, with no taper, for as long as it is a probationer;
- is **re-checked at every plant adjudication**: a plant failure suspends it again at once, and the suspension clock restarts;
- is **readmitted to membership** — new awards, and duty as a member — when its **trailing record** (the one record of 1.2.0 §2.2, which persists through suspension) passes $\theta_{\text{duty}}$, and at least $n_{\min}$ new plant outcomes have been adjudicated since the suspension began. Panel seats return separately when the same trailing record passes $\theta_{\text{panel}}$, as in 1.2.0. **One record, one meaning:** there is no separate "since suspension" record; the count of new outcomes is only a minimum before readmission can be considered.

**Consequence.** A full stamper at $\hat a=0.83$ must reject about four bad plants in a row — $(4+1)/(8+2)=0.5$, some fifty honest reviews, roughly 250 ticks on duty — to work again. "Prove you are inspecting well for a while" is that number. Its panel seats return later still: not until its four approvals have rolled out of the trailing window of twenty bad plants, about twenty more. That slower return of judging seats to a reformed stamper is the right price. A probationer that stamps is out again at its first bad plant, having had every approval in between audited. **A probationer's own plant failure is any failure, not a failing record** — intended: a careful probationer at $\varepsilon=0.05$ restarts its clock with probability about 19% over its four needed bad plants, and the alternative (re-suspend only on a failing record) would let a half-stamper coast through probation on its good plants.

**Consequence — probation is not itself the deterrent.** On probation a stamper earns a little: with every approval audited, at $b=0.2$ and 95% auditor accuracy it loses a bond on about 19% of reviews and earns the fee and uplift on the 80% that stand — roughly $+1.2$ a review at $m=2$. What bites is the award it cannot win. Nobody should expect probation to deter on its own; the gate does.

**Why the pin, and a correction to 1.2.0 §2.4.** The §8.3 taper — odds of 1 until five approvals in a row have stood — is easy to pass by stamping, because about 80% of work is good: a third of stampers pass it immediately. Pinned odds are therefore the rule for probationers. For the same reason, **a newcomer's odds are pinned at 1 until its bad-plant record is determined** ($n_{\min}$ bad plants adjudicated), and only then does §8.3's adaptive rule apply from $p_{\text{start}}=1.0$. This replaces 1.2.0 §2.4's taper-from-the-start; it is one rule for both kinds of unproven actor, stated once. Its cost — about fifty fully audited reviews per newcomer — is a §8 measurement, and it has a known worst case: **in a fresh population every actor is undetermined**, so every approval is audited by an auditor that is itself an undetermined newcomer — a stamper auditing a stamper agrees — and review demand doubles in the first period, sizing $X_t$ up at once. The pin buys little until the first records form; §8 names that cost.

### 2.3 Who carries the load: a cap on members' duty, probationers first

**Rule.** **No member is seated on duty while on-duty members number $\lceil E_t/2\rceil$ or more**, where $E_t$ is the number of actors eligible for duty and not suspended; a member found above the cap when $E_t$ falls completes its active review and leaves duty at its completion (as 1.2.0 §11.2 has it). Probationers on duty do not count against the cap. **The panel floor yields over the cap, bounded by availability:** at least $\min(V_{\max}-1,\ E_t)$ members are on duty **whenever that many free, fundable members exist to seat**; a reserve below the floor is admissible only when none was left — a member committed to a task, unable to fund the bond, or mid-review elsewhere cannot be seated — and the gap counts toward the eligibility shortfall, in the same form as I9. A market with two honest free members seats both and has nobody free, which is what it is. The reserve is sized as in 1.2.0 §2.3 ($X_t$) and filled in this order: **members first for the seats only members may hold** — the period's expected audit and challenge reviews, and never fewer than $\min(V_{\max}-1,E_t)$ members; **then probationers for initial-review demand**, lowest duty credit first; **then members** for any initial-review demand left, up to the cap. Any remaining gap is the eligibility shortfall, counted as before, and reviews wait.

**Rule — sizing on applied odds.** The audit demand that sizes member seats (and $X_t$, 1.2.0 §2.3) is the sum over the period's initial approvals of **the approving reviewer's applied audit odds** — 1 for a probationer or an undetermined newcomer, its adaptive $m_t p_j$ otherwise — not a population mean $m_t\bar p$. Member seats are that sum plus the trailing challenge-review rate, times $\bar d$, floored at $\min(V_{\max}-1,E_t)$.

**Rule — turns.** Duty still rotates by turns with replacement before release (1.2.0 §12.1). A seat a turn vacates is refilled in the order above **for the kind of seat it was**: a member seat by a member, an initial-review seat by a probationer first.

**Rule.** Initial reviews are assigned round-robin among all on-duty actors, probationers included. Audit, appeal and dispute seats are assigned only to on-duty **members** who are panel-eligible.

**Consequence.** The reviewing grind lands on the actors earning their way back; the honest keep at least half their number free to work, and hold every seat that judges a challenge. Where there are no probationers and few members, the reserve runs short and says so.

### 2.4 The raised tax pays the reviewers

**Rule.** Of the service fee $\omega_t=\omega_0 m_t$ collected on each award, $\Omega$ keeps the base $\omega_0 B$ and the remainder $(m_t-1)\,\omega_0 B$ goes to a **duty fund**. At each settlement batch the fund's balance is distributed to the reviews settling in that batch **exactly as emission is** — by role weight, across every case settling that tick — as an **uplift** on the fixed fee. Unlike emission the fund is real money paid in, so a balance no review claims in a tick carries to the next.

**Consequence.** When the dial raises effort, the tax it levies is paid to the actors supplying the effort, not banked by the referee; a plant's stood review draws uplift like any other. At $m=2$ and $B=20$, one extra credit per task — about 3 per tick at 3 tasks a tick — is shared among the roughly four reviews settling each tick: an uplift of about 0.75 per unit of role weight on a fee of 2. At $m_{\max}=4$, three extra credits per task, an uplift of about 2.3.

### 2.5 Plant capital counts only the pots

**Rule.** A plant's award and the plant actor's guarantee are $\Omega$ paying itself and are **netted at creation**: they appear in the record as the plant's notional terms (sealed with the marker) but tie up no balance. The capital a plant requires of $\Omega$'s unlocked balance is $\varphi^E+\varphi^F$ — 15 credits at the defaults, not 45. The capital cap and the plant shortfall of 1.2.0 §2.3 apply to that amount.

**Consequence.** $\Omega$ funds three times the plants on the same float; the clock saturates on effort, not on bookkeeping. $\Omega_0$ may fall back toward its former level; left at 300 here as a default to sweep.

### 2.6 Defaults

| Default | Value | Note |
|---|---|---|
| Readmission | record passes $\theta_{\text{duty}}=0.5$ over $\ge n_{\min}=4$ new plant outcomes since suspension | both rates, as in 1.2.0 |
| $T_{\text{susp}}$ | 100 ticks (unchanged) | the wait before probation begins |
| Probationer / newcomer audit odds | pinned at 1 until readmitted / until the bad-plant record is determined | then §8.3 from $p_{\text{start}}=1.0$ |
| Members' duty cap | $\lceil E_t/2\rceil$ | |
| Duty fund | $(m_t-1)\,\omega_0 B$ per award; distributed as emission, carrying forward | |
| Plant capital | $\varphi^E+\varphi^F=15$ | |
| $m_{\max}$ | 4, **swept against 2** in §8 | run 4: dial off already cut false approvals 650 → 257; the last factor of three cost most of the throughput |
| $\Omega_0$ | 300, swept against 100 | |

All are defaults.

---

## 3. Consequences and hypotheses

**Hypothesis 1 — the contest.** Under 1.3.0 a stamper earns award income only while unsuspended — its first handful of plants — and then nothing until it reforms. At 60/40 the honest eight hold the whole market with at least four of them free at any time; the stampers' 3,311 of delivery income falls to the few awards won before suspension. The sign at 50–70% flips decisively; the money channel is no longer the ~0.6 per review of revision 2 but the award itself.

**Hypothesis 2 — convergence.** Under adaptive dispositions, an actor whose income is zero switches faster than one whose income is merely lower: the stamper share falls faster than 0.50 → 0.29 in 1,000 ticks and reaches an honest equilibrium. The run says whether.

**Hypothesis 3 — slowness.** A captured market shrinks to its honest core: at 60/40, eight members and twelve probationers; throughput is set by what eight members can deliver with half of them free, and by the initial-review capacity of twelve probationers under full audit. Vesting falls further than in run 4 before it recovers as probationers reform or leave. **This revision accepts that cost and does not treat it.** Baruchi has a direction for it, reserved for a later revision [C-rev3]; recording it here keeps the slowness a measured, named consequence rather than a surprise.

**Hypothesis 4 — the fund.** The duty uplift roughly doubles reviewer pay at $m=2$ and triples it at $m_{\max}$, paid only when the dial has risen — so reviewing becomes most attractive when the market most needs reviewers. Whether that draws adapting actors toward honesty faster than the gate alone is separable in the adaptive run (fund on / off).

**Hypothesis 5 — probation safety.** Pinned audits hold a probationer's false approvals to those that survive an audit by a panel-eligible member — at 95% accuracy, about one in twenty of its stamped bad work — and the cost is one audit per probationer approval, carried by the members. The ratio of probationers to members bounds the audit load: at 60/40, roughly twelve probationer approvals per tick-equivalent against eight members' capacity; the run measures whether this binds before the duty cap does.

**Limit, restated.** The accuracy bar stands: an actor below roughly 92% is a bad inspector and under 1.3.0 is also, in time, not a member. That is a product stance — inspection is membership — and it is stated as such.

---

## 4. What does not change

Everything in 1.2.0 not named above: plants, the plant record and its two thresholds, the dial's update rule and what it scales, the alarm, the actor-less view, the two pots and settlement, verdicts, challenges, delegation, $\rho$ and $\kappa$, the record, overrides and grades. Suspension is still triggered as in 1.2.0 §2.2; what it means has changed. $X_t$ is still sized as in 1.2.0 §2.3; who fills it has changed.

---

## 5. Invariants, notation (amendments)

**I22 (new) — membership.** No award is made to an actor that is suspended or on probation; no probationer holds an audit, appeal or dispute seat; every probationer's audit odds are 1; a probationer is readmitted only with a passing record over $\ge n_{\min}$ new plant outcomes.
**I23 (new) — the load and the fund.** No member is seated while on-duty members $\ge\lceil E_t/2\rceil$; a member above the cap holds no assignment past the completion of its active review; on-duty members $\ge\min(V_{\max}-1,E_t)$ whenever that many free, fundable members exist to seat, the gap otherwise counted toward the eligibility shortfall; the duty fund equals the raised tax collected less the uplifts paid (conservation, with I1); the uplift of a batch is distributed by role weight.
**I21 (amended).** The plant capital cap is on $\varphi^E+\varphi^F$; a plant's award and guarantee tie up no balance. Consequences stated so they are not rediscovered: a plant has **no escrow and no guarantee lock**, so **I15** (every live obligation has a lock record of exactly its size) exempts a plant's guarantee; **I12** keeps a plant's $B$ and $G$ as frozen nominals that bind nothing; and **vesting a good plant pays no price and releases no guarantee** — the plant actor's wallet is notional. The §10.4 flows gain the duty fund: in, $(m_t-1)\,\omega_0 B$ per award; out, uplifts by role weight per batch; a wallet, so I1 holds. A plant's stood review settles in the same batch as any other and draws uplift like any other.

**Notation (Appendix C additions).** $E_t$ eligible members; probationer; duty fund; uplift.

**§18.1 (amended).** *Q1*: under 1.3.0, by how much do the honest end richer at each split, and through which channel? *Q9*: does the adaptive population reach an honest equilibrium, and in how many ticks? *New Q11*: throughput of a market shrunk to its honest core — vesting against the control at each split — the measured cost that the next revision addresses.

---

## 6. Worked example

Twenty actors, 60/40 careful to stamper, defaults, $m=2$ at the moment in question.

**C, a stamper, is suspended at tick 310** on its fourth bad plant ($\hat a=0.83$). It finishes the task it holds (paid or not by the ordinary rules) and then wins nothing. Its wallet holds what it earned; its $\rho$ carries four overturns.

**Tick 410: probation.** C returns to duty as a probationer, lowest duty credit first, filling an initial-review slot ahead of any member. Its audit odds are 1. Over its next ten reviews it approves everything: eight approvals of good work stand; two of bad work are caught by the audit — bond lost each time, $\rho$ down. Its eleventh review is a bad plant, approved: suspended again at tick 460, clock restarted. False approvals that reached a customer: those the audit missed — at 95% auditor accuracy, about one in twenty of C's stamped bad work.

**The reformed path.** Had C rejected bad work from tick 410, its first four bad plants over about fifty reviews bring its trailing record to $\hat a=(4+1)/(8+2)=0.5\le\theta_{\text{duty}}$ with four new outcomes adjudicated: readmitted to membership at about tick 660. It is **not** panel-eligible yet — $0.5>0.2$ — and will not be until its four approvals roll out of the trailing window of twenty bad plants, about twenty more plants on. Its odds follow §8.3 from 1.0 once readmitted.

**The members meanwhile.** Eight eligible members; at most four on duty. The reserve of $X_t=7$ seats members first for the audit and panel work — at $m=2$ with every probationer approval audited, that is most of the demand, say three members — then probationers for the initial reviews, four of the twelve; the fourth member slot stays free unless initial demand needs it. Every audit of a probationer's approval, every appeal and dispute seat goes to an on-duty member. The other five members are free to work: at 3 tasks a tick, they are the market.

**The fund.** $m=2$: $\omega_t=10\%$ of $B$; $\Omega$ keeps 1 per task, the fund receives 1. Three tasks a tick, about four reviews settling a tick by weight: an uplift of about 0.75 per unit of role weight — a member's audit (weight 1.5) earns $3+1.1$ plus emission; a probationer's initial review that stood earns $2+0.75$ plus emission.

**Plant capital.** A plant ties up 15, not 45; $\Omega$'s float of 300 carries twenty plants outstanding, three times run 4's.

---

## 7. Implementation note (no code here)

- **Membership state** per actor: member / suspended / probationer; `award` refuses a non-member before any effect; nested posting allowed only within a held commitment.
- **Probation**: transition at $T_{\text{susp}}$; initial-review-only eligibility; pinned odds (the §8.3 update does not run for probationers or undetermined newcomers); re-check at every plant adjudication, any failure re-suspending; readmission when the one trailing record passes $\theta_{\text{duty}}$ and a counter of outcomes since suspension has reached $n_{\min}$ — the counter is a minimum, not a second record.
- **Rotation**: two kinds of seat; member seats sized on applied audit odds plus the challenge rate, floored at $\min(V_{\max}-1,E_t)$; fill order members (for member seats), probationers lowest duty credit first (initial seats), members for remaining initial demand while below the cap; the cap enforced at seating, with a member above it leaving at the completion of its active review; a vacated turn refilled by kind; initial reviews round-robin over all on duty; challenge and audit seats only to panel-eligible on-duty members; eligibility shortfall as before.
- **Duty fund**: a wallet; $(m_t-1)\omega_0 B$ credited at award; distributed at each settlement batch by role weight as a fee uplift; carries forward; I23.
- **Plant capital**: creation nets award and guarantee; capital check on $\varphi^E+\varphi^F$; no escrow and no guarantee lock for a plant (I15 exemption, I12 nominals, vesting pays no price); record entries unchanged in form. `test_v12`'s capital figures (35 moved from $\Omega$; net cost 0) become 15 and are revised as implementer tests.
- **Defaults**: as §2.6; $m_{\max}$ and $\Omega_0$ as params swept.
- **Tests**: `test_v13.py` with the §6 figures, membership refusals (atomic), probation transitions and the pin, readmission arithmetic, the duty cap and fill order, fund conservation and distribution, plant capital. Tests pinning 1.2.0 §2.4's taper-from-start for newcomers are revised; reviewer tests that do are superseded with the reason.
- **Drivers**: columns for membership state counts, probationer reviews and their audit outcomes, fund balance and uplift paid, time-to-readmission; the adaptive driver gains a fund on/off switch.

---

## 8. After acceptance — the runs

1. **Reproduce §6.**
2. **Tipping point under 1.3.0**: 50/60/70/80 fixed splits, 1,000 ticks, against run 4's table — the sign and the channel at each split (Q1); vesting against the control (Q11).
3. **Adaptive dispositions**: 1.3.0 against 1.2.0, fund on and off, 3,000 ticks — equilibrium and time to reach it (Q9).
4. **Drift** as in run 4 under 1.3.0, $m_{\max}\in\{2,4\}$, $\Omega_0\in\{100,300\}$.
5. **Probation safety**: false approvals attributable to probationers; audit load on members; whether the duty cap or the audit load binds first.
6. **Red team**: the camouflaged stamper under the gate; a probationer that behaves until readmitted and then stamps (expected: out again on its next bad plant, having lost its awards in between — measure the cycle's yield to it).

---

## 9. Provenance

**[S4] Run 4 (October 17, 2026)** — `agentic_sim/results/studies/1.2.0-clock/`, 300 runs, engine `544ff19`; hand-off sections "Design revision 2" and "Run 4". **[C-rev3] Design discussion (October 17, 2026).** Baruchi: "if you get thrown from inspection you are banned from receiving a new task. if you want to get a new task back you need to prove you are doing good inspection for a while"; and: "I have an idea for the slowness, but we will get to it later." Claude proposed a duty levy; Baruchi's gate replaced it (§2.1, recorded and rejected). **[I6]** The implementer's probation reading of 1.2.0 §2.2, confirmed as 1.2.1 and restated in §2.2; its three revision-3 candidates — the fee scaled with the dial, a reserve sized to the eligible pool, exclusion from awards through $\hat a$ — of which this revision adopts the third in Baruchi's form and the first as the duty fund, and replaces the second with the members' duty cap. **[I7] Implementation review of rc.1 (October 17, 2026)** — readmission stated two ways with §6 following the wrong one; the duty cap as a standing predicate against mid-review completion and the panel floor at small memberships; reserve sizing on a population mean rather than applied odds; the refill order for turns; the invariant and settlement consequences of netted plant capital; and six smaller points — all adopted in rc.2. 1.2.1 was applied to the text in force the same day. **[I8] Review of rc.2 (October 17, 2026)** — implementable as it stands; one qualifier, the panel floor bounded by availability rather than membership alone, adopted here in the reviewer's wording for the consolidation.

---

## Appendix A — the 1.2.1 sentence

For 1.2.0 §2.2, in place of "otherwise remains suspended for a further $T_{\text{susp}}$":

> *At the end of the suspension an actor whose record still fails is readmitted on probation — to duty, not to panels — until its next plant adjudication re-checks the record; a record that still fails suspends it again at once. $T_{\text{susp}}$ is the interval between re-checks.*

---

## Closing statement

> The loop keeps itself honest with nobody watching; run 4 showed that. It also showed the honest paying for it while the excluded earned. This revision makes inspection the price of membership: lose your seat for negligence and you lose the market, and you buy both back the only way that can be checked — by inspecting well, under full audit, for a while. The tax the dial raises goes to the people doing the work. What is left is that an honest market of few is slow. That is the next question, and it has a direction.
