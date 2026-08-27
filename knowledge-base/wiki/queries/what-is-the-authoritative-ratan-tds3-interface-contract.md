---
type: query
title: What Is the Authoritative RATAN–TDS3 Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, tds3, interface-contract, api, settlement, trade-data]
related: [ratan-tds3-trade-lake-integration, ratan, tds3, razor]
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (TDS3)-29126.md"]
---
# What Is the Authoritative RATAN–TDS3 Interface Contract?

The available interface overview identifies TDS3 as RATAN's source for trade, cashflow, reference, fixing, and spot-rate data, but it does not contain a usable formal contract.

## Evidence

The source documents real-time TDS3 queries, stored trade data, cached identifiers, manual latest-trade-version retrieval, rate-fixing lookup, cashflow processing, and a filtered FX replication route to [[razor]]. Its Interface Specification section contains only an image reference.

## Information Needed

- API endpoints, protocols, authentication, and authorization.
- Request and response schemas, field definitions, and versioning rules.
- Index-to-use-case mapping for Trade, Fixings, and Cashflow indexes.
- Event, batch, and query invocation patterns.
- Data ownership, authoritative-source, and reconciliation responsibilities.
- Trade-filter criteria for the `TDS3 → RATAN → RAZOR` route.
- Delivery guarantees, retries, idempotency, monitoring, and failure recovery.
- Current OLA or SLA terms and confirmed operational owners.

Until supporting specifications are located, [[ratan-tds3-trade-lake-integration]] should be treated as a documented high-level dependency rather than a technical implementation contract.