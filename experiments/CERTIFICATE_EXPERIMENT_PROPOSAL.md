# Certificate Experiment Proposal

## Goal

Measure two capabilities separately:

1. verdict prediction: whether the formula is `sat`, `unsat`, or `unknown`;
2. certified solving: whether the model can provide machine-checkable evidence for
   its verdict.

A benchmark is fully solved only when the verdict is correct and its certificate
passes an independent verifier. Verdict comparison is the gate: an incorrect
verdict is immediately wrong and its certificate is not checked.

## Model-visible input

Use the complete JSON value from `benchmarks/certificate-inputs/cases/`. Do not
send its opaque filename or filesystem path. The input contains only the logic,
original symbol declarations, and CNF(T) expression.

## Proposed model output

The response must be one strict JSON object with no surrounding prose.

### SAT response

```json
{
  "schema_version": 1,
  "status": "sat",
  "certificate": {
    "kind": "sat_model",
    "constants": [
      {
        "symbol": "x",
        "sort": "Int",
        "value_smt2": "2"
      }
    ],
    "functions": [
      {
        "symbol": "f",
        "parameters": [
          {"symbol": "u", "sort": "Int"}
        ],
        "return_sort": "Int",
        "body_smt2": "(ite (= u 0) 1 3)"
      }
    ]
  }
}
```

Requirements:

- every original zero-arity declaration appears exactly once in `constants`;
- every original positive-arity declaration appears exactly once in `functions`;
- values and bodies are SMT-LIB terms, not programs;
- arrays use SMT-LIB constant-array and `store` terms;
- bit-vectors preserve their widths;
- floating-point values use well-sorted SMT-LIB floating-point terms;
- function bodies are total over the declared parameter sorts;
- no undeclared helper symbol or original declared symbol may occur in a value
  or body (function bodies may reference only their own parameters and built-ins).

### UNSAT response (current experiment)

```json
{
  "schema_version": 1,
  "status": "unsat",
  "certificate": {"kind": "none"}
}
```

The scorer compares `status` with the private golden answer after the response is
final. A matching UNSAT verdict is accepted without a certificate or cvc5 call.

### UNSAT formal proof (possible future experiment)

```json
{
  "schema_version": 2,
  "status": "unsat",
  "certificate": {
    "kind": "formal_proof",
    "format": "alethe",
    "proof": "..."
  }
}
```

Phase 2 should use an independently checked proof format. Alethe is appropriate
for SMT proofs when a compatible checker is available. Pure propositional cases
may instead use LRAT. Formal-proof scores must be reported separately from
unsat-core scores.

### UNKNOWN response

```json
{
  "schema_version": 1,
  "status": "unknown",
  "certificate": {
    "kind": "none"
  }
}
```

For benchmarks whose expected result is `sat` or `unsat`, `unknown` is incorrect
and cannot be fully solved.

## SAT verifier

The verifier performs these steps without reading the expected status:

1. parse the response with a strict JSON schema;
2. reject missing, duplicate, unknown, or sort-mismatched symbols;
3. parse each `value_smt2` and `body_smt2` as exactly one SMT-LIB term;
4. reject SMT-LIB commands, file inclusion, solver options, and undeclared names;
5. create constant bindings as `(assert (= symbol value))`;
6. create function bindings as a universally quantified equality between the
   declared function application and the submitted total body;
7. append those bindings to the original SMT-LIB formula in an isolated temporary
   file and run cvc5;
8. accept the certificate only when cvc5 returns `sat` and every original symbol
   has a submitted interpretation.

The verifier must invoke cvc5 with an argument array, not a shell command. Model
text is data only and must never be executed as Python, PowerShell, a batch file,
or another program.

## UNSAT-core verifier

The verifier performs these steps without reading the expected status:

1. parse outer CNF clauses while respecting `⟦...⟧` boundaries;
2. reject zero, negative, duplicate, out-of-range, or excessive clause indices;
3. reconstruct only the selected clauses as an SMT-LIB formula;
4. declare Tseitin Boolean auxiliaries and recursively expand `λN`
   definitional auxiliaries from their unit equality clauses;
5. run cvc5 on the selected subset;
6. accept only an exact `unsat` result; treat `sat`, `unknown`, timeout, or parser
   failure as certificate failure.

The implemented verifier does not need separate `λN` sort metadata: substitution
of each definition into selected clauses preserves its SMT-LIB term and inferred
sort. Cyclic or conflicting definitions, malformed clauses, and oversized
generated scripts are rejected.

## Scoring record

Each model response produces these independent fields:

```json
{
  "verdict_correct": true,
  "certificate_present": true,
  "certificate_kind": "sat_model",
  "certificate_valid": true,
  "fully_solved": true,
  "verification_result": "sat",
  "verification_error": null
}
```

Report exactly two core metrics. SAT/UNSAT accuracy is the fraction of valid
attempts whose verdict matches the golden answer. SAT witness rate is the
fraction of correct SAT predictions whose submitted model passes cvc5. Correct
UNSAT predictions are excluded from both the numerator and denominator of SAT
witness rate. `fully_solved` remains only as a backward-compatible record field.

## Experiment separation

- use certificate solving as the only default task; do not run a separate
  status-only classification baseline;
- use a new prompt hash and experiment ID whenever certificate semantics change;
- use the same certificate output schema and verifier policy across all models;
- keep raw responses, verifier logs, verifier-generated SMT-LIB, and scored
  records in separate per-model directories;
- read the expected manifest status only after certificate verification finishes.

## Recommended delivery order

1. implement strict response schemas and the SAT verifier;
2. implement and test UNSAT-core reconstruction with recursive `λN` expansion;
3. pilot SAT witnesses on small `LIA`, `NIA`, bit-vector, and floating-point cases;
4. pilot UNSAT cores across every benchmark logic;
5. add Alethe or LRAT proof checking as a separate strong-certificate track;
6. run five independent certificate attempts per model and generate paired
   verdict-versus-certificate reports.
