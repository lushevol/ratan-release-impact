---
type: source
title: "RATAN Rule Service Tech Design (Archived)"
created: 2026-08-24
updated: 2026-08-24
tags: [archived, ratan, drools, rule-engine, suppression, maker-checker, api-design]
related: [drools, dynamic-drl-compilation, drools-rule-refresh, drools-rule-language, ratan-rule, ratan-drools-rule, ratan-drools-fact-processor, how-are-top-level-and-conditions-preserved-in-generated-drl, what-is-the-authoritative-ratan-rule-service-api-and-schema-contract, were-suppression-migration-open-cases-resolved, what-replaced-the-archived-ratan-rule-engine-design]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]/Rule Service Tech Design.md"]
authors: [Lin Liang]
year: 2024
url: ""
venue: "RATAN-15255 technical design"
---
# RATAN Rule Service Tech Design (Archived)

> [!warning]
> This is archived design evidence, not a current implementation contract. It describes a proposed Drools-based RATAN Rule Service and does not establish that the design was deployed or remains authoritative. See [[what-replaced-the-archived-ratan-rule-engine-design]].

The design proposes a database-driven rule service behind the API gateway. It separates rule maintenance APIs from rule-execution APIs, stores editable business rules separately from executable DRL, and uses Drools compilation and refresh after rule changes.

## Proposed architecture

- `ratan_rule` stores business-manageable rules and lifecycle data.
- Changes to `ratan_rule` generate DRL persisted in `ratan_drools_rule`.
- Rule execution prepares SCBML-derived logical-model facts, enriches them through `fieldsXpath`, and can add facts from custom fact processors.
- The service loads DRL by business flow and rule type, inserts facts into Drools working memory, and allows eligible rules to activate on the agenda and fire.
- The proposed v2 validation API accepts structured `logicFacts` and `additionalFacts`; SCBML adapters were intended to retain compatibility for `cashflow` and `trade`.

## DRL generation example

Source rule:

```text
Data_Flow.Data_Target_System == ORCID
```

Generated DRL:

```java
import com.scb.ratan.rule.drools.api.Fact;
import java.util.*;

dialect "mvel"

rule "1709829242988974080"
  when
    Fact(name == 'scbml', $m : value)
    Map(Data_Flow!.Data_Target_System[0] matches "(?i)^ORCID$") from $m
  then
    // empty action
end
```

The design uses `dialect "mvel"` and specifies `this['key']` Map access, quoted string literals, `!.` null-safe navigation, `matches '(?i)^...$'` for case-insensitive comparison, and `[0]` array navigation. See [[drools-rule-language]].

## Proposed data model

### `ratan_rule`

The source proposes adding `fact_processor` and removing `operation_level`, `exception_code`, and `exception_category`.

| Item. # | Column Name | Data Type | Nullable | Comment |
| --- | --- | --- | --- | --- |
| 1 | id | text | false | primary key |
| 2 | business_flow | varchar | false | the value can be the one of the following: CONFIRMATION, SETTLEMENT or SETTLEMENT_AUTO_NETTING |
| 3 | rule_type | varchar | false | the value can be the one of the following: NSTP, NETTING, IRS, SUPPRESSION, SWIFT_SUPPRESSION or FX |
| 4 | rule | text | true | |
| 5 | status | varchar | false | |
| 6 | reason | text | true | |
| 7 | fact_processor | varchar | true | either column `'rule'` or `'fact_processor'` is not null |
| 8 | version | int4 | false | |
| 9 | created_at | timestamp | false | |
| 10 | updated_at | timestamp | false | |
| 11 | created_by | varchar | false | |
| 12 | updated_by | varchar | false | |

### `ratan_drools_rule`

| Item. # | Column Name | Data Type | Nullable | Comment |
| --- | --- | --- | --- | --- |
| 1 | id | text | false | primary key |
| 2 | business_flow | varchar | false | the value can be the one of the following: CONFIRMATION, SETTLEMENT or SETTLEMENT_AUTO_NETTING |
| 3 | rule_type | varchar | false | the value can be the one of the following: NSTP, NETTING, IRS, SUPPRESSION, SWIFT_SUPPRESSION or FX |
| 4 | fact_processor | varchar | false | a list of data processors that can fetch the data from various data sources. |
| 5 | drl_content | text | false | DRL (Drools Rule File) content that can be converted from human-readable rules in Table `ratan_rule` |
| 6 | version | int4 | false | the version of DRL file, default is 1. The version plus 1 when the rule is updated. |
| 7 | created_at | timestamp | false | creation time, default is the point time of data inserted. |
| 8 | updated_at | timestamp | false | last update time. |

The narrative calls for a composite unique index on `business_workflow` and `rule_type`, but the documented column is `business_flow`. No DDL is supplied, so the intended index cannot be verified.

### `ratan_drools_fact_processor`

| Item. # | Column Name | Data Type | Nullable | Comment |
| --- | --- | --- | --- | --- |
| 1 | id | int | false | primary key |
| 2 | name | varchar | false | the name of fact processor |
| 3 | fact_name | varchar | false | the name of fact produced by the fact processor. |
| 4 | fact_expression | text | false | the expression of fact used in DRL file. Sample: `[ {"expression": "Fact(name == '${fact_name}', $excludedCounterpartyList : value)"}, {"expression": "Map(this['Entity']!.Counterparty_SCI_FMID[0] not memberOf $excludedCounterpartyList) from $m"} ]` |
| 5 | created_at | timestamp | false | creation time, default is the time of data inserted. |
| 6 | updated_at | timestamp | false | in history table, it shall be same as the creation time. |

## Documented API surface

| API group | Signature | Intended function |
| --- | --- | --- |
| Rule maintenance | `POST /v2/rules?executionFlag=NOT_EXECUTED&needDryRunFlag=false` | Create a rule. |
| Rule maintenance | `PUT /v2/rules?executionFlag=NOT_EXECUTED&needDryRunFlag=false` | Update a rule. |
| Rule maintenance | `GET /v2/rules` | List rules. |
| Rule maintenance | `GET /v2/rules/filter` | Filter by business flows, rule types, and statuses. |
| Rule maintenance | `GET /v2/rules/{ruleId}` | Retrieve a rule. |
| Rule maintenance | `DELETE /v2/rules/{ruleId}` | Delete a rule. |
| Rule history | `GET /v2/rules/{ruleId}/history` | Retrieve a rule's history. |
| Rule history | `GET /v2/rules/history` | Search history records. |
| Rule lifecycle | `PUT /v2/rules/{ruleId}/status/{targetStatus}` | Change status; `userAction` is required for `UPDATE_PENDING` to `SAVE_CONFIRMED`. |
| Special-rule control | `PUT /v2/rules/{ruleId}/{enable/disable}` | Enable or disable a `SPECIAL` rule. |
| Dry-run activation | `/v2/rules/activate/{ruleId}` | Activate a dry-run rule; the HTTP method is not stated. |
| Deprecated validation | `POST /v1/rules/validate` | Validate SCBML against a business-flow/rule-type pair. |
| Validation v2 | `POST /v2/rules/validate` | Validate `logicFacts` and `additionalFacts`. |
| SCBML adapter | `/v2/rules/validate/adaptor/{type}` | Adapt SCBML for `cashflow` or `trade`; the HTTP method is not stated. |
| Pair comparison | `POST /v2/rules/validate/multi` | Validate rules against two fact messages. |
| Batch comparison | `/v2/rules/validate/batch` | Validate pairs of fact messages; maximum list size is `400`; the HTTP method is not stated. |

## Governance and migration observations

The proposed API includes history, versioning, comments, user identifiers, reference rule IDs, dry-run handling, and enable/disable control for `SPECIAL` rules. Checker approval or rejection is required when an update moves from `UPDATE_PENDING` to `SAVE_CONFIRMED`.

The specification is not implementation-ready: it contains inconsistent enum values (`NOT_EXECUTED` versus `NOT_EXECUTION`), flag names (`needDryRunFlag` versus `needDryRun`), the status typo `DELETE_PEDING`, incomplete HTTP methods, and example `SETTLEMENT1` values outside the documented business-flow set.

Suppression comparison testing recorded matching outcome codes for selected scenarios but materially different descriptions between the New Rule Service and Suppression Service. Three migration cases remained open: failed `Instr. Modif` cases, an EG `TOBESENT` pre-check failure, and Funded Swap behavior matching an Equity Swap rule. See [[were-suppression-migration-open-cases-resolved]].

A generated response example splits a top-level `&&` expression into separate DRL rules. Whether an omitted aggregation layer restores conjunction semantics is unspecified. See [[how-are-top-level-and-conditions-preserved-in-generated-drl]].