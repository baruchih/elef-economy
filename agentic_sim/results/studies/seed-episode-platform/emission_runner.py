"""Run the driver with the emission's power either native (the platform's libm pow) or correctly rounded (decimal at 40 digits, then the
double product E0 * p as the engine computes it). Logs (tick, History head) at every emission call. Usage: cr_runner.py native|cr LOG driver args..."""
import math, runpy, sys, importlib
from decimal import Decimal, localcontext
mode, log = sys.argv[1], sys.argv[2]
sys.path.insert(0, ".")
P = importlib.import_module("sim.params").Params
E = importlib.import_module("sim.engine")
_orig_advance = E.World.advance
f = open(log, "w")
def cr_pow2(x):
    with localcontext() as ctx:
        ctx.prec = 40
        return float(Decimal(2) ** Decimal(x))
if mode == "cr":
    P.emission = lambda self, t: self.E0 * cr_pow2(-t / self.H)
_w = {}
def advance(self, *a, **k):
    r = _orig_advance(self, *a, **k)
    f.write(f"{self.t} {self.history.head}\n")
    return r
E.World.advance = advance
sys.argv = sys.argv[3:]
runpy.run_path(sys.argv[0], run_name="__main__")
f.close()
