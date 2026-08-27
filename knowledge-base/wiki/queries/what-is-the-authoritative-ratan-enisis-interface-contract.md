---
type: query
title: What Is the Authoritative RATAN-ENISIS Interface Contract?
created: 2026-08-24
updated: 2026-08-24
tags: [ratan, enisis, interface-contract, swift, solace, open-question]
related: [ratan-enisis-swift-interface, ratan-interface-inventory, ratan-interface-architecture, enisis, fm-solace]
sources: ["RATAN/RATAN -Interfaces/Ratan and ENISIS 50157.md"]
---
# What Is the Authoritative RATAN-ENISIS Interface Contract?

The available Korea interface source identifies four PROD channels, their topics, acknowledgement queues, and capacity settings. It is incomplete as an executable or operationally complete interface contract.

## Questions to resolve

- What are the missing PROD host/IP addresses and connection endpoints?
- Are queue-less outbound publication rows intentional, and which subscriptions consume those topics?
- What are the MX and MT payload schemas, validation rules, and versioning arrangements?
- What are the ACK/NACK payload definitions and correlation identifiers?
- How are delayed, lost, duplicated, or rejected acknowledgements handled?
- What retry, timeout, replay, and idempotency rules apply?
- Is `51358-RATAN`, `51358-RATANONE`, and `ratanone` a single canonical service identity?
- Are the volume, spool, bind-count, and message-size values measured production data, planning assumptions, or SLA commitments?

## Known evidence

[[ratan-enisis-swift-interface]] documents the topics and acknowledgement queues but leaves all host/IP fields blank. It also contains no populated Interface Specification section or payload examples.

The source status is blank despite recorded review information, so publication status should be confirmed before this document is treated as authoritative.