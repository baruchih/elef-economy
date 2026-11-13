"""Tests of the learner with a horizon (Baruchi's ruling of November 13, 2026; brief A1 addendum 10, J5; notes §111): the return targets along a slot's own
sequence (`redteam.data.horizon_targets`) — at a horizon of 1 the stored reward exactly; the H-step return of the attributed reward without the suspension's
counterfactual plus the slot's unclaimed work side, the charge kept only where the horizon does not reach the suspension; the value target's recursion
rho + γ V(next) = the return; the scatter back into an episode's decision order — and the attribution's export (`unclaimed`, `charge`, `charge_t`): the
attributed reward unchanged, the unclaimed sum the pre-boundary total less what fell before a name's first decision, on a synthetic ledger and on a run of
the population cell. Run with the `elef-redteam` environment's Python: `python -m redteam.tests.test_horizon` from `agentic_sim/` (`--quick` skips the run)."""
from __future__ import annotations
import sys, os
import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..")))
from redteam.data import horizon_targets, targets_in_episode_order, parse_horizon
from redteam.attrib import attribute
from redteam.tests.test_attrib import _Run, _marks_decisions, Event


def _ep(T=40, seed=0):
    rng = np.random.default_rng(seed)
    t = np.cumsum(rng.integers(1, 6, T))
    r = rng.normal(0, 3, T); u = rng.normal(0, 10, T) * (rng.random(T) < 0.4)
    ch = np.zeros(T); ct = np.full(T, -1)
    for i in rng.choice(T, 4, replace=False):
        ch[i] = -float(rng.integers(5, 40)); ct[i] = int(t[i] + rng.integers(1, 60))
    return {"reward": (r + ch).astype(np.float32), "unclaimed": u.astype(np.float32), "charge": ch.astype(np.float32), "charge_t": ct, "t": t}


def test_horizon_one_is_the_record():
    e = _ep()
    rho, ret, val = horizon_targets(e, 1, 0.98)
    assert np.array_equal(rho, e["reward"].astype(np.float64)) and np.array_equal(ret, e["reward"].astype(np.float64)) and not val.any()


def test_mc_return_drops_the_charge_and_adds_the_work_side():
    e = _ep(); g = 0.98
    rho, ret, val = horizon_targets(e, None, g)
    base = e["reward"].astype(np.float64) - e["charge"] + e["unclaimed"]
    assert np.allclose(rho, base)                                   # mc: no charge kept
    G = np.zeros(len(base) + 1)
    for i in range(len(base) - 1, -1, -1):
        G[i] = base[i] + g * G[i + 1]
    assert np.allclose(ret, G[:-1]) and np.allclose(val, G)
    assert np.allclose(rho + g * val[1:], ret)


def test_finite_horizon_keeps_the_charge_the_window_does_not_reach():
    e = _ep(); g = 0.9; H = 5; T = len(e["t"])
    rho, ret, val = horizon_targets(e, H, g)
    for i in range(T):
        kept = e["charge_t"][i] >= 0 and i + H - 1 <= T - 1 and e["t"][i + H - 1] < e["charge_t"][i]
        expect = float(e["reward"][i]) - float(e["charge"][i]) + float(e["unclaimed"][i]) + (float(e["charge"][i]) if kept else 0.0)
        assert abs(rho[i] - expect) < 1e-6, (i, rho[i], expect)
        s = sum(g ** j * rho[i + j] for j in range(H) if i + j < T)
        assert abs(ret[i] - s) < 1e-6
    assert np.allclose(rho + g * val[1:], ret)                      # the value head's recursion


def test_scatter_keeps_the_episode_order():
    e = _ep(60); e["slot"] = np.array([i % 3 for i in range(60)]); e["action"] = np.zeros(60, dtype=int)
    rho1, ret1 = targets_in_episode_order(e, 1, 0.98)
    assert np.array_equal(ret1, e["reward"].astype(np.float64))
    rho, ret = targets_in_episode_order(e, None, 0.98)
    for k in range(3):
        idx = np.where(e["slot"] == k)[0]
        sub = {kk: e[kk][idx] for kk in ("reward", "unclaimed", "charge", "charge_t", "t")}
        a, b, _ = horizon_targets(sub, None, 0.98)
        assert np.allclose(rho[idx], a) and np.allclose(ret[idx], b)


def test_parse():
    assert parse_horizon("1") == 1 and parse_horizon("32") == 32 and parse_horizon("mc") is None


def test_export_on_a_synthetic_ledger():
    """Two names, no boundary decision (the population's exit rule): every unclaimed event lands in the window after the name's latest decision, or before
    its first; the attributed reward is the one-decision rule's; the charge export sums to the suspension's charge."""
    ev = [Event(0, "lock", 0, None, None, None, ""),
          Event(5, "escrow_out", 20.0, "ESCROW", "A", "C9", "delivery price"),      # pos 1: before A's first decision — unclaimed, nobody's window
          Event(12, "purchase", 2.0, "A", None, "C1", "review care"),              # pos 2: A's decision on C1
          Event(15, "escrow_out", 30.0, "ESCROW", "A", "C8", "delivery price"),    # pos 3: A's work side after its decision at pos 2
          Event(18, "escrow_out", 25.0, "ESCROW", "B", "C7", "delivery price"),    # pos 4: B's work side after B's decision at pos 2
          Event(30, "feepot_out", 3.0, "POOL", "A", "C1", "initial review fee"),   # pos 5: A's decision on C1
          Event(40, "purchase", 7.0, "B", None, None, "execution")]                # pos 6: B's effort, after B's decision
    decs = [(10, 2, "A", "C1", False), (11, 2, "B", "C2", False), (35, 6, "A", "C3", False)]
    marks, decisions = _marks_decisions(decs, len(ev))
    run = _Run(["A", "B"], ev, {"A": [], "B": []})
    attributed, s = attribute(run, marks, decisions, lineages=[["A"], ["B"]], own_name=True)
    assert np.allclose(attributed, [1.0, 0.0, 0.0]), attributed
    assert np.allclose(s["unclaimed"], [30.0, 25.0 - 7.0, 0.0]), s["unclaimed"]
    assert abs(s["pre_boundary_real"] - (20 + 30 + 25 - 7)) < 1e-9 and abs(s["unclaimed_real"] - (30 + 25 - 7)) < 1e-9
    assert not s["charge"].any() and (s["charge_t"] == -1).all()


def test_export_on_a_run():
    from redteam.env import ElefReviewerEnv, policy_of
    cell = "--entry-pool 20 --stampers 0.6 --learner-pop all --learner-role reviewer --learner-exit rule --temptation 1 --bond-mult-later 1 --pi-a0 0.10 --pi-a-max 0.10".split()
    env = ElefReviewerEnv(cell, ticks=300, role="reviewer", attrib="own")
    pol = policy_of("eps4", "reviewer")
    obs, info = env.reset(seed=3); rng = np.random.default_rng(3); done = info.get("terminal", False)
    while not done:
        obs, r, done, _, info = env.step(int(pol(obs, rng)))
    env.close()
    n = len(info["attributed"])
    u, ch, ct = np.asarray(info["unclaimed"]), np.asarray(info["charge"]), np.asarray(info["charge_t"])
    assert len(u) == len(ch) == len(ct) == n > 0
    s = info["attribution"]
    assert s["boundary_decisions"] == 0                                     # the population's exit rule: no boundary decision
    assert u.sum() <= s["pre_boundary_real"] + 1e-6 and u.sum() > 0           # the work side by window, the rest before the names' first decisions
    assert abs(ch.sum() - s["by_source"].get("suspension", 0.0)) < 1e-6
    assert (ct[ch != 0] >= 0).all()                                        # a charged decision carries its suspension's tick (a zero charge may too: no award income before it)
    print(f"run: {n} decisions, unclaimed {u.sum():.1f} of pre-boundary {s['pre_boundary_real']:.1f}, charges {ch.sum():.1f} on {(ch != 0).sum()} decisions")


if __name__ == "__main__":
    quick = "--quick" in sys.argv
    for name, fn in list(globals().items()):
        if name.startswith("test_") and callable(fn) and not (quick and name == "test_export_on_a_run"):
            fn(); print("ok", name)
