---
type: source
title: FM CES Integration Technical Design
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, data-entitlement, ces, auth-service, query-service, redis, websocket]
related: [ces, auth-service, query-service, ssdr, cash-settlement-data-entitlement, ces-data-entitlement-integration, place-ces-entitlement-mediation-in-auth-service, adopt-two-layer-ces-emergency-disablement, canonical-ces-field-to-cashflow-jsonb-mapping]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
authors: []
year: 2026
url: ""
venue: ""
---
# FM CES Integration Technical Design

This technical design describes the planned integration of [[ces|CES]]—formerly EMS3—as the strategic data-entitlement authority for RATANONE Cash Settlement. CES management, including user onboarding and entitlement-rule configuration, remains owned by the CES team and is outside RATAN's implementation scope.

The design preserves [[ems2|EMS2]] function entitlements. CES-derived data entitlements are mediated by [[auth-service|auth-service]], cached in [[redis|Redis]], and enforced by [[query-service|Query Service]] for cashflow blotter GraphQL queries, [[ssdr|SSDR]] SQL queries, and cashflow WebSocket notifications.

## CES model

CES evaluates access conditions for an individual user. Data Policy rules are linked to a user's HR profile and maintained by a Policy Owner or COO. Data Profile rules are linked to a user's role; as a general rule, Data Profile rules take precedence over Data Policy rules.

| Type | Connected to | Maintained by | Note | Example |
| --- | --- | --- | --- | --- |
| Data policy | Location | Policy Owner / COO | | |
| Data profile | user role | | | |
| User role | | | | |

## CES Consumer API

```http
GET /fmces/v1/entitlement/app/51358/RATAN_ENTITLEMENT_RULE/user/1538147 HTTP/1.1
Authorizatio...
Host: fmcesuat.gdc.standardchartered.com
```

```js
"entitlements": {
  "data_entitlements_logical_indicator": "OR",
  "data_entitlements": [
    {
      "key": "Entity.Counterparty_Country_ISO_Code",
      "values": ["JP"]
    }, {
      "key": "Entity.Booking_Entity_SCI_FMID",
      "values": ["10036382","300010633"]
    }],
}
```

## Constraints and condition translation

CES conditions are converted into backend-specific representations. The supported storage scope is `cashflow_data.cashflow`; fields outside that JSONB document are not supported.

| Notation | Interpret flow | Target field |
| --- | --- | --- |
| Specification | CES condition → Specification JSON → JPA specification → JSONB query | cashflow_data.cashflow |
| SQL | CES condition → JSONB query | cashflow_data.cashflow |
| Direct | CES condition → JSONB condition → evaluate | cashflow_data.cashflow |

```js
// for simple case
{"field":"Entity.Booking_Entity_SCI_FMID","values":["401036553","400994973"]}

// for complex case with multiple conditions
{"or": [
  {"field":"Entity.Booking_Entity_SCI_FMID","values":["401036553","400994973"]},
  {"field":"Entity.Counterparty_Country_ISO_Code","values":["JP"]}
]}
```

```sql
select *
from cashflow_data c 
where
  jsonb_extract_path_text(c.cashflow, 'Cashflow', 'Cashflow_State')=? 
  and ( -- data entitlement conditions
      jsonb_extract_path_text(c.cashflow, 'Entity', 'Booking_Entity_SCI_FMID') in (?, ?) 
      or jsonb_extract_path_text(c.cashflow, 'Entity', 'Counterparty_SCI_DOMICILE_COUNTRY')=?
  ) 
```

The design contains an unresolved field mismatch: CES examples use `Entity.Counterparty_Country_ISO_Code`, while the generated SQL uses `Entity.Counterparty_SCI_DOMICILE_COUNTRY`. See [[canonical-ces-field-to-cashflow-jsonb-mapping]].

## Interface enforcement

- GraphQL filtering is transparent: Query Service adds entitlement constraints to cashflow queries.
- SSDR SQL is augmented with CES-derived JSONB predicates.
- WebSocket notification events are directly evaluated against a user's entitlement conditions before delivery.
- Cashflow clients are expected to subscribe to a user-specific destination rather than the shared `/cashflow/notification` topic.

```java
messagingTemplate.convertAndSendToUser(username, "/cashflow/notification", event);
```

The main design specifies client subscription to:

```text
/user/{username}/cashflow/notification
```

A review note instead refers to `/user/{username}/queue/cashflow/notification`; this remains unresolved in [[canonical-user-specific-cashflow-websocket-destination]].

## Cache and fallback contract

auth-service uses existing FMAA token handling and caches CES results in Redis. Query Service has no separate entitlement cache.

```js
scb:
  ems2:
    expiryTime: 3600 #seconds
    cachingEnabled: true
```

Normal operation is fail-closed: missing user onboarding, missing entitlement data, empty values, or CES failures cause the user query to fail. The design also introduces an emergency downgrade control that can disable CES enforcement globally or for selected users.

```yml
scb:
  ems3:
    enabled: true
    disabled-users:
      - 2022123
```

The emergency bypass changes the effective behavior to no CES entitlement enforcement and therefore requires explicit governance. See [[adopt-two-layer-ces-emergency-disablement]] and [[what-controls-govern-ces-entitlement-emergency-bypass]].

## Error handling recorded by the design

| Error type | Error handling | End user result | Note |
| --- | --- | --- | --- |
| `{ "errorClass": "com.fmces.shared.exception.ResourceNotFoundException", "message": "User Not found-2022123", "status": 404, "timestamp": "2025-12-10T07:26:32.750335381" }` | Throw error | Query failed | Wait for CES to fix it. For emergency, CES can be disabled in RATAN temporarily. |
| Missing data entitlement in the response | Throw error | Query failed | |
| CES 500 internal error | Retry | | |
| CES unavailable `connect ECONNREFUSED 10.198.72.135:443` | Retry | | |
| CES 4xx errors | Retry | | Expiration should be handled in auth service. |
| Unrecognized fields | Do nothing | | JSONB conversion does not throw an error for absent fields. |
| Empty values | Throw error | Query failed | |

Retry classifications, bounds, timeouts, and circuit-breaker behavior are not specified. In particular, treating all CES 4xx responses as retryable conflicts with the explicit non-onboarded-user 404 failure case. See [[what-retry-timeout-and-circuit-breaker-policy-governs-ces-failures]].

## auth-service APIs

```http
GET /v1/data-entitlement?userId=2006999' HTTP/1.1
Host: 10.198.199.160:9255
```

```json
{
  "enabled": true,
  "filters": [
    {
      "field": "Entity.Booking_Entity_SCI_FMID",
      "values": [
        "4",
        "400960089"
      ]
    }
  ],
  "condition": "ANY"
}
```

```json
{
  "status": 500,
  "errorCode": "SERVICE_INTERNAL_ERROR",
  "errorMessage": "Failed to get ems3 entitlements: 404 Not Found: \"{\"errorClass\":\"com.fmces.shared.exception.ResourceNotFoundException\",\"message\":\"User Not found-2006991\",\"status\":404,\"timestamp\":\"2026-01-05T07:57:41.867826445\"}\"",
  "metadata": null
}
```

```http
POST http://10.198.199.160:8868/v1/auth/reset-data-entitlement?userId=*
Basic ratanone-rundeck...
```

`userId=*` clears all data-entitlement caches; another value clears the named user's cache. The endpoint is intended for internal maintenance. Its stated gateway invocation model uses hard-coded Basic credentials for `ratanone-rundeck`, which needs control-plane authorization, secret-management, audit, and wildcard-invalidation safeguards.

## Rollout and evidence status

The document records implementation work across service properties, auth-service, Query Service, and the cashflow blotter; it also records that the Static Data Service implementation was cancelled when CES mediation moved to auth-service.

CES migration is intended to identify users from both `X_RATANONE` and `RATAN_DATA_ENTITLEMENT` in EMS2, retrieve CES outputs, and compare them with historical entitlement expectations. The rollout remains dependent on connectivity, onboarding, reconciliation, UAT, PSS and downstream sign-off, CES/SSDR OLA agreements, health checks, and final rule configuration.

Performance tests were performed with Apache JMeter in FMRP2 and staging, but the textual document provides test workloads and image-only reports rather than extractable latency, throughput, error-rate, or acceptance-threshold results. It demonstrates test activity, not a quantified production-capacity conclusion.

The BCS blotter assessment is partially feasible: `Entity.Booking_Entity_SCI_FMID` is supported in its TDS index, while the Japan case is unsupported because `Entity.Counterparty_Country_ISO_Code` is absent.