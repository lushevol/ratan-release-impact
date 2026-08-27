---
type: concept
title: Region-Entitled Drawer Filtering
created: 2026-08-24
updated: 2026-08-24
tags: [drawer-filtering, region-entitlement, UI-visibility, Indonesia, FMID]
related: [fmo-post-trade-portal, ems3, application-tile, fmid-8-indonesia-entitlement, should-gdc-drawers-exclude-mixed-indonesia-entitlements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# Region-Entitled Drawer Filtering

Region-entitled drawer filtering limits the drawers or blotters returned by the login flow according to a user's data entitlement.

For the Indonesia design, the decision key is `Entity.Booking_Entity_SCI_FMID`. FMID `"8"` identifies Indonesia:

```text
#root['Entity.Booking_Entity_SCI_FMID'].contains('8')
```

The current GDC rule checks for at least one non-`"8"` value:

```text
!#root['Entity.Booking_Entity_SCI_FMID'].?[#this != '8'].isEmpty()
```

This is not an exclusive GDC-only rule. A user with both `"8"` and non-`"8"` values can satisfy both regional rules.

This concept concerns login-time UI selection. It should not be interpreted as proof of data-level authorization for downstream APIs.