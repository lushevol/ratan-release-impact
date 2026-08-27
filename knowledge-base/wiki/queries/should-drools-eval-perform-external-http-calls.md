---
type: query
title: Should Drools eval Perform External HTTP Calls?
created: 2026-08-24
updated: 2026-08-24
tags: [drools, eval, http, resilience, rule-engine]
related: [drools-eval-conditional-element, drools, dynamic-drl-compilation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived", "Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Technology Selection - Rule Engine/RATAN Rule Engine - [Archived]/Drools Features Explore.md"]/Drools Features Explore.md"]/Drools Features Explore.md"]
---
# Should Drools eval Perform External HTTP Calls?

The archived source shows a `RestTemplate` request inside a DRL `eval` function and converts all exceptions to `false`. This is feasibility evidence only and does not define an approved integration pattern.

## Questions to resolve

- Are external HTTP calls permitted during rule-condition evaluation?
- If permitted, what timeout, retry, circuit-breaker, authentication, tracing, and metrics requirements apply?
- Can a condition be evaluated more than once, and what idempotency or caching controls are required?
- Does a remote failure produce `false`, an explicit rule-processing error, a retry, or another outcome?
- Should remote data be retrieved before deterministic rule evaluation instead?