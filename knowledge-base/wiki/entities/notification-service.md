---
type: entity
title: Notification Service
tags: [notifications, backend-service, websocket, authorization]
related: [cash-settlement-home-page, websocket-notification-delivery, entitlement-based-notification-delivery, single-ui-authorization]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
---
# Notification Service

Notification Service is the backend service named in the draft notification design as the target of the Cash Settlement Home Page's notification connection.

## Stated responsibilities

- Accept a notification connection through a WebSocket cluster.
- Receive the frontend-supplied JWT through `Single-UI-Authorization`.
- Derive the user's entitlements from the token.
- Decide which kinds of messages are eligible for delivery to that client.

The source does not establish deployment ownership, event sources, message schemas, endpoint formats, or whether this is a distinct deployed service rather than a logical capability.