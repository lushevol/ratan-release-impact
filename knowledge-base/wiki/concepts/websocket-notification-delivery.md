---
type: concept
title: WebSocket Notification Delivery
tags: [websocket, notifications, real-time-delivery, cluster-failover]
related: [cash-settlement-home-page, notification-service, single-ui-authorization, what-is-the-notification-service-websocket-reconnection-and-delivery-contract, what-error-codes-and-client-actions-govern-notification-connection-failures]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
---
# WebSocket Notification Delivery

WebSocket notification delivery is the proposed real-time channel between the [[cash-settlement-home-page]] and the [[notification-service]]. The draft calls for the client to connect through a WebSocket cluster and automatically reconnect to another server if a cluster node goes down or restarts.

## Resilience intent

The design requires testing reconnection after a node outage or restart. It does not specify endpoint discovery, session affinity, retry delay or backoff, retry limits, cluster health criteria, or recovery of notifications missed while disconnected.

## Failure boundary

The source also requires the client to show a connection error when disconnected and says that it “will not connect” for blocking conditions. Empty, expired, and incorrectly signed tokens are identified as possible blockers. The available evidence does not define whether ordinary transport disconnects remain eligible for automatic retry while authentication and authorization failures suppress retry.

The required reconnection, delivery, ordering, duplicate-handling, and recovery contract remains open in [[what-is-the-notification-service-websocket-reconnection-and-delivery-contract]].