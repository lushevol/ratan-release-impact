---
type: query
title: What Is the Canonical Cash Settlement Query DSL?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, query-dsl, graphql, validation]
related: [cash-settlement-advanced-query-dsl, cashflow-ultra-query, cashflow-ultra-query-count]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# What Is the Canonical Cash Settlement Query DSL?

The design specifies that every `LogicFilter` node contains only one of `and`, `or`, or `filters`, but its count-query example contains both `and` and `or` in one node.

Clarify and publish:

- the formal recursive grammar for `LogicFilter`;
- whether root-level and first-child-level `filters` have different cardinality limits;
- how maximum depth is counted and how over-depth requests fail;
- whether `filters` are implicitly conjoined;
- the normalization behavior for single-child logical groups.

A canonical contract is required before UI validation and backend query translation can be considered interoperable.