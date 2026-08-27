---
type: concept
title: Solace-Based EBBS Acknowledgement Integration
created: 2026-08-24
updated: 2026-08-24
tags: [solace, ebbs, acknowledgement, integration, ratanone, accounting]
related: [solace, ebbs, accounting-file-delivery-acknowledgement, accounting-service, message-bridge, technical-live-versus-business-live]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design/Tech Live of Ratan - Accounting Service with EBBS.md"]
---
# Solace-Based EBBS Acknowledgement Integration

## Definition

Solace-based EBBS acknowledgement integration is the message flow in which Ratan publishes an accounting feed or mocked EBBS payload to a Solace topic, EBBS processes the message, and an acknowledgement is returned for consumption by Ratan.

## Validation Patterns

The source describes two validation patterns:

1. **End-to-end accounting validation:** Ratan processes a payment, generates and publishes the accounting feed, receives the EBBS ACK, and applies an accounting update to the originating cashflow.
2. **Mock-based messaging validation:** Ratan publishes a dummy EBBS JSON feed directly to Solace, EBBS returns an ACK, and Ratan consumes that ACK.

The second pattern validates a narrower integration path and should not be treated as proof of Accounting Service feed generation.

## Missing Operational Contract

The source does not define the production message schema, topic, headers, correlation identifiers, ACK or NACK format, retry and timeout behavior, duplicate-delivery handling, or the mapping from an ACK to a cashflow accounting update. These details are open in [[queries/what-is-the-authoritative-ebbs-solace-feed-and-acknowledgement-contract]].

This concept extends [[concepts/accounting-file-delivery-acknowledgement]] with a specific EBBS/Solace technical-live scenario, without establishing implementation-level protocol behavior.