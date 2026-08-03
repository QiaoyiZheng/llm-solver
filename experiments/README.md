# LLM CNF experiments

The certificate task is the only default experiment. Status-only classification
has been retired. Every response is classified first; an incorrect verdict is
immediately scored wrong, while a correct verdict proceeds to certificate
verification.

Each model has an isolated experiment directory:

- `codex-gpt-5.6-sol/`
- `deepseek-v4-flash/`
- `deepseek-v4-pro/`

Shared label-free certificate inputs live in
`../benchmarks/certificate-inputs/cases/`.
They contain only the logic, structured symbol declarations, and CNF(T)
expression. Opaque case filenames and model-visible content are kept separate
from post-response scoring data.

Every invocation is stored under the model's `runs/` directory using
`YYYYMMDDTHHMMSSZ__实验内容__配置`. Each run is self-contained and separates
configuration snapshots, raw responses, logs, and scored results. Runtime
artifacts are ignored by Git. Benchmark inputs remain under
`benchmarks/CNF-Bench/` and must not be modified.

Run one paid end-to-end certificate smoke attempt per configured model with:

```powershell
python experiments/smoke_test.py
```

Use repeated `--model` options to test only selected models. Smoke runs use one
attempt rather than the five repetitions required for a full experiment.
