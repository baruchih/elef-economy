"""Provisional defaults (spec §18.1) and initialization values (§19)."""
from __future__ import annotations
from dataclasses import dataclass
from typing import Optional


@dataclass
class Params:
    # Windows and deadlines (ticks)
    W: int = 10            # challenge window after the initial verdict
    T_resp: int = 2        # actor's response window to its initial verdict
    T_rev: int = 5         # window to resubmit after choosing to revise (P)
    T_evid: int = 3        # window to resubmit with the named evidence (⊥)
    T_review: int = 5      # review deadline after assignment (pauses while the actor acts)
    T_wait: int = 5        # nested request unawarded this long -> pool-exhaustion exit

    # Guarantees, bonds, fees, caps (t=0 credits; frozen per case at its first lock, §4.5)
    G_frac: float = 0.5    # G = ceil(G_frac * B), min 1
    G_V: float = 5.0       # reviewer bond = total liability
    D: float = 2.0         # court fee (<= G_V by construction)
    K: float = 5.0         # reimbursement cap, all roles
    # The verification deposit is two pots (spec 1.1.0 §4.3): the expense allowance φ^E and the
    # fee pot φ^F, both paid in by the root requester at award; nested requests carry 0 / 0.
    phi_E_root: float = 10.0   # = 2K
    phi_F_root: float = 5.0    # = f (w_ordinary + w_audit): one review and one audit
    f_fee: float = 2.0         # the ordinary-review fee; a role's fee is w_role * f_fee
    omega_rate: float = 0.05

    # Verification structure
    m0_root: int = 1
    V_max: int = 3         # review *positions* per challenge path (§12)
    X: int = 4             # reserve size
    w_ordinary: float = 1.0
    w_appeal: float = 1.5
    w_audit: float = 1.5

    # Selection
    lam: float = 0.2
    band: float = 0.05

    # Emission (§4.2): E_t = E0 * 2^(-t/H); unclaimed emission is NOT minted
    E0: float = 10.0
    H: float = 1000.0

    # Audit rate (§8.3). 1.2.0 (design revision 2): a newcomer is audited every time until five in a
    # row have stood, and the doubling on an overturn or a plant failure can return a reviewer to
    # full audit — p_start and p_cap are 1.0 (were 0.5 / 0.5). The dial scales the odds a driver
    # rolls: min(1, m_t · p_j) (`Actor.p_eff`).
    p_start: float = 1.0
    p_floor: float = 0.2
    p_cap: float = 1.0
    p_halve_every: int = 5

    # Design revision 2 (1.2.0): planted work, the plant record, the effort dial.
    dial: bool = True          # False: m_t stays 1 and X_t stays X — the 1.1.0 reserve and audit odds,
    #                            kept for control runs (with pi0 = 0 and p_start = p_cap = 0.5, 1.1.0 exactly)
    pi0: float = 0.10          # base plant rate: plants per real initial review at m = 1
    pi_max: float = 0.40
    beta_P: float = 0.75       # bad-plant share — the driver's choice of truth; the engine records both kinds
    F_star: float = 0.10       # target bad-plant approval rate
    gamma: float = 1.0         # gain of the dial
    period_plants: int = 50    # a period ends after this many adjudicated plants ...
    period_ticks: int = 200    # ... or this many ticks, whichever first
    m_max: float = 4.0
    n_min: int = 4             # plants of a kind before an actor's record of that kind is determined
    n_P: int = 20              # trailing window per kind
    theta_panel: float = 0.20  # above it, no seat on appeal, dispute or audit panels (= 2 F*)
    theta_duty: float = 0.50   # above it, suspended from duty
    T_susp: int = 100          # suspension length: the wait before probation begins (1.3.0 §2.2)

    # Design revision 3 (1.3.0): inspection is membership. With `membership` off the engine holds the 1.2.1
    # rules (suspension from duty only; probation re-checked at the next plant; the §8.3 taper for
    # newcomers; one kind of reserve seat); with `duty_fund` off the raised tax stays with Ω; with
    # `net_plant_capital` off a plant ties up its award and guarantee too. All three off, with pi0 = 0
    # and p_start = p_cap = 0.5, Omega0 = 20, is the 1.1.0 engine.
    membership: bool = True    # suspension suspends market membership; probation is the way back (§2.1–2.3)
    duty_fund: bool = True     # (m_t − 1) ω_0 B of each award goes to the duty fund, paid out as a fee uplift (§2.4)
    net_plant_capital: bool = True   # a plant ties up φ^E + φ^F only; award and guarantee are notional (§2.5)

    # Reliability and duty credit windows (§11)
    rho_window: int = 100      # settled outcomes
    kappa_window: int = 100    # ticks

    # Rotation (§13)
    duty_turn_reviews: int = 3
    duty_turn_ticks: int = 30

    # Delegation (§9.4)
    rho_pool: float = 0.25
    thin: int = 2

    # Checking (§17). After every tick the engine checks the invariants over what the tick
    # touched (`check_tick`). Every `full_check_every` ticks it also re-audits the whole record
    # from genesis (`check_all`); 0 means only when the caller asks. Not a rule: a check cadence.
    full_check_every: int = 0
    # Where the record lives. None: in memory, as the tests run it. A directory: the History and
    # the event copy are written through to files there and settled cases and reviews are paged
    # out, so RAM holds the working set and a run is bounded by time, not memory (sim/record.py).
    # Not a rule: the engine behaves identically either way.
    record_dir: Optional[str] = None

    # Initialization (§19)
    Res0: float = 10000.0
    v0: float = 1.0
    float_per_actor: float = 50.0
    Omega0: float = 300.0      # 1.2.0 Appendix A: one period of plants at m = 1 (was 20)

    @property
    def phi_root(self) -> float:
        """The whole verification deposit of a root request, φ^E + φ^F."""
        return self.phi_E_root + self.phi_F_root

    def emission(self, t: int) -> float:
        return self.E0 * 2.0 ** (-t / self.H)

    @property
    def M0(self) -> float:
        return self.Res0 / self.v0
