---
type: concept
title: Group Blotter Pagination
created: 2026-08-23
updated: 2026-08-23
tags: [group-blotter, pagination, cashflow-loading, user-interface, performance]
related: [cash-settlement-home-page, settlement-day-2, bulk-manual-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Group Blotter Enhancement.md"]
---
# Group Blotter Pagination

Group Blotter is required to display 1,000 cashflows by default and to provide higher-volume loading behavior based on Cashflow Blotter.

## Proposed Behavior

- Default displayed record count: 1,000 cashflows.
- Additional loading options: next 1,000 or next 5,000 cashflows.
- User-configurable page size: 5,000 cashflows.

## Unspecified Details

The source does not clarify whether “load next 1,000/5,000” means incremental retrieval, navigation to another page, or a change in page size. It also does not specify sorting stability, filter interaction, server-side versus client-side pagination, maximum volume, timeout behavior, or performance acceptance criteria.

This requirement is part of the [[cash-settlement-home-page]] [[settlement-day-2]] enhancement scope and supports selection of records for [[bulk-manual-stp]].