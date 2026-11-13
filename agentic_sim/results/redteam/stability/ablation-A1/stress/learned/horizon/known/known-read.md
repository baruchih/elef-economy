# The known-answer test and the return's spread (I5's second and third tests) — the direct policy and the world model at a horizon to the slot's exit, γ 0.98

## The first review dosed at 0.3 on 1 slot in 4 (the pin; 20 episodes, 97246 decisions)

**(i) The return's spread, with the decisions behind each action at each seat** (the return to the slot's exit at γ 0.98, real; pooled over the 20 episodes):

| slots | seat | action | n | mean | SD | SE |
|---|---|---|---|---|---|---|
| all | audit | inspect | 30071 | 224.6 | 133.4 | 0.8 |
| all | initial | inspect | 55678 | 204.4 | 161.4 | 0.7 |
| all | initial | claim | 3200 | 155.3 | 151.1 | 2.7 |
| all | panel | inspect | 8297 | 217.5 | 128.9 | 1.4 |
| dosing | audit | inspect | 1989 | 245.9 | 147.0 | 3.3 |
| dosing | initial | inspect | 7603 | 161.3 | 151.9 | 1.7 |
| dosing | initial | claim | 3200 | 155.3 | 151.1 | 2.7 |
| dosing | panel | inspect | 516 | 227.7 | 146.2 | 6.4 |

**The data's own answer at the initial seat on the dosing slots** (a claim there the policy's coin): the return after a claim less after an inspection, per episode, **-5.5 ± 2.3** real over 20 episodes.

**(ii) The direct policy** fit at the horizon (40 epochs; `direct-mc.pt`), read on every initial-seat observation: the fitted return of a claim less an inspection, per seed, **-38.5 ± 4.6** real. the direct: fitted -38.5 ± 4.6 against the known -23.1 ± 3.5 — the sign the same, within a factor of three → **passed**.

**(iii) The world model** fit the same way (`wm-mc.pt`), read by the head alone as reward + γ V(next) on the initial-seat observations (up to 400 a seed): a claim less an inspection **-4.8 ± 0.4** real (the reward head's one decision alone +0.7 ± 0.1). the world model: fitted -4.8 ± 0.4 against the known -23.1 ± 3.5 — the sign the same, OUTSIDE a factor of three → **FAILED**.

## The member's audit seat dosed at 0.3 on 1 slot in 4 (the pin; 20 episodes, 91644 decisions)

**(i) The return's spread, with the decisions behind each action at each seat** (the return to the slot's exit at γ 0.98, real; pooled over the 20 episodes):

| slots | seat | action | n | mean | SD | SE |
|---|---|---|---|---|---|---|
| all | audit | inspect | 25975 | 199.0 | 130.6 | 0.8 |
| all | audit | claim | 1205 | 206.8 | 158.4 | 4.6 |
| all | initial | inspect | 57670 | 186.0 | 166.7 | 0.7 |
| all | panel | inspect | 6794 | 193.1 | 125.7 | 1.5 |
| dosing | audit | inspect | 2712 | 201.1 | 140.3 | 2.7 |
| dosing | audit | claim | 1205 | 206.8 | 158.4 | 4.6 |
| dosing | initial | inspect | 10107 | 186.4 | 171.2 | 1.7 |
| dosing | panel | inspect | 988 | 183.4 | 129.0 | 4.1 |

**The data's own answer at the audit seat on the dosing slots** (a claim there the policy's coin): the return after a claim less after an inspection, per episode, **+2.6 ± 4.5** real over 20 episodes.

**(ii) The direct policy** fit at the horizon (40 epochs; `direct-mc.pt`), read on every audit-seat observation: the fitted return of a claim less an inspection, per seed, **+2.7 ± 3.0** real. the direct: the known answer (-4.0 ± 4.8, 60 seeds) cannot be told from nothing — not tested here.

**(iii) The world model** fit the same way (`wm-mc.pt`), read by the head alone as reward + γ V(next) on the audit-seat observations (up to 400 a seed): a claim less an inspection **-2.2 ± 0.3** real (the reward head's one decision alone +3.3 ± 0.2). the world model: the known answer (-4.0 ± 4.8, 60 seeds) cannot be told from nothing — not tested here.

## The member's audit seat dosed at 1.0 on 1 slot in 4 (the pin; 20 episodes, 89559 decisions)

**(i) The return's spread, with the decisions behind each action at each seat** (the return to the slot's exit at γ 0.98, real; pooled over the 20 episodes):

| slots | seat | action | n | mean | SD | SE |
|---|---|---|---|---|---|---|
| all | audit | inspect | 24259 | 210.7 | 131.2 | 0.8 |
| all | audit | claim | 1579 | 171.7 | 170.3 | 4.3 |
| all | initial | inspect | 57270 | 186.9 | 165.8 | 0.7 |
| all | panel | inspect | 6451 | 199.5 | 133.1 | 1.7 |
| dosing | audit | claim | 1579 | 171.7 | 170.3 | 4.3 |
| dosing | initial | inspect | 10627 | 176.2 | 168.0 | 1.6 |
| dosing | panel | inspect | 422 | 164.2 | 150.5 | 7.3 |

**The data's own answer at the audit seat on the dosing slots** (a claim there the policy's coin): the return after a claim less after an inspection, per episode, **+nan ± nan** real over 0 episodes.

**(ii) The direct policy** fit at the horizon (40 epochs; `direct-mc.pt`), read on every audit-seat observation: the fitted return of a claim less an inspection, per seed, **+7.1 ± 8.1** real. the direct: fitted +7.1 ± 8.1 against the known -15.0 ± 2.9 — the sign OPPOSITE, OUTSIDE a factor of three → **FAILED**.

**(iii) The world model** fit the same way (`wm-mc.pt`), read by the head alone as reward + γ V(next) on the audit-seat observations (up to 400 a seed): a claim less an inspection **-4.0 ± 0.7** real (the reward head's one decision alone +4.6 ± 0.2). the world model: fitted -4.0 ± 0.7 against the known -15.0 ± 2.9 — the sign the same, OUTSIDE a factor of three → **FAILED**.

## The member's audit seat dosed at 0.3 on 1 slot in 4 (J4's world 5 cell: π^A 0.30, the fee doubled; 20 episodes, 99427 decisions)

**(i) The return's spread, with the decisions behind each action at each seat** (the return to the slot's exit at γ 0.98, real; pooled over the 20 episodes):

| slots | seat | action | n | mean | SD | SE |
|---|---|---|---|---|---|---|
| all | audit | inspect | 30750 | 233.1 | 128.0 | 0.7 |
| all | audit | claim | 939 | 203.1 | 140.7 | 4.6 |
| all | initial | inspect | 56761 | 188.0 | 171.0 | 0.7 |
| all | panel | inspect | 10977 | 220.8 | 123.3 | 1.2 |
| dosing | audit | inspect | 2229 | 205.8 | 129.7 | 2.7 |
| dosing | audit | claim | 939 | 203.1 | 140.7 | 4.6 |
| dosing | initial | inspect | 10239 | 173.7 | 157.2 | 1.6 |
| dosing | panel | inspect | 996 | 195.8 | 121.7 | 3.9 |

**The data's own answer at the audit seat on the dosing slots** (a claim there the policy's coin): the return after a claim less after an inspection, per episode, **-5.2 ± 4.5** real over 20 episodes.

**(ii) The direct policy** fit at the horizon (40 epochs; `direct-mc.pt`), read on every audit-seat observation: the fitted return of a claim less an inspection, per seed, **-22.6 ± 5.2** real. the direct: fitted -22.6 ± 5.2 against the known -45.1 ± 7.7 — the sign the same, within a factor of three → **passed**.

**(iii) The world model** fit the same way (`wm-mc.pt`), read by the head alone as reward + γ V(next) on the audit-seat observations (up to 400 a seed): a claim less an inspection **-3.8 ± 0.5** real (the reward head's one decision alone +1.1 ± 0.2). the world model: fitted -3.8 ± 0.5 against the known -45.1 ± 7.7 — the sign the same, OUTSIDE a factor of three → **FAILED**.

