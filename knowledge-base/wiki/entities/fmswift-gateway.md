---
type: entity
title: FMSWIFT Gateway
created: 2026-08-22
updated: 2026-08-22
tags: [payment-gateway, cash-settlement, reversal, payment-release]
related: [fmsre, pending-reversal-acknowledgement, pending-payment-release, ratan]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/MX2.11 Decomm - Cash Settlement Business Workflow/NSTP Workflow.md"]
---
# FMSWIFT Gateway

FMSWIFT Gateway is the payment gateway referenced by the NSTP workflow as the source of payment status and reversal acknowledgements.

The proposed Pending Reversal Ack control hard-blocks release of a replacement payment until the original reversal is acknowledged by FMSWIFT Gateway. The workflow also considers whether RATAN should trigger release or delete actions in the gateway; if that integration is too complex, users would handle the action directly in [[entities/fmsre]].

The source describes this as a planned workflow dependency, not as evidence of a currently enabled production integration.
