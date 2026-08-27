---
type: concept
title: Clearing Status Propagation
created: 2026-08-23
updated: 2026-08-23
tags: [clearing, trade-data, data-synchronization, Murex, TDS3, RATAN]
related: [murex-211, murex, tds3, ratan, clearing-trade-payment-risk, cashflow-group-completeness-gating]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Q3 Function Analysis/Clearing Trades & Payment Risk.md"]
---
# Clearing Status Propagation

Clearing status propagation is the transfer of a trade-level clearing indicator from the booking or trade-data system to RATAN in time to control payment release.

## Timing problem

For SWAPSWIRE, the initial booking may not contain clearing status. A later modify event can add it, potentially up to two hours after booking. The original payment may already have been generated and sent to RATAN during that interval.

Murex may also be unable to place the clearing indicator in the payment message, even when the trade already has the status. After the payment is sent, a later UDF update cannot reliably be sent to RATAN as an additional payment event.

## Systems and ownership

The proposed design would have RATAN consume clearing status from [[entities/tds3]]. This is a proposal, not an established authoritative-data decision. It requires confirmation of:

- status ownership and authority;
- delivery timeliness relative to VD-1;
- trade-to-payment correlation;
- completeness and exception handling;
- reconciliation between Murex, TDS3, and RATAN.

## Control requirement

A missing, delayed, or unconfirmed clearing status should prevent automatic bilateral payment release. The system should make the status timing and synchronization state observable rather than assuming that a later trade amendment will reach RATAN.