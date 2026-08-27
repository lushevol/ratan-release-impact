---
type: concept
title: CPN Netting Reversal Cashflow
created: 2026-08-23
updated: 2026-08-23
tags: [cpn, reversal, cashflow, netting, nstp]
related: [cpn-netting, netting-resultant-cashflow-lifecycle, automatic-un-netting-on-trade-market-events, netting-exception-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# CPN Netting Reversal Cashflow

A CPN netting reversal cashflow is a new cashflow created when an amendment or cancellation affects a component of a netting group after the resultant has been released.

## Draft contract

The example in the source defines the following fields:

| Description | Cashflow ID | Reversal Flag | Reversal ID | Netting ID | Source System | Cashflow Status | Cashflow Version | Cashflow Sub Status Type | Payment Lake Version | Comment |
| --- | --- | --- | --- | --- | --- | --- | ---: | --- | ---: | --- |
| Post CPN Netting | C105 | N |  | N001 | CPN | Released | 3 | NA | 4 |  |
| Cashflow Amendment | C106 | Y | C105 | N001 | CPN | Pending | 1 | NSTP Release | 1 | This is Reversal of C105 |

`Reversal Flag=Y` identifies `C106` as a reversal, and `Reversal ID=C105` links it to the original resultant. The reversal retains the original Netting ID in the draft example.

## Operational path

- The original released resultant remains `Released`.
- Components move from `Netted` to `Queued`.
- The reversal starts as `Queued` and later becomes `Pending`.
- The reversal uses `NSTP Release` as its sub-status type.
- The reversal is routed to the NSTP queue for manual operations intervention.
- The latest component versions re-enter CPN eligibility and can be manually netted again.

The draft proposes future use of the reversal cashflow to generate an `MTx92` SWIFT cancellation message. That future integration is not specified as an implemented contract.

## Open contract questions

The source does not define field types, nullability, uniqueness, idempotency, or whether a reversal may reference a settled resultant in the same way as a released resultant.