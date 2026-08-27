---
type: source
title: Failed Cashflow Accounting
authors: []
year: 2026
url: ""
venue: "Cash Settlement Home Page Functional Requirement"
created: 2026-08-23
updated: 2026-08-23
tags: [cash-settlement, failed-cashflow, accounting, reprocessing, functional-requirement]
related: [failed-cashflow-accounting, failed-cashflow-reprocessing-and-trade-amendment, ratan, razor, cashflow-event-versioning, reversal-and-correction-cashflow-processing, swift-suppression, value-date-based-cashflow-materialization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Failed Process/Failed Cashflow Accounting.md"]
---

# Failed Cashflow Accounting

## Summary

This functional requirement describes the accounting and payment-generation treatment for cashflows that fail on Value Date. By end of day on Value Date, [[entities/ratan|Ratan]] sends `FAILED` cashflows to [[entities/razor|Razor]]. Razor generates accounting entries and uses the `FAILED` status to bypass Swift generation.

After the failure, Operations may re-process the cashflow from VD+1 onward. In the normal recovery flow, the cashflow status changes from `FAILED` to `READY`, the Swift Payment Date is updated, and Razor generates the Swift payment. If a trade amendment or cancellation occurs after accounting, the latest cashflow event requires reversal-and-new or reversal accounting treatment.

The requirement provides examples for normal reprocessing, amendment after accounting, and repeated failure. It also lists unresolved cases involving past-Value-Date booking, cancellation, netting-resultant cashflows, and amendments after prior settlement.

## Accounting Requirement

- On Value Date, by end of day, Ratan sends `FAILED` cashflows to Razor for accounting generation.
- Razor generates accounting for the failed cashflows.
- Razor relies on the cashflow status `FAILED` to bypass Swift generation.
- From VD+1 onward, if there is no trade amendment or cancellation, Operations re-processes the cashflow, updates the Swift Payment Date, changes the status to `READY`, and sends the cashflow to Razor for Swift generation.
- If a trade amendment or cancellation occurs after accounting, the latest cashflow event is sent to Razor and reversal-and-new or reversal accounting entries are required.

## Normal Cases

| Action | Sent to Razor | System date | Cashflow ID | Cashflow Event | Cashflow Status | Currency | Amount | Value Date | Accounting Date | Accounting Entry | Swift Value Date | Swift Generation | minorVersionDescription |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|---|
| Failed on VD | Y | 8th May | C101 | New | FAILED | USD | 100 | 8th May | 8th May | Y |  | N |  |
| Re-Process on VD+1 | Y | 9th May | C101 | New | READY | USD | 100 | 8th May |  | Y(Reversal &New) | 9th May | Y | Failed Re-Process |

The normal case separates the initial accounting action from later Swift generation. The source does not explain why the re-processing row contains `Y(Reversal &New)` when no amendment or cancellation is shown.

## Trade Amendment After Accounting EOD

| Action | Sent to Razor | System date | Cashflow ID | Cashflow Event | Cashflow Status | Currency | Amount | Value Date | Accounting Date | Accounting Entry | Swift Value Date | Swift Generation | minorVersionDescription |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|---|
| Failed on VD | Y | 8th May | C101 | New | FAILED | USD | 100 | 8th May | 8th May | Y |  | N |  |
| Trade Amendment post accounting EOD | Y | 9th May | C101 | Amendment | READY | USD | 200 | 8th May |  | Y(Reversal & New) |  | Y |  |

The amendment changes the amount from USD 100 to USD 200 while retaining cashflow ID `C101`. The latest `Amendment` event receives reversal-and-new accounting. Swift generation is marked `Y`, but the Swift Value Date is blank.

## Failed Multiple Times

| Action | Sent to Razor | System date | Cashflow ID | Cashflow Event | Cashflow Status | Currency | Amount | Value Date | Accounting Date | Accounting Entry | Swift Value Date | Swift Generation | minorVersionDescription |
|---|---|---|---|---|---|---|---:|---|---|---|---|---|---|
| Failed on VD | Y | 8th May | C101 | New | FAILED | USD | 100 | 8th May | 8th May | Y |  | N |  |
| Trade Amendment on VD+1 | N | 9th May | C101 | Amendment | WAITING | USD | 200 | 8th May |  |  |  |  |  |
| Failed again on VD+1 | Y | 9th May | C101 | Amendment | FAILED | USD | 200 | 8th May |  | Y(Reversal & New) |  | N |  |
| Re-Process on VD+2 | Y | 10th May | C101 | Amendment | READY | USD | 200 | 8th May |  | N | 10th May | Y |  |

This sequence shows that an amendment may remain in `WAITING` and not be sent to Razor, later become `FAILED`, and then receive reversal-and-new accounting. On VD+2, re-processing changes the amended cashflow to `READY`, assigns a Swift Value Date of 10th May, and enables Swift generation.

## Additional User Cases

The source identifies, but does not define, the following cases:

- Past Value Date booking.
- `FAILED` followed by trade cancellation.
- `FAILED` on netting-resultant cashflows.
- Settlement on Value Date followed by a trade amendment on VD+1 and a subsequent failure.

## Evidence Boundaries

The examples support the intended `FAILED` → `READY` recovery flow and the separation of accounting generation from Swift generation. They do not define a complete state machine, idempotency rules, duplicate handling, event ordering, correlation keys, business-day semantics, or the complete accounting-date contract.

The source also leaves unresolved whether normal reprocessing always requires reversal-and-new accounting, whether `READY` alone guarantees Swift eligibility, and whether the `FAILED` status is a formal suppression state or a status-driven instruction to skip Swift generation.

## Related Wiki Topics

- [[concepts/failed-cashflow-accounting]]
- [[concepts/cashflow-event-versioning]]
- [[concepts/cashflow-lifecycle-supersession-and-audit-history]]
- [[concepts/reversal-and-correction-cashflow-processing]]
- [[concepts/swift-suppression]]
- [[concepts/cashflow-withdrawal-and-new]]
- [[concepts/value-date-based-cashflow-materialization]]
- [[concepts/cashflow-netting-and-un-netting-state-transitions]]