---
type: entity
title: Exception Platform
created: 2026-08-24
updated: 2026-08-24
tags: [exception-handling, NSTP, rule-service, cash-settlement, API]
related: [multiple-cashflow-exception-handling, exception-operation-level, cash-settlement-exception-handling, rule-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Multiple Exception Handling Design.md"]
---
# Exception Platform

The Exception Platform is the proposed service boundary for storing cash settlement exceptions, their statuses, action definitions, metadata, and cashflow-version correlation.

## Exception representation

A platform exception contains:

- Original exception identifier.
- Business flow and source system.
- Exception code, type, category, and description.
- Available actions and their API details.
- Metadata and entity correlation.
- Tracking identifier and exception timestamp.
- Current status.

The source defines three exception types:

```text
TECHNICAL
BUSINESS
TECHNICAL_VISIBLE
```

The common exception statuses are:

```text
PENDING_OPERATOR
PENDING_VERIFICATION
CLOSED
```

## API responsibilities

The proposed platform supports:

- Exception list queries by entity and entity version.
- Exception action-data and metadata queries.
- Exception submit, approve, and reject operations.
- Rule creation, confirmation, cancellation, deletion, and history.
- NSTP and suppression-rule checks.
- Special NSTP rule configuration.

The copied Rule Service URLs are inconsistent and in several places contain malformed duplicated path fragments. They should be verified against the deployed service before documentation or client implementation.