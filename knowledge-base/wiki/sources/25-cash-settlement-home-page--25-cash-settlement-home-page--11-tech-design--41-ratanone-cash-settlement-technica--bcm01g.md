---
type: source
title: Self Service New Branch Entity Onboarding Design
authors: []
year: 2026
url: ""
venue: Internal technical design
created: 2026-08-24
updated: 2026-08-24
tags: [ratanone, entity-onboarding, static-configuration, draft-design]
related: [self-service-entity-branch-onboarding, centralized-static-configuration-management, maker-checker-configuration-governance, entity-onboarding-configuration-architecture-options, ratan-static-data-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Self Service new branch entity onboarding Design.md"]
---
# Self Service New Branch Entity Onboarding Design

## Summary

This draft design proposes replacing developer-led new entity and branch onboarding in RatanOne with UI Blotter-managed configuration. The stated objective is that business users can add or change onboarding data without a production code deployment.

Four alternatives are presented, but the document does not select or approve one:

1. Multiple service-oriented Blotters using service databases and Config Server.
2. Multiple service-oriented Blotters using service databases only.
3. One aggregated Blotter owned by [[ratan-static-data-service]], which distributes configuration to downstream services through Kafka.
4. One Excel upload/download Blotter that writes parsed data into multiple schemas.

The source should be treated as a proposal rather than an implementation-ready specification. It contains unresolved configuration ownership, incomplete Kafka operating semantics, inconsistent table placement, and several draft API defects.

## Intended Configuration Scope

The proposed onboarding capability covers front-end static lists and service-owned configuration including:

- Booking entity, FMID, country, branch-code, currency, and settlement-means mappings.
- Currency cutoff configuration.
- ISO currency mappings.
- Swift sender and correspondent BIC configuration.
- Accounting EBBS bridge-account and transaction-code configuration.
- [[ratan-cashflow-rounding-config]].
- `ratan_bridge_flow`.
- Runtime settings currently held in service configuration, including `time-zone.mappings`, `mx-generation.entity-scope-conditions`, `sd.branch-code.mappings`, and `STRATEGIC_FM_LIST`.

The design requires CRUD, confirmation, cancellation, record audit, and paginated history for managed configuration.

## Architecture Alternatives

| Option | UI model | Primary configuration storage | Distribution model |
|---|---|---|---|
| Option 1 | Multiple service-oriented Blotters | Service DB tables plus Config Server | Services read their DB and Config Server configuration |
| Option 2 | Multiple service-oriented Blotters | Service DB tables | Services read DB configuration |
| Option 3 | One aggregated onboarding Blotter | `ratan-static-data-service` DB plus downstream service DB tables | `ratan-static-data-service` publishes static configuration through Kafka |
| Option 4 | One Excel upload/download Blotter | Different DB schemas | `ratan-static-data-service` parses Excel and inserts data; Config Server remains required for non-migrated `application.yml` settings |

Option 3 is the most centralized UI model, but it creates distributed configuration state. The source proposes `sync_status`, `sync_success_count`, and a per-service result table, but does not define a topic, event schema, replay, idempotency, reconciliation, timeout, rollback, or partial-failure recovery process.

## Proposed Service-File Migration

| Service | Existing configuration | Option 1 treatment | Options 2–3 treatment |
|---|---|---|---|
| `accouting-service` | `time-zone.mappings` | Read from Config Server | Remove and migrate to `ratan_static__country_conf` |
| [[swift-service]] | `mx-generation.entity-scope-conditions` | Read from Config Server | Remove and migrate to `ratanone_swift_service.swift_mx_generation_condition` |
| `static-data-service` | `sd.branch-code.mappings` | Read from Config Server | Remove and migrate to `ratan_static__entity_conf` |
| [[ratan-cash-settlement-orchestration]] | `STRATEGIC_FM_LIST` | Read from Config Server | Remove and migrate to `ratan_static__common_metadata_dict` |

## Proposed Database Table Design

| tableName | columnName | columnType | index | comment | desciption |
|---|---|---|---|---|---|
| ratanone.ratan_static__common_metadata_dict | id | bigserial | PK | | save settlementMeans、currency list for FE blotter config. |
|  | field_value | text |  |  |  |
|  | field_type | text |  |  |  |
|  | created_at | timestamp |  |  |  |
|  | updated_at | timestamp |  |  |  |
| ratanone.ratan_static__country_conf | id | bigserial | PK | | save country zoneId for FE blotter config and accounting service |
|  | code | text |  |  |  |
|  | country | text |  |  |  |
|  | zoneId(use config server, remove the field) | text |  |  |  |
|  | created_at | timestamp |  |  |  |
|  | updated_at | timestamp |  |  |  |
| ratanone.ratan_static__entity_conf | id | bigserial | PK | | 1.save entity and country mapping 2. save entity and branch code mapping 3. save fmid and entity mapping (FE 、swift service and accountting service use it, now store in local config file and FE hard code) |
|  | fmId | text |  |  |  |
|  | booking_entity | text |  |  |  |
|  | country_code | text |  |  |  |
|  | branch_code(use config server, remove the field) | text |  |  |  |
|  | created_at | timestamp |  |  |  |
|  | updated_at | timestamp | PK |  |  |
| ratanone.ratan_static__isocurrency_mapping (use config server, remove this table) | id | bigserial |  |  | save currency and iso currency mapping (swift service and accountting service use it, now store in local config file) |
|  | currency | text |  |  |  |
|  | iso_currency | text |  |  |  |
|  | created_at | timestamp |  |  |  |
|  | updated_at | timestamp |  |  |  |
| ratanone_swift_service.swift_[mx](http://ratanone.mx/)_generation_condition (use config server, remove this table) | id | bigserial |  |  | save [mx](http://ratanone.mx/)_generation_condition (swift service use it, now store in local config file) |
|  | entity | text |  |  |  |
|  | sender | text |  |  |  |
|  | receiver | text |  |  |  |
|  | currency | text |  |  |  |
|  | mtTypes | text |  |  |  |
|  | created_at | timestamp |  |  |  |
|  | updated_at | timestamp |  |  |  |
| ratan_static__entity_onboarding_config | id | bigserial | PK | | save the whole entity static config |
|  | fmId | text |  |  |  |
|  | booking_entity | text |  |  |  |
|  | country_code | text |  |  |  |
|  | country | text |  |  |  |
|  | content | jsonb | gin |  |  |
|  | sync_status | int |  | 0 processing 1 success 2 fail |  |
|  | sync_success_count | int |  |  |  |
|  | data_status | text |  |  |  |
|  | maker_id | text |  |  |  |
|  | checker_id | text |  |  |  |
|  | created_at | timestamp |  |  |  |
|  | updated_at | timestamp |  |  |  |
| ratan_static__entity_onboarding_config_sync_result | id | bigserial |  |  | save service sync result |
|  | config_id | bigint |  |  |  |
|  | service_name | text |  |  |  |
|  | exec_status | bool |  | 1 success 0 fail |  |
|  | reason | text |  |  |  |
|  | created_at | timestamp |  |  |  |
|  | updated_at | timestamp |  |  |  |

## Draft API Pattern

The source repeatedly proposes list/filter, create/update, delete, audit, history, confirm, and cancel endpoints. Common control fields are `dataStatus`, `makerId`, `checkerId`, `createdAt`, and `updatedAt`.

These API examples are illustrative only. In particular:

- Entity create, update, delete, audit, history, confirm, and cancel paths incorrectly use `/v1/static/country`.
- Several example payloads are invalid JSON.
- Naming differs between `fmId`, `fmid`, and `entityId`; `bookingEntity`, `booking_entity`, `legalEntity`, and `entityName`; and `countryCode` versus misspelled `contryCode`.
- Confirmation and deletion paths use inconsistent identifiers in the accounting EBBS examples.
- The aggregate Option 3 cancel path omits `/cancel`.

## Open Design Issues

- The authoritative store for each configuration domain is not determined between Config Server, static-data tables, and downstream service tables.
- The authority of `ratan_static__entity_onboarding_config.content` after Kafka propagation is unspecified.
- Maker-checker status transitions, checker authorization, approval timing, audit retention, and immutable history requirements are not specified.
- The scope for precious-metals lists, Swift PM/UDF configuration, and `static_data_cfi_code` remains open.
- The document asks whether all onboarding Blotters require batch operations but offers no decision.
- [[ratan-cash-settlement-orchestration]] is proposed to add an FMID-filter service task, but its detailed contract is absent.

See [[which-entity-onboarding-configuration-option-is-approved]], [[what-is-the-authoritative-store-for-entity-onboarding-configuration]], and [[what-is-the-kafka-contract-and-recovery-process-for-onboarding-config-sync]].