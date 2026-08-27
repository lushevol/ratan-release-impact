---
type: query
title: What Is the Final Dedicated Nostro Precedence, Refresh, and Uniqueness Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [nostro, rfi, precedence, refresh, uniqueness, static-data, open-question]
related: [dedicated-nostro-stamping, nostro-stamping, nostro-record-composite-uniqueness, nostro-notification-and-refresh, nostro-static-data-migration, ratanone-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio/Dedicated Nostro Stamping Design--deprecated.md"]
---
# What Is the Final Dedicated Nostro Precedence, Refresh, and Uniqueness Contract?

## Question

What are the authoritative rules for selecting, refreshing, and uniquely maintaining dedicated Nostro configurations when RFI, other dedicated types, and default configurations can all match?

## Provisional Historical Proposal

The deprecated source proposes:

```text
Dedicated match first
→ default entity + ccy + settlementMeans + settlementAccount lookup if no dedicated Nostro is found
```

It identifies initial priority as `RFI > normal`, but does not define priority among RFI, STRATEGY, and future dedicated types.

## Unresolved Contract Elements

- Whether one Nostro configuration can serve multiple dedicated types.
- The final uniqueness dimensions for dedicated records, including `portfolio`, `nostroType`, and dedicated-condition data.
- Whether dedicated information is stored in `jsonb`, a child table, or child-table-plus-`jsonb`.
- The exact RFI and dedicated-Nostro refresh scope.
- Whether refresh can affect records beyond the intended dedicated population.
- The dedicated match data that must be compared between new and withdrawn cashflows during amendment processing.
- Whether `Dedicated_Nostro_Id` is mandatory, optional, or populated for both trade and cashflow stamping.

## Evidence Needed

A successor design, database constraints, static-data API contract, refresh test evidence, and production behavior are required before the historical proposal can be treated as authoritative.