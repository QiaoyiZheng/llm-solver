#!/usr/bin/env python3
"""Run one end-to-end certificate smoke case on all three configured models."""

from __future__ import annotations

import argparse
import importlib.util
import json
import os
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[1]
CASE = ROOT / "benchmarks" / "certificate-inputs" / "cases" / "QF_S" / "case-86e332303e31782155c0.json"
PROMPT_PATH = ROOT / "experiments" / "codex-gpt-5.6-sol" / "config" / "prompt.txt"
CODEX_RUNNER = ROOT / "experiments" / "codex-gpt-5.6-sol" / "scripts" / "run_codex.py"
VERIFIER = ROOT / "experiments" / "certificate-verifier" / "scripts" / "verify_certificate.py"


def timestamp() -> str:
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def write_json(path: Path, value: Any) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def load_codex_runner():
    spec = importlib.util.spec_from_file_location("certificate_codex_runner", CODEX_RUNNER)
    if spec is None or spec.loader is None:
        raise RuntimeError("cannot load Codex runner")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def prompt() -> str:
    template = PROMPT_PATH.read_text(encoding="utf-8")
    return template.replace("{{CASE_JSON}}", CASE.read_text(encoding="utf-8").strip())


def load_key(config_path: Path) -> tuple[dict[str, str], str]:
    config = json.loads(config_path.read_text(encoding="utf-8"))
    key_path = (config_path.parent / config["api_key_file"]).resolve()
    key = key_path.read_text(encoding="utf-8").strip() if key_path.is_file() else ""
    if not key:
        key = os.environ.get(config["api_key_environment_fallback"], "").strip()
    if not key:
        raise RuntimeError(f"API key unavailable for {config['model']}")
    return config, key


def call_deepseek(config_path: Path, task_prompt: str, timeout: int, max_tokens: int = 4096) -> dict[str, Any]:
    config, key = load_key(config_path)
    body = {
        "model": config["model"],
        "messages": [{"role": "user", "content": task_prompt}],
        "thinking": {"type": "enabled"},
        "reasoning_effort": "max",
        "response_format": {"type": "json_object"},
        "max_tokens": max_tokens,
        "stream": False,
    }
    request = urllib.request.Request(
        config["base_url"].rstrip("/") + "/chat/completions",
        data=json.dumps(body).encode("utf-8"),
        headers={"Authorization": "Bearer " + key, "Content-Type": "application/json"},
        method="POST",
    )
    started = time.monotonic()
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            payload = json.load(response)
    except urllib.error.HTTPError as error:
        detail = error.read().decode("utf-8", errors="replace")
        raise RuntimeError(f"DeepSeek HTTP {error.code}: {detail[:1000]}") from error
    choice = payload["choices"][0]
    message = choice["message"]
    return {
        "final_text": message.get("content") or "",
        "reasoning_content": message.get("reasoning_content") or "",
        "usage": payload.get("usage", {}),
        "finish_reason": choice.get("finish_reason"),
        "actual_model": payload.get("model"),
        "latency_seconds": round(time.monotonic() - started, 6),
        "response_id": payload.get("id"),
    }


def check_certificate(final_text: str, expected: str, artifact: Path, timeout: int) -> dict[str, Any]:
    try:
        response = json.loads(final_text)
    except json.JSONDecodeError:
        response = None
    prediction = response.get("status") if isinstance(response, dict) else None
    verdict_correct = prediction == expected
    result: dict[str, Any] = {
        "prediction": prediction,
        "expected": expected,
        "verdict_correct": verdict_correct,
        "certificate_checked": False,
        "certificate_valid": False,
        "sat_witness_checked": False,
        "sat_witness_valid": None,
        "fully_solved": False,
    }
    if not verdict_correct:
        result["certificate_skip_reason"] = "unreadable_verdict" if prediction is None else "incorrect_verdict"
        result["verification_basis"] = "none"
        return result
    if prediction == "unsat":
        result.update({
            "certificate_valid": None,
            "certificate_skip_reason": "unsat_golden_answer_match",
            "fully_solved": True,
            "verification_basis": "golden_answer",
            "verification": {
                "schema_version": 1,
                "status": "unsat",
                "verification_result": "golden_answer_match",
                "verification_error": None,
            },
        })
        return result
    with tempfile.TemporaryDirectory(prefix="smoke-certificate-") as directory:
        response_path = Path(directory) / "response.json"
        response_path.write_text(final_text, encoding="utf-8", newline="\n")
        proc = subprocess.run(
            [sys.executable, str(VERIFIER), "--case", str(CASE), "--response", str(response_path), "--artifact", str(artifact), "--timeout", str(timeout)],
            capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout + 30, check=False,
        )
    try:
        verifier_result = json.loads(proc.stdout.strip())
    except json.JSONDecodeError:
        verifier_result = {"verification_result": "invalid_verifier_output", "verification_error": proc.stderr.strip()}
    result.update({
        "certificate_checked": True,
        "certificate_valid": verifier_result.get("certificate_valid") is True,
        "sat_witness_checked": True,
        "sat_witness_valid": verifier_result.get("certificate_valid") is True,
        "certificate_skip_reason": None,
        "fully_solved": verifier_result.get("certificate_valid") is True,
        "verification_basis": "sat_certificate",
        "verification": verifier_result,
    })
    return result


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--model", action="append", choices=["codex-gpt-5.6-sol", "deepseek-v4-flash", "deepseek-v4-pro"])
    args = parser.parse_args()
    task_prompt = prompt()
    runner = load_codex_runner()
    case_value = json.loads(CASE.read_text(encoding="utf-8"))
    benchmark = runner.private_benchmark(case_value)
    expected = runner.expected_status(benchmark)
    stamp = timestamp()
    models = [
        ("codex-gpt-5.6-sol", "gpt-5.6-sol_high_priority_1x-smoke"),
        ("deepseek-v4-flash", "deepseek-v4-flash_max-thinking_1x-smoke"),
        ("deepseek-v4-pro", "deepseek-v4-pro_max-thinking_1x-smoke"),
    ]
    if args.model:
        selected = set(args.model)
        models = [item for item in models if item[0] in selected]
    summaries = []
    for directory_name, configuration_name in models:
        run_dir = ROOT / "experiments" / directory_name / "runs" / f"{stamp}__certificate-smoke__{configuration_name}"
        run_dir.mkdir(parents=True, exist_ok=False)
        started = time.monotonic()
        try:
            if directory_name == "codex-gpt-5.6-sol":
                response = runner.invoke_codex(runner.codex_executable(), task_prompt, 600)
                if response.get("infrastructure_error"):
                    detail = "\n".join(filter(None, [
                        str(response.get("error_detail") or response["infrastructure_error"]),
                        str(response.get("stderr") or ""),
                        str(response.get("stdout") or "")[-5000:],
                    ]))
                    raise RuntimeError(detail[:7000])
            else:
                response = call_deepseek(ROOT / "experiments" / directory_name / "config" / "api.json", task_prompt, 600)
            (run_dir / "raw").mkdir()
            (run_dir / "logs").mkdir()
            (run_dir / "results").mkdir()
            (run_dir / "raw" / "response.json").write_text(str(response["final_text"]), encoding="utf-8", newline="\n")
            if directory_name == "codex-gpt-5.6-sol":
                (run_dir / "raw" / "events.jsonl").write_text(str(response.get("stdout", "")), encoding="utf-8", newline="\n")
                reasoning_summaries = runner.extract_reasoning_summaries(str(response.get("stdout", "")))
                (run_dir / "raw" / "reasoning.txt").write_text("\n\n".join(reasoning_summaries) + ("\n" if reasoning_summaries else ""), encoding="utf-8", newline="\n")
            if response.get("reasoning_content"):
                (run_dir / "raw" / "reasoning.txt").write_text(str(response["reasoning_content"]), encoding="utf-8", newline="\n")
            metadata = {key: value for key, value in response.items() if key not in {"final_text", "reasoning_content", "stdout", "stderr"}}
            if directory_name == "codex-gpt-5.6-sol":
                metadata["reasoning_summary_count"] = len(reasoning_summaries)
                metadata["reasoning_note"] = "Only summaries exposed by Codex CLI are recorded; hidden chain-of-thought is unavailable."
            write_json(run_dir / "logs" / "model-metadata.json", metadata)
            result = check_certificate(str(response["final_text"]), expected, run_dir / "verifier" / "certificate.smt2", 120)
            result.update({"model": directory_name, "smoke_ok": True, "benchmark": benchmark, "elapsed_seconds": round(time.monotonic() - started, 6)})
        except Exception as error:
            result = {"model": directory_name, "smoke_ok": False, "error": str(error), "elapsed_seconds": round(time.monotonic() - started, 6)}
        write_json(run_dir / "configuration.json", {"schema_version": 1, "experiment": "certificate-smoke", "timestamp": stamp, "model": directory_name, "configuration": configuration_name, "case_sent_without_filename": True})
        write_json(run_dir / "results" / "smoke-result.json", result)
        summaries.append(result)
        print(json.dumps(result, ensure_ascii=False, separators=(",", ":")), flush=True)
    all_reachable = all(item["smoke_ok"] for item in summaries)
    print(json.dumps({"all_models_reachable": all_reachable, "runs": len(summaries)}, separators=(",", ":")))
    return 0 if all_reachable else 1


if __name__ == "__main__":
    raise SystemExit(main())
