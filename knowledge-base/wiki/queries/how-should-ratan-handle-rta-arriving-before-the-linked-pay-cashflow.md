---
type: query
title: How Should RATAN Handle RTA Arriving Before the Linked Pay Cashflow?
created: 2026-08-23
updated: 2026-08-23
tags: [rta, replay, correlation, cashflow, dvp]
related: [ratan, auto-dvp, ebbs-rta-notification, receive-to-pay-cashflow-linkage]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# How Should RATAN Handle RTA Arriving Before the Linked Pay Cashflow?

One scenario expects a pay cashflow that arrives after a valid receive RTA to have no DVP exception. However, the stated flow attempts pay lookup when the RTA is processed and does not define pending-event persistence, replay, expiry, or reconciliation.

Decide whether RATAN requires a durable unmatched-RTA correlation store and replay trigger, or whether the scenario expectation should be removed.