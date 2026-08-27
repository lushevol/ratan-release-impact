---
type: concept
title: Failed Cashflow Accounting
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, accounting, failed-cashflow, reprocessing, swift-generation, value-date]
related: [ratan, razor, cashflow-event-versioning, cashflow-lifecycle-supersession-and-audit-history, reversal-and-correction-cashflow-processing, swift-suppression, cashflow-suppression, value-date-based-cashflow-materialization, cashflow-netting-and-un-netting-state-transitions, trade-economic-versus-non-economic-update, trade-event-id-lineage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# Failed Cashflow Accounting

Failed cashflow accounting is the process of accounting for a settlement cashflow that fails on Value Date while preventing immediate Swift payment generation.

## Core Flow

1. By end of day on Value Date, [[entities/ratan|Ratan]] sends the `FAILED` cashflow to [[entities/razor|Razor]].
2. Razor generates accounting entries for the failed cashflow.
3. Razor bypasses Swift generation because the cashflow status is `FAILED`.
4. From VD+1 onward, Operations may re-process the cashflow.
5. Re-processing updates the Swift Payment Date and changes the status to `READY`.
6. Razor can then generate the Swift payment for the revised payment date.

This flow demonstrates that accounting generation and Swift generation are separate processing outcomes. A failed cashflow is accounted for even though its Swift payment is not generated on Value Date.

## Trade Changes After Failure

If a trade amendment or cancellation occurs after the failed cashflow has already been accounted for, the latest cashflow event is sent to Razor. The source requires reversal-and-new or reversal accounting entries rather than treating the event as an ordinary retry.

The repeated-failure example shows the same cashflow ID, `C101`, being used for both a `New` event and a later `Amendment` event. This requires version or event lineage, such as the mechanisms described in [[concepts/cashflow-event-versioning]] and [[concepts/trade-event-id-lineage]].

## Status Semantics

- `FAILED`: The cashflow failed and should be accounted for without Swift generation.
- `WAITING`: An amended cashflow is not yet sent to Razor. The source does not define the trigger that moves it to another state.
- `READY`: The cashflow is eligible for post-failure Swift generation after re-processing, subject to any additional controls not defined in the requirement.

The source does not establish that every `READY` cashflow is automatically eligible for Swift generation.

## Reversal-and-New Ambiguity

The prose associates reversal-and-new accounting with amendments and cancellations. However, the normal re-processing table also contains `Y(Reversal &New)` despite showing no trade amendment or cancellation. It is therefore unresolved whether:

- Every failed-cashflow retry requires reversal-and-new accounting.
- The table uses reversal-and-new as a generic correction label.
- The normal-case row is inconsistent with the prose.

See [[queries/does-failed-cashflow-reprocessing-always-require-reversal-and-new-accounting]].

## Relationship to Swift Suppression

The `FAILED` status causes Razor to bypass Swift generation, but the source does not establish whether this is the same mechanism as formal [[concepts/swift-suppression]] or [[concepts/cashflow-suppression]]. It should be treated as a status-driven bypass until the implementation contract confirms otherwise.

## Open Scope

The requirement does not define processing for past-Value-Date booking, failed cancellation, failed netting-resultant cashflows, or a settled cashflow that is amended and then fails. These cases are tracked in [[queries/how-are-failed-cancelled-and-netting-resultant-cashflows-accounted]].