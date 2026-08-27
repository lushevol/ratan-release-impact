---
type: query
title: What Is the Authoritative RATAN Apollo Rule Engine Interface Contract?
tags: [ratan, apollo, interface-contract, trade-validation, open-question]
related: [apollo-rule-engine, ratan, ratan-rule-service, post-trade-detective-controls, trade-validation, nstp-exception-operation-levels, what-is-the-canonical-nstp-exception-platform-and-publication-contract, what-is-the-authoritative-nstp-rule-and-exception-state-machine]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/RATAN and Apollo 51527.md"]
---
type: query
title: What Is the Authoritative RATAN Apollo Rule Engine Interface Contract?
tags: [ratan, apollo, interface-contract, trade-validation, open-question]
related: [apollo-rule-engine, ratan, ratan-rule-service, post-trade-detective-controls, trade-validation, nstp-exception-operation-levels, what-is-the-canonical-nstp-exception-platform-and-publication-contract, what-is-the-authoritative-nstp-rule-and-exception-state-machine]
created: 2026-08-24
updated: 2026-08-24
sources: ["RATAN/RATAN -Interfaces/RATAN and Apollo 51527.md"]
---
# What Is the Authoritative RATAN Apollo Rule Engine Interface Contract?

## Question

What are the authoritative technical, operational, and ownership details for the RATAN integration with Apollo Rule Engine, Application ID `51527`?

## Evidence Currently Available

The source documents only this high-level flow:

```text
RATAN --(API)--> Apollo Rule Engine
```

RATAN is said to submit trades for business-rule validation, extract Apollo’s rule response, and save it in an exception data store. The stated purposes are post-trade detective controls and regulatory compliance.

## Information Required

Resolve the following:

- Whether Apollo Rule Engine is distinct from [[entities/ratan-rule-service]]
- The API endpoint, operations, environments, and network path
- Authentication and authorization requirements
- Request and response schemas
- Rule identifiers, rule versions, and audit behavior
- Response and error-code semantics
- Timeout, retry, idempotency, duplicate-submission, and partial-response handling
- The identity, schema, ownership, and retention policy of the exception data store
- Whether Apollo responses enter the canonical NSTP exception publication path
- Interface support ownership, contact details, OLA, known issues, and troubleshooting procedures
- Review and publication status of the interface document

## Related Questions

The answer may affect:

- [[queries/what-is-the-canonical-nstp-exception-platform-and-publication-contract]]
- [[queries/what-is-the-authoritative-nstp-rule-and-exception-state-machine]]
- [[concepts/nstp-exception-operation-levels]]
- [[entities/ratan-rule-service]]

## Provisional Assessment

The source establishes an intended or documented relationship, but not an authoritative operational contract. Apollo-specific claims should remain separate from existing RATAN rule-service claims until identity, API, and exception-lifecycle evidence is obtained.