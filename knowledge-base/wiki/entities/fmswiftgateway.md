---
type: entity
title: FMSwiftGateway
created: 2026-08-23
updated: 2026-08-23
tags: [swift, payment-gateway, fmrp, integration]
related: [ratan-swift-message-generation, swift-status-lifecycle-and-reconciliation, fmsre, amh, scpay]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# FMSwiftGateway

FMSwiftGateway, also called FMSGW, is the intended gateway for RATAN-generated SWIFT MT payment messages in the FMRP requirement.

## Intended role

[[ratan]] sends generated messages to FMSwiftGateway. The gateway is expected to communicate with [[amh]] and [[scpay]], then return technical and business ACK/NACK events to RATAN.

A technical ACK/NACK is expected within five minutes. The requirement does not establish timeout detection, retries, replay, or escalation ownership.

## Status interface

FMSwiftGateway technical ACK maps to `Pending FMSGW Disp`; validation success maps to `Pending Manual Rel`; downstream AMH ACK maps to `Released by AMH`. FMSGW validation errors and manual deletion outcomes have distinct UI statuses.

Manual deletion can map the cashflow to `SETTLED` even though manual payment through Oscar or AMH remains expected. See [[swift-status-lifecycle-and-reconciliation]].