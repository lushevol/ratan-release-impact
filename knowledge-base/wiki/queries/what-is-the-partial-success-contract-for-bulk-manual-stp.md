---
type: query
title: What Is the Partial-Success Contract for Bulk Manual STP?
created: 2026-08-23
updated: 2026-08-23
tags: [manual-stp, bulk-processing, partial-success, idempotency, audit]
related: [bulk-manual-stp, group-blotter-bulk-stp-eligibility]
sources: ["Cash Settlement Home Page/Cash Settlement Home Page/Functional Requirement/Settlement Day2 Requirement/Group Blotter Enhancement.md"]
---
# What Is the Partial-Success Contract for Bulk Manual STP?

The requirement provides expected outcomes for all-selected cashflows being processed and for all processing failing. It does not define a contract for mixed batch results.

## Questions to Resolve

- Is bulk Manual STP atomic or best-effort?
- How are successfully processed and failed cashflows presented to the operator?
- Can a group be partially completed, and what is its resulting status?
- Are failures retryable, and what idempotency key prevents duplicate delivery?
- What audit record captures selection, authorization, confirmation, request, outcome, and `bookingSystemEvent`?
- What retry behavior is allowed after timeout or uncertain delivery outcome?

These rules are necessary to manage the duplicate-payment risk that motivates [[group-blotter-bulk-stp-eligibility]].