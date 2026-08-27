---
type: query
title: How Should RATAN Correlate Murex Counterparty Assignment Cashflows?
created: 2026-08-22
updated: 2026-08-22
tags: [murex, ratan, counterparty-assignment, cashflow-grouping, trade-lineage, open-question]
related: [murex-211, murex-payment-trade-lineage-identifiers, murex-to-ratan-cashflow-integration, murex-ratan-reversal-and-replacement-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/02-Issue Tracking & Tech Debt/Murex Counterparty Assignment - Original Trade id Changed.md"]
---
# How Should RATAN Correlate Murex Counterparty Assignment Cashflows?

## Question

How should RATAN correlate cashflows when a Murex 2.11 Counterparty Assignment event changes the Original Trade Id?

## Why This Is Open

RATAN's reported booking-level grouping model relies on a stable Murex Original Trade Id. The source reports that Counterparty Assignment breaks this assumption but does not specify the old-to-new identifier relationship, the payment impact, current RATAN behaviour, or an approved alternative grouping key.

Counterparty Assignment must not be assumed to use the same lifecycle model as [[murex-ratan-reversal-and-replacement-lifecycle]] without supporting event evidence.

## Evidence Needed

- A populated before-and-after Counterparty Assignment example from Murex 2.11.
- Source message format and field paths for prior and replacement Original Trade Id, Trade ID, payment ID, and any assignment or correlation identifier.
- The expected RATAN outcome: retain a group, merge groups, split groups, or create a successor relationship.
- Observed RATAN behaviour and its settlement or operational impact.
- Timing constraints, including whether Counterparty Assignment can occur before payment creation, after publication, or after settlement.
- Ownership agreement between Murex and RATAN teams for providing and consuming a durable lineage key.

## Related Pages

The identifier contract is described in [[murex-payment-trade-lineage-identifiers]], while the broader dependency is documented in [[murex-to-ratan-cashflow-integration]].