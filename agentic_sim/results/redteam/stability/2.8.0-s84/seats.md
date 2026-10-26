# §8.4 — the probe at every seat (AUC, chance 0.5; ± the bootstrap SE over seeds)


## `learned-rev-careful-280` (the population under the direct's final policy, `online11`; the ε set the floor)

| set | seat | test decisions | plant share | raw obs | context only | case fields only | latent | **gap raw − context** | top case fields (added to context) |
|---|---|---|---|---|---|---|---|---|---|
| online11 | all | 34,229 | 0.199 | 0.660 ± 0.005 | 0.645 ± 0.006 | 0.594 ± 0.006 | 0.648 ± 0.005 | **+0.0155 ± 0.0017** | rv_responses_available +0.0104, rv_gap +0.0084, seen_beta_rel +0.0017 |
| online11 | initial | 28,968 | 0.208 | 0.659 ± 0.005 | 0.653 ± 0.006 | 0.585 ± 0.007 | 0.645 ± 0.005 | **+0.0060 ± 0.0012** | rv_gap +0.0016, seen_beta_rel +0.0016, seen_ticks_since +0.0006 |
| online11 | audit | 4,221 | 0.135 | 0.630 ± 0.013 | 0.632 ± 0.013 | 0.498 ± 0.011 | 0.609 ± 0.010 | **-0.0019 ± 0.0023** | rv_cap_rel +0.0009, rv_bond_rel +0.0009, my_bid_lost +0.0008 |
| online11 | panel | 1,040 | 0.222 | 0.570 ± 0.018 | 0.524 ± 0.020 | 0.534 ± 0.024 | 0.577 ± 0.025 | **+0.0463 ± 0.0139** | rv_gap +0.0425, my_bid_lost +0.0033, rv_cap_rel +0.0012 |
| eps | all | 45,275 | 0.122 | 0.673 ± 0.006 | 0.654 ± 0.007 | 0.567 ± 0.007 | 0.656 ± 0.009 | **+0.0183 ± 0.0026** | rv_responses_available +0.0148, rv_gap +0.0059, seen_beta_rel +0.0005 |
| eps | initial | 29,919 | 0.141 | 0.666 ± 0.009 | 0.663 ± 0.010 | 0.523 ± 0.010 | 0.646 ± 0.013 | **+0.0030 ± 0.0009** | seen_beta_rel +0.0005, rv_gap +0.0001, my_bid_lost +0.0001 |
| eps | audit | 11,094 | 0.079 | 0.654 ± 0.015 | 0.655 ± 0.015 | 0.512 ± 0.011 | 0.634 ± 0.014 | **-0.0007 ± 0.0009** | rv_cap_rel +0.0005, rv_bond_rel +0.0005, rv_resumed +0.0000 |
| eps | panel | 4,262 | 0.106 | 0.692 ± 0.016 | 0.663 ± 0.019 | 0.598 ± 0.012 | 0.634 ± 0.023 | **+0.0289 ± 0.0066** | rv_gap +0.0287, seen_beta_rel +0.0001, rv_resumed +0.0000 |

## `learned-rev-disputes-280` (the population under the direct's final policy, `online11`; the ε set the floor)

| set | seat | test decisions | plant share | raw obs | context only | case fields only | latent | **gap raw − context** | top case fields (added to context) |
|---|---|---|---|---|---|---|---|---|---|
| online11 | all | 45,425 | 0.202 | 0.715 ± 0.002 | 0.625 ± 0.006 | 0.658 ± 0.006 | 0.695 ± 0.002 | **+0.0904 ± 0.0052** | rv_q_dispute +0.0621, rv_q_fulfillment +0.0414, rv_responses_available +0.0134 |
| online11 | initial | 30,497 | 0.213 | 0.660 ± 0.006 | 0.655 ± 0.005 | 0.553 ± 0.016 | 0.640 ± 0.005 | **+0.0045 ± 0.0018** | seen_beta_rel +0.0017, seen_ticks_since +0.0007, seen_before +0.0004 |
| online11 | audit | 10,197 | 0.093 | 0.598 ± 0.010 | 0.595 ± 0.010 | 0.525 ± 0.013 | 0.578 ± 0.009 | **+0.0027 ± 0.0029** | rv_gap +0.0018, rv_cap_rel +0.0005, rv_bond_rel +0.0005 |
| online11 | panel | 4,731 | 0.367 | 0.783 ± 0.009 | 0.599 ± 0.008 | 0.752 ± 0.009 | 0.768 ± 0.010 | **+0.1849 ± 0.0100** | rv_q_dispute +0.1828, rv_q_appeal +0.1828, rv_gap +0.0144 |
| online11 | appeal | 2,008 | 0.108 | 0.567 ± 0.016 | 0.577 ± 0.017 | 0.479 ± 0.030 | 0.556 ± 0.014 | **-0.0094 ± 0.0048** | rv_cap_rel +0.0007, rv_bond_rel +0.0007, my_bid_lost +0.0005 |
| online11 | dispute | 2,723 | 0.559 | 0.607 ± 0.011 | 0.603 ± 0.010 | 0.541 ± 0.016 | 0.575 ± 0.013 | **+0.0043 ± 0.0037** | rv_gap +0.0044, seen_beta_rel +0.0016, seen_ticks_since +0.0011 |
| eps | all | 44,575 | 0.102 | 0.688 ± 0.008 | 0.624 ± 0.009 | 0.634 ± 0.010 | 0.665 ± 0.009 | **+0.0637 ± 0.0030** | rv_q_dispute +0.0293, rv_responses_available +0.0200, rv_gap +0.0114 |
| eps | initial | 29,559 | 0.121 | 0.631 ± 0.012 | 0.627 ± 0.011 | 0.521 ± 0.014 | 0.607 ± 0.012 | **+0.0036 ± 0.0013** | seen_beta_rel +0.0008, my_bid_lost +0.0004, rv_resumed +0.0000 |
| eps | audit | 10,329 | 0.045 | 0.641 ± 0.017 | 0.640 ± 0.017 | 0.542 ± 0.016 | 0.618 ± 0.015 | **+0.0018 ± 0.0016** | rv_cap_rel +0.0017, rv_bond_rel +0.0017, seen_beta_rel +0.0005 |
| eps | panel | 4,687 | 0.112 | 0.808 ± 0.010 | 0.610 ± 0.014 | 0.782 ± 0.016 | 0.791 ± 0.010 | **+0.1981 ± 0.0161** | rv_q_dispute +0.1995, rv_q_appeal +0.1995, rv_gap +0.0072 |
| eps | appeal | 3,663 | 0.044 | 0.628 ± 0.027 | 0.633 ± 0.025 | 0.555 ± 0.022 | 0.597 ± 0.022 | **-0.0049 ± 0.0071** | seen_ticks_since +0.0011, seen_before +0.0005, seen_beta_rel +0.0003 |
| eps | dispute | 1,024 | 0.354 | 0.552 ± 0.024 | 0.552 ± 0.024 | 0.525 ± 0.022 | 0.547 ± 0.022 | **-0.0003 ± 0.0039** | rv_cap_rel +0.0023, rv_bond_rel +0.0023, my_bid_lost +0.0007 |
