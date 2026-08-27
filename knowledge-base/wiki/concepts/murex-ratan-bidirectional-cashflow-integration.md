---
type: concept
title: Murex-RATAN Bidirectional Cashflow Integration
created: 2026-08-24
updated: 2026-08-24
tags: [murex-211, ratan, cashflow, messaging, integration]
related: [cn-settlement-murex-211-integration, ratan, control-m, murex-ratan-cashflow-reconciliation, trade-event-triggered-cashflow-stp]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Surrounding System Integration/Settlement - Murex 2.11 Cashflow Integration/CN Settlement - Murex 2.11 Delivery Plan.md"]
---
# Murex-RATAN Bidirectional Cashflow Integration

The delivery plan describes an intended bidirectional integration between [[murex-211]] and [[ratan]].

## Planned outbound path

Murex cashflows were planned to be automatically published to RATAN through Control-m scheduling, new payment queues, processing scripts, stored-procedure capture into a staging table, MSRB, MQ connectivity, workflow distribution, and cashflow tag enrichment.

The workflow was also planned to synchronize flow status in the staging table when messages were distributed to RATAN.

## Planned inbound path

Murex was planned to consume RATAN ACK messages and Release messages. Testing scope included reverse ACK, reverse Release, and end-to-end SIT.

The plan does not specify message schemas, identifiers, ordering, retries, reversal semantics, error handling, or Murex cashflow-state transitions. These remain open in [[what-are-the-murex-ratan-ack-and-release-message-contracts]].

## Scope boundary

This is a planned Murex/RATAN integration stream. It is related to [[trade-event-triggered-cashflow-stp]], but this source does not establish that the two flows use the same entry point, implementation, or lifecycle contract.