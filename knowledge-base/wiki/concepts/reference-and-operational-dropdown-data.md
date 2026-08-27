---
type: concept
title: Reference and Operational Dropdown Data
created: 2026-08-24
updated: 2026-08-24
tags: [ui, dropdowns, reference-data, operational-data, cash-settlement]
related: [ratan-ui-dropdown-data-source, ui-dropdown-data-source-governance, canonical-dropdown-data-source, static-configuration-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# Reference and Operational Dropdown Data

Dropdown values can be broadly distinguished between maintained reference or configuration data and values derived from live operational state.

## Reference or Configuration Data

These values are usually managed through controlled configuration processes and may include settlement methods, settlement means, Nostro-related selections, or flags such as Bic Net Flag. Their contracts should define ownership, approval, effective dates, and auditability.

## Operational or State Data

These values may be derived from domain services or current workflow state. Cashflow State, Sub State, Sub State Type, Group Status, and NSTP Exception are candidates for this category, but the source does not classify them or identify their owners.

## Design Implication

The classification affects the appropriate serving model, freshness requirement, caching strategy, failure behavior, and governance process. It must not be inferred solely from a UI label.

The [[ratan-ui-dropdown-data-source]] inventory should record the classification, authoritative owner, serving API, and refresh policy for each option set. Existing [[concepts/static-configuration-management]] material is relevant but does not resolve the classification for these controls.