---
type: concept
title: Cashflow Status Result Events
created: 2026-08-24
updated: 2026-08-24
tags: [events, stella, correlation, error-handling]
related: [ratanone-stella-ambassador, ratan-cashflow-lifecycle-service, stella-trade-lake-reconciliation, message-header-propagation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Cashflow Status Result Events

Cashflow status result events are published by `ratanone-stella-ambassador` after Stella processing and consumed by `ratan-cashflow-lifecycle-service`.

Successful examples preserve `commandId`, `trackingId`, `cashflowId`, `correlationId`, `businessVersion`, `cashflowVersion`, `stellaCashflowVersion`, `processStatus`, and `stellaStatus`. A documented `TL_RETRY_ERROR` failure leaves `cashflowId`, `correlationId`, `businessVersion`, and `cashflowVersion` as `null`.

This incomplete failure correlation makes recovery and reconciliation an unresolved contract concern.