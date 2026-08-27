---
type: source
title: Bulk Fail
authors: []
year: 2025
url: ""
venue: "Cash Settlement Home Page functional requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, functional-requirement, bulk-fail, manual-fail, maker-checker]
related: [cash-settlement-home-page, bulk-cashflow-manual-fail, cashflow-manual-fail-maker-checker, cashflow-pre-fail-state-restoration, fmo-ops-manual-fail-profiles, what-is-the-atomicity-model-for-bulk-manual-fail, what-is-the-authoritative-bulk-manual-fail-error-and-validation-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md"]
---
# Bulk Fail

## Summary

This functional requirement introduces bulk manual fail processing in the [[entities/cash-settlement-home-page]]. It also places the existing single-cashflow manual fail action behind maker-checker approval.

Manual fail resends a cashflow to the main flow so that workflow processing can be retriggered. The bulk capability addresses the operational cost of processing large volumes one cashflow at a time.

The requirement does not change the [[concepts/held-cashflow-reinstatement]] or other reinstate action behavior. After an approved manual fail moves a cashflow to `FAILED`, a user may still reinstate it into the main flow.

## Authorization

Bulk Fail is available to the existing manual-fail profiles:

- `FMO_OPS_BOL`
- `FMO_OPS_BOC`
- `FMO_OPS_BO`
- `FMO_OPS_INV`
- `FMO_OPS_MKR`
- `FMO_OPS_BOS`
- `FMO_OPS_BOM`

See [[entities/fmo-ops-manual-fail-profiles]] for the profile set captured by this requirement.

## Action and status rules

| Menu Item | Sub Menu | In Status | Out Status |
|---|---|---|---|
| Manual Fail |  | Cashflow state in (`"QUEUED"`, `"WAITING"`, `"READY"`) or (Cashflow state in (`"SWIFT_SUPPRESSED"`, `"CASHFLOW_SUPPRESSED"`) and (`Current Date > Payment Date`)); Cashflow Sub State Type != `"Pending Manual Fail"` | Cashflow State = `"WAITING"`; Cashflow Sub State Type = `"Pending Manual Fail"`; Cashflow Sub State = `"Pending Verification"` |
| Confirm Manual Fail | Approve | Cashflow Sub State Type = `"Pending Manual Fail"` and Cashflow Sub State = `"Pending Verification"` | Cashflow State = `"FAILED"`; Cashflow Sub State Type = `"NA"`; Cashflow Sub State = `"NA"` |
| Confirm Manual Fail | Reject | Cashflow Sub State Type = `"Pending Manual Fail"` and Cashflow Sub State = `"Pending Verification"` | Return to the state before manual fail |

The detailed eligibility condition requires `Current Date > Payment Date` for cashflows in `SWIFT_SUPPRESSED` or `CASHFLOW_SUPPRESSED`. The source's bulk scenario lists those states without repeating the date condition; the detailed action rule is the more precise statement.

## Maker-checker workflow

The maker must provide a comment before submitting either a single-cashflow or bulk manual-fail request. Submission changes each selected cashflow to:

```text
Cashflow State = "WAITING"
Cashflow Sub State Type = "Pending Manual Fail"
Cashflow Sub State = "Pending Verification"
```

A checker must provide a comment to approve or reject the request. The checker must be a different account from the maker. For the maker, `Confirm Manual Fail` is disabled and displays:

```text
For Cashflow XXX , Maker and checker cannot be the same account
```

## Business user cases

### Single cashflow in `WAITING`, checker approves

1. The cashflow is booked and hits an NSTP rule.
2. The maker submits manual fail.
3. The checker approves manual fail.
4. The user reinstates the cashflow.

The expected transitions are:

```text
WAITING / Pending Exception / Pending Operator
→ WAITING / Pending Manual Fail / Pending Verification
→ FAILED / NA / NA
→ WAITING / Pending Exception / Pending Operator
```

### Single cashflow in `READY`, checker rejects

```text
READY / NA / NA
→ WAITING / Pending Manual Fail / Pending Verification
→ READY / NA / NA
```

### Bulk fail, checker approves

Multiple eligible cashflows may originate in different states. After maker submission, each enters:

```text
WAITING / Pending Manual Fail / Pending Verification
```

After approval, each enters:

```text
FAILED / NA / NA
```

Reinstatement resends the cashflows to the main flow, where they may reach different statuses.

### Bulk fail, checker rejects

Each selected cashflow enters the pending manual-fail state after submission. On rejection, each cashflow returns to its own state before manual fail. This requires the workflow to preserve the pre-fail state independently for every cashflow.

## Selection limit

A user may select no more than 1,000 cashflows for one bulk-fail request. Selecting more than 1,000 cashflows must display an error. The supplied requirement references screenshots for the UI behavior but does not provide the exact error text in the document body.

## Scope and unresolved behavior

The requirement does not define:

- Whether checker approval is atomic for the complete bulk request or can produce partial outcomes.
- What happens if a cashflow changes status or becomes ineligible between maker submission and checker approval.
- How the original state and sub-state are persisted for rejection.
- Whether comments are stored per cashflow or once per bulk request.
- Whether the listed profiles have identical maker and checker permissions.
- Which timezone and date semantics govern `Current Date > Payment Date`.
- The exact validation message for selecting more than 1,000 cashflows.

These issues are tracked in [[queries/what-is-the-atomicity-model-for-bulk-manual-fail]] and [[queries/what-is-the-authoritative-bulk-manual-fail-error-and-validation-contract]].

## Source evidence

The source file is:

```text
Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md
```

It contains the requirement background, action matrix, business acceptance cases, and references to screenshots:

```text
attachments/image-2025-6-24_17-17-52.png
attachments/image-2025-6-24_17-34-56.png
attachments/image-2025-10-15_15-44-54.png
```
