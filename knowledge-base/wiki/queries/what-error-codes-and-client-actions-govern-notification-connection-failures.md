---
type: query
title: What Error Codes and Client Actions Govern Notification Connection Failures?
tags: [notifications, errors, authentication, jwt, websocket, open-question]
related: [websocket-notification-delivery, notification-service, single-ui-authorization, entitlement-based-notification-delivery]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Notification Interaction Wireframe (Draft).md"]
---
# What Error Codes and Client Actions Govern Notification Connection Failures?

The draft provisionally assigns blocking Notification Service connection failures to the `400 series` and refers future refinement to *The Error Code Standard*. It identifies empty tokens, expired tokens, and invalid token signatures as possible blocking conditions.

## Questions to resolve

- What distinct error codes apply to missing, expired, malformed, and incorrectly signed JWTs?
- How are insufficient entitlement, token revocation, server failure, cluster-node failure, and network interruption represented?
- Which conditions permanently stop reconnection, and which display an error while retries continue?
- What user-facing message and remediation action apply to each error class?
- When does the client clear a displayed connection error?
- What observability fields, correlation identifiers, and security controls apply without logging JWT contents?
- How will the final mapping align with *The Error Code Standard*?

This query is necessary because the phrase “will not connect” is not reconciled with the separate requirement for automatic cluster failover.