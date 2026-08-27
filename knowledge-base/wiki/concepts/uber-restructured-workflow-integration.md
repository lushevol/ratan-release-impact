---
type: concept
title: Uber Restructured Workflow Integration
created: 2026-08-24
updated: 2026-08-24
tags: [uber, cash-settlement, workflow, api-migration, integration-testing]
related: [uber, scbml, orchestration, netting-service, ssi-stamping-service, cashflow-lifecycle-state-machine-restructuring, uber-restructured-flow-vs-scbml-legacy-flow, what-is-the-authoritative-uber-lifecycle-api-routing-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
---
# Uber Restructured Workflow Integration

Uber restructured workflow integration is the migration of Uber cashflow processing and user actions from legacy, SCBML-oriented API paths to RATAN’s restructured lifecycle, orchestration, netting, and SSI-stamping flows.

## Integration requirement

Uber adoption is incomplete when any required UI or service action continues to invoke a legacy API that supports only [[scbml]]. The source identifies this risk in:

- Swift-service lifecycle calls during the maker-checker flow.
- UI-initiated bilateral netting.
- UI-initiated manual unnetting.
- Unresolved ownership and routing for the `Fail` action.

The requirement applies to the Uber integration scope documented in the source. It is not evidence that every legacy API is universally incompatible with every RATAN flow.

## Responsibilities under migration

The documented target arrangement separates responsibilities:

- [[cashflow-blotter]] invokes lifecycle APIs for direct user-status actions.
- [[orchestration]] owns submit, approval, rejection, validation, and selected workflow actions.
- [[netting-service]] owns netting, unnetting, `NetNew`, and `WaitingAnotherLeg`.
- [[ssi-stamping-service]] owns Nostro and SSI stamping.
- Rule Service evaluates suppression, NSTP, IRS, and netting rules.

Several boundaries remain unsettled, particularly publication to `process_in`, the lifecycle contract for user actions, batch-job flow selection, and ownership of `Fail`.

## Evidence and limitation

The source includes a confirmed integration observation that a `NetNew` result required manual Kafka publication, plus specific UI and legacy-API gaps. It also contains a broad test-case inventory with limited detailed execution evidence. It should therefore guide migration validation, not serve as proof of end-to-end acceptance.

See [[uber-restructured-flow-vs-scbml-legacy-flow]] for the routing contrast and [[does-netnew-automatically-publish-to-process-in-for-uber]] for the publication gap.