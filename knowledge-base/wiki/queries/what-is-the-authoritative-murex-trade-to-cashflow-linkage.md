---
type: query
title: What Is the Authoritative Murex Trade-to-Cashflow Linkage?
created: 2026-08-24
updated: 2026-08-24
tags: [Murex, trade-linkage, TDS3, cashflows, open-question]
related: [murex, tds3, scbml, trade-validation-gating, ratan-cashflow-standardization-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
type: query
title: What Is the Authoritative Murex Trade-to-Cashflow Linkage?
created: 2026-08-24
updated: 2026-08-24
tags: [Murex, trade-linkage, TDS3, cashflows, open-question]
related: [murex, tds3, scbml, trade-validation-gating, ratan-cashflow-standardization-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan processing on cashflow events/Trade Validation Confirmation Process Tech Design.md"]
---
# What Is the Authoritative Murex Trade-to-Cashflow Linkage?

The design does not establish which Murex identifier must be used to join a cashflow in RatanOne to confirmation and validation status in [[tds3]].

## Evidence in the design

The Cashflow Group service extracts both:

- `originalTradeId(murex)` from the originating-trade identifier path.
- `tradeId(murex)` from the standard trade identifier path.

The proposed Murex validation rule is keyed by trade ID and status, but the source does not state whether “trade ID” means the original identifier, the current identifier, or another canonical key.

## Questions to resolve

- Which identifier is authoritative for TDS3 lookup?
- How are amendments and withdrawals linked across Murex trade versions?
- Can one cashflow contain both an originating and current trade identifier?
- What happens when the identifiers disagree or one is absent?
- Is the same mapping valid for all Murex products, including FX SWAP?

A definitive answer should include example SCBML messages, the TDS3 lookup contract, amendment cases, and reconciliation or audit rules.
