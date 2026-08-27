---
type: query
title: What Is the Complete X-Outbound-Property Header Contract?
tags: [open-question, message-header, swift, mt, mx, orchestration]
related: [outbound-property-propagation-to-swift-mt-mx, high-value-payment-control-technical-architecture, swift]
created: 2026-08-23
updated: 2026-08-23
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/High Value Payment Control - RATAN/HVP Tech Design.md"]
---
# What Is the Complete X-Outbound-Property Header Contract?

The design names `X-Outbound-Property-` as an outbound header but provides no suffix or value definition.

## Information needed

Determine the authoritative:

- complete header name and whether it is mandatory;
- payload schema, source fields, permitted values, and versioning;
- publishing routes that must carry the header;
- MT target field or block and MX target element;
- validation, retry, idempotency, and failure-handling rules.

No source in this ingest resolves these questions.