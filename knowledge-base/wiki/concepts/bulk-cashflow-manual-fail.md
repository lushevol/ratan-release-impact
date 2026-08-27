---
type: concept
title: Bulk Cashflow Manual Fail
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, manual-fail, bulk-processing, cash-settlement]
related: [cash-settlement-home-page, cashflow-manual-fail-maker-checker, cashflow-pre-fail-state-restoration, fmo-ops-manual-fail-profiles, what-is-the-atomicity-model-for-bulk-manual-fail]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Bulk Fail.md"]
---
# Bulk Cashflow Manual Fail

## Definition

Bulk Cashflow Manual Fail is a controlled action that submits manual-fail requests for multiple selected cashflows in one operation. It extends the existing single-cashflow manual fail process for high-volume operational processing.

The request is capped at 1,000 selected cashflows. A selection above that limit must be rejected with an error.

## Eligibility

The `Manual Fail` action is available when:

```text
Cashflow state in ("QUEUED", "WAITING", "READY")
or
(
  Cashflow state in ("SWIFT_SUPPRESSED", "CASHFLOW_SUPPRESSED")
  and (Current Date > Payment Date)
)
```

The cashflow must also satisfy:

```text
Cashflow Sub State Type != "Pending Manual Fail"
```

The date restriction applies to the suppressed states. The source does not define the timezone or whether `Payment Date` is evaluated as a local business date or a timestamp.

## Submission transition

The maker must enter a comment. On successful submission, every selected cashflow enters:

```text
Cashflow State = "WAITING"
Cashflow Sub State Type = "Pending Manual Fail"
Cashflow Sub State = "Pending Verification"
```

The selected cashflows can have different pre-fail states. Their individual pre-fail state must be retained so that rejection can restore each item correctly.

## Approval and rejection

A checker, who must be different from the maker, can approve or reject the pending request. The checker must enter a comment.

Approval changes each approved cashflow to:

```text
Cashflow State = "FAILED"
Cashflow Sub State Type = "NA"
Cashflow Sub State = "NA"
```

Rejection returns each cashflow to its own state before manual fail. The source does not specify whether the bulk request is atomic or supports partial approval, as tracked by [[queries/what-is-the-atomicity-model-for-bulk-manual-fail]].

## Downstream behavior

The requirement explicitly states that there is no impact to the reinstate action. A cashflow that reaches `FAILED` after approval may be reinstated and resent to the main flow.

This workflow is distinct from held-cashflow reinstatement described in [[concepts/held-cashflow-reinstatement]].
