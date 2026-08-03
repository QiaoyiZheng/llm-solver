# Certificate verifier

Checks model-generated SAT witnesses and UNSAT CNF cores without reading
benchmark labels. Model output is parsed strictly as data; it is never executed.

```powershell
python experiments/certificate-verifier/scripts/verify_certificate.py `
  --case benchmarks/certificate-inputs/cases/LIA/case-....json `
  --response response.json
```

The verifier automatically uses the pinned project binary under `tools/cvc5/`.
Use `--emit-smt-only --artifact generated.smt2` for structural inspection
without claiming that the certificate is valid.

