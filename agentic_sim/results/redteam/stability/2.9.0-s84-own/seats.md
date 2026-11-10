# §8.4 — the probe at every seat (AUC, chance 0.5; ± the bootstrap SE over seeds)


## `learned-rev-careful-290-own` (the population under the direct's final policy, `online11`; the ε set the floor)

| set | seat | test decisions | plant share | raw obs | context only | case fields only | latent | **gap raw − context** | top case fields (added to context) |
|---|---|---|---|---|---|---|---|---|---|
| online11 | all | 43,949 | 0.114 | 0.654 ± 0.010 | 0.596 ± 0.017 | 0.596 ± 0.009 | 0.625 ± 0.011 | **+0.0575 ± 0.0078** |  |
| online11 | initial | 29,069 | 0.111 | 0.623 ± 0.015 | 0.619 ± 0.015 | 0.516 ± 0.007 | 0.591 ± 0.019 | **+0.0036 ± 0.0016** | seen_beta_rel +0.0006, rv_gap +0.0004, seen_ticks_since +0.0002 |
| online11 | audit | 11,644 | 0.075 | 0.604 ± 0.021 | 0.607 ± 0.019 | 0.514 ± 0.019 | 0.580 ± 0.016 | **-0.0024 ± 0.0038** | rv_gap +0.0003, seen_before +0.0001, seen_beta_rel +0.0001 |
| online11 | panel | 3,236 | 0.274 | 0.623 ± 0.005 | 0.585 ± 0.005 | 0.572 ± 0.024 | 0.601 ± 0.008 | **+0.0378 ± 0.0028** | rv_q_dispute +0.0387, rv_q_appeal +0.0387, seen_beta_rel +0.0010 |
| online11 | appeal | 3,171 | 0.259 | 0.593 ± 0.007 | 0.594 ± 0.007 | 0.538 ± 0.026 | 0.582 ± 0.007 | **-0.0010 ± 0.0014** | seen_beta_rel +0.0019, my_bid_lost +0.0016, seen_before +0.0010 |
| online11 | dispute | 65 | 1.000 | nan ± nan | nan ± nan | nan ± nan | nan ± nan | **+nan ± nan** | seen_ticks_since +nan, seen_beta_rel +nan, seen_before +nan |
| eps | all | 45,965 | 0.156 | 0.686 ± 0.006 | 0.644 ± 0.006 | 0.614 ± 0.009 | 0.654 ± 0.008 | **+0.0419 ± 0.0050** |  |
| eps | initial | 29,646 | 0.151 | 0.664 ± 0.008 | 0.662 ± 0.008 | 0.532 ± 0.012 | 0.647 ± 0.008 | **+0.0012 ± 0.0010** | seen_beta_rel +0.0004, my_bid_lost +0.0002, rv_gap +0.0001 |
| eps | audit | 11,047 | 0.097 | 0.644 ± 0.011 | 0.645 ± 0.011 | 0.545 ± 0.017 | 0.617 ± 0.015 | **-0.0014 ± 0.0006** | my_bid_lost +0.0001, rv_resumed +0.0000, rv_responses_available +0.0000 |
| eps | panel | 5,272 | 0.303 | 0.637 ± 0.011 | 0.610 ± 0.010 | 0.546 ± 0.012 | 0.600 ± 0.006 | **+0.0273 ± 0.0043** | rv_q_dispute +0.0300, rv_q_appeal +0.0300, rv_cap_rel +0.0006 |
| eps | appeal | 5,181 | 0.291 | 0.616 ± 0.011 | 0.618 ± 0.011 | 0.518 ± 0.013 | 0.592 ± 0.007 | **-0.0028 ± 0.0020** | rv_cap_rel +0.0008, rv_bond_rel +0.0008, seen_beta_rel +0.0001 |
| eps | dispute | 91 | 1.000 | nan ± nan | nan ± nan | nan ± nan | nan ± nan | **+nan ± nan** | seen_ticks_since +nan, seen_beta_rel +nan, seen_before +nan |

## `learned-rev-liars-290-own` (the population under the direct's final policy, `online11`; the ε set the floor)

| set | seat | test decisions | plant share | raw obs | context only | case fields only | latent | **gap raw − context** | top case fields (added to context) |
|---|---|---|---|---|---|---|---|---|---|
| online11 | all | 46,939 | 0.117 | 0.744 ± 0.007 | 0.608 ± 0.007 | 0.700 ± 0.005 | 0.707 ± 0.006 | **+0.1357 ± 0.0077** |  |
| online11 | initial | 28,925 | 0.117 | 0.632 ± 0.007 | 0.629 ± 0.007 | 0.540 ± 0.015 | 0.591 ± 0.009 | **+0.0021 ± 0.0013** | rv_gap +0.0005, my_bid_lost +0.0001, rv_resumed +0.0000 |
| online11 | audit | 10,790 | 0.013 | 0.688 ± 0.060 | 0.688 ± 0.061 | 0.382 ± 0.055 | 0.555 ± 0.086 | **+0.0005 ± 0.0020** | rv_cap_rel +0.0002, rv_bond_rel +0.0002, seen_ticks_since +0.0002 |
| online11 | panel | 7,224 | 0.273 | 0.618 ± 0.008 | 0.569 ± 0.009 | 0.604 ± 0.009 | 0.574 ± 0.007 | **+0.0490 ± 0.0096** | rv_q_dispute +0.0494, rv_q_appeal +0.0494, rv_gap +0.0060 |
| online11 | appeal | 3,454 | 0.202 | 0.579 ± 0.018 | 0.571 ± 0.019 | 0.562 ± 0.012 | 0.520 ± 0.010 | **+0.0084 ± 0.0047** | rv_gap +0.0122, my_bid_lost +0.0045, seen_beta_rel +0.0024 |
| online11 | dispute | 3,770 | 0.339 | 0.554 ± 0.009 | 0.558 ± 0.011 | 0.524 ± 0.016 | 0.550 ± 0.011 | **-0.0046 ± 0.0033** | rv_gap +0.0000, rv_resumed +0.0000, rv_responses_available +0.0000 |
| eps | all | 46,962 | 0.150 | 0.736 ± 0.007 | 0.627 ± 0.010 | 0.690 ± 0.008 | 0.704 ± 0.006 | **+0.1096 ± 0.0072** |  |
| eps | initial | 29,288 | 0.143 | 0.648 ± 0.012 | 0.646 ± 0.012 | 0.536 ± 0.011 | 0.623 ± 0.016 | **+0.0020 ± 0.0007** | my_bid_lost +0.0009, seen_beta_rel +0.0008, rv_resumed +0.0000 |
| eps | audit | 9,142 | 0.022 | 0.699 ± 0.040 | 0.700 ± 0.041 | 0.543 ± 0.047 | 0.688 ± 0.038 | **-0.0009 ± 0.0040** | rv_cap_rel +0.0001, rv_bond_rel +0.0001, seen_ticks_since +0.0000 |
| eps | panel | 8,532 | 0.310 | 0.627 ± 0.015 | 0.575 ± 0.010 | 0.609 ± 0.014 | 0.575 ± 0.012 | **+0.0524 ± 0.0132** | rv_q_dispute +0.0442, rv_q_appeal +0.0442, rv_gap +0.0219 |
| eps | appeal | 4,812 | 0.251 | 0.621 ± 0.009 | 0.588 ± 0.012 | 0.594 ± 0.016 | 0.545 ± 0.017 | **+0.0330 ± 0.0064** | rv_gap +0.0328, rv_cap_rel +0.0006, rv_bond_rel +0.0006 |
| eps | dispute | 3,720 | 0.386 | 0.553 ± 0.015 | 0.557 ± 0.015 | 0.466 ± 0.015 | 0.547 ± 0.010 | **-0.0045 ± 0.0013** | rv_gap +0.0000, rv_resumed +0.0000, rv_responses_available +0.0000 |
