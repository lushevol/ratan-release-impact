---
type: source
title: Ratan-rule-service Reconstruction for Rule Engine
authors: []
year: 2024
url: ""
venue: "Cash Settlement Home Page / Tech Design / RATANONE Cash Settlement Technical Design"
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, RatanOne, rule-engine, technical-design, schema-evolution]
related: [ratanone-rule-service, ratan-rule-engine, ratan-special-rule-config-v2, ratan-suppression-fields-xpath-v2, ratan-rule-mapping, rule-maintenance-and-validation-pipeline, special-rule-processing, nstp-exception-metadata, suppression-field-data-type-parsing, rule-mapping-and-update-lineage, ratanone, scbml, netting-service, schema-evolution-for-cash-settlement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Ratan-rule-service reconstruction for rule-engine.md"]
---

# Ratan-rule-service Reconstruction for Rule Engine

## Source context

This technical design reconstructs the proposed relationship between `ratanone-rule-service`, the Ratan Rule Engine, domain services, and three persistence tables used for rule configuration and mapping.

Background references:

- [RATAN Rule Engine Overview - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/pages/viewpage.action?pageId=2970380457#RATANRuleEngineOverview-DryRunDesign)
- [Rule Service Tech Design - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/Rule+Service+Tech+Design)

The source does not provide an author, formal publication date, version, approval status, or evidence that the proposed changes were deployed.

## Rule maintenance

`NSTP`, netting, suppression, and Swift Suppression rules are maintained directly by `ratanone-rule-service`, including creation, deletion, status changes, and rule-content updates. For `NSTP` rules, the UI supplies exception information in `metaData` and passes it to the service.

## Provisional rule response example

The following response is reproduced from the source:

```json
[{
"id": "7165211647473512448",
"businessFlow": "STRATEGIC_SETTLEMENT",
"ruleType": "NSTP",
"userRule": "Cashflow__Cashflow_Amount_USD_Transfered > 1000000",
"runningRule": "...",
"status": "ADD_PENDING",
"reason": "High Value Payment",
"comment": "user comment",
"executionFlag":"EXECUTION",
"needDryRun": false,
"referenceRuleId":"7165211647473512333",
"version": 0,
"ruleCategory": "NORMAL",
"metaData": "{\"exceptions\": [{\"exceptionCode\": \"CORP CLIENT\",\"operationLevel\": \"MAKER_CHECKER\",\"exceptionCategory\": \"NSTP\"}]}",
"createdAt": "2024-02-19T05:12:59.953340101Z",
"updatedAt": "2024-02-19T05:12:59.953361678Z",
"createdBy": "1632093",
"updatedBy": "1632093"
}]
```

The source identifies `ruleCategory` values of `NORMAL` and `SPECIAL`. The example `metaData` contains an exception code, an operation level, and an exception category. The documented operation levels are `MAKER_ONLY`, `CHECKER_ONLY`, and `MAKER_CHECKER`. The documented exception categories are `NSTP`, `HIGH_RISK_NSTP`, `OTHER`, and `AFFIRMATION` / `BACK_VALUE` for special rules.

This example should be treated as a provisional contract rather than a complete normative API specification. Field optionality, validation, enum enforcement, error behavior, and whether `metaData` is formally a JSON string remain unspecified.

## Rules validation flow

The proposed validation flow is:

1. A type-specific rule calls a domain service.
2. The domain service generates JSON from SCBML.
3. The generated JSON is passed to `ratanone-rule-service`.
4. `ratanone-rule-service` returns a filtered result or a success response.

For special rules, the flow performs additional processing, places the result into JSON, and passes that JSON together with the relevant rule information to `ratanone-rule-service`.

The design assigns SCBML transformation to the domain service and rule evaluation or filtering to `ratanone-rule-service`; it does not establish that SCBML or `Netting Service` performs rule evaluation.

## Proposed database changes

### `ratan_special_rule_config_v2`

| column | type | comment |
| --- | --- | --- |
| id | int8 | |
| business_flow | text | `"STRATEGIC_SETTLEMENT"` |
| rule_type | text | `"NSTP"` |
| exception_code | text | |
| exception_category | text | |
| processor | text | |
| active | text | removed |
| is_used | bool | true: rule is save_confirmed/delete_pending, false: rule is neither save_confirmed nor delete_pending |
| is_mapped_rule | bool | true: mapped rule no matter status; false: no rule |
| rule_content | text | `fmEntity__fmAccount__fmType matches "(?i)CORP"` |
| fact_processor | text | removed |
| created_at | timestamp | |
| updated_at | timestamp | |
| created_by | text | |
| updated_by | text | |
| version | int4 | |

The design removes `fact_processor` and adds `rule_content`. Each special-rule configuration predefines its rule expression. The source retains `processor` but does not explain its distinction from `rule_content`. The proposed `is_used` and `is_mapped_rule` fields have different meanings: usage is status-based, whereas mapping indicates whether a mapped rule exists regardless of status.

### `ratan_suppression_fields_xpath_v2`

| column | type | comment |
| --- | --- | --- |
| id | varchar(255) | |
| indexed_term | varchar(500) | fields name: `Cashflow.Is_STP` |
| data_type | varchar(50) | Boolean, String, Date, Numeric |
| field_xpath | text | |
| active | bool | default: true |
| created_at | timestamp | |
| updated_at | timestamp | |
| ratan_label | varchar(25) | default: live |

The design adds `data_type` so extracted field values can be parsed as `Boolean`, `String`, `Date`, or `Numeric`, including conversion of `true` and `false` to Boolean values rather than untyped strings.

### `ratan_rule_mapping`

| column | type | comment |
| --- | --- | --- |
| id | text | |
| rule_id | text | id from `ratanone_rule_service.ratan_rule_engine` |
| is_special | bool | 6 special rules will be true, others false, default false |
| reference_rule_id | text | previous rule id when rule update |
| exception_code | text | |
| exception_category | text | |
| operation_level | text | |
| created_at | timestamp | |
| updated_at | timestamp | |
| version | int4 | |

The design adds `is_special`. Six rules generated by `ratan_special_rule_config` are expected to have `is_special = true`; other rules default to `false`. The source does not name the six rules or define migration, uniqueness, or reconciliation behavior.

## Open implementation questions

The source does not define API endpoints, authentication, authorization, rule-expression grammar, error and timeout handling, transaction boundaries, idempotency, concurrency controls, migration and rollback procedures, mapping-table authority, or audit and retention requirements. It also leaves unresolved the relationship between rule-engine statuses such as `ADD_PENDING` and the `is_used` / `is_mapped_rule` flags.
