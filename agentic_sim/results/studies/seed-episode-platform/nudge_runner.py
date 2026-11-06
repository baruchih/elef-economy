"""Run the driver with one libm site nudged by one ulp. Modes: exp|log|cos|sin|pow|all, direction up|down.
pow nudges Params.emission's result (the engine's one float power); exp/log/cos/sin nudge math.* and random's bound copies."""
import math, random, runpy, sys, importlib
site, direction = sys.argv[1], sys.argv[2]
d = math.inf if direction == "up" else -math.inf
def nudge(f): return lambda *a: math.nextafter(f(*a), d)
sys.path.insert(0, ".")
if site in ("exp", "all"): _e = math.exp; math.exp = nudge(_e); random._exp = nudge(_e)
if site in ("log", "all"): _l = math.log; math.log = nudge(_l); random._log = nudge(_l)
if site in ("cos", "all"): _c = math.cos; math.cos = nudge(_c); random._cos = nudge(_c)
if site in ("sin", "all"): _s = math.sin; math.sin = nudge(_s); random._sin = nudge(_s)
if site in ("pow", "all"):
    P = importlib.import_module("sim.params").Params
    _em = P.emission
    P.emission = lambda self, t: math.nextafter(_em(self, t), d)
sys.argv = sys.argv[3:]
runpy.run_path(sys.argv[0], run_name="__main__")
