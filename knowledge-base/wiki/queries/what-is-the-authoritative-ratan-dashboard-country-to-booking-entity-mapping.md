---
type: query
title: What Is the Authoritative RATAN Dashboard Country-to-Booking-Entity Mapping?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, dashboard, country, booking-entity, fmcode, open-question]
related: [ratan-cashflow-dashboard, dashboard-quick-search-filtering, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/RATAN Cashflow Dashboard.md"]
---
# What Is the Authoritative RATAN Dashboard Country-to-Booking-Entity Mapping?

The requirement calls for a mapped Country list, but its only shown row, China, has no dropdown value or mapped query condition. The adjacent Booking Entity text instead specifies a hard-coded Front End list of in-scope `FMCODE` values.

## Questions

- What Country dropdown values are supported?
- What query condition applies to each Country?
- Which booking entities and `FMCODE` values belong to each Country?
- Is Country filtering derived from Booking Entity or maintained independently?
- What system owns and governs the mapping?

Resolve this before implementing Country filtering in [[dashboard-quick-search-filtering]].