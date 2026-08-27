---
type: concept
title: DEF Rule
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, validation, high-value-payment, approval, settlement]
related: [fmsgw, high-value-payment-queue, scb-nigeria-lag-gbs, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--51mg19]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/009 NIGERIA SCB NIGERIA LAG(GBS).md"]
---

# DEF Rule

A DEF rule is an undefined rule condition referenced in Nigeria UAT evidence for [[fmsgw]]. When an `MT103` or `MT202` payment hits this rule and is classified as high value, it is placed in the [[high-value-payment-queue]] for user approval.

After approval, the documented flow sends the message to AMH, returns an ACK to RATAN, and sends a notification.

The source does not define the DEF acronym, its evaluated fields, thresholds, priority, or rejection and timeout behavior.