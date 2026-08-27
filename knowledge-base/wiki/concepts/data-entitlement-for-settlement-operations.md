---
type: concept
title: Data Entitlement for Settlement Operations
tags: [data-entitlement, data-sovereignty, fmces, access-control, settlement-operations]
related: [ratan, fmo-post-trade-portal]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Ratan One Processing Guide (DOI).md"]
---
# Data Entitlement for Settlement Operations

RATAN integrates with FMCES to enforce data-sovereignty and need-to-know restrictions over cashflow visibility. An operator's permitted entity population depends on their entitlement profile and location.

This is distinct from RATAN function access. A user can have a functional role but still be unable to see or process relevant cashflows if FMCES entitlement is absent or incomplete.

## Operational implications

- Entitlement failures should be resolved through an FMCES access request rather than by changing settlement workflow controls.
- Access design must separately review function permissions and entity data scope.
- Settlement queue monitoring can be incomplete if an operator's entity entitlement is incorrectly configured.

The source describes this control as a regulatory requirement. It does not specify a canonical entitlement-to-entity mapping or the approval workflow for every jurisdiction.