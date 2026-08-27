---
type: query
title: What Is the Canonical Cashflow Storage and History Model?
tags: [cashflow, storage, history, versioning, data-model, cash-settlement]
related: [cashflow-lifecycle-service, cash-settlement-cashflow-read-model, cashflow-standing-settlement-instructions, trade-standing-settlement-instructions, cash-settlement-data-store-requirements]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement Data Store Requirements.md"]
---
# What Is the Canonical Cashflow Storage and History Model?

The source requires both latest-payment views and historical queries while showing a broad nested cashflow structure containing trade, SSI, entity, portfolio, payment, state, and netting data. It does not define the authoritative storage model.

## Questions to Resolve

- Which service owns the canonical cashflow record?
- Is the displayed model a canonical aggregate, immutable event history, temporal tables, a materialized read model, or a composition of service-owned records?
- How are `Cashflow_Version`, `Payment_Version`, business versions, minor versions, and historical corrections related?
- What update, deletion, replay, and retention semantics apply to cashflow records and raw [[stella]] messages?
- Which fields have native boolean, numeric, timestamp, identifier, and nullable types?
- How are SSI account details and audit-related records authorized and protected?

## Evidence

[[cash-settlement-data-store-requirements]] demonstrates the required read surface but explicitly does not supply an approved persistence schema or data-lifecycle contract.