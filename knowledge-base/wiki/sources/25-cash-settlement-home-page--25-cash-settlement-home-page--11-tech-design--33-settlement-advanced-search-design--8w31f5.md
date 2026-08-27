---
type: source
title: Ratan Advanced Search Guide
authors: []
year: 2025
url: "https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7529554"
venue: Azure DevOps
tags: [cash-settlement, advanced-search, query-builder, ui-design]
related: [settlement-advanced-search, nested-boolean-advanced-search, what-is-the-canonical-advanced-search-filter-schema-and-query-semantics, cash-settlement-home-page]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design/Ratan Advanced Search Guide.md"]
---

# Ratan Advanced Search Guide

## Scope

This document describes a proposed change to the Settlement Advanced Search capability in the [[cash-settlement-home-page]]. It refers to Azure DevOps work item [7529554](https://dev.azure.com/sc-ado/FMQPR/_workitems/edit/7529554).

The supplied document ends immediately after the `Usage Guide` heading. It describes the intended design delta but does not provide implementation details, API contracts, persistence schemas, workflow instructions, test results, or acceptance evidence.

## Design comparison

| Compare | Before | After |
| --- | --- | --- |
| Snapshot | ![image-2025-3-19_9-35-43.png](attachments/image-2025-3-19_9-35-43.png) | ![image-2025-3-19_9-35-47.png](attachments/image-2025-3-19_9-35-47.png) |
| Fields Selection | **Not allow** duplicate fields | **Allow** duplicate fields in different groups |
| Operators & Values Selector | No Change | No Change |
| Combinator | All filter items combined with AND, means results should match all filter items. | Logic of filter items regard to the combinator for the level, supporting AND and OR. |
| Group | Only one single Root Group | Multiple group, can be nested. Maximum nested deep is 3. |
| Filter Records | No Change | No Change |
| Create/Modify/Delete Filter | No Change | No Change |
| Permission Control | No Change | No Change |

## Intended changes

The design expands the search interface from a single root group with globally applied `AND` logic to a nested Boolean query builder. The intended behavior includes:

- Duplicate fields may be selected in different groups.
- Filter items may use `AND` or `OR` according to the combinator configured for their level.
- Multiple groups may be created and nested.
- Nesting is limited to a maximum depth of 3.

These behaviors are documented as design intent. The source does not establish that the feature has been implemented or released.

## Unchanged areas

The source marks the following areas as unchanged:

- Operators and values selection.
- Filter-record functionality.
- Create, modify, and delete operations for filters.
- Permission control.

No existing contracts or detailed behavior for these areas are included.

## Missing implementation detail

The source does not define:

- The persisted or API representation of groups, filter items, and combinators.
- Whether the root group counts toward the maximum nesting depth.
- Boolean precedence or evaluation semantics when a group contains both items and nested groups.
- Whether duplicate fields are permitted within the same group.
- Validation and error behavior.
- Migration and backward compatibility for existing saved filters.
- The service or query backend that executes the resulting search.
- Field catalogs, operator compatibility, performance targets, or authorization rules.

The absent `Usage Guide` and unavailable image attachments mean that interaction details cannot be verified from this source.

## Related implementation questions

The missing contract is tracked in [[what-is-the-canonical-advanced-search-filter-schema-and-query-semantics]]. This source does not establish a dependency on [[opensearch]] or [[opensearch-backed-cashflow-querying]].