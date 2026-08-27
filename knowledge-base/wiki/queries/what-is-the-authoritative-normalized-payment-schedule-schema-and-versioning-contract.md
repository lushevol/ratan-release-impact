---
type: query
title: What Is the Authoritative NormalizedPaymentSchedule Schema and Versioning Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, payment-schedule, schema, versioning, integration]
related: [normalized-payment-schedule, tdsx-uber-message-listener, group-management-service, product-agnostic-cashflow-aggregation]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Product Agnostic Aggregation Design.md"]
---
# What Is the Authoritative NormalizedPaymentSchedule Schema and Versioning Contract?

The draft requires `NormalizedPaymentSchedule` to survive UBER message fan-out but supplies no formal schema or compatibility contract.

## Questions to Resolve

- Which system produces the schedule and owns its semantic definition?
- What are the exact field names, types, leg identifiers, and required fields?
- Is the full schedule copied onto every split cashflow message, referenced externally, or propagated selectively?
- Which UBER client-library versions support the element?
- How are absent, malformed, amended, cancelled, or stale schedules handled?
- How does a schedule version correlate with cashflow and trade versions?

Until answered, `NormalizedPaymentSchedule` should be treated as a proposed input to aggregation rather than an established authoritative record.