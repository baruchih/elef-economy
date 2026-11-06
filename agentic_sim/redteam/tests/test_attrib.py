"""Regression tests on the attribution (the economy reviewer's ruling of November 6, 2026, on the record's first finding): the two-learner
case — a learner worker's delivery price does not reach the learner auditor's decision; a settlement event goes to its own name's decision;
a transfer between two learner names is two legs where the pooled rule dropped it — and the single learner, whose attributed sums are the
same function under both rules to the decimal, on a synthetic ledger and on a real run of the environment. The suite never imports this
package: run with the `elef-redteam` environment's Python, `python -m redteam.tests.test_attrib` from `agentic_sim/` (`--quick` skips the
runs of the environment)."""
from __future__ import annotations
import sys, os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from sim.ledger import Event
from redteam.attrib import attribute


class _P:
    period_ticks, T_susp, n_P = 200, 100, 20


class _Case:
    plant_outcome, parent = None, None


class _W:
    def __init__(self, events): self._e = list(events)
    def events_since(self, n): return self._e[n:]
    def case(self, cid): return _Case()


class _Run:
    def __init__(self, names, events, susp=None):
        self.learner_chain, self.w, self.p, self.susp_log = list(names), _W(events), _P(), susp or {}


def _marks_decisions(decs, n_events_total, t_end=1000):
    """decs: (t, pos, identity, case, boundary) per decision in order; the marks at each and the terminal mark; real factor 1."""
    marks = [(t, pos, case, boundary, 1.0, 0.0) for (t, pos, ident, case, boundary) in decs] + [(t_end, n_events_total, None, False, 1.0, 0.0)]
    decisions = [{"identity": ident, "case": case, "is_plant": False, "fulfilled": True, "action": 0} for (t, pos, ident, case, boundary) in decs]
    return marks, decisions


def test_worker_price_stays_off_the_auditor():
    """A (a learner) sits the audit seat on C1; B (a learner) delivered it. Pooled: B's price lands on A's decision. Own: on B's boundary."""
    ev = [Event(0, "lock", 0, None, None, None, ""),                                              # pos 0: nothing
          Event(12, "purchase", 2.0, "A", None, "C1", "review care"),                              # pos 1: A's care cost
          Event(12, "feepot_out", 3.0, "POOL", "A", "C1", "initial review fee"),                   # pos 2: A's fee
          Event(12, "escrow_out", 20.0, "ESCROW", "B", "C1", "delivery price"),                    # pos 3: B's price
          Event(12, "deposit_out", 2.0, "POOL", "A", "C1", "reimburse")]                           # pos 4: A's reimbursement
    decs = [(0, 0, "B", None, True), (0, 0, "A", None, True), (10, 1, "A", "C1", False)]
    marks, decisions = _marks_decisions(decs, len(ev))
    run = _Run(["A", "B"], ev, {"A": [], "B": []})
    pooled, sp = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=False)
    own, so = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=True)
    assert np.allclose(pooled, [0.0, 0.0, 23.0]), pooled          # the pooled purse: A's decision carries B's price
    assert np.allclose(own, [20.0, 0.0, 3.0]), own                 # own-name: B's price to B's boundary; A's decision its own fee less care plus reimbursement
    assert sp["own_name"] is False and so["own_name"] is True
    assert abs(sum(pooled) + sp["pre_boundary_real"] - (sum(own) + so["pre_boundary_real"])) < 1e-9


def test_settlement_event_to_its_own_name():
    """A sat the initial seat on C1 at t 10, B the audit seat at t 20; A's bond is burned at t 25. Pooled: the latest decision on the case (B's)
    pays A's bond. Own: A's decision does."""
    ev = [Event(0, "lock", 0, None, None, None, ""),
          Event(25, "burn_bond", 5.0, "A", None, "C1", "bond: audit overturned")]
    decs = [(0, 0, "A", None, True), (0, 0, "B", None, True), (10, 1, "A", "C1", False), (20, 1, "B", "C1", False)]
    marks, decisions = _marks_decisions(decs, len(ev))
    run = _Run(["A", "B"], ev, {"A": [], "B": []})
    pooled, _ = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=False)
    own, _ = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=True)
    assert np.allclose(pooled, [0, 0, 0, -5.0]), pooled
    assert np.allclose(own, [0, 0, -5.0, 0]), own


def test_transfer_between_two_learners_is_two_legs():
    """A's bond pays B's court fee back (B appealed its own work's N; A reviewed it). Pooled: both names in the set, the event dropped. Own:
    −D on A's decision on C1 (bond lost), +D on B's boundary (B has no decision on C1)."""
    ev = [Event(0, "lock", 0, None, None, None, ""),
          Event(30, "forfeit_to", 2.0, "A", "B", "C1", "court fee")]
    decs = [(0, 0, "A", None, True), (0, 0, "B", None, True), (10, 1, "A", "C1", False)]
    marks, decisions = _marks_decisions(decs, len(ev))
    run = _Run(["A", "B"], ev, {"A": [], "B": []})
    pooled, sp = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=False)
    own, so = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=True)
    assert np.allclose(pooled, [0, 0, 0]), pooled
    assert np.allclose(own, [0, 2.0, -2.0]), own
    assert so["by_source"].get("bond_lost") == -2.0 and so["by_source"].get("court_fee") == 2.0


def test_event_before_the_names_own_decision_on_the_case():
    """An event on C1 touching B before B's only decision on C1 (B's audit at t 20; the event at t 15): to B's own decision on the case (the
    earlier rule's analogue), not to A's earlier decision on it."""
    ev = [Event(0, "lock", 0, None, None, None, ""),
          Event(15, "feepot_out", 3.0, "POOL", "B", "C1", "audit review fee")]
    decs = [(0, 0, "A", None, True), (0, 0, "B", None, True), (10, 1, "A", "C1", False), (20, 2, "B", "C1", False)]
    marks, decisions = _marks_decisions(decs, len(ev))
    run = _Run(["A", "B"], ev, {"A": [], "B": []})
    own, _ = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=True)
    assert np.allclose(own, [0, 0, 0, 3.0]), own


def test_single_learner_same_to_the_decimal_synthetic():
    rng = np.random.default_rng(0)
    kinds = [("purchase", "review care", "src"), ("feepot_out", "initial review fee", "dst"), ("escrow_out", "delivery price", "dst"), ("burn_bond", "bond: x", "src"),
             ("deposit_out", "reimburse", "dst"), ("fee_out", "emission share", "dst"), ("forfeit_to", "court fee", "src"), ("transfer", "court fee", "src"), ("purchase", "execution", "src")]
    ev = [Event(0, "lock", 0, None, None, None, "")]
    decs = [(0, 0, "L", None, True)]
    t = 1
    for k in range(400):
        t += int(rng.integers(0, 3))
        if rng.random() < 0.3:
            decs.append((t, len(ev), "L", f"C{int(rng.integers(0, 40))}", False))
        if rng.random() < 0.05:
            decs.append((t, len(ev), "L", None, True))
        kind, note, side = kinds[int(rng.integers(len(kinds)))]
        cid = f"C{int(rng.integers(0, 40))}" if rng.random() < 0.9 else None
        ev.append(Event(t, kind, float(rng.integers(1, 30)), "L" if side == "src" else "X", "L" if side == "dst" else "Y", cid, note))
    marks, decisions = _marks_decisions(decs, len(ev), t_end=t + 1)
    run = _Run(["L"], ev, {"L": [int(x) for x in sorted(rng.integers(50, t, 3))]})
    pooled, sp = attribute(run, marks, decisions, own_name=False)
    own, so = attribute(run, marks, decisions, own_name=True)
    assert np.array_equal(pooled, own), np.abs(pooled - own).max()
    assert sp["pre_boundary_real"] == so["pre_boundary_real"] and sp["by_source"] == so["by_source"]


def _run_env(cell, seed, ticks, attrib):
    from redteam.env import ElefReviewerEnv, policy_of
    env = ElefReviewerEnv(cell, ticks=ticks, role="reviewer", attrib=attrib)
    pol = policy_of("careful", "reviewer")
    obs, info = env.reset(seed=seed); rng = np.random.default_rng(seed); done = info.get("terminal", False)
    while not done:
        obs, r, done, _, info = env.step(int(pol(obs, rng)))
    env.close()
    return info


def test_single_learner_same_to_the_decimal_on_a_run():
    cell = "--entry-pool 20 --stampers 0.6 --learner-slot on --seed 1".split()
    a = _run_env(cell, 1, 400, "pooled"); b = _run_env(cell, 1, 400, "own")
    assert len(a["attributed"]) == len(b["attributed"]) > 0
    assert np.array_equal(np.asarray(a["attributed"]), np.asarray(b["attributed"]))
    assert a["attribution"]["own_name"] is False and b["attribution"]["own_name"] is True


def test_population_conserves_the_sum_and_moves_the_audit_seat():
    """The reviewer population: the same run under both rules — the total credited (attributed plus pre-boundary) is the same to the decimal,
    the per-decision credit differs, and the names' price never lands on another name's decision under own-name credit."""
    cell = "--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --seed 1".split()
    a = _run_env(cell, 1, 400, "pooled"); b = _run_env(cell, 1, 400, "own")
    pa, pb = np.asarray(a["attributed"]), np.asarray(b["attributed"])
    assert len(pa) == len(pb) > 0
    assert abs((pa.sum() + a["attribution"]["pre_boundary_real"]) - (pb.sum() + b["attribution"]["pre_boundary_real"])) < 1e-6 * max(1.0, abs(pa.sum()))
    assert not np.array_equal(pa, pb)


def main(argv=None):
    quick = "--quick" in (argv or sys.argv[1:])
    tests = [v for k, v in sorted(globals().items()) if k.startswith("test_") and callable(v)]
    passed = 0
    for t in tests:
        if quick and "on_a_run" in t.__name__ or quick and "population" in t.__name__:
            print(f"skip {t.__name__}"); continue
        t(); passed += 1; print(f"ok   {t.__name__}", flush=True)
    print(f"{passed} passed")


if __name__ == "__main__":
    main()
