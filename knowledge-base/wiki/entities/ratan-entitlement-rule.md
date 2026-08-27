---
type: entity
title: RATAN_ENTITLEMENT_RULE
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, entitlement, EMS3, application-identifier]
related: [ems3, application-tile, region-entitled-drawer-filtering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# RATAN_ENTITLEMENT_RULE

## Identity

`RATAN_ENTITLEMENT_RULE` is the EMS3 `app_name` used by the documented region-filter configuration. The associated application identifier is `51358`.

## Use

The filter parameters are:

```json
{
  "appId": "51358",
  "appName": "RATAN_ENTITLEMENT_RULE"
}
```

The rules read `Entity.Booking_Entity_SCI_FMID` from the EMS3 data-entitlement response to determine whether an ID or GDC blotter should be visible.