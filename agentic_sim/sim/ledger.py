"""Wallets, lock records, case pools, the operating account, the backed credit, and a
hash-chained history (spec §4, §10, §14).

Every credit in the system lives in exactly one of: a wallet's unlocked balance U, a
wallet's locked balance L, a case pool (escrow / expense allowance / fee pot / minted
emission), or the operating account Ω. Their sum is the money supply M, and M is also reconstructible
from the mint and burn events alone (invariant I1).

Every locked credit is attributable to a named obligation: a guarantee, a bond, a
nested price ceiling, a rejection bond. L is the sum of a wallet's lock records (I15).

Mints: backed (root pay-in) or emission. Burns: bond forfeiture remainder, or resource
purchase. Nothing else creates or destroys credits (I3).

All amounts crossing the ledger boundary are validated: finite and non-negative.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from itertools import islice
from typing import Optional
import hashlib
import json
import math

from .record import Journal


class LedgerError(Exception):
    pass


def amount(x, name="amount") -> float:
    """Validate a monetary or cost amount: a finite, non-negative number."""
    try:
        v = float(x)
    except (TypeError, ValueError):
        raise LedgerError(f"{name} must be a number, got {x!r}")
    if not math.isfinite(v) or v < 0:
        raise LedgerError(f"{name} must be finite and non-negative, got {x!r}")
    return v


def _i10_exempt(note: str) -> bool:
    """§6 / §4.3: after vesting, obligations established before it may still be paid (deferred
    reimbursements, Ω claims); and, since 1.1.0, a nested case may draw on its root's pots and
    the tree's closure moves the root's remaining deposit; and, since 1.6.0 §2.1, a rebate Ω owed at the
    clock's stop and carried as its liability is paid when Ω can — an obligation established before
    vesting. Nothing else moves money on a vested case."""
    return "deferred" in note or "Ω claim" in note or note.startswith("nested ") or note.startswith("tree closure") \
        or note.startswith("rebate (Ω liability serviced)") or note.startswith("rebate (settled at the period's close)") \
        or note.startswith("node closure")


def _i19_event_ok(e) -> bool:
    """I19, the event half: no fee is paid from the allowance, and the fee pot pays only fixed
    fees — until tree closure, when it may pay the tree's expense debts and return the rest."""
    if e.kind == "deposit_out":
        return "fee" not in e.note
    if e.kind == "feepot_out":
        return e.note in ("review fee", "nested review fee") or e.note.startswith("tree closure") or e.note.startswith("node closure")
    return True


@dataclass
class Wallet:
    id: str
    U: float = 0.0
    L: float = 0.0

    @property
    def W(self) -> float:
        return self.U + self.L


@dataclass
class CasePool:
    """A case's money held by the ledger. The verification deposit is two pots (spec 1.1.0 §4.3):
    `deposit` is the expense allowance φ^E (the name is kept from v1.0.1, where it was the whole
    deposit), `fee_pot` is φ^F. Both are funded on a root case and drawn on by every review in
    its tree; nested cases carry 0 / 0."""
    escrow: float = 0.0    # delivery price B held for the actor
    deposit: float = 0.0   # expense allowance φ^E remaining
    fee_pot: float = 0.0   # fee pot φ^F remaining
    minted: float = 0.0    # emission minted into this case's pool at settlement

    @property
    def total(self) -> float:
        return self.escrow + self.deposit + self.fee_pot + self.minted


@dataclass
class Event:
    t: int
    kind: str
    amount: float
    src: Optional[str] = None
    dst: Optional[str] = None
    case: Optional[str] = None
    note: str = ""
    seq: int = 0
    prev: str = ""
    hash: str = ""
    hseq: int = -1        # position of this event's commitment in the History

    def payload(self) -> dict:
        return {"t": self.t, "kind": self.kind, "amount": self.amount, "src": self.src,
                "dst": self.dst, "case": self.case, "note": self.note, "seq": self.seq}


class History:
    """An append-only, hash-chained record. Tamper-evident within the harness: the chain
    detects any edit to a past entry, and `verify()` recomputes it. It is not a trust
    anchor — there is no external commitment of the head (§14)."""

    def __init__(self, path: Optional[str] = None, tail: int = 4096):
        # the entries: a list in memory, or — given a path — a Journal written through to that
        # file, one entry per line, with the newest `tail` entries kept decoded in memory
        if path is None:
            self.entries: list[dict] = []
        else:
            self.entries = Journal(path, encode=lambda e: json.dumps(e, sort_keys=True, default=str),
                                   decode=json.loads, tail=tail)
        self.head: str = hashlib.sha256(b"genesis").hexdigest()
        # incremental verification state: entries[:_verified_upto] have been re-hashed and
        # found consistent, and _verified_prev is the hash of the last of them
        self._verified_upto: int = 0
        self._verified_prev: str = self.head

    def append(self, kind: str, payload: dict) -> str:
        seq = len(self.entries)
        body = json.dumps({"seq": seq, "kind": kind, "payload": payload, "prev": self.head},
                          sort_keys=True, default=str)
        h = hashlib.sha256(body.encode()).hexdigest()
        entry = {"seq": seq, "kind": kind, "payload": payload, "prev": self.head, "hash": h}
        if isinstance(self.entries, Journal):
            # the line on disk is the hashed body with the hash added: it decodes to `entry`
            self.entries.append(entry, line=body[:-1] + ', "hash": "' + h + '"}')
        else:
            self.entries.append(entry)
        self.head = h
        return h

    def _iter_from(self, start: int):
        it = getattr(self.entries, "iter_from", None)
        return it(start) if it is not None else islice(self.entries, start, None)

    def verify(self) -> bool:
        prev = hashlib.sha256(b"genesis").hexdigest()
        for e in self.entries:
            body = json.dumps({"seq": e["seq"], "kind": e["kind"], "payload": e["payload"], "prev": prev},
                              sort_keys=True, default=str)
            if e["prev"] != prev or hashlib.sha256(body.encode()).hexdigest() != e["hash"]:
                return False
            prev = e["hash"]
        return prev == self.head

    def verify_new(self) -> bool:
        """Verify the entries appended since the last call (or since genesis), continuing the
        chain from the last verified hash. Equivalent to `verify()` for a record that is only
        ever appended to — the engine's case — at a cost proportional to what is new. It does
        not re-examine already-verified entries; `verify()` does, and is what detects an edit
        to one of them after the fact."""
        prev = self._verified_prev
        for i, e in enumerate(self._iter_from(self._verified_upto), self._verified_upto):
            body = json.dumps({"seq": e["seq"], "kind": e["kind"], "payload": e["payload"], "prev": prev},
                              sort_keys=True, default=str)
            if e["seq"] != i or e["prev"] != prev or hashlib.sha256(body.encode()).hexdigest() != e["hash"]:
                return False
            prev = e["hash"]
        if prev != self.head:
            return False
        self._verified_upto, self._verified_prev = len(self.entries), prev
        return True

    def matches(self, seq: int, kind: str, payload: dict) -> bool:
        """Does a working copy agree with the committed entry at `seq`? The History is the
        authoritative record; ledger events and case logs are copies checked against it."""
        if seq < 0 or seq >= len(self.entries):
            return False
        e = self.entries[seq]
        return e["kind"] == kind and json.dumps(e["payload"], sort_keys=True, default=str) == \
            json.dumps(payload, sort_keys=True, default=str)


class Ledger:
    OMEGA = "OMEGA"
    MINTS = {"mint_backed", "mint_emission", "issuance", "creation", "mint_plant", "loan", "mint_scenario", "arrival"}
    BURNS = {"burn_bond", "purchase", "retirement", "departure", "repayment", "retire_plant"}

    def __init__(self, Res0: float, v0: float, history: Optional[History] = None,
                 events_path: Optional[str] = None, tail: int = 4096, floating: bool = False, P0: float = 20.0):
        # 2.0.0: under `floating` there is no backing — Res stays 0, the credit's value is P0/P_t in tasks, the index
        # P_t/P0, and `purchase` burns the credits it is given (the cost API is nominal); the World sets P_t
        self.floating = floating
        self.P0 = amount(P0, "P0")
        self.P_t = self.P0
        self.Res: float = 0.0
        self.M: float = 0.0
        self.halted: bool = False
        self.wallets: dict[str, Wallet] = {}
        self.locks: dict[str, dict[str, float]] = {}
        # 1.4.0: a troop holds no wallet of its own — every operation on a troop id resolves to the
        # duty fund's wallet and lock records (the troop id stays on the event, so the record says who)
        self.aliases: dict[str, str] = {}
        self.pools: dict[str, CasePool] = {}
        # the event copy: a list in memory, or — given a path — a Journal written through to it
        if events_path is None:
            self.events: list[Event] = []
        else:
            self.events = Journal(events_path, encode=lambda e: json.dumps(e.__dict__),
                                  decode=lambda s: Event(**json.loads(s)), tail=tail)
        # per-case index of the same events (same objects; `events` stays the ordered copy I16
        # checks), a running mints-minus-burns, a running sum of every pool, and a hook the
        # engine sets to learn which case an event touched — so a tick's checks cost what the
        # tick did, not what the whole run did
        self.events_by_case: dict[str, list[Event]] = {}
        self._recon_M: float = 0.0
        self._pool_sum: float = 0.0
        self.on_event = None
        self.history = history or History()
        self.t = 0
        self._v0 = amount(v0, "v0")
        if self._v0 <= 0:
            raise LedgerError("v0 must be positive")
        self.wallets[self.OMEGA] = Wallet(self.OMEGA)
        self.wallets["SPONSOR"] = Wallet("SPONSOR")
        if not floating:
            self.mint_backed("SPONSOR", amount(Res0, "Res0"), rate=self._v0)

    # ---- money ------------------------------------------------------------
    @property
    def v(self) -> float:
        """Value of one credit in real units. Res = 0 is the halt state: v = 0 by definition,
        never 0/0 (§4.4). 2.0.0: P0/P_t, the credit's value in tasks — a reading."""
        if self.floating:
            return self.P0 / self.P_t
        if self.Res <= 1e-12:
            self.halted = True
            return 0.0
        return self.Res / self.M

    @property
    def v0(self) -> float:
        return self._v0

    def index(self) -> float:
        """Indexing factor v0/v_t for nominal thresholds (§4.5); 2.0.0: P_t/P0."""
        if self.floating:
            return self.P_t / self.P0
        v = self.v
        if v == 0:
            raise LedgerError("halt state: credit has no value")
        return self._v0 / v

    def _log(self, kind, amt, src=None, dst=None, case=None, note=""):
        e = Event(self.t, kind, amt, src, dst, case, note, seq=len(self.events))
        e.prev = self.history.head                      # the head this event's entry chains to
        e.hash = self.history.append("ledger", e.payload())
        e.hseq = len(self.history.entries) - 1
        self.events.append(e)
        if case is not None:
            self.events_by_case.setdefault(case, []).append(e)
        if kind in self.MINTS:
            self._recon_M += amt
        elif kind in self.BURNS:
            self._recon_M -= amt
        if self.on_event is not None:
            self.on_event(e)

    def __getstate__(self):
        """A pickled ledger is an in-memory ledger: the journal pickles as a list, and the
        per-case index — dropped for paged-out cases — is rebuilt for every case."""
        state = self.__dict__.copy()
        if isinstance(self.events, Journal):
            by_case: dict = {}
            for e in self.events:
                if e.case is not None:
                    by_case.setdefault(e.case, []).append(e)
            state["events_by_case"] = by_case
        return state

    def reconstruct_M(self) -> float:
        """Mints minus burns, recomputed from the whole event copy (the full audit)."""
        return (sum(e.amount for e in self.events if e.kind in self.MINTS)
                - sum(e.amount for e in self.events if e.kind in self.BURNS))

    def reconstruct_M_running(self) -> float:
        """Mints minus burns as accumulated event by event (the per-tick check)."""
        return self._recon_M

    # ---- wallets and lock records ----------------------------------------
    def resolve(self, wid: str) -> str:
        return self.aliases.get(wid, wid)

    def wallet(self, wid: str) -> Wallet:
        wid = self.aliases.get(wid, wid)
        if wid not in self.wallets:
            self.wallets[wid] = Wallet(wid)
        return self.wallets[wid]

    def lock_record(self, wid: str, key: str) -> float:
        return self.locks.get(self.resolve(wid), {}).get(key, 0.0)

    def _add_lock(self, wid, key, amt):
        d = self.locks.setdefault(self.resolve(wid), {})
        d[key] = d.get(key, 0.0) + amt

    def _take_lock(self, wid, key, amt):
        d = self.locks.setdefault(self.resolve(wid), {})
        have = d.get(key, 0.0)
        if have + 1e-9 < amt:
            raise LedgerError(f"{wid} lock {key} holds {have}, cannot take {amt}")
        d[key] = have - amt
        if d[key] <= 1e-9:
            del d[key]

    def lock(self, wid: str, amt: float, key: str, case=None, note=""):
        amt = amount(amt)
        w = self.wallet(wid)
        if w.U + 1e-9 < amt:
            raise LedgerError(f"{wid} cannot lock {amt}: unlocked {w.U}")
        before = w.W
        w.U -= amt
        w.L += amt
        self._add_lock(wid, key, amt)
        assert abs(w.W - before) < 1e-9
        self._log("lock", amt, wid, wid, case, f"{key} {note}".strip())

    def release(self, wid: str, amt: float, key: str, case=None, note=""):
        amt = amount(amt)
        if amt <= 1e-12:
            return
        w = self.wallet(wid)
        self._take_lock(wid, key, amt)
        before = w.W
        w.L -= amt
        w.U += amt
        assert abs(w.W - before) < 1e-9
        self._log("release", amt, wid, wid, case, f"{key} {note}".strip())

    def transfer(self, src: str, dst: str, amt: float, case=None, note=""):
        """Unlocked -> unlocked. Neutral to M."""
        amt = amount(amt)
        s, d = self.wallet(src), self.wallet(dst)
        if s.U + 1e-9 < amt:
            raise LedgerError(f"{src} cannot pay {amt}: unlocked {s.U}")
        s.U -= amt
        d.U += amt
        self._log("transfer", amt, src, dst, case, note)

    def transfer_locked(self, src: str, dst: str, amt: float, key: str, case=None, note=""):
        """Locked (src) -> unlocked (dst): a forfeited guarantee, a court fee from a bond."""
        amt = amount(amt)
        s, d = self.wallet(src), self.wallet(dst)
        self._take_lock(src, key, amt)
        s.L -= amt
        d.U += amt
        self._log("forfeit_to", amt, src, dst, case, f"{key} {note}".strip())

    def burn_locked(self, wid: str, amt: float, key: str, case=None, note=""):
        """Bond forfeiture remainder (§7.2). The only burn besides resource purchase."""
        amt = amount(amt)
        if amt <= 1e-12:
            return
        w = self.wallet(wid)
        self._take_lock(wid, key, amt)
        w.L -= amt
        self.M -= amt
        self._log("burn_bond", amt, wid, None, case, f"{key} {note}".strip())

    def purchase(self, wid: str, real_cost: float, case=None, note="") -> float:
        """Resource purchase: burns real_cost / v credits, pays real_cost from the reserve.
        Value-neutral: v' = v (§4.4). Returns the credits burned."""
        real_cost = amount(real_cost, "real_cost")
        if self.floating:                               # 2.0.0 §2.4: a plain burn of the credits given
            credits = real_cost
            w = self.wallet(wid)
            if w.U + 1e-9 < credits:
                raise LedgerError(f"{wid} cannot afford {credits:.3f} credits of resources")
            w.U -= credits
            self.M -= credits
            if abs(self.M) < 1e-9:
                self.M = 0.0
            self._log("purchase", credits, wid, None, case, note)
            return credits
        if self.halted:
            raise LedgerError("halt state: no purchases")
        v = self.v
        credits = real_cost / v
        w = self.wallet(wid)
        if w.U + 1e-9 < credits:
            raise LedgerError(f"{wid} cannot afford {credits:.3f} credits of resources")
        if self.Res + 1e-9 < real_cost:
            raise LedgerError("reserve cannot pay real resource cost")
        w.U -= credits
        self.M -= credits
        self.Res -= real_cost
        if self.Res <= 1e-9:
            self.Res = 0.0
            self.halted = True
        if abs(self.M) < 1e-9:
            self.M = 0.0
        self._log("purchase", credits, wid, None, case, note)
        return credits

    # ---- 2.0.0: unbacked sources and sinks (§2.4) ---------------------------
    def mint(self, kind: str, wid: str, credits: float, case=None, note=""):
        """issuance (a requester's wallet, the genesis floats) or creation (Ω's shortfall on a required payment); 2.1.0: the
        bank's mint_plant (a plant's pots), loan (a summons's shortfall, tied to it) and mint_scenario (the declared shock)."""
        if kind not in ("issuance", "creation", "mint_plant", "loan", "mint_scenario", "arrival"):
            raise LedgerError(f"mint: unknown source kind {kind}")
        credits = amount(credits, kind)
        if credits <= 1e-12:
            return
        self.M += credits
        self.wallet(wid).U += credits
        self._log(kind, credits, None, wid, case, note)

    def burn_unlocked(self, kind: str, wid: str, credits: float, case=None, note=""):
        """retirement (Ω burns against its deficit) or departure (a leaving requester's wallet); 2.1.0: repayment (a loan or the
        debt, from Ω) and retire_plant (what a closed plant's wallets held)."""
        if kind not in ("retirement", "departure", "repayment", "retire_plant"):
            raise LedgerError(f"burn: unknown sink kind {kind}")
        credits = amount(credits, kind)
        if credits <= 1e-12:
            return
        w = self.wallet(wid)
        if w.U + 1e-9 < credits:
            raise LedgerError(f"{wid} cannot burn {credits}: unlocked {w.U}")
        w.U -= credits
        self.M -= credits
        if abs(self.M) < 1e-9:
            self.M = 0.0
        self._log(kind, credits, wid, None, case, note)

    # ---- mints ------------------------------------------------------------
    def mint_backed(self, wid: str, real: float, rate: Optional[float] = None, case=None) -> float:
        real = amount(real, "real")
        v = rate if rate is not None else self.v
        if v <= 0:
            raise LedgerError("cannot mint against a worthless credit")
        credits = real / v
        self.Res += real
        self.M += credits
        self.wallet(wid).U += credits
        self._log("mint_backed", credits, None, wid, case)
        return credits

    def mint_emission_to_pool(self, case_id: str, credits: float):
        credits = amount(credits, "emission")
        if credits <= 1e-12:
            return
        self.M += credits
        self.pool(case_id).minted += credits
        self._pool_sum += credits
        self._log("mint_emission", credits, None, f"pool:{case_id}", case_id)

    # ---- case pools -------------------------------------------------------
    def pool(self, case_id: str) -> CasePool:
        if case_id not in self.pools:
            self.pools[case_id] = CasePool()
        return self.pools[case_id]

    def fund_escrow(self, src: str, case_id: str, amt: float, from_locked: Optional[str] = None, note=""):
        amt = amount(amt)
        s = self.wallet(src)
        if from_locked:
            self._take_lock(src, from_locked, amt)
            s.L -= amt
        else:
            if s.U + 1e-9 < amt:
                raise LedgerError(f"{src} unlocked {s.U} < {amt}")
            s.U -= amt
        self.pool(case_id).escrow += amt
        self._pool_sum += amt
        self._log("escrow_in", amt, src, f"pool:{case_id}", case_id, note)

    def fund_deposit(self, src: str, case_id: str, amt: float, note=""):
        amt = amount(amt)
        s = self.wallet(src)
        if s.U + 1e-9 < amt:
            raise LedgerError(f"{src} unlocked {s.U} < {amt}")
        s.U -= amt
        self.pool(case_id).deposit += amt
        self._pool_sum += amt
        self._log("deposit_in", amt, src, f"pool:{case_id}", case_id, note)

    def fund_fee_pot(self, src: str, case_id: str, amt: float, note=""):
        amt = amount(amt)
        s = self.wallet(src)
        if s.U + 1e-9 < amt:
            raise LedgerError(f"{src} unlocked {s.U} < {amt}")
        s.U -= amt
        self.pool(case_id).fee_pot += amt
        self._pool_sum += amt
        self._log("feepot_in", amt, src, f"pool:{case_id}", case_id, note)

    def pay_from_escrow(self, case_id: str, dst: str, amt: float, note=""):
        amt = amount(amt)
        p = self.pool(case_id)
        if p.escrow + 1e-9 < amt:
            raise LedgerError(f"escrow {p.escrow} < {amt}")
        p.escrow -= amt
        self._pool_sum -= amt
        self.wallet(dst).U += amt
        self._log("escrow_out", amt, f"pool:{case_id}", dst, case_id, note)

    def pay_from_deposit(self, case_id: str, dst: str, amt: float, note="", case: Optional[str] = None):
        """From the expense allowance φ^E of `case_id`'s pool. `case` attributes the event to
        another case in the same tree (a nested case drawing on its root's pot)."""
        amt = amount(amt)
        p = self.pool(case_id)
        if p.deposit + 1e-9 < amt:
            raise LedgerError(f"allowance {p.deposit} < {amt}")
        p.deposit -= amt
        self._pool_sum -= amt
        self.wallet(dst).U += amt
        self._log("deposit_out", amt, f"pool:{case_id}", dst, case or case_id, note)

    def pay_from_fee_pot(self, case_id: str, dst: str, amt: float, note="", case: Optional[str] = None):
        """From the fee pot φ^F of `case_id`'s pool (fixed fees; at tree closure, the tree's
        expense debts and the refund). Atomic: refused whole."""
        amt = amount(amt)
        p = self.pool(case_id)
        if p.fee_pot + 1e-9 < amt:
            raise LedgerError(f"fee pot {p.fee_pot} < {amt}")
        p.fee_pot -= amt
        self._pool_sum -= amt
        self.wallet(dst).U += amt
        self._log("feepot_out", amt, f"pool:{case_id}", dst, case or case_id, note)

    def fee_pool_balance(self, case_id: str) -> float:
        """A case's fee money: its fee pot plus the emission minted into it."""
        p = self.pool(case_id)
        return p.fee_pot + p.minted

    def pay_from_fee_pool(self, case_id: str, dst: str, amt: float, note=""):
        """Pay from the fee pot first, then from minted emission. Atomic: refused whole. Not used
        by the engine's settlement (which pays the two separately, §4.3); kept as the generic
        fee-money payment, and exercised by the reviewer tests."""
        amt = amount(amt)
        p = self.pool(case_id)
        if amt > p.fee_pot + p.minted + 1e-9:
            raise LedgerError(f"fee pool for {case_id} short by {amt - p.fee_pot - p.minted}")
        take = min(amt, p.fee_pot)
        p.fee_pot -= take
        p.minted -= (amt - take)
        self._pool_sum -= amt
        self.wallet(dst).U += amt
        self._log("fee_out", amt, f"pool:{case_id}", dst, case_id, note)

    def pay_emission(self, case_id: str, dst: str, amt: float, note=""):
        """From the emission minted into this case's pool. Atomic: refused whole."""
        amt = amount(amt)
        p = self.pool(case_id)
        if amt > p.minted + 1e-9:
            raise LedgerError(f"minted emission for {case_id} short by {amt - p.minted}")
        p.minted -= amt
        self._pool_sum -= amt
        self.wallet(dst).U += amt
        self._log("fee_out", amt, f"pool:{case_id}", dst, case_id, note)

    # ---- totals -----------------------------------------------------------
    def total_credits(self) -> float:
        """Every credit in a wallet or a pool, recomputed from the balances (the full audit)."""
        tot = sum(w.W for w in self.wallets.values())
        tot += sum(p.total for p in self.pools.values())
        return tot

    def total_credits_running(self) -> float:
        """Wallet balances summed now, plus the pool total as accumulated movement by movement
        (the per-tick check): the number of pools grows with the run, the number of wallets
        does not."""
        return sum(w.W for w in self.wallets.values()) + self._pool_sum
