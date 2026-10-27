import sys, collections
sys.path.insert(0, ".")
from drivers.stamping import Stamping, parse_args
seed = sys.argv[1] if len(sys.argv) > 1 else "21"
rules = sys.argv[2] if len(sys.argv) > 2 else "2.8.0"
a = parse_args(["--entry-pool", "20", "--stampers", "0.6", "--dispute-policy", "truthful", "--seed", seed, "--rules", rules])
run = Stamping(a)
for t in range(1, a.ticks + 1):
    run.tick(t)
W = run.w._w
roles = collections.Counter(); init_odds = collections.Counter(); init_F = 0; init_F_audited = 0; init_F_state_audit = 0; init_n = 0; no_initial_review = 0
troop_init = 0; troop_init_F = 0; troop_init_odds = collections.Counter(); mao = 0; troop_init_audited = 0
mt = []
for c in W.cases.values():
    if c.plant is not None:
        for (t, role, v) in c.plant_state_seats:
            roles[role] += 1
            if role == "initial":
                init_n += 1
                init_odds[round(c.audit_odds_at_verdict, 3) if c.audit_odds_at_verdict is not None else None] += 1
                if v == "F":
                    init_F += 1
                    if any(W.reviews[x].role == "audit" for x in c.reviews): init_F_audited += 1
                    if any(r2 == "audit" for (_, r2, _) in c.plant_state_seats): init_F_state_audit += 1
                if not any(W.reviews[x].role == "initial" for x in c.reviews): no_initial_review += 1
    elif c.is_root:
        inits = [W.reviews[x] for x in c.reviews if W.reviews[x].role == "initial" and W.reviews[x].status != "withdrawn"]
        if inits and W.is_troop(inits[0].reviewer):
            troop_init += 1
            if inits[0].verdict == "F":
                troop_init_F += 1
                troop_init_odds[round(c.audit_odds_at_verdict, 3) if c.audit_odds_at_verdict is not None else None] += 1
                if any(W.reviews[x].role == "audit" for x in c.reviews): troop_init_audited += 1
            if c.market_audit_only: mao += 1
print("seed", seed, "rules", rules, "m_t at end", round(W.m_t, 3), "p_floor", W.p.p_floor)
print("plant state seats by role", dict(roles))
print("plant initial seats by the state", init_n, "of which F", init_F, "audited by a member", init_F_audited, "audited by the state", init_F_state_audit, "; no initial Review in c.reviews", no_initial_review)
print("their audit_odds_at_verdict", dict(init_odds))
print("real roots with a troop at the initial seat", troop_init, "of which F", troop_init_F, "audited", troop_init_audited, "market_audit_only", mao)
print("their audit_odds_at_verdict", dict(troop_init_odds))
