---
type: concept
title: UI Dropdown Data-Source Governance
created: 2026-08-24
updated: 2026-08-24
tags: [ui, dropdowns, data-governance, source-of-truth, cash-settlement]
related: [ratan-ui-dropdown-data-source, canonical-dropdown-data-source, cashflow-dropdown-consistency, static-configuration-management, centralized-static-configuration-management, ratan-ui-form]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# UI Dropdown Data-Source Governance

UI dropdown data-source governance is the practice of assigning every option list to a documented producer, authoritative owner, and serving interface.

## Required Distinctions

A source inventory should distinguish at least three roles:

1. **Current producer** — the system currently generating or supplying the values.
2. **Authoritative owner** — the system or domain responsible for the canonical business meaning and lifecycle of the values.
3. **Serving API** — the interface consumed by the frontend.

These roles may belong to different systems. A frontend endpoint can serve cached or transformed values while another service remains the system of record.

## Governance Criteria

A proposed source should be evaluated for:

- Authority and ownership
- Code and label completeness
- Freshness and refresh frequency
- Latency and availability
- User entitlement and data visibility
- Localization requirements
- Caching and invalidation behavior
- Failure handling and fallback behavior
- Consistency across UI surfaces
- Versioning and backward compatibility

## Application to Cash Settlement

[[ratan-ui-dropdown-data-source]] inventories controls across [[entities/cashflow-blotter]], [[entities/grouping-blotter]], [[entities/dashboard]], and [[entities/nostro-static]]. Its source columns are empty, so it is evidence of scope rather than a completed governance result.

The inventory should be completed per business field, not merely per screen. Repeated fields such as Booking Entity, Currency (CCY), and state selectors should be checked for consistent codes, labels, filtering semantics, and entitlements.