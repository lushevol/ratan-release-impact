---
type: concept
title: Nested Boolean Advanced Search
tags: [advanced-search, query-builder, boolean-logic, filter-groups]
related: [settlement-advanced-search, what-is-the-canonical-advanced-search-filter-schema-and-query-semantics, cash-settlement-home-page]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design/Ratan Advanced Search Guide.md"]
---

# Nested Boolean Advanced Search

Nested Boolean Advanced Search is a query-builder model in which individual field predicates are organized into groups, and each level applies an `AND` or `OR` combinator to its members.

## Model described by the source

A filter consists conceptually of:

- **Filter items:** individual field, operator, and value predicates.
- **Filter groups:** collections of filter items and potentially nested groups.
- **Combinators:** `AND` or `OR` logic applied at a level.
- **Nested structure:** multiple groups arranged hierarchically, with a stated maximum nesting depth of 3.

The design also permits the same field to appear in different groups. It does not state whether a field may be repeated within one group.

## Contrast with the prior model

The prior model used one root group and combined all filter items with `AND`. The proposed model supports grouped Boolean logic, allowing expressions that cannot be represented by a single globally conjunctive list.

## Unspecified semantics

The source does not define:

- Whether the root group is counted as depth 1.
- Operator precedence when items and child groups coexist.
- Whether combinators apply uniformly to all group members.
- Empty-group behavior.
- Validation errors for excessive nesting.
- Serialization or query translation rules.

These issues are tracked in [[what-is-the-canonical-advanced-search-filter-schema-and-query-semantics]].