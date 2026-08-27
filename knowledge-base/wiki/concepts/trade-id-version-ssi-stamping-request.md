---
type: concept
title: Trade ID and Version SSI Stamping Request
created: 2026-08-23
updated: 2026-08-23
tags: [ssi-stamping, api-contract, trade-id, versioning, uber]
related: [ssi-stamping-service, uber, tl, cdups-ssi-stamping-integration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# Trade ID and Version SSI Stamping Request

The proposed SSI stamping request identifies an `uber` message with a `trade ID` and `version` rather than passing the complete message payload. The stated rationale is that the full `uber` message may be too large.

This approach makes [[entities/tl]] retrieval part of the service interaction. The requirement does not define the identifier format, version semantics, lookup interface, authorization, timeout behavior, unavailable-version response, correlation key, or idempotency behavior.

“Latest major version,” used for cashflow materialization, is related but not defined as identical to the request's `version` field.