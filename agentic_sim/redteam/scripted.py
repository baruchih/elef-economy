"""The scripted wrappers of the stressed world's reads, shared by run_q (the evaluations) and collect (the data): the mixed world's `mix:<policy>[:<share>]`
(addendum 7's F4.1 and addendum 8's entry test) and the dose `dose<q>[audit|first]` (addendum 9's I4.1). Moved here from run_q on November 13, 2026 so that a
collection can carry them too (the learner with a horizon's known-answer test reads a dose world's data); the classes are unchanged, run_q imports them."""
from __future__ import annotations
import hashlib

from redteam.obs import IDX


class MixPolicy:
    """Addendum 7's F4.1 (November 12, 2026), trap or equilibrium: one world, the stressed policy of record on half the slots and the careful on the
    other half. The half is drawn once per slot by a stable hash of the seed and the slot's name (arrivals join by the same draw), so the two halves
    are the same names in every finalist at a seed. The episode loop tells the policy the deciding identity before each decision; its readings are
    tallied by half in `episode` (`half_claim_*` the policy's half, `half_care_*` the careful's). The careful half answers 0 everywhere (a stay at a boundary).
    Addendum 8's entry test (November 12, 2026): `mix:<policy>:<share>` puts the policy on that share of the slots — a reader-side option, the draw the
    same hash read against the share (the first two bytes against share × 65536; at 0.5 the halves of record to the name, since the first byte < 128
    is the same test); the groups keep the `half_claim_*` / `half_care_*` keys, `half_share` records the share."""
    def __init__(self, inner, name, share=0.5):
        self.inner, self.name, self.identity, self.seed, self.share = inner, name, None, None, float(share)
    def set_identity(self, identity, seed):
        self.identity, self.seed = identity, seed
    def set_info(self, info):                                   # addendum 9: the decision's seat kind, forwarded to a dose policy inside the mix
        if hasattr(self.inner, "set_info"): self.inner.set_info(info)
    def half_of(self, identity, seed=None):
        h = int.from_bytes(hashlib.md5(f"{self.seed if seed is None else seed}:{identity}".encode()).digest()[:2], "big")
        return "claim" if h < self.share * 65536 else "care"
    def __call__(self, obs, rng):
        return self.inner(obs, rng) if self.half_of(self.identity) == "claim" else 0


class DosePolicy:
    """Addendum 9's dose (November 12, 2026; the reviewer's I4.1): a scripted policy — careful, and at each review decision a claim (the stressed world's
    fourth action) with probability q, drawn from the episode's rng; `dose<q>` at every review seat, `dose<q>audit` at the member's audit seat only and
    `dose<q>first` at the first review only, the seat kind read from the env's info (`seat`: initial | audit | panel | resumed, from the view alone — the
    seat table's source). A reader-side wrapper, as the share was: nothing in the engine or the driver; a stay at every boundary."""
    def __init__(self, q, seats=None):
        self.q, self.seats, self.seat = float(q), seats, None
    def set_info(self, info):
        self.seat = info.get("seat") or ("initial" if info.get("initial", True) else "audit")
    def __call__(self, obs, rng):
        if obs[IDX["decision_boundary"]] > 0.5: return 0
        if self.seats == "audit" and self.seat != "audit": return 0
        if self.seats == "first" and self.seat != "initial": return 0
        return 3 if rng.random() < self.q else 0


def scripted_of(name, make):
    """`mix:<policy>[:<share>]` and `dose<q>[audit|first]` built around `make(name)` (the caller's factory for the inner policy); None for any other name."""
    if name.startswith("mix:"):
        parts = name[4:].split(":")
        return MixPolicy(make(parts[0]), name, share=float(parts[1]) if len(parts) > 1 else 0.5)
    if name.startswith("dose"):
        rest = name[4:]; seats = "audit" if rest.endswith("audit") else ("first" if rest.endswith("first") else None)
        return DosePolicy(rest[:-5] if seats in ("audit", "first") else rest, seats)
    return None
