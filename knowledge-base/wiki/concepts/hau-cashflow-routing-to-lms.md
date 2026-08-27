---
type: concept
title: HAU Cashflow Routing to LMS
created: 2026-08-23
updated: 2026-08-23
tags: [HAU, LMS, cashflow, settlement, HKCS]
related: [hau, lms, hkcs, manual-entity-lms-reference-data-feed]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/HKCS initiative.md"]
---
# HAU Cashflow Routing to LMS

## Requirement

The HKCS open-question record states that LMS confirmed on 2026-07-29 that HAU cashflows must be sent to LMS.

## Missing Contract Details

The source does not specify the message format, destination, delivery timing, acknowledgement model, reconciliation controls, retry behavior, or test evidence. The stated confirmation should therefore be treated as a requirement-level dependency rather than proof of implementation.

## Relationship to Existing LMS Coverage

This requirement concerns HAU cashflows and may extend the scope of [[concepts/manual-entity-lms-reference-data-feed]]. It should not be treated as identical to a reference-data feed without an explicit LMS contract.