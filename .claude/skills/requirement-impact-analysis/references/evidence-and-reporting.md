# Evidence and reporting contract

## Evidence grades

- `CONFIRMED`: directly observed in authoritative business material or exact runtime source, with a second corroborating source when the assertion spans business and code.
- `LIKELY`: multiple consistent indirect signals, but one required authoritative or runtime link is missing.
- `POSSIBLE`: semantic or naming match only; include it as a lead, not impact.
- `UNRESOLVED`: evidence is missing, contradictory, stale, or ambiguous.

Confidence in reading the current code is separate from proof that a desired behavior works.

## Proof verdicts

- `PROVEN`: the exact desired predicates have passed executable tests at appropriate layers, with observable evidence and no unresolved acceptance criterion.
- `PARTIALLY PROVEN`: some desired predicates passed, but material boundaries or integrations remain unverified.
- `NOT PROVEN`: the desired behavior is absent, tests could not execute, tests mock away the decision, or acceptance criteria remain ambiguous.

## Required report sections

1. Executive verdict and confidence.
2. Normalized current and future decision rules.
3. Ambiguities, contradictions, and explicit assumptions.
4. Current execution flow with source links.
5. Impacted repositories, components, APIs, tables, topics, and external systems.
6. Exact symbols and GitNexus blast radius.
7. Required code/data/config changes, clearly labeled as proposed.
8. Verification matrix and observed test results.
9. Evidence ledger: assertion, grade, evidence path/source, and limitation.
10. Go/no-go recommendation and evidence required to proceed.

For every path, use a specific file when one file owns the fact and a narrow wildcard when several files implement the component. For every dependency, include direction and the source that establishes it.
