# LLM CNF(T) Certificate Evaluation

This project measures whether language models can directly solve predicate-logic
CNF(T) formulas and produce machine-checkable evidence. The certificate task is
the only default experiment; there is no separate status-only baseline.

Chinese documentation: [README_ZH.md](README_ZH.md)

## Evaluated models

- Codex: `gpt-5.6-sol`, reasoning effort `high`, priority service tier, detailed
  reasoning summaries when the CLI exposes them.
- DeepSeek V4 Flash: `deepseek-v4-flash`, thinking enabled,
  `reasoning_effort=max`.
- DeepSeek V4 Pro: `deepseek-v4-pro`, thinking enabled,
  `reasoning_effort=max`.

Every model runs each benchmark five independent times. Infrastructure failures
are retried and do not consume a valid slot. A syntactically invalid model
response is a valid attempt but an incorrect result.

## Repository layout

```text
llm-solver/
|-- AGENTS.md
|-- README.md
|-- README_ZH.md
|-- api-key                         # local secret; ignored by Git
|-- benchmarks/
|   |-- smtlib-2025/                # original SMT-LIB cases and private manifest
|   |-- CNF-Bench/                  # mathematical CNF(T), grouped by logic
|   |-- certificate-inputs/         # label-free model-visible JSON cases
|   `-- smoke/                      # small solver/infrastructure fixtures
|-- experiments/
|   |-- certificate-verifier/       # schemas, verifier, and verifier tests
|   |-- codex-gpt-5.6-sol/          # Codex prompt, runner, and runs
|   |-- deepseek-v4-flash/          # Flash API config, runner, and runs
|   |-- deepseek-v4-pro/            # Pro API config, runner, and runs
|   |-- check_deepseek_config.py    # secret-safe API configuration check
|   |-- smoke_test.py               # one-call end-to-end diagnostic runner
|   `-- CERTIFICATE_EXPERIMENT_PROPOSAL.md
`-- tools/
    `-- cvc5/                       # pinned local certificate checker
```

### Root files

- `AGENTS.md` defines durable experiment rules: label isolation, direct
  reasoning restrictions, five repetitions, certificate scoring, and reporting.
- `README.md` is the English project and validation reference.
- `README_ZH.md` is the Chinese project and validation reference.
- `.gitignore` excludes secrets, Python caches, and runtime experiment outputs.
- `api-key` contains the local DeepSeek secret. It must never be committed,
  copied into run snapshots, or printed in logs.

### `benchmarks/`

- `smtlib-2025/` contains the original `.smt2` formulas. Its `manifest.json`
  contains private expected statuses and source metadata; models never see it.
- `CNF-Bench/` contains one `.md` mathematical CNF(T) expression per benchmark,
  grouped by SMT-LIB logic. These files are the conversion output and must not
  be modified during evaluation.
- `certificate-inputs/cases/` contains the 95 opaque, label-free JSON inputs sent
  to models. `schema/certificate-input.schema.json` defines their format.
- `certificate-inputs/scripts/build_inputs.py` regenerates and audits all public
  certificate cases from the private source/CNF pair.
- `certificate-inputs/README.md` documents the public input boundary.
- `smoke/` contains tiny known SAT/UNSAT SMT-LIB fixtures for local
  infrastructure checks; it is not the 95-case model evaluation corpus.

### `experiments/`

- `certificate-verifier/schema/certificate-response.schema.json` is the shared
  model response schema.
- `certificate-verifier/scripts/verify_certificate.py` performs strict parsing,
  reconstructs SAT/UNSAT checks, and invokes cvc5.
- `certificate-verifier/tests/test_verifier.py` contains synthetic and real-case
  verifier regression tests.
- `codex-gpt-5.6-sol/config/prompt.txt` is the shared certificate prompt currently
  used by all three models.
- `codex-gpt-5.6-sol/scripts/run_codex.py` runs Codex, audits tool contamination,
  stores CLI events/reasoning summaries, scores verdicts, and verifies certificates.
- `deepseek-v4-flash/config/api.json` and `deepseek-v4-pro/config/api.json` contain
  non-secret endpoint/model settings and the relative secret-file reference.
- Each DeepSeek `scripts/run_certificate.py` runs five-repetition certificate
  evaluation with concurrent API calls, retries, label gating, cvc5 checking,
  and resume support. The Pro wrapper reuses the shared Flash implementation
  with the Pro model/configuration.
- `check_deepseek_config.py` verifies that a key can be loaded and optionally
  checks the read-only `/models` endpoint without printing the key.
- `smoke_test.py` performs one real end-to-end request per selected model. Its
  output is diagnostic and must not be mixed with full experiment statistics.
- `CERTIFICATE_EXPERIMENT_PROPOSAL.md` records certificate formats, scoring
  semantics, and the proposed stronger-proof extension.
- `<model>/runs/` contains Git-ignored timestamped runtime artifacts. See
  "Artifacts and run directories" below for its internal layout.

### `tools/cvc5/`

- `README.md` records the pinned cvc5 version, release source, and SHA-256.
- `1.3.3/.../bin/cvc5.exe` is the executable used by the verifier.
- `COPYING`, `AUTHORS`, and `licenses/` contain upstream notices.
- Local SDK headers, static libraries, JNI binaries, and Java files are not
  required by this Python experiment and are excluded from Git.

## Inputs and label isolation

The source SMT-LIB benchmarks and private labels are under
`benchmarks/smtlib-2025/`. Mathematical CNF(T) expressions are under
`benchmarks/CNF-Bench/`.

Models receive only JSON files from `benchmarks/certificate-inputs/cases/`:

```json
{
  "schema_version": 1,
  "logic": "LIA",
  "declarations": [],
  "cnf": "(...)"
}
```

The model-visible JSON contains no expected status, manifest data, source path,
original filename, checksum, or historical result. The opaque case filename is
also not included in the prompt. Private benchmark association and the expected
status are recovered only after the model response is final.

## Model output protocol

The response must be one JSON object with no surrounding prose.

SAT responses contain a complete interpretation of every original declaration:

```json
{
  "schema_version": 1,
  "status": "sat",
  "certificate": {
    "kind": "sat_model",
    "constants": [
      {"symbol": "x", "sort": "Int", "value_smt2": "2"}
    ],
    "functions": []
  }
}
```

UNSAT responses identify a non-empty contradictory subset of the outer CNF
clauses using one-based indices:

```json
{
  "schema_version": 1,
  "status": "unsat",
  "certificate": {
    "kind": "unsat_core",
    "clause_indices": [1, 4, 7]
  }
}
```

When no reliable certificate can be produced, the model may return:

```json
{"schema_version":1,"status":"unknown","certificate":{"kind":"none"}}
```

For benchmarks labeled SAT or UNSAT, `unknown` is incorrect.

## Complete validation flow

The scoring pipeline uses the following order:

1. Load one label-free certificate case.
2. Insert the JSON content—not its filename or path—into the shared prompt.
3. Start a fresh model session with no tools, solver, network search, or previous
   answer context available to the model.
4. Save the raw response and any model-provided reasoning data before scoring.
5. Parse only the top-level `status` as `sat`, `unsat`, or `unknown`.
6. Recover the private original benchmark association from the CNF content.
7. Read the expected status from the private manifest.
8. Compare the predicted and expected statuses.
9. If the verdict is wrong or unreadable, mark the attempt wrong and skip cvc5.
10. If the verdict is correct and is SAT or UNSAT, run the corresponding
    certificate verifier.
11. Record verdict correctness and certificate validity independently.

In compact form:

```text
label-free case -> model response -> compare verdict
                                      | wrong: stop, fully_solved=false
                                      ` correct: verify certificate with cvc5
                                                   | invalid: fully_solved=false
                                                   ` valid: fully_solved=true
```

### SAT certificate verification

The verifier:

1. requires every original zero-arity symbol exactly once in `constants`;
2. requires every original positive-arity symbol exactly once in `functions`;
3. checks exact declared sorts and function signatures;
4. parses each submitted value/body as exactly one SMT-LIB term;
5. rejects commands, missing symbols, extra symbols, duplicate symbols, unsafe
   binders, and references to original declared symbols inside witness terms;
6. adds equality bindings for constants and universally quantified bindings for
   submitted function interpretations;
7. combines those bindings with the original SMT-LIB formula;
8. accepts only when pinned cvc5 returns exactly `sat` with exit code zero.

An empty `constants` array is valid only when the input has no zero-arity
declarations. It is not accepted as a partial witness.

### UNSAT certificate verification

The verifier:

1. parses the outer CNF while respecting theory-atom boundaries;
2. validates unique positive one-based clause indices;
3. reconstructs only the selected clauses;
4. declares referenced Tseitin Boolean auxiliaries;
5. recursively expands `lambda` definitional auxiliaries;
6. rejects malformed, conflicting, cyclic, or oversized reconstructions;
7. accepts only when pinned cvc5 returns exactly `unsat` with exit code zero.

The current UNSAT certificate is an unsatisfiable core, not a standalone formal
proof. Alethe/LRAT proof checking can be added later as a stronger track.

## Result fields

Each valid model attempt records at least:

```json
{
  "prediction": "sat",
  "expected": "sat",
  "verdict_correct": true,
  "certificate_present": true,
  "certificate_checked": true,
  "certificate_valid": true,
  "certificate_skip_reason": null,
  "fully_solved": true
}
```

`fully_solved` is true only when both the verdict and certificate are valid.
Reports must separately aggregate verdict correctness and fully solved counts as
5/5, 4/5, 3/5, 2/5, 1/5, and 0/5 per benchmark and model.

## Artifacts and run directories

Every experiment is isolated under:

```text
experiments/<model>/runs/<UTC timestamp>__<experiment>__<configuration>/
```

Important artifacts are:

- `configuration.json`: immutable run configuration snapshot;
- `prompt.txt`: prompt snapshot;
- `raw/`: final responses and reasoning data;
- `logs/`: token usage, latency, finish reason, and errors;
- `verifier/`: generated SMT-LIB certificate-checking files;
- `results/runs.jsonl`: one scored record per model attempt;
- `results/infrastructure-errors.jsonl`: retryable API/process errors;
- `results/summary.json`: final completion summary;
- `full-run.stdout.log` and `full-run.stderr.log`: live runner logs;
- `launcher.json`: background process and run-directory metadata.

DeepSeek stores API-provided `reasoning_content`. Codex stores the complete CLI
JSONL event stream and any reasoning summary explicitly exposed by the CLI.
Hidden chain-of-thought is not available and is never reconstructed.

## Running experiments

Run the certificate verifier directly:

```powershell
python experiments/certificate-verifier/scripts/verify_certificate.py `
  --case benchmarks/certificate-inputs/cases/LIA/case-....json `
  --response response.json
```

Run or resume DeepSeek Flash:

```powershell
python experiments/deepseek-v4-flash/scripts/run_certificate.py `
  --run-directory RUN_NAME --workers 4 --max-tokens 32768

python experiments/deepseek-v4-flash/scripts/run_certificate.py `
  --run-directory RUN_NAME --workers 4 --max-tokens 32768 --resume
```

DeepSeek Pro uses the same arguments:

```powershell
python experiments/deepseek-v4-pro/scripts/run_certificate.py `
  --run-directory RUN_NAME --workers 4 --max-tokens 32768
```

Run or resume Codex:

```powershell
python experiments/codex-gpt-5.6-sol/scripts/run_codex.py `
  --run-directory RUN_NAME --experiment-id cnf-certificate-full-v1

python experiments/codex-gpt-5.6-sol/scripts/run_codex.py `
  --run-directory RUN_NAME --experiment-id cnf-certificate-full-v1 --resume
```

Use `--dry-run` before paid full runs. Runtime outputs and the repository-root
`api-key` file are ignored by Git.

## Trusted verifier

The pinned verifier binary is cvc5 1.3.3 under `tools/cvc5/`. cvc5 is used only
after the model has completed its answer; models are forbidden from calling it.
The verifier invokes cvc5 with an argument array in an isolated temporary
directory and treats model output strictly as data, never executable code.
