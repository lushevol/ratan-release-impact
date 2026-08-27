---
type: concept
title: High-Value Payment Approval Queue
created: 2026-08-23
updated: 2026-08-23
tags: [high-value-payment, approval, queue, def-rule, fmsgw, settlement]
related: [fmsgw, amh, zambia-scb-zambia-lus-gbs, manual-entity-settlement-enablement]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/005 ZAMBIA SCB ZAMBIA LUS(GBS).md"]
---
# High-Value Payment Approval Queue

The High value payment Queue holds MT103 and MT202 settlement messages that match a DEF rule for high-value payments before their release to [[amh]].

The Zambia UAT records a passing workflow in which an eligible transaction enters the queue, is approved, is sent to AMH, produces an ACK to RATAN, and triggers a notification. The evidence identifier recorded for this scenario is `M00127115344`.

The source does not specify the DEF threshold, approval roles, maker-checker separation, rejection path, rework behavior, or notification recipients.