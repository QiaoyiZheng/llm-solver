#!/usr/bin/env python3
"""Build label-free machine-readable inputs for certificate experiments."""

from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent
INPUT_ROOT = SCRIPT_DIR.parent
REPO_ROOT = INPUT_ROOT.parents[1]
CNF_ROOT = REPO_ROOT / "benchmarks" / "CNF-Bench"
SMT_ROOT = REPO_ROOT / "benchmarks" / "smtlib-2025"
CASE_ROOT = INPUT_ROOT / "cases"
EXPECTED_CASES = 95
sys.setrecursionlimit(100_000)
FORBIDDEN_KEYS = {
    "benchmark",
    "case_id",
    "checksum",
    "expected",
    "filename",
    "path",
    "sha256",
    "source",
    "status",
}


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    position = 0
    while position < len(text):
        char = text[position]
        if char.isspace():
            position += 1
        elif char == ";":
            newline = text.find("\n", position)
            position = len(text) if newline < 0 else newline + 1
        elif char in "()":
            tokens.append(char)
            position += 1
        elif char == "|":
            end = position + 1
            while end < len(text) and text[end] != "|":
                end += 1
            if end >= len(text):
                raise ValueError("unterminated quoted symbol")
            end += 1
            tokens.append(text[position:end])
            position = end
        elif char == '"':
            end = position + 1
            while end < len(text):
                if text[end] == '"':
                    if end + 1 < len(text) and text[end + 1] == '"':
                        end += 2
                        continue
                    end += 1
                    break
                end += 1
            else:
                raise ValueError("unterminated string")
            tokens.append(text[position:end])
            position = end
        else:
            end = position + 1
            while end < len(text) and not text[end].isspace() and text[end] not in "();":
                end += 1
            tokens.append(text[position:end])
            position = end
    return tokens


def parse_all(tokens: list[str]) -> list[object]:
    position = 0

    def parse_one() -> object:
        nonlocal position
        if position >= len(tokens):
            raise ValueError("unexpected end of SMT-LIB input")
        token = tokens[position]
        position += 1
        if token != "(":
            if token == ")":
                raise ValueError("unexpected closing parenthesis")
            return token
        result: list[object] = []
        while position < len(tokens) and tokens[position] != ")":
            result.append(parse_one())
        if position >= len(tokens):
            raise ValueError("unclosed parenthesis")
        position += 1
        return result

    forms: list[object] = []
    while position < len(tokens):
        forms.append(parse_one())
    return forms


def render(node: object) -> str:
    if isinstance(node, list):
        return "(" + " ".join(render(item) for item in node) + ")"
    return str(node)


def parse_signature(smt_text: str) -> tuple[str, list[dict[str, object]]]:
    forms = parse_all(tokenize(smt_text))
    logic: str | None = None
    declarations: list[dict[str, object]] = []
    unsupported_definitions: list[str] = []
    for form in forms:
        if not isinstance(form, list) or not form:
            continue
        head = form[0]
        if head == "set-logic" and len(form) == 2:
            logic = str(form[1])
        elif head == "declare-const" and len(form) == 3:
            declarations.append(
                {
                    "kind": "constant",
                    "symbol": str(form[1]),
                    "parameter_sorts": [],
                    "return_sort": render(form[2]),
                }
            )
        elif head == "declare-fun" and len(form) == 4 and isinstance(form[2], list):
            parameter_sorts = [render(sort) for sort in form[2]]
            declarations.append(
                {
                    "kind": "constant" if not parameter_sorts else "function",
                    "symbol": str(form[1]),
                    "parameter_sorts": parameter_sorts,
                    "return_sort": render(form[3]),
                }
            )
        elif head in {"define-fun", "define-fun-rec", "define-funs-rec"}:
            unsupported_definitions.append(str(head))
    if logic is None:
        raise ValueError("missing set-logic command")
    if unsupported_definitions:
        raise ValueError(f"defined functions are not supported: {sorted(set(unsupported_definitions))}")
    symbols = [str(item["symbol"]) for item in declarations]
    if len(symbols) != len(set(symbols)):
        raise ValueError("duplicate declaration symbol")
    return logic, declarations


def opaque_case_name(cnf: str) -> str:
    digest = hashlib.sha256(cnf.encode("utf-8")).hexdigest()[:20]
    return f"case-{digest}.json"


def validate_public_case(value: object) -> None:
    if not isinstance(value, dict):
        raise ValueError("case is not a JSON object")
    if set(value) != {"schema_version", "logic", "declarations", "cnf"}:
        raise ValueError(f"unexpected top-level keys: {sorted(value)}")

    def walk(node: object) -> None:
        if isinstance(node, dict):
            leaked = {str(key).lower() for key in node} & FORBIDDEN_KEYS
            if leaked:
                raise ValueError(f"forbidden identity/label keys: {sorted(leaked)}")
            for child in node.values():
                walk(child)
        elif isinstance(node, list):
            for child in node:
                walk(child)

    walk(value)
    if value["schema_version"] != 1:
        raise ValueError("unsupported schema version")
    if not isinstance(value["logic"], str) or not value["logic"]:
        raise ValueError("invalid logic")
    if not isinstance(value["declarations"], list):
        raise ValueError("invalid declarations")
    if not isinstance(value["cnf"], str) or not value["cnf"].strip():
        raise ValueError("invalid CNF expression")


def build_case(cnf_path: Path) -> tuple[Path, dict[str, object]]:
    relative = cnf_path.relative_to(CNF_ROOT)
    smt_path = (SMT_ROOT / relative).with_suffix(".smt2")
    if not smt_path.is_file():
        raise FileNotFoundError(f"matching SMT-LIB file not found for {relative}")
    cnf = cnf_path.read_text(encoding="utf-8").strip()
    logic, declarations = parse_signature(smt_path.read_text(encoding="utf-8"))
    if logic != relative.parts[0]:
        raise ValueError(f"logic mismatch for {relative}: {logic}")
    public_case: dict[str, object] = {
        "schema_version": 1,
        "logic": logic,
        "declarations": declarations,
        "cnf": cnf,
    }
    validate_public_case(public_case)
    destination = CASE_ROOT / logic / opaque_case_name(cnf)
    return destination, public_case


def main() -> int:
    cnf_files = sorted(CNF_ROOT.rglob("*.md"))
    if len(cnf_files) != EXPECTED_CASES:
        raise ValueError(f"expected {EXPECTED_CASES} CNF files, found {len(cnf_files)}")
    destinations: set[Path] = set()
    cases: list[tuple[Path, dict[str, object]]] = []
    for cnf_path in cnf_files:
        destination, public_case = build_case(cnf_path)
        if destination in destinations:
            raise ValueError(f"opaque case ID collision: {destination.name}")
        destinations.add(destination)
        cases.append((destination, public_case))

    for destination, public_case in cases:
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(
            json.dumps(public_case, ensure_ascii=False, indent=2) + "\n",
            encoding="utf-8",
            newline="\n",
        )

    generated = sorted(CASE_ROOT.rglob("*.json"))
    unexpected = set(generated) - destinations
    if unexpected:
        names = ", ".join(str(path.relative_to(CASE_ROOT)) for path in sorted(unexpected))
        raise ValueError(f"stale case files found: {names}")

    declaration_count = sum(len(value["declarations"]) for _, value in cases)
    total_bytes = sum(path.stat().st_size for path in generated)
    print(f"cases={len(generated)} declarations={declaration_count} bytes={total_bytes}")
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (FileNotFoundError, ValueError) as exc:
        print(f"error: {exc}", file=sys.stderr)
        raise SystemExit(2)
