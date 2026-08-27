---
type: query
title: What Is the Authoritative Camunda mutiException syncSummary API Contract?
tags: [camunda, api-contract, nstp, cashflow, exception-handling]
related: [confirmation-driven-nstp-exception-auto-closure, ratan-cash-settlement-orchestration, camunda-api-response, trade-cashflow-exception-version-correlation]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/NSTP Maker-Checker Separation From Code/NSTP exception auto close design-Confirmation status handling.md"]
---
# What Is the Authoritative Camunda mutiException syncSummary API Contract?

## Question

Is `/v1/camunda/task/mutiException/syncSummary` the authoritative endpoint path and what are its required request, version, authorization, atomicity, and error-handling semantics?

## Evidence

The source specifies:

```text
POST /v1/camunda/task/mutiException/syncSummary
```

It documents a success response with status `200` and a missing-fixing-task response with status `404`, error code `RATAN-201050003`.

The path is explicitly written as `mutiException`. It must not be silently changed to `multiException` until the deployed API contract confirms the intended spelling.

## Open Contract Points

- Confirm the endpoint path and host naming.
- Specify required versus optional request fields.
- Define the relationship between `cashflowVersion`, `businessVersion`, and `minorVersion`.
- Define `action`, `isNstp`, and multi-exception atomicity semantics.
- Define authorization and maker-checker behavior for payloads with `roleType: "Maker"`.
- Classify `RATAN-201050003` and define expected consumer behavior.