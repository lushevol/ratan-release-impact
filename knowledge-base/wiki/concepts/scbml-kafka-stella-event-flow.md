---
type: concept
title: SCBML over Kafka STELLA Event Flow
tags: [scbml, kafka, stella, ratan, asynchronous-integration, acknowledgements]
related: [ratan-fmrp-stella-interface, fmrp-stella, sabre-booking-api, post-trade-orchestration]
created: 2026-08-25
updated: 2026-08-25
sources: ["RATAN/RATAN -Interfaces/Ratan and SABRE (FMRP STELLA)-29126.md"]
---
# SCBML over Kafka STELLA Event Flow

## Flow

The documented event path is:

```text
RATAN
  -> SCBML message
  -> dedicated Kafka topic
  -> STELLA
  -> Stella trade booking engine
  -> ACK or NACK
```

RATAN uses this path for confirmation events and settlement workflow events. The source describes the stream as continuous and real-time.

## Processing behavior

STELLA reads the SCBML message from Kafka and pushes it into the trade booking engine. The booking engine responds with an ACK or NACK based on whether processing succeeds.

## Missing contract details

The source does not define:

- The SCBML schema.
- The Kafka topic name.
- Message keys, partitioning, ordering, or retention.
- Delivery and retry guarantees.
- Idempotency behavior.
- ACK/NACK transport and correlation.
- Error payloads or recovery procedures.

“Real-time” is therefore a stated operating mode rather than a documented service-level objective.
