---
type: entity
title: Cashflow Lifecycle Service
tags: [cashflow, payments, storage, service]
related: [cash-settlement-platform, cash-settlement-cashflow-read-model, cash-settlement-data-store-requirements]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md"]
---
# Cashflow Lifecycle Service

The Cashflow Lifecycle Service is named as the owner of cashflow storage for the Cash Settlement Platform.

Its required data supports payment-list and payment-detail views, historical queries, economics, payment status, SSI information, and downstream processing messages such as FMSRE. The source does not clarify whether this service owns the canonical cashflow aggregate, a read model, or both.

See [[cash-settlement-cashflow-read-model]] and [[what-is-the-canonical-cashflow-storage-and-history-model]].