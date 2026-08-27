---
type: entity
title: X_RATANONE
created: 2026-08-22
updated: 2026-08-24
tags: [ems2, entitlement, ratanone, authorization, x-ratanone, ratan]
related: [ems2, strategic-cash-settlement-entitlement-model, ratan-one, ratan, fmaa, canonical-ratan-ratanone-service-identity, what-is-the-relationship-between-ratan-and-ratanone]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md", "RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# X_RATANONE

## Role

`X_RATANONE` is an EMS2 entitlement entity.

The Strategic Cash Settlement technical-design source describes it as the single EMS2 entity for Strategic Cash Settlement and states that different RATANONE tiles are controlled by different subjects under this entity.

The RATAN and EMS2-34010 FMAA source states that RATAN retrieves user subjects under `X_RATANONE` during login. According to that source, these subjects determine:

- Which blotters a user can see.
- Which right-click operations or context-menu actions are available in the RATAN UI.

## Entitlement-model status

The Strategic Cash Settlement statement is an intended entitlement-model statement. The underlying subject-to-tile mappings, role ownership, and migration status require validation; see [[what-are-the-x-ratanone-subject-to-tile-entitlement-mappings]].

## Identity ambiguity

The RATAN and EMS2-34010 FMAA source does not explain whether `X_RATANONE` is:

- The canonical entitlement entity for RATAN.
- A legacy identifier.
- A shared identifier associated with RatanOne.
- A distinct entity that happens to support RATAN.

`X_RATANONE` should therefore be treated as concrete evidence of a RATAN/RatanOne naming relationship, not as proof of a canonical service identity. See [[canonical-ratan-ratanone-service-identity]] and [[what-is-the-relationship-between-ratan-and-ratanone]].

## Troubleshooting URLs

- Production: <https://sabre-prod-ems2.gdc.standardchartered.com:16443/ems2/rest/entitlements/entity/name/X_RATANONE>
- Non-production: <https://uklvauems01a.uk.standardchartered.com:16443/ems2/rest/entitlements/entity/name/X_RATANONE>