# Test Engine POC Operating Model

## Role

The test engine is the executable behavior evidence source for the CCIL and
ReBook POC. It has three responsibilities:

1. Preserve the currently accepted local simulation as a before-change baseline.
2. Execute selected scenarios and record the observed results.
3. Support reviewed creation or modification of scenarios for requirement and design changes.

It does not depend on live authentication, APIs, databases, or Kafka. Those
boundaries remain mocked for the POC.

## Evidence Authority

Every successful run is classified as `observed_in_test_engine_simulation`.
It demonstrates behavior inside the versioned local model, not behavior in an
integrated environment or production. Missing coverage and mocked boundaries
remain explicit unknowns.

The POC evidence hierarchy is:

1. `observed_in_production`
2. `observed_in_integrated_test_environment`
3. `observed_in_test_engine_simulation`
4. `supported_by_source`
5. `inferred`
6. `unknown`

Only the third level is produced by this POC test engine.

## Ownership

For the POC, the project owner reviews and approves mappings from a test case to
a business behavior, scenario, or acceptance criterion. In the target operating
model, QA owns this approval.

A test can `EXERCISE` a technical contract based on executable evidence. It can
only `VERIFY` a business behavior after the owner approves the mapping.

## SDLC Lifecycle

Before implementation:

1. Normalize the requirement and proposed behavior delta.
2. Select affected CCIL or ReBook scenarios.
3. Run those scenarios against the current test-engine commit.
4. Store the results as the before-change baseline.
5. Identify tests to execute, update, create, or review.

After implementation or model updates:

1. Run the same baseline scenario set.
2. Run approved new or modified scenarios.
3. Compare before and after results by stable test identity.
4. Classify preserved behavior, intended change, candidate regression, missing coverage, and inconclusive results.
5. Attach the comparison to the SDLC impact report as simulation evidence.

## Artifact Contract

The behavior catalog is stored in `catalog/behaviors.json`,
`catalog/scenarios.json`, and `catalog/test-mappings.json`. Catalog validation is
required before an evidence run.

Each `run.json` records:

- change ID and `before` or `after` phase;
- test-engine commit, dirty state, and source fingerprint;
- stable test, behavior, and scenario identities;
- test status and requirement references;
- evidence mode and mocked boundaries;
- mapping approval and diagnostics.

`comparison.json` classifies preserved behavior, candidate simulation
regressions, recovered baselines, new target observations, missing tests, and
inconclusive results. `impact-fragment.md` is the human-readable verification
matrix for inclusion in the requirement impact report.

The comparison always leaves `production_proof_verdict=NOT_PROVEN` because the
POC does not execute production repository code.

Test creation or modification requires review of the expected outcome before a
new passing result can be treated as accepted current simulation behavior.

## POC Boundary

- Domains: CCIL Netting and ReBook only.
- Execution mode: local simulation only.
- Required execution points: before and after the change.
- POC mapping approver: project owner.
- Target mapping owner: QA.
- Release posture: advisory evidence, not an automated release gate.
