---
type: entity
title: Trade Service
created: 2026-08-24
updated: 2026-08-24
tags: [trade-service, cash-settlement, event-integration]
related: [trade-service-trade-events, lms-business-event-tracking, what-is-the-lms-integration-contract]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/LMS Integration.md"]
---
# Trade Service

The source associates the business event “trade service got `leid` and trader successfully” with [[trade-service-trade-events]].

It does not establish whether Trade Service receives, resolves, validates, or publishes the `leid` and trader information. The meaning of `leid`, the authoritative data source, message payload, and success criteria are unspecified.