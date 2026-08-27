---
type: query
title: What Is the Ratan SUSPENDED Rule-Service API Contract?
tags: [open-question, api-contract, ratan-rule-service, cash-settlement]
related: [ratan-rule-service, ratan-suspended-cashflow-rule-filtering, fail-open-rule-service-evaluation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
---
# What Is the Ratan SUSPENDED Rule-Service API Contract?

The source defines only:

```text
POST /v1/ratanSuspendedRule/check
```

The authoritative contract is needed for request fields, response fields, `matchedRules` aggregation, authentication, authorization, timeout, retry, error codes, correlation identifiers, rule version selection, and idempotency expectations.

The contract must state how the caller distinguishes a valid non-match from an empty result, malformed response, unavailable service, or partial rule evaluation.