---
type: concept
title: Cashflow Failure and Reinstatement
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow, failure-handling, reinstatement, exception-management]
related: [cashflow-exception-handling, maker-checker-settlement-control, stella, ratan-cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/User Actions on Cashflow Blotter.md"]
---
# Cashflow Failure and Reinstatement

Manual failure is the intended FMRP lifecycle action for a cashflow that has not settled by its due date or cutoff. It moves the cashflow to `FAILED`, where it is highlighted for Operations and subject to a failed reprocessing flow.

The source states that no further RATAN action, including exception handling, is available on a `FAILED` cashflow except Re-Instate. Reinstatement creates a maker/checker exception, requires selection of `Settlement_Instruction.Value_Date` (Swift Value Date), returns the cashflow to `QUEUED`, reruns Netting Client Check and Exception Check, and creates a `Cashflow Re-Instate` exception.

A new event from [[stella]] can overwrite the failed cashflow. The precise FMRP Manual Fail state conditions and the divergent BCS rule require clarification in [[what-is-the-authoritative-manual-fail-eligibility-for-fmrp-and-bcs]].