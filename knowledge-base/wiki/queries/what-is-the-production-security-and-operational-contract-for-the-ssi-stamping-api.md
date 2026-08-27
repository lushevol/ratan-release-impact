---
type: query
title: What Is the Production Security and Operational Contract for the SSI Stamping API?
created: 2026-08-23
updated: 2026-08-23
tags: [query, api, security, operations, ssi-stamping, ratan]
related: [ssi-stamping-service, scbml-trade-enrichment-api, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/SSI Stamping Notification/FMRP - SSI Stamping Flow/SSI Stamping Tech Design-Egypt.md"]
---
# What Is the Production Security and Operational Contract for the SSI Stamping API?

The source documents only a UAT endpoint and Basic authentication. It does not define the production endpoint or the operational contract needed for a production integration.

## Questions to resolve

- What is the production endpoint and service-discovery mechanism?
- Is Basic authentication retained, or is mTLS, OAuth, or another mechanism required?
- Where are credentials stored, rotated, revoked, and audited?
- What TLS requirements apply?
- What are the timeout, retry, backoff, and circuit-breaker rules?
- Is `trackingId` an idempotency or correlation key?
- How are duplicate requests handled?
- Does HTTP `400` return an enriched SCBML payload for business-match exceptions?
- Which responses are retryable?
- What logging, metrics, tracing, alerting, and audit requirements apply?
- How are sensitive settlement details and Base64 SCBML protected in logs?

The source includes a directly usable-looking credential in the Authorization example. It should be treated as exposed, rotated or revoked if still valid, and replaced with a secret reference in all maintained documentation.