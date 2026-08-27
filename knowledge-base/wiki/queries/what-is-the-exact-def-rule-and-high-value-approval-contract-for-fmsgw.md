---
type: query
title: What Is the Exact DEF Rule and High-Value Approval Contract for FMSGW?
created: 2026-08-23
updated: 2026-08-23
tags: [fmsgw, def-rule, high-value-payment, approval, open-question]
related: [def-rule, high-value-payment-queue, fmsgw, scb-nigeria-lag-gbs, 25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requir--51mg19]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/009 NIGERIA SCB NIGERIA LAG(GBS).md"]
---

# What Is the Exact DEF Rule and High-Value Approval Contract for FMSGW?

Nigeria UAT evidence shows that a `DEF` rule can place high-value `MT103` and `MT202` payments into the [[high-value-payment-queue]] for approval before AMH routing. It does not define the rule.

## Questions to Resolve

- What does `DEF` stand for, and what data determines a match?
- Which value thresholds, currencies, entities, and message types are in scope?
- Who can approve, reject, or release a queued payment?
- At which point are ACK and notification generated?
- What are the retry, timeout, audit, and idempotency requirements?