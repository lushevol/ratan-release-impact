---
type: concept
title: Multiple Cashflow Exception Handling
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, exception-handling, NSTP, cashflow-blotter, maker-checker]
related: [cash-settlement-exception-handling, partial-success-exception-resolution, exception-operation-level, cashflow-versioned-exception-orchestration, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---
# Multiple Cashflow Exception Handling

Multiple cashflow exception handling is the proposed model for resolving all applicable business exceptions for one cashflow through a single cashflow-scoped operational workflow.

## Scope

The workflow keeps exceptions in the Cashflow Blotter cashflow-detail view instead of requiring users to work from a separate exception closure interface. The combined view may include SSI, pending affirmation, back-value, netting, and NSTP exceptions.

This model is related to, but more specific than, [[concepts/cash-settlement-exception-handling]]. It defines the cashflow as the user and orchestration boundary while preserving separate exception records and statuses.

## Maker/checker control

The maker submits a set of exception fixes with one `Submit` action. The checker reviews the resulting state and uses either `Approve` or `Reject`.

Approval across multiple cashflows is prohibited because it could cause inadvertent bulk approval. The design therefore requires the workflow to be tied to a single cashflow identity and version.

## Cashflow status

The proposed cashflow-level progression is:

```text
WAITING / Pending_Operator
        ↓ maker Submit
WAITING / Pending_Verification
        ↓ checker Approve and all exceptions closed
READY
        ↓
RELEASED
        ↓
SETTLED
```

A checker rejection returns the cashflow to `WAITING / Pending_Operator`. The exact rule for deriving cashflow status from independently changing exception statuses remains to be formalized.

## Design boundary

This is a design proposal. It does not establish the authoritative state machine, transaction model, concurrency policy, or API error semantics. Those should be resolved against the existing exception-handling and adhoc SSI pages.