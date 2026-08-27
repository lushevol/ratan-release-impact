---
type: entity
title: RATAN_DATA_ENTITLEMENT
created: 2026-08-24
updated: 2026-08-24
tags: [RATAN, data-entitlement, EMS2, authorization]
related: [ems2, data-entitlement, ems2-entitlement-lookup, auth-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md"]
---
# RATAN_DATA_ENTITLEMENT

`RATAN_DATA_ENTITLEMENT` is the EMS2 entitlement entity used for RATAN data access.

The documented example associates the entity with the `RATAN` system and returns:

- Role: `Global`
- Action: `VIEW_ENTITLEMENT`
- Entity state: `locked: true`
- Result count: `1`

The source does not establish that `Global` is the only available role or that it grants unrestricted access to all RATAN data.