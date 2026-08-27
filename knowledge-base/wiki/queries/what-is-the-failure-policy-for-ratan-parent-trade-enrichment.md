---
type: query
title: What Is the Failure Policy for Ratan Parent-Trade Enrichment?
created: 2026-08-22
updated: 2026-08-22
tags: [ratan, tds3, enrichment, resilience, idempotency]
related: [tds3, ratan-settlement, cashflow-logical-model, scbml-cashflow-ingestion-and-persistence]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Logical Model & Templates/Cashflow Logical Model Fields & Data Store.md"]
---
# What Is the Failure Policy for Ratan Parent-Trade Enrichment?

Ratan is required to query the TDS3 trade API using trade ID plus trade version and persist returned parent-trade attributes with the cashflow.

The requirement does not define behavior when TDS3 is unavailable, returns no matching version, returns stale attributes, or receives a replayed cashflow message.

The required policy should define:

- API ownership and contract;
- blocking versus non-blocking ingestion;
- retry, timeout, and backoff behavior;
- reconciliation and deferred enrichment;
- version-match and stale-data rules;
- duplicate-message idempotency; and
- user visibility and exception ownership when enrichment is incomplete.