---
type: concept
title: Trade, Cashflow, and Exception Version Correlation
tags: [cashflow, trade-version, exception-handling, data-correlation, nstp]
related: [confirmation-driven-nstp-exception-auto-closure, ratan-stella-message-event-source, cash-settlement-exception-handling]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code/NSTP exception auto close design-Confirmation status handling.md"]
---
# Trade, Cashflow, and Exception Version Correlation

Trade, cashflow, and exception version correlation is the identity-alignment rule used by the NSTP auto-close flow to ensure that processing targets the correct cashflow and business version.

## Required Mappings

| Source field | Cashflow field |
|---|---|
| CDU `tracking_version` | `trade_version` |
| Rule Service `entityId` | `cashflow__cashflow_id` |
| Rule Service `entityVersion` | `cashflow__cashflow_business_version` |

The first mapping supports cashflow lookup by trade identity and version. The latter two mappings associate a Rule Service exception with the intended cashflow identity and cashflow business version.

## Importance

An identifier alone is insufficient where a trade or cashflow can have multiple versions. The documented mappings support version-safe exception closure in [[confirmation-driven-nstp-exception-auto-closure]].

The source does not specify how request fields `cashflowVersion`, `businessVersion`, and `minorVersion` relate to these mappings, nor where each mapping is enforced.