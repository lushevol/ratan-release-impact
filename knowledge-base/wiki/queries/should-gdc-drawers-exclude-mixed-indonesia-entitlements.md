---
type: query
title: Should GDC Drawers Exclude Mixed Indonesia Entitlements?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, GDC, Indonesia, EMS3, mixed-entitlement]
related: [region-entitled-drawer-filtering, fmid-8-indonesia-entitlement, ems3, application-tile-filter-configuration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# Should GDC Drawers Exclude Mixed Indonesia Entitlements?

## Question

Should a user with both FMID `"8"` and non-`"8"` values see both ID and GDC drawers, or should GDC drawers be restricted to users whose entitlement contains no `"8"`?

## Evidence

The current GDC expression is:

```text
!#root['Entity.Booking_Entity_SCI_FMID'].?[#this != '8'].isEmpty()
```

It matches any list containing a non-`"8"` value, including a list that also contains `"8"`. A strict GDC-only expression would more closely resemble:

```text
!#root['Entity.Booking_Entity_SCI_FMID'].contains('8')
```

The source does not record an approval for either mixed-visibility behavior or the strict alternative.