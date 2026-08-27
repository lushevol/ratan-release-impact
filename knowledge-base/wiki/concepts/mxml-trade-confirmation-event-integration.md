---
type: concept
title: MXML Trade Confirmation Event Integration
created: 2026-08-24
updated: 2026-08-24
tags: [mxml, comp, ibm-mq, murex, ratan, event-integration, tactical-architecture]
related: [murex-korea, ratan, trade-confirmation-driven-payment-stp, fxu-message-driven-integration, what-are-the-mxml-comp-event-contract-and-processing-semantics-for-ratan, what-is-the-approved-murex-korea-to-ratan-comp-integration-and-retirement-plan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/Korea Murex Trade COMP High Level Solution.md"]
---
# MXML Trade Confirmation Event Integration

MXML trade confirmation event integration is the proposed tactical path in which [[murex-korea]] publishes trade MXML directly to [[ratan]] through a new IBM MQ integration and RATAN is customized to handle `COMP` events.

## Status

Detailed design is in progress. The source calls this the current possible solution, not an approved or operational architecture.

## Intended outcome

The feed is intended to provide the trade confirmation required for [[trade-confirmation-driven-payment-stp]] while avoiding a Murex Korea–Murex GDC integration. The document expects this simplification to reduce development and testing complexity, but supplies no implementation or test evidence for that expectation.

## Tactical lifecycle

The proposed RATAN customization is explicitly temporary. Its removal must be funded and tracked, with an accountable owner and a concrete migration trigger for retirement. The document anticipates eventual replacement by a Murex Korea to TDS3 flow but does not define whether or when that strategic flow will be delivered.

## Required definition

Before implementation, the integration requires an authoritative contract for MXML payloads, trade identity, `COMP` semantics, delivery guarantees, idempotency, ordering, replay, failure recovery, reconciliation, and observability. These unresolved matters are tracked in [[what-are-the-mxml-comp-event-contract-and-processing-semantics-for-ratan]].