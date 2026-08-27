---
type: query
title: Who Governs RATAN Dashboard Front End Hard-Coded Filter Lists?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, dashboard, front-end, static-data, governance, open-question]
related: [ratan-cashflow-dashboard, dashboard-quick-search-filtering]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/RATAN Cashflow Dashboard.md"]
---
# Who Governs RATAN Dashboard Front End Hard-Coded Filter Lists?

The requirement specifies Front End hard-coded lists for Booking Entity `FMCODE`, Client Type, and cashflow Status. It does not identify ownership, release process, versioning, or alignment with authoritative static data.

## Questions

- Which team owns each hard-coded list?
- What authoritative source validates the lists?
- How are additions, removals, and corrections requested, approved, tested, and released?
- How are country mappings coordinated with booking-entity changes?
- Is a service- or configuration-backed implementation required instead of Front End hard-coding?

The absence of governance risks stale or inconsistent dashboard filtering.