---
type: concept
title: Cashflow Exception Read-Model Enrichment
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, read-model, cashflow, exceptions, event-driven-architecture, history]
related: [nstp-exception-filter, exception-platform-service, query-service, cash-settlement-cashflow-read-model, cashflow-status-write-back, hot-nstp-rule-exception-reconciliation, which-cashflow-domain-events-trigger-nstp-exception-refresh, what-is-the-canonical-nstp-exception-storage-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# Cashflow Exception Read-Model Enrichment

Cashflow Exception Read-Model Enrichment is the proposed pattern of copying exception information from an authoritative exception service into cashflow query models for display, filtering, and history.

## Proposed application

The design proposes adding `nstp_exception` to both `cashflow_data` and `cashflow_data_history`. A consumer of `cash_settlement_cashflow_domain_events` would use the cashflow identity in an event to obtain exception data from the [[exception-platform-service]], then update the cashflow projections.

The current table supports Cashflow Blotter queries; the history table supports detail-history consistency and audit-oriented display.

## Projection requirements

A reliable implementation needs explicit rules for:

- Which event types trigger enrichment.
- Which exception state is projected when a cashflow has multiple exceptions.
- How `exception_time` establishes ordering.
- Whether resolved or cleared exceptions remain in current and historical projections.
- Idempotent handling of duplicate events.
- Out-of-order event and response handling.
- Retry and reconciliation behavior when the external exception service is unavailable.
- Backfill of rows predating the feature.
- Atomicity or recoverability when current and history projections are updated.

The source does not define these rules. Its status-event example is plausible input evidence but is not an approved trigger policy.

## Read-model boundary

This pattern complements [[cash-settlement-cashflow-read-model]]: a read model may carry denormalized data optimized for application queries without becoming the source of truth for exception lifecycle. The projected value must be designed carefully if it is used for user-visible filtering and historical interpretation.