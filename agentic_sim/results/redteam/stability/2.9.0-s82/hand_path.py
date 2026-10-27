"""The hand cell (run 24's population, --entry-pool 20 --stampers 0.6) under 2.9.0: the dial per seat's path per period — m^A, π^A, F̂^A
on the planted approvals' audit adjudications, m^La / m^Ld on the planted lies', the quotas and the counts (the rc's §8.3 'the multipliers'
path per period read')."""
import sys
sys.path.insert(0, ".")
from drivers import stamping
from drivers.stamping import Stamping
seeds = [int(x) for x in sys.argv[1].split(",")]
cell = sys.argv[2:] or ["--entry-pool", "20", "--stampers", "0.6"]
for s in seeds:
    a = stamping.parse_args(cell + ["--seed", str(s), "--ticks", "1000"])
    run = Stamping(a)
    for t in range(1, 1001):
        run.tick(t)
    per = run.w.dial()["periods"]
    print(f"\n== seed {s}  cell {' '.join(cell)}  periods {len(per)}")
    print("| p | t | real approvals | pa posted / verdicts | pa audit adj / confirmed | F̂^A | m^A before → after | π^A | real appeals / disputes | lie quota a / d | lies filed a / d | lie adj a / d | lie sided a / d | F̂^La | F̂^Ld | m^La | m^Ld | π^La | π^Ld | discharged |")
    print("|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|")
    for i, p in enumerate(per):
        g = lambda k, d="—": p.get(k, d)
        lq = g("lie_quota", {}) or {}
        lf = g("lies_filed", {}) or {}
        la = g("lie_adj", {}) or {}
        ls = g("lie_sided", {}) or {}
        f = lambda x, d=3: ("—" if x in (None, "—") else (f"{x:.{d}f}" if isinstance(x, float) else str(x)))
        print(f"| {i} | {g('t')} | {g('real_approvals')} | {g('pa_posted')} / {g('pa_verdicts')} | {g('pa_audit_adj')} / {g('pa_audit_confirmed')} | {f(g('F_hat_A'))} | {f(g('m_A_before'),2)} → {f(g('m_A'),2)} | {f(g('pi_A'))} | {g('real_appeals')} / {g('real_disputes')} | {f(lq.get('appeal'),1)} / {f(lq.get('dispute'),1)} | {lf.get('appeal','—')} / {lf.get('dispute','—')} | {la.get('appeal','—')} / {la.get('dispute','—')} | {ls.get('appeal','—')} / {ls.get('dispute','—')} | {f(g('F_hat_La'))} | {f(g('F_hat_Ld'))} | {f(g('m_La'),2)} | {f(g('m_Ld'),2)} | {f(g('pi_La'))} | {f(g('pi_Ld'))} | {g('obligations_discharged')} |")
    keys = sorted(k for k in per[-1].keys() if any(x in k for x in ("pa_", "lie", "m_A", "pi_A", "pi_L", "m_L", "F_hat", "real_", "oblig")))
    print("period keys:", keys)
