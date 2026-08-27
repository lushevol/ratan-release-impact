---
type: query
title: Does Login Drawer Filtering Enforce Backend Region Authorization?
created: 2026-08-24
updated: 2026-08-24
tags: [open-question, authorization, backend, login-api, EMS3]
related: [region-entitled-drawer-filtering, ems3, fmo-post-trade-portal, indonesia-ratan-data-residency-isolation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Login API get correct drawers according to region entitlement as well.md"]
---
# Does Login Drawer Filtering Enforce Backend Region Authorization?

## Question

Does filtering drawers in the login response enforce regional access to the underlying blotter data, or must each downstream API independently validate the user's EMS3 entitlement?

## Current evidence

The source describes UI visibility filtering only. It does not state that the underlying blotter APIs apply the same `Entity.Booking_Entity_SCI_FMID` rule.

Until confirmed, login filtering should be treated as a presentation and authorization-support control rather than complete backend data isolation.