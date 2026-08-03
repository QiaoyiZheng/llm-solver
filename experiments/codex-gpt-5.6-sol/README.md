# Codex GPT-5.6 Sol certificate experiment

Fixed model configuration:

- model: `gpt-5.6-sol`
- reasoning effort: `high`
- service tier: `priority` (Fast, 1.5x speed)
- repetitions: 5 independent valid runs per benchmark
- session: ephemeral, isolated temporary working directory
- sandbox: read-only
- web search: disabled

The only default task is certificate solving; the former status-only baseline
has been removed. Each response must contain a verdict plus a SAT model or
UNSAT clause core. The scorer first compares the verdict with the private label.
It invokes cvc5 only when that verdict is correct.

The runner audits Codex JSONL events. Any shell, MCP, browser, web, function,
or other tool call marks that attempt as contaminated and it is not counted as
one of the five direct-reasoning runs.

For each attempt, `raw/*.events.jsonl` stores the complete Codex CLI event
stream and `raw/*.reasoning.txt` stores any reasoning summary explicitly exposed
by the CLI. Hidden chain-of-thought is not available and is not reconstructed.

Validate without calling Codex:

```powershell
python experiments/codex-gpt-5.6-sol/scripts/run_codex.py --dry-run
```

Run one benchmark as a pilot:

```powershell
python experiments/codex-gpt-5.6-sol/scripts/run_codex.py --limit 1
```

Run the full experiment:

```powershell
python experiments/codex-gpt-5.6-sol/scripts/run_codex.py
```

Every invocation creates one self-contained directory under `runs/` named:

```text
YYYYMMDDTHHMMSSZ__实验内容__模型_推理强度_服务档位_重复次数
```

For example:

```text
20260803T143000Z__cnf-certificate-v1__gpt-5.6-sol_high_priority_5x
```

That directory contains the configuration, certificate prompt and output-schema
snapshots plus separate `logs/`, `raw/`, `verifier/`, and `results/`
subdirectories. Set `--experiment-id` to a short description of the
experimental content; model configuration is appended automatically.
