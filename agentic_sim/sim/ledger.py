"""Wallets, lock records, case pools, the operating account, the backed credit, and a
hash-chained history (spec §4, §10, §14).

Every credit in the system lives in exactly one of: a wallet's unlocked balance U, a
wallet's locked balance L, a case pool (escrow / deposit / minted fee pool), or the
operating account Ω. Their sum is the money supply M, and M is also reconstructible
from the mint and burn events alone (invariant I1).

Every locked credit is attributable to a named obligation: a guarantee, a bond, a
nested price ceiling, a rejection bond. L is the sum of a wallet's lock records (I15).

Mints: backed (root pay-in) or emission. Burns: bond forfeiture remainder, or resource
purchase. Nothing else creates or destroys credits (I3).

All amounts crossing the ledger boundary are validated: finite and non-negative.
"""
from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional
import hashlib
import json
import math


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
    escrow: float = 0.0   # delivery price B held for the actor
    deposit: float = 0.0  # verification deposit φ remaining
    minted: float = 0.0   # emission minted into this case's fee pool at settlement


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

    def __init__(self):
        self.entries: list[dict] = []
        self.head: str = hashlib.sha256(b"genesis").hexdigest()

    def append(self, kind: str, payload: dict) -> str:
        seq = len(self.entries)
        body = json.dumps({"seq": seq, "kind": kind, "payload": payload, "prev": self.head},
                          sort_keys=True, default=str)
        h = hashlib.sha256(body.encode()).hexdigest()
        self.entries.append({"seq": seq, "kind": kind, "payload": payload, "prev": self.head, "hash": h})
        self.head = h
        return h

    def verify(self) -> bool:
        prev = hashlib.sha256(b"genesis").hexdigest()
        for e in self.entries:
            body = json.dumps({"seq": e["seq"], "kind": e["kind"], "payload": e["payload"], "prev": prev},
                              sort_keys=True, default=str)
            if e["prev"] != prev or hashlib.sha256(body.encode()).hexdigest() != e["hash"]:
                return False
            prev = e["hash"]
        return prev == self.head

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
    MINTS = {"mint_backed", "mint_emission"}
    BURNS = {"burn_bond", "purchase"}

    def __init__(self, Res0: float, v0: float, history: Optional[History] = None):
        self.Res: float = 0.0
        self.M: float = 0.0
        self.halted: bool = False
        self.wallets: dict[str, Wallet] = {}
        self.locks: dict[str, dict[str, float]] = {}
        self.pools: dict[str, CasePool] = {}
        self.events: list[Event] = []
        self.history = history or History()
        self.t = 0
        self._v0 = amount(v0, "v0")
        if self._v0 <= 0:
            raise LedgerError("v0 must be positive")
        self.wallets[self.OMEGA] = Wallet(self.OMEGA)
        self.wallets["SPONSOR"] = Wallet("SPONSOR")
        self.mint_backed("SPONSOR", amount(Res0, "Res0"), rate=self._v0)

    # ---- money ------------------------------------------------------------
    @property
    def v(self) -> float:
        """Value of one credit in real units. Res = 0 is the halt state: v = 0 by definition,
        never 0/0 (§4.4)."""
        if self.Res <= 1e-12:
            self.halted = True
            return 0.0
        return self.Res / self.M

    @property
    def v0(self) -> float:
        return self._v0

    def index(self) -> float:
        """Indexing factor v0/v_t for nominal thresholds (§4.5)."""
        v = self.v
        if v == 0:
            raise LedgerError("halt state: credit has no value")
        return self._v0 / v

    def _log(self, kind, amt, src=None, dst=None, case=None, note=""):
        e = Event(self.t, kind, amt, src, dst, case, note, seq=len(self.events))
        e.hash = self.history.append("ledger", e.payload())
        e.hseq = len(self.history.entries) - 1
        e.prev = self.history.entries[-1]["prev"]
        self.events.append(e)

    def reconstruct_M(self) -> float:
        return (sum(e.amount for e in self.events if e.kind in self.MINTS)
                - sum(e.amount for e in self.events if e.kind in self.BURNS))

    # ---- wallets and lock records ----------------------------------------
    def wallet(self, wid: str) -> Wallet:
        if wid not in self.wallets:
            self.wallets[wid] = Wallet(wid)
        return self.wallets[wid]

    def lock_record(self, wid: str, key: str) -> float:
        return self.locks.get(wid, {}).get(key, 0.0)

    def _add_lock(self, wid, key, amt):
        d = self.locks.setdefault(wid, {})
        d[key] = d.get(key, 0.0) + amt

    def _take_lock(self, wid, key, amt):
        d = self.locks.setdefault(wid, {})
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
        self._log("escrow_in", amt, src, f"pool:{case_id}", case_id, note)

    def fund_deposit(self, src: str, case_id: str, amt: float, note=""):
        amt = amount(amt)
        s = self.wallet(src)
        if s.U + 1e-9 < amt:
            raise LedgerError(f"{src} unlocked {s.U} < {amt}")
        s.U -= amt
        self.pool(case_id).deposit += amt
        self._log("deposit_in", amt, src, f"pool:{case_id}", case_id, note)

    def pay_from_escrow(self, case_id: str, dst: str, amt: float, note=""):
        amt = amount(amt)
        p = self.pool(case_id)
        if p.escrow + 1e-9 < amt:
            raise LedgerError(f"escrow {p.escrow} < {amt}")
        p.escrow -= amt
        self.wallet(dst).U += amt
        self._log("escrow_out", amt, f"pool:{case_id}", dst, case_id, note)

    def pay_from_deposit(self, case_id: str, dst: str, amt: float, note=""):
        amt = amount(amt)
        p = self.pool(case_id)
        if p.deposit + 1e-9 < amt:
            raise LedgerError(f"deposit {p.deposit} < {amt}")
        p.deposit -= amt
        self.wallet(dst).U += amt
        self._log("deposit_out", amt, f"pool:{case_id}", dst, case_id, note)

    def fee_pool_balance(self, case_id: str) -> float:
        p = self.pool(case_id)
        return p.deposit + p.minted

    def pay_from_fee_pool(self, case_id: str, dst: str, amt: float, note=""):
        """Pay from deposit remainder first, then from minted emission. Atomic: refused whole."""
        amt = amount(amt)
        p = self.pool(case_id)
        if amt > p.deposit + p.minted + 1e-9:
            raise LedgerError(f"fee pool for {case_id} short by {amt - p.deposit - p.minted}")
        take_dep = min(amt, p.deposit)
        p.deposit -= take_dep
        p.minted -= (amt - take_dep)
        self.wallet(dst).U += amt
        self._log("fee_out", amt, f"pool:{case_id}", dst, case_id, note)

    # ---- totals -----------------------------------------------------------
    def total_credits(self) -> float:
        tot = sum(w.W for w in self.wallets.values())
        tot += sum(p.escrow + p.deposit + p.minted for p in self.pools.values())
        return tot
