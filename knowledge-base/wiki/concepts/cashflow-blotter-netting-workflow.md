---
type: concept
title: Cashflow Blotter Netting Workflow
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-blotter, netting, operations, NSTP, auto-refresh]
related: [ratan-cashflow-blotter, netting-resultant-cashflow-lifecycle, maker-checker-settlement-control, cpn-netting, dqsl-cashflow-query-limit]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Business Scenario.md"]
---
# Cashflow Blotter Netting Workflow

The cashflow blotter is the operations interface for selecting, previewing, submitting, and reviewing netting requests in RATAN.

## Maker workflow

The Maker filters for cashflows with `Pending Netting`, verifies the proposed group with the client or operations process, selects the components, and invokes the Netting action.

The system validates:

```text
Booking Entity + Counterparty + Currency + Value Date
+ Cashflow Status not in Released or Settled
```

A `Netting Preview` must display both the selected components and the projected resultant, including direction, amount, product, currency, value date, and relevant status information. The Maker submits the request only after confirming the preview.

The example uses user `1111111` as Maker. This identifier is an example user ID, not an identified stakeholder.

## Checker workflow

The resultant is shown in a review queue with `Sub Status = Netting Review`. The Checker can open the shared `Netting ID` and inspect the underlying components before accepting or reverting the operation. The example uses user `2222222` as Checker.

Maker and Checker must have different user IDs.

## Refresh and query behavior

Changes to queried cashflows must appear automatically in the blotter without requiring a manual refresh. DQSL currently limits the number of cashflows returned in a batch query; the requirement calls for removal of that practical limitation, potentially through an unbounded or paginated result design.

The source does not define polling frequency, push-notification behavior, pagination semantics, or how a row changes while a Maker is preparing a preview.
