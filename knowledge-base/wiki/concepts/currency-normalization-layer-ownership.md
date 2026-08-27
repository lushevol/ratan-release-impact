---
type: concept
title: Currency Normalization Layer Ownership
tags: [architecture, currency-normalization, standardization, netting, ownership]
related: [currency-alias-normalization, group-management, standardization-module, netting-service, which-service-owns-sgd-to-sgo-normalization, what-netting-behavior-changes-when-sgd-is-normalized-to-sgo]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Online Offline currency conversion solution.md"]
created: 2026-08-24
updated: 2026-08-24
---
# Currency Normalization Layer Ownership

Currency normalization layer ownership is the architectural choice of where a canonicalization rule is applied so all required consumers operate on a consistent value.

The source presents two unapproved alternatives for `SGD → SGO`:

- [[group-management]]: normalize in the Standardization Module through an ordered `StandardizationCommand`.
- [[netting-service]]: normalize retrieved `CashFlowQueryResult.settlementCurrency` and extend the rule through manual netting, validators, grouping, IRS, and auto-netting paths.

## Evaluation Criteria

The appropriate owner must be assessed against:

- consumer coverage, including manual netting and external delivery;
- preservation of original-value lineage and auditability;
- consistency across retrieval, validation, grouping, IRS, and auto-netting;
- effects on group-key identity and existing netting results;
- operational rollback and reprocessing behavior; and
- testable evidence that the normalized value is visible at every required boundary.

The source identifies a coverage risk for Group Management and a broad-change risk for Netting Service. It does not select an owner.