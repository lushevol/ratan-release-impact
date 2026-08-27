---
type: query
title: What Are the MXML COMP Event Contract and Processing Semantics for RATAN?
created: 2026-08-24
updated: 2026-08-24
tags: [mxml, comp, ratan, ibm-mq, event-processing, idempotency, reconciliation]
related: [mxml-trade-confirmation-event-integration, murex-korea, ratan, trade-confirmation-driven-payment-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP High Level Solution.md"]
---
# What Are the MXML COMP Event Contract and Processing Semantics for RATAN?

## Question

What MXML contract and processing controls will allow RATAN to safely consume Murex Korea `COMP` events through IBM MQ?

## Known evidence

The source proposes direct MXML publication from [[murex-korea]] to [[ratan]] and RATAN customization to handle `COMP`. It does not provide an MXML schema, event version, identifier mapping, delivery model, or error-handling specification.

## Required resolution

- Specify the MXML schema, versioning policy, and mandatory fields.
- Define the source trade identifier and its mapping to RATAN trade, cashflow, and payment records.
- Define the meaning and allowed lifecycle transitions of `COMP`.
- Establish duplicate detection, idempotency, sequencing, and out-of-order event rules.
- Define retry, dead-letter, replay, and missing-event recovery procedures.
- Define persistence and audit requirements for received events and applied status changes.
- Establish reconciliation between Murex Korea and RATAN.
- Define IBM MQ security, queue ownership, monitoring, alerting, and service-level expectations.