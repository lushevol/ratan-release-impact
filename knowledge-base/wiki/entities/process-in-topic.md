---
type: entity
title: process-in topic
created: 2026-08-24
updated: 2026-08-24
tags: [messaging, cash-settlement, event-publication, process-in]
related: [ratan-cashflow-lifecycle-service, cash-settlement-cashflow-domain-events, process-in-publication-contract, cashflow-lifecycle-state-machine-restructuring]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# process-in topic

The `process-in` topic is the downstream messaging destination referenced by the Uber development-testing notes.

The source records the following action-specific expectations or observations:

- Swift unsuppression approval for `C06810140005` did not publish to `process-in`.
- A missing publication for `N00000062629` was reported as fixed.
- `SettleAsGross` for `CH6800724464` needs to publish to `process-in`.
- Materialize for `C07810140013` has an unresolved question about whether publication is required.

These findings show that publication behavior is action-specific and is not yet captured by a single authoritative contract.