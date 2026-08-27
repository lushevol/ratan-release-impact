---
type: concept
title: Cashflow Bulk Submit and Approve
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, cashflows, bulk-submit, bulk-approve, workflow, maker-checker, cashflow]
related: [bulk-cashflow-processing, multi-exception-bulk-eligibility, cash-settlement-home-page, confirmation-status-normalization, cashflow-hold-and-unhold, bulk-processing-for-multi-exceptions, bulk-cashflow-selection-homogeneity, bulk-exception-preview-eligibility, swift-value-date-maker-checker-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions.md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Process for Multi Exceptions/Bulk UI Technical Design.md"]
---
# Cashflow Bulk Submit and Approve

Cashflow Bulk Submit and Bulk Approve are separate, role-specific batch actions for multi-exception cashflow selections. Each action applies to a different cashflow workflow sub-state.

## Bulk Submit

The **Bulk Submit** action is the operator-side action for cashflows in:

- Cashflow state: `WAITING`
- Cashflow sub-state: `Pending Operator`
- Cashflow sub-state type: `Pending Exception`

The technical design states that Bulk Submit is available to an `Initial` user when all selected cashflows match these values.

The Bulk Submit preview includes:

- Exception and cashflow summaries.
- Ineligible exception and cashflow information.
- Affirmation details.

The cashflow summary includes:

- Trade ID
- Cashflow ID
- Counterparty
- Entity
- Currency
- Amount
- Value Date
- Pay/Receive
- Exception

After submission, a process-result view is required. The source does not define the result model, including item-level statuses, error handling, retry behavior, or audit details.

## Bulk Approve

The **Bulk Approve** action is the verification-side action for cashflows in:

- Cashflow state: `WAITING`
- Cashflow sub-state: `Pending Verification`
- Cashflow sub-state type: `Pending Exception`

The technical design states that Bulk Approve is available to a `Verify` user when all selected cashflows match these values.

The Bulk Approve preview contains the same general information as the Bulk Submit preview, with **Affirmation Email ID** added to the cashflow summary and shown separately in the affirmation information.

The source does not explicitly require a post-approval process-result view, so Bulk Approve result behavior remains unspecified.

## Common Selection Requirements

The technical design states that both actions require at least two selected cashflows. It also requires the selected cashflows to have the same values for:

- `Counterparty`
- `Booking Entity`
- `Payment Date`

The existing functional-requirement version instead states that the bulk action is disabled when selected cashflows do not share the same:

- `Counterparty`
- `Booking Entity`
- `Value Date`

This is an unresolved terminology or requirement discrepancy: the technical design specifies `Payment Date`, while the existing functional-requirement version specifies `Value Date`.

The relevant action is displayed only when all selected cashflows have the corresponding pending sub-state. The action is hidden or unavailable when the selected cashflows do not all have the required pending sub-state.

The existing functional-requirement version does not state how the interface handles a selection containing:

- Different workflow sub-states.
- Both eligible and ineligible exceptions.
- A mixture of valid and invalid cashflows.
- Cashflows that become ineligible between preview and execution.

## Approval Controls

According to the technical design, Bulk Approve has additional checker-stage controls. Approval can be blocked:

- When the current checker previously submitted the cashflow.
- When a high-risk exception lacks the required permission.
- When cashflow authorization limits are blocked.

The design does not clarify whether `Initial` and `Verify` profiles are mutually exclusive or how “submitted by current checker” is determined. See [[what-does-submitted-by-current-checker-mean-in-bulk-approval]].

## Maker/Checker Change

The solutioning section of the existing functional-requirement version proposes changing pending affirmation to maker/checker. This establishes a proposed control direction, not a complete approved state model.

Open aspects include:

- The exact maker and checker states.
- The role permitted to perform Bulk Submit.
- The role permitted to perform Bulk Approve.
- Whether the submitting user may also approve.
- The mapping from `Pending Affirmation`.
- Whether the change applies beyond bulk processing.

The proposed change should be reconciled with the authoritative confirmation and authorization model before implementation.