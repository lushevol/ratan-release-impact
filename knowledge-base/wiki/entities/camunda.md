---
type: entity
title: Camunda
created: 2026-08-23
updated: 2026-08-24
tags: ["workflow-engine", "ratan", "cashflow-splitting", "timeout", "workflow", "platform", "api", "cash-settlement", "bpm", "persistence", "database", "orchestration", "maker-checker", "SCBML", "camunda", "task-completion", "ratanone", "performance", "bpmn"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Manual Rounding/Api design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Camunda ER diagram and purge script.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Multi-Exception Handling - Bulk Submit Approve Reject Tech Design/Bulk Approve performance check result/bulk maker checker Performance Analysis.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
related: ["cashflow-auto-split-failure", "techfail", "is-auto-split-atomic-across-parent-and-child-cashflows", "camunda-task-bulk-amend-rounding-api", "maker-checker-rounding-workflow", "manual-rounding-amendment", "camunda-persistence-schema", "destructive-workflow-data-purge", "ratanone-schema", "postgresql", "cash-settlement-platform", "domain-owned-postgresql-schemas", "cash-settlement-data-store-requirements", "multiple-cashflow-exception-handling", "cashflow-versioned-exception-orchestration", "scbml", "ratan", "camunda-api-response", "camunda-based-maker-checker-workflows", "nstp-maker-checker-processing", "ratanone-camunda-flow-starter", "statusmachine", "camunda-task-completion-bottleneck", "bulk-exception-processing-performance", "orchestration", "camunda-task-completion-performance", "bulk-maker-checker-processing", "ratan-suspended-cashflow-rule-filtering", "ratanone-settlement-orchestration-service", "fail-open-rule-service-evaluation"]
---

# Camunda

Camunda is identified as the workflow engine for settlement orchestration in the Cash Settlement Platform. It is also referenced as a workflow engine or workflow platform in several settlement-design contexts.

The RATANONE Cash Settlement performance-test sources specifically describe Camunda as the workflow engine involved in task querying and completion for bulk maker-checker operations.

The sources below describe several distinct contexts rather than one established implementation. They do not collectively establish a single deployment architecture, production implementation, canonical Camunda interface, or general causal explanation for reported checker-completion latency.

## Proposed maker-checker roles

A separate proposal presents Camunda as the platform that would own NSTP and Adhoc Suppression maker-checker workflows. In that proposal, Camunda would:

- Initiate processes.
- Manage checker user-task completion.
- Call service APIs for lifecycle updates and status-machine operations.

This proposed responsibility is distinct from the `CamundaApiResponse` contract documented in [[camunda-api-response]].

The NSTP and Adhoc Suppression proposal is a design proposal only. It does not establish deployment topology, workflow versioning, authorization integration, task-claiming rules, error recovery, or production adoption.

The Multiple Exception Handling Design separately proposes Camunda as the workflow and orchestration platform for maker and checker tasks in cash-settlement exception resolution. According to that design, Camunda:

- Creates and tracks maker and checker user-action tasks.
- Invokes domain-service APIs for individual exception fixes.
- Receives exception statuses through `metadataList`.
- Correlates actions using cashflow identity and version fields.
- Moves the workflow between maker and checker stages based on returned exception states.

The proposed task endpoints in that source are:

```text
/v1/camunda/task/{buisnessType}/maker
/v1/camunda/task/{businessType}/checker
```

The documented business type is:

```text
nstpssi
```

### Contract concerns

The Multiple Exception Handling Design inconsistently names the request and response classes `CamundaApiRequest`, `CamundaApiResponse`, and `CamundaApiRespose`. It also proposes HTTP 500 responses for some business-state outcomes, including unresolved exceptions and missing tasks. That source states that these details require normalization before Camunda's interface can be treated as canonical.

See [[multiple-cashflow-exception-handling]] and [[cashflow-versioned-exception-orchestration]].

## Suspended-rule filtering

The SUSPENDED RULE FILTER in Ratan Tech Design identifies Camunda as the workflow-layer execution point selected for the Ratan SUSPENDED rule filter. That design places the rule check and `RATAN_SUSPENDED` update in `1_1_Cash_Settlement_Inbound.bpmn`, after group-message processing completes.

That design considers each cashflow to run as an independent Camunda process instance. It states that this reduces coupling with group-service transactions, but does not itself define idempotency, retry, compensation, or reconciliation behavior.

See [[ratan-suspended-cashflow-rule-filtering]], [[ratanone-settlement-orchestration-service]], and [[fail-open-rule-service-evaluation]].

## Persistence

The Cash Settlement Data Store Requirements document states that native Camunda persistence is required and that its tables begin with `act_`. That source does not define the deployment model, schema isolation, retention period, backup and restore requirements, or operational ownership of Camunda workflow data.

A separate Camunda ER-diagram and purge-script source identifies a Camunda-style persistence model in the `ratanone` PostgreSQL schema based on `ACT_HI_*`, `ACT_RU_*`, and `ACT_GE_*` table naming conventions. The documented table groups separate:

- Workflow history.
- Active runtime state.
- General byte-array storage.

The listed purge script would affect both completed-workflow records and in-progress workflow state.

The ER-diagram and purge-script source does not establish the Camunda version, deployment topology, application owner, workflow definitions, or which RATAN/RatanOne service administers the schema.

See [[camunda-persistence-schema]] and [[destructive-workflow-data-purge]] for the Camunda persistence schema and purge-script context.

### Performance-test persistence observations

The RATANONE Cash Settlement performance-test source records large `uat2` Camunda runtime and history tables, including:

- `ACT_RU_TASK`
- `ACT_RU_VARIABLE`
- `ACT_RU_EXECUTION`
- `ACT_HI_VARINST`
- `ACT_HI_DETAIL`
- `ACT_GE_BYTEARRAY`

The reported `w` and `W` units are not defined.

That source recommends investigating Camunda table optimization, including indexing, retention, query plans, and separation of runtime and history concerns. It states that table size alone is not sufficient evidence that persistence volume caused the observed latency.

## Cashflow splitting

The cashflow-splitting design identifies Camunda as the workflow engine used by automatic splitting. Its UAT notes spell the name “cammuda” and describe it as detecting an auto-split API timeout and moving the parent cashflow to [[techfail|TechFail]].

In induced timeout scenarios, this parent transition did not reliably indicate child disposition: children could be absent, stuck in `Queue`, or completed. The cashflow-splitting source does not establish whether Camunda retries are idempotent or whether the observed behavior is intentional.

## Manual rounding

The manual-rounding API design names Camunda as the workflow platform in the rounding-amendment path. It documents a task endpoint at `/v1/camunda/task/bulk/AmendRounding` for maker submission and checker approval or rejection of a cashflow rounding amendment.

The manual-rounding source establishes Camunda's presence in this interface, but does not document its wider deployment architecture, task model, authentication configuration, or integration with other settlement systems.

See [[camunda-task-bulk-amend-rounding-api]] and [[maker-checker-rounding-workflow]].

## Bulk maker-checker task completion

The RATANONE Cash Settlement performance-test source describes Camunda as the workflow engine underlying the checker task-completion path. Its checker endpoint is:

```text
POST /api/ratan/v2/camunda/task/NSTPSSI/checker
```

In that tested flow, the reported `taskService.complete` operation is part of the Camunda completion path. It took 4,336 ms in the detailed checker-operation breakdown, making it the largest individually measured component.

`CompleteTaskListener` runs during completion and reportedly introduces an initial 1.5-second sleep along with user-task access, SCBML message retrieval, and other operations.

The performance-test source states that Camunda task completion should be optimized separately from profile limitation validation. It proposes asynchronous completion as a possible improvement, but specifies that its effect on approval semantics, retries, duplicate submissions, and failure reporting must be defined before adoption.

### Performance-analysis findings

A separate bulk maker-checker performance-analysis source reports a broader performance trace containing:

- Camunda task lookup.
- Task completion.
- Status-update processing.
- A fixed 1.5-second sleep during task startup.
- Final task completion.

That analysis identifies Camunda completion as the leading location of residual latency after earlier database, serialization, and validation optimizations.

The same source does not prove that Camunda engine internals are the sole cause. Holding-check execution, transaction waits, event persistence, OpenSearch handling, and downstream operations may occur within or around the completion path.

#### Observed timings

The bulk maker-checker performance-analysis source reports:

- Three bad-performance examples completing in **9,518–10,239 ms**.
- A common example completing in **3,408 ms**.
- Camunda task-table query time improving from approximately **1,600 ms** to **1–2 ms** after index optimization.

These timings are reported by that performance-analysis source and should not be treated as interchangeable with the separate 4,336 ms `taskService.complete` measurement.

#### Investigation boundary

Camunda engine time should be separated from:

- The intentional or workaround-related `sleep 1.5s`.
- Holding-check execution, reported as taking 1–6 seconds.
- Database locking and transaction waits.
- Domain-event insertion and publication.
- `handleDomainEventForOpenSearch`.
- Application-level orchestration and lifecycle service calls.

See [[camunda-task-completion-performance]] for the unresolved critical-path analysis.

## Source boundaries

The Camunda-related claims in this page come from separate documents:

- The Cash Settlement Data Store Requirements source describes a native Camunda persistence requirement.
- The ER-diagram and purge-script source describes Camunda-style tables and purge behavior in the `ratanone` schema.
- The cashflow-splitting source describes automatic-splitting timeout behavior.
- The manual-rounding source describes the bulk rounding-amendment task endpoint.
- The Multiple Exception Handling Design proposes maker-checker exception orchestration and documents interface concerns.
- The NSTP Maker-Checker Separation From Code source proposes Camunda ownership of NSTP and Adhoc Suppression maker-checker workflows.
- The SUSPENDED RULE FILTER in Ratan Tech Design selects Camunda as the execution point for suspended-rule filtering in `1_1_Cash_Settlement_Inbound.bpmn`.
- The RATANONE Cash Settlement performance-test source reports measured checker task-completion timing, listener activity, and `uat2` table-size observations.
- The bulk maker-checker performance-analysis source reports end-to-end examples, task-table query improvements, and an investigation boundary for the remaining latency.

Together, these sources establish Camunda's recurring role in proposed and analyzed settlement workflows, but they do not establish one unified deployment topology, one canonical API contract, or a single proven cause for all observed performance and timeout behavior.