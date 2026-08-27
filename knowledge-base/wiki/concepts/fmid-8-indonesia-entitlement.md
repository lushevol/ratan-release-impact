---
type: concept
title: FMID 8 Indonesia Entitlement
created: 2026-08-24
updated: 2026-08-24
tags: [FMID, Indonesia, EMS3, data-entitlement, region]
related: [ems3, region-entitled-drawer-filtering, indonesia-ratan-data-residency-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# FMID 8 Indonesia Entitlement

The source treats the string value `"8"` in `Entity.Booking_Entity_SCI_FMID` as the Indonesia FMID marker.

An entitlement list containing `"8"` matches the ID blotter expression:

```text
#root['Entity.Booking_Entity_SCI_FMID'].contains('8')
```

The source does not provide an independent FMID reference or formally define whether `"8"` is the sole canonical Indonesia identifier. That assumption should be confirmed before applying the rule beyond this design.