---
type: concept
title: Trade-Cashflow Correlation by Trade Version
created: 2026-08-24
updated: 2026-08-24
tags: [trade-correlation, cashflow, versioning, stella, murex-211]
related: [stella, murex-211, tds3, ratan, cashflow-business-and-message-versioning, cashflow-version-concurrency-control, trade-confirmation-driven-cashflow-stp, what-are-the-authoritative-stella-trade-cashflow-correlation-paths]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Trade Confirmation & Cashflow STP.md"]
---
# Trade-Cashflow Correlation by Trade Version

Trade-cashflow correlation is source-specific in the trade confirmation requirement.

## Stella Correlation

For Stella, the required correlation key is the pair:

- `Trade_ID`
- `Trade_Lake_Trade_Major_version`

Both values are said to exist in trade and cashflow data. The requirement does not supply SCBML paths, cashflow-side schema locations, cardinality constraints, mismatch treatment, or a rule for late and out-of-order versions.

For trade updates, amendments, partial terminations, and novations, CDU is expected to confirm the latest major version. This latest-version principle is a control against applying stale confirmation outcomes.

## Murex 2.11 Correlation

For Murex 2.11, Ratan extracts `Source_System_Trade_Internal_Id` from trade SCBML and searches cashflow records with matching `Trade_Id`.

This mapping does not state that a Murex major version forms part of the lookup. It must therefore remain distinct from the Stella two-field correlation model.

## Open Contract Gap

The source names Stella logical-model fields but leaves their SCBML paths blank. The required contract, including uniqueness and version-mismatch behavior, is tracked in [[what-are-the-authoritative-stella-trade-cashflow-correlation-paths]].