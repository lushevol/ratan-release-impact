---
type: query
title: How Does RATAN Correlate Murex Lien Status to Cashflows?
created: 2026-08-23
updated: 2026-08-23
tags: [open-question, ratan, murex, lien, cashflow-correlation, migration]
related: [murex, murex-211, ratan, ratan-cashflow-lifecycle-service, cashflow-migration, lien-driven-cashflow-nstp, trade-to-cashflow-lien-correlation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration.md"]
---
# How Does RATAN Correlate Murex Lien Status to Cashflows?

## Question

What authoritative key, interface, and processing sequence does RATAN use to associate a Murex cashflow with its originating trade and effective Lien status?

## Evidence

The requirement states that Murex trades and cashflows are separate business objects and separate data flows. RATAN must nevertheless apply a `Lien` exception to all relevant cashflows while Lien is active.

The source does not specify:

- The Murex field or event that carries Lien status.
- The key linking a cashflow to a trade.
- Whether RATAN or another service owns the correlation.
- The behavior when trade and cashflow messages arrive out of order.
- The retry, reconciliation, and missing-data behavior.

## Why It Matters

Without a reliable correlation mechanism, RATAN could incorrectly allow a Liened cashflow to settle STP or incorrectly retain an NSTP exception after Lien removal. The design is a dependency for [[concepts/cashflow-migration-readiness]] and the [[projects/cashflow-migration]] project.

## Resolution Needed

Document the authoritative trade identifier, Lien status source, event sequencing rule, ownership boundary, and operational reconciliation process. Validate the approach against the reported 24 live Murex Lien trades before migration or production activation.
