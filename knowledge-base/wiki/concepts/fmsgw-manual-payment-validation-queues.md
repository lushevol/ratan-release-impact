---
type: concept
title: FMSGW Manual Payment Validation Queues
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, validation-queue, manual-processing, payment-controls, uat]
related: [fmsgw, qatar-scb-doha, ratan-fmsgw-amh-settlement-message-routing, message-holding-and-release, what-are-the-authorization-and-terminal-outcome-rules-for-fmsgw-manual-queues]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/002 QATAR SCB DOHA DOH(GBS).md"]
---
# FMSGW Manual Payment Validation Queues

In the Qatar SCB Doha UAT scope, [[fmsgw]] routes exceptional settlement messages to named operational queues for review or approval. The source validates basic placement and forward-processing actions, not the full control model.

## Tested queues

- **Back Valued Messages Queue:** Back-value-dated transactions are listed with validation-failure details. The source also records ACK and notification behavior.
- **High Value Payment Queue:** MT103 and MT202 payments matching the DEF rule are held pending approval. Following approval, FMSGW sends the message to AMH, returns an ACK, and issues a notification.
- **Manual Cancellation Queue:** Cancelled-trade transactions and MTn92 messages enter this queue. A user can search entries, inspect Data and Action audit tabs, add a comment, process to eligible-currency validation, or terminate a transaction.
- **Duplicate Message Queue:** Duplicate MT103, MT202, and MT202COV messages enter this queue. The Process action advances the transaction to SCB-specific validations.

## Auditability and controls

The source demonstrates UI-level Data and Action audit tabs and user comments for MTn92 queue processing. It does not specify entitlements, maker-checker separation, approval rejection, terminal states, audit retention, or effects of termination. Queue behavior should not be assumed to share the implementation of [[message-holding-and-release]] without further technical evidence.