from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


SOURCE = Path("benchmarks/smtlib-2025")
TARGET = Path("benchmarks/CNF-Bench")
sys.setrecursionlimit(100_000)


def tokenize(text: str) -> list[str]:
    tokens: list[str] = []
    i = 0
    n = len(text)
    while i < n:
        c = text[i]
        if c.isspace():
            i += 1
        elif c == ";":
            j = text.find("\n", i)
            i = n if j < 0 else j + 1
        elif c in "()":
            tokens.append(c)
            i += 1
        elif c == "|":
            j = i + 1
            while j < n:
                if text[j] == "|":
                    j += 1
                    break
                j += 1
            tokens.append(text[i:j])
            i = j
        elif c == '"':
            j = i + 1
            while j < n:
                if text[j] == '"':
                    if j + 1 < n and text[j + 1] == '"':
                        j += 2
                        continue
                    j += 1
                    break
                j += 1
            tokens.append(text[i:j])
            i = j
        else:
            j = i + 1
            while j < n and not text[j].isspace() and text[j] not in "();":
                j += 1
            tokens.append(text[i:j])
            i = j
    return tokens


def parse_all(tokens: list[str]) -> list[object]:
    pos = 0

    def parse() -> object:
        nonlocal pos
        if pos >= len(tokens):
            raise ValueError("unexpected end of input")
        token = tokens[pos]
        pos += 1
        if token != "(":
            if token == ")":
                raise ValueError("unexpected closing parenthesis")
            return token
        result: list[object] = []
        while pos < len(tokens) and tokens[pos] != ")":
            result.append(parse())
        if pos >= len(tokens):
            raise ValueError("unclosed parenthesis")
        pos += 1
        return result

    result = []
    while pos < len(tokens):
        result.append(parse())
    return result


def sexpr(node: object) -> str:
    if isinstance(node, list):
        return "(" + " ".join(sexpr(x) for x in node) + ")"
    return str(node)


def expand_let(node: object, env: dict[str, object] | None = None) -> object:
    env = {} if env is None else env
    if isinstance(node, str):
        return env.get(node, node)
    if not isinstance(node, list) or not node:
        return node
    if node[0] == "let" and len(node) == 3 and isinstance(node[1], list):
        additions: dict[str, object] = {}
        for binding in node[1]:
            if isinstance(binding, list) and len(binding) == 2 and isinstance(binding[0], str):
                additions[binding[0]] = expand_let(binding[1], env)
        nested = dict(env)
        nested.update(additions)
        return expand_let(node[2], nested)
    # Quantifier binders shadow any same-named let variables.
    if node[0] in ("forall", "exists", "lambda") and len(node) >= 3 and isinstance(node[1], list):
        nested = dict(env)
        for binding in node[1]:
            if isinstance(binding, list) and binding and isinstance(binding[0], str):
                nested.pop(binding[0], None)
        return [node[0], node[1], *[expand_let(x, nested) for x in node[2:]]]
    return [expand_let(x, env) for x in node]


@dataclass(frozen=True)
class Lit:
    name: str
    neg: bool = False

    def flipped(self) -> "Lit":
        return Lit(self.name, not self.neg)


TRUE = object()
FALSE = object()


class Encoder:
    def __init__(self) -> None:
        self.counter = 0
        self.clauses: list[list[Lit]] = []
        self.atoms: dict[str, str] = {}

    def atom(self, node: object) -> Lit:
        raw = sexpr(node)
        name = self.atoms.get(raw)
        if name is None:
            name = f"⟦{raw}⟧"
            self.atoms[raw] = name
        return Lit(name)

    def fresh(self) -> Lit:
        self.counter += 1
        return Lit(f"τ{self.counter}")

    def add(self, *items: object) -> None:
        clause: list[Lit] = []
        seen: set[Lit] = set()
        for item in items:
            if item is TRUE:
                return
            if item is FALSE:
                continue
            assert isinstance(item, Lit)
            if item.flipped() in seen:
                return
            if item not in seen:
                clause.append(item)
                seen.add(item)
        self.clauses.append(clause)

    def encode(self, node: object) -> object:
        if node == "true":
            return TRUE
        if node == "false":
            return FALSE
        if not isinstance(node, list) or not node:
            return self.atom(node)

        op = node[0]
        args = node[1:]
        if op == "not" and len(args) == 1:
            value = self.encode(args[0])
            if value is TRUE:
                return FALSE
            if value is FALSE:
                return TRUE
            return value.flipped()
        if op == "=>" and len(args) >= 2:
            # SMT-LIB implication is right associative.
            rhs: object = args[-1]
            for lhs in reversed(args[:-1]):
                rhs = ["or", ["not", lhs], rhs]
            return self.encode(rhs)
        if op in ("and", "or"):
            values = [self.encode(arg) for arg in args]
            if op == "and":
                if any(v is FALSE for v in values):
                    return FALSE
                values = [v for v in values if v is not TRUE]
                if not values:
                    return TRUE
                if len(values) == 1:
                    return values[0]
                p = self.fresh()
                for value in values:
                    self.add(p.flipped(), value)
                self.add(p, *[value.flipped() for value in values])
                return p
            if any(v is TRUE for v in values):
                return TRUE
            values = [v for v in values if v is not FALSE]
            if not values:
                return FALSE
            if len(values) == 1:
                return values[0]
            p = self.fresh()
            for value in values:
                self.add(p, value.flipped())
            self.add(p.flipped(), *values)
            return p
        if op == "xor" and len(args) >= 2:
            value = self.encode(args[0])
            for arg in args[1:]:
                other = self.encode(arg)
                value = self.encode_xor(value, other)
            return value
        if op == "ite" and len(args) == 3:
            c, t, e = (self.encode(arg) for arg in args)
            return self.encode_ite(c, t, e)
        # Quantifiers, comparisons, equality, distinct, and theory predicates
        # remain whole theory atoms in CNF(T).
        return self.atom(node)

    def encode_xor(self, a: object, b: object) -> object:
        if a is TRUE:
            return self.negate(b)
        if b is TRUE:
            return self.negate(a)
        if a is FALSE:
            return b
        if b is FALSE:
            return a
        assert isinstance(a, Lit) and isinstance(b, Lit)
        p = self.fresh()
        self.add(a.flipped(), b.flipped(), p.flipped())
        self.add(a, b, p.flipped())
        self.add(a, b.flipped(), p)
        self.add(a.flipped(), b, p)
        return p

    @staticmethod
    def negate(value: object) -> object:
        if value is TRUE:
            return FALSE
        if value is FALSE:
            return TRUE
        assert isinstance(value, Lit)
        return value.flipped()

    def encode_ite(self, c: object, t: object, e: object) -> object:
        if c is TRUE:
            return t
        if c is FALSE:
            return e
        if t is TRUE and e is FALSE:
            return c
        if t is FALSE and e is TRUE:
            return self.negate(c)
        assert isinstance(c, Lit)
        p = self.fresh()
        # These clauses also work when a branch is a Boolean constant.
        self.add(c.flipped(), self.negate(t), p)
        self.add(c.flipped(), t, p.flipped())
        self.add(c, self.negate(e), p)
        self.add(c, e, p.flipped())
        return p

    def assert_formula(self, node: object) -> None:
        root = self.encode(expand_let(node))
        self.add(root)

    def render(self) -> str:
        if not self.clauses:
            return "⊤\n"
        if any(not clause for clause in self.clauses):
            return "⊥\n"

        def render_lit(lit: Lit) -> str:
            return ("¬" if lit.neg else "") + lit.name

        return " ∧\n".join(
            "(" + " ∨ ".join(render_lit(lit) for lit in clause) + ")"
            for clause in self.clauses
        ) + "\n"


def convert(path: Path) -> str:
    forms = parse_all(tokenize(path.read_text(encoding="utf-8")))
    encoder = Encoder()
    assertions = 0
    for form in forms:
        if isinstance(form, list) and len(form) == 2 and form[0] == "assert":
            encoder.assert_formula(form[1])
            assertions += 1
    if assertions == 0:
        raise ValueError(f"no assertions in {path}")
    return encoder.render()


def main() -> None:
    inputs = sorted(SOURCE.rglob("*.smt2"))
    if len(inputs) != 95:
        raise ValueError(f"expected 95 SMT2 inputs, found {len(inputs)}")
    for source in inputs:
        relative = source.relative_to(SOURCE).with_suffix(".md")
        destination = TARGET / relative
        if destination.exists():
            continue
        print(relative, flush=True)
        destination.parent.mkdir(parents=True, exist_ok=True)
        destination.write_text(convert(source), encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
