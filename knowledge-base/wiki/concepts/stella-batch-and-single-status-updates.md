---
type: concept
title: Stella Batch and Single Status Updates
created: 2026-08-24
updated: 2026-08-24
tags: [kafka, messaging, stella, batch-processing]
related: [ratan-cashflow-lifecycle-service, ratanone-stella-ambassador, cashflow-status-result-events, message-topic-consolidation, message-header-propagation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Strategic Cashflow Stella Ambassandor.md"]
---
# Stella Batch and Single Status Updates

The integration separates scheduled batch commands from individually triggered commands.

- Batch commands use `Cashflow_Status_Batch_Command_In`; responses use `Cashflow_Status_Batch_Response_In`.
- Single commands use `Cashflow_Status_Command_In`; responses use `Cashflow_Status_Response_In`.
- Result routing is documented for event types `ALL` and `BROADCAST`, with API types `BATCH` and the source's spelling `SIGNLE`.

Proposed `Cash_Settlement_*` response-topic names were explicitly not implemented in the source. See [[what-is-the-authoritative-stella-strategic-cashflow-topic-contract]].