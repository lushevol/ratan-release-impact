---
type: concept
title: Cashflow Business and Message Versioning
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow, versioning, integration, deduplication, concurrency]
related: [fmrp-stella, ratan, cashflow-version-concurrency-control, released-settled-amendment-control]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Ratan & Stella cashflow integration.md"]
---
# Cashflow Business and Message Versioning

The proposed integration uses separate version dimensions for trade changes, Stella messages, and Ratan workflow activity.

| Version field | Owner | Purpose |
|---|---|---|
| `Business Version` | FMRP Stella | Identifies a business or economic change such as amendment or withdrawal. |
| `Cashflow Version` | FMRP Stella | Identifies successive cashflow messages, including status updates. |
| `Ratan Minor Version` | Ratan | Records internal workflow and FMO GUI actions within a business version. |

New business versions reset the Ratan minor version to `0`. The source states that duplicate filtering uses:

```text
Cashflow Id
Business Version
Status_Update Event
```

The source also uses `Payment Version` in one scenario instead of `Ratan Minor Version`. Whether these names refer to one field or two separate fields is unresolved.