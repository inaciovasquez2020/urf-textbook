# Experimental exact polynomial identity audit (v0.1)

**Status:** experimental tool / computation certificate, not Lean verification.
This is not a universal math proof checker or a replacement for independent refereeing.

Scope: universally quantified equalities between **one-variable integer-coefficient
polynomials over the real numbers**. Inputs are structured JSON, not arbitrary
LaTeX or natural language. The only permitted expression syntax is integer
literals (absolute value ≤1,000,000), `x`, `+`, `-`, `*`, parentheses, and
nonnegative literal integer powers via `**` (exponents ≤16); no division,
functions, predicates, implicit multiplication, or other variables.

The checker normalizes coefficients exactly and also evaluates the supplied
expressions through a separate AST evaluator. Let `d` be a syntactic upper bound
for the degree of `lhs-rhs`. If values match at `d+1` distinct integer points
`0,1,...,d`, the polynomial root bound proves equality for every real `x`.
Otherwise one exact unequal evaluation refutes the universal equality. The
`verify` command replays the certificate from the **original source claim**, using
exact integer evaluation and recomputing the degree bound. Resource limits are
explicit errors, never passed claims. All input is parsed by an AST whitelist;
no arbitrary Python execution is permitted.

From the `urf-textbook` root:

```sh
python3 -m unittest discover -s tests -p test_math_audit.py -v
workdir="$(mktemp -d)"
python3 tools/math_audit.py check tests/fixtures/math_audit_bad_square.json --output "$workdir/false.json"
python3 tools/math_audit.py verify "$workdir/false.json" --claim tests/fixtures/math_audit_bad_square.json
python3 tools/math_audit.py check tests/fixtures/math_audit_true_square.json --output "$workdir/true.json"
python3 tools/math_audit.py verify "$workdir/true.json" --claim tests/fixtures/math_audit_true_square.json
```

A report embeds the exact claim, its canonical SHA-256 digest, implementation
SHA-256, syntactic degree bound, integer evaluation certificate, replay method,
and classification `REFUTED` or `EXACT_CERTIFICATE_PASS`.
`EXACT_CERTIFICATE_PASS` is limited to the described polynomial setting;
`formal_kernel_verified` is always `false`. The SHA-256 checks protect against
accidental changes but are **not** authentication or signatures. Replay against
the actual claim is necessary to prevent claim substitution; independent source
review is necessary for mapping from a paper to a JSON claim. The checker's own
code is not formally verified; do not inherit a Lean theorem status from it.

No modifications to `urf-core` theorem statuses are implied. The textbook
remains a documentation surface under its `docs/status/SOURCE_OF_TRUTH_2026_04_27.md`.
This is a prototype rather than a claim to solve the general proof-checking
problem.
