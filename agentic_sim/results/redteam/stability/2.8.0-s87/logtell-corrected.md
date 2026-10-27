# The `log` tell-reader on the corrected view (October 27, 2026; the conformance item ruled after run 37, landed at 669c2769)

Run 24's entry cell with disputes on (`--entry-pool 20 --stampers 0.6 --dispute-policy truthful --seed 21`, 2.8.0), one reader in eight careful actors
(`--tell-readers 0.125`), the `log` tell against the same readers with no tell (`--tell none`: every case read as real), in both initial-seat modes
(`--tell-initial stamp`, the Q2 shape; `--tell-initial care`, §59's caring variant — the complete later-seat tell before the correction, 6.10 ± 1.16 plant
reviews read as a plant a run, `2.8.0-s87/hand.md`). The same seed and the same random stream: if the reader reads nothing, the two runs are one run.

| run | History head | entries | events | tell_plant_read_plant | tell_plant_read_real | tell_real_read_plant | tell_real_read_real | tell_initial_cared | tell_later_plant_stamped | tell_later_real_stamped | tell_false_approvals | false_approvals | bad_plants_approved | suspensions |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| log-stamp | `d3a24f0922e0f741…` | 129426 | 87741 | 0 | 5 | 0 | 35 | 0 | 0 | 3 | 2 | 6 | 71 | 16 |
| none-stamp | `d3a24f0922e0f741…` | 129426 | 87741 | 0 | 5 | 0 | 35 | 0 | 0 | 3 | 2 | 6 | 71 | 16 |
| log-care | `dab474e890ad9f8f…` | 128452 | 87641 | 0 | 16 | 0 | 74 | 59 | 3 | 28 | 2 | 6 | 69 | 15 |
| none-care | `dab474e890ad9f8f…` | 128452 | 87641 | 0 | 16 | 0 | 74 | 59 | 3 | 28 | 2 | 6 | 69 | 15 |

**Read.** The History heads are identical pairwise (yes): with the plant entries absent from the view until the reveal, the `log` reader
reads no plant at any seat (`tell_plant_read_plant` 0 in both modes, from 6.10 a run for the caring variant in §59) and decides as a reader with no tell
does, to the hash. The runs live in the scratchpad; this table is their record. The regression is `test_v28`'s eleventh test.
