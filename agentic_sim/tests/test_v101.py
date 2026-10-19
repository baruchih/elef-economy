"""v1.0.1: coverage for the one permitted operation (§16) no suite had exercised — withdrawing an
unawarded request — plus the parameter-exact expected-failure accounting. No rule changed; the
v1.0.1 errata are wording, and the engine already behaved as the corrected text says."""
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
try:
    import pytest
except ImportError:
    sys.path.insert(0, os.path.dirname(__file__))
    from _mini_pytest import pytest

from sim import Params, World, RuleError, check_all
from sim.engine import F

ACTORS = list("ABCDEFGI")
DUTY = list("CDEF")


def world():
    # 2.3.0 (design revision 11) gave a nested request its own pots, posted by the parent; these tests pin the 1.x nested lock (supply=False)
    return World(Params(supply=False), ACTORS, humans={"H": 1000.0}, on_duty=DUTY)


def snapshot(w):
    return (len(w.history.entries), round(w.ledger.M, 9),
            tuple(sorted((k, round(v.W, 9), round(v.U, 9)) for k, v in w.ledger.wallets.items())),
            tuple((c.id, c.state, c.verdict, c.t_verdict) for c in w.cases.values()))


def test_root_request_withdrawn_before_award_moves_no_money_and_is_terminal():
    w = world()
    before = snapshot(w)
    q = w.post_root("H", 10)
    w.withdraw_unawarded(q)
    c = w.cases[q]
    assert c.state == "WITHDRAWN" and c.final
    # a root posting locks nothing (pay-in happens at award), so only the record grew
    assert snapshot(w)[1:3] == before[1:3]
    assert len(w.history.entries) > before[0]
    w.advance(1)
    check_all(w)
    with pytest.raises(RuleError):
        w.award(q, "A", 10, 5)                            # a withdrawn request cannot be awarded


def test_nested_request_withdrawn_before_award_releases_ceiling_and_rejection_bond():
    w = world()
    q = w.post_root("H", 40)
    w.award(q, "A", 40, 20)
    U_before, W_before = w.ledger.wallet("A").U, w.ledger.wallet("A").W
    child = w.post_nested(q, 10)
    GV = w.cases[child].G_V
    assert abs((U_before - w.ledger.wallet("A").U) - (10 + GV)) < 1e-9   # posting set aside beta' + G^V
    w.withdraw_unawarded(child)
    c = w.cases[child]
    assert c.state == "WITHDRAWN" and c.final and c.rejection_bond == 0.0
    assert abs(w.ledger.wallet("A").U - U_before) < 1e-9       # beta' and G^V both released
    assert abs(w.ledger.wallet("A").W - W_before) < 1e-9       # posting and withdrawal moved no money
    # a withdrawn child is a milestone, so the parent may submit (§9, I7)
    w.advance(1)
    w.submit(q)
    r = w.assign_initial(q, "C")
    w.complete_review(r, F, 0)
    w.advance(1)
    check_all(w)


def test_withdrawal_after_award_is_refused_whole():
    w = world()
    q = w.post_root("H", 10)
    w.award(q, "A", 10, 5)
    s = snapshot(w)
    with pytest.raises(RuleError):
        w.withdraw_unawarded(q)
    assert snapshot(w) == s and w.cases[q].state == "COMMITTED"
    w.advance(1)
    check_all(w)


def test_withdrawal_of_an_unknown_case_is_refused_whole():
    w = world()
    s = snapshot(w)
    with pytest.raises(RuleError):
        w.withdraw_unawarded("q999")
    assert snapshot(w) == s
