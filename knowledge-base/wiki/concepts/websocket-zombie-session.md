---
type: concept
title: WebSocket Zombie Session
created: 2026-08-24
updated: 2026-08-24
tags: [websocket, session-lifecycle, race-condition, cashflow-notification, reliability]
related: [websocket-session-lifecycle-and-pure-lookup, websocket-session-handler, data-entitlement-outbound-channel-interceptor, query-service-web-broker, how-are-disconnected-cashflow-notifications-recovered]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Race condition zombie session issue in cashflow notification.md"]
---
# WebSocket Zombie Session

A WebSocket zombie session is a stale session-registry entry that remains after the real client connection has disconnected. In the documented cashflow-notification incident, the zombie has the ID of a removed session but `name = null`, because it is reconstructed from outbound message metadata rather than through authenticated WebSocket `CONNECT` processing.

## Creation Pattern

The failure requires two concurrent activities:

1. Disconnect handling removes the authenticated session after a SockJS buffer-overflow disconnect.
2. An outbound message already queued on an asynchronous channel performs a create-if-absent lookup for that session ID.

If lookup mutates the registry, it reinserts an incomplete session after cleanup has occurred. Since the disconnect event has already been consumed, ordinary disconnect cleanup does not run again for the replacement entry.

## Consequences

A zombie session can:

- make an active-session count include inactive clients;
- inflate the reported broadcast total;
- trigger repeated `convertAndSendToUser(null, ...)` failures;
- generate avoidable logging, CPU, and entitlement-processing load;
- persist indefinitely as further disconnect races create additional entries.

The appropriate correction is not to infer or reconstruct identity after disconnect. Instead, delivery code must use a pure lookup and drop messages whose target session no longer exists. See [[websocket-session-lifecycle-and-pure-lookup]].