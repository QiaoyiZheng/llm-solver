#!/usr/bin/env python3
"""Build a versioned statistics snapshot from model experiment runs."""

from __future__ import annotations

import argparse
import csv
import json
from collections import Counter, defaultdict
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


ROOT = Path(__file__).resolve().parents[2]
STATISTICS_ROOT = ROOT / "experiments" / "statistics"
MODEL_DIRS = (
    ("codex-gpt-5.6-sol", "Codex 5.6 Sol"),
    ("deepseek-v4-flash", "DeepSeek V4 Flash"),
    ("deepseek-v4-pro", "DeepSeek V4 Pro"),
)
REPETITIONS = 5
POLICY = "sat_unsat_accuracy_and_correct_sat_witness_rate"
TOTAL_CASES = len(list((ROOT / "benchmarks" / "certificate-inputs" / "cases").rglob("*.json")))


def read_json(path: Path, default=None):
    try:
        return json.loads(path.read_text(encoding="utf-8-sig"))
    except (OSError, json.JSONDecodeError):
        return default


def read_jsonl(path: Path) -> list[dict[str, Any]]:
    rows = []
    try:
        for line in path.read_text(encoding="utf-8-sig").splitlines():
            try:
                value = json.loads(line)
            except json.JSONDecodeError:
                continue
            if isinstance(value, dict):
                rows.append(value)
    except OSError:
        pass
    return rows


def latest_formal_run(model_dir: str) -> Path:
    root = ROOT / "experiments" / model_dir / "runs"
    candidates = [
        path for path in root.iterdir()
        if path.is_dir()
        and "smoke" not in path.name.lower()
        and (path / "configuration.json").is_file()
    ]
    if not candidates:
        raise FileNotFoundError(f"no formal run found under {root}")
    return max(candidates, key=lambda path: path.name)


def deduplicate(rows: list[dict[str, Any]]) -> list[dict[str, Any]]:
    latest: dict[tuple[Any, Any], tuple[tuple[int, int], dict[str, Any]]] = {}
    for index, row in enumerate(rows):
        key = (row.get("case") or row.get("benchmark"), row.get("run"))
        rank = (int(row.get("attempt") or 0), index)
        if key not in latest or rank > latest[key][0]:
            latest[key] = (rank, row)
    return [entry[1] for entry in latest.values() if entry[1].get("state") == "complete"]


def correct(row: dict[str, Any]) -> bool:
    return row.get("verdict_correct") is True


def correct_sat(row: dict[str, Any]) -> bool:
    return correct(row) and row.get("prediction") == "sat"


def valid_sat_witness(row: dict[str, Any]) -> bool:
    return correct_sat(row) and row.get("certificate_valid") is True


def final_success(row: dict[str, Any]) -> bool:
    """Correct UNSAT, or correct SAT with a cvc5-valid witness."""
    if not correct(row):
        return False
    if row.get("prediction") == "unsat":
        return True
    return valid_sat_witness(row)


def metric(numerator: int, denominator: int) -> dict[str, Any]:
    return {
        "numerator": numerator,
        "denominator": denominator,
        "rate": numerator / denominator if denominator else None,
    }


def aggregate(rows: list[dict[str, Any]]) -> dict[str, Any]:
    completed = len(rows)
    correct_count = sum(correct(row) for row in rows)
    correct_sat_count = sum(correct_sat(row) for row in rows)
    valid_witness_count = sum(valid_sat_witness(row) for row in rows)
    return {
        "completed_slots": completed,
        "sat_unsat_accuracy": metric(correct_count, completed),
        "sat_witness_rate": metric(valid_witness_count, correct_sat_count),
        "correct_unsat": sum(correct(row) and row.get("prediction") == "unsat" for row in rows),
    }


def fmt_rate(value: float | None) -> str:
    return "" if value is None else f"{value:.8f}"


def write_json(path: Path, value: Any) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def write_csv(path: Path, fieldnames: list[str], rows: list[dict[str, Any]]) -> None:
    with path.open("w", encoding="utf-8-sig", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)


def build(batch: str, run_overrides: dict[str, Path], overwrite: bool) -> Path:
    if not batch.startswith("v") or not batch[1:].isdigit() or int(batch[1:]) < 1:
        raise ValueError("batch must be v1, v2, v3, ...")
    output = STATISTICS_ROOT / batch
    if output.exists() and any(output.iterdir()) and not overwrite:
        raise FileExistsError(f"batch already exists: {output}; use --overwrite")
    output.mkdir(parents=True, exist_ok=True)
    benchmark_set_path = ROOT / "experiments" / "benchmark-sets" / f"{batch}.json"
    benchmark_set = read_json(benchmark_set_path, {})
    excluded_cases = {
        item["case"] for item in benchmark_set.get("excluded_cases", [])
        if isinstance(item, dict) and item.get("case")
    }
    planned_cases = TOTAL_CASES - len(excluded_cases)
    planned_slots = planned_cases * REPETITIONS

    source_manifest = []
    model_summaries = []
    model_csv = []
    logic_csv = []
    case_csv = []
    distribution_csv = []
    success_bucket_csv = []
    success_bucket_json: dict[str, dict[str, list[dict[str, Any]]]] = {}

    for model_dir, model_label in MODEL_DIRS:
        run = run_overrides.get(model_dir) or latest_formal_run(model_dir)
        config = read_json(run / "configuration.json", {})
        raw = read_jsonl(run / "results" / "runs.jsonl")
        rows = [row for row in deduplicate(raw) if row.get("case") not in excluded_cases]
        summary = aggregate(rows)
        source_manifest.append({
            "model_directory": model_dir,
            "model_label": model_label,
            "run_directory": run.relative_to(ROOT).as_posix(),
            "configuration": config,
            "raw_result_records": len(raw),
            "deduplicated_completed_slots": len(rows),
        })
        model_summaries.append({
            "model": model_label,
            "planned_slots": planned_slots,
            "completion_rate": summary["completed_slots"] / planned_slots,
            **summary,
        })
        model_csv.append({
            "model": model_label,
            "completed_slots": summary["completed_slots"],
            "planned_slots": planned_slots,
            "completion_rate": fmt_rate(summary["completed_slots"] / planned_slots),
            "accuracy_correct": summary["sat_unsat_accuracy"]["numerator"],
            "accuracy_total": summary["sat_unsat_accuracy"]["denominator"],
            "accuracy_rate": fmt_rate(summary["sat_unsat_accuracy"]["rate"]),
            "valid_sat_witnesses": summary["sat_witness_rate"]["numerator"],
            "correct_sat_verdicts": summary["sat_witness_rate"]["denominator"],
            "sat_witness_rate": fmt_rate(summary["sat_witness_rate"]["rate"]),
            "correct_unsat": summary["correct_unsat"],
        })

        by_logic: dict[str, list[dict[str, Any]]] = defaultdict(list)
        by_case: dict[str, list[dict[str, Any]]] = defaultdict(list)
        for row in rows:
            by_logic[str(row.get("logic") or "?")].append(row)
            by_case[str(row.get("case") or row.get("benchmark") or "?")].append(row)
        for logic, logic_rows in sorted(by_logic.items()):
            item = aggregate(logic_rows)
            logic_csv.append({
                "model": model_label,
                "logic": logic,
                "completed_slots": item["completed_slots"],
                "accuracy_correct": item["sat_unsat_accuracy"]["numerator"],
                "accuracy_total": item["sat_unsat_accuracy"]["denominator"],
                "accuracy_rate": fmt_rate(item["sat_unsat_accuracy"]["rate"]),
                "valid_sat_witnesses": item["sat_witness_rate"]["numerator"],
                "correct_sat_verdicts": item["sat_witness_rate"]["denominator"],
                "sat_witness_rate": fmt_rate(item["sat_witness_rate"]["rate"]),
            })

        accuracy_distribution = Counter()
        success_distribution = Counter()
        incomplete_cases = 0
        model_success_buckets = {str(score): [] for score in range(REPETITIONS + 1)}
        model_success_buckets["incomplete"] = []
        for case_name, case_rows in sorted(by_case.items()):
            item = aggregate(case_rows)
            correct_count = item["sat_unsat_accuracy"]["numerator"]
            success_count = sum(final_success(row) for row in case_rows)
            first = case_rows[0]
            bucket_item = {
                "logic": first.get("logic") or "?",
                "case": case_name,
                "benchmark": first.get("benchmark") or "",
                "completed_runs": len(case_rows),
                "successful_runs": success_count,
            }
            if len(case_rows) == REPETITIONS:
                accuracy_distribution[correct_count] += 1
                success_distribution[success_count] += 1
                model_success_buckets[str(success_count)].append(bucket_item)
                success_bucket_csv.append({"model": model_label, "score": success_count, **bucket_item})
            else:
                incomplete_cases += 1
                model_success_buckets["incomplete"].append(bucket_item)
                success_bucket_csv.append({"model": model_label, "score": "incomplete", **bucket_item})
            case_csv.append({
                "model": model_label,
                "logic": first.get("logic") or "?",
                "case": case_name,
                "benchmark": first.get("benchmark") or "",
                "completed_runs": len(case_rows),
                "correct_verdicts": correct_count,
                "final_successes": success_count,
                "valid_sat_witnesses": item["sat_witness_rate"]["numerator"],
                "correct_sat_verdicts": item["sat_witness_rate"]["denominator"],
                "sat_witness_rate": fmt_rate(item["sat_witness_rate"]["rate"]),
            })
        for score in range(REPETITIONS + 1):
            distribution_csv.append({
                "model": model_label,
                "metric": "sat_unsat_correct_out_of_5",
                "score": score,
                "case_count": accuracy_distribution[score],
            })
            distribution_csv.append({
                "model": model_label,
                "metric": "final_success_out_of_5",
                "score": score,
                "case_count": success_distribution[score],
            })
        distribution_csv.append({
            "model": model_label,
            "metric": "incomplete_cases_excluded_from_distribution",
            "score": "",
            "case_count": incomplete_cases,
        })
        success_bucket_json[model_label] = model_success_buckets

    manifest = {
        "schema_version": 1,
        "batch": batch,
        "batch_status": (
            "complete"
            if all(item["deduplicated_completed_slots"] == planned_slots for item in source_manifest)
            else "in_progress"
        ),
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "scoring_policy": POLICY,
        "repetitions": REPETITIONS,
        "benchmark_set": benchmark_set_path.relative_to(ROOT).as_posix() if benchmark_set_path.exists() else None,
        "excluded_cases": sorted(excluded_cases),
        "planned_cases_per_model": planned_cases,
        "planned_slots_per_model": planned_slots,
        "sources": source_manifest,
    }
    write_json(output / "manifest.json", manifest)
    write_json(output / "summary.json", {
        "schema_version": 1,
        "batch": batch,
        "scoring_policy": POLICY,
        "models": model_summaries,
    })
    write_csv(output / "models.csv", list(model_csv[0]), model_csv)
    write_csv(output / "logics.csv", list(logic_csv[0]), logic_csv)
    write_csv(output / "cases.csv", list(case_csv[0]), case_csv)
    write_csv(output / "distributions.csv", list(distribution_csv[0]), distribution_csv)
    write_csv(output / "success_buckets.csv", list(success_bucket_csv[0]), success_bucket_csv)
    write_json(output / "success_buckets.json", {
        "schema_version": 1,
        "batch": batch,
        "success_definition": "correct_unsat_or_correct_sat_with_valid_witness",
        "models": success_bucket_json,
    })
    return output


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--batch", required=True, help="v1, v2, v3, ...")
    parser.add_argument("--overwrite", action="store_true")
    for model_dir, _ in MODEL_DIRS:
        parser.add_argument(f"--{model_dir}-run", type=Path)
    args = parser.parse_args()
    overrides = {}
    for model_dir, _ in MODEL_DIRS:
        value = getattr(args, f"{model_dir.replace('-', '_')}_run")
        if value:
            overrides[model_dir] = value.resolve()
    output = build(args.batch, overrides, args.overwrite)
    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
