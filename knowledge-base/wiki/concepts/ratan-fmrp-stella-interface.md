---
type: concept
title: RATAN-FMRP STELLA Interface
tags: [ratan, fmrp-stella, sabre, settlement, trade-control, interface-29126]
related: [ratan, fmrp-stella, sabre, sabre-booking-api, settlement-accounting, trade-validation, post-trade-orchestration, scbml-kafka-stella-event-flow, trade-lock-status-for-mo-validation]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# RATAN-FMRP STELLA Interface

## Overview

Interface 29126 connects RATAN with FMRP STELLA/SABRE across settlement processing and trade-control workflows. It combines asynchronous event delivery with API-based operations.

## Settlement processing

RATAN:

1. Retrieves spot rates from the Stella API.
2. Checks fixed and floating legs for netting in the BCS flow.
3. Writes calculated cashflow status and updated trade status back to Stella.
4. Publishes confirmation and settlement workflow events through the `sabre-booking-api` integration.

The source describes these interactions as real-time but gives no measurable latency or throughput objective.

## Trade control

The trade-control scope includes:

- Trade validation status.
- Trade rejection.
- Trade affirmation.
- Trade-lock status retrieval through `StellaBookingRestApi`.
- Economic Affirmation (`E0`) events published directly to Stella through an API.

Trade-lock information includes the lock owner and lock duration or expiry time. This allows Middle Office users to assess whether manual intervention is permissible.

## Integration modes

- **Asynchronous event flow:** RATAN posts SCBML to a dedicated Kafka topic, and the Stella booking engine processes the message and returns ACK or NACK.
- **API request/response flow:** RATAN uses Stella APIs for status updates, validation-related operations, affirmation, and lock-status retrieval.

The source does not clarify how ACK/NACK responses are transported or correlated.

## Ownership and direction

The source table labels FMRP STELLA as API provider and RATAN as consumer. The narrative, however, describes RATAN publishing events and writing status back to Stella. The table may represent API ownership rather than runtime message direction. These two dimensions must be distinguished in any authoritative contract.
