---
type: concept
title: RATAN-ENISIS SWIFT Interface
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, enisis, swift, interface, mx, mt, korea]
related: [ratan, enisis, murex-kr, fm-solace, swift, korea-fmo-payment-recovery, ratan-interface-architecture, ratan-interface-inventory, what-is-the-authoritative-ratan-enisis-interface-contract, how-is-mt210-handled-between-ratan-and-enisis]
sources: ["RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
---
# RATAN-ENISIS SWIFT Interface

The RATAN-ENISIS SWIFT Interface is the documented Korea PROD message path from [[murex-kr]] through [[ratan]] and [[fm-solace]] to [[enisis]], which subsequently forwards messages to [[swift]].

## Message processing

1. Murex KR generates MxML and transmits it through MQ to RATAN.
2. RATAN generates SWIFT MT.
3. RATAN converts MT to ISO 20022 MX, except MT210.
4. RATAN sends converted MX and MT210 to ENISIS through FM Solace.
5. ENISIS processes and forwards the messages to the SWIFT network.

This describes a Korea-specific interface and should not be assumed to represent all RATAN or Murex flows.

## Four-channel contract

The interface contains two outbound message channels and two inbound response channels:

- MX-Swift: RATAN to ENISIS, SCBML.
- MX-ACK/NACK: ENISIS to RATAN, SCBML.
- MT-Swift: RATAN to ENISIS, JSON.
- MT-ACK/NACK: ENISIS to RATAN, JSON.

All channels are designated PROD. The acknowledgement channels have explicitly named RATAN receiver queues; outbound publication rows provide topics but no receiver queues.

## MT210 exception

MT210 is explicitly excluded from the MT-to-MX conversion step. The source states that converted MX messages and MT210 are transmitted to ENISIS, but does not specify whether MT210 always remains MT, whether its acknowledgement route differs, or how it is reconciled. This uncertainty is tracked in [[how-is-mt210-handled-between-ratan-and-enisis]].

## Operational recovery

[[korea-fmo-payment-recovery]] describes the operational process for input failures, RATAN conversion exceptions, and missing ENISIS acknowledgements. Recovery progresses from investigation and replay to manual drafting in ENISIS or OSCAR when technical recovery cannot resolve the payment.

## Contract gaps

The available source lacks host/IP addresses, payload schemas, field-level validation, ACK/NACK definitions, correlation rules, timeout policy, retry policy, and replay semantics. These omissions prevent treating it as a complete interface specification; they are tracked in [[what-is-the-authoritative-ratan-enisis-interface-contract]].