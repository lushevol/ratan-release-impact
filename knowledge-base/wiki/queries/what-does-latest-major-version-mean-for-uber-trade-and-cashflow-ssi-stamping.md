---
type: query
title: What Does Latest Major Version Mean for uber Trade and Cashflow SSI Stamping?
created: 2026-08-23
updated: 2026-08-23
tags: [uber, versioning, cashflow, ssi-stamping, tl]
related: [uber, tl, trade-id-version-ssi-stamping-request, latest-cashflow-ssi-result, ssi-stamping-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/Trade Cashflow SSI Stamping on Uber Message.md"]
---
# What Does Latest Major Version Mean for uber Trade and Cashflow SSI Stamping?

The requirement says that materialized cashflows query the trade SSI stamping result using the latest major version. It does not define the version source, major/minor semantics, snapshot consistency, historical replay behavior, or whether a static-data refresh creates a new trade version.

The team must establish how a cashflow selects the applicable version and how that selection interacts with re-stamping and result retention.