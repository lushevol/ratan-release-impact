---
type: entity
title: Exception Platform Service
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, nstp, exceptions, service, api]
related: [query-service, nstp, nstp-exception-filter, cashflow-exception-read-model-enrichment, what-is-the-canonical-nstp-exception-storage-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Cashflow Blotter Dashboard add NSTP exception filter.md"]
---
# Exception Platform Service

The Exception Platform Service is the proposed source of NSTP exception information for Cashflow Blotter filtering.

## Proposed responsibilities

According to the design note, [[query-service]] calls this service with a `cashflow_id` to retrieve all associated exception codes, ordered by `exception_time`. The service also exposes a status-based catalog endpoint for GUI exception-filter options:

```http
POST /v1/rep/exceptions/nstpExceptionCodes/byStatus
```

The endpoint accepts cashflow statuses and returns NSTP exception options containing `label`, `value`, and `exceptionCategory`.

## Authority boundary

The design implies that this service is authoritative for exception history, while `cashflow_data` and `cashflow_data_history` are denormalized read models. It does not define whether the service provides active, resolved, repeated, or complete historical exceptions, nor how exception clearing is represented.

## Open integration requirements

The source leaves the following requirements unspecified:

- The exact exception retrieval response contract.
- Whether `exception_code` is a stable identifier distinct from the GUI label.
- Selection rules when several exceptions exist for one cashflow.
- Availability, timeout, retry, and idempotency behavior.
- Whether calls occur synchronously within event processing or asynchronously.
- Whether the status-based option catalog is governed by the same exception model as cashflow-level retrieval.

These questions are central to [[nstp-exception-filter]] and [[what-is-the-canonical-nstp-exception-storage-model]].