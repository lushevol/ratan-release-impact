---
type: concept
title: Parent-Client Timeout Consistency
created: 2026-08-24
updated: 2026-08-24
tags: [microservices, distributed-systems, API, idempotency, netting]
related: [ratan-distributed-lock-ownership, cross-service-lock-validation, atomic-batch-locking, ratan-cash-settlement-netting-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Design Principle/RATANONE Distributed Lock ReDesign.md"]
---
# Parent-Client Timeout Consistency

Parent-client timeout consistency concerns the case where a parent service times out or crashes while a downstream client continues processing.

For one-to-one payment processing, the likely result is a technical failure that can be recovered through Reinstate or event re-consumption. For one-to-many netting, the parent and client can become out of sync across Netting Service and Lifecycle Service, making the impact more serious.

The source suggests idempotent APIs, parent retries or result reconciliation, suitable Feign timeout settings, and Kafka rebalance configuration. It does not define a complete result-reconciliation protocol or idempotency-key contract.
