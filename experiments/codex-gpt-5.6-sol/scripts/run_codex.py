#!/usr/bin/env python3
"""Run the certificate-first direct-reasoning Codex CNF(T) experiment."""

from __future__ import annotations

import argparse
import concurrent.futures
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import threading
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


MODEL = "gpt-5.6-sol"
REASONING_EFFORT = "high"
REASONING_SUMMARY = "detailed"
SERVICE_TIER = "priority"  # Codex catalog: Fast, 1.5x speed.
MODEL_CONTEXT_WINDOW = 1_000_000
MODEL_AUTO_COMPACT_TOKEN_LIMIT = 950_000
REPETITIONS = 5
DEFAULT_EXPERIMENT_ID = "cnf-sat-certificate-unsat-golden-v2"
VALID_STATUSES = {"sat", "unsat", "unknown"}
TOOL_EVENT_TYPES = {
    "command_execution",
    "shell_command",
    "mcp_tool_call",
    "web_search",
    "browser",
    "computer_use",
    "function_call",
    "tool_call",
    "apply_patch",
}
TOOL_TYPE_MARKERS = ("tool", "command", "shell", "mcp", "web_search", "browser", "computer", "function_call", "apply_patch")

SCRIPT_DIR = Path(__file__).resolve().parent
MODEL_DIR = SCRIPT_DIR.parent
REPO_ROOT = MODEL_DIR.parents[1]
CNF_ROOT = REPO_ROOT / "benchmarks" / "certificate-inputs" / "cases"
MATHEMATICAL_CNF_ROOT = REPO_ROOT / "benchmarks" / "CNF-Bench"
MANIFEST_PATH = REPO_ROOT / "benchmarks" / "smtlib-2025" / "manifest.json"
VERIFIER_PATH = REPO_ROOT / "experiments" / "certificate-verifier" / "scripts" / "verify_certificate.py"
PROMPT_PATH = MODEL_DIR / "config" / "prompt.txt"
SCHEMA_PATH = REPO_ROOT / "experiments" / "certificate-verifier" / "schema" / "certificate-response.schema.json"
RUN_ROOT = MODEL_DIR / "runs"
WRITE_LOCK = threading.Lock()


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat()


def run_timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def make_run_directory(experiment_id: str, timestamp: str) -> Path:
    config = f"{MODEL}_{REASONING_EFFORT}_{SERVICE_TIER}_{REPETITIONS}x"
    return RUN_ROOT / f"{timestamp}__{experiment_id}__{config}"


def sha256_text(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Run five independent certificate-producing Codex attempts per CNF(T) "
            "benchmark. Verdicts are scored before certificates are checked."
        )
    )
    parser.add_argument("--experiment-id", default=DEFAULT_EXPERIMENT_ID)
    parser.add_argument("--run-directory", help="Explicit directory name under runs/")
    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--logic", action="append", help="Limit to one or more logic folders")
    parser.add_argument("--benchmark", action="append", help="Limit to a relative certificate-case JSON path")
    parser.add_argument("--limit", type=int, help="Limit the selected benchmark count")
    parser.add_argument("--timeout", type=int, default=1800, help="Seconds per Codex attempt")
    parser.add_argument("--certificate-timeout", type=int, default=300, help="Seconds per cvc5 certificate check")
    parser.add_argument("--retries", type=int, default=3, help="Infrastructure retries per slot")
    parser.add_argument("--workers", type=int, default=1, help="Concurrent independent Codex sessions")
    parser.add_argument(
        "--contamination-retries",
        type=int,
        default=3,
        help="Replacement attempts after a tool-contaminated response",
    )
    parser.add_argument("--dry-run", action="store_true", help="Validate and print plan only")
    return parser.parse_args()


def validate_experiment_id(value: str) -> str:
    if not re.fullmatch(r"[A-Za-z0-9][A-Za-z0-9._-]{0,99}", value):
        raise ValueError("experiment ID must match [A-Za-z0-9][A-Za-z0-9._-]{0,99}")
    return value


def discover_tasks(args: argparse.Namespace) -> list[Path]:
    if not CNF_ROOT.is_dir():
        raise FileNotFoundError(f"CNF root not found: {CNF_ROOT}")
    tasks = sorted(CNF_ROOT.rglob("*.json"))
    if args.logic:
        allowed = set(args.logic)
        tasks = [path for path in tasks if path.relative_to(CNF_ROOT).parts[0] in allowed]
    if args.benchmark:
        requested = {Path(item).as_posix() for item in args.benchmark}
        tasks = [path for path in tasks if path.relative_to(CNF_ROOT).as_posix() in requested]
        missing = requested - {path.relative_to(CNF_ROOT).as_posix() for path in tasks}
        if missing:
            raise ValueError(f"unknown benchmark(s): {', '.join(sorted(missing))}")
    if args.limit is not None:
        if args.limit < 1:
            raise ValueError("--limit must be positive")
        tasks = tasks[: args.limit]
    if not tasks:
        raise ValueError("no benchmarks selected")
    return tasks


def load_prompt_template() -> tuple[str, str]:
    template = PROMPT_PATH.read_text(encoding="utf-8")
    if template.count("{{CASE_JSON}}") != 1:
        raise ValueError("prompt must contain exactly one {{CASE_JSON}} placeholder")
    forbidden = ("manifest.json", "expected status", "checksum", "benchmark path")
    lowered = template.lower()
    if any(term in lowered for term in forbidden):
        raise ValueError("prompt template contains a label or identity leakage term")
    return template, sha256_text(template)


def strict_json_status(text: str) -> tuple[str, str | None, dict[str, Any] | None]:
    try:
        value = json.loads(text)
    except json.JSONDecodeError:
        return "invalid", None, None
    if not isinstance(value, dict):
        return "invalid", None, None
    status = value.get("status") if value.get("status") in VALID_STATUSES else None
    envelope_valid = (
        set(value) == {"schema_version", "status", "certificate"}
        and value.get("schema_version") == 1
        and status is not None
        and isinstance(value.get("certificate"), dict)
    )
    return ("valid" if envelope_valid else "invalid"), status, value


def iter_type_values(value: Any):
    if isinstance(value, dict):
        if isinstance(value.get("type"), str):
            yield value["type"]
        for child in value.values():
            yield from iter_type_values(child)
    elif isinstance(value, list):
        for child in value:
            yield from iter_type_values(child)


def audit_events(stdout: str) -> tuple[bool, list[str], dict[str, Any]]:
    seen_types: set[str] = set()
    usage: dict[str, Any] = {}
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        seen_types.update(iter_type_values(event))
        if isinstance(event, dict) and event.get("type") == "turn.completed":
            candidate = event.get("usage")
            if isinstance(candidate, dict):
                usage = candidate
    contaminated = sorted(
        value
        for value in seen_types
        if value in TOOL_EVENT_TYPES or any(marker in value.lower() for marker in TOOL_TYPE_MARKERS)
    )
    return bool(contaminated), contaminated, usage


def extract_reasoning_summaries(stdout: str) -> list[str]:
    """Extract only reasoning summaries exposed by Codex JSONL, never hidden CoT."""
    summaries: list[str] = []
    for line in stdout.splitlines():
        try:
            event = json.loads(line)
        except json.JSONDecodeError:
            continue
        item = event.get("item") if isinstance(event, dict) else None
        if not isinstance(item, dict) or item.get("type") != "reasoning":
            continue
        for key in ("text", "summary", "summary_text"):
            value = item.get(key)
            if isinstance(value, str) and value.strip():
                summaries.append(value.strip())
            elif isinstance(value, list):
                summaries.extend(str(part).strip() for part in value if isinstance(part, str) and part.strip())
    return summaries


def append_jsonl(path: Path, record: dict[str, Any]) -> None:
    with WRITE_LOCK:
        path.parent.mkdir(parents=True, exist_ok=True)
        with path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(json.dumps(record, ensure_ascii=False, separators=(",", ":")) + "\n")
            handle.flush()
            os.fsync(handle.fileno())


def write_text(path: Path, value: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(value, encoding="utf-8", newline="\n")


def load_completed_slots(path: Path) -> set[tuple[str, int]]:
    completed: set[tuple[str, int]] = set()
    if not path.exists():
        return completed
    for line_number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            record = json.loads(line)
        except json.JSONDecodeError as exc:
            raise ValueError(f"invalid results JSONL at line {line_number}: {exc}") from exc
        if record.get("state") == "complete" and record.get("model") == MODEL:
            completed.add((str(record["case"]), int(record["run"])))
    return completed


_EXPECTED_CACHE: dict[str, str] | None = None


def expected_status(relative_md: str) -> str:
    """Load labels only after a response exists; labels never enter model input."""
    global _EXPECTED_CACHE
    if _EXPECTED_CACHE is None:
        manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))
        mapping: dict[str, str] = {}
        for item in manifest["benchmarks"]:
            smt_path = Path(item["path"])
            md_path = smt_path.with_suffix(".md").as_posix()
            mapping[md_path] = item["status"]
        _EXPECTED_CACHE = mapping
    try:
        return _EXPECTED_CACHE[relative_md]
    except KeyError as exc:
        raise ValueError(f"no manifest label for {relative_md}") from exc


def private_benchmark(case: dict[str, Any]) -> str:
    """Recover the private benchmark association only after model output exists."""
    logic = case.get("logic")
    cnf = case.get("cnf")
    if not isinstance(logic, str) or not isinstance(cnf, str):
        raise ValueError("invalid certificate case")
    matches = [
        path for path in (MATHEMATICAL_CNF_ROOT / logic).glob("*.md")
        if path.read_text(encoding="utf-8").strip() == cnf.strip()
    ]
    if len(matches) != 1:
        raise ValueError(f"private benchmark association count is {len(matches)}, expected 1")
    return matches[0].relative_to(MATHEMATICAL_CNF_ROOT).as_posix()


def verify_certificate(case_path: Path, response_text: str, artifact_path: Path, timeout: int) -> dict[str, Any]:
    with tempfile.TemporaryDirectory(prefix="certificate-response-") as temp_name:
        response_path = Path(temp_name) / "response.json"
        response_path.write_text(response_text, encoding="utf-8", newline="\n")
        proc = subprocess.run(
            [
                sys.executable,
                str(VERIFIER_PATH),
                "--case", str(case_path),
                "--response", str(response_path),
                "--artifact", str(artifact_path),
                "--timeout", str(timeout),
            ],
            capture_output=True,
            text=True,
            encoding="utf-8",
            errors="replace",
            timeout=timeout + 30,
            check=False,
        )
    try:
        payload = json.loads(proc.stdout.strip())
    except json.JSONDecodeError:
        payload = {"certificate_valid": False, "verification_result": "invalid_verifier_output", "verification_error": proc.stderr.strip() or proc.stdout.strip()}
    payload["verifier_returncode"] = proc.returncode
    return payload


def codex_executable() -> str:
    executable = shutil.which("codex.cmd") or shutil.which("codex")
    if not executable:
        raise FileNotFoundError("Codex CLI not found; expected codex.cmd on PATH")
    return executable


def codex_version(executable: str) -> str:
    proc = subprocess.run(
        [executable, "--version"],
        capture_output=True,
        text=True,
        encoding="utf-8",
        errors="replace",
        timeout=30,
        check=False,
    )
    if proc.returncode != 0:
        raise RuntimeError(f"codex --version failed: {proc.stderr.strip()}")
    return proc.stdout.strip()


def build_command(executable: str, work_dir: Path, last_message: Path) -> list[str]:
    return [
        executable,
        "exec",
        "--strict-config",
        "--json",
        "--ephemeral",
        "--ignore-user-config",
        "--ignore-rules",
        "--skip-git-repo-check",
        "--sandbox",
        "read-only",
        "--cd",
        str(work_dir),
        "--model",
        MODEL,
        "--config",
        f'model_reasoning_effort="{REASONING_EFFORT}"',
        "--config",
        f'model_reasoning_summary="{REASONING_SUMMARY}"',
        "--config",
        f'service_tier="{SERVICE_TIER}"',
        "--config",
        f"model_context_window={MODEL_CONTEXT_WINDOW}",
        "--config",
        f"model_auto_compact_token_limit={MODEL_AUTO_COMPACT_TOKEN_LIMIT}",
        "--config",
        'approval_policy="never"',
        "--output-schema",
        str(SCHEMA_PATH),
        "--output-last-message",
        str(last_message),
        "-",
    ]


def invoke_codex(
    executable: str,
    prompt: str,
    timeout: int,
) -> dict[str, Any]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="cnf-codex-") as temp_name:
        temp_dir = Path(temp_name)
        work_dir = temp_dir / "empty-workspace"
        work_dir.mkdir()
        last_message = temp_dir / "last-message.json"
        command = build_command(executable, work_dir, last_message)
        try:
            proc = subprocess.run(
                command,
                input=prompt,
                capture_output=True,
                text=True,
                encoding="utf-8",
                errors="replace",
                timeout=timeout,
                check=False,
                env=os.environ.copy(),
            )
        except subprocess.TimeoutExpired as exc:
            return {
                "infrastructure_error": "timeout",
                "error_detail": f"Codex exceeded {timeout} seconds",
                "stdout": exc.stdout or "",
                "stderr": exc.stderr or "",
                "latency_seconds": round(time.monotonic() - started, 6),
            }
        final_text = last_message.read_text(encoding="utf-8") if last_message.exists() else ""
        contaminated, tool_types, usage = audit_events(proc.stdout)
        return {
            "returncode": proc.returncode,
            "stdout": proc.stdout,
            "stderr": proc.stderr,
            "final_text": final_text.strip(),
            "contaminated": contaminated,
            "tool_types": tool_types,
            "usage": usage,
            "latency_seconds": round(time.monotonic() - started, 6),
            "infrastructure_error": None if proc.returncode == 0 else "codex_exit",
            "error_detail": None if proc.returncode == 0 else f"Codex exited with {proc.returncode}",
        }


def attempt_stem(relative: str, run: int, attempt: int) -> Path:
    relative_path = Path(relative)
    safe_name = relative_path.name.removesuffix(".json")
    return Path(relative_path.parts[0]) / safe_name / f"run-{run:02d}-attempt-{attempt:02d}"


def save_attempt_artifacts(
    run_directory: Path,
    relative: str,
    run: int,
    attempt: int,
    response: dict[str, Any],
) -> None:
    stem = attempt_stem(relative, run, attempt)
    raw_base = run_directory / "raw" / stem
    log_base = run_directory / "logs" / stem
    write_text(raw_base.with_suffix(".events.jsonl"), str(response.get("stdout", "")))
    write_text(raw_base.with_suffix(".final.json"), str(response.get("final_text", "")))
    reasoning = extract_reasoning_summaries(str(response.get("stdout", "")))
    write_text(raw_base.with_suffix(".reasoning.txt"), "\n\n".join(reasoning) + ("\n" if reasoning else ""))
    write_text(log_base.with_suffix(".stderr.log"), str(response.get("stderr", "")))
    metadata = {key: value for key, value in response.items() if key not in {"stdout", "stderr", "final_text"}}
    metadata["reasoning_summary_count"] = len(reasoning)
    write_text(
        log_base.with_suffix(".metadata.json"),
        json.dumps(metadata, ensure_ascii=False, indent=2) + "\n",
    )


def print_plan(
    experiment_id: str,
    run_directory: Path,
    tasks: list[Path],
    completed: set[tuple[str, int]],
    prompt_hash: str,
    version: str,
) -> None:
    total = len(tasks) * REPETITIONS
    remaining = sum(
        1
        for path in tasks
        for run in range(1, REPETITIONS + 1)
        if (path.relative_to(CNF_ROOT).as_posix(), run) not in completed
    )
    print(f"experiment_id={experiment_id}")
    print(f"run_directory={run_directory}")
    print(f"model={MODEL}")
    print(f"reasoning_effort={REASONING_EFFORT}")
    print(f"reasoning_summary={REASONING_SUMMARY}")
    print(f"service_tier={SERVICE_TIER} (Fast, 1.5x)")
    print(f"codex_version={version}")
    print(f"prompt_sha256={prompt_hash}")
    print(f"benchmarks={len(tasks)} planned_valid_runs={total} remaining={remaining}")


def main() -> int:
    args = parse_args()
    if args.workers < 1 or args.retries < 1 or args.contamination_retries < 1:
        raise ValueError("workers and retry counts must be positive")
    experiment_id = validate_experiment_id(args.experiment_id)
    tasks = discover_tasks(args)
    prompt_template, prompt_hash = load_prompt_template()
    executable = codex_executable()
    version = codex_version(executable)
    timestamp = run_timestamp()
    if args.run_directory:
        run_name = validate_experiment_id(args.run_directory)
        run_directory = RUN_ROOT / run_name
    else:
        run_directory = make_run_directory(experiment_id, timestamp)
    experiment_results = run_directory / "results"
    results_path = experiment_results / "runs.jsonl"
    errors_path = experiment_results / "infrastructure-errors.jsonl"
    contaminated_path = experiment_results / "contaminated.jsonl"
    initialized = (run_directory / "configuration.json").exists()
    if initialized and not args.resume:
        raise ValueError(f"run directory already initialized: {run_directory}; use --resume")
    if args.resume and not initialized:
        raise ValueError(f"cannot resume uninitialized run directory: {run_directory}")
    completed = load_completed_slots(results_path) if args.resume else set()
    print_plan(experiment_id, run_directory, tasks, completed, prompt_hash, version)
    if args.dry_run:
        return 0

    metadata = {
        "schema_version": 1,
        "created_at": utc_now(),
        "timestamp_key": timestamp,
        "experiment_content": experiment_id,
        "model": MODEL,
        "reasoning_effort": REASONING_EFFORT,
        "reasoning_summary": REASONING_SUMMARY,
        "service_tier": SERVICE_TIER,
        "model_context_window": MODEL_CONTEXT_WINDOW,
        "model_auto_compact_token_limit": MODEL_AUTO_COMPACT_TOKEN_LIMIT,
        "repetitions": REPETITIONS,
        "codex_version": version,
        "prompt_template_sha256": prompt_hash,
        "selected_logics": args.logic,
        "selected_benchmarks": args.benchmark,
        "benchmark_limit": args.limit,
        "attempt_timeout_seconds": args.timeout,
        "certificate_timeout_seconds": args.certificate_timeout,
        "workers": args.workers,
        "scoring_policy": "sat_certificate_unsat_golden_answer",
    }
    if not initialized:
        write_text(run_directory / "configuration.json", json.dumps(metadata, ensure_ascii=False, indent=2) + "\n")
        write_text(run_directory / "prompt.txt", prompt_template)
        write_text(run_directory / "answer.schema.json", SCHEMA_PATH.read_text(encoding="utf-8"))

    def process_slot(task: Path, run: int) -> bool:
        relative = task.relative_to(CNF_ROOT).as_posix()
        case_text = task.read_text(encoding="utf-8").strip()
        case_value = json.loads(case_text)
        prompt = prompt_template.replace("{{CASE_JSON}}", case_text)
        prompt_instance_hash = sha256_text(prompt)
        infrastructure_tries = 0
        contamination_tries = 0
        attempt = 0
        while True:
            attempt += 1
            print(f"[{relative}] run={run}/5 attempt={attempt}", flush=True)
            response = invoke_codex(executable, prompt, args.timeout)
            save_attempt_artifacts(run_directory, relative, run, attempt, response)

            common = {
                "schema_version": 1, "experiment_id": experiment_id,
                "timestamp": utc_now(), "provider": "codex-cli", "model": MODEL,
                "reasoning_effort": REASONING_EFFORT, "reasoning_summary": REASONING_SUMMARY,
                "service_tier": SERVICE_TIER, "codex_version": version, "case": relative,
                "logic": Path(relative).parts[0], "run": run, "attempt": attempt,
                "prompt_template_sha256": prompt_hash, "prompt_instance_sha256": prompt_instance_hash,
                "case_chars": len(case_text), "latency_seconds": response["latency_seconds"],
            }
            if response.get("infrastructure_error"):
                infrastructure_tries += 1
                append_jsonl(errors_path, {**common, "state": "infrastructure_error", "error_type": response["infrastructure_error"], "error_detail": response.get("error_detail")})
                if infrastructure_tries >= args.retries:
                    print(f"  incomplete: infrastructure retries exhausted", file=sys.stderr, flush=True)
                    return False
                time.sleep(min(2 ** (infrastructure_tries - 1), 30))
                continue
            if response.get("contaminated"):
                contamination_tries += 1
                append_jsonl(contaminated_path, {**common, "state": "contaminated", "tool_types": response.get("tool_types", [])})
                if contamination_tries >= args.contamination_retries:
                    print(f"  incomplete: contamination retries exhausted", file=sys.stderr, flush=True)
                    return False
                continue

            final_text = str(response.get("final_text", ""))
            parse_state, prediction, parsed_response = strict_json_status(final_text)
            benchmark = private_benchmark(case_value)
            expected = expected_status(benchmark)
            verdict_correct = prediction == expected
            if verdict_correct and prediction == "sat":
                artifact = run_directory / "verifier" / attempt_stem(relative, run, attempt).with_suffix(".smt2")
                verification = verify_certificate(task, final_text, artifact, args.certificate_timeout)
                certificate_checked = True
                certificate_valid = verification.get("certificate_valid") is True
                skip_reason, verification_basis, fully_solved = None, "sat_certificate", certificate_valid
            elif verdict_correct and prediction == "unsat":
                verification = {"schema_version": 1, "status": "unsat", "verification_result": "golden_answer_match", "verification_error": None}
                certificate_checked, certificate_valid = False, None
                skip_reason, verification_basis, fully_solved = "unsat_golden_answer_match", "golden_answer", True
            else:
                verification = {}
                certificate_checked, certificate_valid = False, False
                skip_reason = "unreadable_verdict" if prediction is None else "incorrect_verdict" if not verdict_correct else "no_certificate_for_unknown"
                verification_basis, fully_solved = "none", False
            record = {
                **common, "state": "complete", "benchmark": benchmark,
                "response_format": parse_state, "prediction": prediction, "expected": expected,
                "verdict_correct": verdict_correct,
                "certificate_present": isinstance(parsed_response, dict) and isinstance(parsed_response.get("certificate"), dict),
                "certificate_checked": certificate_checked, "certificate_valid": certificate_valid,
                "certificate_skip_reason": skip_reason,
                "sat_witness_checked": verdict_correct and prediction == "sat" and certificate_checked,
                "sat_witness_valid": certificate_valid if verdict_correct and prediction == "sat" else None,
                "verification_basis": verification_basis, "fully_solved": fully_solved,
                "verification": verification, "usage": response.get("usage", {}), "tool_types": [],
            }
            append_jsonl(results_path, record)
            print(f"  prediction={prediction or 'invalid'} expected={expected} verdict_correct={verdict_correct} certificate_valid={certificate_valid}", flush=True)
            return True

    slots = [
        (task, run)
        for task in tasks
        for run in range(1, REPETITIONS + 1)
        if (task.relative_to(CNF_ROOT).as_posix(), run) not in completed
    ]
    failures = 0
    with concurrent.futures.ThreadPoolExecutor(max_workers=args.workers) as executor:
        futures = {executor.submit(process_slot, task, run): (task, run) for task, run in slots}
        for future in concurrent.futures.as_completed(futures):
            task, run = futures[future]
            if future.result():
                completed.add((task.relative_to(CNF_ROOT).as_posix(), run))
            else:
                failures += 1

    print(f"completed_slots={len(completed)} incomplete_slots={failures}")
    return 1 if failures else 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, RuntimeError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
