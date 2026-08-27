---
type: query
title: How Is MT210 Handled Between RATAN and ENISIS?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, enisis, mt210, swift, mx-conversion, open-question]
related: [ratan-enisis-swift-interface, ratan, enisis, swift]
sources: ["RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
---
# How Is MT210 Handled Between RATAN and ENISIS?

The source states that RATAN converts generated SWIFT MT messages to MX except MT210, then transmits converted MX messages and MT210 to ENISIS through FM Solace.

## Questions to resolve

- Does MT210 always remain in MT format?
- Does MT210 use the documented MT-Swift topic and JSON payload format?
- Does ENISIS return MT ACK/NACK for MT210?
- Are replay, reconciliation, and manual-recovery procedures the same as for converted MX messages?
- Why is MT210 excluded from conversion, and are there other conversion exceptions?

## Evidence

[[ratan-enisis-swift-interface]] establishes the exception but does not define MT210 routing, payload, acknowledgement, or recovery behavior separately.