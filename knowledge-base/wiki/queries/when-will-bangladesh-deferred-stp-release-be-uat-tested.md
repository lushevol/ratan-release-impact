---
type: query
title: When Will Bangladesh Deferred STP Release Be UAT Tested?
created: 2026-08-23
updated: 2026-08-23
tags: [bangladesh, fmsgw, deferred-message, stp, scheduler, uat]
related: [25-cash-settlement-home-page--25-cash-settlement-home-page--22-functional-requirement--27-settlement-day2-requi--12zi34h, scb-dhaka-dac-in-country, early-release, high-value-payment-approval-queue]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Enable Settlement for Manual Entities/03 UAT testing/015 BANGLADESH SCB DHAKA DAC(In Country).md"]
---
# When Will Bangladesh Deferred STP Release Be UAT Tested?

The Bangladesh deferred-message scenario was de-scoped because UAT dates were back-valued and May test data had been manually processed. Consequently, the source provides no execution evidence for scheduler-driven release from the Deferred Message Queue.

## Required UAT Coverage

A future test should demonstrate:

1. An STP MT103, MT202, or MT202COV waits in the Deferred Message Queue until its configured release time.
2. The scheduler releases the message automatically.
3. A message above the high-value setup reaches the High Value Approval Queue.
4. An approved message reaches AMH.
5. Relevant acknowledgement, audit, and failure-handling events are recorded.

Until this evidence exists, [[early-release]] and deferred-message functionality remain unvalidated for [[scb-dhaka-dac-in-country]].