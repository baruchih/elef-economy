"""Where does this platform's libm `pow` leave the correctly rounded value on the emission's arguments? The engine's one transcendental
call is Params.emission: E0 * 2.0 ** (-t / H) (H 1000 on the defaults), so the thousand arguments of a 1,000-tick run are -t/1000.
The correctly rounded double comes from decimal at 60 digits. Usage: python3 -I pow_check.py [H] [ticks]"""
import sys, platform
from decimal import Decimal, getcontext
getcontext().prec = 60
H = float(sys.argv[1]) if len(sys.argv) > 1 else 1000.0; ticks = int(sys.argv[2]) if len(sys.argv) > 2 else 1000
bad = []
for t in range(ticks):
    x = -t / H; native = 2.0 ** x; cr = float(Decimal(2) ** Decimal(x))
    if native != cr:
        bad.append((t, native, cr, (native - cr) / abs(cr) / 2.220446049250313e-16))
print(f"{platform.platform()} {platform.machine()} python {platform.python_version()}: 2.0 ** (-t/{H:g}) leaves the correctly rounded double at {len(bad)} of {ticks} ticks")
for b in bad: print("  t=%d native=%r correctly rounded=%r (%+.2f ulp)" % b)
