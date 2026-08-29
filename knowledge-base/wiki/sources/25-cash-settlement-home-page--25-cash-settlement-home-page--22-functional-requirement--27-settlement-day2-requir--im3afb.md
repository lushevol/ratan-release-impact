---
type: source
title: Cashflow Auto Netting — Auto Netting Technical Design
authors: []
year: 2025
url: "https://confluence.global.standardchartered.com/display/DSP/Cashflow+Auto+Netting"
venue: "Confluence — Derivative Strategy Projects"
tags: [cash-settlement, cashflow-auto-netting, technical-design, rat​​an, netting]
related: [cashflow-auto-netting, auto-netting-rule-management, auto-netting-rule-check, auto-netting-persistence-model, netting-rule-change-cashflow-refresh, ratan, cash-settlement-home-page, control-m]
created: 2026-08-22
updated: 2026-08-22
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Technical Design.md"]
---
# Cashflow Auto Netting — Auto Netting Technical Design

## Summary

This technical-design document describes the implementation of [[concepts/cashflow-auto-netting]] in RATAN and the netting service. It covers workflow integration, Rule Engine interaction, the auto-netting job and rule-check APIs, proposed persistence tables, and performance observations for rule-change refresh and auto-netting execution.

The document refers to a more detailed business requirement in Confluence but does not fully define business eligibility rules, netting semantics, operational controls, or lifecycle transitions. It should therefore be treated as an implementation design and performance record rather than an approved business requirement or production runbook.

## Workflow and service interactions

The design identifies three service activities:

1. Auto Net Rule Check in the netting service.
2. Cashflow Auto Net Job in the netting service, triggered by [[entities/control-m]].
3. Cashflow refresh following a rule change.

The rule-check result is returned to Camunda through `CamundaApiResponse`. A matched rule is represented by `SUCCESS` and `HIT_AUTO_NETTING`; a non-match is represented by `FILTERED` and `NOT_HIT_AUTO_NETTING`.

## Rule-management request

The Rule Engine request stores auto-netting configuration in the JSON-encoded `metaData` field. It also stores a stable `ruleUuid`; the design states that the user-facing `rule_id` can change when a rule is updated.

```json
create auto netting rule request:
{
    "id": "7336280228010184705",
    "businessFlow": "STRATEGIC_SETTLEMENT",
    "ruleType": "AUTO_NETTING",
    "userRule": "BCS_Trade_Id == \"s33\"",
    "runningRule": "",
    "status": "PROCESSING",
    "reason": "test",
    "metaData": "{\"ruleUuid\":\"5330079720543199232\",\"autoNettingConfig\":{\"nettingDate\":\"VD-1\",\"nettingTime\":\"09:00\",\"stpLevel\":\"FULL_STP\",\"nettingType\":\"Bilateral Netting\",\"ruleActiveTime\":\"2025-05-26 11:12:00\"}}",
    "needDryRun": false,
    "version": 0,
    "createdAt": "2025-06-05T06:38:27.853065197Z",
    "updatedAt": "2025-06-05T06:38:27.853073295Z",
    "createdBy": "1622463",
    "updatedBy": "1622463"
}

metaData structure in above request:
{
	"ruleUuid": "5330079720543199232",
	"autoNettingConfig": {
		"nettingDate": "VD-1",
		"nettingTime": "09:00",
		"stpLevel": "FULL_STP",
		"nettingType": "Bilateral Netting",
		"ruleActiveTime": "2025-05-26 11:12:00"
	}
}
```

The configuration includes a business-calendar-relative netting date such as `VD-1`, a netting time, an STP level, a netting type, and a rule activation timestamp. The source does not establish canonical enum casing or serialization.

## REST APIs

### Scheduled auto-netting job

```text
method: get

url: /v1/cashflows/autoNetting/job
```

The documented response is:

```json
{
    "success": true
    "message": ""
}
```

The source copy omitted a comma between the `success` and `message` properties. The endpoint is documented as being triggered by a Control-M job, although the design does not specify scheduling, authentication, idempotency, concurrency protection, retry behavior, or whether `GET` is the approved method for a mutating operation.

### Auto-netting rule-check API

```text
method: get

url: /v1/cashflows/autoNetting/check
```

The source provides these two response cases:

```json
// Case 1: matched auto netting rule
{
    "camundaResponseCode": "SUCCESS”,
    "metadata": {
        "autoNettingRuleCheckResultCode": "HIT_AUTO_NETTING"
    }
}

// Case 2: no matched auto netting rule
{
    "camundaResponseCode": "FILTERED”,
    "metadata": {
        "autoNettingRuleCheckResultCode": "NOT_HIT_AUTO_NETTING"
    }
}
```

The copied examples contain mismatched quotation marks around the `camundaResponseCode` values and are not valid JSON as written. The source does not define downstream Camunda actions, error responses, authentication, or retry semantics.

## Proposed persistence tables

### `ratan_auto_netting_cashflow`

| # | column | type | comments |
| --- | --- | --- | --- |
| 1 | id | Bigserial | PK |
| 2 | cashflow_id | TEXT | |
| 3 | bussiness_version | TEXT | |
| 4 | minor_version | TEXT | |
| 5 | payment_date | DATE | |
| 6 | currency | TEXT | |
| 7 | rule_id | TEXT | |
| 8 | rule_uuid | TEXT | the reason to add this field is rule id will be changed when the rule updated by user. |
| 9 | stp_level | TEXT | for netting resultant cashflow 1. MakerChecker 2. CheckerOnly 3. FullStp |
| 10 | net_type | TEXT | 1. BilateralNetting 2. SwapAgentNetting 3. CcilNetting 4. BicNetting 5. ... |
| 11 | net_trigger_time | TIMESTAMP | |
| 12 | net_status | TEXT | 1. Waiting 2. Pending 3. Done 4. Disabled 5. Failed |
| 13 | net_group_key | TEXT | format: seperate by comon samples for cci netting as below: 400452428,2024-06-04,USD |
| 14 | failed_reason | TEXT | |
| 15 | version | INT | for optimistic locking |
| 16 | created_at | TIMESTAMP | |
| 17 | updated_at | TIMESTAMP | |

### `ratan_auto_netting_config`

| # | column | type | comments |
| --- | --- | --- | --- |
| 1 | id | Bigserial | PK |
| 2 | net_type | TEXT | 1. BilateralNetting 2. SwapAgentNetting 3. CcilNetting 4. BicNetting |
| 3 | net_group_key_config | TEXT | format: json group key including fields to grouped, samples as below: [ { "field": "entityFmid", "xpath": "" }, { "field": "valueDate", "xpath": "" }, { "field": "settlementCurrency", "xpath": "" } ] |
| 4 | resultant_mapping_config | TEXT | format: json samples as below, for ccil netting, couterparty of resultant cashflow will be filled to fixed value: { "counterpartyFmId": "400021949", "counterpartyFmCode": "CLEARING CORP*MMB", "settlementMethod": "Cash" } |
| 5 | description | TEXT | |
| 6 | created_at | TIMESTAMP | |
| 7 | updated_at | TIMESTAMP | |

The document includes an `Index` heading but does not provide index definitions, uniqueness constraints, foreign keys, check constraints, or DDL. The `bussiness_version` spelling is preserved from the source and requires implementation confirmation.

## Performance observations

### Refresh cashflows after a rule change

| version | environment | service instances number | cashflows number | table row count | total time spent |
| --- | --- | --- | --- | --- | --- |
| old version | uat2 | 3 | 150,000 | | 5min |
| frmp1 | 3 | 53,000 | 12,562,217 | 65s-83s |
| staging | 6 | 25,612 | 39,500,554 | time out |
| new version | frmp1 | 3 | 54,382 | 12,803,124 | 14s-21s |
| staging | 4 | 25,617 | 39,516,462 | 50s-65s |
| production | 4 | 57,940 | 51,423754 | 30s-55s |

The first performance table is malformed relative to its header: some rows labelled `frmp1` and `staging` under `old version` appear to omit the version value and shift the remaining fields. The production row count `51,423754` is also ambiguously formatted. The results provide directional evidence of a faster refresh implementation but omit run dates, infrastructure, database load, concurrency, and percentile distributions.

### Auto-netting execution

| env | service instances number | optimization | volume | group count | call lifecycle for query details time | call lifecycle for update status time | total time | comment |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| fmrp1 | 3 | | 5k | 1 | 1min | 1min10s | 2min16s | ratanTraceId: 2752775a3c56b4e69698a50789f79c62 |
| fmrp1 | 3 | | 5k | 1 | 6s | 44s | 57s | ratanTraceId: 875b3c640d45d26898e9f48366ed6476 (before lifecycle optimiation) |
| fmrp1 | 3 | | 5k | 1 | 8s | 38s | 56s | ratanTraceId: 9cb28b7d9aa6622c3897d95a321318f5 |
| fmrp2 | 3 | | 5k | 1 | 10s | 25s | 43s | ratanTraceId: 41f979e27af48daff895a99e75393adc |
| fmrp2 | 3 | | 10k | 1 | 18s | 54s | 81s | ratanTraceId: d63933182697241766e3e7febfa97360 |
| staging | 6 | before | 5k | 1 | 24s | 1min | 1min52s | ratanTraceId: e58c8844c2a1416ab0232c6107325119 |
| staging | 6 | before | 10k | 1 | 25s | 2min43s | 3min30s | ratanTraceId: 6f05020c77c32fc5c22f54123d8c018f |
| staging | 6 | before | 10k | 2 | 47s | 2min22s | 3min35s | ratanTraceId: 90997fd1a41721f425f8d3db9b45c5f0 |
| staging | 6 | after | 5k | 1 | 26s | 56s | 1min46s | ratanTraceId: 91e513017e4e9b1dbe8ac06922a97e35 |
| staging | 6 | after | 10k | 1 | 41s | 1min31s | 3min | ratanTraceId: 5fe6b5254eee0023cae425fedfec2e18 |
| staging | 6 | after | 10k | 2 | 42s | 1min4s | 2min9s | ratanTraceId: 96183c80f34debfa639ab44c4e1ae5ce |

The measurements indicate that lifecycle-detail queries and especially lifecycle-status updates account for most reported auto-netting runtime. Staging “after” results improve total time in the listed comparisons, but the optimization is unnamed and the query-details phase is not consistently faster.

## Test coverage

| test case | description | expected |
| --- | --- | --- |
| case01 | single cashflow reinstate | also processing auto rule check and manual rule check |

Only one incomplete test case is included. The design does not show coverage for scheduling, grouping, concurrent execution, failure and retry, disabled rules, rule modification, or resultant cashflow creation.

## Related wiki context

This source elaborates on [[concepts/cashflow-auto-netting]], [[concepts/auto-netting-rule-management]], [[concepts/netting-rule-change-cashflow-refresh]], and [[concepts/business-calendar-relative-netting-time]]. It also relates to what is the canonical pending auto netting state model, what are the canonical auto netting stp level enums, [[concepts/ccil-settlement-method-stamping]], [[concepts/netting-resultant-cashflow-lifecycle]], and [[concepts/net-resultant-cashflow]].

It appears to be a technical companion to sources/26-auto-netting-page-md-files--122-cash-settlement-home-page-cash-settlement-home-page-functional-requirement-ne--mc8aul, not a replacement for that functional-requirement source.