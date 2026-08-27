---
type: entity
title: Settlement Advanced Search
tags: [cash-settlement, advanced-search, query-builder, user-interface]
related: [cash-settlement-home-page, nested-boolean-advanced-search, what-is-the-canonical-advanced-search-filter-schema-and-query-semantics]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design/Ratan Advanced Search Guide.md"]
---

# Settlement Advanced Search

Settlement Advanced Search is a filtering capability of the [[cash-settlement-home-page]]. The design described in the [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--33-settlement-advanced-search-design--8w31f5]] source expands the feature from a flat filter structure into a nested Boolean query builder.

## Intended capabilities

- Select duplicate fields when the occurrences are in different groups.
- Combine filter items with level-specific `AND` or `OR` combinators.
- Create multiple filter groups.
- Nest groups to a stated maximum depth of 3.

Operators and value selection, saved filter records, filter CRUD operations, and permission control are explicitly marked as unchanged.

## Status and limits of the evidence

The source is a concise design/change summary. It does not confirm implementation, release status, test completion, or acceptance. It also does not define the persisted filter schema, query execution backend, or formal Boolean semantics.