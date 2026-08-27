---
type: entity
title: Single-UI-Authorization
tags: [http-header, websocket, jwt, authentication]
related: [notification-service, websocket-notification-delivery, entitlement-based-notification-delivery]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
---
# Single-UI-Authorization

`Single-UI-Authorization` is the custom header identifier specified by the draft notification design as the carrier for the JWT supplied by the frontend.

The source states that the JWT must be placed in this header, but does not define the value syntax, such as a `Bearer ` prefix; whether the header is sent during the WebSocket upgrade or another request; token-refresh behavior; or safeguards against token exposure through logs and proxies.