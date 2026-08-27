---
type: source
title: Murex Trade & Cashflow Events
authors: []
year: 2023
url: ""
venue: ""
created: 2026-08-23
updated: 2026-08-23
tags: [deprecated, murex, ratan, cashflow-lifecycle, event-ordering, duplicate-payment-risk]
related: [murex, ratan, reversal-and-correction-cashflow-processing, cashflow-withdrawal-and-new, cashflow-event-versioning, trade-event-id-lineage, trade-cashflow-reference-linkage, cashflow-lifecycle-supersession-and-audit-history, what-is-the-authoritative-murex-cancellation-removal-cashflow-sequencing-and-correlation-model, should-cancellation-removal-be-blocked-after-cancellation-payments-settle, what-does-c-and-r-mean-in-murex-trade-and-cashflow-events]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Deprecated docs/Murex Trade & Cashflow Events.md"]
---
# Murex Trade & Cashflow Events

## Status and scope

This deprecated functional-requirement note records unresolved questions about Murex trade events and the cashflows received by [[ratan]]. It is historical evidence of event-ordering, identity, and duplicate-payment risks; it does not define an approved processing contract.

The note focuses on booking, cancellation, cancellation removal, and repeated `C&R` sequences. It does not define `C&R`, provide event payloads, identify an authoritative correlation key, or specify a resolution for out-of-order delivery.

## Key observations

- The note identifies duplicate-payment risk if Ratan receives cancellation-removal cashflows `C5` and `C6` before earlier related cashflows.
- It reports reversal linkage between `C1` and `C3`, and between `C2` and `C4`.
- It separately reports no linkage between cancellation-removal cashflows and preceding cashflows; `C5` and `C6` appear as standalone cashflows under trade `T1`.
- After `C&R Removal`, the trade ID reportedly reverts to `T1`, making a trade ID alone insufficient to group payments from distinct market events.
- Whether cancellation removal is blocked after cancellation payments settle is posed as a question, not a confirmed rule.

These observations reinforce the need for immutable event lineage and idempotent, out-of-order-safe processing, as tracked by [[what-is-the-authoritative-murex-cancellation-removal-cashflow-sequencing-and-correlation-model]].

## Source scenarios

### Trade Book (Not Settled) + Trade Cancel (Not Settled) + Remove Cancel

> a) How to identify the sequence of cashflows generated from Cancellation & Cancellation Removal? In case C5 & C6 received first by Ratan, there're duplicate payment risk.  
> b) For the cashflow generated from the Cancellation Removal, there're no linkage with the previous cashflow (while there're reversal linkage between C1&C3, C2&C4). C5, C6 looks like standalone cashflows under the same trade T1.  
> c) The Cashflow id consistency challenge C1( Book + Cancellation) → C5( Cancellation Removal).

### Trade Book (Settled) + Trade Cancel (Not Settled) + Remove Cancel

> a) The sequence of the payments from different market events  
> b) If cancellation payments are settled, will the 'Cancellation Removal' action be blocked?

This unresolved settlement-state question is tracked in [[should-cancellation-removal-be-blocked-after-cancellation-payments-settle]].

### Trade Book (Not Settled) + C&R (not settled) + C&R

> a) How to identify the sequence of these 2 C&R.  
> b) How to handle the cases the 2nd C&R cashflow come first.

### Trade Book (not settled) + C&R (not settled) + C&R Removal

> a) The sequence of C&R and C&R Removal  
> b) After C&R Removal, the trade id reverted back to T1, it's challenge to group these payments with different market events.

The undefined terminology is tracked in [[what-does-c-and-r-mean-in-murex-trade-and-cashflow-events]].

## Interpretation limits

The illustrative identifiers `T1` and `C1`–`C6` are scenario labels, not established production identifiers or universal lifecycle keys. The note does not establish that Ratan has issued duplicate payments, that the reported missing linkage originates in Murex, or that cancellation removal is prohibited after settlement.

Later authoritative requirements and interface contracts take precedence. See [[deprecated-functional-requirements]] and [[which-cash-settlement-requirement-documents-are-authoritative-after-deprecation]].