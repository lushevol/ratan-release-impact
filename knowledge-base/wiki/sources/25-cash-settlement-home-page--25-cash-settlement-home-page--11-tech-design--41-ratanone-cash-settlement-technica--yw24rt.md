---
type: source
title: Option2 RATAN Existing Data Entitlement Implementation
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, cash-settlement, entitlement, ems2, query-service, static-data-service]
related: [ems2, auth-service, api-gateway, query-service, static-data-service, oud, group-management-service, function-entitlement, data-entitlement, cash-settlement-data-entitlement, which-jwt-country-field-is-authoritative-for-data-entitlement, what-is-the-static-data-entitlement-rule-language-and-failure-contract, how-are-production-data-entitlement-rules-governed-and-deployed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/Option2  RATAN existing data entitlement implementation.md"]
authors: []
year: 2025
url: "https://confluence.global.standardchartered.com/display/DSP/RATANONE+Data+Entitlement+Solution"
venue: "Derivative Strategy Projects Confluence"
---
# Option2 RATAN Existing Data Entitlement Implementation

## Summary

This design assesses whether RATANONE's existing entitlement implementation can meet Cash Settlement access requirements. It separates [[function-entitlement|function entitlement]], which permits API access or actions, from [[data-entitlement|data entitlement]], which restricts the records a user can view.

The existing design uses EMS2-derived role and action data during authentication. The returned JWT includes serialized entitlement data and user information. API access is controlled both through API-level checks and API gateway registration. Record-level cashflow visibility is filtered in [[query-service|Query Service]] by obtaining an entitlement condition from [[static-data-service|static-data-service]].

The model is assessed as configurable for country-specific access, cross-country access, and explicit exclusions. It does not natively support regional, function-based, hierarchy-based, or multiple-tag entitlement models. Taiwan location restrictions are only partially supported because role-based exceptions require additional logic.

## Functional Entitlement Flow

Users authenticate through SSO and receive a JWT. On login, RATANONE retrieves user entitlement information from [[ems2|EMS2]]. The frontend caches this information and checks it when users perform actions; APIs also perform authorization checks. Frontend controls are not the authoritative security boundary because backend API checks remain required.

Each API is registered with function entitlements in [[api-gateway|API gateway]]. The EMS2 structure maps a role to subjects and permitted actions.

### EMS2 Account Lookup Example

```bash
GET https://uklvauems01a.uk.standardchartered.com:16443/ems2/rest/account/1481696
{
    "accountStatus": "A",
    "accountName": "1481696",
    "accountType": "User",
    "fullName": "IIQ1481696,User",
    "accountOwner": "1481696",
    "entitlementTypes": [
        {
            "uniqueName": "1511446402|MXMLS_FILEUPLOAD_BSM|1511446459|DPS_MLS",
            "roleName": "DPS_MLS",
            "roleDescription": "",
            "applicationName": "MUREX G2000",
            "isPrivilege": "N"
        }
        ...
    ],
    "status": ""
}
```

### Authentication Response Example

```bash
POST https://uklvadapp1345.uk.dev.net:3833/v3/authenticate
single-ui-authorization Bearer eyJ...
{
    "entitlement": "{\"role\":\"FMO_OPS_BOM\",\"actions\":[\"RATAN_TRADE_BLOTTER:ACCESS_FMO_POST_TRADE_PORTAL\", ...],\"dataEntitlementRoles\":\"Global\"}",
    "userInfo": {
        "userId": "1481696",
        "fullName": "1481696",
        "country": "Global",
        "entitlementCountry": "China"
    }
}
```

The sample creates an unresolved ambiguity: `country` is `Global`, while `entitlementCountry` is `China`. The source also presents Query Service rule lookup using a country parameter such as `Nepal`. See [[which-jwt-country-field-is-authoritative-for-data-entitlement]].

### EMS2 Function Entitlement Structure

```json
{
    " id " : 11274101 ,
    " name " : "X_RATANONE" ,
    " applicationName " : "RATAN" ,
    " roleId " : 11274177 ,
    " roleName " : "FMO_OPS_BOM" ,
    " subjects " : [
        {
            " longName " : "/RATAN_CASHFLOW_BLOTTER" ,
            " name " : "RATAN_CASHFLOW_BLOTTER" ,
            " id " : 11274218 ,
            " actions " : [
                {
                    " name " : "F_Ad_Hoc_Nostro_Initiate" ,
                    " id " : 11274299 ,
                    " entitlementId " : 11806798
                },
                // ...
            ]
        }
    ]
}
```

### Existing Function Entitlement Role and Action Inventory

| Role | RATAN_AUTO_NETTING_RULE | Subject.. |
| --- | --- | --- |
| FMO_OPS_BO | F_Ad_Hoc_Nostro_Initiate, … | … |
| FMO_OPS_BOC | F_Ad_Hoc_Nostro_Initiate, … | … |
| FMO_OPS_BOL | F_Ad_Hoc_Nostro_Initiate, … | … |
| FMO_OPS_BOM | F_Ad_Hoc_Nostro_Initiate, … | … |
| FMO_OPS_MKR | F_Ad_Hoc_Nostro_Initiate, … | … |
| FMO_OPS_INV | ACCESS_FMO_POST_TRADE_PORTAL | … |
| FMO_RO | F_Custom_Query_Builder… | … |
| NON_FMO_RO | F_Custom_Query_Builder… | … |
| PSS_RO | F_Custom_Query_Builder… | … |

## Data Entitlement Implementation

The existing filtering logic is implemented in `v2/data/provider/query/cashflows (LoopQueryController.java)` in [[query-service|Query Service]]. It requests a filtering condition from [[static-data-service|static-data-service]].

```bash
GET <static-data-service>/v2/rule/entitlement?role=Onshore&country=Nepal
```

Example returned or applied predicate:

```text
Entity.Booking_Entity_SCI_FMID IN ('400007847')
```

Country data is obtained from [[oud|OUD]] and placed in the login token. The source does not define the expression grammar, predicate validation, permitted/forbidden rule composition, caching, audit trail, or behavior when the rule service is unavailable. See [[what-is-the-static-data-entitlement-rule-language-and-failure-contract]].

### Current Data Entitlement Roles

| Role | Intension | Description |
| --- | --- | --- |
| Global | Able to view all RATAN data | Able to view all data |
| GBS | Used by India & Malaysia GBS Ops who is not Onshore user only | Apply forbidden rules |
| OnShore | supporting onshore business | Apply permitted rules |

The endpoint example uses `Onshore`, while the role table uses `OnShore`. The source does not establish whether casing is significant or which identifier is canonical.

## Feasibility Assessment

| Requirement | Supported by Current Design? | Configuration or Gap |
| --- | --- | --- |
| **Onshore users can access only their location's data.** | Yes | Use `permitted_rule` for each country. Example: `Entity.Booking_Entity_SCI_FMID IN (...)`. |
| **Users in one country need access to another country's data.** | Yes | Add `permitted_rule` for cross-country access. Example: Dubai users accessing Egypt and Saudi data. |
| **Prohibit specific access (e.g., India vs Pakistan).** | Yes | Use `forbidden_country` and `forbidden_rule`. Example: India users cannot access Pakistan data. |
| **Taiwan data restrictions (approved locations, role-based exceptions).** | Partially | Approved locations can be configured using `permitted_rule`. Role-based exceptions need additional logic. |
| **Region-based access (e.g., ASEAN Regional Head).** | No | Requires grouping of countries into regions and assigning roles for regional access. |
| **Function-based access (e.g., ETD users).** | No | Requires tagging users with functions and applying function-specific rules. |
| **Global access with restrictions (e.g., GBS users).** | Partially | Global roles can be configured, but exceptions (e.g., India-Pakistan) need explicit `forbidden_rule`. |
| **Hierarchy-based access (e.g., senior management).** | No | Requires additional logic to define hierarchy and assign enhanced entitlements. |
| **Multiple entitlement tagging for backup purposes.** | No | Current design does not support multiple entitlements per user. |

`dataEntitlementRoles` is plural in the JWT example, but its example value is a single `Global` role. It is not evidence that multi-entitlement assignment is currently supported.

## Assumptions and Governance

The design assumes that OUD can provide distinguishable country values, including Taiwan.

```json
{"lastName":"Song","country":"Taiwan","firstName":"Sybil", ...
```

For non-production environments, the current onboarding flow requires manual database configuration. In production, entitlement data is maintained in EMS2. The source also states that adding rules requires a deployment, but does not clarify which rules are EMS2-managed, which are managed by `static-data-service`, or the approval and rollback process. See [[how-are-production-data-entitlement-rules-governed-and-deployed]].

## Indicative Implementation Estimate

The effort unit is not defined by the source and these estimates have no owners, dates, dependencies, or acceptance criteria.

| Change | Component | Effort | Remark |
| --- | --- | --- | --- |
| Onboard taiwan rules | static-data-service | 2 | Insert new data and unit test |
| SSDR report | query service | 1 | Existing code, add unit test |
| Cashflow blotter | query service | 1 | Existing logic uses mocked entitlements |
| Cashflow history | query service | 2 | New logic |
| Group blotter | group management service | 3 | New logic |

The scoped work is relevant to [[ssdr|SSDR]], [[query-service|Query Service]], [[static-data-service|static-data-service]], and [[group-management-service|Group Management Service]]. It is related to, but does not establish equivalence with, [[ces-data-entitlement-integration|CES Data Entitlement Integration]].