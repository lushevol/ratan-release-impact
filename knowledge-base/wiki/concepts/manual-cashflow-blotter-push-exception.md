---
type: concept
title: Manual Cashflow Blotter Push Exception
created: 2026-08-24
updated: 2026-08-24
tags: [manual-control, cashflow-blotter, RATAN, exception-handling, trade-migration]
related: [ratan, murex-211, trade-validation-cashflow-gating, ratan-group-blotter-event-completeness, fmrp-manual-cashflow-publication, ratan-murex-211-cashflow-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Validation & Cashflow Process/RATAN Settlement Control on Trade Validation.md"]
---
# Manual Cashflow Blotter Push Exception

A manual cashflow blotter push is an operator intervention used when a cashflow is missing from or delayed in the RATAN cashflow blotter and normal automated processing cannot complete.

## Documented scenarios

The source identifies three exception classes:

1. **Cashflow stuck in Murex:** A cashflow is expected to be sent to RATAN but remains in the Murex workflow, or a group waits for a related reversal or rebook event. The source reports 46 such cashflows over four months.
2. **Cashflow cancelled before RATAN feeding:** A related payment has reached RATAN while the expected original payment was cancelled before feeding. The waiting cashflow may need to be pushed manually.
3. **Trade not validated on value date:** Under the interim validation-gated flow, operators monitor the cashflow and manually push it when validation is unavailable on value date.

## Temporary control

Manual action remains required until trade migration is complete. The source does not define the migration population, owner, approval process, audit requirements, monitoring frequency, escalation SLA, retry policy, or exit criteria.

The manual push must not be conflated with [[concepts/fmrp-manual-cashflow-publication]], which concerns FMRP publication and is a separate process unless further evidence establishes equivalence.

## Control question

It is unresolved whether the manual action bypasses trade validation, moves the item into an exception queue, or applies another controlled state transition. This is tracked in [[queries/does-manual-ratan-blotter-push-bypass-trade-validation]].