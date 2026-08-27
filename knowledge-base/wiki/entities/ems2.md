---
type: entity
title: EMS2
created: 2026-08-24
updated: 2026-08-24
tags: ["entitlement", "authorization", "cash-settlement", "ratanone", "entitlements", "rbac", "legacy", "EMS2", "entitlement-management", "ratan", "functional-access", "identity", "user-management"]
related: ["x-ratanone", "strategic-cash-settlement-entitlement-model", "ratan", "fmces", "fmces-based-ratan-entitlement-authorization", "auth-service", "single-ui-authorization", "ratan-data-entitlement", "ems2-entitlement-lookup", "function-entitlement", "data-entitlement", "ces", "functional-versus-data-entitlement", "fmaa", "ratan-ems2-user-entitlement-integration", "ratan-interface-inventory"]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/2026 Design/Cash Settlement Platform Architecture - Indonesia/(Deprecated)API Gateway & Auth Server Combination.md", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Authentication flow.md", "RATAN/RATAN -Interfaces/Ratan and CES 55508.md", "RATAN/RATAN -Interfaces/Ratan and EMS2-34010 FMAA.md"]
---
# EMS2

EMS2 is an entitlement-management system used to retrieve account-level function entitlements and RATAN-specific data entitlements.

## Role in RATAN

The RATAN and CES interface source identifies EMS2 as the system that continues to control RATAN menu and button/function entitlement through its API.

Separately, the RATAN and EMS2-34010 FMAA source describes EMS2 as the central system for managing RATAN user entities and entitlements. When a RATAN user logs in, RATAN retrieves the user's subjects under the `X_RATANONE` entity from EMS2. According to that source, the returned subjects are used to determine RATAN UI behavior, including blotter visibility and context-menu permissions.

These sources describe UI and functional-authorization effects. The RATAN and EMS2-34010 FMAA source does not establish whether EMS2-derived data is also enforced by RATAN backend services.

## Functional access and data entitlement

According to the RATAN and CES interface source, EMS2 has a functional-access role: it controls RATAN menu and button/function entitlement through its API.

That source does not state that EMS2 decides cashflow data visibility and does not provide an EMS2 API contract. It separately identifies [[ces]] as the provider of data-entitlement decisions for scoped cashflow blotters.

The RATAN and EMS2-34010 FMAA source associates subjects returned under `X_RATANONE` with stated RATAN UI behavior, including blotter visibility. This is distinct from the RATAN and CES interface source's statement that [[ces]] provides data-entitlement decisions for scoped cashflow blotters.

See [[functional-versus-data-entitlement]].

## Documented interfaces

Other EMS2 sources document an account lookup at:

`/ems2/rest/account/{account}`

The response includes account metadata and `entitlementTypes`, with fields such as `roleName`, `applicationName`, `uniqueName`, and `isPrivilege`.

A separate lookup targets the `RATAN_DATA_ENTITLEMENT` entity:

`/ems2/rest/entitlements/entity/name/RATAN_DATA_ENTITLEMENT/user/{user}`

Its example response returns the `Global` role and `VIEW_ENTITLEMENT` action for the `RATAN` system.

### `X_RATANONE` endpoints

The RATAN and EMS2-34010 FMAA source provides sample production and non-production REST URLs supporting the existence of an EMS2 integration:

- Production account lookup: `https://sabre-prod-ems2.gdc.standardchartered.com:16443/ems2/rest/account/1431837`
- Production `X_RATANONE` lookup: `https://sabre-prod-ems2.gdc.standardchartered.com:16443/ems2/rest/entitlements/entity/name/X_RATANONE`
- Non-production `X_RATANONE` lookup: `https://uklvauems01a.uk.standardchartered.com:16443/ems2/rest/entitlements/entity/name/X_RATANONE`

That source does not provide the authoritative API contract, authentication details, response schema, caching policy, or outage behavior.

## Architectural role

[[single-ui-authentication-flow]] uses EMS2 for frontend function-entitlement retrieval. [[auth-service]] also depends on EMS2 or EMS2-derived data when the [[api-gateway]] authorizes API requests. The source does not establish whether these are independent reads, cached reads, or a shared entitlement service.