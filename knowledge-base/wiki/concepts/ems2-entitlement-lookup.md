---
type: concept
title: EMS2 Entitlement Lookup
created: 2026-08-24
updated: 2026-08-24
tags: [EMS2, entitlement-management, authorization, RATAN]
related: [ems2, function-entitlement, data-entitlement, ratan-data-entitlement, auth-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# EMS2 Entitlement Lookup

EMS2 entitlement lookup is the retrieval of authorization records for a user account or a specific entitlement entity.

The source documents two lookup patterns:

- An account lookup for function and application entitlements.
- An entity-and-user lookup for the `RATAN_DATA_ENTITLEMENT` data-entitlement entity.

These lookups provide separate inputs for [[function-entitlement]] and [[data-entitlement]]. The source does not define how multiple returned roles are combined or how EMS2 unavailability affects authorization.