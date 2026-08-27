---
type: query
title: What Are the Authoritative Mappings for Cashflow Details Page Unmapped Fields?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow-blotter, field-mapping, ui-requirement, open-question]
related: [cashflow-detail-field-projection, cashflow-blotter, cashflow-status-lifecycle, cashflow-lifecycle-supersession-and-audit-history, what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Cashflow Blotter/Cashflow Details page.md"]
---
# What Are the Authoritative Mappings for Cashflow Details Page Unmapped Fields?

The Cashflow Details page requirement names several display areas without logical-model paths, service sources, or semantics:

- Confirmation Status
- Payment Cutoff
- Sub Status
- Action History
- Exceptions

## Why This Matters

The mapped fields establish a clear trade and cashflow projection, but these unmapped areas cannot be implemented consistently without ownership and contracts. In particular, Sub Status must be distinguished from the mapped Cashflow Status (`Cashflow.Cashflow_State`) rather than assumed to be an equivalent lifecycle value.

Action History may be related to [[cashflow-lifecycle-supersession-and-audit-history]], but the requirement does not establish that its events, ordering, retention, or audit semantics are shared. Likewise, the Exceptions section does not identify an exception taxonomy, severity model, owner, or remediation workflow.

## Evidence Needed

Resolve the following for each area:

1. The authoritative logical-model field, service response, or event source.
2. Whether the value is trade-level, cashflow-level, payment-level, or UI-derived.
3. Display formatting, ordering, null behavior, and permissions.
4. For Action History and Exceptions, retention, pagination, ownership, and user actions.
5. For Confirmation Status, whether it represents confirmation, affirmation, or another external workflow.

The field projection documented in [[cashflow-detail-field-projection]] is the available UI evidence. It does not identify the API contract considered by [[what-is-the-authoritative-response-contract-and-field-projection-model-for-ratan-cashflow-query]].