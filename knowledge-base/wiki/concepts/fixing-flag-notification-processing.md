---
type: concept
title: Fixing Flag Notification Processing
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, fixing-flag, event-processing, IRS]
related: [batch-service, lifecycle-service, netting-service, fixing-notification-event-ordering, pending-fixing-and-waiting-another-leg, cashflow-reinstatement-and-replay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Fixing flag notification.md"]
---
# Fixing Flag Notification Processing

Fixing flag notification processing is the proposed end-to-end flow for receiving IRS fixing information, validating and transporting it, applying it to a cashflow, and determining whether the cashflow requires further processing.

## Processing Flow

1. A file is received in the fixing payment transfer area.
2. The [[entities/batch-service]] processes and validates the file.
3. The Batch Service publishes a notification to Kafka.
4. The [[entities/lifecycle-service]] consumes and persists the original notification.
5. The fixing flag is applied to the associated cashflow when eligible.
6. The cashflow is reverted to `queued` for reprocessing when required.
7. The [[entities/netting-service]] evaluates the IRS waiting-fixing-flag rule.

This flow must support notifications that arrive before their corresponding cashflow and notifications that arrive concurrently with a cashflow.

## State and Data Separation

The design distinguishes, implicitly, between:

- The original persisted notification.
- The fixing flag attached to the cashflow.
- The cashflow lifecycle state.
- The state or value displayed by the GUI.

A cancelled cashflow should remain cancelled even when a later notification updates the fixing flag for display. A failed or `techfailed` cashflow may instead be reinstated using a later fixing flag.

## Limitations

The source is not an implementation-ready protocol. It does not define the event schema, file format, Kafka contract, ordering policy, idempotency mechanism, or transaction boundaries.
