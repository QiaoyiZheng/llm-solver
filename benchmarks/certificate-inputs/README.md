# Certificate experiment inputs

This directory contains model-visible, label-free inputs for certificate-based
CNF(T) evaluation.

Each case JSON contains only:

- schema version;
- SMT-LIB logic;
- structured declarations for the original symbols;
- the CNF(T) mathematical expression.

Case filenames are opaque IDs derived from the CNF content. The JSON does not
contain the case ID, original filename, source path, expected status, checksum,
source metadata, or historical result. A model runner may safely send the full
JSON value to a model.

The `tau` (`τN`) and `lambda` (`λN`) symbols in a CNF expression are conversion
auxiliaries. They are not original model symbols and are therefore not part of
the witness signature. SAT witnesses must interpret the original declarations.

Regenerate and validate all cases with:

```powershell
python benchmarks/certificate-inputs/scripts/build_inputs.py
```

The scoring side must recover the private association only after a model has
returned its response. It must never add that association to a model prompt.
