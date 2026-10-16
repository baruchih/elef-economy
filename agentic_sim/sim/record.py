"""The record on disk: an engineering concern, not a rule.

The engine keeps every History entry, every ledger event, every case and every review for
the whole run, because the full audit (`check_all`) re-derives the §17 invariants from all
of them. In memory that is about sixteen kilobytes per case, and a long run outgrows RAM
before it runs out of time. With `Params.record_dir` set, the record goes to files under
that directory and RAM holds the working set:

  history.jsonl   one committed entry per line, the chain in order (the authoritative record)
  events.jsonl    the ledger's copy of its events, one per line
  cases.pickle    snapshots of settled cases, newest per id wins
  reviews.pickle  snapshots of their reviews

`Journal` is an append-only sequence written through to a file, with the newest items kept
decoded in memory; it stands in for the lists `History.entries` and `Ledger.events`.
`Archive` holds pickled snapshots by sequential id. `PagedDict` is the mapping the engine
reads `cases` and `reviews` through: an object is resident while it can still change, is
paged out to the archive when the working set lets it go, and comes back resident when the
engine touches it again. Nothing here decides anything; with `record_dir` unset the engine
uses plain lists and dicts and these classes are not instantiated.

Two properties keep record mode indistinguishable from memory mode to a caller:

  identity   an object handed out before it was paged out is the object handed back after —
             `PagedDict` remembers paged-out objects weakly and returns the same one while
             anything still holds it, so a reference kept across ticks does not go stale;
  pickling   a `Journal` pickles as the list it replaces and a `PagedDict` as the dict, so a
             snapshot of the world (the reviewer tests hash `pickle.dumps(w)`) is the same
             object graph in both modes.
"""
from __future__ import annotations
from array import array
from collections import OrderedDict
from itertools import islice
from typing import Callable, Iterator, Optional
import pickle
import weakref


class Journal:
    """An append-only sequence of records, one line each in a file. The last `tail` records
    stay decoded in memory, so the engine's own reads (the newest entry, the events of the
    tick just checked) cost nothing; older positions are read back from the file. Supports
    `len`, indexing, slicing and iteration like the list it replaces. Item and slice
    assignment rewrite the file from the first changed position — they exist so that a test
    can tamper with a copy as it would with the list; the engine never assigns. Not for
    appending while an iteration is in progress."""

    def __init__(self, path: str, encode: Callable, decode: Callable, tail: int = 4096):
        self.path = path
        self._encode, self._decode = encode, decode
        self._offsets = array("Q")
        self._tail: list = []
        self._tail_start = 0                      # position of _tail[0]
        self._tail_max = max(1, tail)
        self._w = open(path, "wb")
        self._r = open(path, "rb")
        self._size = 0
        self._pending = False

    def append(self, obj, line: Optional[str] = None):
        data = (line if line is not None else self._encode(obj)).encode("utf-8") + b"\n"
        self._offsets.append(self._size)
        self._w.write(data)
        self._size += len(data)
        self._pending = True
        self._tail.append(obj)
        if len(self._tail) > 2 * self._tail_max:
            del self._tail[: self._tail_max]
            self._tail_start += self._tail_max

    def __len__(self) -> int:
        return len(self._offsets)

    def _flush(self):
        if self._pending:
            self._w.flush()
            self._pending = False

    def iter_from(self, start: int = 0) -> Iterator:
        n = len(self._offsets)
        if start < 0:
            start += n
        start = max(start, 0)
        if start >= n:
            return
        first_tail = self._tail_start
        if start < first_tail:
            self._flush()
            self._r.seek(self._offsets[start])
            for _ in range(start, first_tail):
                yield self._decode(self._r.readline().decode("utf-8"))
            start = first_tail
        for i in range(start, n):
            yield self._tail[i - first_tail]

    def __iter__(self) -> Iterator:
        return self.iter_from(0)

    def __getitem__(self, i):
        n = len(self._offsets)
        if isinstance(i, slice):
            start, stop, step = i.indices(n)
            if step == 1:
                return list(islice(self.iter_from(start), max(0, stop - start)))
            return [self[k] for k in range(start, stop, step)]
        if i < 0:
            i += n
        if not 0 <= i < n:
            raise IndexError(i)
        if i >= self._tail_start:
            return self._tail[i - self._tail_start]
        self._flush()
        self._r.seek(self._offsets[i])
        return self._decode(self._r.readline().decode("utf-8"))

    def _rewrite(self, start: int, items: list):
        """Replace everything from `start` on with `items`: truncate the file there and append."""
        self._flush()
        self._size = self._offsets[start] if start < len(self._offsets) else self._size
        self._w.seek(self._size)
        self._w.truncate(self._size)
        self._r.close()                           # its buffer may hold the bytes just truncated
        self._r = open(self.path, "rb")
        del self._offsets[start:]
        self._tail, self._tail_start = [], start
        for obj in items:
            self.append(obj)

    def __setitem__(self, i, value):
        n = len(self._offsets)
        if isinstance(i, slice):
            start, stop, step = i.indices(n)
            if step != 1:
                raise TypeError("journal slice assignment needs a step of 1")
            rest = self[stop:]
            self._rewrite(start, list(value) + rest)
            return
        if i < 0:
            i += n
        if not 0 <= i < n:
            raise IndexError(i)
        rest = self[i + 1:]
        self._rewrite(i, [value] + rest)

    def __reduce__(self):
        return list, (list(self),)              # a snapshot of a journal is the list it replaces

    def close(self):
        self._flush()
        self._w.close()
        self._r.close()


class Archive:
    """Pickled snapshots keyed by an id of the form `<letter><number>` ("q17"). Appending a
    key again supersedes its earlier snapshot; the index is two arrays by number."""

    def __init__(self, path: str):
        self.path = path
        self._w = open(path, "wb")
        self._r = open(path, "rb")
        self._off = array("Q")
        self._len = array("Q")
        self._size = 0
        self._pending = False

    @staticmethod
    def _num(key: str) -> int:
        return int(key[1:])

    def __contains__(self, key: str) -> bool:
        n = self._num(key)
        return n < len(self._len) and self._len[n] > 0

    def put(self, key: str, obj):
        n = self._num(key)
        while len(self._off) <= n:
            self._off.append(0)
            self._len.append(0)
        blob = pickle.dumps(obj, protocol=pickle.HIGHEST_PROTOCOL)
        self._off[n], self._len[n] = self._size, len(blob)
        self._w.write(blob)
        self._size += len(blob)
        self._pending = True

    def get(self, key: str):
        if key not in self:
            raise KeyError(key)
        if self._pending:
            self._w.flush()
            self._pending = False
        n = self._num(key)
        self._r.seek(self._off[n])
        return pickle.loads(self._r.read(self._len[n]))

    def close(self):
        self._w.close()
        self._r.close()


class PagedDict:
    """A mapping from sequential ids ("q1", "q2", …) to objects, iterated in creation order,
    whose settled objects live in an `Archive`.

    `d[k]` and `d.get(k)` return the *resident* object, loading it from the archive if it was
    paged out — for callers that may change it (the engine). `d.peek(k)` and iteration
    return a resident object when there is one and otherwise a transient copy — for readers
    that must not change anything and must not pull the archive into memory (the audit).
    `evict(k)` writes a resident object to the archive and drops it, keeping a weak reference:
    while anyone still holds the object, every later read returns that same object, so
    identity is what it is in memory. `pack`/`unpack` let the owner bundle side state with the
    snapshot: `pack(obj)` returns what is pickled; `unpack(blob, resident)` returns the object
    and, when `resident`, restores the side state."""

    def __init__(self, archive: Archive, prefix: str, pack: Optional[Callable] = None,
                 unpack: Optional[Callable] = None, peek_cache: int = 4096):
        self._arch = archive
        self._prefix = prefix
        self._pack = pack or (lambda o: o)
        self._unpack = unpack or (lambda blob, resident: blob)
        self._res: dict = {}
        self._count = 0
        self._max = 0
        self._peek: OrderedDict = OrderedDict()
        self._peek_max = peek_cache
        self._ghosts: weakref.WeakValueDictionary = weakref.WeakValueDictionary()

    # -- mapping protocol ------------------------------------------------
    def __setitem__(self, key: str, obj):
        if key not in self._res and key not in self._arch:
            self._count += 1
            self._max = max(self._max, Archive._num(key))
        self._res[key] = obj
        self._peek.pop(key, None)

    def __contains__(self, key) -> bool:
        return key in self._res or (isinstance(key, str) and key[:1] == self._prefix
                                    and key[1:].isdigit() and key in self._arch)

    def __len__(self) -> int:
        return self._count

    def __getitem__(self, key: str):
        o = self._res.get(key)
        if o is None:
            if key not in self:
                raise KeyError(key)
            o = self._unpack(self._arch.get(key), True)
            ghost = self._ghosts.pop(key, None)
            if ghost is not None:
                o = ghost                        # the object someone still holds, unchanged since
            self._res[key] = o
            self._peek.pop(key, None)
        return o

    def get(self, key, default=None):
        return self[key] if key in self else default

    def __iter__(self):
        return iter(self.keys())

    def keys(self):
        for n in range(1, self._max + 1):
            k = f"{self._prefix}{n}"
            if k in self._res or k in self._arch:
                yield k

    def values(self):
        for k in self.keys():
            yield self.peek(k, cache=False)

    def items(self):
        for k in self.keys():
            yield k, self.peek(k, cache=False)

    def __reduce__(self):
        return dict, (dict(self.items()),)      # a snapshot of a paged mapping is the dict it replaces

    # -- paging ------------------------------------------------------------
    def peek(self, key: str, cache: bool = True):
        """Read without taking responsibility for the object: the resident one if any, the one
        still held somewhere if any, else a copy. Recently peeked copies are kept in a small
        cache; a residentized or evicted key leaves it, so a stale copy is never returned."""
        o = self._res.get(key)
        if o is not None:
            return o
        o = self._ghosts.get(key)
        if o is not None:
            return o
        o = self._peek.get(key)
        if o is not None:
            self._peek.move_to_end(key)
            return o
        o = self._unpack(self._arch.get(key), False)
        if cache:
            self._peek[key] = o
            if len(self._peek) > self._peek_max:
                self._peek.popitem(last=False)
        return o

    def is_resident(self, key: str) -> bool:
        return key in self._res

    def resident_items(self) -> list:
        return list(self._res.items())

    def evict(self, key: str):
        o = self._res.pop(key)
        self._arch.put(key, self._pack(o))
        self._ghosts[key] = o
        self._peek.pop(key, None)

    def close(self):
        self._arch.close()
