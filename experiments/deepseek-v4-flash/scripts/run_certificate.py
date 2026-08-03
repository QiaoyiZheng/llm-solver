#!/usr/bin/env python3
"""Run the five-repetition DeepSeek V4 Flash certificate experiment."""

from __future__ import annotations

import argparse
import concurrent.futures
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SCRIPT_DIR = Path(__file__).resolve().parent
MODEL_DIR = SCRIPT_DIR.parent
ROOT = MODEL_DIR.parents[1]
CASE_ROOT = ROOT / "benchmarks" / "certificate-inputs" / "cases"
PROMPT_PATH = ROOT / "experiments" / "codex-gpt-5.6-sol" / "config" / "prompt.txt"
SCHEMA_PATH = ROOT / "experiments" / "certificate-verifier" / "schema" / "certificate-response.schema.json"
VERIFIER = ROOT / "experiments" / "certificate-verifier" / "scripts" / "verify_certificate.py"
API_CONFIG = MODEL_DIR / "config" / "api.json"
SMOKE_MODULE = ROOT / "experiments" / "smoke_test.py"
CODEX_RUNNER = ROOT / "experiments" / "codex-gpt-5.6-sol" / "scripts" / "run_codex.py"
MODEL = "deepseek-v4-flash"
REASONING_EFFORT = "max"
THINKING = "enabled"
REPETITIONS = 5
WRITE_LOCK = threading.Lock()


def load_module(name: str, path: Path):
    spec = importlib.util.spec_from_file_location(name, path)
    if spec is None or spec.loader is None:
        raise RuntimeError(f"cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def append_jsonl(path: Path, value: dict[str, Any]) -> None:
    line = json.dumps(value, ensure_ascii=False, separators=(",", ":")) + "\n"
    with WRITE_LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(line)
            handle.flush()
            os.fsync(handle.fileno())


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def verify(case_path: Path, response_text: str, artifact: Path, timeout: int) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="ds-cert-") as directory:
        response_path = Path(directory) / "response.json"
        response_path.write_text(response_text, encoding="utf-8", newline="\n")
        proc = subprocess.run(
            [sys.executable, str(VERIFIER), "--case", str(case_path), "--response", str(response_path), "--artifact", str(artifact), "--timeout", str(timeout)],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout + 30, check=False,
        )
    try:
        result = json.loads(proc.stdout.strip())
    except json.JSONDecodeError:
        result = {"certificate_valid": False, "verification_result": "invalid_verifier_output", "verification_error": proc.stderr.strip() or proc.stdout.strip()}
    result["verifier_returncode"] = proc.returncode
    return result


def parse_prediction(text: str) -> tuple[str | None, dict[str, Any] | None]:
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return None, None
    status = value.get("status") if isinstance(value, dict) else None
    return (status if status in {"sat", "unsat", "unknown"} else None), value if isinstance(value, dict) else None


def artifact_stem(case_path: Path, run: int) -> Path:
    relative = case_path.relative_to(CASE_ROOT)
    return Path(relative.parts[0]) / relative.stem / f"run-{run:02d}"


def run_slot(case_path: Path, run: int, args: argparse.Namespace, run_dir: Path, prompt_template: str, api, labels) -> dict[str, Any]:
    relative = case_path.relative_to(CASE_ROOT).as_posix()
    case_text = case_path.read_text(encoding="utf-8").strip()
    case_value = json.loads(case_text)
    task_prompt = prompt_template.replace("{{CASE_JSON}}", case_text)
    stem = artifact_stem(case_path, run)
    errors_path = run_dir / "results" / "infrastructure-errors.jsonl"
    for attempt in range(1, args.retries + 1):
        started = time.monotonic()
        try:
            response = api.call_deepseek(API_CONFIG, task_prompt, args.timeout, args.max_tokens)
            final_text = str(response.get("final_text", ""))
            write_text((run_dir / "raw" / stem).with_suffix(".response.json"), final_text)
            write_text((run_dir / "raw" / stem).with_suffix(".reasoning.txt"), str(response.get("reasoning_content", "")))
            metadata = {key: value for key, value in response.items() if key not in {"final_text", "reasoning_content"}}
            write_text((run_dir / "logs" / stem).with_suffix(".metadata.json"), json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")

            # Identity and label recovery happen strictly after the response is final.
            benchmark = labels.private_benchmark(case_value)
            expected = labels.expected_status(benchmark)
            prediction, parsed = parse_prediction(final_text)
            verdict_correct = prediction == expected
            if verdict_correct and prediction in {"sat", "unsat"}:
                verification = verify(case_path, final_text, (run_dir / "verifier" / stem).with_suffix(".smt2"), args.certificate_timeout)
                certificate_checked = True
                certificate_valid = verification.get("certificate_valid") is True
                skip_reason = None
            else:
                verification = {}
                certificate_checked = False
                certificate_valid = False
                skip_reason = "unreadable_verdict" if prediction is None else "incorrect_verdict" if not verdict_correct else "no_certificate_for_unknown"
            record = {
                "schema_version": 1,
                "experiment_id": args.experiment_id,
                "timestamp": utc_now(),
                "provider": "deepseek",
                "model": MODEL,
                "actual_model": response.get("actual_model"),
                "reasoning_effort": REASONING_EFFORT,
                "thinking": THINKING,
                "case": relative,
                "benchmark": benchmark,
                "logic": case_value["logic"],
                "run": run,
                "attempt": attempt,
                "prediction": prediction,
                "expected": expected,
                "verdict_correct": verdict_correct,
                "certificate_present": isinstance(parsed, dict) and isinstance(parsed.get("certificate"), dict),
                "certificate_checked": certificate_checked,
                "certificate_valid": certificate_valid,
                "certificate_skip_reason": skip_reason,
                "fully_solved": verdict_correct and certificate_valid,
                "verification": verification,
                "latency_seconds": response.get("latency_seconds"),
                "finish_reason": response.get("finish_reason"),
                "usage": response.get("usage", {}),
                "state": "complete",
            }
            append_jsonl(run_dir / "results" / "runs.jsonl", record)
            print(f"[{relative}] run={run}/5 verdict={prediction} correct={verdict_correct} certificate={certificate_valid}", flush=True)
            return record
        except Exception as error:
            append_jsonl(errors_path, {"timestamp": utc_now(), "model": MODEL, "case": relative, "run": run, "attempt": attempt, "error": str(error), "elapsed_seconds": round(time.monotonic() - started, 6)})
            if attempt == args.retries:
                print(f"[{relative}] run={run}/5 FAILED after {attempt} attempts: {error}", file=sys.stderr, flush=True)
                return {"state": "incomplete", "case": relative, "run": run, "error": str(error)}
            time.sleep(min(2 ** (attempt - 1), 30))
    raise AssertionError("unreachable")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--run-directory", required=True)
    parser.add_argument("--experiment-id", default="cnf-certificate-full-v1")
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--timeout", type=int, default=600)
    parser.add_argument("--certificate-timeout", type=int, default=300)
    parser.add_argument("--max-tokens", type=int, default=32768)
    parser.add_argument("--retries", type=int, default=3)
    parser.add_argument("--limit", type=int)
    parser.add_argument("--dry-run", action="store_true")
    parser.add_argument("--resume", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    if args.workers < 1 or args.retries < 1 or args.max_tokens < 1 or (args.limit is not None and args.limit < 1):
        raise ValueError("workers, retries, max-tokens, and limit must be positive")
    run_dir = (MODEL_DIR / "runs" / args.run_directory).resolve()
    runs_root = (MODEL_DIR / "runs").resolve()
    try:
        run_dir.relative_to(runs_root)
    except ValueError as error:
        raise ValueError("run directory must remain under the model runs directory") from error
    tasks = sorted(CASE_ROOT.rglob("*.json"))
    if args.limit:
        tasks = tasks[:args.limit]
    print(f"model={MODEL} benchmarks={len(tasks)} repetitions={REPETITIONS} calls={len(tasks)*REPETITIONS} workers={args.workers}")
    print(f"run_directory={run_dir}")
    if args.dry_run:
        return 0
    run_dir.mkdir(parents=True, exist_ok=True)
    initialized = (run_dir / "configuration.json").exists()
    if initialized and not args.resume:
        raise ValueError(f"run directory is already initialized: {run_dir}; use --resume")
    if args.resume and not initialized:
        raise ValueError(f"cannot resume uninitialized run directory: {run_dir}")
    prompt_template = PROMPT_PATH.read_text(encoding="utf-8")
    if not initialized:
        write_text(run_dir / "prompt.txt", prompt_template)
        write_text(run_dir / "certificate-response.schema.json", SCHEMA_PATH.read_text(encoding="utf-8"))
        write_text(run_dir / "configuration.json", json.dumps({
            "schema_version": 1, "created_at": utc_now(), "experiment_id": args.experiment_id,
            "provider": "deepseek", "model": MODEL, "reasoning_effort": REASONING_EFFORT,
            "thinking": THINKING, "repetitions": REPETITIONS, "workers": args.workers,
            "timeout_seconds": args.timeout, "certificate_timeout_seconds": args.certificate_timeout,
            "max_output_tokens": args.max_tokens,
            "scoring_order": "verdict_then_certificate", "benchmarks": len(tasks),
        }, ensure_ascii=False, indent=2) + "\n")
    api = load_module("smoke_api", SMOKE_MODULE)
    labels = load_module("private_labels", CODEX_RUNNER)
    completed: set[tuple[str, int]] = set()
    results_path = run_dir / "results" / "runs.jsonl"
    if args.resume and results_path.exists():
        for line in results_path.read_text(encoding="utf-8").splitlines():
            record = json.loads(line)
            if record.get("state") == "complete":
                completed.add((str(record["case"]), int(record["run"])))
    slots = [(case_path, run) for case_path in tasks for run in range(1, REPETITIONS + 1) if (case_path.relative_to(CASE_ROOT).as_posix(), run) not in completed]
    print(f"completed_before_start={len(completed)} remaining_slots={len(slots)}", flush=True)
    results = []
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = [executor.submit(run_slot, case_path, run, args, run_dir, prompt_template, api, labels) for case_path, run in slots]
        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())
    complete = sum(item.get("state") == "complete" for item in results)
    incomplete = len(results) - complete
    summary = {"schema_version": 1, "completed_slots": len(completed) + complete, "incomplete_slots": incomplete, "planned_slots": len(tasks) * REPETITIONS, "finished_at": utc_now()}
    write_text(run_dir / "results" / "summary.json", json.dumps(summary, ensure_ascii=False, indent=2) + "\n")
    print(json.dumps(summary, separators=(",", ":")))
    return 0 if incomplete == 0 else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (OSError, ValueError, RuntimeError, json.JSONDecodeError) as error:
        print(f"error: {error}", file=sys.stderr)
        raise SystemExit(2)
