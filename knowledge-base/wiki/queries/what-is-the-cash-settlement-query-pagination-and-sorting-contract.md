---
type: query
title: What Is the Cash Settlement Query Pagination and Sorting Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, graphql, pagination, sorting, query-api]
related: [cashflow-ultra-query, cashflow-ultra-query-count, cash-settlement-advanced-query-dsl]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Settlement Advanced Search Design.md"]
---
# What Is the Cash Settlement Query Pagination and Sorting Contract?

The API schema exposes `PAGE_INDEX`, `CURSOR`, and `NO_PAGINATION`, but only page-index pagination is implemented. It also exposes `orderArgs`, while custom sorting remains a placeholder.

Resolve:

- page-index numbering and bounds;
- maximum `itemsPerPage`;
- default created-time ordering and direction;
- supported custom sort fields, tie-breaking, and null ordering;
- cursor encoding, validity, and result-consistency guarantees;
- behavior for unimplemented paging modes;
- whether full-dataset retrieval is ever permitted.

These rules are required for predictable result browsing in [[cashflow-ultra-query]].