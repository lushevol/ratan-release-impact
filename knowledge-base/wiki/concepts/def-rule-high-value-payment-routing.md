---
type: concept
title: DEF Rule High-Value Payment Routing
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, high-value-payment, validation, routing]
related: [high-value-payment-queue, high-value-payment-approval-queue, fmsgw, amh, ratan, sri-lanka-scb-colombo-cmb, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12tf8z2]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/010 SRI LANKA SCB COLOMBO CMB(In Country).md"]
---
# DEF Rule High-Value Payment Routing

A DEF rule is described in the Sri Lanka SCB Colombo UAT record as a condition that causes an inbound high-value MT103 or MT202 payment to enter the [[high-value-payment-queue]].

In the recorded passing path, the payment is sent to [[amh]] only after approval. FMSGW then sends an acknowledgement back to [[ratan]] and sends a notification.

The source does not define the rule criteria, approval roles, maker-checker controls, rejection outcome, timeout behavior, or notification-delivery handling. It demonstrates a passing approval path only.