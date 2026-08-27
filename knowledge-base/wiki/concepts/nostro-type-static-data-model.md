---
type: concept
title: Nostro Type Static-Data Model
tags: [Nostro, static-data, RFI, portfolio, validation, RATAN]
related: [nostro-static-popup, portfolio-based-rfi-nostro-stamping, rfi-nostro-account, ratan]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/RFI Nostro stamping based on Portfolio.md"]
---

# Nostro Type Static-Data Model

The Nostro Type static-data model distinguishes dedicated RFI Nostro records from default/non-RFI records and associates RFI records with one or more portfolios.

## Field requirements

| Field | Type | Requirement |
| --- | --- | --- |
| `Nostro Type` | Dropdown | Values include `RFI` and `DEFAULT`; new records default to `DEFAULT`; displayed in list view; not updateable after creation. |
| `Portfolio` | Text | Mandatory when `Nostro Type = RFI`; supports multiple portfolio values; displayed in list view; updateable. |
| `Primary` | Existing field | Disabled when `Nostro Type = RFI`; an RFI Nostro cannot be primary. |

Duplicate validation uses:

```text
Booking Entity + Currency + Settlement Means + Settlement Account + Nostro Type
```

The requirement separately says that two RFI records cannot be created for the same entity, currency, settlement means, and settlement account. It does not clarify whether portfolio values should be part of the duplicate key.

This model intentionally permits the possibility of multiple lookup matches in the stated runtime flow, but the governance policy for avoiding or resolving legitimate ambiguity is incomplete.
