---
type: concept
title: Fail-Open Rule-Service Evaluation
tags: [resilience, rule-service, failure-handling, cash-settlement, operational-risk]
related: [ratan-rule-service, ratan-suspended-cashflow-rule-filtering, how-are-fail-open-suspended-cashflows-reconciled, retry-exhaustion-compensation, dead-letter-queue-recovery]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/SUSPENDED RULE FILTER in Ratan Tech Design.md"]
---
# Fail-Open Rule-Service Evaluation

Fail-open rule-service evaluation means a cashflow continues normal processing if suspension-rule evaluation cannot establish a match.

The documented outcomes are:

- Timeout or unavailable rule service: log a warning and return `false`.
- Empty `matchedRules`: treat as not suspended.
- Unexpected rule-service error: log an error and return `false`.

This preserves throughput when `ratan-rule-service` is unavailable, but it may allow cashflows that would otherwise have been filtered to reach downstream processing and STP publication. The design does not define alerting thresholds, bypass recording, or a reconciliation and re-evaluation process.