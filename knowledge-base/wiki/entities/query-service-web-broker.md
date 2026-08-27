---
type: entity
title: QueryServiceWebBroker
created: 2026-08-24
updated: 2026-08-24
tags: [query-service, websocket, kafka, cashflow-notification]
related: [query-service, websocket-session-handler, data-entitlement-outbound-channel-interceptor, websocket-zombie-session]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Race condition zombie session issue in cashflow notification.md"]
---
# QueryServiceWebBroker

`QueryServiceWebBroker` is the [[query-service]] component that consumes cashflow-change Kafka events and broadcasts them to registered frontend WebSocket sessions on `/cashflow/notification`.

Its documented listener is configured with 36 concurrent consumers. For each registry entry, it calls `SimpMessagingTemplate.convertAndSendToUser(session.getName(), topic, event)`. A zombie entry with `name = null` causes Spring to reject the call with `IllegalArgumentException: User must not be null`.

The broker catches exceptions per session, preventing one invalid entry from terminating the event loop. However, this also allows the same zombie session to generate failures for every subsequent Kafka event. Correctness therefore depends on [[websocket-session-handler]] containing only authenticated, currently connected sessions.

See [[websocket-zombie-session]] for the failure sequence and [[websocket-session-lifecycle-and-pure-lookup]] for the required registry contract.