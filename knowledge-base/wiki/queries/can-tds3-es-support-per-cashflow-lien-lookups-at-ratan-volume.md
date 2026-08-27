---
type: query
title: Can TDS3 ES Support Per-Cashflow Lien Lookups at RATAN Volume?
created: 2026-08-23
updated: 2026-08-23
tags: [tds3-es, performance, scalability, lien, ratan]
related: [tds3-es, tds3, ratan, lien-driven-cashflow-nstp, lien-aware-netting-and-auto-unnetting]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/2024 changes/Lien Settlement Process - Cashflow Migration/RATAN Cashflow Process with Lien - Function Specs.md"]
---
# Can TDS3 ES Support Per-Cashflow Lien Lookups at RATAN Volume?

The proposed design makes one TDS3 ES lookup per Murex cashflow. The source projects approximately 50,000 daily cashflows before retries, reprocessing, duplicate parent-trade lookups, or netting-component evaluation.

Capacity and operational controls are not specified. Evidence is needed for:

- TDS3 ES throughput, latency, availability, and rate limits;
- bulk-query, caching, and duplicate-trade deduplication options;
- timeout, retry, throttling, and failure-fallback behavior;
- treatment of cashflows when latest lien state cannot be retrieved; and
- expected incremental traffic from notification-driven reprocessing and netting-resultant cashflows.

The projected volume is a functional-requirement estimate, not a validated performance result.