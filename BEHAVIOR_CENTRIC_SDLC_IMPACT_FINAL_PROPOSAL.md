# Behavior-Centric SDLC Impact Assistant

## Final POC Solution Proposal

## 1. Executive decision

Build an advisory **Behavior-Centric SDLC Impact Assistant** for release managers.

The assistant will take a manually supplied requirement derived from an Azure DevOps work item and produce an evidence-backed candidate impact report covering:

- affected UI applications and backend services;
- provided or consumed endpoints;
- published or consumed events;
- affected database tables;
- behavior-affecting configuration, feature flags, and business rules;
- regression tests to consider;
- uncertainties and clarification questions.

The result is decision support, not an authoritative change list and not an automated release gate. Every conclusion must either cite auditable local evidence or be labeled as inferred or unknown. When the requirement cannot be mapped reliably, the assistant must return `INDETERMINATE`; it must never convert missing evidence into low risk.

The POC will introduce no new code-analysis products. It will use only:

- the existing SDLC scanner and graph artifacts;
- the existing GitNexus index for targeted code context;
- repository source, manifests, tests, configuration, and migrations;
- the local Wiki/knowledge base when relevant;
- the AI skill as an orchestrator and reasoner.

SCIP, Joern, a new graph database, live Azure DevOps integration, and runtime telemetry are explicitly excluded from the POC.

## 2. Confirmed product decisions

| Decision | POC choice |
|---|---|
| Primary user | Release manager |
| Product authority | Advisory candidate scope |
| Required granularity | UI/backend applications, endpoints, events, tables, configuration/rules, and tests |
| Requirement source | Manually supplied PO requirement derived from an ADO work item |
| Business confirmation | Placeholder confirmation state until PO/BA participation is available |
| Insufficient evidence | Return `INDETERMINATE` with focused questions |
| Runtime telemetry | Future enhancement, not a POC dependency |
| Repository scope | Four UI repositories and four backend repositories |
| Historical validation data | Not available for the POC |
| Storage | Versioned JSON/YAML/Markdown in local Git |
| Refresh model | Manual refresh before analysis |
| Behavior inputs | Code, APIs, events, tables, configuration, feature flags, and business rules |
| Priority order | Evidence explanation, test recommendation, service recall, false-positive reduction, unexplained-change detection, time reduction |

## 3. POC repository scope

### UI repositories

- `repos/mfe-base`
- `repos/mfe-cashflow-blotter`
- `repos/mfe-ratan-container`
- `repos/mfe-root-config`

### Backend repositories

- `repos/ratan-cashflow-lifecycle-service`
- `repos/ratan-cash-settlement-netting-service`
- `repos/ratan-cash-settlement-orchestration`
- `repos/ratan-cash-settlement-ssi-stamping-service`

The current scope contains React/TypeScript microfrontends and Java/Spring services. The UI includes route-level cashflow capabilities and generated OpenAPI/GraphQL clients, while the backend contains REST endpoints, Kafka interactions, SQL migrations, application configuration, and Java tests.

## 4. Problem definition

A release manager needs to answer four questions before implementation or release review:

1. What existing business behavior is the requirement trying to change?
2. Which technical contracts and state may need consideration?
3. Which existing behaviors and tests form the regression boundary?
4. Which parts of the answer are confirmed, inferred, stale, or unknown?

The system must not answer only with code proximity. It must connect a requirement to behavior and then connect that behavior to technical evidence.

The target reasoning chain is:

```text
Requirement snapshot
    -> proposed behavior delta
    -> affected scenario
    -> realizing UI/backend applications
    -> endpoints/events/tables/configuration/rules
    -> regression tests
    -> evidence and uncertainty
```

## 5. Non-goals

The POC will not:

- predict exact files that developers must edit;
- claim method-level business correctness;
- prove that an unobserved dependency does not exist;
- query Azure DevOps directly;
- ingest production OpenTelemetry data;
- act as an automated release gate;
- install or introduce another static-analysis or code-property-graph tool;
- store all GitNexus symbols inside the SDLC graph;
- build a graph database or enterprise metadata platform;
- claim statistically meaningful accuracy without historical labeled cases and PO/BA review.

## 6. Corrected architecture

```text
Manually supplied requirement
        |
        v
Requirement normalizer
  - actors, entities, actions
  - current and expected behavior
  - constraints and invariants
  - explicit unknowns
        |
        v
Behavior-delta proposal
  - placeholder-unconfirmed in POC
        |
        +-----------------------------+
        |                             |
        v                             v
Local behavior catalog          Local evidence sources
  - stable behavior IDs           - SDLC graph
  - scenarios and aliases         - GitNexus targeted context
  - current/expected states       - source and manifests
  - confirmation status           - tests and migrations
                                  - config/flags/rules
                                  - local Wiki
        |                             |
        +---------------+-------------+
                        v
               Typed impact reasoner
               - constrained paths
               - evidence aggregation
               - uncertainty/abstention
               - regression boundary
                        |
                        v
               Release impact report
               - Markdown for humans
               - JSON for automation
               - evidence paths
               - clarification questions
```

### Component responsibilities

#### Existing SDLC scanner

The scanner remains the deterministic source for application-level technical relationships. It must be enhanced, not replaced, to cover all eight repositories and the required POC granularity.

#### Existing GitNexus

GitNexus is an on-demand enrichment source. It can provide context around an already identified route, test, controller, or service symbol. It must not be the primary requirement-to-behavior matcher, and its entire symbol graph must not be copied into `graph.json`.

#### AI skill

The AI skill:

- structures requirement text;
- proposes the behavior delta;
- queries deterministic evidence;
- selects allowed graph paths;
- explains conclusions;
- recommends tests;
- asks questions or abstains when evidence is insufficient.

It does not silently create confirmed graph relationships.

## 7. Minimal canonical model

The POC should keep the graph smaller than the original target-state ontology. Only nodes required for release impact decisions should be stored.

### Node types

| Layer | Node | Purpose |
|---|---|---|
| Business | `RequirementSnapshot` | Immutable manual input and revision |
| Business | `Behavior` | Stable business capability identity |
| Business | `Scenario` | Specific behavior path or condition set |
| Architecture | `UIApplication` | React/microfrontend boundary |
| Architecture | `Service` | Backend deployable/service boundary |
| Contract | `Endpoint` | Provided or consumed REST/GraphQL operation |
| Contract | `Event` | Published or consumed message/event |
| Data | `Table` | Persisted table or view where resolvable |
| Control | `Configuration` | Behavior-affecting configuration key |
| Control | `FeatureFlag` | Explicit feature switch |
| Control | `BusinessRule` | Configured or coded rule/policy |
| Verification | `Test` | Unit, integration, contract, or UI test |

Repositories, commits, files, and line ranges remain provenance on assertions rather than graph nodes.

Classes and methods remain GitNexus/source evidence rather than first-class SDLC graph nodes in the POC.

### Canonical relationships

```text
RequirementSnapshot --PROPOSES_DELTA--> Scenario
Scenario            --SCENARIO_OF-----> Behavior
Behavior            --REALIZED_BY-----> UIApplication | Service
UIApplication       --PROVIDES--------> Endpoint
Service             --PROVIDES--------> Endpoint
UIApplication       --CALLS-----------> Endpoint
Service             --CALLS-----------> Endpoint
UIApplication       --PUBLISHES-------> Event
Service             --PUBLISHES-------> Event
UIApplication       --SUBSCRIBES_TO---> Event
Service             --SUBSCRIBES_TO---> Event
Service             --READS_FROM------> Table
Service             --WRITES_TO-------> Table
Behavior            --CONTROLLED_BY---> Configuration | FeatureFlag | BusinessRule
Test                --VERIFIES--------> Behavior | Scenario
Test                --EXERCISES-------> Endpoint | Event
```

Stored edge direction must be canonical. The reasoner may display inverse labels, but it must not turn every edge into an unrestricted bidirectional traversal.

## 8. Behavior identity and versioning

`Behavior` is a governed identity, not free text. Example:

```yaml
id: behavior:cashflow:auto-netting
name: Automatic cashflow netting
aliases:
  - auto netting
  - automatic netting
owner: placeholder-po-ba
confirmationStatus: placeholder-unconfirmed
```

Scenarios carry the state-specific detail:

```yaml
id: scenario:cashflow:auto-netting:eligible-cashflow:v1
behavior: behavior:cashflow:auto-netting
given:
  - cashflow satisfies configured netting rule
when:
  - automatic netting evaluation runs
then:
  - cashflow is assigned to the matching netting group
invariants:
  - ineligible cashflows remain ungrouped
status: placeholder-unconfirmed
```

For a new requirement, store current and expected outcomes in the immutable requirement snapshot. Do not overwrite the previous scenario definition. A later confirmed revision should use a new scenario version and a `SUPERSEDES` link or equivalent catalog metadata.

## 9. Assertion and evidence model

Confidence must not be represented as a fabricated probability. Store an assertion with explicit evidence strength and review status.

```json
{
  "assertionId": "assertion:...",
  "relationship": "CALLS",
  "source": "ui:mfe-cashflow-blotter",
  "target": "endpoint:POST:/example",
  "classification": "supported",
  "reviewStatus": "unreviewed",
  "validAt": {
    "repository": "mfe-cashflow-blotter",
    "commit": "..."
  },
  "evidence": [
    {
      "kind": "source",
      "path": "src/...",
      "startLine": 10,
      "endLine": 14,
      "extractor": "react.api-client",
      "extractorVersion": "...",
      "detail": "RTK Query operation uses POST /example"
    }
  ]
}
```

Allowed classifications:

| Classification | Meaning |
|---|---|
| `confirmed` | Explicit contract or human-confirmed mapping |
| `supported` | Deterministic repository evidence supports the assertion |
| `inferred` | Reasonable hypothesis requiring review |
| `unknown` | Evidence is missing or contradictory |
| `stale` | Evidence does not match the current baseline |

Keep these separate from:

- business impact severity;
- graph coverage;
- requirement-mapping confidence;
- overall uncertainty.

## 10. Required improvements to the existing SDLC scanner

The current scanner only promotes repositories with a valid Maven `pom.xml` into the graph. It therefore skips all four UI repositories. Its feature catalog is also keyed by the former backend directory names. These are blocking POC gaps.

### 10.1 Repository identity

Support both:

- Maven identity from `pom.xml`;
- npm identity from `package.json`.

Move repository aliases and curated feature mappings from hardcoded Python names to a versioned local configuration file.

### 10.2 React/TypeScript evidence

Without adding a new code-analysis tool, add bounded, format-aware detectors for:

- `package.json` application identity and dependencies;
- React Router route declarations;
- single-spa registration and microfrontend loading;
- RTK Query endpoint definitions;
- generated OpenAPI client operations;
- GraphQL operation documents and generated clients;
- literal `fetch`/Axios request paths where present;
- WebSocket/STOMP destinations where statically resolvable;
- environment-variable references with values redacted;
- Jest/Testing Library test files and test names.

Unsupported dynamic expressions must produce diagnostics rather than guessed edges.

### 10.3 Spring/backend evidence

Retain and improve existing extraction for:

- Spring REST endpoints;
- Feign/client calls;
- Kafka producers and consumers;
- SQL migrations;
- datasource connectivity;
- Maven dependencies.

Add bounded extraction for:

- JUnit test identities and obvious endpoint/service targets;
- scheduled jobs;
- configuration-property declarations and usages;
- feature-flag patterns configured for this repository;
- business-rule definitions and rule identifiers;
- ORM/entity-to-table mappings where explicit;
- procedures, triggers, and views in migrations;
- unresolved dynamic SQL, reflection, topics, and service discovery as diagnostics.

### 10.4 Tests

Do not label a test as verifying a business behavior merely because it is near production code.

Use two different relationships:

- `EXERCISES`: supported by direct imports, calls, endpoint fixtures, event fixtures, or coverage artifacts when available;
- `VERIFIES`: explicit tag/catalog mapping or later PO/BA/test-owner confirmation.

For the POC, most recommendations will be `EXERCISES` or `inferred VERIFIES` and must be labeled accordingly.

### 10.5 Configuration and rules

Detect keys and identifiers, not secret values. Configuration and rule evidence should record:

- declaring path;
- consuming application;
- default or environment-specific status without exposing secrets;
- whether the value is static, externally supplied, or unresolved;
- linked behavior when curated or inferred.

## 11. Requirement input contract

The POC accepts a local YAML or JSON file. No ADO API is needed.

```yaml
id: ADO-POC-001
revision: 1
title: Example requirement
source: manual-ado-derived
actor: operations-user
requirement: >-
  Requirement text supplied by the PO.
acceptanceCriteria:
  - Criterion one
currentBehavior:
  - What happens today, if known
expectedBehavior:
  - What should happen after the change
constraints:
  - Product, region, status, timing, permission, or other conditions
invariants:
  - Existing outcomes that must remain unchanged
businessCriticality: unknown
confirmationStatus: placeholder-unconfirmed
```

If current behavior, expected behavior, or material constraints are absent and the omission changes the impact boundary, the analysis must return `INDETERMINATE` with questions.

## 12. Safe impact reasoning

### 12.1 Seed selection

Map the requirement to candidate behaviors using this priority:

1. Exact behavior/scenario ID supplied in the requirement.
2. Confirmed aliases in the behavior catalog.
3. Exact business entities and actions from the local Wiki/catalog.
4. Supported endpoint, event, rule, or configuration identifiers.
5. Explicitly labeled AI inference.

The existing “at least two overlapping words” algorithm may remain only as a low-priority suggestion generator. It must not establish a match or risk level by itself.

### 12.2 Abstention rules

Return `INDETERMINATE` when any of these hold:

- no behavior or technical contract can be matched with supported evidence;
- multiple plausible behaviors produce materially different scope;
- the graph baseline is stale relative to a scoped repository;
- a required repository failed scanning;
- current versus expected behavior is materially ambiguous;
- dynamic configuration/rules are central but unresolved.

An indeterminate result may still list candidate questions and partial evidence, but must not report `LOW` impact.

### 12.3 Traversal policy

Replace generic bidirectional breadth-first search with allow-listed path templates.

Examples:

```text
Scenario -> Behavior -> REALIZED_BY -> UI/Service
UI/Service -> PROVIDES/CALLS -> Endpoint
UI/Service -> PUBLISHES/SUBSCRIBES_TO -> Event
Service -> READS_FROM/WRITES_TO -> Table
Behavior -> CONTROLLED_BY -> Config/Flag/Rule
Test -> VERIFIES -> Behavior/Scenario
Test -> EXERCISES -> Endpoint/Event
```

Traversal controls:

- preserve edge direction;
- retain every edge and its evidence in the result path;
- stop at generic libraries by default;
- do not expand from an owning service to every endpoint automatically;
- use endpoint/event/table identity to cross application boundaries;
- cap path length and high-fan-out expansion;
- place low-support paths in `possible context`, not `direct impact`;
- never infer non-impact from an absent edge.

### 12.4 Impact categories

Every result belongs to one category:

| Category | Meaning |
|---|---|
| `direct-consideration` | Evidence connects the requirement delta to this item |
| `regression-verification` | Existing behavior or consumer should be checked but may not change |
| `possible-context` | Weak or transitive evidence; review if relevant |
| `unknown` | Required relationship cannot be resolved |

Avoid the term `predictedChanges` in the POC. Use `candidateImpact` unless an actual implementation diff exists.

## 13. Risk and uncertainty

Do not calculate risk from reachable-node count alone.

### Impact severity inputs

- externally consumed endpoint or event contract;
- database write or schema change;
- shared rule, flag, or configuration;
- number and criticality of supported consumers;
- business criticality supplied in the requirement/catalog;
- absence of regression verification;
- cross-application boundary count.

### Uncertainty inputs

- behavior confirmation status;
- scanner diagnostics;
- unresolved dynamic configuration, topics, or URLs;
- stale/missing repository baseline;
- inferred rather than supported relationships;
- missing test mappings.

Report severity and uncertainty separately. Example:

```text
Impact severity: HIGH
Uncertainty: HIGH
Reason: shared event and database write are supported, but the behavior mapping
        is placeholder-unconfirmed and the topic configuration is dynamic.
```

## 14. Regression test recommendation

Test recommendation is the second-highest POC outcome after auditable explanation.

Rank tests in this order:

1. Tests explicitly mapped to the affected behavior/scenario.
2. Contract tests for affected endpoints/events.
3. Integration tests that exercise affected endpoints/events/tables.
4. UI tests for affected routes/components and API operations.
5. Unit tests for targeted GitNexus/source context.
6. Neighboring regression tests inferred from shared contracts or data.

For every recommendation include:

- why it is recommended;
- whether the link is `confirmed`, `supported`, or `inferred`;
- repository, path, and test name;
- which behavior, endpoint, event, table, rule, or configuration it covers;
- whether to execute, update, or create a test.

Do not treat test existence or code coverage as proof that the business outcome is verified.

## 15. Release-manager report contract

The human report should be ordered by the confirmed product priorities.

### 15.1 Decision summary

```text
Status: ACTIONABLE | INDETERMINATE
Impact severity: LOW | MEDIUM | HIGH | CRITICAL | UNKNOWN
Uncertainty: LOW | MEDIUM | HIGH
Baseline: scan ID and eight repository commits
Behavior confirmation: placeholder-unconfirmed
```

### 15.2 Expected behavior delta

- current behavior;
- expected behavior;
- invariants/regression boundary;
- unresolved business questions.

### 15.3 Auditable impact paths

Show complete relationship paths with evidence, not just node names.

### 15.4 Regression tests

Separate:

- execute;
- update;
- create;
- inferred recommendations requiring review.

### 15.5 Affected applications and contracts

- UI applications;
- backend services;
- endpoints;
- events;
- tables;
- configuration, feature flags, and rules.

### 15.6 Explicit non-impact boundary

Only list behaviors expected not to change when the requirement supplies an invariant or a confirmed behavioral contract supports it. Never derive this section from graph absence.

### 15.7 Unknowns and questions

List missing evidence, stale scans, dynamic values, ambiguous behavior mappings, and clarification questions.

### 15.8 Machine-readable output

Generate matching JSON for later comparison with implementation diffs.

## 16. Manual POC workflow

```text
1. Place or update all eight repositories under repos/.
2. Record each repository commit in a baseline manifest.
3. Manually refresh GitNexus.
4. Run the enhanced SDLC scanner.
5. Reject the baseline if required repositories failed or diagnostics are fatal.
6. Add a manual requirement snapshot.
7. Extract a placeholder-unconfirmed behavior delta.
8. Match the behavior and technical seeds.
9. Traverse allow-listed evidence paths.
10. Enrich only high-value targets with GitNexus/source context.
11. Recommend and classify regression tests.
12. Produce Markdown and JSON reports.
13. Release manager reviews the evidence and unknowns.
```

Every report must embed the scan ID, graph version, requirement revision, and the commit of each repository.

## 17. POC delivery phases

### Phase 0: Contracts and fixtures

Deliver:

- requirement input schema;
- behavior/scenario catalog schema;
- assertion/evidence schema;
- report schema;
- five to ten manually authored POC requirements grounded in existing repository capabilities;
- placeholder confirmation policy.

Exit criterion: the same requirement and baseline produce deterministic inputs and report structure.

### Phase 1: Eight-repository evidence baseline

Enhance the existing SDLC scanner for:

- npm/React repository identity;
- React routes and API clients;
- backend renamed repository aliases;
- endpoints and events;
- tables, views, procedures, and triggers where explicit;
- tests;
- configuration, feature flags, and rule identifiers;
- fatal versus non-fatal diagnostics.

Exit criterion: all eight repositories appear in the scan manifest, and each required evidence category reports coverage or an explicit unsupported diagnostic.

### Phase 2: Behavior mapping and safe traversal

Deliver:

- local behavior/scenario catalog;
- exact aliases and technical seed mappings;
- placeholder-unconfirmed behavior extraction;
- `INDETERMINATE` state;
- allow-listed directional traversal;
- separated severity and uncertainty.

Exit criterion: known no-match and ambiguous requirements abstain, while seeded requirements return bounded evidence paths rather than graph-wide expansion.

### Phase 3: Regression test recommendation

Deliver:

- test inventory;
- `EXERCISES` evidence;
- placeholder/inferred `VERIFIES` mappings;
- execute/update/create recommendations;
- missing-test warnings.

Exit criterion: every actionable POC report contains evidence-backed test recommendations or explicitly states why none can be supported.

### Phase 4: Release-manager report and POC evaluation

Deliver:

- final Markdown and JSON reports;
- evidence-path rendering;
- coverage and diagnostic summaries;
- manual reviewer worksheet;
- POC findings and readiness decision.

Exit criterion: a release manager can trace every conclusion to a repository path or explicit business placeholder and can identify unresolved risk without reading the full codebase.

### Phase 5: Post-change comparison, after the POC

Once real before/after examples become available:

- compare predicted candidate scope with actual graph/diff changes;
- report predicted-but-unaddressed items;
- report changed-but-unpredicted items;
- distinguish implementation choices, refactoring, and possible scope creep;
- never claim an actual behavior regression without test or runtime evidence.

## 18. POC evaluation without historical production data

Because real historical requirements, linked diffs, and PO/BA labels are unavailable, the POC must evaluate capability and evidence quality—not predictive accuracy.

### Valid POC metrics

- 100% of conclusions have evidence or an explicit inference/unknown label;
- zero no-match cases are reported as low risk;
- all eight repository commits are recorded in every baseline;
- deterministic reruns produce equivalent graph/report results;
- scanner coverage is reported for endpoints, events, tables, tests, configuration, flags, and rules;
- evidence paths preserve edge type, direction, source path, and line range;
- actionable reports remain bounded and do not expand to most of the graph;
- each recommended test has a stated rationale and evidence classification;
- unsupported dynamic relationships appear as diagnostics.

### Invalid POC claims

Do not claim:

- production precision or recall;
- behavior correctness;
- full dependency coverage;
- release-risk reduction percentage;
- analyst time savings;
- proven regression detection.

Those require real PO/BA-confirmed behaviors and historical before/after ground truth.

## 19. POC success gates

| Gate | Pass condition |
|---|---|
| Baseline integrity | All eight repositories and commits recorded; no fatal scan failure |
| Evidence integrity | Every assertion contains provenance and classification |
| Safe failure | Missing/ambiguous mappings return `INDETERMINATE` |
| Bounded scope | No unrestricted bidirectional traversal or service-to-everything expansion |
| Required coverage | Endpoints, events, tables, tests, configuration, flags, and rules covered or diagnosed |
| Test usefulness | Recommendations show execute/update/create and evidence rationale |
| Release-manager usability | Reviewer can explain why each application/contract is listed |
| Reproducibility | Same requirement revision and commit manifest reproduce the result |

Failure of a gate does not invalidate the graph; it limits which claims the assistant may make.

## 20. Suggested repository-local artifacts

```text
config/
  sdlc-graph.yaml
  repository-aliases.yaml

requirements/
  poc/
    ADO-POC-001.yaml

behavior-catalog/
  behaviors.yaml
  scenarios.yaml
  aliases.yaml
  test-mappings.yaml

graph/
  graph.json
  diagnostics.json
  scan-report.md
  snapshots/
    <scan-id>.json

reports/
  <requirement-id>/
    impact.md
    impact.json
    review.yaml
```

Raw requirements, secret configuration values, and production data must not be committed without explicit authorization. Store redacted identifiers and evidence paths only.

## 21. Future architecture

### 21.1 PO/BA confirmation

Replace `placeholder-unconfirmed` mappings with an approval workflow that records reviewer, decision, rationale, and effective version.

### 21.2 Azure DevOps integration

Fetch immutable work-item revisions, acceptance criteria, links, and associated PR/commit metadata. Preserve source ACLs and do not assume the latest work-item text represents the historical requirement.

### 21.3 Runtime telemetry

Runtime evidence is valuable but must remain optional. Add it only when services expose usable telemetry with:

- service and build version;
- environment;
- sampling policy and observation window;
- HTTP, database, and messaging semantic attributes;
- correlation across Kafka and scheduled workflows;
- privacy/redaction controls.

Store aggregate observations or trace references in the SDLC graph, not every raw span. An observed path proves occurrence for that version and window; absence of a trace never proves non-use.

### 21.4 Historical evaluation

Build a time-split, leakage-free dataset containing requirement revisions, exact multi-repository baselines, actual implementation changes, tests, and human labels. Only then measure service recall, false positives, test recommendation recall, calibration, unexpected-change usefulness, and analysis-time reduction.

### 21.5 Release integration

After evidence quality and historical evaluation are credible, add post-change comparison to release review. Automated gating should remain a separate later decision.

## 22. Principal risks and mitigations

| Risk | Mitigation |
|---|---|
| Behavior mapping appears authoritative without PO/BA | Placeholder status, visible uncertainty, no automatic promotion |
| No match incorrectly looks safe | Mandatory `INDETERMINATE` state |
| Graph expansion lists everything | Directional path templates, fan-out caps, evidence categories |
| UI repositories are omitted | npm identity and React evidence support in existing scanner |
| Tests are overclaimed | Separate `EXERCISES` from `VERIFIES` |
| Dynamic flags/rules/topics are missed | Explicit diagnostics and unknowns |
| Graph becomes stale | Manual pre-analysis refresh and commit manifest |
| GitNexus output is semantically noisy | Use only after a behavior/contract seed is established |
| Local Git contains sensitive values | Redaction, path-only evidence, repository review |
| POC overstates accuracy | Capability metrics only until historical labels exist |

## 23. Final recommendation

Proceed with the POC as an **evidence-backed release impact assistant**, not as an impact prediction engine.

The most valuable first milestone is not a larger graph. It is a trustworthy, bounded report that:

1. expresses the proposed behavior delta;
2. explains each impacted UI/service/contract/data item with evidence;
3. recommends regression tests with honest evidence classifications;
4. distinguishes impact severity from uncertainty;
5. abstains when the graph or business understanding is insufficient.

This design preserves the original behavior-centric vision while removing the highest-risk assumptions: no new analysis stack, no runtime dependency for the POC, no unrestricted reachability, no false precision, no unsafe low-risk result from missing evidence, and no accuracy claims without real business validation.
