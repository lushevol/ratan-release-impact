---
type: entity
title: CPN Service
created: 2026-08-23
updated: 2026-08-23
tags: [cpn, service, cash-settlement, netting]
related: [cpn, cpn-netting, cpn-netting-reversal-cashflow, payment-lake, netting-resultant-cashflow]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Netting/CPN Tech Design - Draft for now.md"]
---
# CPN Service

CPN Service is the application component described as executing CPN netting operations and maintaining the related cashflow records.

## Documented behavior

CPN Service:

- Updates netting components in Payment Lake.
- Creates netting resultant cashflows.
- Supports manual un-netting after maker/checker review.
- Automatically un-nets a previous netting group when an amended or cancelled component version is received.
- Marks pre-release resultants as `Dead` or `DEAD` after un-netting.
- Creates reversal cashflows for released resultants.
- Links a reversal to its original resultant through `Reversal ID`.

The design does not provide an API, message schema, retry policy, or idempotency contract. Its exact separation from the broader CPN process remains unspecified.