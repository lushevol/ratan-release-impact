---
type: query
title: What Is the Authoritative Behavior When SCI LEI Data Is Missing or Invalid?
created: 2026-08-23
updated: 2026-08-23
tags: [SCI, LEI, exception-handling, data-quality, SWIFT]
related: [sci, sci-lei-regulatory-data-lookup, india-payment-lei-swift-enrichment, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Capture LEI.md"]
---
# What Is the Authoritative Behavior When SCI LEI Data Is Missing or Invalid?

The requirement mandates both booking-entity and counterparty LEIs for qualifying payments, but it does not define the outcome when SCI cannot provide valid data.

## Cases Requiring a Decision

Clarification is needed for:

- Missing booking-entity or counterparty SCI FMID.
- No record matching `regulatoryTypeValue = 'MIFID'` and `regulatoryFields = 'LEI'`.
- Multiple matching regulatory records.
- Malformed or incorrectly sized LEI values.
- Expired or stale LEI data.
- SCI timeout or unavailability.
- A runtime SCI value that differs from the stated SCB LEI `RILFO74KP1CM8P6PCT96`.

The decision should specify whether SWIFT generation is blocked, proceeds without one or both LEIs, retries, or creates an operational exception. Audit and user-notification requirements should also be defined.