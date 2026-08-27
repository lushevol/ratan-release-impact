---
type: concept
title: DVP Received UI Indicator
created: 2026-08-23
updated: 2026-08-23
tags: [ui, cashflow-detail, dvp, observability]
related: [auto-dvp, ratan, dvp-nstp-exception-handling]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# DVP Received UI Indicator

The DVP Received UI indicator is an operational marker added to the pay cashflow in RATAN Cashflow Detail after successful Auto DVP receipt confirmation.

The required display text is `DVP Received`, presented like an exception-code comment with a green background. The source does not define persistence, timestamp, actor, audit attributes, duplicate-event rendering, or removal behavior. Those details should be specified before implementation.