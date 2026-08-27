---
type: query
title: What Is the Authoritative RATAN FMRP STELLA 29126 Interface Contract?
tags: [ratan, fmrp-stella, interface-contract, open-question]
related: [ratan-fmrp-stella-interface, fmrp-stella, sabre-booking-api, scbml-kafka-stella-event-flow, trade-lock-status-for-mo-validation]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# What Is the Authoritative RATAN FMRP STELLA 29126 Interface Contract?

## Question

Which document defines the authoritative ownership, runtime direction, API methods, schemas, versions, security, timeout, retry, error, and ACK/NACK-correlation behavior for interface 29126?

## Evidence

The source labels FMRP STELLA as the API provider and RATAN as the consumer, but its narrative describes RATAN publishing events and writing status to Stella. It also documents incomplete endpoint and operational details.

The referenced materials include the FMRP STELLA Booking API, MO Validation design, Trade and Lifecycle Events workflows, and Ratan-to-FMRP Stella API integration documentation.

## Resolution criteria

Resolve this query when the authoritative documentation identifies:

- API ownership separately from runtime producer and consumer direction.
- HTTP methods and payload schemas.
- The meaning of `{type}/{operation}/{action}`.
- Validation, rejection, affirmation, and `E0` event contracts.
- SCBML schema and Kafka delivery semantics.
- ACK/NACK transport and correlation.
- Canonical production URLs.
- Authentication, timeout, retry, and failure policies.
