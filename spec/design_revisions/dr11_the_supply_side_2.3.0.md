# Agentic Economics — The Task, Verification, and Dispute Loop

## Design revision 11 — specification 2.3.0-rc.2: the supply side

**Project:** ELEF / Agentic Economics  
**Version:** 2.3.0-rc.2 — a release candidate, not yet in force. rc.1 (October 19) was the sketch as first sent; rc.2 settles the implementation review [I24]: two corrections (the §6 child must be an admitted member; a nested request has carried no pots since 1.1.0 and drew on the root's — now **the parent posts the pots**, a §19 decision this revision makes, answering §18.1 Q3), and six readings taken into the text — among them admission on $n_{\min}$ **bad** plants, four conditions for a clean departure, and "never nested" read as deliveries only. On acceptance it becomes **2.3.0**, consolidated into one standalone text, and 2.2.0 moves to history.  
**Prepared:** October 19, 2026 (rc.1–rc.2)  
**Supersedes:** 2.2.0 where this document speaks; everywhere else 2.2.0 stands unchanged — the bank, the state's expected cost and its price at $\bar B$, the rebate from income, the index per period, the price, the lock, and all of 1.x about honesty. §9 (delegation) stands as written since v1.0; this revision gives it a reason to run.  
**Nature of this revision:** A **design revision** (minor, by §19) — the first since 1.4.0 to add something actors may *do*. Fifteen runs had a fixed population: the twenty actors of tick 0 were the twenty of tick 1,000, with one cost between them. Run 13 found the lever on the price — **supply**: 20 honest members give 22.5, 30 give 11.6, 40 give 10.9 — and found that nothing in the rules could move it, because nobody could arrive. Run 12 found that delegation could not run, because with one cost for everyone there is no gain from trade. This revision opens both: **entry and exit** as public operations — an arrival enters as a probationer, with a float the bank mints by rule, and becomes a member only when its inspection record says so; a departure takes its wallet out of the economy — and **competence**: a cost per unit of work drawn once per actor from a wide spread, private to the actor, revealed only through its bids, so that a dear actor gains by paying a cheap one and delegation has a reason to exist. The troops never take a nested request. One ruling from run 15 is carried in: a reviewer's reimbursement advance may draw on the rebate pool — verification before the state's blame.  
**Design assumptions, unchanged:** humans do not intervene; troops bear no malicious intent; the bank is not an actor; the economy is closed. **New, stated:** an actor's competence is its own, like its effort cost — a reservation price, not a rule's parameter, and not a quality: a cheap actor is not a worse one in this revision.  
**Status:** Proposed. Accompanied by what required it (§1) and the runs that test it (§8).

> **Money enters with requests. Truth enters with requesters — and with the orchestrator's own planted work.**
>
> **Workers enter through inspection.** *(new)*

---

## 1. Why: what runs 12–15 said

1. **The price is the quantity's, and the quantity is the strategy's until members can enter [S13].** Where free members are scarce the margin rule ratchets until a free member wins one award per 3.6 ticks and the price is whatever makes the customers buy at that rate — 34 against a cost of 8 at 60/40, the cap when the customers bid above the market. Adding workers takes it to cost: 22.5 / 11.6 / 10.9 at 20 / 30 / 40 honest. But the twenty actors were given, and nothing in the rules admitted a twenty-first. The lever was outside the loop.
2. **Honest earnings fall with headcount [S13]** — 1,446 → 830 → 589 real at 20 / 30 / 40 — so entry on earnings is self-limiting: the thing that invites a worker is the thing more workers destroy. Supply will find a level if it is let.
3. **Delegation has never run [S12].** With one cost for every actor a child bids no lower than its parent would, and the parent pays the nested overhead for nothing. §9 has stood since v1.0 untested; 2.0.0 deferred it to "heterogeneous costs" and that is here.
4. **A customer who posts at the market price gets the state [S13, S15].** The members' ratchet bids sit above $\bar B$, so a request at $\bar B$ waits $w_A$ and goes to a troop — the state at 52–75% in those cells, the cheapest markets in the programme, paid for by the state's margin. Under entry the question is whether a newcomer bidding at its cost takes that work back.
5. **The state's books are clean enough to read supply against [S14, S15]**: neutral deliveries, the loans line empty in a quiet market and nearly empty in a riot, the lateness bill read and sized to income.
6. **Baruchi's positions [C-2.3]:** entry on earnings — agreed; arrivals **as probationers** — agreed; the competence spread — "not sure, what do you think?" — wide, swept, cost only, private (the design reviewer's answer, §2.3).

**Classification.** A design revision: two new public operations (arrive, depart), one new mint (the arrival float), one restriction on the summons (never a nested request), and a declared per-actor cost in the drivers. The rules of honesty, the record, probation, the price, the lock, the bank and the rebate are untouched; §9 is untouched. Minor, by the rule.

**Recorded and rejected.** *Arrivals as undetermined members* (the genesis reading of 1.3.0 §2.2: may win awards, odds pinned, no panel seats until determined): a suspended stamper would depart and re-arrive to deliver again — entry as the way around the record. *An entry bond* (a stake posted to arrive): deters the honest poor as much as the dishonest, and probation is already the gate. *A membership fee to ELEF*: a tax on supply where supply is the lever. *Competence coupled to quality* (a cheap actor fails more often): a real question and a second dimension; held for its own revision so the first read is clean. *Competence visible in the view*: the market discovers it through bids, or it is not a market; and §14 keeps actors from reviewers. *Troops taking nested requests*: the state inside a member's margin — the state would become every parent's child.

---

## 2. The rules

### 2.1 Entry: an arrival is a probationer with a float

**Rule — arrive.** `arrive` is a public operation of `World`: the orchestrator admits a new actor with a fresh identity, no record, and a **float** — $F_0=50$ at $P_0$, indexed at the arrival tick, **minted by the bank** (`arrival`, a source; the mirror of `departure`), as the genesis actors had theirs. Nothing else is asked of it: no stake, no fee, no sponsor.

**Rule — the arrival is a probationer.** An arrival enters in the state 1.3.0 §2.2 defines for a suspended actor after $T_{\text{susp}}$, **without the suspension**: it serves **initial reviews only** — no appeal, dispute or audit seat; it is seated as any duty actor is and receives plants at the ordinary rate, mixed with work it cannot tell apart; its **audit odds are pinned at 1**; a plant failure restarts its probation; it **wins no award**. It is **admitted to membership** — new awards, duty as a member — when its trailing record passes $\theta_{\text{duty}}$ with at least $n_{\min}$ **bad** plants adjudicated — the kind that tests a reviewer, so that an arrival whose first plants all happen to be good (one in 250 at $\beta_P=0.75$) is not admitted untested; panel seats when it passes $\theta_{\text{panel}}$, as 1.2.0 has it. 1.3.0's readmission of the suspended, which counts outcomes of both kinds against a record that already exists, is unchanged. **One record, one meaning**: the arrival's record is the record of 1.2.0 §2.2, and admission is readmission without a prior suspension. **An arrival wins no award of any kind** — a nested request refuses a probationer as a root does.

**Consequence — entry's first effect is on inspection, its second on the price.** An arrival reviews from its first tick on duty and delivers only after its record is determined — about four bad plants adjudicated, some fifty audited reviews, 250 ticks on duty at the 1.3.0 reading. So a wave of arrivals relieves the review seat at once (1.6.0: the seat, not the treasury, caps the market) and the price only a period or two later. **Time to membership** is a reading, and it is the cost of the gate; the gate is the thesis. An arrival earns while it waits — the fee and uplift on the reviews that stand, about $+1.2$ a review at $m=2$ (1.3.0 §2.2) — so probation is not unpaid, only unawarded.

**Consequence — entry is not the way around the record.** A suspended actor that departs and arrives anew is a probationer with no record and no hoard: it has given up its wallet (§2.2) to stand where it already stood. Identity cycling buys nothing, and §8 checks it.

### 2.2 Exit: a departure takes its wallet out

**Rule — depart.** `depart` is a public operation of `World`, admissible when **no obligation to or from the actor is live**: no commitment, no active review, no completed review awaiting its settlement (its fee, uplift and bond release pay at the case's batch, to a wallet that must still exist), no lock — guarantee, bond or nested escrow in flight — and no claim on Ω naming the actor (a deferred reimbursement, §4.3); otherwise refused whole, and the actor finishes what it holds by the ordinary rules and departs after. An actor on duty leaves duty as it departs, and the rotation refills the seat as it does for a suspension. Its unlocked wallet leaves $M$ as `departure` (the kind 2.0.0's acceptance ruling made for a requester; one kind for both). Its identity and record are archived, never reused, and never consulted for a later arrival. A suspended actor or a probationer may depart; the record stays archived against the identity that earned it.

**Consequence.** Who leaves is the strategy's — earnings below a reservation for a period, in the default. The rules make leaving clean and returning expensive, and leave the rest to the market.

### 2.3 Competence: a cost per unit of work, drawn once, private, wide

**Rule — in the rules.** Nothing. An actor's effort cost $c_D$ has been its own since 2.0.0 §2.3 — a reservation price, nominal, declared in the strategy, burned at submission through `spend`, never the engine's to index or to know. This revision makes it **differ across actors**, and the difference is the drivers' to declare and the view's to keep hidden: **the public view exposes nothing per actor** — no cost, no wallet, no record field; the market sees bids. The History (§13) is public and append-only as it has always been, and an effort burn is in it under the actor's id with its amount: a strategy that read the ledger could learn a cost at an actor's first submission, as a market participant reading public accounts can. Declared strategies read the view (the drivers' convention); the record is not changed to hide a burn, because hiding amounts in the authoritative record would cost more than it protects — and in the system itself an agent's effort is its own compute, in no ledger at all.

**Declared default (the drivers').** Each actor's $c_D$ is **drawn once at its creation** — at genesis or at arrival — from a **log-normal around the anchor**: median 8 (so every 2.x figure compares), $\sigma=0.43$, clipped to $[2,40]$; at that $\sigma$ the cheapest tenth of actors is about three times cheaper than the dearest tenth (10th percentile ≈ 4.6, 90th ≈ 13.9). **Swept** $\sigma\in\{0.2,\ 0.43,\ 0.8\}$ — narrow, default, wide — so the run says where delegation starts to pay rather than the text. The bid policy is unchanged: $c_D(1+m)$ with the margin dynamics of 2.0.0. The care cost of a review (the driver's 2–3) is **not** spread in this revision. **Cost only**: competence touches neither an actor's fail rate nor its honesty disposition.

**Consequence.** With a spread, two things the rules have always allowed begin to happen. *Selection*: a cheap arrival undercuts the ratchet, wins, stays; a dear member watches the price fall below $c_D(1+m_{\min})$, earns nothing, leaves — the population's median cost falls and the price with it. *Trade*: a dear parent awarded $B$ gains by paying a cheap child $B'$ when $c_A > B' + \text{overhead}$ — the child's pots and fee, the parent's care in judging — which at the default spread is the dearest sixth of parents against the cheapest sixth of children, and at the wide spread most of the market.

### 2.4 Delegation under competence; the troops never nested

**Rule — §9 stands.** A nested request is a full loop (§9.1): posted by a committed parent at $\beta'$ with $\text{root}(q')=\text{root}(q)$, locking $\beta'+G^V$ at the posting index (2.0.0's posting lock is §9.1's model); awarded at the child's bid $B'$; the child locks its guarantee; **the parent judges the child** and its judgment is the initial verdict; the rejection bond, the appeal, the kill fee, pool exhaustion and the exits of §9.3 as written. The child's work is reviewed, audited and planted as any case's is.

**Rule — the parent posts the pots.** Since 1.1.0 §4.3 a nested case has carried no pots of its own — $\varphi^E=\varphi^F=0$ — and its reviews drew on the **root's** deposit, so that a root requester paid for the inspection of work a parent chose to delegate, and a tree of two or three exhausted the root's allowance and had Ω advance the rest. That was written when delegation did not run. **From this revision a nested request is a full loop in money as in procedure**: the parent posts the two pots at the nested posting index, locked with its all-in as a root's are (2.0.0 §2.1: $\beta'+\varphi^{E\prime}+\varphi^{F\prime}+\omega_0 m_t\beta'$, plus the §9.1 rejection bond $G^V$); the pots pay the child's reviewers and audits and refund to the parent at the nested case's closure as a root's refund to its requester. The root's deposit pays for the root's inspection only. **§18.1 Q3 — should the pots grow with the tree — is answered: they grow by one pair per node, posted by the node's requester.** The 1.1.0 reading (the children on the root's pots) is the control.

**Rule — the troops never *deliver* a nested request.** The per-request summons (1.7.1) reads **root requests only** for deliveries — as the engine has read it since 1.4.0; this revision writes it down. A nested request past $w_A$ is the parent's problem, as §9.3 has it: self-execute, cancel, or withdraw as pool exhaustion. The state is not inside a member's margin. **Review seats on nested cases stay the troops'** when the market cannot seat them — 1.6.0's inspection first applies to a child's initial review and audit as to a root's; a child's inspection in a thin market does not wait on the parent.

**Rule — nested requests have no service clock.** The clock and the rebate are the root's (1.6.0 §2.1); a parent that waits is not late to anyone but itself.

**Consequence — accountability cascades, now tested.** A careful parent that catches a child's bad work rejects, the child forfeits to the parent, and the child may appeal against the parent's bond; a stamping parent that passes it forfeits upstream with no recourse (§9.2). Under competence the dear parent is also the one with the most to gain from delegating, so the question §9 was written to answer — *does the chain hold when the one judging has paid for what it judges?* — finally has cases. A **broker** — a parent that delegates most of what it wins — is a structure the rules permit and have never met; §8 looks for it, and reads its accountability, not its existence, as the finding.

### 2.5 What an outsider may read

**Rule.** The public view (`drivers.view.Public`) offers, to an actor outside the market as to one inside it: $P_t$, $\bar B$, the members' count and the free members, posts a tick, the state's share, the mean time to membership of the last period's admissions, and the on-time share. Nothing per actor: no costs, no wallets, no records. The entry decision is a declared strategy made on these.

**Declared default (the drivers').** An **entry pool** of candidates, each with a cost drawn from §2.3's distribution and a **reservation** $r$ in real earnings a tick (default 0.8); a candidate arrives when its expected earnings from the view — $(\bar B - c_D)$ times the awards a free member wins a tick, discounted by the time to membership — exceed $r$, at most one arrival a tick; a member departs when its trailing period's real earnings fall below $r$ and it holds no obligation. Both are strategies; the swept variants are §8's.

### 2.6 Ruling carried from run 15 — verification before the state's blame

**Rule.** A reviewer's §4.3 reimbursement advance, when the allowance is exhausted, **may draw on the period's rebate pool** during the period; the pool at the close is net of advances paid. Inspection never waits on the state's cash (2.1.0: seats always lent for, plants minted) and does not wait on the customers' rebate settlement either. The two reviewer tests that waited (`test_review_06`, `test_r4_08`) return.

### 2.7 Defaults

| Default | Value | Note |
|---|---|---|
| `arrive` | a fresh identity, no record, a float $F_0=50$ at $P_0$ indexed, minted by the bank (`arrival`) | a probationer (1.3.0 §2.2 without the suspension) |
| Admission | trailing record passes $\theta_{\text{duty}}$ with $\ge n_{\min}$ **bad** plants adjudicated; panels at $\theta_{\text{panel}}$; no award of any kind before | 1.3.0's readmission, no prior suspension; readmission itself unchanged |
| `depart` | admissible with no live obligation to or from the actor (commitment, active or unsettled review, lock, claim on Ω); off duty as it leaves; the wallet leaves as `departure`; the record archived, never reused | one kind for actors and requesters |
| $c_D$ (drivers') | log-normal, median 8, $\sigma=0.43$, clipped $[2,40]$, drawn once per actor; swept $\sigma$ 0.2 / 0.43 / 0.8 | private; cost only |
| Entry pool (drivers') | 20 candidates; reservation $r=0.8$ real a tick; at most one arrival a tick; depart after one period below $r$ | swept $r$ 0.5 / 0.8 / 1.2; cap 1 / 3 a tick |
| Summons | deliveries for root requests only; review seats on nested cases as on roots | nested past $w_A$ is the parent's (§9.3) |
| Nested pots | posted by the parent at the nested posting index, refunded to it; control: the 1.1.0 reading (the children on the root's pots) | `nested_pots parent|root` |
| Nested clock | none | the clock is the root's |
| Outsider's view | $P_t$, $\bar B$, members, free, posts a tick, state's share, time to membership, on-time share | nothing per actor |
| Reviewer advance | may draw on the rebate pool | run 15's ruling |
| Everything else | as 2.2.0 | |

---

## 3. Consequences and hypotheses

**Hypothesis 1 — entry takes the price toward cost, after the gate.** At 60/40 with the entry pool: arrivals begin within the first period (expected earnings at $\bar B\approx30$ against costs of 5–13 clear $r$ by a wide margin); the first admissions at about tick 300–400; $P_t$ falls from 34 toward 12–18 by the run's end as the members' count passes 20; the state's share falls from 38% toward 10%; the honest's real earnings per member fall toward $r$ and arrivals stop — supply finds its level. Against run 15's fixed population on the same seeds.

**Hypothesis 2 — entry relieves inspection first.** Reviews waiting and the eligibility shortfall fall within a period of the first arrivals, before any arrival is admitted; the duty cap, two thirds of a larger unsuspended list, seats more members; false approvals do not rise while probationers with pinned odds carry the initial reviews.

**Hypothesis 3 — selection.** Under the default spread the population's median cost falls over the run (arrivals cheaper than the incumbents are admitted; incumbents dearer than the falling price depart); under the narrow spread it does not move; under the wide spread it falls further and faster. The price follows the median cost of the *members*, not of the population.

**Hypothesis 4 — delegation runs where the spread is wide, and not where it is narrow.** The share of awards under which a nested request is posted: near zero at $\sigma=0.2$, a few percent at 0.43, a fifth or more at 0.8; the gain from trade on a delegated case ($B-B'-$ overhead) is positive in the mean where it runs; a parent that delegates most of what it wins — a broker — appears at 0.8 and is read: how many, their cost rank, their share of the market.

**Hypothesis 5 — the chain holds.** On nested cases: a careful parent's rejection of a child's bad work is upheld on appeal at the panel's ordinary rate; a stamping parent's wrongful acceptance forfeits the parent's guarantee upstream; false approvals on nested cases are within noise of roots; wrongful rejections (overturned on appeal) are rare because the rejection bond pays the child's court fee. The lagging auditor stays zero.

**Hypothesis 6 — identity cycling buys nothing.** A suspended stamper that departs and arrives anew is admitted no sooner than one that serves its probation, and ends poorer by its surrendered wallet. A swarm of stamper arrivals fails probation at the first bad plant and costs the market only the audits of its pinned reviews.

**Hypothesis 7 — honesty is unmoved by supply.** False approvals, suspensions and readmissions within noise of run 15 at every entry cell; the record's gate does not weaken as the population grows.

**Hypothesis 8 — the circuit begins to close.** Where delegation runs, credits flow member to member through nested awards; the members' hoards relative to $M$ fall against run 15; "a pipe from the mint to hoards" (2.0.0 §3) becomes a loop with a second turn. Read, not promised: at the default spread the second turn is small.

**Hypothesis 9 — the state and entry answer the same riot differently.** Under the crowd of thirty with the entry pool, arrivals come but are not admitted before the crowd leaves; the state carries the riot as in run 15, and the arrivals carry the inspection; the price after the crowd is lower than run 15's, because the admitted arrivals stay.

---

## 4. What does not change

Everything in 2.2.0: the bank and its three jobs, the loans, the debt, the wall; the state's expected cost and its price at $\bar B$; the rebate from the period's income; the index per period; every refusal told; the price, the lock, $N_T$, the crowd, the below-market flag; and everything in 1.x about honesty — the record, suspension, probation, plants, the dial, panels, the duty cap, troops and their per-request summons. §9 as written. What changes is who is in the market, and that they differ.

---

## 5. Invariants, notation (amendments)

**I1 (amended).** Sources gain `arrival` (the bank's, at `arrive`); `departure` covers actors and requesters.
**I33 (new) — entry through inspection.** An arrival holds no award — root or nested — and no panel seat until its trailing record passes the thresholds with $\ge n_{\min}$ bad plants adjudicated; its audit odds read 1 until then; its float is minted once, at arrival, at the arrival index; the public view exposes nothing per actor.
**I34 (new) — a clean departure.** `depart` is refused while any obligation to or from the actor is live — a commitment, an active or unsettled review, a lock, a claim on Ω; on departure the actor leaves duty, its unlocked wallet leaves $M$ as `departure`, and its identity never reappears.
**I35 (new) — the summons is for roots.** No troop is summoned to *deliver* a nested request; seats are as on roots.
**I36 (new) — the pots grow with the tree.** Every case, root or nested, carries its own two pots, posted by its requester at its posting index and refunded to it; a child's reviews never draw on its root's deposit.
**I32 (amended).** The pool may pay a §4.3 reviewer advance during the period; the close settles claims from the pool net of advances.
**I28, I30** stand; `arrival` is a minting by rule, listed with issuance, emission and plants.

**Notation (Appendix C).** `arrive`, `depart`; the float $F_0$; the entry pool; the reservation $r$; time to membership; a broker (a parent delegating most of its awards — a reading, not a status); the gain from trade $B-B'-$ overhead.

**§18.1.** *Q5* opened at last: delegation under competence. *New Q20*: entry — time to membership, the price under supply, selection. *New Q21*: the chain under delegation — the parent as judge. *Q7, Q10* untouched.

---

## 6. Worked example

Twenty actors at genesis, 60/40, costs drawn at $\sigma=0.43$ — the eight members' costs 5, 6, 7, 8, 8, 9, 11, 14; the stampers' similar. Tick 300, $P_t$ 33, $\bar B$ 30, three members free, posts 1.9 a tick, the state at 38%. An entry pool of twenty candidates with costs from 3 to 19.

**An arrival.** A candidate with cost 5 reads the view: $\bar B-c_D=25$ an award, a free member wins about 0.27 awards a tick, time to membership about 250 ticks — expected earnings well above $r=0.8$. It arrives; the bank mints its float, $50\times33/20=83$; it is a probationer: seated for initial reviews, every approval audited, plants at the ordinary rate. It earns review fees and uplift, about $+1.2$ a review, and wins no award. At tick 560, four bad plants adjudicated and its record at 0.5, it is admitted; it bids $5\times1.0=5$ on the oldest request against the incumbents' ratchet bids of 29 and the state's $\bar B$ of 30, and wins at 5. $\bar B$ begins to fall. Over the next two periods six more candidates with costs 3–8 arrive and are admitted; by tick 900 the members number fifteen, $P_t$ is 14, the state's share 9%, and the honest real earnings per member about 0.9 a tick — just above $r$; the remaining candidates, costs 10–19, read earnings below $r$ and do not come.

**A departure.** The incumbent with cost 14 has won nothing since tick 700: the price is 14 and its bid floor is $14\times1.0$. Its trailing period's earnings are 0.2 a tick, below $r$. It holds no commitment, no review, no lock; it departs; its wallet of 1,100 leaves $M$ as `departure`; its record is archived. Had it been mid-review, the departure would have been refused until the review settled.

**A delegation.** The incumbent with cost 11 wins a request at 20 (its bid at $m=0.8$). Its own margin is 9. It posts a nested request at $\beta'=9$, locking $9+G^V$; the arrival with cost 3 — admitted at tick 620, a member now — bids $3\times1.3=3.9$ and wins; the parent's lock releases $9-3.9$ and the fee on the difference. (A probationer could not have bid: no award of any kind until admitted.) The child delivers; the parent judges — carefully, it is a careful actor — and approves; the child's work is audited at the member's ordinary odds, stands, and vests to the child. The parent submits its own delivery, built on the child's, and vests at 20. The parent's take: $20-3.9-$ the nested fee $\omega_0\cdot3.9$ $-$ the nested pots' net cost, about 1.5 (posted by the parent, §2.4, refunded less what the child's reviewers drew) $-$ its care in judging, about 2 — some 12, against 9 had it done the work itself. The root requester's deposit paid for none of it. The gain from trade, about 3, is the spread between its cost and the child's bid, less the overhead. **Had the parent been a stamper** and the child's work bad, the parent approves, builds on it, and forfeits its own guarantee upstream with no recourse (§9.2) — the chain holds at the parent's expense. **Had the parent rejected good work** to collect the child's guarantee, the child appeals against the parent's rejection bond and the panel overturns at its ordinary rate; the bond pays the child's court fee and the rest burns.

**A cycler.** A stamper suspended at tick 400 departs at tick 420 with a wallet of 190 (gone from $M$) and arrives anew at tick 421 with a float of 83 and no record. It is a probationer — initial reviews, pinned odds, no awards — exactly where it stood, 107 credits poorer; its first bad plant restarts its probation as before. It is admitted, if ever, no sooner than it would have been readmitted.

---

## 7. Implementation note (no code here)

- **One flag.** `Params.supply`; off is 2.2.0 for the goldens.
- **`arrive(name)` / `depart(name)`** on `World`: `arrive` creates the actor with `probation=True`, `since_susp=0`, `susp_started=t`, odds pinned, and mints the float through `BANK` (`arrival`, $F_0\times P_t/P_0$); the 1.3.0 probation code applies, with admission on $n_{\min}$ **bad** plants (a one-word variant of `record_passes` for arrivals; readmission unchanged); `award` refuses a probationer on a nested request as on a root. `depart` validates the four conditions whole, takes the actor off duty (the rotation refills), moves the unlocked wallet out as `departure`, archives the identity and refuses it to `arrive` forever; refused otherwise with no effect. `admissions` and `time_to_membership` counted apart from `readmissions`.
- **Nested pots.** `post_nested` locks $\beta'+\varphi^{E\prime}+\varphi^{F\prime}+\omega_0 m_t\beta'+G^V$ at the nested posting index from the parent; the nested case's reviews draw on its own pots; refunds to the parent at closure; `Params.nested_pots parent|root` (root = the 1.1.0 reading, the control); I36. The reading per delegated root: how much of the root's deposit the children took (zero by construction under `parent`) and how often Ω advanced.
- **The summons** for deliveries reads roots only, as the award pass has since 1.4.0 (`c.is_root`); I35 pins it; the seat pass keeps no root filter. `_reimburse`'s advance draws on Ω's unlocked balance and then on the pool lock (the run 15 ruling); the close nets it; the remainder released at the close keeps 2.2.0's order.
- **Costs are the drivers'.** Each actor's `c_d` drawn once (`--c-d-sigma`, `--c-d-median 8`, `--c-d-clip 2 40`, seeded) and used in its bid and its `spend`; the engine never sees it. The public view exposes nothing per actor.
- **The entry pool is a driver** (`drivers/entry.py`): `--entry-pool 20 --reservation 0.8 --arrivals-per-tick 1 --exit-patience 1`, candidates' costs drawn from the same distribution, decisions on `view.market()` — the §2.5 fields, two of them new: `time_to_membership` (mean over the last period's admissions) and `members_free`.
- **Delegation is a driver** (`drivers/delegate.py`): a committed parent posts a nested request when $c_A > \bar B'_{\text{expected}} + \text{overhead}$, at $\beta'=$ its margin less the overhead; children bid as members do; the parent judges by its disposition (careful / stamper); §9.3's nested-first priority is the driver's selection order; `--delegation on|off`.
- **Readings.** Per period: arrivals, admissions, departures, time to membership (mean, max), members' count, the members' and the population's median cost (the driver's, from its own declaration — a reading of the strategy, not the view), nested requests posted / awarded / self-executed / cancelled / pool-exhausted, the gain from trade (mean), brokers (parents delegating $>$ half their awards: count, cost rank, share), nested false approvals and overturns, hoards / $M$.
- **Tests.** `test_v23`: `arrive` mints once through the bank and creates a probationer that wins no award and holds no panel seat until admitted; admission at the record's thresholds; `depart` refused with a commitment, a review, a lock; departure's wallet out as `departure`; the summons skips a nested request past $w_A$; the reviewer advance from the pool and the close net of it; the two reviewer tests return (`EXPECTED_FAIL` 28); a probationer refused a nested award; a departure refused for an unsettled review and for a claim on Ω; a nested case's reviews paid from its own pots and the root's deposit untouched; the §6 arrival, departure, delegation and cycler reproduced in the six-actor world. Goldens re-pinned once.

---

## 8. After acceptance — the runs

Every comparison in real terms, from the second period on, against run 15's cells on the identical seeds (fixed population, one cost). Every cell names its requester policy, $K_{\text{open}}$, $\sigma$, and the entry pool.

1. **Reproduce §6.**
2. **Entry** at 60/40 and 80/20, wallet rule, $K_{\text{open}}$ 5, $\sigma=0.43$, the pool of 20 honest candidates: arrivals and admissions by period, time to membership, members' count, $P_t$, the state's share, reviews waiting, honest real earnings per member, honesty (Hypotheses 1, 2, 3, 7).
3. **The spread** without entry, 20 honest, $\sigma\in\{0.2,0.43,0.8\}$, delegation on and off: nested share, gain from trade, brokers, nested false approvals and overturns, hoards / $M$ (Hypotheses 4, 5, 8). At $\sigma=0.8$ also `nested_pots root` — the 1.1.0 reading as the control: how much of the root's deposit the children's inspection took, how often Ω advanced, and whether the parents delegate more when the root pays for it.
4. **Entry and the spread together** at 60/40, $\sigma\in\{0.2,0.43,0.8\}$: the members' median cost over the run, $P_t$, who departs (Hypothesis 3).
5. **Knobs**: the reservation 0.5 / 0.8 / 1.2; arrivals a tick 1 / 3; the float 0 / 50 (a floatless arrival must earn its first bond on duty — can it?).
6. **The riot with entry**: the crowd of thirty at 60/40 with the pool — the state's share, arrivals during the crowd, admissions after, $P_t$ after against run 15 (Hypothesis 9).
7. **Red team**: the cycler (a suspended stamper departs and re-arrives) against one that serves its probation; a swarm of twenty stamper arrivals (review demand, false approvals, time to their first suspension); a parent that rejects good child work for the guarantee (the appeal rate and the bond); a child that bids below cost to win and misses (the kill fee, the parent's pool exhaustion); a broker that stamps its children's work (the forfeit upstream, its reliability).
8. **Told and the busy line** under entry: the marks, lateness and the forgone share as members arrive — does supply empty the busy line?

---

## 9. Provenance

**[S12]** delegation cannot pay with one cost; **[S13]** supply is the trigger and the cure (22.5 / 11.6 / 10.9), honest earnings fall with headcount, a request at $\bar B$ goes to the state; **[S14, S15]** the state's books neutral and read, the loans line empty, the lateness bill sized to income. **[C-2.3] Design discussion (October 19, 2026).** The design reviewer's three questions and Baruchi's answers: *what makes an honest member arrive — earnings, self-limiting since they fall with headcount*: "agreed"; *does a newcomer start as a member or a probationer*: "agreed, as probationer"; *the competence spread, wide or narrow*: "not sure, what do you think?" — the design reviewer: wide and swept (too narrow and nothing happens; wide is what the real market looks like; wide is where selection and brokers live), cost only, private, arrivals from the same distribution; Baruchi: "ok, let's draft 2.3.0". The reviewer's own question had said an arrival "can deliver" while on probation; the draft takes the strict reading — a probationer wins no award, as 1.3.0 defines it — because the loose one is entry as the way around the record (§1, recorded and rejected). **2.0.0 §2.7** deferred delegation to heterogeneous costs with the questions this revision opens. **[S15 §7]** the reviewer-advance ruling. **[I24] Implementation review of rc.1 (October 19, 2026)** — implementable, with two corrections and six readings. The corrections, adopted: the §6 child was a probationer and a probationer wins no award — the child is now an admitted member audited at ordinary odds, and `award` refuses a probationer on a nested request as on a root; a nested case has carried no pots since 1.1.0 §4.3 and drew on the root's deposit, so a root requester paid for inspection it did not choose and Ω advanced for trees of two or three — resolved as a rule (§2.4): the parent posts the pots, a nested request a full loop in money, §18.1 Q3 answered, the 1.1.0 reading kept as the control. The readings, taken as written: the cost is hidden by the view and not by the record (the ledger stays public; declared strategies read the view); a clean departure needs four conditions and takes the actor off duty; admission on $n_{\min}$ **bad** plants (the reviewer's choice of the one word; readmission unchanged); the summons for deliveries has read roots only since 1.4.0 and seats on nested cases stay the troops' — "never nested" means deliveries; admissions counted apart from readmissions; §2.6 as written, the two reviewer tests returning.

---

## Closing statement

> For fifteen runs the market was twenty actors who could neither leave nor be joined, and who all cost the same. The price they set was theirs to set. This revision opens the door both ways and lets the actors differ. Whoever comes in comes in through inspection — reviewing before earning, audited on every verdict, admitted when the record says so — and whoever leaves takes their money and leaves their name. Between them, for the first time, there is a reason to trade: the dear may pay the cheap, and answer for the result. If the price falls, it was supply; if a broker appears, the chain is what we read; and if the honest earn less for it, that was always the price of a market that works.
