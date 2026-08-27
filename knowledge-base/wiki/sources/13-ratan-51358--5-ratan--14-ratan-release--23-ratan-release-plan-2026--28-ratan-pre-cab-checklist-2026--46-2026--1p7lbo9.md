---
type: source
title: "RATAN BAU Release — Pre-Cab Checklist for 29 August 2026"
authors: []
year: 2026
url: ""
venue: ""
created: 2026-08-22
updated: 2026-08-22
tags: [RATAN, BAU-release, production-release, change-management, pre-cab-checklist]
related: [ado, servicenow, release-readiness-attestation, does-the-ratan-august-2026-release-have-complete-test-and-rollback-evidence, nstp-exception-handling, single-cashflow-auto-netting-exception, last-mile-payment-release-control, auto-netting-rule-configuration]
sources: ["RATAN - 51358/RATAN/RATAN -Release/Ratan Release Plan 2026/Ratan Pre-Cab Checklist 2026/2026_08_29_CHG1053540_Ratan BAU Release - 29th Aug.md"]
---

# RATAN BAU Release — Pre-Cab Checklist for 29 August 2026

## Summary

This source is a BPMS production-release operational-readiness questionnaire for a RATAN business-as-usual release scheduled for **29 August 2026**. The planned PSS release slot is **09:00–10:00**, within the stated maximum of two hours per change request, including implementation and verification.

The change scope contains six ADO work items spanning data lifecycle management, NSTP workflow behavior, auto-netting affirmation controls, a backend service, a database-column rename, and rule-field validation.

## Change scope

| ADO ID | Exact work-item title | Scope |
|---|---|---|
| 14766466 | `[Archival & Retrieval] production tech live phase 1` | Production technical-live Phase 1; the justification states “Drop table.” |
| 15614143 | `[Enhancement] checker reject NSTP exception but approve to ready status` | Changes checker handling of NSTP exceptions and approval to Ready status. |
| 15696109 | `[Enhancement] resultant/single cashflow won't be auto affirmed when auto netting` | Prevents automatic affirmation for the specified resultant or single cashflows when auto-netting applies. |
| 14784910 | `[Last Mile Check] Back end new service dev` | Develops a backend service for Last Mile Check. |
| 15513255 | `Rename auto_dvp_msg column trade_version to major_version` | Renames the `auto_dvp_msg` column from `trade_version` to `major_version`. |
| 15698441 | `Check rule fields before rule execute` | Adds validation of rule fields before rule execution. |

The source links the work items through the following ADO URLs:

- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14766466/
- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15614143
- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15696109
- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/14784910
- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15513255/
- https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/15698441/

## Implementation and rollback

The implementation response is:

> All ADO pipelines

The rollback response is also:

> All ADO pipelines

The questionnaire does not identify the pipeline for each story or describe story-specific rollback steps. It does not establish whether pipeline rollback includes database state, table recovery, data migration, message-contract compatibility, or restoration of consumers affected by the `trade_version` to `major_version` rename.

## Test and verification evidence

Functional test evidence is recorded as:

> in progress

The following evidence fields are blank:

- Regression test evidence
- Performance test evidence
- UAT sign-off
- DR test evidence

The UVT plan field contains no story-level details. The source therefore records release intent and scheduling, but does not demonstrate complete functional, regression, performance, UAT, DR, or UVT readiness.

## Scheduling and governance

- **Change date:** 29/08/2026
- **PSS booking:** 09:00–10:00
- **PSS constraint:** Maximum two hours per change request, including implementation and verification.
- **Safe Change status:** `SAFE`
- **Non-compliant escalation:** CRP Meeting approval is required if the Safe Change result is non-compliant.
- **Document updates:** OLA, SLA, ASRM, DOI, PSS Core Function Confluence page, and PSS Interface Confluence page are marked `NA`.
- **Monitoring:** Marked `NA`.

The source does not include supporting Safe Change Dashboard evidence, business-owner approval evidence for any out-of-greenzone work, or rationale for marking monitoring and documentation updates as not applicable.

## Operational-readiness interpretation

The release combines six technically distinct changes and should not be treated as a single undifferentiated auto-netting feature. The most material readiness risks are:

1. Recovery and retrieval for the table-drop change.
2. Compatibility and migration handling for the `auto_dvp_msg` column rename.
3. Verification of the NSTP checker and Ready-status behavior.
4. Confirmation that auto-affirmation prevention is limited to the stated resultant and single cashflows when auto-netting applies.
5. Integration and failure-path testing for the new Last Mile Check backend service.
6. Validation of invalid and incomplete rule fields before execution.
7. Reconciliation of the `SAFE` attestation with incomplete test evidence and unspecified UVT coverage.

## Source limitations and open questions

The questionnaire does not specify:

- Which table is dropped by ADO story `14766466`.
- How the dropped table can be restored or retrieved.
- Whether `trade_version` and `major_version` are database, message, API, or multiple contract fields.
- Which producers and consumers must migrate for the rename.
- The exact NSTP status transition introduced by story `15614143`.
- Additional eligibility conditions for the auto-netting affirmation restriction.
- ADO pipeline names or story-specific rollback procedures.
- The meaning and evidence location of the `SAFE` result.
- Why monitoring and operational documentation are not required.

## Related wiki context

The release extends existing knowledge about [[concepts/nstp-exception-handling]], [[concepts/single-cashflow-auto-netting-exception]], [[concepts/last-mile-payment-release-control]], and [[concepts/auto-netting-rule-configuration]]. Any updates to lifecycle or versioning pages should be made only after implementation and test evidence confirms the authoritative behavior.