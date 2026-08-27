---
type: query
title: What Is the Bulk Processing Partial Success, Concurrency, and Retry Contract?
created: 2026-08-23
updated: 2026-08-23
tags: [cashflow, bulk-processing, partial-success, concurrency, retry]
related: [bulk-cashflow-exception-processing, cashflow-event-versioning]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Multi Exceptions/Bulk Processing for Multi Exception Demo.md"]
---
# What Is the Bulk Processing Partial Success, Concurrency, and Retry Contract?

The planned bulk-approval demo expects partial success when another user processes one selected cashflow offline. The requirement does not define the operational contract for this condition.

## Questions

- What item-level statuses, reasons, and error codes are returned for a bulk action?
- How does the system detect that another user has processed, changed, or locked an item?
- Are optimistic-version checks, locks, or idempotency keys used?
- Are successful items retained when other items fail, or is the operation atomic?
- Which items may be retried, by whom, and under what state-transition rules?
- How are stale preview selections reconciled with current cashflow state?

The source creates a concurrency requirement pressure point for [[cashflow-event-versioning]] but does not provide a versioning solution.