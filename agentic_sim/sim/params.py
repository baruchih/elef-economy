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

    # Design revision 4 (1.4.0): the orchestrator's troops. The audit obligation (a rolled audit holds the
    # case) is in force whatever `troops` says — it is a conformance correction of the drivers' dropped
    # rolls as much as a rule. With `troops` off no seat or award is ever summoned for.
    troops: bool = True
    eps_T: float = 0.05        # a troop reviewer's error rate — the driver's disposition, declared here as the default
    w_R: int = 2               # ticks a required review seat waits unfilled before a troop takes it
    w_A: int = 2               # ticks a root request waits unawarded (no free fundable member) before a troop delivers it
    c_T: float = 3.0           # a troop review's cost, purchased from the fund at summons (credits at v ≈ 1)
    c_D_T: float = 10.0        # a troop delivery's cost, likewise
    A_T: float = 100.0         # Ω's advance to the fund, outstanding at most
    tau_T: int = 2             # a troop's delivery time
    # Design revision 5 (1.5.0): the reserve is sized to the need. True: R_T is the peak over the current period of the
    # troop demand D_s — capital held by live troops plus the cost of the summonses the fund refused at that seating —
    # starting at the standing demand at the period's first seating (§2.1). False: 1.4.0's reading, the peak capital
    # carried over this period and the previous one.
    reserve_demand: bool = True
    # Design revision 6 (1.6.0): auto-scale — one flag per rule, all on; `drivers.stamping --rules 1.5.0` turns them
    # off together (and A_T then binds). §2.1 the service clock; §2.2 Ω backs the fund above a plant reserve, inspection
    # first, a delivery carries its inspection; §2.3 the reserve sized on the reviews waiting; §2.4 a panel seat needs a
    # determined record once the world's first plant is adjudicated; §2.5 R_T over this and the previous period.
    service_clock: bool = True
    T_s: int = 8               # the service target: posting to first verdict, in ticks
    r_s: float = 0.0           # the rebate per tick late; 0 = ω_0 B (omega_rate × B); capped at B
    omega_backs_fund: bool = True
    seat_the_queue: bool = True
    panel_determined: bool = True
    reserve_periods: int = 2   # 1 = 1.5.0's one-period reset
    duty_cap_frac: float = 2.0 / 3.0   # the members' duty cap as a fraction of E_t — 1.7.0 §2.3 moved it from 1/2 (1.6.0 §2.6 swept
    #                                   1/2, 2/3, 1; `--duty-cap half` is the 1.6.0 control)
    # The plant reserve's horizon (§2.2): the text says the ticks remaining in the period; a plant's pots return to Ω at
    # its closure, so the capital the clock needs at once is a plant's life of plants — the implementer's reading, W +
    # T_review ticks. 0 = the text's literal horizon (kept as a declared cell).
    plant_reserve_life: int = 15
    # Design revision 7 (1.7.0): the state's earnings. True: the troops' wallet is a separate troop account — Ω's advances
    # and every troop's earnings in; costs, locks, forfeits, burns, repayments out; at each settlement batch its unlocked
    # balance above R_T flows to Ω — and the duty fund is 1.3.0's uplift fund again (the raised tax in, its whole balance
    # out as uplift every batch, no reserve); R_T is then the two-period peak of the capital troops held (1.4.0's
    # reading; the 1.5.0 refused component withdrawn). False: the 1.4.0–1.6.0 merged fund (`--rules 1.6.0`).
    troop_account: bool = True
    # Design revision 8 (2.0.0): the price of work. True: the price level P_t (the trailing mean awarded price, P_0 = 20 before
    # the first award) indexes every nominal the rules fix in place of v_0/v_t, frozen at a case's first lock — a root's
    # posting, which locks the all-in maximum (I29); no backing (Res held at 0, purchase a plain burn, the cost API in
    # credits); Ω creates for a required payment it cannot meet and retires the deficit from every inflow (I28); the
    # troops' wallet is Ω and the state delivers at cost; N_T bounds the field; issuance funds requesters. False is the
    # 1.7.1 engine (the backing, A_T/R_T, the plant reserve, Ω's order, the troop account, the liability stock).
    floating: bool = True
    P0: float = 20.0           # the former fixed price; the indexing base
    issuance: float = 0.0      # credits a tick minted to each requester (the driver declares it; 0 so reviewer tests see none)
    N_T: int = 40              # the most troops ELEF can field at once, deliveries and review seats together (0 = unbounded);
    #                            a delivery holds two places until its initial review is seated (Appendix M)
    troop_cost_at_price: bool = True   # c^D_T = B̄, the state at cost; False: the 1.x c_D_T × P_t/P_0 (the control, half of P_t)
    bbar_counts_troops: bool = False   # 2.0.0 §8.8's control: troop awards counted in B̄ (the rule excludes them, §2.2)

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
