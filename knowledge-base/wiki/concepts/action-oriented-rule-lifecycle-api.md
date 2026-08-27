---
type: concept
title: "Action-Oriented Rule Lifecycle API"
created: 2026-08-24
updated: 2026-08-24
tags: [rule-engine, rest-api, lifecycle, maker-checker, governance]
related: [ratan-rule-engine, ratan-rule-service-ratan-rule, adhoc-suppression-maker-checker-workflow, rule-governance-and-auditability, what-is-the-canonical-rule-maintenance-maker-checker-state-machine, what-are-the-canonical-rule-api-action-endpoint-paths-and-ruleid-location]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]
---
# Action-Oriented Rule Lifecycle API

An action-oriented rule lifecycle API represents business commands through explicit operations such as create, update, confirm, reject, enable, disable, and activate. It avoids allowing clients to set arbitrary lifecycle statuses through generic CRUD or a `targetStatus` parameter.

For maker/checker governance, separate `confirm` and `reject` actions make reviewer intent explicit and provide clear points for authorization, validation, comments, audit recording, and idempotency controls.

## Proposed RATAN pattern

An archived proposal for [[ratan-rule-engine]] uses the following action set:

```text
POST /v2/rules/create
PUT /v2/rules/update
PUT /v2/rules/confirm
PUT /v2/rules/reject
PUT /v2/rules/enable
PUT /v2/rules/disable
PUT /v2/rules/activate
```

The proposal intends these commands to replace direct calls such as:

```text
PUT /v2/rules/{ruleId}/status/{targetStatus}
```

## Governance implications

Action endpoints do not by themselves define a safe governed lifecycle. A complete design still needs:

- an allowed state-transition matrix;
- maker/checker authorization and segregation-of-duties rules;
- expected behavior for duplicate or conflicting commands;
- versioning and optimistic-concurrency requirements;
- audit identity, timestamps, reason/comment retention, and retention policy;
- production controls for any exceptional delete operation.

The archived proposal provides a candidate command vocabulary but does not provide these controls or confirm their deployment. The authoritative API shape and lifecycle remain open in [[what-is-the-authoritative-ratan-rule-service-v2-api-and-json-schema]] and [[what-is-the-canonical-rule-maintenance-maker-checker-state-machine]].