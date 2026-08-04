# Experiment statistics

This directory stores immutable, derived statistics for each experiment batch.
Batch directories are named sequentially: `v1`, `v2`, `v3`, and so on.

Each batch contains:

- `manifest.json`: scoring policy and exact source run directories;
- `summary.json`: machine-readable aggregate statistics;
- `models.csv`: one row per model;
- `logics.csv`: metrics grouped by model and SMT logic;
- `cases.csv`: per-case five-run counts;
- `distributions.csv`: 0/5 through 5/5 classification distributions.
- `success_buckets.csv`: every benchmark assigned to its final-success bucket;
- `success_buckets.json`: the same 5/5 through 0/5 lists in nested JSON form.

The two reported metrics are:

1. SAT/UNSAT accuracy = correct verdicts / completed slots.
2. SAT witness rate = cvc5-valid SAT witnesses / correct SAT verdicts.

Correct UNSAT verdicts contribute only to SAT/UNSAT accuracy. They are excluded
from both the numerator and denominator of SAT witness rate.

The additional final-success distribution counts each of the five independent
runs as successful when it is either a correct UNSAT verdict or a correct SAT
verdict with a cvc5-valid witness. Every fully completed benchmark is listed in
exactly one of the 5/5, 4/5, 3/5, 2/5, 1/5, or 0/5 buckets. Incomplete benchmarks
are listed separately and never treated as failed runs.

SAT/UNSAT accuracy is micro-averaged over all individual repetitions. All five
runs participate; no majority vote is used.

Generate a new batch from the latest formal run of every model:

```powershell
python experiments/statistics/build_statistics.py --batch v2
```

Existing batch directories are not overwritten unless `--overwrite` is passed.
