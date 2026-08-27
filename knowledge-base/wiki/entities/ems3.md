---
type: entity
title: EMS3
created: 2026-08-24
updated: 2026-08-24
tags: [EMS3, entitlement, data-entitlement, region-filtering, RATAN]
related: [ems2, ratan-entitlement-rule, region-entitled-drawer-filtering, fmo-post-trade-portal]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# EMS3

## Role

EMS3 is the entitlement source proposed for data and regional filtering in the FMO Post Trade Portal login flow.

The design retrieves data for:

```text
app_name: RATAN_ENTITLEMENT_RULE
itam_id: 51358
```

The relevant data entitlement is:

```text
Entity.Booking_Entity_SCI_FMID
```

Its values are evaluated by the configured filter expression. The source distinguishes this from EMS2 function filtering.

## Example

The response for user `1633330` contains FMID `"8"` and many non-`"8"` values. Under the current expressions, this user qualifies for both ID and GDC drawer filters.

## Limitations

The source does not define behavior for unavailable EMS3 responses, missing entitlement keys, empty value lists, malformed values, or backend API enforcement.