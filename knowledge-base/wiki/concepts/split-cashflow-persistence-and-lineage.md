---
type: concept
title: Split Cashflow Persistence and Lineage
tags: [cashflow-splitting, lineage, persistence, versioning, ratan]
related: [cashflow-splitting, splitting-cashflow, split-cashflow-api-contract, split-cashflow-withdrawal-propagation]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Splitting/Splitting Tech Design.md"]
---
# Split Cashflow Persistence and Lineage

Split lineage links a parent cashflow and its children through a split-group identifier while retaining each cashflow's own identifier and version.

The documented `splitting_cashflow` table records `splitting_id`, `cashflow_id`, `business_version`, and `minor_version`, together with amounts, currency, participants, payment date, status, action, and split type. It has indexes for individual cashflow and split-group retrieval.

Unsplit requests include parent cashflow identity, business version, minor version, and `splittingId`, confirming that reversal is version-sensitive. The design does not define which identifier is canonical across manual split, automatic split, unsplit, amendment, and external query use.

The source represents money as text in persistence and API payloads. Validation of numeric format, scale, currency consistency, and aggregate child totals remains unspecified.

See [[what-is-the-canonical-splitting-id-and-rule-unique-id-contract]].