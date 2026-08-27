---
type: query
title: "What Are the Canonical Rule API Action Endpoint Paths and ruleId Location?"
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, rule-engine, api-contract, rest-api, ruleid]
related: [ratan-rule-engine, ratan-rule-service-ratan-rule, action-oriented-rule-lifecycle-api, what-is-the-authoritative-ratan-rule-service-v2-api-and-json-schema]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]/[Rule Engine] Status Machine Refactor Plan.md"]
---
# What Are the Canonical Rule API Action Endpoint Paths and ruleId Location?

The archived status-machine refactor proposal contains incompatible endpoint forms for rule actions.

## Candidate forms in the proposal

Detailed request examples use action paths and include `ruleId` in the body:

```text
PUT /v2/rules/confirm
PUT /v2/rules/reject
PUT /v2/rules/update
PUT /v2/rules/enable
PUT /v2/rules/disable
PUT /v2/rules/activate
```

Migration mappings use `ruleId` in the path:

```text
PUT /api/ratan/v2/rules/${ruleId}/confirm
PUT /api/ratan/v2/rules/${ruleId}/reject
PUT /api/ratan/v2/rules/${ruleId}/enable
PUT /api/ratan/v2/rules/${ruleId}/disable
```

The narrative also refers generally to:

```text
/v2/rules/{action}
```

## Evidence needed

Locate the approved OpenAPI specification, deployed API-gateway routes, controller implementation, and consumer integration contract. Confirm the canonical paths, HTTP methods, request schemas, and whether `ruleId` belongs in the path, request body, or both.

Until corroborated, the archived proposal must not be treated as the current API contract. See [[what-is-the-authoritative-ratan-rule-service-v2-api-and-json-schema]].