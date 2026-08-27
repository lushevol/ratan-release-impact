---
type: concept
title: Process-In Publication Contract
created: 2026-08-24
updated: 2026-08-24
tags: [event-driven-processing, cash-settlement, lifecycle, process-in]
related: [process-in-topic, ratan-cashflow-lifecycle-service, cashflow-lifecycle-state-machine-restructuring, materialize-process-in-publication]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Tech Design/RATANONE Cash Settlement Technical Design/RATAN - Uber Integration/Uber Development Testing/Uber Dev Testing Question.md"]
---
# Process-In Publication Contract

The process-in publication contract defines which cashflow actions publish downstream processing events, with what payload, and under which lifecycle conditions.

The Uber development-testing notes identify inconsistent or unresolved behavior:

- Swift unsuppression approval did not publish for `C06810140005`.
- A missing publication for `N00000062629` was reported fixed.
- `SettleAsGross` for `CH6800724464` is explicitly expected to publish.
- Materialize for `C07810140013` has no confirmed publication requirement.

The contract must distinguish command execution, event publication, downstream processing, and UI or Query Service projection. A successful command does not by itself demonstrate that a process-in event was published.