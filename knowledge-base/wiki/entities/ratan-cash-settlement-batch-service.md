---
type: entity
title: ratan-cash-settlement-batch-service
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, batch-processing, murex, solace, gdc, indonesia]
related: [ratanone-message-bridge, indonesia-hybrid-gdc-id-message-flow, solace, ratan-indonesia-onshoring-2026]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/Indonesia Development Integration Plan.md"]
---
# ratan-cash-settlement-batch-service

`ratan-cash-settlement-batch-service` is the batch-processing service listed for the Indonesia UAT release as `51358-ratan-cash-settlement-batch-service`.

The plan states that Batch is **GDC only** and that Indonesia does not deploy this service. It must publish messages to `Cash_Settlement_Mxg_Inbound_Batch_All` for [[ratanone-message-bridge]] to consume. The release table identifies “Fixing flag changes,” a mandatory GDC deployment dependency, release branch `release/v2.1.0`, and UAT deployment owner `@Haolin Song`.

The document does not specify the topic schema, acknowledgement policy, processing order, replay behaviour, or whether GDC-only placement is transitional or steady state.