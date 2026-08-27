---
type: query
title: What Is the Authoritative SGD to SGO Mapping Scope?
tags: [open-question, currency, mapping-governance, data-lineage]
related: [currency-alias-normalization, currency-normalization-layer-ownership, which-service-owns-sgd-to-sgo-normalization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# What Is the Authoritative SGD to SGO Mapping Scope?

What authority defines `SGD → SGO`, and under which business, technical, temporal, and source-system conditions does the mapping apply?

## Unspecified Policy Elements

The source assumes the mapping but does not specify:

- whether it is permanent or effective-dated;
- whether it is global or scoped by entity, market, product, or source;
- whether `SGO` is a technical alias or a separate business currency;
- handling for already-normalized, unknown, or reverse-mapped values;
- ownership and governance of the mapping table; or
- audit requirements for preserving source `SGD` alongside normalized `SGO`.

A mapping contract is needed before either proposed implementation can be evaluated as complete.