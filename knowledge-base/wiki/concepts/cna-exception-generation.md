---
type: concept
title: CnA Exception Generation
created: 2026-08-25
updated: 2026-08-25
tags: [cna, exceptions, ratan, pnl, settlement-control]
related: [ratan, ratan-markets-udp-pv-integration, marketudp]
sources: ["RATAN/RATAN -Interfaces/Ratan and Markets UDP（SSDR）.md"]
---
# CnA Exception Generation

## Definition

CnA exception generation is the downstream RATAN process that produces exceptions for users to review in the exception blotter after RATAN processes PV data received from Markets UDP.

## Role in the Integration

RATAN retrieves PV data after receiving a readiness notification from OVV through Solace. It uses the data for P&L and PV-impact calculations, then generates CnA exceptions.

The source does not define the exception criteria, severity model, deduplication behavior, user workflow, or handling of calculation failures.
