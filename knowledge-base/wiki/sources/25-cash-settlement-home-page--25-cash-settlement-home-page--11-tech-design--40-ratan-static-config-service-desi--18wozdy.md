---
type: source
title: Ratan Static Config Service Design (Draft)
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, static-configuration, draft, graphql, json-schema, caching]
related: [static-data-service, static-configuration-management, schema-validated-static-configuration, cache-first-static-configuration-retrieval, static-config-service-draft-vs-static-configuration-design, what-is-the-authoritative-static-config-api-and-protocol, what-is-the-static-configuration-lifecycle-and-versioning-model]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Ratan Static Config Service Design (Draft).md"]
authors: []
year: 2025
url: ""
venue: ""
---
# Ratan Static Config Service Design (Draft)

This early draft proposes a central, database-backed static-configuration capability to remove mutable configuration from UI code and deployment cycles. It distinguishes UI-only configuration from configuration shared across applications and backend services.

The design assumes that [[static-data-service]] can be extended to expose GraphQL APIs, but this is an unconfirmed assumption. Architecture, management APIs, GUI, service integration, cache behavior, real-time subscription mechanics, and release phases remain incomplete.

## Motivation and scope

The draft identifies hardcoded UI configuration as a release dependency even for minor changes.

| Configuration category | Description | Examples |
| --- | --- | --- |
| UI Config | Configuration used only by a UI. | Query Builder operator mappings, blotter column definitions, UI dropdown options such as CCY. |
| Shared UI Config | Configuration shared across UI applications. | Booking Entity FMCODE/FMID. |

Booking-entity configuration is additionally consumed by a backend service. The high-change example covers CPT entities, system whitelists, and UI entity options for [[ratanone-settlement-orchestration-service]] and multiple micro-frontends.

## Design principles

1. Move mutable configurations to a database instead of hardcoding them, and provide a query service.
2. Provide an intuitive API to query a configuration by name or domain.
3. Store generic configuration data.
4. Provide version control and audit history.

## Proposed persistence structures

The source provides logical table structures rather than physical DDL. It does not specify primary keys, foreign keys, indexes, length limits, transaction semantics, or retention.

### Config Table

| Key | Type | Mandatory | Description |
| --- | --- | --- | --- |
| id | VARCHAR | Yes | unique id |
| context | VARCHAR | Yes | name of config |
| domain | VARCHAR | No | belonging of config. multiple domains separate by comma. |
| schema | VARCHAR | No | schema definition of content, validate the fomat. Use **JSON-Schema**. |
| state | VARCHAR | Yes | LIVE/DISABLED |
| version | VARCHAR | Yes | version |

### Config Content Table

| Key | Type | Mandatory | Description |
| --- | --- | --- | ---|
| id | VARCHAR | Yes | unique id |
| context | VARCHAR | Yes | name of config |
| key | VARCHAR | Yes | key, unique under context |
| value | VARCHAR | Yes | value |
| type | VARCHAR | No | |
| sub_type | VARCHAR | No | |
| metadata | VARCHAR | No | metadata, normally it's a JSON string. |
| state | VARCHAR | Yes | LIVE/DISABLED/UPDATE_PENDING/DEAD/ADD_PENDING |
| version | INT | Yes | |

### Audit Table

| Key | Type | Description |
| --- | --- | --- |
| id | VARCHAR | unique id of audit |
| config_id | VARCHAR | id of config |
| content_id | VARCHAR | id of config content |
| context | VARCHAR | context of config |
| domain | VARCHAR | domain of config. multiple domains separate by comma. |
| state | VARCHAR | UPDATE/ADDED/DELETED/PENDING_UPDATE/PENDING_ADDED/PENDING_DELETED |
| key | VARCHAR | key |
| value | VARCHAR | value |
| type | VARCHAR | type |
| metadata | VARCHAR | metadata |
| schema | VARCHAR | schema definition of content, validate the fomat. Use **JSON-Schema**. |
| version | INT | |
| updated_at | VARCHAR | |
| updated_by | VARCHAR | |

## Example configuration contexts

### `settlement_field_type_operator_mapping`

This low-change context is assigned to `mfe-cashflow-blotter,mfe-cashflow-dashboard`. It maps a field data type to supported filter operators.

```js
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "key": {
      "title": "fieldType",
      "type": "string"
    },
    "value": {
      "title": "operators",
      "type": "string"
    }
  },
  "required": ["key", "value"],
  "additionalProperties": false
}
```

| context | key | value | type | sub_type | metadata | version |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_field_type_operator_mapping | text | `["=", "!=", "in", "notIn"]` | | | | 0 |
| settlement_field_type_operator_mapping | number | `["=", "!=", ">=", "<="]` | | | | 0 |

### `settlement_booking_entities`

This high-change context is assigned to `mfe-cashflow-blotter,mfe-cashflow-dashboard,mfe-trades, ratanone-settlement-orchestration-service`. It represents FMID, FM Code, flow classification, and country metadata.

```js
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "type": "object",
  "properties": {
    "key": {
      "title": "fmId",
      "type": "string"
    },
    "value": {
      "title": "fmCode",
      "type": "string"
    },
    "type": {
      "title": "flow",
      "type": "string",
      "enum": ["NORMAL", "STRATEGIC", "CPT"]
    },
    "metadata": {
      "type": "object",
      "properties": {
        "country": {
          "type": "string"
        }
      }
    }
  },
  "required": ["key", "value", "type", "metadata"],
  "additionalProperties": false
}
```

| context | key | value | type | sub_type | metadata | version |
| --- | --- | --- | --- | --- | --- | --- |
| settlement_booking_entities | 10036642 | SCB SHANGH*SHA | STRATEGIC | | `{"country":"CHINA"}` | 0 |
| settlement_booking_entities | 400899993 | SCB CN CHO*CHO | CPT | | `{"country":"CHINA"}` | 0 |

The source also provides these current-style backend whitelist fields:

```js
{
  FM_LIST: "401036553|400991880|400007847",
  STRATEGIC_FM_LIST: "10075222|400041070|400906330|300036368|3|400452428 ...",
  CPT_ENTITY_LIST: "6|2|10038345|300011345|300075472"
}
```

## Illustrative client interfaces

The draft refers both to assumed GraphQL APIs and to a REST-style POST example. No authoritative protocol or contract is defined.

```js
fetch("/api/ratan/staticconfig", { method: "POST", body: { query: "" } })
```

```js
const { data, isLoading, error } = useStatisConfigByNames(["settlement_booking_entities"], { cache: true });
// data
{ totalResults: 2, results: [ ], }
```

`useStatisConfigByNames` is preserved as written in the source.

## Cache and real-time direction

For web consumers, the draft recommends cache-first retrieval: return cached configuration when available, refresh it in the background, and update with the latest result when the query completes. On a first call or cleared cache, dependent components wait for the current result and populate the cache.

The service-side cache is recorded only as “Radis,” likely referring to [[redis]], without topology or correctness semantics. Feature flags are identified as a use case for real-time subscription because query-only usage cannot detect configuration changes.

## Draft limitations and unresolved tensions

- The operator-mapping schema declares `value` as a string, while its examples use arrays. The generic storage model also defines `value` as `VARCHAR`.
- Definition, content, and audit records use different state vocabularies without transition, approval, rollback, or live-read rules.
- `Config Table.version` is `VARCHAR`, while content and audit versions are `INT`; version scope and optimistic-concurrency behavior are unspecified.
- Multiple domains are represented as comma-separated values, with no normalization or query/indexing model.
- API protocol, authorization, mutation behavior, pagination, errors, subscriptions, and cache invalidation are unspecified.
- The draft should be reconciled with [[static-configuration-design]] and [[self-service-entity-branch-onboarding]] before being treated as authoritative.