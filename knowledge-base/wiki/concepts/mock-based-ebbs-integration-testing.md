---
type: concept
title: Mock-Based EBBS Integration Testing
created: 2026-08-24
updated: 2026-08-24
tags: [mock-testing, ebbs, solace, integration-testing, accounting]
related: [solace-based-ebbs-acknowledgement-integration, ebbs, solace, accounting-service, accounting-file-delivery-acknowledgement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]
---
# Mock-Based EBBS Integration Testing

## Definition

Mock-based EBBS integration testing uses a directly constructed EBBS JSON payload instead of exercising the complete Ratan payment and accounting-feed generation workflow.

## Application in the Technical-Live Plan

Option 2 proposes that Ratan publish a mocked feed directly to a Solace topic. The payload uses `CFID: 00` and `Trade id: 00`, and includes both a new posting and a reversal posting. EBBS is expected to return an ACK, which Ratan consumes.

## Coverage and Limitations

This approach can validate connectivity and a basic acknowledgement path. It does not establish that:

- Ratan's Accounting Service generates a production-compatible feed from a payment
- The mocked payload matches the production schema, headers, or topic contract
- An EBBS ACK updates the originating cashflow
- The new and reversal postings have the required accounting semantics

The relationship between the mock reversal and [[concepts/accounting-feed-withdrawal-as-reversal]] is not defined by the source.