---
type: source
title: LIEN Processing and Pending Fixing Flag Technical Design
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page technical design"
tags: [cash-settlement, lien, pending-fixing, technical-design, lifecycle-processing]
related: [lien, lien-stamping-and-re-stamping, pending-fixing-flag-processing, lien-processing-solution-1-vs-solution-2, lifecycle-service, netting-service, rule-service, scbml, fixing-flag-notification-processing]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LIEN Processing & Pending Fixing Flag Technical Design.md"]
---

# LIEN Processing and Pending Fixing Flag Technical Design

## Summary

This technical-design note covers two related requirements in cash settlement processing:

- Obtaining the latest LIEN amount and stamping or re-stamping it on cashflows.
- Handling `PendingFixingFlag`, particularly the unresolved `WAITING + Pending Fixing` lifecycle state.

The document is an early and incomplete design artifact. Its high-level and low-level design diagram sections are empty, the data-model mapping is unpopulated, and the comparison between the proposed solutions is incomplete.

## Referenced requirements

### LIEN

- Confluence page: `RATAN Cashflow Process with Lien - Function Specs`
- ADO Story 6165570: Assessment on TDSX API latency and performance impact of cashflow processing
- ADO URL: <https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/6165570>

### PendingFixingFlag

- Confluence page: `IRS Fix Leg & Floating leg payment handling - Derivative Strategy Projects - Confluence`
- ADO Story 5967648: `Waiting Fixing Flag handling (Jan 25)`
- ADO URL: <https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/5967648>
- Technical design: `Fixing flag notification - Derivative Strategy Projects - Confluence`
- Confluence URL: <https://confluence.global.standardchartered.com/display/DSP/Fixing+flag+notification>

## Proposed solution comparison

The source proposes two approaches:

- **Solution 1:** Avoid workflow changes and perform LIEN stamping alongside other attribute stamping when the target is intended to be `QUEUED + NA + NA`. Its stated disadvantage is increased Trade Event Notification complexity.
- **Solution 2:** Simplify Trade Event Notification logic and avoid a re-stamping-only case by changing a workflow node that may be reusable in future scenarios. No disadvantages are recorded in the source.

The diagrams for both solutions are not populated, so the implementation and operational implications cannot be determined from this document alone. See [[lien-processing-solution-1-vs-solution-2]].

## Lifecycle breakpoint matrix

The following table is preserved from the source:

| SN | Breakpoint | LIEN Stamping/Re-stamping Action | Next Status |
| --- | --- | --- | --- |
| 1 | PROJECTED | Auto Materialize | QUEUED |
| 2 | QUEUED + TechFail | Reinstate | QUEUED |
| 3 | WAITING + Pending Netting | Net/RevertToQueued | NETTED/QUEUED |
| | WAITING + Pending AnotherLeg | Net/RevertToQueued | NETTED/QUEUED |
| 4 | WAITING + Pending Fixing | ?? | ?? |
| 5 | WAITING + Pending Exception | RevertToQueued | QUEUED/Ready |
| 6 | CASHFLOW_SUPPRESSED | UnSuppress | QUEUED |
| 7 | SWIFT_SUPPRESSED | ManualSwiftUnSuppress/Approve | QUEUED |
| 8 | READY+NA+NA | RevertToQueued | QUEUED |
| 9 | NETTED | UnNet | QUEUED |
| 10 | HOLD | UnHold | Nil(status roll back) |
| ~~11~~ | ~~CANCELLED~~ | | |
| ~~12~~ | ~~DEAD~~ | | |

The source uses `QUEUD` in the Solution 1 comparison but `QUEUED` throughout the matrix. `QUEUD` should be treated as a probable typo pending confirmation.

## Service changes

### `ratan-cash-settlement-netting-service`

1. Resultant generation should select the LIEN amount field from component 2.
2. The service should query the LIEN amount for each component before generating the resultant, so that the latest value is used.

This establishes a service-specific requirement to refresh LIEN immediately before resultant generation rather than relying only on an earlier stamped or cached value.

### `ratan-cashflow-lifecycle-service`

1. Change the precheck API to cover a new-event unnet withdrawal component.
2. During status updates, attempt re-stamping whenever the target status is `QUEUED`.
3. Reuse the existing DA connection to query the trade LIEN amount and stamp it onto the cashflow SCBML.

The source refers to `Cashflow Lifecycle Stamping Logic` for the detailed lifecycle behavior, but does not reproduce that design.

### `ratan-rule-service`

The source proposes adding a rule to:

1. Handle NSTP cashflows with a LIEN amount.
2. Generate LIEN on trade exceptions.

The source leaves open whether this requires a database change or user coverage change. It does not define the rule expression, precedence, or exception behavior.

## Data-model changes

The source contains an empty data-model table:

| Logical model | Xpath | Description | Change Flag |
| --- | --- | --- | --- |
| | | | |
| | | | |

No schema, XPath, API signature, event payload, or field mapping is established by this document.

## Design limitations and open issues

- The action and next status for `WAITING + Pending Fixing` are unspecified.
- The transaction boundary between status updates and LIEN stamping is unspecified.
- Failure, timeout, and retry behavior for TDSX or DA LIEN queries is unspecified.
- Idempotency and concurrency behavior for repeated re-stamping is unspecified.
- The relationship between `QUEUED`, `READY`, and `QUEUED + NA + NA` is not formally defined.
- The rollback target for `HOLD` is not given.
- No performance measurements are included despite the TDSX latency reference.
- No test cases or acceptance criteria are included.
- The ultimate selection between Solution 1 and Solution 2 is not recorded.

This source should therefore be treated as a requirements and issue-identification document, not as an authoritative implementation contract.

## Related wiki pages

- [[lien]]
- [[lien-stamping-and-re-stamping]]
- [[pending-fixing-flag-processing]]
- [[lien-processing-solution-1-vs-solution-2]]
- [[concepts/pending-fixing-and-waiting-another-leg]]
- [[concepts/fixing-flag-notification-processing]]
- [[concepts/fixing-notification-event-ordering]]
- [[entities/lifecycle-service]]
- [[entities/netting-service]]
- [[entities/rule-service]]
- [[entities/scbml]]
- [[concepts/cash-settlement-exception-handling]]