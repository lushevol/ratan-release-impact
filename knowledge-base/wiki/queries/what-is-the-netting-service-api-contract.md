---
type: query
title: What Is the Netting Service API Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [cash-settlement, netting, API, open-question]
related: [netting-service, cashflow-netting, netting-eligibility, maker-checker-netting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Netting Service Design.md"]
---

# What Is the Netting Service API Contract?

The source requires interfaces for netting, netting validation, and unnetting, and represents splitting with the `SPLIT` action. However, the API table contains no URLs, parameters, responses, or notes.

The missing contract should define:

- Operation endpoints and methods.
- Request and response schemas.
- Validation and eligibility errors.
- Maker/checker approval actions.
- Idempotency keys and duplicate-request behavior.
- Authorization and audit fields.
- Partial-success and retry semantics.
- Transaction boundaries for component and resultant updates.
- Status-write-back behavior for STELLA and Murex2.11.
- Event publication and message correlation.

Until these details are documented, the Netting Service design should be treated as a business and persistence outline rather than an implementation-ready API specification.