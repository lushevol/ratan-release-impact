---
type: concept
title: RATAN-FMSGW-AMH Settlement Message Routing
created: 2026-08-23
updated: 2026-08-23
tags: [settlement, message-routing, acknowledgement, swift, uat]
related: [ratan, fmsgw, amh, qatar-scb-doha, fmsgw-manual-payment-validation-queues, what-is-the-authoritative-mt103-ack-dependent-mt202cov-release-contract, what-are-the-fmsgw-ack-failure-retry-and-idempotency-rules-for-ratan-settlement-messages]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/002 QATAR SCB DOHA DOH(GBS).md"]
---
# RATAN-FMSGW-AMH Settlement Message Routing

The Qatar SCB Doha UAT records a nominal settlement-message route in which [[ratan]] submits a message to [[fmsgw]], FMSGW forwards it to [[amh]], and FMSGW returns an ACK to RATAN.

## Tested scope

Passed scenarios cover:

- MT103 with MT202COV.
- MT202.
- MT192 and MT292.
- Approved high-value MT103 and MT202.
- Original MT103 or MT202 processing associated with a cancelled trade.

A source note states that MT202COV should be released when the related MT103 has been successfully acknowledged. The source does not define the correlation key, the meaning or producer of the ACK, or the behavior when the MT103 ACK is delayed, unsuccessful, or absent.

## Evidence boundary

This is UAT evidence for [[qatar-scb-doha]], rather than a complete integration contract. It does not establish retry, timeout, negative-ACK, delivery-failure, reconciliation, or idempotency behavior. Those gaps are tracked in [[what-are-the-fmsgw-ack-failure-retry-and-idempotency-rules-for-ratan-settlement-messages]].