---
type: query
title: What Is the Authoritative Adhoc SSI API Contract?
tags: [ssi, api-contract, adhoc-ssi, camunda, integration-risk]
related: [ssi-stamping-service, ssi-stamping-message-contract, adhoc-ssi-exception-lifecycle]
created: 2026-08-24
updated: 2026-08-24
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Cash Settlement System Design/SSI Stamping Service Design/SSI Stamping Design.md"]
---
# What Is the Authoritative Adhoc SSI API Contract?

The historical design contains material contradictions that prevent its API inventory from being treated as a deployable contract.

## Questions to resolve

- Which service host and port applies to each operation? The interface inventory includes `60001` for some Adhoc endpoints, while concrete Maker and Checker-rejection examples use `50001`.
- What are the complete Checker-approval request and response semantics?
- Is `FILTERED` an expected successful business outcome, a workflow-routing outcome, or an integration failure?
- Which response metadata names are canonical: `businessVersion`/`minorVersion` or `cashflowBusinessVersion`/`cashflowMinorVersion`?
- Is `requestBody` a string, object, or nullable field for each operation?
- Which headers, authentication, authorization, idempotency, timeout, retry, and error contracts apply?
- Is `READY` the canonical eligibility status, and how does it relate to the `QUEUED` status in the supplied SCBML example?

## Required evidence

Obtain the current OpenAPI or equivalent interface specification, deployed route configuration, Camunda integration definition, and approval-path test evidence. Confirm whether historical localhost examples remain representative.