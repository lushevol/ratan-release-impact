---
type: entity
title: ratanone-stella-ambassador
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, integration-service, stella, messaging]
related: [stella, ratan-cashflow-lifecycle-service, sabre-booking-api, stella-cashflow-status-synchronization, stella-batch-and-single-status-updates]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# ratanone-stella-ambassador

`ratanone-stella-ambassador` is the Ratan integration service between [[ratan-cashflow-lifecycle-service]] and [[stella]].

It consumes single and batch status-update commands, invokes Stella through the SDK, and publishes Stella result events to the corresponding response topics. The source identifies wrapper classes including `StellaSingleMessageApi`, `AbstractStellaApiWrapper`, and `StellaApiCallExecutor` in the timeout call path.

An acknowledgement received by this service must not be assumed to confirm durable synchronization to [[trade-lake]].