---
type: comparison
title: Stella Ambassador vs Cashflow Lifecycle Service
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, stella, integration, ownership]
related: [ratanone-stella-ambassador, ratan-cashflow-lifecycle-service, stella-cashflow-status-synchronization]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Stella Ambassador vs Cashflow Lifecycle Service

[[ratan-cashflow-lifecycle-service]] owns the Ratan-side production of status-update commands and consumption of response messages.

[[ratanone-stella-ambassador]] owns consumption of those commands, invocation of Stella through `sabre-booking-api`, and publication of Stella result events.

The source does not assign ownership for prevalidation of invalid Stella transitions, durable Trade Lake confirmation, or recovery after `TL_RETRY_ERROR`.