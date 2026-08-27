---
type: source
title: Expose The Cashflow Data Design
authors: []
year: 0
url: ""
venue: Internal technical design
tags: [cash-settlement, cashflow-data, query-service, api-design, entitlement]
related: [query-service, cash-settlement-query-cn-cashflow-data, entitlement-controlled-cashflow-query-api, sql-query-governance-for-cashflow-data-provider, cashflow-audit-query-payload, what-is-the-approved-query-language-and-security-boundary-for-cashflow-data-provider, what-are-the-authoritative-cashflow-query-api-slos-and-volume-limits, what-field-level-data-entitlements-and-masking-apply-to-external-cashflow-queries]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# Expose The Cashflow Data Design

This internal design specifies a phased Query Service that exposes RATAN cashflow data to external consumers. It identifies RATANEOD, DQSL (for SSDR), and FMMIS as consumers, using the `RATAN_FUNC: SYS_RO` EMS2 role.

The source is detailed evidence of an intended API contract but does not confirm that every endpoint, access setup, consumer integration, or proposed scaling design is currently deployed or approved.

## API contract

| API Name | Interface | Method | Request Sample | Response Sample | Header | Scenario | Note |
| --- | --- | --- | --- | --- | --- | --- | --- |
| Query Cashflows | `http://{domain}/v1/data/provider/query/cashflows` | `Post` | `{ queryCondition：“SQL string” }` | `{ [cashflow info list with json formatt] }` | `FMAA-Token：“string” FMAA-UserId:"string" FMAA-AppId:"string" Bank-Id:"string"(only for DQSL) Country : string"(only for DQSL)` | `records less than 30000 ，2 request/second for each node` | `RATAN-16976` PT research |

```groovy
{
    "queryCondition": "Select Cashflow.Audit,Cashflow.Cashflow_Id from cash_settlement_query_cn.cashflow_data LIMIT 1 OFFSET 0"
}
```

The documented source table is [[cash-settlement-query-cn-cashflow-data]]. The API accepts a SQL string in `queryCondition`, returns JSON records, and is intended to return valid data matching query criteria on demand.

## Environment URLs

| ENV | URL |
| --- | --- |
| Dev | `http://10.198.199.160:8868/v1/data/provider/query/cashflows` |
| SIT | `https://ratan-aws-sit-ns4-fmo-shell.ir.standardchartered.com/api/v1/data/provider/query/cashflows` |
| Uat | `https://fmo-shell.uk.dev.net:8453/api/v1/data/provider/query/cashflows` |
| Staging | `https://uklvadrtn002a.pi.dev.net:8868/v1/data/provider/query/cashflows` |
| Prod | `https://fmo-shell.gdc.standardchartered.com:8453/api/v1/data/provider/query/cashflows` |

These operational URLs require validation before use.

## Request headers and routing

| Header Name | Data Type | mandatory/optional | Field Description | note |
| --- | --- | --- | --- | --- |
| FMAA-Token | String | mandatory | the token which was got from FMAA endpoint | |
| FMAA-UserId | String | mandatory | same value with user_id when create FMAA token | |
| FMAA-AppId | String | mandatory | same value with app_id when create FMAA token | |
| Bank-Id | String | optional | user id in bank | if has this attribute and Country in the request header will handle request as return data to SSDR, else will handle request as return data to EOD |
| Country | String | optional | country code from OUD | if has this attribute and Bank-Id in the request header will handle request as return data to SSDR, else will handle request as return data to EOD |

Both `Bank-Id` and `Country` designate the SSDR retrieval path. Requests without both are handled as EOD retrieval. The source describes [[fmaa]] authentication and [[ems2]] functional-role and data-entitlement setup, but does not define the actual row-filtering or field-filtering enforcement logic.

## Phase-one response codes

| http response code | Behavior | Note |
| --- | --- | --- |
| 200 | OK | |
| 400 | Bad Request | |
| 401 | Unauthorized | |
| 461 | invalid SQL, the SQL not query type ,unsupported operation | will return different message for different error: 1)dataEntitlement Role or userCountry is null value 2)invalid SQL, the SQL with unsupported operation or fields 3)get data entitlement error |
| 462 | 1. System is Busy, try later pls 2. too many records, please use limit to split the sql | |
| 463 | get data entitlement rule fail | |
| 500 | Internal Server Error | |
| 502 | Bad Gateway | |
| 503 | Service Unavailable | |
| 504 | Gateway Timeout | |
| 505 | HTTP Version Not Supported | |

## Phase-two response codes

| http response code | Behavior | Note |
| --- | --- | --- |
| 200 | OK | |
| 400 | Bad Request | |
| 401 | Unauthorized | |
| 402 | Payment Required | |
| 403 | Forbidden | |
| 404 | Not Found | |
| 405 | Method Not Allowed | |
| 406 | Not Acceptable | |
| 415 | Unsupported Media Type | |
| 429 | Too Many Requests | |
| 500 | Internal Server Error | |
| 502 | Bad Gateway | |
| 503 | Service Unavailable | |
| 504 | Gateway Timeout | |
| 505 | HTTP Version Not Supported | |

The change from phase-one custom errors `461`–`463` to the phase-two list is not explained and may represent an incomplete or breaking response-contract change.

## Phased design

- **Phase one:** CN DayOne with fewer than 100,000 cashflows in the database. The stated query envelope is fewer than 30,000 records and 2 requests/second/node. Expected return time remains unspecified.
- **Phase two:** More than 300,000 database records, where a query returning fewer than 100,000 records takes more than 60 seconds. Proposals are to remove unneeded columns, set queried columns to defaults and `NOT NULL`, choose suitable database types, and add indexes for queried columns. A PostgreSQL leader–follower topology is considered, with `hot_standby=on` for the follower.
- **Phase three:** More than 1,000,000 database records, many consumer systems, and second-level response expectations. Elasticsearch or other middleware and independent storage are proposed for consideration only.

These thresholds mix database size, result size, latency, and consumer-count metrics. They are not an approved capacity plan; see [[what-are-the-authoritative-cashflow-query-api-slos-and-volume-limits]].

## Documented query keyword support

| Function keyword | Note |
| --- | --- |
| `limit` | |
| `count` | |

The source says DB function keywords are not supported in `SELECT` and `WHERE` except for the listed allowance, but its examples also use `OFFSET`. It does not specify a complete SQL grammar, AST-validation method, query cost limit, timeout, ordering policy, parameter binding, or table and column allowlists.

## `Cashflow.Audit` V2 structure

The source explicitly requires a query for `Cashflow.Audit` to include `Cashflow.Cashflow_Id`.

| Indexed Term | Field Description | Type | Data structure |
| --- | --- | --- | --- |
| `Cashflow.Audit` | Number of cashflow manual touchpoints; detail of all cashflow exceptions; touchpoint history. | Json | `"Cashflow.Audit": { "touchPointHistory": [Json Array] , "exceptionList": [Json Array] }` |
| `touchPointHistory` | History of cashflow touchpoints, including time, user, and action. | Json Array | `"touchPointHistory": [ { "time": "String", "user": "String", "action": "String" } ]` |
| `exceptionList` | Detail of all exceptions on a cashflow. | Json Array | `"exceptionList": [ { "exceptionCode": "String", "businessFlow": "String", "sourceSystem": "String", "exceptionType": "String", "description": "String ", "status": "String" } ]` |

```json
{
  "Cashflow.Audit": {
    "touchPointHistory": [
      {
        "time": "2023-11-21 05:02:08.968011",
        "user": "1129381",
        "action": "Materialize"
      }
    ],
    "exceptionList": [
      {
        "exceptionCode": "Missing Nostro",
        "businessFlow": "SETTLEMENT",
        "sourceSystem": "RATAN",
        "exceptionType": "BUSINESS",
        "description": "MISSING_NOSTRO_ERROR",
        "status": "PENDING_OPERATOR"
      }
    ]
  }
}
```

## Data exposure and risks

The V1 projection includes trade, payment, account, BIC, beneficiary, correspondent, address, counterparty, staff PSID, operator-comment, exception, and encoded transaction-detail fields. The source documents broad read access and an entitlement role but does not establish consumer-specific field permissions, masking, classification, response typing, or serialization rules.

Examples use JSON `null`, empty strings, literal `"null"` strings, and boolean-like strings such as `"f"` and `"false"`. Consumers therefore need a stable response-schema and nullability contract.

## Related pages

- [[entitlement-controlled-cashflow-query-api]]
- [[sql-query-governance-for-cashflow-data-provider]]
- [[cashflow-audit-query-payload]]
- [[cash-settlement-cashflow-read-model]]
- [[denormalized-cashflow-query-read-model]]
- [[postgresql-global-replication-and-continuous-consistency]]
- [[what-is-the-approved-query-language-and-security-boundary-for-cashflow-data-provider]]
---

---FILE: wiki/entities/ems2.md---
---
type: entity
title: EMS2
tags: [access-management, authorization, cash-settlement]
related: [fmaa, entitlement-controlled-cashflow-query-api, dqsl, rataneod, fmmis]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# EMS2

EMS2 is the access-management system referenced by the cashflow Query Service design.

The documented consumer identities require the `RATAN_FUNC: SYS_RO` functional role. DQSL/SSDR retrieval additionally uses the source-spelled `RATAN_DATA_ENTIELEMENT` data-entitlement role, with Global, GBS, and Onshore scopes mentioned but not defined.

Production role and bank-ID mapping requests are described as ServiceNow/SRM bulk-request processes. The source does not define the entitlement evaluation logic or prove row-level and field-level enforcement.

See [[entitlement-controlled-cashflow-query-api]] and [[what-field-level-data-entitlements-and-masking-apply-to-external-cashflow-queries]].
---

---FILE: wiki/entities/fmaa.md---
---
type: entity
title: FMAA
tags: [authentication, token, cash-settlement]
related: [ems2, entitlement-controlled-cashflow-query-api, query-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# FMAA

FMAA is the authentication system named by the cashflow Query Service contract.

Requests require `FMAA-Token`, `FMAA-UserId`, and `FMAA-AppId` headers. The source states that the user ID and application ID must match the values used to create the FMAA token.

Authentication is documented separately from EMS2 authorization and data entitlement. Token validation, expiry, audience, and service-to-service identity controls are not specified.
---

---FILE: wiki/entities/dqsl.md---
---
type: entity
title: DQSL
tags: [consumer-system, ssdr, cashflow-data]
related: [ems2, entitlement-controlled-cashflow-query-api, query-service]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# DQSL

DQSL is a documented consumer of the cashflow Query Service on behalf of SSDR.

The listed identity is `fmdp_dqsl_batch` with the EMS2 role `RATAN_FUNC: SYS_RO`. A DQSL request is treated as SSDR data retrieval only when it contains both `Bank-Id` and `Country` headers; otherwise the service handles it as EOD retrieval.

The source does not establish which fields DQSL may retrieve, whether the two headers enforce row filtering, or whether the integration is active in production.
---

---FILE: wiki/entities/rataneod.md---
---
type: entity
title: RATANEOD
tags: [consumer-system, eod, cashflow-data]
related: [ems2, query-service, entitlement-controlled-cashflow-query-api]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# RATANEOD

RATANEOD is a named consumer of the cashflow Query Service.

The documented service identity is `srv.ratan.001`, assigned the EMS2 role `RATAN_FUNC: SYS_RO`. Requests that do not include both `Bank-Id` and `Country` are handled as EOD retrieval in the documented routing model.

The source does not confirm RATANEOD production use, expected query patterns, or authorized field set.
---

---FILE: wiki/entities/fmmis.md---
---
type: entity
title: FMMIS
tags: [consumer-system, cashflow-data]
related: [ems2, query-service, entitlement-controlled-cashflow-query-api]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# FMMIS

FMMIS is a named consumer of the cashflow Query Service.

The source lists `g.fmoappdev.001` as its service identity and assigns `RATAN_FUNC: SYS_RO` in EMS2. No FMMIS-specific query contract, data scope, field entitlement, or production-validation evidence is provided.
---

---FILE: wiki/concepts/entitlement-controlled-cashflow-query-api.md---
---
type: concept
title: Entitlement-Controlled Cashflow Query API
tags: [cashflow-data, api-security, authorization, data-entitlement]
related: [query-service, cash-settlement-query-cn-cashflow-data, ems2, fmaa, dqsl, rataneod, fmmis, sql-query-governance-for-cashflow-data-provider]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# Entitlement-Controlled Cashflow Query API

The cashflow Query Service is designed as an external REST data-provider API over [[cash-settlement-query-cn-cashflow-data]]. It combines FMAA authentication, EMS2 functional authorization, and a separate data-entitlement mechanism.

## Consumer routing

- [[dqsl]] requests containing both `Bank-Id` and `Country` are documented as SSDR retrieval.
- Requests missing either header are documented as EOD retrieval, applicable to consumers such as [[rataneod]].
- [[fmmis]] is also identified as a read-only consumer.

## Documented authorization model

Consumers receive `RATAN_FUNC: SYS_RO`. SSDR-related access additionally depends on `RATAN_DATA_ENTIELEMENT`, a source-spelled role whose Global, GBS, and Onshore scopes are named but not defined.

Errors `461` and `463` indicate entitlement-related failures in phase one. The source does not clarify whether entitlement is implemented as row filtering, country-to-bank mapping, query denial, field filtering, or a combination.

## Required security boundary

Because callers submit SQL-like text and the available projection includes sensitive payment, account, address, staff, audit, and transaction fields, functional read access alone is insufficient as a complete policy. A secure contract requires explicit authentication, consumer identity, row scope, field scope, masking, auditability, and query-resource controls.

See [[what-field-level-data-entitlements-and-masking-apply-to-external-cashflow-queries]].
---

---FILE: wiki/concepts/sql-query-governance-for-cashflow-data-provider.md---
---
type: concept
title: SQL Query Governance for Cashflow Data Provider
tags: [sql, api-security, query-governance, cashflow-data]
related: [query-service, cash-settlement-query-cn-cashflow-data, entitlement-controlled-cashflow-query-api, value-date-bounded-cashflow-queries, what-is-the-approved-query-language-and-security-boundary-for-cashflow-data-provider]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# SQL Query Governance for Cashflow Data Provider

The Query Service design accepts `queryCondition` as a SQL string referencing `cash_settlement_query_cn.cashflow_data`. It documents rejection of invalid SQL, non-query SQL, unsupported operations, and unsupported fields through phase-one error `461`.

The documented keyword allowance contains `limit` and `count`, while examples also use `OFFSET`. This is not a complete query-language definition.

## Governance requirements

A production query-provider contract should define:

- a parsed and allowlisted SQL grammar rather than text-pattern validation;
- permitted tables, columns, operators, functions, clauses, aliases, and aggregates;
- parameter binding and injection resistance;
- role- and consumer-specific row and field authorization;
- mandatory deterministic ordering for pagination;
- maximum result count, page size, payload size, execution time, and query cost;
- rate limiting, concurrency limits, cancellation, and retry behavior;
- query and entitlement-decision audit logging; and
- stable error semantics across API phases.

The source's fewer-than-30,000-record phase-one limit and `462` instruction to use `LIMIT` are useful constraints, but do not by themselves establish governance or safety.

See [[what-is-the-approved-query-language-and-security-boundary-for-cashflow-data-provider]].
---

---FILE: wiki/concepts/cashflow-audit-query-payload.md---
---
type: concept
title: Cashflow Audit Query Payload
tags: [cashflow-data, audit, json, query-api]
related: [cash-settlement-query-cn-cashflow-data, query-service, entitlement-controlled-cashflow-query-api, what-field-level-data-entitlements-and-masking-apply-to-external-cashflow-queries]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# Cashflow Audit Query Payload

`Cashflow.Audit` is a JSON-valued output documented for the cashflow Query Service. It contains manual touchpoint history and cashflow exception details.

## Query prerequisite

A SQL query that selects `Cashflow.Audit` must also select `Cashflow.Cashflow_Id`.

## Payload structure

```json
{
  "Cashflow.Audit": {
    "touchPointHistory": [
      {
        "time": "String",
        "user": "String",
        "action": "String"
      }
    ],
    "exceptionList": [
      {
        "exceptionCode": "String",
        "businessFlow": "String",
        "sourceSystem": "String",
        "exceptionType": "String",
        "description": "String ",
        "status": "String"
      }
    ]
  }
}
```

`touchPointHistory` may be `null` in the documented response samples. The payload may expose operator identifiers, workflow actions, exception reasons, and source-system information. Consumer authorization and masking requirements are not specified.
---

---FILE: wiki/queries/what-is-the-approved-query-language-and-security-boundary-for-cashflow-data-provider.md---
---
type: query
title: What Is the Approved Query Language and Security Boundary for Cashflow Data Provider?
tags: [open-question, sql, api-security, cashflow-data]
related: [sql-query-governance-for-cashflow-data-provider, entitlement-controlled-cashflow-query-api, query-service, cash-settlement-query-cn-cashflow-data]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# What Is the Approved Query Language and Security Boundary for Cashflow Data Provider?

The source accepts a SQL string in `queryCondition` and states that unsupported SQL operations and fields should be rejected. It lists `limit` and `count` as function keywords, while examples use `OFFSET`.

## Questions to resolve

- What SQL grammar, clauses, operators, aggregates, functions, aliases, joins, and identifiers are allowed?
- Is SQL parsed into an AST before execution, and are table, field, function, and predicate allowlists enforced?
- How are parameters bound, query cost bounded, and execution timeout enforced?
- What are the pagination, ordering, rate-limit, audit-log, and denial semantics?
- How do EMS2 roles and data entitlement control rows and sensitive columns independently of SQL validation?

The answer should establish a versioned client contract and security review evidence.
---

---FILE: wiki/queries/what-are-the-authoritative-cashflow-query-api-slos-and-volume-limits.md---
---
type: query
title: What Are the Authoritative Cashflow Query API SLOs and Volume Limits?
tags: [open-question, capacity-planning, performance, query-service]
related: [query-service, cash-settlement-capacity-planning-baseline, cash-settlement-query-cn-cashflow-data, postgresql-global-replication-and-continuous-consistency]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# What Are the Authoritative Cashflow Query API SLOs and Volume Limits?

The source contains several provisional thresholds:

- phase one: fewer than 100,000 database records;
- phase-one endpoint envelope: fewer than 30,000 returned records and 2 requests/second/node;
- phase two: more than 300,000 database records and more than 60 seconds for fewer than 100,000 returned records;
- phase three: more than 1,000,000 records, many consumers, and second-level return time.

The 100,000–300,000 database-record range is not addressed. The thresholds describe different dimensions and do not provide formal latency percentiles, timeout values, payload limits, concurrency targets, or a distinction between interactive and batch workloads.

## Resolution needed

Define authoritative SLOs and capacity tiers, including data volume, result size, payload size, p95/p99 latency, request concurrency, rate limits, timeout behavior, freshness requirements, and evidence required before transitioning to replica or alternative-storage architectures.
---

---FILE: wiki/queries/what-field-level-data-entitlements-and-masking-apply-to-external-cashflow-queries.md---
---
type: query
title: What Field-Level Data Entitlements and Masking Apply to External Cashflow Queries?
tags: [open-question, data-entitlement, data-security, cashflow-data]
related: [entitlement-controlled-cashflow-query-api, cashflow-audit-query-payload, ems2, cash-settlement-query-cn-cashflow-data]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/Expose The Cashflow Data Design.md"]
---
# What Field-Level Data Entitlements and Masking Apply to External Cashflow Queries?

The external query projection includes account numbers, BICs, beneficiary and correspondent names and addresses, counterparty identifiers, staff PSIDs, user comments, audit histories, exception details, and encoded `Cashflow.Transaction_Details`.

The source describes `RATAN_FUNC: SYS_RO` and `RATAN_DATA_ENTIELEMENT` but does not state which consumers may retrieve each field, whether fields are masked, how data classifications apply, or whether `Bank-Id` and `Country` impose row-level restrictions.

## Resolution needed

Define a consumer-by-field authorization matrix, row-scope policy, masking and redaction rules, audit-data access policy, retention controls, and test evidence for RATANEOD, DQSL/SSDR, FMMIS, and future consumers.
---

---FILE: wiki/log.md---
## 2026-08-24 ingest | Expose The Cashflow Data Design

- Ingested the cashflow Query Service design, including the SQL-string API contract, EMS2/FMAA access model, phased capacity proposals, and `Cashflow.Audit` payload requirement.