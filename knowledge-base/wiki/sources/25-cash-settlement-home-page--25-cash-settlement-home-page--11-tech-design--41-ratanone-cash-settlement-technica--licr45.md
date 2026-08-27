---
type: source
title: API Gateway & Auth Server Merge Solution Design
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, iam, api-gateway, authorization, entitlements, indonesia]
related: [api-gateway, microsoft-entra-id, forgerock, ems2, fmces, single-ui-entitlement, token-embedded-functional-and-data-entitlements, ems2-to-ces-entitlement-migration, indonesia-data-residency-and-session-isolation, ratanone-entra-and-ces-migration, where-should-data-entitlement-be-resolved-and-enforced, can-single-ui-entitlement-jwt-size-remain-within-header-limits-for-ces-power-users, what-is-the-authoritative-id-fmid-mapping-and-id-gateway-filtering-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
authors: []
year: 2026
url: ""
venue: Internal technical design
---
# API Gateway & Auth Server Merge Solution Design

## Summary

This proposal describes an IAM and entitlement migration for RATAN/RatanOne. It proposes replacing ForgeRock-based browser and service authentication dependencies with [[microsoft-entra-id]], migrating entitlement management from [[ems2]] to [[fmces]], and moving token endpoints into the [[api-gateway]].

The design also identifies Indonesia deployment as a regulatory isolation requirement: PostgreSQL, Redis, and session management must be provisioned as isolated in-country instances.

The design is not a confirmed implementation plan. Its current-state sections for Entra login, API authorization, and data-entitlement checks are empty, and the referenced post-merge diagrams are absent.

## Migration Drivers

- ForgeRock, including OneMFA / OneDS, is planned for decommissioning by the end of Q3 2026.
- RATAN currently uses OneMFA and OUD for browser SSO and FMAA for service-to-service authentication.
- RATAN requires an EMS2-to-CES mapping before ServiceNow entitlement-request onboarding can proceed.
- Indonesia requires isolated country-scoped storage and session infrastructure.

## Proposed Entitlement Token

The proposal is to include functional and data entitlements in a BFF-issued `Single-UI-Entitlement` JWT.

```js
{
  "header": { "typ": "JWT", "alg": "RS512" },
  "payload": {
    "role_entitlements": [
      { "feature": "Cashflow", "action": "Query" },
      { "feature": "NostroBlotter", "action": "View" },
      { "feature": "ID Access", "action": "View" }
    ],
    "data_entitlements_logical_indicator": "OR",
    "data_entitlements": [
      { "key": "Entity.Booking_Entity_SCI_FMID", "values": ["10036382", "300010633"] },
      { "key": "Entity.Counterparty_Country_ISO_Code", "values": ["JP"] }
    ],
    "sub": "2022123",
    "iss": "single-ui-bff-entitlement",
    "exp": 1778783332,
    "iat": 1778740132,
    "jti": "single-ui-bff-id"
  }
}
```

A previous token-embedding implementation was removed because a full EMS2 entity-tree response could reach approximately 21 KB per user. The source estimates a CES-based entitlement payload at approximately 3–5 KB, but requires measurement using real CES user profiles before Go Live.

## API Migration Scope

The following endpoints are proposed to move into the API gateway:

```text
GET /v3/token
GET /v3/kong/token
```

The following legacy login endpoints are proposed for removal:

```text
/v1/login
/v2/login
```

The source records that frontend usage of the legacy APIs was checked, but does not supply a complete client inventory, migration plan, or retirement schedule.

## CES Mapping

| EMS2 concept | CES concept | Remark |
| --- | --- | --- |
| Subject | Feature | |
| Role | Entitlement | |
| Action | Action | CES recommends more standard action names like View, Edit, Download |

| EMS2 | CES |
| --- | --- |
| subject=`RATAN_CASHFLOW_BLOTTER`, action=`F_Export_Data` | feature=`CashflowBlotter`, action=`Export` |
| subject=`RATAN_TRADE_BLOTTER`, action=`F_Export_Data` | feature=`TradeBlotter`, action=`Export` |
| subject=`RATAN_CASHFLOW_BLOTTER`, action=`ACCESS_FMO_POST_TRADE_PORTAL` | feature=`CashflowBlotter`, action=`View` |

## Indonesia Access Rule

The proposed frontend rule displays the Indonesia Cashflow Blotter tile only when a user has both Cashflow Blotter functional access and a data entitlement containing `fmid="8"`. The ID Gateway is expected to apply equivalent filtering logic.

The source does not define how `fmid="8"` maps to the booking-entity FMID values shown in the JWT example. See [[what-is-the-authoritative-id-fmid-mapping-and-id-gateway-filtering-rule]].

## Unresolved Design Points

- Whether data entitlement is resolved at the API gateway and propagated in headers, or fetched by each downstream service from an authorization server.
- Whether the API gateway issues, proxies, exchanges, or only validates the BFF-issued JWT.
- JWT signing-key ownership, claim versioning, revocation, refresh, and missing-claim behavior.
- Actual CES payload distribution and end-to-end browser, ingress, proxy, and service header limits.
- The complete infrastructure and operational controls needed to demonstrate Indonesia data and session isolation.
---

---FILE: wiki/entities/api-gateway.md---
---
type: entity
title: API Gateway
created: 2026-08-24
updated: 2026-08-24
tags: [api, gateway, authentication, authorization, ratanone]
related: [single-ui-entitlement, microsoft-entra-id, token-embedded-functional-and-data-entitlements, where-should-data-entitlement-be-resolved-and-enforced]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# API Gateway

The API Gateway is the proposed destination for RATAN token API functions. The design proposes migrating `GET /v3/token` and `GET /v3/kong/token` into this layer and retiring `/v1/login` and `/v2/login`.

Its authorization responsibility remains unresolved. The source describes gateway-side entitlement resolution and header propagation as one option, while downstream services fetching entitlements from an authorization server is another. See [[where-should-data-entitlement-be-resolved-and-enforced]].

The source does not establish whether the gateway is the authoritative issuer, validator, proxy, or token-exchange participant for [[single-ui-entitlement]] JWTs.
---

---FILE: wiki/entities/microsoft-entra-id.md---
---
type: entity
title: Microsoft Entra ID
created: 2026-08-24
updated: 2026-08-24
tags: [iam, identity-provider, authentication, ratanone]
related: [forgerock, ratanone-entra-and-ces-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# Microsoft Entra ID

Microsoft Entra ID is the target enterprise IAM platform for RATAN authentication migration. The source states that RATAN must replace browser SSO dependencies on OneMFA/ForgeRock and OUD, plus service-to-service authentication through FMAA, before ForgeRock is decommissioned by the end of Q3 2026.

The source does not provide a target Entra login flow, service-authentication protocol, migration milestones, or ownership model.
---

---FILE: wiki/entities/forgerock.md---
---
type: entity
title: ForgeRock
created: 2026-08-24
updated: 2026-08-24
tags: [iam, legacy-platform, authentication, decommissioning]
related: [microsoft-entra-id, ratanone-entra-and-ces-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# ForgeRock

ForgeRock is RATAN's legacy enterprise IAM dependency. RATAN currently integrates with OneMFA / OneDS and OUD for browser-based SSO, and relies on FMAA for service-to-service authentication.

The source states that ForgeRock is scheduled for full decommissioning by the end of Q3 2026 and identifies migration to [[microsoft-entra-id]] as required before that deadline.
---

---FILE: wiki/entities/ems2.md---
---
type: entity
title: EMS2
created: 2026-08-24
updated: 2026-08-24
tags: [entitlements, authorization, legacy-platform, ratanone]
related: [fmces, ems2-to-ces-entitlement-migration, single-ui-entitlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# EMS2

EMS2 is the current RATAN source of truth for functional entitlements and data entitlements. It is being replaced by [[fmces]] / CES.

A previous `Single-UI-Entitlement` JWT design embedded the full EMS2 entity tree and was removed after EMS2 responses reportedly reached approximately 21 KB per user, making tokens impractically large. The proposed CES condition model is expected to be more compact, but must be measured before adoption. See [[token-embedded-functional-and-data-entitlements]].
---

---FILE: wiki/entities/fmces.md---
---
type: entity
title: FMCES
created: 2026-08-24
updated: 2026-08-24
tags: [entitlements, ces, authorization, ratanone]
related: [ems2, ems2-to-ces-entitlement-migration, ratanone-entra-and-ces-migration, can-single-ui-entitlement-jwt-size-remain-within-header-limits-for-ces-power-users]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# FMCES

FMCES, also called CES in the source, is the target entitlement platform replacing [[ems2]] for RATAN functional and data entitlements.

RATAN registration in CES and a defined EMS2-to-CES model mapping are described as prerequisites for ServiceNow entitlement-request onboarding. CES uses Feature, Entitlement, and Action concepts in place of EMS2 Subject, Role, and Action constructs.
---

---FILE: wiki/entities/single-ui-entitlement.md---
---
type: entity
title: Single-UI-Entitlement
created: 2026-08-24
updated: 2026-08-24
tags: [jwt, entitlement, authorization, bff, ratanone]
related: [api-gateway, ems2, fmces, token-embedded-functional-and-data-entitlements, can-single-ui-entitlement-jwt-size-remain-within-header-limits-for-ces-power-users]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# Single-UI-Entitlement

`Single-UI-Entitlement` is the JWT described by the source as a BFF-issued bearer of RATAN functional and data entitlements.

The proposed claims include `role_entitlements`, `data_entitlements_logical_indicator`, `data_entitlements`, `sub`, `iss`, expiry, issue time, and token ID. The illustrated issuer is `single-ui-bff-entitlement`, while token endpoints are proposed to move to the [[api-gateway]].

The design has unresolved issuer ownership, signing-key lifecycle, token refresh, revocation, claim-versioning, and data-filter enforcement semantics.
---

---FILE: wiki/concepts/token-embedded-functional-and-data-entitlements.md---
---
type: concept
title: Token-Embedded Functional and Data Entitlements
created: 2026-08-24
updated: 2026-08-24
tags: [jwt, authorization, entitlements, token-size, ratanone]
related: [single-ui-entitlement, api-gateway, ems2, fmces, where-should-data-entitlement-be-resolved-and-enforced, can-single-ui-entitlement-jwt-size-remain-within-header-limits-for-ces-power-users]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# Token-Embedded Functional and Data Entitlements

The proposed RATAN approach places both functional access permissions and data-filter conditions in a BFF-issued [[single-ui-entitlement]] JWT.

Functional entitlements are represented by `role_entitlements`, containing feature/action pairs. Data entitlements are represented by keyed allowed-value conditions, with `data_entitlements_logical_indicator` specifying logical combination behavior.

## Constraints

The source estimates an added 3–5 KB payload for typical CES-backed tokens. This is a planning estimate, not a measured result. JWT serialization and base64url encoding, plus the complete HTTP header, must be tested against browser, proxy, ingress, and service limits.

The source records a prior failure: full EMS2 entity-tree content could produce responses of approximately 21 KB per user, making the prior token approach unworkably large.

## Required Contract Decisions

Before production adoption, the architecture needs explicit rules for:

- Authoritative issuer and signing-key ownership.
- Claim schema and versioning.
- Expiry, refresh, and revocation after an entitlement change.
- Authorization behavior for missing, malformed, or stale claims.
- Whether the gateway, downstream services, or both enforce data filters.
- Bypass prevention for traffic that does not traverse the gateway.
---

---FILE: wiki/concepts/ems2-to-ces-entitlement-migration.md---
---
type: concept
title: EMS2-to-CES Entitlement Migration
created: 2026-08-24
updated: 2026-08-24
tags: [entitlements, ems2, ces, migration, servicenow]
related: [ems2, fmces, ratanone-entra-and-ces-migration, token-embedded-functional-and-data-entitlements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# EMS2-to-CES Entitlement Migration

EMS2-to-CES entitlement migration translates RATAN's legacy entitlement model into FMCES/CES concepts and APIs. The source identifies this migration as a hard prerequisite for ServiceNow onboarding of access and role-change requests.

## Model Mapping

| EMS2 concept | CES concept | Remark |
| --- | --- | --- |
| Subject | Feature | |
| Role | Entitlement | |
| Action | Action | CES recommends more standard action names like View, Edit, Download |

## Example Mappings

| EMS2 | CES |
| --- | --- |
| subject=`RATAN_CASHFLOW_BLOTTER`, action=`F_Export_Data` | feature=`CashflowBlotter`, action=`Export` |
| subject=`RATAN_TRADE_BLOTTER`, action=`F_Export_Data` | feature=`TradeBlotter`, action=`Export` |
| subject=`RATAN_CASHFLOW_BLOTTER`, action=`ACCESS_FMO_POST_TRADE_PORTAL` | feature=`CashflowBlotter`, action=`View` |

Migration readiness requires RATAN registration in [[fmces]], a complete mapping, and validation that CES entitlement responses support all required functional access and data-filter semantics.
---

---FILE: wiki/concepts/indonesia-data-residency-and-session-isolation.md---
---
type: concept
title: Indonesia Data Residency and Session Isolation
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, data-residency, session-management, postgres, redis, ratanone]
related: [ratanone-entra-and-ces-migration, what-is-the-authoritative-id-fmid-mapping-and-id-gateway-filtering-rule]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# Indonesia Data Residency and Session Isolation

Indonesia deployment requires an isolated RatanOne instance with customer and transaction data located in in-country infrastructure. The source explicitly includes PostgreSQL, Redis, and session management in the required country-scoped isolation boundary.

This is a whole-system obligation rather than a frontend tile-visibility feature. Implementation evidence should establish boundaries for data stores, session state, backups, logs, observability, key management, disaster recovery, network paths, and support access.

The source does not provide the underlying regulation, data classification, control evidence, or operational design.
---

---FILE: wiki/queries/where-should-data-entitlement-be-resolved-and-enforced.md---
---
type: query
title: Where Should Data Entitlement Be Resolved and Enforced?
created: 2026-08-24
updated: 2026-08-24
tags: [authorization, data-entitlements, api-gateway, ratanone]
related: [api-gateway, single-ui-entitlement, token-embedded-functional-and-data-entitlements, ratanone-entra-and-ces-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# Where Should Data Entitlement Be Resolved and Enforced?

The source leaves unresolved whether data entitlements should be resolved by the [[api-gateway]] and propagated as headers, or fetched on demand by each downstream service from an authorization server.

A decision must define the authoritative enforcement point, downstream-service obligations, propagation contract, behavior on authorization-service failures, latency implications, and controls preventing non-gateway bypasses.

The proposed [[single-ui-entitlement]] token may support either approach, but does not resolve responsibility by itself.
---

---FILE: wiki/queries/can-single-ui-entitlement-jwt-size-remain-within-header-limits-for-ces-power-users.md---
---
type: query
title: Can Single-UI-Entitlement JWT Size Remain Within Header Limits for CES Power Users?
created: 2026-08-24
updated: 2026-08-24
tags: [jwt, header-limits, ces, performance, authorization]
related: [single-ui-entitlement, ems2, fmces, token-embedded-functional-and-data-entitlements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# Can Single-UI-Entitlement JWT Size Remain Within Header Limits for CES Power Users?

The source estimates that CES-backed entitlement content adds approximately 3–5 KB per token/request, but this is not supported by measured production-like profiles. A prior EMS2 entity-tree implementation reached approximately 21 KB per user and was removed as impractical.

Validation should measure raw CES responses, serialized claims, signed and base64url-encoded JWTs, and complete `single-ui-entitlement` header sizes for ordinary users, broad-access users, and users with large FMID sets.

The validation must also confirm the smallest applicable browser, reverse-proxy, ingress, gateway, and downstream-service header limit, and define a fallback design if the limit is exceeded.
---

---FILE: wiki/queries/what-is-the-authoritative-id-fmid-mapping-and-id-gateway-filtering-rule.md---
---
type: query
title: What Is the Authoritative ID FMID Mapping and ID Gateway Filtering Rule?
created: 2026-08-24
updated: 2026-08-24
tags: [indonesia, fmid, authorization, data-entitlements, gateway]
related: [indonesia-data-residency-and-session-isolation, api-gateway, single-ui-entitlement, token-embedded-functional-and-data-entitlements]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
---
# What Is the Authoritative ID FMID Mapping and ID Gateway Filtering Rule?

The source proposes displaying the Indonesia Cashflow Blotter tile when a user has Cashflow Blotter functional entitlement and data entitlement containing `fmid="8"`. It also states that the ID Gateway should apply the same logic.

However, the example JWT contains booking-entity FMID values `10036382` and `300010633`, without defining their relationship to `fmid="8"`.

An authoritative contract is needed for the Indonesia identifier, CES claim key and value format, functional-entitlement requirement, logical combination rules, gateway filtering behavior, and denial behavior for missing or ambiguous claims.
---

---FILE: wiki/projects/ratanone-entra-and-ces-migration.md---
---
type: project
title: RatanOne Entra and CES Migration
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, iam, entra, ces, migration, indonesia]
related: [microsoft-entra-id, forgerock, ems2, fmces, api-gateway, single-ui-entitlement, token-embedded-functional-and-data-entitlements, ems2-to-ces-entitlement-migration, indonesia-data-residency-and-session-isolation, where-should-data-entitlement-be-resolved-and-enforced]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/API Gateway & Auth server merge solution design.md"]
status: planned
owner: ""
start_date: 2026-08-24
target_date: 2026-09-30
---
# RatanOne Entra and CES Migration

## Objective

Migrate RATAN/RatanOne identity and entitlement dependencies from ForgeRock and EMS2 to Microsoft Entra ID and FMCES/CES, while supporting Indonesia's isolated deployment requirements.

## Scope

- Replace OneMFA / OneDS and OUD browser SSO dependencies.
- Replace FMAA service-to-service authentication dependency.
- Register RATAN in CES and complete EMS2-to-CES mapping.
- Enable ServiceNow onboarding after CES migration prerequisites are met.
- Migrate `GET /v3/token` and `GET /v3/kong/token` into the [[api-gateway]].
- Retire `/v1/login` and `/v2/login` after all consumers are migrated.
- Establish isolated Indonesia data storage and session infrastructure.

## Dependencies and Risks

ForgeRock is scheduled for decommissioning by the end of Q3 2026. The source provides no detailed migration plan or ownership assignments.

The proposed token-embedded entitlement model has an unresolved enforcement boundary and unvalidated header-size risk. CES entitlement size must be measured before Go Live. See [[can-single-ui-entitlement-jwt-size-remain-within-header-limits-for-ces-power-users]].

## Open Decisions

- Select gateway-side versus service-side data-entitlement resolution and enforcement.
- Define JWT issuer, signing-key ownership, revocation, refresh, and claim-versioning rules.
- Define the ID FMID mapping and ID Gateway filter contract.
- Define evidence and controls for Indonesia in-country isolation.
---

---FILE: wiki/log.md---
## 2026-08-24 ingest | API Gateway & Auth Server Merge Solution Design

- Ingested the RATAN API Gateway and authentication-server merge proposal, including Entra migration, EMS2-to-CES migration, token-embedded entitlements, and Indonesia isolation requirements.