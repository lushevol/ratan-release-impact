---
type: source
title: NSTP Maker-Checker Separation From Code
authors: []
year: 2023
url: ""
venue: Internal technical design
tags: [cash-settlement, nstp, maker-checker, camunda, workflow, technical-design]
related: [nstp, camunda, camunda-based-maker-checker-workflows, nstp-maker-checker-processing, ratanone-camunda-flow-starter, cashflow-user-operation-record, statusmachine, adhoc-suppression-maker-checker-workflow, canonical-nstp-maker-checker-state-machine, cashflow-user-operation-record-schema-and-audit-policy, maker-checker-segregation-of-duties-and-authorization, nstp-maker-checker-camunda-design-approval-and-implementation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code.md"]
created: 2026-08-24
updated: 2026-08-24
---
# NSTP Maker-Checker Separation From Code

This internal technical-design proposal, targeted for 2023 Sprint 1, recommends moving NSTP and Adhoc Suppression maker-checker workflow logic out of Cash Settlement business microservices and into native Camunda workflows.

The stated architectural rationale is DDD-aligned separation of responsibilities: business services retain core business operations, while maker-checker behavior is treated as process-domain responsibility. The source is a proposal and does not confirm approval, implementation, release, or operational outcomes.

## Current-system diagnosis

The source identifies the following disadvantages in the current architecture:

1. Service integration is excessive, and domain services handle responsibilities that do not belong to them; maker and checker operations are cited as process-domain responsibilities.
2. Maker-checker behavior is hard-coded in business services and is not flexible to adjust.
3. Services are heavy and complex.

## Proposed workflow ownership

The proposal contains diagrams for an NSTP Maker-Checker Workflow and an Adhoc Suppression Maker-Checker workflow. Their detailed semantics are not extractable from the source text.

The intended design places user-operation workflow logic in Camunda. Microservices remain responsible for basic business operations and expose APIs that Camunda can call.

## Architecture comparison

|  | Current Workflow | Proposed Workflow |
| --- | --- | --- |
| Workflow Visualization | Lowly streamlined. Only main workflow can be seen, most of the Maker-Checker details are implement in code | Highly streamlined, all user operations logic can be seen in workflow |
| Code Intrusive | Intrusive. Maker-checker logic is coupling with the business code in micro-service | Non-Intrusive. Maker-Checker logic is implemented by native Camunda workflow |
| Maintainability | Hard to maintain. If Maker-Checker logic change, code should be changed accordingly and the impacts have been estimated for other logic. For Maker-Checker new requirement, it have been implement in code | Maintainable. If Maker-Checker logic change, only change the Camunda workflow, new Maker-Checker requirement can be implemented in Camunda |
| Complexity | High code complexity. | High Camunda workflow complexity. |
| Independency | Micro-service include workflow logic and business logic as well | Micro-service keeping basic business logic, workflow logic implemented by Camunda |

The source explicitly describes a trade-off rather than the elimination of complexity: high code complexity is intended to become high Camunda workflow complexity.

## Planned implementation

**Target: 2023 Sprint 1**

| Module | Changes | Estimation |
| --- | --- | ---|
| ratanone-camunda-flow-starter | adding trigger workflow with API request | 2 |
| create a maker API, this API will start a Camunda process by ratanone-camunda-flow-starter | 2 |
| create a checker API, this API will complete a checker user task | 2 |
| provide a API to save cashflow_user_operation_record | 1 |
| add table cashflow_user_operation_record, and provide CRUD functions | 2 |
| ratan-cash-settlement-orchestration | modify 1_5_Nstp_Check.bpmn, If it's a NSTP cashflow, add a sub-workflow in this diagram | 2 |
| ratan-cashflow-lifecycle-service | provide a API to update the scbml history table as Pending_Operator / NSTP_Release for Camunda calling | 1 |
| statusmachine provide a API for camunda calling | 1 |

The listed estimates total 13, but the source does not identify the estimation unit.

## Integration points

- [[ratanone-camunda-flow-starter]] is planned to trigger workflows through API requests and start Camunda processes.
- A maker API is planned to initiate a Camunda process; a checker API is planned to complete a checker user task.
- [[cashflow-user-operation-record]] is planned as a persistence and CRUD capability for user-operation records.
- [[ratan-cash-settlement-orchestration]] is planned to modify `1_5_Nstp_Check.bpmn` so NSTP cashflows invoke a sub-workflow.
- `ratan-cashflow-lifecycle-service` is planned to expose an API for Camunda to update SCBML history to `Pending_Operator` or `NSTP_Release`.
- [[statusmachine]] is planned to expose an API for Camunda.

## Limitations and open design issues

The source does not define the maker-checker state machine, approval or rejection semantics, cancellation and rework handling, duplicate-operation behavior, concurrency controls, compensation, authorization, segregation of duties, or audit-record retention.

The referenced User Operation Table is an image. No extractable SQL DDL, column definitions, keys, constraints, indexes, or retention policy are available; none should be inferred.

“Non-intrusive” should be understood as reducing workflow logic embedded in business services, not as eliminating service, API, BPMN, persistence, or data-contract changes.