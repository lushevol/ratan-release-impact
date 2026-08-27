---
type: query
title: What Is the Notification Service WebSocket Reconnection and Delivery Contract?
tags: [websocket, notifications, reconnection, reliability, open-question]
related: [websocket-notification-delivery, notification-service, cash-settlement-home-page, entitlement-based-notification-delivery]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
---
# What Is the Notification Service WebSocket Reconnection and Delivery Contract?

The draft requires cluster-based WebSocket connectivity and automatic client reconnection when a node is unavailable or restarting. It does not provide an implementable recovery or delivery contract.

## Questions to resolve

- What WebSocket protocol, endpoint format, and handshake sequence are required?
- How does the client discover an alternate cluster node?
- Which failures are retryable, and what retry delay, backoff, jitter, and retry limit apply?
- Does reconnecting restore a session, create a new session, or require reauthentication?
- What delivery guarantee applies: at-most-once, at-least-once, or effectively-once?
- How are duplicate notifications, ordering, and missed notifications handled?
- How does notification history synchronize with messages delivered after reconnection?
- What monitoring and acceptance tests prove node-failover behavior?

The related ambiguity between auto-reconnection and connection blocking should be resolved together with [[what-error-codes-and-client-actions-govern-notification-connection-failures]].