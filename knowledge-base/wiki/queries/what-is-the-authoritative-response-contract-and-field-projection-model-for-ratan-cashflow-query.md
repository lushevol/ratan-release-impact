---
type: query
title: What Is the Authoritative Response Contract and Field Projection Model for RATAN Cashflow Query?
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, cashflow, api-contract, projection, compatibility]
related: [ratan-cashflow-lifecycle-service, cashflow-query-api-performance-optimization, lien-aware-netting-and-auto-unnetting, trade-lien-notification-reconciliation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2025 changes/Cashflow query api optimization.md"]
---
# What Is the Authoritative Response Contract and Field Projection Model for RATAN Cashflow Query?

## Question

Do `/v1/ratan/cashflow/query` and `/v1/ratan/cashflow/query/cashflowIds` return a canonical full response, support explicit categories or projections, or provide caller-specific response forms?

## Known evidence

Callers have non-identical data requirements. Some require a narrow lifecycle subset or affirmation details, while netting operations require combined data from `ratan_cashflow_scbml_history`, `ratan_stella_message_event_source`, and `Ratan_Cashflow_Scbml_Message`.

The source proposes category-based fetching but does not define request parameters, DTO schemas, category names, field nullability, endpoint semantics, response ordering, duplicate-ID handling, versioning, or partial-failure behavior.

## Decisions needed

- Define the authoritative response schema for each endpoint.
- Define whether projections are internal-only or part of the public API contract.
- Specify field presence and nullability guarantees for each category.
- Specify batch ordering, duplicate IDs, missing IDs, and partial-result semantics.
- Define compatibility and versioning controls for consumers.
- Confirm snapshot and consistency expectations for lock-sensitive netting and lien workflows.

## Risk

An undocumented projection model can silently remove fields needed for unnetting, splitting, amount amendment, or lien placement. These dependencies are particularly sensitive to lifecycle status, versions, and `nettingId`.