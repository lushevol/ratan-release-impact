---
type: query
title: How Are Post-Query Cancellations and Reversals Reconciled in TIS and OLTP?
created: 2026-08-23
updated: 2026-08-23
tags: [reversal, cancellation, reconciliation, tis, oltp, korea-migration]
related: [ratan-tis-payment-query-integration, ratan, tis, oltp, korea-cash-settlement-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2026 Changes/Cash Settlement -- Korea Migration/Ratan to TIS.md"]
---
# How Are Post-Query Cancellations and Reversals Reconciled in TIS and OLTP?

## Question

How are TIS and OLTP(UI) notified or reconciled when a cashflow previously retrieved from RATAN is later cancelled, withdrawn, or reversed?

## Evidence

The source states that withdrawal cashflows are unavailable to TIS/OLTP query and are settled with a Reversed/Reversal flag. API filters exclude `Cashflow_Event_Reason = 'Reversal'`.

It also states that reversal cashflows retain the original cashflow ID and are not in TIS scope. TIS does not refresh duplicate records because its key is trade ID/cashflow ID, and it sends no acknowledgement or other message to RATAN after querying.

## Risk

A payment already obtained by TIS can later be invalidated in RATAN without a compensating event or refreshed record arriving through the specified interface.

## Needed decision

Define ownership, reconciliation frequency, cancellation detection, exception queue handling, and the compensating OLTP(UI) action for a post-query reversal.