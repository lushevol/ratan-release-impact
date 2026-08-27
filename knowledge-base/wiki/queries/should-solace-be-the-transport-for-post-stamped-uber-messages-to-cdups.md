---
type: query
title: Should Solace Be the Transport for Post-Stamped uber Messages to CDUPS?
created: 2026-08-23
updated: 2026-08-23
tags: [solace, uber, cdups, messaging, architecture]
related: [solace, cdups, uber-message-ssi-stamping, cdups-ssi-stamping-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# Should Solace Be the Transport for Post-Stamped uber Messages to CDUPS?

Solace is proposed as a possible transport because the post-stamped `uber` message may be large. The source also contains wording that treats Solace as though it is already selected, but the meeting notes explicitly say that the option requires further assessment.

The decision should compare message size, latency, request/reply behavior, delivery guarantees, replay, security, operational support, failure handling, and alternatives such as a direct API.