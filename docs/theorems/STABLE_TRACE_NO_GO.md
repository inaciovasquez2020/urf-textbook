# Stable Trace No-Go Theorem

Status: `EXTERNAL_READABLE_NOTE / REFUTED_UNCONDITIONAL_TARGET`

## Theorem

For an arbitrary URF capacity interface, the following unconditional targets are false:

```text
∀ X, StableTraceCertificateExists X
∀ X, StableGenAdmissibleTrace X
∀ X, StableGenAdmissibleTrace X → StableTraceCertificateExists X
Exact surviving statement
The valid equivalence requires inhabited traces:
[Inhabited X.Trace] →
StableGenAdmissibleTrace X ↔ StableTraceCertificateExists X
Countermodel 1: no certificate from vacuous stability
Let:
Generator := Unit
Trace := Empty
StableGen := fun _ => False
Then StableGenAdmissibleTrace holds vacuously, but StableTraceCertificateExists fails because there is no total function:
Unit → Empty
Thus:
StableGenAdmissibleTrace X → StableTraceCertificateExists X
is not valid for arbitrary CapacityInterface.
Countermodel 2: no stable admissible trace
Let:
Generator := Unit
Trace := Empty
StableGen := fun _ => True
Then StableGenAdmissibleTrace fails because the unique generator is stable but no trace exists.
Thus:
∀ X, StableGenAdmissibleTrace X
is not valid for arbitrary CapacityInterface.
Interpretation
The no-go result is credibility-positive because the framework rejects an overstrong target rather than forcing a false closure.
The correct dependency is:
[Inhabited X.Trace]
Without this dependency, a total certificate function cannot be constructed.
Formal source
This note summarizes the urf-core Lean result:
lean/URF/Foundation/UnconditionalStableTraceNoGo.lean
Merged result:
urf-core PR #341
main commit f1f28fa
Boundary
This note does not prove:
- unconditional `StableTraceCertificateExists`
- unconditional `StableGenAdmissibleTrace`
- unrestricted `UniversalFiberEntropyGap`
- unrestricted Chronos-RR
- unrestricted H4.1/FGL
- P vs NP
- any Clay problem
