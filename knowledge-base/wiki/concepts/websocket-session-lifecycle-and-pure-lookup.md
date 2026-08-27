---
type: concept
title: WebSocket Session Lifecycle and Pure Lookup
created: 2026-08-24
updated: 2026-08-24
tags: [websocket, session-lifecycle, concurrency, pure-lookup, data-entitlement]
related: [websocket-zombie-session, websocket-session-handler, data-entitlement-outbound-channel-interceptor, query-service, cash-settlement-data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Race condition zombie session issue in cashflow notification.md"]
---
# WebSocket Session Lifecycle and Pure Lookup

WebSocket session handling must distinguish session creation, authenticated identity assignment, retrieval, and removal. In particular, lookup during asynchronous outbound delivery must not create or restore registry entries.

## Required Lifecycle

1. An authenticated `CONNECT` establishes a session and assigns its user identity.
2. The session registry exposes the active authenticated session for delivery.
3. `SessionDisconnectEvent` removes that session.
4. Outbound work that runs after removal performs a pure lookup.
5. If the session is absent, the message is dropped as stale delivery work.

This lifecycle makes session removal final for a connection instance. A later outbound operation cannot recreate the session from its ID alone because it lacks the authenticated context supplied during `CONNECT`.

## Why Pure Lookup Matters

A create-if-not-exists lookup is appropriate only where callers are authorized to establish new registry state. It is unsafe in an outbound interceptor because asynchronous queues can process messages after a disconnect.

For the documented [[websocket-zombie-session]] incident, `getSessionById()` is the required retrieval operation because it maps to a plain `sessions.get(sessionId)`. The existing create-if-absent `getSession()` method should not be globally redefined without reviewing other callers that may intentionally rely on its creation behavior.

## Delivery Reliability Boundary

Dropping delivery for an absent session protects registry integrity but makes the WebSocket channel best-effort unless a replay, refresh, or reconciliation mechanism is available after reconnect. This boundary must be explicit for cashflow blotter users; see [[how-are-disconnected-cashflow-notifications-recovered]].