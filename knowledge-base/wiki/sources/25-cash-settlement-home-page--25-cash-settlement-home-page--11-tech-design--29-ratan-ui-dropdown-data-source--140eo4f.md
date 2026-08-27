---
type: source
title: Ratan UI Dropdown Data Source
authors: []
year: 2025
url: ""
venue: ""
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ratan, ui, dropdowns, data-governance]
related: [ui-dropdown-data-source-governance, canonical-dropdown-data-source, cash-settlement-dropdown-consistency, cashflow-blotter, grouping-blotter, dashboard, nostro-static, ratan-ui-form, static-data-service, static-configuration-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# Ratan UI Dropdown Data Source

## Summary

This document is an intake inventory for identifying data sources behind dropdowns in Cash Settlement UI surfaces. It catalogs controls across the Cashflow Blotter, Grouping Blotter, Dashboard, and Nostro Static views, with columns for both the current data source and the intended proper data source.

The **Current Data Source** and **Proper Data Source** columns are blank for every listed entry. Consequently, this document establishes the scope of a data-source rationalization exercise but does not establish an implementation source, authoritative owner, API contract, or architectural decision.

## Scope

The inventory covers the following UI contexts:

- Cashflow Blotter Quick Search
- Cashflow Blotter Quick Filter
- Cashflow Blotter Custom Search
- Cashflow Blotter Cashflow Details — Vostro Exception
- Grouping Blotter Quick Search
- Dashboard Quick Search
- Nostro Static Quick Search

The screenshot references provide visual evidence of the controls but do not, by themselves, establish the underlying data contracts.

## Collection Inventory

The following table preserves the source inventory. Blank cells in the source remain blank because no source mapping was provided.

| Topic | Domain | Component | Snapshot | Current Data Source | Proper Data Source |
| --- | --- | --- | --- | --- | --- |
| Product Taxonomy | Cashflow Blotter | Quick Search | ![image-2025-5-20_16-2-44.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-2-44.png) | | |
| Cashflow Blotter | Quick Filter | ![image-2025-5-20_16-18-16.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-18-16.png) | | |
| Cashflow Blotter | Custom Search | ![image-2025-5-20_16-18-49.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-18-49.png) | | |
| Currency (CCY) | Cashflow Blotter | Quick Search | ![image-2025-5-20_16-19-43.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-19-43.png) | | |
| Cashflow Blotter | Custom Search | ![image-2025-5-20_16-20-13.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-20-13.png) | | |
| Booking Entity | Cashflow Blotter | Quick Search | ![image-2025-5-20_16-21-2.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-21-2.png) | | |
| Cashflow Blotter | Quick Filter | ![image-2025-5-20_16-23-9.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-23-9.png) | | |
| Cashflow Blotter | Custom Search | ![image-2025-5-20_16-21-33.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-21-33.png) | | |
| Grouping Blotter | Quick Search | ![image-2025-5-20_20-7-47.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_20-7-47.png) | | |
| Dashboard | Quick Search | ![image-2025-5-20_20-58-11.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_20-58-11.png) | | |
| NSTP Exception | Cashflow Blotter | Quick Filter | ![image-2025-5-20_16-22-55.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-22-55.png) | | |
| Cashflow State/Sub State/Sub State Type | Cashflow Blotter | Quick Filter | ![image-2025-5-20_16-23-54.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-23-54.png) | | |
| Grouping Blotter | Quick Search | ![image-2025-5-20_19-52-24.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_19-52-24.png) | | |
| Group Status | Grouping Blotter | Quick Search | ![image-2025-5-20_20-8-18.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_20-8-18.png) | | |
| Settlement Methods/Settlement Means | Cashflow Blotter | Quick Filter | ![image-2025-5-20_16-24-31.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-24-31.png) | | |
| Cashflow Blotter | Cashflow Details - Vostro Exception | ![image-2025-5-20_16-25-21.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-25-21.png) | | |
| Nostro Static | Quick Search | ![image-2025-5-20_21-13-10.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_21-13-10.png) | | |
| Bic Net Flag | Cashflow Blotter | Quick Filter | ![image-2025-5-20_16-24-53.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-24-53.png) | | |
| SSI Type | Cashflow Blotter | Cashflow Details - Vostro Exception | ![image-2025-5-20_16-28-20.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-28-20.png) | | |
| Msg | Cashflow Blotter | Cashflow Details - Vostro Exception | ![image-2025-5-20_16-28-57.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-28-57.png) | | |
| Charges | Cashflow Blotter | Cashflow Details - Vostro Exception | ![image-2025-5-20_16-29-11.png](../media/ratan-ui-dropdown-data-source/image-2025-5-20_16-29-11.png) | | |
| Other Options in Custom Search | | | | | |

## Interpretation Notes

Several rows omit a Topic value and appear to carry forward the subject from a preceding row. For example, the rows labelled `Cashflow Blotter | Quick Filter` and `Cashflow Blotter | Custom Search` may continue the `Product Taxonomy` topic, but the table does not make that relationship explicit.

The final `Other Options in Custom Search` row is a placeholder without additional field detail. The original editable table or screenshots should be reviewed before using this inventory as an implementation checklist.

## Findings

1. The document identifies a broad, cross-screen inventory of dropdown controls.
2. It does not identify the current producer, authoritative owner, serving API, refresh policy, or caching policy for any option set.
3. Repeated fields such as Product Taxonomy, Currency (CCY), Booking Entity, and state-related selectors create a potential consistency and ownership risk across UI surfaces.
4. The document is an intake artifact rather than an approved technical design or decision record.
5. “Proper Data Source” is undefined; possible decision criteria include authority, freshness, latency, entitlement, localization, completeness, and resilience.

## Related Wiki Topics

The inventory extends the scope of [[entities/ratan-ui-form]] and [[concepts/ratanone-ui-form-principles]] from form behavior to option-list provenance. [[entities/static-data-service]], [[entities/ratan-static-data-service]], and [[concepts/static-configuration-management]] are relevant possible ownership domains, but this source does not authorize assigning any listed dropdown to them.

The `Nostro Static`, `Settlement Methods/Settlement Means`, and `Bic Net Flag` entries warrant comparison with [[entities/nostro-configuration]] and [[entities/bicnetting-configuration]]. The `Cashflow State/Sub State/Sub State Type` and `Group Status` entries require vocabulary and API confirmation against [[concepts/cashflow-group-and-message-state-machines]] and [[concepts/major-version-cashflow-grouping]].

## Open Questions

- What are the current producer, authoritative owner, serving API, and refresh policy for each dropdown?
- Which option sets are static or configuration-backed, and which are derived from live operational data?
- Must repeated fields return identical codes, labels, filtering semantics, and entitlement behavior across all screens?
- What are the intended source and filter semantics for `NSTP Exception`, `SSI Type`, `Msg`, and `Charges`?
- Is `Other Options in Custom Search` a placeholder for an incomplete field inventory?
- Can the original table or screenshots resolve the implicit Topic associations?