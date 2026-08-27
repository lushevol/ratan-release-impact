---
type: query
title: Can RATAN Consume the India CorporateFinancial RTA Topic Without Queue Impact?
created: 2026-08-23
updated: 2026-08-23
tags: [india, ebbs, rta, performance, subscription]
related: [ratan, ebbs, auto-dvp, auto-dvp-pilot-scope, razor]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Auto DVP (eBBS).md"]
---
# Can RATAN Consume the India CorporateFinancial RTA Topic Without Queue Impact?

The India CorporateFinancial topic has high volume and may affect consumption for other queues. Razor reportedly excludes `v1/14147-ebbs-/casa/scbml-1.0/in/pub/corp-fin/all`, where DVP is triggered by MT910.

Confirm the RATAN subscription and filtering design, expected throughput, queue-isolation controls, and any alternative notification source required to preserve DVP coverage.