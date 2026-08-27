---
type: query
title: Does NetNew Automatically Publish to process_in for Uber?
created: 2026-08-24
updated: 2026-08-24
tags: [uber, netting, kafka, netnew, process-in]
related: [uber, netting-service, uber-restructured-workflow-integration, kafka-persistent-retry-and-dlt-recovery]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing.md"]
---
# Does NetNew Automatically Publish to process_in for Uber?

In the documented Uber IRS-netting test, the netting resultant `N00000003845` was expected to settle after two related cashflows were netted. The source records that the `NetNew` message needed manual publication to a Kafka topic and identifies this as a gap.

## Unknowns

- Whether publication is absent, delayed, misrouted, or consumed unsuccessfully.
- Whether the target is specifically `process_in` or another processing topic.
- Which component owns publication: [[netting-service]], [[orchestration]], or lifecycle.
- Whether the issue affects only the tested Uber scenario or other netting paths.

## Required evidence

Collect correlated input message IDs, Kafka topic and partition, offsets, timestamps, resultant cashflow ID, service logs, and final lifecycle state for a reproducible netting test.