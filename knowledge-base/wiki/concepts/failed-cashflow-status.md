---
type: concept
title: FAILED Cashflow Status
tags: [cashflow, status-lifecycle, settlement-failure, operations]
related: [cashflow-status-lifecycle, ratan, cashflow-blotter-functional-scope, failed-cashflow-reprocessing, reinstated-from-failed-exception, stella]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process.md"]
---
# FAILED Cashflow Status

`FAILED` is a main cashflow status used to identify cashflows that were not settled before the applicable due date, cutoff, or processing time. It also allows Operations to explicitly set a new `Swift Value Date` for Swift message generation.

## Entry Paths

A cashflow can enter `FAILED` through either of the following paths:

- A scheduled job applies predefined failure rules.
- FM Ops manually move the cashflow to `FAILED` from the Cashflow Blotter. Manual movement requires Maker/Checker control.

Back-value-date cashflows are not moved to `FAILED` immediately according to the source; they wait for the scheduled job on that day.

## Actions and Recovery

No further direct actions, including ordinary exception handling, can be performed on a `FAILED` cashflow. The only stated Ratan action is `Re-Instate` from the Cashflow Blotter.

Reinstatement creates the [[reinstated-from-failed-exception]] and sends the cashflow into the separate [[failed-cashflow-reprocessing]] flow. The source therefore indicates that `FAILED` is recoverable rather than terminal.

The restriction applies to direct operational actions as described in the requirement. The source separately states that new events from [[stella]] can overwrite a failed cashflow, but does not define the precedence or versioning rules for that behavior.

## Unresolved Rules

The requirement does not define:

- Scheduled-job eligibility, timing, or timezone.
- Whether manual failure is permitted before or after scheduled processing.
- The effect of concurrent scheduled and manual failure.
- Whether Stella overwrites status, fields, or the complete cashflow.
- Whether `Re-Instate` mutates the existing cashflow or creates a new version.