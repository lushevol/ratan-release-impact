---
type: source
title: Notification Interaction Wireframe (Draft)
authors: []
year: 2023
url: ""
venue: ""
tags: [cash-settlement, notifications, websocket, ux-wireframe, draft]
related: [cash-settlement-home-page, notification-service, websocket-notification-delivery, entitlement-based-notification-delivery, notification-drawer-interaction, single-ui-authorization, what-is-the-notification-service-websocket-reconnection-and-delivery-contract, what-error-codes-and-client-actions-govern-notification-connection-failures]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
---
# Notification Interaction Wireframe (Draft)

This draft technical-design and UX-wireframe document proposes real-time notifications for the [[cash-settlement-home-page]]. It specifies a clustered WebSocket connection to a [[notification-service]], JWT propagation through `Single-UI-Authorization`, backend entitlement evaluation, and a notification-drawer interaction flow.

The detailed UX behavior is primarily contained in embedded images. The text confirms the scope of message display, notification-history access, drawer closing, and two alternative notification-detail designs, but it does not select a detail option or define the underlying history and read-state behavior.

## Wireframe scope

The source includes wireframes for:

- Workflow
- Show Message
- View Notification History
- Close Notification Drawer
- View Notification Detail Option 1
- View Notification Detail Option 2

The image assets are referenced by the source but their detailed visual content is not available as text:

- `media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--40-notification-interaction-wirefram--rfz80s/image2023-1-16_15-15-5.png`
- `media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--40-notification-interaction-wirefram--rfz80s/image2023-1-16_15-41-12.png`
- `media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--40-notification-interaction-wirefram--rfz80s/image2023-1-16_15-42-21.png`
- `media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--40-notification-interaction-wirefram--rfz80s/image2023-1-16_15-45-30.png`
- `media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--40-notification-interaction-wirefram--rfz80s/image2023-1-16_15-52-4.png`
- `media/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--40-notification-interaction-wirefram--rfz80s/image2023-1-16_15-54-14.png`

## Explicit connection contract

```text
1. Connect to Cluster Based on web socket cluster, test the reconnection that when one node is down or rest, client side can auto reconnect to other server in cluster
2. Error Any block error when connect to notification service, use error code "400 series" first ( will make a further definition according to "The Error Code Standard" ), and client will show error message when disconnected, will not connect. Empty token, expire token, error of token's signature may cause the block error.
3. Header Place the JWT token to header "Single-UI-Authorization"
4. Entitlement FE pass token to BE, backend will get the user's entitlement and judge what kind of message should push to client side
```

## Design intent

The intended architecture is a WebSocket-cluster connection that can reconnect the frontend to another cluster server when a node is unavailable or restarting. The backend evaluates entitlements derived from the supplied JWT and determines which message types may be delivered to the user.

The proposed `400 series` connection-error treatment is provisional and is expected to be refined under *The Error Code Standard*. The source does not define error-code mappings, WebSocket handshake details, JWT syntax or refresh behavior, retry backoff, delivery guarantees, missed-message recovery, or history data semantics.

## Unresolved issues

The text requires auto-reconnection after a cluster-node failure but also says the client “will not connect” after a disconnection error. It does not distinguish retryable transport failures from non-retryable token or authorization failures. This ambiguity is tracked in [[what-is-the-notification-service-websocket-reconnection-and-delivery-contract]] and [[what-error-codes-and-client-actions-govern-notification-connection-failures]].

The two notification-detail wireframe alternatives are not accompanied by a selected option or evaluation criteria. [[notification-drawer-interaction]] records this as an unresolved UX decision.