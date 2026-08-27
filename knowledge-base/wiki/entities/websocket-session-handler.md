---
type: entity
title: WebSocketSessionHandler
created: 2026-08-24
updated: 2026-08-24
tags: [websocket, session-registry, query-service, lifecycle]
related: [query-service, query-service-web-broker, data-entitlement-outbound-channel-interceptor, websocket-zombie-session, websocket-session-lifecycle-and-pure-lookup]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Race condition zombie session issue in cashflow notification.md"]
---
# WebSocketSessionHandler

`WebSocketSessionHandler` is the session registry used by [[query-service]] for WebSocket cashflow-notification delivery. It provides the sessions iterated by [[query-service-web-broker]], removes sessions during disconnect handling, and exposes both mutating and pure retrieval paths.

The incident attributes zombie-session creation to the semantic difference between:

- `getSession(session)`, which creates and stores the supplied session object when its ID is absent.
- `getSessionById(sessionId)`, which performs a non-mutating `sessions.get(sessionId)` lookup.

A session removed after `SessionDisconnectEvent` must remain absent. When [[data-entitlement-outbound-channel-interceptor]] invokes the create-if-absent method after asynchronous outbound processing begins, it can insert a replacement session with no authenticated name. The registry can then report dead entries as active and inflate broadcast totals.

The source proposes retaining create-if-absent behavior where it is intentionally needed, while requiring `getSessionById()` for post-connect outbound processing.