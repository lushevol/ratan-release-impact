---
type: concept
title: Cash Settlement Cashflow Read Model
tags: [cashflow, read-model, payment-history, graphql, ssi, cash-settlement]
related: [cashflow-lifecycle-service, cashflow-standing-settlement-instructions, trade-standing-settlement-instructions, stella, cash-settlement-data-store-requirements, what-is-the-canonical-cashflow-storage-and-history-model]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md"]
---
# Cash Settlement Cashflow Read Model

The Cash Settlement cashflow read model is the user-facing data shape needed to list payments, inspect payment details, and query history.

The illustrated result combines cashflow state and versions with trade identity, data-flow metadata, SSI and account-routing details, instrument data, entity data, portfolio data, payment economics, dates, netting information, and downstream processing context. It is therefore broader than a minimal payment record.

The source’s GraphQL example supports filtering by `Cashflow.Cashflow_Id`, `IN` matching, and paginated results. It does not determine whether this model is a canonical aggregate, a denormalized projection, or a run-time composition of service-owned records. It also leaves current-state versus immutable-history semantics unresolved.

SSI details are relevant to [[cashflow-standing-settlement-instructions]] and [[trade-standing-settlement-instructions]]. The sample’s string representations of apparent booleans and numeric amounts must not be treated as a finalized type contract.