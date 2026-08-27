---
type: concept
title: Currency Alias Normalization
tags: [currency, canonicalization, cash-settlement, data-lineage, netting]
related: [currency-normalization-layer-ownership, which-service-owns-sgd-to-sgo-normalization, what-is-the-authoritative-sgd-to-sgo-mapping-scope, what-netting-behavior-changes-when-sgd-is-normalized-to-sgo, netting-service, group-management]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Currency Alias Normalization

Currency alias normalization rewrites an incoming currency representation to a canonical representation before dependent processing. This source proposes the mapping:

```text
SGD -> SGO
```

For this scenario, `SGO` is treated as the required downstream representation. The source does not establish whether this is a global mapping or one scoped by entity, product, market, effective date, or source system.

## Required Semantics

A reliable normalization policy should define:

- the authoritative owner of the alias map;
- the processing boundary at which normalization occurs;
- idempotency, so `SGO` remains `SGO`;
- behavior for unknown aliases and any reverse mapping;
- whether the original received value and normalized value must both be retained;
- representation in audit records, logs, UIs, and delivered messages; and
- treatment of historical, cached, and persisted grouping data.

The source's objective is consistent downstream representation, but neither proposed implementation demonstrates that every consumer sees `SGO`.