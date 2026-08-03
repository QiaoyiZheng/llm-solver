#!/usr/bin/env python3
"""Verify label-free SAT models and UNSAT CNF cores using cvc5."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import time
from pathlib import Path
from typing import Any

sys.setrecursionlimit(100_000)

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
CNF_ROOT = ROOT / "benchmarks" / "CNF-Bench"
SMT_ROOT = ROOT / "benchmarks" / "smtlib-2025"
PINNED_CVC5 = ROOT / "tools" / "cvc5" / "1.3.3" / "cvc5-Win64-x86_64-static" / "bin" / "cvc5.exe"

AND, OR, NOT = "\u2227", "\u2228", "\u00ac"
BL, BR, TOP, BOTTOM = "\u27e6", "\u27e7", "\u22a4", "\u22a5"
TAU = re.compile(r"\u03c4([0-9]+)$")
LAM = re.compile(r"\u03bb([0-9]+)$")
SAFE_NAME = re.compile(r"[A-Za-z_][A-Za-z0-9_]*$")
MAX_SCRIPT = 50_000_000


class VerifyError(ValueError):
    pass


def tokens(text: str) -> list[str]:
    out: list[str] = []
    i = 0
    while i < len(text):
        c = text[i]
        if c.isspace():
            i += 1
        elif c == ";":
            j = text.find("\n", i)
            i = len(text) if j < 0 else j + 1
        elif c in "()":
            out.append(c)
            i += 1
        elif c == "|":
            j = text.find("|", i + 1)
            if j < 0:
                raise VerifyError("unterminated quoted symbol")
            out.append(text[i : j + 1])
            i = j + 1
        elif c == '"':
            j = i + 1
            while j < len(text):
                if text[j] == '"':
                    if j + 1 < len(text) and text[j + 1] == '"':
                        j += 2
                        continue
                    j += 1
                    break
                j += 1
            else:
                raise VerifyError("unterminated string")
            out.append(text[i:j])
            i = j
        else:
            j = i + 1
            while j < len(text) and not text[j].isspace() and text[j] not in "();":
                j += 1
            out.append(text[i:j])
            i = j
    return out


def parse_all(text: str) -> list[object]:
    ts = tokens(text)
    pos = 0

    def one() -> object:
        nonlocal pos
        if pos >= len(ts):
            raise VerifyError("unexpected end of SMT-LIB")
        token = ts[pos]
        pos += 1
        if token != "(":
            if token == ")":
                raise VerifyError("unexpected closing parenthesis")
            return token
        result: list[object] = []
        while pos < len(ts) and ts[pos] != ")":
            result.append(one())
        if pos >= len(ts):
            raise VerifyError("unclosed parenthesis")
        pos += 1
        return result

    result: list[object] = []
    while pos < len(ts):
        result.append(one())
    return result


def term(text: str, field: str) -> object:
    forms = parse_all(text)
    if len(forms) != 1:
        raise VerifyError(f"{field} must contain exactly one SMT-LIB term")
    value = forms[0]
    commands = {"assert", "check-sat", "declare-const", "declare-fun", "define-fun", "exit", "get-model", "get-value", "include", "set-info", "set-logic", "set-option"}
    if isinstance(value, list) and value and isinstance(value[0], str) and value[0] in commands:
        raise VerifyError(f"{field} contains a command")
    return value


def render(value: object) -> str:
    return "(" + " ".join(render(x) for x in value) + ")" if isinstance(value, list) else str(value)


def atoms(value: object) -> set[str]:
    if isinstance(value, list):
        return set().union(*(atoms(item) for item in value)) if value else set()
    return {str(value)}


def exact(value: Any, keys: set[str], where: str) -> dict[str, Any]:
    if not isinstance(value, dict) or set(value) != keys:
        actual = set(value) if isinstance(value, dict) else set()
        raise VerifyError(f"{where} keys mismatch: missing={sorted(keys-actual)} extra={sorted(actual-keys)}")
    return value


def validate_response(value: Any) -> dict[str, Any]:
    value = exact(value, {"schema_version", "status", "certificate"}, "response")
    if value["schema_version"] != 1:
        raise VerifyError("schema_version must be 1")
    cert = value["certificate"]
    if value["status"] == "sat":
        cert = exact(cert, {"kind", "constants", "functions"}, "certificate")
        if cert["kind"] != "sat_model" or not isinstance(cert["constants"], list) or not isinstance(cert["functions"], list):
            raise VerifyError("invalid sat_model certificate")
        for i, item in enumerate(cert["constants"]):
            item = exact(item, {"symbol", "sort", "value_smt2"}, f"constant[{i}]")
            if any(not isinstance(v, str) or not v for v in item.values()):
                raise VerifyError(f"constant[{i}] fields must be non-empty strings")
        for i, item in enumerate(cert["functions"]):
            item = exact(item, {"symbol", "parameters", "return_sort", "body_smt2"}, f"function[{i}]")
            if any(not isinstance(item[k], str) or not item[k] for k in ("symbol", "return_sort", "body_smt2")) or not isinstance(item["parameters"], list):
                raise VerifyError(f"invalid function[{i}]")
            for j, parameter in enumerate(item["parameters"]):
                parameter = exact(parameter, {"symbol", "sort"}, f"function[{i}].parameter[{j}]")
                if not isinstance(parameter["symbol"], str) or not SAFE_NAME.fullmatch(parameter["symbol"]) or not isinstance(parameter["sort"], str) or not parameter["sort"]:
                    raise VerifyError("unsafe function parameter")
    elif value["status"] == "unsat":
        cert = exact(cert, {"kind", "clause_indices"}, "certificate")
        indices = cert["clause_indices"]
        if cert["kind"] != "unsat_core" or not isinstance(indices, list) or not indices:
            raise VerifyError("invalid unsat_core certificate")
        if any(isinstance(i, bool) or not isinstance(i, int) or i < 1 for i in indices) or len(indices) != len(set(indices)):
            raise VerifyError("clause_indices must be unique positive integers")
    elif value["status"] == "unknown":
        cert = exact(cert, {"kind"}, "certificate")
        if cert["kind"] != "none":
            raise VerifyError("unknown certificate kind must be none")
    else:
        raise VerifyError("invalid status")
    return value


def load_case(path: Path) -> dict[str, Any]:
    value = exact(json.loads(path.read_text(encoding="utf-8")), {"schema_version", "logic", "declarations", "cnf"}, "case")
    if value["schema_version"] != 1 or not isinstance(value["logic"], str) or not isinstance(value["declarations"], list) or not isinstance(value["cnf"], str):
        raise VerifyError("invalid case")
    return value


def original_path(case: dict[str, Any]) -> Path:
    matches = [p for p in (CNF_ROOT / case["logic"]).glob("*.md") if p.read_text(encoding="utf-8").strip() == case["cnf"].strip()]
    if len(matches) != 1:
        raise VerifyError(f"private case association count is {len(matches)}, expected 1")
    return (SMT_ROOT / matches[0].relative_to(CNF_ROOT)).with_suffix(".smt2")


def source_parts(path: Path) -> tuple[list[object], list[object]]:
    prelude_heads = {"set-logic", "declare-const", "declare-fun", "declare-sort", "declare-datatype", "declare-datatypes", "define-fun", "define-fun-rec", "define-funs-rec"}
    prelude, assertions = [], []
    for form in parse_all(path.read_text(encoding="utf-8")):
        if isinstance(form, list) and form:
            if form[0] in prelude_heads:
                prelude.append(form)
            elif form[0] == "assert" and len(form) == 2:
                assertions.append(form)
    if not prelude or not assertions:
        raise VerifyError("source prelude/assertions missing")
    return prelude, assertions


def declarations(case: dict[str, Any]) -> dict[str, dict[str, Any]]:
    result = {}
    for i, declaration in enumerate(case["declarations"]):
        declaration = exact(declaration, {"kind", "symbol", "parameter_sorts", "return_sort"}, f"declaration[{i}]")
        symbol = declaration["symbol"]
        if not isinstance(symbol, str) or not symbol or symbol in result:
            raise VerifyError("invalid/duplicate declaration")
        result[symbol] = declaration
    return result


def sat_script(case: dict[str, Any], response: dict[str, Any], source: Path) -> str:
    decls = declarations(case)
    constants = {x["symbol"]: x for x in response["certificate"]["constants"]}
    functions = {x["symbol"]: x for x in response["certificate"]["functions"]}
    if len(constants) != len(response["certificate"]["constants"]) or len(functions) != len(response["certificate"]["functions"]):
        raise VerifyError("duplicate witness symbol")
    expected_c = {s for s, d in decls.items() if not d["parameter_sorts"]}
    expected_f = set(decls) - expected_c
    if set(constants) != expected_c:
        raise VerifyError(f"constant coverage mismatch: missing={sorted(expected_c-set(constants))} extra={sorted(set(constants)-expected_c)}")
    if set(functions) != expected_f:
        raise VerifyError(f"function coverage mismatch: missing={sorted(expected_f-set(functions))} extra={sorted(set(functions)-expected_f)}")
    bindings = []
    declared_symbols = set(decls)
    for symbol in sorted(expected_c):
        witness, decl = constants[symbol], decls[symbol]
        if witness["sort"] != decl["return_sort"]:
            raise VerifyError(f"sort mismatch for {symbol}")
        value = term(witness["value_smt2"], symbol)
        references = atoms(value) & declared_symbols
        if references:
            raise VerifyError(f"constant witness {symbol} references declared symbols: {sorted(references)}")
        bindings.append(f"(assert (= {symbol} {render(value)}))")
    for symbol in sorted(expected_f):
        witness, decl = functions[symbol], decls[symbol]
        params, sorts = witness["parameters"], decl["parameter_sorts"]
        if len(params) != len(sorts) or witness["return_sort"] != decl["return_sort"] or [p["sort"] for p in params] != sorts:
            raise VerifyError(f"signature mismatch for {symbol}")
        names = [p["symbol"] for p in params]
        if len(names) != len(set(names)):
            raise VerifyError(f"duplicate binder for {symbol}")
        if set(names) & declared_symbols:
            raise VerifyError(f"binder for {symbol} shadows a declared symbol")
        binders = " ".join(f"({p['symbol']} {p['sort']})" for p in params)
        body_term = term(witness["body_smt2"], symbol)
        references = atoms(body_term) & declared_symbols
        if references:
            raise VerifyError(f"function witness {symbol} references declared symbols: {sorted(references)}")
        body = render(body_term)
        bindings.append(f"(assert (forall ({binders}) (= ({symbol} {' '.join(names)}) {body})))")
    prelude, assertions = source_parts(source)
    return checked_script([render(x) for x in prelude + assertions] + bindings + ["(check-sat)"])


def split_outer(text: str, separator: str) -> list[str]:
    result, start, depth, boxed = [], 0, 0, False
    for i, char in enumerate(text):
        if boxed:
            if char == BR:
                boxed = False
        elif char == BL:
            boxed = True
        elif char == "(":
            depth += 1
        elif char == ")":
            depth -= 1
        elif char == separator and depth == 0:
            result.append(text[start:i].strip())
            start = i + 1
        if depth < 0:
            raise VerifyError("unbalanced CNF")
    if boxed or depth:
        raise VerifyError("unclosed CNF")
    result.append(text[start:].strip())
    return result


def clauses(cnf: str) -> list[list[str]]:
    text = cnf.strip()
    if text == TOP:
        return []
    if text == BOTTOM:
        return [[]]
    result = []
    for i, clause in enumerate(split_outer(text, AND), 1):
        if not clause.startswith("(") or not clause.endswith(")"):
            raise VerifyError(f"clause {i} is not parenthesized")
        body = clause[1:-1].strip()
        result.append(split_outer(body, OR) if body else [])
    return result


def literal(text: str) -> tuple[bool, str, str]:
    neg = text.startswith(NOT)
    core = text[1:].strip() if neg else text.strip()
    match = TAU.fullmatch(core)
    if match:
        return neg, "tau", match.group(1)
    if core.startswith(BL) and core.endswith(BR):
        return neg, "atom", core[1:-1]
    raise VerifyError(f"invalid literal: {text[:80]}")


def lambda_definitions(all_clauses: list[list[str]]) -> dict[str, object]:
    result = {}
    for clause in all_clauses:
        if len(clause) != 1:
            continue
        neg, kind, raw = literal(clause[0])
        value = term(raw, "theory atom") if not neg and kind == "atom" else None
        if isinstance(value, list) and len(value) == 3 and value[0] == "=" and isinstance(value[1], str) and LAM.fullmatch(value[1]):
            if value[1] in result and result[value[1]] != value[2]:
                raise VerifyError(f"conflicting definition {value[1]}")
            result[value[1]] = value[2]
    return result


def expand(value: object, definitions: dict[str, object], stack: tuple[str, ...] = ()) -> object:
    if isinstance(value, str) and value in definitions:
        if value in stack:
            raise VerifyError(f"cyclic definition {value}")
        return expand(definitions[value], definitions, stack + (value,))
    return [expand(x, definitions, stack) for x in value] if isinstance(value, list) else value


def unsat_script(case: dict[str, Any], response: dict[str, Any], source: Path) -> str:
    all_clauses = clauses(case["cnf"])
    indices = response["certificate"]["clause_indices"]
    if any(i > len(all_clauses) for i in indices):
        raise VerifyError(f"clause index exceeds {len(all_clauses)}")
    definitions = lambda_definitions(all_clauses)
    taus, assertions = set(), []
    for index in indices:
        terms = []
        for item in all_clauses[index - 1]:
            neg, kind, raw = literal(item)
            if kind == "tau":
                atom = f"__cert_tau_{raw}"
                taus.add(atom)
            else:
                atom = render(expand(term(raw, "theory atom"), definitions))
            terms.append(f"(not {atom})" if neg else atom)
        clause_term = "false" if not terms else terms[0] if len(terms) == 1 else f"(or {' '.join(terms)})"
        assertions.append(f"(assert {clause_term})")
    prelude, _ = source_parts(source)
    tau_declarations = [f"(declare-const {symbol} Bool)" for symbol in sorted(taus)]
    return checked_script([render(x) for x in prelude] + tau_declarations + assertions + ["(check-sat)"])


def checked_script(lines: list[str]) -> str:
    script = "\n".join(lines) + "\n"
    if len(script) > MAX_SCRIPT:
        raise VerifyError("generated script exceeds size limit")
    return script


def find_cvc5(requested: str | None) -> str:
    if requested:
        path = Path(requested)
        resolved = str(path.resolve()) if path.is_file() else shutil.which(requested)
    else:
        resolved = str(PINNED_CVC5) if PINNED_CVC5.is_file() else shutil.which("cvc5")
    if not resolved:
        raise FileNotFoundError("cvc5 executable not found")
    return resolved


def solve(executable: str, script: str, timeout: int) -> dict[str, Any]:
    started = time.monotonic()
    with tempfile.TemporaryDirectory(prefix="cert-cvc5-") as directory:
        path = Path(directory) / "verify.smt2"
        path.write_text(script, encoding="utf-8", newline="\n")
        try:
            proc = subprocess.run([executable, "--lang=smt2", "--arrays-exp", str(path)], capture_output=True, text=True, encoding="utf-8", errors="replace", timeout=timeout, check=False)
        except subprocess.TimeoutExpired:
            return {"result": "timeout", "returncode": None, "stderr": "", "seconds": round(time.monotonic()-started, 6)}
    first = proc.stdout.strip().splitlines()[0] if proc.stdout.strip() else ""
    return {"result": first if first in {"sat", "unsat", "unknown"} else "invalid_output", "returncode": proc.returncode, "stderr": proc.stderr.strip(), "seconds": round(time.monotonic()-started, 6)}


def arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--case", type=Path, required=True)
    parser.add_argument("--response", type=Path, required=True)
    parser.add_argument("--cvc5")
    parser.add_argument("--timeout", type=int, default=300)
    parser.add_argument("--artifact", type=Path)
    parser.add_argument("--emit-smt-only", action="store_true")
    return parser.parse_args()


def main() -> int:
    args = arguments()
    case = load_case(args.case)
    response = validate_response(json.loads(args.response.read_text(encoding="utf-8")))
    status = response["status"]
    if status == "unknown":
        print(json.dumps({"schema_version": 1, "status": status, "certificate_present": False, "certificate_valid": False, "verification_result": "not_applicable", "verification_error": None}, separators=(",", ":")))
        return 0
    source = original_path(case)
    script = sat_script(case, response, source) if status == "sat" else unsat_script(case, response, source)
    if args.artifact:
        args.artifact.parent.mkdir(parents=True, exist_ok=True)
        args.artifact.write_text(script, encoding="utf-8", newline="\n")
    if args.emit_smt_only:
        print(json.dumps({"schema_version": 1, "status": status, "certificate_present": True, "certificate_valid": None, "verification_result": "not_run", "verification_error": None, "generated_smt_chars": len(script)}, separators=(",", ":")))
        return 0
    result = solve(find_cvc5(args.cvc5), script, args.timeout)
    wanted = status
    valid = result["returncode"] == 0 and result["result"] == wanted
    print(json.dumps({"schema_version": 1, "status": status, "certificate_present": True, "certificate_valid": valid, "verification_result": result["result"], "verification_error": None if valid else result["stderr"] or None, "solver_returncode": result["returncode"], "latency_seconds": result["seconds"]}, ensure_ascii=False, separators=(",", ":")))
    return 0 if valid else 1


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (VerifyError, FileNotFoundError, json.JSONDecodeError) as error:
        print(json.dumps({"schema_version": 1, "certificate_present": False, "certificate_valid": False, "verification_result": "verifier_error", "verification_error": str(error)}, ensure_ascii=False, separators=(",", ":")))
        raise SystemExit(2)
