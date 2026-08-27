---
type: concept
title: Failed Cashflow Re-Processing
tags: [cashflow, reprocessing, settlement-operations, exceptions]
related: [failed-cashflow-status, reinstated-from-failed-exception, cashflow-blotter-functional-scope, payment-date-override, fmo-ops]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process.md"]
---
# Failed Cashflow Re-Processing

Failed cashflows follow a separate operational flow after they are moved to `FAILED`. Settlement Ops give these cashflows additional attention and re-process them after review.

The source distinguishes this flow from ordinary exception handling: direct exception actions cannot be performed while a cashflow remains in `FAILED`. Recovery begins with the Ratan `Re-Instate` action in the Cashflow Blotter.

## Operational Sequence

1. A scheduled job or FM Ops moves the cashflow to `FAILED`.
2. Ratan exposes `Re-Instate` as the only stated direct action.
3. Reinstatement creates the `Re-Instated from Failed` exception.
4. FMO Ops handle the exception manually as part of multi-exception processing.
5. FMO Ops update `Swift Value Date` before Swift message generation.
6. The cashflow proceeds through the applicable re-processing flow.

The source does not provide the final success, failure, or accounting transitions after re-processing.

## Operational Controls

Manual movement to `FAILED` requires Maker/Checker control. The source does not state whether the same control applies to reinstatement or to the Swift Value Date update.

The referenced **Failed Re-Process - New Swift Value Date** requirement should be used to establish validation, approval, completion, and error-handling rules.