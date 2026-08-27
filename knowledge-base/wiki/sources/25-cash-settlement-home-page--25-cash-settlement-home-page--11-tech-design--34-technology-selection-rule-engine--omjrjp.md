---
type: source
title: "Rule Engine Status Machine Refactor Plan"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-engine, api-design, maker-checker, archived]
related: [ratan-rule-engine, ratan-rule-service-ratan-rule, action-oriented-rule-lifecycle-api, what-is-the-authoritative-ratan-rule-service-v2-api-and-json-schema, what-are-the-canonical-rule-api-action-endpoint-paths-and-ruleid-location, what-are-the-canonical-executionflag-and-needdryrun-api-values, what-is-the-canonical-rule-maintenance-maker-checker-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]
authors: []
year: 0
url: ""
venue: "Archived technical design"
---
# Rule Engine Status Machine Refactor Plan

This archived technical-design proposal describes a planned refactor of the [[ratan-rule-engine]] rule-management API. It proposes replacing generic CRUD operations and direct status mutation with explicit lifecycle actions: create, update, confirm, reject, enable, disable, and activate.

The document is design intent only. It does not establish approval, implementation, deployment, current consumer adoption, or a production API contract.

## Proposed API direction

The proposal retains rule filtering and history search, adding `ruleId` as a query parameter:

```text
businessFlow=CONFIRMATION,SETTLEMENT
&ruleType=NSTP
&status=LIVE,ADD_PENDING
&ruleId=12315456
```

It proposes the following action endpoints:

```text
POST /v2/rules/create
PUT /v2/rules/confirm
PUT /v2/rules/reject
PUT /v2/rules/update
PUT /v2/rules/enable
PUT /v2/rules/disable
PUT /v2/rules/activate
```

The business delete workflow is removed in the proposal. `DELETE /v2/rules/{ruleId}` is retained only as an internal testing endpoint.

## Proposed create request

```json
POST /v2/rules/create
{
  "businessFlow": "SETTLEMENT",
  "ruleType": "NSTP",
  "rule": ".....",
  "reason": "Suppress by CHENGDU & counterpart",
  "metaData": "",
  "comment": "system initial",
  "executionFlag": "EXECUTION",
  "needDryRun": false
}
```

The document marks `businessFlow`, `ruleType`, and `rule` as mandatory. It states that `executionFlag` is optional and defaults to `EXECUTION`; `needDryRun` is optional and defaults to `false`.

## Proposed action payloads

```json
PUT /v2/rules/confirm
{
  "ruleId": "12313",
  "comment": "456"
}
```

```json
PUT /v2/rules/reject
{
  "ruleId": "12313",
  "comment": "456"
}
```

```json
PUT /v2/rules/update
{
  "ruleId": "12313",
  "rule": "Cashflow__Status_Event_Type == \"bbb\"",
  "reason": "test",
  "comment": "maker update",
  "metaData": "",
  "executionFlag": "ExecutionFlag.EXECUTION",
  "needDryRun": false
}
```

```json
PUT /v2/rules/enable
{
  "ruleId": "12313",
  "comment": "456"
}
```

```json
PUT /v2/rules/disable
{
  "ruleId": "12313",
  "comment": "456"
}
```

```json
PUT /v2/rules/activate
{
  "ruleId": "12313",
  "comment": "456"
}
```

## Proposed maker/checker migration

The proposal maps direct status changes to explicit commands:

```text
PUT /api/ratan/v2/rules/${ruleId}/status/DISCARDED
→ PUT /api/ratan/v2/rules/${ruleId}/reject

PUT /api/ratan/v2/rules/${ruleId}/status/SAVE_CONFIRMED
→ PUT /api/ratan/v2/rules/${ruleId}/confirm

PUT /api/ratan/v1/special/rules/${ruleId}/disable
→ PUT /api/ratan/v2/rules/${ruleId}/disable

PUT /api/ratan/v1/special/rules/${ruleId}/enable
→ PUT /api/ratan/v2/rules/${ruleId}/enable
```

This is a candidate API-level mechanism for [[adhoc-suppression-maker-checker-workflow]], not evidence of an implemented state machine.

## Contract uncertainties

The source contains incompatible endpoint forms. Its detailed payload examples place `ruleId` in the request body, while migration mappings place it in the URL path. It also refers generally to `/v2/rules/{action}`.

`executionFlag` is represented as `EXECUTION`, `NOT_EXECUTION`, `NOT_EXECUTED`, and `ExecutionFlag.EXECUTION`. Dry-run control is named both `needDryRunFlag` and `needDryRun`. The source does not resolve canonical serialization, state transitions, authorization, idempotency, versioning, or the relationship between create and activate.

These ambiguities are tracked in [[what-is-the-authoritative-ratan-rule-service-v2-api-and-json-schema]], [[what-are-the-canonical-rule-api-action-endpoint-paths-and-ruleid-location]], and [[what-are-the-canonical-executionflag-and-needdryrun-api-values]].