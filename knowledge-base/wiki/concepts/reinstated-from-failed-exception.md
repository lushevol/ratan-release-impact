---
type: concept
title: Re-Instated from Failed Exception
tags: [cashflow, exception-handling, reinstatement, swift]
related: [failed-cashflow-status, failed-cashflow-reprocessing, payment-date-override, cashflow-blotter-exception-panel-visibility, fmo-ops]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process.md"]
---
# Re-Instated from Failed Exception

`Re-Instated from Failed` is a dedicated exception created when a cashflow is reinstated from `FAILED` through Ratan.

The exception participates in multi-exception handling and is grouped with the `Back value date` exception because both update the same attribute: `Swift Value Date`.

## Required Operations Action

FMO Ops must manually update `Swift Value Date`, which is used for Swift message generation. The source gives three choices:

1. **Current System Date** — the latest business day calculated using the relevant currency calendar.
2. **Current cashflow value date**.
3. **A manually selected new date**.

The requirement does not define date validation, approval requirements, permitted date ranges, or whether the selected date is persisted as an amendment or a new cashflow version.

## Relationship to Other Exceptions

The shared Swift Value Date update explains the grouping with `Back value date`, but the source does not establish that the exceptions have identical UI behavior, ownership, priority, lifecycle, or resolution criteria. These details should be confirmed against [[cashflow-blotter-exception-panel-visibility]] and [[payment-date-override]].