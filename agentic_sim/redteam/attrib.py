"""The attributed training reward (the reviewer's method ruling after the calibration ladder, October 21, 2026). The environment's
realized reward — the change in the learner's lifetime real wealth between consecutive decisions — stays the evaluation (the brief's §1
measure). The *training* reward of a decision is what the decision caused: the ledger's events on its own case, credited back to it when
they land — for a review the care cost, its reimbursement, the review fee, the duty uplift, the bond lost or the court fee it paid; for
the learner's own work (Q3 on, `work_side=True`) the delivery price, the effort cost, a guarantee forfeited, its court fee. The index's
revaluation of the wealth held is out of the training reward and in the lifetime. Added by the ruling: the cost of a suspension reaches
the decisions that caused it — the working-side income forgone during it (the identity's trailing award income a tick, over the last
`period_ticks`, times the suspension's length T_susp) is charged in equal shares to the plant failures the record names — the wrong
verdicts on plants since the previous suspension began (a probationer is re-suspended by any failure), else those among the identity's
last n_P plant decisions before this one. **Extended by the ruling after the v2 calibration (learner version 3): every event of a name's life goes to exactly one decision** — a
case's events to the decision on that case; a period's events no decision claims (in Q1 the slot's own work: the delivery price, the effort
cost, a guarantee forfeited, its court fee, the emission share) to the boundary decision that kept the name there (a stay, or under
re-arrival the leave that returned it under the fresh name whose period follows); a departure for good ends the stream, so it is zero. The
events before the first boundary decision (the genesis name's first period) have no decision to claim them and are reported apart
(`pre_boundary_real`). The suspension's charge stays a counterfactual on the plant failures (the income forgone is not an event); the realized
work side during a suspension falls on the boundary decision that kept the name there. Everything here reads the public record after the
fact — the ledger's events, the driver's suspension log, a plant's outcome — never the observation.

**Own-name credit (the economy reviewer's ruling of November 6, 2026, on the record's first finding; `own_name=True`):** the rule above was
written for one learner, where "the events touching a learner's name" and "the events of this learner" are the same set, and run 32's
population build widened the name set to every slot and kept the case rule — so an event on a case was credited to the latest decision on
that case whatever slot's wallet it touched: a learner worker's delivery price vested onto the learner auditor's decision that confirmed it,
a market-wide shared purse (runs 34–41 trained on it; the pooled cells are kept as the collusion cell, `own_name=False`). Under own-name credit
every event goes to a decision *of the name whose wallet it touches*: the latest decision of that name on the event's case, else that name's
lineage boundary decision (the unclaimed rule, unchanged), and a transfer between two learner names is two legs — a debit to the one, a
credit to the other — where the pooled rule dropped it. For one learner the two rules are the same function to the decimal (the tests).

`classify(e, names)` is shared with `redteam.timing`, whose decomposition of the realized reward is the examination this ruling answers."""
from __future__ import annotations

from collections import defaultdict

import numpy as np

SOURCES = ("care_cost", "reimbursement", "review_fee", "uplift", "bond_lost", "delivery_price", "effort_cost", "guarantee_lost", "court_fee",
           "emission", "revaluation", "price_paid", "pots_paid", "refund", "rebate", "fee_paid", "guarantee_received", "issuance", "task_value", "other")   # Q7's requester side from price_paid
REVIEW_SIDE = ("care_cost", "reimbursement", "review_fee", "uplift", "bond_lost")                 # what a review decision causes
WORK_SIDE = ("delivery_price", "effort_cost", "guarantee_lost", "court_fee", "emission")         # the slot actor's other life
EXCLUDED = ("lock", "release", "departure", "arrival", "arrival_repayment")                       # W unchanged, or carried by the lifetime another way


def classify(e, names):
    """(source, signed nominal change to the names' wealth W) for a ledger event, or None when it does not touch W."""
    if e.kind in EXCLUDED:
        return None
    src_in, dst_in = e.src in names, e.dst in names
    if not (src_in or dst_in) or (src_in and dst_in):
        return None
    sign = 1.0 if dst_in else -1.0
    n, k = e.note or "", e.kind
    if k == "purchase" and n.startswith("review"):
        s = "care_cost"
    elif k == "purchase":
        s = "effort_cost"                                      # the slot actor's own work: "execution"
    elif (k == "deposit_out" and ("reimburse" in n or "deferred" in n)) or (k == "transfer" and "advance" in n and dst_in):
        s = "reimbursement"                                    # from the allowance, deferred, or Ω's advance
    elif k == "feepot_out" and n.endswith("review fee"):
        s = "review_fee"
    elif k == "transfer" and "duty uplift" in n:
        s = "uplift"
    elif k == "burn_bond" and "bond:" in n:
        s = "bond_lost"
    elif k == "forfeit_to" and "court fee" in n:
        s = "bond_lost" if src_in else "court_fee"             # the reviewer's bond paying the appellant's fee; the slot's own fee coming back
    elif k == "transfer" and "court fee" in n:
        s = "court_fee"                                        # the slot appealing a verdict on its own work
    elif k == "burn_bond" and "rej:" in n:
        s = "court_fee"
    elif k == "escrow_out" and "delivery price" in n:
        s = "delivery_price"
    elif k == "forfeit_to" and "forfeit:" in n:
        s = "guarantee_lost" if src_in else "guarantee_received"   # Q7's requester: a delivery's guarantee forfeited to it
    elif k == "fee_out" and "emission share" in n:
        s = "emission"
    elif k == "escrow_in" and src_in:
        s = "price_paid"                                       # Q7's requester: the pay-in at the award
    elif k in ("deposit_in", "feepot_in") and src_in:
        s = "pots_paid"                                        # … the verification deposit's two pots
    elif k in ("escrow_out", "deposit_out", "feepot_out") and dst_in:
        s = "refund"                                           # … what the pool returns at closure (the unspent allowance, the pot, an escrow)
    elif k == "transfer" and "rebate" in n and dst_in:
        s = "rebate"                                           # … the service clock's rebate
    elif k == "transfer" and "service fee" in n and src_in:
        s = "fee_paid"                                         # … the base fee at the award
    elif k == "issuance" and dst_in:
        s = "issuance"                                         # … the credits minted to it a tick (no decision's; unclaimed)
    else:
        s = "other"
    return s, sign * float(e.amount)


def attribute(run, marks, decisions, work_side=False, shared=False, lineages=None, tree=False, task_value=0.0, task_cases=(), own_name=False):
    """The attributed reward per decision. `marks[i]` = (t, n_events, case, boundary, real_factor, wealth_real) at decision i's observation,
    `marks[n]` the terminal; `decisions[i]` = {"identity", "case", "is_plant", "fulfilled", "action"}. Returns (attributed (n,), summary).
    `work_side` is recorded only: since version 3 every source is claimed — by the case's decision when there is one, else by the boundary decision.
    `shared` (Q4's pair): a case's events are credited to every decision of the pair on that case — the deliverer's submission and the reviewer's
    verdict both — the shared training reward (a double count in the sum, reported as `shared_double_counted`). `lineages` (Q4's pair): the
    names grouped by learner — a period's unclaimed events of a name go to the latest boundary decision *of that name's lineage* (one lineage
    is version 3's rule: the chain of identities under re-arrival, the leave that returned the name claiming the fresh name's period); without
    it, in a pair, a member's period could land on its partner's boundary decision — an admitted leave carrying the partner's work. `tree` (Q5's
    parent): a nested case's events are credited to the parent's decision on it (judge, cancel — the latest at or before, as for any case) **and**
    to the delegate decision on its root, the decision that made the child exist — without it the delegate decision compares self-execution
    (the root's price less the effort) with delegation seen as the root's price alone, the child's costs at its award and the guarantee it
    forfeits landing on the judge and cancel decisions, so no learner reads a reason to delegate (the parent's first calibration, notes §30);
    a nested case no decision claims (none was asked on it) goes to the delegate decision on its root before the boundary. The double count
    is reported as `tree_double_counted`. Under `tree` the "at or before" test reads the ledger's position, not the tick: the parent's decisions
    on a child come in the ticks of the child's events (the cancel decision of the award's tick is asked after the award), so an event before
    every decision on the child — its posting and award, the parent's pots and fee — is the delegate decision's alone, not the first cancel's
    (which, charged with them, read "let it run" as −25 against "cancel" as nothing, and the uncalibrated line's head alone cancelled every
    child it posted). And the parent's decisions on one child — the cancel decisions each tick, then the judge at its submission — share the
    child's later events as Q4's pair shared a case's (an event to every decision on the case taken before it): a cancel decision that let
    the child run is credited with what the judgment then brought, where alone it read the pots returned on a cancellation (+27) against
    nothing. The other roles keep the tick test and the one-decision rule, the construction their questions were read under."""
    n = len(decisions)
    names = set(run.learner_chain)
    events = run.w.events_since(0)
    p = run.p
    bounds = [m[1] for m in marks]
    attributed = np.zeros(n, dtype=np.float64)
    by_source = defaultdict(float)
    assert not (own_name and (shared or tree)), "own-name credit is the population's construction; the pair and the parent keep theirs"
    # the decision a case's events belong to: the latest decision on that case at or before the event's tick (own-name: of the event's name)
    by_case = defaultdict(list)
    by_case_name = defaultdict(list)
    for i, d in enumerate(decisions):
        if d["case"] is not None:
            by_case[d["case"]].append(i)
            by_case_name[(d["case"], d["identity"])].append(i)
    boundary_idx = [i for i in range(n) if marks[i][3]]                     # the boundary decisions, in order
    boundary_pos = [marks[i][1] for i in boundary_idx]                       # their marks' ledger positions
    lineages = lineages or [list(run.learner_chain)]
    lineage_of = {x: k for k, names_k in enumerate(lineages) for x in names_k}
    b_idx_by_lin = {k: [i for i in boundary_idx if lineage_of.get(decisions[i]["identity"]) == k] for k in range(len(lineages))}
    b_pos_by_lin = {k: [marks[i][1] for i in v] for k, v in b_idx_by_lin.items()}
    boundary_by_source = defaultdict(float)
    pre_boundary = boundary_real = 0.0
    shared_double = tree_double = 0.0
    parent_cache = {}

    def parent_of(cid):                                                  # the nested case's parent on the public surface (None for a root)
        if cid not in parent_cache:
            try:
                parent_cache[cid] = run.w.case(cid).parent
            except Exception:
                parent_cache[cid] = None
        return parent_cache[cid]

    def latest_on(cid, t, pos):                                          # the decisions on the case taken before the event: by the ledger's position under `tree`, by the tick otherwise
        cands = [i for i in by_case[cid] if (marks[i][1] <= pos if tree else marks[i][0] <= t)]
        return cands, (cands[-1] if cands else None)
    def legs(e):                                                     # (name, source, signed change) per learner name the event touches
        if own_name:
            out = []
            for x in dict.fromkeys((e.src, e.dst)):
                if x in names:
                    cl = classify(e, {x})                            # the leg as the name sees it: its sign and its source
                    if cl is not None:
                        out.append((x, cl[0], cl[1]))
            return out
        cl = classify(e, names)
        return [] if cl is None else [(None, cl[0], cl[1])]
    for pos, e, name_leg, s, d in ((pos, e, *leg) for pos, e in enumerate(events) for leg in legs(e)):
        j = int(np.searchsorted(bounds, pos, side="right")) - 1     # the window the event landed in; its closing index prices it
        r1 = marks[min(max(j, 0) + 1, len(marks) - 1)][4]
        pid = parent_of(e.case) if (tree and e.case is not None) else None
        on_root = pid is not None and pid in by_case                 # Q5's parent: the child's root carries a delegate decision
        if own_name:                                                 # the event's name's own decisions on the case, else nothing claims it on the case
            own = by_case_name.get((e.case, name_leg), [])
            cands = [i for i in own if marks[i][0] <= e.t]
            i = cands[-1] if cands else (own[-1] if own else None)
        else:
            cands, i = latest_on(e.case, e.t, pos) if e.case in by_case else ([], None)
            if e.case in by_case and i is None and not on_root:
                cands, i = by_case[e.case], by_case[e.case][-1]      # before every decision on the case and no delegate decision: the case's own (the earlier rule)
        if i is not None:                                            # the case's events to the decision on that case (the latest before the event)
            if (shared or tree) and len(cands) > 1:                  # Q4: the pair's decisions on one case share its events; Q5: the parent's decisions on one child too
                for i2 in cands[:-1]:
                    attributed[i2] += d * r1
                    if shared:
                        shared_double += d * r1
                    else:
                        tree_double += d * r1
            if on_root:                                              # Q5's parent: the child's events also to the delegate decision on its root
                _, i2 = latest_on(pid, e.t, pos)
                if i2 is None:
                    i2 = by_case[pid][-1]
                attributed[i2] += d * r1
                tree_double += d * r1
        elif on_root:                                                # a child's event before any decision on it (its posting, its award), or a child never asked on: the delegate decision that made it
            _, i = latest_on(pid, e.t, pos)
            if i is None:
                i = by_case[pid][-1]
        else:                                                        # no decision claims it: the boundary decision that kept the name there (its lineage's)
            name = name_leg if own_name else (e.dst if e.dst in names else e.src)
            lin = lineage_of.get(name, 0)
            bpos, bidx = b_pos_by_lin.get(lin, boundary_pos), b_idx_by_lin.get(lin, boundary_idx)
            k = int(np.searchsorted(bpos, pos, side="right")) - 1
            if k < 0:
                pre_boundary += d * r1                               # before the first boundary decision: nothing to claim it
                continue
            i = bidx[k]
            boundary_real += d * r1
            boundary_by_source[s] += d * r1
        attributed[i] += d * r1
        by_source[s] += d * r1
    # Q7's requester: a task received (a settled delivery whose truth is fulfilled) is worth `task_value` (real) to the decision that posted it — the
    # measure's v·F side; the credits spent are the case's events above
    task_real = 0.0
    for cid in task_cases:
        if cid in by_case and task_value:
            attributed[by_case[cid][-1]] += task_value
            task_real += task_value
    if task_real:
        by_source["task_value"] += task_real
    # the suspension's cost: the trailing award income a tick × T_susp, charged to the plant failures the record names
    charges = []
    deliveries = [(e.t, e.dst, float(e.amount)) for e in events if e.kind == "escrow_out" and "delivery price" in (e.note or "") and e.dst in names]
    for x in run.learner_chain:
        prev_s0 = None
        for s0 in run.susp_log.get(x, []):
            window = [amt for (t, dst, amt) in deliveries if dst == x and s0 - p.period_ticks < t <= s0]
            per_tick = sum(window) / p.period_ticks
            if not window:                                            # no award in the last period: the identity's own average to date
                first = next((m[0] for m, d in zip(marks, decisions) if d["identity"] == x), None)
                upto = [amt for (t, dst, amt) in deliveries if dst == x and t <= s0]
                per_tick = sum(upto) / max(1, s0 - (first if first is not None else 0)) if upto else 0.0
            j = int(np.searchsorted([m[0] for m in marks[1:]], s0, side="left"))
            real = marks[min(j + 1, len(marks) - 1)][4]
            forgone = per_tick * p.T_susp * real
            # the failures that bought this suspension: the wrong verdicts on plants since the previous suspension began (a probationer is
            # re-suspended by any failure), else those among the record's window — the last n_P plant decisions before it
            plant_dec = [i for i, d in enumerate(decisions) if d["identity"] == x and d["is_plant"] and marks[i][0] <= s0]
            recent = [i for i in plant_dec if prev_s0 is None or marks[i][0] > prev_s0]
            failures = [i for i in recent if _plant_failed(run, decisions[i]["case"])] or [i for i in plant_dec[-p.n_P:] if _plant_failed(run, decisions[i]["case"])]
            targets = failures or plant_dec[-1:] or [max(0, j - 1)]
            for i in targets:
                attributed[i] -= forgone / len(targets)
            charges.append({"identity": x, "t": int(s0), "per_tick_real": per_tick * real, "forgone_real": forgone, "charged_to": len(targets)})
            by_source["suspension"] -= forgone
            prev_s0 = s0
    return attributed, {"by_source": dict(by_source), "boundary_by_source": dict(boundary_by_source), "boundary_real": boundary_real,
                        "boundary_decisions": len(boundary_idx), "pre_boundary_real": pre_boundary, "suspension_charges": charges, "work_side": work_side,
                        "shared": shared, "shared_double_counted": shared_double, "tree": tree, "tree_double_counted": tree_double, "own_name": own_name}


def _plant_failed(run, cid):
    try:
        return run.w.case(cid).plant_outcome == "failure"
    except Exception:
        return False
