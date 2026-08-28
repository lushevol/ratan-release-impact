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

1. Executive business verdict and confidence.
2. Business outcome, current capability, target capability, and affected scope.
3. Business gap and impact ledger, using this minimum shape:

   ```markdown
   | Business expectation | Current evidence | Gap | Business consequence | Owner/evidence needed | Status |
   |---|---|---|---|---|---|
   ```

4. Normalized current and future decision rules.
5. Ambiguities, contradictions, and explicit assumptions.
6. Current execution flow with source links.
7. Confirmed business-impact scope by capability, persona, and workflow.
8. Impacted repositories, components, APIs, tables, topics, and external systems.
9. Exact symbols and GitNexus blast radius.
10. Required code/data/config changes, clearly labeled as proposed.
11. Verification matrix and observed test results.
12. Evidence ledger: assertion, grade, evidence path/source, and limitation.
13. Analysis decision log and tool trace. Record the reproducible rationale, ordered MCP/tool calls, inputs, material outputs, transport used, and limitations. Do not expose private chain-of-thought, credentials, tokens, or unredacted private document content. Distinguish direct MCP calls from CLI calls to the same backend and state when the raw response envelope was not retained.
14. Go/no-go recommendation and evidence required to proceed.

For every path, use a specific file when one file owns the fact and a narrow wildcard when several files implement the component. For every dependency, include direction and the source that establishes it.
