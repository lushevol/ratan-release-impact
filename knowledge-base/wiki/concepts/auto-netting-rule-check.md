---
type: concept
title: Auto-Netting Rule Check
created: 2026-08-22
updated: 2026-08-22
tags: [cashflow-auto-netting, rule-evaluation, camunda, workflow]
related: [cashflow-auto-netting, auto-netting-rule-management, ratan, netting-resultant-cashflow-lifecycle]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Cashflow Auto Netting/Auto Netting Technical Design.md"]
---
# Auto-Netting Rule Check

## Definition

Auto-Netting Rule Check is the netting service decision interface used to determine whether a cashflow matches an auto-netting rule before downstream workflow processing. The result is returned to Camunda through `CamundaApiResponse`.

## Documented contract

The source defines two outcomes:

- A matched rule returns `camundaResponseCode: SUCCESS` and `autoNettingRuleCheckResultCode: HIT_AUTO_NETTING`.
- No matched rule returns `camundaResponseCode: FILTERED` and `autoNettingRuleCheckResultCode: NOT_HIT_AUTO_NETTING`.

The source examples contain malformed quotation marks and should be normalized before being treated as an executable API contract.

## Boundary of responsibility

The interface establishes a binary eligibility gate. It does not define:

- The rule precedence or matching semantics.
- The Camunda activity after either result.
- Authentication or authorization.
- Error responses, retries, or idempotency.
- Whether the endpoint must remain a `GET` request.

The rule-check interface should therefore be read together with [[concepts/auto-netting-rule-management]] and the canonical-state queries linked from [[concepts/cashflow-auto-netting]].