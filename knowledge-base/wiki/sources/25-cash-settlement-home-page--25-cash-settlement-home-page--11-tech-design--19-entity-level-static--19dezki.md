---
type: source
title: Entity-Level Static Data Onboarding Design
authors: []
year: 2026
url: "https://confluence.global.standardchartered.com/display/DSP/FXU+-+RATAN+analysis"
venue: "Internal Confluence technical design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, RATAN, entity-onboarding, static-data, configuration]
related: [cash-settlement-entity-onboarding, entity-level-static-data-consolidation, ratan-static-cashflow-nostro, static-data-service, cash-settlement-platform, cash-settlement-service-landscape, cash-settlement-shared-platform-architecture, cashflow-blotter]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Entity level static.md"]
---
# Entity-Level Static Data Onboarding Design

## Summary

This internal technical design addresses the fragmented configuration and static-data work required to onboard a new entity across the RATAN and Cash Settlement service landscape. The source identifies multiple manual updates spanning Rule Engine, Static Data, LMS, Swift Service, Accounting, Cashflow Blotter, and Workflow.

The proposal is to maintain most entity-level onboarding attributes in one table and allow self-service configuration. Nostro Static is explicitly excluded and remains a separate mandatory setup.

## Current onboarding dependencies

| **#** | **Description** | **Table** | **Type** | **Domain** | **Key** | **Comment** |
| --- | --- | --- | --- | --- | --- | --- |
| 1 | Bypass Validation Rule | ratanone.ratan_rule_engine | DB Static | Rule engine | | This will be dropped by new MO validation |
| 2 | Nostro Static Setup (mandatory for each entity) | ratanone.ratan_static__cashflow_nostro | Static | Static Data | Entity FMID + CCY + Settlement Means + Settlement Method | Self Serviced |
| 3 | Currency Release Time (mandatory for each entity) | ratanone.ratan_static_cashflow_currency_cut_off | DB Static | Static Data | Entity FMID + CCY | Can be made self-service |
| 4 | LMS Feed Exclusion Entity List Update | | Service Config | LMS | Entity FMID | Can be merged into 1 table to maintain Booking Entity Information, as well as self-service |
| 5 | SWIFT Generation Changes | ratanone_swift_service.swift_static_data_sender_bic ratanone_swift_service.swift_static_data_correspondent_bic | DB Static | Swift Service | Entity FMID |
| 6 | ratanone-static-data-service: Branch Code Mapping | | Config | Static Data | Entity FMID |
| 7 | Settlement Accounting | ratanone.ratan_static__cashflow_ebbs_txn_code ratanone.ratan_static__cashflow_ebbs_bridge_account | DB Static | Accounting service | Entity FMID |
| 8 | Include new branch in GUI Drop down | | UI Config | Cashflow Blotter | Entity FMID |
| 9 | STP White List | | Config | Workflow | Entity FMID |
| | | | | | | |

## Proposed consolidated table

The source proposes maintaining one table for the onboarding attributes listed below, except for Nostro Static.

| ** ** | **Type** | **Possible Value** | **Comment** | **Nature** |
| --- | --- | --- | --- | --- |
| 1 | Booking Entity FMID | 300089409 | To cover above item 8, Include new branch in GUI Drop down | Data |
| 2 | Booking Entity FMCODE | SCB MNL FCD*MNL | |
| 3 | Workflow Flag | Strategic/Legacy/CPT | To cover above item 9, STP White List | Config / Dev |
| 4 | LMS Filter | true/false | To cover above item 4, LMS Feed Entity White List | Config / Dev |
| 5 | Branch Code | 59 | To cover above item 6, ratanone-static-data-service: Branch Code Mapping | Data |
| 6 | country | PH | To cover above item 7 Settlement Accounting ratanone.ratan_static__cashflow_ebbs_txn_code ratanone.ratan_static__cashflow_ebbs_bridge_account | Data |
| 7 | posting_branch | 100 | |
| 8 | txn_type_code | RTO | |
| 9 | txn_dr_code | 478 | |
| 10 | txn_cr_code | 378 | |
| 11 | ebbs_bridge_account | 78653775888 | |
| 12 | currency | PHP | To cover above item 5 ratanone_swift_service.swift_static_data_correspondent_bic ratanone_swift_service.swift_static_data_sender_bic | Data |
| 13 | Correspondent BIC | SCBLPHMMXXX | |
| 14 | Sender BIC | SCBLPHMMXXX | |

The example values appear to be illustrative configuration values rather than universal production constants.

## Proposed operating model

The design aims to replace multiple manual uploads and change requests with a central, self-service entity configuration process. Its stated benefits are:

- Fewer onboarding touchpoints.
- Reduced risk of manual error.
- Automated or systematic validation.
- Faster time to market.
- Reduced dependence on formal change requests.
- Potentially shorter onboarding lead time than the stated minimum of two weeks.

The source does not define whether consuming services would read the table directly or receive service-specific projections through APIs, events, exports, or configuration refreshes.

## Nostro Static exception

Nostro Static remains outside the proposed consolidated table. Its key is:

- Entity FMID
- Currency
- Settlement Means
- Settlement Method

This creates a two-model onboarding process: a consolidated entity-level model for most attributes and a separate Nostro model for settlement-specific configuration. Nostro setup is described as mandatory and self-serviced.

## Additional thinking

The source suggests a common key/value static-data pattern for:

1. BIC netting static
2. FXU static
3. Profile limit

This is presented as future thinking rather than a completed design. The source does not specify namespaces, type safety, validation semantics, ownership, versioning, auditability, effective dates, or approval workflows for such a model.

## Design gaps and risks

The source does not define:

- The physical schema and cardinality of the consolidated table.
- Whether the table has one row per entity, entity and currency, or entity and domain attribute.
- Composite keys for accounting and Swift configuration.
- The system of record and field-level ownership.
- Validation rules for identifiers, currencies, countries, BICs, accounting codes, and cross-field consistency.
- Authorization, maker-checker approval, audit history, versioning, effective dates, or rollback.
- Propagation and cache-refresh behavior for consuming services.
- Migration from existing service-specific tables and configuration.
- Coordination between the central entity record and separate Nostro configuration.

Centralizing data from multiple domains may reduce onboarding effort, but it may also create a shared database dependency or coordination bottleneck. The proposal should therefore be treated as an architectural hypothesis pending a formal data model and operating model.

## Relationship to existing wiki knowledge

This source extends [[concepts/cash-settlement-service-landscape]] and [[concepts/cash-settlement-shared-platform-architecture]] by focusing on entity onboarding as a cross-service configuration problem. It is also relevant to [[entities/static-data-service]], [[entities/cashflow-blotter]], and [[entities/cash-settlement-platform]].

The source does not directly contradict existing wiki content, but it leaves unresolved whether centralization should use a shared physical table, a central service, or a central source with domain-specific projections.

## Source context

The source references **FXU - RATAN analysis - Derivative Strategy Projects - Confluence** and is located at:

`Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Entity level static.md`