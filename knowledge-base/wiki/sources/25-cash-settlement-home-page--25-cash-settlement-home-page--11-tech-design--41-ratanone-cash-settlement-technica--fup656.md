---
type: source
title: RATANONE Cash Settlement Technical Design — RATAN - Uber Integration Proposals
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [ratanone, uber, cash-settlement, technical-design, migration, scbml, json]
related: [ratan, ratan-one, ratanone-foundation, murex, fmrp, uber, scbml, uber-legacy-workflow-isolation, ratan-strategic-json-data-model, lifecycle-compatibility-api, ratan-uber-migration-options, murex-to-ratan-cashflow-integration, murex-ratan-migration-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/RATAN - Uber Integration - Proposals.md"]
---
# RATANONE Cash Settlement Technical Design — RATAN - Uber Integration Proposals

## Summary

This technical design evaluates how RATANONE and RATAN can introduce Uber-format, JSON-based cashflow processing while preserving existing Murex and SCBML processing during migration. It compares four migration options and proposes isolating the Uber workflow from the legacy workflow, with selective compatibility APIs and routing controls at lifecycle, UI, netting, orchestration, rule, scheduled-job, and SSI boundaries.

The document is a design proposal rather than an approved architecture decision. It does not provide final API contracts, ownership assignments, performance evidence, production validation, or a confirmed cutover date.

## Systems and responsibilities

- **FMRP** provides inbound groups in the evaluated flows.
- **Murex** remains an upstream source for legacy SCBML data.
- **Standardization Service** manages Murex groups, stamps cashflow attributes, and performs trade validation and confirmation control.
- **Lifecycle Service** owns status movement, persistence, and validation, and is proposed as the stable external status-update boundary.
- **Workflow and orchestration** determine business-flow routing, trigger status movement, complete user tasks, process exceptions, and handle SSI refresh subflows.
- **Camunda** is affected by message extraction changes in the smallest-change option.
- **TDSX** must enable publishing and coordinate an upstream production release before the RATAN release.
- An **EDMI topic** is an explicit UAT prerequisite.

Existing wiki context for the surrounding platform is documented in [[entities/ratan]], [[entities/ratan-one]], [[entities/ratanone-foundation]], and [[entities/ratan-cash-settlement-group-management-service]].

## Migration options

The following table is preserved from the source design.

| | Options | Flow | Standardization Service inbound (Group) | Standardization Service outbound | Effort | Risk to Current Flow | PROs | CONs |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Current BAU Flow | FMRP + Murex | SCBML | SCBML | - | - | - | - |
| 2 | Strategic RATAN Settlement Data Model principle | FMRP | UBER | Strategic RATAN data model (JSON) | **Medium** Many services to be updated | High | 1. Strategic movement in one go, single strategic data model in RATAN 2. Get rid of SCBML completely in RATAN processing flow | Higher risk on full migration, potentially impacts Murex flow. |
| Murex | SCBML |  |  |  |  |  |  |  |
| 3 | Murex flow no impact principle | FMRP | UBER | Strategic RATAN data model (JSON) | **Medium +** Effort of above option + effort of managing 2 workflows | Medium | Minimal risk for Murex flow | 1. 2 workflows to be managed 2. Both SCBML and JSON exist in Ratan data model |
| Murex | SCBML | SCBML |  |  |  |  |  |  |
| 4 | Smallest change principle | FMRP | UBER | Strategic RATAN data model (JSON), additionally add SCBML | **Small** Only change Group & Camunda msg extraction | Low | 1. Only Group Service and Camunda are mandatory and sensitive on UBER/JSON 2. All other services remain the same, support one by one migration | Duration will be long for getting rid of SCBML eventually |
| Murex | SCBML | SCBML |  |  |  |  |  |  |

Option 2 offers the most direct strategic migration but carries the highest risk to the current Murex flow. Option 3 protects Murex by operating two workflows, at the cost of sustained operational and data-model complexity. Option 4 minimizes immediate change but prolongs SCBML coexistence. The later proposal combines workflow isolation with selective compatibility rather than adopting one option without modification.

## Migration phases

| Phase | Summary | Purpose and Testing Scope |
| --- | --- | --- |
| 1 | New workflow UBER front to back process New version of all APIs | Build capability of processing UBER 1. EG, NP, SA 2. FXO |
| 2 | Integration 1. Historical SCBML data 2. Murex SCBML data | Historical data and Murex Data compatibility All entities |
| 3 | Open Search Build for extract from new data model + integration with front end |  |
| 4 | Production go live rehearsal by a clear cutover | Ensure no events lost during transition of topic |
|  |  |  |

The sequence starts with an end-to-end Uber capability, then adds historical and Murex SCBML compatibility, followed by extraction and front-end integration, and finally a controlled cutover rehearsal.

## Proposed routing model

1. **UI to Lifecycle:** Lifecycle publishes to the correct workflow.
2. **UI to Netting:** UI checks the selected cashflow booking-entity list; Uber-scope cashflows use the Netting Service V2 API. Historical Uber-scope cashflows may still carry SCBML, while the resultant should be JSON.
3. **UI to Orchestration:** UI checks booking-entity scope for single and bulk multi-exception handling. Real-time conversion to JSON is suggested for historical SCBML in Uber scope.
4. **Trade confirmation:** Rule calls Lifecycle with `Affirmed`; Lifecycle returns message type so Rule can select the appropriate flow, while Rule publishes the relevant orchestration user-task event.
5. **Scheduled jobs:** Materialize, Release, and AutoNetting rely on Lifecycle to publish to the correct workflow.
6. **SSI refresh:** Orchestration provides a new-service subflow, consumes the event, updates status, and either handles the result itself or publishes to the legacy workflow according to the status response.

## API and event behavior

The design prefers one externally consumed lifecycle API for each business action. Lifecycle should hide the choice between old and new internal APIs. This compatibility API is explicitly tactical and is expected to be removed after migration.

The live actions identified after the referenced release are:

- `NetNew`
- `Net`
- `Affirmed`
- `UnNet`
- `RevertToQueued`

The new API changes event-publishing responsibility for `NetNew` and `RevertToQueued`: Lifecycle no longer publishes to the `process_in` topic, so the domain service must publish the message. This creates additional requirements for retries, failure handling, and behavioral alignment with the legacy API.

The design also proposes keeping cashflow stamping, holding-check, and cut-off calculation APIs unchanged while the workflow remains unchanged. It notes that Group Service stamping may need to be rolled back or disabled.

## Delivery prerequisites

- EDMI topic creation was scheduled to start on `2025-08-14`.
- TDSX must enable the publisher.
- Because TDSX releases quarterly, the upstream release date must be agreed before the RATAN production release.
- The BAU all-actions delivery plan is recorded as having no plan and requiring agreement with Nick.

## Open questions

- Who owns workflow selection for single-cashflow and batch operations?
- How should operations spanning JSON and SCBML be routed?
- Does the restructured Lifecycle API support all Uber actions?
- Who owns `process_in` publishing for `NetNew` and `RevertToQueued`?
- What is the authoritative rule for historical SCBML cashflows in Uber entity scope?
- What is the approved cutover and rollback plan for preventing event loss?
- Which Group Service stamping behavior is retained, rolled back, or disabled?

## Evidence and limitations

The document provides an option comparison, integration concerns, proposed routing responsibilities, migration phases, and UAT prerequisites. It does not establish that the preferred design has been approved or validated in production. Exact message schemas, API signatures, topic names beyond `process_in` and the EDMI prerequisite, ownership matrices, test results, and production dates remain unspecified.
