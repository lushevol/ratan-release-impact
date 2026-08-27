---
type: query
title: What Is the Authoritative RATAN-FXU MX-FXCASH 40630 Interface Contract?
tags: [ratan, fxu, mx-fxcash, interface-contract, open-question]
related: [5-ratan--17-ratan-interfaces--28-ratan-and-fxumx-fxcash-40630--hwa4i8, fxu, mx-fxcash, ratan-fxu-utilization-integration, ratan-interface-architecture, ratanone-message-bridge, what-is-the-relationship-between-ratan-and-ratanone]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and FXU(MX-FXCASH) 40630.md"]
---

# What Is the Authoritative RATAN-FXU MX-FXCASH 40630 Interface Contract?

## Question

What are the authoritative technical and operational details for interface `40630` between `FXU`/`MX-FXCASH` and `RATAN`?

## Known Evidence

The source confirms that:

- `FXU` queries cashflow status through a RATAN API.
- `FXU` sends a `FullUtilize` accounting request through `Solace`.
- The utilization flow includes `RATANONE`.
- The message format is `JSON`.
- The product scope is `SPOT`, `Forward`, and `SWAP`.

## Information Required

The linked FXU technical design should be used to establish:

1. The API endpoint, HTTP method, authentication, request and response schemas, status values, and error contract.
2. Whether the cashflow-status API and the utilization message flow are one interface or separate interaction patterns under `40630`.
3. Whether `FullUtilize` is a message type, business event, API operation, or field value.
4. The actual Solace topic and queue names, subscriptions, consumer ownership, and response correlation mechanism.
5. Whether `RATANONE` performs business processing, message bridging, or both.
6. Acknowledgement, retry, timeout, duplicate, ordering, replay, and dead-letter behavior.
7. Whether `SPOT`, `Forward`, and `SWAP` share the same contract.
8. Support ownership, escalation contacts, and applicable OLA commitments.
9. Whether the source status should be changed to `Published` following the recorded review.

## Current Assessment

The source is sufficient for a high-level integration summary but not for implementation, operational validation, or formal contract approval.