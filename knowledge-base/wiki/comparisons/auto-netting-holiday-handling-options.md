---
type: comparison
title: Auto Netting Holiday Handling Options
tags: [auto-netting, holidays, weekends, business-calendar, operational-fallback]
related: [auto-netting-datetime-calculation, business-calendar-relative-netting-time, cashflow-auto-netting, manual-cashflow-netting, what-is-the-authoritative-auto-netting-cutoff-time-semantics]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Datetime Calculation.md"]
---

# Auto Netting Holiday Handling Options

## Context

The source reports that the same `VD-1 5AM` configuration produces `2025-11-11 5:00` for XAU and `2025-11-10 5:00` for USD when 2025-11-11 is a USD holiday. It discusses several possible responses but records no final decision.

## Option comparison

| Option | Datetime calculation | Processing implication | Benefits | Risks or unresolved points |
| --- | --- | --- | --- | --- |
| Skip weekends and currency holidays | Move the calculated datetime to the preceding eligible currency business day | The job can target a non-holiday date if it runs on that date | Aligns the target with the currency calendar | Can create different batches for currencies sharing a payment date; may cause early processing |
| Skip weekends only | Retain a holiday as the calculated datetime | Requires the job to run on holidays or Operations to process manually | Directly addresses the reported XAU/USD date discrepancy | The source does not confirm holiday job availability; manual fallback must be explicit |
| Calculate on holidays with manual fallback | Retain the holiday datetime and route missed processing to Operations | Operations manually nets cashflows when the job is unavailable | Separates calculation policy from operational availability | Requires ownership, alerts, controls, and a clear handoff |
| Configure a later netting datetime | Move the configured offset or time later when late arrivals are expected | More cashflows may be available before the job starts | Simple operational mitigation | Configuration-dependent; does not resolve unavoidable late arrivals |
| Route post-datetime cashflows to manual netting | Keep the original calculation and assign late cashflows to `Pending Manual Net` | Users process late cashflows outside auto netting | Explicit and controlled exception path | Requires a canonical state, user workflow, and reconciliation controls |
| Automatically net post-datetime cashflows | Keep the original calculation and allow a later automated run | Late cashflows remain in an automated channel | Reduces manual work and supports later arrivals | Requires clear batch boundaries, idempotency, and scheduling rules |

## Decision status

No option is authoritative based on this source. The source presents “skip weekends, not holiday” as a proposed solution and records manual processing as an acceptable operational fallback, but it does not confirm implementation or approval.

## Questions requiring resolution

1. Does the auto-netting job execute on currency holidays?
2. If it does not, is manual processing mandatory when the calculated datetime is a holiday?
3. Is holiday handling configured globally, per currency, per product, or per netting rule?
4. Does a late-arriving cashflow enter `Pending Manual Net`, `Pending Netting`, or `Pending Auto Netting`?
5. Are cashflows arriving during job execution included in the current batch or deferred?
6. After withdrawal from a resultant, should remaining cashflows be eligible for immediate replacement netting or only the next scheduled run?

## Related lifecycle example

The source illustrates `N1` becoming `DEAD` after withdrawal of `C1`, with `C1` becoming `CANCELLED`. Remaining cashflows `C2` and `C3`, together with new cashflow `C4`, are then shown either in `Pending Auto Netting` before creation of replacement resultant `N2`, or in `Pending Netting` without a subsequent automated step.

This distinction should be resolved alongside the holiday and late-arrival policy, rather than treated as an independent state-label choice.