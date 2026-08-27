---
type: query
title: What Are the Accounting-Feed Validation Retry Error Codes and Limits?
created: 2026-08-24
updated: 2026-08-24
tags: [accounting-feed, validation, retry, ebbs, cash-settlement]
related: [ebbs, ratanone, value-date-accounting-feed-cutoff, accounting-file-delivery-acknowledgement, what-is-the-authoritative-ebbs-accounting-feed-state-machine]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/Swift Generation & Settlement Accounting Tech design.md"]
---
# What Are the Accounting-Feed Validation Retry Error Codes and Limits?

The Swift generation design states that publication should “Retry max to 3 times on validate error codes.” It does not define the operational contract behind that rule.

## Questions to resolve

- Which validation error codes are eligible for retry?
- Does “max to 3 times” mean three total attempts or three retries after the initial attempt?
- Is retry synchronous, scheduled, event-driven, or manually initiated?
- What delay, backoff, and timeout rules apply?
- What terminal status is recorded after retries are exhausted?
- Is a failed feed eligible for manual replay, and how is duplicate publication prevented?

The value-date eligibility rule is documented in [[value-date-accounting-feed-cutoff]], while the missing lifecycle treatment is tracked in [[what-is-the-authoritative-ebbs-accounting-feed-state-machine]].