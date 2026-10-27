import sys, collections
sys.path.insert(0, ".")
from drivers.stamping import Stamping, parse_args
seed = sys.argv[1]; rules = sys.argv[2]; extra = sys.argv[3:]
a = parse_args(["--entry-pool", "20", "--stampers", "0.6", "--dispute-policy", "truthful", "--seed", seed, "--rules", rules] + extra)
run = Stamping(a)
for t in range(1, a.ticks + 1):
    run.tick(t)
W = run.w._w
stuck = []; disputed_lost = 0; disputed = 0; delays = collections.Counter(); gaps = collections.Counter(); durs = collections.Counter(); audits = 0; approvals = 0
for c in W.cases.values():
    if not c.is_root or c.plant is not None:
        continue
    inits = [W.reviews[x] for x in c.reviews if W.reviews[x].role == "initial" and W.reviews[x].verdict is not None]
    if inits and c.t_submit is not None and c.t_verdict is not None and not W.is_troop(inits[0].reviewer):
        delays[c.t_verdict - c.t_submit] += 1; gaps[inits[0].t_assign - c.t_submit] += 1; durs[(inits[0].t_done or c.t_verdict) - inits[0].t_assign] += 1
    if any(W.reviews[x].role == "audit" for x in c.reviews): audits += 1
    if c.verdict == "F": approvals += 1
    ch = c.challenge
    if ch is not None and ch.get("kind") == "dispute":
        disputed += 1
        if ch.get("resolved") and ch.get("outcome") == "F": disputed_lost += 1
    if c.state == "PENDING" and not c.final and c.audit_obligation and ch is not None and ch.get("resolved") and W.t > c.window_end:
        stuck.append((c.id, c.t_verdict, ch.get("kind"), ch.get("outcome"), c.open_items))
n = sum(delays.values())
print("seed", seed, rules, extra, "t", W.t)
print("real roots disputed", disputed, "lost (F upheld)", disputed_lost, "| STUCK pending past the window with an obligation and a resolved challenge:", len(stuck), stuck[:6])
print("audits held (roots with an audit review)", audits, "approvals (F verdicts)", approvals)
print("verdict delay t_verdict - t_submit:", {k: round(v / n, 3) for k, v in sorted(delays.items())[:8]}, "share >= 2:", round(sum(v for k, v in delays.items() if k >= 2) / n, 3))
print("seating gap:", {k: round(v / n, 3) for k, v in sorted(gaps.items())[:6]}, "review duration:", {k: round(v / n, 3) for k, v in sorted(durs.items())[:6]})
