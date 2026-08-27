---
type: concept
title: SSI Stamping Reference Data
created: 2026-08-24
updated: 2026-08-24
tags: [SSI-stamping, Vostro, Nostro, counterparty, reference-data, cashflow]
related: [static-reference-data-synchronization, database-first-static-data-caching, cashflow-lifecycle-stamping, cashflow-precheck-validation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/The Cache Data Layer Design.md"]
---

# SSI Stamping Reference Data

SSI stamping is the use of settlement-related static data to enrich or stamp cashflows during STP processing. The design identifies three distinct datasets with different ownership and update models.

## Dataset responsibilities

| Dataset | Master or owner | Initialization | Update model | Approximate 2022 size | Key |
| --- | --- | --- | --- | ---: | --- |
| Vostro data | SSI+ | SSI+-provided database dump | SSI+ notifications, EOD reconciliation and refresh | About 1 million records | `SSI-ID` |
| Nostro data | RatanOne | Manual initialization | New-data dump | 100,000 records | `legalEntityFmId+Currency+settlementMeans+settlementAccount` |
| Counterparty information | SCI | SCI API query | SCI notifications and scheduled daily sync | 400 records | `FMID` |

Vostro records contain nested entity and settlement-instruction information. Nostro records contain legal-entity, currency, settlement-account, Swift, and correspondent fields. Counterparty records provide FMID and profile mappings.

## Boundary and governance gaps

The source distinguishes external golden-source data from RatanOne-owned Nostro data, but does not define authoritative tables, ownership of maintenance workflows, maker-checker controls, validation, auditability, or security classification for account and counterparty information.

The data supports cashflow processing and is adjacent to [[concepts/cashflow-lifecycle-stamping]] and [[concepts/cashflow-precheck-validation]], but the source does not assign ownership of the static-data layer to those components.
