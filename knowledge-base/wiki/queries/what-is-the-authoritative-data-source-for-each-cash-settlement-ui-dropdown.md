---
type: query
title: What Is the Authoritative Data Source for Each Cash Settlement UI Dropdown?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, ui, dropdowns, open-question, data-governance]
related: [ratan-ui-dropdown-data-source, ui-dropdown-data-source-governance, canonical-dropdown-data-source, reference-and-operational-dropdown-data, static-configuration-management, ratan-ui-form]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan UI Dropdown Data Source.md"]
---
# What Is the Authoritative Data Source for Each Cash Settlement UI Dropdown?

## Question

For every dropdown in the Cash Settlement UI inventory, what are the current producer, authoritative owner, serving API, refresh or caching policy, entitlement rules, and failure behavior?

## Evidence

[[ratan-ui-dropdown-data-source]] lists controls across Cashflow Blotter, Grouping Blotter, Dashboard, Cashflow Details — Vostro Exception, and Nostro Static. Both `Current Data Source` and `Proper Data Source` are blank for all entries.

## Investigation Scope

The investigation should separately resolve:

- Product Taxonomy
- Currency (CCY)
- Booking Entity
- NSTP Exception
- Cashflow State/Sub State/Sub State Type
- Group Status
- Settlement Methods/Settlement Means
- Nostro Static
- Bic Net Flag
- SSI Type
- Msg
- Charges
- Any fields represented by `Other Options in Custom Search`

The answer should not assume that all fields share one service. Each field may have a distinct authoritative owner and frontend-serving endpoint.

## Acceptance Criteria

The question is resolved when each field has a documented owner and serving contract, and when repeated fields have confirmed code, label, entitlement, and filtering semantics across all relevant screens.