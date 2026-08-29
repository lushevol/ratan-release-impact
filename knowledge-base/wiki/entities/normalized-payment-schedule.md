---
type: entity
title: NormalizedPaymentSchedule
created: 2026-08-24
updated: 2026-08-24
tags: [uber, payment-schedule, cashflow, aggregation]
related: [product-agnostic-cashflow-aggregation, normalized-payment-schedule-completeness-check, netting-service, cashflow, tdsx-uber-message-listener, what-is-the-authoritative-normalized-payment-schedule-schema-and-versioning-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# NormalizedPaymentSchedule

`NormalizedPaymentSchedule` is an element carried in UBER messages and proposed as the basis for determining the expected number of cashflow payment legs in automatic aggregation.

The draft design requires the service that splits an UBER message into cashflow-level messages to preserve and forward this element. The source references schedule-element currency, `paymentDate`, and `payment_type`, but does not define a complete schema, identifiers, versioning, producer ownership, or update lifecycle.

## Proposed Use

For a given cashflow, [[netting-service]] is intended to count schedule entries with matching currency and payment date, excluding Fee entries. This count becomes `expected_num` in the proposed [[normalized-payment-schedule-completeness-check]].

The structure is not yet established as authoritative. Consumers need a defined contract for absent, malformed, revised, and replayed schedules; see what is the authoritative normalized payment schedule schema and versioning contract.