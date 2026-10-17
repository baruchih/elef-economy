"""A minimal stand-in for the pytest helpers the suites use (approx, raises,
mark.parametrize), so the tests run with plain `python3 run_tests.py` where pytest is
not installed. With pytest present it is unused."""
from __future__ import annotations
import math
from contextlib import contextmanager


class _Approx:
    def __init__(self, expected, rel=1e-6, abs=1e-9):
        self.expected, self.rel, self.abs = expected, rel, abs

    def __eq__(self, other):
        e = self.expected
        if isinstance(e, (tuple, list)):
            if not isinstance(other, (tuple, list)) or len(other) != len(e):
                return False
            return all(_Approx(a, self.rel, self.abs) == b for a, b in zip(e, other))
        return math.isclose(float(other), float(e), rel_tol=self.rel, abs_tol=max(self.abs, 1e-12))

    def __req__(self, other):
        return self.__eq__(other)

    def __repr__(self):
        return f"approx({self.expected})"


def approx(expected, rel=1e-6, abs=1e-9):
    return _Approx(expected, rel, abs)


@contextmanager
def raises(exc_type, match=None):
    """`match`, as in pytest: a regular expression searched in str(the exception)."""
    import re
    try:
        yield
    except exc_type as e:
        if match is not None and not re.search(match, str(e)):
            raise AssertionError(f"expected {exc_type} matching {match!r}, got: {e}") from e
        return
    except Exception as e:  # noqa: BLE001
        raise AssertionError(f"expected {exc_type}, got {type(e).__name__}: {e}") from e
    raise AssertionError(f"expected {exc_type} to be raised")


class _MarkInfo:
    def __init__(self, name, args):
        self.name, self.args = name, args


class _Mark:
    @staticmethod
    def parametrize(names, values):
        def deco(fn):
            marks = list(getattr(fn, "pytestmark", []))
            marks.append(_MarkInfo("parametrize", (names, list(values))))
            fn.pytestmark = marks
            return fn
        return deco


class pytest:  # noqa: N801
    approx = staticmethod(approx)
    raises = staticmethod(raises)
    mark = _Mark()
