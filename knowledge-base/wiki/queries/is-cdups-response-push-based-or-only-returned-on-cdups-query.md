---
type: query
title: Is the CDUPS Response Push-Based or Only Returned on a CDUPS Query?
created: 2026-08-23
updated: 2026-08-23
tags: [cdups, notifications, ssi-stamping, integration, solace]
related: [cdups, cdups-ssi-stamping-integration, ssi-stamping-notification, ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# Is the CDUPS Response Push-Based or Only Returned on a CDUPS Query?

The meeting notes state that Vostro refresh, Nostro refresh, and approved ad-hoc SSI actions are not published to CDUPS and that CDUPS retrieves results on a call-based basis. The business-case tables nevertheless say that the SSI Stamping Service sends the latest result to CDUPS.

The intended interaction pattern—synchronous query response, asynchronous request/reply, event push, or a combination by event type—must be specified before implementation.