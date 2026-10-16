"""Provisional defaults (spec §18.1) and initialization values (§19)."""
from __future__ import annotations
from dataclasses import dataclass


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
    phi_root: float = 10.0 # verification deposit, root requests (= 2K)
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

    # Audit rate (§8.3)
    p_start: float = 0.5
    p_floor: float = 0.2
    p_cap: float = 0.5
    p_halve_every: int = 5

    # Reliability and duty credit windows (§11)
    rho_window: int = 100      # settled outcomes
    kappa_window: int = 100    # ticks

    # Rotation (§13)
    duty_turn_reviews: int = 3
    duty_turn_ticks: int = 30

    # Delegation (§9.4)
    rho_pool: float = 0.25
    thin: int = 2

    # Initialization (§19)
    Res0: float = 10000.0
    v0: float = 1.0
    float_per_actor: float = 50.0
    Omega0: float = 20.0

    def emission(self, t: int) -> float:
        return self.E0 * 2.0 ** (-t / self.H)

    @property
    def M0(self) -> float:
        return self.Res0 / self.v0
