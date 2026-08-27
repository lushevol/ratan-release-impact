---
type: concept
title: Entitlement-Based Notification Delivery
tags: [notifications, authorization, entitlements, jwt, backend]
related: [notification-service, single-ui-authorization, websocket-notification-delivery]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
---
# Entitlement-Based Notification Delivery

Entitlement-based notification delivery is the proposed authorization model in which the frontend supplies a JWT to the backend and the backend determines which kinds of notification messages may be pushed to the connected user.

This design places message eligibility enforcement with the [[notification-service]] rather than relying on client-side filtering.

## Unspecified policy details

The draft does not define:

- Entitlement claims or the mapping from claims to notification categories.
- Business scope rules, such as account, trade, or regional eligibility.
- Deny-by-default behavior when claims are absent or ambiguous.
- Reauthorization after entitlement changes or token expiry during an active connection.
- Audit requirements for delivery decisions.