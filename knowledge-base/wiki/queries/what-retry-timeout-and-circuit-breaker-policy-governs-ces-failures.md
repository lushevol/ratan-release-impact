---
type: query
title: What Retry, Timeout, and Circuit-Breaker Policy Governs CES Failures?
created: 2026-08-24
updated: 2026-08-24
tags: [ces, resilience, retry, timeout, circuit-breaker, authorization]
related: [ces, auth-service, query-service, cash-settlement-data-entitlement, adopt-two-layer-ces-emergency-disablement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Data entitlement solution/FM CES Integration Technical Design.md"]
---
# What Retry, Timeout, and Circuit-Breaker Policy Governs CES Failures?

The design requires user queries to fail when valid CES entitlement data cannot be obtained. It specifies retries for CES 500 errors, connection failures, and CES 4xx errors, but gives no retry count, backoff, timeout, rate limit, or retry eligibility classification. It also explicitly excludes circuit breakers.

A 404 response for an un-onboarded user is separately treated as a terminal query failure, creating ambiguity with the instruction to retry CES 4xx errors.

## Questions

- Which CES response codes and transport failures are retryable?
- What are the timeout, retry-count, backoff, jitter, and total request-budget limits?
- How should permanent client errors, including missing-user 404 responses, be reported and monitored?
- Does the emergency disablement mechanism replace a circuit breaker, or is a bounded circuit-breaker policy still required?
- What CES SLO, rate-limit, health-check, and escalation contract governs this dependency?