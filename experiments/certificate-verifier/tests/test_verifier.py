import importlib.util
import tempfile
import unittest
from pathlib import Path


SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "verify_certificate.py"
SPEC = importlib.util.spec_from_file_location("verify_certificate", SCRIPT)
verifier = importlib.util.module_from_spec(SPEC)
assert SPEC.loader
SPEC.loader.exec_module(verifier)


def case(declarations, cnf):
    return {"schema_version": 1, "logic": "QF_LIA", "declarations": declarations, "cnf": cnf}


def declaration(symbol, parameter_sorts=None, return_sort="Int"):
    return {"kind": "function", "symbol": symbol, "parameter_sorts": parameter_sorts or [], "return_sort": return_sort}


class VerifierTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.cvc5 = verifier.find_cvc5(None)

    def source(self, text):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        path = Path(temporary.name) / "case.smt2"
        path.write_text(text, encoding="utf-8")
        return path

    def test_sat_complete_constant_model(self):
        source = self.source("(set-logic QF_LIA)\n(declare-const x Int)\n(assert (>= x 2))\n")
        response = {"certificate": {"constants": [{"symbol": "x", "sort": "Int", "value_smt2": "2"}], "functions": []}}
        script = verifier.sat_script(case([declaration("x")], "(⟦(>= x 2)⟧)"), response, source)
        self.assertEqual(verifier.solve(self.cvc5, script, 10)["result"], "sat")

    def test_sat_rejects_partial_and_circular_models(self):
        source = self.source("(set-logic QF_LIA)\n(declare-const x Int)\n(declare-const y Int)\n(assert true)\n")
        partial = {"certificate": {"constants": [{"symbol": "x", "sort": "Int", "value_smt2": "2"}], "functions": []}}
        with self.assertRaises(verifier.VerifyError):
            verifier.sat_script(case([declaration("x"), declaration("y")], "⊤"), partial, source)
        circular = {"certificate": {"constants": [
            {"symbol": "x", "sort": "Int", "value_smt2": "y"},
            {"symbol": "y", "sort": "Int", "value_smt2": "x"}], "functions": []}}
        with self.assertRaises(verifier.VerifyError):
            verifier.sat_script(case([declaration("x"), declaration("y")], "⊤"), circular, source)

    def test_sat_rejects_command_injection(self):
        source = self.source("(set-logic QF_LIA)\n(declare-const x Int)\n(assert true)\n")
        response = {"certificate": {"constants": [{"symbol": "x", "sort": "Int", "value_smt2": "(assert false)"}], "functions": []}}
        with self.assertRaises(verifier.VerifyError):
            verifier.sat_script(case([declaration("x")], "⊤"), response, source)

    def test_term_accepts_indexed_operator_head(self):
        parsed = verifier.term("((_ to_fp 11 53) RNE 0.0)", "floating-point value")
        self.assertIsInstance(parsed, list)

    def test_unsat_core(self):
        source = self.source("(set-logic QF_LIA)\n(declare-const x Int)\n(assert true)\n")
        response = {"certificate": {"clause_indices": [1, 2]}}
        script = verifier.unsat_script(case([declaration("x")], "(⟦(> x 2)⟧) ∧\n(⟦(< x 1)⟧)"), response, source)
        self.assertEqual(verifier.solve(self.cvc5, script, 10)["result"], "unsat")

    def test_unsat_core_expands_lambda_definitions(self):
        source = self.source("(set-logic QF_LIA)\n(declare-const x Int)\n(assert true)\n")
        cnf = "(⟦(= λ1 (+ x 1))⟧) ∧\n(⟦(> λ1 3)⟧) ∧\n(⟦(< x 0)⟧)"
        response = {"certificate": {"clause_indices": [2, 3]}}
        script = verifier.unsat_script(case([declaration("x")], cnf), response, source)
        self.assertNotIn("λ1", script)
        self.assertEqual(verifier.solve(self.cvc5, script, 10)["result"], "unsat")

    def test_real_corpus_unsat_case_with_all_clauses(self):
        cnf_path = verifier.CNF_ROOT / "QF_AUFLIA" / "5a4e2f93cf-smt3150137541310906277.md"
        cnf = cnf_path.read_text(encoding="utf-8").strip()
        candidates = list((verifier.ROOT / "benchmarks" / "certificate-inputs" / "cases" / "QF_AUFLIA").glob("*.json"))
        real_case = next(verifier.load_case(path) for path in candidates if verifier.load_case(path)["cnf"].strip() == cnf)
        response = {"certificate": {"clause_indices": list(range(1, len(verifier.clauses(cnf)) + 1))}}
        source = verifier.SMT_ROOT / "QF_AUFLIA" / "5a4e2f93cf-smt3150137541310906277.smt2"
        script = verifier.unsat_script(real_case, response, source)
        self.assertEqual(verifier.solve(self.cvc5, script, 10)["result"], "unsat")


if __name__ == "__main__":
    unittest.main()
