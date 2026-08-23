# Behavior-Centric SDLC Impact Assistant

## Final POC Solution Proposal

## 1. Executive decision

Build an advisory **Behavior-Centric SDLC Impact Assistant** for release managers.

The assistant will take a small manual trigger derived from an Azure DevOps work item, retrieve the corresponding requirements and design evidence from the existing local LLM Wiki MCP, and produce an evidence-backed candidate impact report covering:

- affected UI applications and backend services;
- provided or consumed endpoints;
- published or consumed events;
- affected database tables;
- behavior-affecting configuration, feature flags, and business rules;
- regression tests to consider;
- uncertainties and clarification questions.

The result is decision support, not an authoritative change list and not an automated release gate. Every conclusion must either cite auditable local evidence or be labeled as inferred or unknown. When the requirement cannot be mapped reliably, the assistant must return `INDETERMINATE`; it must never convert missing evidence into low risk.

The POC will introduce no new code-analysis products. It will use only:

- the existing local `llm-wiki` MCP as the primary POC interface for requirements, acceptance criteria, business rules, and design evidence;
- the existing SDLC scanner and graph artifacts;
- the existing GitNexus index for targeted code context;
- repository source, manifests, tests, configuration, and migrations;
- the checked-in `knowledge-base/wiki` only as an explicit fallback when the live Wiki is unavailable;
- the AI skill as an orchestrator and reasoner.

SCIP, Joern, a new graph database, live Azure DevOps integration, and runtime telemetry are explicitly excluded from the POC.

## 2. Confirmed product decisions

| Decision | POC choice |
|---|---|
| Primary user | Release manager |
| Product authority | Advisory candidate scope |
| Required granularity | UI/backend applications, endpoints, events, tables, configuration/rules, and tests |
| Business source | PO-authored requirement, initially identified by an ADO work-item reference |
| POC retrieval source | Local `llm-wiki` MCP project `Ratan-Settlement` (`9e1984bc-764f-4abd-b898-84ea9d8e95b9`) |
| Analysis trigger | Manual work-item reference, title, search terms, and optional pasted requirement text; no ADO API |
| Wiki fallback | Checked-in `knowledge-base/wiki`, visibly classified as `wiki-local-fallback` |
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
Manual analysis trigger
    -> LLM Wiki requirement/design evidence bundle
    -> immutable requirement snapshot
    -> proposed behavior delta
    -> affected scenario
    -> realizing UI/backend applications
    -> routes/endpoints/GraphQL/events/schemas/data/configuration/rules
    -> regression tests
    -> evidence and uncertainty
```

## 5. Non-goals

The POC will not:

- predict exact files that developers must edit;
- claim method-level business correctness;
- prove that an unobserved dependency does not exist;
- query Azure DevOps directly;
- treat an LLM Wiki answer without source references as confirmed evidence;
- ingest production OpenTelemetry data;
- act as an automated release gate;
- install or introduce another static-analysis or code-property-graph tool;
- store all GitNexus symbols inside the SDLC graph;
- build a graph database or enterprise metadata platform;
- claim statistically meaningful accuracy without historical labeled cases and PO/BA review.

## 6. Corrected architecture

```text
Manual ADO-derived analysis trigger
        |
        v
LLM Wiki MCP evidence retrieval
  - health and project selection
  - requirement and acceptance criteria
  - related design and business rules
  - source document/section references
        |
        v
Frozen Wiki evidence bundle
  - retrieval timestamp and project ID
  - item IDs, titles, paths, headings
  - live or explicit local-fallback status
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
Local behavior catalog          Technical evidence sources
  - stable behavior IDs           - SDLC graph
  - scenarios and aliases         - GitNexus targeted context
  - current/expected states       - source and manifests
  - confirmation status           - tests and migrations
                                  - config/flags/rules
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

#### Existing LLM Wiki MCP

The local `llm-wiki` MCP is the primary POC retrieval interface for business meaning. The PO remains the business authority; the Wiki supplies the accessible requirement and design record.

The configured server is:

```json
{
  "command": "node",
  "args": [
    "/Applications/LLM Wiki.app/Contents/Resources/mcp-server/dist/src/index.js"
  ]
}
```

The validated project is `Ratan-Settlement`, project ID `9e1984bc-764f-4abd-b898-84ea9d8e95b9`. The logical operations are:

- health/status and project discovery;
- `search` for requirements, concepts, features, rules, and processes;
- `get`/`context` for the authoritative matched content;
- `related` for linked requirements, designs, systems, and business concepts;
- `source` for the exact document section used as evidence;
- graph queries where the server exposes a useful relationship graph.

The current adapter already calls `llm_wiki_search`. The POC should extend the workflow contract to retain item IDs, project ID, title, source path, heading/section, retrieval time, server confidence when present, and whether the evidence came from the live MCP or local fallback.

The desktop LLM Wiki application must be running for live retrieval. If it is unavailable, the assistant may use `knowledge-base/wiki` only when the fallback contains enough cited content. Otherwise the business mapping becomes `unknown` and the result is `INDETERMINATE`. The fallback must never be presented as live Wiki evidence.

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
| Business | `RequirementSnapshot` | Immutable normalized requirement revision backed by Wiki evidence |
| Business | `AcceptanceCriterion` | Individually traceable expected outcome or constraint |
| Business | `DesignArtifact` | Wiki-hosted design page, section, decision, or process description |
| Business | `Behavior` | Stable business capability identity |
| Business | `Scenario` | Specific behavior path or condition set |
| Architecture | `UIApplication` | React/microfrontend boundary |
| Architecture | `Service` | Backend deployable/service boundary |
| Architecture | `ExternalDependency` | Out-of-scope system or unresolved service target |
| Contract | `UIRoute` | User-visible route or microfrontend activation contract |
| Contract | `Endpoint` | Provided or consumed REST operation |
| Contract | `GraphQLOperation` | Query, mutation, or subscription contract |
| Contract | `Event` | Published or consumed message/event |
| Contract | `PayloadSchema` | OpenAPI, GraphQL, JSON, Avro, or other payload shape/version |
| Data | `Table` | Persisted table; retained for compatibility with the existing graph |
| Data | `DataObject` | View, procedure, trigger, or other explicit database contract |
| Control | `Configuration` | Behavior-affecting configuration key |
| Control | `FeatureFlag` | Explicit feature switch |
| Control | `BusinessRule` | Configured or coded rule/policy |
| Verification | `Test` | Unit, integration, contract, or UI test |

Repositories, commits, files, and line ranges remain provenance on assertions rather than graph nodes.

Classes and methods remain GitNexus/source evidence rather than first-class SDLC graph nodes in the POC.

### Canonical relationships

```text
RequirementSnapshot --SUPPORTED_BY-----> DesignArtifact
RequirementSnapshot --HAS_CRITERION-----> AcceptanceCriterion
RequirementSnapshot --PROPOSES_DELTA----> Scenario
AcceptanceCriterion --CONSTRAINS--------> Scenario | Behavior
DesignArtifact      --DESCRIBES---------> Behavior | Scenario
DesignArtifact      --SPECIFIES---------> UIRoute | Endpoint | GraphQLOperation | Event | PayloadSchema | Table | DataObject | Configuration | FeatureFlag | BusinessRule
Scenario            --SCENARIO_OF-------> Behavior
Behavior            --REALIZED_BY-------> UIApplication | Service
UIApplication       --EXPOSES_ROUTE-----> UIRoute
UIRoute             --INVOKES-----------> Endpoint | GraphQLOperation
UIApplication       --PROVIDES----------> Endpoint | GraphQLOperation
Service             --PROVIDES----------> Endpoint | GraphQLOperation
UIApplication       --CALLS-------------> Endpoint | GraphQLOperation | ExternalDependency
Service             --CALLS-------------> Endpoint | GraphQLOperation | ExternalDependency
UIApplication       --PUBLISHES---------> Event
Service             --PUBLISHES---------> Event
UIApplication       --SUBSCRIBES_TO-----> Event
Service             --SUBSCRIBES_TO-----> Event
Endpoint            --USES_SCHEMA-------> PayloadSchema
GraphQLOperation    --USES_SCHEMA-------> PayloadSchema
Event               --USES_SCHEMA-------> PayloadSchema
Service             --READS_FROM--------> Table | DataObject
Service             --WRITES_TO---------> Table | DataObject
Service             --EXECUTES----------> DataObject
Behavior            --CONTROLLED_BY-----> Configuration | FeatureFlag | BusinessRule
Test                --VERIFIES----------> AcceptanceCriterion | Behavior | Scenario
Test                --EXERCISES---------> UIRoute | Endpoint | GraphQLOperation | Event | PayloadSchema | Table | DataObject
```

Stored edge direction must be canonical. The reasoner may display inverse labels, but it must not turn every edge into an unrestricted bidirectional traversal.

### Technical contract identity

Each contract type needs a deterministic identity and compatibility attributes:

| Contract | Minimum identity | Compatibility evidence |
|---|---|---|
| `UIRoute` | owning UI application + normalized route pattern | route params, guards, feature flag, lazy-loaded module |
| REST `Endpoint` | provider + HTTP method + normalized path | operation ID, request/response schema, status codes, version |
| `GraphQLOperation` | provider/client + operation type + operation name | selected fields, variables, schema/version reference |
| `Event` | broker/system + topic/destination + event type | key, headers, payload schema/version, producer/consumer |
| `PayloadSchema` | schema kind + canonical name + version/hash | required/optional fields and compatibility mode when known |
| `Table` | database/schema/table | read/write mode, columns where explicit, migration version |
| `DataObject` | database/schema/object type/name | arguments, returned shape, trigger source/target where explicit |
| `Configuration` | application + normalized key | default presence, source, environment override status; value redacted |
| `FeatureFlag` | owner/application + flag key | default state and target behavior when known; value redacted |
| `BusinessRule` | domain + stable rule ID/name | inputs, outcome, version/effective state where available |
| `Test` | repository + framework + test file + stable test name | test type, exercised contracts, confirmation status |

Dynamic or unresolved contract identities must remain diagnostic records; they must not be merged merely because display names are similar.

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
- OpenAPI request/response schema references and operation IDs;
- GraphQL operation documents, selected fields, variables, and generated clients;
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
- request/response DTO or explicit schema references;
- event type, header, key, and payload-schema references where static;
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

The POC accepts a small local YAML or JSON analysis request. No ADO API is needed. The request identifies the PO requirement and tells the assistant what to retrieve from the LLM Wiki. Pasted requirement text is an optional hint or override that must remain visibly distinct from Wiki evidence.

```yaml
analysisRequestId: impact-ADO-POC-001-r1
workItemRef: ADO-POC-001
title: Example requirement
wiki:
  server: llm-wiki
  projectId: 9e1984bc-764f-4abd-b898-84ea9d8e95b9
  projectName: Ratan-Settlement
  requirementRef: optional-wiki-item-id-or-path
  searchTerms:
    - exact domain noun
    - meaningful action phrase
manualHints:
  requirementText: optional PO-supplied text
  currentBehavior: []
  expectedBehavior: []
  constraints: []
  invariants: []
requestedMode: prediction
confirmationStatus: placeholder-unconfirmed
```

The assistant converts the analysis request and retrieved Wiki evidence into an immutable normalized `RequirementSnapshot`. That snapshot must retain:

- analysis request ID and work-item reference;
- Wiki server/project ID;
- exact retrieved Wiki item IDs, paths, headings, and retrieval time;
- live/fallback status;
- normalized requirement, acceptance criteria, current behavior, expected behavior, constraints, and invariants;
- every manual hint and whether it agrees or conflicts with Wiki content;
- placeholder confirmation status.

If current behavior, expected behavior, or material constraints remain absent after Wiki retrieval and the omission changes the impact boundary, the analysis must return `INDETERMINATE` with questions.

## 12. Safe impact reasoning

### 12.1 Seed selection

Map the requirement to candidate behaviors using this priority:

1. Exact Wiki requirement, behavior, scenario, rule, process, or design IDs and cited source sections.
2. Exact behavior/scenario ID supplied in the analysis request or retrieved design.
3. Confirmed aliases in the behavior catalog.
4. Exact business entities and actions from cited Wiki evidence.
5. Supported route, endpoint, GraphQL operation, event, schema, data object, rule, or configuration identifiers.
6. Explicitly labeled AI inference.

The existing “at least two overlapping words” algorithm may remain only as a low-priority suggestion generator. It must not establish a match or risk level by itself.

### 12.2 Abstention rules

Return `INDETERMINATE` when any of these hold:

- no behavior or technical contract can be matched with supported evidence;
- the configured Wiki project cannot be resolved and the explicit fallback is insufficient;
- Wiki results lack source paths/sections needed for business claims;
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
Requirement -> DesignArtifact -> DESCRIBES/SPECIFIES -> Behavior/Contract
Requirement -> AcceptanceCriterion -> CONSTRAINS -> Scenario/Behavior
Scenario -> Behavior -> REALIZED_BY -> UI/Service
UI -> UIRoute -> Endpoint/GraphQLOperation
UI/Service -> PROVIDES/CALLS -> Endpoint/GraphQLOperation/ExternalDependency
Endpoint/GraphQLOperation/Event -> USES_SCHEMA -> PayloadSchema
UI/Service -> PUBLISHES/SUBSCRIBES_TO -> Event
Service -> READS_FROM/WRITES_TO/EXECUTES -> Table/DataObject
Behavior -> CONTROLLED_BY -> Config/Flag/Rule
Test -> VERIFIES -> AcceptanceCriterion/Behavior/Scenario
Test -> EXERCISES -> Route/Endpoint/GraphQLOperation/Event/Schema/DataObject
```

Traversal controls:

- preserve edge direction;
- permit an inverse lookup only when an allow-listed path explicitly starts from a matched contract, rule, flag, configuration, or test; inverse lookup is not generic bidirectional traversal;
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
Wiki evidence: project ID, evidence-bundle ID, retrieval time, LIVE | LOCAL_FALLBACK | UNAVAILABLE
Behavior confirmation: placeholder-unconfirmed
```

### 15.2 Expected behavior delta

- current behavior;
- expected behavior;
- invariants/regression boundary;
- unresolved business questions.

### 15.3 Auditable impact paths

Show complete relationship paths with evidence, not just node names.

Business conclusions must cite the LLM Wiki item ID/path and section. Technical conclusions must cite graph/source evidence. A path that joins business and technical evidence must expose the mapping assertion and its classification rather than hiding the join inside model prose.

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

List missing Wiki evidence, fallback use, stale scans, dynamic values, ambiguous behavior mappings, unresolved technical contracts, and clarification questions.

### 15.8 Machine-readable output

Generate matching JSON for later comparison with implementation diffs.

## 16. Manual POC workflow

```text
1. Place or update all eight repositories under repos/.
2. Record each repository commit in a baseline manifest.
3. Manually refresh GitNexus.
4. Run the enhanced SDLC scanner.
5. Reject the baseline if required repositories failed or diagnostics are fatal.
6. Add a manual analysis request containing the ADO reference and Wiki lookup hints.
7. Check LLM Wiki health and resolve the configured project.
8. Search/retrieve the requirement, acceptance criteria, related designs, rules, and exact source sections.
9. Freeze the retrieved content as a provenance-only Wiki evidence bundle; mark live or local fallback.
10. Normalize an immutable requirement snapshot and identify conflicts with manual hints.
11. Extract a placeholder-unconfirmed behavior delta.
12. Match the behavior and technical contract seeds.
13. Traverse allow-listed evidence paths.
14. Enrich only high-value targets with GitNexus/source context.
15. Recommend and classify regression tests.
16. Produce Markdown and JSON reports.
17. Release manager reviews the evidence and unknowns.
```

Every report must embed the scan ID, graph version, requirement revision, Wiki project/evidence-bundle identity, retrieval mode/time, and the commit of each repository.

## 17. End-to-end flow contracts

In this section, a flow contract is the versioned input/output agreement between POC components. It is distinct from the product contracts discovered in the software, such as endpoints and events.

All machine-readable contracts require:

- `schemaVersion`;
- a stable record ID;
- `createdAt` in UTC;
- producer name/version;
- source baseline or retrieval identity;
- deterministic ordering where arrays are emitted;
- explicit status and diagnostics;
- no secret values.

### Contract C01: `BaselineManifest`

**Producer:** baseline preparation step

**Consumer:** SDLC scanner, GitNexus enrichment, impact reasoner, report generator

Required fields:

```yaml
schemaVersion: "1.0"
baselineId: baseline-<hash>
createdAt: <UTC timestamp>
repositories:
  - name: mfe-cashflow-blotter
    path: repos/mfe-cashflow-blotter
    ref: main
    commit: <full commit>
gitnexus:
  repository: ratan-release-impact
  indexedCommit: <commit-or-index-identity>
  status: fresh
sdlcGraph:
  expectedScannerVersion: <version>
```

Validation and failure:

- all eight scoped repositories must appear exactly once;
- missing/unknown commits or stale GitNexus status make the baseline invalid;
- nested repository commits are authoritative, not only the parent repository commit;
- baseline failure stops technical impact analysis.

### Contract C02: `AnalysisRequest`

**Producer:** release manager/PO-facing manual entry

**Consumer:** Wiki retrieval orchestrator

Required fields:

- `analysisRequestId`;
- `workItemRef`;
- title or exact search terms;
- Wiki project ID;
- requested mode (`prediction` for the POC);
- optional manual hints with their source explicitly marked.

Validation and failure:

- reject an empty request with neither reference, title, nor search terms;
- do not treat manual hints as Wiki-confirmed facts;
- the request ID and effective content must be immutable for a run.

### Contract C03: `WikiAvailability`

**Producer:** LLM Wiki adapter

**Consumer:** Wiki retrieval orchestrator and report diagnostics

Required fields:

```json
{
  "schemaVersion": "1.0",
  "server": "llm-wiki",
  "status": "LIVE | LOCAL_FALLBACK | UNAVAILABLE",
  "projectId": "9e1984bc-764f-4abd-b898-84ea9d8e95b9",
  "projectName": "Ratan-Settlement",
  "checkedAt": "...",
  "availableOperations": [],
  "diagnostics": []
}
```

Validation and failure:

- resolve the requested project before search;
- if live retrieval fails, record the error class without exposing sensitive response content;
- local fallback is a separate status, not a successful live result;
- `UNAVAILABLE` plus insufficient manual/fallback content forces `INDETERMINATE`.

### Contract C04: `WikiQuery`

**Producer:** requirement normalizer/retrieval orchestrator

**Consumer:** LLM Wiki adapter

Logical operations:

```text
status/projects -> verify server and project
search          -> discover candidate requirements/designs/rules/processes
get/context     -> retrieve authoritative matched content
related         -> retrieve linked business/design artifacts
source          -> retrieve exact evidence section
graph           -> optional related-item discovery when supported
```

Minimum search request:

```json
{
  "project_id": "...",
  "query": "exact domain nouns and meaningful action phrase",
  "top_k": 8,
  "include_content": true
}
```

Rules:

- use concise domain nouns and actions rather than repeatedly sending the full requirement;
- preserve request ID, operation, normalized query, project ID, and retrieval time;
- responses without a source item/path/section may guide further retrieval but cannot confirm a business assertion.

### Contract C05: `WikiEvidenceBundle`

**Producer:** LLM Wiki retrieval orchestrator

**Consumer:** requirement normalizer, behavior mapper, impact report

Required fields:

```yaml
schemaVersion: "1.0"
bundleId: wiki-evidence-<hash>
analysisRequestId: impact-...
projectId: 9e1984bc-764f-4abd-b898-84ea9d8e95b9
retrievalMode: live-mcp | wiki-local-fallback
retrievedAt: <UTC timestamp>
queries: []
items:
  - itemId: <server-id-if-present>
    title: <title>
    kind: requirement | acceptance-criteria | design | rule | process | concept | unknown
    sourcePath: <path-or-source-id>
    section: <heading-or-anchor>
    revision: <if-present>
    serverConfidence: <if-present>
    contentDigest: <hash>
    excerpt: <bounded evidence text>
diagnostics: []
```

Rules:

- retain bounded excerpts and references, not unrestricted Wiki dumps;
- deduplicate by stable item/source identity and content digest;
- never invent an item ID, path, heading, revision, or citation;
- preserve conflicting sources as separate items;
- do not commit sensitive Wiki content unless authorized; the bundle may contain references and hashes with report-safe excerpts.

### Contract C06: `RequirementSnapshot`

**Producer:** requirement normalizer

**Consumer:** behavior-delta extractor and report generator

Required fields:

- stable snapshot ID and work-item reference;
- Wiki evidence-bundle ID;
- normalized requirement statement;
- acceptance criteria as individually identified entries;
- actor, entities, actions, conditions, current behavior, expected behavior, constraints, and invariants;
- conflicts between manual hints and Wiki evidence;
- completeness status;
- `placeholder-unconfirmed` business confirmation.

Rules:

- every normalized statement cites one or more Wiki evidence items or is marked `manual`/`inferred`;
- current and expected behavior must not be merged into one text block;
- material contradictions or missing boundary conditions force clarification or `INDETERMINATE`.

### Contract C07: `BehaviorDeltaProposal`

**Producer:** behavior-delta extractor

**Consumer:** behavior mapper, reasoner, report generator

Required fields:

```yaml
deltaId: behavior-delta-<hash>
requirementSnapshotId: requirement-...
candidateBehaviorIds: []
candidateScenarioIds: []
current:
  outcomes: []
  sideEffects: []
expected:
  outcomes: []
  sideEffects: []
invariants: []
conditions: []
evidenceRefs: []
classification: supported | inferred | unknown
confirmationStatus: placeholder-unconfirmed
questions: []
```

Rules:

- a new behavior may be proposed without being promoted to the confirmed catalog;
- multiple materially different mappings remain separate candidates;
- an empty or ambiguous delta cannot seed a low-risk result.

### Contract C08: `BehaviorCatalogMapping`

**Producer:** local catalog plus placeholder mapper

**Consumer:** typed impact reasoner

Required fields:

- stable behavior/scenario ID;
- aliases and Wiki source references;
- technical seed IDs;
- mapping classification and review status;
- effective/superseded version metadata;
- evidence references.

Rules:

- exact IDs precede aliases; aliases precede inference;
- fuzzy text overlap is suggestion-only;
- an AI proposal cannot set `confirmed` review status;
- stale or missing target IDs are diagnostics.

### Contract C09: `SdlcScanResult`

**Producer:** enhanced existing SDLC scanner

**Consumer:** impact reasoner, GitNexus enrichment selector, report generator

Required fields:

- graph schema and scan ID;
- scanner/extractor versions;
- baseline repository/commit manifest;
- deterministically ordered nodes, relationships, and evidence assertions;
- coverage summary by repository and contract type;
- diagnostics with severity and affected scope;
- scan completion status.

Rules:

- the scan manifest must match `BaselineManifest` exactly;
- partial repository failure must not be reported as a complete graph;
- unsupported syntax yields diagnostics, never guessed relationships;
- fatal diagnostics block actionable analysis; non-fatal diagnostics raise uncertainty.

### Contract C10: `GitNexusEnrichment`

**Producer:** existing GitNexus query/context/impact operations

**Consumer:** impact reasoner and evidence reporter

Required fields:

- operation (`query`, `context`, or later `impact`);
- repository/index identity and freshness;
- exact requested concept or symbol UID;
- matched symbols/processes with file paths and lines;
- epistemic status such as exact, ambiguous, or not found;
- diagnostics.

Rules:

- enrichment starts only after a Wiki/catalog/technical seed exists;
- ambiguous symbols must be disambiguated by UID or file path;
- generic semantic-query results do not establish business mappings;
- absence of a GitNexus process does not prove absence of an execution path;
- do not persist the entire GitNexus graph into the SDLC graph.

### Contract C11: `EvidenceAssertion`

**Producer:** Wiki mapper, SDLC scanner, local catalog, GitNexus/source confirmer

**Consumer:** impact reasoner and report renderer

Required fields:

- assertion ID;
- subject, relationship, and object IDs;
- canonical direction;
- classification (`confirmed`, `supported`, `inferred`, `unknown`, or `stale`);
- review status;
- valid baseline/retrieval identity;
- one or more typed evidence references;
- producer/extractor version.

Rules:

- business evidence and technical evidence remain distinguishable;
- a business-to-technical join is its own reviewable assertion;
- no unsupported numeric probability is required;
- contradictory assertions remain visible and raise uncertainty.

### Contract C12: `ImpactPath`

**Producer:** typed impact reasoner

**Consumer:** candidate-impact classifier and report renderer

Required fields:

```json
{
  "pathId": "...",
  "seedId": "...",
  "nodes": [],
  "assertionIds": [],
  "pathTemplate": "behavior-to-contract",
  "classification": "direct-consideration | regression-verification | possible-context | unknown",
  "uncertainties": []
}
```

Rules:

- node order and assertion direction must be preserved;
- every hop must be allow-listed and evidence-bearing;
- no generic bidirectional BFS;
- truncated fan-out must be reported, not silently discarded.

### Contract C13: `CandidateImpactSet`

**Producer:** candidate-impact classifier

**Consumer:** test recommender and report generator

Required fields:

- requirement snapshot and behavior-delta IDs;
- baseline and Wiki evidence-bundle IDs;
- grouped UI applications, services, routes, endpoints, GraphQL operations, events, schemas, data objects, external dependencies, configurations, flags, and rules;
- impact category and supporting path IDs for every item;
- separated impact severity and uncertainty;
- unknowns and questions.

Rules:

- use `candidateImpact`, not `predictedChanges`;
- deduplicate by canonical technical-contract identity;
- items without a supported path belong in `possible-context` or `unknown`;
- no-match or material ambiguity yields `INDETERMINATE`.

### Contract C14: `TestRecommendationSet`

**Producer:** test recommender

**Consumer:** report generator and release manager

Required fields:

- recommendation ID;
- test identity, repository, file, and stable test name;
- action (`execute`, `update`, or `create`);
- test type;
- affected behavior/criterion/technical-contract IDs;
- rationale;
- evidence classification and path IDs;
- missing-coverage warnings.

Rules:

- `EXERCISES` and `VERIFIES` remain distinct;
- inferred verification is never presented as confirmed business coverage;
- no tests found is an explicit result, not an empty success.

### Contract C15: `DiagnosticSet`

**Producer:** every workflow component

**Consumer:** orchestrator, uncertainty calculator, report generator

Required fields:

- diagnostic ID and component;
- severity (`info`, `warning`, `error`, or `fatal`);
- code;
- affected project/repository/item/path;
- redacted detail;
- whether analysis can continue;
- suggested resolution when known.

Rules:

- diagnostics are accumulated across Wiki, scanning, GitNexus, mapping, traversal, and test recommendation;
- fatal diagnostics stop actionable reporting;
- warning/error counts alone do not determine business impact severity.

### Contract C16: `ImpactReport`

**Producer:** report generator

**Consumer:** release manager and future comparison workflow

Required outputs:

- `impact.md` for humans;
- `impact.json` with the same conclusions;
- status, severity, uncertainty, baselines, and evidence mode;
- behavior delta and confirmation status;
- auditable business-to-technical paths;
- candidate impacts;
- test recommendations;
- explicit non-impact invariants only where supported;
- diagnostics, unknowns, and questions.

Rules:

- Markdown and JSON must not contradict each other;
- every conclusion links to an evidence assertion/path;
- fallback Wiki evidence is visibly marked;
- an `INDETERMINATE` report may contain partial evidence but no reassuring low-risk conclusion.

### Contract C17: `ReleaseReviewDecision`

**Producer:** release manager

**Consumer:** local report archive and future evaluation dataset

Required fields:

- analysis/report ID;
- decision (`accepted-for-consideration`, `needs-clarification`, `rejected-evidence`, or `deferred`);
- reviewed impact items/test recommendations;
- comments and corrections;
- reviewer identity placeholder for the POC;
- review timestamp;
- PO/BA confirmation status.

Rules:

- review does not promote business mappings to PO/BA-confirmed status in the POC;
- corrections should become new versioned catalog assertions, not edits to historical reports.

### Contract C18: `ChangeComparison` (future)

**Producer:** post-change comparison workflow

**Consumer:** release review and historical evaluation

Required fields:

- before and after baseline manifests;
- predicted candidate-impact set ID;
- actual changed graph/contracts/symbol evidence;
- predicted-and-changed, predicted-but-unchanged, changed-but-unpredicted, and unresolved classifications;
- test execution or runtime evidence when behavior-change claims are made;
- reviewer disposition.

Rules:

- code differences alone prove technical change, not business regression;
- implementation alternatives and incidental refactoring require human disposition;
- comparison is outside the initial POC until suitable before/after cases exist.

### Cross-contract invariants

- IDs must remain stable within a version and never be derived from display text alone when a canonical ID exists.
- Every artifact must identify the Wiki evidence bundle and repository baseline that produced it.
- Business claims require Wiki/manual business evidence; technical claims require graph/source evidence.
- A join between business and technical evidence is an explicit assertion with its own classification.
- Live Wiki, local fallback, manual hint, deterministic extraction, GitNexus evidence, and AI inference must remain distinguishable.
- No component may silently downgrade an upstream error or ambiguity.
- Secrets, full connection strings, credentials, and unrestricted Wiki content must not enter committed artifacts.
- Contract schema changes require a schema-version change and backward-compatibility or migration decision.

## 18. POC delivery phases

### Phase 0: Contracts and fixtures

Deliver:

- LLM Wiki availability/query/evidence-bundle contracts;
- configured Wiki project identity and explicit fallback policy;
- analysis-request schema;
- requirement input schema;
- behavior/scenario catalog schema;
- assertion/evidence schema;
- report schema;
- five to ten manually authored POC requirements grounded in existing repository capabilities;
- placeholder confirmation policy.

Exit criterion: the same analysis request, Wiki evidence bundle, and repository baseline produce deterministic inputs and report structure; Wiki outage/fallback behavior is testable.

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
- Wiki concept/requirement/design-to-behavior mappings with cited source sections;
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

## 19. POC evaluation without historical production data

Because real historical requirements, linked diffs, and PO/BA labels are unavailable, the POC must evaluate capability and evidence quality—not predictive accuracy.

### Valid POC metrics

- 100% of conclusions have evidence or an explicit inference/unknown label;
- zero no-match cases are reported as low risk;
- all eight repository commits are recorded in every baseline;
- every run records the Wiki project, evidence-bundle identity, retrieval time, and live/fallback status;
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

## 20. POC success gates

| Gate | Pass condition |
|---|---|
| Baseline integrity | All eight repositories and commits recorded; no fatal scan failure |
| Business evidence integrity | Wiki project and evidence bundle recorded; every normalized business claim is cited or explicitly manual/inferred |
| Wiki failure safety | Live outage is visible; fallback is explicit; insufficient fallback returns `INDETERMINATE` |
| Evidence integrity | Every assertion contains provenance and classification |
| Safe failure | Missing/ambiguous mappings return `INDETERMINATE` |
| Bounded scope | No unrestricted bidirectional traversal or service-to-everything expansion |
| Required coverage | Endpoints, events, tables, tests, configuration, flags, and rules covered or diagnosed |
| Test usefulness | Recommendations show execute/update/create and evidence rationale |
| Release-manager usability | Reviewer can explain why each application/contract is listed |
| Reproducibility | Same requirement revision and commit manifest reproduce the result |

Failure of a gate does not invalidate the graph; it limits which claims the assistant may make.

## 21. Suggested repository-local artifacts

```text
config/
  sdlc-graph.yaml
  repository-aliases.yaml
  llm-wiki.yaml

analysis-requests/
  poc/
    impact-ADO-POC-001-r1.yaml

requirements/
  poc/
    ADO-POC-001-r1.snapshot.yaml

wiki-evidence/
  <bundle-id>.manifest.json
  # bounded excerpts only when authorized

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

Raw requirements, unrestricted Wiki content, secret configuration values, and production data must not be committed without explicit authorization. Prefer Wiki item references, sections, content digests, and bounded report-safe excerpts.

## 22. Future architecture

### 22.1 PO/BA confirmation

Replace `placeholder-unconfirmed` mappings with an approval workflow that records reviewer, decision, rationale, and effective version.

### 22.2 Azure DevOps integration

Fetch immutable work-item revisions, acceptance criteria, links, and associated PR/commit metadata. Preserve source ACLs and do not assume the latest work-item text represents the historical requirement.

### 22.3 Runtime telemetry

Runtime evidence is valuable but must remain optional. Add it only when services expose usable telemetry with:

- service and build version;
- environment;
- sampling policy and observation window;
- HTTP, database, and messaging semantic attributes;
- correlation across Kafka and scheduled workflows;
- privacy/redaction controls.

Store aggregate observations or trace references in the SDLC graph, not every raw span. An observed path proves occurrence for that version and window; absence of a trace never proves non-use.

### 22.4 Historical evaluation

Build a time-split, leakage-free dataset containing requirement revisions, exact multi-repository baselines, actual implementation changes, tests, and human labels. Only then measure service recall, false positives, test recommendation recall, calibration, unexpected-change usefulness, and analysis-time reduction.

### 22.5 Release integration

After evidence quality and historical evaluation are credible, add post-change comparison to release review. Automated gating should remain a separate later decision.

## 23. Principal risks and mitigations

| Risk | Mitigation |
|---|---|
| Behavior mapping appears authoritative without PO/BA | Placeholder status, visible uncertainty, no automatic promotion |
| Wiki MCP or desktop application is unavailable | Health contract, explicit local fallback, visible retrieval mode, `INDETERMINATE` when insufficient |
| Wiki search result lacks authoritative context | Follow with context/source retrieval; uncited results remain discovery hints |
| Wiki and manual hints disagree | Preserve both sources, report the conflict, request clarification |
| No match incorrectly looks safe | Mandatory `INDETERMINATE` state |
| Graph expansion lists everything | Directional path templates, fan-out caps, evidence categories |
| UI repositories are omitted | npm identity and React evidence support in existing scanner |
| Tests are overclaimed | Separate `EXERCISES` from `VERIFIES` |
| Dynamic flags/rules/topics are missed | Explicit diagnostics and unknowns |
| Graph becomes stale | Manual pre-analysis refresh and commit manifest |
| GitNexus output is semantically noisy | Use only after a behavior/contract seed is established |
| Local Git contains sensitive values | Redaction, path-only evidence, repository review |
| POC overstates accuracy | Capability metrics only until historical labels exist |

## 24. Final recommendation

Proceed with the POC as an **evidence-backed release impact assistant**, not as an impact prediction engine.

The most valuable first milestone is not a larger graph. It is a trustworthy, bounded report that:

1. expresses the proposed behavior delta;
2. cites the exact LLM Wiki requirement/design evidence used to understand that delta;
3. explains each impacted UI/service/contract/data item with technical evidence and an explicit business-to-technical mapping assertion;
4. recommends regression tests with honest evidence classifications;
5. distinguishes impact severity from uncertainty;
6. abstains when the Wiki, graph, or business understanding is insufficient.

This design preserves the original behavior-centric vision while removing the highest-risk assumptions: no new analysis stack, no runtime dependency for the POC, no unrestricted reachability, no false precision, no unsafe low-risk result from missing evidence, and no accuracy claims without real business validation.
