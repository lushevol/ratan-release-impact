---
type: source
title: Rule Service Migration
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, rule-engine, migration, archived-design, drools]
related: [ratanone-rule-service, ratan-rule-service, ratan-suppression-service, rule-service-consolidation, business-flow-and-rule-type-classification, database-backed-rule-loading, rule-service-domain-boundaries, cn-rule-prevalidation, canonical-business-flow-and-rule-type-taxonomy, authoritative-rule-service-migration-and-reconciliation-plan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Migration.md"]/Rule Service Migration.md"]/Rule Service Migration.md"]
authors: []
year: 0
url: ""
venue: "Archived internal technical design"
---
# Rule Service Migration

## Status and scope

This archived design proposes consolidating the CN-focused [[ratan-rule-service]] and the BAU suppression-rule service into [[ratanone-rule-service]]. The intended target would maintain and validate the migrated rules from a common database table.

The document records design intentions rather than implementation evidence. AS-IS and TO-BE diagrams, target API details, production-rule inventory, migration controls, UI estimates, and completion evidence are absent.

It supplements the broader rule-engine selection material in [[sources/25-cash-settlement-home-page--25-cash-settlement-home-page--11-tech-design--34-technology-selection-rule-engine--1jza84g]].

## Proposed service consolidation

The intended target service is [[ratanone-rule-service]], which already serves FX-replication filtering rules and detective rules. Proposed migration scope includes:

- CN rules from [[ratan-rule-service]].
- BAU Suppression Rules and Netting Rules.
- Database storage and validation of the consolidated rules.

The document explicitly excludes Data Entitlement Rule from this migration; it should remain a standalone capability. This is consistent only with the migration boundary, not with a conclusion about the current owner of entitlement enforcement; see [[concepts/cash-settlement-data-entitlement]].

A naming ambiguity remains: the Background refers to `ratan-suppression-service`, while the schema-comparison section refers to `ratanone-suppression-service`. See [[does-ratan-suppression-service-mean-ratanone-suppression-service]].

## Database schema changes

### BAU suppression-rule schema mapping

|  | `ratanone.ratan_suppresion_rule` | `ratanone_rule_service.ratan_rule` |  |
| --- | --- | --- | --- |
| **Column Changed** | id (bigserial) | id (text) | Column type was changed from bigserial to text. |
| *business_workflow* | *business_flow* | Column name changed. |
| creator | created_by | Column name changed. |
| create_timestamp | created_at | Column name changed. |
| last_modifier | updated_by | Column name changed. |
| last_modify_timestamp | updated_at | Column name changed. |
| *hierarchy* | N/A | Removed. |
| *value_date* | N/A | Removed. |

The recorded answers approve the renamed columns and confirm that `hierarchy` and `value_date` are no longer used by the new Rule Service. This is a stated design decision, not proof that historical reporting or downstream consumers no longer require those fields.

### CN-rule schema mapping

|  | `ratan_rule_service.ratan_rule` | `ratanone_rule_service.ratan_rule` |  |
| --- | --- | --- | --- |
| **Column Changed** | operation_level | N/A | Removed. |
| exception_code | N/A | Removed. |
| exception_category | N/A | Removed. |
| N/A | fact_processor | Add, a replacement for CN special rule processor. |

The source explicitly states that the Rule Service will not maintain exception-to-rule relationships. It does not identify the target owner for exception metadata, action data, or traceability. See [[where-are-rule-to-exception-relations-and-nstp-exception-metadata-owned]].

## Rule retrieval and classification

The proposed target stores rules in database tables and loads applicable rules for validation using `business_flow` and `rule_type`. CN and BAU rules are intended to share `ratanone_rule_service.ratan_rule` and be differentiated by that pair of values.

A default `rule_type` was accepted, but its value is not specified. The model is incomplete because the listed BAU rules include `NULL` rule types and use lower-case values while listed CN rules use upper-case values. See [[business-flow-and-rule-type-classification]] and [[canonical-business-flow-and-rule-type-taxonomy]].

### BAU UAT rule inventory

| Item # | business_workflow | rule_type | num_of_rules |
| --- | --- | --- | --- |
| 1 | SETTLEMENT | nstp | 6 |
| 2 | SETTLEMENT | NULL | 11 |
| 3 | SETTLEMENT_AUTO_NETTING | netting | 2 |
| 4 | CONFIRMATION | NULL | 16 |

```sql
select sr.business_workflow, sr.rule_type, count(1) as num_of_rules from ratanone.ratan_suppresion_rule sr  
 where sr.status = 'ADD_CONFIRMED' or sr.status = 'DEL_PEDNING' group by sr.business_workflow, sr.rule_type;
```

### CN UAT rule inventory

| Item # | business_flow | rule_type | num_of_rules |
| --- | --- | --- | --- |
| 1 | STRATEGIC_SETTLEMENT | IRS | 1 |
| 2 | STRATEGIC_SETTLEMENT | NSTP | 23 |
| 3 | STRATEGIC_SETTLEMENT | NETTING | 2 |
| 4 | STRATEGIC_SETTLEMENT | SUPPRESSION | 29 |

```sql
select rr.business_flow, rr.rule_type, count(1) as num_of_rules from ratan_rule_service.ratan_rule rr 
    where rr.status = 'ADD_CONFIRMED' or rr.status = 'DEL_PEDNING' group by rr.business_flow, rr.rule_type;
```

`DEL_PEDNING` is preserved exactly as written. It must be verified before treating it as either a valid persisted status or a typographical error.

## Migration approach

BAU and CN teams are asked to provide production rules in `sample.csv` format. Lin Liang is assigned to import the rules into Rule Service and generate corresponding [[drools]] rule records in the database.

The source gives no CSV mapping, transformation specification, count reconciliation, semantic validation, approval gate, rollback procedure, idempotency method, promotion process, or confirmation that the import occurred. See [[authoritative-rule-service-migration-and-reconciliation-plan]].

## Service boundaries

| Area | Stated direction |
| --- | --- |
| BAU Suppression Rule | Implement in `ratanone-rule-service`. |
| BAU Netting Rule | Implement in `ratanone-rule-service` with `netting` rule type. |
| Data Entitlement Rule | Standalone; does not migrate to `ratanone-rule-service`. |
| Fields / Fields Xpath | Remove from Rule Service; most likely part of static data service. |
| Profile Limitation | In scope of the Rule domain service. |
| Frontend Validation Rule | Not in Rule Service; should belong to static data service. |

These decisions define the proposed boundary captured in [[rule-service-domain-boundaries]], but do not specify the static-data-service target, data migration, authorization, client transition, or API ownership.

## CN validation behavior

The CN path is not described as a single uniform rule execution flow:

- Suppression Rule checks `Cashflow.Is_Cashflow_Unsuppress`.
- Special Rule fetches data from a third-party service before processing.
- IRS Rule has additional checks before validation.
- Netting Rule has additional checks before validation.
- NSTP Rule does not start validation if exceptions exist.
- Swift Suppression Rule follows Suppression Rule behavior.

The sequence, conditions, third-party contract, and target implementation are unspecified. See [[cn-rule-prevalidation]], [[concepts/nstp-maker-checker-processing]], and [[concepts/cashflow-netting]].

## Legacy APIs

### CN Rule Service API

| API Group | API Endpoint | Method | Remark |
| --- | --- | --- | --- |
| Rule Maintenance | `/v1/rule/add` | POST | Add a new rule. |
|  | `/v1/nstpRule/addSpecial` | POST | Add a new special rule. |
|  | `/v1/nstpRule/SpecialConfig/{businessFlow}` | POST | Special rule configuration by given business_flow. |
|  | `/v1/rule/{businessFlow}/listAll` | GET | List all the rules by given business_flow. |
|  | `/v1/rule/NSTP/listByType` | GET | List all the nstp rules. |
|  | `/v1/rule/SWIFT_SUPPRESSION/listByType` | GET | List all the swift_suppression rules. |
|  | `/v1/rule/SUPPRESSION/listByType` | GET | List all the suppression rules. |
|  | `/v1/rule/NETTING/listByType` | GET | List all the netting rules. |
|  | `/v1/rule/histories` | GET | Get the histories of rules. |
|  | `/v1/rule/{ruleId}/delete` | DELETE | Delete the rule by given rule id. |
|  | `/v1/rule/{ruleId}/delete/confirm` | PUT | Confirm the deleted rule. |
|  | `/v1/rule/{ruleId}/delete/cancel` | PUT | Cancel the rule deletion. |
| Exception | `/v1/nstpException/metaData` | GET | Removed. |
|  | `/v1/nstpException/actionData` | GET | Removed. |
| Profile Limitation? | `/v1/profileLimitation/create` | POST |  |
|  | `/v1/profileLimitation/edit` | PUT |  |
|  | `/v1/profileLimitation/{profile}/{currency}` | DELETE |  |
|  | `/v1/profileLimitation/reject/{profile}/{currency}/{status}` | PUT |  |
|  | `/v1/profileLimitation/confirm/{profile}/{currency}/{status}` | PUT |  |
| Fields | `/v1/fields` | GET |  |
|  | `/v1/fields/upload` | PUT |  |
|  | `/v1/fields/export` | GET |  |
|  | `/v1/fields/config/upload` | PUT |  |
|  | `/v1/fields/versions` | GET |  |
|  | `/v1/fields/versions/activate` | GET |  |
|  | `/versions/{tableName}/{version}/active` | PUT |  |
|  | `/v1/fields/versions/{tableName}/{version}` | DELETE |  |
|  | `/v1/fields/recon/{version}` | PUT |  |
| Validation Rule | `/v1/validationRules/entities/{entity}` | PUT |  |
|  | `/v1/validationRules/entities/{entity}/fields/{field}` | PUT |  |
|  | `/v1/validationRules/entities` | PUT |  |
|  | `/rule/v1/validationRules/entities/{entity}/validate` | POST |  |
|  | `/rule/v1/validationRules/entities/{entity}/fields/{field}` | DELETE |  |

### BAU Suppression Service API

| API Group | API Endpoint | Method | Remark |
| --- | --- | --- | --- |
| Suppression Rule | `/v1/suppressions/rules` | GET |  |
|  | `/v1/suppressions/criteria` | GET |  |
|  | `/v1/suppressions/rules` | POST |  |
|  | `/v1/suppressions/rules/{id}/status` | PUT |  |
|  | `/v1/suppressions/rules/{id}/approve` | PUT |  |
|  | `/v1/suppressions/rules/histories` | GET |  |
| Validation Rule |  |  |  |
| Fields |  |  | Same as CN rule |
| Data Entitlement |  |  | Out of scope |

The target API is referenced only through an external Confluence page. The archived design therefore cannot demonstrate API compatibility, lifecycle equivalence, or UI readiness.