---
type: query
title: What Is the Canonical Advanced Search Filter Schema and Query Semantics?
tags: [advanced-search, query-builder, filter-schema, boolean-logic, open-question]
related: [settlement-advanced-search, nested-boolean-advanced-search, cash-settlement-home-page, what-is-the-opensearch-index-schema-for-cashflow-querying]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design/Ratan Advanced Search Guide.md"]
---

# What Is the Canonical Advanced Search Filter Schema and Query Semantics?

## Question

What persisted and executable contract represents Settlement Advanced Search filters after the introduction of duplicate fields across groups, level-specific `AND`/`OR` combinators, and nested groups?

## Evidence

The [[25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--33-settlement-advanced-search-design--8w31f5]] source states that:

- Duplicate fields are allowed in different groups.
- Combinators support `AND` and `OR` according to the level.
- Multiple groups may be nested to a maximum depth of 3.
- Filter records and filter CRUD remain unchanged.

## Required resolution

The authoritative design should specify:

1. The JSON, database, or API schema for filter groups, filter items, operators, values, and combinators.
2. Whether the root group counts toward the depth limit.
3. Boolean evaluation and precedence for mixed items and nested groups.
4. Whether duplicate fields are allowed within one group.
5. Valid field/operator combinations and validation errors.
6. Empty-group and empty-value behavior.
7. Migration and rendering rules for legacy flat, all-`AND` saved filters.
8. Execution and authorization behavior.

The answer should be cross-referenced with [[what-is-the-opensearch-index-schema-for-cashflow-querying]] if the same field and operator contract governs indexed search.