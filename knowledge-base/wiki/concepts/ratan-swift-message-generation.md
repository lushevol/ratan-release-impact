---
type: concept
title: RATAN SWIFT Message Generation
created: 2026-08-23
updated: 2026-08-23
tags: [ratan, swift, fmrp, payment-messaging, settlement]
related: [swift-status-lifecycle-and-reconciliation, ssi-driven-swift-field-generation, ratan-razor-swift-generation-scope, fmrp-to-ratan-migration-scope, settlement-first-migration]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/FMRP Swift Generation.md"]
---
# RATAN SWIFT Message Generation

RATAN SWIFT message generation is the FMRP requirement for [[ratan]] to compose payment messages using cashflow data and SSI data, then dispatch them through [[fmswiftgateway]], [[fmsre]], or [[enisis]].

## Functional scope

The requirement assigns RATAN MT generation to China, Malaysia, India, and partial Singapore. It assigns RATAN MX generation to Singapore only. It excludes Malaysia from ISO MX processing.

Supported MT variants include MT103, MT202, MT202 Flip, MT202 CrossDebit, MT103/202 COV, MT192, MT292, MT210, MT604, MT605, and MT692.

## Processing boundary

RATAN is intended to generate messages and expose message and status data by cashflow ID. Downstream gateways are responsible for message receipt, manual release queues, and onward communication with payment systems.

[[razor]] remains the legacy message-generation source for LOANIQ, Egypt, Nepal, and Saudi Arabia. This coexistence is documented in [[ratan-razor-swift-generation-scope]].

## Dependency and constraint

Message formation depends on upstream cashflow and strategy data from [[murex]], together with SSI and static data. The specification includes detailed formatting logic but contains inconsistent pseudocode and later amendments. It should be converted into versioned, testable rules before being treated as an executable contract.