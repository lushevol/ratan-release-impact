---
type: concept
title: Amendment-Driven Cashflow Correlation
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, trade-amendment, correlation, lineage, ratan]
related: [ratan, murex, rebook-exception, payment-date-proximity-matching, settlement-day-2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Ingenuine Rebook Exception in Ratan.md"]
---
# Amendment-Driven Cashflow Correlation

Amendment-driven cashflow correlation is the ability to identify that a new cashflow is the replacement for an original cashflow withdrawn because of a trade amendment.

This relationship is needed to distinguish genuinely amendment-driven rebooks from unrelated cashflows that happen to share attributes. In the documented Ratan flow, the absence of direct lineage prevents certain identification of replacement cashflows and requires a [[payment-date-proximity-matching]] proxy.

## Operational implication

When an original cashflow has already been released, the withdrawal and replacement cashflow require additional operational validation. Correct correlation supports generation of a reversal exception for the withdrawal and a [[rebook-exception]] for the replacement.

## Current and prospective approaches

The current approach uses shared Trade ID, currency, comparator status, and payment-date proximity. For Murex, Ratan uses Original Trade ID as the relevant Trade ID input.

The proposed future approach is to consume a trade event after Uber is enabled. A trade-event solution requires a stable original-to-replacement identifier, delivery timing compatible with Ratan release processing, and reconciliation and ownership arrangements. See [[can-uber-trade-events-provide-authoritative-amendment-lineage-for-ratan]].