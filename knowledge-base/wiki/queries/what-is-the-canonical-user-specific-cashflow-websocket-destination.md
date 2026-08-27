---
type: query
title: What Is the Canonical User-Specific Cashflow WebSocket Destination?
created: 2026-08-24
updated: 2026-08-24
tags: [websocket, cashflow, spring, data-entitlement, notification]
related: [cashflow-blotter, query-service, cash-settlement-data-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
---
# What Is the Canonical User-Specific Cashflow WebSocket Destination?

The main design directs clients to subscribe to:

```text
/user/{username}/cashflow/notification
```

A review note instead requires:

```text
/user/{username}/queue/cashflow/notification
```

The server-side pattern is:

```java
messagingTemplate.convertAndSendToUser(username, "/cashflow/notification", event);
```

## Questions

- Which client subscription destination is canonical in the deployed Spring messaging configuration?
- Does the configured user-destination prefix or broker mapping require the `/queue` segment?
- Which destination is covered by `DataEntitlementOutboundChannelInterceptor#preSend`?
- What migration and compatibility behavior applies to clients currently subscribed to `/cashflow/notification`?