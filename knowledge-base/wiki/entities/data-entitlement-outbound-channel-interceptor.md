---
type: entity
title: DataEntitlementOutboundChannelInterceptor
created: 2026-08-24
updated: 2026-08-24
tags: [data-entitlement, websocket, spring, outbound-messaging, query-service]
related: [query-service, websocket-session-handler, websocket-zombie-session, websocket-session-lifecycle-and-pure-lookup, cash-settlement-data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Race condition zombie session issue in cashflow notification.md"]
---
# DataEntitlementOutboundChannelInterceptor

`DataEntitlementOutboundChannelInterceptor` is an outbound WebSocket messaging interceptor in the [[query-service]] cashflow-notification path. It obtains session information during `ClientOutboundChannel` processing, where message handling can occur after a client has disconnected.

The incident identifies its use of `WebSocketSessionHandler.getSession()` as the immediate source of registry corruption. That method creates a new entry when the requested session ID is absent. During a disconnect race, the newly created object contains the session ID but no authenticated user name, creating a [[websocket-zombie-session]].

The proposed remediation is to use `getSessionById(accessor.getSessionId())`. A missing result should be treated as an expected stale-delivery condition: log the event and drop the outbound message. This preserves the distinction between session creation during authenticated connection establishment and non-mutating lookup during delivery.

The source does not verify whether `return null` is the correct channel-interceptor behavior for the deployed Spring configuration; that implementation contract requires validation before release.