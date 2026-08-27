---
type: concept
title: Cashflow Materialization
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, materialization, lifecycle, ratan, value-date]
related: [ratan, cashflow-record, stella, cashflow-blotter, what-is-the-authoritative-ratan-cashflow-materialization-threshold-and-vd-calendar, cashflow-status-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 13 (31th Oct 2022- 11th Nov 2022).md", "Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/CN Settlement Demo Session/Sprint 14 (14th Nov 22 - 28th Nov 22).md"]
---
# Cashflow Materialization

Cashflow materialization is the documented RATAN process for transitioning an eligible individual cashflow from `Projected` to `Queued` as its payment date approaches.

## Sprint 13 Requirement

The Sprint 13 demo case specifies the following sequence:

1. A mocked Stella New message with payment date VD-7 is stored by RATAN as `Projected`.
2. The materialization job is run on VD-5.
3. RATAN changes the cashflow status to `Queued`.

This is a 2022 functional-demo requirement, not evidence of an implemented or currently authoritative operational rule.

## Sprint 14 Behavior

The Sprint 14 documentation states that:

- A cashflow received at VD-7 is stored as `Projected`.
- Running the materialization job on VD-5 changes it to `Queued`.
- Cashflows received at VD-5 or VD-4 are expected to be stored directly as `Queued`.

The Sprint 14 source does not define whether VD is measured in calendar days, business days, or another value-date convention. It also does not define the materialization job's schedule or whether it may run more than once daily.

## Unspecified Behavior

Across the documented requirements, the sources do not define:

- The meaning of VD beyond the examples given.
- Whether VD uses calendar days, business days, or another value-date convention.
- Calendar and time-zone handling.
- Processing cut-off times.
- Automatic job scheduling.
- Whether the job may run more than once daily.
- Retry behavior and failure recovery.
- Rerun idempotency.
- Treatment of dates other than the documented VD-7, VD-5, and VD-4 cases.

These gaps are tracked in [[what-is-the-authoritative-ratan-cashflow-materialization-threshold-and-vd-calendar]].