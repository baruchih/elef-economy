# §8.2: the C5 retrained at 0.25 chains' finals (learned-rev-<cell>/{direct,wm}/eval/final/, seeds 21–40) beside the run 42's policies frozen at 0.25 chains' (/, eval/final/), the same seeds and references; paired C5 retrained at 0.25 − run 42's policies frozen at 0.25 by seed; within 2.9.0 paired against the hand; the 2.9.0 readings; the rounds' mix; the stages after the first verdict. Produced by finals-paired.py over the eval.json files.

## ablation-A1/detection/retrain-d0.25

| reading | C5 retrained at 0.25 direct | C5 retrained at 0.25 head alone | C5 retrained at 0.25 hand | C5 retrained at 0.25 careful | run 42's policies frozen at 0.25 direct | run 42's policies frozen at 0.25 head alone | run 42's policies frozen at 0.25 hand | run 42's policies frozen at 0.25 careful |
|---|---|---|---|---|---|---|---|---|
| mix care / approve / reject | 0.794 / 0.201 / 0.006 | 0.818 / 0.182 / 0.000 | 0.000 / 0.000 / 0.000 | 1.000 / 0.000 / 0.000 | 0.826 / 0.168 / 0.006 | — | 0.000 / 0.000 / 0.000 | 1.000 / 0.000 / 0.000 |
| initial seats stamped plant / real | 0.009 (5384) / 0.010 (52359) | 0.001 (5345) / 0.002 (52370) | 0.000 (12271) / 0.000 (48723) | 0.000 (5185) / 0.000 (52085) | 0.025 (5536) / 0.027 (52557) | — | 0.000 (12271) / 0.000 (48723) | 0.000 (5185) / 0.000 (52085) |
| audit seats stamped plant / real | 0.622 (1076) / 0.696 (23042) | 0.612 (1125) / 0.628 (23707) | 0.000 (2784) / 0.000 (26160) | 0.000 (1026) / 0.000 (25160) | 0.502 (1032) / 0.543 (21303) | — | 0.000 (2784) / 0.000 (26160) | 0.000 (1026) / 0.000 (25160) |
| panel seats stamped plant / real | 0.097 (1494) / 0.146 (3034) | 0.028 (1433) / 0.035 (3047) | 0.000 (3267) / 0.000 (4401) | 0.000 (1644) / 0.000 (4224) | 0.400 (1291) / 0.205 (2999) | — | 0.000 (3267) / 0.000 (4401) | 0.000 (1644) / 0.000 (4224) |
| initial seats blind, measured from the reviews, plant / real | 0.009 (5384) / 0.010 (52359) | 0.001 (5345) / 0.002 (52370) | 0.100 (12271) / 0.150 (48723) | 0.000 (5185) / 0.000 (52085) | 0.026 (5536) / 0.028 (52557) | — | 0.100 (12271) / 0.150 (48723) | 0.000 (5185) / 0.000 (52085) |
| audit seats blind, measured from the reviews, plant / real | 0.622 (1076) / 0.696 (23042) | 0.612 (1125) / 0.628 (23707) | 0.000 (2784) / 0.009 (26160) | 0.000 (1026) / 0.000 (25160) | 0.502 (1032) / 0.543 (21303) | — | 0.000 (2784) / 0.009 (26160) | 0.000 (1026) / 0.000 (25160) |
| panel seats blind, measured from the reviews, plant / real | 0.097 (1494) / 0.146 (3034) | 0.028 (1433) / 0.035 (3047) | 0.000 (3267) / 0.009 (4401) | 0.000 (1644) / 0.000 (4224) | 0.400 (1291) / 0.206 (2999) | — | 0.000 (3267) / 0.009 (4401) | 0.000 (1644) / 0.000 (4224) |
| planted approvals confirmed at the members' audit seat (pooled F̂^A) | 0.541 (412) | 0.619 (443) | 0.024 (381) | 0.037 (356) | — | — | — | — |
| non-initial seats stamped (share of decisions) | 0.604 (0.332) | 0.537 (0.337) | 0.000 (0.375) | 0.000 (0.359) | 0.496 (0.314) | — | 0.000 (0.375) | 0.000 (0.359) |
| false approvals (run) | 10.8 ± 1.0 | 9.9 ± 0.8 | 6.7 ± 0.6 | 2.0 ± 0.4 | 15.4 ± 1.2 | — | 6.7 ± 0.6 | 2.0 ± 0.4 |
| bad plants approved | 13.2 | 10.6 | 66.3 | 10.0 | 14.9 | — | 66.3 | 10.0 |
| good plants rejected | 3.2 | 2.9 | 7.0 | 3.1 | 3.5 | — | 7.0 | 3.1 |
| suspensions | 5.2 | 5.0 | 15.4 | 5.0 | 4.8 | — | 15.4 | 5.0 |
| audit overturn rate | 0.016 | 0.012 | 0.044 | 0.021 | 0.021 | — | 0.044 | 0.021 |
| audits held | 1913 | 1904 | 1924 | 1893 | 1946 | — | 1924 | 1893 |
| disputes filed | 7.8 | 7.7 | 23.5 | 7.1 | 11.0 | — | 23.5 | 7.1 |
| disputes won | 7.5 | 7.7 | 22.6 | 7.0 | 7.7 | — | 22.6 | 7.0 |
| appeals filed | 105.0 | 106.0 | 78.3 | 105.8 | 102.5 | — | 78.3 | 105.8 |
| appeals won | 100.7 | 102.8 | 76.2 | 102.8 | 97.5 | — | 76.2 | 102.8 |
| lying appeals (real) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | — | 0.0 | 0.0 |
| lying appeals paid | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | — | 0.0 | 0.0 |
| lying disputes (real) | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | — | 0.0 | 0.0 |
| lying disputes paid | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | — | 0.0 | 0.0 |
| slots alive | 23.4 | 23.2 | 20.6 | 23.3 | 22.6 | — | 20.6 | 23.3 |
| nominal surplus | 25185 ± 441 | 25979 ± 280 | 29930 ± 326 | 24515 ± 297 | 24494 ± 394 | — | 29930 ± 326 | 24515 ± 297 |
| real lifetime | 35147 ± 907 | 36133 ± 899 | 32661 ± 670 | 34718 ± 757 | 33734 ± 804 | — | 32661 ± 670 | 34718 ± 757 |
| tasks per 1,000 | 36.9 ± 0.4 | 36.4 ± 0.4 | 31.9 ± 0.2 | 36.3 ± 0.4 | 36.5 ± 0.3 | — | 31.9 ± 0.2 | 36.3 ± 0.4 |
| P_t | 15.4 ± 0.4 | 15.4 ± 0.4 | 19.9 ± 0.5 | 15.2 ± 0.4 | 15.6 ± 0.3 | — | 19.9 ± 0.5 | 15.2 ± 0.4 |
| members' price | 18.2 | 18.4 | 19.6 | 17.9 | 18.2 | — | 19.6 | 17.9 |
| requesters' wallet | 796 | 694 | 67 | 668 | 694 | — | 67 | 668 |
| state share | 0.001 | 0.001 | 0.021 | 0.001 | 0.001 | — | 0.021 | 0.001 |
| awarded | 2621 | 2621 | 2402 | 2609 | 2632 | — | 2402 | 2609 |
| idle for bond | 204 | 191 | 186 | 185 | 192 | — | 186 | 185 |
| cost of truth | 1805 ± 34 | 1815 ± 43 | 4207 ± 75 | 1921 ± 26 | 1715 ± 43 | — | 4207 ± 75 | 1921 ± 26 |
| state seats per real root | 0.350 | 0.335 | 0.317 | 0.298 | 0.402 | — | 0.317 | 0.298 |
| state seats per plant | 0.317 | 0.310 | 0.216 | 0.262 | 0.346 | — | 0.216 | 0.262 |
| F̂ | 0.066 | 0.053 | 0.065 | 0.061 | 0.073 | — | 0.065 | 0.061 |
| leak: false approvals per vested task | 0.0052 | 0.0048 | 0.0035 | 0.0010 | 0.0074 | — | 0.0035 | 0.0010 |
| leak: false approvals per bad delivery | 0.021 | 0.019 | 0.014 | 0.004 | 0.029 | — | 0.014 | 0.004 |
| system overhead a vested task | 9.044 | 9.124 | 15.972 | 10.044 | 9.280 | — | 15.972 | 10.044 |
| customers' overhead a vested task | 11.288 | 11.408 | 14.402 | 12.247 | 11.632 | — | 14.402 | 12.247 |
| ticks to vest p50 | 12.0 | 12.0 | 12.0 | 12.0 | 12.0 | — | 12.0 | 12.0 |
| ticks to vest p90 | 12.0 | 12.1 | 13.0 | 12.5 | 12.0 | — | 13.0 | 12.5 |
| rulings sought | 56.1 | 64.2 | 102.2 | 98.4 | 73.7 | — | 102.2 | 98.4 |
| rulings wrong | 10.3 | 13.2 | 20.8 | 20.9 | 14.9 | — | 20.8 | 20.9 |
| false penalties: initial seat | 20.65 | 13.05 | 22.80 | 22.65 | 23.95 | — | 22.80 | 22.65 |
| false penalties: audit seat | 0.10 | 0.05 | 0.20 | 0.15 | 0.10 | — | 0.20 | 0.15 |
| false penalties: panel seat | 4.95 | 7.15 | 14.30 | 14.25 | 7.00 | — | 14.30 | 14.25 |

The C5 retrained at 0.25 readings (means over the seeds):

| reading | C5 retrained at 0.25 direct | C5 retrained at 0.25 head alone | C5 retrained at 0.25 hand | C5 retrained at 0.25 careful |
|---|---|---|---|---|
| planted approvals posted | 29.8 | 30.6 | 25.6 | 24.9 |
| their verdicts | 29.4 | 30.2 | 25.5 | 24.9 |
| audited by a member | 20.6 | 22.1 | 19.1 | 17.8 |
| confirmed at the audit seat | 11.2 | 13.7 | 0.5 | 0.7 |
| rejected at the audit seat | 9.4 | 8.4 | 18.6 | 17.1 |
| third seats | 8.7 | 7.7 | 18.1 | 15.9 |
| audited by the state (past w_R) | 0.0 | 0.0 | 0.0 | 0.0 |
| the pass would have seated (read) | 0.0 | 0.0 | 0.1 | 0.0 |
| disputed first | 8.7 | 7.8 | 6.3 | 6.8 |
| the pass would have taken the audit seat (read) | 3.0 | 2.6 | 1.1 | 2.5 |
| unseated at the window's end (closed by truth) | 0.1 | 0.1 | 0.1 | 0.1 |
| obligations discharged at a dispute | 8.6 | 7.7 | 6.3 | 6.8 |
| closed | 29.2 | 29.9 | 25.4 | 24.8 |
| m^A at the end | 2.55 | 2.85 | 1.00 | 1.04 |
| π^A at the end | 0.051 | 0.057 | 0.020 | 0.021 |
| F̂^A (last period) | 0.525 | 0.668 | 0.000 | 0.059 |
| planted lies by the coin | 31.4 | 31.4 | 26.7 | 27.1 |
| planted lies by the floor | 12.7 | 12.5 | 30.3 | 12.1 |
| filing position in the period: real | 0.440 | 0.459 | 0.256 | 0.469 |
| truthful plant | 0.422 | 0.451 | 0.229 | 0.485 |
| planted lie | 0.433 | 0.429 | 0.216 | 0.429 |
| planted appeals filed | 33.2 | 33.1 | 35.8 | 28.3 |
| their seats answered by members | 33.7 | 32.9 | 53.9 | 29.8 |
| members siding with the lie | 3.1 | 2.9 | 2.1 | 1.1 |
| m^La at the end | 1.58 | 1.39 | 1.14 | 1.09 |
| π^La at the end | 0.394 | 0.346 | 0.285 | 0.273 |
| F̂^La (last period) | 0.085 | 0.123 | 0.038 | 0.050 |
| planted disputes filed | 10.6 | 10.4 | 21.1 | 10.4 |
| their seats answered by members | 8.7 | 9.3 | 27.1 | 11.8 |
| members siding with the lie | 0.8 | 0.3 | 1.5 | 0.8 |
| m^Ld at the end | 1.10 | 1.04 | 1.18 | 1.08 |
| π^Ld at the end | 0.275 | 0.260 | 0.295 | 0.271 |
| F̂^Ld (last period) | 0.178 | 0.035 | 0.053 | 0.065 |
| bad plants met at the initial seat | 204.9 | 199.9 | 464.3 | 196.3 |
| at the audit seat | 25.9 | 26.2 | 40.9 | 22.2 |
| at the third seat | 11.7 | 10.0 | 40.5 | 20.5 |
| at an appeal panel | 33.7 | 32.9 | 53.9 | 29.8 |
| at a dispute panel | 15.9 | 15.5 | 24.1 | 14.2 |
| member-periods | 119.5 | 118.4 | 236.8 | 116.3 |
| of them panel-ineligible | 82.3 | 78.2 | 78.3 | 63.5 |
| minted: the dial's plants | 13740 | 13532 | 25683 | 12855 |
| minted: the planted approvals | 1502 | 1517 | 1040 | 1229 |
| minted: the planted lies | 83 | 83 | 110 | 73 |
| minted: the alias reviewer's bonds | 133 | 141 | 122 | 115 |
| share of planted approvals audited by the state | 0.000 | 0.000 | 0.000 | 0.000 |
| share of member-periods panel-ineligible | 0.688 | 0.661 | 0.331 | 0.546 |
| bad plants met at the audit seat per one met at the initial seat | 0.126 | 0.131 | 0.088 | 0.113 |
| members siding with the planted lie, appeal / dispute (pooled F̂^La / F̂^Ld) | 0.092 / 0.098 | 0.088 / 0.032 | 0.040 / 0.055 | 0.039 / 0.068 |

Paired C5 retrained at 0.25 − run 42's policies frozen at 0.25 by seed (same seeds, the same policy class; for the learners the two chains' own policies):

| reading | direct | head alone | hand | careful |
|---|---|---|---|---|
| false approvals (run) | -4.6 ± 1.3 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| bad plants approved | -1.8 ± 1.5 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| good plants rejected | -0.3 ± 0.6 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| suspensions | +0.4 ± 0.7 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| audit overturn rate | -0.005 ± 0.002 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| audits held | -32 ± 17 | — | +0 ± 0 | +0 ± 0 |
| disputes filed | -3.2 ± 0.8 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| disputes won | -0.2 ± 0.7 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| appeals filed | +2.6 ± 2.7 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| appeals won | +3.1 ± 2.7 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| lying appeals (real) | +0.0 ± 0.0 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| lying appeals paid | +0.0 ± 0.0 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| lying disputes (real) | +0.0 ± 0.0 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| lying disputes paid | +0.0 ± 0.0 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| slots alive | +0.8 ± 0.4 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| nominal surplus | +691 ± 509 | — | +0 ± 0 | +0 ± 0 |
| real lifetime | +1414 ± 708 | — | +0 ± 0 | +0 ± 0 |
| tasks per 1,000 | +0.4 ± 0.5 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| P_t | -0.3 ± 0.5 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| members' price | +0.1 ± 0.3 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| requesters' wallet | +102 ± 80 | — | +0 ± 0 | +0 ± 0 |
| state share | +0.000 ± 0.001 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| awarded | -11 ± 20 | — | +0 ± 0 | +0 ± 0 |
| idle for bond | +11 ± 41 | — | +0 ± 0 | +0 ± 0 |
| cost of truth | +90 ± 47 | — | +0 ± 0 | +0 ± 0 |
| state seats per real root | -0.052 ± 0.016 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| state seats per plant | -0.028 ± 0.015 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| F̂ | -0.007 ± 0.013 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| leak: false approvals per vested task | -0.0022 ± 0.0006 | — | +0.0000 ± 0.0000 | +0.0000 ± 0.0000 |
| leak: false approvals per bad delivery | -0.008 ± 0.003 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| system overhead a vested task | -0.236 ± 0.153 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| customers' overhead a vested task | -0.343 ± 0.121 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| ticks to vest p50 | +0.0 ± 0.0 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| ticks to vest p90 | +0.0 ± 0.0 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| rulings sought | -17.5 ± 2.5 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| rulings wrong | -4.6 ± 1.1 | — | +0.0 ± 0.0 | +0.0 ± 0.0 |
| false penalties: initial seat | -3.30 ± 2.69 | — | +0.00 ± 0.00 | +0.00 ± 0.00 |
| false penalties: audit seat | +0.00 ± 0.10 | — | +0.00 ± 0.00 | +0.00 ± 0.00 |
| false penalties: panel seat | -2.05 ± 1.04 | — | +0.00 ± 0.00 | +0.00 ± 0.00 |
| care share | -0.032 ± 0.006 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| approve blind | +0.032 ± 0.006 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| reject blind | -0.000 ± 0.001 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| initial plant stamp rate (per seed) | -0.016 ± 0.004 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| initial real stamp rate (per seed) | -0.018 ± 0.004 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| audit plant stamp rate (per seed) | +0.112 ± 0.024 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| audit real stamp rate (per seed) | +0.154 ± 0.019 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| panel plant stamp rate (per seed) | -0.300 ± 0.021 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |
| panel real stamp rate (per seed) | -0.061 ± 0.024 | — | +0.000 ± 0.000 | +0.000 ± 0.000 |

Within C5 retrained at 0.25, paired against the hand on the same seeds:

| reading | direct − hand | head alone − hand | careful − hand |
|---|---|---|---|
| false approvals (run) | +4.2 ± 1.0 | +3.2 ± 1.1 | -4.7 ± 0.7 |
| bad plants approved | -53.1 ± 1.8 | -55.7 ± 1.3 | -56.3 ± 1.6 |
| good plants rejected | -3.8 ± 0.7 | -4.1 ± 0.7 | -3.8 ± 0.7 |
| suspensions | -10.2 ± 0.8 | -10.4 ± 0.9 | -10.4 ± 0.7 |
| audit overturn rate | -0.028 ± 0.001 | -0.032 ± 0.001 | -0.023 ± 0.001 |
| audits held | -10 ± 16 | -19 ± 18 | -31 ± 12 |
| disputes filed | -15.8 ± 1.2 | -15.8 ± 1.3 | -16.4 ± 1.2 |
| disputes won | -15.1 ± 1.2 | -14.9 ± 1.2 | -15.6 ± 1.1 |
| appeals filed | +26.8 ± 2.8 | +27.7 ± 2.9 | +27.4 ± 3.2 |
| appeals won | +24.5 ± 2.9 | +26.7 ± 3.0 | +26.6 ± 3.1 |
| lying appeals (real) | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| lying appeals paid | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| lying disputes (real) | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| lying disputes paid | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| slots alive | +2.8 ± 0.4 | +2.5 ± 0.5 | +2.6 ± 0.5 |
| nominal surplus | -4745 ± 467 | -3951 ± 353 | -5415 ± 385 |
| real lifetime | +2487 ± 701 | +3472 ± 1036 | +2057 ± 1068 |
| tasks per 1,000 | +5.0 ± 0.4 | +4.5 ± 0.5 | +4.4 ± 0.4 |
| P_t | -4.5 ± 0.4 | -4.5 ± 0.7 | -4.6 ± 0.7 |
| members' price | -1.3 ± 0.3 | -1.2 ± 0.4 | -1.7 ± 0.3 |
| requesters' wallet | +729 ± 66 | +627 ± 68 | +600 ± 65 |
| state share | -0.019 ± 0.004 | -0.020 ± 0.004 | -0.020 ± 0.004 |
| awarded | +219 ± 26 | +220 ± 28 | +207 ± 22 |
| idle for bond | +18 ± 33 | +5 ± 39 | -1 ± 54 |
| cost of truth | -2402 ± 92 | -2392 ± 61 | -2286 ± 77 |
| state seats per real root | +0.033 ± 0.013 | +0.018 ± 0.017 | -0.019 ± 0.010 |
| state seats per plant | +0.101 ± 0.017 | +0.095 ± 0.015 | +0.046 ± 0.010 |
| F̂ | +0.002 ± 0.010 | -0.012 ± 0.007 | -0.004 ± 0.012 |
| leak: false approvals per vested task | +0.0017 ± 0.0005 | +0.0013 ± 0.0005 | -0.0025 ± 0.0004 |
| leak: false approvals per bad delivery | +0.007 ± 0.002 | +0.005 ± 0.002 | -0.010 ± 0.001 |
| system overhead a vested task | -6.928 ± 0.186 | -6.848 ± 0.146 | -5.928 ± 0.139 |
| customers' overhead a vested task | -3.114 ± 0.115 | -2.994 ± 0.130 | -2.155 ± 0.090 |
| ticks to vest p50 | +0.0 ± 0.0 | +0.0 ± 0.0 | +0.0 ± 0.0 |
| ticks to vest p90 | -1.0 ± 0.0 | -0.9 ± 0.1 | -0.5 ± 0.1 |
| rulings sought | -46.0 ± 2.8 | -38.0 ± 3.1 | -3.8 ± 2.5 |
| rulings wrong | -10.4 ± 1.2 | -7.7 ± 1.2 | +0.1 ± 1.5 |
| false penalties: initial seat | -2.15 ± 1.84 | -9.75 ± 1.23 | -0.15 ± 1.48 |
| false penalties: audit seat | -0.10 ± 0.10 | -0.15 ± 0.11 | -0.05 ± 0.14 |
| false penalties: panel seat | -9.35 ± 1.00 | -7.15 ± 0.95 | -0.05 ± 1.13 |
- C5 retrained at 0.25 direct: false approvals / hand's = 1.62; seeds above the hand: 16/20
- C5 retrained at 0.25 head alone: false approvals / hand's = 1.49; seeds above the hand: 16/20
- run 42's policies frozen at 0.25 direct: false approvals / hand's = 2.32; seeds above the hand: 19/20

Mix by period (C5 retrained at 0.25 finals, pooled over seeds):
- **C5 retrained at 0.25 direct**: p0 0.943/0.056/0.002 (596); p1 0.774/0.217/0.009 (719); p2 0.729/0.263/0.008 (805); p3 0.727/0.269/0.004 (881); p4 0.816/0.182/0.003 (925); p5 0.837/0.151/0.012 (353); p6 0.766/0.232/0.003 (35); p7 0.667/0.242/0.091 (1)
- **C5 retrained at 0.25 head alone**: p0 0.941/0.059/0.000 (604); p1 0.837/0.163/0.000 (732); p2 0.771/0.229/0.000 (835); p3 0.759/0.241/0.000 (916); p4 0.806/0.194/0.000 (925); p5 0.855/0.145/0.000 (296); p6 0.951/0.049/0.000 (30); p7 0.932/0.068/0.000 (10)

Stages after the first verdict (C5 retrained at 0.25 finals), real / plant, pooled; then plant − real period-matched (real rates reweighted by the plants' count per period), paired by seed:
| policy | audited share | audit wait | filed share | filing delay | panel wait | state seats | Δ audited (matched) | Δ state seats (matched) | Δ filed (matched) |
|---|---|---|---|---|---|---|---|---|---|
| C5 retrained at 0.25 direct | 0.434 / 0.120 | 0.44 / 0.42 | 0.042 / 0.218 | 0.00 / 0.00 | 0.39 / 0.41 | 0.350 / 0.317 | -0.318 ± 0.007 | -0.028 ± 0.012 | +0.176 ± 0.007 |
| C5 retrained at 0.25 head alone | 0.446 / 0.124 | 0.39 / 0.43 | 0.043 / 0.214 | 0.00 / 0.00 | 0.40 / 0.41 | 0.335 / 0.310 | -0.328 ± 0.009 | -0.018 ± 0.008 | +0.171 ± 0.007 |
| C5 retrained at 0.25 hand | 0.527 / 0.194 | 0.10 / 0.14 | 0.041 / 0.139 | 0.00 / 0.00 | 0.10 / 0.11 | 0.317 / 0.216 | -0.427 ± 0.006 | +0.025 ± 0.003 | +0.098 ± 0.003 |
| C5 retrained at 0.25 careful | 0.477 / 0.127 | 0.30 / 0.29 | 0.043 / 0.199 | 0.00 / 0.00 | 0.29 / 0.31 | 0.298 / 0.262 | -0.350 ± 0.007 | -0.035 ± 0.007 | +0.156 ± 0.004 |
