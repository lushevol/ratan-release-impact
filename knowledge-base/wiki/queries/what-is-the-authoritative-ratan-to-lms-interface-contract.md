---
type: query
title: What Is the Authoritative RATAN-to-LMS Interface Contract?
created: 2026-08-25
updated: 2026-08-25
tags: [ratan, lms, interface-contract, solace, open-question]
related: [ratan-lms-liquidity-cashflow-feed, ratan, lms, fm-bpms-lms, solace, operational-level-agreement, ratan-interface-inventory]
sources: ["RATAN/RATAN -Interfaces/Ratan and LMS 50686.md"]
---
# What Is the Authoritative RATAN-to-LMS Interface Contract?

## Question

What authoritative technical and operational documentation defines the RATAN-to-LMS liquidity-management cashflow feed?

## Known evidence

The source documents the direction:

```text
Ratan --(Solace)--> LMS
```

It links to:

- [LMS Feed - Derivative Strategy Projects - Confluence](https://confluence.global.standardchartered.com/display/DSP/LMS+Feed)
- [BCS - Sophis Decom - Service Specs](https://confluence.global.standardchartered.com/display/FMEDMI/BCS+-+Sophis+Decom+-+Service+Specs)
- [RATAN - OLA - FM Settlement - IS - Confluence](https://confluence.global.standardchartered.com/display/PSS/RATAN+-+OLA)

## Missing contract elements

The source does not identify:

- Solace topic or queue names;
- Message and payload schemas;
- Field definitions and versioning;
- Push versus pull semantics;
- Frequency, latency, or delivery guarantees;
- Authentication and authorization;
- Retry, duplicate, and dead-letter behavior;
- Reconciliation and completeness controls;
- Interface ownership, support contacts, or troubleshooting;
- OLA service levels and incident targets.

## Additional identity questions

The authoritative documentation should also clarify:

1. Whether LMS and SAIL-LMS are the same system or distinct deployments.
2. What FM-BPMS-LMS denotes.
3. Whether the FMRP table should be split into separate feed rows.
4. Which scope values are countries, legal entities, booking centres, or operating units.
5. Why the source status remained blank after the recorded review.

## Why this matters

The existing source is sufficient to record the integration inventory, business purpose, transport, and high-level scope. It is not sufficient to implement, operate, reconcile, or certify the interface.