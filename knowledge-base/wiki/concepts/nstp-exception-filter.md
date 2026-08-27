---
type: concept
title: NSTP Exception Filter
created: 2026-08-24
updated: 2026-08-24
tags: [cashflow-blotter, nstp, exception-filtering, graphql, postgresql]
related: [exception-platform-service, cashflow-exception-read-model-enrichment, nstp, query-service, cash-settlement-cashflow-read-model, cashflow-blotter-query-performance, hot-nstp-rule-exception-reconciliation, what-is-the-canonical-nstp-exception-storage-model, which-cashflow-domain-events-trigger-nstp-exception-refresh, is-the-nstp-exception-regex-filter-compatible-with-cashflow-blotter-performance-slas]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# NSTP Exception Filter

NSTP Exception Filter is a proposed Cashflow Blotter capability that lets users find cashflows by NSTP exception values such as `Pending Affirmation` and `Missing Vostro`.

## Proposed architecture

The proposed implementation uses an event-driven enrichment path:

1. A cashflow event is consumed from `cash_settlement_cashflow_domain_events`.
2. [[query-service]] looks up exception information by `cashflow_id` from the [[exception-platform-service]].
3. A derived exception value is persisted in `cashflow_data` and `cashflow_data_history`.
4. GraphQL operations `cashflowsNew` and `graphCashFlowDetails` expose current and detail-history data.
5. A GUI calls the status-based NSTP exception-code endpoint to populate filter values.

This separates the authoritative exception source from the query-optimized Cashflow Blotter projection. See [[cashflow-exception-read-model-enrichment]].

## Proposed filter contract

The note references a `${RegExp_String}` filter representation and PostgreSQL POSIX regular-expression support. It does not define:

- The GraphQL input type or resolver behavior.
- Whether matching is case-sensitive.
- How special characters are escaped.
- Whether users can submit arbitrary expressions.
- Whether matching is against one value or a multi-value representation.
- The index and query-plan strategy.

A raw regex contract should not be considered performance-safe solely because PostgreSQL supports it. Validation is tracked in [[is-the-nstp-exception-regex-filter-compatible-with-cashflow-blotter-performance-slas]].

## Status-dependent filter options

The proposed REST endpoint maps selected statuses, including `PENDING_OPERATOR` and `PENDING_VERIFICATION`, to available GUI options. This implies that valid or relevant NSTP exception choices may depend on cashflow status.

The design does not specify whether this catalog constrains server-side filtering, merely guides the interface, or is versioned with NSTP rule changes.

## Unresolved semantics

The central ambiguity is how a singular `nstp_exception` field represents an exception platform response containing all exception codes ordered by `exception_time`. The required model must establish stable identifier, display-label, ordering, active-versus-resolved state, and multiple-exception behavior. See [[what-is-the-canonical-nstp-exception-storage-model]].