---
type: query
title: What Are the Murex-RATAN ACK and Release Message Contracts?
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, ack, release, messaging, integration]
related: [murex-ratan-bidirectional-cashflow-integration, cn-settlement-murex-211-integration, ratan-cashflow-lifecycle-service]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Delivery Plan.md"]
---
# What Are the Murex-RATAN ACK and Release Message Contracts?

## Question

What are the schemas, correlations, lifecycle effects, retry rules, and reversal behaviors for ACK and Release messages sent from RATAN to Murex?

## Evidence

The plan schedules Murex consumption of RATAN ACK messages in Q1 2023 Sprint 1 and RATAN Release messages in Sprint 2. It also plans reverse ACK and reverse Release functional tests and end-to-end SIT.

## Unknowns

The plan does not define:

- message fields or transport format;
- cashflow and trade correlation identifiers;
- expected state transitions;
- ordering and idempotency rules;
- retry and failure handling; or
- the semantic meaning of reverse ACK and reverse Release.

## Needed evidence

Retrieve the functional design, message schemas, MQ contracts, test packs, and the Jira records for `RATAN-10822`, `RATAN-11254`, `RATAN-11281`, and `RATAN-11569`.